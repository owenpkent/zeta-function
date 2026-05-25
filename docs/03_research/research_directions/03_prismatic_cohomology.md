# Direction 3: Prismatic cohomology of Spec(W(Z)), all five technical questions resolved

> **Parent doc**: [`2A_R5_prismatic_cohomology.md`](../../../experiments/arithmetic_geometric/2A_R5_prismatic_cohomology.md) (the original R5 analysis). This document is the operational execution roadmap.
>
> **Phase in proof_program.md**: Phase 2 (years 2-3).
>
> **Headline**: apply Bhatt-Morrow-Scholze (BMS) prismatic cohomology to Borger's W(Z), and resolve the five technical questions R5.1-R5.5 that close constraints (iv)-(vii) of the 17-constraint framework.

## 1. Problem statement

Prismatic cohomology (BMS 2018-2019, Bhatt-Scholze 2022) unifies p-adic cohomology theories (étale, crystalline, de Rham, Hodge-Tate) into a single framework built on delta-rings. A delta-ring (R, delta) has an operator delta: R -> R satisfying:
- delta(0) = 0
- delta(1) = 0
- delta(x + y) = delta(x) + delta(y) - sum_{i=1}^{p-1} (1/p) (p choose i) x^i y^{p-i}
- delta(xy) = x^p delta(y) + y^p delta(x) + p delta(x) delta(y)

Delta-rings are essentially "Lambda-rings at one prime p": the operator delta(x) = (psi_p(x) - x^p)/p relates them to Lambda-ring Adams operations.

R5's structural finding: Borger's Lambda-structure on Z (and on W(Z)) gives delta-structures at every prime, so prismatic cohomology naturally applies to Spec(W(Z)).

The five technical questions to resolve:
- **Q1**: define the prismatic cohomology of Spec(W(Z)) precisely.
- **Q2**: verify finite-dimensionality / trace-class structure.
- **Q3**: verify Poincaré duality.
- **Q4**: construct the cycle class map.
- **Q5**: verify Künneth formula for products.

## 2. What "done" looks like

A 50-80 page paper "Prismatic cohomology of the big Witt scheme of Z" containing:

1. **Q1 resolution**: explicit description of the prismatic site of Spec(W(Z)) and its derived prismatic cohomology RGamma_pris(Spec(W(Z))).
2. **Q2 resolution**: finite-dimensionality theorem (or precise characterization of when it holds, in some completed/perfect sense).
3. **Q3 resolution**: Poincaré duality statement and proof for an appropriate "compactification" of Spec(W(Z)).
4. **Q4 resolution**: cycle class map from arithmetic cycles to prismatic cohomology classes.
5. **Q5 resolution**: Künneth formula for Spec(W(Z)) x Spec(W(Z)) and other product schemes.
6. Comparison theorems: prismatic cohomology of Spec(W(Z)) compared to étale cohomology of Spec(Z), crystalline cohomology at each prime, de Rham cohomology in the limit.

The paper would close constraints (iv)-(vii) of the 17-constraint scorecard for Borger's framework. Publishable in Annals or Compositio.

## 3. Prerequisites

- Working knowledge of BMS prismatic cohomology (Bhatt-Morrow-Scholze 2018-2019, Bhatt-Scholze 2022).
- Working knowledge of delta-rings (Joyal 1985, Buium 1996+).
- Working knowledge of Borger's big Witt ring functor and Lambda-algebraic geometry.
- Comfort with derived / infinity-categorical machinery (the prismatic site lives there).
- Working knowledge of p-adic Hodge theory (Fontaine theory, perfectoid spaces).

## 4. Sub-problems and milestones

### 4.1 Q1: Define prismatic cohomology of Spec(W(Z))

The big Witt scheme W(Z) is profinite. The prismatic site of a profinite object requires careful handling. Options:

- (a) Define it as a derived inverse limit of prismatic sites of truncated Witt rings W_n(Z).
- (b) Define it directly via the formal scheme structure of Spf W(Z) (if one exists in a useful sense).
- (c) Use Bhatt's recent (2024+) work on prismatic sites of formal schemes.

**Milestone**: precise definition with verification of basic properties (functoriality, base change, comparison with classical cohomology theories in special cases). ~15 pages.

**Falsifiability**: if no consistent definition exists (e.g., the inverse limit doesn't converge or has pathological behavior), Q1 fails and Direction 3 is blocked.

### 4.2 Q2: Finite-dimensionality

Prismatic cohomology of a smooth proper scheme over a field is finite-dimensional. Spec(W(Z)) is not smooth proper in the classical sense. The finite-dimensionality question is therefore subtle.

Options:
- (a) Show finite-dimensionality holds in a derived / completed sense.
- (b) Show that for the trace formula to work, only a "trace-class" property is needed (weaker than finite-dimensional).
- (c) Show finite-dimensionality holds for an appropriate "compactification" of Spec(W(Z)) à la Arakelov.

**Milestone**: finite-dimensionality theorem (or trace-class result), ~10 pages.

**Falsifiability**: if no version of finite-dimensionality holds, the Lefschetz trace formula in Direction 4 cannot be defined cleanly. May still be possible to proceed with a different regularization scheme.

### 4.3 Q3: Poincaré duality

In classical algebraic geometry, Poincaré duality on a d-dimensional smooth proper variety gives a non-degenerate pairing H^i x H^{2d - i} -> H^{2d}.

For Spec(W(Z)), the "dimension" question is delicate (W(Z) has Krull dimension 2 in truncated cases but profinite in the full case). The duality should be:
- H^i_pris(Spec(W(Z))) x H^{n - i}_pris(Spec(W(Z))) -> H^n_pris(Spec(W(Z)))
for an appropriate cohomological dimension n.

**Milestone**: Poincaré duality theorem with explicit n and verification of non-degeneracy, ~15 pages.

**Falsifiability**: if no Poincaré duality holds, the Weil-template proof structure is broken at the second pillar.

### 4.4 Q4: Cycle class map

The cycle class map sends arithmetic cycles on Spec(W(Z)) to prismatic cohomology classes:

cl: CH^i(Spec(W(Z))) -> H^{2i}_pris(Spec(W(Z)))

(or to some appropriately graded prismatic cohomology). This is necessary for the intersection theory of Direction 8 to translate to cohomological positivity.

**Milestone**: cycle class map definition with verification of basic properties (functoriality, compatibility with intersection product), ~10 pages.

**Falsifiability**: if no natural cycle class map exists, Direction 8's intersection theory cannot be cohomologized. May still be possible via direct algebraic-geometric methods.

### 4.5 Q5: Künneth formula

The Künneth formula for prismatic cohomology of products:

H^*_pris(X x Y) ≅ H^*_pris(X) ⊗ H^*_pris(Y)

For Spec(W(Z)) x Spec(W(Z)) (the surface), this is the structural ingredient needed for the Hodge index theorem on a surface.

**Milestone**: Künneth theorem, ~10 pages.

**Falsifiability**: if no Künneth holds, the surface structure on the product is not cohomologically detected, and the Weil-template proof's third pillar is broken.

## 5. Falsifiability summary

- Q1 fails: no consistent prismatic cohomology of Spec(W(Z)). Direction 3 is blocked.
- Q2 fails: no finite-dimensionality / trace-class. Direction 4's trace formula is blocked.
- Q3 fails: no Poincaré duality. Direction 8 cannot proceed.
- Q4 fails: no cycle class map. Direction 8 cannot proceed.
- Q5 fails: no Künneth. Direction 8 cannot proceed on the surface.

Q1, Q3, Q4, Q5 are independently necessary. Q2 has weaker variants that might be sufficient. Sequential failure of Q2 might be repairable; failure of any of Q1, Q3, Q4, Q5 likely is not.

## 6. Estimated effort

4-8 postdoc-years. Calendar time: 2-3 years for a 2-3 person group with prismatic-cohomology expertise.

Each of Q1-Q5 is publishable as a separate paper if substantial. As a complete program, a single 50-80 page paper is the right format.

## 7. Connections

- **Direction 1** (Lambda-blueprints): if the Lambda-blueprint surface is the chosen surface, Direction 3 should extend to that surface (not just Spec(W(Z))).
- **Direction 2** (Borger+Connes hybrid): the cohomology H^*(W(Z), psi) in Direction 2 should agree with prismatic cohomology where they overlap.
- **Direction 4** (prismatic foliation): builds on Direction 3 by adding the foliation structure. Q1-Q5 are prerequisites.
- **Direction 8** (Hodge index): Q3, Q4, Q5 are inputs to the Hodge index argument.
- **2E** ([`2E_adams_spectrum_probe.md`](../../../experiments/arithmetic_geometric/2E_adams_spectrum_probe.md)): the negative result that bare psi_p has no zeta-zero spectrum is the structural motivation for Direction 3.

## 8. References

- Bhatt, B.; Morrow, M.; Scholze, P. (2019). *Integral p-adic Hodge theory*. Publ. Math. IHES 129, 199-310.
- Bhatt, B.; Scholze, P. (2022). *Prisms and prismatic cohomology*. Ann. Math. 196.
- Bhatt, B. (2022). *Prismatic F-crystals and crystalline Galois representations*. arXiv:2206.10240.
- Joyal, A. (1985). *Delta-anneaux et vecteurs de Witt*. CR Math. Rep. Acad. Sci. Canada 7.
- Buium, A. (1996). *Geometry of differential polynomial functions, I, II, III*.
- Borger, J. (2009). *Lambda-rings and the field with one element*. arXiv:0906.3146.

## 9. Status

This direction is **research-grade, beyond project scope**. The 2A R5 analysis provides the framework; this document provides the operational specification. Execution requires a research mathematician with prismatic-cohomology expertise (postdoc-or-faculty level) operating over 2-3 years.

The Q1-Q5 individual results are independently valuable contributions to p-adic Hodge theory and arithmetic geometry, regardless of the broader proof program.
