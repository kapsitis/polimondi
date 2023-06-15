from itertools import permutations

def get_permutations(n):
    num_list = list(range(1, n + 1))
    return sorted(list(permutations(num_list)))


def main():
    print(get_permutations(3))

if __name__ == '__main__':
    main()