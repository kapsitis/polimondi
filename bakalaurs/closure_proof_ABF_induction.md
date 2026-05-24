# Closure Proof by Induction: $S_k = ABF + (DFBF)^k + DED + (CDCB)^k + CDC$

## Triangular Coordinates

| $A$ | $B$ | $C$ | $D$ | $E$ | $F$ |
|-----|-----|-----|-----|-----|-----|
| $(1,0,-1)$ | $(1,-1,0)$ | $(0,-1,1)$ | $(-1,0,1)$ | $(-1,1,0)$ | $(0,1,-1)$ |

The **closure sum** for a string $S_k$ of length $n = 8k+9$ is:
$$V(k) = \sum_{i=0}^{n-1}(n-i)\,\vec{s_i}$$
We want $V(k)=\mathbf{0}$ for all $k\geq 1$.

---

## Insertion Lemma

Inserting a block $t = t_0 t_1\cdots t_{m-1}$ at position $p$ in a string of length $n$ changes $V$ by:
$$\boxed{\Delta V = m\cdot P(s_{<p}) + (n+m-p)\cdot P(t) - W(t)}$$
where $P(s_{<p}) = \sum_{i<p}\vec{s_i}$, $\ P(t) = \sum_i\vec{t_i}$, and $W(t) = \sum_{i=0}^{m-1}i\cdot\vec{t_i}$.

> **Why:** characters before $p$ each gain $+m$ in length (adding $m\cdot P(s_{<p})$); characters after $p$ are unaffected (their position and length shift cancel); the new characters contribute $(n+m-p-i)$ each for $i=0,\ldots,m-1$.

Useful values:
$$P(DFBF) = (0,1,-1), \quad W(DFBF) = 0D+1F+2B+3F = (2,2,-4)$$
$$P(CDCB) = (0,-3,3), \quad W(CDCB) = 0C+1D+2C+3B = (2,-5,3)$$

---

## Base Case: $k = 1$

$S_1 = A,B,F,D,F,B,F,D,E,D,C,D,C,B,C,D,C$ with $n=17$, lengths $17,16,\ldots,1$.

| dir | lengths used | contribution |
|-----|-------------|-------------|
| $A$ | 17 | $(17,0,-17)$ |
| $B$ | 16, 12, 4 | $32(1,-1,0) = (32,-32,0)$ |
| $F$ | 15, 13, 11 | $39(0,1,-1) = (0,39,-39)$ |
| $D$ | 14, 10, 8, 6, 2 | $40(-1,0,1) = (-40,0,40)$ |
| $E$ | 9 | $9(-1,1,0) = (-9,9,0)$ |
| $C$ | 7, 5, 3, 1 | $16(0,-1,1) = (0,-16,16)$ |

$$V(1) = (17+32+0-40-9+0,\ 0-32+39+0+9-16,\ -17+0-39+40+0+16) = (0,0,0)\ \checkmark$$

---

## Inductive Step

**Assume $V(k) = \mathbf{0}$.** We obtain $S_{k+1}$ from $S_k$ by two insertions:

| | block | position $p$ in current string | current $n$ |
|-|-------|-------------------------------|-------------|
| **Insert 1** | $DFBF$ | $p_1 = 3+4k$ (end of $(DFBF)^k$) | $8k+9$ |
| **Insert 2** | $CDCB$ | $p_2 = 10+8k$ (end of $(CDCB)^k$ in updated string) | $8k+13$ |

### Insert 1 — adding one $DFBF$ block

$$P(s_{<p_1}) = P(ABF) + k\cdot P(DFBF) = (2,0,-2)+k(0,1,-1) = (2,\ k,\ -2{-}k)$$
$$n+m-p = (8k+9)+4-(3+4k) = 4k+10$$
$$\Delta V_1 = 4(2,k,-2{-}k) + (4k+10)(0,1,-1) - (2,2,-4)$$
$$= (8,\ 4k,\ -8{-}4k) + (0,\ 4k{+}10,\ -4k{-}10) + (-2,\ -2,\ 4)$$
$$= \mathbf{(6,\ 8k+8,\ -8k-14)}$$

### Insert 2 — adding one $CDCB$ block

After Insert 1, $n=8k+13$.
$$P(s_{<p_2}) = P(ABF)+(k{+}1)\cdot P(DFBF)+P(DED)+k\cdot P(CDCB)$$
$$= (2,0,-2)+(k{+}1)(0,1,-1)+(-3,1,2)+k(0,-3,3)$$
$$= (-1,\ -2k+2,\ 2k-1)$$
$$n+m-p_2 = (8k+13)+4-(10+8k) = 7$$
$$\Delta V_2 = 4(-1,-2k{+}2,2k{-}1) + 7(0,-3,3) - (2,-5,3)$$
$$= (-4,\ -8k{+}8,\ 8k{-}4) + (0,\ -21,\ 21) + (-2,\ 5,\ -3)$$
$$= \mathbf{(-6,\ -8k-8,\ 8k+14)}$$

### The two deltas cancel

$$\Delta V_1 + \Delta V_2 = (6{-}6,\ (8k{+}8){-}(8k{+}8),\ (-8k{-}14){+}(8k{+}14)) = (0,0,0)$$

Therefore:
$$V(k+1) = V(k) + \Delta V_1 + \Delta V_2 = \mathbf{0} + \mathbf{0} = \mathbf{0}\ \checkmark$$

---

## Conclusion

By induction, $V(k)=\mathbf{0}$ for all $k\geq 1$: the polyiamond $S_k = ABF + (DFBF)^k + DED + (CDCB)^k + CDC$ **always returns to its starting point**. $\blacksquare$

> **Elegant observation:** $\Delta V_1$ and $\Delta V_2$ are exact negatives of each other. This happens because $P(CDCB) = -3\cdot P(DFBF)$, so inserting one block of each type creates equal and opposite perturbations to the closure sum.
