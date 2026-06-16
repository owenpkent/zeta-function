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

## Mathlib dependency audit

**Present (usable):**
- Weierstrass curves, the affine model, and the group law (Angdinata-Xu, ITP 2023;
  `Mathlib.AlgebraicGeometry.EllipticCurve.*`).
- Finite fields, $\sqrt q$ bounds, basic field theory.
- The repo's own `IsogenyDegree.lean` / `FunctionFieldRH.lean` (the path-(a) downstream chain), reusable
  for the final $t^2 \le 4q \Rightarrow |\alpha|^2 = q$ step if the bound is obtained.

**Absent (the real work), roughly in dependency order:**
1. The pole-order filtration $R_n$ on the Weierstrass function field and $\dim R_n \ge n$ (elementary,
   but needs the function field + a pole-order valuation at $\infty$; partially constructible from
   Mathlib's coordinate ring).
2. The Frobenius endomorphism on $E/\mathbb{F}_q$ and the fact that its fixed points are exactly
   $E(\mathbb{F}_q)$ (needs Frobenius on the curve; status unclear, likely partial).
3. Rational functions on $C \times C$ and the pole-order bookkeeping for $V = R_\ell \otimes R_m$.
4. "#zeros = #poles on a projective curve" (a divisor-degree statement; this is the one piece closest
   to needing real divisor theory, and the likeliest hidden cost).
5. The lower-bound trick ($\mathbb{F}_{q^2}$ non-residue or the functional equation).

## Milestone plan (path b1, elliptic curves)

- **M-b1.1** the explicit $R_n$ filtration + $\dim R_n \ge n$ from the Weierstrass basis.
- **M-b1.2** Frobenius on $E/\mathbb{F}_q$; fixed points $=$ $E(\mathbb{F}_q)$.
- **M-b1.3** divisor degree on $E$: #zeros $=$ #poles (the load-bearing analytic input).
- **M-b1.4** the auxiliary function on $C \times C$ + the injectivity/degree-count upper bound.
- **M-b1.5** the lower bound; assemble $|t| \le 2\sqrt q$; wire into the existing eigenvalue step.

## Verdict

**Path (b1) is the better unconditional target, but it is still a multi-month formalization.** It is
genuinely more tractable than (a) because it avoids the Tate module / Galois-representation machinery
(no FLT dependency) and, specialized to elliptic curves, avoids general Riemann-Roch. The honest cost
center is M-b1.3 (divisor degree / #zeros = #poles), the one step that brushes against the divisor
theory Mathlib only partially has; it should be the **first feasibility probe** before committing,
because if it needs general scheme cohomology the wall is back.

**Recommendation.**
- **Short term:** the only *finished* artifact is the path-(a) conditional reduction. If a paper is
  wanted now, it is "a conditional Lean formalization reducing function-field RH to the existence of
  $A$" (modest, honest).
- **Higher-value target:** path (b1). **Gate it on a one-week M-b1.3 feasibility probe** (can
  #zeros = #poles for the Weierstrass curve be built from current Mathlib without scheme cohomology?).
  If yes, (b1) is a clean, citable, Mathlib-bound contribution and the right thing to build. If no,
  fall back to the conditional reduction and coordinate the Tate-module piece with the FLT project.

This is the one research/formalization candidate that survived its lit-check; it is worth the probe.
