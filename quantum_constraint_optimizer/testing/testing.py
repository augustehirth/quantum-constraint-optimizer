# #execution time
from qiskit import Aer, execute, QuantumCircuit
import time
from numpy import array_equal

# OUT OF DATE, KEPT TEMPORARILY

#Calculate reliabilities for CirqCircuit and optimized schedule CirqCircuit
def correctness(pre_circuit: QuantumCircuit, post_circuit: QuantumCircuit):
    sim = Aer.get_backend("statevector_simulator")
    print("Testing: Correctness:")
    pre_result = execute(pre_circuit, sim).result().get_statevector()

    post_result = execute(post_circuit, sim).result().get_statevector()

    print("Pre-Circuit Waveform ", pre_result)
    print("Post-Circuit Waveform ", post_result)
    assert array_equal(pre_result, post_result)

#Compare prior Z3Circuit reliability with post Z3-produced model's reliability.
def improved_reliability(m, s, qubit_reliabilities, pre_circuit):
    post_reliability = [m.evaluate(o).as_decimal(10) for o in s.objectives()]
    post_reliability = post_reliability[0]
    post_reliability = post_reliability[:-1] if post_reliability.endswith("?") else post_reliability
    post_reliability = round(-float(post_reliability), 10)
    pre_reliability = calculate_z3_circuit_reliability(qubit_reliabilities, pre_circuit)
    print("Pre Reliability:\n" + str(pre_reliability))
    print("Post Reliability:\n" + str(post_reliability))
    assert post_reliability >= pre_reliability

#Calculate log-reliability from a QuantumCircuit
def calculate_z3_circuit_reliability(qubit_reliabilities, circuit):
    reliability = 1
    for inst in circuit:
        gate, qubits, cubits = inst
        qubits = reversed(qubits)
        target = next(qubits).index
        controls = map(lambda x:x.index, qubits)
        reliabilities = qubit_reliabilities[target]
        key = gate.name+str(target)
        for control in controls:
            key += "_"+str(control)
        reliability *= reliabilities[key]
    return round(reliability, 10)
