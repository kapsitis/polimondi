import sys
from polyforms.n_gon import NGonProblem
from polyforms.n_gon import FileWriter
from polyforms.n_gon import Format
from polyforms.backtrackk import Backtrackk
from polyforms.polyiamond import Polyiamond



files = [
    'perfect_5.txt',
    'perfect_7.txt',
    'perfect_9.txt',
    'perfect_11.txt',
    'perfect_13.txt',
    'perfect_15.txt',
    'perfect_17.txt',
    'perfect_19.txt',
    'perfect_21.txt',
    'perfect_23.txt'
]


def f(line, metric):
    p = Polyiamond(line)
    if metric == 'array':
        return p.get_area()
    elif metric == 'diameter':
        return p.diameter()[0]

def main(lower, upper):
    metric = 'diameter'
    max_array = dict()
    max_value = dict()
    min_array = dict()
    min_value = dict()
    for i in range(lower, upper):
        print(f"Processing {i}...")
        max_value[i] = 0
        max_array[i] = []
        min_value[i] = 10000000000
        min_array[i] = []
        fileName = f'../../docs/polimondi/perfect_{i}.txt'
        with open(fileName, 'r') as file:
            for line in file:
                line = line.rstrip('\n')
                val = f(line, metric)
                if val > max_value[i]:
                    max_array[i] = []
                    max_value[i] = val
                if val == max_value[i]:
                    max_array[i].append(line)
                if val < min_value[i]:
                    min_array[i] = []
                    min_value[i] = val
                if val == min_value[i]:
                    min_array[i].append(line)

    for i in range(lower, upper):
        print(f'{i}-polyiamond(s) with max {metric} {max_value[i]}:')
        for pp in max_array[i]:
            print(pp)
    print()
    for i in range(lower, upper):
        print(f'{i}-polyiamond(s) with min {metric} {min_value[i]}:')
        for pp in min_array[i]:
            print(pp)



# This file is meant to write all perfect polyiamonds to a file 'perfect_nn.txt'
if __name__ == '__main__':
    lower = int(sys.argv[1])
    upper = int(sys.argv[2])
    main(lower,upper)
