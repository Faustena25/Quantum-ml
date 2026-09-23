

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
from bloch_sphere.animate_bloch import draw_bloch_sphere
from hyperbolic import euclid3d
import drawsvg as d
import numpy as np

def save_bloch(filename, label, inner_proj=None):
    drawing = d.Drawing(300, 300, origin='center')
    g = d.Group(transform='scale(120)')
    if inner_proj is not None:
        draw_bloch_sphere(g, inner_proj=inner_proj, label=label)
    else:
        draw_bloch_sphere(g, label=label)
    drawing.append(g)
    drawing.save_svg(filename)
    print(f'  Saved {filename}')

def print_state(label, sv):
    print(f'\n  State after {label}:')
    print(f'    Statevector : {np.round(sv.data, 3)}')
    probs = sv.probabilities()
    print(f'    P(|0>) = {probs[0]:.4f}')
    print(f'    P(|1>) = {probs[1]:.4f}')


print('\n========== PART 1: Initial State |0> ==========')
sv = Statevector.from_label('0')
print_state('initialization', sv)
save_bloch('bloch_1_init.svg', '|0>')



print('\n========== PART 2: X Gate ==========')
qc = QuantumCircuit(1)
qc.x(0)
sv = Statevector.from_label('0').evolve(qc)
print_state('X gate', sv)
rot = euclid3d.rotation(3, 0, 2, np.pi)
save_bloch('bloch_2_X.svg', 'X|0>=|1>', inner_proj=rot)
print(f'  Circuit:\n{qc.draw()}')



print('\n========== PART 3: H Gate ==========')
qc = QuantumCircuit(1)
qc.h(0)
sv = Statevector.from_label('0').evolve(qc)
print_state('H gate', sv)
rot = euclid3d.rotation(3, 0, 1, np.pi/2)
save_bloch('bloch_3_H.svg', 'H|0>=|+>', inner_proj=rot)
print(f'  Circuit:\n{qc.draw()}')



print('\n========== PART 4: Z Gate ==========')
qc = QuantumCircuit(1)
qc.z(0)
sv = Statevector.from_label('0').evolve(qc)
print_state('Z gate', sv)
rot = euclid3d.rotation(3, 0, 1, np.pi)
save_bloch('bloch_4_Z.svg', 'Z|0>', inner_proj=rot)
print(f'  Circuit:\n{qc.draw()}')


print('\n========== PART 5: Y Gate ==========')
qc = QuantumCircuit(1)
qc.y(0)
sv = Statevector.from_label('0').evolve(qc)
print_state('Y gate', sv)
rot = euclid3d.rotation(3, 1, 2, np.pi)
save_bloch('bloch_5_Y.svg', 'Y|0>', inner_proj=rot)
print(f'  Circuit:\n{qc.draw()}')


print('\n========== PART 6: S Gate (90 deg Z rotation) ==========')
qc = QuantumCircuit(1)
qc.s(0)
sv = Statevector.from_label('0').evolve(qc)
print_state('S gate', sv)
rot = euclid3d.rotation(3, 0, 1, np.pi/4)
save_bloch('bloch_6_S.svg', 'S|0>', inner_proj=rot)

print('\n========== PART 6b: T Gate (45 deg Z rotation) ==========')
qc = QuantumCircuit(1)
qc.t(0)
sv = Statevector.from_label('0').evolve(qc)
print_state('T gate', sv)
rot = euclid3d.rotation(3, 0, 1, np.pi/8)
save_bloch('bloch_6_T.svg', 'T|0>', inner_proj=rot)


print('\n========== PART 7: Measurement after H Gate ==========')
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

simulator = AerSimulator()
job = simulator.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()
print(f'  Circuit:\n{qc.draw()}')
print(f'\n  Measurement results (1024 shots): {counts}')
total = sum(counts.values())
for state, count in counts.items():
    print(f'    |{state}> : {count} times = {count/total*100:.1f}%')


print('\n========== PART 8: Gate Sequence H→Z→H ==========')
qc = QuantumCircuit(1)
qc.h(0)
qc.z(0)
qc.h(0)
sv = Statevector.from_label('0').evolve(qc)
print_state('H→Z→H (should equal X)', sv)
print(f'  Circuit:\n{qc.draw()}')
