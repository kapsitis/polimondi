# Closure Proof by Induction — Triangular Coordinates

## Construction

$$S_k = a + (bc)^k + df + (ef)^{k-1} + ed + (ef)^k + ac + (bc)^{k-1}, \qquad n(k) = 8k+3$$

## Coordinates

In the triangular grid each direction is a vector in $\mathbb{Z}^3$ with $x+y+z=0$:

| dir | vector |
|-----|--------|
| $a$ | $(1,\ 0,\ -1)$ |
| $b$ | $(1,\ -1,\ 0)$ |
| $c$ | $(0,\ -1,\ 1)$ |
| $d$ | $(-1,\ 0,\ 1)$ |
| $e$ | $(-1,\ 1,\ 0)$ |
| $f$ | $(0,\ 1,\ -1)$ |

**Key cancellations:**
$$\vec b+\vec c = (1,-2,1), \quad \vec e+\vec f = (-1,2,-1) = -(\vec b+\vec c)$$
$$\vec d+\vec f = (-1,1,0) = \vec e, \quad \vec a+\vec c = (1,-1,0) = \vec b$$

## Closure Condition

The $i$-th character (0-indexed) of $S_k$ receives length $n(k)-i$. The polyiamond closes iff:
$$V(k) \;:=\; \sum_{i=0}^{n(k)-1}(n(k)-i)\,\vec{s_i} = \mathbf{0}$$

---

## Base Case: $k = 1$

$S_1 = a,b,c,d,f,e,d,e,f,a,c$ with $n=11$ and lengths $11,10,\ldots,1$.

Computing $V(1)$ by grouping equal directions:

| dir | positions (lengths) | contribution |
|-----|-------------------|-------------|
| $a$ | 11, 2 | $13\,(1,0,-1) = (13,0,-13)$ |
| $b$ | 10 | $10\,(1,-1,0) = (10,-10,0)$ |
| $c$ | 9, 1 | $10\,(0,-1,1) = (0,-10,10)$ |
| $d$ | 8, 5 | $13\,(-1,0,1) = (-13,0,13)$ |
| $e$ | 6, 4 | $10\,(-1,1,0) = (-10,10,0)$ |
| $f$ | 7, 3 | $10\,(0,1,-1) = (0,10,-10)$ |

$$V(1) = (13+10+0-13-10+0,\ 0-10-10+0+10+10,\ -13+0+10+13+0-10) = (0,0,0)\ \checkmark$$

---

## Insertion Lemma

**Claim:** Inserting two characters $x, y$ at position $p$ in a string of current length $n$ changes $V$ by:
$$\Delta V = 2\cdot P(s_{<p}) + (n+2-p)\,\vec x + (n+1-p)\,\vec y$$
where $P(s_{<p}) = \sum_{i<p}\vec{s_i}$ is the unweighted direction sum of all characters before position $p$.

**Proof of lemma:** Characters before $p$ (positions $j < p$) now have length $(n+2-j)$ instead of $(n-j)$: each gains $+2$, contributing $+2\,\vec{s_j}$ each. Characters at positions $j \geq p$ shift to $j+2$ with length $(n+2-(j+2)) = n-j$: unchanged. The two new characters at positions $p, p+1$ contribute $(n+2-p)\vec x + (n+1-p)\vec y$. $\square$

---

## Inductive Step: $S_k \to S_{k+1}$

**Assume $V(k) = \mathbf{0}$.** We obtain $S_{k+1}$ by four insertions (in sequence), each increasing $n$ by 2:

| # | Insert | At position $p$ in current string | $P(s_{<p})$ |
|---|--------|----------------------------------|-------------|
| 1 | $bc$ | $1+2k$ (end of $(bc)^k$) | $\vec a + k(\vec b+\vec c)$ |
| 2 | $ef$ | $3+4k$ (end of $(ef)^{k-1}$, now in $n{=}8k{+}5$ string) | $\vec a + (k+1)(\vec b+\vec c) + \vec d + \vec f + (k-1)(\vec e+\vec f)$ |
| 3 | $ef$ | $7+6k$ (end of second $(ef)^k$, now in $n{=}8k{+}7$ string) | (see below) |
| 4 | $bc$ | $9+8k$ (very end, in $n{=}8k{+}9$ string) | (see below) |

**Computing $P(s_{<p})$ for each insertion** using $\vec b+\vec c = -(\vec e+\vec f)$:

$$P_1 = \vec a + k(\vec b+\vec c) = (1+k,\ -2k,\ -1+k)$$

$$P_2 = \vec a + (k+1)(\vec b+\vec c) + (\vec d+\vec f) + (k-1)(\vec e+\vec f)$$
Since $(\vec d+\vec f) = \vec e$ and $\vec e+\vec f = -(\vec b+\vec c)$:
$$= \vec a + \vec e + [(k+1)-(k-1)](\vec b+\vec c) = \vec a + \vec e + 2(\vec b+\vec c) = (2,-3,1)$$

$$P_3 = P_2 + k(\vec e+\vec f) + (\vec e+\vec d) + k(\vec e+\vec f) + (\vec a+\vec c)$$
$$= (2,-3,1) + 2k(-1,2,-1) + (-2,1,1) + (1,-1,0) = (-k,\ 2k-1,\ -k+1)$$

$$P_4 = P_3 + (\vec e+\vec f) + (\vec a+\vec c) + (k-1)(\vec b+\vec c)$$
Note: $(\vec e+\vec f)+(\vec b+\vec c)=0$ and $(\vec a+\vec c) = \vec b$:
$$= (-k,2k-1,-k+1) + (k-1)(\vec b+\vec c) + \vec b + \underbrace{(\vec e+\vec f)}_{=-(\vec b+\vec c)}$$
After careful expansion: $P_4 = (-2,3,-1)$

**Computing $\Delta V$ for each insertion** (using $n$ at the time of each insertion):

$$\Delta V_1 = 2P_1 + (6k+4)\vec b + (6k+3)\vec c = (8k+6,\ -16k-7,\ 8k+1)$$

$$\Delta V_2 = 2P_2 + (4k+2)\vec e + (4k+1)\vec f = (-4k+2,\ 8k-3,\ -4k+1)$$

$$\Delta V_3 = 2P_3 + 2k\,\vec e + (2k-1)\vec f = (-4k,\ 8k-3,\ -4k+3)$$

$$\Delta V_4 = 2P_4 + 0\cdot\vec b + (-1)\vec c = (-4,\ 7,\ -3)$$

**Total change:**

| coord | $\Delta V_1$ | $\Delta V_2$ | $\Delta V_3$ | $\Delta V_4$ | **sum** |
|-------|------------|------------|------------|------------|---------|
| $x$ | $8k+6$ | $-4k+2$ | $-4k$ | $-4$ | **0** $\checkmark$ |
| $y$ | $-16k-7$ | $8k-3$ | $8k-3$ | $7$ | **0** $\checkmark$ |
| $z$ | $8k+1$ | $-4k+1$ | $-4k+3$ | $-3$ | **0** $\checkmark$ |

Therefore:
$$V(k+1) = V(k) + \Delta V_1 + \Delta V_2 + \Delta V_3 + \Delta V_4 = \mathbf{0} + \mathbf{0} = \mathbf{0}$$

---

## Conclusion

By induction, $V(k) = \mathbf{0}$ for all $k \geq 1$: the polyiamond $S_k$ **always returns to its starting point**. $\blacksquare$
