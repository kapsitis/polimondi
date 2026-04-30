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

---

## Area moment of inertia tensor (2026-05)

`get_inertia_tensor()` returns the planar **area moment of inertia tensor**
about the origin (the first polyiamond vertex) for a uniform unit-density
lamina bounded by the polyiamond's sides:

$$
I \;=\; \int_{\Omega} \bigl(\lVert\mathbf r\rVert^2\,I_2 - \mathbf r\,\mathbf r^{T}\bigr)\,dm
\;=\;
\begin{pmatrix}
\int y^2\,dA & -\int xy\,dA\\[2pt]
-\int xy\,dA & \int x^2\,dA
\end{pmatrix}
$$

with `dm = dA` (uniform unit density).  The result is a `(2, 2)` `float`
NumPy array.  Real Cartesian coordinates are used (so the unit equilateral
triangle has area `√3/4`).

### Why not a brute-force area integral?

A naive implementation discretises Ω into pixels or triangles and sums
`x²`, `y²`, `xy` over them.  Cost scales with **area** — O(N²) for a
polyiamond of side O(N) — which is wasteful and noisy.  Instead, the three
double integrals are converted analytically into **boundary line
integrals** by Green's theorem, then evaluated as a closed-form sum over
polygon vertices.

### Closed-form polygon moment formulas

For a polygon with vertices `(x_i, y_i)` in CCW order and the per-edge
shoelace term `c_i = x_i·y_{i+1} − x_{i+1}·y_i`:

```
∫ x²  dA = (1/12) Σ c_i · (x_i² + x_i x_{i+1} + x_{i+1}²)
∫ y²  dA = (1/12) Σ c_i · (y_i² + y_i y_{i+1} + y_{i+1}²)
∫ x y dA = (1/24) Σ c_i · (x_i y_{i+1} + 2 x_i y_i
                          + 2 x_{i+1} y_{i+1} + x_{i+1} y_i)
```

If the polygon is traversed CW the three sums all flip sign; the
implementation multiplies by `sign(signed_area)` so the returned tensor
always corresponds to the geometric region with positive area.

### GPU-friendliness

Each surface integral becomes **one element-wise NumPy expression over the
N vertices followed by a single sum-reduction**.  There is no interior
sampling at all, so cost is O(N) (perimeter) instead of O(N²) (area).  The
three reductions are independent and can be fused into a single GPU kernel;
multiple polyiamonds are batched by stacking padded vertex arrays into a
leading batch dimension and broadcasting `np.roll`/`einsum` across it
(directly portable to CuPy or JAX with no algorithmic change).


---

## Closest-Hausdorff regular hexagon (2026-05)

`get_closest_hausdorff_hexagon()` returns the regular hexagon `S` (any 6
real-valued Cartesian vertices, **not** required to lie on the triangular
grid) that minimises the one-sided Hausdorff distance from the polyiamond's
vertices to the hexagon's perimeter:

$$
h(P, S) \;=\; \max_{v\,\in\,V(P)} \;\min_{x\,\in\,\partial S} \;\lVert v - x\rVert
$$

Returned as `(vertices, distance)` where `vertices` is a list of 6
`(x, y)` tuples (CCW order, vertex 0 at angle `θ + π/6` from the centre).

### Parametrisation

A regular hexagon has only 4 real degrees of freedom: centre `(cx, cy)`,
orientation `θ ∈ [0, π/3)` (60° rotational symmetry) and apothem `a > 0`.
The corresponding side length is `s = 2a/√3`.

### Two-stage GPU-friendly algorithm

The objective is a non-smooth `max` of distances, so a derivative-free
strategy is used:

1. **Vectorised coarse grid.**  An initial guess for `(θ, a, cx, cy)` is
   taken from `get_smallest_enclosing_hexagon()` (see above), then a small
   4-D grid of perturbations around it is built.  The cost
   `max_v dist(v, ∂S)` is evaluated for **every** grid candidate and
   **every** polyiamond convex-hull vertex in one broadcast of shape
   `(M, N, 6)` (M candidates × N hull vertices × 6 hexagon edges).  The
   inner kernel is a pure element-wise expression (`np.clip`, `np.sqrt`,
   `np.roll`, `np.argmin`) — directly portable to CuPy / JAX with no
   algorithmic change.  Only the convex hull is needed because the
   Hausdorff distance is determined by the extreme vertices.
2. **Local Nelder–Mead refinement.**  A simplex-based search starting from
   the best grid candidate converges to the local optimum.  Nelder–Mead
   needs no derivatives, which suits the non-smooth `max` cost exactly.

### Why a regular hexagon's distance kernel is GPU-trivial

For a candidate hexagon with vertices `h_0 … h_5` (CCW) and any query point
`p`, the distance to the perimeter is

$$
\text{dist}(p, \partial S) \;=\; \min_{k=0..5} \; \big\lVert p - \mathrm{proj}_{[h_k, h_{k+1}]}(p) \big\rVert
$$

with the segment projection clamped to `t ∈ [0, 1]`.  This is one
`np.clip` + one Euclidean distance per `(candidate, vertex, edge)` triple
— exactly the kind of dense, regular tensor expression that GPUs run at
peak throughput.

### Tie breaking

When several optima exist (numerically tied) the implementation returns
the one found first by the optimiser, as the spec allows any optimum.

---

## Incircle and circumcircle (2026-05)

Two complementary circle-based methods on `Polyiamond`:

| Method | Returns |
|--------|---------|
| `get_incircle()` | `((cx, cy), r)` — centre and radius of the **largest** circle fully inside the polyiamond |
| `get_circumcircle()` | `((cx, cy), r)` — centre and radius of the **smallest** circle containing every polyiamond vertex |

Coordinates and radii are real Cartesian (NumPy) floats; no exact-integer
or symbolic √3 expressions are needed (the polyiamond's vertices already
involve √3/2 from the triangular grid).

### Circumcircle — `O(H³)` vectorised candidate enumeration

The smallest enclosing circle of any finite point set equals that of its
**convex hull**, and the optimum is determined by either:

* a **diameter pair** of hull vertices (centre at the segment midpoint,
  radius half the segment length), or
* a **circumscribed triple** of hull vertices (the three points lie on
  the circle).

Both candidate sets are enumerated and tested in pure NumPy:

1. All `H·(H−1)/2` pairs are evaluated in one broadcast: each candidate
   circle is checked against all `H` hull vertices via a single
   `(N_pairs, H)` distance tensor, kept iff every vertex is inside.
2. All `H·(H−1)·(H−2)/6` triples produce circumcircle centres via the
   closed-form determinant formula (no matrix inverse, only element-wise
   arithmetic), and are validated by another `(N_triples, H)` broadcast.

The smallest valid radius wins.  The hull of an integer-grid polyiamond
typically has very few vertices, so `O(H³)` is in practice trivial; the
inner kernels are pure broadcast operations and run unchanged on
CuPy/JAX.  This avoids the recursion of Welzl's algorithm — the
recursion is what makes Welzl GPU-unfriendly.

### Incircle — coarse-grid + Nelder–Mead

The largest inscribed circle problem on a (possibly non-convex) simple
polygon is

$$
r^{\star} \;=\; \max_{c\,\in\,P}\;\operatorname{dist}(c, \partial P)
$$

with the maximum-of-`min`-of-distances objective being non-smooth.  The
implementation has two stages, both driven by element-wise NumPy:

1. **Vectorised coarse grid (GPU-friendly).**  Sample the polygon's
   bounding box with an `n_grid × n_grid` rectangular grid (default
   `n_grid = 80`).  In a single broadcast:
     * a vectorised even-odd ray-casting test
       (`_points_in_polygon`) masks out exterior points;
     * `_polygon_edge_distances` returns a `(N, E)` matrix of
       point-to-edge distances, reduced with `min` over the edge axis to
       give each grid point's distance to the polygon boundary.
   The interior point with the largest boundary distance is the coarse
   optimum.
2. **Local Nelder–Mead refinement.**  `scipy.optimize.minimize`
   maximises the same signed-distance objective (with a strong
   exterior-penalty term) starting from the coarse optimum.  Nelder–Mead
   is derivative-free, which suits the non-smooth `min` objective.

For a *convex* polygon this problem reduces to the Chebyshev-centre LP
(linear-programming on the half-plane intersection); we deliberately do
**not** branch on convexity — the grid-plus-refine pipeline handles both
convex and non-convex polyiamonds with the same code path.

### Why these two helpers are GPU-friendly

The two private static helpers introduced for the incircle —
`_points_in_polygon` and `_polygon_edge_distances` — are themselves
pure element-wise NumPy expressions over `(E, 1)`-vs-`(1, N)` broadcasts
of edges versus query points.  They reduce to a single `np.sqrt`,
`np.clip`, and a couple of comparisons each.  Both replace ``shapely``
calls (which are Python-level, per-point) with batchable tensor ops that
port directly to CuPy/JAX device arrays.
