# -*- coding: utf-8 -*-

# https://dl.acm.org/doi/pdf/10.1145/331795.331886
# https://realpython.com/python-interface/
# https://stackoverflow.com/questions/19151/how-to-build-a-basic-iterator

import sys
import time

from backtrack import *

# Mazliet izmainīts šaha dāmu algoritms - rindas un kolonnas numurētas, sākot ar 0.
class QueenProblem:
    # Galdiņa izmēru faktiski uzstāda __init__
    MAXROW = 0

    # Ja rowPos[x]==y  (y pieder [0;n-1]), tad x-tās kolonnas y-tajā rindiņā ir novietota dāma;
    # ja rowPos[x] neeksistē (jo stekā nav pietiekami vērtību), tad x-tajā kolonnā dāma vēl nav novietota.
    rowPos = []

    # Aizņemtās rindas. Ja row[x]==1, tad x-tajā rindā jau ir dāma.  Rindas numurē ar skaitļiem no [0; n-1]
    row = []

    # Aizņemtās diagonāles, kuras iet uz leju un pa kreisi. Ja leftDiag[x]==1, tad šajā diagonālē novietota dāma
    # Diagonāles skaitli iegūst, saskaitot rindiņu un kolonnu. Teiksim, dāma kreisajā augšējā stūrī (0,0) ir uz diagonāles 0+0=0.
    # Piemēram, 8*8 galdiņam masīva elementi ir leftDiag[0],...,leftDiag[14]
    leftDiag = []
    # Aizņemtās diagonāles, kuras iet uz leju un pa kreisi. Ja leftDiag[x]==1, tad šajā diagonālē novietota dāma
    # Diagonāles skaitli iegūst, atņemot no kolonnas rindiņu. Šaha galdiņam 8*8 šīs diagonāles ir -7, -6, ...., 6, 7.
    # Šim skaitlim vēl pieskaita (MAXROW-1), t.i. masīva elementi ir rightDiag[0], ... , rightDiag[14].
    rightDiag = []


    initValues = []




    # Izveido šaha galdiņu n*n; visas dāmu pozīcijas un visas apdraudētās pozīcijas sākotnēji ir False.
    # (Polimondiem - visi saraksti sākumā ir tukši)
    def __init__(self, n):
        self.MAXROW = n
        self.leftDiag = [0] * (2*self.MAXROW-1)
        self.rightDiag = [0] * (2*self.MAXROW-1)
        self.row = [0]*(self.MAXROW)
        self.rowPos = []
        self.initValues = []


    def reset(self):
        self.leftDiag = [0] * (2*self.MAXROW-1)
        self.rightDiag = [0] * (2*self.MAXROW-1)
        self.row = [0]*(self.MAXROW)
        self.rowPos = []



    # Funkcija, lai ielūkotos backtracking objekta iekšējā stāvoklī
    def debugState(self, prefix):
        #print('{}: rowPos={}, row={}, leftDiag={}, rightDiag={}'.format(prefix, self.rowPos, self.row, self.leftDiag, self.rightDiag))
        pass

    # Pielabo apdraudējumu datu struktūras pēc dāmas uzlikšanas/novākšanas
    def setPosition(self, rowNo, colNo, status):
        self.row[rowNo] = status
        self.leftDiag[rowNo+colNo] = status
        self.rightDiag[rowNo - colNo + self.MAXROW - 1] = status

    # Vai var dāmu uzlikt uz galdiņa?
    # "move" te nozīmē jaunas dāmas uzlikšanu.
    def valid(self, level, move):
        rowNo = move

        colNo = level
        # colNo = len(self.rowPos)

        # visiem apdraudējumiem jābūt 0
        result = (self.row[rowNo] == 0) and (self.leftDiag[rowNo + colNo] == 0) and (self.rightDiag[rowNo - colNo + self.MAXROW - 1] == 0)
        return result

    # Vai visas dāmas jau izvietotas (vai n-polimonds sekmīgi noslēdzis vienkāršo lauzto līniju)?
    def done(self, level):
        # return (level + 1 >= self.MAXROW)
        # return len(self.rowPos) == self.MAXROW
        # print ('IS DONE = {}, level = {}'.format(level >= self.MAXROW - 1, level))
        return level >= self.MAXROW - 1

    # Pievienojam esošo gājienu
    def record(self, level, move):
        rowNo = move

        colNo = level
        # colNo = len(self.rowPos)

        # self.rowPos[colNo] = rowNo
        self.rowPos.append(rowNo)
        self.setPosition(rowNo, colNo, 1)
        # Push a new item to the stack




    # Parāpjamies atpakaļ, ja bija sasniegts strupceļš
    def undo(self, level, move):
        rowNo = move
        # colNo = level
        #self.rowPos[colNo] = -1
        self.rowPos.pop()
        self.initValues = []

        colNo = len(self.rowPos)
        self.setPosition(rowNo, colNo, 0)


    # Izvada risinājumu kompaktā formā
    def display(self):
        print('rowPos={}'.format(self.rowPos))

    def displayBoard(self):
        level = len(self.rowPos)
        for i in range(0, self.MAXROW):
            for j in range(0, self.MAXROW):
                if j < level and self.rowPos[j] == i:
                    print("1", end=" ")
                else:
                    print("0", end=" ")
            print()


    # Atgriež iteratoru ar iespējamiem gājieniem:
    # Kārtējā kolonnā dāmu mēģina nolikt jebkurā rindiņā (1...n), algoritms pats izlaidīs apdraudētās pozīcijas.
    def moves(self, level):
        if len(self.initValues) <= level:
            # self.debugState("CCC, level={}, init={} ".format(level, 0))
            return QueenEnumeration(0, self.MAXROW)
        elif level < self.MAXROW-1:
            # self.debugState("DDD, level={}, init={} ".format(level, self.initValues[level]))
            return QueenEnumeration(self.initValues[level], self.MAXROW)
        else:
            # self.debugState("EEE, level={}, init={} ".format(level, self.initValues[level]+1))
            return QueenEnumeration(self.initValues[level]+1, self.MAXROW)


# Iterators, kurš ģenerē iespējamos dāmu novietojumus kārtējā kolonnā
class QueenEnumeration:
    cursor = 0
    end = 0

    # Konstruktors: iterators sāksies ar vērtību "initial" un beidzas ar max-1.
    def __init__(self, initial, max):
        self.cursor = initial - 1
        self.end = max

    # Sagatavo iteratoru "for" cikla pašā sākumā un atgriež to
    def __iter__(self):
        return self

    # atgriež tekošo vērtību intervālā [initial; max-1]. Ja beidzas, tad izlec no cikla ar "StopIteration"
    def __next__(self):
        self.cursor += 1
        if self.cursor < self.end:
            return self.cursor
        raise StopIteration


def findFirstPlacement(n):
    q = QueenProblem(n)
    b = Backtrack(q)
    if b.attempt(0):
        q.displayBoard()



def findAllPlacements(n):
    q = QueenProblem(n)
    b = Backtrack(q)
    n = 0
    while b.attempt(0):
        q.display()
        q.initValues = q.rowPos
        q.reset()
        n += 1
    print('{} positions found'.format(n))


def recordRunTimes(n1, n2):
    computation_times = dict()

    with open('computation_times4.txt', 'a') as file_object:
        file_object.write('N,milliseconds\n')

    for n in range(n1, n2+1):
        start_time = time.time()

        q = QueenProblem(n)
        b = Backtrack(q)
        if b.attempt(0):
            q.displayBoard()


        end_time = time.time()
        print('---{}: {:.3f} seconds ---'.format(n, end_time - start_time))
        computation_times[n] = round(1000*(end_time - start_time))
        with open('computation_times3.txt', 'a') as file_object:
            file_object.write("{},{}\n".format(n, computation_times[n]))




def main():
    if len(sys.argv) <= 2:
        print('Usage: python queens.py <n1> <n2>')
        exit(0)
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    recordRunTimes(n1, n2)




if __name__ == '__main__':
    main()
