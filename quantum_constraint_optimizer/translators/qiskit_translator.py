from z3 import ModelRef
from qiskit import QuantumCircuit
from quantum_constraint_optimizer.datastructures.circuit import Circuit
from quantum_constraint_optimizer.datastructures import Qubit
from collections import defaultdict
from typing import Dict, Tuple
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
    num_qubits = max(circuit.qubit_indices)+1
    for iid, timeslot in times.items():
        moments[timeslot].add((iid, on_indices[iid]))
    
    # Create a new QuantumCircuit and append new instructions into it, by moment order
    qcircuit = QuantumCircuit(num_qubits, num_qubits)
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

def QuantumCircuit_to_Circuit(qiskit_circuit:QuantumCircuit, reliabilities:Dict[int,Dict[str,float]], position_map:Dict[int, Tuple[int, int]]=None) -> Circuit:
    # Create a new Circuit with new Qubits which match the QuantumCircuit's indexes
    if position_map:
        circuit = Circuit([Qubit("q_"+str(index), index, position_map[index][0], position_map[index][1], reliabilities[index]) for index in reliabilities.keys()])
    else:
        circuit = Circuit([Qubit("q_"+str(index), index, index, index, reliabilities[index]) for index in reliabilities.keys()])

    # Append new instructions into the Circuit for each instruction in the QuantumCircuit
    for gate, qubits, cubits in qiskit_circuit: 
        qubit_indices = list(map(lambda x:x.index, reversed(qubits)))
        circuit = circuit.append(gate.name, qubit_indices, gate._params)

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
            reliabilities["measure"+str(qindex)] = 1-float(measure_err)
            reliabilities["id"+str(qindex)] = 1
            reliabilities["u1"+str(qindex)] = 1
            reliabilities["u2"+str(qindex)] = 1-float(u2_err)
            reliabilities["u3"+str(qindex)] = (1-float(u2_err))**2
            for pair in cx_errs.split(", "):
                opid, reliability = pair.split(":")
                reliability = 1-float(reliability)
                reliabilities[opid] = reliability
            all_reliabilities[qindex] = reliabilities

    # Return reliability data map for each qubit index
    return all_reliabilities
            
