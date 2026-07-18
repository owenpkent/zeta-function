# ADVERSARY report: e2al SP3c/W6 ghost/THH rung

> ADVERSARY attack on `experiments/arithmetic_geometric/e2al_sp3c_ghost_thh_rung.py`
> / `.md`, 2026-07-17. Target: the B1 rung 5 probe (the C1 counting joint,
> derived-base half; spec `docs/03_research/c1_joint_build_spec.md`). This is
> the first ADVERSARY round on the e2ai/e2aj/e2ak/e2al family (no prior
> `_e2a*_adversary.md` exists). Grading precedent: `e1l_absorption_count.py`
> (W6-shaped vs. installed), `e1p_rank_one_interlacing.md` (measured profile
> vs. theorem instance; `PASS_WITH_FIXES` format followed here). All
> synthetic checks were RUN, not reasoned in the abstract; scratch scripts
> lived in the session scratchpad (not the repo) and any scratch copies
> placed inside `experiments/arithmetic_geometric/` for module-import reasons
> were deleted immediately after use.

## (a) One-paragraph verdict

e2al **holds up on every load-bearing numerical claim** (Phase 0's exact
reproduction, Phase 1's Gap-A wall, Phase 2's multiplicativity wall), but the
BUILDER's deviation 3 (a source-inspection proof standing in for the spec's
literal Beurling rebuild) turned out to be an **incomplete**, not a wrong,
argument: the "overflow excuse" for skipping a literal rebuild is true for
the naive array-permutation construction but false for the construction the
spec actually names (`BeurlingSystem.gen_integers`'s exponent-vector
representation, which has no array bound). Building and running that literal
rebuild (new Checks P1.12/P1.13, ADVERSARY-added) **confirms** the rank/
position sub-layer's Beurling-blindness literally, and **additionally finds**
a genuine, previously unmeasured result: the domain-*counting* sub-layer
(`tr(V_kF_k)`) IS Beurling-sensitive, which corrects an overreach in the
original P1.9/old-P1.12 wording ("every native invariant... Beurling-
identical") without overturning the module's headline finding (Gap A's
eigenvalue claim is still shown blind, now more rigorously). The Phase 2
strawman check independently confirms the multiplicativity wall is not an
artifact of the one construction tested: a 7-variant sweep (new Check P2.7)
finds every natural composition of necklace weight + Bökstedt order fails at
the same first pair. A real, unrelated defect was found and fixed: 24 em
dashes in the companion `.md` (a hard CLAUDE.md style violation; the `.py`
was already clean), and a stale internal claim ("the highest LEARNINGS entry
is #164") that a direct search shows is wrong (#165 is already taken by the
same-day e1p retirement; the correct next number is #166, confirmed, not
"TBD"). Three checks were spot-verified falsifiable by deliberately
corrupting the underlying computation in a scratch copy and confirming each
failure is correctly detected. Verdict: **PASS_WITH_FIXES**.

## (b) Reproduction

| run | expected | observed |
|---|---|---|
| baseline (pre-fix, `python -m experiments.arithmetic_geometric.e2al_sp3c_ghost_thh_rung`) | 24/24 | **24/24 passed, 25.5s** (cold run; a later re-run of the unmodified code showed 8-9s, consistent with the `.md`'s original "~9s" claim; the variance is import/first-run overhead, not a correctness issue) |
| post-fix (all ADVERSARY checks added) | 27/27 | **27/27 passed, 8.2-8.4s** across three re-runs |

24/24 reproduced exactly before any change was made, matching the task
brief's expectation precisely.

## (c) Attack axes

### Axis 1 -- Phase 1's structural proof (deviation 3). VERDICT: HOLDS, WITH A GENUINE ADDITION

**Prong (a), faithfulness.** `e2al` does not reimplement `apply_F`/`apply_V`;
it imports them directly from `e2ai_base_battery.py`
(`from experiments.arithmetic_geometric.e2ai_base_battery import (apply_F,
apply_V, basis, divisors, factorize, lambda_vec, logvec, mobius, vadd)`).
This resolves the "diff the semantics" concern by construction: Check P1.9's
`inspect.getsource(apply_F)` inspects the actual, shared e2ai functions, not
a local copy that could have drifted. Independently re-derived the
underlying math (not merely trusted the import): the ghost-lattice model
`(F_k w)_n = w_{kn}`, `(V_k w)_n = k w_{n/k}` (if `k|n`) is the standard
Witt-vector Frobenius/Verschiebung action on ghost components (Hesselholt's
convention), and by direct computation `F_k V_k = k\cdot\mathrm{Id}`
(`(F_kV_k w)_n = (V_kw)_{kn} = k w_{kn/k} = kw_n`, since `k | kn` always) and
`\mathrm{tr}(F_k)=0` for `k\ge2` (a basis vector `e_n` maps to `e_{n/k}`,
whose coefficient at position `n` is nonzero only if `n/k=n`, impossible for
`k\ge2`), matching Checks B3.Q2/B3.Q4 in `e2ai` and P1.1 here exactly. PASS.

**Prong (b), the overflow excuse.** This is where the real content is. The
`.md`'s Section 5 (before this round) argued a literal Beurling rebuild was
infeasible because a *permutation*-based relabeling inside the fixed
`N=720` array overflows for composite `k` (verified true: swapping which
literal integer plays "prime 2" vs "prime 3" sends `2^7=128` to
`3^7=2187>720`). But re-reading the spec's own Section (b) text: "rebuild
the *entire* battery with the index set relabeled by a `BeurlingSystem`
generator list... using `BeurlingSystem.gen_integers(x,
with_factorization=True)` for the exponent-vector data exactly as e2ak's C4
check already does" -- this is not the permutation construction. Since
`F_aF_b=F_{ab}` (verified directly: `(F_aF_bw)_n=(F_bw)_{an}=w_{ban}=
(F_{ab}w)_n`), every `F_k`/`V_k` for `k=2..12` decomposes into shifts along
`k`'s own prime factors, so the entire layer is re-expressible as pure
**exponent-vector arithmetic** (add/subtract `k`'s own factorization from an
index's exponent vector), which has no array bound at all: the domain is
just "which exponent vectors have value `<=X`", exactly what `gen_integers`
already returns. This is buildable, and per the task brief's instruction it
was built and run (first in a scratchpad script, then folded into the module
as Checks P1.12/P1.13; see (d) below). **Result: MIXED, and informative
either way**, exactly the outcome the task anticipated:
- The rank/position sub-layer (`tr(F_k)=0`, N_op's eigenvalue on a basis
  vector) is **confirmed identical** between a 720-element rational domain
  and a 1134-element `gen_integers`-derived Beurling domain (same bound
  `X=720`): eigenvalues `2, 3, 27, 11` on the "prime 2", "prime 3", "n=12
  shape", "n=6 shape" patterns match exactly in both domains. This
  **upgrades** the structural claim from source-inspection-only to a literal
  test, closing the honest-limitations gap for this sub-layer. Per the task
  brief: **upgrade applied**, marked `[ADVERSARY, literal test added]`.
- The domain-*counting* sub-layer (`tr(V_kF_k) = k\cdot\#\{n\le
  \text{bound}: k|n\}`) is **sharply different** between the two domains:
  e.g. `k=2` gives `720` (rational) vs. `1402` (Beurling); `k=8` gives `720`
  vs. `2120`. This is because the rational and Beurling domains have
  different SHAPES under a size bound (1134 vs. 720 elements at the same
  `X=720`, a direct, stark illustration of e2ak's own C5a finding that
  Beurling integer counting is not `x+O(1)`), and `tr(V_kF_k)` sums over the
  *entire* domain rather than following one element down (division only
  ever shrinks, so it never leaves a downward-closed domain, which is why
  the rank sub-layer is immune but the counting sub-layer is not). **This
  is a genuine catch**: the original P1.9/old-P1.12 wording ("the F_k/V_k
  trace... layer cannot see a Beurling relabeling by construction", "every
  native... invariant tested is Beurling-identical") over-generalizes from
  "apply_F/apply_V's own source never references size" (true, and the only
  thing P1.9's source-inspection actually tests) to "the whole trace layer
  is blind" (false for this specific counting quantity). Per the task
  brief's instruction ("if it does not confirm the structural claim, that
  is a major catch, report FAIL on that check"): **this is reported as a
  catch on the ORIGINAL P1.9/P1.12 wording specifically**, not on the
  module's headline Gap-A finding, which survives and is strengthened. Both
  the wording and the check numbering were fixed in place (see (d)).

**Prong (c), the positive control.** P1.8 already demonstrates an
externally-appended `w()` readout differs under relabeling. The new P1.13
finding is a *stronger* positive control than P1.8: it shows an **internal**
battery quantity (not an artificially appended one) changes, which
independently answers "is the sweep's machinery capable of detecting a
difference when there is one" even more convincingly than the original
design, since it is not an outside-the-battery readout.

### Axis 2 -- Phase 2 strawman check. VERDICT: HOLDS, STRENGTHENED

**(a) No tuning-to-fail.** Read `f_tc`'s construction: `f_TC(n) =
sum_{d|n} mu(n/d) * d * M(q0,d)`, a direct Möbius-inversion analogue of B4's
own mechanism (`Lambda_hat(n) = sum_{d|n} mu(n/d)*logvec(d)`), substituting
the necklace weight `M(q0,d)` in place of B4's bare weight, exactly the
spec's Section (a).2 instruction ("necklace weights composed with the
Bökstedt torsion order"). No `Lambda`/zeta-fitted parameter appears anywhere
(confirmed by K1 Checks P2.5/P2.6, both re-verified clean in this round).

**(b) Reproduced the failing arithmetic exactly.** `q0=2`: `f_TC(2)=0,
f_TC(3)=4, f_TC(6)=48 != f_TC(2)*f_TC(3)=0`. `q0=3`: `f_TC(2)=3, f_TC(3)=21,
f_TC(6)=669 != f_TC(2)*f_TC(3)=63`. Both match the module's own printed
output exactly, independently re-derived in a scratch script before touching
the module.

**(c) Enumerated other natural compositions.** Swept six other natural
variants of the same two ingredients (necklace-only Möbius sum; raw
`M(q,n)` with no composition; a Möbius **product** form
`prod_{d|n}(d*M(q,d))^{mu(n/d)}`, the Euler-product-native inversion as
opposed to the additive sum the builder used; the same product form on the
necklace weight alone; a sign-alternating `(-1)^d` variant; and a
log-composed variant matching B4's actual `log|torsion|` shape). **All six,
plus the builder's own, fail, and all fail at the identical first pair
`(2,3)`.** Five of the six (the exact-`Fraction`-arithmetic ones, matching
this module's convention) were folded into the module as a new tracked
Check P2.7 (10 variant/alphabet combinations); the sixth (log-composed, uses
floats) was verified informally and reported in the `.md` but not tracked
as a formal check, since it falls outside this module's exact-arithmetic
discipline. No variant was found multiplicative; had one been, this would
have been reported prominently as a discovery, per the task brief's explicit
instruction, not buried.

### Axis 3 -- Phase 0 grading. VERDICT: HOLDS, no fix needed

The "exact-by-construction (`c_p=p`)" honesty is **already** in the STATUS
banner's Result column ("PASS, exactly, by construction"), not buried; it is
also restated in Section 1's "Verdict" paragraph and the module's own
printed "PHASE 0 HONESTY SUMMARY" block. No fix needed on this point.
Reproduced the P0.5 computation independently: gaps
`log(n+1)-log(n)` for `n=1..5` are `0.693, 0.405, 0.288, 0.223, 0.182`, max
minus min `= 0.511`, matching the check's own reported `0.51` (and the
`.md`'s `gap spread 0.51`) exactly. The TP-periodicization/negative-level
caveat (P0.6) is genuinely **cited**, not asserted: Direction 10B's own text
states "Its Tate construction TP(Z)... is 2-periodic... (Nikolaus-Scholze;
this is the homotopy-theoretic source of the... 2-step structure)" and lists
Nikolaus-Scholze (2018), *On topological cyclic homology*, Acta Math.
221(2), in its References section, confirmed by direct read of
`10B_thh_weight_and_mobius.md`. No fix needed.

### Axis 4 -- standard battery. VERDICT: TWO CATCHES, BOTH FIXED

- **K1 guard**: present and tested (P2.5 static scan, P2.6 runtime
  call-count guard). Re-verified by direct `rg` search of the final module:
  the only matches for `mp.zetazero|ZETA_ZEROS|davenport_heilbronn` are the
  discipline-note prose and the forbidden-token list definition itself, no
  actual zero-list access anywhere. HOLDS.
- **Discipline wording**: matches the e1l/e1p tier vocabulary
  ("installed"/"computed", "blind", "measured profile... NOT graded a
  theorem instance") verified by direct comparison against
  `e1l_absorption_count.py` and `e1p_rank_one_interlacing.py`'s own printed
  VERDICT blocks; the spec's own Section (d) explicitly instructs reading
  the tier vocabulary off this exact precedent, and it does. HOLDS.
- **Em dashes**: **CATCH.** The `.py` was already clean (0 occurrences,
  confirmed by direct character-code scan for U+2014). The `.md` had **24**
  em dashes, a hard violation of CLAUDE.md's "no em dashes anywhere...
  don't use them at all, anywhere, ever" rule. **Fixed**: all 24 replaced
  with periods, colons, or commas depending on context, re-verified at 0
  after the fix.
- **The 24 (now 27) checks are genuine.** Spot-verified by deliberately
  corrupting three pieces of underlying logic in a scratch copy (deleted
  after use) and confirming each corruption is caught: (1) flipping the
  divisibility test in `nop_eig_closed` (`n%k==0` to `n%k==1`) trips a
  load-bearing internal `assert` before even reaching Check P1.4 ("N_op
  closed form disagrees with direct F_k/V_k composition"), showing this
  invariant is cross-validated twice, not just check()-gated; (2) offsetting
  the pole location by 0.1 in the Phase 0 Euler-factor formula correctly
  flips Check P0.4 to `[FAIL]`; (3) corrupting the hand-expansion coefficient
  in the P2.1 sanity check (`7` to `8`) correctly flips P2.1 to `[FAIL]` and
  drops the total to 25/26 (pre-P2.7). All three corruptions were caught;
  none was silently absorbed. HOLDS.

### Axis 5 -- LEARNINGS numbering. VERDICT: CATCH, CORRECTED (not applied to LEARNINGS.md itself)

The `.md`'s original Section 6 claimed "the highest entry number directly
confirmed present in `LEARNINGS.md` at time of writing is #164," flagging
#165 as possibly taken but unresolved. Direct search
(`rg "### 165\." experiments/LEARNINGS.md`) finds `### 165. THE #154 LEDGER
RETIRED: rank-one interlacing... (e1p, 2026-07-17)` present in the file:
**#165 is taken.** The correct next number is definitively **#166**, not
"#165 or #166, TBD by SYNTHESIZER." Fixed in the `.md`'s own proposal text
only (per the task brief, `LEARNINGS.md` itself is left untouched here; the
SYNTHESIZER pass consumes the corrected `#166` label directly).

## (d) Fixes applied

All marked `[ADVERSARY, ...]` in place, in
`e2al_sp3c_ghost_thh_rung.py`/`.md`:

1. **`.py`**: added Check **P1.12** (literal exponent-vector Beurling
   rebuild confirming the rank sub-layer's blindness; 1134-element Beurling
   domain vs. 720-element rational domain, same bound) and Check **P1.13**
   (the same rebuild showing the domain-counting sub-layer, `tr(V_kF_k)`, IS
   Beurling-sensitive at every `k=2..12`).
2. **`.py`**: renumbered the original aggregate `P1.12 WALL` check to
   **P1.14**, narrowing its claim and detail text to the rank sub-layer
   specifically (was an unscoped "every native invariant" claim).
3. **`.py`**: corrected Check **P1.9**'s description to state precisely what
   the source-inspection proves (no per-element operator can see a
   relabeling) and explicitly flag what it does not cover (domain-wide
   aggregates), cross-referencing P1.12/P1.13.
4. **`.py`**: added Check **P2.7** (the 5-variant exact-arithmetic strawman
   sweep, 10 variant/alphabet combinations, all failing at `(2,3)`).
5. **`.py`**: updated the module docstring's Phase 1 paragraph and the
   terminal `VERDICT` print block to reflect the rank-vs-counting scope
   correction.
6. **`.md`**: rewrote Section 2 (Phase 1) to document P1.12/P1.13, the
   resolved overflow-excuse limitation, and the corrected scope of the
   Beurling-blindness claim.
7. **`.md`**: rewrote Section 3 (Phase 2) to document Check P2.7 and the
   seven-variant strawman finding.
8. **`.md`**: corrected Section 6's stale LEARNINGS-numbering claim
   (`#164`/`"#165 or #166, TBD"` to the confirmed `#166`), and updated the
   proposed LEARNINGS entry text to fold in the ADVERSARY findings.
9. **`.md`**: updated Sections 4-5 (Disciplines, Honest limitations) and the
   Deviations section for the new check/line counts (27 checks, 869 lines)
   and to mark the overflow-excuse limitation `[RESOLVED, ADVERSARY]`.
10. **`.md`**: replaced all 24 em dashes with periods, colons, or commas.
11. **`.md`**: added a Pointers entry and a `.md`-header reference to this
    adversary record.

No claim was softened and nothing was upgraded past its evidence: every fix
either makes an honestly-true claim more completely justified (the literal
Beurling test), corrects an over-generalization back to what was actually
proven (P1.9/P1.14's scope), fixes a stale internal fact (the LEARNINGS
number), strengthens a finding with independent replication (the Phase 2
sweep), or is a pure style fix (em dashes) with no effect on any claim.

## (e) Post-fix re-verification

Re-ran the full module after all `.py` changes:

```
27/27 checks passed
runtime: 8.2-8.4s (three consecutive re-runs)
```

All new checks (P1.12, P1.13, P2.7) PASS as predicted. All 24 original
checks continue to PASS unchanged. Confirmed 0 em dashes remain in either
file (character-code scan). Confirmed no stray scratch files were left in
`experiments/arithmetic_geometric/` after the spot-check corruption tests
(`git status --short` shows only the two legitimately new, untracked
target files).

## Verdict: PASS_WITH_FIXES

Headline numbers, post-fix: **27/27** (was 24/24; +3 ADVERSARY-added
checks: P1.12, P1.13, P2.7). Every load-bearing numerical claim in the
original module reproduced exactly and holds up under independent,
from-scratch re-derivation (the Witt/ghost-lattice identities, the Phase 2
failing arithmetic at both `q0` values, the P0.5 gap-spread computation).
The one substantive finding this round adds is genuinely two-sided: it
*upgrades* the module's central claim (Gap A's blindness, now literally
tested on an actual Beurling domain, not only source-inspected) while
*correcting* an over-generalization in how that claim was worded
(domain-counting quantities are Beurling-sensitive, which the original
P1.9/P1.12 text did not distinguish from the rank/position quantities that
are genuinely blind). This is exactly the kind of result the task's own
framing anticipated ("if it does not confirm the structural claim, that is
a major catch"): here the LOAD-BEARING sub-claim (Gap A's own eigenvalue
statement, P1.4/P1.5) is confirmed and strengthened, while a narrower,
over-broad supporting claim (P1.9/P1.12's blanket wording) is the one that
needed correcting, not reversing. The Phase 2 wall is now demonstrated
robust across seven natural variants, not resting on one construction. Two
independent, unrelated defects (24 em dashes; a stale LEARNINGS-numbering
claim) were caught and fixed. The Phase 1 tier after this round's prong-(b)
result: **still blind (tier 3, per spec Section (d).3), on the rank/
position sub-layer specifically, now literally confirmed rather than only
source-inspected**; the domain-counting sub-layer is tier 2 (measured/
installed), consistent with its pre-existing P1.6 diagnosis and newly shown
Beurling-sensitive for the same underlying reason. The provisional LEARNINGS
entry number in the dossier's Section 6 is corrected to **#166** (not
"#165 or #166, TBD"); `LEARNINGS.md` itself was not edited, per the task
brief, and remains a SYNTHESIZER-pass action item.
