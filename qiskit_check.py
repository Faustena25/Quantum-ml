from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Build a simple circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# Run on simulator
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

print("✅ Qiskit is working!")
print("✅ Measurement results from 1000 shots:")
print(counts)