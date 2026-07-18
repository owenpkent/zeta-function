# Reading notes: Chen-Moriwaki, *Hilbert-Samuel formula and positivity over adelic curves* (arXiv:2207.02033, 5 Jul 2022)

> SURVEYOR reading note for one of the four "closest live-M4 papers still lacking a reading note"
> flagged in [`PHASE_STATE.md`](../../../PHASE_STATE.md) line 9 / LEARNINGS #155 (Abboud 2503.14099,
> He 2512.01811, Connes-Consani 2606.06604, Chen-Moriwaki 2207.02033). This is the Chen-Moriwaki
> *Arakelov-geometry-over-adelic-curves* orbit: the abstract framework that packages a global field's
> places into a single measure space and does Arakelov intersection theory over it. Positioned against
> the repo's Arakelov-face findings ([`2L_arakelov_face_probe.md`](../../../experiments/arithmetic_geometric/2L_arakelov_face_probe.md),
> LEARNINGS #131; [`2M_arakelov_construction_attempt.md`](../../../experiments/arithmetic_geometric/2M_arakelov_construction_attempt.md),
> LEARNINGS #132) and scored against the S1-S7 skeleton
> ([`breadth_program.md`](../breadth_program.md) lines 55-80), R1 ([`sourcing_gap_r1.md`](../sourcing_gap_r1.md)),
> and the #156 WATCH clause. Verification status is tagged per claim throughout.

## Verified bibliographic header

- **Title:** *Hilbert-Samuel formula and positivity over adelic curves.* [VERIFIED-BY-FETCH: abstract page + PDF, two independent fetches agree]
- **Authors:** Huayi Chen, Atsushi Moriwaki. [VERIFIED-BY-FETCH]
- **arXiv:** 2207.02033, submitted 5 July 2022. [VERIFIED-BY-FETCH]
- **Subjects:** primary math.AG (Algebraic Geometry), cross-list math.NT (Number Theory). MSC primary 14G40 (Arakelov theory / heights), secondary 11G50 (heights). [VERIFIED-BY-FETCH]
- **Abstract (verbatim, VERIFIED-BY-FETCH, both fetches identical):** "We establish, in the setting of Arakelov geometry over adelic curves, an arithmetic Hilbert-Samuel theorem describing the asymptotic behaviour of the metrized graded linear series of an adelic line bundle in terms of its arithmetic intersection number. We then study positivity conditions of adelic line bundles."
- **Does NOT mention** the Riemann zeta function, L-functions, Frobenius, or the Riemann Hypothesis anywhere in the abstract or (per the PDF fetch) the body. [VERIFIED-BY-FETCH on abstract; PDF-SUMMARIZER-CONFIRMED on body]
- **Reading depth (honesty flag):** This note is written from the verified abstract plus two WebFetch passes over the arXiv abstract page and the 946 KB PDF. The main-theorem statements below are at the abstract + framework level, not a line-by-line proof read. Any claim resting only on the PDF-summarizer pass (not corroborated by the abstract) is tagged [PDF-SUMMARIZER-REPORTED, NOT LINE-VERIFIED]. The scorecard conclusion is polarity-robust and does not depend on those tagged claims.

## One-line takeaway

This is the most general **fixed-base** Arakelov intersection theory: an arithmetic Hilbert-Samuel
formula and a bigness/nef/pseudo-effective positivity theory for adelic line bundles on a projective
variety over a single adelic curve $S$. It generalizes the **base** of Arakelov geometry (from
$\mathrm{Spec}(\mathcal{O}_K)$ to an arbitrary adelic curve) but supplies **no self-product, no
diagonal, no Frobenius correspondence, and no contact with zeta**. It is the general engine of the
Yuan-Zhang / Moriwaki fixed-scheme arithmetic Hodge-index bracket that 2L already scored as
**NODE-fh-too-local**. Direct answer to the load-bearing question: **it does NOT supply the Arakelov
BASE** ($\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z}) + \Gamma_S$) that #131/#132
identified as the gap.

## What it does

Two parts, matching the two abstract sentences.

**Part 1: the arithmetic Hilbert-Samuel theorem.** For an adelic line bundle $\overline{L}$ on a
projective variety $X$ of dimension $d$ over an adelic curve $S$ with base field $K$, the paper gives
the asymptotic of the **metrized graded linear series** $\bigoplus_n H^0(X, L^{\otimes n})$ equipped
with its sup-metrics (or the arithmetic degrees / positive-degree of the induced adelic vector
bundles). The leading term of the arithmetic $\chi$ / positive-degree is governed by the top
**arithmetic self-intersection number** $(\overline{L})^{d+1}$, i.e. the arithmetic volume
$\widehat{\mathrm{vol}}(\overline{L}) = (\overline{L})^{d+1}$ in the nef/ample regime, with the
$(d+1)!/n^{d+1}$ normalization. This is the adelic-curves analogue of the Gillet-Soule / Abbes-Bouche
/ Zhang arithmetic Hilbert-Samuel theorem, ported into the Chen-Moriwaki abstract framework.
[FRAMEWORK-LEVEL, consistent with the verified abstract and the authors' program; exact normalization BIBLIOGRAPHIC-ONLY]

**Part 2: positivity conditions of adelic line bundles.** With the Hilbert-Samuel / arithmetic-volume
functional in hand, the paper studies the standard positivity hierarchy: **big** (positive arithmetic
volume), **pseudo-effective** (limit of effective / a boundary condition), **nef** (non-negative
intersection against curves), and arithmetic ampleness, plus the criteria relating them
(arithmetic Nakai-Moishezon / Fujita-type; bigness $\iff \widehat{\mathrm{vol}} > 0$). [FRAMEWORK-LEVEL,
consistent with the verified abstract's second sentence]

**On an arithmetic Hodge-index / signature statement:** the PDF-summarizer pass reported "a Hodge-index
type theorem with signature $(1, n-1)$ for the quadratic form defined by adelic intersection products."
[PDF-SUMMARIZER-REPORTED, NOT LINE-VERIFIED] The abstract-page fetch could **not** corroborate a Hodge-index
theorem in this specific paper; the abstract advertises only Hilbert-Samuel + the bigness/nef/pseudo-effective
positivity hierarchy. Chen-Moriwaki's broader adelic-curves program (their 2020 Springer LNM 2258 book;
Moriwaki's earlier arithmetic Hodge-index work, cited in 2L as arXiv:1010.1599) **does** contain arithmetic
Hodge-index theorems, so a Hodge-index-flavored statement here is bibliographically plausible, but its
presence in *this* paper is not confirmed by me. **The scorecard below is robust either way:** whether the
carried positivity is a full $(1,n-1)$ Hodge index or "only" bigness/nef, it is unconditional per-variety
over a fixed base, which is the load-bearing structural fact.

## Central object

An **adelic curve** $S = (K, (\Omega, \mathcal{A}, \nu), (\lvert\cdot\rvert_\omega)_{\omega\in\Omega})$:
a field $K$, a measure space $(\Omega, \mathcal{A}, \nu)$, and for each $\omega$ an absolute value
$\lvert\cdot\rvert_\omega$ on $K$, such that the family integrates to a product-formula-like global
structure (Chen-Moriwaki 2020). This is a **measure-theoretic packaging of the places of one global
field** into a single "arithmetic base curve." The intersection theory, heights, and positivity live on
a projective variety $X$ **over** $K$, i.e. **over** the adelic base $S$.

The three structural facts that fix the scorecard, all [VERIFIED-BY-FETCH on the PDF pass, and forced by
the definition of an adelic curve]:

1. **$S$ is a fixed base field $K$**, not a self-product. "This is a fixed field framework, not involving
   diagonal embeddings or self-products."
2. **No product of two arithmetic schemes.** "The document does not construct
   $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$ or diagonal embeddings. It works entirely
   within a single arithmetic curve framework without correspondence machinery."
3. **No Frobenius / correspondence and no zeta.** No $\mathrm{Frob}_p$, no $\Gamma_S$, no L-function.

The adelic curve **generalizes the base** ($\mathrm{Spec}(\mathcal{O}_K) \rightsquigarrow$ arbitrary
adelic curve), but the generalized base is still a **base**, and $X$ has relative dimension $\ge 1$ over
it. In 2L's language this is exactly "a curve OVER $\mathrm{Spec}(\mathbb{Z})$, relative dim 1, lacks the
self-product": the object is the ambient framework of the **NODE-fh-too-local** bracket, not an escape from it.

## Scorecard: S1-S7 + R1 + K1 (central object vs the repo M4 skeleton)

Skeleton per [`breadth_program.md`](../breadth_program.md) lines 59-80; S6 (contingency) is the master
discriminator, S7 non-circularity. R1 per [`sourcing_gap_r1.md`](../sourcing_gap_r1.md).

| Slot | What it demands | Chen-Moriwaki 2207.02033 | Verdict |
|---|---|---|---|
| **S1** Lefschetz operator $L$ (deg $+1$, hard Lefschetz) | a cup-by-ample operator with HL | YES-analogue: cup by an arithmetically ample adelic line bundle gives the Lefschetz-style operator on arithmetic Chow groups. Geometry-over-a-fixed-base version. | HAS (fixed-base) |
| **S2** primitive decomposition $V=\bigoplus L^j P$ | a primitive part orthogonal to the ample class | YES-analogue in the fixed-variety setting (the ample-orthogonal complement). | HAS (fixed-base) |
| **S3** duality / pairing $Q$ (the functional equation) | a perfect intersection pairing | YES as the arithmetic intersection pairing, but it is the **geometric intersection form of a fixed variety**, NOT the functional-equation pairing of $\zeta$. | HAS (wrong $Q$: geometric, not the FE) |
| **S4** trace datum $t$ (the Frobenius eigenvalue the sign must see) | a spectral parameter | **NO.** There is no Frobenius, no eigenvalue, no spectral $t$. The parameters are heights / volumes. This is the critical absence. | ABSENT |
| **S5** polarization: $Q$ definite on each primitive piece (signature $(1,n-1)$) | a definite / signature statement | YES-analogue **if** the Hodge-index claim holds (the fixed-variety arithmetic Hodge index / negative-definiteness on the primitive part); at minimum bigness/nef positivity. [Hodge-index specific: PDF-SUMMARIZER-REPORTED] | HAS (fixed-variety, unconditional) |
| **S6** right polarity: S5 is **contingent** on $t$ (flips off the critical locus) | the sign must FLIP when a parameter leaves the line | **NO.** The arithmetic positivity is **unconditional**: it holds for the fixed variety and does not flip on any spectral parameter (there is no spectral parameter). This is the #125/#132 "unconditionally definite = wrong polarity" bracket. | **FAILS (master discriminator)** |
| **S7** non-circularity (proved without inputting the answer) | not assuming the zeros | Vacuously YES: proved by unconditional Arakelov geometry, no zeros input. But also zeta-blind: it never touches the zeros to be non-circular about. | PASS (vacuous / zeta-blind) |
| **R1** face: does it supply the missing BASE ($\mathrm{Spec}(\mathbb{Z})\times\mathrm{Spec}(\mathbb{Z}) + \Gamma_S$)? | a genuine self-product with diagonal / Frobenius correspondence | **NO.** It generalizes the base to an arbitrary adelic curve, but that is a fixed base, not a self-product; no diagonal, no $\Gamma_S$. Stays fixed-scheme / per-surface. | **DOES NOT SUPPLY THE BASE** |
| **K1** circularity (does it input the zeros?) | no zeta zeros consumed | K1-clean but zeta-untouched: it neither consumes nor discriminates the zeros. | CLEAN but INERT |
| **#156** WATCH clause: index-set-preserving AND non-endomorphism-shaped | a candidate R1 filler operator | Index-set-preserving (all places of $K$ packaged as $\Omega$) and non-endomorphism-shaped (an intersection/measure framework, not a ring endomorphism), BUT supplies **no operator / Frobenius at all**, so it is not an R1 filler candidate. It is the base+intersection half, not the missing endomorphism. | Not the binding screen (supplies no operator) |

## The M4-specific question, answered

> Is the polarization it carries the **CONTINGENT** $(1,n-1)$ Weil/Rosati signature that flips off-line,
> or the **UNCONDITIONAL** Hodge-index positivity of a single arithmetic surface (which #132 showed is
> the wrong, per-motive object)?

**The unconditional one.** The arithmetic positivity in this paper (bigness/nef/pseudo-effective, and
whatever Hodge-index statement it carries) is a theorem about a **fixed** projective variety over a
**fixed** adelic base. It does not flip on a spectral parameter, because there is no spectral parameter
(S4 absent). This is precisely the object 2L/#131 and 2M/#132 identified as **NODE-fh-too-local**:
"Faltings-Hriljac / Yuan-Zhang is unconditionally definite (cannot flip) = wrong polarity" (#125), and
"realize (Frobenius spectrum = zeros) and polarize (the arithmetic Chow height pairing) sit on
orthogonal cohomologies even when both are present" (#132). Chen-Moriwaki 2207.02033 is the general
framework for the **polarize** side of that split; it carries no **realize** side (no Frobenius spectrum
= zeros) and no base to attach polarization to zeta's actual zeros. It is the per-surface / per-motive
positivity object, not the contingent Weil/Rosati signature M4 requires.

## Verdict: ADJACENT-WATCH (on the KNOWN-TO-REPO boundary)

- **The specific positivity object is KNOWN-TO-REPO.** The adelic-curve arithmetic Hilbert-Samuel +
  bigness/nef/Hodge-index positivity is the most general packaging of the Yuan-Zhang (Math. Ann. 367,
  2017) and Moriwaki (arXiv:1010.1599) fixed-scheme arithmetic Hodge index, both already scored as
  **NODE-fh-too-local** in [`2L`](../../../experiments/arithmetic_geometric/2L_arakelov_face_probe.md)
  section 4 (the 2026-frontier table) and named as "the natural index machinery on such a carrier" in
  2L section 3. The repo already lists "Chen-Moriwaki / Yuan-Zhang adelic Hodge index" explicitly as a
  B-credible-but-no-free-lunch accident candidate ([`rh_solved_by_accident.md`](../rh_solved_by_accident.md),
  LEARNINGS #113/#155 era). So the bracket is already scored.
- **The ADJACENT-WATCH aspect** is the generalization direction: the adelic-curves framework is the
  natural, most-general **home** in which 2L section 3's "strictly-construction-weaker sufficient
  object" (a single arithmetic carrier over an **auxiliary** curve/base, with Chen-Moriwaki / Yuan-Zhang
  intersection machinery applied directly) would be **written**. If a future construction produces a
  carrier whose Frobenius/flow spectrum on an odd cohomology equals zeta's zeros with a definite
  primitive cup form, this is the intersection-theory language it would be stated in. So keep it on the
  watch-list as the ambient framework, not as a mover of the kernel.
- **NOT NEW-LOAD-BEARING.** To cross that threshold the paper would have to supply either (a) the base
  ($\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z}) + \Gamma_S$, the self-product / Frobenius
  correspondence) or (b) a **contingent** polarization that flips off-line. It supplies **neither**. It
  fails the S6 master discriminator (unconditional, wrong polarity) and the R1 base question (fixed base,
  no self-product). This matches the honest prior: the 2026 Arakelov frontier is fixed-scheme
  (Yuan-Zhang / Moriwaki / CGHX), and this 2022 paper predates and sits inside that same fixed-scheme
  bracket.

## Direct statement: does it supply the Arakelov BASE that #131/#132 named as the gap?

**NO.** #131 (2L) localized the Arakelov face as dying "not at facet A (R1) and not at facet B
(M4-positivity, a theorem per surface), but at the BASE: the nonexistent product surface
$\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$ and its Frobenius correspondence
$\Gamma_S$." Chen-Moriwaki 2207.02033 **generalizes the base** (from a number-field ring of integers to
an arbitrary adelic curve) but does **not** build the self-product: it "works entirely within a single
arithmetic curve framework without correspondence machinery" and "does not construct
$\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$ or diagonal embeddings"
[VERIFIED-BY-FETCH on the PDF pass]. A more general **base** is not a **self-product of the base** plus a
diagonal; those are exactly the missing ingredients, and this paper leaves them missing. The BSD
severance (#131 section 3) is untouched: with no Frobenius correspondence and no L-function contact, the
paper never even enters the channel where Faltings-Hriljac positivity would attach to zeta's zeros.

## Discrepancy log

- **Apparent tension (a refinement, not a contradiction), flagged not resolved.**
  [`rh_solved_by_accident.md`](../rh_solved_by_accident.md) (Session 010, LEARNINGS line 173) lists
  "Chen-Moriwaki / Yuan-Zhang adelic Hodge index" in its **B-credible tier** ("right KIND of tool, all
  pass D-H"). The **later** dossiers 2L/#125/#131 and 2M/#132 sharpen this to "the fixed-scheme
  arithmetic Hodge index is **unconditionally** definite = **wrong polarity** (cannot flip), the
  RH-relevant content delegated to the unbuilt $\Gamma_S$." These are reconcilable: "right KIND of
  object" (a genuine intersection signature, D-H-unbuildable, not archimedean-only) and "wrong polarity
  as literally stated" (unconditional per-scheme) are both true, and rh_solved_by_accident.md already
  records "no-free-lunch: the residual step is RH-equivalent in every case." I flag it as a wording
  refinement the surveyor pass should carry forward, not a live contradiction, and I do not resolve it
  further (that is ADVERSARY/VERIFIER territory).
- **No numerical or definitional disagreement** between this paper and the repo's Arakelov-face
  analyses. The paper is off the zeta target and internally consistent with the repo's fixed-scheme
  classification of the adelic Arakelov machinery.

## References to follow up (bibliographic-only unless tagged)

- Chen-Moriwaki, *Arakelov geometry over adelic curves*, Springer LNM 2258 (2020): the foundational
  framework; the natural place a Hodge-index-over-adelic-curves theorem is stated. [BIBLIOGRAPHIC-ONLY]
- X. Yuan, S. Zhang, *The arithmetic Hodge index theorem for adelic line bundles*, Math. Ann. 367 (2017):
  the fixed-scheme predecessor 2L scored as NODE-fh-too-local; 2207.02033 is its abstract-framework
  generalization. [Already in-repo via 2L]
- A. Moriwaki, arXiv:1010.1599 (higher-dim arithmetic Hodge index, Dirichlet-unit-theorem analogue on a
  fixed variety): the other NODE-fh-too-local row in 2L. [Already in-repo via 2L]
- Chen-Moriwaki follow-ups on positivity / bigness over adelic curves (arithmetic Fujita approximation,
  arithmetic Nakai-Moishezon), and any adelic-curves arithmetic Hodge-index paper, to pin whether the
  $(1,n-1)$ statement the PDF-summarizer reported lives in 2207.02033 or a companion. [WATCH]

## What this enables / what remains open

- **For BUILDER:** this is the intersection-theory **vocabulary** for the "strictly-construction-weaker
  sufficient object" of [`2L`](../../../experiments/arithmetic_geometric/2L_arakelov_face_probe.md)
  section 3 (a single carrier over an auxiliary adelic base, Yuan-Zhang / Chen-Moriwaki index applied
  directly). It does **not** supply the missing pieces: the carrier must still host an odd cohomology
  whose Frobenius/flow spectrum equals zeta's zeros (R1 / S4), and the polarization must be the
  **contingent** one (S6). Use the framework to *state* a candidate, do not mistake the framework for a
  candidate.
- **For ADVERSARY:** the paper is K2-clean by non-mimicry (no Euler product, no motive, so Davenport-
  Heilbronn cannot enter), but the pass is **inert**, not informative: with no zeta contact and no
  contingent flip, there is nothing for the D-H discipline to discriminate. Any future claim that routes
  zeta positivity through this framework should be attacked at S4 (where is the Frobenius spectrum?) and
  S6 (does the signature flip, and on what?), the same two slots 2M's three fronts walled at.
- **For SYNTHESIZER:** file under the [`reading_notes` section 06](README.md) (Intersection theory /
  Hodge index, Direction 8 signature) as the general-framework companion to the Hartshorne / AHK /
  Voisin rows, and record the verdict in the fixed-scheme column of the Arakelov-face scorecard. It
  moves nothing on the open kernel; it names the ambient framework the base-construction would inhabit.
- **Open, unchanged by this paper:** the BASE ($\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})
  + \Gamma_S$, = PROP-global bundled with R1), the contingent polarization (M4 / S6), and the
  realize-vs-polarize orthogonality (#132). This 2022 paper is a fixed-base datapoint that confirms,
  rather than moves, the #131/#132 verdict.

## Connections

- [`2L_arakelov_face_probe.md`](../../../experiments/arithmetic_geometric/2L_arakelov_face_probe.md) (#131): the Arakelov face dies at the BASE; Yuan-Zhang / Moriwaki = NODE-fh-too-local (the bracket this paper generalizes).
- [`2M_arakelov_construction_attempt.md`](../../../experiments/arithmetic_geometric/2M_arakelov_construction_attempt.md) (#132): the realize-vs-polarize orthogonality; the construction-side three-front convergence on the same base gap.
- [`sourcing_gap_r1.md`](../sourcing_gap_r1.md): the two variety-gated facets (R1 sourcing + M4 polarization) and the #156 index-set-preserving/non-endomorphism WATCH clause.
- [`breadth_program.md`](../breadth_program.md) lines 55-80: the S1-S7 skeleton; S6 contingency as the master discriminator.
- [`rh_solved_by_accident.md`](../rh_solved_by_accident.md): the B-credible listing of "Chen-Moriwaki / Yuan-Zhang adelic Hodge index" the discrepancy log refines.
- [`Connes-2026-RH-Past-Present-Letter.md`](Connes-2026-RH-Past-Present-Letter.md): style template for this note.
