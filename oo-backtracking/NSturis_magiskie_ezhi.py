from NSturis import *

import copy

import time

class NSturisMagiskieEzhiProblem(NSturisProblem):

    # Ierakstiet maksimālo atļauto plato leņķu skaitu (ieteicamās vērtības 0 vai 2)
    MAX_OBTUSE = 0

    def __init__(self, n): 
        super(NSturisMagiskieEzhiProblem, self).__init__(n)
        # plato leņķu skaitītājs
        self.total_obtuse = 0

    # Pārliecinās, vai netiek pārsniegts atļauto plato leņķu skaits
    def check4(self, level, move):
        if len(self.directions) == 0: 
            return True
        elif self.total_obtuse < self.MAX_OBTUSE:
            return True
        else: 
            result = PointTg.is_acute(self.directions[-1], move)
            return result

    def valid(self, level, move):
        c123 = super(NSturisMagiskieEzhiProblem, self).valid(level, move)
        c4 = self.check4(level, move)
        return c123 and c4

    # Pievienojam esošo gājienu
    def record(self, level, move):
        # pielabo plato leņku skaitītāju:
        if len(self.directions) > 0 and not PointTg.is_acute(self.directions[-1], move):
            self.total_obtuse += 1
        self.directions.append(move)
        self.setPosition(move, 1)



    # Parāpjamies atpakaļ, ja apakškokā zem šī gājiena visur bija strupceļš.
    def undo(self, level, move):
        move = self.directions.pop()
        self.setPosition(move, 0)
        # pielabo plato leņku skaitītāju:
        if len(self.directions) > 0 and not PointTg.is_acute(self.directions[-1], move):
            self.total_obtuse -= 1


def findAllSolutions(n):
    q = NSturisMagiskieEzhiProblem(n)
    b = Backtrackk(q)
    while b.attempt(0):
        pass
    print('{} solutions found'.format(q.solution_count))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Usage: python NSturis_magiskie_ezhi.py <odd-number>')
        exit(0)
    n = int(sys.argv[1])
    findAllSolutions(n)