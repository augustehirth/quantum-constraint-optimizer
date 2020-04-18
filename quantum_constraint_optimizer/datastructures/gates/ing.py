from z3 import *
from quantum_constraint_optimizer.datastructures.gates.onequbitgate import OneQubitGate
from quantum_constraint_optimizer.datastructures import Instruction

class InGate(OneQubitGate):
    # Effect-less instruction factory used to denote beginning of a circuit
    name = "in"

    # Check for InGates:
    # 1. That the instruction has the correct number of dependencies (0)
    @staticmethod
    def checks(ins:Instruction):
        yield len(ins.prev) == 1
    
