import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, '../../polyforms/src'))
sys.path.insert(0, parent_dir)

from polyforms.n_gon import NGonProblem
from polyforms.n_gon import FileWriter
from polyforms.n_gon import Format
from polyforms.backtrackk import Backtrackk
from multiprocessing import Pool, cpu_count


def process_prefix(n, prefix):
    parent_dir = "../../docs/obtuse"
    q = NGonProblem(n, list(range(n, 0, -1)), 
                    prefix, 
                    Format.COMPACT, 
                    FileWriter(os.path.join(parent_dir, f'obtuse_{n}_{prefix}.txt')))
    b = Backtrackk(q)
    while b.attempt(0):
        q.display()
    print(f'Found {q.solution_count} solutions for prefix {prefix}')
    return q.solution_count


def main(n):
    
    prefixes = ['ABABAB', 'ABABAF', 'ABABCB', 'ABABCD',
            'ABAFAB', 'ABAFAF', 'ABAFED', 'ABAFEF', 
            'ABCBAB', 'ABCBAF', 'ABCBCB', 'ABCBCD', 
            'ABCDCB', 'ABCDCD', 'ABCDED', 'ABCDEF']

    # Determine the number of processes based on available CPU cores and prefixes count
    print('CPU count = {}; prefixes = {}'.format(cpu_count(), prefixes))
    num_processes = min(cpu_count(), len(prefixes))

    # Create a multiprocessing pool with desired number of processes
    with Pool(num_processes) as pool:
        # Map each prefix to be processed in parallel
        results = pool.starmap(process_prefix, [(n, prefix) for prefix in prefixes])

    # Compute and print the sum of results
    total = sum(results)
    print('Total polyiamonds found: {}'.format(total))
    print(results)


if __name__ == '__main__':
    n = int(sys.argv[1])
    main(n)

