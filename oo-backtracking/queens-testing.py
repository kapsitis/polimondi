# import pytest

from backtrack import *
from queens import *

def test_board22_with_6_queens():
    expected = [0, 2, 4, 1, 3, 9, 13, 16, 19, 12, 18, 21, 17, 7, 20, 11, 8, 5, 15, 6, 10, 14]
    q = QueenProblem(22)
    q.record(0, 0)
    q.record(1, 2)
    q.record(2, 4)
    q.record(3, 1)
    q.record(4, 3)
    q.record(5, 9)
    b = Backtrack(q)
    if b.attempt(6):
        assert q.rowPos == expected

def test_board1():
    q = QueenProblem(1)
    b = Backtrack(q)
    if b.attempt(0):
        assert q.rowPos == [0]

def test_board4():
    q = QueenProblem(4)
    b = Backtrack(q)
    if b.attempt(0):
        assert q.rowPos == [1, 3, 0, 2]


def test_board5():
    q = QueenProblem(5)
    b = Backtrack(q)
    if b.attempt(0):
        assert q.rowPos == [0, 2, 4, 1, 3]

def test_board6():
    q = QueenProblem(6)
    b = Backtrack(q)
    if b.attempt(0):
        assert q.rowPos == [1, 3, 5, 0, 2, 4]

def test_board7():
    q = QueenProblem(7)
    b = Backtrack(q)
    if b.attempt(0):
        assert q.rowPos == [0, 2, 4, 6, 1, 3, 5]


def test_board8(): 
    expected = [0, 4, 7, 5, 2, 6, 1, 3]
    q = QueenProblem(8)
    b = Backtrack(q)
    if b.attempt(0):
        assert q.rowPos == expected

