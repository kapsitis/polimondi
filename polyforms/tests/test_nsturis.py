from polyforms.mag_enum import MagEnum
from polyforms.n_gon import Format

def main():
    n = 5
    permutation = list(range(1,n+1))
    permutation.reverse()
    me = MagEnum(Format.LETTERS)
    me.list_iamonds(permutation)

if __name__ == '__main__':
    main()