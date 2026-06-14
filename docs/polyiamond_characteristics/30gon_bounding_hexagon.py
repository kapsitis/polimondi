import sys
import os
from polyforms.polyiamond import Polyiamond
from polyforms.point_tg import PointTg

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




# Bounding hexagon
a_min, a_max, b_min, b_max, c_min, c_max = p.get_hex_bounds()
y_min, y_max = a_min, a_max
z_min, z_max = b_min, b_max
x_min, x_max = c_min, c_max

# The bounding hexagon in (x, y) integer coordinates is formed by these intersections
hex_pts = p.get_bounding_hexagon_vertices()

hex_xs = []
hex_ys = []
for pt in hex_pts:
    xy = pt.get_xy()
    hex_xs.append(xy[0])
    hex_ys.append(xy[1])

# add first vertex again to close the loop
hex_xs.append(hex_xs[0])
hex_ys.append(hex_ys[0])

ax.plot(hex_xs, hex_ys, color='red', linewidth=2)




# Draw the polyiamond perimeter 
poly_xs = xs + [xs[0]]
poly_ys = [y * TH for y in (ys + [ys[0]])]

ax.fill(poly_xs, poly_ys, color='blue', alpha=0.1)
ax.plot(poly_xs, poly_ys, color='blue', linewidth=2)



plt.savefig('30gon_bounding_hexagon.svg', format='svg', bbox_inches='tight', transparent=True, pad_inches=0.1)

# Remove hardcoded width and height from the generated SVG
with open('30gon_bounding_hexagon.svg', 'r') as f:
    svg_content = f.read()

import re
svg_content = re.sub(r'width="[0-9.]+pt" height="[0-9.]+pt" ', '', svg_content)

with open('30gon_bounding_hexagon.svg', 'w') as f:
    f.write(svg_content)

print("Saved 30gon_bounding_hexagon.svg")
