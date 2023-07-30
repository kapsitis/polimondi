import math
from .point_tg import PointTg
from .point_tg import DIRECTIONS
from .geom_utilities import L2_dist

from shapely.geometry import Point, Polygon, LineString
# from shapely.ops import rotate
from shapely import affinity
from scipy.spatial import ConvexHull
import numpy as np


#DIRECTIONS = {'A': PointTg(1,0,-1), 'B': PointTg(1,-1,0), 'C': PointTg(0,-1,1),
#        'D': PointTg(-1,0,1), 'E': PointTg(-1,1,0),'F': PointTg(0,1,-1)}

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
        self.setup()

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
        result = "sides = {}".format(self.sides) + ", " + "signed_area = {}".format(self.signed_area)
        return result

    # All vertices in triangle coordinates.
    def get_vertices(self):
        if not hasattr(self, 'vertices'):
            self.vertices = [PointTg(0, 0, 0)]
            for (side_length, direction) in self.sides:
                new_vertex = self.vertices[-1] + side_length * DIRECTIONS[direction]
                if len(self.vertices) < len(self.sides):
                    self.vertices.append(new_vertex)
        return self.vertices

    # Get vertex coordinates (but assume that triangle height is 1 unit; not sqrt(3)/2).
    def get_mod_descartes(self):
        if not hasattr(self, 'mod_descartes'):
            vectors = [(L*DESCARTES[D][0], L*DESCARTES[D][1]) for (L, D) in self.sides]

            self.mod_descartes = [(0.0, 0.0)]
            for i in range(0, len(self.sides)-1):
                new_pair = (self.mod_descartes[-1][0] + vectors[i][0], self.mod_descartes[-1][1] + vectors[i][1])
                self.mod_descartes.append(new_pair)
        return self.mod_descartes

    # Get regular (x,y) coordinates of vertices
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

    # Return (a,b,c) showing the length totals for the polyiamond's sides in all 3 directions.
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

    # Do not store perimeter with the object
    def list_perimeter(self):
        curr_point = PointTg(0,0,0)
        result = []
        for (L, D) in self.sides:
            vect = DIRECTIONS[D]
            for i in range(L):
                curr_point += vect
                result.append(curr_point)
        return result

    # Ray casting algorithm to check, if "pt" is
    # inside the polygon represented by "self".
    # def is_inside1(self, pt):
    #     # self.get_vertices()
    #     vertices = [vv.get_xy() for vv in self.vertices]
    #     (x, y) = pt.get_xy()
    #     print('vertices = {}'.format(vertices))
    #     print('pt = {},{}'.format(x,y))
    #     count = 0
    #     p1x, p1y = vertices[0]
    #     for i in range(1, len(vertices) + 1):
    #         p2x, p2y = vertices[i % len(vertices)]
    #         if y > min(p1y, p2y):
    #             if y <= max(p1y, p2y):
    #                 if x <= max(p1x, p2x):
    #                     if p1y != p2y:
    #                         xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
    #                     if p1x == p2x or x <= xinters:
    #                         count += 1
    #         p1x, p1y = p2x, p2y
    #     if count % 2 == 0:
    #         return False
    #     else:
    #         return True

    def winding_number(self, pt):
        vertices = [vv.get_xy() for vv in self.vertices]
        (x, y) = pt.get_xy()
        sum_angle = 0.0

        for i in range(len(vertices)):
            dx1, dy1 = vertices[i][0] - x, vertices[i][1] - y
            dx2, dy2 = vertices[(i + 1) % len(vertices)][0] - x, vertices[(i + 1) % len(vertices)][1] - y
            angle1 = math.atan2(dy1, dx1)
            angle2 = math.atan2(dy2, dx2)
            da = angle1 - angle2
            if da <= -math.pi:
                da += 2 * math.pi
            elif da > math.pi:
                da -= 2 * math.pi
            sum_angle += da
        return round(sum_angle / (2 * math.pi))


    # Winding-number based algorithm to find out, if "pt" is
    # inside the polygon represented by "self".
    # def is_inside2(self, pt):
    #     winding_number = self.winding_number(pt)
    #     return winding_number != 0


    def is_inside(self, pt):
        vertices = [vv.get_xy() for vv in self.vertices]
        (x, y) = pt.get_xy()
        pp = Point(x, y)
        poly = Polygon(vertices)
        cond1 = poly.contains(pp)
        cond2 = True
        for i in range(len(vertices)):
            v1 = vertices[i]
            v2 = vertices[(i+1)%len(vertices)]
            line = LineString([v1, v2])
            if pp.distance(line) < 1e-07:
                cond2 = False
                break
        return cond1 and cond2

    # Return triplet (diam, i_max, j_max) - the diameter for a set of points and where it was achieved
    def diameter(self):
        vertices = [vv.get_xy() for vv in self.vertices]
        diam, i_max, j_max = 0, -1, -1
        for i in range(len(vertices)):
            for j in range(i+1, len(vertices)):
                dist = L2_dist(vertices[i], vertices[j])
                if dist > diam:
                    diam = dist
                    i_max, j_max = i, j
        return (diam, i_max, j_max)

    # Returns the minimum width: The closest possible distance between two parallel lines
    # such that all vertices are between these parallel lines (or on these lines).
    def min_width(self):
        vertices = [vv.get_xy() for vv in self.vertices]
        hull = ConvexHull(vertices)
        # Create a Polygon from the convex hull vertices
        convex_vertices = vertices[hull.vertices]
        pol = Polygon(convex_vertices)

        # the rotating calipers algorithm needs the vertices ordered by angle
        sorted_vertices = sorted(pol.exterior.coords[:-1])
        # initialize min_width variable as infinity
        min_width = float('inf')
        seg_min_width = [0, 0]

        n = len(sorted_vertices)
        for i in range(n):
            # Create a LineString from a pair of vertices
            line = LineString([sorted_vertices[i], sorted_vertices[(i + 1) % n]])

            # 180 deg rotation to compute parallel line through opposite vertex
            # rotated_line = rotate(line, 180, sorted_vertices[i])
            rotated_line = affinity.rotate(line, 180, sorted_vertices[i])


            # Find the closest point on the rotated line to the opposite vertex
            closest_point = rotated_line.interpolate(rotated_line.project(Point(sorted_vertices[(i + n // 2) % n])))

            # Compute the distance between the vertex and its closest point on the rotated line
            width = Point(sorted_vertices[i]).distance(closest_point)

            # Update min_width and seg_min_width if the width is smaller than min_width
            if width < min_width:
                min_width = width
                seg_min_width = [sorted_vertices[i], (closest_point.x, closest_point.y)]

        return min_width, seg_min_width

    # Return all internal points as [PointTg, PointTg, ...]
    def list_internal(self):
        # Cache answers to avoid computing anything twice
        good_points = set()
        bad_points = set()

    # Return all contained triangles as list of triplets:
    # [(PointTg, PointTg, PointTg), (PointTg, PointTg, PointTg), ...]
    def list_triangles(self):
        return []



