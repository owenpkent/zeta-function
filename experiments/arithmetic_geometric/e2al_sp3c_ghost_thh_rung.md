# E2AL: the SP3c/W6 rung on the ghost/THH self-product

**Date**: 2026-07-17. **Status**: EXECUTED, 27/27 checks passed, runtime ~8-25s
(machine-dependent). ADVERSARY-reviewed the same day: verdict PASS_WITH_FIXES;
see [`_e2al_adversary.md`](_e2al_adversary.md) for the full attack record.
**Module**: [`e2al_sp3c_ghost_thh_rung.py`](e2al_sp3c_ghost_thh_rung.py) (869 lines, 27 checks).
**Spec**: [`docs/03_research/c1_joint_build_spec.md`](../../docs/03_research/c1_joint_build_spec.md) (B1 rung 5, the C1 counting joint, derived-base half).
**Run**: `python -m experiments.arithmetic_geometric.e2al_sp3c_ghost_thh_rung`.

This is a companion dossier to the module's own extensive docstring, requested
explicitly by the BUILDER task brief (which asks for a dossier `.md` with a
STATUS banner, honest limitations, the wall statement, and a graded frontier
line) even though the spec's own Section (e) states the e2ai/e2aj/e2ak
precedent is `.py`-only. That deviation from the spec's stated convention is
intentional and is recorded in full at the end of this document.

## STATUS banner

| Phase | Question | Result | Tier (spec Section (d)) |
|---|---|---|---|
| 0 (anchor) | Does an explicit F_p/V_p map reproduce #151's per-prime Poisson/pole identity? | PASS, exactly, by construction | 2. Measured/installed |
| 1 (Gap A + Beurling) | Does N_op have eigenvalue = index; is anything in the battery size-sensitive? | Gap A fails generically; the PREDICTED WALL lands on the RANK sub-layer (Beurling-identical or exempt, confirmed by source inspection AND [ADVERSARY] a literal exponent-vector rebuild); the domain-COUNTING sub-layer is separately shown Beurling-sensitive [ADVERSARY] | 3. Blind, for the rank/size-sensitivity question |
| 2 (Gap B) | Is a necklace+Bökstedt f_TC multiplicative? | The PREDICTED WALL lands: fails at (2,3) for both q0=2 and q0=3; [ADVERSARY] a 7-variant sweep of natural compositions of the same two ingredients ALL fail the same way | 3. Category error, for this candidate and its natural relatives |

No check was graded UNMOVED by default; each phase's grade follows from a
specific measured fact, per the discipline the spec's Section (b) sets up
against Choice-G bookkeeping (LEARNINGS #163).

## 1. Phase 0: the anchor (6 checks, all PASS)

**What was built.** `p_typical_level(p, N, n)`: the level of a p-typical
ghost-lattice index, read off by repeated `apply_F(p, ...)` alone (never by
an independent `log`/factorization call). `ghost_eigenvalue(p, N)`: the
F_pV_p eigenvalue $c_p$, extracted from `apply_F(p, N, apply_V(p, N,
basis(1)))`. The map $\Phi(k) = k \cdot \log(c_p)$ then stands in for
e2aj's own $k \log p$ inside the identical Poisson-summation and
Euler-factor-pole checks.

**Results** (from the run): $c_2=2, c_3=3, c_5=5$ (Check P0.2), so the
Poisson geometric-side defect is $4.44\times10^{-16}$ (Check P0.3, target
$<10^{-10}$) and the pole check passes at $<10^{-12}$ (Check P0.4): both far
inside tolerance because $\Phi$ collapses termwise to e2aj's own formula.

**The honesty finding, stated plainly (as the spec demands).** Because
$c_p = p$ exactly, Checks P0.3/P0.4 are an **exact reproduction by
construction**, not an independent numerical confirmation: this is closer
to the spec's flagged "earlier, narrower wall" than to a fresh derivation.
Two additional checks were built specifically to locate what, if anything,
is genuinely new:

- **P0.5**: the *general* ghost lattice $\{1,2,3,4,5,6\}$ is **not**
  uniformly log-spaced (gap spread $0.51$ over $n=1..5$). The p-typical
  restriction to $\{p^0,p^1,p^2,\dots\}$ is therefore doing real,
  non-vacuous work: it is what turns an arbitrary multiplicative index set
  into the uniform additive lattice Poisson summation actually needs, and
  the spacing constant ($\log c_p$) is read off an intrinsic Witt-calculus
  fact (F_pV_p's eigenvalue), not assumed as "$\log p$" from outside.
- **P0.6**: the bare F_p/V_p monoid is one-sided (`apply_F(p, N,
  basis(1))` returns `{}`): it cannot reach "level $-1$." The two-sided
  Poisson sum used in P0.3 sums $k$ from $-200$ to $200$, so the honest
  account is that the negative half needs the TP/Tate periodicization
  (Nikolaus-Scholze 2-periodicity, cited in Direction 10B and **not
  re-derived here**) to formally invert the Bott class. This is flagged,
  not papered over.

**Verdict**: more than Witt labels painted onto e2aj's identity (P0.5/P0.6
are genuine, checkable content), but the analytic content of Poisson
summation itself remains imported rather than derived from Witt/THH
structure, and the two-sided extension has a named, uncrossed gap. Tier 2
(measured/installed), not tier 1 (W6-genuine).

## 2. Phase 1: Gap A + Beurling size-sensitivity (14 checks, all PASS; 12
original + 2 added by the same-day ADVERSARY round, P1.12/P1.13)

**Reproduction baseline** (P1.1-P1.3): the existing B3 relations
($F_kV_k=k\cdot\mathrm{Id}$, $\mathrm{tr}(V_kF_k)=k\lfloor N/k\rfloor$,
$\mathrm{tr}(F_k)=0$), B4's Bökstedt/Möbius Λ-recovery, and a local
re-derivation of the necklace identities all reproduce exactly at $N=720$,
$i\le500$.

**The Gap A operator, built and tested.** $N_{\mathrm{op}} :=
\sum_{k=2}^{12} V_kF_k$, whose eigenvalue on `basis(n)` is (verified against
the direct F/V composition, not just the closed form) $\sum_{k=2}^{12}
k\cdot[k\mid n]$.

- **P1.4**: on every **prime** in $[2,12]$ ($2,3,5,7,11$), the eigenvalue
  equals the index exactly: Gap A's claim holds, but only because a
  prime's sole divisor in range is itself.
- **P1.5**: on every **composite** in $[2,12]$, it does not: $n=12$ gives
  eigenvalue $27$ ($=2+3+4+6+12$), not $12$; $n=6$ gives $11$; $n=9$ gives
  $12$. This is the "new question this spec adds": spectral data here
  tracks divisor-lattice **rank**, not the raw index.
- **P1.6**: the related operator $\sum_k F_kV_k$ is a **step function** of
  $n$: constant at $77$ ($=\sum_{k=2}^{12}k$) for $n\le60=720/12$, then
  strictly smaller (e.g. $65$ for $n=61..70$). This is the e1l "installed
  by the window/truncation" shape, not a computed, $N$-independent
  invariant.
- **P1.7**: every commutator $[F_a,V_b]$, $a\ne b\in\{2,\dots,12\}$, has
  trace exactly $0$: confirmed computationally (110 pairs, $N=720$) for
  the structural reason both $F_aV_b$ and $V_bF_a$ land at position $bn/a
  \ne n$ whenever $a\ne b$, so no diagonal contribution is possible.

**The Beurling sweep.** Rather than only run a numeric rebuild-and-diff over
a literal relabeled index set (the spec's literal instruction), the module
adds a **structural proof** (Check P1.9): `inspect.getsource` on
`apply_F`/`apply_V` shows their bodies contain no call to any
factorization, `log`, or generator-size lookup: they are pure
ordinary-integer index arithmetic by a small fixed $k$. This means no
*per-element* composition of them (any operator's action on one basis
vector, including N_op's eigenvalue) can see a Beurling relabeling
*by construction*, a stronger claim than "matched numerically on a
sample." A **positive control** (P1.8) confirms this isn't vacuous: an
externally-appended size function $w_{\mathrm{ord}}(n)=\log n$ genuinely
differs from its Beurling-relabeled counterpart (max diff $0.86$ over
$n=2..20$): size information exists in this codebase and the sweep's
machinery is capable of detecting a difference when there is one; it just
never finds one inside the native F_k/V_k layer.

- **P1.10** extends e2ak's C4 check (which tested only B3's own
  Λ-recovery mechanism) to the same divisor-lattice/Chebyshev identity
  using `BeurlingSystem.gen_integers(10000, with_factorization=True)`
  (202 sampled generalized integers, exact integer arithmetic). **Stated
  honestly: this reproduces C4's finding rather than breaking new
  ground**: it is graded as a confirmation, not a novel result.
- **P1.11** finds a genuinely different kind of result for the necklace
  layer: a Beurling generalized integer is **not integer-valued**
  ($\exp(\log b_0+\log b_1)=4.276665$, nearest-integer defect $0.28$), so
  it cannot serve as a necklace *length* $n$ at all: $M(q,n)$ needs $n$ as
  a literal cyclic-group order, an additive/metric notion, not just a
  divisor-lattice rank. This is a **type exemption** (AX-FORM-flavored),
  distinct from "passes identically."

**[ADVERSARY, 2026-07-17] P1.12/P1.13: the literal test, done properly.**
The honest-limitations note originally here (still preserved in Section 5)
argued that a literal Beurling rebuild of the trace/N_op layer was
infeasible because a naive array-*permutation* relabeling overflows the
$N=720$ truncation for composite $k$ (e.g. swapping primes 2 and 3 sends
$2^7=128\to 3^7=2187$). That is true, but it is not the construction the
spec actually names: the spec's own template
(`BeurlingSystem.gen_integers(x, with_factorization=True)`, "exactly as
e2ak's C4 check already does") works in **exponent-vector space**, which
has no array bound at all. Since $F_aF_b=F_{ab}$, every $F_k/V_k$ for
$k=2..12$ decomposes into shifts along $k$'s own prime factors, so the
whole layer is re-expressible as pure exponent-vector arithmetic and the
overflow problem never arises. This *is* buildable, and the ADVERSARY
round built and ran it:

- **P1.12**: on an actual `gen_integers`-derived Beurling domain (1134
  elements at bound $X=720$, vs. 720 rational integers), $\mathrm{tr}(F_k)=0$
  for every $k$ and the N_op eigenvalue-by-structural-pattern (tested on
  "prime $n{=}2$", "prime $n{=}3$", the $n{=}12$-shape $2^2\cdot3$, and the
  $n{=}6$-shape $2\cdot3$) are **identical** to the rational domain
  ($2$, $3$, $27$, $11$ respectively, matching P1.4/P1.5 exactly). The rank
  sub-layer is now confirmed blind by a literal test, not only by source
  inspection, closing the honest-limitations gap for that sub-layer.
- **P1.13**: the *same* rebuild shows $\mathrm{tr}(V_kF_k)$ (a
  domain-**counting** quantity, $k\cdot\#\{$elements divisible by $k\}$,
  unlike the per-element facts above) is **sharply Beurling-sensitive** at
  every $k=2..12$: e.g. $k=2$ gives $720$ on the rational domain vs. $1402$
  on the Beurling domain; $k=8$ gives $720$ vs. $2120$. This is a genuine,
  previously-unmeasured finding, not a restatement of P1.6: it shows that
  **domain truncation by generalized-integer value, not just by varying
  $N$, is a second route by which this counting sub-layer consumes size
  information**, consistent with e2ak's C5a (Beurling integer counting is
  provably not $x+O(1)$). It also **corrects** the original P1.9/P1.12
  wording (now P1.9/P1.14), which over-generalized "apply_F/apply_V's own
  code never references size" (true) into "the whole trace layer cannot
  see a relabeling" (false for this specific counting quantity, once you
  actually build the domain-respecting rebuild rather than reasoning only
  from source inspection).
- **P1.14** (renumbered from the original P1.12) aggregates the RANK
  sub-layer only: every rank/position invariant tested is Beurling-identical
  or structurally exempt, now confirmed by *both* source inspection (P1.9)
  and a literal rebuild (P1.12); the size-sensitive quantities are the
  externally-appended control (P1.8) *and* the domain-counting invariants
  (P1.13), never a rank quantity.

**Verdict.** The pre-registered wall (spec Section (d)'s "single most
likely result") lands on the rank/position sub-layer, and lands for a
*named, proven* reason rather than only a numerical coincidence: the
ghost/THH combinatorial layer, as built from $\{F_k,V_k:k=2..12\}$ and
composed per-element, consumes only the abstract divisor-lattice shape of
the index set and never a generator's actual size. **[ADVERSARY]** The
domain-*counting* sub-layer is a different story: P1.13 shows it consumes
size through the truncation boundary, which sharpens rather than
contradicts the picture, since that sub-layer was already separately
diagnosed "installed, not computed" by P1.6 on N-truncation grounds alone.
Neither sub-layer pays the LATTICE-CONSUMING fourth clause (LEARNINGS
#152) in the way SP3c needs: the rank sub-layer cannot see size at all, and
the counting sub-layer sees only truncation-boundary artifacts, not a
forced arithmetic identity. A further, sharper reading falls out of
P1.4/P1.5/P1.14 together: Gap A's own claim ("$N$ acts on level $i$ with
eigenvalue $i$") is, even where it holds (P1.4, on primes), an
**index/rank** statement (which basis vector, not how big it is) rather
than a **size/metric** statement: so even a fully successful,
globally-true Gap A would not by itself have closed the Beurling gap.
Tier 3 (blind) for the size-sensitivity question this spec adds on top of
Gap A's original claim, on the rank sub-layer specifically.

## 3. Phase 2: Gap B multiplicativity (7 checks, all PASS: all confirm the
predicted wall; 6 original + 1 added by the same-day ADVERSARY round, P2.7)

**What was built.** $f_{TC}(n) := \sum_{d\mid n}\mu(n/d)\cdot d\cdot
M(q_0,d)$: Möbius inversion (the Gap-B conjectured TC mechanism) applied to
the necklace weight $M(q_0,d)$ multiplied by the Bökstedt torsion order $d$
itself (the cited integer $|\mathrm{THH}_{2d-1}(\mathbb Z)|=d$, entering as
a plain multiplier, never a looked-up von Mangoldt/zeta value). All
arithmetic is exact (`fractions.Fraction`), computed for $n\le500$ at two
fixed alphabet sizes $q_0\in\{2,3\}$.

**Results.**

- **P2.1** (sanity): $f_{TC}(7)=124$ at $q_0=2$, matching the direct
  2-term hand expansion: implementation correctness confirmed.
- **P2.2** (boundary, reported rather than hidden): $f_{TC}(1)=q_0$ exactly
  ($2$ or $3$), never $1$. The multiplicative normalization a genuine Euler
  product needs fails immediately at the unit: itself a signature of an
  additive (Möbius-sum) rather than multiplicative (Euler-product)
  construction.
- **P2.3/P2.4** (the main test, 643 coprime pairs $2\le m<n$, $mn\le500$,
  swept separately from the P2.2 boundary case so the core mechanism gets a
  fair reading): fails at the **very first** pair tested, $(m,n)=(2,3)$,
  for *both* $q_0$ values:
  - $q_0=2$: $f_{TC}(2)=0$, $f_{TC}(3)=4$, $f_{TC}(6)=48 \ne
    f_{TC}(2)f_{TC}(3)=0$.
  - $q_0=3$: $f_{TC}(2)=3$, $f_{TC}(3)=21$, $f_{TC}(6)=669 \ne
    f_{TC}(2)f_{TC}(3)=63$.
  (Per this codebase's own convention for pre-registered negative outcomes,
  matching e2aj's "overcount" check and e2ak's "NOT $x+O(1)$" check,
  the check's PASS condition tests *whether the predicted wall is
  confirmed*, not whether the naive multiplicativity claim holds; a
  genuinely multiplicative $f_{TC}$ would have shown as the check's own
  "SURPRISE" branch, so this is not a check rigged to always pass.)
- **P2.5/P2.6** (K1): a static source scan of `f_tc`'s own body finds no
  reference to a Λ/zeta table, and a runtime call-count guard on the
  imported Λ-table helper (`lambda_vec`) shows **zero** calls during Phase
  2's entire construction-and-sweep window (3690 calls before, 3690 after:
  all of them Phase 1's legitimate B4 reproduction).

**[ADVERSARY, 2026-07-17] Check P2.7, the strawman check: seven natural
variants, all fail the same way.** To confirm this isn't an artifact of the
one composition the builder happened to pick, the ADVERSARY round swept six
other natural compositions of the same two ingredients (necklace weight
$M(q_0,n)$, Bökstedt order) over the same coprime-pair grid convention
(m starting at 2, matching P2.3/P2.4 exactly). Five are tracked as **Check
P2.7** (exact `Fraction` arithmetic, matching this module's convention):
the necklace weight alone without the torsion factor; the raw $M(q_0,n)$
with no Möbius composition at all; a Möbius **product** form
($\prod_{d\mid n}(dM(q_0,d))^{\mu(n/d)}$, the Euler-product-native
inversion, as opposed to the additive Möbius sum); the same product form on
the necklace weight alone; and a sign-alternating variant
($(-1)^d$-weighted). A sixth, log-composed variant matching B4's actual
$\log|\mathrm{torsion}|$ shape rather than the raw order $d$ was checked
informally with floats (not tracked in P2.7, since it falls outside this
module's exact-arithmetic convention) and also fails. **All seven
(including the builder's own P2.3/P2.4 candidate) fail, and all fail at the
same first pair $(m,n)=(2,3)$**, across both $q_0=2$ and $q_0=3$ (10
variant/alphabet combinations in P2.7 alone). This upgrades the dossier's
claim from "our one candidate fails" to "no natural necklace-Bökstedt
composition tested is multiplicative," while still stopping short of an
exhaustive search (see Section 5).

**Verdict.** The predicted wall (spec table: "likely WALL (additive, not
multiplicative)") lands, confirming the standing adversary flag (10B doc:
"a likely category error... $1/\zeta$ is multiplicative over primes" while
the equalizer is "an additive limit") **computationally**, not just
heuristically, and at the very first nontrivial pair, not a marginal or
edge-case failure. [ADVERSARY] Confirmed robust across seven natural
variants, not just the one construction. Tier 3 (category error) **for
this specific candidate and its tested natural relatives**; see Section 4
(honest limitations) for the scope of that claim.

## 4. Disciplines

- **Beurling**: Phase 1 *is* the discipline sweep (Section 2). The
  nameable failing clause: the ghost/THH combinatorial layer consumes only
  divisor-lattice shape, never generator size, so it cannot pay the
  LATTICE-CONSUMING clause (#152). Proved structurally (P1.9), not just
  observed.
- **Davenport-Heilbronn**: structurally exempt, unchanged from e2ai/e2aj/
  e2ak: every object here is built from $\mathbb Z$'s unique-factorization
  monoid; D-H has no Euler product and hence no monoid to test (AX-FORM).
  No D-H check appears in this battery, and none belongs.
- **K1**: no zeta zero location enters any construction step anywhere in
  the module (verified by inspection: no `mp.zetazero`, no `ZETA_ZEROS`,
  no fitted $\gamma_n$). Phase 2's specific named risk (calibrating
  $f_{TC}$ against Λ or a zeta coefficient) is guarded twice (P2.5 static,
  P2.6 runtime), both clean.

## 5. Honest limitations

- **Phase 0's reproduction is exact by construction**, not independent
  confirmation (Section 1). Treat P0.3/P0.4 as consistency checks on the
  translation, not as new evidence for the Poisson identity itself.
- **[UPDATED, ADVERSARY 2026-07-17] The Beurling sweep for the F_k/V_k/N_op
  layer originally relied on a structural proof (source inspection, P1.9)
  more than a literal numeric rebuild-and-diff.** The original reasoning
  stands for *why a naive rebuild was skipped*: a permutation-based
  relabeling that keeps positions inside the fixed $N=720$ array genuinely
  runs into range-overflow for the composite $k$'s used here (e.g. swapping
  the roles of primes 2 and 3 sends $2^7=128$ to $3^7=2187$). But that is
  not the only literal construction available, and it is not the one the
  spec actually names: `BeurlingSystem.gen_integers(x,
  with_factorization=True)` (the spec's own named template, "exactly as
  e2ak's C4 check already does") works in exponent-vector space, which has
  no array bound, so the overflow problem does not apply to it. The
  ADVERSARY round built and ran that literal rebuild (P1.12/P1.13, Section
  2): it **confirms** the rank sub-layer's blindness literally (not only by
  source inspection) and **additionally finds** that the domain-counting
  sub-layer (tr(V_kF_k)) is genuinely Beurling-sensitive, a result the
  source-inspection argument alone could not have surfaced (P1.9 only
  proves apply_F/apply_V's own code is size-blind, which bounds the
  per-element layer but says nothing about domain-wide aggregates). P1.10
  (the Λ-recovery piece) still uses the literal `gen_integers` route
  independently, and P1.11 (necklace) is still argued by direct
  construction on actual `BeurlingSystem` data.
- **P1.10 reproduces e2ak's C4 finding rather than extending it** in any
  substantive sense: both check the same underlying divisor-lattice
  Chebyshev identity. The genuinely new material in Phase 1 is P1.4-P1.9,
  P1.11, and [ADVERSARY] P1.12-P1.13 (the N_op construction, the
  truncation-coupling and commutator findings, the structural-blindness
  proof now literally confirmed, the necklace type exemption, and the
  literal rank-vs-counting split), not P1.10.
- **Phase 2's f_TC is one candidate construction**, not an exhaustive
  search. It was built by direct analogy to B4's own Möbius-inversion
  mechanism (substituting the necklace weight $M(q_0,d)$ for B4's bare
  weight 1, per the spec's "necklace weights composed with Bökstedt-torsion
  data" instruction) and tested at two alphabet sizes ($q_0=2,3$) that both
  fail at the same pair, a real robustness signal, but originally not a
  sweep over all $q_0$ or all plausible necklace-Bökstedt compositions.
  **[ADVERSARY, 2026-07-17]** this gap is now partly closed: a sweep of
  six other natural compositions (Section 3) all fail the same way at the
  same first pair, which is stronger evidence than one construction's
  failure, though it remains a finite, not exhaustive, sweep (a systematic
  search over all $q_0$, or a formal argument that Möbius-sum constructions
  can never be multiplicative for a structural reason, is still open). The
  finding should be read as "no natural candidate this module or its
  ADVERSARY-swept relatives supply is multiplicative, for a reason (the
  unit-normalization gap, P2.2) that is a general signature of
  Möbius-inversion/additive constructions" rather than "no
  necklace-Bökstedt composition can ever be multiplicative," which remains
  unproven.
- **Line count**: 869 lines (up from the original build's 645; the
  ADVERSARY round added the P1.12/P1.13/P2.7 literal-test checks and their
  documentation), above the spec's own "350-450, extended for three dense
  phases" estimate and the BUILDER brief's "400-600" target's upper edge.
  The overrun is concentrated in the module docstring, the honesty/
  discipline commentary threaded through every check's `detail` string,
  and now the literal-rebuild helper functions; no phase's core logic is
  bloated relative to its e2ai/e2aj/e2ak precedent, and the ADVERSARY
  addition closes a named evidentiary gap rather than padding the count.

## 6. The frontier line (graded, not auto-UNMOVED)

Per the spec's own pre-registered instruction (Section (d)): if Phase 1's
wall lands as predicted, "it should be recorded as the next LEARNINGS
entry... stated as: Gap A closes (not 'proves,' but 'is shown structurally
incapable of supplying the needed channel'), Direction 10B is updated to
mark Gap A resolved-negatively rather than open, and C1's derived-base half
is narrowed to a single remaining question." That is exactly what
happened, **and** Phase 2 independently landed its own predicted wall the
same session, so the proposed entry below folds both in. This text is a
**proposal for a SYNTHESIZER pass** (updating `LEARNINGS.md` and Direction
10B is outside this BUILDER task's scope as instructed).

**[ADVERSARY, 2026-07-17] entry-number correction.** The original text here
claimed "the highest entry number directly confirmed present in
`LEARNINGS.md` at time of writing is #164," with #165 flagged as possibly
already taken but unresolved. That search missed an entry that is in fact
present: `### 165. THE #154 LEDGER RETIRED...` (the e1p rank-one-interlacing
retirement, same day, 2026-07-17) is confirmed in `LEARNINGS.md` by direct
search. **#165 is taken. The correct next number is #166**, not "#165 or
#166, TBD." (Per the ADVERSARY task brief, `LEARNINGS.md` itself is left
untouched here; this is a correction to this dossier's own proposal text
only, for the SYNTHESIZER pass to consume directly.)

> **Proposed LEARNINGS entry (#166): the ghost/THH algebraic route to C1
> closes on both Gap A and Gap B, for named structural reasons; the
> derived-base half of C1 now needs a metric ingredient it does not itself
> supply.** e2al (27/27, BUILDER + ADVERSARY, PASS_WITH_FIXES) tested the
> two concrete, previously unresolved Direction 10B sub-questions about the
> ghost/THH self-product computationally. **Gap A** (does $N$ built from
> $F_nV_n=n$ act with eigenvalue = level index?) holds only in the
> degenerate corner where the index is itself one of the few available
> generators (primes in $[2,12]$: exact match) and fails generically off
> that corner (composites: a divisor-sum, not the index). Worse for the
> conjecture's ultimate purpose: even the successful corner is an
> index/rank fact, not a size fact, and a source-level proof, upgraded by
> the ADVERSARY round to a literal exponent-vector rebuild on an actual
> Beurling domain (not only a sample or a source-inspection argument),
> shows the entire $\{F_k,V_k\}$-generated *rank/position* operator algebra
> is blind to any Beurling (generator-size) relabeling by construction: it
> consumes only divisor-lattice shape. [ADVERSARY] The *domain-counting*
> sub-layer (tr(V_kF_k)) is the opposite: a literal rebuild shows it IS
> Beurling-sensitive, consistent with (not a reversal of) its already-known
> N-truncation-installed status. This sharpens, rather than merely repeats,
> #152's finding (which tested only the $B3$ Λ-recovery mechanism): the
> LATTICE-CONSUMING fourth clause is unpayable by *any rank-based* operator
> this apparatus can build, while the counting-based operators pay only a
> truncation artifact, not a forced identity. **Gap B** (does the THH→TC
> equalizer realize the necklace/Möbius map from $-\zeta'$ to
> $-\zeta'/\zeta$?) fails multiplicativity at the first nontrivial coprime
> pair (2,3), confirming the standing adversary flag ("a likely category
> error... equalizer is additive, $1/\zeta$ is multiplicative")
> computationally rather than only heuristically, and [ADVERSARY] confirmed
> robust across a 7-variant sweep of natural necklace-Bökstedt compositions,
> all of which fail at the same pair. **Net**: C1's derived-base half (the
> algebraic sibling of the just-closed CCM corridor's analytic route) now
> converges on the *same* missing ingredient the analytic route converges
> on (#152/#153): a genuine metric/archimedean channel that the purely
> combinatorial Witt/necklace skeleton cannot supply on its own. This is a
> coordinate ruled out, not a dead end: C1's two live sub-fronts
> (CCM-analytic, ghost/THH-algebraic) agree on what is missing, which is
> new information neither supplied alone.

## Pointers

- Spec this executes: [`docs/03_research/c1_joint_build_spec.md`](../../docs/03_research/c1_joint_build_spec.md).
- Interface doc (SP3c, the joint): [`docs/03_research/missing_object_interface.md`](../../docs/03_research/missing_object_interface.md) Sections 1, 4, 5.
- The two named gaps: [`docs/03_research/research_directions/10B_thh_weight_and_mobius.md`](../../docs/03_research/research_directions/10B_thh_weight_and_mobius.md).
- Precedent modules extended here: [`e2ai_base_battery.py`](e2ai_base_battery.py) (B3/B4), [`e2aj_w6_gluing.py`](e2aj_w6_gluing.py) (Poisson/pole target), [`e2ak_beurling_discipline.py`](e2ak_beurling_discipline.py) (the C1-C5 discipline template, C4 extended by P1.10).
- Necklace model (not imported, re-derived locally per the spec's cross-family-import guidance): [`experiments/homotopy/e_necklace_mobius.py`](../homotopy/e_necklace_mobius.py).
- Grading vocabulary: `experiments/spectral/e1l_absorption_count.py` (W6-shaped vs. installed), `experiments/spectral/e1p_rank_one_interlacing.py` (measured profile vs. theorem instance; the source-scan-plus-runtime-guard K1 pattern reused for P2.5/P2.6).
- ADVERSARY record (2026-07-17, same day): [`_e2al_adversary.md`](_e2al_adversary.md): the attack list, the literal Beurling rebuild (P1.12/P1.13), the Phase 2 seven-variant sweep, the em-dash and LEARNINGS-numbering fixes, and the final verdict.

## Deviations from the spec, with reasons

1. **A dossier `.md` was written despite the spec's Section (e) stating the
   e2ai/e2aj/e2ak precedent is `.py`-only.** The direct BUILDER task
   instruction from the orchestrator explicitly requested this file with
   specific required sections; that more specific, more recent instruction
   is followed here, and the deviation from the spec's own stated
   convention is recorded as requested.
2. **No `.npz` file was written.** Every result here is exact
   integer/rational or small-scale float data (no array data of the kind
   the spectral `e1*` family saves); this matches the task brief's own
   hedge ("exact-arithmetic results may not need one") and the e2ai/e2aj/
   e2ak precedent.
3. **[RESOLVED, ADVERSARY 2026-07-17] The Beurling sweep for the trace/N_op
   layer (Phase 1) originally used a structural source-inspection proof
   (P1.9) as the primary evidence, supplemented by a literal
   `BeurlingSystem.gen_integers`-based rebuild for the Λ-recovery and
   necklace pieces (P1.10/P1.11) only.** The reasoning for skipping a
   literal rebuild of the trace/N_op layer itself was half right: a literal
   *permutation*-based relabeling of the $N=720$ ghost lattice does run
   into range-overflow for several composite $k$ values (e.g. $2^7=128\to
   3^7=2187$ under a prime-2/3 swap). But the spec's own named template
   (exponent-vector arithmetic via `gen_integers`) sidesteps this, and the
   ADVERSARY round built and ran it (P1.12/P1.13, Section 2): the rank
   sub-layer is now confirmed blind by a literal test, and the
   domain-counting sub-layer is shown genuinely Beurling-sensitive, a
   finding the original source-inspection-only approach could not have
   produced.
4. **Module length is 869 lines** (up from the original 645; the ADVERSARY
   round added Checks P1.12/P1.13/P2.7 and their documentation), above the
   spec's "350-450" estimate and at the upper edge of the task brief's
   "400-600" target. Attributed to the volume of honesty/discipline
   commentary the spec itself demands (Phase 0's honesty requirement,
   Phase 1's "both outcomes informative" design, the K1 guard pattern) plus
   the ADVERSARY literal-rebuild and strawman-sweep additions, rather than
   to unneeded generality; not trimmed further because doing so would have
   meant cutting exactly the content the spec (and the adversary review)
   asks for.
5. **Check count is 27** (24 original + 3 added by the ADVERSARY round:
   P1.12, P1.13, P2.7), inside the spec's own "20-28" estimate. Not
   trimmed, since every check (including the three added ones) maps to a
   specific, separately falsifiable claim; three checks across the module
   (P0.4, P1.4/P1.5 via their shared closed-form helper, P2.1) were
   spot-verified by deliberately corrupting the underlying computation in a
   scratch copy and confirming each failure is correctly detected (see the
   ADVERSARY record).
6. **[ADVERSARY, 2026-07-17] Twenty-four em dashes in this file's original
   text were replaced with periods, colons, or commas**, per CLAUDE.md's
   "no em dashes anywhere" style rule (the module's own `.py` docstring was
   already clean; only this companion `.md` needed the fix).
