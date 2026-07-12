# The sourcing gap (R1): a weight-1 $\sqrt q$ carrier is variety-gated

> Written 2026-06-27, after the AHK route to P3 closed into R1 ([`research_directions/09A_ahk_arithmetic_lattice.md`](research_directions/09A_ahk_arithmetic_lattice.md) Section 6D; [`../../experiments/arithmetic_geometric/e2zb_super_ahk_recursion.md`](../../experiments/arithmetic_geometric/e2zb_super_ahk_recursion.md), LEARNINGS #129). It answers a single sharp question and records the literature verification (a SURVEYOR pass over Sarnak, Fontaine-Mazur, Lafforgue, Deligne, Drinfeld-module RH, Scholze torsion). The question is the cleanest statement of the program's universal gap, so it earns its own note.

## The question

> Can a **non-Tate weight-1 object with modulus-$\sqrt q$ Frobenius** ($H^1$ with all eigenvalues $|\alpha|=\sqrt q$) be **sourced without a variety**?

This is the residual R1 the AHK arc reduced to. RH-for-a-curve runs on $H^1(C)$, whose Frobenius eigenvalues satisfy $|\alpha|=\sqrt q$ (purity) and whose primitive cup form is a polarization. To get RH for $\zeta$ over $\mathrm{Spec}(\mathbb{Z})$ from a combinatorial / non-geometric source (no surface), one must first manufacture that $\sqrt q$-weight-1 carrier from the prime data directly. The AHK route ([09A](research_directions/09A_ahk_arithmetic_lattice.md)) showed combinatorics cannot: a matroid Chow ring is purely even / Tate, with no $H^1$ at all (e2yy/#124), and no super-AHK induction runs on a hand-grafted odd piece (e2zb/#129).

## Shape versus purity

Split R1 into two genuinely different asks:

1. **Source the shape**: a non-Tate, weight-1 object with *some* Frobenius/Galois action. Comparatively easy and genuinely doable without a variety: 2-dimensional Galois representations, automorphic (Maass) forms, the Bost-Connes / KMS modular structure, even artificial representations.
2. **Source it with provable $|\alpha|=\sqrt q$ (purity)**: the hard part, and on all available evidence equivalent to having a motive (a variety).

The combinatorial routes (AHK, tropical) fail at **(1)** already: they are Tate (no weight-1 shape) or, in the tropical case, Frobenius-free (over $(\mathbb{R},\max,+)$: no $q$, no $\sqrt q$, no Galois). The automorphic / Galois routes have the shape but not provable purity. Nobody has **(2)** without a variety.

## The verified answer: conjecturally NO, operationally OPEN

A SURVEYOR pass hard-checked four claims (HOLDS / WEAKENED / REFUTED, with reading-depth flagged); all hold.

| # | Claim | Ruling | Key citation |
|---|---|---|---|
| 1 | Weight-1 $|\alpha|=\sqrt q$ purity is PROVEN only via varieties/stacks | HOLDS | Deligne, Weil II; even Lafforgue's function-field GRC realizes the rep in the $\ell$-adic cohomology of the **moduli stack of Drinfeld shtukas**, then invokes Deligne purity |
| 2 | Fontaine-Mazur $\Rightarrow$ a pure geometric weight-1 $\sqrt q$ Galois rep is motivic | HOLDS as direction / WEAKENED as a lever (CONJECTURE; proven GL2/$\mathbb{Q}$ cases route motivicity through a Kuga-Sato variety; and it presupposes a Galois action a combinatorial object lacks) | Kisin (JAMS 2009), Emerton |
| 3 | Ramanujan for **Maass** forms is OPEN precisely because there is no variety; for holomorphic forms it is a Deligne theorem via the modular curve | HOLDS (verbatim in Sarnak) | Sarnak, Clay 2005, pp. 660, 663-664 |
| 4 | No genuinely variety-free pure weight-1 $\sqrt q$ object is known | HOLDS | composite; each near-counterexample fails one clause of {variety-free, $\sqrt q$-bearing, proven-pure} |

### The cleanest dramatization: holomorphic versus Maass (Sarnak)

For **holomorphic** modular forms, Ramanujan $|a_p|\le 2\sqrt p$ is **Deligne's theorem** *because* $\Gamma_0(N)\backslash\mathbb{H}$ is a moduli space of elliptic curves (a variety): the bound is the purity of Frobenius on the $\ell$-adic cohomology of a Kuga-Sato variety. For **Maass** forms, the symmetric space $SL_n(\mathbb{C})/SU(n)$ is non-Hermitian, so (Sarnak, p. 664) "there is no apparent algebro-geometric moduli interpretation," and Ramanujan is **open**, with only partial bounds (Kim-Sarnak $7/64$), never $\theta=0$. The instant the variety is removed, purity becomes open. The variety *is* the purity.

### Why each candidate variety-free source fails

- **Drinfeld modules / Anderson $t$-motives** (incl. the RH preprint arXiv:2512.12374): purity is proven, but the $t$-motive *is* a geometric-arithmetic object (a Tate module with a genuine Frobenius), and it lives only over function fields of characteristic $p$, not $\mathrm{Spec}(\mathbb{Z})$. Fails variety-free + wrong base.
- **Nori / Voevodsky / pure motives**: defined starting from smooth (projective) varieties; they reorganize variety-cohomology, they do not source purity ex nihilo. Fails variety-free by construction.
- **Scholze torsion classes / Calegari-Geraghty**: the closest to "automorphic but not yet motivic," but the Galois reps are extracted from the cohomology of locally symmetric / Shimura varieties, and purity for the genuinely non-self-dual (Maass-type) objects is open. Fails variety-free + proven-pure.
- **Amini-Piquerez non-Tate tropical Kähler / Babaee-Huh / tropical Jacobians**: genuinely combinatorial and genuinely non-Tate (so they refute the naive "combinatorial $\Rightarrow$ Tate"), but **Frobenius-free** (no $q$) with a positive-definite (wrong) signature. Fails $\sqrt q$-bearing entirely.

## The structural framing: the universal gap has two variety-gated facets

The [spec_z cohomology landscape](spec_z_cohomology_landscape.md) records that every candidate **realizes** $\zeta$ as a trace and **none** carries the **polarization** (the universal gap $=$ M4). R1 sharpens this. The universal gap has two facets, both variety-gated, distinct theorems in general, coincident in the genus-1 shadow:

- **(A) Sourcing / purity (R1).** Produce a weight-1 carrier with $|\alpha|=\sqrt q$. Over $\mathbb{F}_q$ this is **Deligne's purity theorem**, which holds for any variety; the verified R1 finding is that no *non-geometric* source for it is known.
- **(B) Polarization / signature (M4).** The arithmetic Hodge standard conjecture: the primitive cup form is definite with the indefinite $(1,n-1)$ signature. Over $\mathbb{F}_q$ this is **Weil's / the Rosati positivity** (a theorem for abelian varieties).

For a curve (genus 1) the two collapse to one inequality: $|\alpha|=\sqrt q \iff$ the primitive form is negative-definite $\iff t^2<4q$ (e2g). In general they are distinct (Deligne purity is a *weight* statement; the Hodge standard conjecture is *positivity*), and both are theorems over the function field precisely because there is a variety. Over $\mathrm{Spec}(\mathbb{Z})$ neither has a known non-geometric source. R1 is therefore not a softer residual we reduced to: it is the **sourcing facet of the same universal gap**, and it is exactly the residual lever B reaches (the scheme-theoretic existence of the rank-2 Frobenius/Tate-module datum, [`research_directions/lever_b_function_field_plan.md`](research_directions/lever_b_function_field_plan.md), #108).

## Gap, not obstruction

There is no impossibility theorem. "Variety-free $\Rightarrow$ no $\sqrt q$-purity" is a strong empirical regularity and the negative shadow of Fontaine-Mazur plus the open Maass-form status, but it has **not** been proven. So R1 cannot be closed by citation; it can only be closed by

- (a) **supplying** the geometric / motivic source (the FLT-adjacent existence problem the Arakelov face inherits), or
- (b) genuinely **refuting** the regularity with a variety-free pure-$\sqrt q$ construction, which would itself be a major theorem (a non-geometric proof of purity).

This is why every construction route in the project walls identically: each supplies **realization** (the shape) and none supplies **purity without a variety** (facet A) or **the polarization** (facet B). The Deninger program is precisely the attempt to be such a variety-free source; so R1 is the Deninger / arithmetic-cohomology-of-$\mathrm{Spec}(\mathbb{Z})$ question, stated at the sharpest level.

## Update (2026-07-01): R1 is self-adjointness-gated, not merely variety-gated

The graph world sharpens the "variety-gated" reading. Graph-RH (Ramanujan, $|\lambda| \le 2\sqrt q$) carries the *same* $\sqrt q$ purity, and Marcus-Spielman-Srivastava (Interlacing Families I, Annals 2015) source it with **no variety**: bipartite Ramanujan graphs of every degree exist by the method of expected characteristic polynomials. So a non-geometric source of the $\sqrt q$ bound provably exists in the graph world, and R1 is *crossed* there.

The reason it does not transfer to $\mathrm{Spec}(\mathbb{Z})$ ([`../../experiments/toy/interlacing.py`](../../experiments/toy/interlacing.py), LEARNINGS #140) is that the MSS engine runs on **real-rootedness** (Heilmann-Lieb; the interlacing family needs real-rooted polynomials), which holds because the signed adjacency is self-adjoint. The arithmetic L-polynomial (the characteristic polynomial of Frobenius on $H^1$) is **not** real-rooted: its roots are the Frobenius eigenvalues on the circle $|\alpha|=\sqrt q$, genuinely complex. The non-variety source is paid for with self-adjointness, exactly the ingredient $\mathrm{Spec}(\mathbb{Z})$ lacks.

So R1 sharpens from **variety-gated** to **self-adjointness-gated**: the missing ingredient is the self-adjoint operator behind Frobenius (Hilbert-Pólya), and R1 (facet A, sourcing) and M4 (facet B, polarization) are two faces of that one missing operator. The graph proven world confirms this from three sides: the sourcing gap (#140), marginal positivity as the universal-cover extremal bound (#141), and the archimedean place as the atomic-flat-to-continuous-never-flat passage (#142). See [`../../experiments/toy/README.md`](../../experiments/toy/README.md).

## Update (2026-07-01, cont.): the circle-rooted engine does not exist; the gate refines to self-adjointness-OR-positivity

The direct follow-up to #140 was executed (survey + [`../../experiments/toy/circle_interlacing.py`](../../experiments/toy/circle_interlacing.py) + adversary, LEARNINGS #143): a circle-rooted variant of the interlacing-families engine, which is what a transfer to the circle-rooted L-polynomial would need, **does not exist in the literature, and the miss is structural**. Two thirds of the engine are already present on the circle (the convolution algebra: Grace-Szegő, Suffridge 1976, Leake-Ryder 2020; the interlacing order: POPUC). The missing third is the extremal-selection step: circle-rootedness is an exact locus with no native one-sided order, and manufacturing the order via $x = T + q/T$ (DiPippo-Howe) re-poses real-rootedness, the thing self-adjointness was paying for.

Two refinements to the gate statement. First, the circle does possess **non-operator** rootedness sources (Lee-Yang/Grace positivity; Suffridge-mesh convolutions), so the honest form is: R1 is **self-adjointness-or-positivity-gated**, and the positivity branch is exactly the all-positive polarity already killed for M4 (#95, #119). Second, an independent classical convergence: the Schur-Cohn certificate (1922) states that circle-rootedness for a self-inversive polynomial is the functional equation (an identical vanishing) plus a Hermitian positive-semidefiniteness, so the century-old root-location corpus already says the circle problem **is** a polarization problem.

## Update (2026-07-01, cont. 2): the counting road lands here; the sharpened WATCH trigger; one object, three names

Three same-day dossiers reach R1 from the counting side (LEARNINGS #145-#147) and sharpen this note in four ways.

- **The counting road dies at R1, not at M4.** The Stepanov-Bombieri engine audit ([`stepanov_engine_audit.md`](stepanov_engine_audit.md), #145): diffed against $\mathrm{Spec}(\mathbb{Z})$, the engine's form-free moves all exist (Arakelov $h^0$ / Bost, the Siegel lemma, the product formula, Landau's conversion), and the two moves that fail are both Frobenius-powered: S1 (the graph; the only endomorphism of $\mathbb{Z}$ is the identity, and $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z}) = \mathrm{Spec}(\mathbb{Z})$, the PROP-global rider) and S4 (the cheap-multiplicity derivation). No signature is ever consumed. So R1 is not only the sourcing facet of the form roads' gap; it is the *entire* wall of the counting road, and a supplied R1 would let that road bypass the polarization, needing only one-sided upper bounds ($\psi(x) \le x + O(x^{1/2+\epsilon})$ forces RH by Landau oscillation).
- **The sharpened WATCH trigger (the sieve-side form of the variety-free-purity watch item, #133).** From the parity audit ([`parity_vs_polarization.md`](parity_vs_polarization.md), #146): *unconditional power-saving bilinear Mobius cancellation in the critical narrow range near $\sqrt x$, for a non-algebraic sequence, without finite-field geometry* (the Friedlander-Iwaniec bilinear hypothesis gone variety-free). The qualitative $o(1)$ tier is already crossed variety-free (Matomaki-Radziwill, Tao's entropy decrement), so the trigger is specifically the **exponent**; watch that school for any move from $o(1)$ to a power saving. The same audit makes the sieve corpus a second independent witness for this document's two-tier split: shape sourceable, $\sqrt q$-strength variety-gated.
- **Vojta's shape constraint on the missing operator.** Vojta's CIME notes, Section 29, read verbatim ([`reading_notes/vanFrankenhuijsen-2008-Nevanlinna-RH.md`](reading_notes/vanFrankenhuijsen-2008-Nevanlinna-RH.md), #147): the number-field case has "no known counterpart to the derivative," and the needed arithmetic derivative must live in the **relative** tangent bundle (relative to the arithmetic base), not the absolute one; Conjecture 29.1 (the tautological conjecture) specifies what the operator must do without supplying a mechanism. Any candidate R1 operator should be screened against this constraint (and against the Gauss-lemma floor, since landed as a machine-checked theorem: [`../../experiments/arithmetic_geometric/e2ah_gauss_floor.py`](../../experiments/arithmetic_geometric/e2ah_gauss_floor.py) + [`../../lean/ZetaRH/GaussFloor.lean`](../../lean/ZetaRH/GaussFloor.lean) #GF-1..#GF-5, LEARNINGS #149; the floor screen comes first, it is the cheapest kill) before anything else.
- **One object, three names.** The convergence of #145-#147 with the standing self-adjointness reading above: the missing object behind R1 appears as the **Frobenius** (the endomorphism; van Frankenhuijsen 2008 openly identifies the Frobenius flow with the derivative operator), the **arithmetic derivation** (its infinitesimal face; over $\mathbb{F}_q$ the one structure $x \mapsto x^{\sqrt q}$ supplies both), and the **diagonal** (its fixed-point geometry; vF's verbatim "there is no diagonal" = #131's PROP-global). M4 is that object's polarization face, R1 its operator face. The rebalance recorded in the spine ([`all_roads_to_the_signature.md`](all_roads_to_the_signature.md) scope correction): M4 is not the unique bottleneck; R1 is a co-equal target.

## Update (2026-07-01, cont. 3): the amplification road lands here too; the four consequence-faces; the W6 spec

The third and last non-polarization proof engine was audited the same day ([`deligne_weil1_engine_audit.md`](deligne_weil1_engine_audit.md), LEARNINGS #148): Deligne's Weil I tensor-power amplification, the engine that proved RH over $\mathbb{F}_q$ while bypassing the standard conjectures. Diffed against $\mathrm{Spec}(\mathbb{Z})$ move by move, it walls at W6 (trace-formula rationality with an invariant-theoretically computed pole budget) plus the PROP-global rider (no family base W1, no Künneth self-powers W8), and never consumes a signature. Three sharpenings for this note.

- **The four consequence-faces.** The missing operator behind R1 + M4 now has four named consequence-faces, each the wall of exactly the engine that consumes it: the **endomorphism** (Stepanov S1, graph vs diagonal), the **derivation** (Stepanov S4, cheap multiplicity; Vojta's relative-tangent-bundle constraint above), the **trace formula** (Weil I W6: rationality with an independently computable pole budget; over $\mathbb{F}_q$ bounded-degree rationality is not a primitive, it IS the Grothendieck trace formula, a Frobenius consequence), and the **polarization** (the Weil route, M4). Over $\mathbb{F}_q$ one structure ($x \mapsto x^q$ acting on a cohomology) supplies all four; over $\mathbb{Z}$ all four are open. This upgrades the two-facet map (facets A/B above) into a four-face map of one object without changing the object count; the one-object-three-names reading (cont. 2) is unchanged, with the diagonal as the shared base rider.
- **The W6 spec (what the trace-formula face demands).** A **determinant-class trace formula with an independently computable pole budget**: a carrier on which $\xi(s)$ is the regularized characteristic polynomial of one operator (zeros = spectrum, all singularities accounted, so nuclear/trace-class per weight, not merely a distributional trace; every candidate in [`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md) realizes the trace, none the determinant), with enough symmetry that the pole budget of every powered object is computed without reading the zeros (K1-cleanness), plus a monoidal/Künneth structure to power the carrier. That is Deninger's program spec, re-derived from an engine with no cohomological wish-list: independent corroboration that the spec is forced, not aesthetic. The measured size of the missing face: with W6 absent, positivity plus Landau reach exactly the convergence edge, and the amplification road's all-$k$ closure over $\mathbb{Z}$ is the Lindelöf hypothesis (Titchmarsh Ch. XIII), so **the Lindelöf-RH gap is the measured size of the missing W6**. The WATCH list accordingly gains its third face: alongside the variety-free purity theorem (#130/#133) and the sieve-side bilinear trigger (#146, above), *any determinant-class trace formula for $\zeta$ with an independently computable pole budget/spectrum* is an R1 event; the Deninger-adjacent and Weil-étale literatures are where it would surface. Three analytic shapes, one R1 slot.
- **The not-M4 certificate (purity without polarization).** Weil I proves RH over $\mathbb{F}_q$ while the Hodge standard conjecture (M4's $\mathbb{F}_q$ form) remains open there to this day (Milne 2015, p. 42: beyond surfaces almost nothing is known in characteristic $p$; Ancona 2021 covers abelian fourfolds only). So facet A (purity) is produced at the theorem level without facet B (polarization) ever being produced: the two facets split in proof-space, not just conceptually. This is the producer-side dual of the parity audit's consumer-side finding (#146: sieves consume purity moduli, discard signs); the two audits close the loop from both directions. Reading-depth honesty: the audit's engine skeleton is verified against Milne (arXiv:1509.00797, read in full), which follows Deligne 1974 and Katz 1976; Katz was located but not text-readable this session, and Deligne 1974 was bibliographically verified only.

## Update (2026-07-09): the ultralimit face of R1; NG1 is limit-independent rigidity; the WATCH slot gains a two-conjunct clause

The one published global characteristic-0 Frobenius was screened (LEARNINGS #156,
[`model_theoretic_frobenius.md`](model_theoretic_frobenius.md)): the ultraproduct
$K = \prod_p \overline{\mathbb{F}}_p/\mathcal{U}$ carries a genuine non-identity automorphism $\sigma$
(coordinatewise Frobenius; $(K,\sigma) \models$ ACFA) with the only quantitative fixed-point theory in
characteristic 0 (Hrushovski's twisted Lang-Weil). Four sharpenings for this note.

- **NG1: the S1 "only endomorphism is the identity" line is limit-independent rigidity, not a fact about
  $\mathbb{Z}$'s smallness.** Every unital ring endomorphism of every unital ring fixes the prime ring
  pointwise, and fixes $m/n$ wherever $n$ is invertible; Fermat's little theorem is the coordinatewise
  witness for $\sigma$ ($\sigma = \mathrm{id}$ on the diagonal $\mathbb{Q}$, whose image is $K$'s prime
  field). The rigidity holds in every receptacle where $\mathbb{Q}$ is generated by $1$: ultraproducts,
  Witt ultraproducts, and, decisively, the index-set-preserving adele ring $\mathbb{A}_\mathbb{Q}$ (every
  standard integer is a unit there, so the one-line argument runs verbatim). Consequence for R1: **the
  missing operator cannot act on the arithmetic through a ring endomorphism of anything**; it must move
  arithmetic by non-endomorphism means (a correspondence on a bigger space, a flow, an operator on a
  function space), which is now a screened-in-advance clause rather than an observed pattern of the
  survivors (Connes, Deninger, vF's derivative).
- **NG2: no index-set-quotienting limit over the primes can carry the explicit formula's prime sum.**
  Proven in three tiers ($\mathcal{U}$-invariance vs delete-$p{=}2$; supersimplicity vs interpreting
  $(\mathbb{Z},+,\times)$; the ZFC-clean finite-or-continuum dichotomy for internal sets, so no twist has
  the countable prime-indexed diagonal as fixed set), with the full-nonstandard-universe tier conservative
  (MECHANISM). The #153 glue must be metric/archimedean-aware, not elementary.
- **The corrected WATCH-slot clause (necessary conditions only).** Any candidate R1 filler must be
  **index-set-preserving AND non-endomorphism-shaped**. The first conjunct alone is provably insufficient
  (the adele witness above: index-preserving, yet NG1-rigid); the second is NG1's and is limit-independent.
  Restricted products genuinely do carry the prime sum (Tate's thesis), which is why the quotienting/
  preserving distinction must be pinned when this clause is applied.
- **Two published pointers.** Cherlin-Jarden (cited via Hrushovski math/0406514 p. 6; primary source not
  yet pulled): the ACFA generic automorphism does not live on $\bar{\mathbb{Q}}$ or on any field of finite
  transcendence degree, a published negative at exactly the global base an application would need.
  Dor-Hrushovski arXiv:2212.05366 (WATCH): the valued-field continuation of the Frobenius limit theory,
  the one corner of the corpus moving toward L-functions (transformal zero-cycles "encapsulate" zeta/L-data,
  per Hrushovski's v2 abstract); re-check periodically for any archimedean or global place entering.

K1 status of the corpus itself: every known proof of the twisted Lang-Weil estimate consumes Deligne
purity (Hrushovski Prop 11.11 verbatim; Shuddhodan-Varshavsky; Bourbaki 2308.16132), and untwisted
Lang-Weil consumes Weil 1948, so the model-theoretic Frobenius is strictly downstream of RH over
$\mathbb{F}_q$: consistent with, and a fourth witness for, this document's central regularity (no
variety-free source of $\sqrt q$-strength purity).

## Update (2026-07-10): the wild ingredient is the archimedean ORDER, not tameness; the R1 filler must inject $S(f)$ archimedeanly

The #156 Section-10 heuristic ("a structure too tame to interpret arithmetic cannot state the summed explicit
formula") was sharpened and partly corrected (LEARNINGS #157, [`tameness_trade.md`](tameness_trade.md)). The net
is a definability-side RE-CONFIRMATION of the #62/#153 archimedean-lattice reading, not a new theorem, and it
tightens the WATCH clause above.

- **The R1 / $S(f)$ obstruction is the archimedean order, not tameness.** The first-draft claim "a tame (simple/
  NIP) structure cannot definably carry the primes" is **REFUTED** by Kaplan-Shelah (arXiv:1601.07099, Thm 1.2,
  read at source): under Dickson, $\mathrm{Th}(\mathbb{Z},+,\mathrm{Pr})$ WITHOUT order is decidable and
  **supersimple** of U-rank 1, so a maximally-tame structure DOES carry the prime predicate as a definable set.
  What flips supersimple to full arithmetic (SOP + IP, wild) is the **archimedean ORDER** coupled to $+$ and the
  primes: Bateman-Jockusch-Woods use $\mathrm{Th}(\mathbb{N},+,\mathrm{Pr})$ WITH order (mod Dickson it defines
  $\times$), and Poizat / Point-Schmidt show $\mathrm{Th}(\mathbb{Z},+,P_q)$ (a sparse multiplicative set, no
  order) is superstable. So the ring/difference-field worlds (ACFA, the ultraproduct $K$) fail to carry
  $S(f)=\sum_n\Lambda(n)f(\log n)$ for **lack of the archimedean order** (the incommensurable $\{\log p\}$
  scaling, #62/#153), reinforced by but not caused by supersimplicity. This is exactly the "$\log p$ is not in
  the language of rings" point (#62/#153) met from the definability side, and it identifies the missing
  ingredient of the R1 filler with precision: the ORDER-BEARING archimedean data, not the bare prime set and not
  tameness per se. The unconditional keystone ("ordered prime structure forces $\times$ without Dickson") is
  OPEN, so this is a conditional-plus-open sharpening, not a floor under R1.
- **The saturation face is orthogonal to the RH engine.** Lemma P3 (in any $\aleph_1$-saturated structure no
  countably-infinite set is definable over countable parameters) generalizes #156's NG2(iii) off the
  ultraproduct and kills the standard-prime diagonal for tame AND wild saturated models alike, but the structure
  that CARRIES the formula is the standard $(\mathbb{N},+,\times)$, which is not saturated. So the saturation leg
  forecloses the "twist a saturated tame world to get the prime diagonal" move (the #156 concern) and nothing
  more; the R1-relevant content is the order leg above.
- **C3: the filler must inject $S(f)$ archimedeanly (the survivor-class split).** The #156 survivor class splits
  by the coordinate "does it carry $S(f)$": Connes (scaling flow $\mathbb{R}^\ast_+\subset C_k$ on
  $L^2(\mathbb{A}/k^\ast)$), CCM (prolate/Sonin + the periodization map $E$ on the log-line), and Deninger
  (foliated $\mathbb{R}$-flow, closed-orbit lengths $\log p$) all reach $S(f)$ and each does so by coupling the
  discrete prime index to an EXTERNAL archimedean object (MECHANISM, forced by ingredient 3: any object
  outputting the real number $S(f)$ must contain $\mathbb{R}$ with $\log$, convergence, and the external $f$).
  Borger is the odd one out: it carries the multiplicative Euler PRODUCT, all primes non-invertible, no $\log$,
  no summation, so it does NOT carry $S(f)$ at all; pushing it to a trace formula requires the multiplicative
  completion $\Phi_t=\prod_p\psi_p^{t/\log p}$ = the archimedean injection (the R4 hybrid), landing it back in
  the analytic family with Connes' K1 wall. So the WATCH clause above gains a corollary: **any R1 filler that
  reaches $S(f)$ injects it through an order-bearing archimedean object; the alternative inside first-order
  tameness is not internal definition (that requires going wild) but carrying only the Euler product.** As a
  reading (HEURISTIC), this is why the CCM Section-7 = M4 wall is archimedean not geometric: the Section-7 objects
  live verbatim on the archimedean injection line, so a better geometric substrate (Borger / CC-2026) does not
  move the wall.

## Update (2026-07-11): the W6 pole-budget clause cannot be discharged by counting alone on the form side

A form-side check of the W6 spec's counting face (the Hamburger-pin probe, [`experiments/spectral/e1m_hamburger_pin.md`](../../experiments/spectral/e1m_hamburger_pin.md), LEARNINGS #160): no budget-substitution converse theorem exists in the literature (surveyor-verified absence), and the bare pin "FE + order-1 growth + RvM budget $\Rightarrow F = c\,\Xi$" is PROVEN FALSE by an explicit K1-clean relocation family with identical counting to O(1). So the W6 spec's "independently computable pole budget" is necessary fuel but can never by itself force the identification of a candidate determinant with $\xi$ on the form side; the identifying clause is the additive lattice (Hamburger's Dirichlet abscissa, i.e. the #152 fourth clause), and at the CCM family that clause is conditionally equivalent to the Section-7 identification itself (reformulated, not reduced).

## Update (2026-07-11, later): the S4 face gets a precise carrier question; the WATCH list gains its fourth analytic shape

The Landau one-sided dossier ([`landau_one_sided.md`](landau_one_sided.md), LEARNINGS #161, adversary-reconciled against the e1n prime-comb measurements) makes the S4 face of the counting road (cont. 2 above: "a supplied R1 would let that road bypass the polarization, needing only one-sided upper bounds") a PRECISE question on a concrete carrier. Theorem A there is PROVEN classical: $\psi(x) \le x + C_\epsilon x^{1/2+\epsilon}$ for every $\epsilon$ forces RH, upper bound only, Euler-gated at comb nonnegativity (D-H cannot pose it; Beurling runs it but nothing forces the bound: a translator, not a discriminator). Its bridge to the finite-$\lambda$ CCM family (BRIDGE-H) was adversary-corrected to be layer-dependent: the below-horizon transfer is exact and VACUOUS at the input layer, and FALSE without an error term at the built-object layer (e1n: comb-mass errors +4-9 percent, ~3 percent floor not shrinking). What survives is exactly an S4/R1 question: **can the CCM $D_{\log}$ carrier PROVE a $\lambda$-uniform one-sided upper bound on $\psi$ operator-theoretically, i.e. is there a Spec(Z) analogue of Stepanov's S4 cheap-multiplicity mechanism on this carrier, without passing through a positivity?** In that reading (and only that reading) the finite-$\lambda$ wall reroutes from M4 to R1's S4 face; e1n's measured mixed-sign comb error (one-signed within builds, +, +, +, - across them) locates the obstruction at the $\lambda$-uniformity joint. The WATCH list (cont. 3 above: variety-free purity #130/#133; the sieve-side bilinear trigger #146; a determinant-class trace formula with an independently computable pole budget #148) accordingly gains its FOURTH analytic shape: *a $\lambda$-uniform operator-theoretic one-sided upper-bound mechanism on a determinant-class carrier* (a cheap-multiplicity engine rather than a trace formula or a positivity). Four analytic shapes, one R1 slot. Posed, not answered; nothing here supplies the mechanism.

**Update (2026-07-11, later still): the fourth shape now carries a measured negative baseline, a forcing question, and a screen** (LEARNINGS #162, [`s4_carrier_audit.md`](s4_carrier_audit.md)). The first survey + probe round on the shape found both literature slots VERIFIED EMPTY (no Stepanov engine on any archimedean carrier; no one-sided extremal problem ever posed in a Sonin space, no prolate dimension count ever connected to an arithmetic upper bound) and measured every known cheap mechanism at its proven ceiling on the newest carrier: the majorant/sieve family is factor-2-ceilinged (parity, #146; Siegel-zero sharp, Granville), the band-limited pairing is family-universally divergent without a horizon (the carrier's $p \le \lambda^2$ injection horizon is exactly the required device), the dimension budget is NOT the binding constraint (ratio $3.5\times10^{-3}$ at $x = 10^6$, $\to 0$), and cheap multiplicity at $\{\log p\}$ is absent under five adversarial subspace families while being EXACT at commensurate combs: the S4 absence on the carrier IS the $\mathbb{Q}$-linear independence of $\{\log p\}$, the additive-lattice wall met from the extremal-function side. The shape's forcing question is now a banked SPEC (a $\lambda$-uniform, well-conditioned rank collapse at $\{k \log p\}$ at cost $o(M)$, restoring the linear Stepanov pairing, sourced by an identity that fails for perturbed logs), and its screen is the adversary-verified DMV kill (any candidate whose inputs a $\theta > 1/2$ Beurling system possesses is pre-killed at every exponent below 1; escapes: the additive lattice, the FE, or the one unsourced $\theta \le 1/2$ corner).

## References

- Peter Sarnak, *Notes on the Generalized Ramanujan Conjectures*, Clay Math. Proc. 4 (2005), pp. 659-666 (the decisive reference: proven purity = geometric; the holomorphic-vs-Maass split; "no algebro-geometric moduli interpretation" for the non-Hermitian case).
- P. Deligne, *La conjecture de Weil II* (purity from Frobenius on étale cohomology of varieties).
- J.-M. Fontaine, B. Mazur, *Geometric Galois representations* (the conjecture); M. Kisin, *The Fontaine-Mazur conjecture for $GL_2$*, JAMS 22 (2009); M. Emerton (completed cohomology).
- L. Lafforgue (function-field GRC via moduli of shtukas); cf. arXiv:2204.06053; Rapoport, *The work of Laurent Lafforgue*.
- *On the Riemann Hypothesis for Drinfeld Modules*, arXiv:2512.12374 (purity for $t$-motives, function-field only).
- P. Scholze, *On torsion in the cohomology of locally symmetric varieties*.

## Cross-references

- [09A Section 6D](research_directions/09A_ahk_arithmetic_lattice.md) (where R1 was named), [`../../experiments/arithmetic_geometric/e2zb_super_ahk_recursion.md`](../../experiments/arithmetic_geometric/e2zb_super_ahk_recursion.md) (R2 closes into R1), [`../../experiments/arithmetic_geometric/e2za_ahk_p3_super_graft.md`](../../experiments/arithmetic_geometric/e2za_ahk_p3_super_graft.md).
- [`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md) (the universal gap; R1 is its sourcing facet), [`all_roads_to_the_signature.md`](all_roads_to_the_signature.md) (the thesis R1 refines), [`research_directions/08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md) (M4, facet B).
- LEARNINGS #129 (AHK route closed into R1), #130 (this verification), #140-#142 (R1 is self-adjointness-gated: the graph proven-world probe arc), #145-#147 (the counting road walls here: the Stepanov engine audit, parity-vs-polarization, the van Frankenhuijsen deep read), #148 (the amplification road walls here too: the Deligne Weil I audit, the four consequence-faces, the W6 determinant-class spec), #149 (the Gauss-lemma floor machine-checked: the vF model's S3 slot is provably empty, so the S4/R1 operator is its only open slot), #156 (the model-theoretic Frobenius: NG1 limit-independent rigidity, NG2 generic-prime-vs-prime-sum, the two-conjunct WATCH clause; [`model_theoretic_frobenius.md`](model_theoretic_frobenius.md)), #157 (the tameness trade: the wild ingredient is the archimedean order not tameness, the C3 archimedean-injection survivor-class split; [`tameness_trade.md`](tameness_trade.md)), #161 (the Landau one-sided translator + the S4-on-the-CCM-carrier question, the fourth analytic shape above; [`landau_one_sided.md`](landau_one_sided.md)), #162 (the fourth shape's measured negative baseline + the S4 forcing spec + the DMV screen; [`s4_carrier_audit.md`](s4_carrier_audit.md)).
