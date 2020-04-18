from z3 import Real
from quantum_constraint_optimizer.datastructures.gates.twoqubitgate import TwoQubitGate

class CXGate(TwoQubitGate):
    # CX instruction factory
    name = "cx"