# The model-theoretic Frobenius: the one global characteristic-0 Frobenius, screened against R1

> A SURVEYOR + BUILDER + ADVERSARY loop (2026-07-09) on a corpus with zero prior repo coverage: Ax's
> pseudofinite fields (1968), Chatzidakis-Hrushovski ACFA, Hrushovski's twisted Lang-Weil estimate, and the
> ultraproduct Frobenius on $K = \prod_p \overline{\mathbb{F}}_p / \mathcal{U}$. Question posed: can the one
> global characteristic-0 Frobenius mathematics actually has fill the R1 slot
> ([`sourcing_gap_r1.md`](sourcing_gap_r1.md)), i.e. the S1 endomorphism / S4 derivation the Stepanov engine
> needs ([`stepanov_engine_audit.md`](stepanov_engine_audit.md))? Answer: no, and the failure sharpens into
> two proven no-gos (NG1, NG2), one corrected trivialization theorem (Borger), and one K1 audit. All
> corrections from the ADVERSARY pass (18 in-place repairs, the largest being the Borger mechanism flip and
> the adele witness against the sufficiency of index-set preservation) are incorporated below at their
> post-correction scope. Per [`../researcher_mindset.md`](../researcher_mindset.md): these are coordinates,
> not verdicts on the problem; each no-go says where the R1 filler cannot live, which narrows where it must.
>
> Reading depth, stated honestly: Ax 1968 pp. 239-241, Hrushovski arXiv:math/0406514v2 pp. 1-8 and 117-126,
> Shuddhodan-Varshavsky arXiv:2106.10682 pp. 1-6, and the Chatzidakis 3ECM survey (13 pp.) read in full by
> fetch; both key arXiv identifiers re-fetched and matched by the adversary; Cherlin-Jarden cited via
> Hrushovski only (primary source not read); Borger, Buium, Henson-Keisler from knowledge. Rigor labels:
> **PROVEN** (proof included or one-line reduction to a standard theorem), **MECHANISM** (precise statement,
> no known counterexample), **HEURISTIC** (directional).

## 1. The question

The repo's R1 wall has an operator face: the counting engines (Stepanov S1/S4, Weil I W6) run over
$\mathbb{F}_q$ on one structure, $x \mapsto x^q$, and over $\mathrm{Spec}(\mathbb{Z})$ that structure is
absent (the only ring endomorphism of $\mathbb{Z}$ is the identity, LEARNINGS #145). The model-theoretic
Frobenius literature is the one published place where "Frobenius survives to characteristic 0" is a theorem
rather than a hope: a non-principal ultraproduct of the difference fields
$(\overline{\mathbb{F}}_p, x \mapsto x^p)$ is a characteristic-0 field with a genuine non-identity
automorphism whose fixed-point theory is quantitative (Hrushovski's twisted Lang-Weil estimate; the ACFA
model companion). Since this corpus had never been screened, the two questions that decide everything were
posed to it directly: (i) does the global Frobenius engage the arithmetic (the S1/S4 slots), and (ii) does
the limit object see the sum over all primes (the #153 additive-lattice clause), and what does its
fixed-point count consume (K1)?

## 2. The object

Let $P$ be the rational primes and $\mathcal{U}$ a non-principal ultrafilter on $P$. Set

$$K \;=\; \Big(\prod_{p \in P} \overline{\mathbb{F}}_p\Big) \Big/ \mathcal{U}, \qquad
\sigma\big([(x_p)_p]\big) = [(x_p^{\,p})_p].$$

Basic facts, all PROVEN (elementary or standard):

- $\sigma$ is a field automorphism of $K$ (each coordinate map is one; germs of a.e.-automorphisms descend).
- $K$ is algebraically closed of characteristic 0 (Łoś; "$q \cdot 1 = 0$" holds at the single coordinate
  $p = q$, a $\mathcal{U}$-null set), of cardinality $2^{\aleph_0}$, hence abstractly $K \cong \mathbb{C}$
  by Steinitz. No CH needed anywhere (the cardinality dichotomy in Section 4 is the classical
  Frayne-Morel-Scott branching argument).
- Under any identification $K \cong \mathbb{C}$, $\sigma$ is a wild automorphism: not the identity, not
  conjugation, hence discontinuous for every analytic structure. The one global Frobenius acts on a copy of
  the field where $\zeta$'s zeros live, but invisibly to every topology.
- $(K, \sigma) \models$ ACFA (Hrushovski, arXiv:math/0406514: the elementary theory of the Frobenius
  automorphisms is exactly ACFA, the model companion of difference fields, via the twisted Lang-Weil
  estimate). Every completion of ACFA is supersimple (Chatzidakis-Hrushovski, Trans. AMS 351 (1999)).
- The fixed field is $\mathrm{Fix}(\sigma) = \prod_p \mathbb{F}_p / \mathcal{U}$, a **pseudofinite field**
  (Ax 1968): characteristic 0, cardinality $2^{\aleph_0}$, internally "of size" the nonstandard prime
  $p^* = [(p)_p]$. The tower $\mathrm{Fix}(\sigma^n) = \prod_p \mathbb{F}_{p^n}/\mathcal{U}$ replays the
  $\mathbb{F}_q \subset \mathbb{F}_{q^2} \subset \cdots$ tower at one generic prime.

The diagonal $d : \mathbb{Z} \to K$, $d(n) = [(n \bmod p)_p]$, is the unique ring homomorphism
$\mathbb{Z} \to K$ (injective; extends to $\mathbb{Q}$), and $d(\mathbb{Q})$ is the prime field of $K$.
This is where the arithmetic lives, and it is exactly where the construction degenerates.

## 3. NG1: the Fermat degeneracy is limit-independent rigidity

**Theorem (NG1, corrected scope). PROVEN.** *Every unital ring endomorphism $\tau$ of every unital ring $A$
fixes the prime ring $\mathbb{Z} \cdot 1$ pointwise, and fixes $m/n$ whenever $n$ is invertible in $A$
(units have unique inverses, so $\tau(n^{-1}) = n^{-1}$). In particular every ring endomorphism of every
$\mathbb{Q}$-algebra fixes the canonically imported $\mathbb{Q}$ pointwise.*

Proof: $\tau(1) = 1$ forces $\tau(n) = n$ for $n \in \mathbb{Z}$; multiplicativity plus uniqueness of
inverses does the rest. One line, and the line is the point.

Applied to $K$: $\sigma(d(n)) = [(n^p \bmod p)_p] = [(n \bmod p)_p] = d(n)$ by Fermat's little theorem at
every coordinate. Fermat is the coordinatewise witness of the general rigidity: the diagonal integers are
already Frobenius-fixed at every prime, which is the #145 statement "the identity is the universal Frobenius
lift on $\mathbb{Z}$" wearing model-theoretic clothes.

Three consequences, each adversary-corrected into its honest form:

1. **Limit-independence.** The rigidity has nothing to do with ultrafilters or limits. It holds in any
   receptacle where $\mathbb{Q}$ is generated by $1$: index-set-quotienting limits (ultraproducts, germs)
   AND index-set-preserving ones. Witness: every unital ring endomorphism of the adele ring
   $\mathbb{A}_\mathbb{Q}$ fixes the diagonal $\mathbb{Q}$ pointwise (every standard integer is a unit in
   $\mathbb{A}_\mathbb{Q}$; the one-line argument runs verbatim). It also covers
   $\prod_p \mathbb{Z}/p^2/\mathcal{U}$ and $\prod_p W(\overline{\mathbb{F}}_p)/\mathcal{U}$ (both
   $\mathbb{Q}$-algebras: each fixed $n$ is invertible at cofinitely many coordinates). So the #145
   identity-Frobenius degeneracy is not a limit artifact; it is a rigidity theorem about
   ring-endomorphism-shaped fillers on any ring-shaped receptacle.
2. **The kill mechanism, stated exactly (K3 discipline).** "Every endomorphism fixes the prime field" is
   equally true in characteristic $p$, where it is the FEATURE: the counted objects $C(\mathbb{F}_q)$ are
   prime-field-rational fixed points, isolated because the fixed field is finite. NG1's S1 kill in
   characteristic 0 is the INFINITUDE of what is forced to be fixed: the prime field is $\mathbb{Q}$, and
   $\mathrm{Fix}(\sigma)$ is a continuum-sized pseudofinite field, so no endomorphism-shaped Frobenius can
   have isolated or prime-indexed fixed arithmetic. The disanalogy with Weil's proof is "prime field finite
   vs prime field $= \mathbb{Q}$", not the fixing itself.
3. **Scope.** NG1 covers ring endomorphisms of ring-shaped receptacles, full stop: coordinatewise power
   maps, arbitrary coordinatewise automorphism families, wild abstract endomorphisms of $K \cong \mathbb{C}$.
   It does NOT cover non-ring categories: correspondences on external objects
   (e.g. on $\mathrm{Spec}(K) \times_\mathbb{Q} \mathrm{Spec}(K)$ or motives over $K$), flows, groupoid or
   measure-space actions, noncommutative spaces. Internal correspondences and twists are caught by NG2
   instead; external-category fillers are caught by neither and remain the live shape, consistent with the
   screening survivors (Connes' scaling flow, Deninger's flow).

## 4. NG2: generic prime versus sum over primes

Twists $\sigma \circ \phi$ (with $\phi$ an algebraic self-map or correspondence, not a ring endomorphism)
escape NG1 and have honestly counted isolated fixed points. Worked example: $\tau(x) = \sigma(x) + 1$ on
$\mathbb{A}^1(K)$ solves $x^p - x + 1 = 0$ per coordinate (Artin-Schreier, irreducible over $\mathbb{F}_p$),
giving exactly $p$ isolated fixed points per coordinate, none arithmetic: in $K$, exactly $p^*$ internal
fixed points at the one generic prime. The question is what the fixed points are indexed by, and the answer
is: by nothing standard. NG2 makes this provable in four tiers.

- **(i) $\mathcal{U}$-invariance. PROVEN.** Any invariant extracted functorially from the single difference
  field $(K, \sigma)$ is unchanged under deleting any $\mathcal{U}$-null set of coordinates, in particular
  the prime 2 (the restriction map on germs is a canonical difference-field isomorphism commuting with
  $\sigma$; this is isomorphism-invariance, not transfer, so no definability restriction is needed). The
  explicit formula's prime side $\sum_p \sum_k (\log p) f(k \log p)$ is not invariant under deleting
  $p = 2$. Hence no construction functorial in one ultraproduct computes the prime sum.
- **(ii) Interpretability. PROVEN at rescoped conclusion.** ACFA is supersimple, $(\mathbb{Z}, +, \times)$
  has the strict order property, simplicity passes to interpreted structures: $(K, \sigma)$ does not
  interpret the standard model of arithmetic. Corrected scope: this closes the specific route "interpret
  arithmetic internally, then state the explicit formula first-order"; it does not by itself exclude a
  prime-indexed internal object with less than full arithmetic. That kill is tier (iii)'s. Corollary kept:
  $d(\mathbb{Z})$ is an undefinable subset of $\mathrm{Fix}(\sigma)$, set-theoretically present,
  structurally invisible.
- **(iii) Cardinality dichotomy. PROVEN, ZFC-clean.** Every internal subset of $K$ (every ultraproduct of
  coordinate sets, twists-with-parameters included) is finite or of cardinality $\ge 2^{\aleph_0}$
  (branching injection $\{0,1\}^\omega \hookrightarrow \prod S_p/\mathcal{U}$ when $|S_p| \to_\mathcal{U}
  \infty$; no CH, no saturation theory). Countably infinite is excluded. So **no twist, correspondence, or
  internal definable-with-parameters construction has fixed-point set the prime-indexed diagonal**
  $\{d(2), d(3), d(5), \dots\}$: the primary kill of the prime-indexed-fixed-points hope.
- **(iv) Full nonstandard universes. MECHANISM.** In an ultrapower of the set-theoretic universe, internal
  sums $\sum_{p \le x}$ exist for nonstandard $x$, but by transfer they are verbatim copies of the standard
  sums, exactly as hard; the route is conservative for the statements at issue. Honest caveat carried:
  saturation principles can in general add proof-theoretic strength (Henson-Keisler); nothing RH-shaped
  (positivity, symmetry) is among the known additions, and RH's $\Pi^0_1$ status keeps the conservativity
  remark relevant.

**The external-decoration rider (adversary attack A1, executed).** There EXISTS a canonical, countable,
prime-indexed external subset of $K$: the diagonal image $d(P)$, canonical because $d$ is the unique ring
homomorphism $\mathbb{Z} \to K$. So "the index set is exactly what the quotient removed" must be read as
scoped to internal objects (as proven). Why the rider does not reopen the route: the decorated structure
$(K, \sigma, d)$ factors with no interaction. NG1 makes $\sigma$ the identity on $d(\mathbb{Q})$, so the
Frobenius never couples to the imported arithmetic; all analytic content of the prime side ($\log p$, the
ordering, the summation) is computed in $\mathbb{Z}$ through $d$, in the standard world, with $K$ a passive
container. Coordinate-reading decorations are not well-defined on germs; internal-cardinality measures land
at the generic prime. No decoration simultaneously index-aware, canonical, and $\sigma$-interacting was
found, and for endomorphism-mediated couplings NG1 proves there is none.

**Reading against #153.** NG2 is the additive-lattice wall met from the model-theory side. The ultraproduct
is the mathematically maximal all-primes-at-once limit that preserves first-order structure, and it provably
forgets exactly the lattice: Łoś keeps for-almost-all-$p$ facts (indeed perfects per-prime uniformity, which
is what the corpus's exports, Ax-Grothendieck included, actually are), quotients away the prime index, and
$\log p$ (archimedean size data, whose $\mathbb{Q}$-linear independence is the elementary lattice fact of
#62) is not in the language of rings at all. So the #153 glue must be metric/archimedean-aware, not
elementary: no first-order-preserving limit over the primes can be it. Definition pinned by the adversary:
"limit along the primes" here means index-set-QUOTIENTING constructions (germs, ultraproducts, colimits
along the cofinite filter); restricted products are excluded from the slogan, and correctly so, since the
adelic explicit formula (Tate's thesis) does state the prime sum on an index-set-preserving carrier, with
the moving object a flow, not a ring endomorphism.

## 5. The Borger trivialization (corrected mechanism)

Borger's $\mathbb{F}_1$-position: a $\Lambda$-structure = commuting Frobenius lifts $\psi_q$ at all primes
jointly on one carrier = descent to $\mathbb{F}_1$. Does the ultraproduct-of-all-characteristics carry it?
The first-draft headline "the ultrafilter destroys the $\Lambda$-structure" was FALSE and is withdrawn on
record; the corrected theorem is sharper:

- **The ultrafilter inverts every standard prime.** In $K$ (and in $\prod_p \mathbb{Z}/p^2/\mathcal{U}$ away
  from the generic nilpotent, and in $\prod_p W(\overline{\mathbb{F}}_p)/\mathcal{U}$), each standard prime
  $q$ is invertible, so $qK = K$ and the Frobenius-lift congruence $\psi_q(x) \equiv x^q \bmod qK$ is
  stateable but VACUOUS: every ring endomorphism is a lift at every standard prime. PROVEN.
- **$\Lambda$-structures therefore exist in profusion and carry nothing.** On a $\mathbb{Q}$-algebra a
  $\Lambda$-structure is exactly a commuting family of arbitrary ring endomorphisms (the Newton relations
  are invertible over $\mathbb{Q}$; Wilkerson), so $K \cong \mathbb{C}$ carries continuum-many, with
  $\psi_n = \mathrm{id}$ one of them, all information-free: zero $\mathbb{F}_1$-descent data. The
  coordinatewise $q$-power map is additive only when $p \mid 2^q - 2$ (a finite, $\mathcal{U}$-null set of
  coordinates), but that kills only the power-map candidate; the vacuity statement is the real content.
- **The structural moral. MECHANISM.** Ultralimit-along-primes and $\mathbb{F}_1$-descent are structurally
  disjoint completions of the per-prime family: Borger keeps the index set alive as $\mathrm{Spec}(\mathbb{Z})$
  with all primes non-invertible (the congruences are the content); the ultrafilter quotients the index set
  to one generic point and inverts every standard prime, emptying the congruence of descent content. The
  limit does not break the $\Lambda$-condition; it inverts the primes the condition was about.

The S4 face degenerates the same way: the ultraproduct packages all Buium Fermat-quotient $p$-derivations
into one operator $\delta^*(n) = [((n^p - n)/p \bmod p)_p]$ at the generic prime (a real gain in uniformity,
zero gain in globality), with no archimedean coupling (the index set has no coordinate at $\infty$, and any
single added coordinate is $\mathcal{U}$-null). A signature curiosity recording whose hostage the
construction is: $\delta^*(2) = 0$ iff the Wieferich primes lie in $\mathcal{U}$, i.e. iff there are
infinitely many, an open problem (numerics verified: coordinates $(2,1,4,10,6)$ at $p = 3,5,7,11,13$; zero
at $p = 1093, 3511$).

## 6. The K1 audit: what twisted Lang-Weil consumes

The corpus's quantitative engine is Hrushovski's twisted Lang-Weil estimate (Theorem 1.1 of
arXiv:math/0406514): for a correspondence $S \subseteq X \times X^{\phi_q}$ with the right dominance and
dimension hypotheses, $|S(k) \cap \Phi_q(k)| = a q^d + O(q^{d - 1/2})$, with $a$ an intersection-theoretic
degree ratio computed without reading the points; the diagonal case is classical Lang-Weil. That is exactly
the W6 shape (#148). The audit question: what certifies the error term?

Answer, confirmed three independent ways at source: **Deligne purity, every time.**

1. Hrushovski's own proof: Proposition 11.11 states verbatim that it uses Deligne 1974 (Weil I); Theorem
   11.2 is a Lefschetz trace formula with the sub-main terms bounded by purity and the pole budget by
   effective Betti bounds (Katz 2001). His v2 abstract concedes the input "hinges on a result going slightly
   beyond" RH for curves.
2. The descended case follows from Deligne's conjecture (Fujiwara, Pink) plus his theorem on Frobenius
   eigenvalues.
3. Shuddhodan-Varshavsky (arXiv:2106.10682, Algebraic Geometry 9 (2022) 651-687): "a combination of the
   Deligne's purity theorem and a variant of the argument of [Hr]"; the Bourbaki expose arXiv:2308.16132
   follows their proof. An arXiv sweep found NO claim of a purity-free proof of the twisted estimate.

Tier note: the UNTWISTED Lang-Weil (1954) needs only Weil 1948 (RH for curves); the twisted/correspondence
case is Deligne-strength. Both tiers consume finite-field RH. And Ax 1968 opens the whole corpus with the
same dependency, p. 239 verbatim: "In our proof the crucial properties of finite fields are Weil's Riemann
hypothesis for curves and Cebotarev's density theorem", followed on p. 241 by "we have found no striking
number-theoretic applications of our results".

**K1 verdict (HOLDS): the model-theoretic Frobenius corpus is strictly downstream of RH over
$\mathbb{F}_q$. It redistributes the theorem (to almost-all-$p$ first-order statements, to characteristic 0
along ultrafilters); it never re-proves or re-sources it.** Using any of it as an R1 source would import the
conclusion as a premise.

## 7. Scorecard

Slots: **S1** = non-identity endomorphism with isolated prime-indexed fixed points; **S4** = derivation
(cheap-multiplicity source); **W6** = trace formula with independently computable pole budget; **DIAG** =
a genuine $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$ (PROP-global); **#153** = sees the
additive lattice $\{\log p\}$ / the sum over all primes, vs one generic prime along the ultrafilter.

| Candidate object | S1 | S4 | W6 | DIAG | #153 lattice |
|---|---|---|---|---|---|
| Pseudofinite field $\prod \mathbb{F}_p/\mathcal{U}$ (Ax 1968) | NO: no endomorphism in the structure; the Frobenius is already spent (this IS the fixed field) | NO | consumes W6-shaped counting (the CDM definable measure = Lang-Weil), produces none | NO | NO: one generic prime; $\log p$ not in the language; sums over $p$ not first-order |
| ACFA generic $\sigma$ on $K = \prod \overline{\mathbb{F}}_p/\mathcal{U}$ | SHAPE yes, INDEX no: a genuine non-identity char-0 endomorphism (the only published one), but $\sigma = \mathrm{id}$ on $d(\mathbb{Q})$ (NG1) and $\mathrm{Fix}(\sigma)$ is a continuum-sized pseudofinite field: fail in both directions | NO: $\delta^*$ lives at the generic prime, values in $\mathrm{Fix}(\sigma)$, no archimedean coupling (Section 5) | NO for $\zeta$: per-generic-prime counting only | NO: the products are $X \times X^\sigma$ over $\overline{\mathbb{F}}_p$-like bases, never over $\mathbb{Z}$ | NO, provably: NG2 tiers (i)-(iii) |
| Twisted Lang-Weil count (Hrushovski Thm 1.1 / SV Thm 0.3) | YES over $\overline{\mathbb{F}}_q$: the maximal published graph-vs-correspondence generalization of the S1 move | n/a | YES-shaped AND consumed: it IS a Lefschetz trace formula; error certified by DELIGNE PURITY; as a source, K1-circular | NO: lives on $X \times X^{(q)}$, char $p$ | NO: uniform in $q$ but one $q$ at a time |
| Witt/ultra-Frobenius ($\prod_p W(\overline{\mathbb{F}}_p)/\mathcal{U}$; Belair-Macintyre-Scanlon 2007, Schoutens) | degenerate on the arithmetic again: a $\mathbb{Q}$-algebra, NG1 applies; per-prime fixed ring $\mathbb{Z}_p$ | the Joyal/Buium $\delta$-ring, the repo's already-filed $p$-adic S4 shadow | NO | NO | NO |

Against the SP interface ([`missing_object_interface.md`](missing_object_interface.md)): SP2 partially
inhabited (a real endomorphism, wrong fixed structure), SP3 fails (the diagonal degenerates on the
arithmetic locus), SP4 per-generic-prime only, SP5 never reached. Another SP1/SP2-partial object that cannot
conjoin, consistent with the interface's satisfiability matrix.

## 8. The corrected WATCH clause

The builder's first-draft clause was "the R1 filler must be index-set-preserving." The adversary demoted it:
**necessary but provably not sufficient**, witnessed by the adele ring, which preserves the index set while
its ring endomorphisms are exactly as arithmetic-rigid as $K$'s (NG1 is limit-independent). The honest
clause is a conjunction of necessary conditions:

> **The R1 filler must be index-set-preserving AND must move arithmetic by non-endomorphism means.**

Any construction that factors through a germ, limit, or generic point along the primes (index-set-quotienting)
inherits NG1 + NG2; any construction that acts through a ring endomorphism of any unital receptacle,
index-preserving or not, is killed by NG1 alone. Both conditions are necessary only: the adele witness shows
index-preservation rescues nothing by itself, and no sufficiency claim is made. This is consistent with, and
explains the shape of, the constructions that survive screening: Borger (all primes jointly,
non-invertible), Deninger (a flow gluing all circumferences), CCM's lattice map $\mathcal{E}$ (all $n$
simultaneously, #153), Connes (a scaling action on a quotient measure space, not a ring map).

## 9. Two published pointers worth keeping

- **Cherlin-Jarden (via Hrushovski math/0406514 p. 6, verbatim):** "an example of Cherlin and Jarden shows
  that a generic automorphism of $\bar{\mathbb{Q}}$ does not yield a model of ACFA, nor is this true for any
  other field of finite transcendence degree." A published negative at exactly the global base: the
  model-theoretic generic Frobenius exists on big fields and provably refuses to descend to the algebraic
  numbers, the one base a global-arithmetic application would need. Ammunition against any future proposal
  wanting a "generic Frobenius on $\bar{\mathbb{Q}}$"; primary source worth pulling if one appears.
- **Dor-Hrushovski, arXiv:2212.05366 (WATCH):** the limit theory of Frobenius on algebraically closed
  VALUED fields, "motivic intersection theory for difference varieties". Still per-prime, still geometric,
  but valuations are the corpus's first step toward metric data, and Hrushovski's own v2 abstract flags that
  transformal zero-cycles "encapsulate data described in classical cases by zeta or L-functions". This is
  the one corner of the corpus moving toward L-functions; low-cost periodic re-check for any archimedean or
  global place entering the theory.

## 10. Honest scope and the Davenport-Heilbronn note

The construction consumes the per-prime local worlds $\overline{\mathbb{F}}_p$, i.e. the Euler structure;
D-H has no Euler product and no local factors, so the construction cannot be instantiated for D-H at all:
exemption by non-mimicry, Architecture-2 style. Per the #131 convention the honest classification is: **as a
proof route this axis is hollow** (it walls at NG1/NG2 before any discriminating positivity is reached, and
there is no unbuilt object it delegates to); **as a map contribution it carries content** (NG1 and NG2 are
no-gos with proofs, the Borger statement is a trivialization theorem with proven core, and kills are allowed
to be L-function-blind: the D-H discipline binds proof methods, not negative results).

What the no-gos do NOT cover, stated plainly: non-ring categories (correspondences on external objects,
motives over $K$, flows, noncommutative spaces) escape NG1, and external structures escape NG2's internal
scope (with the A1 rider showing the known external import, $d(P)$, is $\sigma$-inert). The one HEURISTIC
worth a future sharpening pass: the tameness trade. The quantitative fixed-point theory exists BECAUSE the
world is supersimple, and supersimple worlds cannot interpret the arithmetic the explicit formula sums over;
the ACFA instance is proven, and a general theorem "definable quantitative fixed-point theory $\Rightarrow$
too tame to state the summed explicit formula" would put a model-theoretic floor under R1.

> **[Correction 2026-07-10, per LEARNINGS #157 / [`tameness_trade.md`](tameness_trade.md)].** The sharpening
> pass ran, and this heuristic sentence needs two scoped corrections (NG2(iii)'s own statement in Section 4 is
> untouched: it is already a ZFC/cardinality fact, and its saturation face is Lemma P3 of the tameness-trade
> dossier). (i) **The primary ACFA prime-diagonal kill is NG2(iii) = saturation, not NG2(ii) =
> supersimple-cannot-interpret-arithmetic.** In any $\aleph_1$-saturated structure no countably-infinite set is
> definable over countable parameters (Lemma P3), so the standard-prime diagonal is undefinable for TAME and
> WILD saturated models alike; a wild $\aleph_1$-saturated monster of $\mathrm{Th}(\mathbb{N},+,\times)$ also
> fails to define the standard prime sum (overspill on the standard cut + external $f$). Interpretability
> (NG2(ii)) is a separate, weaker kill that does not by itself exclude the bare prime set. (ii) **The invariant
> "supersimple worlds cannot carry the primes" is REFUTED.** Kaplan-Shelah (arXiv:1601.07099, Thm 1.2): under
> Dickson, $\mathrm{Th}(\mathbb{Z},+,\mathrm{Pr})$ WITHOUT order is decidable and SUPERSIMPLE of U-rank 1, so a
> supersimple structure DOES carry the prime predicate. The fault line is the archimedean ORDER coupled to $+$
> and the primes (Bateman-Jockusch-Woods use $\mathrm{Th}(\mathbb{N},+,\mathrm{Pr})$ WITH order; primes-with-order
> mod Dickson force $\times$), and the order-free additive prime set is tame. So the correct reading is:
> supersimple worlds have no archimedean order, so they cannot carry the ORDERED, log-weighted prime sum; the
> kill is the MISSING ORDER (the incommensurable $\{\log p\}$ scaling, #62/#153), reinforced by supersimplicity,
> not the missing prime set. This aligns #153 (the glue must be archimedean) and re-confirms it from the
> definability side. The unconditional keystone ("ordered prime structure forces $\times$ without Dickson") is
> OPEN; the "model-theoretic floor under R1" the sentence hoped for is therefore NOT a general theorem, and the
> publishable-shaped claim is withdrawn to a possible-future-expository note (details in
> [`tameness_trade.md`](tameness_trade.md)).

## 11. Handed forward

- **VERIFIER (Lean 4 / Mathlib), targets T1-T4 as corrected:**
  - T1 (NG1 core; hours): `ZMod.pow_card` ($n^p = n$ in $\mathbb{Z}/p$) + `map_ratCast` (any
    `f : K →+* K` on a `DivisionRing` with `CharZero` fixes every rational). Near-one-liners; the value is
    pinning the statement. **DONE 2026-07-10** (`lean/ZetaRH/ModelTheoreticFrobenius.lean`, target ID
    #MTF-1): eight declarations, sorry-free, `#print axioms` $\subseteq$ `[propext, Classical.choice,
    Quot.sound]`. Four faces: prime-ring rigidity (`endo_fixes_natCast`/`endo_fixes_intCast`), the
    division-ring $\mathbb{Q}$ form (`endo_fixes_ratCast`), the Fermat coordinatewise witness
    (`fermat_little_zmod`, `frobenius_zmod_eq_id`, `zmod_endo_eq_id`: the local Frobenius is the identity
    on the prime field at every $p$, and the prime field is endomorphism-rigid outright), and the NG1
    composite (`ng1_rigidity`: $\sigma \circ \mathrm{algebraMap}\,\mathbb{Q}\,R = \mathrm{algebraMap}\,
    \mathbb{Q}\,R$ for every ring endomorphism $\sigma$ of every $\mathbb{Q}$-algebra $R$, covering the
    2.3a receptacles: adeles, $\prod \mathbb{Z}/p^2/\mathcal{U}$, Witt ultraproducts; no ultrafilter in
    statement or proof, machine-checking the limit-independence). **NG1 is now CANONICAL at 3 independent
    consensus witnesses** (`ModelTheoreticFrobenius.ng1_rigidity` via `RingHom.ext_rat`;
    `TamenessTrade.ng1_rigidity_indep` via `num`/`den` unit cancellation; `BorgerVacuity.ng1_rigidity_w3`
    via `IsLocalization.ringHom_ext` + `Int.subsingleton_ringHom`), satisfying the four-layer consensus rule.
  - T2 (the object; days): $K$ as an ultraproduct of `AlgebraicClosure (ZMod p)` via
    `Mathlib.ModelTheory.Ultraproducts` or a `Filter.Germ` quotient; $\sigma$ coordinatewise; prove
    automorphism, char 0, $\sigma \circ d = d$ (via T1), $\mathrm{Fix}(\sigma) = $ the ultraproduct of
    `ZMod p`. **PARTIAL 2026-07-10** (`lean/ZetaRH/BorgerVacuity.lean`, #MTF-2): the coordinatewise
    Frobenius `productFrobenius` is built on Mathlib's genuine DEPENDENT ultraproduct
    `Filter.Product (fun p => ZMod (P p)) l` (as a bare function) and `productFrobenius_fixes_diag` proves
    $\sigma \circ d = d$ (the Fermat witness via `ZMod.pow_card`, using no filter property = NG1
    limit-independence machine-checked); plus `germRingHom` (a coordinatewise ring endomorphism descends to
    a ring hom on the NON-dependent germ ring `Filter.Germ l R`). WALL: `Filter.Product` carries only a
    model-theoretic `FirstOrder.Language.Ultraproduct.Structure` (+ Łoś), NOT `CommRing`/`Field`/`IsAlgClosed`,
    so `productFrobenius` is not a `RingHom` and "automorphism / char 0 / $\mathrm{Fix}(\sigma)$ pseudofinite"
    need the `FirstOrder.Language.ring` + `CompatibleRing` + Łoś transport Mathlib does not provide
    automatically (feasible, multi-day).
  - T3 (the trivialization statement; hours given T2): every standard prime $q$ is invertible in $K$, hence
    $qK = K$ and for EVERY `f : K →+* K` the lift condition $f(x) - x^q \in qK$ holds trivially: the
    Frobenius-lift congruence is the full endomorphism set, i.e. carries no information. Plus the finite-set
    witness $\{p : x \mapsto x^q \text{ additive on } \overline{\mathbb{F}}_p\} \subseteq \{p : p \mid 2^q - 2\}$.
    **DONE 2026-07-10** (`lean/ZetaRH/BorgerVacuity.lean`, #MTF-3): `borger_lift_congruence_vacuous`
    ($\psi x \equiv x^q \ [\mathrm{SMOD}\ (q)]$ for EVERY $\psi$ and $x$, via
    `natCast_isUnit_of_ne_zero` $\to$ `span_natCast_eq_top` ($\mathrm{span}\{(q{:}R)\} = \top$) $\to$
    `quotient_span_natCast_subsingleton` ($R/qR$ subsingleton) $\to$ `SModEq.top`), the two-endomorphism
    face `borger_lift_any_two_congruent`, and the $\mathbb{Q}$-algebra/prime packaging
    `borger_lift_congruence_vacuous_prime`; sorry-free, `#print axioms` $\subseteq$ `[propext,
    Classical.choice, Quot.sound]`. (The finite-set additivity witness $p \mid 2^q - 2$ is a separate,
    lower-value target not needed for the vacuity core; left unformalized.)
  - T4 (NG2(iii); stretch, self-contained): an ultraproduct of finite sets with sizes $\to_\mathcal{U} \infty$
    has cardinality $\ge 2^{\aleph_0}$; corollary, no internal set is countably infinite. Not proposed:
    ACFA supersimplicity, twisted Lang-Weil (research-scale; cite, do not formalize). **BLOCKED-ON-MATHLIB
    2026-07-10** (#MTF-4): the dichotomy needs a `Saturated` / $\kappa$-saturation predicate on
    `FirstOrder.Language.Structure`, the type-realization (`CompleteType`) machinery, and the internal-subset
    (ultraproduct-of-subsets) API on `Filter.Product`; Mathlib has none of these. Precise failure mode
    recorded in `BorgerVacuity.lean`; building saturation theory is out of scope for this pass.
- **ADVERSARY residual surfaces:** A3 (check that $\mathrm{Fix}(\sigma \circ \phi)$ is a coordinatewise
  ultraproduct for $\phi$ definable with arbitrary parameters, so no leak evades the tier-(iii) dichotomy);
  A1/A2/A4 executed 2026-07-09 (external decorations: rider installed; numerics confirmed; the
  Hindman/idempotent-ultrafilter probe on $\beta P$ came back empty).
- **SURVEYOR:** the tameness-trade question (Section 10); and whether the pseudofinite-dimension literature
  (Hrushovski's pseudo-finite dimensions, CDM descendants) anywhere sums over primes rather than staying
  uniform-per-prime. None found this session.

## 12. One line

The only global Frobenius mathematics has is constitutionally generic: it acts at one nonstandard prime,
fixes all of the arithmetic pointwise (a rigidity that survives every ring-shaped receptacle, adeles
included), lives in a world too tame to state the explicit formula, and carries a vacuous $\Lambda$-structure
because it inverted the primes the congruences were about. The R1 filler must keep all primes alive at once
and must move arithmetic by non-endomorphism means; that pair of necessary conditions is this axis's
contribution to the map.

## References

- J. Ax, *The elementary theory of finite fields*, Ann. of Math. 88 (1968) 239-271 (pp. 239-241 read; the
  Weil-RH + Cebotarev dependency and the "no striking number-theoretic applications" concession, verbatim).
- E. Hrushovski, *The Elementary Theory of the Frobenius Automorphisms*, arXiv:math/0406514 (v2 2022; pp.
  1-8, 117-126 read; Thm 1.1, Prop 11.11 "uses [Deligne 74]", the Cherlin-Jarden negative p. 6, the
  transformal zero-cycles abstract).
- Z. Chatzidakis, E. Hrushovski, *Model theory of difference fields*, Trans. AMS 351 (1999) (ACFA;
  supersimplicity; fixed field pseudofinite); Z. Chatzidakis, 3ECM survey (2000), read in full.
- K.V. Shuddhodan, Y. Varshavsky, *The Hrushovski-Lang-Weil estimates*, arXiv:2106.10682, Algebraic Geometry
  9 (2022) 651-687 (identifier verified live); Bourbaki expose arXiv:2308.16132.
- Y. Dor, E. Hrushovski, arXiv:2212.05366 (valued-field continuation; the WATCH item).
- J. Borger, *Lambda-rings and the field with one element*, arXiv:0906.3146; C. Wilkerson (Λ-structures on
  $\mathbb{Q}$-algebras = commuting endomorphism families); A. Buium, *Arithmetic Differential Equations*,
  AMS Surveys 118 (2005).
- Repo-internal: [`sourcing_gap_r1.md`](sourcing_gap_r1.md) (R1),
  [`stepanov_engine_audit.md`](stepanov_engine_audit.md) (S1/S4),
  [`missing_object_interface.md`](missing_object_interface.md) (SP1-SP5),
  [`deligne_weil1_engine_audit.md`](deligne_weil1_engine_audit.md) (W6), LEARNINGS #62, #133, #145, #148,
  #153, #156.

*Provenance: the working dossiers (SURVEYOR, BUILDER, ADVERSARY with 18 in-place corrections) live in
`scratchpad/model_theoretic_frobenius/{01_surveyor,02_builder,03_adversary}.md`, untracked (scratchpad/ is
gitignored). This document is self-contained; nothing above depends on those files surviving.*
