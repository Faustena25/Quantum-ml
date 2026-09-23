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
    print(f'Saved {filename}')

# ── 1. Initial state |0> (north pole) ──
save_bloch('1_state_0.svg', '|0>')

# ── 2. X gate: 180 deg around X-axis → |0> becomes |1> ──
rot_x = euclid3d.rotation(3, 0, 2, np.pi)
save_bloch('2_after_X_gate.svg', 'X|0>=|1>', inner_proj=rot_x)

# ── 3. Y gate: 180 deg around Y-axis ──
rot_y = euclid3d.rotation(3, 1, 2, np.pi)
save_bloch('3_after_Y_gate.svg', 'Y|0>', inner_proj=rot_y)

# ── 4. Z gate: 180 deg around Z-axis ──
rot_z = euclid3d.rotation(3, 0, 1, np.pi)
save_bloch('4_after_Z_gate.svg', 'Z|0>', inner_proj=rot_z)

# ── 5. H gate: Hadamard → superposition |+> ──
rot_h = euclid3d.rotation(3, 0, 1, np.pi/2)
save_bloch('5_after_H_gate.svg', 'H|0>=|+>', inner_proj=rot_h)

# ── 6. S gate: 90 deg around Z-axis ──
rot_s = euclid3d.rotation(3, 0, 1, np.pi/4)
save_bloch('6_after_S_gate.svg', 'S|0>', inner_proj=rot_s)

# ── 7. T gate: 45 deg around Z-axis ──
rot_t = euclid3d.rotation(3, 0, 1, np.pi/8)
save_bloch('7_after_T_gate.svg', 'T|0>', inner_proj=rot_t)

print('\nAll saved! Open SVG files in your browser.')
print('Gates covered: |0>, X, Y, Z, H, S, T')