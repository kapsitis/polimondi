import sys
from polyforms.n_gon import NGonProblem
from polyforms.n_gon import FileWriter
from polyforms.n_gon import Format
from polyforms.backtrackk import Backtrackk
from multiprocessing import Pool, cpu_count


def process_prefix(n, prefix):
    q = NGonProblem(n, list(range(n, 0, -1)), prefix, Format.COMPACT, FileWriter(f'perfect_{n}_{prefix}.txt'))
    b = Backtrackk(q)
    while b.attempt(0):
        q.display()
    print(f'Found {q.solution_count} solutions for prefix {prefix}')


def main(n):
    # For perfect_13.txt these 8 prefixes of length=3 give polymond counts:
    # 18 + 42 + 26 + 19 + 2 + 52 + 46 + 23 = 228
    # prefixes3 = ['ABA', 'ABC', 'ABD', 'ABF', 'ACA', 'ACB', 'ACD', 'ACE']

    prefixes4 = ['ABAB', 'ABAC', 'ABAE', 'ABAF',
                 'ABCA', 'ABCB', 'ABCD', 'ABCE',
                 'ABDB', 'ABDC', 'ABDE', 'ABDF',
                 'ABFA', 'ABFB', 'ABFD', 'ABFE',
                 'ACAB', 'ACAC', 'ACAE', 'ACAF',
                 'ACBA', 'ACBC', 'ACBD', 'ACBF',
                 'ACDB', 'ACDC', 'ACDE', 'ACDF',
                 'ACEA', 'ACEC', 'ACED', 'ACEF']



    # Determine the number of processes based on available CPU cores and prefixes count
    print('CPU count = {}; prefixes = {}'.format(cpu_count(), prefixes4))
    num_processes = min(cpu_count(), len(prefixes4))

    # Create a multiprocessing pool with desired number of processes
    with Pool(num_processes) as pool:
        # Map each prefix to be processed in parallel
        pool.starmap(process_prefix, [(n, prefix) for prefix in prefixes4])


if __name__ == '__main__':
    n = int(sys.argv[1])
    main(n)