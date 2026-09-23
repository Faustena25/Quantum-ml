from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Put first qubit in superposition
qc.h(0)

# Entangle both qubits
qc.cx(0, 1)

# Draw the circuit
print("✅ Quantum Circuit:")
print(qc.draw())

# Simulate the quantum state
state = Statevector(qc)
print("\n✅ Quantum State Probabilities:")
print(state.probabilities_dict())