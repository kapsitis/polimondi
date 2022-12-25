import sys
import time
import itertools
import copy

from backtrack import *

class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.z)

    def __repr__(self):
        return "({},{},{})".format(self.x, self.y, self.z)

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

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


# DIRECTIONS = {'X+': Point3D(1,0,0), 'X-': Point3D(-1,0,0),
#               'Y+': Point3D(0,1,0), 'Y-': Point3D(0,-1,0),
#               'Z+': Point3D(0,0,1), 'Z-': Point3D(0,0,-1)}

# An "empty" block, if some position in the Burr cross has to be left empty.
CROSS00 = [[0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0]]

# Block details
CROSS01 = [[3,3,3,3,1,2,0,1,3,3,3,3],
           [3,3,3,3,1,3,1,1,3,3,3,3]]
CROSS02 = [[3,3,3,3,1,0,1,1,3,3,3,3],
           [3,3,3,3,1,1,1,1,3,3,3,3]]
CROSS03 = [[3,3,3,3,1,1,0,1,3,3,3,3],
           [3,3,3,3,1,1,1,1,3,3,3,3]]
CROSS04 = [[3,3,3,3,1,1,0,1,3,3,3,3],
           [3,3,3,3,1,1,3,1,3,3,3,3]]
CROSS05 = [[3,3,3,3,1,1,1,1,3,3,3,3],
           [3,3,3,3,1,3,1,1,3,3,3,3]]
CROSS06 = [[3,3,3,3,1,1,1,1,3,3,3,3],
           [3,3,3,3,1,1,3,1,3,3,3,3]]


# One piece for the Burr cross of size 12x2x2.
class Block:
    arrays = []
    spacePoints = []

    # Mark the points involved.
    # Place the origin at the center of the Block.
    def __init__(self, arrays, letter, flip):
        # print('Creating Block({}, {}, {})'.format(arrays, letter, flip))
        self.spacePoints = []
        self.arrays = arrays
        for i in range(0, 2):
            for j in range(0, 12):
                if arrays[i][j] // 2 == 1:
                    self.spacePoints.append(Point3D(2*j-11, 2*i - 1, 1))
                if arrays[i][j] % 2 == 1:
                    self.spacePoints.append(Point3D(2*j-11, 2*i - 1, -1))
        # Need to start with a 180 degree turn around vertical Z axis
        if flip == 1:
            self.rotateZ(1)
            self.rotateZ(1)
        if letter == 'A':
            self.rotateX(1)
            self.translate(Point3D(0, -2, 0))
        elif letter == 'B':
            self.rotateX(-1)
            self.translate(Point3D(0, 2, 0))
        elif letter == 'C':
            self.rotateZ(-1)
            self.translate(Point3D(0, 0, -2))
        elif letter == 'D':
            self.rotateZ(-1)
            self.rotateY(1)
            self.rotateY(1)
            self.translate(Point3D(0, 0, 2))
        elif letter == 'E':
            self.rotateY(1)
            self.rotateZ(1)
            self.rotateZ(1)
            self.translate(Point3D(-2, 0, 0))
        elif letter == 'F':
            self.rotateY(1)
            self.translate(Point3D(2, 0, 0))


    # Rotate counter-clockwise (dir = +1) or clockwise (dir = -1) around X axis
    def rotateX(self, dir):
        self.spacePoints = [Point3D(p.x, dir*p.z, -dir*p.y) for p in self.spacePoints]

    # Rotate counter-clockwise (dir = +1) or clockwise (dir = -1) around Y axis
    def rotateY(self, dir):
        self.spacePoints = [Point3D(-dir*p.z, p.y, dir*p.x) for p in self.spacePoints]

    # Rotate counter-clockwise (dir = +1) or clockwise (dir = -1) around Z axis
    def rotateZ(self, dir):
        self.spacePoints = [Point3D(dir*p.y, -dir*p.x, p.z) for p in self.spacePoints]

    def translate(self, vect):
        self.spacePoints = [p + vect for p in self.spacePoints]

    def contains(self, pt):
        return pt in self.spacePoints



# https://johnrausch.com/PuzzlingWorld/chap05.htm
class BurrCrossProblem:

#    initMap = {'A': (CROSS01, 0), 'B': (CROSS02, 0), 'C': (CROSS03, 0),
#               'D': (CROSS04, 0), 'E': (CROSS05, 0), 'F': (CROSS06, 0), }

    perm = ('A', 'B', 'C', 'D', 'E', 'F')
    flips = (0, 0, 0, 0, 0, 0)
    moves = []
    offsets = dict()
    blocks = dict()


    # for each block store which points are taken
    # spacePoints = dict()

    def __init__(self, perm, flips, crosses):
        self.perm = perm
        self.flips = flips
        self.moves = []
        self.offsets = dict()
        self.blocks = dict()
        self.prev_hashes = set()

        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        for i in range(len(letters)):
            self.offsets[letters[i]] = Point3D(0, 0, 0)
            self.blocks[letters[i]] = Block(crosses[i], self.perm[i], self.flips[i])

    def can_fit(self):
        all_points = set()
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        for letter in letters:
            for pt in self.blocks[letter].spacePoints:
                if pt in all_points:
                    return False
                else:
                    all_points.add(pt)
        return True


    def full_debug(self):
        # print('display')
        minX, maxX, minY, maxY, minZ, maxZ = -11, 11, -11, 11, -11, 11
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        for letter in letters:
            for pt in self.blocks[letter].spacePoints:
                minX, maxX = min(minX, pt.x), max(maxX, pt.x)
                minY, maxY = min(minY, pt.y), max(maxY, pt.y)
                minZ, maxZ = min(minZ, pt.z), max(maxZ, pt.z)

        for z in range(maxZ, minZ-2, -2):
            print('   *** Level({}) ***'.format(z))
            for y in range(minY, maxY+2, 2):
                for x in range(minX, maxX+2, 2):
                    found = False
                    for letter in letters:
                        if self.blocks[letter].contains(Point3D(x, y, z)):
                            print('{} '.format(letter), end='')
                            found = True
                            break
                    if not found:
                        print('.', end=' ')
                print()


# class MoveEnumeration:
#     cursor = 0
#     end = 0
#
#     # Konstruktors: iterators sāksies ar vērtību "initial" un beidzas ar max-1.
#     def __init__(self, initial, direction):
#         self.next_moves = NEXT_MOVES[direction]
#         self.cursor = initial - 1
#         self.end = len(self.next_moves)
#
#     # Sagatavo iteratoru "for" cikla pašā sākumā un atgriež to
#     def __iter__(self):
#         return self
#
#     # atgriež tekošo vērtību intervālā [initial; max-1]. Ja beidzas, tad izlec no cikla ar "StopIteration"
#     def __next__(self):
#         self.cursor += 1
#         if self.cursor < self.end:
#             return self.next_moves[self.cursor]
#         raise StopIteration



def main():
    abc = list(itertools.permutations(['A', 'B', 'C', 'D', 'E', 'F']))
    all_flips = list(itertools.product([0,1], repeat=6))

    total_combinations = 0
    for perm in abc:
        for flips in all_flips:
            bcp = BurrCrossProblem(perm, flips, [CROSS01, CROSS02, CROSS03, CROSS04, CROSS05, CROSS06])
            if bcp.can_fit():
                print('Solution {}, {}'.format(perm, flips))
                total_combinations += 1
    print('Sth is {}'.format(total_combinations))

    # bcp = BurrCrossProblem(['A', 'B', 'C', 'D', 'E', 'F'], [0, 0, 0, 0, 0, 0],
    #                        [CROSS01, CROSS02, CROSS03, CROSS04, CROSS05, CROSS06])
    # bcp.full_debug()
    # for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
    #     print('Block {} has {} points'.format(letter, len(bcp.blocks[letter].spacePoints)))
    # print("Can fit = {}".format(bcp.can_fit()))
    #
    # print("Block A has points: {}".format(bcp.blocks['A'].spacePoints))
    # print("Block B has points: {}".format(bcp.blocks['B'].spacePoints))
    # print("Block C has points: {}".format(bcp.blocks['C'].spacePoints))
    # print("Block D has points: {}".format(bcp.blocks['D'].spacePoints))
    # print("Block E has points: {}".format(bcp.blocks['E'].spacePoints))
    # print("Block F has points: {}".format(bcp.blocks['F'].spacePoints))

if __name__ == '__main__':
    main()

