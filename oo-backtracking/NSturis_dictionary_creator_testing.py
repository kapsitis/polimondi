import pytest

from backtrack import *
from NSturis_dictionary_creator import *

# Record move 'A' to ['B']
def test_record():
    n2_prob = NSturisDictionaryCreator(2)
    n2_prob.directions = ['B']
    n2_prob.vertices = [PointTg(0,0,0), PointTg(1,-1,0)]
    n2_prob.points = [PointTg(0,0,0), PointTg(1,-1,0)]
    n2_prob.record(1, 'A')
    assert n2_prob.directions == ['B', 'A']
    assert n2_prob.vertices == [PointTg(0,0,0), PointTg(1,-1,0), PointTg(3,-1,-2)]
    assert set(n2_prob.points) == set([PointTg(0,0,0), PointTg(1,-1,0), PointTg(2,-1,-1), PointTg(3,-1,-2)])

# Undo move 'B' from ['B']
def test_undo():
    n2_prob = NSturisDictionaryCreator(2)
    n2_prob.directions = ['B']
    n2_prob.vertices = [PointTg(0,0,0), PointTg(1,-1,0)]
    n2_prob.points = [PointTg(0,0,0), PointTg(1,-1,0)]
    n2_prob.undo(1, 'B')
    assert n2_prob.directions == []
    assert n2_prob.vertices == [PointTg(0,0,0)]
    assert set(n2_prob.points) == set([PointTg(0,0,0)])
