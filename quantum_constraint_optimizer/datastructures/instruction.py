from __future__ import annotations
from z3 import Union, BoolRef, Real, Int, AstRef, Implies, And, Or, Not
from functools import reduce
from itertools import product, starmap, combinations
from typing import List, TYPE_CHECKING
from collections import OrderedDict
if TYPE_CHECKING:
    from quantum_constraint_optimizer.datastructures.gate import Gate, Qubit

class Instruction:
    def __init__(self, id:int, gate:Gate, prev:OrderedDict[int,Instruction], qubit_map:Dict[int, Qubit], other_args:List=[]):

        # The instructions numerical identifier
        self.id : int = id

        # The gate of the instruction
        self.gate : Gate = gate

        # A name for the instruction
        self.name : str = str(self.gate.name) + "_" + str(self.id)

        # Previous instructions in the dependency graph: those instrs that this one depends on
        self.prev : OrderedDict[int,Instruction] = prev

        # Available Qubits, mapped from their indices
        self.qubit_map: Dict[int, Qubit] = qubit_map

        # Qubit indicies applied to:
        # This is intuitively the primary mapping from "logical" indices to real ones. 
        # The consistency over the entire graph is maintained by the constraints.
        self.on_indices: OrderedDict[int, Int] = OrderedDict([(edge,Int(self.name+".edge_"+str(edge))) for edge in prev.keys()])

        # Time slot to run this instruction in
        self.time: Int = Int(self.name + ".timeslot")

        # Reliability of this instruction: depends on the operation and which qubit it's assigned to
        self.reliability: Real = Real(self.name + ".reliability")

        # Other args like rotations: TODO
        self.other_args: List = other_args
    
    def __str__(self):
        return str(self.name)

    def __repr__(self): return str(self)

    # Get constraints for this object:
    #   The two free variables are Time and Qubit. Reliability is bound by choice of Qubit.
    def constraints(self) -> Iterable[AstRef]: 

        # Assert that the instruction's time is greater than zero (the input instructions), for sanity
        yield self.time > 0

        # Assert that reliability is nonnegative for "real" operations
        if self.gate.name not in {"in", "out"}:
            yield self.reliability > 0

        # Assert that all assigned indices are actually available qubits
        for on_index in self.on_indices.values():
            yield Or(*map(lambda qubit_ind:on_index == qubit_ind, self.qubit_map.keys()))

        # Assert that if the instruction only depends on one None type, it is an In instruction
        if len(self.prev) == 1 and next(iter(self.prev.values())) == None: return self.gate.name == "in"

        # Assert that this instruction's time must be greater than it's previous instructions
        for previnst in self.prev.values():
            yield previnst.time < self.time

        # Assert that, for each edge from a previous instruction, that instruction's out edge is assigned to the same qubit index
        for prevind, previnst in self.prev.items():
            yield previnst.on_indices[prevind] == self.on_indices[prevind]

        # Assert that the reliability of this instruction is based on the qubit indices assigned. 
        for tupl in product(self.qubit_map.items(), repeat=len(self.prev)):
            inds, qubits = zip(*tupl)
            # Condition: If the on_indices are in this exact configuration
            match = starmap(lambda on_index, qubit_index:on_index == qubit_index, zip(self.on_indices.values(), inds))
            yield Implies(And(*match), \
                # Result: Then the reliability will be equal to the reliability of that gate on those qubits
                self.reliability == qubits[0].reliability(self.gate, qubits[1:])
                )

        # Assert that the qubit indices that this instruction is applied to are different
        for onind1, onind2 in combinations(self.on_indices.values(), 2):
            yield Not(onind1 == onind2)

        # Assert that no non-Out instruction follows a measure
        if self.gate.name != "out": 
            for prevind, previnst in self.prev.items():
                yield previnst.gate.name != "measure"