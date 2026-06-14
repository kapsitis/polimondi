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

# Slanted lines 1 (y = 2*x - C) => 2x - y = C
min_c1 = int(np.floor(2 * left - top)) - 5
max_c1 = int(np.ceil(2 * right - bottom)) + 5
for c in range(min_c1, max_c1 + 1):
    if c % 10 == 0:
        draw_line([left, right], [2*left - c, 2*right - c], '#cccccc')

# Slanted lines 2 (y = -2*x + C) => 2x + y = C
min_c2 = int(np.floor(2 * left + bottom)) - 5
max_c2 = int(np.ceil(2 * right + top)) + 5
for c in range(min_c2, max_c2 + 1):
    if c % 10 == 0:
        draw_line([left, right], [c - 2*left, c - 2*right], '#cccccc')

# Draw the polyiamond perimeter (no fill)
poly_xs = xs + [xs[0]]
poly_ys = [y * TH for y in (ys + [ys[0]])]
ax.plot(poly_xs, poly_ys, color='blue', linewidth=2) # Blue perimeter

# Call min_width function
min_width, seg_min_width, parallel_lines = p.min_width()

# Extract returned parallel line data (already scaled by TH)
p1 = np.array(parallel_lines[0])
p2 = np.array(parallel_lines[1])
p_max = np.array(parallel_lines[2])

# Edge direction
direction = p2 - p1
direction_len = np.linalg.norm(direction)
if direction_len > 1e-9:
    direction = direction / direction_len
    
    # We want these lines to span the entire plot area (1000 units is more than enough)
    t_min = -1000
    t_max = 1000
    
    line1_start = p1 + t_min * direction
    line1_end = p1 + t_max * direction
    
    line2_start = p_max + t_min * direction
    line2_end = p_max + t_max * direction
    
    # Draw enclosing parallel lines in black
    ax.plot([line1_start[0], line1_end[0]], [line1_start[1], line1_end[1]], color='black', linewidth=1.5)
    ax.plot([line2_start[0], line2_end[0]], [line2_start[1], line2_end[1]], color='black', linewidth=1.5)

# Draw the perpendicular width segment in red
w_start = np.array(seg_min_width[0])
w_end = np.array(seg_min_width[1])
ax.plot([w_start[0], w_end[0]], [w_start[1], w_end[1]], color='red', linewidth=2)

plt.savefig('30gon_min_width.svg', format='svg', bbox_inches='tight', transparent=True, pad_inches=0.1)

# Remove hardcoded width and height from the generated SVG
with open('30gon_min_width.svg', 'r') as f:
    svg_content = f.read()

import re
svg_content = re.sub(r'width="[0-9.]+pt" height="[0-9.]+pt" ', '', svg_content)

with open('30gon_min_width.svg', 'w') as f:
    f.write(svg_content)

print("Saved 30gon_min_width.svg")
