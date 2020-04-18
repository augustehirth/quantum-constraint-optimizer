from __future__ import annotations
from typing import Tuple, List, Iterable, TYPE_CHECKING, Dict
from z3 import Real
from quantum_constraint_optimizer.datastructures.instruction import Instruction
if TYPE_CHECKING:
    from quantum_constraint_optimizer.datastructures import Qubit


class Gate:
    # Superclass for all gates
    name : str = "ABSTRACT GATE TYPE"

    # Create an instruction for this gate, with given dependencies, for a set of available qubits
    @classmethod
    def on(cls, prev:List[Instruction], qubit_map:Dict[int, Qubit], instctr:int, other_args:List=[]) -> Iterable[Tuple[Instruction, int]]:
        yield Instruction(id=instctr, gate = cls, prev = prev, qubit_map = qubit_map, other_args=other_args), instctr + 1