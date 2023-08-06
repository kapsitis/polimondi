from itertools import permutations


def get_permutations(n):
    num_list = list(range(1, n + 1))
    return sorted(list(permutations(num_list)))


def main():
    n = 5
    permutations = get_permutations(n)
    for perm in permutations:
        if perm[0] == n and perm[1] > perm[n-1]:
            print(perm)
        else:
            continue

if __name__ == '__main__':
    main()