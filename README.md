# quantum_constraint_optimizer

Quantum Constraint Optimizer
A framework for representing quantum circuits in terms of variables in the Z3 solver. 
 - Handles conversion from Qiskit QuantumCircuits into an internal Circuit object, and conversion from the produced Z3 model back into Qiskit QuantumCircuits
 - The Circuit object has simple constraint generation built in, in order to preserve the legitimacy of the produced circuit. 
 - Includes some simple objective functions, in order to optimize some feature of the circuit

Currently, the available constraints allow for instructions to be assigned a timeslot and a qubit index, within the bounds of the circuit, and attempt to optimize for the overall reliability of the circuit, based on input calibration data

The framework is intended to be understandable and extensible. Adding features to classes, constraints to the solver, or new gate operations are examples of things that should be easy to implement. 

#TODO: 
 - Rigorous empirical testing
 - Support for subcircuit substitution (Necessary for routing in an arbitrary DAG?)
 - Support for symbolic parameterized gates (Requires subcircuit substitution, necessary to enable some valuable substitution optimizations)
 - More comprehensive reliability data usage (Decay times, crosstalk data, etc)

