from __future__ import annotations
from z3 import Real
from typing import Set, DefaultDict, Tuple, List
from quantum_constraint_optimizer.datastructures.gate import Gate
from itertools import chain
from functools import reduce
from collections import defaultdict

class Qubit:
    def __init__(self, name:str, index:int, reliabilities: DefaultDict[str,float], **kwargs):
        #super().__init__()

        # A name for the qubit
        self.name : str  = name

        # The qubit's numerical index
        self.index : int = index 

        # The qubit's column index
        self.col : int = kwargs['col']

        # The qubit's row index
        self.row : int = kwargs['row']

        # Reliability data for each gate on this qubit
        #   map from supported_gates -> Real
        self.reliabilities : DefaultDict[Tuple[Gate, Tuple[Qubit]], Real] = reliabilities or defaultdict(float)

        # Gates supported by this qubit
        self.supported_gates : Set[Gate] = self.reliabilities.keys() 

    # Reliability of an  gate operation on this qubit, optionally with respect to another control qubit
    def reliability(self, gate: Gate, controls: Iterable[Qubit] = ()) -> float:
        key = (gate.name, tuple(map(lambda x:x.index,controls)))
        key = gate.name + str(self.index)
        for control in controls:
            key += "_" + str(control.index)
        return self.reliabilities.get(key, 0)
    
    def __repr__(self): return str(self)

    def __str__(self): return str(self.name) + "_" + str(self.index)
