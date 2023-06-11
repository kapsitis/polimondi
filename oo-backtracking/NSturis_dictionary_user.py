from NSturis import *

from NSturis_dictionary_creator import *

import copy

import time


class NSturisDictionaryUserProblem(NSturisProblem):

    def __init__(self, n, tail_length = 0): 
        if tail_length == 0:
            self.tail_length = round(n/3)
        else:
            self.tail_length = tail_length

        super(NSturisDictionaryUserProblem, self).__init__(n)
        self.n = n
        self.solution_count

        q = NSturisDictionaryCreator(self.tail_length)
        self.move_dict = q.getMoveDictionary()
        # self.prettyPrintDictionary()

    def prettyPrintDictionary(self):
        total = 0
        is_first = True
        for kkk in sorted(self.move_dict.keys()):
            vvv = self.move_dict[kkk]
            if is_first:
                print('{', end='')
            else:
                print(',')
            vvv.sort()
            total += len(vvv)
            print('PointTg({},{},{}):{}'.format(kkk.x, kkk.y, kkk.z, vvv), end='')
            is_first = False
        print('}')
        print('# {} tails inserted in dictionary'.format(total))
        print('\n')
 

    def undo(self, level, move):
        if isinstance(move, str):
            super(NSturisDictionaryUserProblem, self).undo(level, move)
        else: 
            LL = len(move)
            for i in range(LL):
                super(NSturisDictionaryUserProblem, self).undo(level-i, move[LL - i - 1])


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
                # Impossible branch - "directions" must be nonempty when lists of moves are inserted
                return True
            else: 
                last_direction = self.directions[-1]
                if move[0] in PointTg.FORBIDDEN_AFTER[last_direction]:
                    return False
                else:
                    currPoint = self.vertices[-1]
                    for dir, sidelen in zip(move, range(self.tail_length,0,-1)):
                        for i in range(sidelen):
                            currPoint = currPoint + DIRECTIONS[dir]
                            if currPoint in self.points:
                                return False
                    return True


    # Pievienojam esošo gājienu
    def record(self, level, move):
        if isinstance(move, str):
            self.directions.append(move)
            self.setPosition(move, 1)
        else:
            i = 0
            for mm in move:
                self.record(level, mm)
                i += 1


    def done(self, level):
        if level == self.N - self.tail_length:
            # print("IS DONE (leve = {}, self.N = {}, self.tail_length = {})".format(level, self.N, self.tail_length))
            self.solution_count += 1
            return True
        else:
            return False


    def moves(self, level):
        if level == 0:
            direction = '0'
            return PointTg.NEXT_MOVES[direction]
        elif level == 1:
            direction = '1'
            return PointTg.NEXT_MOVES[direction]
        elif level < self.n - self.tail_length:
            direction = self.directions[level-1]
            return PointTg.NEXT_MOVES[direction]

        elif level == self.n - self.tail_length:
            opposite = (-1)*self.vertices[-1]
            if opposite in self.move_dict:
                return self.move_dict[opposite]
            else:
                return []
                

def findAllSolutions(n, m):
    q = NSturisDictionaryUserProblem(n, m)
    b = Backtrackk(q)
    if b.attempt(0):
        q.display('file')
        
    print('{} positions found'.format(q.solution_count))


if __name__ == '__main__':

    start_time = time.time()

    if len(sys.argv) <= 1:
        print('Usage: python NSturis_dictionary_user.py <odd-number> [<tail-length>]')
        exit(0)
    n = int(sys.argv[1])
    if len(sys.argv) == 2:
        tail_length = round(n/3)
        findAllSolutions(n, tail_length)
    else:
        tail_length = int(sys.argv[2])
        findAllSolutions(n, tail_length)

    end_time = time.time()
    print('---{}: {:.3f} seconds ---'.format(n, end_time - start_time))




    
