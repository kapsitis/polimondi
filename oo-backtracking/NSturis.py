import math
import itertools

from backtrackk import *
from point_tg import *

class NSturisProblem:

    def __init__(self, n):
        self.N = n
        self.directions = []
        # Uzkrāj polimonda virsotnes
        self.vertices = [PointTg(0, 0, 0)]
        # Punkti, kurus šķērso polimonda perimetrs.
        self.points = set()
        # aritmētisko progresiju summas. Ja n == 5, tad  series_sums = [0, 1, 3, 6, 10, 15]
        self.series_sums  = list(itertools.accumulate(range(0, n+1)))
        # līdz šim atrasto atrisinājumu skaits
        self.solution_count = 0


    def reset(self):
        self.directions = []
        self.vertices = [PointTg(0, 0, 0)]
        self.points = set()

    # Funkcijas, lai ielūkotos backtracking objekta iekšējā stāvoklī
    def debug_state(self, prefix):
        print('{}, directions = {}'.format(prefix, self.directions))

    def debug_full(self, prefix):
        print('{}: directions={}, vertices={}, points={}'.format(prefix, self.directions, self.vertices))


    # Pielabo datu struktūras, pievienojot (status=1) vai atceļot (status=0) gājienu.
    def setPosition(self, move, status):
        sideLength = self.N - len(self.directions) + 1

        if status == 1:
            nextSide = sideLength*DIRECTIONS[move]
            nextVertex = self.vertices[-1] + nextSide
            for i in range(1, sideLength+1):
                currPoint = self.vertices[-1] + i*DIRECTIONS[move]
                self.points.add(currPoint)
            self.vertices.append(nextVertex)

        if status == 0:
            prevVertext = self.vertices.pop()
            for i in range(0, sideLength - 1):
                currPoint = prevVertext - i*DIRECTIONS[move]
                self.points.remove(currPoint)


    # Vai nekrustojas ar agrāk novilktām malām
    def check1(self, level, move):
        for i in range(1, self.N - level + 1):
            currPoint = self.vertices[-1] + i * DIRECTIONS[move]
            if currPoint in self.points:
                return False
        return True

    # Vai pietiek atlikušo malu garumu, lai atgrieztos
    def check2(self, level, move):
        nextSide = (self.N - level) * DIRECTIONS[move]
        nextVertex = self.vertices[-1] + nextSide
        return nextVertex.abs() <= self.series_sums[self.N - level - 1]

    # Pēdējā/īsākā polimonda mala nedrīkst būt horizontāla, jo pirmā ir horizontāls.
    def check3(self, level, move):
        if level == self.N - 1 and (move == 'A' or move == 'D'):
            return False
        return True

    # Vai drīkst vilkt malu norādītajā virzienā?
    def valid(self, level, move):
        c1 = self.check1(level, move)
        c2 = self.check2(level, move)
        c3 = self.check3(level, move)
        return c1 and c2 and c3

    # Vai polimonds ir pabeigts?
    def done(self, level):
        if level == self.N - 1:
            self.solution_count += 1
            return True
        else:
            return False

    # Pievienojam esošo gājienu
    def record(self, level, move):
        self.directions.append(move)
        #print('RECORD() at level {} add move {} to state {}'.format(level, move, self.directions))
        self.setPosition(move, 1)


    # Parāpjamies atpakaļ, ja apakškokā zem šī gājiena visur bija strupceļš.
    def undo(self, level, move):
        move = self.directions.pop()
        self.setPosition(move, 0)
        # pārejot uz citu apakškoku, "initValues" vērtības nepielieto, bet sāk no 0.
        # self.initValues = []

    # Kompakti izvada vienu risinājumu, ja polimonada zīmēšana pabeigta: done(self,level)==True
    def display(self):
        print(self.directions, end='')
        print(', #S = {}'.format(self.get_signed_area()))

    def get_joc_koord(self):
        result = []
        side_length = self.N
        for item in self.directions:
            if item == 'A':
                result.append([0, side_length])
            elif item == 'B':
                result.append([side_length, 0.5*side_length])
            elif item == 'C':
                result.append([side_length, -0.5*side_length])
            elif item == 'D':
                result.append([0, -side_length])
            elif item == 'E':
                result.append([-side_length, -0.5*side_length])
            else:
                result.append([-side_length, 0.5*side_length])
            side_length -= 1
        return result

    # Atgriež iteratoru ar iespējamiem gājieniem, ja iepriekšējās malas virziens bija "direction"
    # Ja direction=='0', tad drīkst braukt tikai pa labi.
    # Ja direction=='1', tad drīkst pagriezties pa kreisi šaurā 60 grādu leņķī ('C') vai 120 grādu leņķī ('B')
    # Visos citos gadījumos nākamie gājieni ir četri (nevar sakrist ar "direction" vai tam pretējo).
    def moves(self, level):
        if level == 0:
            direction = '0'
        elif level == 1:
            direction = '1'
        else:
            direction = self.directions[level-1]

        return PointTg.NEXT_MOVES[direction]


    def get_signed_area(self):
        unit_triangle_height = math.sqrt(3)/2
        unit_triangle_area = math.sqrt(3)/4
        joc_koord = self.get_joc_koord()

        # Summē malu vektoriņus, aprēķina virsotnes jocīgajās koordinātēs (sākas un beidzas ar [0;0])
        partial_sums = [[0,0]]
        for i in range(0, self.N):
            new_pair = [partial_sums[-1][0] + joc_koord[i][0], partial_sums[-1][1] + joc_koord[i][1]]
            partial_sums.append(new_pair)

        # Pārveido jocīgās koordinātes Dekarta koordinātēs (pareizina y ar trijstūra augstumu)
        dekartaXY = [[unit_triangle_height*y, x] for [y,x] in partial_sums]
        summa = 0
        for i in range(0, self.N - 1):
            summa += dekartaXY[i][1]*dekartaXY[i+1][0] - dekartaXY[i][0]*dekartaXY[i+1][1]
        summa += dekartaXY[self.N-1][1]*dekartaXY[0][0] - dekartaXY[self.N-1][0]*dekartaXY[0][1]
        # summa/2 ir laukums 1*1 kvadrātiņu vienībās; pārveido to mazo trijstūrīšu vienībās.
        result = (summa/2)/unit_triangle_area
        return int(round(result))
 

def findFirstSolution(n):
    q = NSturisProblem(n)
    b = Backtrack(q)
    if b.attempt(0):
        q.display()

def findAllSolutions(n):
    q = NSturisProblem(n)
    b = Backtrack(q)
    n = 0
    while b.attempt(0):
        # q.display() 
        q.reset()
        n += 1
    print('{} solutions found'.format(q.solution_count))

# This is not finished - will not work for findFirstPlacement(...)
def main():
    findAllSolutions(17)


if __name__ == '__main__':
    main()
