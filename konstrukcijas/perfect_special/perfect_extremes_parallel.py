import sys

from polyforms.polyiamond import Polyiamond
from multiprocessing import Pool, cpu_count


def f(line, metric):
    p = Polyiamond(line)
    if metric == 'area':
        return p.get_area()
    elif metric == 'diameter':
        return p.diameter()[0]
    elif metric == 'width':
        return p.width()


def process_prefix(type, n, metric, prefix):
    print(f"Processing {type} {n}-polyiamonds, prefix {prefix} with metric {metric}")
    max_value = 0
    max_array = []
    min_value = 10000000000
    min_array = []
    fileName = f'../editing_distance/{type}_{n}_{prefix}.txt'
    with open(fileName, 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            val = f(line, metric)
            if val > max_value:
                max_array = []
                max_value = val
            if val == max_value:
                max_array.append(line)
            if val < min_value:
                min_array = []
                min_value = val
            if val == min_value:
                min_array.append(line)

    file1 = open(f'max_{type}_{metric}.txt', 'a')
    for pp in max_array:
        file1.write(f'{pp},{max_value}\n')
    file1.close()

    file2 = open(f'min_{type}_{metric}.txt', 'a')
    for pp in min_array:
        file2.write(f'{pp},{min_value}\n')
    file2.close()




def main(type, n, metric):

    prefixes4 = ['ABAB', 'ABAC', 'ABAE', 'ABAF',
                 'ABCA', 'ABCB', 'ABCD', 'ABCE',
                 'ABDB', 'ABDC', 'ABDE', 'ABDF',
                 'ABFA', 'ABFB', 'ABFD', 'ABFE',
                 'ACAB', 'ACAC', 'ACAE', 'ACAF',
                 'ACBA', 'ACBC', 'ACBD', 'ACBF',
                 'ACDB', 'ACDC', 'ACDE', 'ACDF',
                 'ACEA', 'ACEC', 'ACED', 'ACEF']


    num_processes = min(cpu_count(), len(prefixes4))

    with Pool(num_processes) as pool:
        pool.starmap(process_prefix, [(type, n, metric, prefix) for prefix in prefixes4])


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python perfect_extremes_parallel.py <type> <n> <correct>")
        sys.exit(1)
    type = sys.argv[1]
    n = int(sys.argv[2])
    metric = sys.argv[3]
    if not type in ['perfect', 'acute', 'obtuse']:
        print("Type must be 'perfect', 'acute', or 'obtuse'")
        sys.exit(1)
    if not metric in ['area', 'diameter', 'width', 'dimension']:
        print("Type must be 'perfect', 'acute', or 'obtuse'")
        sys.exit(1)

    main(type, n, metric)
