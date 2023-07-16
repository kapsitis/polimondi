from .n_gon import findAllSolutions
from .n_gon import Format

class MagEnum:

    def __init__(self, out_format):
        self.out_format = out_format

    def list_iamonds(self, perm):
        findAllSolutions(perm, self.out_format, 'poly_{}_{}.txt'.format(len(perm), perm))


