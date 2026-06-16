# Scoping (P6): an unconditional Lean Hasse bound for elliptic curves

> Status: **scoping**, 2026-06-16. Registry entry: [`../PUBLICATIONS.md`](../PUBLICATIONS.md) P6.
> Decision being scoped: P6 path **(b)**, the unconditional Hasse bound via the elementary
> Stepanov-Bombieri method, vs the existing conditional chain (path **(a)**). Read "Verdict" first.

## Goal

An **unconditional**, sorry-free Lean theorem: for an elliptic curve $E/\mathbb{F}_q$,
$$\bigl|\, \#E(\mathbb{F}_q) - (q+1)\,\bigr| \le 2\sqrt q,$$
i.e. the genus-1 Hasse bound, with no hypothesis like the existence of the Frobenius Tate-module
representation $A$ (which path (a) assumes and which is FLT-adjacent / months out).

## The two routes, and why the lit-check reshaped the choice

| Route | Idea | Deep dependency | Mathlib status of that dependency |
|-------|------|-----------------|-----------------------------------|
| **(a)** endomorphism / deg = det | $\deg$ is a positive-definite quadratic form on $\mathrm{End}(E)$; $\deg(\phi - n) \ge 0$ gives $t^2 \le 4q$ (Hasse's original; the repo's existing chain formalizes everything *downstream* of this) | the existence of $A$ = Frobenius on the Tate module with $\deg = \det$ and $\deg \ge 0$ | **absent**, FLT-adjacent (the repo's open input O1) |
| **(b)** Stepanov-Bombieri | construct a rational function on $C \times C$ of controlled pole order vanishing on the Frobenius graph; degree-count | **Riemann's inequality** $\dim R_n \ge n + 1 - g$ (weak Riemann-Roch) | for general curves: **absent and "a long way off"** (Mathlib lacks sheaf cohomology for schemes); **for elliptic curves: elementary** (see below) |

The lit-check (2026-06-16) found that the general Stepanov-Bombieri route hits the Riemann-Roch wall,
so naively (b) is no freer than (a). **But the elliptic-curve specialization dodges that wall.**

## The Bombieri-Stepanov skeleton (Tao's exposition)

Source: [Tao, *The Bombieri-Stepanov proof of the Hasse-Weil bound*](https://terrytao.wordpress.com/2014/05/02/the-bombieri-stepanov-proof-of-the-hasse-weil-bound/).

1. Work on $C \times C$; let $R_n$ be the rational functions with poles of order $\le n$ only at
   $P_\infty$. Form $V = R_\ell \otimes R_m$.
2. **Injectivity (Lemma 3).** If $\ell < \sqrt q$, the pole orders $d_i + \sqrt q\, e_j$ of the
   tensor-basis elements are all distinct, so the projection onto $k(C_1)$ (the Frobenius graph) is
   injective.
3. **Auxiliary function.** By dimension counting, find $0 \ne f \in V$ vanishing on the Frobenius graph
   $C_1$ but not identically; its pole order is $\le \ell + m\sqrt q$.
4. **Upper bound (Prop 4).** On a projective curve #zeros = #poles, and the relevant zeros are exactly
   the $\mathbb{F}_q$-points, so $\#C(\mathbb{F}_q) \le \ell + m\sqrt q$. Optimizing $\ell, m$ gives
   $\#C(\mathbb{F}_q) \le q + O(\sqrt q)$.
5. **Lower bound.** Pass to a reducible auxiliary curve / use the $\mathbb{F}_{q^2}$ non-residue trick
   (Theorem 5), or the functional equation, to get the matching lower bound.

External theorems: Riemann's inequality $\dim R_n \ge n+1-g$; that Frobenius fixed points are exactly
$\mathbb{F}_q$-points; #zeros = #poles on a projective curve (a divisor-degree fact).

## The elliptic-curve specialization (the unlock)

For $g = 1$ with a Weierstrass model $y^2 = x^3 + ax + b$, the spaces $R_n$ are **explicit**:
$$R_0 = \langle 1\rangle,\quad R_1 = \langle 1, x\rangle,\quad R_2 = \langle 1, x, y\rangle,\quad
R_3 = \langle 1, x, y, x^2\rangle,\ \dots$$
(monomials $x^i$ and $x^i y$ ordered by pole order at $\infty$: $\deg_\infty x = 2$, $\deg_\infty y =
3$). So $\dim R_n \ge n$ for $n \ge 1$ is **proved by exhibiting the basis**, with no general
Riemann-Roch and no sheaf cohomology. This is the workaround to the Mathlib RR wall.

## Mathlib dependency audit (probed against the v4.30.0 source cache, 2026-06-16)

**Present (usable):**
- A substantial `Mathlib.AlgebraicGeometry.EllipticCurve.*`: `Affine`, `Projective`, `Jacobian`,
  `Weierstrass`, `DivisionPolynomial`, `Reduction`, and an `LFunction.lean` (the Hasse-Weil
  $L$-function). The group law (Angdinata-Xu, ITP 2023) is here.
- Finite fields, $\sqrt q$ bounds, basic field theory.
- `Mathlib.NumberTheory.FunctionField` (the *rational* function field $\mathbb{F}_q(t)$ as a global
  field, with places + ring of integers) and `Mathlib.AlgebraicGeometry.FunctionField` (the function
  field of a scheme as the generic-point stalk, a definition).
- The repo's own `IsogenyDegree.lean` / `FunctionFieldRH.lean` (the path-(a) downstream chain, pure
  linear algebra), reusable for the final $t^2 \le 4q \Rightarrow |\alpha|^2 = q$ step.

**Absent (the real work):**
1. **No algebraic-curve divisor theory at all.** A source grep finds **no** Weil/Cartier divisor, no
   divisor degree, no Picard group, no Riemann-Roch for curves. The only `*Divisor*` of a function is
   `Analysis/Meromorphic/Divisor.lean` (complex-analytic, wrong setting); every other `*Divisor*` file
   is `NonZeroDivisors` / arithmetic divisor functions / `ChainOfDivisors`. The EC development is built
   **without** divisors (consistent with the Lean precedent that did the group law via the ideal class
   group, ~1500 lines, precisely to avoid the ~6500-line divisor route). So **M-b1.3 cannot reuse
   existing machinery**.
2. The pole-order filtration $R_n$ on the Weierstrass function field and $\dim R_n \ge n$ (M-b1.1):
   elementary but to be built from the coordinate ring + a pole-order valuation at $\infty$.
3. Frobenius on $E/\mathbb{F}_q$ with fixed points $= E(\mathbb{F}_q)$ (M-b1.2): to be built.
4. The lower-bound trick (M-b1.5).

## Milestone plan (path b1, elliptic curves)

- **M-b1.1** the explicit $R_n$ filtration + $\dim R_n \ge n$ from the Weierstrass basis.
- **M-b1.2** Frobenius on $E/\mathbb{F}_q$; fixed points $=$ $E(\mathbb{F}_q)$.
- **M-b1.3** divisor degree on $E$: #zeros $=$ #poles (the load-bearing analytic input).
- **M-b1.4** the auxiliary function on $C \times C$ + the injectivity/degree-count upper bound.
- **M-b1.5** the lower bound; assemble $|t| \le 2\sqrt q$; wire into the existing eigenvalue step.

## Verdict (M-b1.3 probe resolved, 2026-06-16)

**There is no cheap unconditional path in Mathlib v4.30.** The probe killed the hope that (b1) was a
quick win and located the precise blocker: Mathlib has **no curve divisor theory**, so M-b1.3
("#zeros = #poles") cannot be borrowed. Two sub-routes for M-b1.3:

- **(i) general curve divisor theory:** BLOCKED. Building Weil divisors + degree + "principal $\Rightarrow$
  degree 0" for curves is itself a major Mathlib contribution Mathlib has deliberately avoided.
- **(ii) elementary resultant route (elliptic-curve-specific):** PLAUSIBLE but substantial. A function
  $a(x) + b(x)\,y \in R_n$ has poles only at $\infty$, and its affine zeros are the roots of the
  resultant $a(x)^2 - b(x)^2 (x^3 + ax + b)$, whose degree equals the pole order at $\infty$. So
  #zeros = #poles becomes a polynomial-degree identity, doable without divisor theory but needing the
  resultant API + careful multiplicity bookkeeping at $\infty$ and at branch points ($y = 0$, $b(x) =
  0$). Weeks, not days.

So **both P6 paths require months of Mathlib-absent infrastructure**: path (a) needs the Tate module /
deg-as-quadratic-form (FLT-adjacent), path (b1) needs either curve divisor theory (i) or the explicit
resultant build (ii). There is no shortcut.

**Recommendation (updated).**
- **The only finished, citable artifact is the path-(a) conditional reduction.** If a paper is wanted
  in the near term, it is exactly that: "a conditional Lean formalization reducing function-field RH
  for elliptic curves to the existence of the Frobenius Tate-module representation $A$." Modest, honest,
  real, and done.
- **An unconditional Lean Hasse bound is a genuine multi-month project either way.** If pursued, route
  (b1)(ii) (the explicit resultant build) is the most self-contained (no FLT dependency, no scheme
  cohomology), and **M-b1.3(ii) is the first build target to de-risk**, not a one-week probe. Route (a)
  is the alternative and is best coordinated with whatever Tate-module / Galois-representation
  infrastructure the FLT project produces.

This is the one research/formalization candidate that survived its lit-check, but the probe shows it is
a project, not a paper-in-waiting. Decide deliberately.
