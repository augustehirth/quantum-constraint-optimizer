from z3 import Real
from quantum_constraint_optimizer.datastructures.gates import CXGate
from quantum_constraint_optimizer.datastructures.gates.twoqubitgate import TwoQubitGate
from quantum_constraint_optimizer.datastructures import Instruction, Qubit
from typing import List, Iterable, Tuple, Dict
from collections import OrderedDict

class SwapGate(TwoQubitGate):
    # Swap instruction factory
    #   implemented as three cnots
    name = "swap"

    # Return three CXGate instructions applied alternatingly to qubits the Swap was applied to 
    @classmethod
    def on(cls, prev:List[Instruction], qubit_map:Dict[int, Qubit], instctr:int, other_args:List=[]) -> Iterable[Tuple[Instruction, int]]:
        ind1, ind2 = prev.keys()
        fst, instctr = next(CXGate.on(prev, qubit_map, instctr))
        yield fst, instctr
        snd, instctr = next(CXGate.on(OrderedDict([(ind2, fst), (ind1, fst)]), qubit_map, instctr))
        yield snd, instctr
        thd, instctr = next(CXGate.on(OrderedDict([(ind1, snd), (ind2, snd)]), qubit_map, instctr))
        yield thd, instctr


