from z3 import ModelRef
from qiskit import QuantumCircuit
from quantum_constraint_optimizer.datastructures.circuit import Circuit
from quantum_constraint_optimizer.datastructures import Qubit
from collections import defaultdict
from csv import reader

# Turn z3 model back into a qiskit QuantumCircuit
def model_to_QuantumCircuit(model:ModelRef, circuit:Circuit) -> QuantumCircuit:

    # Sort timing and qubit variables into separate dicts
    times = {}
    on_indices = {}
    for inst in circuit.instructions.values():
        times[inst.name] = model[inst.time].as_long()
        on_indices[inst.name] = tuple(model[on_index].as_long() for on_index in inst.on_indices.values())

    # Bucket instructions into moments, where all instructions in a moment are run in parallel, on different qubits
    moments = defaultdict(set)
    max_qind = 0
    for iid, timeslot in times.items():
        moments[timeslot].add((iid, on_indices[iid]))
        max_qind = max(max_qind, *on_indices[iid])
    
    # Create a new QuantumCircuit and append new instructions into it, by moment order
    qcircuit = QuantumCircuit(max_qind+1, max_qind+1)
    for timeslot in sorted(moments):
        moment = moments[timeslot]
        for iid, qubit_indices in moment:
            iname, inum = iid.split("_")
            if iname in ["in", "out"]: continue
            if iname == "measure":
                qcircuit.measure(*qubit_indices, *qubit_indices)
                continue
            other_arguments = circuit.instructions[iid].other_args
            getattr(qcircuit, iname)(*other_arguments, *reversed(qubit_indices))

    # Return the new QuantumCircuit
    return qcircuit

def QuantumCircuit_to_Circuit(qiskit_circuit:QuantumCircuit) -> Circuit:
    # Create a new Circuit with new Qubits which match the QuantumCircuit's indexes
    circuit = Circuit([Qubit("q_"+str(index), index) for index in map(lambda x:x.index, qiskit_circuit.qubits)])

    # Append new instructions into the Circuit for each instruction in the QuantumCircuit
    for gate, qubits, cubits in qiskit_circuit: 
        qubit_indices = list(map(lambda x:x.index, reversed(qubits)))
        circuit = circuit.append(gate.name, qubit_indices)

    # Return the new Circuit
    return circuit

def reliability_loader(filename:str):
    # Open and read the IBM Quantum Experience CSV format
    all_reliabilities = {}
    with open(filename, "r") as f:
        csv = reader(f, delimiter=",", quotechar="\"")
        # Consume the header line
        next(csv)

        # Collect qubit index, measurement error, u2 gate errow, and cx gate errors (for each pairing with another qubit)
        for line in csv:
            qid, t1, t2, freq, measure_err, u2_err, cx_errs, date = line
            qindex = int(qid[1:])
            reliabilities = defaultdict(float)
            reliabilities["measure"+str(qindex)] = float(measure_err)
            reliabilities["u2"+str(qindex)] = float(u2_err)
            for pair in cx_errs.split(","):
                opid, reliability = pair.split(":")
                reliability = float(reliability)
                reliabilities[opid] = reliability
            all_reliabilities[qindex] = reliabilities

    # Return reliability data map for each qubit index
    return all_reliabilities
            
