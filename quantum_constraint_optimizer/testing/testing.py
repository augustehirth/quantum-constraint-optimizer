import cirq
from pyquil import Program
from pyquil.api import WavefunctionSimulator, QuantumComputer, local_forest_runtime
# #execution time
import time

# OUT OF DATE, KEPT TEMPORARILY

#Calculate reliabilities for CirqCircuit and optimized schedule CirqCircuit
def correctness(pre_circuit: cirq.Circuit, post_circuit: cirq.Circuit):
    print("Testing: Correctness:")
    sim = cirq.Simulator()
    pre_result = sim.simulate(pre_circuit)

    sim = cirq.Simulator()
    post_result = sim.simulate(post_circuit)

    print("Pre-Circuit Waveform ", pre_result.dirac_notation())
    print("Post-Circuit Waveform ", post_result.dirac_notation())
    assert pre_result.dirac_notation() == post_result.dirac_notation()


#Compare prior Z3Circuit reliability with post Z3-produced model's reliability.
def improved_reliability(m, s, E, pre_circuit):
    post_reliability = [m.evaluate(o).as_decimal(10) for o in s.objectives()]
    post_reliability = float(post_reliability[0][:-1])
    pre_reliability = calculate_z3_circuit_reliability(E, pre_circuit)
    print("Pre Log-Reliability:\n" + str(pre_reliability))
    print("Post Log-Reliability:\n" + str(post_reliability))
    assert post_reliability <= pre_reliability


#Run a pyquil program on the wavefunction simulator and return waveform
def run_pyquil_test(p:Program, qc:QuantumComputer=False):
    wf = WavefunctionSimulator()
    with local_forest_runtime():
        dirac = wf.wavefunction(p)
        if qc:
            code = qc.compile(p)
            result = qc.run(code)
            return dirac,result
    return dirac

def run_dirac(p: Program):
    wf = WavefunctionSimulator()
    with local_forest_runtime():
        dirac = wf.wavefunction(p)
    return dirac


# print("--- %s seconds ---" % (time.time() - start_time))
def run_pyquil(p: Program, qc:QuantumComputer, rig_opt):
    # print(rig_opt)
    # code = qc.compile(p, True, True)   # RUN RIGETTI OPT ALWAYS
    code = qc.compile(p, rig_opt, rig_opt)  # RUN RIGETTI OPT WHEN NO Z3 OPT

    # print(code)
    start_time = time.time()
    result = qc.run(code)
    diff = time.time() - start_time
    # print(diff)
    return result, diff

#Calculate log-reliability from a Z3Circuit
def calculate_z3_circuit_reliability(E, circuit):
    Er,Ec = E
    reliability = 0
    for gate in circuit.gates:
        if gate.name == "CX":
            reliability += Ec[(gate.target, gate.control, gate.junction)]
        if gate.name == "M":
            reliability += Er[(gate.target)]
    return reliability
