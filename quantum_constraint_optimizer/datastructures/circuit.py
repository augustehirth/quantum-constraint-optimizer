from __future__ import annotations
from z3 import *
from typing import List
from quantum_constraint_optimizer.datastructures import Instruction, Qubit
from quantum_constraint_optimizer.datastructures.gates import HGate, RGate, XGate, YGate, ZGate, U1Gate, U2Gate, U3Gate, CXGate, SwapGate, InGate, OutGate, MeasureGate
from copy import copy
from collections.abc import Iterable
from itertools import combinations

class Circuit:
    # our gate names, goal is to be above plus in, out, measure
    gate_names = {"h":HGate, "r":RGate, "x":XGate, "y":YGate, "z":ZGate, "u1":U1Gate, "u2":U2Gate, "u3":U3Gate, "cx":CXGate, "swap":SwapGate, "in":InGate, "out":OutGate, "measure":MeasureGate}

    def __init__(self, qubits:List[Qubit]):

        # Store available qubits
        self.qubits: List[Qubit] = qubits

        # Store qubit indices
        self.qubit_indices: List[int] = [q.index for q in self.qubits]

        # Store index->qubit mapping
        self.qubit_map: Dict[int, Qubit] = dict(zip(self.qubit_indices, self.qubits))

        # Initialize set of instructions
        self.instructions: Dict[str,Instruction] = {}

        # Initialize instruction counter
        self.instctr : int = 0

        # Initialize map of In instructions to represent the inputs to the circuit
        self.input_instructions : Dict[int, Instruction]= {}
        for ind in self.qubit_indices:
            self.input_instructions[ind], self.instctr = next(InGate.on(prev = {ind:None}, qubit_map = self.qubit_map, instctr = self.instctr))
            #self.instctr = instctr

        # Initialize frontier of instructions furthest along the dependency chain for each qubit
        self.frontier = self.input_instructions.copy()

        # Initialize map of Out instructions to represent the outputs of the circuit
        self.output_instructions : Dict[int, Instruction]= {}
        for ind, in_ins in self.input_instructions.items():
            self.output_instructions[ind], self.instctr = next(OutGate.on(prev = {ind:in_ins}, qubit_map = self.qubit_map, instctr = self.instctr))
            #self.instctr = instctr

    def append(self, gate_name:str, on_indices:List[int], other_args:List=[]) -> Circuit:
    
        # Hack to allow simpler append statements
        if not isinstance(on_indices, Iterable):
            on_indices = [on_indices]

        # Make sure all requested qubit indices are available
        for index in on_indices: 
            if index not in self.qubit_indices:
                raise IndexError("Unavailable qubit index: " + str(index))

        # Prepare a new circuit to return 
        ret = copy(self)

        # Get the gate class from the qubit's name
        gate = Circuit.gate_names.get(gate_name)

        if gate is None: 
            if gate_name is "barrier": return ret
            if gate_name is "id": return ret
            raise Exception("Unsupported Gate: " + gate_name)

        # Get the most recently added instruction on each of those qubits
        prev = {index:ret.frontier.get(index) for index in on_indices}

        last_instruction = None
        # Generate a new instruction (or multitude of instructions)
        for new_instruction, instctr in gate.on(prev = prev, qubit_map = self.qubit_map, instctr = ret.instctr, other_args=other_args):
            # Actually add the instruction to the circuit
            ret = ret.append_instruction(new_instruction)
            # Update the instruction counter
            ret.instctr = instctr
            # Record the last instruction produced
            last_instruction = new_instruction

        # Update the frontier to note the most recently appended instruction
        if last_instruction: 
            for index in on_indices:
                ret.frontier[index] = last_instruction

        # Update the output instructions to point to the most recently appended instruction
        if last_instruction: 
            for index in on_indices:
                lastoutinst = ret.output_instructions.get(index)
                if lastoutinst:
                    # Make a new one with updated prev and the same identifying number
                    outinst, _ = next(OutGate.on(prev= {index:last_instruction}, qubit_map= ret.qubit_map, instctr=lastoutinst.id))
                else: 
                    # Else, Make a new one with updated prev. Update the instctr
                    outinst, ret.instctr = next(OutGate.on(prev= {index:last_instruction}, qubit_map= ret.qubit_map, instctr=ret.instctr))

                # Add the new output instruction to refer to the target qubit
                ret.output_instructions[index] = outinst

        return ret

    def append_instruction(self, instruction:Instruction) -> Circuit:
        # Prepare a new circuit to return
        ret = copy(self)

        # Add the new instruction to the instruction set
        ret.instructions[instruction.name] = instruction

        return ret

    def append_many(self, instructions:Iterable[Instruction]) -> Circuit:
        # Prepare a new circuit to return
        ret = copy(self)

        # Simply append each instruction to the new circuit
        for instruction in instructions: 
            ret = ret.append_instruction(instruction)
        return ret

    def constraints(self) -> Iterable[AstRef]:

        for inst in self.input_instructions.values():
            # Assert input instruction constraints
            yield from inst.constraints()

             # Assert that all input instructions are on different qubits. 
            for otherinst in self.input_instructions.values():
                if inst is not otherinst: 
                    yield next(iter(inst.on_indices.values())) != next(iter(otherinst.on_indices.values()))
                       
        for inst in self.output_instructions.values():
            # Assert output instruction constraints
            yield from inst.constraints()

        for inst in self.instructions.values():
            # Assert the instruction's circuit-independent constraints
            yield from inst.constraints()
        
        # Assert circuit specific constraints
        def time_overlap(cx1, cx2):
            return cx1.time == cx2.time 

        def space_overlap(qid1, qid2, qid3, qid4):
            c1, t1 = self.qubit_map[qid1], self.qubit_map[qid2]
            r1cols = set(range(abs(c1.col - t1.col)+1))
            r1rows = set(range(abs(c1.row - t1.row)+1))
            c2, t2 = self.qubit_map[qid3], self.qubit_map[qid4]
            r2cols = set(range(abs(c2.col - t2.col)+1))
            r2rows = set(range(abs(c2.row - t2.row)+1))
            return bool(r1cols.intersection(r2cols)) and bool(r1rows.intersection(r2rows))

        print("Yielding overlap constraints")
        for cx1, cx2 in combinations(filter(lambda x:x.gate.name == "cx", self.instructions.values()), 2):
            for qid1, qid2, qid3, qid4 in combinations(self.qubit_indices, 4):
                c1,t1 = cx1.on_indices.values()
                c2,t2 = cx2.on_indices.values()
                yield Implies(And(c1 == qid1, t1 == qid2, c2 == qid3, t2 == qid4), \
                    Or(Not(time_overlap(cx1, cx2)), Not(space_overlap(qid1, qid2, qid3, qid4))))
            
    def __repr__(self):
        return str(self)

    def __str__(self):
        return str([(instruction, instruction.prev) for instruction in self.instructions.values()])