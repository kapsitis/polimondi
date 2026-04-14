import sys
import os
from polyforms.polyiamond import Polyiamond
import warnings
warnings.filterwarnings('ignore')

DATA_DIR = r'C:\Users\marta\Documents\workspace\polimondi\docs\polimondi'
CONSTRUCTIONS_FILE = r'C:\Users\marta\Documents\workspace\polimondi\constructions.txt'

def load(n):
    path = os.path.join(DATA_DIR, f'perfect_{n}.txt')
    if not os.path.exists(path):
        return None
    with open(path) as f:
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

all_new = {}  # n -> list of (u,v,w,x,y)

# Search perfect_N using perfect_(N+8) as the verification target
for base_n in range(5, 15):
    target_n = base_n + 8
    words_base = load(base_n)
    words_target = load(target_n)

    if words_base is None:
        print(f'perfect_{base_n}: file not found, skipping')
        continue
    if words_target is None:
        print(f'perfect_{target_n}: file not found (needed as target), skipping')
        continue

    words_target_set = set(words_target)
    print(f'\nScanning perfect_{base_n} ({len(words_base)} entries) -> verify in perfect_{target_n} ({len(words_target)} entries)')

    confirmed = []
    seen = set()

    for sides in words_base:
        L = len(sides)
        for i in range(0, L):
            for j in range(i+1, L):
                v = sides[i:j]
                lv = len(v)
                if lv < 1 or lv > 7:
                    continue
                lx_target = 8 - lv
                for k in range(j+1, L):
                    for m in range(k+1, min(k+lx_target+1, L+1)):
                        x = sides[k:m]
                        if len(x) != lx_target:
                            continue
                        u = sides[:i]
                        w = sides[j:k]
                        y = sides[m:]
                        candidate = u + v*2 + w + x*2 + y
                        if candidate in words_target_set:
                            rule = (u, v, w, x, y)
                            if rule not in seen:
                                seen.add(rule)
                                if test_rule(u, v, w, x, y, k_max=20):
                                    confirmed.append(rule)
                                    base = len(u+v+w+x+y)
                                    parity = 'odd' if base % 2 else 'even'
                                    print(f'  CONFIRMED ({parity}, base={base}, step=8): {rule}')

    print(f'  -> {len(confirmed)} confirmed from perfect_{base_n}')
    if confirmed:
        all_new[base_n] = confirmed

# Load already-known rules to avoid duplicates
known = set()
with open(CONSTRUCTIONS_FILE) as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) == 5:
                known.add(tuple(parts))

# Append new groups to constructions.txt
group_num = 5  # Groups 1-4 already exist
with open(CONSTRUCTIONS_FILE, 'a') as f:
    for base_n in sorted(all_new.keys(), reverse=True):  # largest first
        new_rules = all_new[base_n]
        to_add = []
        for r in new_rules:
            key = tuple(p.strip() for p in r)
            if key not in known:
                to_add.append(r)
                known.add(key)
        if not to_add:
            continue
        parity = 'odd' if base_n % 2 else 'even'
        f.write(f'\n# -------------------------------------------------------\n')
        f.write(f'# Group {group_num}: {"ODD" if base_n%2 else "EVEN"} — base {base_n}, step 8')
        f.write(f'  (string-matching perfect_{base_n} -> perfect_{base_n+8})\n')
        f.write(f'# Verified valid for k = 1 .. 20\n')
        f.write(f'# Last updated: 2026-04-05\n')
        f.write(f'# -------------------------------------------------------\n\n')
        for r in to_add:
            u, v, w, x, y = r
            f.write(f'{u} | {v} | {w} | {x} | {y}\n')
        group_num += 1
        print(f'  Wrote {len(to_add)} rules for perfect_{base_n} to constructions.txt')

print('\nDone. constructions.txt updated.')
