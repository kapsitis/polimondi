import sys
import time

sys.path.insert(0, '..')
sys.path.insert(0, '../../oo-backtracking')
from polimondi import *
from NSturis import *



def get_computation_times(n1, n2, step):
    computation_times = list()

    #with open('computation_times4.txt', 'a') as file_object:
    #    file_object.write('N,milliseconds\n')

    for n in range(n1, n2, step):
        start_time = time.time()

        # By Marta: To get runtimes, uncomment the code section below (and comment "By Kalvis" section)
        q = Polimondi(n)
        b = Backtrack(q)
        if b.attempt(1):
            print('Attempting n = {}'.format(n))
            # q.display()

        # By Kalvis
        # q = NSturisProblem(n)
        # b = Backtrack(q)
        # n = 0
        # while b.attempt(0):
        #     q.initValues = q.find_indices()
        #     q.reset()
        #     n += 1
        # print('{} positions found'.format(q.solution_count))

        end_time = time.time()
        print('---{}: {:.3f} seconds ---'.format(n, end_time - start_time))
        computation_times.append(round(1000 * (end_time - start_time)))

    return computation_times

if __name__ == '__main__':
    computation_times = get_computation_times(9, 21, 2)
    n_values = list(range(9,21,2))
    print('compTimes for {} are {}'.format(n_values, computation_times))