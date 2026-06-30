# A map of the obstruction to the Riemann Hypothesis: the missing polarization, pinned from four sides

> **Status: DRAFT, expository survey (2026-06-28).** A research note that maps, rather than removes,
> the obstruction to RH for the Riemann zeta function. It is **not** a proof and claims **no** new
> theorem: it is a survey of the project's own localization of the obstruction together with the
> standard literature. Distinguishes PROVEN from CONJECTURAL throughout; attributes every result.
> Companion to the broader all-roads survey ([`../P4_survey_draft.md`](../P4_survey_draft.md)); this
> note is the focused account of the four-sided bracket and the two disciplines that pin the missing
> object.

## Abstract

Every mature approach to the Riemann Hypothesis for the Riemann zeta function reaches the same wall:
each *realizes* $\zeta$ as a trace or a determinant of an operator or a correspondence, and none
supplies a *polarization*, a signed intersection pairing of indefinite signature $(1, n-1)$ whose
positivity is RH. Over a curve $C/\mathbb{F}_q$ this polarization is supplied by Weil's proof (the
Hodge index theorem on $C \times C$), which is why RH is a theorem there. Over $\mathrm{Spec}(\mathbb{Z})$
it is missing, and the gap is "variety-gated": it splits into two facets, both currently needing an
actual variety to close, R1 (sourcing a weight-1 carrier with $|\alpha| = \sqrt q$, which over
$\mathbb{F}_q$ is Deligne's purity theorem) and M4 (the polarization itself, which over $\mathbb{F}_q$
is Weil-Rosati positivity), coincident in genus 1. We organize the survey around a four-sided
**bracket**: the missing object is pinned from four directions by four proven near-misses, each missing
in a precisely diagnosable way, Faltings-Hriljac (too local), Adiprasito-Huh-Katz (too blind),
de Branges (too strong), and Rankin-Selberg / Deligne-Weil-II (too shallow). Two cross-cutting
disciplines hold the map honest: the marginal-positivity thesis (RH is "just barely true", which the
Rodgers-Tao theorem $\Lambda \ge 0$ makes rigorous, so no soft or generic-positivity proof can work)
and the Davenport-Heilbronn discipline (a functional equation without an Euler product has off-line
zeros, so any method that does not use the Euler product essentially is wrong). The contribution is
expository and organizational: the bracket as a device, and the two disciplines as a spine. Supplying
the missing object *is* RH (the arithmetic Hodge standard conjecture), itself open.

## 1. Introduction

The Riemann Hypothesis is usually surveyed as a catalog of approaches: analytic, spectral,
arithmetic-geometric, each with its partial results and its obstruction. This note takes a different
cut. We argue that the catalog has a structure, and that the structure is a single missing object. Read
at the right altitude, the major approaches are not independent bets on different mechanisms. They are
different constructions of the same object, and they fail at the same step.

The template is the one place where the analogous statement is a theorem: a smooth projective curve $C$
of genus $g$ over a finite field $\mathbb{F}_q$. Its zeta function

$$Z(C, T) = \exp\left( \sum_{k \ge 1} \frac{|C(\mathbb{F}_{q^k})|}{k} T^k \right) = \frac{P(T)}{(1 - T)(1 - qT)}, \qquad P(T) \in \mathbb{Z}[T], \ \deg P = 2g,$$

has all its reciprocal roots on the circle $|\alpha_i| = \sqrt q$ (Weil 1948). Under $T = q^{-s}$ this
is "all zeros on $\mathrm{Re}(s) = 1/2$", the function-field RH. Weil's proof runs on the cohomology
$H^1(C, \mathbb{Q}_\ell)$ and uses exactly three ingredients:

- **(i) Trace.** A Lefschetz fixed-point formula. Geometric Frobenius $F_q$ acts on $H^*(C)$, and
  $|C(\mathbb{F}_{q^k})| = \sum_i (-1)^i \mathrm{tr}(F_q^k \mid H^i)$, so $\zeta_C$ is a ratio of
  characteristic determinants $\det(1 - F_q\, q^{-s} \mid H^i)$, and the eigenvalues of $F_q$ on $H^1$
  are the "zeros" $\alpha_i$. This is a realization of $\zeta$ as a determinant or trace.
- **(ii) Duality.** Poincare duality $H^1 \otimes H^1 \to H^2 \cong \mathbb{Q}_\ell(-1)$ is a
  non-degenerate pairing. Its Frobenius-compatibility forces $\alpha \mapsto q/\alpha$, which **is** the
  functional equation $\xi(s) = \xi(1-s)$, pairing the roots.
- **(iii) Polarization.** The intersection form on $\mathrm{NS}(C \times C) \otimes \mathbb{R}$ has
  signature $(1, \rho - 1)$ (the Hodge index theorem), equivalently the Rosati involution on
  $\mathrm{End}^0(\mathrm{Jac}\, C)$ has a positive-definite trace form. Applied to the divisor
  $F_q^* - \alpha\, \mathrm{id}^*$ via the Castelnuovo-Severi inequality, this positivity forces
  $|\alpha_i| = \sqrt q$, which **is** RH-for-$C$.

This is the function-field template: **Lefschetz + Poincare duality + Hodge index** (the diff table in
[`../../experiments/arithmetic_geometric/2A_weil_proof_diff.md`](../../experiments/arithmetic_geometric/2A_weil_proof_diff.md)).
The project verified the template end-to-end in the function-field case: across 23 elliptic curves over
$\mathbb{F}_p$ the intersection form on $\mathrm{NS}(E \times E)$ has signature exactly $(1, 3)$ for
every curve, the primitive part is negative-definite, and $|a| < 2\sqrt p$ (Hasse) holds with an
$O(q)$ buffer ([`../../experiments/LEARNINGS.md`](../../experiments/LEARNINGS.md) #54, the Rosati
formulation in [`../../experiments/arithmetic_geometric/e2t_rosati_positivity.py`](../../experiments/arithmetic_geometric/e2t_rosati_positivity.py)).

The central observation of this note: over $\mathbb{Q}$, every serious program supplies (i) and most
supply a partial (ii), and **none** supplies (iii). Realization is the easy half. The polarization is
the whole gap. We make this precise (Section 2), grade the candidate cohomologies against it
(Section 3), exhibit the four-sided bracket that pins it (Section 4), split it into its two
variety-gated facets (Section 5), give the two disciplines that organize the map (Section 6), and state
the honest scope (Section 7).

A word on posture, following [`../../docs/researcher_mindset.md`](../../docs/researcher_mindset.md). We
document several methods that provably cannot close RH. We frame each as a coordinate, not a defeat: a
method that fails for a precise structural reason removes a branch and sharpens where the real proof
must live. The marginal-positivity finding in particular reads as a compass. It says the proof must
engage the exact structure of $\zeta$, not as a discouragement but as a direction.

## 2. The realization-vs-signature dichotomy

The one-sentence finding (the project's "all roads to the signature",
[`../../docs/03_research/all_roads_to_the_signature.md`](../../docs/03_research/all_roads_to_the_signature.md)):
every architecture produces the **realization** of $\zeta$ (a determinant, a trace, a detector, a
Dirichlet-series identity), and that half is comparatively easy and exists in several frameworks; RH
itself is the **signature / positivity**, which is separate, irreducible, and the same problem in every
framework. The realization is not the proof. The signature is.

This is not a vague slogan. It survives the strongest realization theorem in the literature.
Hesselholt's theorem proves, **over $\mathbb{F}_q$**, that $\zeta_C$ is the regularized determinant of
the Frobenius flow on the $S^1$-Tate periodic topological cyclic homology, $\zeta =
\det_\infty(s - \Theta \mid \mathrm{TP}_{\mathrm{odd}}) / \det_\infty(s - \Theta \mid \mathrm{TP}_{\mathrm{ev}})$
(Hesselholt 2018). And yet RH for the variety is *not* a corollary: it remains $|\alpha_i| = q^{1/2}$,
the Weil/Hodge-index positivity, a separate input. The best realization theorem confirms the
dichotomy: the determinant is the easy half, the signature is RH.

The dichotomy has a physical restatement (the acoustic / passive-network reading,
[`../../docs/03_research/all_roads_to_the_signature.md`](../../docs/03_research/all_roads_to_the_signature.md),
LEARNINGS #90-94): the impedance $Z = -\zeta'/\zeta = \sum \Lambda(n) n^{-s}$ is **passive** (a
positive von Mangoldt comb) iff there is an Euler product, which is the realization and is
unconditional; RH is the separate statement that the medium is **lossless** (resonances on the critical
line); and the coupling "passive + reciprocal $\Rightarrow$ lossless" is Weil's two-sided argument as
network theory. The missing ingredient is the energy form that **halves** the free passive bound
$\mathrm{Re} \le 1 \to \mathrm{Re} \le \tfrac12$, and that halving is Poincare duality placing the
self-dual middle weight at the geometric mean of the extremes, $q^{1/2} = \sqrt{q^0 \cdot q^1}$. This
is a clarifying language, not a new construction (the synthesis route lands on Suzuki's canonical
system, which is RH-equivalent), but it names the split: passivity is the Euler product (free),
losslessness is the missing signature (RH).

## 3. The scorecard: who realizes $\zeta$, and who carries the polarization

The consolidating reference for this section is the project's Spec($\mathbb{Z}$) cohomology landscape
([`../../docs/03_research/spec_z_cohomology_landscape.md`](../../docs/03_research/spec_z_cohomology_landscape.md)),
which grades every candidate cohomology against the three Weil ingredients plus the K2 (Davenport-Heilbronn)
discipline. The verdict is uniform and is the empirical backbone of the survey: **every candidate
realizes $\zeta$ as a trace or determinant; none carries the polarization.**

Legend: present/proven, partial (proven only in a restricted sense), absent.

| Candidate | (i) Trace | (ii) Duality | (iii) Polarization | Single sharpest open step |
|---|:--:|:--:|:--:|---|
| **Deninger** foliated $\mathbb{R}$-flow | partial | partial | absent | intersection form on $X \times X$ + Hodge-index signature |
| **Connes** adele-class trace formula (1999) | present | partial | absent (K1 wall) | global Weil positivity as a theorem, not a trace identity |
| **Connes-Consani** arithmetic site / Jacobian (2014, 2026) | present | partial | absent | turn the Picard/realization structure into a signed pairing |
| **Bhatt-Lurie** absolute prismatic / WCart | present | partial (duality, no sign) | absent | a positive cup/Rosati form on the global prismatic $H^1$ |
| **Bhatt-Scholze** per-prime prismatic | partial (local) | partial (local) | absent | assembly over all $p$ + the polarization |
| **Hesselholt** THH / TP / TC | present (over $\mathbb{F}_q$) | partial (over $\mathbb{F}_q$) | absent over $\mathbb{Z}$ | TP over $\mathbb{Z}$ with a periodic flow + negative-definite cup form |
| **Arakelov / Faltings-Hriljac** | absent (no $\zeta$) | partial (wrong dim) | **proven, single surface** | the product $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$ + Frobenius $\Gamma_S$ |
| **Adiprasito-Huh-Katz** matroid Hodge theory | absent | absent | **proven signature, no variety, arithmetic-blind** | a $t$-carrying Lefschetz element + indefinite $(1, n-1)$ primitive form |
| **Clausen-Scholze** condensed / analytic six functors | absent (no $\zeta$) | present (perfect, no sign) | absent (perfectness, not polarization) | a native polarization (an "archimedean Deligne-Illusie", conjectural) |
| **Fargues-Fontaine / Fargues-Scholze** | partial | partial | absent | reduces to M4 (LEARNINGS #133, the first-principles audit) |
| **Weil-etale** (Lichtenbaum / Flach-Morin) | partial | partial | absent | reduces to M4 (LEARNINGS #133) |

The structural reading (the graph diagnostic,
[`../../docs/03_research/spec_z_cohomology_landscape.md`](../../docs/03_research/spec_z_cohomology_landscape.md)
section 9): of the $\sim 17$ candidate frameworks the project entered into a dependency graph, nine
**collapse** onto the single gap node (they differ only in substrate, never in the positivity they
lack), four sit **off to the side** as the proven near-misses of Section 4, two are on the **K1 wall**
(the Connes trace-formula family, which is a circularity to escape, not a near-miss to extend), and two
are **pre-realization** (no realized $\zeta$ whose polarization could be missing). A targeted 2026 audit
of the three strongest recent constructions (Tang's prismatic Poincare duality, Compositio 2024;
Gurney's *Prismatization over $\mathbf{Z}$*, arXiv:2301.12392; Connes-Consani's 2026 Jacobian,
arXiv:2602.15941) found that **none supplies the polarization**: they stop at three different adjacent
inputs, perfectness without the sign, the global substrate without the cup/sign, the trace without a
signed pairing, which are three two-thirds of the same construction (LEARNINGS #71, #133).

The realization side is moving fast and the polarization has not moved. Deninger's foliated space is
now constructed via sheafified rational Witt vectors (arXiv:1807.06400, 2018); its cohomology, duality,
and polarization remain open. A new obstruction appeared on the prismatic side: Petrov proved the
Bhatt-Lurie Sen operator is not semisimple in general (arXiv:2302.11389, Annals), which blocks any
eigenspace-based Hodge-Riemann polarization on the prismatic substrate, so the polarization must be
intrinsic. Both 2026 Connes papers (the Jacobian, arXiv:2602.15941; the "Letter to Riemann",
arXiv:2602.04022) sharpen the realization half and explicitly defer the positivity, the latter via a
construction the project verified to be zeta-blind (it manufactures on-line zeros for any admissible
even-kernel form, and reproduces Davenport-Heilbronn's on-line zeros identically, LEARNINGS #50).

## 4. The four-sided bracket

The single most useful structural fact in the landscape is that there exist, anywhere near the problem,
exactly four proven positivity statements of roughly the right kind, and **all four miss in a precisely
diagnosable way**. Together they pin the missing object from four sides. This bracket is the
organizing device of the note.

### 4.1 Faltings-Hriljac: too local

The arithmetic intersection form on a **single** arithmetic surface is negative semi-definite on the
primitive part; equivalently the Neron-Tate height pairing is positive-definite. This is a **real,
proven polarization** (Faltings 1984, Hriljac 1985; the project reproduced it end-to-end, ranks 1-4,
in 2H-2P). It fails to give RH only because it lives on **one surface** of relative dimension $\ge 1$,
not on the product $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$, and carries no
Frobenius correspondence reaching the zeta zeros. The whole generalized-arithmetic-Hodge-index family
shares this bracket: Moriwaki's higher-dimensional arithmetic Hodge index (arXiv:1010.1599) and
Yuan-Zhang's adelic-line-bundle index theorem (Math. Ann. 367, 2017) prove the same
negative-definiteness on a *fixed* arithmetic variety, and Cantat-Gao-Habegger-Xie (Duke 170(2), 2021)
*use* the single-variety index for the geometric Bogomolov conjecture rather than extending it to a
product. Bost's theta-invariant / pro-Hermitian infinite-dimensional Arakelov geometry (Prog. Math.
334, 2020; arXiv:1512.08946) is genuinely over the arithmetic curve but is a different miss: it
produces a Diophantine $h^0_\theta$ (a non-negative scalar), the wrong signature class, not an
indefinite $(1, n-1)$ form.

A 2026 probe of this face (the Arakelov-face probe,
[`../../experiments/arithmetic_geometric/2L_arakelov_face_probe.md`](../../experiments/arithmetic_geometric/2L_arakelov_face_probe.md),
LEARNINGS #131-#132) sharpened the diagnosis: the Arakelov face does not escape the gap, it
**relocates** it. AHK has the base ($\mathrm{Spec}(\mathbb{Z})$ directly) but no carrier; the Arakelov
face has a genuine carrier and a genuine **proven per-surface polarization**, so it dies neither at R1
nor at M4-per-surface but at the **base**: the nonexistent product plus the Frobenius correspondence
$\Gamma_S$ that would globalize the per-surface theorem onto zeta's actual zeros. The only proven
height-to-L channel is Gross-Zagier / BSD, which equates a height to the central derivative
$L'(E, 1)$, the order of vanishing at the single point $s = 1$, severed from where the other zeros sit;
this retires the entire Gross-Zagier / Beilinson-Bloch family from the RH search by a
central-value-vs-all-heights disqualifier (LEARNINGS #113). *Too local.*

### 4.2 Adiprasito-Huh-Katz: too blind

The Kahler package, including Hodge-Riemann positivity, holds on the Chow ring of **any** matroid, even
non-realizable ones (Adiprasito-Huh-Katz, Ann. Math. 2018): a **signature with no underlying variety**,
exactly the shape Weil's proof wants. It fails because it is **arithmetic-blind**: it takes no Frobenius
trace $t$ (the project's mixed-volume probe reads the same $(1, 3)$ signature for $t = 2$ and
$t = 100$, LEARNINGS #40), and the convex-Hodge signature is *unconditionally* $(1, n-1)$ for every
weighting, so it has the **wrong polarity** for a detector: it can never flip to flag an off-line zero,
whereas the Weil form flips PSD $\to$ indefinite exactly when an off-line zero appears (the polarity
check, LEARNINGS #48). It is nonetheless the **one retained positive coordinate** of the
breadth-over-proof-engines sweep (LEARNINGS #97): alone among five from-below
signature-manufacturing engines it is K1-clean (the signature comes from a submodular flip, not the
zeros), so it is the unique proven witness that a $(1, n-1)$ signature is manufacturable K1-clean with
no ambient variety. The sharpened BUILDER target
([`../../docs/03_research/research_directions/08A_rosati_standard_conjecture.md`](../../docs/03_research/research_directions/08A_rosati_standard_conjecture.md),
and the 09A AHK lattice) asks for a finite graded prime-lattice whose degree map carries $t$ and whose
primitive form is born indefinite, leaving only the positivity (= M4) open. That route was pushed to
its end and closed into the sourcing facet R1 (LEARNINGS #129, #130, Section 5): a matroid Chow ring
is purely Tate with no $H^1$, so the combinatorial source fails *before* the polarization. *Too
blind.*

### 4.3 de Branges: too strong

The de Branges space of $\xi$ realizes the analytic continuation as a signed reproducing-kernel inner
product that **does** reach the global zeros. But its positivity is **strictly stronger than RH**: it
implies GRH for all Dirichlet $L$-functions at once, and Conrey-Li proved it **fails for $\zeta$** at
the 34th zero (Conrey-Li, arXiv:math/9812166; the project reproduced this to 12 significant figures,
LEARNINGS #43 / 2DB.1). A positivity that is provably false for the very function it is supposed to
certify cannot be the missing object. The bracket is doubly informative: de Branges shows that a
pairing reaching the global zeros is available, and that reaching the zeros is not the hard part;
reaching them with the *RH-equivalent* (not RH-stronger) sign is. *Too strong.*

### 4.4 Rankin-Selberg / Deligne-Weil-II: too shallow

This is the fourth and most recently added side of the bracket (the first-principles audit,
LEARNINGS #133, 2026-06-28). It is a different *type* of near-miss: a proven *analytic* positivity,
non-circular and Euler-essential, that is too shallow to reach the critical line.

Deligne's 1974 Weil-II proof reaches $|\alpha| = \sqrt q$ **without** the Hodge index theorem, via
global monodromy of a Lefschetz pencil plus the Rankin-Selberg even-tensor-power positivity (the pole
structure of $L(s, \mathrm{Sym}^{2k})$). Its one variety-free number-field shadow is the classical
Rankin-Selberg / de la Vallee-Poussin positivity, the $3 + 4\cos\theta + \cos 2\theta \ge 0$ engine
behind the zero-free region. That positivity is **proven and non-circular** (K1-clean: it comes from
the pole of $L(s, \pi \times \tilde\pi)$ at $s = 1$ and from non-negative convolution coefficients,
not from reading the zeros) and **Euler-essential** (it correctly does **not** fire for
Davenport-Heilbronn, which has no Rankin-Selberg square), but it lives at the $\mathrm{Re} = 1$ edge
and provably **saturates the Vinogradov-Korobov $2/3$ ceiling**: it cannot be pushed to
$\mathrm{Re} = 1/2$. Walked to its wall over a number field, the monodromy engine SPLITS into exactly
the two facets already on this map (Section 5): the geometric core needs the purity/monodromy group
that only a variety supplies (R1), and the variety-free shadow is the analytic zero-free ceiling
(Architecture 4). Unlike Weil-I Hodge-index/Rosati positivity it is genuinely a *different engine*,
which is why it earns its own bracket; it is no more tractable. *Too shallow.*

### 4.5 The shape of what is missing

The four sides together specify the missing object. It is a polarization that is

- **global** (unlike Faltings-Hriljac, which is single-surface),
- **carries the arithmetic Frobenius trace $t$** (unlike AHK, which is arithmetic-blind),
- **RH-equivalent, not strictly stronger** (unlike de Branges, which is RH-stronger and false for
  $\zeta$), and
- **deep enough to reach $\mathrm{Re} = 1/2$** (unlike Rankin-Selberg, which is a real, non-circular,
  Euler-essential positivity but is capped at the $\mathrm{Re} = 1$ edge).

In the project's dependency-graph vocabulary, the gap node is the **logical conjunction** of four
independently-named, independently-droppable properties: `PROP-global`, `PROP-carries-trace`,
`PROP-rh-equivalent`, `PROP-noncircular`. Each conjunct is proven-droppable by a distinct object,
which is what makes the conjunction irreducible (no property is redundant): Faltings-Hriljac drops
global, AHK drops carries-trace, de Branges drops (and is refuted on) rh-equivalent, and the Connes
trace-formula family drops noncircular. The no-go (the four-property conjunction) IS the target, and
there is no soft shortcut: any proof must supply all four at once.

## 5. The two variety-gated facets

A 2026 sharpening ([`../../docs/03_research/sourcing_gap_r1.md`](../../docs/03_research/sourcing_gap_r1.md),
LEARNINGS #130) splits the universal gap into two distinct-but-linked facets, both currently
"variety-gated" (closeable, on all available evidence, only by supplying an actual variety):

- **(A) Sourcing / purity (R1).** Produce a weight-1 carrier with $|\alpha| = \sqrt q$ in the first
  place. Over $\mathbb{F}_q$ this is **Deligne's purity theorem** (free for any variety). The verified
  finding is that no non-geometric source is known: every proof of weight-1 purity routes through a
  variety or stack. The decisive dramatization is the holomorphic-vs-Maass split (Sarnak, Clay 2005):
  for **holomorphic** modular forms, the Ramanujan bound $|a_p| \le 2\sqrt p$ is Deligne's theorem
  *because* the modular curve is a variety; for **Maass** forms the symmetric space is non-Hermitian,
  there is "no apparent algebro-geometric moduli interpretation", and Ramanujan is **open** (best bound
  Kim-Sarnak $7/64$, never $\theta = 0$). The instant the variety is removed, purity becomes open.

- **(B) Polarization / signature (M4).** The arithmetic Hodge standard conjecture: the primitive cup
  form is definite with the indefinite $(1, n-1)$ signature. Over $\mathbb{F}_q$ this is **Weil's /
  the Rosati positivity** (a theorem for abelian varieties), placed by Grothendieck inside the standard
  conjectures circle (the Hodge standard conjecture, a theorem in characteristic 0 via the
  Hodge-Riemann relations, open in general characteristic).

For a curve (genus 1) the two collapse to one inequality:
$|\alpha| = \sqrt q \iff$ the primitive form is negative-definite $\iff t^2 < 4q$. In general they are
distinct theorems (a *weight* statement vs a *positivity* statement), both holding over the function
field precisely because there is a variety. So the scorecard's "(i) free, (iii) missing" is more
precisely: realization gives the *shape*, while both the *purity* of the carrier (A) and the
*polarization* (B) are the variety-gated content. It is a **gap, not an obstruction**: there is no
impossibility theorem. R1 closes only by (a) supplying the geometric / motivic source (the FLT-adjacent
existence problem the Arakelov face inherits) or (b) a variety-free proof of purity (itself a major
theorem). This is the precise reason every road walls identically: each supplies the realization shape,
and none supplies variety-free purity (A) or the polarization (B).

The target M4 has a concrete milestone ladder (M1-M5,
[`../../docs/03_research/research_directions/08A_rosati_standard_conjecture.md`](../../docs/03_research/research_directions/08A_rosati_standard_conjecture.md)).
M1 is done (the function-field Rosati formulation verified, genus 1-2). M2 through M2.6 built the
truncated, **non-circular** arithmetic Weil form $M = A_{\mathrm{arch}} + P_{\mathrm{fin}} +
B_{\mathrm{pole}}$ from the $\Gamma$-factor and the von Mangoldt primes, with no zeros, and found
$\min\mathrm{eig}(M) = +0.035 > 0$ for $\zeta$ (a non-circular positivity certificate, necessary not
sufficient). But the four-way discrimination *fails*: D-H reads spuriously positive ($+0.094$) because
its off-line obstruction sits below the reconstruction-residual floor. This is the stealth window
(Section 6) on the Rosati side, and it is why M3 onward must be analytic, engaging the exact off-line
structure rather than a finer truncation. The Lean face is machine-checked at the zero level: the
functional equation provides the perfect pairing $\rho \leftrightarrow 1 - \rho$, and RH is equivalent
to that pairing being conjugation, sorry-free and axiom-clean
([`../../lean/ZetaRH/ArithmeticPolarization.lean`](../../lean/ZetaRH/ArithmeticPolarization.lean)); the
deep step, that a *polarization* forces $1 - \rho = \overline\rho$, is M4 itself and is not formalized.

## 6. The two disciplines

Two cross-cutting disciplines organize the whole map. The first says no *soft* proof can work; the
second says the *Euler product* must be used essentially. Together they cut the problem so cleanly that
the missing object is forced to live in one place.

### 6.1 Marginal positivity: RH is just barely true

The project's central structural finding is that RH is true only at the margin, with no buffer for soft
proofs. This is the exact statement that the signature is the whole content: if the positivity had any
slack, a soft realization (a trace, a statistic, a determinant) would close it.

The finding is rigorous, not merely numerical. **Rodgers-Tao proved $\Lambda \ge 0$** for the de
Bruijn-Newman constant (Rodgers-Tao, *Duke Math. J.* 2020): the zeros are, in the heat-flow sense, at
the exact boundary of being on the line, and "$\Lambda < 0$ would mean a buffer" is provably false.
RH is the statement $\Lambda \le 0$, so RH is $\Lambda = 0$, criticality with no margin. The project
quantified the same wall from several independent directions:

- The Weil-form minimal eigenvalue collapses **doubly-exponentially**, $\varepsilon(x) \sim
  \exp(-4\pi x)$ in the prime cutoff $x$, derived directly from the Slepian prolate concentration
  eigenvalues (Fuchs 1964, Slepian 1965), and confirmed independently by Connes' Figure 1
  (arXiv:2602.04022). Positivity for $\zeta$ is a $\sim 370\times$ cancellation residue, not
  cushion-plus-perturbation, and the archimedean block $A_{\mathrm{arch}}$ is itself indefinite, so
  "the archimedean term dominates the primes" is false: $\zeta$'s positivity is the residue of a
  three-way near-cancellation (LEARNINGS #52, #56, #128 Front 1).
- Over $\mathbb{F}_q$ the same positivity is *definite with an $O(q)$ buffer* (LEARNINGS #54). The
  contrast is the sharpest statement of the gap: where the polarization is a theorem there is room to
  spare; where it is RH the buffer is doubly-exponentially marginal, and the surface carrying the
  Frobenius class is not even constructed.
- The most concrete face of this (LEARNINGS #135, `e2w2_loglog_arch_coupling`): the non-circular
  Rosati positivity of $\zeta$ on the project's test family is a min-eigenvalue of $+0.035$, which is
  the difference of two blocks of norm $\approx 44$ ($\|A_{\mathrm{arch}}\| = 44.3$ vs $\|P+B\| =
  44.4$). It is a razor with no slack, and this is provable, not rhetorical: the one named candidate
  for making multiplicativity act on the continuation (rescale $A_{\mathrm{arch}}$ by the Rankin
  loglog-coefficient $c_F$, the sharp Euler discriminator) was executed and destroys the positivity
  for *every* control including RH-true Euler $\zeta$ ($c_F = 1.105 > 1$), because perturbing a
  norm-44 block by $\sim 10\%$ swamps a $+0.035$ margin. Multiplicativity cannot be injected into the
  signature: there is no margin to inject into. This closes the last marginally-live thread the
  four-mechanism construction sweep left open, by the razor rather than by the (also-fatal) non-Euler
  trap.

The de Bruijn-Newman side is also a **mirror** rather than a lever: the de Bruijn / Polya kernel
positivity $\Phi \ge 0$ is verified correct but pre-empted (Dobner 2020, Newman-Wu 2019) and is
orthogonal to RH (D-H passes it identically to $\zeta$); the de Bruijn-Newman criticality flow,
D-H-tested in 2026, is D-H-blind by the same archimedean stealth window as the kernel (LEARNINGS #38,
#133). The Nyman-Beurling / Baez-Duarte criterion is the other classical "RH at the margin" object,
and it too was D-H-tested and found to be a **mirror**: it does not read D-H's off-line zero (which sits
archimedean-suppressed off the line) and does not detect the missing Euler product, failing by the
stealth window, not by circular zero-reading (LEARNINGS #133). So the three soft / critical-line
objects nearest RH (Lee-Yang, the de Bruijn kernel, Nyman-Beurling-Baez-Duarte) are all D-H-blind by
the same mechanism: marginal positivity is what closes the soft routes.

One honesty correction belongs here (LEARNINGS #133). The frame "Level 4 = positivity = signature" is
five-sixths a falsification-grounded law and one-sixth a *choice* stated as a law: it generalizes from
two reformulations (Weil, Li) and then enforces convergence by re-describing every Level-4
non-polarization as "the signature in different clothes". The de Bruijn-Newman criticality flow is the
witness of a genuinely Level-4, non-polarization region the program had subsumed by fiat. The project
retracted that over-reach (in `CLAUDE.md` and the four-level framing doc), keeping every theorem intact
and softening the claim to "every Level-4 *reformulation analyzed so far* reduces to a positivity". The
map of the obstruction is to a polarization; the claim that *every* Level-4 route must be a polarization
is the one place where the compass was stated more strongly than the evidence supports.

### 6.2 The Davenport-Heilbronn discipline: the Euler product must be used essentially

The Davenport-Heilbronn L-function has a functional equation but **no Euler product**, and it has
**known off-line zeros** (the first at $\rho \approx 0.8085 + 85.699\,i$, with the partner
$0.1915 + 85.699\,i$ by the functional equation). It is therefore the project's **wrong-approach
detector**: any method in the spectral, positivity, or analytic architectures that does not distinguish
$\zeta$ from D-H is structurally wrong, because a D-H-blind "RH proof" would prove a false statement.
This is the canonical Selberg-class philosophy (Bombieri's Clay problem description; Conrey, *Notices
AMS* 2003); the project's contribution is to run it as a *quantitative, build-time* discipline
(`experiments/_shared/davenport_heilbronn.py`, with a 5/5 smoke-test control).

The discipline cuts the problem cleanly in two (the K2 firewall,
[`../../docs/03_research/spec_z_cohomology_landscape.md`](../../docs/03_research/spec_z_cohomology_landscape.md)
section 6). The **archimedean / continuation half** (the $\Gamma$-factor, the Sonin space, the Sen
$\Theta$ divisor, the de Branges kernel positivity) is **shared by D-H** and is therefore RH-agnostic:
D-H has the same functional equation and $\Gamma$-factor by construction. **All discrimination lives on
the Euler-product / Frobenius half** (the orbit lengths $\{\log p\}$, the $(1, p)$ bidegree, the
prismatic Frobenius, THH). The polarization that proves RH must therefore be carried by the **Frobenius
direction**, the one object that is structurally unbuildable for D-H: no Euler product $\Rightarrow$ no
Frobenius correspondence $\Rightarrow$ no surface $\Rightarrow$ no intersection form to take the
signature of. The single object whose positivity is RH is exactly the single object that cannot be
built for the known counterexample. That is not a coincidence; it is the discipline telling us where
the proof must live.

The published literature now confirms this prediction with a theorem. Connes-Consani proved a
Weil-positivity fragment (*Selecta Math.* 2021, arXiv:2006.13771), but **only at the archimedean
place** (the Sonin space), the half D-H shares, so the one provable positivity is RH-agnostic. The K2
firewall predicted exactly this. The remaining live thread on the spectral side, the Connes-Consani-Moscovici
semilocal prolate operator (arXiv:2310.18423), is the one QM object that injects Euler content on the
Frobenius side and is structurally unbuildable for D-H; its positivity is a *strategy* with a standing
K1 risk, and it reduces to M4 from the continuation side (LEARNINGS #111-#118).

There is a sharp **stealth window** inside this discipline, and it must be stated honestly. D-H's
off-line zero at height $85.7$ is archimedean-suppressed: at a truncated prime cutoff its effect sits
below the reconstruction-residual floor, so the *non-circular* truncated Weil form is numerically blind
to it (LEARNINGS #34, #47). This is not a hole in the discipline (the rigorous Li-criterion leg shows
D-H $\lambda_n < 0$ at $n = 336{,}000$, and a continuum-rigorous one-test certificate excludes the D-H
cone, LEARNINGS #82-#84); it is the analytic shadow of marginal positivity. The two disciplines are the
same wall seen from two sides: the off-line signal D-H must produce, and the buffer $\zeta$ does not
have, are both doubly-exponentially small, which is why a soft method (Section 6.1) cannot see either.

## 7. Honest scope

This note is a **map** of the obstruction, not a step across it. To be scrupulous about what is and is
not claimed:

- **PROVEN, and cited as such:** the function-field template (Weil 1948; verified in-repo, 2G/2T/e2t,
  LEARNINGS #54); the single-surface arithmetic Hodge index (Faltings 1984, Hriljac 1985); the AHK
  Kahler package with no variety (Adiprasito-Huh-Katz 2018); Hesselholt's determinant formula over
  $\mathbb{F}_q$ (2018); the archimedean Weil positivity, RH-agnostic (Connes-Consani 2021); the
  Rodgers-Tao theorem $\Lambda \ge 0$ (2020); the de Branges positivity *fails* for $\zeta$ at the
  34th zero (Conrey-Li); the Rankin-Selberg / de la Vallee-Poussin positivity and its $2/3$ saturation;
  the non-semisimplicity of the prismatic Sen operator (Petrov, Annals); Deninger's foliated-space
  construction (2018).
- **CONJECTURAL, and labeled as such:** the global determinant over $\mathbb{Z}$; the spectral
  identification $\mathrm{spec}(H) = \{\gamma_n\}$; the product surface
  $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$ and its Frobenius cycle class $\Gamma_S$;
  **every** product/global polarization. The arithmetic standard conjectures, the would-be source of
  RH-positivity, are themselves open.
- **The central caveat:** do **not** read any candidate's realization (i) or duality (ii) as progress
  toward RH. RH is (iii), and (iii) is open in every framework. Supplying the missing object is not a
  shortcut to RH: it **is** RH (the arithmetic Hodge standard conjecture / Rosati positivity).
  "Spec($\mathbb{Z}$) cohomology" is RH in cohomological clothing.

The contribution of the note is expository and organizational. The convergence claim itself (RH = the
missing polarization = the arithmetic Hodge standard conjecture) is **known folklore**: the project's
own spine calls it "the arithmetic analogue of Grothendieck's Hodge standard conjecture", and it must
be framed as an organizing equivalence, never as progress toward a proof. What this note adds is the
**four-sided bracket** as a device for pinning the missing object (the fourth side, Rankin-Selberg /
Weil-II "too shallow", is the 2026 addition), and the **marginal-positivity and Davenport-Heilbronn
disciplines** as the spine that makes the localization precise and keeps it honest. The value of a map
is not that it crosses the territory. It is that it tells the next traveler, with unusual precision,
where the river actually is.

## References

The reference list of the landscape document
([`../../docs/03_research/spec_z_cohomology_landscape.md`](../../docs/03_research/spec_z_cohomology_landscape.md))
is the source; the items below are those load-bearing for this note. ArXiv identifiers, authors, and
venues are as recorded there and in the project's reading notes. Items not independently re-verified at
the source for this draft are flagged in the README's open-review list.

**The function-field template and the standard conjectures.**
Weil, A. (1948). *Sur les courbes algebriques et les varietes qui s'en deduisent.*
Deligne, P. (1974). *La conjecture de Weil. I.* Publ. Math. IHES 43.
Deligne, P. (1980). *La conjecture de Weil. II.* Publ. Math. IHES 52.
Grothendieck, A. (1969). *Standard conjectures on algebraic cycles.*
Tate, J. (1965). *Algebraic cycles and poles of zeta functions.*

**The four-sided bracket.**
Faltings, G. (1984). *Calculus on arithmetic surfaces.* Ann. Math.
Hriljac, P. (1985). *Heights and Arakelov's intersection theory.*
Gillet, H.; Soule, C. (1992). *An arithmetic Riemann-Roch theorem.* Invent. Math.
Moriwaki, A. *Arithmetic Hodge index theorem* (arXiv:1010.1599); Yuan, X.; Zhang, S.-W. (2017). *The
arithmetic Hodge index theorem for adelic line bundles.* Math. Ann. 367.
Cantat, S.; Gao, Z.; Habegger, P.; Xie, J. (2021). *The geometric Bogomolov conjecture.* Duke Math. J.
170(2).
Bost, J.-B. (2020). *Theta invariants of Euclidean lattices...* Prog. Math. 334 (arXiv:1512.08946).
Adiprasito, K.; Huh, J.; Katz, E. (2018). *Hodge theory for combinatorial geometries.* Ann. Math.
Conrey, J. B.; Li, X.-J. *A note on some positivity conditions...* (arXiv:math/9812166).

**The candidate cohomologies.**
Deninger, C. (1998). *Some analogies between number theory and dynamical systems on foliated spaces.*
ICM 1998. Deninger, C. *Dynamical systems for arithmetic schemes* (arXiv:1807.06400, 2018).
Connes, A. (1999). *Trace formula in noncommutative geometry and the zeros of the Riemann zeta
function.* Selecta Math. Connes, A.; Consani, C. (2014). *The hyperring of adele classes...*; (2021).
*Weil positivity and the archimedean place* (arXiv:2006.13771, Selecta Math.); (2026). *On the Jacobian
of $\overline{\mathrm{Spec}\,\mathbb{Z}}$* (arXiv:2602.15941). Connes, A. (2026). *Letter to Riemann*
(arXiv:2602.04022). Connes, A.; Consani, C.; Moscovici, H. (2024). *semilocal prolate operator*
(arXiv:2310.18423).
Bhatt, B.; Lurie, J. *Absolute prismatic cohomology* (arXiv:2201.06120). Bhatt, B.; Scholze, P. (2022).
*Prisms and prismatic cohomology.* Ann. Math. Petrov, A. *Non-decomposability of the de Rham complex
and non-semisimplicity of the Sen operator* (arXiv:2302.11389, Annals). Gurney, L. *Prismatization over
$\mathbf{Z}$* (arXiv:2301.12392).
Hesselholt, L. (2018). *Topological Hochschild homology and the Hasse-Weil zeta function.*

**The two disciplines.**
Rodgers, B.; Tao, T. (2020). *The de Bruijn-Newman constant is non-negative.* Duke Math. J.
Dobner, A. (2020). *A new proof of Newman's conjecture and a generalization* (the class $S^\#$ including
D-H). Newman, C.; Wu, W. (2019). Slepian, D. (1965); Fuchs, W. H. J. (1964). *On the eigenvalues of an
integral equation arising in the theory of band-limited signals.*
Sarnak, P. (2005). *Notes on the Generalized Ramanujan Conjectures.* Clay Math. Proc. 4 (the
holomorphic-vs-Maass split, the R1 facet).
Bombieri, E. (2000). *Problems of the Millennium: The Riemann Hypothesis.* Clay Mathematics Institute.
Conrey, J. B. (2003). *The Riemann Hypothesis.* Notices AMS.

**Project internal (the localization this note surveys).**
[`spec_z_cohomology_landscape.md`](../../docs/03_research/spec_z_cohomology_landscape.md) (the scorecard,
the bracket, the universal gap);
[`all_roads_to_the_signature.md`](../../docs/03_research/all_roads_to_the_signature.md) (the
realization-vs-signature dichotomy);
[`08A_rosati_standard_conjecture.md`](../../docs/03_research/research_directions/08A_rosati_standard_conjecture.md)
(M4, the M1-M5 ladder);
[`sourcing_gap_r1.md`](../../docs/03_research/sourcing_gap_r1.md) (the R1 facet);
[`2A_weil_proof_diff.md`](../../experiments/arithmetic_geometric/2A_weil_proof_diff.md) (the diff table,
the 17 constraints);
[`LEARNINGS.md`](../../experiments/LEARNINGS.md) #30, #40, #43, #48, #50, #52, #54, #56, #71, #97,
#111-#118, #128-#133.
