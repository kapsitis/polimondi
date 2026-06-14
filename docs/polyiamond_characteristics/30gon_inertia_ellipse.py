import sys
import os
from polyforms.polyiamond import Polyiamond

import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import numpy as np

TH = np.sqrt(3)/2

# The perfect 30-gon polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
pts = p.get_mod_descartes()

xs = [pt[0] for pt in pts]
ys = [pt[1] for pt in pts]

min_x, max_x = min(xs), max(xs)
min_y, max_y = min(ys), max(ys)

# Add some padding
padding_x = 5
padding_y = 5

left = int(np.floor(min_x)) - padding_x
right = int(np.ceil(max_x)) + padding_x
bottom = int(np.floor(min_y)) - padding_y
top = int(np.ceil(max_y)) + padding_y

width = right - left
height = top - bottom

# Create figure
fig, ax = plt.subplots(figsize=(10, 10))
ax.axis('equal')
ax.axis('off')
plt.margins(x=0, y=0)

# Set limits
ax.set_xlim(left, right)
ax.set_ylim(bottom * TH, top * TH)

# Create a clipping path for the grid
vertices = np.array([
    [left, bottom * TH],
    [right, bottom * TH],
    [right, top * TH],
    [left, top * TH],
    [0, 0]
])
codes = [
    mpath.Path.MOVETO, mpath.Path.LINETO, mpath.Path.LINETO, mpath.Path.LINETO,
    mpath.Path.CLOSEPOLY
]
clip_path = mpath.Path(vertices, codes)
patch = mpatches.PathPatch(clip_path, transform=ax.transData, fill=False, edgecolor='none')
ax.add_patch(patch)

# Grid lines
def draw_line(x_coords, y_coords, is_dark):
    linewidth = 1.0 if is_dark else 0.25
    color = '#cccccc' if is_dark else '#cccccc'
    line, = ax.plot(x_coords, [y * TH for y in y_coords], color=color, linewidth=linewidth, linestyle='solid')
    line.set_clip_path(patch)

for y in range(bottom, top + 1):
    if y % 5 == 0:
        draw_line([left, right], [y, y], '#cccccc')

# Slanted lines 1
min_c1 = int(np.floor(2 * left - top)) - 5
max_c1 = int(np.ceil(2 * right - bottom)) + 5
for c in range(min_c1, max_c1 + 1):
    if c % 10 == 0:
        draw_line([left, right], [2*left - c, 2*right - c], '#cccccc')

# Slanted lines 2
min_c2 = int(np.floor(2 * left + bottom)) - 5
max_c2 = int(np.ceil(2 * right + top)) + 5
for c in range(min_c2, max_c2 + 1):
    if c % 10 == 0:
        draw_line([left, right], [c - 2*left, c - 2*right], '#cccccc')

# Draw the polyiamond perimeter (no fill)
poly_xs = xs + [xs[0]]
poly_ys = [y * TH for y in (ys + [ys[0]])]
ax.plot(poly_xs, poly_ys, color='blue', linewidth=2)

# Compute centroid in Euclidean coordinates
descartes = p.get_descartes()
verts = np.asarray(descartes, dtype=float)
x = verts[:, 0]
y = verts[:, 1]
x1 = np.roll(x, -1)
y1 = np.roll(y, -1)
cross = x * y1 - x1 * y
signed_area = 0.5 * np.sum(cross)
cx = np.sum((x + x1) * cross) / (6.0 * signed_area)
cy = np.sum((y + y1) * cross) / (6.0 * signed_area)

# Get inertia tensor and its eigenvalues/eigenvectors
tensor = p.get_inertia_tensor()
eigenvalues, eigenvectors = np.linalg.eigh(tensor)
# eigenvalues[0] = lambda1 (smaller), eigenvalues[1] = lambda2 (larger)
# eigenvectors columns are the principal axes

# Semi-axes proportional to sqrt(lambda2) and sqrt(lambda1)
# The eigenvector for lambda1 (smaller eigenvalue) corresponds to the direction
# with LESS spread, and lambda2 to MORE spread. For inertia tensor, larger
# eigenvalue means more mass spread in that direction. So the ellipse semi-axis
# proportional to sqrt(lambda2) should be along the eigenvector of lambda1
# (the axis of minimum inertia = direction of maximum extent), and vice versa.
# Actually: in inertia tensor, I_xx = integral(y^2), so large eigenvalue means
# large spread perpendicular to that axis. The eigenvector of lambda1 (min inertia)
# points along the direction of maximum extent. So:
#   semi-axis a (along eigvec of lambda1) proportional to sqrt(lambda2)
#   semi-axis b (along eigvec of lambda2) proportional to sqrt(lambda1)
# This matches the user's request: a ~ sqrt(lambda2), b ~ sqrt(lambda1).

sqrt_l1 = np.sqrt(eigenvalues[0])
sqrt_l2 = np.sqrt(eigenvalues[1])

# Choose scale so the ellipse fits nicely within the image
# Use a fraction of the polyiamond's bounding size
poly_extent = max(max_x - min_x, (max_y - min_y) * TH)
# Scale so the larger semi-axis is about 45% of the polyiamond extent
scale = 0.45 * poly_extent / sqrt_l2

semi_a = sqrt_l2 * scale  # larger semi-axis
semi_b = sqrt_l1 * scale  # smaller semi-axis

# Rotation angle: the eigenvector for lambda1 (column 0) gives the direction
# of the larger semi-axis (a ~ sqrt(lambda2))
evec_min = eigenvectors[:, 0]  # eigenvector for lambda1 (min eigenvalue)
angle_rad = np.arctan2(evec_min[1], evec_min[0])
angle_deg = np.degrees(angle_rad)

# Draw ellipse with transparent fill
ellipse = mpatches.Ellipse(
    (cx, cy), 2*semi_a, 2*semi_b,
    angle=angle_deg,
    facecolor='green', alpha=0.15,
    edgecolor='green', linewidth=1.5
)
ax.add_patch(ellipse)

# Draw principal axes (non-transparent lines)
# Major axis direction (along eigvec of lambda1)
dx_major = semi_a * np.cos(angle_rad)
dy_major = semi_a * np.sin(angle_rad)
ax.plot([cx - dx_major, cx + dx_major], [cy - dy_major, cy + dy_major],
        color='green', linewidth=1.5)

# Minor axis direction (perpendicular)
dx_minor = semi_b * np.cos(angle_rad + np.pi/2)
dy_minor = semi_b * np.sin(angle_rad + np.pi/2)
ax.plot([cx - dx_minor, cx + dx_minor], [cy - dy_minor, cy + dy_minor],
        color='green', linewidth=1.5)

# Mark the centroid
ax.plot(cx, cy, 'go', markersize=6)

plt.savefig('30gon_inertia_ellipse.svg', format='svg', bbox_inches='tight', transparent=True, pad_inches=0.1)

# Remove hardcoded width and height from the generated SVG
with open('30gon_inertia_ellipse.svg', 'r') as f:
    svg_content = f.read()

import re
svg_content = re.sub(r'width="[0-9.]+pt" height="[0-9.]+pt" ', '', svg_content)

with open('30gon_inertia_ellipse.svg', 'w') as f:
    f.write(svg_content)

print("Saved 30gon_inertia_ellipse.svg")
