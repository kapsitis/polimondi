# -*- coding: utf-8 -*-

import pytest

from backtrack import *
from queens import *


def test_board1():
    q = QueenProblem(1)
    b = Backtrack(q)
    assert b.attempt(0)
    assert q.rowPos == [0]


def test_board4():
    q = QueenProblem(4)
    b = Backtrack(q)
    assert b.attempt(0)
    assert q.rowPos == [1, 3, 0, 2]


def test_board5():
    q = QueenProblem(5)
    b = Backtrack(q)
    assert b.attempt(0)
    assert q.rowPos == [0, 2, 4, 1, 3]


def test_board6():
    q = QueenProblem(6)
    b = Backtrack(q)
    assert b.attempt(0)
    assert q.rowPos == [1, 3, 5, 0, 2, 4]


def test_board7():
    q = QueenProblem(7)
    b = Backtrack(q)
    assert b.attempt(0)
    assert q.rowPos == [0, 2, 4, 6, 1, 3, 5]


def test_board8():
    q = QueenProblem(8)
    b = Backtrack(q)
    assert b.attempt(0)
    assert q.rowPos == [0, 4, 7, 5, 2, 6, 1, 3]


def test_reenter4():
    q = QueenProblem(4)
    q.initValues = [1,3,0,2]
    b = Backtrack(q)
    assert b.attempt(0)
    assert q.rowPos == [2, 0, 3, 1]


# @pytest.mark.skip(reason="no way of currently testing this")
def test_board22_with_6_queens():
    q = QueenProblem(22)
    q.initValues = [0, 2, 4, 1, 3, 9, 13, 16, 19, 12]
    b = Backtrack(q)
    assert b.attempt(0)
    assert q.rowPos == [0, 2, 4, 1, 3, 9, 13, 16, 19, 12, 18, 21, 17, 7, 20, 11, 8, 5, 15, 6, 10, 14]

# def output_all_with6():
#     q = QueenProblem(6)
#     b = Backtrack(q)
#     if b.attempt(0):
#         q.displayBoard()
#     q.initValues = q.rowPos
#     q.reset()
#     if b.attempt(0):
#         q.displayBoard()
