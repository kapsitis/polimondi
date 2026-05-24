import sys
from polyforms.polyiamond import Polyiamond
import warnings
warnings.filterwarnings('ignore')

DATA_DIR = r'C:\Users\marta\Documents\workspace\polimondi\docs\polimondi'

def load(n):
    with open(f'{DATA_DIR}\\perfect_{n}.txt') as f:
        return [l.strip() for l in f if l.strip()]

def test_rule(u, v, w, x, y, k_max=20):
    for k in range(1, k_max+1):
        s = u + v*k + w + x*k + y
        sides = list(zip(range(len(s), 0, -1), list(s)))
        try:
            p = Polyiamond(sides)
            if not p.is_valid():
                return False
        except:
            return False
    return True

print('Loading files...')
words15 = load(15)
words23 = set(load(23))
print(f'  perfect_15: {len(words15)} entries')
print(f'  perfect_23: {len(words23)} entries')

confirmed = []
seen = set()

print('\nSearching...')
count = 0
for sides in words15:
    L = len(sides)
    for i in range(0, L):
        for j in range(i+1, L):
            v = sides[i:j]
            lv = len(v)
            if lv < 1 or lv > 7: continue
            lx_target = 8 - lv
            for k in range(j+1, L):
                for m in range(k+1, min(k+lx_target+1, L+1)):
                    x = sides[k:m]
                    if len(x) != lx_target: continue
                    u = sides[:i]
                    w = sides[j:k]
                    y = sides[m:]
                    candidate23 = u + v*2 + w + x*2 + y
                    if candidate23 in words23:
                        rule = (u, v, w, x, y)
                        if rule not in seen:
                            seen.add(rule)
                            if test_rule(u, v, w, x, y, k_max=20):
                                confirmed.append(rule)
                                base = len(u+v+w+x+y)
                                parity = 'odd' if base % 2 else 'even'
                                print(f'CONFIRMED ({parity}, base={base}, step=8): {rule}')
    count += 1
    if count % 100 == 0:
        print(f'  ... {count}/{len(words15)} scanned, {len(confirmed)} found')

print(f'\nTotal confirmed from perfect_15: {len(confirmed)}')
for c in confirmed:
    u, v, w, x, y = c
    print(f'{u} | {v} | {w} | {x} | {y}')
