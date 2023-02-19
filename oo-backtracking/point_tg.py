import math

# This class deals with the triangle grid coordinates (x,y,z) such that x+y+z = 0. 
# It also has some static methods describing the geometry of the triangular grid. 
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


    def __lt__(self, other):
        b1 = self.x < other.x 
        b2 = self.x == other.x and self.y < other.y
        b3 = self.x == other.x and self.y == other.y and self.z < other.z
        return b1 or b2 or b3


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


    FORBIDDEN_AFTER = {'A': ['A', 'D'], 'B': ['B', 'E'], 'C': ['C', 'F'], 
    'D': ['A', 'D'], 'E': ['B', 'E'], 'F': ['C', 'F']}

    # Secība, kādā pārbaudīt nākamos gājienus (kā definēts Martas zīmējumos)
    # NEXT_MOVES = {'0': ['A'], '1': ['C', 'B'],
    #     'A': ['C', 'B', 'E', 'F'], 'B': ['D', 'C', 'A', 'F'], 'C': ['D', 'B', 'A', 'E'],
    #     'D': ['C', 'B', 'E', 'F'], 'E': ['D', 'C', 'A', 'F'], 'F': ['D', 'B', 'A', 'E']}
    
    # Secība, kādā pārbaudīt nākamos gājienus (alfabētiska) - ja būvē vārdnīcu
    NEXT_MOVES_DICT = {'0': ['B', 'C', 'E', 'F'], '1': ['B', 'C'],
       'A': ['B', 'C', 'E', 'F'], 'B': ['A', 'C', 'D', 'F'], 'C': ['A', 'B', 'D', 'E'],
       'D': ['B', 'C', 'E', 'F'], 'E': ['A', 'C', 'D', 'F'], 'F': ['A', 'B', 'D', 'E']}

    NEXT_MOVES = {'0': ['A'], '1': ['B', 'C'],
       'A': ['B', 'C', 'E', 'F'], 'B': ['A', 'C', 'D', 'F'], 'C': ['A', 'B', 'D', 'E'],
       'D': ['B', 'C', 'E', 'F'], 'E': ['A', 'C', 'D', 'F'], 'F': ['A', 'B', 'D', 'E']}



    DIRECTIONS_JOC_KOORD = {'A': [0, 1], 'B': [1, 0.5], 'C': [1, -0.5], 'D': [0, -1], 'E': [-1, -0.5], 'F': [-1, 0.5]}

    ANGLES = {('A','B'): 120, ('A','C'): 60, ('A','E'): -60, ('A','F'): -120,
    ('B','C'): 120, ('B','D'): 60, ('B','F'): -60, ('B','A'): -120,
    ('C','D'): 120, ('C','E'): 60, ('C','A'): -60, ('C','B'): -120,
    ('D','E'): 120, ('D','F'): 60, ('D','B'): -60, ('D','C'): -120,
    ('E','F'): 120, ('E','A'): 60, ('E','C'): -60, ('E','D'): -120,
    ('F','A'): 120, ('F','B'): 60, ('F','D'): -60, ('F','E'): -120}

    @staticmethod
    def convert_divainas_dekarta(directions, lengths=[]):
        if lengths==[]:
            lengths = list(range(len(directions),0,-1))
        result = []
        for i in range(len(directions)):
            side_length = lengths[i]
            if directions[i] == 'A':
                result.append([0, side_length])
            elif directions[i] == 'B':
                result.append([side_length, 0.5*side_length])
            elif directions[i] == 'C':
                result.append([side_length, -0.5*side_length])
            elif directions[i] == 'D':
                result.append([0, -side_length])
            elif directions[i] == 'E':
                result.append([-side_length, -0.5*side_length])
            else:
                result.append([-side_length, 0.5*side_length])
        return result

    # Atgriež pozitīvu skaitli t.t.t, ja polimonda virsotnes izkārtotas pretēji pulksteņa virzienam
    @staticmethod
    def get_signed_area(directions):
        N = len(directions)
        unit_triangle_height = math.sqrt(3)/2
        unit_triangle_area = math.sqrt(3)/4
        divain_dekarta = PointTg.convert_divainas_dekarta(directions)

        # Summē malu vektoriņus, aprēķina virsotnes dīvainajās koordinātēs (sākas un beidzas ar [0;0])
        partial_sums = [[0,0]]
        for i in range(0, N):
            new_pair = [partial_sums[-1][0] + divain_dekarta[i][0], partial_sums[-1][1] + divain_dekarta[i][1]]
            partial_sums.append(new_pair)

        # Pārveido dīvainās Dekarta koordinātes parastajās Dekarta koordinātēs (pareizina y ar trijstūra augstumu)
        dekartaXY = [[unit_triangle_height*y, x] for [y,x] in partial_sums]
        summa = 0
        for i in range(0, N - 1):
            summa += dekartaXY[i][1]*dekartaXY[i+1][0] - dekartaXY[i][0]*dekartaXY[i+1][1]
        summa += dekartaXY[N-1][1]*dekartaXY[0][0] - dekartaXY[N-1][0]*dekartaXY[0][1]
        # summa/2 ir laukums 1*1 kvadrātiņu vienībās; pārveido to mazo trijstūrīšu vienībās.
        result = (summa/2)/unit_triangle_area
        intResult = int(round(result))
        return intResult

    # Saskaita N-polimonda iekšējos leņķus, sadalot pa izmēriem (60, 120, 240, 300 grādi) 
    @staticmethod
    def count_angles(directions):
        (a60, a120, a240, a300) = (0,0,0,0)
        N = len(directions)
        signed_area = PointTg.get_signed_area(directions)
        orientation = int(abs(signed_area)/signed_area)
        for i in range(0, N):
            side1 = directions[i]
            side2 = directions[(i+1) % N]
            signed_angle = orientation*PointTg.ANGLES[(side1, side2)]
            if signed_angle == 60:
                a60 += 1
            elif signed_angle == 120: 
                a120 += 1
            elif signed_angle == -120: 
                a240 += 1
            else:
                a300 += 1
        return (a60, a120, a240, a300)

    @staticmethod
    def is_acute(d1, d2): 
        angle = abs(PointTg.ANGLES[(d1,d2)])
        return (angle == 60)




DIRECTIONS = {'A': PointTg(1,0,-1), 'B': PointTg(1,-1,0), 'C': PointTg(0,-1,1),
        'D': PointTg(-1,0,1), 'E': PointTg(-1,1,0),'F': PointTg(0,1,-1)}



