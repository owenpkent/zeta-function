# The tameness trade: assembling the explicit formula's prime side is a tame/wild fault-line phenomenon

> **Status: DRAFT, expository structural-obstruction note (2026-07-10).** A research note that locates,
> from the model theory of arithmetic definability, where the prime side of the Weil explicit formula can
> and cannot be assembled inside a first-order structure. It is **not** a proof and claims **no** new
> theorem about RH: the contribution is the **synthesis packaging** of a developed but scattered corpus
> (Kaplan-Shelah, Bateman-Jockusch-Woods, Boffa, Poizat, Palacin-Sklinos, Bes, Korec, Green-Tao) around
> one target functional, together with an honest map of what is PROVEN, what is CONDITIONAL on Dickson's
> conjecture, and what is OPEN. Companion to the obstruction-map survey
> ([`../obstruction_map/obstruction_map.md`](../obstruction_map/obstruction_map.md)); this note is the
> definability-side detail behind that survey's Section 6.2 (the Davenport-Heilbronn / archimedean-order
> firewall). Source dossier: [`../../docs/03_research/tameness_trade.md`](../../docs/03_research/tameness_trade.md)
> (self-contained), LEARNINGS #157, and [`../../docs/03_research/model_theoretic_frobenius.md`](../../docs/03_research/model_theoretic_frobenius.md) #156.
>
> Rigor labels, used throughout: **PROVEN** (proof included or a one-line reduction to a standard
> theorem), **KNOWN** (published theorem, cited), **CONDITIONAL** (proven modulo a named standard
> conjecture), **REFUTED** (a stated claim disproved by a cited theorem), **MECHANISM** (precise
> statement, no known counterexample, not reduced to a theorem), **HEURISTIC** (directional), **OPEN**.
> No em dashes anywhere. Distinguishes PROVEN from CONJECTURAL throughout; attributes every result.

## Abstract

The Weil explicit formula couples addition and multiplication in a single functional. Its prime side
$S(f) = \sum_n \Lambda(n)\, f(\log n)$ reads the von Mangoldt function (which is supported on prime
powers, a **multiplicative** datum) against $f$ evaluated on the additive lattice $\{\log p^k\} =
\{k \log p\}$ (an **additive**, order-bearing datum). Any construction that hopes to realize $S(f)$ as
an internal, definable object of some first-order structure must therefore carry both couplings at once.
We ask, at the level of the model theory of additive expansions of $\mathbb{Z}$ and $\mathbb{N}$ by a
prime predicate, whether a **tame** structure (in the neostability sense: simple, or NIP, or o-minimal)
can do this. The answer splits into two logically independent legs at different tiers. **Leg A**
(saturation) is PROVEN but orthogonal to the RH engine: in any $\aleph_1$-saturated model no
countably-infinite set is definable over countable parameters (Lemma P3), so the standard-prime diagonal
is external for tame **and** wild saturated models alike, with the caveat that the structure that
actually carries the formula, the standard $(\mathbb{N}, +, \times)$, is not saturated. **Leg B** (the
tameness claim) is REFUTED as stated: Kaplan-Shelah proved that the order-free additive prime structure
$\mathrm{Th}(\mathbb{Z}, +, \mathrm{Pr})$ is supersimple of U-rank 1 (conditional on Dickson), a
maximally-tame-in-the-simple-hierarchy structure that **does** carry the primes as a definable predicate,
so "tame cannot carry the primes" is false. The correct invariant is the archimedean **order** coupled to
$+$ and the primes: Bateman-Jockusch-Woods use the ordered $\mathrm{Th}(\mathbb{N}, +, \mathrm{Pr})$ and
(conditional on Dickson) recover multiplication, while order-free additive prime sets stay tame
(Kaplan-Shelah), as do order-free $q$-power sets (Poizat, Palacin-Sklinos). This re-confirms the project's
archimedean-lattice obstruction from the definability
side. The **keystone**, whether the ordered prime structure forces multiplication **without** Dickson,
is a genuine open problem in arithmetic definability, and we flag it OPEN. The RH-engine reading is a
hedged mechanism: any counting or point-fixing engine that reaches $S(f)$ must inject it archimedeanly,
which is why the CCM Section-7 = M4 wall is archimedean by necessity rather than geometric. The
contribution is the synthesis, with the keystone open; nothing here is a step toward RH.

## 1. Introduction: one functional, two arithmetics

The Riemann zeta function's arithmetic content is concentrated in one identity, the Weil explicit
formula, whose prime side is the functional

$$S(f) \;=\; \sum_p \sum_{k \ge 1} (\log p)\, f(k \log p) \;=\; \sum_{n=1}^{\infty} \Lambda(n)\, f(\log n),$$

where $\Lambda(n) = \log p$ if $n = p^k$ and $0$ otherwise. The rewrite is exact (**PROVEN**, elementary).
Read structurally, $S(f)$ is the pairing of two different arithmetics:

- The **multiplicative** datum is the support of $\Lambda$, the prime powers, i.e. the factorization
  structure of $\mathbb{N}$. This is what a prime predicate $\mathrm{Pr}$, or the von Mangoldt function
  $\Lambda$, expresses in a first-order language.
- The **additive** datum is the argument $\log n$, which lives on the lattice $\{k \log p\}$. This is an
  ordered, archimedean object: $\log(p^k) = k \log p$ is addition on the log-line, and the lengths
  $\{\log p\}$ are incommensurable reals with a linear order. This is the object the project's earlier
  findings (#62, #153) isolate as "the $\{\log p\}$ lattice".

So $S(f)$ **couples addition (the $\{\log p\}$ lattice) and multiplication (prime factorization) in one
functional**. This note asks a precise version of "where can that coupling live": can $S(f)$ be
**assembled inside a first-order structure**, meaning realized as a definable-with-parameters object of a
structure $M$ in some language, in a way that is **tame** (model-theoretically well-behaved: simple, or
NIP, or o-minimal)?

The question is not idle. The project's R1 sourcing facet (produce a weight-1 carrier for $\zeta$ without
already assuming a variety) and the survivor class of constructions that reach $S(f)$ (Connes, CCM,
Deninger) all live or die on how the prime index couples to an archimedean object. A general theorem
"tame structures cannot carry the prime sum" would put a model-theoretic floor under R1. The finding of
this note is that no such general theorem is available: the question splits into two legs, one PROVEN but
orthogonal to the RH engine, the other REFUTED in the form the floor would need, with the unconditional
keystone OPEN. What survives is sharper than the failed general law and points in the same direction as
the rest of the project's map: the wild ingredient is the **archimedean order**, not tameness and not
the bare prime set.

A word on posture, following [`../../docs/researcher_mindset.md`](../../docs/researcher_mindset.md). This
note documents a corrected negative. A first-draft claim ("no tame counting engine carries the summed
explicit formula") rested on an inverted central citation and a refuted invariant, and is **withdrawn**
(Section 7). We do not restore it. A corrected negative is a coordinate: this pass moves the fault line
from "tameness forbids the primes" (false) to "the archimedean order coupled to $+$ and the primes is the
wild ingredient" (a definability-side re-confirmation of #153/#62), which sharpens where the R1 filler
must live rather than walling it off.

## 2. What "assemble it in a first-order structure" means

Fix a first-order language $L$ and an $L$-structure $M$. To say $M$ **carries $S(f)$ internally** is to
ask for two things at once:

1. The **index set** (the primes, or the prime powers, or the von Mangoldt weighting) is definable in
   $M$ with parameters. This is a statement about the multiplicative datum: e.g. $\mathrm{Pr}(x)$ or the
   graph of $\Lambda$ is an $L$-formula.
2. The **summation against $f$** is an internal operation of $M$ producing the real number $S(f)$. This
   is a statement about the additive/archimedean datum: it needs the log-line, its order, the lengths
   $\log p$, convergence, and the external test function $f$.

The relevant tame/wild axis is the neostability classification of the theory $\mathrm{Th}(M)$. The
baselines are KNOWN (Kaplan-Shelah, page 1): Presburger arithmetic $T_+ = \mathrm{Th}(\mathbb{Z}, +, 0, 1)$
is superstable of U-rank 1, and $T_{+,<} = \mathrm{Th}(\mathbb{Z}, +, 0, 1, <)$ is dp-minimal, hence NIP.
Both are maximally tame. The wild extreme is full arithmetic $\mathrm{Th}(\mathbb{N}, +, \times)$, which
has the strict order property (SOP) and the independence property (IP), interprets everything, and is
undecidable. The question of this note is exactly which additive-plus-predicate expansion sits where, and
whether the specific object $S(f)$ forces the wild side.

The corpus that answers this is the **model theory of additive expansions of $\mathbb{Z}$ (or
$\mathbb{N}$) by a prime predicate**, a developed area with a precise tame/wild map. It was largely
unengaged by the project's earlier passes; this note engages it. The single primary source read at length
is Kaplan-Shelah, arXiv:1601.07099 (abstract, introduction, Section 3); the rest is standard neostability
and definability-of-arithmetic knowledge, tagged where load-bearing.

## 3. Leg A: saturation is the kill, not tameness (PROVEN, orthogonal)

The first leg is a clean theorem that has nothing to do with tameness. It is included because #156's
NG2(iii) (the ACFA prime-diagonal kill) is exactly its ultraproduct face, and naming the general
mechanism prevents future sessions from re-crediting the kill to simplicity.

**Lemma P3 (saturation kills countable definable sets). PROVEN.** Let $M$ be $\aleph_1$-saturated and let
$D \subseteq M$ be infinite and definable with parameters from a countable set $A \subseteq M$. Then $D$
is uncountable ($|D| \ge \aleph_1$).

*Proof.* Suppose $D = \{a_0, a_1, a_2, \dots\}$ is countably infinite. Consider the type over the
countable parameter set $A \cup \{a_i : i \in \omega\}$,

$$p(x) \;=\; \{\, x \in D \,\} \;\cup\; \{\, x \ne a_i : i \in \omega \,\}.$$

Every finite subset of $p$ excludes only finitely many points of the infinite $D$, so it is satisfiable;
$p$ is finitely satisfiable. By $\aleph_1$-saturation (realization of types over parameter sets of size
$< \aleph_1$, i.e. countable sets), $p$ is realized by some $b \in D$ with $b \ne a_i$ for all $i$,
contradicting $D = \{a_i\}$. $\square$

The hypothesis needs saturation over **countable** parameter sets; $\omega$-saturation (types over finite
sets only) does not close the argument, because $A \cup \{a_i\}$ is infinite. This is the one place the
statement could be mis-weakened.

**Corollary. PROVEN.** In any $\aleph_1$-saturated $M$, no countably-infinite subset is
parametrically definable. In particular the standard-prime diagonal $\{d(2), d(3), d(5), \dots\}$
(countable) is not definable with parameters, and no twist's fixed-point set can equal it. This is
#156's NG2(iii) with the ultrafilter removed, valid for **every** $\aleph_1$-saturated model of **every**
theory: no CH, no $\{0,1\}^\omega$ branching, no supersimplicity. Countably-indexed non-principal
ultraproducts are $\aleph_1$-saturated (Chang-Keisler 6.1.1), so P3 applies to the ACFA ultraproduct
$K = \prod_p \overline{\mathbb{F}}_p / \mathcal{U}$ and reproduces the NG2(iii) kill; the ultrafilter
branching **was** the concrete face of countable saturation.

**The honesty flag: P3 uses saturation, not tameness.** It applies verbatim to a **wild**
$\aleph_1$-saturated structure. Take $M$ an $\aleph_1$-saturated (nonstandard) model of true arithmetic
$\mathrm{Th}(\mathbb{N}, +, \times)$. Then $M$ interprets arithmetic, has an internal von Mangoldt
function and internal summation $\sum_{n \le X} \Lambda(n) g(n)$ for internal $g$ and nonstandard $X$; and
yet $M$ does not define the **standard** prime sum $S$, because (a) the standard cut
$\mathbb{N} \subset M$ is not definable (overspill in nonstandard models of PA, **KNOWN**), so "sum over
exactly the standard primes" is not internal, and (b) $f$ is an external Schwartz function. The internal
nonstandard sum is a **different** object (nonstandard range, internal $g$, nonstandard value), so it does
not rescue the wild model. In the saturated formalization nobody, tame or wild, internally defines $S$:
the kill is carried by saturation plus the externality of $f$, and the simple/NIP hypothesis contributes
nothing.

**Caveat (load-bearing, the orthogonality). PROVEN.** The structure that actually **carries** the
explicit formula is the **standard** $(\mathbb{N}, +, \times)$: primality is definable, $\Lambda$ is
definable, and the external sum against $f$ is a well-defined standard real. The standard model is **not**
$\aleph_1$-saturated. So Leg A kills $S$ only in the **saturated** formalization, which is not the natural
home of the RH engine. Leg A is therefore **orthogonal to the RH-engine question**: it forecloses exactly
the "twist a saturated tame world to get the prime diagonal as a fixed set" move that #156 screened, and
nothing more. The substantive "can a tame engine carry the formula" content is entirely in Leg B.

## 4. Leg B: "tame cannot carry the primes" is REFUTED; the order is the wild ingredient

The genuine tameness content is the interpretation direction: does carrying the prime data internally
**force** interpreting $(\mathbb{N}, +, \times)$, hence wildness? The naive conjecture places the fault
line at the bare prime set. That is **REFUTED**.

### 4.1 The counterexample (Kaplan-Shelah)

**KNOWN (read at source).** Kaplan-Shelah, "Decidability and classification of the theory of integers with
primes" (arXiv:1601.07099, 2016; J. Symbolic Logic 82(3), 2017), **Theorem 1.2** (verbatim): "Assuming
(D), the theory $T_{+,\mathrm{Pr}}$ is decidable, unstable and supersimple of U-rank 1", where
$T_{+,\mathrm{Pr}} = \mathrm{Th}(\mathbb{Z}, +, 0, 1, \mathrm{Pr})$, $\mathrm{Pr}$ the predicate for
primes and their negations, and there is **no order** in the language. (D) is Dickson's conjecture. So a
**supersimple** structure, maximally tame in the simple hierarchy, carries the prime predicate as a
definable set. The claim "if $M$ is simple then $M$ cannot define the primes as a set" is **false**.

The abstract states the contrast directly (verbatim): "This is in contrast with
$\mathrm{Th}(\mathbb{Z}, +, 0, \mathrm{Pr}, <)$ which is known to be undecidable by the works of
Jockusch, Bateman and Woods." And on instability (page 3, verbatim): "To show that $T_{+,\mathrm{Pr}}$ is
unstable we show that it has the independence property (see **Proposition 3.6**). This turns out to follow
from the proof of the Green-Tao theorem about arithmetic progressions in the primes [GT08] (i.e., without
using (D)) ... (but we also show that this follows from (D))." The intro's pointer "(see Proposition 3.6)"
is to the combinatorial input; the theorem that states the result is **Theorem 3.7** ("Without assuming
Dickson's conjecture ... $T_{+,\mathrm{Pr}}$ has the independence property and even the $n$-independence
property"). So the **independence property of the order-free additive prime structure is unconditional**
(Theorem 3.7, resting on Proposition 3.6, from Green-Tao); the decidability and supersimplicity are
conditional on Dickson.

> **Citation structure, on record.** The unconditional IP of $\mathrm{Th}(\mathbb{Z}, +, \mathrm{Pr})$
> is Kaplan-Shelah **Theorem 3.7** ("Without assuming Dickson's conjecture ... has the independence
> property"), whose proof rests on **Proposition 3.6** (the Green-Tao arithmetic-progression lemma: for
> all $n$ and $s$ there is an AP $at+b$ with $at+b$ prime iff $t \in s$). The source dossier
> ([`../../docs/03_research/tameness_trade.md`](../../docs/03_research/tameness_trade.md) Section 3.1) and
> #156 cite Theorem 3.7 for this result, which is **correct**; the intro's pointer "(see Proposition 3.6)"
> is to the combinatorial input inside that proof, not the location of the theorem. Future drafts should
> cite the IP result as Theorem 3.7 (via Proposition 3.6, from Green-Tao).
>
> **Independent re-verification (2026-07-10).** The load-bearing claim, that arXiv:1601.07099 puts the
> order-free additive prime structure at supersimple (decidable and unstable, conditional on Dickson), was
> re-fetched from the arXiv abstract this pass and confirmed at the source: the abstract reads "under
> Dickson's conjecture ... the theory $\mathrm{Th}(\mathbb{Z},+,1,0,\mathrm{Pr})$ ... is decidable,
> unstable and supersimple." This is the fact the whole note turns on, and it is not the inverted reading
> that a prior FETCH-tag once asserted (see the process note in LEARNINGS #157). The body-level refinements
> quoted above, the "of U-rank 1" clause of Theorem 1.2 and the exact numbering of the unconditional-IP
> Theorem 3.7, rest on the drafting pass's reading of the introduction and Section 3, not on this
> abstract-level re-fetch; per the PUBLICATIONS gate they must be human-pinned against the PDF before any
> submission.

### 4.2 The wild direction is a different structure (the order)

Kaplan-Shelah restate the wild base (introduction, verbatim): "In [BJW93, Woo13], they proved that
assuming Dickson conjecture, $\mathrm{Th}(\mathbb{N}, +, 0, \mathrm{Pr})$ is undecidable and even defines
multiplication. It follows immediately that $T_{+,\mathrm{Pr},<}$ is undecidable and as complicated as
possible in the sense of stability theory."

The primary source is **Bateman-Jockusch-Woods** (JSL 58(2), 1993), abstract (verbatim): "It is shown,
assuming the linear case of Schinzel's Hypothesis, that the first-order theory of the structure
$\langle \omega, +, P \rangle$, where $P$ is the set of primes, is undecidable and, in fact, that
multiplication of natural numbers is first-order definable in this structure." The base is over
$\omega = \mathbb{N}$, where the order is definable from $+$, so this is the **with-order** case. The
linear case of Schinzel's Hypothesis H equals Dickson's conjecture (D). So the ordered additive prime
structure defines $\times$ (undecidable, SOP + IP, maximally wild), **CONDITIONAL** on Dickson.

Two consequences, both structural:

- The base is $(\mathbb{N}, +, \mathrm{Pr})$, i.e. **full addition** plus the primes, not "successor
  only". Any framing that reads BJW as "arithmetic from the primes with only successor" is factually
  wrong.
- The fault line is the archimedean **order** coupled to $+$ and the primes, **not** the bare prime set.
  Over $\mathbb{N}$ the order is free from $+$; over $\mathbb{Z}$ it is not; and that is exactly what
  flips supersimple (Kaplan-Shelah, order-free) to full arithmetic (BJW, ordered), conditionally on
  Dickson.

**Reinforcing datum. KNOWN.** Poizat, "Supergenerix" (J. Algebra 404, 2014, **Theorem 25**) and
Palacin-Sklinos (arXiv:1405.0568, "On superstable expansions of free abelian groups", = [PS14] in
Kaplan-Shelah) prove that $\mathrm{Th}(\mathbb{Z}, +, 0, P_q)$, with $P_q$ the set of powers of $q$, is
**superstable of U-rank $\omega$**, a second tame additive structure carrying a sparse
multiplicatively-defined set, with no order. So "a sparse multiplicative set forces wildness" is wrong
twice over; the wildness is the coupling to the archimedean order, not the sparse set.

> **Repo correction, load-bearing.** The source dossier and the task brief label [PS14] as
> "Point-Schmidt". The actual Kaplan-Shelah bibliography entry reads "[PS14] Daniel **Palacin** and Rizos
> **Sklinos**. On superstable expansions of free abelian groups. preprint, arXiv:1405.0568, 2014." The
> authors are **Palacin-Sklinos**, not Point-Schmidt. Use the correct attribution.

The **signature/order half** is clean and KNOWN, and it is what actually rules out the ring and
difference-field worlds: o-minimal structures cannot define any infinite discrete set (definable subsets
of the line are finite unions of points and intervals), so no o-minimal structure defines $\{\log p\}$
even though $\mathbb{R}_{\exp}$ (o-minimal, Wilkie 1996) carries each value $\log p$ as an element; and
ring-language tame structures (ACF, pseudofinite fields, ACFA) have **no archimedean order at all**, so
$\{\log p\}$ is not even expressible. This is the project's #62/#153 point ("$\log p$ is not in the
language of rings") met from the definability side.

### 4.3 The tame/wild map (the corpus, assembled)

The one table this note contributes is the assembled map. Legend: tame = well-behaved in the marked
hierarchy; wild = interprets arithmetic. All Dickson-conditional entries are marked (D).

| Structure | Order in language | Predicate | Classification | Status |
|---|:--:|---|---|---|
| $T_+ = \mathrm{Th}(\mathbb{Z},+,0,1)$ | no | none | superstable, U-rank 1 (**tame**) | KNOWN (Presburger) |
| $T_{+,<} = \mathrm{Th}(\mathbb{Z},+,0,1,<)$ | yes | none | dp-minimal, hence NIP (**tame**) | KNOWN |
| $T_{+,\mathrm{Pr}} = \mathrm{Th}(\mathbb{Z},+,0,1,\mathrm{Pr})$ | no | primes | decidable, unstable, supersimple U-rank 1 (**tame**); IP unconditional | KNOWN, decid./supersimple **(D)** (KS Thm 1.2); IP **unconditional** (KS Thm 3.7, via Prop 3.6, from Green-Tao) |
| $\mathrm{Th}(\mathbb{Z},+,0,P_q)$ | no | powers of $q$ | superstable, U-rank $\omega$ (**tame**) | KNOWN (Poizat Thm 25; Palacin-Sklinos) |
| $\mathrm{Th}(\mathbb{N},+,0,\mathrm{Pr}) \equiv \mathrm{Th}(\mathbb{Z},+,\mathrm{Pr},<)$ | yes | primes | defines $\times$, undecidable, SOP + IP (**wild**) | KNOWN **(D)** (BJW93, Woods); **unconditional = OPEN keystone** |
| $\mathrm{Th}(\mathbb{N},+,P_{m,r})$ (primes in AP) | yes | primes $\equiv r \bmod m$ | defines $\times$, undecidable (**wild**) | KNOWN **(D)** (Boffa 1998) |
| $\langle \mathbb{N}, S, \mid \rangle$ (successor, divisibility) | order-def. | divisibility | Def-complete, recovers $(\mathbb{N},+,\times)$ (**wild**) | KNOWN (Robinson; Korec [Kor01] catalog) |

The map reads as one clean statement: crossing from a tame row to a wild row is exactly adding the
archimedean **order** to an additive prime structure (and, unconditionally, only the IP threshold is
crossed; the SOP/arithmetic threshold is conditional). Bes's survey [Bes01] and Korec's list [Kor01] are
the reference atlas of which additive-plus-predicate expansions of $(\mathbb{N},+)$ recover the full
$(\mathbb{N},+,\times)$; the note cites them as the map's boundary.

## 5. The open keystone

The corrected tameness leg, stated as a theorem, is CONDITIONAL, and one link is genuinely OPEN.

> **Leg B (corrected). CONDITIONAL on Dickson.** A simple or NIP structure cannot carry the **ordered**
> prime structure (the primes with the ambient additive order, i.e. the log-line ordering the explicit
> formula already carries), because that structure interprets $(\mathbb{N}, +, \times)$
> (Bateman-Jockusch-Woods, mod Dickson) and so has SOP and IP. The **order-free** additive prime set is
> compatible with supersimplicity (Kaplan-Shelah).

Two residual gaps keep this from being unconditional. First, a reduction from an *internal ordered prime
set* to BJW's ambient $(\mathbb{N}, +, \mathrm{Pr}, <)$ is not exhibited ("next prime on the prime set" is
not "successor/addition on $\mathbb{N}$"), so even conditionally the internal-prime-set hypothesis does
not yet yield BJW without strengthening it to carry the ambient additive order. Second, and decisive:

> **The keystone (OPEN).** Whether the ordered additive prime structure forces $\times$ **without**
> Dickson is a genuine open problem in arithmetic definability. Kaplan-Shelah state this explicitly (page
> 2, verbatim): "Up to now, the only known results about the theory are under a strong number-theoretic
> conjecture known as Dickson conjecture (D)."

The cleanly separated tiers:

- **CONDITIONAL, KNOWN, Dickson-dependent.** BJW93 + Woods: under the linear case of Schinzel's
  Hypothesis H (= Dickson (D)), $\mathrm{Th}(\mathbb{N}, +, \mathrm{Pr})$ is undecidable and defines
  $\times$. Kaplan-Shelah Thm 1.2: under the **same** (D), the order-free $\mathrm{Th}(\mathbb{Z}, +,
  \mathrm{Pr})$ is decidable and supersimple of U-rank 1. The pair isolates the archimedean order coupled
  to $+$ and the primes as the wild ingredient, **but only conditionally on (D)**.
- **PROVEN unconditionally.** $\mathrm{Th}(\mathbb{Z}, +, \mathrm{Pr})$ has IP (Kaplan-Shelah Theorem
  3.7, via Proposition 3.6, from Green-Tao). IP alone does **not** give SOP, arithmetic, or
  undecidability, so it does **not** close the keystone.
- **ALSO OPEN unconditionally.** (i) Whether $\mathrm{Th}(\mathbb{Z}, +, \mathrm{Pr})$ (no order) is
  decidable / supersimple without (D). (ii) Whether $(\mathbb{N}, +, \Lambda)$, the **von Mangoldt**
  structure, which is the actual explicit-formula datum and is closer to $S(f)$ than the bare predicate,
  forces $\times$. This is not treated anywhere in the corpus.

So the force-multiplication / order-is-wild direction may be presented as KNOWN only in its
Dickson-conditional form, and the unconditional keystone is a real open problem, not a formality. A
Dickson-free tameness note would need exactly this keystone, and it is not available.

## 6. The RH-engine reading: archimedean injection (MECHANISM / HEURISTIC)

The definability map has a direct reading for the RH engine, carried at the hedged tier it deserves. It
concerns the survivor class of the project's #156 pass, the four construction shapes that pass the
two-conjunct WATCH clause (index-set-preserving AND non-endomorphism-shaped): Connes' adele-class trace
formula, the Connes-Consani-Moscovici (CCM) prolate / scaling-site program, Deninger's foliated flow, and
Borger's $\Lambda$-ring / $\mathbb{F}_1$-descent.

**C3 (archimedean injection). MECHANISM.** Every survivor construction that carries $S(f)$ carries it by
**coupling its discrete prime index to an external archimedean object** $O$ (a real line, a flow, a
scaling action, an operator on an $L^2$ of the log variable): $\log p$ enters as an archimedean
length / period / frequency living in $O$, and the summation is realized as a distributional trace or a
periodization over $O$, not as an internal definable sum. This is forced, not stylistic: $S(f)$ **is**
integration of $f \circ \log$ against the von Mangoldt measure on $\mathbb{R}$, so any object outputting
the real number $S(f)$ must contain a copy of $\mathbb{R}$ with $\log$, convergence, and the external $f$;
the tameness trade (Leg A saturation + Leg B ordered-interpretation) forbids a tame carrier from defining
that summation internally. Within the survivor class the only alternative to archimedean injection is
**not** internal definition (that requires going wild, i.e. interpreting arithmetic and losing tameness);
it is to **not carry $S(f)$ at all**.

| Survivor | Reaches $S(f)$? | Archimedean injection object $O$ | $S(f)$ sited |
|---|:--:|---|---|
| **Connes** adele class space | yes | scaling flow $\mathbb{R}^\ast_+ \subset C_k$ on $L^2(\mathbb{A}/k^\ast)$; $\log p$ = orbit period; sum = Guillemin-Sternberg trace | **external** (archimedean) |
| **CCM** prolate / scaling site | yes | prolate/Sonin operator + periodization $E(f)(u) = u^{1/2}\sum_n f(nu)$ on the log-line; $\log p$ = L-factor frequency; sum = the archimedean Weil functional $W_\infty$ | **external** (archimedean log-line) |
| **Deninger** foliated flow | yes | foliated $\mathbb{R}$-flow $\phi^t$; $\log p$ = closed-orbit length; sum = Poisson summation per orbit + trace | **external** (archimedean flow) |
| **Borger** $\Lambda$-ring / $\mathbb{F}_1$ | no | none internal (no $\log$, no summation into $\mathbb{R}$) | **absent** (carries the multiplicative Euler **product**, not the sum) |

Borger violates the literal C3, but not by the route C3 excludes (internal definition): it avoids
archimedean injection by not carrying $S(f)$ at all, stopping at the multiplicative Euler product
$\zeta(s) = \prod_p \det(1 - \psi_p p^{-s} \mid M)^{-1}$, all primes non-invertible, no $\log$, no
summation. Pushing Borger to a trace formula requires the multiplicative completion $\Phi_t = \prod_p
\psi_p^{\,t/\log p}$ (= Connes' scaling action), where the $t/\log p$ exponent **is** the archimedean
injection, landing Borger back in the analytic family with Connes' K1 wall. So C3 is a **conditional
universal**: the split coordinate is exactly "does the survivor carry the additive summed explicit formula
$S(f)$", and it partitions the class into archimedean-injecting {Connes, CCM, Deninger} and
integral-descent {Borger}.

**The reading of the M4 = CCM Section-7 wall. MECHANISM for the object-coincidence, HEURISTIC for the
causation.** The project's standing M4 wall (LEARNINGS #148/#153/#154) is the CCM Section-7 uniform
determinant-class limit $\hat\xi_\lambda \to \Xi$ (equivalently uniform global Weil positivity) as $S \to$
all primes, stated in the prolate/Sonin space and the Weil form $W_\infty$ on the real log-line. Those
Section-7 objects **are** C3's archimedean injection object for CCM (MECHANISM: the objects coincide,
verbatim). The Section-7 difficulty is making the injection uniform as $S \to$ all primes; C3 therefore
gives a structural reading of **why** the wall is archimedean and not geometric: the summation $S(f)$ can
only be reached by injecting an archimedean object, so the last hard step (making the sign survive the
full injection over all primes) is necessarily an archimedean-limit step, not a finite-place or
geometric-descent step.

**Mandatory hedge.** This is a reading of known constructions, not a theorem. It does not predict
**whether** the uniform limit holds (that is RH-equivalent); it says only **where** the decisive step must
live and **why** it is archimedean. The diagnostic value is negative and concrete: do not expect the wall
to move by improving the geometric substrate (the Borger / Connes-Consani 2606.06604 absolute-geometry
side), because that side does not carry $S(f)$. This matches the observed outcome that the 2026 CCM
geometric carrier (with the scaling-site periodic orbits of length $\log p$ now geometrically derived,
$E_p \cong C_p \times \widetilde{X}_\infty$, rather than posited) has **no Section 7**, no $\Xi$, no
prolate/Weil form, and does not move the positivity wall (LEARNINGS #157).

## 7. Honest scope

This note is a structural-obstruction note. It is **not** a proof of anything about RH, and it does not
put a general model-theoretic floor under R1. To be scrupulous:

- **PROVEN, and cited as such:** Lemma P3 (saturation kills countable definable sets), and its corollary
  that the standard-prime diagonal is undefinable in any $\aleph_1$-saturated model (Leg A), with the
  caveat that Leg A is orthogonal to the RH engine because the carrier $(\mathbb{N}, +, \times)$ is not
  saturated. The independence property of $\mathrm{Th}(\mathbb{Z}, +, \mathrm{Pr})$ (Kaplan-Shelah
  Theorem 3.7, via Proposition 3.6, from Green-Tao) is unconditional.
- **KNOWN, published, and attributed:** the tame/wild map of Section 4.3. Kaplan-Shelah Theorem 1.2
  (order-free additive prime structure is supersimple, conditional on Dickson); BJW93 + Woods (ordered
  additive prime structure defines $\times$, conditional on Dickson); Boffa 1998 (primes in an arithmetic
  progression, same hypothesis); Poizat Theorem 25 and Palacin-Sklinos ($q$-powers, superstable, U-rank
  $\omega$); Bes [Bes01] and Korec [Kor01] as the definability atlas.
- **REFUTED, and named so no future session re-makes the claim:** "a tame (simple/NIP) structure cannot
  carry the primes" is **false** (Kaplan-Shelah). The correct invariant is the archimedean **order**
  coupled to $+$ and the primes, not the bare prime set. This re-confirms the project's #62/#153
  archimedean-lattice obstruction from the definability side; it does not add a new obstruction.
- **CONDITIONAL, labeled (D):** every force-multiplication / order-is-wild statement (BJW, Boffa, and
  Kaplan-Shelah's decidability half) holds only modulo Dickson's conjecture.
- **OPEN, flagged honestly:** the keystone (does the ordered prime structure force $\times$ **without**
  Dickson); whether $\mathrm{Th}(\mathbb{Z}, +, \mathrm{Pr})$ is decidable / supersimple without (D);
  and whether $(\mathbb{N}, +, \Lambda)$, the actual explicit-formula datum, forces $\times$. None of
  these is closed by the unconditional IP result.
- **MECHANISM / HEURISTIC, hedged:** the archimedean-injection reading (C3) and its reading of the CCM
  Section-7 = M4 wall as archimedean by necessity. The object-coincidence is exact (MECHANISM); the
  causal "therefore the wall must be archimedean" is a reading of known constructions (HEURISTIC), not a
  theorem, and it predicts nothing about whether RH holds.

**The withdrawn overclaim, on record.** A first-draft publishable-shaped claim, "no tame counting engine
carries the summed explicit formula", is **withdrawn**. It rested on an inverted central citation
(arXiv:1601.07099 was read as proving $\times$-definability; it proves the opposite, order-free
supersimplicity), a refuted invariant (the bare prime set), and an unengaged state-of-the-art corpus. The
process learning is that FETCH-tagged citations need independent source verification before being treated
as load-bearing (the inversion was caught only on re-fetch). This note is what survives after engaging the
corpus honestly.

**The publishable residue is the synthesis packaging.** What is potentially novel is **not** any theorem
here (the model-theoretic core is published and more refined than any first-draft treatment) but the
**assembly**: one target functional $S(f)$, the two-legged split (saturation vs order-interpretation),
the tame/wild map keyed to the archimedean order, the honest tier separation with the keystone flagged
OPEN, and the C3 reading connecting the definability invariant to the RH engine's Section-7 wall. The
RH-engine packaging appears genuinely un-treated (the adjacent published corpus, logical complexity of RH
as $\Pi^0_1$ and reverse mathematics of PNT, is about the complexity of the **statement**, not the
tameness of proof-engine **structures**). But "no prior art" would overstate the case: only the packaging
is new, and it ships only with the keystone open.

## References

Load-bearing items, attributions and identifiers verified at source this pass where marked.

**The model theory of additive prime structures (the corpus this note assembles).**
Kaplan, I.; Shelah, S. (2016/2017). *Decidability and classification of the theory of integers with
primes.* arXiv:1601.07099; J. Symbolic Logic 82(3). [Read at source: abstract, introduction, Section 3.
Theorem 1.2: under Dickson, $\mathrm{Th}(\mathbb{Z}, +, 0, 1, \mathrm{Pr})$ (no order) is decidable,
unstable, supersimple of U-rank 1. Theorem 3.7: $\mathrm{Th}(\mathbb{Z}, +, \mathrm{Pr})$ has IP (and
$n$-IP) unconditionally, resting on Proposition 3.6 (the Green-Tao arithmetic-progression lemma). Page 1:
$T_+$ superstable U-rank 1, $T_{+,<}$ dp-minimal. Page 2 verbatim:
"Up to now, the only known results about the theory are under a strong number-theoretic conjecture known
as Dickson conjecture (D)."]
Bateman, P. T.; Jockusch, C. G.; Woods, A. R. (1993). *Decidability and undecidability of theories with a
predicate for the primes.* J. Symbolic Logic 58(2):672-687. [Abstract verbatim: assuming the linear case
of Schinzel's Hypothesis, $\mathrm{Th}\langle \omega, +, P \rangle$ is undecidable and $\times$ is
first-order definable in it.] Woods, A. R. (2013), and Woods's thesis (1981).
Boffa, M. (1998). *More on an undecidability result of Bateman, Jockusch and Woods.* J. Symbolic Logic
63(1). [Linear Schinzel-H implies $\times$ definable in $\langle \omega, +, P_{m,r} \rangle$, primes
$\equiv r \bmod m$; same Dickson hypothesis. This, not Kaplan-Shelah, is the home of the "force $\times$"
sentence.]
Poizat, B. (2014). *Supergenerix* (a la memoire d'Eric Jaligot). J. Algebra 404:240-270, Theorem 25.
[$\mathrm{Th}(\mathbb{Z}, +, 0, P_q)$ ($q$-powers) is superstable of U-rank $\omega$.]
Palacin, D.; Sklinos, R. (2014). *On superstable expansions of free abelian groups.* arXiv:1405.0568
(= [PS14] in Kaplan-Shelah). [Cited jointly with Poizat for the $q$-power result. Authors are
Palacin-Sklinos, correcting the "Point-Schmidt" misattribution in the repo dossier.]
Bes, A. (2001). *A survey of arithmetical definability.* Bull. Belg. Math. Soc. Simon Stevin (suppl.):1-54
(= [Bes01]). [The decidability/definability survey Kaplan-Shelah cite as "very good".]
Korec, I. (2001). *A list of arithmetical structures complete with respect to first-order definability.*
Theoret. Comput. Sci. 257(1-2):115-151 (= [Kor01]). [Catalog of Def-complete arithmetical structures,
e.g. $\langle \mathbb{N}, S, \mid \rangle$ (Robinson).]
Green, B.; Tao, T. (2008). *The primes contain arbitrarily long arithmetic progressions.* Ann. of Math.
(2) 167(2):481-547 (= [GT08]). [The unconditional IP of the order-free additive prime structure is derived
from its proof; IP alone does not force arithmetic.]

**Neostability / definability background (standard, cited where load-bearing).**
Chang, C. C.; Keisler, H. J. *Model Theory* (6.1.1: countable ultraproducts are $\aleph_1$-saturated).
Wilkie, A. (1996). *Model completeness results for expansions of the ordered field of real numbers...*
($\mathbb{R}_{\exp}$ is o-minimal). Overspill in nonstandard models of PA (standard).

**Project internal (the localization this note supports).**
[`../../docs/03_research/tameness_trade.md`](../../docs/03_research/tameness_trade.md) (the source dossier:
Leg A / Leg B split, Lemma P3, the C3 survivor screen);
[`../../docs/03_research/model_theoretic_frobenius.md`](../../docs/03_research/model_theoretic_frobenius.md)
(#156: NG1/NG2, the two-conjunct WATCH clause, Section 10 heuristic corrected 2026-07-10);
[`../../docs/03_research/sourcing_gap_r1.md`](../../docs/03_research/sourcing_gap_r1.md) (the R1 facet the
tameness map sharpens);
[`../obstruction_map/obstruction_map.md`](../obstruction_map/obstruction_map.md) (the survey whose Section
6.2 archimedean-order firewall this note details);
[`../../experiments/LEARNINGS.md`](../../experiments/LEARNINGS.md) #157 (this arc), #156 (the parent),
#153, #62 (the archimedean-lattice wall re-confirmed from the definability side), #148, #154 (the M4 =
Section-7 wall C3 reads), #133 (the Level-4 / frame-audit discipline).
