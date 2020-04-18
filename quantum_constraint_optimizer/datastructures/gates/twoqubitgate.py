from typing import List, Iterable, Tuple, TYPE_CHECKING, Dict
from quantum_constraint_optimizer.datastructures import Gate, Instruction, Qubit

class TwoQubitGate(Gate):
    # Superclass of all two qubit instructions

    # Check for two qubit gates: 
    # 1. That the instruction has the correct number of dependencies
    @staticmethod
    def checks(ins:Instruction) -> bool:
        yield len(ins.prev) == 2

    # Return instruction if it passes the checks for one qubit gates
    @classmethod
    def on(cls, prev:List[Instruction], qubit_map:Dict[int, Qubit], instctr:int, other_args:List=[]) -> Iterable[Tuple[Instruction, int]]:
        ret, instctr = next(super().on(prev, qubit_map, instctr, other_args))
        yield (ret, instctr) if all(cls.checks(ret)) else (False, instctr)
    