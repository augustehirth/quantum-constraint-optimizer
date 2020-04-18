from z3 import Real
from quantum_constraint_optimizer.datastructures.gates.onequbitgate import OneQubitGate
from quantum_constraint_optimizer.datastructures import Instruction, Qubit
from typing import List, Tuple, Iterable, Dict

class RGate(OneQubitGate):
    # Rotation instruction factory
    name = "r"

    # Add the given angle to the instruction
    # Return instruction if it passes the checks for RGates
    @classmethod
    def on(cls, prev:List[Instruction], qubit_map:Dict[int, Qubit], angle:Real, instctr:int, other_args:List=[]) -> Iterable[Tuple[Instruction, int]]:
        ret, instctr = next(super().on(prev, qubit_map, instctr, []))
        yield (ret, instctr) if all(ret.checks(ret)) else (False, instctr)