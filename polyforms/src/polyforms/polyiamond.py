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

    def get_bounding_rectangle(self):
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
        if len(vertices) < 3:
            return 0.0, None

        import numpy as np
        from scipy.spatial import ConvexHull
        import math

        hull = ConvexHull(vertices)
        hull_pts = [vertices[i] for i in hull.vertices]

        min_width = float('inf')
        best_p1 = None
        best_p2 = None
        best_pt = None

        n = len(hull_pts)
        for i in range(n):
            p1 = np.array(hull_pts[i])
            p2 = np.array(hull_pts[(i+1)%n])
            
            edge_vec = p2 - p1
            edge_len = np.linalg.norm(edge_vec)
            if edge_len < 1e-9:
                continue
            
            edge_dir = edge_vec / edge_len
            normal = np.array([-edge_dir[1], edge_dir[0]])
            
            max_dist = -1.0
            furthest_pt = None
            
            for j in range(n):
                if j == i or j == (i+1)%n: continue
                pt = np.array(hull_pts[j])
                dist = abs(np.dot(pt - p1, normal))
                if dist > max_dist:
                    max_dist = dist
                    furthest_pt = hull_pts[j]
                    
            if max_dist < min_width:
                min_width = max_dist
                best_p1 = tuple(float(x) for x in p1)
                best_p2 = tuple(float(x) for x in p2)
                best_pt = tuple(float(x) for x in furthest_pt)

        # Calculate projection of furthest point onto the edge
        # so we return the line segment measuring the width.
        p1_arr = np.array(best_p1)
        p2_arr = np.array(best_p2)
        pt_arr = np.array(best_pt)
        edge_vec = p2_arr - p1_arr
        edge_dir = edge_vec / np.linalg.norm(edge_vec)
        proj_pt = p1_arr + np.dot(pt_arr - p1_arr, edge_dir) * edge_dir
        
        seg_min_width = (best_pt, tuple(float(x) for x in proj_pt))
        parallel_lines_data = (best_p1, best_p2, best_pt)

        return float(min_width), seg_min_width, parallel_lines_data

    # def width(self):
    #     vertices = [vv.get_xy() for vv in self.vertices]
    #     vertice_lists = [[x,y] for (x,y) in vertices]
    #     return minimum_width(np.array(vertice_lists))

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

    def convex_hull_area(self):
        """Compute the area of the convex hull in triangle units."""
        hull = self.convex_hull()
        if len(hull) < 3:
            return 0
        s = 0
        N = len(hull)
        for i in range(N):
            s += hull[i].x * hull[(i+1)%N].y - hull[(i+1)%N].x * hull[i].y
        return abs(s)

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

    def get_inertia_tensor(self):
        """Compute the planar area moment of inertia tensor about the origin
        (the first polyiamond vertex) for a uniform unit-density lamina
        bounded by the polyiamond's sides.

        Returns a ``(2, 2)`` ``float`` NumPy array::

            I = [[  ∫ y²  dA,  - ∫ x y dA ],
                 [- ∫ x y dA,    ∫ x²  dA ]]

        Computation
        -----------
        Rather than discretising the interior into a brute-force pixel/triangle
        grid, the surface integrals are converted to **closed-form polygon
        boundary sums** via Green's theorem.  For a polygon with vertices
        ``(x_i, y_i)`` traversed CCW and ``c_i = x_i·y_{i+1} − x_{i+1}·y_i``::

            ∫ x²  dA = (1/12) Σ c_i · (x_i² + x_i x_{i+1} + x_{i+1}²)
            ∫ y²  dA = (1/12) Σ c_i · (y_i² + y_i y_{i+1} + y_{i+1}²)
            ∫ x y dA = (1/24) Σ c_i · (x_i y_{i+1} + 2 x_i y_i
                                       + 2 x_{i+1} y_{i+1} + x_{i+1} y_i)

        Each sum is implemented with a single NumPy vectorised expression over
        the ``N`` vertices — i.e. ``O(N)`` floating-point ops with no
        interior sampling.  That is dramatically faster than any
        rasterised/quadrature approach (which would scale with the **area**),
        and it maps directly to GPU array libraries (CuPy / JAX): every step
        is an element-wise op or a reduction over the vertex axis.  Multiple
        polyiamonds can be batched by stacking their padded vertex arrays into
        a leading batch dimension.

        Sign convention: if the polygon is traversed CW (negative signed
        area), the boundary sums above all change sign; the result is
        multiplied by ``sign(signed_area)`` so the returned tensor always
        corresponds to the geometric region with positive area.
        """
        if not hasattr(self, 'inertia_tensor'):
            self.get_descartes()
            verts = np.asarray(self.descartes, dtype=float)
            x = verts[:, 0]
            y = verts[:, 1]
            x1 = np.roll(x, -1)
            y1 = np.roll(y, -1)
            cross = x * y1 - x1 * y                             # c_i

            int_xx = np.sum(cross * (x*x + x*x1 + x1*x1)) / 12.0
            int_yy = np.sum(cross * (y*y + y*y1 + y1*y1)) / 12.0
            int_xy = np.sum(cross * (x*y1 + 2.0*x*y
                                     + 2.0*x1*y1 + x1*y)) / 24.0

            signed_area_real = 0.5 * float(np.sum(cross))
            sign = 1.0 if signed_area_real >= 0.0 else -1.0
            int_xx *= sign
            int_yy *= sign
            int_xy *= sign

            self.inertia_tensor = np.array(
                [[int_yy, -int_xy],
                 [-int_xy, int_xx]],
                dtype=float,
            )
        return self.inertia_tensor

    # ------------------------------------------------------------------

    @staticmethod
    def _hex_perimeter_distances(points, cx, cy, theta, apothem):
        """Vectorised distance from each row of ``points`` (shape ``(N, 2)``)
        to the perimeter of the regular hexagon with given centre, orientation
        ``theta`` and apothem ``apothem``.

        All work is element-wise NumPy on broadcast-compatible arrays of
        shape ``(N, 6)`` (one column per hexagon edge), so the same routine
        runs unchanged on CuPy / JAX device arrays for batched evaluation.
        """
        side = 2.0 * apothem / math.sqrt(3.0)
        # Hexagon vertices: at angles theta + pi/6 + k*pi/3, distance ``side``
        # from centre (vertex distance == side length for a regular hexagon).
        ks = np.arange(6)
        ang = theta + math.pi / 6.0 + ks * (math.pi / 3.0)
        hx = cx + side * np.cos(ang)
        hy = cy + side * np.sin(ang)
        ax = hx[None, :]                       # (1, 6) edge start x
        ay = hy[None, :]
        bx = np.roll(hx, -1)[None, :]          # (1, 6) edge end x
        by = np.roll(hy, -1)[None, :]
        px = points[:, 0:1]                    # (N, 1)
        py = points[:, 1:2]
        abx = bx - ax
        aby = by - ay
        apx = px - ax
        apy = py - ay
        ab_len2 = abx * abx + aby * aby        # (1, 6) > 0
        t = np.clip((apx * abx + apy * aby) / ab_len2, 0.0, 1.0)
        qx = ax + t * abx
        qy = ay + t * aby
        seg_d = np.sqrt((px - qx) ** 2 + (py - qy) ** 2)   # (N, 6)
        return seg_d.min(axis=1)               # (N,)

    def get_closest_hausdorff_hexagon(self, n_angles=60, n_apothem=11,
                                      n_centre=7, refine=True):
        """Find a regular hexagon ``S`` minimising the one-sided Hausdorff
        distance from the polyiamond's vertices to the hexagon's perimeter::

            h(P, S) = max_{v ∈ vertices(P)}  min_{x ∈ ∂S}  ||v − x||

        Returns
        -------
        (vertices, distance)
            ``vertices`` is a list of 6 ``(x, y)`` floats (CCW order); the
            first vertex is the one whose outward direction is at angle
            ``θ + π/6`` from the centre (i.e. the canonical hexagon-vertex
            convention used by :py:meth:`get_smallest_hexagon`).
            ``distance`` is the achieved Hausdorff distance ``h(P, S)``.

        Algorithm
        ---------
        A regular hexagon has 4 real parameters: centre ``(cx, cy)``,
        orientation ``θ ∈ [0, π/3)`` (60° rotational symmetry) and apothem
        ``a > 0``.  The objective ``f(cx, cy, θ, a) = max_v dist(v, ∂S)`` is
        non-smooth (a max-of-distances), so we use a two-stage strategy:

        1. **Vectorised coarse search (GPU-friendly).**  Build a small dense
           grid of candidate ``(θ, a, cx, cy)`` quadruples around an initial
           guess derived from :py:meth:`get_smallest_hexagon` (which already
           supplies a near-optimal orientation and size), evaluate the
           objective for *all* candidates *and* all polyiamond vertices in a
           single broadcast, and pick the best.  The inner kernel is
           :py:meth:`_hex_perimeter_distances` — a pure element-wise
           NumPy/CuPy/JAX expression with shape ``(M, N, 6)`` (M candidates,
           N vertices, 6 edges).
        2. **Local refinement.**  Run a Nelder–Mead minimisation from the
           best grid point.  Nelder–Mead handles the non-smooth ``max``
           objective without derivatives.

        Parameters
        ----------
        n_angles : int
            Number of orientation samples in ``[0, π/3)`` for the coarse
            grid.
        n_apothem : int
            Number of apothem samples (geometrically spaced around the
            initial guess).
        n_centre : int
            Per-axis number of centre offset samples for the coarse grid.
        refine : bool
            If ``True`` (default), follow the coarse search with a
            Nelder–Mead refinement.

        Notes
        -----
        Tie-breaking is implicit: when several optima are numerically tied,
        the one found first by the optimiser is returned (the spec allows
        any optimum).
        """
        from scipy.optimize import minimize

        # --- Initial guess from the smallest enclosing regular hexagon. -----
        init_hex = np.asarray(self.get_smallest_hexagon(), dtype=float)
        cx0, cy0 = init_hex.mean(axis=0)
        # apothem = distance from centre to midpoint of an edge
        mid01 = 0.5 * (init_hex[0] + init_hex[1])
        a0 = float(np.hypot(mid01[0] - cx0, mid01[1] - cy0))
        # orientation: edge-midpoint direction is at angle theta + pi/6 + pi/6
        # (vertex 0 sits at theta+pi/6; midpoint between v0,v1 sits at
        # theta + pi/6 + pi/6 = theta + pi/3).  Recover theta:
        theta0 = math.atan2(mid01[1] - cy0, mid01[0] - cx0) - math.pi / 3.0
        theta0 = (theta0 % (math.pi / 3.0))   # fold to fundamental domain

        verts = self._hull_xy_array() if len(self.vertices) >= 3 \
            else np.array([p.get_xy() for p in self.vertices], dtype=float)
        # NB: the Hausdorff distance is determined by the *extreme* vertices;
        # using the convex hull is sufficient and dramatically faster.

        # --- Stage 1: vectorised coarse grid around the initial guess. ------
        thetas = np.linspace(0.0, math.pi / 3.0, n_angles, endpoint=False)
        apothems = a0 * np.linspace(0.5, 1.0, n_apothem)
        span = 0.5 * a0
        offs = np.linspace(-span, span, n_centre)
        # All combinations: shape (n_angles, n_apothem, n_centre, n_centre)
        TH, AP, CX, CY = np.meshgrid(thetas, apothems,
                                     cx0 + offs, cy0 + offs, indexing='ij')
        TH_f = TH.ravel(); AP_f = AP.ravel()
        CX_f = CX.ravel(); CY_f = CY.ravel()
        M = TH_f.size

        # Hexagon vertex coordinates per candidate, shape (M, 6).
        ks = np.arange(6)
        ang = TH_f[:, None] + math.pi / 6.0 + ks[None, :] * (math.pi / 3.0)
        side = 2.0 * AP_f / math.sqrt(3.0)
        hx = CX_f[:, None] + side[:, None] * np.cos(ang)        # (M, 6)
        hy = CY_f[:, None] + side[:, None] * np.sin(ang)
        ax = hx[:, None, :]                                     # (M, 1, 6)
        ay = hy[:, None, :]
        bx = np.roll(hx, -1, axis=1)[:, None, :]
        by = np.roll(hy, -1, axis=1)[:, None, :]
        # Polyiamond hull vertices, shape (1, N, 1).
        N = verts.shape[0]
        px = verts[:, 0][None, :, None]
        py = verts[:, 1][None, :, None]
        abx = bx - ax; aby = by - ay
        apx = px - ax; apy = py - ay
        ab_len2 = abx * abx + aby * aby                         # (M, 1, 6)
        t = np.clip((apx * abx + apy * aby) / ab_len2, 0.0, 1.0)
        qx = ax + t * abx
        qy = ay + t * aby
        seg_d = np.sqrt((px - qx) ** 2 + (py - qy) ** 2)        # (M, N, 6)
        per_vertex_min = seg_d.min(axis=2)                      # (M, N)
        haus = per_vertex_min.max(axis=1)                       # (M,)
        best_idx = int(np.argmin(haus))
        h_best = float(haus[best_idx])
        th_best = float(TH_f[best_idx])
        a_best = float(AP_f[best_idx])
        cx_best = float(CX_f[best_idx])
        cy_best = float(CY_f[best_idx])

        # --- Stage 2: Nelder–Mead refinement. ------------------------------
        if refine:
            def _obj(p):
                cx, cy, th, a = p
                if a <= 1e-12:
                    return 1e18
                return float(self._hex_perimeter_distances(
                    verts, cx, cy, th, a).max())

            x0 = np.array([cx_best, cy_best, th_best, a_best], dtype=float)
            scale = max(a_best, 1e-6)
            initial_simplex = np.vstack([
                x0,
                x0 + [scale * 0.05, 0.0,           0.0,            0.0          ],
                x0 + [0.0,          scale * 0.05,  0.0,            0.0          ],
                x0 + [0.0,          0.0,           math.pi / 180., 0.0          ],
                x0 + [0.0,          0.0,           0.0,            scale * 0.05 ],
            ])
            res = minimize(_obj, x0, method='Nelder-Mead',
                           options={'xatol': 1e-10, 'fatol': 1e-12,
                                    'maxiter': 5000, 'maxfev': 10000,
                                    'initial_simplex': initial_simplex})
            if res.fun < h_best:
                cx_best, cy_best, th_best, a_best = (float(v) for v in res.x)
                h_best = float(res.fun)

        # --- Build the 6 hexagon vertices in CCW order. --------------------
        side = 2.0 * a_best / math.sqrt(3.0)
        verts_out = []
        for k in range(6):
            ang = th_best + math.pi / 6.0 + k * (math.pi / 3.0)
            verts_out.append((cx_best + side * math.cos(ang),
                              cy_best + side * math.sin(ang)))
        return verts_out, h_best

    # ------------------------------------------------------------------

    @staticmethod
    def _tri_perimeter_distances(points, cx, cy, theta, side):
        """Vectorised distance from each row of ``points`` (shape ``(N, 2)``)
        to the perimeter of the equilateral triangle with given centre,
        orientation ``theta`` and side length ``side``.

        Triangle vertex ``k`` (``k = 0, 1, 2``) sits at angle
        ``theta + π/2 + k·2π/3`` from the centre, at distance
        ``side / √3`` (the circumradius).  All work is element-wise NumPy
        on broadcast-compatible arrays of shape ``(N, 3)`` (one column per
        triangle edge), so the same routine runs unchanged on CuPy / JAX
        device arrays for batched evaluation.
        """
        R = side / math.sqrt(3.0)            # circumradius
        ks = np.arange(3)
        ang = theta + math.pi / 2.0 + ks * (2.0 * math.pi / 3.0)
        hx = cx + R * np.cos(ang)
        hy = cy + R * np.sin(ang)
        ax = hx[None, :]                     # (1, 3)
        ay = hy[None, :]
        bx = np.roll(hx, -1)[None, :]
        by = np.roll(hy, -1)[None, :]
        px = points[:, 0:1]                  # (N, 1)
        py = points[:, 1:2]
        abx = bx - ax; aby = by - ay
        apx = px - ax; apy = py - ay
        ab_len2 = abx * abx + aby * aby      # (1, 3) > 0
        t = np.clip((apx * abx + apy * aby) / ab_len2, 0.0, 1.0)
        qx = ax + t * abx
        qy = ay + t * aby
        seg_d = np.sqrt((px - qx) ** 2 + (py - qy) ** 2)   # (N, 3)
        return seg_d.min(axis=1)             # (N,)

    def get_closest_hausdorff_triangle(self, n_angles=120, n_side=11,
                                       n_centre=7, refine=True):
        """Find an equilateral triangle ``T`` minimising the one-sided
        Hausdorff distance from the polyiamond's vertices to the triangle's
        perimeter::

            h(P, T) = max_{v ∈ vertices(P)}  min_{x ∈ ∂T}  ||v − x||

        Returns
        -------
        (vertices, distance)
            ``vertices`` is a list of 3 ``(x, y)`` floats (CCW order); the
            first vertex is at angle ``θ + π/2`` from the centre (the
            "apex-up" canonical convention used by
            :py:meth:`get_smallest_triangle`).
            ``distance`` is the achieved Hausdorff distance ``h(P, T)``.

        Algorithm
        ---------
        An equilateral triangle has 4 real degrees of freedom: centre
        ``(cx, cy)``, orientation ``θ ∈ [0, 2π/3)`` (120° rotational
        symmetry) and side length ``s > 0``.  The objective
        ``f(cx, cy, θ, s) = max_v dist(v, ∂T)`` is non-smooth (a
        max-of-distances), so a two-stage strategy is used — identical in
        spirit to :py:meth:`get_closest_hausdorff_hexagon`:

        1. **Vectorised coarse search (GPU-friendly).**  Build a small
           dense 4-D grid of candidate ``(θ, s, cx, cy)`` quadruples
           around an initial guess derived from
           :py:meth:`get_smallest_triangle`, evaluate the objective for
           *all* candidates *and* all (convex-hull) polyiamond vertices in
           a single broadcast of shape ``(M, N, 3)`` (M candidates, N
           vertices, 3 triangle edges).  The inner kernel
           :py:meth:`_tri_perimeter_distances` is a pure element-wise
           NumPy/CuPy/JAX expression.
        2. **Local refinement.**  Nelder–Mead from the best grid point —
           derivative-free, so it tolerates the non-smooth ``max``.

        Parameters
        ----------
        n_angles : int
            Number of orientation samples in ``[0, 2π/3)`` for the coarse
            grid.
        n_side : int
            Number of triangle-side samples (linearly spaced around the
            initial guess; range ``[0.5·s0, 1.0·s0]`` where ``s0`` is the
            side of the smallest enclosing equilateral triangle).
        n_centre : int
            Per-axis number of centre offset samples for the coarse grid.
        refine : bool
            If ``True`` (default), follow the coarse search with a
            Nelder–Mead refinement.

        Notes
        -----
        Tie-breaking is implicit: when several optima are numerically tied,
        the one found first by the optimiser is returned (the spec allows
        any optimum).
        """
        from scipy.optimize import minimize

        # --- Initial guess from the smallest enclosing triangle. -----------
        init_tri = np.asarray(self.get_smallest_triangle(), dtype=float)
        cx0, cy0 = init_tri.mean(axis=0)
        # Side length: distance between any two consecutive vertices.
        s0 = float(np.hypot(init_tri[1, 0] - init_tri[0, 0],
                            init_tri[1, 1] - init_tri[0, 1]))
        # Orientation: vertex 0 sits at angle theta + pi/2 from the centre.
        theta0 = math.atan2(init_tri[0, 1] - cy0,
                            init_tri[0, 0] - cx0) - math.pi / 2.0
        theta0 = (theta0 % (2.0 * math.pi / 3.0))   # fold to fundamental domain

        verts = self._hull_xy_array() if len(self.vertices) >= 3 \
            else np.array([p.get_xy() for p in self.vertices], dtype=float)

        # --- Stage 1: vectorised coarse grid. ------------------------------
        thetas = np.linspace(0.0, 2.0 * math.pi / 3.0, n_angles, endpoint=False)
        sides_grid = s0 * np.linspace(0.5, 1.0, n_side)
        span = 0.5 * s0
        offs = np.linspace(-span, span, n_centre)
        TH, SD, CX, CY = np.meshgrid(thetas, sides_grid,
                                     cx0 + offs, cy0 + offs, indexing='ij')
        TH_f = TH.ravel(); SD_f = SD.ravel()
        CX_f = CX.ravel(); CY_f = CY.ravel()

        # Triangle vertex coordinates per candidate, shape (M, 3).
        ks = np.arange(3)
        ang = TH_f[:, None] + math.pi / 2.0 + ks[None, :] * (2.0 * math.pi / 3.0)
        R = SD_f / math.sqrt(3.0)                               # circumradius
        hx = CX_f[:, None] + R[:, None] * np.cos(ang)           # (M, 3)
        hy = CY_f[:, None] + R[:, None] * np.sin(ang)
        ax = hx[:, None, :]; ay = hy[:, None, :]                # (M, 1, 3)
        bx = np.roll(hx, -1, axis=1)[:, None, :]
        by = np.roll(hy, -1, axis=1)[:, None, :]
        px = verts[:, 0][None, :, None]                         # (1, N, 1)
        py = verts[:, 1][None, :, None]
        abx = bx - ax; aby = by - ay
        apx = px - ax; apy = py - ay
        ab_len2 = abx * abx + aby * aby                         # (M, 1, 3)
        t = np.clip((apx * abx + apy * aby) / ab_len2, 0.0, 1.0)
        qx = ax + t * abx
        qy = ay + t * aby
        seg_d = np.sqrt((px - qx) ** 2 + (py - qy) ** 2)        # (M, N, 3)
        per_vertex_min = seg_d.min(axis=2)                      # (M, N)
        haus = per_vertex_min.max(axis=1)                       # (M,)
        best_idx = int(np.argmin(haus))
        h_best = float(haus[best_idx])
        th_best = float(TH_f[best_idx])
        s_best = float(SD_f[best_idx])
        cx_best = float(CX_f[best_idx])
        cy_best = float(CY_f[best_idx])

        # --- Stage 2: Nelder–Mead refinement. ------------------------------
        if refine:
            def _obj(p):
                cx, cy, th, s = p
                if s <= 1e-12:
                    return 1e18
                return float(self._tri_perimeter_distances(
                    verts, cx, cy, th, s).max())

            x0 = np.array([cx_best, cy_best, th_best, s_best], dtype=float)
            scale = max(s_best, 1e-6)
            initial_simplex = np.vstack([
                x0,
                x0 + [scale * 0.05, 0.0,           0.0,            0.0          ],
                x0 + [0.0,          scale * 0.05,  0.0,            0.0          ],
                x0 + [0.0,          0.0,           math.pi / 180., 0.0          ],
                x0 + [0.0,          0.0,           0.0,            scale * 0.05 ],
            ])
            res = minimize(_obj, x0, method='Nelder-Mead',
                           options={'xatol': 1e-10, 'fatol': 1e-12,
                                    'maxiter': 5000, 'maxfev': 10000,
                                    'initial_simplex': initial_simplex})
            if res.fun < h_best:
                cx_best, cy_best, th_best, s_best = (float(v) for v in res.x)
                h_best = float(res.fun)

        # --- Build the 3 triangle vertices in CCW order. -------------------
        R = s_best / math.sqrt(3.0)
        verts_out = []
        for k in range(3):
            ang = th_best + math.pi / 2.0 + k * (2.0 * math.pi / 3.0)
            verts_out.append((cx_best + R * math.cos(ang),
                              cy_best + R * math.sin(ang)))
        return verts_out, h_best

    # ------------------------------------------------------------------

    @staticmethod
    def _polygon_edge_distances(poly_xy, px, py):
        """Vectorised distance from each query point ``(px[i], py[i])`` to
        every edge of the polygon ``poly_xy`` (shape ``(E, 2)``, CCW or CW
        irrelevant).

        Returns a ``(N, E)`` array of point-to-segment distances using a
        single broadcast of clamped projections.  Pure element-wise NumPy
        — ports unchanged to CuPy / JAX.
        """
        x1 = poly_xy[:, 0]; y1 = poly_xy[:, 1]
        x2 = np.roll(x1, -1); y2 = np.roll(y1, -1)
        ax = x1[None, :]; ay = y1[None, :]                 # (1, E)
        bx = x2[None, :]; by = y2[None, :]
        qx = px[:, None];  qy = py[:, None]                # (N, 1)
        abx = bx - ax; aby = by - ay
        apx = qx - ax; apy = qy - ay
        ab_len2 = abx * abx + aby * aby
        # Avoid divide-by-zero on degenerate (zero-length) edges.
        ab_len2 = np.where(ab_len2 > 0, ab_len2, 1.0)
        t = np.clip((apx * abx + apy * aby) / ab_len2, 0.0, 1.0)
        proj_x = ax + t * abx
        proj_y = ay + t * aby
        return np.sqrt((qx - proj_x) ** 2 + (qy - proj_y) ** 2)   # (N, E)

    @staticmethod
    def _points_in_polygon(poly_xy, px, py):
        """Vectorised even-odd ray-casting point-in-polygon test.

        ``poly_xy``: ``(E, 2)`` polygon vertices (any orientation).
        ``px``, ``py``: ``(N,)`` query coordinates.

        Returns a boolean array of shape ``(N,)``.  Pure NumPy element-wise
        broadcasting — runs unchanged on CuPy / JAX device arrays.
        """
        x1 = poly_xy[:, 0]; y1 = poly_xy[:, 1]
        x2 = np.roll(x1, -1); y2 = np.roll(y1, -1)
        # (E, 1) edges  vs  (1, N) query points
        y1c = y1[:, None]; y2c = y2[:, None]
        x1c = x1[:, None]; x2c = x2[:, None]
        qx = px[None, :];  qy = py[None, :]
        crosses_y = (y1c > qy) != (y2c > qy)
        # avoid div-by-zero on horizontal edges; result is masked out by crosses_y
        dy = np.where(y2c - y1c == 0, 1.0, y2c - y1c)
        x_intersect = (qy - y1c) * (x2c - x1c) / dy + x1c
        cond = crosses_y & (qx < x_intersect)
        return (np.sum(cond, axis=0) % 2) == 1            # (N,)

    def get_incircle(self, n_grid=80, refine=True):
        """Find the largest circle that lies entirely inside the polyiamond
        (an inscribed circle / "inradius").

        Returns
        -------
        ((cx, cy), r) : tuple
            Centre as a pair of floats and radius as a float.

        Algorithm
        ---------
        The inscribed-circle problem on a (possibly non-convex) simple
        polygon ``P`` is::

            r* = max_{c ∈ P} dist(c, ∂P)

        i.e. the maximum, over interior points ``c``, of the distance from
        ``c`` to the polygon boundary.  The objective is non-smooth (it is
        a min-of-distances) so a derivative-free strategy is used:

        1. **Vectorised coarse grid (GPU-friendly).**  Build an
           ``n_grid × n_grid`` rectangular sample grid covering the
           polygon's bounding box.  In **one** broadcast:
             * mask out exterior points with a vectorised even-odd
               ray-casting test (:py:meth:`_points_in_polygon`),
             * compute every grid point's distance to every polygon edge
               via :py:meth:`_polygon_edge_distances` and reduce with
               ``min`` over the edge axis.
           The grid point with the largest interior distance is the
           coarse optimum.  Both inner kernels are pure element-wise
           NumPy operations and port unchanged to CuPy / JAX.
        2. **Local refinement.**  ``scipy.optimize.minimize`` (Nelder–
           Mead) maximises the same signed distance starting from the
           coarse optimum.  A penalty term is added when the candidate
           leaves the polygon.

        Note: for a convex polygon the inscribed-circle radius equals the
        Chebyshev radius (a small LP).  We do not branch on convexity —
        the grid-plus-refine algorithm handles both convex and non-convex
        polyiamonds with the same code path.
        """
        from scipy.optimize import minimize

        poly = np.asarray(self.get_descartes(), dtype=float)
        # Bounding box.
        xmin, ymin = poly.min(axis=0)
        xmax, ymax = poly.max(axis=0)

        # Stage 1: vectorised coarse grid.
        gx = np.linspace(xmin, xmax, n_grid)
        gy = np.linspace(ymin, ymax, n_grid)
        GX, GY = np.meshgrid(gx, gy, indexing='ij')
        px = GX.ravel(); py = GY.ravel()
        inside = self._points_in_polygon(poly, px, py)
        if not inside.any():
            # Polyiamond is degenerate; return a zero-radius circle at origin.
            return ((float(poly[0, 0]), float(poly[0, 1])), 0.0)

        d_to_edge = self._polygon_edge_distances(poly, px, py).min(axis=1)
        # Exterior points get distance 0 (so they cannot win the argmax).
        d_to_edge = np.where(inside, d_to_edge, -np.inf)
        best_idx = int(np.argmax(d_to_edge))
        cx_best, cy_best = float(px[best_idx]), float(py[best_idx])
        r_best = float(d_to_edge[best_idx])

        # Stage 2: Nelder–Mead refinement on the signed-distance objective.
        if refine:
            def _neg_radius(p):
                cx, cy = p
                ins = self._points_in_polygon(
                    poly, np.array([cx]), np.array([cy]))[0]
                d = float(self._polygon_edge_distances(
                    poly, np.array([cx]), np.array([cy])).min())
                if not ins:
                    # Strong outside-penalty, smooth in distance to boundary.
                    return d + 1e6
                return -d

            scale = max(min(xmax - xmin, ymax - ymin), 1e-6)
            x0 = np.array([cx_best, cy_best], dtype=float)
            initial_simplex = np.vstack([
                x0,
                x0 + [scale * 0.05, 0.0],
                x0 + [0.0,          scale * 0.05],
            ])
            res = minimize(_neg_radius, x0, method='Nelder-Mead',
                           options={'xatol': 1e-10, 'fatol': 1e-12,
                                    'maxiter': 5000, 'maxfev': 10000,
                                    'initial_simplex': initial_simplex})
            if -res.fun > r_best:
                cx_best, cy_best = float(res.x[0]), float(res.x[1])
                r_best = float(-res.fun)

        return ((cx_best, cy_best), r_best)

    def get_circumcircle(self):
        """Find the smallest circle containing every vertex of the
        polyiamond (the minimum enclosing circle of the vertex set).

        Returns
        -------
        ((cx, cy), r) : tuple
            Centre and radius as floats.

        Algorithm
        ---------
        The smallest enclosing circle of a finite point set equals the
        smallest enclosing circle of its convex hull and is determined by
        either:

        * a **diameter pair** — two hull vertices spanning a circle whose
          diameter is the segment between them, or
        * a **circumscribed triple** — three hull vertices on the circle's
          boundary (the polygon's circumscribed circle for that triple).

        Both candidate sets are enumerated and validated in fully
        vectorised NumPy:

        1. **Diameter candidates.**  All ``H·(H−1)/2`` pairs of hull
           vertices give one circle each (centre = midpoint, radius =
           half-distance).  Validity = every other hull vertex lies
           within radius (one ``(N_pairs, H)`` distance broadcast).
        2. **Triple candidates.**  All ``H·(H−1)·(H−2)/6`` ordered
           triples are converted to circumcircles via the closed-form
           determinant formula::

               D = 2 ((B−A) × (C−A))
               cx = ( |B|²−|A|² )(C_y−A_y) − ( |C|²−|A|² )(B_y−A_y)) / D + A_x
               cy = ( |C|²−|A|² )(B_x−A_x) − ( |B|²−|A|² )(C_x−A_x)) / D + A_y

           Degenerate (collinear) triples have ``D ≈ 0`` and are masked
           out.  Validity is again a single ``(N_triples, H)`` distance
           broadcast.

        The smallest valid radius among both candidate sets is returned.
        Computation cost is ``O(H³)`` in NumPy — for typical polyiamonds
        ``H`` is small (the convex hull of an integer-grid polygon has
        few vertices) so this is dramatically faster than Welzl in pure
        Python and runs unchanged on CuPy / JAX.
        """
        hull_xy = self._hull_xy_array()
        H = hull_xy.shape[0]

        if H == 1:
            return ((float(hull_xy[0, 0]), float(hull_xy[0, 1])), 0.0)
        if H == 2:
            cx = 0.5 * (hull_xy[0, 0] + hull_xy[1, 0])
            cy = 0.5 * (hull_xy[0, 1] + hull_xy[1, 1])
            r = 0.5 * float(np.hypot(hull_xy[1, 0] - hull_xy[0, 0],
                                     hull_xy[1, 1] - hull_xy[0, 1]))
            return ((float(cx), float(cy)), r)

        tol = 1e-9 * float(np.linalg.norm(hull_xy.max(axis=0)
                                          - hull_xy.min(axis=0)))
        tol = max(tol, 1e-12)

        candidates = []   # list of (radius, cx, cy)

        # --- Stage 1: diameter pairs (vectorised). ------------------------
        i_idx, j_idx = np.triu_indices(H, k=1)
        ax = hull_xy[i_idx, 0]; ay = hull_xy[i_idx, 1]
        bx = hull_xy[j_idx, 0]; by = hull_xy[j_idx, 1]
        cx_p = 0.5 * (ax + bx)
        cy_p = 0.5 * (ay + by)
        r_p = 0.5 * np.hypot(bx - ax, by - ay)
        # Validity: every hull vertex within radius (with tolerance).
        d = np.hypot(hull_xy[None, :, 0] - cx_p[:, None],
                     hull_xy[None, :, 1] - cy_p[:, None])
        valid_p = (d <= r_p[:, None] + tol).all(axis=1)
        if valid_p.any():
            best = int(np.argmin(np.where(valid_p, r_p, np.inf)))
            candidates.append((float(r_p[best]),
                               float(cx_p[best]), float(cy_p[best])))

        # --- Stage 2: circumscribed triples (vectorised). -----------------
        # Build all unordered triples (i < j < k).
        ii, jj, kk = np.array(np.meshgrid(np.arange(H), np.arange(H),
                                          np.arange(H), indexing='ij'))
        mask = (ii < jj) & (jj < kk)
        i3 = ii[mask]; j3 = jj[mask]; k3 = kk[mask]
        Ax = hull_xy[i3, 0]; Ay = hull_xy[i3, 1]
        Bx = hull_xy[j3, 0]; By = hull_xy[j3, 1]
        Cx = hull_xy[k3, 0]; Cy = hull_xy[k3, 1]
        D = 2.0 * ((Bx - Ax) * (Cy - Ay) - (By - Ay) * (Cx - Ax))
        nondeg = np.abs(D) > 1e-14
        Dsafe = np.where(nondeg, D, 1.0)
        ABsq = (Bx - Ax) ** 2 + (By - Ay) ** 2
        # Use cofactor formulas relative to A.
        # ux = ((B-A)·(B-A)) (Cy-Ay) - ((C-A)·(C-A)) (By-Ay)  ... etc.
        Bx2 = (Bx - Ax) ** 2 + (By - Ay) ** 2
        Cx2 = (Cx - Ax) ** 2 + (Cy - Ay) ** 2
        ux = (Bx2 * (Cy - Ay) - Cx2 * (By - Ay)) / Dsafe
        uy = (Cx2 * (Bx - Ax) - Bx2 * (Cx - Ax)) / Dsafe
        cx_t = Ax + ux
        cy_t = Ay + uy
        r_t = np.hypot(ux, uy)
        d3 = np.hypot(hull_xy[None, :, 0] - cx_t[:, None],
                      hull_xy[None, :, 1] - cy_t[:, None])
        valid_t = nondeg & (d3 <= r_t[:, None] + tol).all(axis=1)
        if valid_t.any():
            r_masked = np.where(valid_t, r_t, np.inf)
            best = int(np.argmin(r_masked))
            candidates.append((float(r_t[best]),
                               float(cx_t[best]), float(cy_t[best])))

        if not candidates:
            # Defensive fallback (should not happen for valid polyiamond).
            cx = float(hull_xy[:, 0].mean())
            cy = float(hull_xy[:, 1].mean())
            r = float(np.hypot(hull_xy[:, 0] - cx,
                               hull_xy[:, 1] - cy).max())
            return ((cx, cy), r)

        candidates.sort(key=lambda t: t[0])
        r_best, cx_best, cy_best = candidates[0]
        return ((cx_best, cy_best), r_best)

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