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

## Operational implication: a research program, not a catalog

Stop building realizations. Connes, Deninger, Hesselholt, Morin, and the project's own 2R/2Q dictionary already supply the determinant/trace side over $\mathbb{F}_q$ and partially over $\mathbb{Z}$. The signature is the work, and it is a *program with attackable milestones*, not a 1% lottery ticket. The sharpened target is **arithmetic Rosati positivity** (the standard-conjecture form; see [`research_directions/08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md)):

> RH = positivity (no negative spectrum) of the Rosati trace form $B(x,y)=\mathrm{Tr}(x\,y^\dagger)$ on the arithmetic Frobenius algebra $\mathcal{A}$ of $\mathrm{Spec}(\mathbb{Z})$.

This is the actual engine of Weil 1948, needs no ambient surface to state, is the arithmetic analogue of Grothendieck's **Hodge standard conjecture**, and is non-circular (the positivity comes from a polarization, not from the zeros). The four equivalent function-field faces are all in the record: Rosati positivity (2T), primitive intersection negative-definiteness (2G), $|\alpha_i|=\sqrt q$, and the TP/flow zeros on $\mathrm{Re}(s)=1/2$ (2S).

The milestones (08A §4), with status as of 2026-05-30:
- **M1** (done, 2T): verify the function-field Rosati formulation. The full $2g$-dim Rosati trace form has no negative eigenvalues $\Leftrightarrow |\alpha_i|=\sqrt q$, across genus 1-2.
- **M2 / M2.5 / M2.6** (done, 2U/2V/2W; LEARNINGS #32-34): construct the truncated non-circular arithmetic Weil form $M = A_{\mathrm{arch}} + P_{\mathrm{fin}} + B_{\mathrm{pole}}$ from the Gamma factor + von Mangoldt primes (no zeros), with the archimedean block in its validated Bombieri physical-space form ($C_\mu = \log\pi - \psi((1+\mu)/2)$). RESULT: $\min\mathrm{eig}(M) = +0.035 > 0$ for $\zeta$ (non-circular positivity certificate, necessary-not-sufficient). BUT the four-way RH-vs-Euler discrimination FAILS: D-H reads spuriously positive ($+0.094$) because its off-line obstruction ($\gamma\approx85.7$, $\sim$2.6% of the raw spectrum) sits below the reconstruction-residual floor: the stealth window (#18/#19/#27) on the non-circular Rosati side. The infrastructure (correct non-circular Weil form for any Gamma factor) is complete and validated.
- **M3** (open, and it must be ANALYTIC): prove the archimedean-dominates-prime domination engaging the EXACT off-line structure (the Euler product / Gamma-factor cancellation that distinguishes $\zeta$ from D-H below the marginal-positivity floor). A finer numerical truncation cannot do this (the signal is below the floor; Schur amplification is answer-side/circular). The candidate polarization is the Arakelov/archimedean Green's-function positivity (2I-2L).
- **M4** control the $P\to\infty$ limit (= the arithmetic Hodge standard conjecture); **M5** derive RH and verify K1/K2/K3.

The numerical phase (M1-M2.6) is complete: the non-circular Rosati form is built and validated, and it confirms exactly what the marginal-positivity thesis predicts -- a soft/numerical certificate is positive for $\zeta$ but cannot separate $\zeta$ from D-H. The frontier is the analytic domination (M3), where #20/3M always located the hard step.

## Pointers

- Directions: [`research_directions/08_hodge_index_surface.md`](research_directions/08_hodge_index_surface.md) (the signature, central), [`research_directions/10A_thh_vonmangoldt_checkpoint.md`](research_directions/10A_thh_vonmangoldt_checkpoint.md), [`research_directions/10B_thh_weight_and_mobius.md`](research_directions/10B_thh_weight_and_mobius.md).
- Findings: LEARNINGS #18-21 (signature vs trace, marginal positivity), #25-26 (bidegree, dynamical zeta), #27 (Dir 9/13 detectors), #28-29 (THH route + Hesselholt reorientation).
- Experiments: 2G (function-field Hodge index, exact signature), e2s (TP odd/even = Hodge-index split), e_thh_vonmangoldt, e_necklace_mobius, survey_tc_zeta_literature.
