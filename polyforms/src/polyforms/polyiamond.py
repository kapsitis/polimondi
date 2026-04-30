import math
from .point_tg import PointTg
from .point_tg import DIRECTIONS
from .point_tg import AA,BB,CC,DD,EE,FF
from .geom_utilities import *
from .inductive_splits import InductiveSplits

from shapely.geometry import Point, Polygon, LineString
# from shapely.ops import rotate
from shapely import affinity
from scipy.spatial import ConvexHull
import numpy as np
import copy as cp



#DIRECTIONS = {'A': PointTg(1,0,-1), 'B': PointTg(1,-1,0), 'C': PointTg(0,-1,1),
#        'D': PointTg(-1,0,1), 'E': PointTg(-1,1,0),'F': PointTg(0,1,-1)}

DESCARTES = {'A': (1.0, 0.0), 'B': (0.5, 1.0), 'C': (-0.5, 1.0), 'D': (-1.0, 0.0), 'E': (-0.5, -1.0), 'F': (0.5, -1.0) }

# Integer-doubled mod-Cartesian direction vectors (all entries are exact integers).
# A PointTg(a,b,c) maps to DESCARTES2 coordinates (2a+b, -2b).
# Unit equilateral triangle has area 2 in these coordinates (shoelace/2).
# Therefore: signed_area_in_triangles = shoelace_sum_in_DESCARTES2 // 4
DESCARTES2 = {'A': (2, 0), 'B': (1, 2), 'C': (-1, 2), 'D': (-2, 0), 'E': (-1, -2), 'F': (1, -2)}

unit_triangle_height = math.sqrt(3) / 2
unit_triangle_area = math.sqrt(3) / 4

class Polyiamond:
    # "sides" is a list of tuples for a polyiamond
    # such as [(5,'A'), (4,'C'), (3,'E'), (2,'D'), (1,'F')].
    # It does not need to be perfect or even magic, so the side lengths can be any integers.
    # Side directions are always one of the following: 'A', 'B', 'C', 'D', 'E', 'F'.
    def __init__(self, sides):
        self.compact_sides = sides
        if isinstance(sides, str):
            sides = list(zip(range(len(sides), 0, -1), list(sides)))
        self.sides = sides
        if not self.is_valid():
            print(f"WARNING: Polyiamond {self.compact_sides} is not valid - line segments do not close!")
            pass
            # raise ValueError("Polyiamond {} cannot exist".format(sides))
        else:
            self.setup()

    # The 1st check: The last side should return back to (0,0,0)
    # The 2nd check: The line segments must not cross themselves (not implemented)
    def is_valid(self):
        self.get_vertices()
        (side_length, direction) = self.sides[-1]
        new_vertex = self.vertices[-1] + side_length * PointTg.get_direction(direction)
        check1 = (new_vertex == PointTg(0,0,0))

        currVertex = PointTg(0,0,0)
        check2 = True  # assume the sides do not intersect
        points = set()
        for (sidelen,dir) in self.sides:
            for i in range(1, sidelen+1):
                currPoint = currVertex + i*DIRECTIONS[dir]
                if currPoint in points:
                    # print('Intersecting STUFF!')
                    check2 = False
                else:
                    points.add(currPoint)
            nextSide = sidelen*DIRECTIONS[dir]
            currVertex = currVertex + nextSide
        return check1 and check2

    # This method will do custom initializations
    def setup(self):
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
                new_vertex = self.vertices[-1] + side_length * PointTg.get_direction(direction)
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

    def get_rect_box(self):
        if not hasattr(self, 'descartes'):
            self.get_mod_descartes()
        min_x = min([uu[0] for uu in self.mod_descartes])
        max_x = max([uu[0] for uu in self.mod_descartes])
        min_y = min([uu[1] for uu in self.mod_descartes])
        max_y = max([uu[1] for uu in self.mod_descartes])
        return (min_x, max_x, min_y, max_y)

    def get_signed_area(self):
        """Compute signed area in triangle units using exact integer arithmetic.

        Uses integer-doubled mod-Cartesian coordinates (DESCARTES2) where every
        vertex has integer coordinates.  The shoelace sum divided by 4 gives the
        exact signed area measured in unit-triangle units (always an integer).
        """
        if not hasattr(self, 'signed_area'):
            # Build integer vertices in DESCARTES2 coords without any floating point.
            verts2 = [(0, 0)]
            for (L, D) in self.sides[:-1]:
                dx, dy = DESCARTES2[D]
                verts2.append((verts2[-1][0] + L * dx, verts2[-1][1] + L * dy))
            N = len(verts2)
            shoelace = 0
            for i in range(N - 1):
                shoelace += verts2[i][0] * verts2[i+1][1] - verts2[i][1] * verts2[i+1][0]
            shoelace += verts2[N-1][0] * verts2[0][1] - verts2[N-1][1] * verts2[0][0]
            # shoelace == 4 * signed_area_in_triangles  (exact, no rounding needed)
            assert shoelace % 4 == 0, "Shoelace sum not divisible by 4 – invalid polyiamond?"
            self.signed_area = shoelace // 4
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
            vect = PointTg.get_direction(D)
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
        """Compute the winding number of the polygon around *pt* using exact
        integer arithmetic in DESCARTES2 coordinates.

        Sign convention matches the original atan2-based implementation:
        returns -1 for interior points of CCW-oriented polygons, +1 for
        CW-oriented polygons, and 0 for exterior or boundary points.

        Algorithm: for each directed edge (v_i -> v_{i+1}) count upward and
        downward crossings of the horizontal line y = qy using integer cross
        products.  Boundary points (on a vertex or edge) return 0 explicitly.
        """
        # Convert query point PointTg(a,b,c) -> DESCARTES2: (2a+b, -2b)
        qx = 2 * pt.x + pt.y
        qy = -2 * pt.y

        # Build polygon vertices in DESCARTES2 integer coords
        verts2 = [(0, 0)]
        for (L, D) in self.sides[:-1]:
            dx, dy = DESCARTES2[D]
            verts2.append((verts2[-1][0] + L * dx, verts2[-1][1] + L * dy))

        winding = 0
        N = len(verts2)
        for i in range(N):
            x1, y1 = verts2[i]
            x2, y2 = verts2[(i + 1) % N]
            # cross product (v1->v2) x (v1->pt)
            cross = (x2 - x1) * (qy - y1) - (y2 - y1) * (qx - x1)
            # If cross == 0 the point lies on the line through this edge;
            # check if it also lies within the segment bounds -> boundary point.
            if cross == 0:
                if min(x1, x2) <= qx <= max(x1, x2) and min(y1, y2) <= qy <= max(y1, y2):
                    return 0  # on boundary
            if y1 <= qy:
                if y2 > qy and cross > 0:   # upward crossing, pt is left of edge
                    winding += 1
            else:
                if y2 <= qy and cross < 0:  # downward crossing, pt is right of edge
                    winding -= 1
        # Negate to preserve original sign convention (CCW polygon -> -1 for interior)
        return -winding


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

    def diameter_sq(self):
        """Return the squared diameter (maximum squared Euclidean distance between
        any two vertices) as an exact integer, together with the index pair where
        it is achieved.

        Working in DESCARTES2 integer coordinates avoids all floating-point
        arithmetic.  The actual diameter is sqrt(diameter_sq()) / 2 because the
        DESCARTES2 scale factor is 2 relative to mod-Cartesian, but since we only
        need comparisons the squared value suffices.
        """
        verts2 = [(0, 0)]
        for (L, D) in self.sides[:-1]:
            dx, dy = DESCARTES2[D]
            verts2.append((verts2[-1][0] + L * dx, verts2[-1][1] + L * dy))
        diam_sq, i_max, j_max = 0, -1, -1
        n = len(verts2)
        for i in range(n):
            for j in range(i + 1, n):
                dx = verts2[i][0] - verts2[j][0]
                dy = verts2[i][1] - verts2[j][1]
                d2 = dx * dx + dy * dy
                if d2 > diam_sq:
                    diam_sq = d2
                    i_max, j_max = i, j
        return (diam_sq, i_max, j_max)

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
        convex_vertices = [vertices[i] for i in hull.vertices]
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

    def width(self):
        vertices = [vv.get_xy() for vv in self.vertices]
        vertice_lists = [[x,y] for (x,y) in vertices]
        return minimum_width(np.array(vertice_lists))

    # ------------------------------------------------------------------
    # Convex hull and minimum-enclosing-shape methods (added 2026-04-30).
    # ------------------------------------------------------------------
    #
    # All four methods below operate on the convex hull of the polyiamond's
    # vertices.  The hull is computed in exact integer DESCARTES2 coordinates
    # using Andrew's monotone chain (only integer cross products), so the hull
    # itself is exact.  The enclosing-shape searches then operate on the hull
    # in real Cartesian floats — they use a fully NumPy-vectorised angular
    # sweep that is trivially batchable across many polyiamonds (just stack
    # the per-shape hull arrays into a leading "batch" axis).
    # ------------------------------------------------------------------

    def convex_hull(self):
        """Return the convex hull of the polyiamond's vertices as a list of
        :class:`PointTg` instances in CCW order (standard mathematical
        orientation, y-axis pointing up).

        Andrew's monotone chain is run on the integer-doubled mod-Cartesian
        coordinates (DESCARTES2), so all orientation tests are exact integer
        cross products with no floating-point error.

        Vectorisation note: a batched version (operating on stacked
        coordinate arrays of multiple polyiamonds) is straightforward to
        derive — the per-polyiamond loop body uses only integer comparisons
        and arithmetic.
        """
        self.get_vertices()
        coord_to_pt = {}
        for p in self.vertices:
            key = (2 * p.x + p.y, -2 * p.y)
            coord_to_pt.setdefault(key, p)
        coords = sorted(coord_to_pt.keys())
        if len(coords) <= 1:
            return [coord_to_pt[c] for c in coords]

        def _cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        lower = []
        for p in coords:
            while len(lower) >= 2 and _cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        upper = []
        for p in reversed(coords):
            while len(upper) >= 2 and _cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)
        hull_coords = lower[:-1] + upper[:-1]
        return [coord_to_pt[c] for c in hull_coords]

    def _hull_xy_array(self):
        """Internal helper: convex-hull vertices as an (M, 2) ``float`` numpy
        array of real Cartesian (x, y) coordinates."""
        return np.array([p.get_xy() for p in self.convex_hull()], dtype=float)

    def _hull_edge_angles(self):
        """Hull edge directions reduced to the interval ``[0, π)``."""
        pts = self._hull_xy_array()
        n = len(pts)
        if n < 2:
            return np.array([], dtype=float)
        edges = pts[(np.arange(n) + 1) % n] - pts
        return np.mod(np.arctan2(edges[:, 1], edges[:, 0]), math.pi)

    @staticmethod
    def _candidate_angles(edge_angles, period, n_grid):
        """Build a sorted, deduplicated array of candidate orientations in
        ``[0, period)`` containing both an evenly spaced grid (``n_grid``
        samples) and all hull-edge angles modulo ``period``."""
        grid = np.linspace(0.0, period, n_grid, endpoint=False)
        if edge_angles.size == 0:
            return grid
        edges_mod = np.mod(edge_angles, period)
        return np.unique(np.concatenate([grid, edges_mod]))

    def get_smallest_hexagon(self, n_angles=1440):
        """Return the smallest *regular* hexagon containing the polyiamond.

        Returns a list of 6 ``(x, y)`` Cartesian coordinate tuples — the
        hexagon vertices in CCW order.  The first polyiamond vertex is at
        Cartesian ``(0, 0)``.

        Algorithm
        ---------
        For a fixed orientation ``θ`` the hexagon is the intersection of
        three width-``2a`` strips perpendicular to the unit normals
        ``n_k = (cos(θ + k·π/3), sin(θ + k·π/3))``, ``k = 0, 1, 2``.
        Containment of the convex polygon ``P`` requires both:

        1. **Strip width**:  ``2a ≥ A_k`` for each ``k``, where
           ``A_k = max(p·n_k) − min(p·n_k)`` is the polygon width.
        2. **Translational feasibility**:  the 2-D centre ``c`` exists with
           ``c·n_k ∈ [max(p·n_k) − a, min(p·n_k) + a]`` for all ``k``.

        Eliminating ``c`` (using the linear identity ``c·n_0 = c·n_1 − c·n_2``
        for normals 60° apart in 2-D) gives the closed-form lower bound

        ::

            a*(θ) = max( A_0/2, A_1/2, A_2/2,
                         (|M_1 − M_0 − M_2| + (A_0+A_1+A_2)/2) / 3 )

        with ``M_k = (max + min)/2`` of the polygon's projection on ``n_k``.
        The hexagon side length is ``s(θ) = 2 a*(θ) / √3``.

        Candidate orientations are the union of an evenly spaced grid in
        ``[0, π/3)`` (``n_angles`` samples) and the convex-hull edge angles
        modulo ``π/3``.  The full sweep is vectorised with NumPy and is
        trivially batchable across many polyiamonds.

        Tie-breaking: when several optimal hexagons exist (numerically tied
        sizes), the one with the smallest centre x-coordinate is returned.
        """
        pts = self._hull_xy_array()
        period = math.pi / 3.0
        angles = self._candidate_angles(self._hull_edge_angles(), period, n_angles)

        # 3 normal directions per angle: shape (M, 3, 2)
        ks = np.arange(3)
        phi = angles[:, None] + ks[None, :] * period             # (M, 3)
        normals = np.stack([np.cos(phi), np.sin(phi)], axis=-1)  # (M, 3, 2)

        # Project hull points onto every normal: (M, 3, N)
        proj = np.einsum('mkd,nd->mkn', normals, pts)
        pmax = proj.max(axis=2)                                  # (M, 3)
        pmin = proj.min(axis=2)
        widths = pmax - pmin                                     # (M, 3) -> A_k
        midpts = (pmax + pmin) / 2.0                             # (M, 3) -> M_k

        # apothem candidates: half-widths + translational feasibility term
        half_w_max = widths.max(axis=1) / 2.0
        sum_half_widths = widths.sum(axis=1) / 2.0
        unbalance = np.abs(midpts[:, 1] - midpts[:, 0] - midpts[:, 2])
        translate_term = (unbalance + sum_half_widths) / 3.0
        apothem = np.maximum(half_w_max, translate_term)         # (M,)
        sides = 2.0 * apothem / math.sqrt(3.0)                   # hexagon side

        # Compute centre c from chosen u_k = M_k + d_k that satisfy
        # u_1 − u_0 − u_2 = M_1 − M_0 − M_2  (the 2-D linear constraint).
        # Distribute deviations proportionally to slacks δ_k = a − A_k/2:
        deltas = apothem[:, None] - widths / 2.0                 # (M, 3) >= 0
        S = deltas.sum(axis=1)                                   # (M,)
        T = midpts[:, 1] - midpts[:, 0] - midpts[:, 2]           # (M,)
        # Avoid div-by-zero when S == 0 (then T must also be 0).
        safe_S = np.where(S > 0, S, 1.0)
        ratio = T / safe_S                                       # (M,)
        d0 =  deltas[:, 0] * ratio
        d1 = -deltas[:, 1] * ratio
        d2 =  deltas[:, 2] * ratio
        u0 = midpts[:, 0] + d0
        u1 = midpts[:, 1] + d1
        # u2 = midpts[:, 2] + d2  (consistent by construction)

        # c = α n_0 + β m_0  with α = u0, β = (2 u1 − u0)/√3, m_0 ⟂ n_0
        alpha = u0
        beta = (2.0 * u1 - u0) / math.sqrt(3.0)
        cos_t = np.cos(angles); sin_t = np.sin(angles)
        cx = alpha * cos_t - beta * sin_t
        cy = alpha * sin_t + beta * cos_t

        s_min = sides.min()
        tol = 1e-9 * max(1.0, s_min)
        cand_idx = np.flatnonzero(sides <= s_min + tol)
        best = cand_idx[int(np.argmin(cx[cand_idx]))]

        theta = float(angles[best])
        s = float(sides[best])
        cxf, cyf = float(cx[best]), float(cy[best])

        # Hexagon vertices: at angles θ + π/6 + k·π/3, distance s from centre.
        verts = []
        for k in range(6):
            ang = theta + math.pi / 6.0 + k * (math.pi / 3.0)
            verts.append((cxf + s * math.cos(ang), cyf + s * math.sin(ang)))
        return verts

    def get_smallest_square(self, n_angles=1440):
        """Return the smallest enclosing square as a list of 4 ``(x, y)``
        Cartesian vertices in CCW order (first polyiamond vertex at origin).

        Algorithm
        ---------
        For each candidate orientation ``θ`` we rotate the convex hull by
        ``-θ`` and take its axis-aligned bounding box.  The smallest square
        at this orientation has side ``max(width_x, width_y)``.  The optimum
        is found over a vectorised sweep of candidate angles in
        ``[0, π/2)``.

        Candidate angles include both an evenly spaced grid of ``n_angles``
        samples and all hull-edge angles modulo ``π/2`` (an edge of the
        optimal square is generally flush with a hull edge — the
        rotating-calipers theorem for the minimum-area enclosing rectangle
        — and the smallest square's optimum is either at such an angle or
        at a balance angle where ``width_x = width_y``, both well-covered
        by a fine grid).
        """
        pts = self._hull_xy_array()
        period = math.pi / 2.0
        angles = self._candidate_angles(self._hull_edge_angles(), period, n_angles)

        cos_t = np.cos(angles)
        sin_t = np.sin(angles)
        # rotated coords: x' = cos·x + sin·y ; y' = -sin·x + cos·y
        x = pts[:, 0]
        y = pts[:, 1]
        xp = cos_t[:, None] * x[None, :] + sin_t[:, None] * y[None, :]   # (M, N)
        yp = -sin_t[:, None] * x[None, :] + cos_t[:, None] * y[None, :]  # (M, N)

        xmax = xp.max(axis=1); xmin = xp.min(axis=1)
        ymax = yp.max(axis=1); ymin = yp.min(axis=1)
        wx = xmax - xmin
        wy = ymax - ymin
        sides = np.maximum(wx, wy)

        # Centre in rotated frame, then in original frame.
        cxp = (xmax + xmin) / 2.0
        cyp = (ymax + ymin) / 2.0
        cx = cos_t * cxp - sin_t * cyp
        cy = sin_t * cxp + cos_t * cyp

        s_min = sides.min()
        tol = 1e-9 * max(1.0, s_min)
        cand_idx = np.flatnonzero(sides <= s_min + tol)
        best = cand_idx[int(np.argmin(cx[cand_idx]))]

        theta = float(angles[best])
        s = float(sides[best])
        cxf, cyf = float(cx[best]), float(cy[best])

        # Square corners in CCW order, in canonical (rotated) frame:
        half = s / 2.0
        canonical = [(-half, -half), (half, -half), (half, half), (-half, half)]
        ct, st = math.cos(theta), math.sin(theta)
        return [(cxf + ct * vx - st * vy, cyf + st * vx + ct * vy)
                for (vx, vy) in canonical]

    def get_smallest_triangle(self, n_angles=1440):
        """Return the smallest enclosing equilateral triangle as a list of
        3 ``(x, y)`` Cartesian vertices in CCW order (first polyiamond
        vertex at origin).

        Algorithm
        ---------
        Rotate the convex hull by ``-θ`` so the candidate triangle becomes
        the canonical "apex-up" equilateral triangle.  In that frame, with
        outward normals ``(0,-1)``, ``(√3/2, 1/2)``, ``(-√3/2, 1/2)``::

            cy = min(y_rot)
            A  = max( (√3/2)·x_rot + (1/2)·y_rot )
            B  = max(-(√3/2)·x_rot + (1/2)·y_rot )
            s  = 2·(A + B - cy) / √3
            cx = (A - B) / √3

        gives the smallest enclosing apex-up equilateral triangle at this
        orientation.  We sweep ``θ`` over ``[0, 2π/3)`` (the rotational
        period of an equilateral triangle) and return the configuration
        with the smallest side ``s``.

        The whole sweep is fully vectorised with NumPy.
        """
        pts = self._hull_xy_array()
        period = 2.0 * math.pi / 3.0
        angles = self._candidate_angles(self._hull_edge_angles(), period, n_angles)

        cos_t = np.cos(angles)
        sin_t = np.sin(angles)
        x = pts[:, 0]
        y = pts[:, 1]
        xp = cos_t[:, None] * x[None, :] + sin_t[:, None] * y[None, :]    # (M, N)
        yp = -sin_t[:, None] * x[None, :] + cos_t[:, None] * y[None, :]   # (M, N)

        sqrt3_2 = math.sqrt(3.0) / 2.0
        cy = yp.min(axis=1)
        A = ( sqrt3_2 * xp + 0.5 * yp).max(axis=1)
        B = (-sqrt3_2 * xp + 0.5 * yp).max(axis=1)
        sides = 2.0 * (A + B - cy) / math.sqrt(3.0)
        cx_rot = (A - B) / math.sqrt(3.0)
        cy_rot = cy

        # Centre in original frame (for tie-breaking).
        cx = cos_t * cx_rot - sin_t * cy_rot
        # cy_orig = sin_t * cx_rot + cos_t * cy_rot   # not needed for tie-break

        s_min = sides.min()
        tol = 1e-9 * max(1.0, s_min)
        cand_idx = np.flatnonzero(sides <= s_min + tol)
        best = cand_idx[int(np.argmin(cx[cand_idx]))]

        theta = float(angles[best])
        s = float(sides[best])
        cxr = float(cx_rot[best])
        cyr = float(cy_rot[best])

        # Triangle vertices in canonical (rotated) frame, CCW:
        #   bottom-left, bottom-right, apex
        h = s * math.sqrt(3.0) / 2.0
        canonical = [(cxr - s/2.0, cyr),
                     (cxr + s/2.0, cyr),
                     (cxr,        cyr + h)]
        ct, st = math.cos(theta), math.sin(theta)
        return [(ct * vx - st * vy, st * vx + ct * vy) for (vx, vy) in canonical]

    # ------------------------------------------------------------------

    # Return all internal+perimeter points as [PointTg, PointTg, ...]
    def list_inside(self):
        # Cache answers to avoid computing anything twice
        black_points = set()
        bad_points = set()
        gray_points = cp.copy(self.list_perimeter())
        while len(gray_points) > 0:
            current = gray_points.pop(0)
            # print('current = {}; len(gray_points) = {}'.format(current, len(gray_points)))
            for v in [AA,BB,CC,DD,EE,FF]:
                new_point = current + v
                if (new_point not in gray_points) and (new_point not in bad_points) and (new_point not in black_points):
                    if self.is_inside(new_point):
                        gray_points.append(new_point)
                    else:
                        bad_points.add(new_point)
            black_points.add(current)
        return sorted(black_points)




    # Return all contained triangles as list of triplets:
    # [(PointTg, PointTg, PointTg), (PointTg, PointTg, PointTg), ...]
    def list_triangles(self):
        inside_points = self.list_inside()
        queue = cp.copy(inside_points)
        result = set()
        while len(queue) > 0:
            curr0 = queue.pop(0)
            curr1 = curr0 + FF
            curr2 = curr0 + AA
            if curr1 in inside_points and curr2 in inside_points:
                result.add((curr0, curr1, curr2))
            curr3 = curr0 + BB
            if curr2 in inside_points and curr3 in inside_points:
                result.add((curr0, curr3, curr2))
        return sorted(result)


    # Assuming that polyiamond is 2-colored (usual parity coloring),
    # Return pair (black, white) -- the count of black and white triangles.
    # The following equality should be satisfied: black+white == area.
    # TODO: Should use list_trianles()
    def black_white(self):
        return (0,0)

    # Return a quadruplet (a,b,c,d) representing the
    # counts of internal angles by their size. They can be 60 or 120 degrees;
    # as well as -120 or -60 degrees (for vertices where polyiamond is not convex).
    def internal_angles(self):
        (a60, a120, a240, a300) = (0,0,0,0)
        signed_area = self.get_signed_area()
        orientation = int(abs(signed_area)/signed_area)
        for i in range(0, len(self.sides)):
            side1 = self.sides[i][1]
            side2 = self.sides[(i+1) % len(self.sides)][1]
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
    def find_fragments_cfg(sides):
        n = len(sides)
        D = dict()
        result = []
        for i in range(n, 0, -1):
            for j in range(i-1, -1, -1):
                x = sides[j:i]
                # result.append(x)
                px = InductiveSplits.p(x)

                # skip zero-sequences
                if (px == PointTg(0,0,0)):
                    continue
                # skip sequences that cannot concatenate as polyiamonds:
                if x[0] == x[-1]:
                    continue
                if DIRECTIONS[x[0]] + DIRECTIONS[x[-1]] == PointTg(0,0,0):
                    continue

                x_px = abs(i-j)*px
                if x_px in D:
                    D[x_px].append((x,j,i))
                else:
                    D[x_px] = [(x, i, j)]
                pv = px
                for xlen in range(1, n):
                    searchkey = (-2*xlen - abs(i-j))*px
                    if not searchkey in D:
                        continue
                    for (x2, j2, i2) in D[searchkey]:
                        if xlen == (i2-j2) and j2 >= i:
                            u2 = sides[0:j]
                            v2 = x
                            w2 = sides[i:j2]
                            y2 = sides[i2:]

                            AA = InductiveSplits.g(y2) + InductiveSplits.g(w2) + InductiveSplits.g(u2)
                            AA += len(y2)*InductiveSplits.p(w2)
                            AA += (len(y2) + len(w2))*InductiveSplits.p(u2)
                            # (A) g(y) + g(w) + g(u) + |y| * p(w) + (|y|+|w|) * p(u) = (0,0,0)
                            BB = InductiveSplits.g(x2)  +  InductiveSplits.g(v2)
                            BB += len(y2)*InductiveSplits.p(x2)
                            BB += len(x2)*InductiveSplits.p(w2)
                            BB += (len(y2) + len(x2) + len(w2))*InductiveSplits.p(v2)
                            BB += (len(x2) + len(v2))*InductiveSplits.p(u2)
                            # (B) g(x) + g(v) + | y | *p(x) + | x |*p(w) + (| y | + | x | + | w |) * p(v) + (| x | + | v |) * p(u) = (0, 0, 0)
                            if AA == PointTg(0,0,0) and BB == PointTg(0,0,0):
                                result.append((u2, v2, w2, x2, y2))
        return result




# A function that returns those polygons which have minimal-size bounding hexagons from polylist.
def get_minimal_bounding_sizes(polylist):
    min_item = min(polylist, key=lambda ai: ai.get_bounding_sizes())
    f_list = [ai for ai in polylist if ai.get_bounding_sizes() == min_item.get_bounding_sizes()]
    return f_list