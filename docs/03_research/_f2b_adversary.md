# ADVERSARY report: F2b, the visibility-floor law (same-session, mandated)

> ADVERSARY deliverable, 2026-08-28, frame session F2b of the funding-boundary frame.
> Targets: [`f2b_visibility_floor.md`](f2b_visibility_floor.md) (the theorem document),
> [`../../experiments/spectral/e1ag_visibility_curve.py`](../../experiments/spectral/e1ag_visibility_curve.py)
> with dossier
> [`../../experiments/spectral/e1ag_visibility_curve.md`](../../experiments/spectral/e1ag_visibility_curve.md)
> (the calibration build), and
> [`../../lean/ZetaRH/F2bSkeleton.lean`](../../lean/ZetaRH/F2bSkeleton.lean) (the Section 5
> bar's artifact). Frozen foundation read in full and not re-attacked:
> [`f2a_certificate_class.md`](f2a_certificate_class.md) (delta-checked),
> [`_f2a_class_adversary.md`](_f2a_class_adversary.md),
> [`_f2a_delta_check.md`](_f2a_delta_check.md),
> [`reading_notes/glss_full_funding_boundary.md`](reading_notes/glss_full_funding_boundary.md)
> Sections 1-2. Charter: exit 2's letter (theorem-shape at the Section 5 bar, or an evading
> family, by end of F2b), the #206 verdict wiring (the grade is this report's), the
> #209 audit's named generosity warning at exactly this session, and LEARNINGS #211(iv)(b)
> (if only the scope-honesty theorem lands, exit 2's language must say so). This report
> edits nothing; fixes are listed for the builder. No em dashes anywhere.
>
> **Verdict up front: PASS_WITH_FIXES** (ten blocking fixes, each with an explicit
> counterexample or drift witness below; none requires new mathematics beyond what this
> report supplies). **Grade: non-UNMOVED, carried by mint M2 alone** (the two-sided
> resolution frontier), conditional on the M2-touching blocking fixes (F2, F3, F4, F7,
> F8) landing in the session's bounded fix pass, per the F2a re-pose precedent. M4 does
> NOT land as delivered (proof gaps, not named hypotheses). Exit 2 does not fire, at the
> narrowed scope stated in G.

---

## 0. Reproduction record (mandated; executed first)

- **Build, quick**: `.venv/bin/python -m experiments.spectral.e1ag_visibility_curve --quick`:
  **15/15 passed (1 s)**, all four pre-registrations SURVIVED. Envelope rel err
  $2.12 \times 10^{-15}$; block/rescue 6372x / 0.0000x; C0 finding 7.9x; frontier
  products $[3.93, 3.93, 3.93]$ spread 1.000; band 3.24; exchange $10/37 = 0.27$.
- **Build, full**: **16/16 passed (7 s)**, all four pre-registrations SURVIVED.
  Headline numbers verified against the dossier line by line: envelope rel err
  $6.92 \times 10^{-15}$ (dossier $6.9 \times 10^{-15}$); Bernstein $0.1855 \le 0.2527$;
  C0 naive-site block 105.9x (dossier 106x); C1 worst 0.60x slack with $E = 44 = 2k$;
  D1 exchange $44/147 = 0.30$; D2 second rung 0.32x with $E = 2k$; E1 block 6393x;
  E2 rescue 0.0000x with $E = 48$; F1 products $[5.29, 5.29, 5.29]$ spread 1.000;
  F2 band 3.98 vs $\log 100 = 4.61$; F3 $N_{\mathrm{off}} = 40$ at $\delta = 0.0108$
  (dossier 0.011), link shift 0.23x, $E$ unchanged; G1 landmark $\gamma = 85.699$,
  $\beta = 0.8085$, FE-paired, $E(\mathrm{strip}) = 2$; G2 type refusal. **One drift**:
  the run prints $N = 14659$ ($T L = 14658.7$, rounds to 14659; quick $N = 3664 =
  14659 // 4$) while the dossier claims $N = 14657$ twice (fix F10). Runtime 7 s vs the
  dossier's 6 s: noise, no fix.
- **Lean**: `~/.elan/bin/lake env lean ZetaRH/F2bSkeleton.lean`: **exit 0, zero errors,
  exactly two `sorry` warnings** (lines 190 and 228, i.e. V-F2b-6 and V-F2b-7), plus one
  cosmetic linter warning (line 97, `unnecessarySeqFocus`). The Section 9 claim
  "typechecks standalone with zero errors, exactly two sorry-bodied statements" is
  CONFIRMED at the typecheck tier. Statement-drift findings are attack G/fixes F7-F9.
- **D-H cell provenance probe** (beyond the mandate): the shared control's scan at the
  cached tuple returns BOTH members of the landmark pair ($0.8085 + 85.699i$ and
  $0.1915 + 85.699i$), so gate G1's insert-partner fallback branch was NOT exercised and
  the module docstring's "measured: $\beta_1 + \beta_2 = 1$, $\gamma_1 = \gamma_2$" is
  accurate as run. (Recommended, non-blocking: log found-vs-inserted so a future cache
  change cannot silently manufacture the pair.)

## 1. Attack A: the site-selection lemma L4 and the resonance budget L5. LANDED (three findings; the rigid route survives)

**A.1 The balancing invariant is unproven and false as stated.** L4(ii) asserts: "GREEDY
VECTOR BALANCING of the selected $v_e$'s across all granted resonance frequencies
simultaneously keeps every partial sum $\le \max_e |v_e|$ (Steinitz-type, finitely many
frequencies per L5)." No Steinitz-type theorem delivers that constant (the classical
Steinitz lemma reorders a ZERO-SUM set and pays a dimension constant; selection from a
$3k$ pool is a different problem), and the invariant is false for adversarial phase
pools: if every candidate's phase $u_0 c_e \bmod 2\pi$ lies in one half-plane at a
granted frequency, every selection has $|\sum_e v_e| \ge c \sum_e |v_e| \asymp k \min
|v_e|$, greedy or not, so partial sums grow linearly. A same-phase pool at a single
frequency already defeats it; with two frequencies at integer ratio ($u, 2u$) even
antipodal pairing is impossible ($u\tau \equiv \pi$ forces $2u\tau \equiv 0 \ne \pi$)
and cancellation needs batches (cube-roots-of-unity triples work at ratio 2). What is
provable is a batch-selection bound $\le C(R)\max_e|v_e|$ with $C(R)$ depending on the
frequency count and rational structure. CONSEQUENCE: the regime condition's residual
$\bar v$ ("bounded by the largest selected $|v_e|$") understates by the factor $C(R)$,
and since $R(T) = O(\Delta\,\mathrm{polylog})$ may grow with $T$, the factor must be
carried explicitly. Fix F5(a).

**A.2 The generic route misses repulsion-law batteries (the positioning kick).**
A granted small-gap repulsion law (e.g. "$N(T, \lambda_0) = 0 + o(TL)$" at fixed
$\lambda_0$, or AH-Pairs) is jointly satisfiable by bases with NO gaps below
$\lambda_0$; on such a base the existing-small-gap candidate pool of L4(ii) is EMPTY.
The mover must position pairs, which the o-class repulsion law tolerates (sub-slack
many small gaps are invisible to it: the absolute-error reading working as designed),
but the positioning's own resonance cost is NOT small: moving the pair
$(\gamma_1, \gamma_2)$ to a chosen midpoint $m$ changes $\Sigma(u)$ by the exact
three-term vector $v_e = 2e^{ium} - e^{iu\gamma_1} - e^{iu\gamma_2}$ of magnitude
$2(1 - \cos(u s_0/2)) = O(1)$ at the ORIGINAL gap $s_0 \asymp 1$, not at the target
gap. L3 explicitly defers non-decaying families to L4; L4's generic route balances only
the merge $v_e$'s of existing candidates: the seam is covered by neither. The repair
exists and is bounded: state the selection over TOTAL position-plus-merge cost vectors
with the mover-chosen midpoint phase $e^{ium}$ as a free parameter (this is in fact
what the build's `select_sites` computes: its `v[a,b]` is the total three-term vector),
and prove the free-phase balancing. Note the build cannot rescue the written lemma: its
C1/E2 instances probe benign equidistributed phase pools only. Fix F5(b), F5(c).

**A.3 L5's display is false as stated.** "Over any C0-configuration with
$N^{\circledast}(T) \le C_0 TL$: $\int_W |\Sigma(u)|^2 du \le C |W| N^{\circledast}
\cdot A$ for unit windows, by the MV mean-value theorem." The MV theorem carries a
min-spacing correction ($\int \le \sum |a_n|^2 (|W| + 3\pi/\delta_n)$), which the cap
on $N^{\circledast}$ does not control. Counterexample: $N/m$ clusters of $m$ simple
lines ($h \equiv 1$, so $N^{\circledast} = N$) at intra-cluster spacing $2^{-T}$: at
every accessible $u$ the sum behaves as the cluster-collapsed configuration with
$N^{\circledast}_{\mathrm{eff}} = mN \gg N$, and $\int_W |\Sigma|^2 \asymp |W| m N$
violates the display. The CONCLUSION survives at the same strength: replace
$N^{\circledast}$ by the unit-resolution pair count $N^{\circledast} + N(T, O(1))$,
which the same core (Fujii plus the combinatorial identity) caps at $C \cdot TL$, so
$R(T)$'s bound is unchanged. The lemma's proof route must be corrected (smoothed-window
Fejér pair-count bound, or MV with the spacing hypothesis made explicit). Fix F6.

**A.4 What survives A.** The rigid-base route L4(i) is exact and pretty ($v_e = 2 - 1 -
1 = 0$ identically at aligned sites; the build's 6393x / 0.0000x dichotomy measures
it); the regime condition's honest-scope framing survives with the $C(R)$ reweighting;
the amplification diagnosis itself (the F2a (M) bookkeeping false for $|\Sigma|^2$
reads) is correct and independently confirmed by gate C0.

## 2. Attack B: the slack bootstrap L3. MISSED (survives)

The absolute-vs-relative seam holds: positioning $k \le c_1 \varepsilon_G TL$
near-coincident pairs costs each granted family $O(k)$ absolute, below every $o(TL)$
absolute slack; the shrinking-window exactness smuggler needs the relative reading,
which the delta-check's edit 1 excluded; a granted small-gap repulsion law cannot
forbid sub-slack many positioned pairs (its own slack tolerates them), and the damage
that battery does lands on L4's generic route (attack A.2), not on L3. Moment-shaped
families at other normalizations: the fixed-$n$ coincidence family costs the fixed
constant $2^n - 2$ per event, within L3's $C_{\mathrm{bat}}$ accounting per family. The
one real battery-level attack I found is against Theorem 1's PARAMETRIZATION, not
L3's satisfiability, and is filed under attack C.

## 3. Attack C: Theorem 1. PARTIAL (the ceiling (ii) survives; the sharpness (iii) is false at an admissible battery)

**C.1 The ceiling (ii): MISSED (survives).** The GLSS subtraction is correctly quoted:
the combinatorial identity matches the reading note's Proposition 1, the Fujii floor
term $\frac{TL}{\lambda}\sqrt{\log(2+\lambda)}$ is present and correctly placed, the
moving-window requirement ($\lambda(T) \to \infty$ per GLSS Remark 1) is stated, the
$\varepsilon$-endpoint recovers GLSS I/II and the GS25 density-register exchange. The
engine's in-class membership is airtight under the delta-checked pool: arity 2, bounded
Fejér amplitude, Remark-1 window clause, $o(TL)$ absolute, finite-rank realizable per
C1(ii), satisfiability presupposition carried as the delta-check prescribed. The
unconditional cap $N^{\circledast} \le C_0 TL$ from the core alone checks (two lines,
$U = 1/L$).

**C.2 The sharpness (iii): LANDED.** The countable graded coincidence battery
$G^{\sharp} = \{\Phi_n : n \ge 2\}$, $\Phi_n := \sum_{\mathrm{lines}} h^n$, each
granted as "$\Phi_n = N + o(TL)$", is admissible (fixed arity $n$ per family, kernel
sup $\le 1$, no $T$-dependence, $o(TL)$ absolute, countably many in one support window,
which L4's own statement allows) and jointly satisfiable (any all-simple configuration
satisfies every member exactly, with the core). Its per-event merge cost on family $n$
is $c_n = 2^n - 2 \to \infty$, so D2's slack floor degenerates:
$\varepsilon_{G^{\sharp}} = \min_n \varepsilon_n / c_n = 0$. Then (iii)'s claim "the
certifiable-against region is exactly $\{g : g \gtrsim \varepsilon_G TL\}$" reads
"every growth rate is certifiable-against", which is FALSE: configurations with
$E = 2\log^2 T \to \infty$ match $G^{\sharp}$ plus core (each fixed family sees
$\log^2 T \cdot (2^n - 2) = o(TL)$), so "$E \le \log T$ eventually" is not certifiable,
while the floor clause (i) is silently vacuous (its admissible range
$[CR, c_1 \varepsilon_G TL]$ is empty). The battery is the o-class approximation OF the
exact register (the $n \to \infty$ limit of o-grants approaches exactness non-uniformly),
which is exactly why the linear parametrization breaks there. D2's parenthetical "for
every standard battery all $c_i = O(1)$" is doing load-bearing undefined work. FIX:
make "standard battery" (finitely many granted families, $c_i = O(1)$ uniformly) a
NAMED hypothesis of Theorem 1(i)/(iii) and record $G^{\sharp}$ as the boundary case.
Fix F1.

## 4. Attack D: Theorem 2. LANDED (two constructions and one omission; the cosh cap, the band arithmetic, and the orthogonality survive)

**D.1 The "$|M| \le CTL$ derived, not assumed" claim is a false derivation; the
hypothesis is real and necessary (the document's own pre-registered surface 3,
confirmed with the construction).** Take the sup-normalized height-windowed link family
and grant the law whose main-term profile is $M^{\ast}(T) := (\text{base read}) +
2\cosh(\delta_0 \theta)$-pair-term for a fixed $\delta_0 > (1+o(1))/\Delta_G$. This is
G-LAW-syntactic (nothing in the delta-checked C2 bounds a granted MAIN TERM), and it is
jointly satisfiable with C0 plus the entire proven core: the satisfier is any
core-matching base plus one injected off-line FE pair at $(\delta_0, \gamma_0)$ (an
$O(1)$ perturbation of every core read, the (I)-move logic), and the law then holds
with error zero. For this law $|M^{\ast}| \asymp e^{\delta_0 \Theta_G} =
T^{\delta_0 \Delta_G} \gg TL$, and the exclusion engine at $\delta_0$ MUST fail over
the matching class (the satisfier contains the pair; soundness). So the document's
parenthetical derivation ("a satisfiable law's main term is within slack plus capacity
of an actual read") is wrong precisely because the actual read's configuration may
itself carry the off-line pair: the capacity bound $\le C_0 TL$ holds only for on-line
mass. $|M| \le CTL$ is a genuine NAMED HYPOTHESIS restricting the granted profile
(it excludes exactly the laws that hard-code above-frontier pairs into their main
terms, which is the right scope), and (iii)'s "the frontier's sharpness is thus
universal over the default pool" must be conditioned on it. Fix F2.

**D.2 The near-real-ordinate corner: the cos-existence parenthetical is false.** The
claim "(existing since the window's log-length exceeds the cosine's period scale)"
fails for $\gamma_0 \lesssim 1/\Theta_G$: at $\gamma_0 = \pi/(2\Theta_G)$ the phase
$\gamma_0 \log x$ over the top-of-support window $[(1-\eta)\Theta_G, \Theta_G]$ is
confined near $\pi/2$, where $|\cos| < 1/2$ throughout. Such near-real strip points are
C0-legal (the RvM frame's $S \ll \log T$ allows up to $C \log T$ of them), so (ii)'s
sharp constant as stated is unproven at that corner; recovery at $\log x \asymp
\Theta_G/2$ costs a factor 2 in the threshold for those pairs. Two clean repairs,
either sufficient: (a) declare the complex-read convention for the upper-half C0
multiset, in which case the pair's contribution has MODULUS $2\cosh(\delta\theta)\phi$
and the cos step should be deleted outright; or (b) keep real reads, scope the sharp
constant to $\gamma_0 \ge c/\Theta_G$, and price the $\le C\log T$ near-real pairs at
the degraded threshold. Fix F3.

**D.3 Theorem 2(i) omits the regime condition its merge stage consumes.** The floor's
route is merge-then-split; the merge stage at $k$ up to $c_1 \varepsilon_G TL$ needs L4
whenever the granted battery includes non-decaying families, yet (i) carries no regime
condition while Theorem 1(i) does: an internal inconsistency. Note the useful
decomposition this exposes: at $k = O(1)$, and in particular the C4-loc headline
($k = 1$: "no member certifies $N_{\mathrm{off}} \equiv 0$"), no balancing is needed on
generic bases (a single event's resonance cost $2|\Sigma| \cdot O(1) \asymp \sqrt{N}
\ll \varepsilon TL$) and only L4(i)-alignment on rigid ones, so the co-primary
endpoint is unconditional; the FULL $k$-range inherits L4's repaired regime condition.
Fix F4.

**D.4 What survives D.** The floor's cosh currency is right: the delta-check's
sup-normalization pin delivers the $\le 4$ merge cap (L2b), and the general
sup-normalized split cost is $\le C(\cosh(\delta\Theta) - 1)$ in both Phragmen-Lindelof
branches (ratio bounded at small and large $\delta\Theta$; constants absorbed into
$c_2$), so (i)'s currency and the $\delta \le (1-o(1))\log(\varepsilon_G TL/k)/\Theta_G$
display are sound. The thin-band arithmetic (iii) checks with $k$ explicit. The
endpoint reading (iv) ($\delta^{\ast} = 1 + o(1) > 1/2$ at proven-core support) checks.
The multi-pair clause's degradation $O(\log(m/\eta)/\Theta_G)$ is an honest price,
including its blow-up at exponentially clustered families (recommended, non-blocking:
note in (iii) that sharpness is a single-pair and $\eta$-separated statement; the
clustered blind spot is priced, not thin). The orthogonality (v) survives my coupling
hunt: under large granted support the mergeable-gap pool shrinks, but positioning at
$O(1)$ link cost per event (the sup cap) restores support-blindness of the Theorem 1
floor, and resonance frequencies are marginal parameters, not $\Theta_G$, so no
slack-support coupling channel appears.

## 5. Attack E: the discipline bracket. MISSED (both cells honest)

The D-H clause is honest at both arms: the class over D-H runs zero-side only (prime
and link channels empty by type refusal per #202(iv), restated at the link per the
delta-checked definition), so Theorem 2's ceiling is EMPTY over D-H and nothing in the
document quietly assumes otherwise; the floor over D-H is correctly stated over
satisfiable $G$ for its strip multiset, exactly as the F2a harness clause prescribes;
the landmark pair's invisibility is the measured extreme of the same species (#199).
The build's G1 cell measures the genuine scanned pair (Section 0 probe). Beurling: the
theorems are not statable over a Beurling system (no zero side), and the prime channel
enters the curve only as the FUNDING of $\Theta_G$, typed as L1-congruence-rich per
e1af; no step of the exclusion engine runs on a generic Beurling prime side. The
theorems themselves are configuration-space no-go/pricing statements, so D-H
insensitivity of the FLOORS is by design and correctly named; the only engine with
discriminating power (the ceiling) names its D-H refusal. No fare-dodging found.

## 6. Attack F: the derivability run (decisive for the grade)

Ledger clauses used: #148 (uniformity/determinant-class), #160 (growth), #194
(vanishing-locus funding statement), #199 (certified line-window floors; the 700x D-H
invisibility), #192 (the measured $4(\cosh(\delta u) - 1)$ envelope and the
$U^{\ast} = 1.41/\delta$ detector curve), #206 (the two-wall typing), #208 (banked GLSS
sentence), plus the F2a adversary report's own A2/A3(iv)/A4(ii) sentences (in the
ledger since #211).

| Item | Wordable from the ledger? | Grade |
|---|---|---|
| Contrapositive of the no-go ("completeness must consume exact-class contact") | YES: #148/#194/#201's wall statement verbatim | NOT MINTED by the document (label checked: HOLDS; Section 7 carries the prohibition correctly) |
| The no-go itself (Corollary) | YES: soft-true, decided at F2a (A4(ii)) | NOT MINTED (label HOLDS; endpoint-only status carried) |
| M1: sharp linear $E$/$N_{\mathrm{off}}$ exchange, two-sided | Largely: ceiling half is GS25/GLSS in print (conceded in-doc); floor half at the qualitative register is A4(ii) verbatim ("below every granted slack floor... $E$ unbounded"); the constant-matched conjunction assembles from these plus #211(iv)(a)'s own target wording | ENRICHMENT (the non-assemblable content is L4's repair, which is M4's, not M1's) |
| M2: resolution frontier $\delta^{\ast} = (1+o(1))\log(TL)/\Theta$, two-sided, thin band | NO: #192 is an instrument curve at the zeta instance, #199 a certified instance, A3(iv)'s near-line-split sentence lives at displacement $1/(\Delta L)$, a full $\log$ factor BELOW the frontier; the class-quantified two-sided form (every sound member blind below, an explicit member excludes above, under the named $|M|$ hypothesis) has quantifier structure absent from every ledger entry | **NEW-COORDINATE as scoped**, conditional on fixes F2/F3/F4 (a relabeling, a convention pin, a condition restore: no new mathematics); this is the item that lands |
| M3: orthogonality/decoupling | YES: #206's registration typed the two walls apart in nearly these words ("budgets bound HOW MANY, never WHERE"); the document itself says "derived rather than typed" | CORROBORATION (epistemic upgrade of an existing sentence; valuable, not a coordinate) |
| M4: site-selection lemma | Statement NOT wordable (the delta-check's weighted averaging is qualitative per-family $o(TL)$; A4(ii)'s bookkeeping is what L4 corrects); but the lemma is NOT PROVEN at its stated scope (findings A.1, A.2, A.3 are proof gaps, not named hypotheses) | NEW-COORDINATE CANDIDATE, **does not land this session**; the rigid-base half (exact alignment) lands as a proven sub-lemma |

Honest in both directions, as charged: the document's pre-labels (no-go and
contrapositive not-minted) HOLD; of the four candidate mints exactly one (M2) escapes
the derivability net in landable condition, one (M4) escapes as a statement but fails
the proven clause, and the other two are correctly priced by their own ancestry
paragraphs once read strictly.

## 7. Attack G: the exit-2 bar, strictly

The bar: proven modulo NAMED analytic hypotheses; finite skeleton machine-checked or at
minimum VERIFIER-drafted with the hypothesis load priced; derivability run on the
contrapositive.

**At the bar as delivered**: the L2 cost calculus (L2a-L2e, with Bernstein and
Phragmen-Lindelof named, the envelope exact); Theorem 1(ii) (clean GLSS arithmetic,
named inputs); Theorem 2(i)'s cost accounting and the $k = O(1)$ / C4-loc endpoint;
L4(i) (rigid route, exact); the register lemmas (machine-checked); the unconditional
$N^{\circledast}$ cap; the corollary correctly carried as endpoint-only with the scope
sentence verbatim; the contrapositive derivability pre-run honest.

**Short of the bar as delivered**: Theorem 1(iii) at full generality (FALSE at the
admissible battery $G^{\sharp}$: fix F1 names the missing hypothesis); Theorem 2(ii)'s
$|M|$ clause (claimed derived; it is a necessary named hypothesis: F2) and its
near-real corner (F3); Theorem 2(i)'s missing regime condition (F4); L4's generic route
(proof gaps A.1/A.2: repairs, not relabelings; this is why M4 does not land); L5's
display (false as stated, conclusion salvageable: F6); and the Lean artifact's two
sorry-bodied statements, BOTH refutable as typed:

- **V-F2b-6 is false as typed**: `hderiv : ∀ t, HasDerivAt (deriv g) (g'' t) t` never
  asserts $g$ is differentiable. Take $g = $ indicator of $\{0\}$: `deriv g` is the
  junk constant $0$, so the hypotheses hold with $g'' \equiv 0$, $B = 0$, yet
  $|g(x{+}a) + g(x{-}a) - 2g(x)| = 2$ at $x = 0$, $a = 1$. The sorry is undischargeable.
  Fix F7.
- **V-F2b-7 is false as typed**: `hdisc : True` carries nothing and no on-line-mass or
  move-structure hypothesis appears. Instantiate `Config := Unit`,
  `profile _ := 0`, `reads := []`, `slack := 16`, `g := 2`: `Invisible` is vacuous,
  `excess = 0 < 2`. A drafted formalization TARGET that is refutable fails the
  drafting's purpose. Fix F8.
- Statement drift: `domination` proves `defectMass ≤ excess` (total zero mass on
  defective lines), which is NOT the profile form of $N_{\mathrm{off}} + N_{\mathrm{mult}}
  \le E$: an $h = 4$ line of two off-line doubles contributes $8 = 2h$ to the sum
  register versus $4 = h$ to `defectMass`; the sum form needs the FE corner argument
  (delta-check Section 4) that lives outside the h-profile model. The per-register
  bounds $N_{\mathrm{off}} \le E$ and $N_{\mathrm{mult}} \le E$ do follow, and nothing
  downstream uses more, but the docstring and Section 9 must say which statement is
  proved. Similarly `conversion` proves $\#\{h = 1 \text{ lines}\} \ge 2N -
  N^{\circledast}$; the "simple critical" reading rides on the unformalized extraction
  (the in-file caveat exists; Section 9 should mirror it). Fix F9.

**The honest classification, per the mandate's (a)-vs-(b) fork**: **(a) as scoped.**
The visibility-floor law lands as a theorem-shape at the Section 5 bar AT ITS NARROWED
SCOPE: finite uniformly-priced batteries (F1); link laws with the named $|M| \le CTL$
main-term hypothesis (F2); the read convention pinned or the near-real corner priced
(F3); Theorem 2(i) under the regime condition with its unconditional $k = O(1)$
endpoint (F4); the L4-generic extension carried as a repaired-regime-condition claim
with its two proof obligations named (F5), or the floor scoped to batteries where L2a
covers the marginal side. This is NOT the (b) outcome: the two-sided frontier and the
scoped linear exchange have content strictly beyond the scope-honesty corollary, which
the document itself correctly refuses to mint. Exit 2 therefore does not fire, PROVIDED
the blocking fixes land in the session's bounded fix pass (the F2a re-pose precedent:
synthesizer applies the adversary's list in place, no new session, no 3a event). If the
fixes do NOT land, the honest record is "theorem-shape at the bar only at narrowed
scope with unapplied repairs", and the audit should read that as exit 2 firing with
the #211(iv)(b) sentence.

## 8. Required fixes (blocking F1-F10; the builder applies, this report edits nothing)

1. **F1 (Theorem 1(i)/(iii) + D2).** Add the named hypothesis: the grant battery is
   STANDARD (finitely many granted families, per-event costs $c_i = O(1)$ uniformly);
   record $G^{\sharp} = \{\sum_{\mathrm{lines}} h^n = N + o(TL) : n \ge 2\}$ as the
   admissible boundary case where $\varepsilon_G = 0$, (i) is vacuous, and (iii) is
   false as posed. D2's "for every standard battery" parenthetical becomes the
   hypothesis, not a reassurance.
2. **F2 (Theorem 2(ii)).** OLD: "(Section 2 of the adversary report's A4 wording;
   derived, not assumed, since a satisfiable law's main term is within slack plus
   capacity of an actual read)". NEW: name $|M| \le C\,TL$ as a hypothesis on the
   granted profile; record the wild-$M$ construction (a satisfiable link law whose main
   term encodes an off-line pair at $\delta_0$ has $|M| \asymp e^{\delta_0 \Theta_G}
   \gg TL$, and exclusion at $\delta_0$ is unsound over its matching class); condition
   (iii)'s "universal over the default pool" sentence on the hypothesis.
3. **F3 (Theorem 2(ii) corner).** Pin the read convention: either complex reads
   (delete the cos step; the pair contributes modulus $2\cosh(\delta\theta)\phi$) or
   real reads with the sharp constant scoped to $\gamma_0 \ge c/\Theta_G$ and the
   $\le C \log T$ near-real pairs priced at the factor-2-degraded threshold. Delete the
   false parenthetical "(existing since the window's log-length exceeds the cosine's
   period scale)".
4. **F4 (Theorem 2(i)).** Add "under L4's regime condition" to the floor; state the
   unconditional sub-case: at $k = O(1)$ (in particular the C4-loc $k = 1$ endpoint)
   no balancing is needed on generic bases and only L4(i)-alignment on rigid ones.
5. **F5 (L4).** (a) Replace "keeps every partial sum $\le \max_e |v_e|$
   (Steinitz-type)" by a batch-selection bound $\le C(R)\max_e|v_e|$ and fold $C(R)$
   into the regime condition's $\bar v$. (b) Cover repulsion-law batteries: the
   selection runs over TOTAL position-plus-merge cost vectors $v_e = 2e^{ium_e} -
   e^{iu\gamma_1} - e^{iu\gamma_2}$ with mover-chosen midpoints (as the build's
   `select_sites` already computes), with the free-phase balancing stated and proved
   or priced. (c) Note that the build's gates probe benign phase pools only.
6. **F6 (L5).** Replace the display's $N^{\circledast}$ by the unit-resolution pair
   count $N^{\circledast} + N(T, O(1))$ (core-capped at $C\,TL$ by the same Fujii
   argument), or add the min-spacing hypothesis MV actually needs; record the
   clustered-lines counterexample ($h \equiv 1$ clusters at spacing $2^{-T}$:
   $\int_W |\Sigma|^2 \asymp |W| m N \gg |W| N^{\circledast}$). $R(T)$'s bound is
   unchanged.
7. **F7 (Lean V-F2b-6).** Carry the first derivative explicitly:
   `(g' : ℝ → ℝ) (hg' : ∀ t, HasDerivAt g (g' t) t) (hg'' : ∀ t, HasDerivAt g' (g'' t) t)`,
   replacing `deriv g`; as typed the statement is refuted by $g = $ indicator of
   $\{0\}$ with $B = 0$.
8. **F8 (Lean V-F2b-7).** Type the load so the target is not false: an opaque
   discipline structure (moves, cost bounds, regime condition) plus an on-line-mass
   hypothesis, replacing `hdisc : True`; as typed the statement is refuted at
   `Config := Unit`, `reads := []`.
9. **F9 (Lean/doc drift).** Fix the `domination` docstring and Section 9's wording to
   the statement proved (defective-line mass $\le E$; per-register domination follows;
   the sum register's FE corner is extraction-side); mirror the `conversion`
   extraction caveat in Section 9.
10. **F10 (dossier).** $N = 14657 \to N = 14659$, both occurrences (Sections 1 and 4).

Recommended, non-blocking: the clustered-pair sharpness note in Theorem 2(iii); the G1
found-vs-inserted log line; the line-97 linter nit.

## 9. Verdict block

- **Verdict: PASS_WITH_FIXES.** The core curve survives attack: the cost calculus is
  exact where claimed, both ceilings are correctly derived at their honest scopes, both
  floors stand at the repaired quantifiers, the discipline bracket is honest, the build
  reproduces bit-for-bit at seed 212, and the pre-labeled non-mints are honestly
  labeled. The failures are at quantifier edges and packaging: one false sharpness
  claim at an admissible battery, one false derivation claim hiding a necessary named
  hypothesis, one false existence parenthetical, one missing regime condition, two
  proof gaps in L4's generic route, one false lemma display, two refutable Lean
  statements, and three drift items.
- **Grade: non-UNMOVED**, carried by M2 alone (the two-sided resolution frontier
  $\delta^{\ast} = (1+o(1))\log(TL)/\Theta_G$ at the class register: lands at the bar
  modulo fixes F2/F3/F4/F7/F8, which are relabelings, a convention pin, a restored
  condition, and two statement repairs, none new mathematics; passes the derivability
  run in Section 6). M4 does not land (proof obligations F5/F6 outstanding); M1
  ENRICHMENT; M3 CORROBORATION. Conditionality stated plainly: if the blocking fix
  pass does not execute in-session, the grade reverts to UNMOVED and exit 2 fires per
  Section 7's last sentence.
- **Exit-2 assessment**: exit 2 does not fire: the visibility-floor law lands as a
  theorem-shape at the Section 5 bar at its narrowed scope (standard batteries; named
  $|M| \le CTL$; regime-conditioned floors with the unconditional $k = O(1)$ C4-loc
  endpoint), which is outcome (a) as scoped and not the #211(iv)(b) relabeling case,
  since the frontier and the scoped exchange carry content strictly beyond the
  scope-honesty corollary the document already refuses to mint.
- **Tripwire arithmetic**: entering count 1/3 post-#209-reset; on the non-UNMOVED
  grade the consecutive-UNMOVED counter RESETS to 0/3 (on a no-reset reading of the
  wiring it holds at 1/3; on neither reading does it advance). Frame sessions used:
  4/6. If the conditional grade reverts (fixes unapplied), the count becomes 2/3 and
  exit 2 fires simultaneously, which the audit should record together.
