# The Breadth Program: mathematical breadth as the AI edge on RH

> The strategic program for turning breadth of mathematical knowledge into a genuine advantage on RH.
> Companion to [`math_iteration_engines.md`](math_iteration_engines.md) (the generate/evaluate loop),
> [`reduction_engine.md`](reduction_engine.md) (EVALUATE) and [`generative_engine.md`](generative_engine.md)
> (GENERATE), the disqualifier record in [`eight_angle_sweep_2026-06.md`](eight_angle_sweep_2026-06.md) +
> [`exploration_sweep_2026-06.md`](exploration_sweep_2026-06.md), and the target spec in
> [`08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md) (M4). Read
> [`researcher_mindset.md`](../researcher_mindset.md) first; this program is that mindset applied to the
> one lever AI actually has.

## 0. The thesis (and the trap)

The human research community has spent a century on RH with depth: each researcher pushes one technique to
its frontier. The depth frontier is well-defended. The lever an AI actually has is the **orthogonal** one:
**breadth**, plus three things humans structurally cannot do.

1. **Exhaustiveness.** Hold combinatorial Hodge theory, condensed mathematics, operator algebras, tropical
   geometry, statistical mechanics, and TQFT in working memory at once, and cross-connect them in a single
   pass. No human knows all of these at research depth simultaneously.
2. **No home-field bias.** Search the disreputable corners (physics heuristics, experimental math, IUT,
   q-to-1 numerology) on equal footing with the respectable ones, weighting by structural fit, not by
   sociology.
3. **Persistent, compounding memory.** A corpus that grows every session and never forgets, so the
   hundredth sweep stands on the ninety-nine before it instead of rediscovering them.

**The trap, named so we never fall into it again.** Naive breadth is *accumulation*: survey a field, find
that it realizes $\zeta$ as a trace/determinant/spectrum, never the signature, write CLOSE, repeat. The
project has now executed this loop twelve times (eight-angle #111-#117, four-area #119) with the same
verdict every time: **realization is everywhere, the signature is nowhere but M4.** Breadth-as-accumulation
is a firehose of false positives and CLOSE verdicts; it feels like progress and is not.

**The reframe.** Breadth is an edge only when it is *transfer and compression*, disciplined by an
evaluator. Its three real payoffs:

- **(P1) The one right-polarity transfer source.** Weil proved the function-field RH by *importing* the
  Hodge index theorem from algebraic surfaces. The arithmetic case needs the analogous import, in a form
  with the **right polarity** (contingent on the zeros, not unconditional). Breadth's job is to find that
  one source among thousands of wrong-polarity look-alikes.
- **(P2) Disqualifiers that compress the search.** A single cross-field structural observation can retire a
  whole family of approaches at once. This session's **discriminant screen** ($t_p^2-4p<0$, the complex-root
  half, vs the real-rooted convex/log-concave engine) retired the entire real-stability / Lee-Yang /
  Lorentzian / log-concave family in one inequality (#119). One breadth insight, a permanent reduction of
  the search space. This is the highest-value output, higher than any single survey.
- **(P3) Better components for the assembly.** M4 is an assembly of pieces (a substrate, a Lefschetz
  operator, a primitive decomposition, a duality, a sign). Breadth can supply a strictly better *component*
  even when the whole stays open. The condensed/analytic norm-stack (#119) is a better archimedean-inclusive
  substrate than any prior candidate, even though it carries no sign.

The program below is the machine that extracts P1-P3 from breadth while the disqualifier battery keeps the
firehose off.

## 1. What we are searching FOR (the field-agnostic skeleton of M4)

Breadth fails when it searches by *vocabulary* ("number theory adjacent"). It succeeds when it searches by
*structure*. So the first move is to strip M4 of its number theory and state its bare skeleton, the thing a
transfer source in any field must match.

**M4, stripped.** On a finite-dimensional graded space $V = \bigoplus_k V_k$ with:
- (S1) a **Lefschetz operator** $L$ (degree $+1$, with hard-Lefschetz $L^k: V_{n-k}\xrightarrow{\sim}V_{n+k}$),
- (S2) a **primitive decomposition** $V = \bigoplus L^j P$ ($P$ = primitive part),
- (S3) a **duality / pairing** $Q$ (a perfect, $(-1)$-symmetric or symmetric form; the functional equation),
- (S4) a distinguished **trace datum** $t$ (the Frobenius eigenvalue / the parameter the sign must see),
- (S5) a **polarization**: $Q$ is *definite of a fixed sign* on each primitive piece (the Hodge-Riemann
  bilinear relations), equivalently the signature of $Q$ is the forced $(1, n-1)$ pattern,
- (S6) **right polarity**: (S5) is **contingent** on $t$ (it holds iff the spectral parameter stays on the
  critical locus, and *fails* when a parameter leaves it), NOT an unconditional theorem,
- (S7) **non-circularity**: (S5)-(S6) are proved without inputting the answer (the zeros / the bound on $t$).

RH $\iff$ (S5)-(S6) hold for the specific $(V, L, Q, t)$ attached to the Frobenius side of
$\mathrm{Spec}(\mathbb{Z})$. The realization half (build *some* $(V, L, Q)$ with $\zeta$ as a trace) is free
in framework after framework; (S5)-(S6)-(S7) together are M4.

**The polarity test is the master discriminator.** Almost every "positivity theorem" across mathematics
satisfies (S1)-(S5) but is **wrong polarity**: the Hodge-Riemann signature of a Kähler manifold, a matroid
(AHK), a convex body (Alexandrov-Fenchel), a Lorentzian polynomial, is **unconditional**, $(1,n-1)$ for
*every* valid input, so it can never flip to flag a violation. The Weil/Rosati form is **contingent**: it
flips PSD $\to$ indefinite exactly when a zero leaves the line. A transfer source is useful for P1 only if
its positivity is contingent. The first question to ask any candidate is: **does your signature flip, and
on what does it flip?**

## 2. The breadth corpus (the compounding memory)

A persistent, structured atlas of every place in mathematics and physics where a "positivity / signature /
polarization / forced-middle" phenomenon appears, indexed by the skeleton above so it is **queryable by
structure**. This is the organ that makes memory compound; it lives at
[`experiments/lemma_db/`](../../experiments/lemma_db/) (reuse the existing lemma DB substrate) with a
companion human-readable index at [`breadth_corpus.md`](../../experiments/lemma_db/breadth_corpus.md).

**Schema (one row per phenomenon).**

| Field | Meaning |
|---|---|
| `phenomenon` | the named theorem/structure (e.g. "Hodge-Riemann bilinear relations") |
| `field` | where it lives (Kähler geometry, matroids, CFT, ...) |
| `skeleton_hits` | which of S1-S7 it has |
| `polarity` | **contingent** / **unconditional** / n/a (the master discriminator) |
| `produces` | realization / perfectness / signature |
| `t_slot` | does it have a place for the trace datum $t$? |
| `dh_status` | engages the Euler product, or D-H-blind by type? |
| `regime` | all-heights signature / central L-value (BSD) / Level-3 statistical |
| `distance` | crude distance-to-M4 (how many of S1-S7, right polarity?) |
| `verdict` | TRANSFER-CANDIDATE / DISQUALIFIED-BY / COMPONENT / WATCH |
| `yield` | the durable disqualifier or component it produced |

Seeded from the existing record (the eight-angle and four-area sweeps already populate ~15 rows; the
transfer shortlist Hodge-Riemann / Alexandrov-Fenchel / Bost-Connes; the cohomology landscape's ~16
candidates). The corpus is **append-only and deduplicated**; every sweep adds rows and never re-derives an
existing one.

## 3. The transfer engine (GENERATE, scaled to all of mathematics)

The existing Generative Engine 6b (`experiments/lemma_db/transfer_search.py`) already retrieves proven
positivity theorems nearest the M4 residual. The breadth program scales it from "the lemma DB" to "the
corpus," with the skeleton as the query.

**The query.** Not "what's near number theory" but: *"Return phenomena with (S1) a Lefschetz operator, (S3)
a duality, (S5) a primitive-definite signature, that is (S6) CONTINGENT on a parameter, with (S4) a slot for
a trace datum."* Rank by `skeleton_hits` + right polarity + a $t$-slot. The output is a ranked shortlist of
**transfer candidates**, each with its explicit gap to M4.

**The inversion that finds the good candidates.** The most productive query is not "how do I prove M4" but
**"in what setting is the analogue of (S5)-(S6) a THEOREM, and what makes it work there but not here?"** The
function-field RH is the master answer (Weil: the Hodge index theorem on a surface over $\mathbb{F}_q$). The
program asks the same question of every contingent-positivity theorem in the corpus and reads off the single
missing ingredient. This is lever B generalized to all of mathematics.

## 4. The disqualifier battery (EVALUATE, the guardrail that beats the firehose)

Breadth without an evaluator is the trap. The battery is the Reduction Engine's job: kill false positives
fast, and when a kill generalizes, **bank it as a reusable disqualifier** that retires a whole family. The
current battery (each retires by *regime* or *structure*, not case-by-case):

1. **Davenport-Heilbronn.** Does it distinguish $\zeta$ from D-H (engage the Euler product)? If not,
   structurally wrong. (`experiments/_shared/davenport_heilbronn.py`.)
2. **The e3r polarity test.** Is the signature contingent (right) or unconditional (wrong, like all convex
   Hodge)? (#48.)
3. **The discriminant screen (#119).** Is the positivity on the complex-root half $t^2-4q<0$ (RH's half) or
   the real-root half (the convex/log-concave/Lee-Yang engine)? Retires the entire real-stability family in
   one inequality.
4. **The L-value/order-of-vanishing rule (#113).** Is the native output a central L-value or a rank/derivative
   at the center (BSD/Gross-Zagier regime), rather than the signature across all heights? Retires the
   Gross-Zagier family (Kudla, the eta-invariant #119, the isogeny near-miss).
5. **The R3.5 / K1 wall.** Is it a trace-formula with "spectrum = zeros" (positivity $\iff$ RH, no content),
   with no independent geometric input? (`lean/ZetaRH/R3_5.lean`.)
6. **The cheap-spectral-surrogate disqualifiers (#115/#117).** Is it reweighting-blind (a diagonal
   similarity) or moment-reading (a Jacobi-matrix function), so arithmetic entering only as a measure weight
   is invisible?
7. **The supertrace/grading split (#119).** Is it the Euler-characteristic supertrace (free realization)
   rather than the signature, whose grading is itself the polarization?

The first aimed acquisition batch (acq1, #120) added four more, the **fingerprint screens** (each catches a
*contingent* positivity that is still wrong, which the polarity test #48 alone passes):

8. **The wrong-axis screen (#120).** Does the contingency flip on the **line** axis (Re = 1/2, where RH
   lives), or on a shadow axis: the vertical *spacing* law (level statistics), the *central rank* (symmetry
   type, = the #113 L-value regime), or the *strip width* (a spectral-gap = zero-free region, Architecture
   4)? Only line-axis is right.
9. **The curative-flip screen (#120).** Is the flip **prohibitive** (failure = a forbidden configuration on
   a locus *fixed a priori* by the duality), or **curative** (the locus relocates, support/band/S-curve
   adapts, and the zeros track it)? Curative = realization, and circular (the locus is *solved-for*); this
   operationalizes the K1 wall into a cheap predicate: *is the locus given, or solved-for?*
10. **The input/output split (#120).** Is the positivity an **indefinite signature of the output** (the
    zeros), or a **definite condition on the input** (membership in a stability / Laguerre-Polya / Polya-
    Schur class)? Input-class membership is a kernel property coefficient multiplicativity does not touch,
    hence structurally Euler-blind (it holds for the whole extended Selberg class, D-H included).

The second aimed batch (acq2, #121) tested the fingerprint against its three best candidates and added two
more screens:

11. **The selection-not-sign screen (#121, refines #120).** When a field offers a genuine fixed indefinite
    form *and* a contingency, ask **which object the contingency acts on**: does the **sign** of the form
    flip (definite ↔ indefinite) on a *fixed object set*, or does **class-membership** (which objects are
    in the positive cone) flip while the signature stays fixed? Selection-not-sign is realization (the
    selection moves, curatively). Bridgeland's support-property $Q$ is the type case: a fixed indefinite
    form whose signature *never* flips. So an indefinite form is necessary but not sufficient; the *sign*
    must be the thing that flips.
12. **The special-value / period regime screen (#121, a third tier of #113).** Three increasing distances
    of zeta-contact: zero-*location* (RH), central-*value* / order-of-vanishing (BSD = #113), and
    special-*value* / period ($\zeta(k)$ for $k\geq 2$, periods, Chern-class coefficients; the Gamma
    conjecture, Apery constants). The third tier reads zeta *values* in the convergent half-plane where
    $\zeta$ has no zeros, disqualified by regime *even when structurally deep* (the $\hat\Gamma$-integral
    lattice is a real integral structure, not numerology).

The counting-side frame audit (2026-07-01, #145/#146) added one more screen and a new flavor of an old one.
Both passed the requested ADVERSARY pass on 2026-07-02 (**upheld with corrections**; resolution section in
[`parity_vs_polarization.md`](parity_vs_polarization.md)) and are now **machine-enforced** in
`breadth_corpus.py` (suite 26/26 since #218, 23/23 at the time; the "16/16" previously recorded here was stale, the suite was already
19/19 after #143):

13. **The modulus-only-consumer screen (#146, machine-enforced 2026-07-02).** If a technology consumes a
    polarization theorem only through **sign-free corollaries**, the absolute-value tier
    ($|S| \le 2\sqrt p$, $|\alpha| \le q^{i/2}$) or the angle/monodromy tier (weights in all degrees,
    monodromy classifications, equidistribution laws such as vertical Sato-Tate), then every imported
    statement is invariant under flipping the polarizing form $Q \mapsto -Q$ and no geometric carrier
    crosses the border: the S5 signature never enters and cannot be re-emitted, so the technology can never
    be an M4 **source** no matter how deep its imports (it stays alive as a purity/R1 consumer, and as an
    ingredient in assemblies whose sign is sourced elsewhere, per the #143 operator branch). The ADVERSARY
    corrections: the original binary "modulus bound only" antecedent was too narrow
    (Fouvry-Kowalski-Michel trace functions and Sawin-Shusterman consume the angle/monodromy tier); "sign"
    is pinned to the S5 signature, not eigenvalue phases (Gauss-sum signs, root numbers = S3 data) and not
    proof-internal oscillation (Kloostermania's Kloosterman-sum sign changes are Kuznetsov/operator-sourced).
    Falsifier on record: an analytic argument importing the Hodge-index inequality itself. Encoded as the
    `weil_consumption` skeleton dimension ('sign-free' fires; 'signature' and 'producer' do not). Source:
    [`parity_vs_polarization.md`](parity_vs_polarization.md).

Screen 8 (wrong-axis) also gains a **fourth shadow-axis flavor**, machine-enforced with the same pass: the
**level of distribution** ($\theta \in [1/2, 1]$, the sieve frame's native averaged modulus-range axis,
`axis="level"`), joining spacing / central-rank / strip-width (#146).

The density-matrix round (2026-09-04, LEARNINGS #218) banked the disqualifier the arithmetic Chern-Simons door
had proposed (#177), machine-enforced as the `export_type` skeleton dimension (suite 26/26):

14. **The entropic/torsion-export screen (#218).** What KIND of real-valued object does the candidate export?
    If it is **nonnegative by construction** (an entropy, a mutual information, a relative entropy, a partition
    function) there is no sign to flip; if its **value group is torsion** (a linking form, a root number) it caps
    at $\sigma \bmod 8$; M4 needs the exact signed integer. Scope: the tag applies to the object HANDED to M4 as
    the polarization, not to an internal intermediate (a sum rule with an entropic term, the Killip-Simon
    register, is 'signed' if its export is the signed identity), and 'signed' is provisional until the #48
    polarity is measured on the control cube. Measured on the costume itself in
    [`e3ac_entropic_exports.md`](../../experiments/positivity/e3ac_entropic_exports.md): the Gibbs density
    matrix $\rho_\beta = \sum_n a_n n^{-\beta}|n\rangle\langle n|/L(\beta)$ is diagonal (von Neumann = Shannon,
    the quantum inert), exists exactly where the coefficients are nonnegative (the Euler pencil's segment
    $[-1, 1]$ between the two Epstein forms of $d = -15$, RH-false at every census point $|\lambda| \geq 0.01$
    below height 200, while $L(\chi_{-3})L(\chi_5)$ is an Euler product satisfying RH under GRH whose weights are
    signed), and its one invariant, the total correlation across prime modes = the relative-entropy distance to
    the Euler-product manifold, reads the Euler axis of the control cube and nothing else ($\zeta$ and the
    Beurling fake $0$, Epstein $0.13$ to $0.58$ nats, D-H undefined; the fold $C(+0.05) = C(-0.0491)$ pairs
    census lowest off-line heights $43.4$ and $13.8$, and one height persists across a 25x range of $C$). The
    rank-one state $\sum_n a_n n^{-s}|n\rangle$ reaches $\sigma > 1/2$ for every control, D-H included, and its
    entanglement reads the same axis and is exactly $t$-blind (a product of local unitaries). Two machine screens
    fire on it (#48 unconditional, #218), with the $\beta > 1$ regime the #121 tier by hand; pushed to where it
    could act at the zeros it is costume 2 of the trojan ledger at a temperature. 'entropic' and 'torsion' fire;
    'signed' does not.

**The M4 polarity fingerprint (the acq1 yield, sharpened by acq2).** Screens 2 + 8 + 9 + 10 + 11 compose
into a near necessary-and-sufficient profile: a contingent positivity is a transfer candidate iff it is
**contingent + complex-root + line-axis + output-indefinite-with-the-sign-flipping + prohibitive-on-a-fixed-
locus**, and that profile *is* a polarization (Weil/Rosati). **acq2 converged the search:** tested against
its three best candidates (Bridgeland, the scattering sign, Frobenius manifolds), the fixed-indefinite-form
space outside arithmetic geometry is now mapped and shown *insufficient* (the rare ingredient exists; the
sign-flip + the Frobenius $t$-slot do not). The closest non-arithmetic candidate (Bridgeland) is off by
*exactly one Hodge weight* (its $(2,n{-}2)$ is the weight-2 Mukai polarization; Weil uses the weight-1
$(1,n{-}1)$). So the residual profile **is** M4, and the productive next move is the construction (09A AHK,
Faltings-Hriljac + $\Gamma_S$, lever B) and the `R3_5.lean` VERIFIER target (a discrete-vs-continuous
spectrum predicate separating the Selberg operator-exists case from the zeta scattering-resonance case), not
more breadth draws until a genuinely new orbit point appears. Encoded in `breadth_corpus.py` (`FINGERPRINT`,
`battery()`, `aim()` now reports CONVERGED).

**The battery is the real output.** A sweep is scored not by "areas covered" but by **disqualifiers
produced**. Each new disqualifier is a permanent compression of the search space for every future sweep.
The program's success metric is the *growth and sharpening of this battery*, plus any P1 transfer source or
P3 component. (Tally so far: ~15 screens: 4 from acq1, 2 from acq2, the machine-enforced selection-order
screen from #143, and the machine-enforced modulus-only-consumer screen from #146, ADVERSARY-passed
2026-07-02; the search has CONVERGED, #121.)

## 5. Breadth acquisition: how to reach the UNEXPECTED locations

This is the core of the program: a *principled* method for finding insights in fields no one would think to
connect to RH. Six mechanisms, in increasing order of how non-obvious they are.

1. **Vocabulary-stripping (the bare-structure search).** The same phenomenon hides under different names:
   the Hodge-Riemann relations $=$ hard Lefschetz $=$ the $\mathfrak{sl}_2$ primitive decomposition $=$ (in
   physics) certain reflection-positivity statements. Always search by the skeleton (S1-S7), never by the
   field name. Maintain a **synonym map** of the same structure across fields.
2. **Orbit mapping.** For each phenomenon in the corpus, map its *full orbit*: every field where the same
   abstract structure is a theorem. Hodge-Riemann's orbit so far: Kähler geometry, matroids (AHK), convex
   bodies (Alexandrov-Fenchel), tropical/Berkovich, Lorentzian polynomials, representation theory (hard
   Lefschetz for semisimple Lie algebras). The **unexpected locations are the under-visited points in the
   orbit** of a phenomenon we already care about. (Open orbit points to visit: stability conditions on
   triangulated categories / Bridgeland; Schur / cluster-algebra positivity; the Hodge theory of cluster
   varieties; quantum-cohomology / Frobenius-manifold flatness; the positivity of the Weil-Petersson and
   Hodge metrics; KZ / quantum-group positive bases.)
3. **The Rosetta-stone columns (Weil/Mazur).** Maintain the explicit table of settings where the analogue of
   RH is *solved* (function fields = the master column; finite graphs / Ihara = the Ramanujan column;
   random matrices = the GUE column; the Lee-Yang circle = a wrong-polarity column). Each column is a
   transfer source; reading across is the method. New columns are acquired by asking "where else is a
   'zeros forced to a locus' statement a theorem?"
4. **Deliberate distance sampling.** Each cadence, deliberately sample $k$ fields *far* from number theory
   and run the skeleton query, regardless of apparent relevance. The four-area sweep (SUSY, condensed,
   index theory, Lorentzian) was a hand-run instance; institutionalize it as a standing draw from a
   maintained list of "distant fields not yet swept" (current queue: quantum information: the density-matrix /
   entropy face SWEPT 2026-09-04 (LEARNINGS #218, e3ac, screen 14), entanglement monogamy still undrawn; integrable systems / the tau-function and Riemann-Hilbert;
   free probability / the subordination and the Brown measure; optimal transport / displacement convexity;
   topological recursion / the spectral curve; the c-/a-theorem monotonicity in QFT; persistent homology /
   the stability of the signature under perturbation; error-correcting codes / the MacWilliams duality as a
   functional equation).
5. **Disqualifier-complement mining.** Every disqualifier names a *half* of a space; the productive move is
   to **search the complement**. The discriminant screen says RH lives on the complex-root / negative-
   discriminant half. So the next acquisition is targeted: *which fields produce CONTINGENT, complex-root,
   spectral-gap positivity?* (Candidates the complement points to: the Plancherel-Rotach / Riemann-Hilbert
   transition where real roots become complex; the Lee-Yang *failure* regime; the spectral-gap-contingent
   positivity of transfer operators; the Berry-Tabor vs GUE transition.) Disqualifiers are not just kills;
   each one *aims* the next acquisition.
6. **Cross-corpus pattern mining.** Periodically run a critic over the whole corpus asking "what structural
   pattern do the CONTINGENT-polarity rows share that the unconditional rows lack?" The discriminant screen
   was found this way (the contingent rows are complex-root, the unconditional ones real-root). Each such
   pattern is a candidate new disqualifier or a candidate new transfer feature.

## 6. The value signal (the known blind spot, handled honestly)

The project's standing blind spot ([`generative_engine.md`](generative_engine.md)): there is no gradient at
M4; you cannot tell a near-miss from a far-miss by the proof attempt alone. The breadth program does not
solve this, it *routes around* it:

- The **positive gradient** is the function-field shadow: a candidate is closer if its analogue is the *same
  theorem* that proves function-field RH (lever B), not a different one.
- The **negative gradient** is D-H: a candidate is farther if D-H satisfies it too.
- The **breadth-specific metric** is `distance` in the corpus: how many of S1-S7, and is the polarity right?
  A candidate that hits S1-S5 with *unconditional* polarity is a far-miss dressed as a near-miss; the
  polarity test is the cheap gradient.

Honest statement: breadth gives a *better-sampled* search of the space and a *compounding* disqualifier
battery, not a gradient to descend. Its bet is that the right transfer source (P1) exists and is findable by
exhaustive structural matching, and that even if it does not, the disqualifier battery (P2) will compress
the problem until M4's irreducible content is laid bare. Both are real wins; only the first is a proof.

## 7. Operational cadence

A standing loop, one unit per session, designed so each unit *compounds*:

1. **DRAW.** Pull the next acquisition target by the Pillar-5 mechanisms (an orbit point, a Rosetta column,
   a distant-field sample, or a disqualifier-complement). Prefer disqualifier-complement and orbit draws
   (aimed) over blind distant sampling (cheap but lower yield).
2. **GENERATE.** Run the skeleton query / a SURVEYOR on the target: does the M4 skeleton appear, with what
   polarity, what $t$-slot, what regime?
3. **EVALUATE.** Run the full disqualifier battery + a mandatory D-H and polarity control (the honesty
   engine; every artifact survives a builder $\to$ adversary loop before it is recorded).
4. **EXTRACT.** Bank the durable yield: a new corpus row, and if the kill generalized, a **new disqualifier**
   (the highest-value output). Update the battery, the synonym map, the Rosetta columns, the distant-field
   queue, and the disqualifier-complement aims.
5. **SYNTHESIZE.** When the corpus crosses a structural threshold (e.g. a new contingent-polarity row, or a
   cross-corpus pattern), write it up and re-test the all-roads convergence.

Scored by: disqualifiers produced; transfer candidates with right polarity surfaced; components banked; and
the *shrinkage* of the un-disqualified search space, NOT by areas surveyed.

## 8. Why this could actually move RH (the honest case, not a promise)

The history says M4 is the difficulty and breadth keeps confirming it. So the case for the program is
specific, not triumphal:

- **It is the only lever where AI dominates.** Depth is defended; exhaustive unbiased compounding transfer
  is not a thing humans do, and it is exactly what an AI with persistent memory does best.
- **The compression is real and already happening.** Each sweep has produced a reusable disqualifier (the
  three from the eight-angle sweep, the discriminant screen from the four-area sweep). Five more such, and
  the un-disqualified search space may be small enough that M4's missing ingredient is forced into view.
- **The right transfer source may exist and be hiding in an unexpected location.** Weil's proof was itself a
  transfer from an unexpected location (algebraic surfaces, for a problem about counting points). The
  arithmetic analogue's source, if it exists, is most likely in a field no number theorist has the breadth
  to have checked. That is precisely the search this program runs.
- **Even total failure is a sharp coordinate.** If the program exhausts the corpus and finds no
  right-polarity source, it will have proved, constructively, that M4's content is not a transfer from any
  existing mathematics, which would itself be a profound and publishable statement about the irreducibility
  of RH.

## 9. Concrete next steps

1. **Build the corpus substrate.** Create `experiments/lemma_db/breadth_corpus.{py,md}`: the schema of
   Section 2, seeded from the eight-angle + four-area sweeps and the cohomology landscape (~30 rows), with
   the skeleton query of Section 3 implemented over it (extend `transfer_search.py`).
2. **Run the first aimed acquisition batch.** Use disqualifier-complement mining (Pillar 5.5): the
   discriminant screen points at *contingent, complex-root, spectral-gap positivity*. Sweep the 3-4 fields
   the complement names (Riemann-Hilbert / Plancherel-Rotach transitions, Lee-Yang failure regime, transfer-
   operator spectral-gap positivity, the Berry-Tabor/GUE transition) through GENERATE + EVALUATE.
3. **Map two orbits.** Fully map the orbits of Hodge-Riemann and of "the functional equation as a duality"
   across all fields in the corpus, to expose the under-visited points (Pillar 5.2).
4. **Stand up the cadence.** Adopt Section 7 as the standing per-session loop, with the disqualifier battery
   as the scored output.

## Provenance

Drafted 2026-06-25, in response to the strategic directive that breadth is the AI's edge on RH. Built on the
math-iteration engine arc ([`math_iteration_engines.md`](math_iteration_engines.md),
[`reduction_engine.md`](reduction_engine.md), [`generative_engine.md`](generative_engine.md)), the
disqualifier record (#111-#117, #118, #119), the M4 spec (08A), and the cohomology landscape. This document
is the *methodology*; the corpus and the cadence are the operational organs it specifies.
