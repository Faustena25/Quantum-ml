from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib
matplotlib.use('Agg')  # No display window needed
import matplotlib.pyplot as plt


qc = QuantumCircuit(1, 1)
qc.h(0)
qc.x(0)
qc.measure(0, 0)

print("=== 1-Qubit Circuit ===")
print(qc.draw())


simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

print("\n1-Qubit Counts:", counts)

plot_histogram(counts)
plt.savefig('histogram_1qubit.png')
print("Saved: histogram_1qubit.png")
plt.close()

# ─── Deutsch-Jozsa ─────────────────────────────
n = 2
dj = QuantumCircuit(n + 1, n)

dj.x(n)
for qubit in range(n + 1):
    dj.h(qubit)

dj.barrier()
dj.cx(0, n)
dj.cx(1, n)
dj.barrier()

for qubit in range(n):
    dj.h(qubit)

for qubit in range(n):
    dj.measure(qubit, qubit)

print("\n=== Deutsch-Jozsa Circuit ===")
print(dj.draw())

# Simulate DJ
result2 = simulator.run(dj, shots=1024).result()
counts2 = result2.get_counts()

print("\nDeutsch-Jozsa Counts:", counts2)

plot_histogram(counts2)
plt.savefig('histogram_dj.png')
print("Saved: histogram_dj.png")
plt.close()