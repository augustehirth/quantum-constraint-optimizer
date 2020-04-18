from quantum_constraint_optimizer.datastructures.gates.onequbitgate import OneQubitGate

class OutGate(OneQubitGate):
    # Effect-less instruction factory used to denote end of a circuit
    name = "out"