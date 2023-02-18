from point_tg import *

import sys
import time
import math
import copy

from backtrack import *

DIRECTIONS = {'A': PointTg(1, 0, -1), 'B': PointTg(1, -1, 0), 'C': PointTg(0, -1, 1),
              'D': PointTg(-1, 0, 1), 'E': PointTg(-1, 1, 0), 'F': PointTg(0, 1, -1)}

class NSturisDictionaryCreator:
    # Malu skaits augoša garuma virknē (1,2,...,N)
    N = 5

    # Saraksts ar debesspusēm (A,B,C,D,E,F), kas atbilst garumiem (1,2,...,N)
    directions = []

    # Polimonda virsotnes PointTg koordinātēs, kuras ir jau atrastas,
    vertices = []

    # PointTg kopa - punkti, kuriem cauri iet polimonda perimetrs.
    # points = set()
    points = []

    # Ja meklē visus atrisinājumus - kuras ir sākumvērtības.
    initValues = []

    def __init__(self, n):
        self.N = n
        self.directions = []
        self.vertices = [PointTg(0, 0, 0)]
        #self.points = set()
        #self.points.add(PointTg(0,0,0))
        self.points = [PointTg(0,0,0)]

        self.initValues = []


    def reset(self):
        self.directions = []
        self.vertices = [PointTg(0, 0, 0)]
        #self.points = set()
        #self.points.add(PointTg(0,0,0))
        self.points = [PointTg(0,0,0)]


    # Ja ir atrasts iepriekšējais derīgais polimonds - gājienu virknīte ar debesspusēm
    # (piemēram, ['A', 'C', 'D', 'E', 'F', 'B', 'F']), tad šajā funkcijā atrod skaitļu virknīti
    # (skaitļi no 0 līdz 3), kas parāda, kura no izvēlēm bija katrs burts. Šajā gadījumā tā
    # virknīte ir [0, 0, 0, 2, 3, 1, 3].
    # Pirmais gājiens (A) pārvēršas par 0, jo braukt pirmajā gājienā pa labi ir vienīgā iespēja.
    # Otrais gājiens (C) arī pārvēršas par 0, jo braukt otrajā gājienā uz ziemeļrietumiem
    # ir pirmā iespēja (savukārt gājiens B pārvērstos par 1) utt.
    # Tas, ko atrod "find_indices()" ir būtiski atkarīgs no gājienu sakārtojuma (masīvs NEXT_MOVES).
    def find_indices(self):
        result = []
        for i in range(0, self.N):
            if i == 0:
                result.append(PointTg.NEXT_MOVES_DICT['0'].index(self.directions[i]))
            else:
                result.append(PointTg.NEXT_MOVES_DICT[self.directions[i-1]].index(self.directions[i]))
        return result


    # Funkcija, lai ielūkotos backtracking objekta iekšējā stāvoklī
    def debug_state(self, prefix):
        print('{}, directions = {}, initValues = {}'.format(prefix, self.directions, self.initValues))

    def debug_full(self, prefix):
        print('{}: directions={}, vertices={}, points={}, initValues={}'.format(prefix, self.directions, self.vertices, self.points, self.initValues))


    # Pielabo datu struktūras, pievienojot vai atceļot gājienu.
    # status = 0 (ja atceļ malu ar "undo"), status = 1 (ja pievieno malu ar "record").
    def setPosition(self, move, status):
        sideLength = len(self.directions)
        if status == 1:
            nextSide = sideLength*DIRECTIONS[move]
            nextVertex = self.vertices[-1] + nextSide
            for i in range(1, sideLength+1):
                currPoint = self.vertices[-1] + i*DIRECTIONS[move]
                self.points.append(currPoint)
            self.vertices.append(nextVertex)

        if status == 0:
            prevVertext = self.vertices.pop()
            for i in range(0, sideLength + 1):
                currPoint = prevVertext - i*DIRECTIONS[move]
                self.points.remove(currPoint)


    # Vai nekrustojas ar agrākām malām
    def check1(self, level, move):
        for i in range(1, level + 2):
            currPoint = self.vertices[-1] + i * DIRECTIONS[move]
            if currPoint in self.points:
                return False
        return True

    # Vai var novilkt malu norādītajā virzienā?
    def valid(self, level, move):
        c1 = self.check1(level, move)
        #if not c1:
        #    self.debug_full("#### VALID(level={}, move={}) = {}".format(level, move, c1))
        return c1

    # Vai polimonda līnija pabeigta?
    def done(self, level):
        return level >= self.N - 1

    # Pievienojam esošo gājienu
    def record(self, level, move):
        # self.debug_full("RECORD(level={}, move={})".format(level, move))
        self.directions.append(move)
        self.setPosition(move, 1)


    # Parāpjamies atpakaļ, ja apakškokā zem šī gājiena visur bija strupceļš.
    def undo(self, level, move):
        move = self.directions.pop()
        self.setPosition(move, 0)
        # Ja pie tam izrādās, ka "initValues" nav tukšs, to nomet uz [], lai turpmāk sevi neierobežotu
        self.initValues = []



    # Atgriež iteratoru ar iespējamiem gājieniem, ja iepriekšējās malas virziens bija "direction"
    # Ja direction=='0', tad drīkst braukt tikai pa labi.
    # Ja direction=='1', tad drīkst pagriezties pa kreisi šaurā 60 grādu leņķī ('C') vai 120 grādu leņķī ('B')
    # Visos citos gadījumos nākamie gājieni ir četri (nevar sakrist ar "direction" vai tam pretējo).
    def moves(self, level):
        if level == 0:
            direction = '0'
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

    def display(self):
        print("{}: {}".format(self.vertices[-1], self.directions))


    def getMoveDictionary(self):
        the_dict = dict()
        # q = NSturisDictionaryCreator(n)
        b = Backtrack(self)
        n = 0
        while b.attempt(0):
            # self.display()

            the_key = self.vertices[-1]
            the_val = self.directions
            if the_key in the_dict.keys():
                the_val2 = copy.copy(the_val)
                the_val2.reverse()
                the_dict[the_key].append(the_val2)
                # the_dict[the_key].append("".join(the_val))
            else:
                the_val2 = copy.copy(the_val)
                the_val2.reverse()
                the_dict[the_key] = [the_val2]
                # the_dict[the_key] = ["".join(the_val)]
            self.initValues = self.find_indices()
            self.reset()
            n += 1
        print('{} positions found'.format(n))
        return the_dict


class MoveEnumeration:
    cursor = 0
    end = 0

    # Konstruktors: iterators sāksies ar vērtību "initial" un beidzas ar max-1.
    def __init__(self, initial, direction):
        self.next_moves = PointTg.NEXT_MOVES_DICT[direction]
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

    # izdrukā visas atlikušās vērtības iteratorā
    def debug_full(self, message):
        values = '[^'
        for i in range(self.cursor+1, self.end):
            values = values + self.next_moves[i]
            if i < self.end - 1:
                values = values + ","
        values = values + ']'
        print('{}: {}'.format(message, values))





def findFirstSolution(n):
    q = NSturisDictionaryCreator(n)
    b = Backtrack(q)
    if b.attempt(0):
        q.display()

def storeMoveDictionary(n):
    q = NSturisDictionaryCreator(n)
    the_dict = q.getMoveDictionary()
    with open("dict_stuff3.py", 'w') as f:
        f.write('from point_tg import *\n\n')
        f.write('dictionary = {\n')
        is_first = True
        for kkk, vvv in the_dict.items():
            if not is_first:
                f.write(',\n')
            vvv.sort()
            f.write('PointTg({},{},{}):{}'.format(kkk.x, kkk.y, kkk.z, vvv))
            is_first = False
        f.write('}\n\n')
        f.write('print(len(dictionary.keys()))\n')



def main():
    storeMoveDictionary(3)

if __name__ == '__main__':
    main()
