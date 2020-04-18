from __future__ import annotations
from functools import reduce
from z3 import OptimizeObjective, If
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from quantum_constraint_optimizer.datastructures.circuit import Circuit

# Reliability objective is the product of every instruction's reliabilities
def reliability_objective(circuit: Circuit) -> OptimizeObjective:
    total_reliability = reduce(lambda acc, x: x * acc, map(lambda x:x.reliability, circuit.instructions.values()))
    return total_reliability

# Currently very incorrect. Size objective minimizes the number of two qubit gates. Dependent on ability to substitute instructions
def size_objective(circuit: Circuit) -> OptimizeObjective: 
    num_2q_instructions = sum(map(lambda ins: 1 if len(ins.prev)>= 2 else 0, circuit.instructions.values()), 0)
    return num_2q_instructions

# Time objective is the largest time out of all the instructions; the last one. 
def time_objective(circuit: Circuit) -> OptimizeObjective:
    last_gate_time = reduce(lambda acc,x: If(x > acc, x, acc), map(lambda x:x.time, circuit.instructions.values()))
    return last_gate_time
