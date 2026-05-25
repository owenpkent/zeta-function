# Direction 4: 2D-M3 prismatic foliation hypothesis verified

> **Parent doc**: [`2D_deninger_micro_target.md`](../../../experiments/arithmetic_geometric/2D_deninger_micro_target.md) (the 2D analysis identifying M3 as the smallest open conjecture in Deninger's program). This document is the operational execution roadmap.
>
> **Phase in proof_program.md**: Phase 2 / 3 boundary (years 2-4).
>
> **Headline**: define a foliation F on the prismatic site of Spec(W(Z)) (or the Lambda-blueprint surface from Direction 1) whose leaves are orbits of Phi_t = prod_p U_{log p}^{t/log p} (the R4 multiplicative-completion flow), and verify the leafwise prismatic cohomology has finiteness, Poincaré duality, Künneth, and a Lefschetz trace formula recovering at least the Euler-product piece of zeta(s).

## 1. Problem statement

Direction 4 combines:
- The flow Phi_t from Direction 2 (R4 multiplicative completion of Adams operations).
- The prismatic cohomology of Direction 3 (R5 BMS framework applied to W(Z)).
- The foliated-cohomology framework from Deninger's program (leafwise cohomology of a foliation).

The four formal properties to verify:

1. **Finiteness**: H^i_{F, pr} is finite-dimensional (or trace-class for Phi_t) in a precise sense.
2. **Poincaré duality**: a non-degenerate pairing H^i_{F, pr} ⊗ H^{n-i}_{F, pr} -> H^n_{F, pr} for the appropriate cohomological dimension n.
3. **Künneth**: H^*_{F, pr}(X x X) = H^*_{F, pr}(X) ⊗ H^*_{F, pr}(X) for the leafwise prismatic site of the double.
4. **Lefschetz trace formula**: a regularized determinant det_zeta(s · id - Phi_t | H^*_{F, pr}) recovering at least the Euler product piece of zeta(s).

What M3 does NOT include: the Hodge index theorem on X x X. That is Direction 8.

## 2. What "done" looks like

A 40-60 page paper "Prismatic foliations and the zeta function of Spec(Z)" containing:

1. Definition of the foliation F on the prismatic site, with explicit description of leaves as Phi_t orbits.
2. Construction of leafwise prismatic cohomology H^*_{F, pr}.
3. Verification of (1)-(4) above.
4. Comparison with classical leafwise cohomology of foliated manifolds (Connes, Heitsch-Lazarov).
5. Explicit computation in low-dimensional cases.

Publishable in Inventiones, Annals of Math, or JAMS. This closes constraints (iv)-(v)-(vii) and partially (viii)-(ix) of the 17-constraint scorecard.

## 3. Prerequisites

- Direction 2 (Borger+Connes hybrid): provides Phi_t = prod_p U_{log p}^{t/log p}.
- Direction 3 (prismatic cohomology Q1-Q5): provides the cohomology theory on which the foliation lives.
- Working knowledge of foliated cohomology (Connes 1982-1994, Moore-Schochet, Heitsch-Lazarov).
- Working knowledge of Deninger's program (Deninger 1991, 1998, 2002, 2008).
- Working knowledge of regularized determinants and zeta-function regularization.

Direction 4 sits at the intersection of Direction 2 and Direction 3. Its rigorous treatment requires those directions to have advanced enough that Phi_t and prismatic cohomology are both available.

## 4. Sub-problems and milestones

### 4.1 Define the foliation

A foliation on the prismatic site is non-standard. The classical notion (a smooth foliation on a manifold) doesn't directly apply. Options:

- (a) Define F via the orbits of Phi_t directly: leaves are Phi_t-invariant subsets of (the formal scheme underlying) the prismatic site.
- (b) Define F via a sub-Lie-algebroid structure on the prismatic site's tangent complex.
- (c) Define F via the kernel of a "leafwise differential" d_F compatible with prismatic data.

**Milestone**: precise definition with verification of basic properties (e.g., Phi_t-invariance, compatibility with prismatic data), ~10 pages.

**Falsifiability**: if no natural foliation structure exists, Direction 4 is fundamentally blocked.

### 4.2 Construct leafwise prismatic cohomology

Once F is defined, the leafwise cohomology H^*_{F, pr} should be a sheaf-cohomology theory on the prismatic site that is "transverse" to F.

**Milestone**: construction of H^*_{F, pr} as a derived functor (or equivalent), ~10 pages.

### 4.3 Finiteness

Inherits from Direction 3 Q2, but with the foliation structure adding more conditions. Specifically: H^i_{F, pr} should be trace-class for Phi_t (so the trace formula in 4.6 makes sense).

**Milestone**: finiteness / trace-class theorem, ~5-10 pages.

### 4.4 Poincaré duality

Inherits from Direction 3 Q3, with the foliation adding the leaf structure. The duality should be:

H^i_{F, pr}(X) x H^{n - i}_{F, pr}(X) -> H^n_{F, pr}(X)

for the appropriate leafwise cohomological dimension n.

**Milestone**: leafwise Poincaré duality, ~10 pages.

### 4.5 Künneth

Inherits from Direction 3 Q5 with foliation product structure.

**Milestone**: Künneth for X x X with the product foliation F x F, ~5-10 pages.

### 4.6 Lefschetz trace formula

The headline result: define a regularized determinant

det_zeta(s · id - Phi_t | H^*_{F, pr})

and verify it equals (or includes as a factor) zeta(s) restricted to the Euler product piece, i.e., prod_p (1 - p^{-s})^{-1}.

Methodology:
- For each prime p, the action of psi_p on H^*_{F, pr} should have eigenvalues that contribute (1 - p^{-s})^{-1} to the regularized determinant.
- The multiplicative completion Phi_t = prod_p U_{log p}^{t/log p} should give the full Euler product when traced.

**Milestone**: trace formula calculation with explicit zeta-regularization, ~15-20 pages.

**Falsifiability**: if the regularized determinant gives a DIFFERENT zeta-like function, the framework is recovering an adjacent object. If it gives nothing recognizable, the framework is broken.

## 5. Falsifiability summary

- 4.1 fails: no natural foliation. Direction 4 blocked.
- 4.2 fails: leafwise cohomology not well-defined.
- 4.3-4.5 fail: cohomology lacks the basic properties.
- 4.6 fails: trace formula recovers something other than zeta's Euler product.

5-year window to verify (1)-(4) of M3. If not verified, the framework is structurally incompatible with Deninger's program; pivot to alternative cohomology choices (Hochschild, motivic, cyclic).

## 6. Estimated effort

4-8 postdoc-years. Calendar time: 2-4 years.

Direction 4 depends on Directions 2 and 3. Sequence: Direction 2 first (gives Phi_t), then Direction 3 (gives prismatic cohomology), then Direction 4 (combines them).

## 7. Connections

- **Direction 2** (Borger+Connes): provides Phi_t.
- **Direction 3** (prismatic cohomology): provides the cohomology theory.
- **Direction 8** (Hodge index): Direction 4's leafwise prismatic cohomology is the cohomology in which the Hodge index theorem must be proved.
- **2D** ([`2D_deninger_micro_target.md`](../../../experiments/arithmetic_geometric/2D_deninger_micro_target.md)): the M3 statement is the verbatim deliverable of Direction 4.
- **Deninger's program** ([`2A_deninger_dossier.md`](../../../experiments/arithmetic_geometric/2A_deninger_dossier.md)): Direction 4 is the most concrete realization of Deninger's foliated dynamical system X via the Borger+Connes+prismatic hybrid.

## 8. References

- Deninger, C. (1998). *Some analogies between number theory and dynamical systems on foliated spaces*. Doc. Math. Extra Vol. ICM Berlin 1998, I, 163-186.
- Connes, A. (1982). *A survey of foliations and operator algebras*. Proc. Sympos. Pure Math. 38.
- Heitsch, J.; Lazarov, C. (2002). *Spectral asymptotics of foliated manifolds*. Illinois J. Math. 46.
- Bhatt, B.; Morrow, M.; Scholze, P. (2019). *Integral p-adic Hodge theory*. Publ. Math. IHES 129.
- Leichtnam, E. (2005). *Scaling group flow and Lefschetz trace formula for laminated spaces*. Bull. Sci. Math. 129.

## 9. Status

This direction is **research-grade, beyond project scope**. The 2D dossier identifies M3 as the right size; this document provides the operational specification. Execution requires a research group with expertise in (a) prismatic cohomology, (b) noncommutative geometry, (c) Deninger-style foliated dynamics. Estimated 2-4 years.

A positive resolution would be the first explicit realization of Deninger's foliated space X, a major contribution to arithmetic geometry independent of whether the broader proof program reaches its target.
