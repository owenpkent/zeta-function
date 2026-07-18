# Reading notes: Abboud, *A Local Version of the Arithmetic Hodge Index Theorem over Quasiprojective Varieties* (arXiv:2503.14099v2, 22 Apr 2025)

> Reading note on one of the four "closest live-M4" math.AG papers that the #155 corpus cross-reference
> ([`rh_corpus_2021-2026_vs_frontier.md`](rh_corpus_2021-2026_vs_frontier.md) lines 40, 57) flagged as
> lacking a reading_notes entry (the others: He 2512.01811, Connes-Consani 2606.06604, Chen-Moriwaki
> 2207.02033). **The parent task flagged this as Connes-Consani / arithmetic-site orbit; it is not.** It is
> Arakelov intersection theory / non-archimedean pluripotential theory, in the direct service of arithmetic
> dynamics. It is the local (single-place) polarization face, facet B of the universal gap
> ([`../sourcing_gap_r1.md`](../sourcing_gap_r1.md)), extended to quasiprojective varieties. Scored against
> the repo's M4 skeleton (S1-S7, [`../breadth_program.md`](../breadth_program.md) lines 55-80) and the R1 /
> K1 / #156 screens.
>
> **Reading depth, stated honestly.** The abstract, introduction (Section 1: Theorems A, B, C, and the
> quoted global [YZ17] statement), and preliminaries (Section 2, through 2.9) were read directly from the
> rendered arXiv PDF pages 1-8 (VERIFIED-BY-FETCH); the full HTML was also fetched to confirm no
> RH-adjacent content and the theorem statements. The proofs (Section 3 onward: the density result and the
> Hodge-index argument itself) were NOT read. All cited references ([YZ17], [YZ23], [CD12], [CM21],
> [Gub98], [Abb24], [Mor16], [Laz04], [Ber12]) are BIBLIOGRAPHIC-ONLY (identified, not read); the [CM21]
> and [Abb24] identifications are inferred from context and flagged as such.

## Bibliographic header (VERIFIED-BY-FETCH)

- **Title:** *A Local Version of the Arithmetic Hodge Index Theorem over Quasiprojective Varieties*
- **Author:** Marc Abboud (Université de Neuchâtel)
- **arXiv:** 2503.14099, v1 18 Mar 2025, v2 22 Apr 2025. Primary **math.AG**, cross-list **math.NT**.
- **MSC 2020:** 14G40 (Arithmetic varieties, heights), 32P05 (non-archimedean analysis), 32W20
  (complex Monge-Ampère operators). **Key words:** adelic divisors, adelic line bundles, arithmetic Hodge
  index.
- **Funding / venue:** Swiss National Science Foundation grant "Birational transformations of higher
  dimensional varieties" 200020-214999; acknowledges BICMR (Beijing) and discussions with Junyi Xie and
  Xinyi Yuan. arXiv admin note: substantial text overlap with arXiv:2406.11510 (the author's companion).
  No journal-ref recorded at fetch time.

## One-line takeaway

Abboud extends the Yuan-Zhang arithmetic Hodge index theorem from projective to **quasiprojective**
varieties over a **single complete field $K_v$** (archimedean or non-archimedean), by defining a local
intersection number for **compactly supported vertical** metrised line bundles and proving
$\overline M^2\cdot\overline L_1\cdots\overline L_{n-1}\le 0$ with equality iff the metric is constant.
The motivation and payload are **arithmetic dynamics** (a Calabi-type Monge-Ampère uniqueness, applied in
[Abb24] to periodic points of affine-surface automorphisms). Zeta, $L$-functions, RH, Frobenius,
$\mathrm{Spec}(\mathbb{Z})$, primes, and the functional equation appear **nowhere** (checked pages 1-8 +
full-HTML fetch). This is the repo's already-mapped "Faltings-Hriljac / Yuan-Zhang too local" object
([#131 Arakelov-face probe](../../../experiments/arithmetic_geometric/2L_arakelov_face_probe.md);
[#133 obstruction map](../../../publications/obstruction_map/obstruction_map.md)), pushed in the strictly
**more local** direction (one place, non-proper base) that is the opposite of the global assembly M4 needs.

## What the paper does (VERIFIED-BY-FETCH, Sections 1-2)

The setting is Yuan-Zhang's theory of **adelic / metrised line bundles over quasiprojective varieties**
([YZ23]) and Chambert-Loir-Ducros non-archimedean pluripotential theory ([CD12], Berkovich spaces). A
metrised line bundle over a projective $X$ has a well-defined intersection number; over a quasiprojective
(non-proper) $U$ there was no local intersection number, because the Green function $g_{\overline M}$ of a
vertical bundle (trivial underlying line bundle) need not be integrable against the Chambert-Loir measure.

- **Theorem A (well-definedness, eq. 3-5).** For a normal quasiprojective $U/K_v$, restricting the first
  argument to **compactly supported vertical** metrised bundles ($g_{\overline M}$ constant outside a
  compact subset of $U^{\mathrm{an}}$) gives a well-defined local intersection number
  $\widehat{\mathrm{Pic}}_c(U)\times\widehat{\mathrm{Pic}}(U)_{int}\to\mathbb R$,
  $\overline M\cdot\overline L_1\cdots\overline L_n=\int_{U^{\mathrm{an}}} g_{\overline M}\,
  c_1(\overline L_1)\cdots c_1(\overline L_n)$, linear in the first variable, symmetric multilinear in the
  last $n$, invariant under scalar extension, with an integration-by-parts formula. Proof engine (not read
  in detail): a density result that model functions constant outside a compact $\Omega$ are dense in
  continuous functions constant outside $\Omega$.
- **Theorem B (the local arithmetic Hodge index, eq. 7).** For $\overline M$ compactly supported vertical
  and $\overline L_1,\dots,\overline L_{n-1}$ **nef**:
  $$\overline M^{2}\cdot\overline L_1\cdots\overline L_{n-1}\ \le\ 0,$$
  and if $\overline M$ is $\overline L_i$-bounded for each $i$ and $L_i^{n}>0$, **equality holds iff the
  metric of $\overline M$ is constant** over $U^{\mathrm{an}}$. This is the quasiprojective extension of
  the projective statement Abboud quotes verbatim from [YZ17] (eq. 6): for projective $X$, $\overline M$
  vertical integrable, $\overline L_i$ semipositive with $L_i$ big and nef, the same inequality holds.
- **Theorem C (Monge-Ampère uniqueness / Calabi variant).** For two nef $\overline L_1,\overline L_2$ with
  $c_1(\overline L_1)^n=c_1(\overline L_2)^n$ and vertical compactly supported difference (same underlying
  $L$), if $L^n>0$ then the metric of $\overline L_1-\overline L_2$ is constant. The positivity hypothesis
  $L_i^n>0$ is shown necessary.
- **The application (Section 1, via [Abb24]).** For a normal affine surface $U$ over an algebraically
  closed field and automorphisms $f,g$ of first dynamical degree $>1$: $f,g$ share a Zariski-dense set of
  periodic points **iff** they have the same periodic points. This is the paper's actual purpose;
  arithmetic dynamics, no analytic number theory.

## The central object

The quadratic form $\overline M\mapsto \overline M^{2}\cdot\overline L_1\cdots\overline L_{n-1}$ on
**compactly supported vertical** metrised line bundles over a quasiprojective $U$ over **one complete
field $K_v$**, with Theorem B its negative-semidefiniteness (definite modulo constant metrics). It is a
**local factor** (one place $v$) of the global arithmetic Hodge index, the finest-grained, most-local
version of the Arakelov polarization: the global Yuan-Zhang statement over a number field sums such local
contributions over all places; this paper isolates and extends **one** of them.

## Scorecard: S1-S7 + R1 + K1 + #156

Skeleton per [`../breadth_program.md`](../breadth_program.md) lines 55-80 (M4, stripped). The central
object is the local intersection pairing and its Theorem-B negativity.

| Slot | Reading | Verdict |
|---|---|---|
| **S1** Lefschetz operator | Cup with the nef classes $\overline L_1\cdots\overline L_{n-1}$ is the arithmetic-Lefschetz-shaped operator (multiply by the ample/nef class). Present as the geometric hard-Lefschetz $L^{n-1}$, but with no Frobenius / spectral coupling. | YES-shaped (geometric), decorative for RH |
| **S2** primitive decomposition | The **vertical** bundles $\overline M$ (trivial underlying line bundle = generic-fibre class $0$) are exactly the primitive/degree-0 part on which the index sign is stated. A vertical/horizontal split, not a full $\mathfrak{sl}_2$ Lefschetz decomposition. | PARTIAL: vertical = the primitive piece the sign lives on |
| **S3** duality / pairing | The local intersection number is a symmetric, multilinear, scalar-extension-invariant pairing (Thm A). A genuine pairing, but it is geometric intersection / Poincaré-type duality, **not** the $s\leftrightarrow 1-s$ functional equation of any $L$-function (none present). | YES as a pairing; NO as a functional equation |
| **S4** trace datum $t$ | **No Frobenius eigenvalue, no spectral parameter, no $t$-slot.** The nef $\overline L_i$ are fixed geometric data; nothing the sign could be contingent on. | **NO (empty)** |
| **S5** polarization | Theorem B: $\overline M^2\cdot\overline L_1\cdots\overline L_{n-1}\le 0$, equality iff constant metric. A genuine definite-sign (negative-semidefinite, definite mod constants) statement on the primitive/vertical part = a Hodge-Riemann-type polarization. | YES (a proven polarization theorem) |
| **S6** RIGHT POLARITY | **WRONG POLARITY.** Theorem B is **unconditional**: it holds for every compactly supported vertical $\overline M$ and every nef $\overline L_i$, always $\le 0$; it **never flips**, because there is no spectral parameter for it to be contingent on. This is the exact master-discriminator failure mode ([breadth_program](../breadth_program.md) lines 74-80): the arithmetic Hodge index, like the Kähler Hodge-Riemann relations / AHK / Alexandrov-Fenchel, can never flag an RH violation. | **WRONG POLARITY (fatal slot)** |
| **S7** non-circularity | K1-clean: the proof consumes no zeros, no RH (pure Arakelov + Chambert-Loir-Ducros + Yuan-Zhang density). But non-circularity here is a **consequence** of the wrong polarity: it is zeta-blind precisely because it is unconditional. | YES, but moot (S6 already fails) |
| **R1** face | Supplies **neither** a Frobenius-like endomorphism / correspondence with isolated prime-indexed fixed points on a genuine $\mathrm{Spec}(\mathbb Z)\times\mathrm{Spec}(\mathbb Z)$, **nor** a trace realization of zeta. Base = one complete field $K_v$; no self-product, no fixed-point count, no prime index, no $L$-function. Pure facet-B (polarization), and made strictly **more local**, not facet-A (sourcing). | **NO on both** |
| **K1** circularity | No positivity/RH claim; nothing to consume RH or the zeros. | CLEAN (vacuously) |
| **#156** WATCH clause | The clause (R1 filler must be index-set-preserving AND non-endomorphism-shaped) screens candidate *movers*; this is a polarization theorem, not a mover. On the conjuncts: **non-endomorphism-shaped YES** (a symmetric quadratic form, not a ring endomorphism), but **index-set-preserving NO** in the operative sense: it is single-place / local, carrying no prime index set at all (the opposite of a global-over-$\mathrm{Spec}(\mathbb Z)$ object). | Not an R1 filler; fails the global conjunct |

**Fingerprint:** S1 geometric-YES, S2 partial, S3 pairing-YES/FE-NO, **S4 empty**, S5 YES, **S6 WRONG
POLARITY**, S7 moot. Same fingerprint as every unconditional Hodge-index / Hodge-Riemann theorem in the
breadth corpus: it has the pairing and a definite sign, but no trace datum for the sign to see and an
unconditional (never-flipping) polarity. The two slots that carry RH (S4 the parameter, S6 the
contingency) are exactly the two that are empty/wrong.

## Honest verdict (#155 histogram convention)

**KNOWN-TO-REPO** (primary), with a thin **ADJACENT-WATCH** sub-flag on one technical ingredient.

- **Why KNOWN-TO-REPO.** The load-bearing object is the Yuan-Zhang / Faltings-Hriljac arithmetic Hodge
  index: a **proven per-place/per-surface polarization with unconditional (wrong-polarity) sign that
  "dies at the base / is too local."** The repo has this fully mapped and named as "the nearest proven
  polarization" ([#131 probe](../../../experiments/arithmetic_geometric/2L_arakelov_face_probe.md);
  corpus note [line 40](rh_corpus_2021-2026_vs_frontier.md): *"Nearest proven polarization remains
  Faltings-Hriljac on a single surface; transport to the self-product with a Frobenius correspondence is
  untouched"*; obstruction map bracket *"Faltings-Hriljac too local"*). Abboud moves this exact object in
  the **strictly more local** direction (one place instead of the global sum; quasiprojective/non-proper
  base; a compactly supported local factor), which is the **opposite** of the global-$\mathrm{Spec}(\mathbb
  Z)$-self-product-with-Frobenius assembly that M4 requires. It supplies no Frobenius, no self-product base,
  no contingent sign, and (unlike Connes' survey, the ADJACENT-WATCH exemplar) it does not even **name**
  the RH residual: RH is absent from the paper. That is more inert than the average ADJACENT-WATCH, not
  less.
- **The one ADJACENT-WATCH ingredient (genuinely new relative to the repo, wrong-direction for M4).** The
  **quasiprojective / compactly-supported extension** of the arithmetic Hodge index is new mathematics
  post-dating the repo's projective Yuan-Zhang treatment. $\mathrm{Spec}(\mathbb Z)$ is affine (non-proper),
  so an arithmetic Hodge index that works over **open / non-proper** models is, in shape, the right technical
  primitive **if** a future M4 assembly ever needs the polarization on a non-compactified arithmetic model
  (an arithmetic surface with fibres removed, a boundary-divisor setting). This is why it earns a watch
  line rather than a flat file-and-forget. But the direction is wrong (more local, single place) and it
  carries no trace datum and no contingent sign, so the watch is thin: it is a **better component candidate**
  (P3 in [breadth_program](../breadth_program.md)) for the substrate, never a mechanism for the sign.
- **Not NEW-LOAD-BEARING.** No Frobenius, no self-product, no contingent polarity, no trace realization,
  no RH content. The two RH-carrying slots (S4, S6) are empty/wrong. Survives my own skeptical re-read as
  inert for the open kernel.

## What this supplies for M4 / R1 (and what it does not)

- **For M4 (facet B, the polarization sign):** it supplies a *proven local polarization theorem* of exactly
  the wrong polarity (unconditional) at exactly one place, i.e. one more instance of the object the repo
  already brackets as too-local + wrong-polarity. It does **not** supply the contingent sign (S6) or the
  global sum-over-places-with-a-Frobenius-correspondence assembly. The genuinely reusable residue is the
  **compactly-supported / non-proper** technical extension, logged as a component (substrate) candidate for
  any future BUILDER attempt that needs Arakelov positivity over an open arithmetic base.
- **For R1 (facet A, the sourcing / trace-budget operator):** nothing. No Frobenius, no
  $\mathrm{Spec}(\mathbb Z)\times\mathrm{Spec}(\mathbb Z)$, no prime-indexed fixed points, no determinant-class
  trace formula, not even a trace realization of $\zeta$.
- **Davenport-Heilbronn note:** the object has no Euler product and no $L$-function to instantiate; it is
  D-H-exempt by non-mimicry (Architecture-2 style), consistent with the repo's #131/#132 handling of the
  Arakelov face.

## References to chase (BIBLIOGRAPHIC-ONLY; identifications flagged)

- **[YZ17]** X. Yuan, S.-W. Zhang, *The arithmetic Hodge index theorem for adelic line bundles* (the global
  polarization Abboud localizes; the repo's "nearest proven polarization"). **[YZ23]** Yuan-Zhang, *adelic
  line bundles over quasi-projective varieties* (the metrised-bundle-as-limit framework Abboud runs on).
- **[CD12]** A. Chambert-Loir, A. Ducros, *Formes différentielles réelles et courants sur les espaces de
  Berkovich* (non-archimedean pluripotential theory; the $dd^c$ / Poincaré-Lelong machinery).
- **[CM21]** *inferred* Chen-Moriwaki (the local-intersection-number reference "we follow §3.6 of [CM21]",
  Section 2.8). Likely the same lineage as the companion flagged paper **Chen-Moriwaki 2207.02033**; worth
  pinning when that note is written.
- **[Gub98]** W. Gubler, *Local heights of subvarieties over non-archimedean fields* (model-function density,
  Prop. 2.3/2.4). **[Ber12]** Berkovich (spaces). **[Laz04]** Lazarsfeld, *Positivity in Algebraic Geometry*
  (volumes, big/nef, Thm 2.1). **[Mor16]** Moriwaki (Green functions convention).
- **[Abb24]** *inferred* M. Abboud, the affine-surface-automorphism / shared-periodic-points paper that
  consumes Theorem C. The paper's actual application domain (arithmetic dynamics).

## Cross-references (repo)

- The object's home bracket: [#131 Arakelov-face probe](../../../experiments/arithmetic_geometric/2L_arakelov_face_probe.md)
  and [#132 construction attempt](../../../experiments/arithmetic_geometric/2M_arakelov_construction_attempt.md)
  (Faltings-Hriljac/Yuan-Zhang = per-surface polarization, dies at the base; M4 is not what it lacks).
- The two-facet gap this paper sits inside: [`../sourcing_gap_r1.md`](../sourcing_gap_r1.md) (facet A / R1
  sourcing vs facet B / M4 polarization; this paper is pure facet B, single place).
- The verdict convention and the flag that named this paper: [`rh_corpus_2021-2026_vs_frontier.md`](rh_corpus_2021-2026_vs_frontier.md)
  (lines 40, 57) and [`../../literature_survey/rh_arch2_supplement.md`](../../literature_survey/rh_arch2_supplement.md).
- The polarity master-discriminator: [`../breadth_program.md`](../breadth_program.md) lines 74-80
  (unconditional Hodge-Riemann-type signatures can never flag a violation).
- The three still-un-noted companions in the same math.AG cluster: He 2512.01811, Connes-Consani 2606.06604,
  Chen-Moriwaki 2207.02033 (the [CM21]-lineage local-intersection reference).
