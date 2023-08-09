from .n_gon import findAllSolutions
from .n_gon import Format
from itertools import permutations

class MagEnum:

    def __init__(self, out_format):
        self.out_format = out_format

    def list_iamonds(self, perm):
        findAllSolutions(perm, self.out_format, 'poly_{}_{}.txt'.format(len(perm), perm))


    @staticmethod
    def get_permutations(n):
        num_list = list(range(1, n + 1))
        all_permutations = sorted(list(permutations(num_list)))
        valid_permutations = []
        # Only keep permutations that are not symmetric against rotation or reverse:
        # (1) every permutation should start by the size of length `n`
        # (2) both neighbors of the side of length `n` have certain length relationship
        for perm in all_permutations:
            if perm[0] == n and perm[1] > perm[n - 1]:
                valid_permutations.append(perm)
        return valid_permutations