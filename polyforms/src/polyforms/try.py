import sys
sys.path.append('c:/Users/marta/Documents/workspace/polimondi/polyforms/src')
from polyforms.draw_scene import DrawScene, Align
import matplotlib.pyplot as plt
from polyforms.polyiamond import Polyiamond
import warnings
warnings.filterwarnings('ignore')

OUT = r'C:\Users\marta\.gemini\antigravity\brain\d9bcfafd-42a6-4a7b-b7c0-3d03887356ed'

# 6 distinct confirmed constructions (varying middle and growth blocks)
constructions = [
    # Previously known even
    ('ABD', 'BDFD', 'EDE', 'AFAB', 'AB'),
    ('AB',  'DBDF', 'DEDE', 'AFAB', 'AB'),
    # Newly found from perfect_17 scans
    ('ABF', 'BFDF', 'DEDCD', 'CDCB', 'C'),
    ('ABFD','FBFD', 'EDCD', 'CBCD', 'C'),
    ('A',   'BFDF', 'BFDED', 'CDCB', 'CDC'),
    ('A',   'CACE', 'DFDBD', 'EFAF', 'BAE'),
    ('ACEC','BDFD', 'EAE',   'AFAB', 'AC'),
    ('ACEC','BDFD', 'FDF',   'AFAB', 'AC'),
]

labels = [
    'Even A (step 8)',
    'Even B (step 8)',
    'New 1 (step 8)',
    'New 2 (step 8)',
    'New 3 (step 8)',
    'New 4 (step 8)',
    'New 5 (step 8)',
    'New 6 (step 8)',
]

for idx, (c, label) in enumerate(zip(constructions, labels)):
    u, v, w, x, y = c
    scene = DrawScene(Align.BASELINE)
    added = 0
    for k in range(1, 5):
        s = u + v*k + w + x*k + y
        sides = list(zip(range(len(s), 0, -1), list(s)))
        try:
            p = Polyiamond(sides)
            if p.is_valid():
                scene.add_polyiamond(f'k{k}', p, (added * 50, 0))
                added += 1
        except:
            pass
    if added == 0:
        print(f'Skipping {label} - no valid polyiamonds')
        continue
    scene.pack()
    fig = scene.fig
    fig.suptitle(label, fontsize=10, y=1.02)
    fig.set_size_inches(12, 3)
    out_path = f'{OUT}\\new_construction_{idx+1}.png'
    fig.savefig(out_path, bbox_inches='tight')
    plt.close(fig)
    print(f'Saved: {out_path}  ({added} polyiamonds, k=1..{added})')

print('Done.')
