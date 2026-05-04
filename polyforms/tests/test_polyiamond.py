from polyforms.polyiamond import Polyiamond
from polyforms.polyiamond import get_minimal_bounding_sizes
from polyforms.point_tg import *
from polyforms.perfect_seq import PerfectSeq

def test_bounding_hexagon():
    p1 = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    p1.setup()
    result = p1.get_hex_bounds()
    assert result == (-4, 0, -5, 1, 0, 5)

def test_bounding_box():
    p1 = Polyiamond([(5,'A'), (4,'C'), (3,'E'), (2,'D'), (1,'F')])
    p1.setup()
    bounds = p1.get_bounding_sizes()
    # print('bounds = {}'.format(bounds))
    assert bounds == (4, 6, 5)

def test_direction_counts():
    p1 = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    p1.setup()
    counts = p1.get_direction_counts()
    # print('bounds = {}'.format(bounds))
    assert counts == (7, 3, 5)

def test_is_inside3():
    p1 = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    # p1.setup()
    assert not p1.is_inside(PointTg(0, 0, 0))
    assert not p1.is_inside(AA)
    assert not p1.is_inside(BB)
    assert not p1.is_inside(CC)
    assert not p1.is_inside(AA + BB)
    assert p1.is_inside(2*AA + BB)
    assert p1.is_inside(2*AA + 2*BB)
    assert p1.is_inside(3*AA + BB)
    assert not p1.is_inside(5*AA)
    assert not p1.is_inside(4*AA + BB)


def test_winding_number():
    p1 = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    p1.setup()
    assert p1.winding_number(AA + BB) == 0
    assert p1.winding_number(2*AA + BB) == -1
    assert p1.winding_number(AA + 2*BB) == 0

def test_perimeter_points():
    p1 = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    all_points = p1.list_perimeter()
    for pt in all_points:
        assert not p1.is_inside(pt)

def test_long_perimeter_points():
    polyiamonds = ['ACACACACAEAEAEAEAECECECECEAECECECECECECECACAEACAEAC',
                   'ACECECEAEAEAEAEACACACACECEAECECECACACECACACACECACAE',
                   'ABABABCEDEDEDEDEDEFEFAC',
                   'ACEDFEFEFBCBCBFBCBCBDCB']
    for pp in polyiamonds:
        sides = list(zip(range(len(pp), 0, -1), list(pp)))
        pmond = Polyiamond(sides)
        all_points = pmond.list_perimeter()
        for pt in all_points:
            #if pmond.is_inside(pt):
            #    print('pp = {}, pt = {}'.format(pp, pt))
            assert not pmond.is_inside(pt)

def test_large_polygon():
    pp = 'ACACACACAEAEAEAEAECECECECEAECECECECECECECACAEACAEAC'
    pt = PointTg(51, -3, -48)
    pmond = Polyiamond(list(zip(range(len(pp), 0, -1), list(pp))))
    assert not pmond.is_inside(pt)


def test_get_min_bounding_box():
    perfect_nine_dir = ['ABFDEDCDC', 'ACECEAEAC', 'ACEDEABAC']
    perfect_nine_poly = [Polyiamond(list(zip(range(len(pp), 0, -1), list(pp)))) for pp in perfect_nine_dir]
    sublist = get_minimal_bounding_sizes(perfect_nine_poly)
    sublist_codes = [''.join([t[1] for t in poly.sides]) for poly in sublist]
    assert sublist_codes == ['ACECEAEAC']

def test_polyiamond_isvalid():
    seq0 = 'ACBACBDFEDFEDFEDFEACBAC'
    p0 = Polyiamond(list(zip(range(len(seq0), 0, -1), list(seq0))))
    assert p0.is_valid()

    seq1 = 'ACBABCBDFEDFDFEDFEDEFEACBFCFC'
    p1 = Polyiamond(list(zip(range(len(seq1), 0, -1), list(seq1))))
    assert not p1.is_valid()

    seq2 = 'ACBACBACBDFEDFDEFEDFEDFEDFEACBACFBC'
    p2= Polyiamond(list(zip(range(len(seq2), 0, -1), list(seq2))))
    assert not p2.is_valid()


def test_polyseq6_isvalid():
    perfectSeq = PerfectSeq()
    pSequence = perfectSeq.pseq['SEQ_6_5_B']
    for n in range(0, 6):
        p = Polyiamond(pSequence.get(n))
        assert p.is_valid()

def test_list_inside():
    pp = Polyiamond('ACEDF')
    result = pp.list_inside()
    assert len(result) == 18

def test_list_triangles():
    # pp = Polyiamond('ACDCEAEACAEAECEAEAC')
    pp = Polyiamond('ACEDF')
    area = pp.get_area()
    triangles = pp.list_triangles()
    assert len(triangles) == area


# ---------------------------------------------------------------------------
# Tests for the exact-integer implementations added in 2026-04:
#   get_signed_area, get_area, winding_number (integer version), diameter_sq
# ---------------------------------------------------------------------------

def test_signed_area_integer_type():
    """get_signed_area must return a Python int, not a float."""
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    result = p.get_signed_area()
    assert isinstance(result, int)


def test_signed_area_basic():
    """Known value: the (5A 4C 3E 2D 1F) polyiamond has signed area 19."""
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    assert p.get_signed_area() == 19

def test_largest_areas():
    print("Testing get_area on larger shapes...")

    shapes = [
        list(zip(range(12, 0, -1), list('ABCDEDEFAFAB'))),
        list(zip(range(18, 0, -1), list('ABAFEDEDEDCBCBCBAB'))),
        list(zip(range(24, 0, -1), list('ABAFEFEDEDCDCBCDCBABABAB'))),
        list(zip(range(30, 0, -1), list('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF'))),
        list(zip(range(36, 0, -1), list('ABABCBCDCDCDEDEFEFEFEFEFAFAFAFABABCB'))),
        list(zip(range(42, 0, -1), list('ABABCBCBCDCDEDEDEDEFEFEFEFAFAFAFAFAFABABCB'))),
        list(zip(range(48, 0, -1), list('ABABCBCDCDCDCDEDEDEFEFEFEFAFAFAFAFAFABABABAFABCB')))
    ]

    expected_areas = [820, 2997, 10178, 25617, 54692, 101621, 170018]

    for sides, expected in zip(shapes, expected_areas):
        p = Polyiamond(sides)
        actual_area = p.get_area()
        assert actual_area == expected, f"Expected area {expected} but got {actual_area} for shape with sides {sides}"

def test_area_equals_abs_signed_area():
    """get_area == abs(get_signed_area) for all test shapes."""
    shapes = [
        [(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')],
        list(zip(range(9, 0, -1), list('ABFDEDCDC'))),
        list(zip(range(9, 0, -1), list('ACECEAEAC'))),
    ]
    for sides in shapes:
        p = Polyiamond(sides)
        assert p.get_area() == abs(p.get_signed_area())


def test_signed_area_orientation_sign():
    """Reversing traversal direction negates the signed area."""
    sides_fwd = [(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')]
    # The same polygon traversed CW has opposite direction letters (A<->D, B<->E, C<->F).
    sides_rev = [(1, 'C'), (2, 'A'), (3, 'B'), (4, 'F'), (5, 'D')]
    p_fwd = Polyiamond(sides_fwd)
    p_rev = Polyiamond(sides_rev)
    assert p_fwd.get_signed_area() == -p_rev.get_signed_area()


def test_signed_area_large_integers():
    """Exact integer arithmetic must handle large side lengths without overflow
    or floating-point rounding (Python ints are arbitrary precision)."""
    # Scale sides by 1000; area should scale by 1000^2 = 1_000_000.
    scale = 1000
    sides_small = [(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')]
    sides_large = [(L * scale, D) for (L, D) in sides_small]
    p_small = Polyiamond(sides_small)
    p_large = Polyiamond(sides_large)
    assert p_large.get_signed_area() == p_small.get_signed_area() * scale * scale


def test_winding_number_interior():
    """Winding number for a clearly interior point equals -1 (CCW polygon convention)."""
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    # 2*AA + 2*BB is well inside the polygon
    assert p.winding_number(2 * AA + 2 * BB) == -1


def test_winding_number_exterior():
    """Winding number for an exterior point equals 0."""
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    assert p.winding_number(10 * AA) == 0
    assert p.winding_number(PointTg(0, 0, 0)) == 0  # origin is a vertex -> boundary -> 0


def test_winding_number_consistent_with_is_inside():
    """winding_number != 0 iff is_inside returns True."""
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    # sample a grid of points
    for a in range(-2, 8):
        for b in range(-2, 8):
            pt = PointTg(a, b, -a - b)
            wn = p.winding_number(pt)
            inside = p.is_inside(pt)
            assert (wn != 0) == inside, f"Mismatch at {pt}: winding={wn}, is_inside={inside}"


def test_diameter_sq_integer_type():
    """diameter_sq must return (int, int, int)."""
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    d2, i, j = p.diameter_sq()
    assert isinstance(d2, int)
    assert isinstance(i, int)
    assert isinstance(j, int)


def test_diameter_sq_consistent_with_diameter():
    """diameter_sq and diameter should be consistent: d^2 == d2 * (1/2)^2 in real coords.

    DESCARTES2 coords are 2x the mod-Cartesian coords, and mod-Cartesian y is
    the actual triangle-height unit (1 = sqrt(3)/2 in real lengths).  So the
    squared Euclidean distance in real units is::

        real_dist^2 = (dx_d2/2)^2 + (dy_d2/2 * sqrt(3)/2)^2
                    = dx_d2^2/4 + 3*dy_d2^2/16

    which is irrational in general.  We only check ordering: the pair achieving
    diameter_sq also achieves the maximum real distance.
    """
    import math
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    d2_val, i_sq, j_sq = p.diameter_sq()
    d_val, i_fl, j_fl = p.diameter()
    # The diameter() function uses floating-point L2 distances; the maximising
    # pair of vertices should be the same (or symmetrically equivalent).
    assert i_sq == i_fl and j_sq == j_fl


def test_diameter_sq_scales_quadratically():
    """Scaling side lengths by k scales diameter_sq by k^2."""
    k = 7
    sides_small = [(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')]
    sides_large = [(L * k, D) for (L, D) in sides_small]
    p_small = Polyiamond(sides_small)
    p_large = Polyiamond(sides_large)
    d2_small, _, _ = p_small.diameter_sq()
    d2_large, _, _ = p_large.diameter_sq()
    assert d2_large == d2_small * k * k


# ---------------------------------------------------------------------------
# Tests for the convex hull and minimum-enclosing-shape methods (2026-04-30).
# ---------------------------------------------------------------------------

import math
import numpy as np


_EPS = 1e-7  # numerical slack for "is the polyiamond inside this shape?" checks


def _hull_vertices_xy(p):
    """Real-Cartesian coordinates of all polyiamond vertices."""
    return np.array([v.get_xy() for v in p.vertices], dtype=float)


def _point_in_convex_polygon(pt, poly_verts_ccw):
    """True iff *pt* lies inside (or on boundary of) the convex CCW polygon."""
    n = len(poly_verts_ccw)
    for i in range(n):
        x1, y1 = poly_verts_ccw[i]
        x2, y2 = poly_verts_ccw[(i + 1) % n]
        # cross product (edge) x (edge -> pt) should be >= 0 for CCW polygon
        cross = (x2 - x1) * (pt[1] - y1) - (y2 - y1) * (pt[0] - x1)
        if cross < -_EPS:
            return False
    return True


# ---- convex_hull ----------------------------------------------------------

def test_convex_hull_returns_pointtg():
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    hull = p.convex_hull()
    assert len(hull) >= 3
    for v in hull:
        assert isinstance(v, PointTg)


def test_convex_hull_contains_all_vertices():
    """Every polyiamond vertex must lie inside the convex hull."""
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    hull_xy = [v.get_xy() for v in p.convex_hull()]
    for v in p.vertices:
        assert _point_in_convex_polygon(v.get_xy(), hull_xy)


def test_convex_hull_is_ccw():
    """Hull edges should be CCW: the signed area is positive."""
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    hull_xy = [v.get_xy() for v in p.convex_hull()]
    n = len(hull_xy)
    s = 0.0
    for i in range(n):
        x1, y1 = hull_xy[i]
        x2, y2 = hull_xy[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    assert s > 0


def test_convex_hull_triangle_polyiamond():
    """A single triangle 'ACE' has exactly 3 hull vertices."""
    p = Polyiamond('ACE')
    hull = p.convex_hull()
    assert len(hull) == 3


# ---- get_smallest_hexagon -------------------------------------------------

def _hexagon_side_length(verts):
    """Side length of a polygon given as list of (x,y) tuples."""
    return math.hypot(verts[1][0] - verts[0][0], verts[1][1] - verts[0][1])


def _hexagon_is_regular(verts, tol=1e-6):
    sides = [math.hypot(verts[(i+1) % 6][0] - verts[i][0],
                        verts[(i+1) % 6][1] - verts[i][1]) for i in range(6)]
    s0 = sides[0]
    return all(abs(s - s0) < tol * max(1.0, s0) for s in sides)


def test_smallest_hexagon_returns_six_vertices():
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    hexa = p.get_smallest_hexagon()
    assert len(hexa) == 6
    assert _hexagon_is_regular(hexa)


def test_smallest_hexagon_contains_polyiamond():
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    hexa = p.get_smallest_hexagon()
    for v in p.vertices:
        assert _point_in_convex_polygon(v.get_xy(), hexa), \
            f"vertex {v} = {v.get_xy()} is outside the enclosing hexagon"


def test_smallest_hexagon_size_lower_bound():
    """A regular hexagon's max width (vertex-to-vertex) equals 2*side, so the
    smallest enclosing hexagon must satisfy: side >= max_polygon_width / 2."""
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    hexa = p.get_smallest_hexagon()
    side = _hexagon_side_length(hexa)
    pts = _hull_vertices_xy(p)
    s = 0.0
    for k in range(180):
        ang = k * math.pi / 180.0
        n = np.array([math.cos(ang), math.sin(ang)])
        proj = pts @ n
        s = max(s, proj.max() - proj.min())
    assert side + 1e-6 >= s / 2.0


# ---- get_smallest_square --------------------------------------------------

def _square_is_square(verts, tol=1e-6):
    sides = [math.hypot(verts[(i+1) % 4][0] - verts[i][0],
                        verts[(i+1) % 4][1] - verts[i][1]) for i in range(4)]
    s0 = sides[0]
    if not all(abs(s - s0) < tol * max(1.0, s0) for s in sides):
        return False
    # check perpendicularity of adjacent edges
    e0 = (verts[1][0] - verts[0][0], verts[1][1] - verts[0][1])
    e1 = (verts[2][0] - verts[1][0], verts[2][1] - verts[1][1])
    return abs(e0[0] * e1[0] + e0[1] * e1[1]) < tol * s0 * s0


def test_smallest_square_returns_four_vertices():
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    sq = p.get_smallest_square()
    assert len(sq) == 4
    assert _square_is_square(sq)


def test_smallest_square_contains_polyiamond():
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    sq = p.get_smallest_square()
    for v in p.vertices:
        assert _point_in_convex_polygon(v.get_xy(), sq)


def test_smallest_square_axis_aligned_for_axis_aligned_input():
    """A right-triangle polyiamond 'ACE' has a small enclosing square."""
    p = Polyiamond('ACE')
    sq = p.get_smallest_square()
    side = math.hypot(sq[1][0] - sq[0][0], sq[1][1] - sq[0][1])
    # The triangle 'ACE' is the unit triangle (vertices at (0,0), (1,0), (0.5, sqrt(3)/2))
    # The smallest enclosing square has side >= height = sqrt(3)/2 ≈ 0.866
    assert side >= math.sqrt(3) / 2.0 - 1e-6


# ---- get_smallest_triangle ------------------------------------------------

def _triangle_is_equilateral(verts, tol=1e-6):
    sides = [math.hypot(verts[(i+1) % 3][0] - verts[i][0],
                        verts[(i+1) % 3][1] - verts[i][1]) for i in range(3)]
    s0 = sides[0]
    return all(abs(s - s0) < tol * max(1.0, s0) for s in sides)


def test_smallest_triangle_returns_three_vertices():
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    tri = p.get_smallest_triangle()
    assert len(tri) == 3
    assert _triangle_is_equilateral(tri)


def test_smallest_triangle_contains_polyiamond():
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    tri = p.get_smallest_triangle()
    for v in p.vertices:
        assert _point_in_convex_polygon(v.get_xy(), tri)


def test_smallest_triangle_of_unit_triangle():
    """The smallest enclosing equilateral triangle of a unit equilateral
    triangle must itself have side 1."""
    # A valid unit triangle: A + C + E = (0,0,0).
    p = Polyiamond([(1, 'A'), (1, 'C'), (1, 'E')])
    tri = p.get_smallest_triangle()
    side = math.hypot(tri[1][0] - tri[0][0], tri[1][1] - tri[0][1])
    assert abs(side - 1.0) < 1e-4


# ---- batch / scaling sanity ----------------------------------------------

def test_smallest_shapes_scale_linearly():
    """Scaling polyiamond side lengths by k scales bounding shape sides by k."""
    k = 4
    sides_small = [(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')]
    sides_large = [(L * k, D) for (L, D) in sides_small]
    p_small = Polyiamond(sides_small)
    p_large = Polyiamond(sides_large)
    for getter in ('get_smallest_hexagon',
                   'get_smallest_square',
                   'get_smallest_triangle'):
        small_v = getattr(p_small, getter)()
        large_v = getattr(p_large, getter)()
        s_small = math.hypot(small_v[1][0] - small_v[0][0],
                             small_v[1][1] - small_v[0][1])
        s_large = math.hypot(large_v[1][0] - large_v[0][0],
                             large_v[1][1] - large_v[0][1])
        assert abs(s_large - k * s_small) < 1e-3 * s_large, \
            f"{getter}: small={s_small}, large={s_large}, k={k}"

# ---------------------------------------------------------------------------
# Tests for the area moment of inertia tensor (2026-05).
# ---------------------------------------------------------------------------

def test_inertia_tensor_unit_triangle():
    """For the unit upward triangle (0,0)-(1,0)-(0.5, sqrt(3)/2) the
    closed-form values are::

        ∫ y²  dA = sqrt(3)/32
        ∫ x²  dA = 7*sqrt(3)/96
        ∫ x y dA = 1/16

    so the inertia tensor is
        [[ sqrt(3)/32, -1/16        ],
         [ -1/16,       7*sqrt(3)/96]].
    """
    import math
    import numpy as np
    p = Polyiamond([(1, 'A'), (1, 'C'), (1, 'E')])
    I = p.get_inertia_tensor()
    expected = np.array([[math.sqrt(3) / 32.0, -1.0 / 16.0],
                         [-1.0 / 16.0,         7.0 * math.sqrt(3) / 96.0]])
    assert isinstance(I, np.ndarray)
    assert I.shape == (2, 2)
    assert np.allclose(I, expected, atol=1e-12)
    # Symmetry of the tensor.
    assert np.isclose(I[0, 1], I[1, 0])


def test_inertia_tensor_orientation_invariant():
    """Reversing the traversal direction (CW vs CCW) must not change the
    tensor -- the geometric region is the same."""
    import numpy as np
    fwd = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    rev = Polyiamond([(1, 'C'), (2, 'A'), (3, 'B'), (4, 'F'), (5, 'D')])
    assert np.allclose(fwd.get_inertia_tensor(), rev.get_inertia_tensor(),
                       atol=1e-9)


def test_inertia_tensor_scaling():
    """Scaling all side lengths by k scales every tensor entry by k**4."""
    import numpy as np
    k = 3
    p_small = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    p_large = Polyiamond([(L * k, D) for (L, D) in p_small.sides])
    assert np.allclose(p_large.get_inertia_tensor(),
                       (k ** 4) * p_small.get_inertia_tensor(),
                       rtol=1e-12, atol=1e-9)


# ---------------------------------------------------------------------------
# Tests for get_closest_hausdorff_hexagon (2026-05).
# ---------------------------------------------------------------------------

def test_hausdorff_hexagon_regular_polyiamond():
    import math
    p = Polyiamond([(1, 'A'), (1, 'B'), (1, 'C'),
                    (1, 'D'), (1, 'E'), (1, 'F')])
    verts, h = p.get_closest_hausdorff_hexagon()
    assert h < 1e-6
    assert len(verts) == 6
    poly_verts = [pt.get_xy() for pt in p.vertices]
    for pv in poly_verts:
        d_min = min(math.hypot(pv[0] - hv[0], pv[1] - hv[1]) for hv in verts)
        assert d_min < 1e-5


def test_hausdorff_hexagon_scaled_regular():
    import math
    k = 4
    p = Polyiamond([(k, 'A'), (k, 'B'), (k, 'C'),
                    (k, 'D'), (k, 'E'), (k, 'F')])
    verts, h = p.get_closest_hausdorff_hexagon()
    assert h < 1e-5
    side = math.hypot(verts[1][0] - verts[0][0], verts[1][1] - verts[0][1])
    assert abs(side - k) < 1e-4


def test_hausdorff_hexagon_bound_by_smallest_enclosing():
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    verts, h = p.get_closest_hausdorff_hexagon()
    assert h >= 0
    assert h < p.get_perimeter()


def test_hausdorff_hexagon_returns_regular_hexagon():
    import math
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    verts, _ = p.get_closest_hausdorff_hexagon()
    cx = sum(v[0] for v in verts) / 6.0
    cy = sum(v[1] for v in verts) / 6.0
    radii = [math.hypot(v[0] - cx, v[1] - cy) for v in verts]
    sides = [math.hypot(verts[(i + 1) % 6][0] - verts[i][0],
                        verts[(i + 1) % 6][1] - verts[i][1])
             for i in range(6)]
    r0 = radii[0]; s0 = sides[0]
    assert all(abs(r - r0) < 1e-6 * max(1.0, r0) for r in radii)
    assert all(abs(s - s0) < 1e-6 * max(1.0, s0) for s in sides)


# ---------------------------------------------------------------------------
# Tests for get_closest_hausdorff_triangle (2026-05).
# ---------------------------------------------------------------------------

def test_hausdorff_triangle_equilateral_polyiamond():
    """A polyiamond whose 3 vertices already form an equilateral triangle
    (sides = kA, kC, kE) must give Hausdorff distance ~0 and the returned
    triangle must coincide with that triangle."""
    import math
    k = 5
    p = Polyiamond([(k, 'A'), (k, 'C'), (k, 'E')])
    verts, h = p.get_closest_hausdorff_triangle()
    assert h < 1e-6
    assert len(verts) == 3
    poly_verts = [pt.get_xy() for pt in p.vertices]
    for pv in poly_verts:
        d_min = min(math.hypot(pv[0] - tv[0], pv[1] - tv[1]) for tv in verts)
        assert d_min < 1e-5
    # Side length matches.
    side = math.hypot(verts[1][0] - verts[0][0], verts[1][1] - verts[0][1])
    assert abs(side - k) < 1e-4


def test_hausdorff_triangle_returns_equilateral():
    """Result must be an equilateral triangle: 3 equal sides and 3 equal
    distances from the centroid."""
    import math
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    verts, _ = p.get_closest_hausdorff_triangle()
    assert len(verts) == 3
    cx = sum(v[0] for v in verts) / 3.0
    cy = sum(v[1] for v in verts) / 3.0
    radii = [math.hypot(v[0] - cx, v[1] - cy) for v in verts]
    sides = [math.hypot(verts[(i + 1) % 3][0] - verts[i][0],
                        verts[(i + 1) % 3][1] - verts[i][1])
             for i in range(3)]
    r0 = radii[0]; s0 = sides[0]
    assert all(abs(r - r0) < 1e-6 * max(1.0, r0) for r in radii)
    assert all(abs(s - s0) < 1e-6 * max(1.0, s0) for s in sides)


def test_hausdorff_triangle_bounded_and_nonneg():
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    verts, h = p.get_closest_hausdorff_triangle()
    assert h >= 0
    assert h < p.get_perimeter()


def test_hausdorff_triangle_optimum_no_worse_than_smallest_enclosing():
    """The closest Hausdorff triangle must achieve a distance at least as
    small as the one obtained by using the smallest *enclosing* equilateral
    triangle (which trivially bounds the one-sided Hausdorff distance from
    above)."""
    import math
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    verts_opt, h_opt = p.get_closest_hausdorff_triangle()
    enc = p.get_smallest_triangle()
    poly_verts = np.array([pt.get_xy() for pt in p.vertices], dtype=float)
    # Compute Hausdorff distance of polyiamond vertices to smallest enclosing
    # triangle's perimeter using the same helper.
    cx = sum(v[0] for v in enc) / 3.0
    cy = sum(v[1] for v in enc) / 3.0
    side = math.hypot(enc[1][0] - enc[0][0], enc[1][1] - enc[0][1])
    theta = math.atan2(enc[0][1] - cy, enc[0][0] - cx) - math.pi / 2.0
    d = Polyiamond._tri_perimeter_distances(poly_verts, cx, cy, theta, side)
    h_enc = float(d.max())
    assert h_opt <= h_enc + 1e-9


def test_hausdorff_30gon_distances():
    p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
    _, h_hex = p.get_closest_hausdorff_hexagon()
    assert abs(h_hex - 7.580773208149545) < 1e-6

    _, h_tri = p.get_closest_hausdorff_triangle()
    assert abs(h_tri - 9.824065054293587) < 1e-6

# ---------------------------------------------------------------------------
# Tests for get_incircle and get_circumcircle (2026-05).
# ---------------------------------------------------------------------------

def test_circumcircle_unit_triangle():
    """Circumcircle of the unit equilateral triangle (A,C,E):
    centroid = (0.5, sqrt(3)/6), circumradius = sqrt(3)/3."""
    import math
    p = Polyiamond([(1, 'A'), (1, 'C'), (1, 'E')])
    (cx, cy), r = p.get_circumcircle()
    assert abs(cx - 0.5) < 1e-9
    assert abs(cy - math.sqrt(3) / 6.0) < 1e-9
    assert abs(r - math.sqrt(3) / 3.0) < 1e-9


def test_circumcircle_contains_all_vertices():
    """Every polyiamond vertex must lie inside (or on) the returned circle."""
    import math
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    (cx, cy), r = p.get_circumcircle()
    for v in p.vertices:
        x, y = v.get_xy()
        d = math.hypot(x - cx, y - cy)
        assert d <= r + 1e-9


def test_circumcircle_scaling():
    """Scaling all sides by k scales centre and radius by k."""
    import math
    k = 5
    p_small = Polyiamond([(1, 'A'), (1, 'C'), (1, 'E')])
    p_large = Polyiamond([(k, 'A'), (k, 'C'), (k, 'E')])
    (cxs, cys), rs = p_small.get_circumcircle()
    (cxl, cyl), rl = p_large.get_circumcircle()
    assert abs(cxl - k * cxs) < 1e-9
    assert abs(cyl - k * cys) < 1e-9
    assert abs(rl - k * rs) < 1e-9


def test_incircle_unit_triangle():
    """Incircle of unit equilateral triangle: centre = (0.5, sqrt(3)/6),
    inradius = sqrt(3)/6."""
    import math
    p = Polyiamond([(1, 'A'), (1, 'C'), (1, 'E')])
    (cx, cy), r = p.get_incircle()
    assert abs(cx - 0.5) < 1e-3
    assert abs(cy - math.sqrt(3) / 6.0) < 1e-3
    assert abs(r - math.sqrt(3) / 6.0) < 1e-3


def test_incircle_inside_polygon():
    """The incircle's centre must be inside the polyiamond and every point
    on the circle must lie inside or on the polyiamond's perimeter (i.e.
    the centre's distance to the polygon boundary equals the radius)."""
    import math
    p = Polyiamond([(5, 'A'), (4, 'C'), (3, 'E'), (2, 'D'), (1, 'F')])
    (cx, cy), r = p.get_incircle()
    # Centre is inside.
    poly_xy = np.asarray(p.get_descartes(), dtype=float)
    inside = Polyiamond._points_in_polygon(
        poly_xy, np.array([cx]), np.array([cy]))[0]
    assert bool(inside)
    # Min distance from centre to polygon edges is >= r (within tol).
    d = float(Polyiamond._polygon_edge_distances(
        poly_xy, np.array([cx]), np.array([cy])).min())
    assert d + 1e-6 >= r


def test_incircle_scaling():
    """Scaling sides by k scales incircle centre and radius by k."""
    k = 4
    p_small = Polyiamond([(1, 'A'), (1, 'C'), (1, 'E')])
    p_large = Polyiamond([(k, 'A'), (k, 'C'), (k, 'E')])
    (cxs, cys), rs = p_small.get_incircle()
    (cxl, cyl), rl = p_large.get_incircle()
    # Coarse-grid + Nelder-Mead refinement → modest tolerance.
    assert abs(cxl - k * cxs) < 1e-2
    assert abs(cyl - k * cys) < 1e-2
    assert abs(rl - k * rs) < 1e-2

def test_min_width():
    # Test on a known polyiamond
    p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
    min_w, seg_min_width, parallel_lines = p.min_width()
    # The expected min_width from previous test script was ~109.87076689881448
    assert abs(min_w - 109.87076689881448) < 1e-6
    assert len(seg_min_width) == 2
    assert len(parallel_lines) == 3
