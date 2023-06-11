import math
import itertools
import sys

from backtrackk import *
from point_tg import *

class NSturisProblem:



    def __init__(self, n):
        self.N = n
        self.directions = []

        # Record the min/max area; and the min/max count of acute angles 
        self.minArea = n**4
        self.maxArea = 0
        self.minAcute = n
        self.maxAcute = 0
        self.updateExtremes = False

        self.outfile = open("../konstrukcijas/editing_distance/acute_{}.txt".format(n), "w")

        # Uzkrāj polimonda virsotnes
        self.vertices = [PointTg(0, 0, 0)]
        # Punkti, kurus šķērso polimonda perimetrs.
        self.points = set()
        # aritmētisko progresiju summas. Ja n == 5, tad  series_sums = [0, 1, 3, 6, 10, 15]
        self.series_sums  = list(itertools.accumulate(range(0, n+1)))
        # līdz šim atrasto atrisinājumu skaits
        self.solution_count = 0


    # def reset(self):
    #     self.directions = []
    #     self.vertices = [PointTg(0, 0, 0)]
    #     self.points = set()

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
        self.setPosition(move, 1)


    # Parāpjamies atpakaļ, ja apakškokā zem šī gājiena visur bija strupceļš.
    def undo(self, level, move):
        move = self.directions.pop()
        self.setPosition(move, 0)
        # pārejot uz citu apakškoku, "initValues" vērtības nepielieto, bet sāk no 0.
        # self.initValues = []

    # Kompakti izvada vienu atrisinājumu kā daudzstūri, ja polimonada zīmēšana pabeigta: done(self,level)==True
    def display(self, format='file'):
        if self.updateExtremes:
            polyiamond_area = PointTg.get_signed_area(self.directions)
            (a60, a120, a240, a300) = PointTg.count_angles(self.directions)
            if self.maxArea < abs(polyiamond_area):
                self.maxArea = abs(polyiamond_area)
            if self.minArea > abs(polyiamond_area):
                self.minArea = abs(polyiamond_area)
            if self.minAcute > a60 + a300:
                self.minAcute = a60 + a300
            if self.maxAcute < a60 + a300:
                self.maxAcute = a60 + a300 

            if format == 'letters':
                print(self.directions, end='')
                print(', #S = {}, acute={}, obtuse={}'.format(polyiamond_area, a60+a300, a120+a240))
            elif format == 'dekarta':
                print(PointTg.convert_divainas_dekarta(self.directions), end='')
                print(', #S = {}, acute={}, obtuse={}'.format(polyiamond_area, a60+a300, a120+a240))
            else:
                # silent mode
                return
        else: 
            if format == 'letters':
                print(self.directions)
            elif format == 'dekarta':
                print(PointTg.convert_divainas_dekarta(self.directions))
            elif format == 'file':
                self.outfile.write("".join(self.directions))
                self.outfile.write("\n")

            else:
                # silent mode
                return            


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


 

def findFirstSolution(n):
    q = NSturisProblem(n)
    b = Backtrackk(q)
    if b.attempt(0):
        q.display('file')

def findAllSolutions(n):
    q = NSturisProblem(n)
    b = Backtrackk(q)
    n = 0
    while b.attempt(0):
        # q.display() 
        # q.reset()
        n += 1
    print('{} solutions found'.format(q.solution_count))
    print('Area is in [{},{}]'.format(q.minArea, q.maxArea))
    print('Acute angles in [{}, {}]'.format(q.minAcute, q.maxAcute))
    q.outfile.close()

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print('Usage: python NSturis.py <n1> <n2')
        exit(0)
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    for n in range(n1,n2):
        if n % 2 == 1:
            findAllSolutions(n)

