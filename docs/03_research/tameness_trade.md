# The tameness trade: is #156's NG2 an instance of a general tameness law?

> A SURVEYOR + BUILDER + ADVERSARY + BUILDER loop (2026-07-10) on the one HEURISTIC that
> [`model_theoretic_frobenius.md`](model_theoretic_frobenius.md) Section 10 handed forward: the ACFA prime-sum
> kill (LEARNINGS #156, NG2) proved that the ultraproduct $K = \prod_p \overline{\mathbb{F}}_p/\mathcal{U}$
> cannot carry the explicit formula's prime side. The residual question: is that an instance of a GENERAL law,
> "a first-order structure tame enough to carry a definable quantitative fixed-point / point-counting theory
> CANNOT define a genuine sum over the primes"? This dossier records the corrected answer at the rigor tier the
> ADVERSARY established. The bottom line is a sharpened negative, and per
> [`../researcher_mindset.md`](../researcher_mindset.md) a corrected negative is a coordinate: this pass moves
> the fault line from "tameness forbids the primes" (false) to "the archimedean ORDER is the wild ingredient"
> (a definability-side re-confirmation of #153/#62), which is a sharper statement of where the R1 filler must
> live, not a wall.
>
> Rigor labels on every claim: **PROVEN** (proof included or one-line reduction to a standard theorem),
> **KNOWN** (published theorem, cited), **CONDITIONAL** (proven modulo a named standard conjecture),
> **REFUTED** (a stated claim disproved by a cited theorem), **MECHANISM** (precise statement, no known
> counterexample, not reduced to a theorem), **HEURISTIC** (directional), **OPEN**. No em dashes anywhere.
>
> Provenance: the working dossiers (SURVEYOR, BUILDER, ADVERSARY, survivor-screen BUILDER, with the ADVERSARY's
> in-place corrections) live in gitignored `scratchpad/tameness_trade/{01_surveyor,02_builder,03_adversary,04_survivor_screen}.md`.
> This document is self-contained; nothing below depends on those files surviving. The single primary source
> read at length this pass is Kaplan-Shelah arXiv:1601.07099 (PDF: abstract, introduction, Section 3); the rest
> is standard neostability and definability-of-arithmetic knowledge, tagged where load-bearing.

## 1. The question, and why it splits in two

The target functional is the explicit formula's prime side,
$$S(f) \;=\; \sum_p \sum_{k\ge 1} (\log p)\, f(k\log p) \;=\; \sum_{n=1}^{\infty} \Lambda(n)\, f(\log n),$$
the integration of $f\circ\log$ against the von Mangoldt measure (the rewrite is exact: $\Lambda(n) = \log p$
when $n = p^k$, else $0$; **PROVEN**). The #156 dossier proved the ACFA instance: no twist, correspondence, or
internal definable-with-parameters construction on $K$ has the standard-prime diagonal as its fixed-point set,
so $K$ cannot carry $S(f)$ internally. The Section 10 HEURISTIC asked whether this is a corollary of a general
"tameness cannot carry the prime sum" theorem.

The main structural finding of this pass is that the general law, as #156 bundled it, splits into **two
logically independent legs that land at different tiers**. Naming them apart is the pass's contribution:

- **Leg A (saturation).** In any $\aleph_1$-saturated structure the standard-prime diagonal is undefinable, so
  $S(f)$ is external, for TAME and WILD structures alike. **PROVEN**, but the work is done by saturation, not
  tameness.
- **Leg B (tameness forbids the prime set).** "A tame structure cannot definably carry the primes" is
  **REFUTED as stated**. The correct fault line is the archimedean ORDER coupled to $+$ and the primes, not the
  bare prime set.

The two legs are complementary, not redundant: each independently expels the standard primes from the inside of
$K$ (saturation makes any definable infinite set uncountable; the missing order makes the ORDERED prime sum
inexpressible). But neither delivers the general tameness theorem #156's heuristic hoped for, and the second is
false in the form the heuristic assumed.

## 2. Leg A: saturation, not tameness (PROVEN, with an orthogonality caveat)

**Lemma P3 (saturation kills countable definable sets). PROVEN.** Let $M$ be $\aleph_1$-saturated and let
$D \subseteq M$ be infinite and definable with parameters from a countable $A \subseteq M$. Then $D$ is
uncountable ($|D| \ge \aleph_1$).

*Proof.* Suppose $D = \{a_0, a_1, a_2, \dots\}$ is countably infinite. The type over the countable set
$A \cup \{a_i : i \in \omega\}$,
$$p(x) \;=\; \{\,x \in D\,\} \;\cup\; \{\,x \ne a_i : i \in \omega\,\},$$
is finitely satisfiable (each finite subset excludes only finitely many points of the infinite $D$). By
$\aleph_1$-saturation (realization of types over parameter sets of size $< \aleph_1$, i.e. countable sets) $p$
is realized by some $b \in D$ with $b \ne a_i$ for all $i$, contradicting $D = \{a_i\}$. $\square$

The hypothesis needs $\aleph_1$-saturation over COUNTABLE parameter sets; $\omega$-saturation (types over finite
sets only) does not close the argument, because the parameter set $A \cup \{a_i\}$ is infinite countable. This is
the one place the statement could be mis-weakened.

**Corollary (the generalized NG2(iii)). PROVEN.** In any $\aleph_1$-saturated $M$, no countably infinite subset
is parametrically definable. In particular the standard-prime diagonal $\{d(2), d(3), d(5), \dots\}$ (countable)
is not definable with parameters, and neither is any twist's fixed-point set equal to it. **This is #156's
NG2(iii) with the ultrafilter removed, valid for every $\aleph_1$-saturated model of every theory.** No CH, no
$\{0,1\}^\omega$ branching, no supersimplicity. Countably-indexed non-principal ultraproducts are
$\aleph_1$-saturated (Chang-Keisler 6.1.1), so P3 applies to $K$ and reproduces exactly the NG2(iii)
branching-cardinality kill; the ultrafilter branching was the concrete face of countable saturation. (Scope
note: NG2(iii) as printed is about all INTERNAL sets, a broader class than parametrically-definable sets; P3
delivers the definable-set version, which suffices for the twist kill because a twist $\sigma\circ\phi$ with
$\phi$ a formula has a parametrically-definable fixed set. P3 subsumes the application; it does not literally
re-prove NG2(iii)'s stated generality.)

**The critical honesty flag: P3 uses saturation, not tameness.** It applies verbatim to a WILD
$\aleph_1$-saturated structure. Test: let $M$ be an $\aleph_1$-saturated (nonstandard) model of true arithmetic
$\mathrm{Th}(\mathbb{N},+,\times)$. Then $M$ interprets arithmetic (it is a model of it) and has an internal von
Mangoldt function and internal summation $\sum_{n\le X}\Lambda(n)g(n)$ for internal $g$ and nonstandard $X$; yet
$M$ does not define the STANDARD prime sum $S$, because (a) the standard cut $\mathbb{N}\subset M$ is not
definable (overspill in nonstandard models of PA; **KNOWN**), so "sum over exactly the standard primes" is not
internal, and (b) $f$ is an external Schwartz function. The internal nonstandard sum $\sum_{n\le X}\Lambda(n)g(n)$
is a DIFFERENT object (nonstandard range, internal $g$, nonstandard value), so it does not rescue the wild model.
So in the $\aleph_1$-saturated formalization NOBODY, tame or wild, internally defines $S$: the kill is carried by
saturation plus the externality of $f$, and the `simple`/`NIP` hypothesis contributes nothing.

**Caveat (ADVERSARY Attack 1c, load-bearing).** The structure that actually CARRIES the explicit formula is the
STANDARD $(\mathbb{N},+,\times)$: primality is definable, $\Lambda$ is definable, and the external sum against
$f$ is a well-defined standard real. The standard model is NOT $\aleph_1$-saturated. So Leg A kills $S$ only in
the SATURATED formalization, which is not the natural home of the RH engine. **Leg A is therefore orthogonal to
the RH-engine question**: it forecloses exactly the "twist a saturated tame world to get the prime diagonal as a
fixed set" move that #156 was screening, and nothing more. The substantive "can a tame engine carry the formula"
content is entirely in Leg B. This is a sharpening of #156, not a re-expression: NG2(iii) was never a tameness
fact, so the genuine misattribution is in Section 10's heuristic sentence (which credits the ACFA kill to
NG2(ii) = supersimple-cannot-interpret-arithmetic), corrected in Section 5.

## 3. Leg B: the tameness leg is refuted; the order is the wild ingredient

The genuine tameness content is the interpretation direction: does carrying the prime data internally force
interpreting $(\mathbb{N},+,\times)$, hence wildness (SOP and IP, not simple and not NIP)? The surveyor and the
first builder located the fault line at the bare prime SET. That is **REFUTED**.

### 3.1 The counterexample (Kaplan-Shelah, arXiv:1601.07099)

**KNOWN (read at source this pass).** Kaplan-Shelah, "Decidability and classification of the theory of integers
with primes" (2016), Theorem 1.2: **assuming Dickson's conjecture (D), the theory $\mathrm{Th}(\mathbb{Z},+,0,1,\mathrm{Pr})$
(the primes with addition, NO order) is decidable, unstable, and SUPERSIMPLE of U-rank 1.** (Theorem 3.7:
$\mathrm{Th}(\mathbb{Z},+,\mathrm{Pr})$ has IP unconditionally.) So a **supersimple structure, maximally tame in
the simple hierarchy, carries the prime predicate $\mathrm{Pr}$ as a definable set.** The claim "if $M$ is simple
then $M$ does not define the primes as a set" is false.

The wild direction is a DIFFERENT structure. Kaplan-Shelah cite, as a contrast (introduction, verbatim): "In
[BJW93, Woo13], they proved that assuming Dickson conjecture, $\mathrm{Th}(\mathbb{N},+,0,\mathrm{Pr})$ is
undecidable and even defines multiplication. It follows immediately that
$\mathrm{Th}(\mathbb{Z},+,0,1,\mathrm{Pr},<)$ is undecidable." So the undecidable, multiplication-defining base
is $\mathrm{Th}(\mathbb{N},+,\mathrm{Pr})$ over $\mathbb{N}$ (where $<$ is free from $+$), equivalently
$\mathrm{Th}(\mathbb{Z},+,\mathrm{Pr},<)$ with the order added. Two things follow, both damaging to the
first-draft framing:

- **Bateman-Jockusch-Woods use full ADDITION, not "only successor".** The first builder's "BJW forces arithmetic
  from the primes with only successor $(\mathbb{N},S,\mathrm{Pr})$" is factually wrong; the base is
  $(\mathbb{N},+,\mathrm{Pr})$.
- **The fault line is the archimedean ORDER coupled to $+$ and the primes, not the prime set.** The order-free
  additive prime structure is supersimple (tame); adding the order (present over $\mathbb{N}$ for free, absent
  over $\mathbb{Z}$) flips it to full arithmetic (maximally wild), CONDITIONAL on Dickson.

Reinforcing datum (KNOWN, in Kaplan-Shelah's bibliography): Poizat [Poi14, Thm 25] and Point-Schmidt [PS14] show
$\mathrm{Th}(\mathbb{Z},+,P_q)$ (powers of $q$) is SUPERSTABLE of U-rank $\omega$. Another tame structure
carrying a sparse multiplicatively-defined set. So "a sparse multiplicative set forces wildness" is wrong twice
over; it is the coupling to the ORDER that does.

### 3.2 What survives: the ordered form, conditional, with the keystone open

The corrected honest statement of the tameness leg:

> **Leg B (corrected). CONDITIONAL on Dickson.** A simple or NIP structure cannot carry the ORDERED prime
> structure (the primes with the ambient additive order, i.e. the log-line ordering the explicit formula already
> carries), because that structure interprets $(\mathbb{N},+,\times)$ (Bateman-Jockusch-Woods, mod Dickson) and
> so has SOP and IP. The ORDER-FREE additive prime set is compatible with supersimplicity (Kaplan-Shelah).

Two residual gaps keep this from being a clean theorem. First, the reduction from an internal ORDERED prime set
to BJW's ambient $(\mathbb{N},+,\mathrm{Pr},<)$ is not exhibited: "next prime on the prime set" is not
"successor/addition on $\mathbb{N}$," so even conditionally the internal-prime-set hypothesis does not yet yield
BJW without strengthening it to carry the ambient additive order. Second and decisive:

> **The keystone (OPEN).** Whether the ordered additive prime structure forces $\times$ WITHOUT Dickson is a
> genuine open problem in arithmetic definability. Unconditionally, whether $(\mathbb{N},+,\mathrm{Pr})$ or
> $(\mathbb{N},+,\Lambda)$ interprets $\times$ is OPEN. The IP of $(\mathbb{Z},+,\mathrm{Pr})$ is unconditional
> (Kaplan-Shelah Thm 3.7), but IP alone does not give arithmetic.

The signature half is clean and KNOWN, and it is what actually kills ACFA: o-minimal structures cannot define
any infinite discrete set (definable subsets of the line are finite unions of points and intervals), so no
o-minimal structure defines $\{\log p\}$ even though it carries each value $\log p$ as an element ($\mathbb{R}_{\exp}$
is o-minimal by Wilkie 1996 and has $\log$, but the SET $\{\log p\}$ is not definable); and ring-language tame
structures (ACF, pseudofinite fields, ACFA) have no archimedean order at all, so $\{\log p\}$ is not even
expressible. This is the #62/#153 point ("$\log p$ is not in the language of rings") met from the definability
side.

### 3.3 The net for ACFA, and the re-confirmation of #153/#62

The corrected reading of why the ACFA / ultraproduct world fails to carry $S(f)$: **it is the ABSENCE OF THE
ARCHIMEDEAN ORDER** (no $\{\log p\}$, no incommensurable scaling, #62/#153), REINFORCED by supersimplicity, not
CAUSED by supersimplicity alone. ACFA has no order at all, so it could carry a bare order-free prime predicate
the way $(\mathbb{Z},+,\mathrm{Pr})$ does and stay supersimple; what it cannot carry is the ordered, log-weighted
sum. This RE-CONFIRMS #153/#62 from a new (definability) side: the glue the R1 filler needs is archimedean and
order-bearing, exactly the ingredient the ring/difference-field worlds lack. The humbler, correct net is a
re-confirmation of a standing finding, not a new general theorem.

## 4. C3: the survivor screen and the archimedean-injection reading

The survivor-screen BUILDER pass carried the trade back to the #156 survivor class (the four construction shapes
that pass the two-conjunct WATCH clause: index-set-preserving AND non-endomorphism-shaped) and tested a proposed
criterion C3.

**C3 (archimedean injection), final form. MECHANISM.** Every survivor construction that carries the summed
functional $S(f)$ carries it by COUPLING its discrete prime index to an EXTERNAL archimedean object $O$ (a real
line, a flow, a scaling action, an operator on an $L^2$ of the log variable): $\log p$ enters as an archimedean
length / period / frequency living in $O$, and the summation is realized as a distributional trace or a
periodization over $O$, not as an internal definable sum. This is forced, not stylistic: $S(f)$ IS integration
of $f\circ\log$ against the von Mangoldt measure on $\mathbb{R}$, so any object outputting the real number
$S(f)$ must contain a copy of $\mathbb{R}$ with $\log$, convergence, and the external $f$; the tameness trade
(Leg A saturation + Leg B ordered-interpretation) forbids a tame carrier from defining that summation
internally. Within the survivor class the only alternative to archimedean injection is NOT internal definition
(that requires going wild, i.e. interpreting arithmetic and losing tameness); it is to NOT carry $S(f)$ at all.

**The screen table.** WATCH-1 = index-set-preserving; WATCH-2 = non-endomorphism-shaped (both from #156);
$O$ = the archimedean injection object; "$S(f)$ sited" = where the summed functional lives.

| Survivor | WATCH-1 | WATCH-2 | C3 injection object $O$ | $S(f)$ sited |
|---|---|---|---|---|
| **Connes** adele class space (`math/9811068`) | PASS (restricted product over ALL places; trace over all $v$) | PASS (scaling action of $C_k$, a group action) | the scaling flow $\mathbb{R}^\ast_+ \subset C_k$ on $L^2(\mathbb{A}/k^\ast)$; $\log p$ = modulus/period of the local orbit integral; sum = distributional (Guillemin-Sternberg) trace over periodic orbits | **EXTERNAL** (archimedean) |
| **CCM** prolate / scaling site (`2310.18423`, `2511.22755`) | PASS (measure over all of $\mathrm{Spec}\,\mathbb{Z}$) | PASS (periodization $E$, scaling $\vartheta$, Weil-group action) | the prolate/Sonin operator + the map $E(f)(u)=u^{1/2}\sum_n f(nu)$ on the archimedean log-line $\mathbb{R}$; $\log p$ = L-factor frequency in $dm_S$; sum = the archimedean Weil functional $W_\infty$ | **EXTERNAL** (archimedean log-line) |
| **Deninger** foliated flow (ICM 1998, `1807.06400`) | PASS ($\mathbb{R}$-flow glues all closed orbits, one per prime) | PASS (a foliated flow $\phi^t$, not a ring map) | the archimedean foliated flow $\phi^t$; $\log p = l(\gamma)$ = length of a closed orbit; sum = Poisson summation on each orbit circle $\mathbb{R}/(\log p)\mathbb{Z}$ + the Guillemin-Sternberg trace | **EXTERNAL** (archimedean flow) |
| **Borger** $\Lambda$-ring / $\mathbb{F}_1$-descent (`0906.3146`) | PASS (all primes kept NON-INVERTIBLE, $\mathrm{Spec}\,\mathbb{Z}$ alive) | PASS-with-nuance (on $\mathbb{Z}$ every $\psi_p=\mathrm{id}$ by NG1; arithmetic moved by joint $\Lambda$-descent, not a single moving endomorphism) | **NONE internal.** No archimedean line, no $\log$, no summation into $\mathbb{R}$ | **ABSENT** (carries the multiplicative Euler PRODUCT, not the additive sum $S(f)$) |

**Verdict on C3: analytic-family-only, and the split is the finding (MECHANISM).** C3 holds as a genuine common
necessary property for the three survivors that carry $S(f)$ (Connes, CCM, Deninger): each injects ingredient 3
through its named archimedean object. Borger VIOLATES the literal C3, but not by the route C3 excludes (internal
definition); it avoids archimedean injection by NOT carrying $S(f)$ at all: it stops at the multiplicative Euler
product $\zeta(s)=\prod_p\det(1-\psi_p p^{-s}\mid M)^{-1}$, the integral-descent side, all primes non-invertible,
no $\log$, no summation into $\mathbb{R}$. Pushing Borger to a trace formula requires the multiplicative
completion $\Phi_t = \prod_p \psi_p^{\,t/\log p}$ (= Connes' scaling action $U_t$; the R4 hybrid,
[`research_directions/02_borger_connes_hybrid.md`](research_directions/02_borger_connes_hybrid.md) sub-problem 4.2,
and the Deninger dossier), where the $t/\log p$ exponent IS the archimedean injection, at which point Borger
lands back in the analytic family and inherits Connes' K1 wall. So C3 is a **CONDITIONAL UNIVERSAL**: the split
coordinate is exactly "does the survivor carry the additive summed explicit formula $S(f)$," and it partitions
the survivor class into archimedean-injecting {Connes, CCM, Deninger} and integral-descent {Borger}. The split
recurs INSIDE CCM's own program: the $\mathbb{F}_1$ absolute-geometry paper 2606.06604 is the geometric-carrier
thread (no Section 7, no positivity, the scaling-site periodic orbits of length $\log p$ now geometrically
DERIVED via $E_p \cong C_p \times \widetilde{X}_\infty$, not posited) while the analytic prolate thread carries
$S(f)$ and is where positivity lives.

**The archimedean-injection reading of the CCM Section-7 wall. HEURISTIC for the causation, MECHANISM for the
object-coincidence.** The repo's standing M4 wall (LEARNINGS #148/#153/#154) is the CCM Section-7 uniform
determinant-class limit $\hat\xi_\lambda \to \Xi$ (equivalently uniform global Weil positivity) as $S\to$ all
primes, stated in the prolate/Sonin space and the Weil form $W_\infty$ on the real log-line. Those Section-7
objects ARE C3's archimedean injection object for CCM (MECHANISM: the objects coincide, verbatim). The Section-7
difficulty is making the injection uniform as $S\to$ all primes; C3 therefore gives a structural READING (hedged)
of WHY the wall is archimedean and not geometric: the summation $S(f)$ can only be reached by injecting an
archimedean object, so the last hard step (making the sign survive the full injection over all primes) is
necessarily an archimedean-limit step, not a finite-place or geometric-descent step. This matches the repo's
independent #148/#154 diagnosis (all finite/local channels blind; content is the global $S\to\infty$ assembly)
and the "a better geometric substrate does not move the positivity wall" finding
([`reading_notes/Connes-Consani-2026-Absolute-Geometry-SpecZ.md`](reading_notes/Connes-Consani-2026-Absolute-Geometry-SpecZ.md)).
**Mandatory hedge:** this is a reading of known constructions, not a theorem. It does not predict WHETHER the
uniform limit holds (that is RH-equivalent); it says only WHERE the decisive step must live and WHY it is
archimedean. The diagnostic value: do not expect the wall to move by improving the geometric substrate (the
Borger / CC-2026 side), because that side does not carry $S(f)$.

## 5. Correction applied to #156 Section 10

The ADVERSARY's single actionable YES: edit #156's Section 10 heuristic sentence (NOT NG2(iii), which is already
correctly stated as a ZFC/cardinality fact). The correction, applied 2026-07-10 in
[`model_theoretic_frobenius.md`](model_theoretic_frobenius.md) Section 10 and cross-referenced to #157:

- Re-attribute the ACFA prime-diagonal kill to NG2(iii) = saturation (the primary kill, tameness-independent via
  Lemma P3, applies to wild $\aleph_1$-saturated models too), NOT to NG2(ii) = supersimple-cannot-interpret-arithmetic
  (a separate, weaker kill that does not by itself exclude the bare prime set).
- Correct the invariant: the fault line is the archimedean ORDER coupled to $+$ and the primes (BJW/Woods, mod
  Dickson), and the order-free additive prime set is itself supersimple (Kaplan-Shelah Thm 1.2). "Supersimple
  worlds cannot interpret the arithmetic the explicit formula sums over" becomes "supersimple worlds have no
  archimedean order, so they cannot carry the ORDERED, log-weighted prime sum; the order-free additive prime
  predicate is itself supersimple, so the kill is the missing order, not the missing prime set." This aligns
  #153 (archimedean glue) and refutes the "primes-as-a-set is the fault line" reading.

NG2(iii)'s own statement is untouched (it is correct as a ZFC/cardinality fact; Lemma P3 is its saturation face).

## 6. The honest net

- **A corrected negative, framed as a coordinate.** This pass did NOT produce a general tameness theorem. It
  SHARPENED and re-confirmed #153/#62 from the definability side: the R1 filler's obstruction is the archimedean
  ORDER (the incommensurable $\{\log p\}$ scaling), not tameness, and the order-free additive prime set is tame.
  That is a sharper coordinate for where the filler must live, consistent with the #156 survivors (all of which
  inject the order archimedeanly).
- **Leg A survives (PROVEN), Leg B is refuted (REFUTED as stated, CONDITIONAL in corrected form, keystone OPEN).**
  Leg A generalizes NG2(iii) off the ultraproduct via Lemma P3 but is orthogonal to the RH-engine question (the
  carrier is the non-saturated standard model). Leg B's "tame cannot carry the primes" is false by
  Kaplan-Shelah; the corrected invariant is ORDER + $+$ + primes, Dickson-conditional, with the unconditional
  keystone open.
- **C3 stands (MECHANISM / HEURISTIC), reinforced by the order-is-wild finding.** All four survivors pass the
  #156 WATCH clause; the three that carry $S(f)$ inject it archimedeanly, Borger is the odd one out that carries
  the Euler product not the sum; C3 gives the hedged structural reading of why the Section-7 = M4 wall is
  archimedean.
- **The publishable-shaped claim is WITHDRAWN.** The first-draft "no tame counting engine carries the summed
  explicit formula" rested on an inverted central citation (arXiv:1601.07099), a refuted invariant (the bare
  prime set), and an unengaged state-of-the-art corpus. It is recorded here as a POSSIBLE-FUTURE-EXPOSITORY item,
  NOT a result in hand: it could become a legitimate expository structural-obstruction note only after engaging
  the Kaplan-Shelah / Poizat / Point-Schmidt / Bes / Korec corpus with the unconditional keystone honestly
  flagged OPEN. The RH-engine PACKAGING may still be novel (the logical-complexity-of-RH corpus, RH-as-$\Pi^0_1$
  and reverse math of PNT, is about the complexity of the STATEMENT, not the tameness of proof-engine
  STRUCTURES), but "no prior art" as first written overstates the case: the model-theoretic core is published and
  more refined than the first-draft treatment.

## 7. Corpus additions (model theory of arithmetic expansions)

These sit exactly on the load-bearing invariant and were missed by the first survey; they are the honest
required reading for any future expository writeup.

- **Kaplan-Shelah, "Decidability and classification of the theory of integers with primes", arXiv:1601.07099
  (2016). [READ this pass].** Thm 1.2: under Dickson, $\mathrm{Th}(\mathbb{Z},+,\mathrm{Pr})$ (no order) is
  decidable, unstable, supersimple of U-rank 1. Thm 3.7: $\mathrm{Th}(\mathbb{Z},+,\mathrm{Pr})$ has IP
  unconditionally. Cites BJW/Woods for the ordered undecidable base.
- **Bateman-Jockusch-Woods, "Decidability and undecidability of theories with a predicate for the primes", JSL
  58 (1993) 672-687; A. Woods's thesis (1981).** Under Dickson, $\mathrm{Th}(\mathbb{N},+,\mathrm{Pr})$ is
  undecidable and defines $\times$.
- **B. Poizat [Poi14, Thm 25]; Point-Schmidt [PS14].** $\mathrm{Th}(\mathbb{Z},+,P_q)$ (powers of $q$) is
  superstable of U-rank $\omega$: a tame structure carrying a sparse multiplicatively-defined set.
- **A. Bes, decidability survey [Bes01]; I. Korec, list of arithmetic-defining structures [Kor01].** The map of
  which additive-plus-predicate expansions define $(\mathbb{N},+,\times)$.

## 8. Process flag (record it, do not bury it)

A load-bearing [FETCH]-tagged citation (arXiv:1601.07099) was **inverted** by the SURVEYOR: the tag claimed the
paper proves "the linear case of Schinzel's Hypothesis H implies $\times$ is definable in $(\mathbb{N},+,P)$,"
whereas the paper (Kaplan-Shelah) proves the ORDER-FREE additive prime structure is SUPERSIMPLE (tame), the
opposite conclusion, and does not contain the quoted sentence at all (that is the BJW ORDERED result, cited
therein as a contrast). The ADVERSARY's re-fetch of the source caught it. This is a data point that
[FETCH]-tagged citations need independent verification before being treated as load-bearing; the surveyor's own
honesty legend did not hold on this line. For VERIFIER: the #156-arc citation-check target (BJW base signature
$+$ vs $S$, and the exact 1601.07099 statement) is flagged RE-RUN-NEEDED, and any future draft leaning on this
corpus must re-verify at source.

## 9. What this enables / what remains open

- **For BUILDER.** The R1-filler necessary condition is sharpened: the filler must inject the summation through
  an ORDER-BEARING archimedean object (C3), because the archimedean order (not tameness, not the bare prime set)
  is the wild ingredient the ring/difference-field worlds lack. Any proposal of the shape "find a
  supersimple/NIP/o-minimal structure whose internal counting IS the explicit formula" is killed in advance: a
  tame carrier either goes wild (interprets arithmetic, losing the counting uniformity) or injects the sum
  externally (route (b), the three survivors) or does not carry $S(f)$ (route (c), Borger). There is no fourth
  door inside first-order tameness.
- **For ADVERSARY / VERIFIER.** The keystone is the attack surface: proving "$(\mathbb{N},+,\mathrm{Pr})$ or
  $(\mathbb{N},+,\Lambda)$ interprets $\times$ UNCONDITIONALLY" would upgrade Leg B from CONDITIONAL to KNOWN; it
  is a real open problem, not a formality. The two surviving Lean micro-targets are pinning toys only, at their
  real value (Section 10), **both DISCHARGED 2026-07-10** in
  [`../../lean/ZetaRH/TamenessTrade.lean`](../../lean/ZetaRH/TamenessTrade.lean) (sorry-free, axiom-clean):
  **T-TT-1 (#TT-1, DONE)** as the arithmetic core `two_mul_mul_eq` ($2xy=(x+y)^2-x^2-y^2$ over any `CommRing`)
  plus the subtraction-free `two_mul_mul_add_sq_eq` valid over $\mathbb{N}$, chosen over the full `Set.Definable`
  wrapper (a bespoke `FirstOrder.Language` + `Structure` on $\mathbb{N}$ is heavy overhead for a pinning toy with
  no RH content; the identity IS the definability mechanism); **T-TT-2 (#TT-2, DONE)** as the full $\Leftrightarrow$
  `prime_iff_vonMangoldt` (both directions proved) over `ArithmeticFunction.vonMangoldt` in $(\mathbb{N},<,\Lambda)$.
  In the same module the NG1 kernel #MTF-1 gained an INDEPENDENT second formalization `ng1_rigidity_indep`
  (consensus witness #2). The load-bearing content (Lemma P3, BJW, the transfer lemma) remains beyond current
  Mathlib (no developed theory of saturation, simplicity, SOP, or interpretation-transfer).
- **Remains open.** (1) The unconditional keystone (ordered prime structure forces $\times$ without Dickson).
  (2) Whether $(\mathbb{N},+,\Lambda)$ (von Mangoldt, closer to the explicit-formula datum than the bare
  predicate) interprets $\times$. (3) The precise ordered-tame signature-obstruction statement for the
  NIP-with-order case (the o-minimal case is clean; dp-minimal/distal may need care). None of these blocks the
  net finding, which is the definability-side re-confirmation of #153/#62.

## Cross-references

- [`model_theoretic_frobenius.md`](model_theoretic_frobenius.md): the #156 dossier this sharpens (NG1/NG2, the
  two-conjunct WATCH clause, Section 10 heuristic corrected 2026-07-10).
- [`sourcing_gap_r1.md`](sourcing_gap_r1.md): the R1 sourcing gap; the 2026-07-10 update records the
  order-is-the-wild-ingredient coordinate and C3.
- [`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md): the survivor class and the M4 = Section-7
  wall C3 reads.
- LEARNINGS #157 (this arc), #156 (the parent), #153/#62 (the archimedean-lattice wall re-confirmed), #148/#154
  (the M4 = Section-7 wall), #133 (the Level-4 framing / frame-audit discipline).
