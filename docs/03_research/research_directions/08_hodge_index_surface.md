# Direction 8: The Hodge index theorem on a constructed arithmetic surface

> **The central open problem.** Every other direction in this research_directions/ folder builds toward this one. Identified throughout the project: [`2A_weil_proof_diff.md`](../../../experiments/arithmetic_geometric/2A_weil_proof_diff.md) §3 makes it explicit; [`2A_R3_5_K1_universality.md`](../../../experiments/arithmetic_geometric/2A_R3_5_K1_universality.md) proves it is the UNIQUE escape route from the K1 wall; [`2A_path_forward.md`](../../../experiments/arithmetic_geometric/2A_path_forward.md) treats it as the central open problem.
>
> **Phase in proof_program.md**: Phase 4 (years 4-10). This is THE central problem.
>
> **Headline**: prove a Hodge index theorem on the constructed surface $S = \mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ (or its analog in the chosen surface framework), giving positivity from the SIGNATURE of an intersection form. This is the unique known route to escape the K1 wall (R3.5) and close RH via Architecture 2.

## 1. Problem statement

In Weil's 1948 proof of RH for curves over $\mathbb{F}_q$, the Hodge index theorem provides the central positivity argument:

**Hodge index theorem (function field case)**: on the smooth proper surface $C \times C$ over $\mathbb{F}_q$ (where $C$ is a curve), the intersection form on the divisor group $\mathrm{Div}(C \times C)$, restricted to the orthogonal complement of an ample divisor, is NEGATIVE DEFINITE.

Equivalently: the intersection form has signature $(1, 2g)$ where $g$ is the genus of $C$.

This is what FORCES the Frobenius eigenvalues on $H^1(C, \mathbb{Q}_\ell)$ to have magnitude $\sqrt{q}$, closing RH for the curve.

**Direction 8's question**: state and prove an analogous Hodge index theorem on the constructed arithmetic surface $S$ from Direction 1 (Lambda-blueprints) or Direction 2 (Borger+Connes hybrid).

The hard part: $S$ is not a smooth proper variety in the classical sense. Its "intersection form" must be defined via the framework's machinery (prismatic cohomology from Direction 3, leafwise from Direction 4, possibly hyperring-valued from Direction 5).

## 2. What "done" looks like

A 100-200 page paper or monograph "Hodge index theorem for the arithmetic surface below $\mathrm{Spec}(\mathbb{Z})$" containing:

1. The precise statement of the Hodge index theorem in the chosen framework (signature condition on the intersection form).
2. The proof, by some combination of:
   - (4.A) Tropical Hodge index theorem (Adiprasito-Huh-Katz 2018) lifted to the arithmetic surface.
   - (4.B) Sheaf-theoretic positivity in the Connes-Consani topos.
   - (4.C) Direct algebraic-geometric argument on the Lambda-blueprint surface.
3. Verification that the Hodge index implies RH for zeta (via the Weil-template proof).
4. Verification that the Hodge index does NOT imply RH for Davenport-Heilbronn (the K2 check).
5. Verification that the proof specializes to Weil 1948 in the function-field case (the K3 check).
6. Verification that the proof escapes R3.5's no-shortcut theorem (the K1 check).

This is a candidate proof of RH. Publishable in Annals of Math. Submission to the Clay Mathematics Institute for the Millennium Prize.

## 3. Prerequisites

The full prerequisite stack:
- Direction 1 OR Direction 2: the surface $S$ exists as a Lambda-blueprint or as Borger's $\mathrm{Spec}(W(\mathbb{Z}))$.
- Direction 3: prismatic cohomology of $S$ is well-defined with Q1-Q5 resolved.
- Direction 4: the prismatic foliation hypothesis (M3) is verified.
- (Optional) Direction 5: Connes-Consani infrastructure is available (hyperring intersection theory, tropical bridge).
- Working knowledge of classical Hodge theory (Griffiths-Schmid, Voisin's books).
- Working knowledge of arithmetic intersection theory (Arakelov, Faltings, Gillet-Soulé).
- Working knowledge of tropical Hodge theory (Adiprasito-Huh-Katz, Babaee-Huh).
- Working knowledge of motivic and étale cohomology.
- Mathematical taste and judgment at the level of a top-tier research mathematician.

## 4. Three a priori distinct attack angles

### 4.A Tropical-arithmetic Hodge bridge

**Approach**: adapt the Adiprasito-Huh-Katz tropical Hodge index theorem (2018) to the arithmetic surface $S$.

The AHK theorem says: for a tropical variety $X^{\text{trop}}$ of pure dimension $d$, the Hodge-Riemann relations hold on the Chow ring of $X^{\text{trop}}$.

The adaptation: treat $S$ as a "tropical limit" of some classical algebraic variety (or as a stand-alone object with tropical-like structure). Apply AHK.

**Obstacles**:
- Tropical varieties live in $\mathbb{R}^n$, not over $\mathrm{Spec}(\mathbb{Z})$.
- The Connes-Consani characteristic-one limit maps $\mathbb{F}_q$-objects to tropical objects in the $q \to 1$ limit. But $\mathrm{Spec}(\mathbb{Z})$ is not $\mathbb{F}_q$-defined for any $q$.
- The "tropicalization" of $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ is not standard.

This is Direction 5's R3.6.3.c sub-direction (the tropical-arithmetic Hodge bridge). Probability of success: ~10% per R3.6.3 analysis.

### 4.B Sheaf-theoretic positivity in the Connes-Consani topos

**Approach**: develop a sheaf-theoretic Hodge index on the Connes-Consani arithmetic site $\mathcal{A}$, using hyperring-valued sheaves.

The natural setting: hyperring sheaves on $\mathcal{A}$ (post-Direction 5 development) might host a "signature" structure that gives positivity.

**Obstacles**:
- No published work points in this direction directly.
- Hyperring-sheaf Chow theory is not developed (Direction 5 R3.6.3.b).
- The "signature" interpretation of a hyperring-valued bilinear form is not standard.

Probability of success: ~5% per R3.6.3 analysis (lower than 4.A because more layers of new mathematics required).

### 4.C Direct algebraic-geometric construction

**Approach**: forget the F_1 / hyperring machinery. On the Lambda-blueprint surface $S$ (Direction 1), equipped with prismatic cohomology (Direction 3) and the foliation structure (Direction 4), directly argue Hodge index via classical algebraic-geometric methods.

Specifically: show that the intersection form on $H^*_{\mathcal{F}, \mathrm{pr}}(S)$ has signature $(1, k)$ on the appropriate subspace.

**Obstacles**:
- "Classical algebraic-geometric methods" assumes the surface behaves classically, which is the very thing in question.
- The intersection form may have different signature structure than the function-field case.
- No a priori reason the signature is $(1, k)$ rather than, e.g., $(2, k)$ or $(0, k)$.

This is the MOST CONSERVATIVE approach and most likely to succeed if the surface is "geometric enough" to support classical-style arguments. Probability of success: ~12-15% — the bulk of Direction 8's success probability comes from 4.C.

### Sub-direction probabilities (for direction 8 alone, conditional on Directions 1-3 succeeding)

- 4.A: 10%
- 4.B: 5%
- 4.C: 12-15%
- All three pursued in parallel: 25-30% probability that AT LEAST ONE succeeds.

## 5. Sub-problems and milestones (for the chosen attack angle)

Independent of which angle is chosen, the key milestones are:

### 5.1 State the Hodge index precisely

Define the intersection form on the appropriate (co)homology / Chow group of $S$. State the signature condition.

**Milestone**: precise statement, ~10 pages.

### 5.2 Prove the Hodge index theorem

The bulk of the work. Approach via 4.A, 4.B, or 4.C.

**Milestone**: the proof, 50-100 pages.

### 5.3 Derive RH from Hodge index

Use the Weil template: Lefschetz + Poincaré duality + Hodge index forces the relevant eigenvalues to have unit magnitude.

**Milestone**: 5-10 pages.

### 5.4 Verify D-H discipline (K2)

The proof must not "prove RH" for Davenport-Heilbronn. K2 is satisfied by construction of the surface framework (per Direction 1's verification), but the assembled proof must transparently use the Euler-product / cohomological structure that D-H lacks.

**Milestone**: K2 verification, ~5 pages.

### 5.5 Verify Weil specialization (K3)

The proof restricted to a curve over $\mathbb{F}_q$ must recover Weil 1948.

**Milestone**: K3 verification, ~5 pages.

### 5.6 Verify K1 escape

The positivity must come from the SIGNATURE of an intersection form, NOT from a trace identity. Otherwise R3.5 kicks in and the proof is circular.

**Milestone**: K1 verification with explicit structural argument, ~5 pages.

## 6. Falsifiability

Direction 8 is FALSIFIED (and the proof program either pivots or terminates) if:

- All three attack angles (4.A, 4.B, 4.C) fail to produce a proof in 5-7 years.
- The intersection form on $H^*(S)$ has signature OTHER than $(1, k)$. The Weil-template approach is structurally incompatible with $S$.
- The proof goes through but violates K1, K2, or K3. The proof is circular or insufficient.
- A counterexample is found: an alternative $S$ where the Hodge index holds but RH fails. This would refute the entire approach.

Per the marginal-positivity thesis, the prior probability that Direction 8 succeeds is LOW (<15%). But the structural argument (R3.5) says this is the unique route, so it must be attempted.

## 7. Estimated effort

20-50 postdoc-years. Calendar time: 7-15 years.

This is the longest and hardest direction. It requires:
- A multi-person research group with deep expertise across arithmetic geometry, NCG, prismatic cohomology, and tropical geometry.
- Funding over the 7-15 year timeline.
- Patience: most years will produce partial results without closing the central problem.

## 8. Connections

- **Every other direction**: Directions 1-7 are infrastructure for Direction 8.
- **Direction 1 / 2**: provide the surface $S$.
- **Direction 3**: provides the cohomology theory on $S$.
- **Direction 4**: provides the foliation structure (if applicable).
- **Direction 5**: provides infrastructure for attack angles 4.A and 4.B.
- **Direction 7**: alternative (smaller) Architecture 4 escape; doesn't close Direction 8 but provides a partial result if Direction 8 stalls.
- **R3.5** ([`2A_R3_5_K1_universality.md`](../../../experiments/arithmetic_geometric/2A_R3_5_K1_universality.md)): identifies Direction 8 as the UNIQUE escape route.
- **2A weil proof diff** ([`2A_weil_proof_diff.md`](../../../experiments/arithmetic_geometric/2A_weil_proof_diff.md)): the diff table establishing what Direction 8 must produce.

## 9. References

### Function-field Hodge index (template)
- Weil, A. (1948). *Sur les courbes algébriques et les variétés qui s'en déduisent*. Hermann.
- Deligne, P. (1974, 1980). *La conjecture de Weil*. Publ. Math. IHES 43, 52.

### Arithmetic Hodge index (partial)
- Faltings, G. (1984). *Calculus on arithmetic surfaces*. Ann. Math. 119.
- Gillet, H.; Soulé, C. (1992). *An arithmetic Riemann-Roch theorem*. Invent. Math. 110.
- Bost, J.-B. (1990s+). Multiple papers on arithmetic intersection theory.

### Tropical Hodge index (the AHK breakthrough)
- Adiprasito, K.; Huh, J.; Katz, E. (2018). *Hodge theory for combinatorial geometries*. Ann. Math. 188(2), 381-452.
- Babaee, F.; Huh, J. (2017). *A tropical approach to a generalized Hodge conjecture for positive currents*. Duke Math. J. 166(14).
- Mikhalkin, G. (2005). *Enumerative tropical algebraic geometry in $\mathbb{R}^2$*. J. AMS 18.

### F_1 and related
- See [Direction 1 references](01_lambda_blueprints.md#8-references).
- See [Direction 2 references](02_borger_connes_hybrid.md#8-references).

### Deninger's program
- Deninger, C. (1998). *Some analogies between number theory and dynamical systems on foliated spaces*. Doc. Math. ICM Berlin 1998.
- Deninger, C. (2002). *A note on arithmetic topology and dynamical systems*. Contemp. Math. 300.

## 10. Status

**This is THE central open problem of the proof program.** Status: open. No known proof, no known obstruction.

Probability of success, conditional on Directions 1-3 succeeding: 25-30% (at least one of 4.A, 4.B, 4.C delivers).

Probability of success unconditional: under 1% (because Directions 1-3 themselves have probabilities under 50% each).

Either outcome (proof or refutation) would be a top-tier mathematical result. A proof closes RH. A refutation (e.g., showing the natural intersection form has wrong signature) would identify a deep structural obstacle and force the entire architectural picture to be rethought.

Most likely actual outcome over 10-15 years: substantial partial progress (lifting of AHK to arithmetic settings, development of new intersection theories, refinement of the surface frameworks), without a definitive resolution either way. The partial results would themselves be major contributions to arithmetic geometry.

## 11. Closing

If RH is true, the proof goes here. The R3.5 no-shortcut theorem says there is no other way (within the four-architecture framework). The marginal-positivity thesis says the proof must use exact zeta structure. The Hodge index theorem on a constructed arithmetic surface is the unique candidate combining "exact zeta structure" with "structural positivity from a signature".

This is what would actually close the Riemann Hypothesis. Everything else in the project leads here.
