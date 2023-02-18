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



DIRECTIONS = {'A': PointTg(1,0,-1), 'B': PointTg(1,-1,0), 'C': PointTg(0,-1,1),
        'D': PointTg(-1,0,1), 'E': PointTg(-1,1,0),'F': PointTg(0,1,-1)}



