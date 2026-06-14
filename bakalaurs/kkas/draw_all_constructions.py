import sys
import os
import matplotlib.pyplot as plt

# Ensure the polyforms source directory is in the path
script_dir = os.path.dirname(os.path.abspath(__file__))
polyforms_src = os.path.join(script_dir, 'polyforms', 'src')
sys.path.insert(0, polyforms_src)

from polyforms.draw_scene import DrawScene, Align
from polyforms.polyiamond import Polyiamond

CONSTRUCTIONS_FILE = os.path.join(script_dir, 'constructions.txt')
OUTPUT_DIR = os.path.join(script_dir, 'construction_images')


def parse_constructions(filepath):
    """Read constructions.txt and return list of (u, v, w, x, y) tuples."""
    constructions = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = [p.strip() for p in line.split('|')]
            if len(parts) == 5:
                constructions.append(tuple(parts))
    return constructions


def make_title(u, v, w, x, y):
    """Format title as S_k = u + (v)^k + w + (x)^k + y with lowercase, brackets around repeating parts."""
    def lower(s):
        return s.lower() if s else ''

    parts = []
    if u:
        parts.append(lower(u))
    if v:
        parts.append(f'({lower(v)})ᵏ')
    if w:
        parts.append(lower(w))
    if x:
        parts.append(f'({lower(x)})ᵏ')
    if y:
        parts.append(lower(y))
    return 'S\u2096 = ' + ' + '.join(parts)


def get_poly_key(u, v, w, x, y):
    """
    Compute a canonical key for the first 3 polyiamonds of a construction.
    Returns a tuple of vertex-list tuples for k=1,2,3, or None if any k fails.
    """
    key_parts = []
    for k in range(1, 4):
        s = u + v * k + w + x * k + y
        sides = list(zip(range(len(s), 0, -1), list(s)))
        try:
            p = Polyiamond(sides)
            verts = tuple(p.get_mod_descartes())
            key_parts.append(verts)
        except Exception:
            return None
    return tuple(key_parts)


def draw_group(group_constructions, poly_key, output_path):
    """Draw the first 3 polyiamonds and title with all equivalent formulas."""
    u, v, w, x, y = group_constructions[0]

    scene = DrawScene(Align.BASELINE)
    added = 0
    current_x_offset = 0

    for k in range(1, 4):
        s = u + v * k + w + x * k + y
        sides = list(zip(range(len(s), 0, -1), list(s)))
        try:
            p = Polyiamond(sides)
            scene.add_polyiamond(f'k={k}', p, (current_x_offset, 0))
            min_x, max_x, min_y, max_y = p.get_rect_box()
            current_x_offset += (max_x - min_x) + 5
            added += 1
        except Exception as e:
            print(f"  Error at k={k}: {e}")

    if added == 0:
        print(f"  Skipping — no valid polyiamonds.")
        return False

    scene.pack()
    fig = scene.fig

    # Build multi-line title: one line per equivalent formula
    title_lines = [make_title(*c) for c in group_constructions]
    title_text = '\n'.join(title_lines)

    n_lines = len(title_lines)
    line_height = 0.4   # inches per title line
    fig_w = 4 * added
    fig_h = 3 + n_lines * line_height

    fig.set_size_inches(fig_w, fig_h)
    # Place title in figure-fraction coordinates, leaving room at top
    fig.text(0.5, 1.0, title_text, ha='center', va='top',
             fontsize=9, fontfamily='DejaVu Sans', linespacing=1.6,
             transform=fig.transFigure)

    fig.savefig(output_path, bbox_inches='tight', dpi=150)
    plt.close(fig)
    return True


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    constructions = parse_constructions(CONSTRUCTIONS_FILE)
    print(f"Found {len(constructions)} constructions. Grouping duplicates...")

    # Group by canonical visual key
    seen = {}       # key -> list of (u,v,w,x,y)
    key_order = []  # ordered list of unique keys

    for c in constructions:
        u, v, w, x, y = c
        key = get_poly_key(u, v, w, x, y)
        if key is None:
            print(f"  Could not compute key for: {c}")
            continue
        if key not in seen:
            seen[key] = []
            key_order.append(key)
        seen[key].append(c)

    n_unique = len(key_order)
    print(f"{n_unique} unique visual groups (merged from {len(constructions)} constructions).\n")

    for i, key in enumerate(key_order, start=1):
        group = seen[key]
        u, v, w, x, y = group[0]
        label = f'{u}_{v}_{w}_{x}_{y}'.replace(' ', '')
        safe_label = ''.join(c if c.isalnum() or c == '_' else '' for c in label)[:40]
        out_path = os.path.join(OUTPUT_DIR, f'{i:02d}_{safe_label}.png')

        print(f"[{i}/{n_unique}] {len(group)} formula(s):")
        for c in group:
            print(f"  {' | '.join(c)}")

        success = draw_group(group, key, out_path)
        if success:
            print(f"  Saved: {out_path}")

    print(f"\nDone! Images saved to: {OUTPUT_DIR}")


if __name__ == '__main__':
    main()
