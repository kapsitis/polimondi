import math
from .point_tg import PointTg

DIRECTIONS = {'A': PointTg(1,0,-1), 'B': PointTg(1,-1,0), 'C': PointTg(0,-1,1),
        'D': PointTg(-1,0,1), 'E': PointTg(-1,1,0),'F': PointTg(0,1,-1)}

DESCARTES = {'A': (1.0, 0.0), 'B': (0.5, 1.0), 'C': (-0.5, 1.0), 'D': (-1.0, 0.0), 'E': (-0.5, -1.0), 'F': (0.5, -1.0) }

unit_triangle_height = math.sqrt(3) / 2
unit_triangle_area = math.sqrt(3) / 4

class PolyGeometry:
    # "sides" is a list of tuples for a polyiamond
    # such as [(5,'A'), (4,'C'), (3,'E'), (2,'D'), (1,'F')].
    # It does not need to be perfect or even magic, so the side lengths can be any integers.
    # Side directions are always one of the following: 'A', 'B', 'C', 'D', 'E', 'F'.
    def __init__(self, sides):
        self.sides = sides

    # This method will do custom initializations
    def setup(self):
        self.get_vertices()
        self.get_mod_descartes()
        self.get_descartes()
        self.get_signed_area()
        self.get_area()
        self.get_perimeter()
        self.get_bounding_hexagon()
        self.get_bounding_sizes()


    def __str__(self):
        return 'PolyGeometry({})'.format(self.sides)

    def __repr__(self):
        result = "sides = {}".format(self.sides) + "\n"
        result += "vertices = {}".format(self.vertices) + "\n"
        result += "modif_descartes = {}".format(self.mod_descartes) + "\n"
        result += "signed_area = {}".format(self.signed_area)
        return result

    # All vertices in triangle coordinates.
    def get_vertices(self):
        if not hasattr(self, 'vertices'):
            self.vertices = [PointTg(0, 0, 0)]
            for (side_length, direction) in self.sides:
                new_vertex = self.vertices[-1] + side_length * DIRECTIONS[direction]
                self.vertices.append(new_vertex)
        return self.vertices

    def get_mod_descartes(self):
        if not hasattr(self, 'mod_descartes'):
            vectors = [(L*DESCARTES[D][0], L*DESCARTES[D][1]) for (L, D) in self.sides]

            self.mod_descartes = [(0.0, 0.0)]
            for i in range(0, len(self.sides)-1):
                new_pair = (self.mod_descartes[-1][0] + vectors[i][0], self.mod_descartes[-1][1] + vectors[i][1])
                self.mod_descartes.append(new_pair)
        return self.mod_descartes

    def get_descartes(self):
        if not hasattr(self, 'descartes'):
            self.get_mod_descartes()
            self.descartes = [(x, unit_triangle_height*y) for (x,y) in self.mod_descartes]
        return self.descartes



    # @staticmethod
    # def stretched_descartes(sides):
    #     result = []
    #     for (side_length, direction) in sides:
    #         if direction == 'A':
    #             result.append((side_length, 0))
    #         elif direction == 'B':
    #             result.append((0.5*side_length, side_length))
    #         elif direction == 'C':
    #             result.append((-0.5*side_length, side_length))
    #         elif direction == 'D':
    #             result.append((-side_length, 0))
    #         elif direction == 'E':
    #             result.append((-0.5*side_length, -side_length))
    #         else:
    #             result.append((0.5*side_length, -side_length))
    #     return result

    def get_signed_area(self):
        if not hasattr(self, 'signed_area'):
            self.get_descartes()
            N = len(self.descartes)
            array = 0
            for i in range(0, N - 1):
                array += self.descartes[i][0]*self.descartes[i+1][1] - self.descartes[i][1]*self.descartes[i+1][0]
            array += self.descartes[N-1][0]*self.descartes[0][1] - self.descartes[N-1][1]*self.descartes[0][0]
            # array/2 būtu laukums vienības kvadrātiņu vienībās; pārveido to mazo trijstūrīšu vienībās.
            result = (array/2)/unit_triangle_area
            self.signed_area = int(round(result))
        return self.signed_area

    def get_area(self):
        if not hasattr(self, 'area'):
            self.get_signed_area()
            self.area = abs(self.signed_area)
        return self.area

    def get_perimeter(self):
        if not hasattr(self, 'perimeter'):
            self.perimeter = sum([L for (L, D) in self.sides])
        return self.perimeter

    def get_bounding_hexagon(self):
        if not hasattr(self, 'bounding_hexagon'):
            self.get_vertices()
            a_min = min([p.y for p in self.vertices])
            a_max = max([p.y for p in self.vertices])

            b_min = min([p.z for p in self.vertices])
            b_max = max([p.z for p in self.vertices])

            c_min = min([p.x for p in self.vertices])
            c_max = max([p.x for p in self.vertices])
            self.bounding_hexagon = (a_min, a_max, b_min, b_max, c_min, c_max)

        return self.bounding_hexagon

    def get_bounding_sizes(self):
        if not hasattr(self, 'bounding_sizes'):
            (a_min, a_max, b_min, b_max, c_min, c_max) = self.get_bounding_hexagon()
            self.bounding_sizes = (a_max - a_min, b_max - b_min, c_max - c_min)
        return self.bounding_sizes

    def get_direction_counts(self):
        if not hasattr(self, 'direction_counts'):
            aa, bb, cc = 0, 0, 0
            for (L, D) in self.sides:
                if D in ['A','D']:
                    aa += L
                elif D in ['B', 'E']:
                    bb += L
                else:
                    cc += L
            self.direction_counts = (aa,bb,cc)
        return self.direction_counts
