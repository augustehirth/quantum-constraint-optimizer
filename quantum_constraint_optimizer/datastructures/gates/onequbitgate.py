from __future__ import annotations
from typing import List, Iterable, Tuple, TYPE_CHECKING, Dict
from quantum_constraint_optimizer.datastructures.gate import Gate
if TYPE_CHECKING:
    from quantum_constraint_optimizer.datastructures import Instruction, Qubit

class OneQubitGate(Gate):
    # Superclass of all one qubit instructions

    # Check for one qubit gates:
    # 1. That the instruction has the correct number of dependencies (1)
    @classmethod
    def checks(cls, ins:Instruction) -> bool:
        yield len(ins.prev) == 1

    # Return instruction if it passes the checks for one qubit gates 
    @classmethod
    def on(cls, prev:List[Instruction], qubit_map:Dict[int, Qubit], instctr:int, other_args:List=[]) -> Iterable[Tuple[Instruction, int]]:
        ret, instctr = next(super().on(prev, qubit_map, instctr, other_args))#, target, []))
        yield (ret, instctr) if all(cls.checks(ret)) else (False, instctr)