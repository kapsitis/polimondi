import re


# Get frequencies of start fragments
def get_start_fragments():
    result = dict()

    perfect_list = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    acute_list = [9, 27, 29, 33, 35, 39, 41, 45, 47, 51]

    patterns = ('^AB', '^AC', '^ABA', '^ABC', '^ABD', '^ABF', '^ACA', '^ACB', '^ACD', '^ACE')
    patterns_re = []
    for pattern in patterns:
        patterns_re.append(re.compile(pattern))



    for perf in perfect_list:
        counts = [0]*len(patterns_re)
        count = 0
        file_name = 'perfect_{}.txt'.format(perf)
        with open(file_name, 'r') as fp:
            for line in fp:
                count += 1
                for idx, p_re in enumerate(patterns_re):
                    if p_re.match(line):
                        counts[idx] += 1
        result[perf] = [num/count for num in counts]
        # print("In {} lines = {}, and counts = {}".format(file_name, count, counts))
    return result

def main():
    perfect_list = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    acute_list = [9, 27, 29, 33, 35, 39, 41, 45, 47, 51]

    patterns = ('^AB', '^AC', '^ABA', '^ABC', '^ABD', '^ABF', '^ACA', '^ACB', '^ACD', '^ACE')
    patterns_re = []
    for pattern in patterns:
        patterns_re.append(re.compile(pattern))



    for perf in perfect_list:
        counts = [0]*len(patterns_re)
        count = 0
        file_name = 'perfect_{}.txt'.format(perf)
        with open(file_name, 'r') as fp:
            for line in fp:
                count += 1
                for idx, p_re in enumerate(patterns_re):
                    if p_re.match(line):
                        counts[idx] += 1

        print("In {} lines = {}, and counts = {}".format(file_name, count, counts))


if __name__ == '__main__':
    main()