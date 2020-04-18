from z3 import Real
from quantum_constraint_optimizer.datastructures.gates.onequbitgate import OneQubitGate
from quantum_constraint_optimizer.datastructures import Instruction, Qubit
from typing import List, Tuple, Iterable, Dict

class U2Gate(OneQubitGate):
    # U2 gate factory
    name = "u2"

    # Add the given angles to the instruction
    # Return instruction if it passes the checks for RGates
    @classmethod
    def on(cls, prev:List[Instruction], qubit_map:Dict[int, Qubit], instctr:int, other_args:List=[]) -> Iterable[Tuple[Instruction,int]]:
        ret, instctr = next(super().on(prev, qubit_map, instctr, other_args))
        yield (ret, instctr) if all(cls.checks(ret)) else (False, instctr)