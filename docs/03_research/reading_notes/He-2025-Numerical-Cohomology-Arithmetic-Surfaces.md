# Reading notes: Wei He, *Numerical cohomology for arithmetic surfaces and applications* (arXiv:2512.01811v1, 1 Dec 2025)

> Reading note for one of the four closest live-M4 papers flagged as lacking coverage in the 2021-2026
> Architecture-2 supplement (PHASE_STATE 2026-07-03 update / LEARNINGS #155; the other three: Abboud
> 2503.14099, Connes-Consani 2606.06604, Chen-Moriwaki 2207.02033). Screened against the M4 skeleton
> ([`../breadth_program.md`](../breadth_program.md) §1, S1-S7), the R1 sourcing face
> ([`../sourcing_gap_r1.md`](../sourcing_gap_r1.md)), and the #156 WATCH clause
> ([`../model_theoretic_frobenius.md`](../model_theoretic_frobenius.md) §8). Verdict lands where the repo
> already places the whole Arakelov face: the `NODE-fh-too-local` bracket of
> [`../spec_z_cohomology_landscape.md`](../spec_z_cohomology_landscape.md). Tags below: **[VF]** =
> verified by fetch (arXiv abstract page + v1 + HTML), **[VF-ext]** = fetched HTML but read through the
> extraction model (verbatim fidelity of formulas not independently confirmed), **[BIB]** =
> bibliographic / structural inference, not read at the source.

## Verified bibliographic header

- **Title [VF]:** *Numerical cohomology for arithmetic surfaces and applications.*
- **Author [VF]:** Wei He (single author).
- **arXiv [VF]:** 2512.01811, v1 submitted 1 Dec 2025 (v1 revised 2 Dec 2025), 14 pages.
- **Subjects [VF]:** math.NT (primary), math.AG (cross-list).
- **Abstract [VF, verbatim]:** "In this paper, we introduce numerical cohomology for arithmetic
  surfaces, which leads to an absolute version of arithmetic Riemann-Roch formula. As an application, we
  derive an upper bound for the self-intersection number of relative dualizing sheaf in terms of
  successive minima with respect to $L^2$-norm. The result has the geometric analogue that the slopes of
  the Harder-Narasimhan filtration of relative dualizing sheaf provide an upper bound for
  self-intersection number. Suppose that the arithmetic surface admits a section and has generic fiber of
  genus at least two, we obtain a refined upper bound for the self-intersection number, which is governed
  by the topological and arithmetic information of the section."

**Orbit correction.** The launch brief expected "arithmetic geometry / Spec(Z) cohomology / L-function
positivity." Verified [VF], the paper is **Arakelov intersection theory on arithmetic surfaces**: bounding
the self-intersection $(\omega_{\mathcal{X}/\mathcal{O}}, \omega_{\mathcal{X}/\mathcal{O}})$ of the
relative dualizing sheaf, in the effective-Bogomolov / Parshin-Szpiro-Zhang tradition. It is NOT about
$\mathrm{Spec}(\mathbb{Z})$-cohomology in the Connes-Consani sense, NOT about $\zeta$/L-functions, and NOT
about Weil positivity. The word "absolute" is a **false friend** with Connes-Consani "absolute geometry of
$\mathrm{Spec}\,\mathbb{Z}$ over $\mathbb{F}_1$" (2606.06604) and with their "Riemann-Roch for
$\mathrm{Spec}\,\mathbb{Z}$" (2205.01391): here "absolute" means the Deligne / Gillet-Soulé
determinant-of-cohomology sense (a self-contained arithmetic Euler characteristic that folds the
regularized Laplacian determinant into $\chi$, base-field-independent), NOT $\mathbb{F}_1$-descent. Its
arithmetic surface is a **2-dimensional** scheme (a curve over $\mathrm{Spec}\,\mathcal{O}_F$), not
$\mathrm{Spec}\,\mathbb{Z}$ treated as a 1-dimensional arithmetic curve.

## One-line takeaway

He introduces a "numerical cohomology" $h^i_{\mathcal{X}}(\mathcal{L})$ bookkeeping for Hermitian line
bundles on an arithmetic surface, packages it into an **absolute arithmetic Riemann-Roch** identity (Thm
1.1) whose right side is the Arakelov self-intersection $(\mathcal{L}, \mathcal{L}\otimes\omega^\vee)$, and
uses it to prove **upper bounds** on the canonical self-intersection $\omega^2$ via $L^2$ successive minima
and Harder-Narasimhan slopes of $f_*\omega$. This is a fresh, technically substantive contribution to the
single-surface Arakelov line, and it is **structurally exactly where the repo already places that line**:
a proven per-surface intersection theory with an **unconditional** (hence wrong-polarity) Hodge-index
background, on a base that is a curve over the arithmetic ring rather than the
$\mathrm{Spec}(\mathbb{Z})\times\mathrm{Spec}(\mathbb{Z})$ the Weil lift needs. No $\zeta$, no Frobenius, no
contingent signature.

## What it does (central object + main theorems)

**Central object [VF-ext].** An arithmetic surface $f: \mathcal{X}\to\mathrm{Spec}\,\mathcal{O}_F$ (regular,
projective, flat; generic fiber a smooth curve) with a Hermitian line bundle $\mathcal{L}$. He defines a
graded **numerical cohomology**:
- $h^0_{\mathcal{X}}(\mathcal{L}) := h^0_{\mathcal{O}}(f_*\mathcal{L})$ (Arakelov $h^0$ of the pushforward,
  i.e. a Bost/Gillet-Soulé $L^2$-lattice-point count of small sections),
- $h^2_{\mathcal{X}}(\mathcal{L}) := h^0_{\mathcal{X}}(\omega_{\mathcal{X}}\otimes\mathcal{L}^\vee)$ (the
  Serre-dual slot),
- $h^1_{\mathcal{X}}(\mathcal{L})$ via the Leray spectral sequence + relative Serre duality (a combination
  of pushforward Arakelov $h^0$ terms and $\tfrac12\deg\det H^1$ torsion corrections),
- $\chi_{\mathcal{X}}(\mathcal{L}) = h^0 - h^1 + h^2$.

**Theorem 1.1 (absolute arithmetic Riemann-Roch) [VF-ext, formula not verbatim-confirmed].**
$$\chi_{\mathcal{X}}(\mathcal{L}) + \tfrac12\log\det\Delta_{\mathcal{L},\infty}
= \tfrac12\,(\mathcal{L},\mathcal{L}\otimes\omega_{\mathcal{X}}^\vee)
+ \big(\chi_{\mathcal{X}}(\mathcal{O}_{\mathcal{X}}) + \tfrac12\log\det\Delta_{\mathcal{O},\infty}\big),$$
with $(\cdot,\cdot)$ the Arakelov intersection pairing and $\det\Delta$ the regularized Laplacian
determinant at the archimedean fibers. This is the Arakelov/Faltings arithmetic Riemann-Roch reorganized
so the Euler characteristic is "absolute" (self-contained, with the analytic torsion inside $\chi$).

**Theorem 1.3 (self-intersection bound via successive minima) [VF-ext].**
$(\omega_{\mathcal{X}/\mathcal{O}}, \omega_{\mathcal{X}/\mathcal{O}}) \le
-12[F:\mathbb{Q}]\sum_{i=1}^{2g-2}\log\lambda_i + C$, where $\lambda_i$ are the successive minima of
$f_*\omega_{\mathcal{X}/\mathcal{O}}$ w.r.t. the $L^2$-norm, $g\ge 2$ the generic-fiber genus, and $C$
absorbs discriminant/Noether-formula terms. The stated geometric analogue: HN slopes of $f_*\omega$ bound
$\omega^2$ from above.

**Theorem 1.5 (refined bound with a section) [VF-ext].** If $\mathcal{X}$ has a section $P$ and $g\ge 2$,
a refined upper bound governed by the topological/arithmetic data of $P_\infty$.

**Inputs consumed [VF-ext / BIB]:** the Arakelov intersection pairing; relative Serre duality; the
Harder-Narasimhan filtration and successive minima of $f_*\omega$ ($L^2$-norm); regularized Laplacian
determinants (analytic torsion); genus, field discriminant, Noether formula. References [VF] (38 items)
are the standard arithmetic-intersection corpus: Arakelov, Faltings (*Calculus on arithmetic surfaces*),
Deligne, Gillet-Soulé, Szpiro, Parshin, Zhang, plus recent Faltings-invariant work (Wilms, Bost). This is
the **effective-Bogomolov / bounding-$\omega^2$** lineage.

**Absences, checked [VF-ext, negative; caveat below].** The HTML extraction found no occurrence of the
Riemann Hypothesis, $\zeta$, L-functions, Frobenius, or Weil/Hodge-Riemann positivity, and no stated Hodge
index / Faltings-Hriljac *theorem* (the Arakelov pairing is used, but its negative-definiteness on the
degree-0 part is not invoked as a headline result). Honesty caveat: the negative was produced by the
extraction model over the HTML, so a citation to Faltings-Hriljac/Moriwaki/Yuan-Zhang in the 38-item
bibliography is plausible even if no positivity *theorem* is stated in the body; the structural point below
does not depend on the exact citation set.

## The scorecard (M4 skeleton S1-S7 + R1 + K1 + #156)

Scored against [`../breadth_program.md`](../breadth_program.md) §1. "n/a-not-engaged" means the paper does
not touch the RH-relevant slot at all (so the constraint is neither satisfied nor violated by it).

| Slot | Question | Verdict for He 2512.01811 |
|---|---|---|
| **S1** Lefschetz | hard-Lefschetz operator $L$ on a graded space? | **NO.** Arakelov intersection theory on a 2-dim scheme; no Lefschetz operator with the hard-Lefschetz iso is developed. Cup-with-arithmetic-ample exists on the face but is not used; the engine is Riemann-Roch + successive minima. [VF-ext] |
| **S2** primitive decomp | $V=\bigoplus L^j P$? | **n/a-not-developed.** The face's primitive part (degree-0 / $\widehat{\mathrm{Pic}}^0$) exists via Faltings-Hriljac but this paper does not invoke a primitive decomposition. [BIB] |
| **S3** duality / pairing (FE) | perfect $(-1)$-symmetric pairing = the functional equation? | **YES, but wrong object.** The Arakelov intersection pairing + relative Serre duality are present and central (Thm 1.1). But this is the duality of the arithmetic *surface* (Arakelov RR / Serre duality), NOT the functional equation of $\zeta$. Perfect pairing on the wrong base. [VF-ext] |
| **S4** trace datum $t$ | the Frobenius eigenvalue / spectral parameter the sign must see? | **NO.** The invariants are successive minima, HN slopes, genus, discriminant: geometric-arithmetic data of a fixed surface. No Frobenius eigenvalue, no zeta-zero parameter $t$. The object does not even realize $\zeta$ as a trace. [VF-ext] |
| **S5** polarization | $Q$ definite of fixed sign on each primitive piece? | **Background only, not produced.** The ambient face has one (Faltings-Hriljac: Arakelov pairing negative-definite on degree-0). This paper produces one-sided *inequalities* ($\omega^2 \le \ldots$) in the Bogomolov tradition, not a signature/Hodge-Riemann statement. [VF-ext / BIB] |
| **S6** RIGHT POLARITY | is (S5) **contingent** on $t$ (flips off the critical locus), vs **unconditional**? | **WRONG POLARITY.** The inherited arithmetic Hodge index (Faltings-Hriljac) is **unconditional**: negative-definite on degree-0 for *every* arithmetic surface, always; it never flips to flag a violation. The self-intersection bounds are likewise unconditional inequalities. This is the master-discriminator failure (breadth §1). [BIB, structural] |
| **S7** non-circularity | are (S5)-(S6) proved without inputting the zeros? | **n/a-vacuous.** No RH-relevant claim is made, so nothing consumes the zeros; non-circularity holds trivially by non-engagement, and buys nothing. [VF-ext] |
| **R1 face** | Frobenius-like correspondence with isolated prime-indexed fixed points on genuine $\mathrm{Spec}(\mathbb{Z})\times\mathrm{Spec}(\mathbb{Z})$, or only zeta-as-trace? | **NEITHER.** No Frobenius correspondence, no prime-indexed fixed points, no product base. The surface is a curve over $\mathrm{Spec}\,\mathcal{O}_F$ (a *single* arithmetic surface), not $\mathrm{Spec}(\mathbb{Z})^{\times 2}$ (PROP-global, #131). It does not even realize $\zeta$ as a trace. R1 not supplied. [VF-ext / BIB] |
| **K1** | does any RH-relevant claim consume RH / the zeros? | **n/a-clean by non-engagement.** No RH claim, so no circularity; but also no RH-relevant output. [VF-ext] |
| **#156 WATCH** | index-set-preserving AND non-endomorphism-shaped R1 filler? | **not triggered.** The paper proposes no R1 filler. Its object is a fixed geometric surface (all primes present, no ring endomorphism moving arithmetic), but it carries no Frobenius-shaped mover at all, so the two-conjunct clause is inapplicable. [BIB] |

**Where the whole card lives in the repo.** This is a new 2025-12 entrant on the existing
`NODE-fh-too-local` bracket of [`../spec_z_cohomology_landscape.md`](../spec_z_cohomology_landscape.md)
(the Faltings-Hriljac single-surface arithmetic Hodge index row: "✗ (no $\zeta$) / ◑ (wrong dim) / ◑
**PROVEN, but single surface** / vacuous / missing = the **product** $\mathrm{Spec}(\mathbb{Z})\times
\mathrm{Spec}(\mathbb{Z})$ + Frobenius $\Gamma_S$"). He's paper adds machinery to that node (a numerical
cohomology, an absolute RR, sharper $\omega^2$ bounds) without moving any of its five columns.

## Verdict: KNOWN-TO-REPO

The repo's standing analysis of the Arakelov face (arch2 supplement tie-in; landscape `NODE-fh-too-local`)
is: it "HAS a carrier AND a proven per-surface polarization (Faltings-Hriljac / Yuan-Zhang) but dies at the
BASE (no $\mathrm{Spec}(\mathbb{Z})\times\mathrm{Spec}(\mathbb{Z})$)." He 2512.01811 instantiates this
exactly: a carrier (numerical cohomology + absolute RR on a single arithmetic surface), an intersection
duality (S3), a background unconditional polarization (S5 wrong-polarity via S6), no zeta trace (S4), no
product base (R1). Every load-bearing gap the repo attributes to the face is present and unaddressed.

**Skeptical re-read for a NEW-LOAD-BEARING escape (per [`../researcher_mindset.md`](../researcher_mindset.md)).**
Three candidate upgrades were tested and each fails:
1. *Could "absolute arithmetic RR" be the $\mathbb{F}_1$/absolute-geometry step the repo wants?* No: "absolute"
   is the determinant-of-cohomology sense (analytic torsion folded into $\chi$), a bookkeeping normalization
   over the actual number ring, not $\mathbb{F}_1$-descent nor a product base. False friend, disambiguated above.
2. *Could the numerical cohomology be a genuinely new right-polarity signature?* No: it produces one-sided
   $\omega^2$ inequalities and an unconditional intersection identity; nothing is contingent on a spectral
   parameter, nothing flips (S6 fails structurally).
3. *Could it supply R1 (a variety-free pure-$\sqrt q$ carrier or a genuine product/diagonal)?* No: it is
   entirely a single-surface, zeta-blind, Frobenius-free construction; it does not even reach the
   zeta-as-trace tier, let alone the $\mathrm{Spec}(\mathbb{Z})^{\times 2}$ + $\Gamma_S$ tier that R1/M4
   require.

The verdict survives the skeptical pass: **KNOWN-TO-REPO** (Arakelov-face `NODE-fh-too-local`).

## What it supplies for M4/R1 that the repo lacks

- **For M4 (the polarization / S5-S6-S7):** nothing load-bearing. The polarization it lives near is the
  wrong polarity (unconditional), which is the exact defect M4 must avoid. At most a **COMPONENT-tier**
  (P3) item: the "numerical cohomology + absolute arithmetic RR" is a cleaner archimedean-inclusive
  Euler-characteristic bookkeeping for the Arakelov substrate (analytic torsion inside $\chi$), which a
  future BUILDER could reuse *if* a product base and a contingent sign were ever supplied. It carries no
  sign by itself, so it does not move the front.
- **For R1 (sourcing / the product base):** nothing. It is on the wrong side of the base collapse: a curve
  over $\mathrm{Spec}\,\mathcal{O}_F$, not a self-product of $\mathrm{Spec}\,\mathbb{Z}$. It is a fresh
  witness *of* R1's shape (per-surface intersection theory is available and effective; the missing step is
  the product + Frobenius correspondence), not a supplier for it.
- **New-to-repo technical content worth keeping [VF-ext]:** the specific $\omega^2$ upper bound via $L^2$
  successive minima (Thm 1.3) and its HN-slope form, and the section-refined bound (Thm 1.5), are sharper
  than what the repo currently cites for the Arakelov face (Zhang, Moriwaki 1010.1599, Yuan-Zhang 2017,
  Cantat-Gao-Habegger-Xie). These belong in the `NODE-fh-too-local` reference bracket as the 2025 state of
  effective-$\omega^2$; they are effectivity refinements, not polarity or base moves.

## What this enables / what remains open

- **For BUILDER:** treat He's numerical cohomology / absolute RR as an optional cleaner substrate component
  for any Arakelov-surface attempt, but do NOT read it as progress toward a signature. The load-bearing
  moves (a product base $\mathrm{Spec}(\mathbb{Z})^{\times 2}$; a Frobenius/diagonal correspondence
  $\Gamma_S$; a *contingent* sign) are all still absent, and this paper does not touch them.
- **For ADVERSARY:** no new attack surface. The D-H discipline is not engaged (Architecture-2 exemption:
  the object requires no $\zeta$/L-function at all, so it cannot be instantiated for Davenport-Heilbronn;
  classify as face-mapping content, not a proof route). The wrong-polarity finding (S6) is the durable kill
  and needs no counterexample search.
- **For SYNTHESIZER:** add one row to the `NODE-fh-too-local` bracket in
  [`../spec_z_cohomology_landscape.md`](../spec_z_cohomology_landscape.md) recording He 2512.01811 as the
  2025-12 effective-$\omega^2$ refinement, same five-column verdict as the Faltings-Hriljac row; and close
  the first of the four PHASE_STATE/LEARNINGS-#155 open reading-note items (He). No LEARNINGS-worthy new
  object; this is confirmation, not a survivor.
- **Open (unchanged frontier):** the M4/R1 wall is exactly the two things this paper does not have, a
  product base and a contingent polarization. The three siblings still lacking notes (Abboud 2503.14099 =
  a *local* arithmetic Hodge index, the direct positivity analogue; Connes-Consani 2606.06604 = the
  competing absolute-$\mathrm{Spec}\,\mathbb{Z}$ substrate; Chen-Moriwaki 2207.02033 = adelic-curve
  positivity) are the higher-priority next reads: Abboud and Chen-Moriwaki actually state positivity
  theorems (so they can be scored on S5-S6 for polarity, unlike He), and Connes-Consani is the one candidate
  that could reopen a signed pairing on a genuinely $\mathbb{F}_1$-absolute base.

## References (paper-internal + repo anchors)

**Paper-internal to chase [VF]:** Arakelov (1974); Faltings, *Calculus on arithmetic surfaces* (Ann. Math.
1984); Deligne (determinant of cohomology); Gillet-Soulé (arithmetic Riemann-Roch); Szpiro, Parshin
(effective bounds); Zhang (admissible pairing / $\omega^2$); Wilms, Bost (Faltings invariants, $\theta$-
invariants). Full list 38 items, not individually read here.

**Repo anchors:** [`../spec_z_cohomology_landscape.md`](../spec_z_cohomology_landscape.md)
(`NODE-fh-too-local`; the four-property irreducible gap PROP-global/carries-trace/rh-equivalent/noncircular);
[`../sourcing_gap_r1.md`](../sourcing_gap_r1.md) (facets A purity / B polarization, both variety-gated);
[`../breadth_program.md`](../breadth_program.md) §1 (S1-S7, the polarity master discriminator);
[`../model_theoretic_frobenius.md`](../model_theoretic_frobenius.md) §8 (#156 two-conjunct WATCH clause,
#131 PROP-global); [`literature_survey/rh_arch2_supplement.md`](../literature_survey/rh_arch2_supplement.md)
§B (the Arakelov-positivity cluster this paper joins); [`Connes-2026-RH-Past-Present-Letter.md`](Connes-2026-RH-Past-Present-Letter.md)
(style template). LEARNINGS #155 (the corpus cross-reference that flagged this paper); #131 (PROP-global,
no $\mathrm{Spec}(\mathbb{Z})^{\times 2}$); #148 (the W6 det-class spec the Arakelov face also lacks).
