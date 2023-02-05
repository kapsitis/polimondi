from NSturis import *

from NSturis_dictionary_creator import *

import copy

class NSturisDictionaryUserProblem(NSturisProblem):
    def __init__(self, n): 
        super(NSturisDictionaryUserProblem, self).__init__(n)
        self.n = n
        self.halfsize = n // 2
        self.dictionaryPointer = 0

        q = NSturisDictionaryCreator(self.halfsize)
        self.move_dict = q.getMoveDictionary()
        # print(self.move_dict)
        is_first = True
        #for kkk, vvv in self.move_dict.items():
        #all_keys = copy.copy(self.move_dict.keys())
        #all_keys.sort()
        for kkk in sorted(self.move_dict.keys()):
            vvv = self.move_dict[kkk]
            if not is_first:
                print(',')
            vvv.sort()
            print('PointTg({},{},{}):{}'.format(kkk.x, kkk.y, kkk.z, vvv), end='')
            is_first = False
        print('}\n')


    # Pārveido debespušu kodējumu (piemēram, directions = ['A', 'C', 'D', 'E', 'F', 'B', 'F']),
    # par indeksiem, kuri rāda, kura izvēle bija attiecīgais burts (piemēram, [0, 0, 0, 2, 3, 1, 3]).
    # Tas, ko atrod "find_indices()" ir būtiski atkarīgs no gājienu sakārtojuma (masīvs NEXT_MOVES).
    def find_indices(self):
        print("FIND_INDICES!!!")
        result = []
        for i in range(0, self.N - self.halfsize):
            if i == 0:
                result.append(NEXT_MOVES['0'].index(self.directions[i]))
            elif i == 1:
                result.append(NEXT_MOVES['1'].index(self.directions[i]))
            else:
                result.append(NEXT_MOVES[self.directions[i-1]].index(self.directions[i]))
        return result


    def undo(self, level, move):
        super(NSturisDictionaryUserProblem, self).undo()
        self.dictionaryPointer = 0


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
        if isinstance(move, str):
            c1 = self.check1(level, move)
            c2 = self.check2(level, move)
            c3 = self.check3(level, move)
            return c1 and c2 and c3
        else:
            if level == 0:
                return True
            else: 
                last_direction = self.directions[-1]
                if move[0] in PointTg.FORBIDDEN_AFTER[last_direction]:
                    return False
                else: 
                    return True


    # Pievienojam esošo gājienu
    def record(self, level, move):
        if isinstance(move, str):
            self.directions.append(move)
            # print("USER.RECORD() at level {} add move {} to state {}".format(level, move, self.directions))
            print('In RECORD({},{},{}) InitValues = {}'.format(level, move, self.directions, self.initValues))
            self.setPosition(move, 1)
        else:
            print("...RECORD LIST ({},{})".format(level, move))
            i = 0
            for mm in move:
                self.record(level, mm)
                i += 1


    # Izvada risinājumu kompaktā formā
    def display(self):
        print(self.directions)

    def done(self, level):
        isDone = level >= self.N - self.halfsize
        if isDone:
            print("IS DONE (leve = {}, self.N = {}, self.halfsize = {})".format(level, self.N, self.halfsize))

        # return level >= self.N - self.halfsize
        return isDone


    def moves(self, level):
        if level == 0:
            direction = '0'
            return NEXT_MOVES[direction]
        elif level == 1:
            direction = '1'
            return NEXT_MOVES[direction]
        elif level < self.n - self.halfsize:
            direction = self.directions[level-1]
            if len(self.initValues) <= level:
                return NEXT_MOVES[direction]
            else:
                return NEXT_MOVES[direction][self.initValues[level]:]
        elif level == self.n - self.halfsize:
            print("moves(level={}, directions={}, vertice={})".format(level, self.directions, self.vertices[-1]))
            opposite = (-1)*self.vertices[-1]
            if opposite in self.move_dict and len(self.initValues) <= level:
                print("  move_dict({}) = {}".format(opposite, self.move_dict[opposite]))
                return self.move_dict[opposite]
            elif opposite in self.move_dict: 
                print("  move_dict({}) = {}".format(opposite, self.move_dict[opposite]))
                return self.move_dict[opposite][self.initValues[level]+1:]
            else:
                print("  move_dict({})=[]".format(opposite))
                return []
                # return self.move_dict[self.vertices[-1]]


        

def findAllSolutions(n):
    q = NSturisDictionaryUserProblem(n)
    b = Backtrack(q)
    n = 0
    while b.attempt(0):
        q.display()
        q.initValues = q.find_indices()
        q.reset()
        n += 1
    print('{} positions found'.format(n))
    print('halfsize is {}'.format(q.halfsize))


def main():
    findAllSolutions(5)


if __name__ == '__main__':
    main()


    
