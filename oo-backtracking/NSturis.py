# -*- coding: utf-8 -*-

import sys
import time
import math

from backtrack import *

class PointTg:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.z)

    def __repr__(self):
        return "({},{},{})".format(self.x, self.y, self.z)

    # Ar šo funkciju var pieskaitīt pašreizējam punktam izmaiņu "delta" (jauno malu)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return PointTg(x, y, z)

    # Ar šo funkciju var pieskaitīt pašreizējam punktam izmaiņu "delta" (jauno malu)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return PointTg(x, y, z)


    # Reizina vektoru ar skaitli (skaitlim jābūt rakstītam pa kreisi no vektora)
    def __rmul__(self, other):
        return PointTg(other*self.x, other*self.y, other*self.z)

    # Atgriež īsāko attālumu līdz (0,0,0), ejot pa trijstūru režģa līnijām
    def abs(self):
        return int(max(abs(self.x), abs(self.y), abs(self.z)))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __ne__(self, other):
        return not self.__eq__(other)

DIRECTIONS = {'A': PointTg(1,0,-1), 'B': PointTg(1,-1,0), 'C': PointTg(0,-1,1),
              'D': PointTg(-1,0,1), 'E': PointTg(-1,1,0),'F': PointTg(0,1,-1)}

DIRECTIONS_JOC_KOORD = {'A': [0, 1], 'B': [1, 0.5], 'C': [1, -0.5], 'D': [0, -1], 'E': [-1, -0.5], 'F': [-1, 0.5]}

# Secība, kādā pārbaudīt nākamos gājienus (kā definēts Martas zīmējumos)
NEXT_MOVES = {'0': ['A'], '1': ['C', 'B'],
    'A': ['C', 'B', 'E', 'F'], 'B': ['D', 'C', 'A', 'F'], 'C': ['D', 'B', 'A', 'E'],
    'D': ['C', 'B', 'E', 'F'], 'E': ['D', 'C', 'A', 'F'], 'F': ['D', 'B', 'A', 'E']}
# Secība, kādā pārbaudīt nākamos gājienus (alfabētiska)
#NEXT_MOVES = {'0': ['A'], '1': ['B', 'C'],
#    'A': ['B', 'C', 'E', 'F'], 'B': ['A', 'C', 'D', 'F'], 'C': ['A', 'B', 'D', 'E'],
#    'D': ['B', 'C', 'E', 'F'], 'E': ['A', 'C', 'D', 'F'], 'F': ['A', 'B', 'D', 'E']}


class NSturisProblem:
    # Polimonda malu skaits
    N = 5

    # Saraksts ar debesspusēm (A,B,C,D,E,F) - tā būs izvadāmā atbilde
    directions = []

    # Polimonda virsotnes PointTg koordinātēs, kuras atrastas līdz šim
    vertices = []

    # PointTg kopa - punkti, kuriem cauri iet polimonda perimetrs.
    points = set()
    # points = []

    # Meklējot nākamo risinājumu, atceras, no kuras vietas meklēt katrā līmenī.
    # Ja netiek izmantots, tad jābūt []; nedrīkst likt nulles (citādi var zaudēt atrisinājumus)
    initValues = []

    # aritmētisko progresiju summas. Ja n == 5, tad  series_sums = [0, 1, 3, 6, 10, 15]
    series_sums = []

    def __init__(self, n):
        self.N = n
        self.directions = []
        self.vertices = [PointTg(0, 0, 0)]
        self.points = set()
        # self.points = list()
        self.initValues = []
        self.series_sums = []
        partial_sum = 0
        for i in range(0, n+1):
            partial_sum += i
            self.series_sums.append(partial_sum)

    def reset(self):
        self.directions = []
        self.vertices = [PointTg(0, 0, 0)]
        self.points = set()
        # self.points = list()




    # Pārveido debespušu kodējumu (piemēram, directions = ['A', 'C', 'D', 'E', 'F', 'B', 'F']),
    # par indeksiem, kuri rāda, kura izvēle bija attiecīgais burts (piemēram, [0, 0, 0, 2, 3, 1, 3]).
    # Tas, ko atrod "find_indices()" ir būtiski atkarīgs no gājienu sakārtojuma (masīvs NEXT_MOVES).
    def find_indices(self):
        result = []
        for i in range(0, self.N):
            if i == 0:
                result.append(NEXT_MOVES['0'].index(self.directions[i]))
            elif i == 1:
                result.append(NEXT_MOVES['1'].index(self.directions[i]))
            else:
                result.append(NEXT_MOVES[self.directions[i-1]].index(self.directions[i]))
        return result


    # Funkcija, lai ielūkotos backtracking objekta iekšējā stāvoklī
    def debug_state(self, prefix):
        print('{}, directions = {}, initValues = {}'.format(prefix, self.directions, self.initValues))

    def debug_full(self, prefix):
        print('{}: directions={}, vertices={}, points={}'.format(prefix, self.directions, self.vertices, self.points))
        # print('{}: directions={}, vertices={}, points={}'.format(prefix, self.get_joc_koord(), self.vertices, self.points))


    # Pielabo datu struktūras, pievienojot (status=1) vai atceļot (status=0) gājienu.
    def setPosition(self, move, status):
        sideLength = self.N - len(self.directions) + 1

        if status == 1:
            nextSide = sideLength*DIRECTIONS[move]
            nextVertex = self.vertices[-1] + nextSide
            for i in range(1, sideLength+1):
                currPoint = self.vertices[-1] + i*DIRECTIONS[move]
                self.points.add(currPoint)
                # self.points.append(currPoint)
            self.vertices.append(nextVertex)

        if status == 0:
            prevVertext = self.vertices.pop()
            for i in range(0, sideLength - 1):
                currPoint = prevVertext - i*DIRECTIONS[move]
                self.points.remove(currPoint)


    # Vai nekrustojas ar agrākām malām
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

    def check3(self, level, move):
        if level == self.N - 1 and (move == 'A' or move == 'D'):
            return False
        return True

    # Vai var novilkt malu norādītajā virzienā?
    def valid(self, level, move):
        # print()
        c1 = self.check1(level, move)
        c2 = self.check2(level, move)
        c3 = self.check3(level, move)
        return c1 and c2 and c3

    # Vai polimonda līnija pabeigta?
    def done(self, level):
        return level >= self.N - 1

    # Pievienojam esošo gājienu
    def record(self, level, move):
        self.directions.append(move)
        self.setPosition(move, 1)


    # Parāpjamies atpakaļ, ja apakškokā zem šī gājiena visur bija strupceļš.
    def undo(self, level, move):
        move = self.directions.pop()
        self.setPosition(move, 0)
        # pārejot uz citu apakškoku, "initValues" vērtības nepielieto, bet sāk no 0.
        self.initValues = []

    # Izvada risinājumu kompaktā formā
    def display(self):
        # print('***********', end="")
        print(self.get_joc_koord(), end="")
        print(", #S = {}".format(self.get_signed_area()))

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

        # Ja initValues nav tukšs saraksts, tad šī gājienu ģenerēšanas funcija moves(self, level)
        # nepiedāvās tādus gājienus, kuri ir "pirms" jau atrastā labā polimonda (konkrētajā polimondu sakārtojumā).
        if len(self.initValues) <= level:
            return MoveEnumeration(0, direction)
        elif level < self.N-1:
            return MoveEnumeration(self.initValues[level], direction)
        # Ja moves(self, level) ģenerē iespējas pašam pēdējam gājienam (level == self.N - 1),
        # tad pat pieprasa, lai nākamais gājiens nesakristu ar initValues -
        # citādi algoritms atrastu visu laiku vienu un to pašu labo polimondu un netiktu uz priekšu
        else:
            return MoveEnumeration(self.initValues[level]+1, direction)


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



# Iterators, kurš ģenerē iespējamos dāmu novietojumus kārtējā kolonnā
class MoveEnumeration:
    cursor = 0
    end = 0

    # Konstruktors: iterators sāksies ar vērtību "initial" un beidzas ar max-1.
    def __init__(self, initial, direction):
        self.next_moves = NEXT_MOVES[direction]
        self.cursor = initial - 1
        self.end = len(self.next_moves)

    # Sagatavo iteratoru "for" cikla pašā sākumā un atgriež to
    def __iter__(self):
        return self

    # atgriež tekošo vērtību intervālā [initial; max-1]. Ja beidzas, tad izlec no cikla ar "StopIteration"
    def __next__(self):
        self.cursor += 1
        if self.cursor < self.end:
            return self.next_moves[self.cursor]
        raise StopIteration


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
        q.display()
        q.initValues = q.find_indices()
        q.reset()
        n += 1
    print('{} positions found'.format(n))

# This is not finished - will not work for findFirstPlacement(...)
def main():
    findAllSolutions(19)


if __name__ == '__main__':
    main()
