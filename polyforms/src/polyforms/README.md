# polyforms — source module notes

## `polyiamond.py` — numeric functions

### Coordinate systems

There are three coordinate systems used throughout the module.

| System | Description | Values |
|--------|-------------|--------|
| **TriGrid (`PointTg`)** | Integer triple `(x,y,z)` with `x+y+z=0` living on the triangular lattice. | exact integers |
| **Mod-Cartesian** | `(x_m, y_m)` where `y_m` counts triangle-height units (height = 1, not √3/2). Maps from `PointTg(a,b,c)` as `x_m = a + b/2`, `y_m = −b`. | halves allowed |
| **DESCARTES2** | `(x_2, y_2) = (2a+b, −2b)` — the mod-Cartesian coords scaled by 2 so that every vertex has **exact integer** coordinates. | exact integers |

The `DESCARTES2` dict in `polyiamond.py` encodes the per-direction unit vectors in this system:

```python
DESCARTES2 = {'A': (2,0), 'B': (1,2), 'C': (-1,2),
              'D': (-2,0), 'E': (-1,-2), 'F': (1,-2)}
```

A unit equilateral triangle has **area 2** in DESCARTES2 coordinates (shoelace / 2).

---

### Changes made (2026-04)

All changes are in `polyiamond.py`.

#### 1. `get_signed_area()` — now exact integer

**Before:** vertices were converted to floating-point Cartesian coordinates
(`get_descartes()`), the shoelace formula was applied, and the result divided
by `unit_triangle_area = sqrt(3)/4` after multiplying by `unit_triangle_height
= sqrt(3)/2`. For large integer side lengths (say, L ∼ 10⁶) the products of
floating-point vertex coordinates introduce rounding errors.

**After:** vertices are accumulated directly in `DESCARTES2` integer
coordinates.  The algebraic identity

```
signed_area_in_triangles = shoelace_in_DESCARTES2 / 4
```

holds exactly because one unit triangle has area 2 in DESCARTES2 (so dividing
the shoelace by 2 gives area in DESCARTES2 units, and dividing again by 2
converts to triangle units).  Since the area is always an integer, the
shoelace sum is always divisible by 4; this is asserted at runtime.  Python
`int` arithmetic is arbitrary-precision, so there is no overflow or
floating-point loss regardless of side-length magnitude.

The function no longer calls `get_descartes()`.

#### 2. `winding_number(pt)` — now exact integer with boundary handling

**Before:** used `math.atan2` to sum the angular sweep of polygon vertices
around the query point and divided by `2π`.  `atan2` involves floating-point
trigonometry, and the result for points that lie exactly on the polygon
boundary (vertices or edges) was undefined (due to `atan2(0,0) = 0`
coincidence).

**After:** the standard integer winding-number algorithm based on horizontal
crossing counts and cross products (W. R. Franklin, "PNPOLY"):

* The query `PointTg(a,b,c)` is converted to `DESCARTES2` integers
  `(2a+b, −2b)`.
* For each polygon edge, a single integer cross product determines the
  left/right relationship.
* **Boundary points** (cross product = 0 and query between edge endpoints)
  return 0 explicitly, which matches the convention used by `is_inside`.
* The final value is negated to preserve the original sign convention: a
  CCW-oriented polygon returns **−1** for interior points (the old `atan2`
  implementation computed `angle_prev − angle_next`, yielding −1 for CCW).

#### 3. `diameter_sq()` — new exact-integer method

The existing `diameter()` method computes vertex distances using floating-point
`L2_dist`.  A new companion method `diameter_sq()` returns the **squared**
maximum vertex distance as an exact integer, together with the achieving index
pair `(i_max, j_max)`.

It works entirely in `DESCARTES2` integer coordinates:

```
d2 = (x_i − x_j)² + (y_i − y_j)²
```

The actual real-valued diameter can be recovered when needed but for all
comparison and maximisation purposes the squared integer value suffices and
is GPU-friendly (uniform integer dot products, no sqrt).

The original `diameter()` method is retained unchanged for backward
compatibility.

#### 4. `DESCARTES2` constant

Added the module-level constant `DESCARTES2` (see table above).  It is
exported alongside `DESCARTES` and can be imported by other modules that need
pure-integer coordinate computations.

---

### Why this matters for large polyiamonds

Consider a polyiamond whose side lengths are O(N).  The vertex coordinates in
float64 can be O(N), so products in the shoelace formula reach O(N²).  With
N ∼ 10⁶ and float64 having 53-bit mantissa (≈ 15 decimal digits), products of
O(N²) ≈ 10¹² are still exact — but only just.  At N ∼ 10⁷ the products reach
10¹⁴, and accumulated shoelace sums across many vertices can lose integer
precision.  Python `int` has no such limit; the DESCARTES2 integer path scales
without any precision concern.

---

### GPU adaptability

All three new/revised functions operate on uniform arrays of integer (x, y)
pairs with element-wise arithmetic (multiply, add, subtract, compare).  This
maps directly to GPU integer SIMD operations.  The only non-uniform step is
the final sum reduction for the shoelace, which is a standard parallel
reduction pattern.

---

## Convex hull and minimum enclosing shapes (2026-04-30)

Four new methods added to `Polyiamond`:

| Method | Returns |
|--------|---------|
| `convex_hull()` | `list[PointTg]` — hull vertices in CCW order |
| `get_smallest_hexagon()` | `list[(x, y)]` — 6 Cartesian vertices, CCW |
| `get_smallest_square()` | `list[(x, y)]` — 4 Cartesian vertices, CCW |
| `get_smallest_triangle()` | `list[(x, y)]` — 3 Cartesian vertices, CCW |

The first polyiamond vertex is the Cartesian origin `(0, 0)`; all returned
coordinates are in that frame.

### Convex hull

Andrew's monotone chain on the integer `DESCARTES2` coordinates.  All
orientation tests are exact integer cross products, so the hull itself is
exact regardless of polyiamond size.  Output is converted back to `PointTg`
instances.

### Bounding-shape methods (general approach)

For each of the three minimum enclosing shapes the algorithm follows the same
pattern:

1. Compute the convex hull as a `(N, 2)` NumPy array of real Cartesian
   coordinates.
2. Build a candidate set of orientation angles `θ` covering the shape's
   rotational symmetry interval `[0, period)`:
   * an evenly spaced grid of `n_angles` samples (default 1440), and
   * the convex-hull edge angles taken modulo `period` — these are the
     critical orientations at which the optimum can occur (rotating-calipers
     theorem for the minimum-area enclosing rectangle generalises to
     enclosing regular polygons of fixed shape).
3. For every candidate `θ` simultaneously, evaluate the smallest enclosing
   shape size using only NumPy vectorised dot products (`np.einsum`) — this
   is the trivially batchable step.  Multiple polyiamonds can be processed in
   parallel by adding a leading "batch" dimension to the hull-points array.
4. Pick the optimal `θ` and reconstruct the shape's vertices.  Tie-breaking
   selects the configuration with the smallest centre x-coordinate.

### Hexagon: closed-form size formula

A regular hexagon at orientation `θ` is the intersection of three
width-`2a` strips perpendicular to unit normals
`n_k = (cos(θ + k·π/3), sin(θ + k·π/3))`, `k = 0,1,2`.  Containment of the
convex polygon imposes both a strip-width constraint and a translational
feasibility constraint (the three strips must share a common centre `c`).
Eliminating `c` analytically (using `c·n_0 = c·n_1 − c·n_2`, valid for any
3 unit vectors at 60° in the plane) gives the apothem as

```
A_k  =  max(p·n_k) − min(p·n_k)         # width in direction n_k
M_k  =  ½(max(p·n_k) + min(p·n_k))      # midpoint of projection
a*(θ) = max( A_0/2, A_1/2, A_2/2,
             (|M_1 − M_0 − M_2| + (A_0+A_1+A_2)/2) / 3 )
side(θ) = 2·a*(θ) / √3
```

The first three terms enforce strip widths; the fourth enforces feasibility
of a common centre.  An earlier draft missed this last term, producing
hexagons that were too small in directions where the polygon was unbalanced.

### Square: rotated-bbox sweep

For each `θ` rotate the hull by `−θ` and take the axis-aligned bounding box;
the smallest square at this orientation has side `max(width_x, width_y)`.
Sweeping `θ ∈ [0, π/2)` finds the optimum.

### Equilateral triangle: support-function formula

In the rotated frame (canonical apex-up triangle) with outward normals
`(0, −1)`, `(√3/2, 1/2)`, `(−√3/2, 1/2)`:

```
cy = min(y_rot)
A  = max( (√3/2)·x_rot + (1/2)·y_rot )
B  = max(-(√3/2)·x_rot + (1/2)·y_rot )
side = 2·(A + B − cy) / √3
cx   = (A − B) / √3
```

Sweep over `θ ∈ [0, 2π/3)` and pick the smallest `side`.

### Parallelisation note

The three minimum-enclosing-shape methods use NumPy `einsum` and broadcasting
exclusively.  All operations are uniform across the candidate-angle axis,
making batched processing of many polyiamonds (or migration to GPU array
libraries such as CuPy / JAX) straightforward — the per-polyiamond `for`
loop becomes another broadcast axis with no algorithmic change.

