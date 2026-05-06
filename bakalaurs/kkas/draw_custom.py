"""
Draw first 3 polyiamonds for the construction:
  s(k) = A + (BC)^k + DF + (EF)^(k-1) + ED + (EF)^k + AC + (BC)^(k-1)
"""
import sys
import os
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
polyforms_src = os.path.join(script_dir, 'polyforms', 'src')
sys.path.insert(0, polyforms_src)

from polyforms.draw_scene import DrawScene, Align
from polyforms.polyiamond import Polyiamond

def build_sequence(k):
    """Build the direction string for a given k."""
    s = (
        'A'          +   # a
        'BC' * k     +   # (bc)^k
        'DF'         +   # df
        'EF' * (k-1) +   # (ef)^(k-1)
        'ED'         +   # ed
        'EF' * k     +   # (ef)^k
        'AC'         +   # ac
        'BC' * (k-1)     # (bc)^(k-1)
    )
    return s

TITLE = r'$S_k = a + (bc)^k + df + (ef)^{k-1} + ed + (ef)^k + ac + (bc)^{k-1}$'

scene = DrawScene(Align.BASELINE)
added = 0
current_x_offset = 0

for k in range(1, 4):
    s = build_sequence(k)
    sides = list(zip(range(len(s), 0, -1), list(s)))
    print(f"k={k}: s = {s}  ({len(s)} sides)")
    try:
        p = Polyiamond(sides)
        scene.add_polyiamond(f'k={k}', p, (current_x_offset, 0))
        min_x, max_x, min_y, max_y = p.get_rect_box()
        current_x_offset += (max_x - min_x) + 5
        added += 1
    except Exception as e:
        print(f"  Error at k={k}: {e}")

if added > 0:
    scene.pack()
    fig = scene.fig
    fig.set_size_inches(5 * added, 4)
    fig.text(0.5, 1.01, TITLE, ha='center', va='bottom',
             fontsize=11, transform=fig.transFigure)

    out = os.path.join(script_dir, 'custom_construction.png')
    fig.savefig(out, bbox_inches='tight', dpi=150)
    plt.close(fig)
    print(f"\nSaved: {out}")
else:
    print("No valid polyiamonds generated.")
