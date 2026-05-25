# 2D: A micro-target in Deninger's program

> **Plan reference**: PROOF_ARCHITECTURES_PLAN row "2D | Identify the smallest open conjecture in Deninger's program that would, if proved, be a meaningful step | A target".
>
> **Companion to** [`2A_deninger_dossier.md`](2A_deninger_dossier.md) (the full Deninger scorecard), [`2A_R4_borger_connes_hybrid.md`](2A_R4_borger_connes_hybrid.md) (the most promising Deninger realization), [`2A_R5_prismatic_cohomology.md`](2A_R5_prismatic_cohomology.md) (candidate cohomology theory), [`2A_path_forward.md`](2A_path_forward.md) (the multi-decade strategic plan).
>
> **Headline**: the recommended micro-target is the **"prismatic foliation hypothesis"**: define a foliation structure on the prismatic site of $\mathrm{Spec}(W(\mathbb{Z}))$ compatible with Borger's $\Lambda$-action / Connes' $\mathbb{R}^*_+$-action, and verify that the leafwise prismatic cohomology has the formal properties required by Deninger's program (Lefschetz trace formula, Poincaré duality, Künneth). This is the single most decisive intermediate step toward Architecture 2's geometric route to RH, sitting at the intersection of R4 (Borger + Connes), R5 (prismatic cohomology), and Deninger's program. Its proof would be a 5-15 page paper or thesis chapter; its non-existence after 30 years of Deninger work + 7 years of prismatic cohomology suggests it's hard. The target is concrete, smaller than RH, and substantively new.

## 1. What "smallest open conjecture" means here

Deninger's program proposes constructing a foliated dynamical system $(X, \mathcal{F}, \Phi_t)$ whose leafwise cohomology, under a regularized determinant, recovers $\zeta(s)$. The full program has five conjectural pieces (per [`2A_deninger_dossier.md`](2A_deninger_dossier.md) §3): $X$, $\Phi_t$, $H^i_\mathcal{F}(X)$, the Lefschetz trace formula, the Hodge index theorem on $X \times X$.

**A micro-target should:**
- Be smaller than RH (so achieving it does not require closing the program).
- Be meaningful: success advances the program substantively, not vacuously.
- Be concrete: stated precisely enough that "proof" has a well-defined meaning.
- Be tractable: in principle approachable with current machinery, not requiring fundamentally new mathematics.
- Connect cleanly to existing 2A R-series work.

The micro-target is not unique; multiple choices satisfy the criteria. This document recommends one with the strongest connection to the R4 + R5 path forward.

## 2. Candidate micro-targets (surveyed)

Three families of candidate micro-targets, ordered by tractability:

### (M1) Construct an archimedean fiber of $X$ explicitly

**Statement**: construct a specific compact foliated manifold $X_\infty$ whose foliated trace formula recovers the archimedean local factor $\Gamma_\mathbb{R}(s) = \pi^{-s/2} \Gamma(s/2)$ of the completed zeta function $\xi(s)$.

**Pros**: concrete; the archimedean local factor is well-studied; foliated machinery for compact manifolds is in place (Heitsch-Lazarov).

**Cons**: gamma factors are not standard outputs of foliated trace formulas, which typically produce Euler-product-style factors $(1 - p^{-s})^{-1}$. The archimedean piece's "geometry" in Deninger's program is the least clear part of the dictionary. Substantial setup work would precede any meaningful test.

**Verdict**: tractable but the connection to Deninger's actual program is weak.

### (M2) Local Lefschetz at one prime

**Statement**: construct a local foliated space $X_p$ at one prime $p$ whose foliated trace formula gives the Euler factor $(1 - p^{-s})^{-1}$, and whose leafwise cohomology realizes Frobenius eigenvalues consistent with the local structure of $\zeta$ at $p$.

**Pros**: closely matches the Deninger dictionary (periodic orbits = primes; period = $\log p$). Local versions of foliated trace formulas exist (Patterson-Sullivan, Selberg).

**Cons**: this is essentially the **Bost-Connes QSM system** restricted to one prime, which already exists. So (M2) is partially "complete" via Bost-Connes 1995. The non-trivial content is making the foliated geometry explicit (Bost-Connes is NCG, not literal foliations), but that's a translation exercise more than a structural advance.

**Verdict**: too small. Mostly recovers known machinery.

### (M3) Prismatic foliation hypothesis (recommended)

**Statement**: Define a foliation structure on the prismatic site of $\mathrm{Spec}(W(\mathbb{Z}))$ (Borger's Witt scheme; per [`2A_R5_prismatic_cohomology.md`](2A_R5_prismatic_cohomology.md), prismatic cohomology naturally applies here) compatible with Borger's $\Lambda$-action $\{\psi_p\}_p$ via the multiplicative-completion bridge $\Phi_t = \prod_p U_{\log p}^{t/\log p}$ proposed in [`2A_R4_borger_connes_hybrid.md`](2A_R4_borger_connes_hybrid.md). Verify that the leafwise prismatic cohomology $H^*_\mathcal{F, \mathrm{pr}}$ has:
1. **Finiteness**: $H^i_\mathcal{F, \mathrm{pr}}$ is finite-dimensional (or trace-class for $\Phi_t$) in a precise sense.
2. **Lefschetz trace formula**: there is a well-defined regularized determinant $\det_\zeta(s \cdot \mathrm{id} - \Phi_t | H^*)$ recovering a non-trivial part of $\zeta(s)$ (target: at least the Euler product piece, ideally also the gamma factor).
3. **Poincaré duality**: a non-degenerate pairing $H^i_\mathcal{F, \mathrm{pr}} \otimes H^{n-i}_\mathcal{F, \mathrm{pr}} \to k$ for the appropriate cohomological dimension $n$ and base $k$.
4. **Künneth**: $H^*_\mathcal{F, \mathrm{pr}}(X \times X) = H^*_\mathcal{F, \mathrm{pr}}(X) \otimes H^*_\mathcal{F, \mathrm{pr}}(X)$ (for the leafwise prismatic site of the double).

What this does NOT include: the Hodge index theorem on $X \times X$. That remains the central open problem of Deninger's program, beyond the micro-target.

**Pros**:
- **Concrete**: every term in the statement is independently defined. Borger's $\mathrm{Spec}(W(\mathbb{Z}))$ exists. Prismatic cohomology exists. The bridge $\Phi_t = \prod_p U_{\log p}^{t/\log p}$ is proposed (R4) and computable on test cases.
- **Smaller than RH**: closes (iv)-(vii) and partially (viii)-(ix) of the 17-constraint scorecard but leaves (xi)-(xiii) (Hodge index, the K1-escape route) untouched.
- **Meaningful**: a positive result would be the first explicit piece of Deninger's $X$ built, and would simultaneously close several R-series questions (R4.1-R4.5, R5.1-R5.5 partially).
- **Bridges three frameworks**: Deninger (foliations + flow), Borger (Witt schemes + $\Lambda$-action), prismatic cohomology (BMS 2018+). The bridge between these is the natural research-grade target identified in [`2A_path_forward.md`](2A_path_forward.md).
- **Falsifiable**: if the verification of (1)-(4) fails, the failure pinpoints exactly which slot of Deninger's framework is incompatible with prismatic cohomology, narrowing the search.

**Cons**:
- **Hard**: 30 years of Deninger + 7 years of prismatic cohomology have not produced this bridge. There may be a structural obstruction we're not seeing.
- **Requires deep prerequisites**: working knowledge of BMS prismatic cohomology, foliated cohomology, $\Lambda$-ring structure, and Connes' adèle class space. PhD-thesis level.
- **The "right" foliation structure is not unique**: $\mathrm{Spec}(W(\mathbb{Z}))$ has multiple plausible foliations (by $\psi_p$ orbits for fixed $p$; by the multiplicative-completion $\Phi_t$ orbits; by the topological structure of $W(\mathbb{Z}) \cong 1 + t\mathbb{Z}[[t]]$). Identifying the correct one is part of the problem.

**Verdict**: the right size and shape for a 2D micro-target. Concrete, smaller than RH, meaningful, with the strongest connection to the path forward.

## 3. The recommendation: prismatic foliation hypothesis (M3)

**Full statement of the micro-target**:

> Let $X = \mathrm{Spec}(W(\mathbb{Z}))$ be Borger's Witt scheme. The $\Lambda$-structure on $\mathbb{Z}$ (Adams operations $\psi_p$, one per prime $p$, all equal to $\mathrm{id}$ on $\mathbb{Z}$ by Fermat's little theorem; non-trivial on $W(\mathbb{Z})$) gives a $\delta$-structure at every prime, so prismatic cohomology of $X$ (in the sense of Bhatt-Morrow-Scholze) is well-defined.
>
> Define the flow $\Phi_t$ on $X$ by the multiplicative completion $\Phi_t = \prod_p U_{\log p}^{t/\log p}$ where $U_{\log p}$ is the time-$\log p$ part of the $\mathbb{R}^*_+$-action lifting $\psi_p$ (per [`2A_R4_borger_connes_hybrid.md`](2A_R4_borger_connes_hybrid.md)).
>
> **Conjecture (Prismatic Foliation):** there is a foliation $\mathcal{F}$ on the prismatic site of $X$ whose leaves are orbits of $\Phi_t$, such that the leafwise prismatic cohomology $H^*_\mathcal{F, \mathrm{pr}}(X)$ has finite-dimensionality, Poincaré duality, Künneth, and a Lefschetz trace formula for $\Phi_t$ recovering at least the Euler product factor $\prod_p (1 - p^{-s})^{-1}$ of $\zeta(s)$.

A proof of the prismatic foliation conjecture would close:
- Constraint (iv) (finite cohomology with required properties) for Borger's framework.
- Constraint (v) (Poincaré duality).
- Constraint (vii) (Künneth).
- Constraint (viii) (Frobenius substitute) explicitly via $\Phi_t$.
- Constraint (ix) (Lefschetz trace formula) for at least the Euler-product piece.

What remains after a positive resolution:
- Constraint (xi)-(xiii) (Hodge index positivity on $X \times X$). This is the central open problem and would not be addressed by M3.
- Constraint (vi) (cycle class map and intersection theory) only partial — the prismatic side would give one half of the pairing, but the intersection-theoretic structure on $X \times X$ would still need separate development.

## 4. Why this size is right

**Smaller than RH**:
- M3 does not address positivity. The Hodge index theorem on $X \times X$ remains open.
- M3 does not by itself imply RH. Without Hodge index, no positivity, so no force on Frobenius eigenvalues.

**Meaningful, not vacuous**:
- Closes 5 of the 17 constraints in one go.
- Provides the first explicit construction of "Deninger's $X$" via the Borger + Connes + prismatic hybrid.
- Tests whether prismatic cohomology can play the role of leafwise cohomology — a structural question about the compatibility of BMS machinery with Deninger's program.
- A negative resolution (no such foliation exists) would be equally informative: it would rule out the most natural Deninger-prismatic bridge and force a different cohomology choice.

**Concrete**:
- Every term in the statement has a precise mathematical definition.
- Verification of properties (1)-(4) is a finite checklist of standard cohomological tests.
- The trace formula recovery is a calculation, not a conjecture: $\det_\zeta(s \cdot \mathrm{id} - \Phi_t | H^*_\mathcal{F, \mathrm{pr}})$ either does or doesn't reproduce $\prod_p (1 - p^{-s})^{-1}$.

**Tractable**:
- All prerequisite frameworks (Borger's $\Lambda$-rings, BMS prismatic cohomology, foliated cohomology, Connes' adèle class space) exist as published mathematics.
- The bridge $\Phi_t = \prod_p U_{\log p}^{t/\log p}$ is concrete and computable.
- A graduate student with the right background (algebraic geometry + NCG + $p$-adic Hodge theory) could attack this as a thesis project.

## 5. Status and prerequisites

**Status**: open. No work directly addressing the prismatic foliation conjecture exists. The closest is:
- Bhatt-Morrow-Scholze 2018-2022: defines prismatic cohomology, applies it to Witt schemes.
- Borger 2009+: develops $\Lambda$-algebraic geometry; identifies $\mathrm{Spec}(W(\mathbb{Z}))$ as the natural $\Lambda$-base.
- Connes 1999, Connes-Marcolli 2008: the adèle class space and its $\mathbb{R}^*_+$-action.
- Deninger 1991+: foliated dynamical system framework.

What's missing is the explicit bridge tying these together, articulated as the foliated prismatic site with $\Phi_t$ action.

**Prerequisites for an attacker**:
- $\Lambda$-rings and the big Witt vector functor (Borger 2009, Joyal, Cartier).
- Prismatic cohomology at a working level (BMS 2018, Bhatt-Scholze 2022, Bhatt's lecture notes).
- Connes' adèle class space and the Bost-Connes QSM (Bost-Connes 1995, Connes-Marcolli 2008).
- Foliated cohomology (Connes' book *Noncommutative Geometry*, Heitsch-Lazarov, Moore-Schochet).
- Comfort with derived / $\infty$-categorical infrastructure (the prismatic site lives there).

**Estimated effort**: thesis-level, 2-3 years for a strong graduate student with the right advisor. The "negative results" (showing one of (1)-(4) fails) are likely easier and might constitute a useful paper on their own.

## 6. Connections to existing 2A work

- **R4** ([`2A_R4_borger_connes_hybrid.md`](2A_R4_borger_connes_hybrid.md)): the multiplicative-completion bridge $\Phi_t = \prod_p U_{\log p}^{t/\log p}$ is proposed in R4. M3 makes this bridge the flow in Deninger's framework. M3's questions (1)-(4) overlap substantially with R4's questions (R4.1-R4.5). A positive resolution of M3 would close most of R4.
- **R5** ([`2A_R5_prismatic_cohomology.md`](2A_R5_prismatic_cohomology.md)): R5 identifies prismatic cohomology as the candidate cohomology theory for Borger's $\mathrm{Spec}(W(\mathbb{Z}))$ and predicts it closes constraints (iv)-(vii). M3 adds the foliation structure on top, asking whether the prismatic cohomology is compatible with Deninger's leafwise picture. R5's open questions (R5.1-R5.5) are subsumed by M3.
- **R2.5 ($\Lambda$-blueprints)**: alternative hybrid framework. If $\Lambda$-blueprints turn out to be a better setting than pure Borger, M3 generalizes: foliated prismatic cohomology of the $\Lambda$-blueprint analog of $\mathrm{Spec}(W(\mathbb{Z}))$.
- **R3.5** ([`2A_R3_5_K1_universality.md`](2A_R3_5_K1_universality.md)): the no-shortcut theorem rules out trace-formula NCG approaches to K1. M3 still falls under R3.5 (it relies on a trace formula), so even if M3 is fully proved, the Hodge index positivity (xi-xiii) remains the K1-escape. M3 is infrastructure progress, not K1 progress. This is consistent with [`2A_path_forward.md`](2A_path_forward.md)'s framing.
- **Cross-cut to 2E**: [`2E_adams_spectrum_probe.md`](2E_adams_spectrum_probe.md) showed that bare $\psi_p$ on concrete $\Lambda$-rings has no zeta-zero spectrum. M3 asks whether the cohomology (specifically prismatic) does the lifting that the bare structure cannot. A positive resolution of M3 would directly extend 2E's negative result.

## 7. Why this is NOT the same as R4 or R5

R4 asks: can Borger and Connes be hybridized into a single Hilbert-space framework with explicit flow? R5 asks: does prismatic cohomology give the cohomology theory Borger needs? Both are STRUCTURE questions about specific frameworks.

M3 (2D micro-target) asks: **does the prismatic cohomology of Borger's Witt scheme, equipped with the R4 flow, give a leafwise cohomology in Deninger's sense?** This is the bridge question between the three frameworks. It is the natural intersection of R4 and R5 plus the Deninger compatibility check.

The key sharpening over R4 / R5: M3 makes the FOLIATION explicit, which is the Deninger-specific structure absent from R4 and R5 individually. R4's flow lives on $W(\mathbb{Z})$; R5's cohomology lives on the prismatic site; M3 says the orbits of R4's flow define a foliation on R5's prismatic site, and asks whether the leafwise cohomology has Deninger's required properties.

## 8. Verdict

The recommended 2D micro-target is **M3: the prismatic foliation hypothesis**. It is the smallest open conjecture in Deninger's program with the following combination of properties:
- Concretely formulable in published mathematics.
- Smaller than RH (does not address Hodge index / K1).
- Substantively new (no existing literature addresses the prismatic-Deninger bridge directly).
- Tractable as a thesis-level project, given the right background.
- Connects cleanly to the R-series strategic plan in [`2A_path_forward.md`](2A_path_forward.md).

Alternative targets M1 (archimedean fiber) and M2 (local Lefschetz at one prime) are too small or too disconnected from the active Deninger program. The prismatic foliation hypothesis is the right size.

A negative resolution would be equally informative — it would pinpoint which slot of Deninger's framework is incompatible with the prismatic + Connes + Borger hybrid, narrowing the search for alternative cohomology theories.

**Status: open. Recommended next step after [`2A_path_forward.md`](2A_path_forward.md) is sketched: develop the precise statement of M3 (1)-(4), and attempt either (a) a positive resolution via explicit construction or (b) a no-go theorem identifying which slot fails.**

## 9. Output format

This document IS the 2D deliverable per the plan: "Identify the smallest open conjecture in Deninger's program that would, if proved, be a meaningful step | A target". The target is M3, the prismatic foliation hypothesis, with full statement in §3.

No code or numerical experiment is associated with 2D — it is literature-and-analysis. The next step beyond 2D would be either developing M3 rigorously (research-grade work) or identifying a smaller sub-target within M3 if M3 itself is too large.
