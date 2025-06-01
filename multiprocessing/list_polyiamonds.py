import sys
import os
import time
from random import randrange


from polyforms.polyiamond import Polyiamond
from multiprocessing import Pool, cpu_count

def process_prefix(ptype, n, prefix):
    time.sleep(randrange(100)/100)
    print(f"Finding {n}-polyiamonds of type {ptype}, prefix '{prefix}'")
    return (prefix, n, ptype, os.getpid())


def main(ptype, n, n_cpu):
    # prefixes = ['ABAB', 'ABAF', 'ABCB', 'ABCD']
    prefixes = ['ABABAB', 'ABABAF', 'ABABCB', 'ABABCD',
                'ABAFAB', 'ABAFAF', 'ABAFED', 'ABAFEF', 
                'ABCBAB', 'ABCBAF', 'ABCBCB', 'ABCBCD', 
                'ABCDCB', 'ABCDCD', 'ABCDED', 'ABCDEF']

    num_processes = 4
    with Pool(num_processes) as pool:
        results = pool.starmap(process_prefix, [(ptype, n, prefix) for prefix in prefixes])

    file0 = open(f'mmsummary_{ptype}_{n}.txt', 'a')
    for result in results:
        csv_string = ','.join(str(item) for item in result)
        file0.write(f'{csv_string}\n')
    file0.close()



# python perfect_extremes_parallel.py perfect 25 area
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python list_polyiamonds.py <poly-type> <n> <n_cpu>")
        sys.exit(1)
    ptype = sys.argv[1]
    n = int(sys.argv[2])
    n_cpu = sys.argv[3]

    main(ptype, n, n_cpu)
