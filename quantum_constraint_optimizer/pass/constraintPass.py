from qiskit.transpiler.basepasses import TransformationPass
from qiskit.dagcircuit import DAGCircuit
from qiskit.converters import dag_to_circuit, circuit_to_dag
from qiskit.circuit import QuantumCircuit
from qiskit.extensions.standard import *
from quantum_constraint_optimizer.datastructures import Circuit
from quantum_constraint_optimizer.datastructures import Instruction

#from qiskit.circuit.quantumregister import QuantumRegister
#from qiskit.extensions.standard import SwapGate
#from qiskit.transpiler.exceptions import TranspilerError
#from qiskit.transpiler.layout import Layout
#from qiskit.dagcircuit import DAGNode

#TODO Outdated

class ConstraintPass(TransformationPass):

    def __init__(self, ofunc, c_gs=[]):
        super().__init__()
        #self.solver = Optimize()
        #self.constraint_generators = c_gs
        #self.objective_function = ofunc

    def run(self, dag):

        circuit = dag_to_circuit(dag)
        optimizer_input = circuit.qasm()
        print(optimizer_input)

        #temp
        optimizer_output = optimizer_input

        optimized_circuit = QuantumCircuit.from_qasm_str(optimizer_output)
        dag = circuit_to_dag(optimized_circuit)
        
        #z3circuit = to_Circuit(dag)

        #for constraint_gen in self.constraint_generators:
            #better? interface: 
            #self.append(constraint_gen(z3circuit))
        #    constraint_gen(self.solver, z3circuit)

        #self.objective_function(self.solver, z3circuit)
        
       # if self.solver.check() == unsat:
       #     print("UNSAT EXCEPTION")
            #TODO raise exception
       #     return

        #dag = to_DAGCircuit(self.solver.model())

        return dag

    #def append(self, constraints):
    #    for constraint in constraints: 
    #        self.solver.add(constraint)

#standard_extension = {"u1": U1Gate,"u2": U2Gate,"u3": U3Gate,"x": XGate,"y": YGate,"z": ZGate,"t": TGate,"tdg": TdgGate,"s": SGate,"sdg": SdgGate,"swap": SwapGate,"rx": RXGate,"rxx": RXXGate,"ry": RYGate,"rz": RZGate,"rzz": RZZGate,"id": IdGate,"h": HGate,"cx": CXGate,"cy": CyGate,"cz": CzGate,"ch": CHGate,"crx": CrxGate,"cry": CryGate,"crz": CrzGate,"cu1": Cu1Gate,"cu3": Cu3Gate,"ccx": ToffoliGate,"cswap": FredkinGate}

def DAGCircuit_to_Circuit(dagcircuit):
    circuit = dag_to_circuit(dagcircuit)
    z3circuit = Circuit();
    for instruction, qargs, cargs in circuit.data:
        ins_name = instruction.name
        on_qbits = qargs
        on_cbits = cargs
        ins_condition = instruction.condition
        instruction = Instruction()
        z3circuit.append(instruction)

    return z3circuit

def Circuit_to_DAGCircuit(z3schedule, qubits):
    n = len(qubits)
    circuit = QuantumCircuit(n,n)
    for (gate, time) in z3schedule: 
        #op = standard_extension(gate.name.lower())
        opname = gate.name.lower()
        #circuit.op(*gate.targets)
        op = getattr(circuit, opname)
        if opname == 'cx':
            op(gate.control, gate.target)
        else:
            op(gate.target)

    #TODO
    res = circuit_to_dag(circuit)
    return res