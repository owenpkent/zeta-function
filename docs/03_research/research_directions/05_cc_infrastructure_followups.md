# Direction 5: R3.6.3.a/b/c Connes-Consani infrastructure follow-ups

> **Parent doc**: [`2A_R3_6_3_cc_infrastructure.md`](../../../experiments/arithmetic_geometric/2A_R3_6_3_cc_infrastructure.md) (the original R3.6.3 analysis identifying the three follow-ups). This document is the operational execution roadmap for each.
>
> **Phase in proof_program.md**: Phase 3 / 4 support (years 3-7).
>
> **Headline**: develop the three infrastructure follow-ups identified in R3.6.3 — literature deep-dive of Connes-Consani 2017-2025, hyperring tensor product theory at intersection-theory level, and the tropical-arithmetic Hodge bridge — to provide infrastructure for the Hodge index attempt in Direction 8.

## 1. Problem statement

R3.6.3 concluded that Connes-Consani's categorical machinery (arithmetic site topos, hyperring sheaves, characteristic-one calculus) does NOT directly provide K1-escaping positivity but might serve as INFRASTRUCTURE for the geometric route (Direction 8) in three decreasing senses of strength:

- **Strong sense (categorical setting)**: open. No published intersection theory on hyperring-sheaf topoi.
- **Medium sense (combinable ingredients)**: partial. Hyperring sheaves could enrich Borger's W(Z) but the combination is undeveloped.
- **Weak sense (inspiration via tropical Hodge index)**: yes, but doesn't transfer because tropical varieties encode degenerations of existing algebraic varieties.

The three follow-ups R3.6.3.a, .b, .c each target one of these senses.

## 2. R3.6.3.a — Literature deep-dive (2017-2025)

### 2.1 Problem statement

Read Connes-Consani 2017-2025 papers focusing on intersection-theoretic or motivic content. Identify whether the infrastructure has been developed in any direction since R3.6's analysis. Specifically:

- Has the arithmetic site $\mathcal{A}$ been equipped with an intersection product on its cohomology?
- Has hyperring-sheaf algebra been pushed toward Chow-style structures?
- Has the characteristic-one limit been made compatible with arithmetic intersection theory?

### 2.2 What "done" looks like

A 20-30 page survey covering 2017-2025 Connes-Consani papers and adjacent literature, with an updated R3.6.3 verdict per sense. Independently publishable as an expository / survey article.

### 2.3 Sub-tasks

- 2.3.1 Compile a complete bibliography of Connes, Consani, and Connes-Consani papers from 2017 onward.
- 2.3.2 Read each paper looking for intersection-theoretic / Chow-style / Hodge-style content.
- 2.3.3 Update the R3.6.3 verdicts based on findings.
- 2.3.4 Identify which specific papers (if any) provide partial machinery for Direction 8.

### 2.4 Effort

1-2 postdoc-years. Calendar time: 6-12 months.

### 2.5 Falsifiability

If the deep-dive reveals that the Connes-Consani program has explicitly addressed intersection theory in 2017-2025 (e.g., a recent Connes-Consani paper proves a Hodge index theorem on $\mathcal{A}$), the R3.6 verdict is incorrect and Direction 5 might directly contribute to Direction 8. If the deep-dive confirms the R3.6 picture (no such development), the verdict stands.

## 3. R3.6.3.b — Hyperring tensor product theory

### 3.1 Problem statement

Develop the tensor product of hyperring sheaves on the arithmetic site (or on Borger's W(Z)) rigorously, and check whether it has the formal properties needed for a Chow-style intersection product:

- Bilinearity in the appropriate sense.
- Compatibility with the multivalued addition structure of hyperrings.
- A "moving lemma" for hyperring cycle classes.
- Flat / proper pullback functors with the right compatibility.

### 3.2 What "done" looks like

A 30-50 page paper "Tensor products of hyperring sheaves and arithmetic intersection theory" containing:

1. Precise definition of the tensor product of hyperring sheaves on a topos.
2. Verification of bilinearity, associativity, and unit properties.
3. Definition of a hyperring Chow group.
4. Definition of an intersection product with verification of bilinearity and projection formula.
5. Computation in low-dimensional cases.

Publishable in Compositio or Adv. Math.

### 3.3 Sub-tasks

- 3.3.1 Extend Marshall 2006 (hyperring tensor products) to hyperring sheaves on a site.
- 3.3.2 Define the analog of the "moving lemma" for hyperring cycles.
- 3.3.3 Construct flat and proper pullbacks for hyperring-sheaf-valued morphisms.
- 3.3.4 Define the intersection product as a tensor-product-induced map on Chow groups.
- 3.3.5 Verify basic properties.

### 3.4 Effort

3-5 postdoc-years. Calendar time: 1-2 years for a 2-3 person group.

### 3.5 Falsifiability

If the tensor product fails to be bilinear OR if no moving lemma analog exists, the hyperring approach to intersection theory is broken. Pivot to Direction 8's other angles (4.A tropical bridge, 4.C direct algebraic-geometric construction).

## 4. R3.6.3.c — Tropical-arithmetic Hodge bridge

### 4.1 Problem statement

The Adiprasito-Huh-Katz tropical Hodge index theorem (2018) gives Hodge-Riemann relations on tropical varieties. Question: can the characteristic-one limit of Connes-Consani's framework be wired to import these tropical Hodge-index statements as a Hodge index theorem for the geometric route (Direction 8)?

The obstacle (per R3.6.3): tropical varieties encode degenerations of EXISTING algebraic varieties (Mikhalkin 2005), not constructed-from-scratch arithmetic surfaces. The bridge would need to invert this: take an arithmetic surface (Direction 1 or 2 candidate) as the "limit object" of a tropical degeneration argument.

### 4.2 What "done" looks like

A 60-100 page paper "Tropical Hodge index in characteristic-one arithmetic" containing:

1. A framework for treating the Lambda-blueprint surface (or Borger's W(Z)-surface) as the limit of a tropical degeneration.
2. Application of Adiprasito-Huh-Katz to the limit object.
3. Recovery of a Hodge index theorem on the original arithmetic surface.

This would be a major contribution to BOTH tropical geometry and arithmetic geometry. Publishable in Annals.

### 4.3 Sub-tasks

- 4.3.1 Identify the "tropicalization" of the arithmetic surface (the analog of tropical limit for non-classical-algebraic objects).
- 4.3.2 Verify the tropicalization is itself a tropical variety in the Adiprasito-Huh-Katz sense.
- 4.3.3 Apply AHK to get a Hodge-Riemann relation on the tropicalization.
- 4.3.4 Invert the tropicalization to get a statement on the original arithmetic surface.
- 4.3.5 Verify the inverted statement is the Hodge index for the geometric route.

### 4.4 Effort

5-10 postdoc-years. Calendar time: 2-4 years for a 3-4 person group with expertise in tropical geometry, characteristic-one calculus, and arithmetic geometry.

### 4.5 Falsifiability

- 4.3.1 fails: no natural tropicalization. The bridge is broken.
- 4.3.2 fails: the tropicalization is not a tropical variety in the AHK sense (e.g., not pure-dimensional, or not balanced). AHK doesn't apply.
- 4.3.4-4.3.5 fail: the inverted statement doesn't recover Hodge index on the arithmetic surface. The bridge is unidirectional only.

If 4.3.1 or 4.3.2 fails, the program reverts to direct algebraic-geometric Hodge index attempts (Direction 8 angle 4.C).

## 5. How the three sub-directions relate

R3.6.3.a is a literature task: relatively low-cost, identifies whether the Connes-Consani machinery already provides what we need. Should be done FIRST.

R3.6.3.b is a structural development: builds the hyperring intersection theory machinery. Independent of R3.6.3.c. Provides one angle for Direction 8.

R3.6.3.c is the tropical Hodge bridge: depends on having a tropicalization of the arithmetic surface (which depends on Direction 1 or 2 surface candidate being settled). Provides another angle for Direction 8.

Sequence: a → (b and c in parallel after Direction 1 / 2).

## 6. Falsifiability for the combined direction

- a finds 2017-2025 has already done R3.6.3.b/c: direction is largely subsumed.
- a finds 2017-2025 has not addressed: R3.6.3.b and .c remain open.
- b fails: hyperring intersection theory is not a viable Direction 8 input.
- c fails: tropical Hodge bridge is not a viable Direction 8 input.

If both b and c fail, Direction 5's contribution to Direction 8 is limited to inspiration only. Direction 8 must proceed via the direct algebraic-geometric angle.

## 7. Estimated effort

Total for all three: 8-15 postdoc-years. Calendar time: 3-5 years.

R3.6.3.a is the cheapest and fastest (12 months); R3.6.3.b is medium (1-2 years); R3.6.3.c is the most expensive (2-4 years).

## 8. Connections

- **Direction 8** (Hodge index on constructed surface): Direction 5 provides three potential infrastructure inputs (literature scaffolding, hyperring intersection theory, tropical bridge).
- **Direction 1** (Lambda-blueprints): Direction 5.c needs the surface to tropicalize.
- **Direction 2** (Borger+Connes): alternative surface candidate for Direction 5.c.
- **R3.6.3** ([`2A_R3_6_3_cc_infrastructure.md`](../../../experiments/arithmetic_geometric/2A_R3_6_3_cc_infrastructure.md)): the R3.6.3 analysis is the input to Direction 5.

## 9. References

- Connes, A.; Consani, C. (2010-2025). Various papers on the arithmetic site, hyperrings, and characteristic-one geometry.
- Adiprasito, K.; Huh, J.; Katz, E. (2018). *Hodge theory for combinatorial geometries*. Ann. Math. 188(2), 381-452.
- Babaee, F.; Huh, J. (2017). *A tropical approach to a generalized Hodge conjecture for positive currents*. Duke Math. J. 166(14).
- Mikhalkin, G. (2005). *Enumerative tropical algebraic geometry in R^2*. J. AMS 18.
- Marshall, M. (2006). *Real reduced multirings and multifields*. J. Pure Appl. Algebra 205.
- Allermann, L.; Rau, J. (2010). *First steps in tropical intersection theory*. Math. Z. 264.

## 10. Status

This direction is **research-grade, beyond project scope**. The R3.6.3 analysis identifies the three follow-ups; this document provides the operational specification for each.

R3.6.3.a is the cheapest and should be done first (1-year project). R3.6.3.b and .c are more substantial.

Note: each of the three sub-directions is independently publishable. Even partial progress (e.g., R3.6.3.a confirming the R3.6 verdict, or R3.6.3.b producing a working hyperring tensor product without Chow-style intersection theory) is a valuable contribution.
