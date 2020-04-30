from z3 import Optimize
from quantum_constraint_optimizer.constraint_generators.objectives import *
from quantum_constraint_optimizer.translators.qiskit_translator import model_to_QuantumCircuit, QuantumCircuit_to_Circuit, reliability_loader
from quantum_constraint_optimizer.datastructures import Qubit
from quantum_constraint_optimizer.datastructures.circuit import Circuit
from quantum_constraint_optimizer.testing.testing import correctness, improved_reliability
from qiskit import QuantumCircuit

# Initialize available qubits
qubits = [Qubit("q_"+str(i),i) for i in range(5)]
# Initialize Circuit
circ = Circuit(qubits)
# Append many gates to circuit
circ = circ.append("h", 4)
circ = circ.append("x", 4)
circ = circ.append("x", 3)
circ = circ.append("cx", [1,3])
circ = circ.append("swap", [3, 4])
circ = circ.append("measure", 0)
circ = circ.append("measure", 1)
circ = circ.append("measure", 2)
circ = circ.append("measure", 3)
circ = circ.append("measure", 4)
# Collect constraints generated by circuit
cons = list(circ.constraints())
# Create a new Optimizer
s = Optimize()
# Add all the constraints to the optimizer
for con in cons:
    #print(con)
    s.add(con)

# Add a reliability objective
s.minimize(time_objective(circ))
# Check and print the model
print(s.check())
m = s.model()
#print({o:m.evaluate(o) for o in s.objectives()})

# Translate the model back into a qiskit QuantumCircuit
qcirc = model_to_QuantumCircuit(m, circ)
print(qcirc)
# Translate the QuantumCircuit back again into a Z3 Circuit
zcirc = QuantumCircuit_to_Circuit(qcirc)


def opt(circ):
    from qiskit.compiler import transpile

    coupling_map = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 6],
                    [14,13], [13,12], [12,11], [11,10], [10,9], [9,8], [8,7],
                    [0,14],[1,13],[12,2],[11,3],[10,4],[9,5],[8,6]]

    return transpile(circ,
                basis_gates=['u1', 'u2', 'u3', 'cx', 'id'],
                coupling_map=coupling_map, optimization_level=3)

# Collect reliabilities from an IBM Quantum Experience daily calibration
fname = "ibmq_16_melbourne.csv"
melbourne_rels = reliability_loader(fname)
# Intitialize available qubits with those reliabilities
qubits = [Qubit("q_"+str(qid), qid, melbourne_rels[qid]) for qid in melbourne_rels]
# Initialize Circuit
circ = Circuit(qubits)
precirc = QuantumCircuit(len(qubits), len(qubits))
# Add gates to the circuit
circ = circ.append("u2", 9, [3.1415,0])
precirc.u2(3.1415, 0, 9)
circ = circ.append("u2", 9, [3.1415,0])
precirc.u2(3.1415, 0, 9)
circ = circ.append("cx", [9,12])
precirc.cx(12,9)
circ = circ.append("u2", 13, [3.1415,0])
precirc.u2(3.1415, 0, 13)
circ = circ.append("u2", 10, [3.1415,0])
precirc.u2(3.1415, 0, 10)
circ = circ.append("measure", 10)
precirc.measure(10,10)
circ = circ.append("measure", 13)
precirc.measure(13,13)
circ = circ.append("measure", 9)
precirc.measure(9,9)
circ = circ.append("measure", 12)
precirc.measure(12,12)
circ = circ.append("measure", 11)
precirc.measure(11,11)
#circ = QuantumCircuit_to_Circuit(precirc)
# Collect Constraints
cons = circ.constraints()
# New Optimizer
s = Optimize()
# Add constraints
for con in cons:
    s.add(con)
# Add reliability objective
s.maximize(reliability_objective(circ))
# Check and print
print(s.check())
m = s.model()
#TODO There is something wrong with attaching the reliability to the instruction. Check on: 
# - Reliability table
# - Calls of reliability()
# - Reliability attachment constraint

# Translate to qiskit QuantumCircuit
qcirc = model_to_QuantumCircuit(m, circ)
print(qcirc)
improved_reliability(m,s,melbourne_rels, qcirc)
print(precirc)
improved_reliability(m,s,melbourne_rels, precirc)
print(opt(precirc))
improved_reliability(m,s,melbourne_rels, opt(precirc))
print(opt(qcirc))
improved_reliability(m,s,melbourne_rels, opt(qcirc))
#correctness(precirc, qcirc)