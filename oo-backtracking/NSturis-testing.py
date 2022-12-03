# -*- coding: utf-8 -*-

import pytest

from backtrack import *
from NSturis import *


def test_joc_koord5():
    n5_prob = NSturisProblem(5)
    n5_prob.record(0, 'A')
    n5_prob.record(1, 'C')
    n5_prob.record(2, 'E')
    n5_prob.record(3, 'D')
    n5_prob.record(4, 'F')
    result = n5_prob.get_joc_koord()
    assert result == [[0, 5], [4, -2.0], [-3, -1.5], [0, -2], [-1, 0.5]]


def test_joc_koord7():
    n7_prob = NSturisProblem(7)
    n7_prob.directions = ['A', 'C', 'D', 'E', 'F', 'B', 'F']
    result = n7_prob.get_joc_koord()
    assert result == [[0, 7], [6, -3.0], [0, -5], [-4, -2.0], [-3, 1.5], [2, 1.0], [-1, 0.5]]

    n7_prob2 = NSturisProblem(7)
    n7_prob2.directions = ['A', 'C', 'D', 'E', 'F', 'A', 'C']
    result = n7_prob2.get_joc_koord()
    assert result == [[0, 7], [6, -3.0], [0, -5], [-4, -2.0], [-3, 1.5], [0, 2], [1, -0.5]]

def test_5sturis():
    n5_problem = NSturisProblem(5)
    b = Backtrack(n5_problem)
    assert b.attempt(0)
    assert n5_problem.directions == ['A', 'C', 'E', 'D', 'F']

def test_7sturis():
    n7_problem = NSturisProblem(7)
    b = Backtrack(n7_problem)
    assert b.attempt(0)
    assert n7_problem.directions == ['A', 'C', 'D', 'E', 'F', 'B', 'E']
    n7_problem.initValues = n7_problem.directions
    n7_problem.reset()
    assert b.attempt(0)
    assert n7_problem.directions == ['A' 'C', 'D', 'E', 'F', 'A', 'C']
    n7_problem.initValues = n7_problem.directions
    n7_problem.reset()
    assert not b.attempt(0)

