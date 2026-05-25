# The $\mathbb{F}_1$ and Arakelov Programs: A Survey as of 2025

> **Companion document to** [`experiments/PROOF_ARCHITECTURES_PLAN.md`](../../experiments/PROOF_ARCHITECTURES_PLAN.md) (Arch 2C) and the per-candidate dossiers in [`experiments/arithmetic_geometric/`](../../experiments/arithmetic_geometric/) (Deitmar, Lorscheid, Borger, Connes, Connes-Consani, Deninger).
>
> **Scope:** state of the $\mathbb{F}_1$ ("field with one element") program and Arakelov-cohomology program for Architecture 2 (arithmetic-geometric route to RH), with emphasis on developments since 2020. The two programs address the **same** structural gap (lifting Weil's proof template from curves over $\mathbb{F}_q$ to $\mathrm{Spec}(\mathbb{Z})$) but from **different directions**: $\mathbb{F}_1$ tries to manufacture a "base below $\mathbb{Z}$" so that $\mathrm{Spec}(\mathbb{Z})$ becomes a curve over it; Arakelov compactifies $\mathrm{Spec}(\mathbb{Z})$ by adding archimedean data.
>
> **Verdict:** both programs have produced substantial infrastructure but neither has closed the Hodge-index positivity gap that the per-candidate scorecards ([`2A_candidate_evaluation.md`](../../experiments/arithmetic_geometric/2A_candidate_evaluation.md)) identify as the central open construction problem. Recent (2018-2025) machinery — prismatic cohomology, condensed/light condensed mathematics, perfectoid spaces — provides genuinely new infrastructure but has not yet been wired into either program in a way that produces RH-relevant positivity. The path forward is multi-decade research-grade work along the hybrid lines identified in [`2A_path_forward.md`](../../experiments/arithmetic_geometric/2A_path_forward.md).

---

## 1. The problem these programs address

[Weil's 1948 proof](../../experiments/arithmetic_geometric/2A_weil_proof_diff.md) of RH for curves $C/\mathbb{F}_q$ relies on three structural ingredients:

1. **Lefschetz fixed-point theorem**: Frobenius $F$ acts on $\ell$-adic cohomology $H^*(C, \mathbb{Q}_\ell)$; the trace of $F^n$ counts $\mathbb{F}_{q^n}$-points; this gives the zeros of $Z(C, T)$ as eigenvalues of $F$ on $H^1$.
2. **Poincaré duality**: a non-degenerate pairing $H^1 \otimes H^1 \to H^2 = \mathbb{Q}_\ell(-1)$, equivalent at the L-function level to the functional equation $Z(C, T) = (qT)^{-g} Z(C, 1/(qT))$.
3. **Hodge index theorem**: on the surface $C \times C$, the intersection form has signature $(1, 2g)$ on the relevant subspace. This is the positivity argument forcing $|\alpha_i|^2 = q$ for Frobenius eigenvalues.

For $\zeta(s)$ on $\mathrm{Spec}(\mathbb{Z})$ all three are missing in their standard forms:

| Ingredient | Function field | $\mathrm{Spec}(\mathbb{Z})$ |
|---|---|---|
| Frobenius | $F: x \mapsto x^q$, concrete endomorphism | none geometrically; needs a substitute |
| Compact base curve | $C/\mathbb{F}_q$ smooth projective | $\mathrm{Spec}(\mathbb{Z})$ not proper |
| 2D ambient space | $C \times_{\mathbb{F}_q} C$ surface | $\mathrm{Spec}(\mathbb{Z}) \times_? \mathrm{Spec}(\mathbb{Z})$ requires "$?$" below $\mathbb{Z}$ |
| Cohomology | $H^*_{\acute{e}t}(C, \mathbb{Q}_\ell)$ | none with all required properties |
| Hodge index | intersection form on $\mathrm{NS}(C \times C)$ | no surface to put an intersection form on |

The **$\mathbb{F}_1$ program** addresses the missing "$?$" — invent a base over which $\mathrm{Spec}(\mathbb{Z})$ becomes a curve, so the fiber product $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ is a surface analog. The **Arakelov program** addresses the compactness — extend $\mathrm{Spec}(\mathbb{Z})$ by adding the archimedean place $\infty$ to get a proper arithmetic surface.

Both are partial answers. Neither delivers the full Hodge index positivity.

---

## 2. The $\mathbb{F}_1$ program

### 2.1 Origins

The phrase "field with one element" goes back to Tits (1956), who noted that several combinatorial identities in algebraic groups make sense if one formally treats a Coxeter system as $G(\mathbb{F}_1)$. Manin (1995) made the $\mathbb{F}_1$ idea explicit in the context of motives: $\mathrm{Spec}(\mathbb{Z})$ should be a curve over $\mathbb{F}_1$, and the Riemann hypothesis should follow from a Weil-type proof in that geometry.

The catch: $\mathbb{F}_1$ cannot be a literal field of cardinality 1 (which would force $0 = 1$). The proposed substitutes redefine "field" to a weaker structure (monoid, blueprint, hyperring, $\Lambda$-ring, ...) under which $\mathrm{Spec}(\mathbb{Z})$ has more geometric structure than as a $\mathbb{Z}$-scheme.

### 2.2 Major variants

Six candidates have been seriously developed and are scorecarded in [`2A_candidate_evaluation.md`](../../experiments/arithmetic_geometric/2A_candidate_evaluation.md). Synthesizing their per-candidate dossiers:

**Deitmar (2005)** — $\mathbb{F}_1$-schemes via commutative monoids. The simplest variant: replace rings with monoids, replace $\mathrm{Spec}(R)$ with $\mathrm{Spec}(M)$ where $M$ is a monoid. Foundation for later frameworks, but the monoid structure is too rigid: the natural fiber product $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ in Deitmar collapses back to $\mathrm{Spec}(\mathbb{Z})$. See [`2A_deitmar_dossier.md`](../../experiments/arithmetic_geometric/2A_deitmar_dossier.md). Scorecard: 3 ✅ / 1 🟡 / 0 ⏳ / 13 ❌ (subsumed by Lorscheid / Borger).

**Lorscheid (2010+)** — Blueprints. A blueprint is a pair $(B, B^\bullet)$ where $B$ is a semiring and $B^\bullet$ is a multiplicative monoid generating $B$. The category of blueprints contains both rings (where $B = B^\bullet$ closed under addition) and monoids (Deitmar's case) as special cases. The natural fiber product $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ in blueprints is the blueprint $(\mathbb{Z} \times \mathbb{Z}, \text{doubled relations})$, a 2-dimensional object in Lorscheid's blueprint dimension theory. See [`2A_lorscheid_dossier.md`](../../experiments/arithmetic_geometric/2A_lorscheid_dossier.md). Scorecard: ~4 ✅ / 4 🟡 / 6 ⏳ / 3 ❌. Strong on the surface side (i-iii) but weak on Frobenius (viii).

**Borger (2009+)** — $\Lambda$-algebraic geometry. The $\Lambda$-ring structure (commuting Adams operations $\psi_p: R \to R$ satisfying $\psi_p(x) \equiv x^p \pmod{p}$) provides the Frobenius lift. $\mathbb{Z}$ is canonically a $\Lambda$-ring (Fermat's little theorem gives $\psi_p = \mathrm{id}$). The fiber product $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ in Borger gives $\mathrm{Spec}(W(\mathbb{Z}))$ via the big Witt ring functor $W$, with $W(\mathbb{Z}) \cong 1 + t\mathbb{Z}[[t]]$ as a multiplicative monoid and Krull dimension 2 in the truncated cases. See [`2A_borger_dossier.md`](../../experiments/arithmetic_geometric/2A_borger_dossier.md). Scorecard: ~4 ✅ / 5 🟡 / 5 ⏳ / 3 ❌. Strong on Frobenius (viii) via the $\psi_p$, but weak on surface structure (ii) since $W(\mathbb{Z})$ is not a clean 2-dimensional scheme.

**Connes & Connes-Consani (2008+)** — Arithmetic site, hyperrings, characteristic-one geometry. The most aggressive direction: a topos $\mathcal{A}$ with hyperring-valued structure sheaf and a Frobenius-like endomorphism $\mathrm{Frob}_{\mathrm{ar}}$, designed to host the full Weil-type machinery. The "characteristic-one" calculus models the formal $q \to 1$ limit of $\mathbb{F}_q$-geometry. See [`2A_connes_dossier.md`](../../experiments/arithmetic_geometric/2A_connes_dossier.md) and [`2A_R3_6_arithmetic_site.md`](../../experiments/arithmetic_geometric/2A_R3_6_arithmetic_site.md). Scorecard: 3 ✅ / 6 🟡 / 4 ⏳ / 3 ❌. Strongest on the L-function side (the trace formula is explicit and produces $\zeta$), but the geometric Hodge index is uncertain. **Per R3.5 ([`2A_R3_5_K1_universality.md`](../../experiments/arithmetic_geometric/2A_R3_5_K1_universality.md))**: every trace-formula NCG framework has positivity $\iff$ RH (the no-shortcut theorem), so the Connes/Connes-Consani positivity conjectures fail kill criterion K1 by structure.

**Deninger (1992+)** — Foliated dynamical systems. Not strictly an $\mathbb{F}_1$ candidate but adjacent: $\mathrm{Spec}(\mathbb{Z})$ should be replaced by a foliated dynamical system $X$ with a real-time flow $\Phi_t$; the leafwise cohomology of this foliation should give the zeta zeros as Frobenius-like eigenvalues, with positivity coming from the Hodge theory of the foliation. The space $X$ has never been constructed. See [`2A_deninger_dossier.md`](../../experiments/arithmetic_geometric/2A_deninger_dossier.md). Scorecard: 2 ✅ / 3 🟡 / 12 ⏳ / 0 ❌ — the program is "honest" in the sense that it makes the right wish list, but it does not provide an explicit construction.

**Toën-Vaquié (2005+)** — Categorification approach. Schemes "under $\mathrm{Spec}(\mathbb{Z})$" defined via symmetric monoidal categories. Not scorecarded in 2A (subsumed by Lorscheid for our purposes). Not directly competitive with the above as an RH-route, but provides categorical infrastructure used by later work.

### 2.3 The universal kill: the Hodge index positivity slot

The 2A evaluation framework identified 17 specific constraints the missing mathematics must satisfy. The scorecards [`2A_candidate_evaluation.md`](../../experiments/arithmetic_geometric/2A_candidate_evaluation.md) reveal a universal pattern: **no candidate has even a partial ✅ on the Hodge index positivity slot (constraints xi-xiii)**. Some candidates have ❌ (provably ruled out for that slot, e.g., Connes/Connes-Consani after R3.5/R3.6) and others have ⏳ (open), but none has a positive answer.

This is the single open problem the $\mathbb{F}_1$ program has failed to address. The Frobenius slot (viii-x) is well-covered by Borger and Connes. The surface slot (i-iii) is well-covered by Lorscheid and Connes-Consani. The Hodge index — the actual SOURCE of the positivity that closes Weil's proof — has not been delivered by any single candidate.

### 2.4 Hybrid proposals

[`2A_path_forward.md`](../../experiments/arithmetic_geometric/2A_path_forward.md) synthesizes the R-series follow-ups into two hybrid proposals that combine strengths across candidates:

- **R2.5 $\Lambda$-blueprints** ([`2A_R2_5_lambda_blueprints.md`](../../experiments/arithmetic_geometric/2A_R2_5_lambda_blueprints.md)): a triple $(B, B^\bullet, \{\psi_p\})$ combining Lorscheid's blueprint structure with Borger's Adams operations. Predicted scorecard: 8 ✅ / 4 🟡 / 5 ⏳. Improves over Borger on the surface slot (ii) and over Lorscheid on the Frobenius slot (viii). The Hodge index slot (xi-xiii) remains universally open.
- **R4 Borger + Connes hybrid** ([`2A_R4_borger_connes_hybrid.md`](../../experiments/arithmetic_geometric/2A_R4_borger_connes_hybrid.md)): Borger's Adams operations $\psi_p$ generate Connes' $\mathbb{R}^*_+$-action via $U_t = \prod_p U_{\log p}^{t/\log p}$ in the multiplicative completion. Candidate Hilbert space $H = L^2(W(\mathbb{Z}), \mu)$ for an appropriate measure $\mu$. Predicted scorecard similar to R2.5 but with trace formula explicit.

**Status: both are research proposals, not established mathematics.** The R2.5 framework needs precise categorical definitions, fiber product computations, and verification of the predicted scorecard. The R4 framework needs the right measure $\mu$, convergence of the multiplicative completion, and explicit trace formula recovery. Estimated effort per [`2A_path_forward.md`](../../experiments/arithmetic_geometric/2A_path_forward.md): thesis-level for each, multi-paper research program for the combined attack.

---

## 3. The Arakelov program

### 3.1 Arakelov geometry, classical (1974-2000s)

Arakelov (1974) addressed the same compactness gap but from the opposite direction: rather than invent a base below $\mathbb{Z}$, **add the archimedean place $\infty$** to $\mathrm{Spec}(\mathbb{Z})$ to produce a proper "arithmetic curve" $\overline{\mathrm{Spec}(\mathbb{Z})}$. The construction:

- For an arithmetic surface $X \to \mathrm{Spec}(\mathcal{O}_K)$ over a number ring $\mathcal{O}_K$, define an **Arakelov divisor** to be a finite formal sum $D = \sum n_v v + \sum_{\sigma: K \to \mathbb{C}} \alpha_\sigma F_\sigma$, where $v$ ranges over finite places (closed points of $\mathrm{Spec}(\mathcal{O}_K)$) and $\sigma$ ranges over archimedean places, with $\alpha_\sigma \in \mathbb{R}$ being a real "intersection multiplicity" at $\infty$.
- Equip the fiber at $\infty$ with **Hermitian metrics** (smooth real-valued positive functions) representing the archimedean intersection theory.
- Define an **arithmetic intersection pairing** $D_1 \cdot D_2 \in \mathbb{R}$ combining finite-place intersections (from algebraic geometry of the special fibers) with archimedean contributions (Green's functions, Hermitian metrics).

The pairing satisfies an analog of Hodge index (Arakelov 1974, sharpened by Faltings 1984): for arithmetic surfaces (relative dimension 1 over $\mathrm{Spec}(\mathcal{O}_K)$), the pairing is negative semi-definite on the orthogonal complement of an "ample" divisor.

**This is a partial Hodge index for arithmetic surfaces over a base of higher relative dimension.** It does NOT directly give a Hodge index for $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$, because that fiber product doesn't exist in scheme theory.

### 3.2 Soulé, Gillet-Soulé, and arithmetic Riemann-Roch

Soulé and collaborators (1980s-1990s) developed arithmetic Chow groups $\widehat{\mathrm{CH}}^*(X)$ for arithmetic varieties of arbitrary relative dimension, with an arithmetic intersection pairing and an arithmetic Riemann-Roch theorem (Gillet-Soulé 1992). Bismut, Lebeau, Gillet, Soulé extended this with **analytic torsion** and the arithmetic Grothendieck-Riemann-Roch (1991).

What this gives:

- A well-defined arithmetic intersection theory on arithmetic varieties $X \to \mathrm{Spec}(\mathcal{O}_K)$.
- A characteristic class theory ("arithmetic Chern classes") that combines algebraic and analytic data.
- Analogs of Hirzebruch-Riemann-Roch in the arithmetic setting.

What this does NOT give for RH:

- An arithmetic intersection theory on $\mathrm{Spec}(\mathbb{Z})$ itself (relative dimension 0). The Arakelov-Soulé framework requires positive relative dimension; the base $\mathrm{Spec}(\mathbb{Z})$ has no further structure.
- A Frobenius-like operator. The framework is essentially analytic at $\infty$ and algebraic at finite places, with no unified endomorphism analog to function-field Frobenius.

**Consequence:** classical Arakelov geometry does not directly attack RH. It compactifies $\mathrm{Spec}(\mathbb{Z})$ in a sense (adding the archimedean Green's function data), but the compactified $\overline{\mathrm{Spec}(\mathbb{Z})}$ is a "curve" of arithmetic Krull dimension 1, not the 2D surface that Weil's proof needs.

### 3.3 Bost, Burgos-Kramer-Künnemann, and higher Arakelov

Bost (1990s-2010s) developed arithmetic intersection theory in the context of $\mathrm{GL}_2$ Eisenstein series, with explicit applications to the Faltings-Bost arithmetic Riemann-Roch. Burgos-Kramer-Künnemann (2000s) extended Arakelov to **logarithmically singular metrics**, enlarging the class of metrics that can carry arithmetic intersection theory.

These developments expand the technical toolkit of Arakelov geometry but do not change its fundamental structure: they remain frameworks for proper arithmetic varieties of relative dimension $\geq 1$, not for $\mathrm{Spec}(\mathbb{Z})$ itself.

### 3.4 The Arakelov gap for RH

The Arakelov program addresses two of the three Weil ingredients:

- **Compactification (Poincaré duality)**: partially addressed via the archimedean place. The arithmetic intersection pairing gives a duality, but on objects one dimension up.
- **Frobenius**: not addressed. Arakelov has no Frobenius substitute.
- **Hodge index**: partially addressed for arithmetic surfaces (Faltings 1984), but not at the level of $\mathrm{Spec}(\mathbb{Z})$.

For Architecture 2's RH target, Arakelov supplies infrastructure that any RH-relevant construction will need (Hermitian metrics, Green's functions at $\infty$, arithmetic intersection theory) but does not directly provide the missing positivity. The 2A scorecards reflect this: Arakelov-style constructions score on the surface side (i-iii) and partially on cohomology (iv-vii) but not on Frobenius (viii-x) or Hodge index (xi-xiii).

---

## 4. The 2018-2025 infrastructure: prismatic cohomology, condensed mathematics, perfectoid spaces

### 4.1 Prismatic cohomology (Bhatt-Morrow-Scholze 2018+)

The biggest cohomological development of the late 2010s. Prismatic cohomology unifies $p$-adic cohomology theories (étale, crystalline, de Rham, Hodge-Tate) into a single framework built on **$\delta$-rings**. A $\delta$-ring is a ring $R$ with an operator $\delta: R \to R$ satisfying $\delta(x + y) = \delta(x) + \delta(y) - \binom{?}{?}...$ — the "Frobenius descent" structure. Importantly, **$\delta$-rings are essentially $\Lambda$-rings at one prime** $p$: the operator $\delta$ encodes $\psi_p$ at the local level.

Connection to Borger's framework: a global $\Lambda$-ring structure (Adams operations $\psi_p$ for every prime $p$, satisfying the standard relations) gives a $\delta$-structure at every prime. So **prismatic cohomology naturally applies to Borger's $\mathrm{Spec}(W(\mathbb{Z}))$** ([`2A_R5_prismatic_cohomology.md`](../../experiments/arithmetic_geometric/2A_R5_prismatic_cohomology.md)). Predicted impact: closes the cohomology slots (iv-vii) — finite cohomology, Poincaré duality, cycle class map, Künneth — in one move for Borger's framework.

What prismatic cohomology does NOT give for RH:

- Direct attack on K1 (positivity ⇒ RH). Prismatic cohomology has its own trace formula structure, which falls under R3.5's no-shortcut theorem.
- A Hodge index theorem on the prismatic side. The Hodge-Tate spectral sequence for prismatic cohomology gives filtrations and weights, but no positivity argument analogous to Hodge index on $C \times C$ in the function field case.

**Status (2025):** prismatic cohomology is genuinely new and very active. It provides infrastructure for Borger's framework and (via the $\delta$-ring connection) for any $\Lambda$-ring-based RH approach. But it does not close the Hodge index gap. Open R5 questions enumerated in [`2A_R5_prismatic_cohomology.md`](../../experiments/arithmetic_geometric/2A_R5_prismatic_cohomology.md): right notion of prismatic cohomology of $\mathrm{Spec}(W(\mathbb{Z}))$, $\psi_p$-equivariant cohomology, etc.

### 4.2 Condensed and light condensed mathematics (Clausen-Scholze 2019+)

A foundational reformulation of topology designed to make topological algebra behave like algebra. Topological spaces are replaced by **condensed sets** (sheaves on the pro-étale site of profinite sets), and topological abelian groups by condensed abelian groups. The motivation: classical functional analysis ("locally convex topological vector spaces") has bad categorical properties (no kernels, cokernels not well-behaved); condensed math fixes this.

Implications for Architecture 2:

- Condensed math gives a clean framework for $p$-adic functional analysis and infinite-dimensional algebra over $\mathbb{Z}_p$ or $\mathbb{Q}_p$. The Connes adèle class space, which lives in topological algebra territory, can in principle be reformulated condensed-mathematically.
- Connes' trace formula on $\mathbb{A}_{\mathbb{Q}}/\mathbb{Q}^*$ has been hampered by topological subtleties (continuity of $\zeta$ at $s = 1$, distributional issues). Condensed math is a natural setting to resolve these.
- "Light condensed" (Clausen-Scholze 2022+): a simpler variant restricted to "countable" presentations. May be sufficient for arithmetic applications.

**Status (2025):** condensed math is reorganizing the foundations of analytic geometry. Direct RH applications have not been demonstrated, but the framework is plausibly the right setting for rigorizing Connes' construction. Cross-cut to R4 (Borger + Connes hybrid): condensed math could be the formalism for the Hilbert space $L^2(W(\mathbb{Z}), \mu)$ proposed there.

### 4.3 Perfectoid spaces and tilting (Scholze 2012+, ongoing)

Perfectoid spaces (Scholze 2012) provide a setting where characteristic $0$ ($\mathbb{Q}_p$) and characteristic $p$ ($\mathbb{F}_p((t))$) can be related via the "tilting equivalence" $X^\flat$. This was Scholze's tool for proving the weight-monodromy conjecture and (with Bhatt) substantial parts of the $p$-adic Langlands program.

Relation to $\mathbb{F}_1$ and Arakelov:

- The tilting equivalence is a precise instance of the "lift function-field structure to characteristic $0$" intuition that motivates $\mathbb{F}_1$.
- However, tilting is one-prime-at-a-time ($p$-perfectoid spaces): not a single global lift.
- Bhatt-Scholze "Prismatic F-crystals" (2021) extends prismatic cohomology with crystal-theoretic data that is somewhat F_1-flavored.

**Status (2025):** perfectoid spaces are now standard machinery in $p$-adic geometry but have not been wired into the $\mathbb{F}_1$ or Arakelov programs in an RH-relevant way. They provide infrastructure for $p$-adic constructions in characteristic 0, complementary to the global structures the RH problem needs.

### 4.4 Other 2020s developments

**Bost's foliations** (1990s-2020s, ongoing): Bost has continued developing arithmetic foliations in the context of Bost-Connes Q-statistical mechanics systems and the Arakelov geometry of Shimura varieties. Adjacent to Deninger's foliated-space program but with concrete examples (specifically the Bost-Connes QSM and modular Shimura varieties) rather than the conjectural foliated space $X$.

**Motivic Arakelov cohomology** (Kahn, Soulé, others 2010s-2020s): unifying Arakelov geometry with motivic cohomology. Open whether this unification provides RH-relevant structure; not yet demonstrated.

**Manin-Marcolli "geometry of $\mathbb{F}_1$"** (ongoing): a continuation of the Manin 1995 program, with applications to "absolute" motives and to Connes-Consani's arithmetic site. Largely synthesis-and-survey work; not novel constructions.

---

## 5. Status assessment as of 2025

### 5.1 The aggregated landscape

Combining the per-candidate scorecards from [`2A_candidate_evaluation.md`](../../experiments/arithmetic_geometric/2A_candidate_evaluation.md) with the 2020s infrastructure:

| Constraint slot | Best candidate(s) | Status |
|---|---|---|
| (i)-(iii) Surface base $\mathrm{Spec}(\mathbb{Z}) \times_? \mathrm{Spec}(\mathbb{Z})$ | Lorscheid (blueprint), Borger (Witt ring); $\Lambda$-blueprints would improve | 🟡 partial; the candidates produce non-trivial 2D-ish objects but not the geometric surface |
| (iv)-(vii) Cohomology with required properties | Borger + prismatic cohomology (R5) | 🟡 prismatic gives finite cohomology, Poincaré duality, Künneth, cycle class for Borger's framework |
| (viii)-(x) Frobenius substitute | Borger ($\psi_p$), Connes ($\mathbb{R}^*_+$-action) | ✅ for both, complementary mechanisms |
| (xi)-(xiii) **Hodge index positivity** | **NONE** | ❌ **universal open** |
| (xiv)-(xvi) Trace formula recovering explicit formula | Connes (explicit), Deninger (conjectural) | 🟡 Connes' is rigorous but topological, Deninger's depends on missing $X$ |
| (xvii) D-H exclusion (K2) | All six candidates by construction | ✅ structural (linear combinations of L-functions not constructible) |

**Central finding (unchanged from 2A R3.5 / R3.6 synthesis):** the Hodge index positivity slot is the unique open construction problem. Every candidate provides some of the infrastructure; none provides the positivity. **The geometric route — intersection theory + Hodge index theorem on a constructed surface — is structurally the unique escape** from the K1 wall ([`2A_R3_5_K1_universality.md`](../../experiments/arithmetic_geometric/2A_R3_5_K1_universality.md)).

### 5.2 What's strong as of 2025

- **Borger + prismatic cohomology** for the Frobenius and cohomology slots. Prismatic cohomology is a real advance and naturally applies to Borger's $\mathrm{Spec}(W(\mathbb{Z}))$.
- **Lorscheid blueprints** for the base / surface slot. Clean 2D structure with the right categorical properties.
- **Connes' arithmetic site** as a host for the trace formula and L-function recovery. The categorical machinery (topos with hyperring-valued structure sheaf, characteristic-one calculus) is rich infrastructure.
- **Condensed mathematics** as a foundational setting for $p$-adic and adèlic analysis.

### 5.3 What's weak / unaddressed

- **No candidate constructs the Hodge index positivity.** Per R3.5, NCG-only approaches (Connes-style) provably cannot escape K1 by structure. The positivity must come from intersection theory on a constructed surface, not from a trace formula.
- **No candidate has been fully developed** — every candidate has open technical questions enumerated in its R-series follow-up. The hybrid proposals (R2.5 $\Lambda$-blueprints, R4 Borger + Connes) are research proposals, not established mathematics.
- **Arakelov-style archimedean compactification has not been wired into $\mathbb{F}_1$ candidates.** The arithmetic intersection theory of Soulé-Gillet et al. assumes a fixed scheme structure; combining it with $\mathbb{F}_1$-style modified base requires reformulating both.

### 5.4 The path forward

[`2A_path_forward.md`](../../experiments/arithmetic_geometric/2A_path_forward.md) lays out a multi-paper research program. The strategic outline:

1. **Develop the $\Lambda$-blueprints framework rigorously** (R2.5): definitions, categorical properties, fiber product computations.
2. **Apply prismatic cohomology to both Borger and the $\Lambda$-blueprints framework** (R5): closes (iv)-(vii) slots.
3. **Construct an arithmetic intersection theory on the fiber product** (open): the actual Hodge index positivity. This is the central open construction problem, projected at 5-10 years of multi-author research.
4. **Verify via Davenport-Heilbronn discipline**: the resulting framework must distinguish $\zeta$ from D-H (covered by K2 / R1 for all six candidates by construction, but new hybrids need to inherit this).

Success probability per [`2A_path_forward.md`](../../experiments/arithmetic_geometric/2A_path_forward.md): < 50%, with substantial intellectual value in the partial progress regardless.

### 5.5 What this project can and cannot contribute

The project's experimental thread has produced concrete artifacts at the per-candidate scorecard level:

- [2A diff document](../../experiments/arithmetic_geometric/2A_weil_proof_diff.md) and [evaluation framework](../../experiments/arithmetic_geometric/2A_candidate_evaluation.md): a working set of constraints and predicates for evaluating new candidates.
- Six per-candidate dossiers: rigorous scorecards for the existing major frameworks.
- R-series follow-ups: hybrid proposals (R2.5, R4), no-shortcut theorem (R3.5), prismatic cohomology connection (R5).
- 2B worked example: the only place in the project where RH is actually proved (for $E/\mathbb{F}_5$).
- 2E Adams-spectrum probe: numerical confirmation that bare $\psi_p$ on concrete $\Lambda$-rings does not host zeta-zero spectra (the cohomology must do the lifting).

What the project cannot deliver: the Hodge index construction itself. That requires multi-decade research-grade work along the lines identified, beyond the scope of the project as currently scoped.

---

## 6. Cross-architecture context

The $\mathbb{F}_1$ / Arakelov programs (Architecture 2) are the **only** route to RH among the four candidate architectures that can escape the K1 wall:

- **Architecture 1 (spectral / Hilbert-Pólya)**: every trace-formula NCG framework with standard spectral identification has positivity $\iff$ RH (R3.5 no-shortcut theorem). NCG-only approaches universally fail K1 by structure.
- **Architecture 3 (direct positivity / Weil / Li)**: the analytic Weil-form duality hits a circularity wall (LEARNINGS finding #7) — unconditional proof requires GRH-strength input. The wall is universal across the Selberg class, including for $\chi_3$ where cancellation is milder (LEARNINGS finding #7).
- **Architecture 4 (analytic / zero-free regions)**: 67-year stagnation at the V-K exponent $2/3$, with all three inputs of the recipe near-optimal (LEARNINGS finding #14). The line-restriction lemma is robust under the entire LP/SDP relaxation family (LEARNINGS findings #12, #13, #15). Architecture 4 is a constraint-mapping architecture, not a route to RH.

**Only Architecture 2 has a structural escape route**: intersection theory + Hodge index theorem on a constructed surface provides positivity from the **signature** of an intersection form, a structurally different kind of positivity not subject to R3.5's no-shortcut theorem. This is the unique direction in the four-architecture framework where K1 can be escaped.

But: as documented above, the construction is hard. No candidate framework as of 2025 closes the Hodge index slot. The path forward is multi-decade research-grade work.

---

## 7. Selected references

### $\mathbb{F}_1$ program

- Tits, J. (1956). "Sur les analogues algébriques des groupes semi-simples complexes." *Centre Belge Rech. Math.*
- Manin, Y. (1995). "Lectures on zeta functions and motives." *Astérisque* 228.
- Deitmar, A. (2005). "Schemes over $\mathbb{F}_1$." In *Number Fields and Function Fields — Two Parallel Worlds*. Birkhäuser.
- Soulé, C. (2004). "Les variétés sur le corps à un élément." *Mosc. Math. J.* 4(1).
- Toën, B. & Vaquié, M. (2009). "Au-dessous de $\mathrm{Spec}\,\mathbb{Z}$." *J. K-Theory* 3(3).
- Lorscheid, O. (2012). "The geometry of blueprints." *Adv. Math.* 229(3).
- Borger, J. (2009). "$\Lambda$-rings and the field with one element." arXiv:0906.3146.
- Connes, A. & Consani, C. (2008-present). Multiple papers on the arithmetic site and hyperrings.
- Manin, Y. & Marcolli, M. (2014). "Quantum statistical mechanics, $L$-series and anabelian geometry, I."

### Arakelov geometry

- Arakelov, S.J. (1974). "Intersection theory of divisors on an arithmetic surface." *Izv. Akad. Nauk SSSR Ser. Mat.* 38.
- Faltings, G. (1984). "Calculus on arithmetic surfaces." *Ann. Math.* 119.
- Soulé, C. (1992). *Lectures on Arakelov Geometry* (with Abramovich, Burnol, Kramer). Cambridge.
- Gillet, H. & Soulé, C. (1992). "An arithmetic Riemann-Roch theorem." *Invent. Math.* 110.
- Burgos Gil, J.I., Kramer, J. & Künnemann, U. (2007). "Cohomological arithmetic Chow rings." *J. Inst. Math. Jussieu* 6.
- Bost, J.-B. (1990s-present). Multiple papers on arithmetic intersection theory and Bost-Connes systems.

### Recent infrastructure (2018-2025)

- Bhatt, B., Morrow, M. & Scholze, P. (2018-2019). "Topological Hochschild homology and integral $p$-adic Hodge theory" and "Integral $p$-adic Hodge theory."
- Bhatt, B. & Scholze, P. (2022). "Prisms and prismatic cohomology." *Ann. Math.* 196.
- Clausen, D. & Scholze, P. (2019-2024). "Lectures on Condensed Mathematics" and "Lectures on Analytic Geometry."
- Scholze, P. (2012). "Perfectoid spaces." *Publ. Math. IHES* 116.

### Project-internal cross-references

- [2A weil proof diff](../../experiments/arithmetic_geometric/2A_weil_proof_diff.md): the diff table at the heart of the F_1 + Arakelov programs' joint target.
- [2A candidate evaluation](../../experiments/arithmetic_geometric/2A_candidate_evaluation.md): scorecards for the six candidates.
- [2A R3.5 K1 universality](../../experiments/arithmetic_geometric/2A_R3_5_K1_universality.md): the no-shortcut theorem ruling out NCG-only approaches.
- [2A R5 prismatic cohomology](../../experiments/arithmetic_geometric/2A_R5_prismatic_cohomology.md): the 2018+ BMS infrastructure applied to Borger.
- [2A path forward](../../experiments/arithmetic_geometric/2A_path_forward.md): the strategic multi-paper plan.
- [Research atlas §2.2](../research_atlas/README.md#22-arithmetic-geometry--function-field-analogy): high-level overview at the project-master-document level.
