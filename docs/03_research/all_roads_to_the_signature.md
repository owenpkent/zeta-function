# All roads lead to the signature: cross-direction synthesis (2026-05-30)

> A consolidation written after a session that proposed five new directions (9-13) and pushed the THH route (Direction 10) far enough to hit, via Hesselholt's theorem and a literature survey, the same wall every other architecture hits. The finding is structural and worth stating plainly.

## The one-sentence finding

Every architecture and every new direction produces the **realization** of $\zeta$ (a determinant, a trace, a detector, a Dirichlet-series identity), and that half is comparatively easy and exists in several frameworks; but RH itself is the **signature / positivity**, which is separate, irreducible, and the same problem in every framework. The realization is not the proof. The signature is.

## The ledger

| Framework | What it realizes (the easy half) | Where RH-positivity sits (the hard half) | Status of the hard half |
|---|---|---|---|
| **Arch 1** (Connes spectral / NCG) | adelic trace formula = Weil explicit formula | positivity of the Weil distribution (trace-side) | R3.5-circular (K1): a trace identity, not a signature |
| **Arch 2 / Dir 8** (Weil / Deninger) | intersection form on a surface; Frobenius correspondence | **Hodge-index signature** $(1,k)$ on the primitive part | the target; function-field case exact (2G), Spec(Z) open |
| **Arch 3** (Weil / Li positivity) | the Weil quadratic form / Li coefficients | positivity of the form $\Leftrightarrow$ archimedean dominates the prime obstruction | marginal (#18-20): no soft input-side bookkeeping manufactures it |
| **Arch 4** (zero-free regions) | non-negative trig-polynomial inequalities | (not a signature route) | capped at V-K $2/3$ (#14-15); constraint-mapping, not RH |
| **Dir 9** (arithmetic matroid) | Li log-concavity from a matroid characteristic polynomial | the AHK Hodge-Riemann signature on the Chow ring | log-concavity is a NON-Euler detector, not RH (#27); the HR signature is the would-be source |
| **Dir 10** (THH / Hesselholt) | $\zeta = \det_\infty(s-\Theta\mid \mathrm{TP}_{\mathrm{od}})/\det_\infty(s-\Theta\mid \mathrm{TP}_{\mathrm{ev}})$ | cup-product signature on $\mathrm{TP}_{\mathrm{odd}}$ (= primitive $H^1$) | **realization PROVEN over $\mathbb{F}_q$** (#29); signature = the Dir 8 Hodge index; Spec(Z) open |
| **Dir 13** (tau-function) | $\xi$ as a KP tau-function | Riemann bilinear relations (= the Hodge index, infinite genus) | Jensen/Turán stealth window (#27); the signature is the bilinear positivity |

Read the table top to bottom: the middle column is populated, in several cases by theorems. The right column is, in every row, the *same* object wearing different clothes, the negative-definiteness of an intersection / cup / quadratic form on a primitive subspace, and it is unsolved in every row over $\mathbb{Z}$.

## Why this is the marginal-positivity thesis, restated

The project's central structural finding, "RH is just barely true, no buffer for soft proofs", is exactly the statement that the signature is the whole content. If the positivity had any slack, a soft realization (a trace, a statistic, a determinant) would close it. It has zero slack (#18: D-H fails Weil positivity by 78.7% per off-line direction; the wall is tight), so the realization frameworks, which see only the trace/spectral side, cannot close it. The session added three independent confirmations from new bases (log-concavity #27, Jensen/Turán #27, and now the THH/Hesselholt route #29), each landing on the same signature.

## The cleanest evidence from this session: Hesselholt closes the loop

Hesselholt's theorem (#29) is decisive precisely because it is the strongest possible realization result: it *proves*, over $\mathbb{F}_q$, that $\zeta$ is the regularized determinant of the Frobenius flow on the $S^1$-Tate periodic $\mathrm{TP}$. And yet RH for the variety is *not* a corollary, it is $|\alpha_i| = q^{1/2}$, the Weil/Hodge-index positivity, a separate input. So even the best realization theorem in the literature confirms the dichotomy: the determinant is the easy half; the signature is RH. Over $\mathbb{Z}$, Hesselholt's framework breaks for the #25 reason (TP not periodic, no single Frobenius), so it does not even deliver the easy half there, but the lesson stands.

## The D-H discipline is the reason the signature is the right locus

The wrong-approach detector cuts the same way every time: the realization frameworks are often *buildable* for Davenport-Heilbronn (D-H has a functional equation, hence an explicit formula, hence a trace), and that is exactly why a trace-side proof is suspect (K1/R3.5). The signature is *unbuildable* for D-H: no Euler product $\Rightarrow$ no Frobenius correspondence $\Rightarrow$ no surface $\Rightarrow$ no intersection form to take the signature of (2G's K2 reading; #25/#26's bidegree form). The one object that cannot be built for the known counterexample is the one object whose positivity is RH. That is not a coincidence; it is the discipline telling us where the proof must live.

## Operational implication

Stop building realizations. Connes, Deninger, Hesselholt, Morin, and the project's own 2R/2Q dictionary already supply the determinant/trace side over $\mathbb{F}_q$ and partially over $\mathbb{Z}$. Concentrate effort on the **signature**:

- the Hodge-index theorem on the constructed surface (Direction 8), the project's stated central problem;
- equivalently, form 10A.iii: a definite cup-product signature on $\mathrm{TP}_{\mathrm{odd}}$ over $\mathbb{Z}$;
- with the new TP/flow lens as input: the odd/even split of $\mathrm{TP}$ is exactly the primitive/hyperbolic split of the Weil Hodge index (verified in the function-field case, see [`experiments/arithmetic_geometric/e2s_tp_hodge_split.py`](../../experiments/arithmetic_geometric/e2s_tp_hodge_split.py)).

Whether any framework supplies a *new tool* for the signature (rather than another realization) is the only question that distinguishes progress from reformulation.

## Pointers

- Directions: [`research_directions/08_hodge_index_surface.md`](research_directions/08_hodge_index_surface.md) (the signature, central), [`research_directions/10A_thh_vonmangoldt_checkpoint.md`](research_directions/10A_thh_vonmangoldt_checkpoint.md), [`research_directions/10B_thh_weight_and_mobius.md`](research_directions/10B_thh_weight_and_mobius.md).
- Findings: LEARNINGS #18-21 (signature vs trace, marginal positivity), #25-26 (bidegree, dynamical zeta), #27 (Dir 9/13 detectors), #28-29 (THH route + Hesselholt reorientation).
- Experiments: 2G (function-field Hodge index, exact signature), e2s (TP odd/even = Hodge-index split), e_thh_vonmangoldt, e_necklace_mobius, survey_tc_zeta_literature.
