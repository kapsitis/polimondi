# -*- coding: utf-8 -*-

import sys
import time

from backtrack import *

class PointTg:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.z)

    # Ar šo funkciju var pieskaitīt pašreizējam punktam izmaiņu "delta" (jauno malu)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return PointTg(x, y, z)

    # Reizina vektoru ar skaitli (skaitlim jābūt rakstītam pa kreisi no vektora)
    def __rmul__(self, other):
        return PointTg(other*self.x, other*self.y, other*self.z)

    # Atgriež trijstūru režģī novilktas malas garumu (ja paralēla režģa līnijām)
    # Vai nu arī - īsāko ceļu no PointTg virsotnes līdz sākumpunktam (ejot pa trijstūrīšu līnijām)
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

# Secība, kādā pārbaudīt nākamos gājienus.
NEXT_MOVES = {'A': ['C', 'B', 'E', 'F'], 'B': ['D', 'C', 'A', 'F'], 'C': ['D', 'B', 'A', 'E'],
              'D': ['C', 'B', 'E', 'F'], 'E': ['D', 'C', 'A', 'F'], 'F': ['D', 'B', 'A', 'E']}

class NSturisProblem:
    # Polimonda malu skaits
    N = 5

    # Saraksts ar debesspusēm (A,B,C,D,E,F) - tā būs izvadāmā atbilde
    directions = []

    # Polimonda virsotnes PointTg koordinātēs, kuras ir atrastas,
    # lai no pareizās vietas zīmētu tālāk, vai parāptos atpakaļ
    vertices = []

    # PointTg kopa - punkti, kuriem cauri iet polimonda perimetrs.
    points = set()

    # Līdz kurai vietai ir nonākts katrā no virsotnēm
    initValues = []

    # aritmētisko progresiju summas
    series_sums = []

    def __init__(self, n):
        self.N = n
        self.directions = []
        self.vertices = [PointTg(0, 0, 0)]
        self.points = set()
        self.initValues = []
        series_sums = []
        partial_sum = 0
        for i in range(1, n+1):
            partial_sum += i
            series_sums.append(partial_sum)


    def reset(self):
        self.directions = []
        self.vertices = []
        self.points = set()

    # Funkcija, lai ielūkotos backtracking objekta iekšējā stāvoklī
    def debugState(self, prefix):
        print('{}: directions={}, vertices={}, points={}'.format(prefix, self.directions, self.vertices, self.points))

    # Pielabo datu struktūras, pievienojot vai atceļot gājienu.
    # status = 0 (ja atceļ malu ar "undo"), status = 1 (ja pievieno malu ar "record").
    def setPosition(self, move, status):
        sideLength = self.N - len(self.directions)
        if status == 1:
            nextSide = sideLength*DIRECTIONS[move]
            nextVertex = self.vertices[-1] + nextSide
            self.vertices.append(nextVertex)
            for i in range(0, sideLength):
                currPoint = self.vertices[-1] + i*DIRECTIONS[move]
                self.points.add(currPoint)
        if status == 0:
            prevVertext = self.vertices.pop()
            for i in range(0, sideLength):
                currPoint = prevVertext + i*DIRECTIONS[move]
                self.points.remove(currPoint)


    # Vai var novilkt malu norādītajā virzienā?
    def valid(self, level, move):
        # does the move lead to a place we can return?
        nextSide = (self.N - level) * DIRECTIONS[move]
        nextVertex = self.vertices[-1] + nextSide
        if nextVertex.abs() > self.series_sums[self.N - level - 1]:
            return False
        for i in range(1, self.N - level + 1):
            currPoint = self.vertices[-1] + i * DIRECTIONS[move]
            if currPoint in self.points:
                return False
        return True

    # Vai polimonda līnija pabeigta?
    def done(self, level):
        return level >= self.N - 1

    # Pievienojam esošo gājienu
    def record(self, level, move):
        self.directions.append(move)
        self.setPosition(move, 1)

    # Parāpjamies atpakaļ, ja apakškokā zem šī gājiena visur bija strupceļš
    def undo(self, level, move):
        move = self.directions.pop()
        self.setPosition(move, 0)


    # Izvada risinājumu kompaktā formā
    def display(self):
        print('directions={}'.format(self.directions))


    # Atgriež iteratoru ar iespējamiem gājieniem, ja iepriekšējās malas virziens bija "direction"
    def moves(self, level, direction):
        if len(self.initValues) <= level:
            return MoveEnumeration(0, direction)
        elif level < self.N-1:
            return MoveEnumeration(self.initValues[level], direction)
        else:
            return MoveEnumeration(self.initValues[level]+1, direction)


# Iterators, kurš ģenerē iespējamos dāmu novietojumus kārtējā kolonnā
class MoveEnumeration:
    cursor = 0
    end = 0

    # Konstruktors: iterators sāksies ar vērtību "initial" un beidzas ar max-1.
    def __init__(self, initial, direction):
        self.cursor = initial - 1
        self.end = 4
        self.next_moves = NEXT_MOVES[direction]

    # Sagatavo iteratoru "for" cikla pašā sākumā un atgriež to
    def __iter__(self):
        return self

    # atgriež tekošo vērtību intervālā [initial; max-1]. Ja beidzas, tad izlec no cikla ar "StopIteration"
    def __next__(self):
        self.cursor += 1
        if self.cursor < self.end:
            return self.next_moves[self.cursor]
        raise StopIteration


def findFirstPlacement(n):
    q = NSturisProblem(n)
    b = Backtrack(q)
    if b.attempt(0):
        q.display()


# This is not finished - will not work for findFirstPlacement(...)
def main():
    #findFirstPlacement(7)
    dd = DIRECTIONS['A']
    nextSide = 13 * dd
    print('nextSide = {}'.format(nextSide))


if __name__ == '__main__':
    main()
