import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import numpy as np

from konstrukcijas.inductive_drawings import poly_seq

# Triangle height
TH = np.sqrt(3)/2



def direction_to_vector(d):    
    if d == 'A':
        return np.array([1, 0])
    elif d == 'B':
        return np.array([1/2, np.sqrt(3)/2])
    elif d == 'C':
        return np.array([-1/2, np.sqrt(3)/2])
    elif d == 'D':
        return np.array([-1, 0])
    elif d == 'E':
        return np.array([-1/2, -np.sqrt(3)/2])
    elif d == 'F':
        return np.array([1/2, -np.sqrt(3)/2])


def draw_seq(ax, seq, color, dd):
    # Draw polyline
    x, y = [0+dd[0]], [dd[1]]
    for i, d in enumerate(seq):
        v = direction_to_vector(d)
        x.append(x[-1] + (len(seq) - i) * v[0])
        y.append(y[-1] + (len(seq) - i) * v[1])

    ax.plot(x, y, '{}-'.format(color), linewidth=0.8)


def create_rectangle_path(left, bottom, m, n):
    vertices = np.array([ [left, bottom], [left+m, bottom], [left+m, (n + bottom) * TH], [left, (n + bottom) * TH], [0, 0] ])
    codes = [
        mpath.Path.MOVETO, mpath.Path.LINETO, mpath.Path.LINETO, mpath.Path.LINETO,
        mpath.Path.CLOSEPOLY
    ]
    path = mpath.Path(vertices, codes)
    return path


def draw_triangle_grid(left, bottom, m, n, color, linestyle, linewidth):
    plt.figure()
    fig, ax = plt.subplots()
    ax.axis('equal')
    ax.axis('off')
    fig.set_size_inches(8, 13)
    ax.set_xlim(-20,60)
    ax.set_ylim(-20,110)

    path = create_rectangle_path(left, bottom, m,n)
    patch = mpatches.PathPatch(path, transform=ax.transData)
    
    # Horizontal lines
    for i in range(0, n + 1):
        plus_minus = 0 if i % 2 == 0 else 0.5
        line, = ax.plot([left + plus_minus, left + m - plus_minus], [(bottom + i) * TH, (bottom + i) * TH], 
                        color=color, linestyle=linestyle, linewidth=linewidth)
        line.set_clip_path(patch)


    # Slanted-upwards lines
    for i in range(-n//2, m + 1):
        line, = ax.plot([left + i, left + i + n * TH / np.sqrt(3)], [bottom*TH, (bottom + n) * TH],  color=color, linestyle=linestyle, linewidth=linewidth)
        line.set_clip_path(patch)

    # Slanted-downwards lines
    for i in range(0, m + n//2 + 1):
        line, = ax.plot([left + i, left + i - n * TH / np.sqrt(3)], [bottom*TH, (bottom + n) * TH], color=color, linestyle=linestyle, linewidth=linewidth)
        line.set_clip_path(patch)

    draw_seq(ax, poly_seq.SEQUENCE_8_5_A[0], 'r', [0.0,0.0])
    draw_seq(ax, poly_seq.SEQUENCE_8_5_A[1], 'b', [0.1, 0.1])

    
    plt.savefig('triangle_grid.svg', format='svg')
    # plt.show()

draw_triangle_grid(-20, -20, 80, 130, 'black', 'solid', 0.25)


