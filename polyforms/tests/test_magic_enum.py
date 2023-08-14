from polyforms.magic_enum import *

def test_get_permutations4():
    result = MagEnum.get_permutations(4)
    assert len(result) == 3
    assert result == [(4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)]

def test_get_permutations5():
    result = MagEnum.get_permutations(5)
    assert len(result) == 12



