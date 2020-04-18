from quantum_constraint_optimizer.datastructures.gates.onequbitgate import OneQubitGate
from typing import List, Iterable, Tuple
from quantum_constraint_optimizer.datastructures import Qubit, Instruction

class MeasureGate(OneQubitGate):
    # Measure instruction factory
    name = "measure"