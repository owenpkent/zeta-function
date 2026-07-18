# ADVERSARY report: e1q theta/Poisson wrap-collapse rung

> ADVERSARY attack on `experiments/spectral/e1q_s4_theta_wrap_rung.py` /
> `.md` / `.npz`, 2026-07-17. Target: the form-side S4 probe (the theta/
> Poisson wrap-collapse kernel; spec
> [`docs/03_research/theta_s4_build_spec.md`](../../docs/03_research/theta_s4_build_spec.md)).
> This is the first ADVERSARY round on e1q. Precedents: e1o's rank/
> cost-ratio instrument conventions (`e1o_s4_carrier.py`/`.md`, the
> "min sv" discipline and the near-commensurate-decimation mirage it
> caught once already), and grading style from
> [`_e1p_adversary.md`](_e1p_adversary.md) and
> [`_e2al_adversary.md`](../arithmetic_geometric/_e2al_adversary.md)
> (`PASS_WITH_FIXES` format, tiered attack axes, followed here). All
> synthetic/exploratory checks were RUN, not reasoned in the abstract;
> scratch scripts and scratch copies of the module lived in the session
> scratchpad (outside the repo) and were not committed.

## (a) One-paragraph verdict

e1q **holds up on every load-bearing numerical claim** (Phase 0's identity,
Phase 1's wall, Phase 2's twin/D-H/K1 disciplines), and the sharpest
attack (small-M triviality) **strengthens the result rather than
threatening it**: extending the collapse test to M ~ 100+ (an order of
magnitude past the original grid's M=11 ceiling) reproduces the identical
wall, with the raw fluctuation shrinking monotonically as M grows and, at
M >= 44, not even reaching the spec's own 0.1 magnitude bar at all. Three
real, previously-unverified gaps were found and closed: (1) the twin
Beurling system's own larger raw fluctuation (0.231) was asserted to be
"generic SVD-tail noise" but never actually checked against the same
`sig_r`/`sig_r1` conditioning gate zeta's cells are held to (now computed
and confirmed: max `sig_r` among the twin's raw-gap cells is 1.1e-05, three
orders of magnitude below the bar); (2) the K1 source-scanner's exemption
check was a bare substring test that an injection test showed is gameable
by a comment merely *discussing* the marker without granting it (the
runtime guard caught the same injection regardless, so K1 was never
actually violated, but the static scan is now hardened); (3) a
periodization invariant (the wrap-free control is never less full-rank
than the wrapped kernel) was implicit in every printed table but never
asserted as a check, so a scratch-copy corruption that swapped `G`/`G0`'s
return order silently passed every existing self-test -- now closed with a
dedicated guard at all four tested systems (zeta original, zeta extended,
Beurling twin, Beurling twin extended). One documentation-precision defect
was found and fixed: the `.md`'s claim that the three flagged mirage cells
show "smooth monotone decay, no clean gap anywhere" was demonstrated (only
for the one cell actually shown) and silently generalized to all three; a
direct ratio audit finds a real, sharp ratio-sense step at the
declared-rank boundary in *all three* cells, and the correct, precise
reason they are still mirages is the absolute scale of `sig_r` (still
three to six orders of magnitude below 1e-3), not the local shape of the
decay -- a correction that makes the module's own design (gating on
absolute scale, not shape) look better justified, not worse. Two numeric
slips were caught and fixed: a hand-derived exponent estimate
("`n=81` gives `~1e-2800`") was off by about 6150 orders of magnitude from
the true value (`~2e-8952`, independently verified), and Phase 0's quoted
"~1e-36" defect was clarified as the `dps=35` working-precision rounding
floor, not the identity's true mathematical tightness (which the
Nwrap=Kwrap=80 truncation bounds far tighter). None of these fixes change
any check's pass/fail status or the module's tier-3 (MIRAGE) verdict; they
make already-true claims more completely verified, or correct claims that
were stated more broadly than what had actually been shown. Verdict:
**PASS_WITH_FIXES**.

## (b) Reproduction

| run | expected | observed (before any ADVERSARY change) |
|---|---|---|
| full (`python -m experiments.spectral.e1q_s4_theta_wrap_rung`) | 16/16, ~0.1s | **16/16 passed, 0.1s** |
| quick (`--quick`) | 14/14 | **14/14 passed, 0.0s** |
| `.npz` untouched by quick | mtime/size/content unchanged | size **4042 bytes**, mtime and full SHA-256 hash **identical** before and after a `--quick` run (filesystem-verified, not just the printed message) |

Both runs printed all `[PASS]` lines with no `[FAIL]`s, exactly matching
the task brief's expected headline numbers before any change was made.

| run, post-ADVERSARY | observed |
|---|---|
| full | **25/25 passed**, 1.5-1.6s across three consecutive re-runs |
| quick | **23/23 passed**, 0.0s |
| `.npz` untouched by quick, post-fix | size **7279 bytes**, mtime and SHA-256 hash identical before/after `--quick` (re-verified at the filesystem level after every round of `.py` edits) |

The +9 checks (16->25 full, 14->23 quick; the same +2 quick/full gap as
before, entirely from Phase 0's per-lambda count, confirmed by a full
check-name diff between the two runs) are: `P1a2`, `P1e`, `P1e2`, `P1f`,
`P1g`, `P2a2`, `P2a3`, `P2h`, `P2h2`. Every check name present in quick
mode is byte-identical to one present in full mode (no quick-only check,
no quick-only threshold), matching the e1p Axis-7 parity discipline this
round re-applied to the new checks as well as the old ones.

## (c) Attack axes

### Attack 1 -- small-M triviality. VERDICT: HOLDS, HARDENS (the sharpest attack, and the wall survives it)

The task's own framing was correct: at the spec's grid, M(lambda) =
pi(lambda^2) tops out at 11 (lambda=6), and one rank unit there is
Delta_rho = 1/11 = 0.091, right at the 0.1 discovery threshold -- an
11x11 verdict is statistically thin. Re-ran the IDENTICAL Phase 1 +
conditioning battery (imported the module's own `node_set_zeta`,
`gram_matrices`, `numeric_rank`, `is_discovery_candidate`, `t_grid_for` --
no reimplementation) at lambda in {10, 14, 20, 30}, giving M = 25, 44, 78,
154 (pi(100)=25, pi(196)=44, pi(400)=78, pi(900)=154; the task's estimates
of 46/114 were rough, the true pi(lambda^2) values are what was tested).
Pure-compute cost for all four extra lambdas (zeta + Beurling twin, 9 t
points each): ~1.5s, still comfortably fast, so all four were folded into
the tracked module rather than stopping at the two the task named as
mandatory.

**Result: the wall not only holds, it hardens.**

| lambda | M | max raw Delta_rho (any cell) | sig_r at that cell | crosses the 0.1 raw-gap bar? |
|---|---|---|---|---|
| 6.0 (original grid) | 11 | 0.182 | 9.9e-06 | yes (2 cells) |
| 10 | 25 | 0.120 | 2.3e-06 | yes (1 cell) |
| 14 | 44 | 0.068 | 1.9e-06 | **no** |
| 20 | 78 | 0.038 | 1.7e-06 | **no** |
| 30 | 154 | 0.020 | 1.3e-06 | **no** |

The maximum raw fluctuation shrinks monotonically as M grows and never
exceeds the original grid's own 0.182 ceiling; at M >= 44 it does not even
reach the spec's own 0.1 magnitude bar, let alone the conditioning gate on
top of it. No cell at any tested M clears the conditioning gate (`sig_r`
stays at the 1e-6 to 1e-7 noise-floor scale throughout, itself trending
down, never approaching the 1e-3 requirement). This is the single most
decisive finding of the round: the tier-3 verdict does not rest on
small-sample statistics. Folded into the module as new Checks `P1e`
("small-M triviality closed... no cell reaches the S4 discovery bar"),
`P1f` (the hardening-trend check, with a quick/full parity subtlety fixed
below), and `P1e2` (the periodization invariant at the extended grid); the
matching Beurling-twin extension is `P2h`/`P2h2`. Reported prominently in
both `.py` and `.md`, per the task's own instruction for either outcome
(a genuine conditioned gap at larger M would have been a MAJOR catch; none
appeared, so the wall's robustness is the reportable result instead).

**A bug in my own new check, found and fixed during this attack.** The
first version of `P1f` compared the extended grid's max Delta_rho against
`max(c["drho"] for c in zeta_cells)` unconditionally. Under `--quick`,
`zeta_cells` only covers lambda in {2.2, 3.0} (Phase 1's own quick-mode
grid), which never reaches lambda=6 where the original grid's actual gaps
live, so `orig_max` was a vacuous 0.0 and the comparison spuriously FAILED
(`extended max 0.1200 <= original grid max 0.0000 = False`). This is
exactly the "quick/full parity" attack surface named in the task's
standard-battery item, and it caught a real defect in this round's own
addition, not the BUILDER's original code. Fixed: the original-grid bound
comparison is now gated on `not quick` (quick mode reports the extended
numbers for the record without asserting a bound that quick's own reduced
grid cannot fairly support), matching the existing precedent pattern
(`P1d`'s `len(lam_sorted) >= 2` guard for the same reason). Re-verified
23/23 quick and 25/25 full after the fix.

### Attack 2 -- the mirage grading. VERDICT: HOLDS, WITH A REAL DOCUMENTATION CORRECTION

Loaded the tracked `.npz`, located the three flagged cells
(`p1_drho >= 0.1`: lambda=3.6056 t=6.579, lambda=6.0 t=4.743, lambda=6.0
t=12.84 -- matching the `.md`'s own table exactly), and independently
recomputed their full SVD spectra from the module's own `gram_matrices`
(not from any cached array). Applied a plot-free numeric criterion for
"smooth decay vs. genuine gap": for each cell, the ratio
sigma_{r+1}/sigma_r AT the declared-rank boundary, compared against the
MEDIAN of all other consecutive singular-value ratios in the same
spectrum.

**Finding.** All three cells show a ratio at the boundary 3+ orders of
magnitude below the median ratio elsewhere in the spectrum -- i.e. there
genuinely IS a disproportionate step exactly at the rank boundary in every
case (lambda=3.6056: boundary ratio 2.47e-07 vs. median 2.46e-01;
lambda=6.0,t=4.743 -- the ONE cell the original `.md` actually showed a
spectrum for: boundary ratio 5.4e-04 vs. median 7.5e-02; lambda=6.0,
t=12.84: boundary ratio 2.95e-07 vs. median 3.3e-01). This means the
original text's "smooth monotone decay with no clean gap anywhere,"
generalized from the one shown spectrum to a blanket description of all
three, is not an accurate characterization: a real ratio-sense cliff
exists at the boundary in all three, not just a gradual roll-off.

**What this does NOT do: change the verdict.** The step is between two
already-negligible values -- `sig_r` itself (the value just BEFORE the
step) is only 1.7e-06 to 9.9e-06 at these three cells, three to six orders
of magnitude below the 1e-3 floor the spec requires for a step to count as
"genuine" rather than noise. So the correct, precise characterization is:
a boundary between noise and deeper noise, not signal falling off a cliff
into noise. This is textbook behavior for Gaussian/RBF-kernel Gram
matrices, whose eigenvalues are known to decay super-exponentially and can
show a locally sharp RATIO step at essentially any threshold-crossing
index purely from smoothness, with zero arithmetic content. This is
exactly why `is_discovery_candidate` was built to gate on the ABSOLUTE
scale of `sig_r` (> 1e-3) rather than on local spectral shape -- the
finding, properly read, is a confirmation that the module's design choice
was the right one, not a challenge to it. It also, independently, confirms
`is_discovery_candidate`'s conditioning-pair convention matches e1o's own
`cheapness()` "min sv" discipline exactly: `sig_r = sv[r-1]/sv[0]` (e1o's
single reported number when the declared rank is `r`) with `sig_r1 =
sv[r]/sv[0]` as the natural pair-extension the build spec's own text
requested.

Folded into the module as printed diagnostics (the full spectrum +
boundary-vs-median ratio for every raw-gap cell, every run) plus a new
Check `P1g` confirming numerically, not just by eyeball on one example,
that every raw-gap cell is rejected on absolute scale regardless of local
shape. Both `.py` (the docstring's RESULT section) and `.md` (the Phase 1
section and STATUS BANNER) were corrected in place, marked `[ADVERSARY,
mirage grading]`.

### Attack 3 -- small-t validity. VERDICT: HOLDS, with a numeric slip fixed (direction of the error was harmless)

The build spec requires the direct wrap-sum truncation's dropped tail to
be `<1e-12` relative to the kept sum. The module fixes `Nwrap=80`
everywhere (not adaptive) and justifies this in a code comment claiming
"the dropped-tail exponent `-pi(nL)^2/t` is then at least `-pi n^2`,
e.g. `n=81` gives `~1e-2800`." Independently recomputed `exp(-pi*81^2)`
directly (mpmath, 50 decimal digits): **2.122e-8952**, not `~1e-2800` --
the original comment's estimate was off by roughly 6150 orders of
magnitude (in the safe direction: the true bound is astronomically
smaller/safer than claimed, so no check or conclusion was ever
threatened, but the specific quoted number was simply wrong, a
hand-arithmetic slip). Fixed in both `.py` (the `theta_wrap_np` docstring)
and `.md` (the "why the tested pairs are anchored" paragraph), each noting
the correction explicitly.

**Beyond the reasoning, direct empirical confirmation** (not just trusting
either estimate): compared `Nwrap=80` against `Nwrap=400` in the ACTUAL
float64 `theta_wrap_np` code path (the one Phase 1/2 actually run) at
lambda=6's smallest tested t (0.00445) and largest tested t (12.84, i.e.
`L^2`) -- exact equality to double precision at both extremes (relative
discrepancy exactly 0.0). Separately, in mpmath at 50 decimal digits,
compared `Nwrap=80` against `Nwrap=400` across every `(lambda, t, node
difference x_j - x_k)` triple in the entire Phase-1 grid (both t extremes,
all four lambda, actual node diffs not just `y=0`): relative discrepancy
below `1e-50` everywhere, 38 orders of magnitude past the spec's `1e-12`
bar. `Nwrap=80` is not merely "safe" as claimed; it is safe with margin to
spare by any reasonable standard. No check needed correcting; this
confirms the BUILDER's underlying engineering judgment was sound, only one
quoted supporting number was wrong.

**A related, deeper finding not on the original attack list but
discovered while investigating it.** Phase 0's own quoted "~1e-36" defect
figure is the `mp.mp.dps=35` working-precision *rounding floor*, not the
identity's true mathematical tightness. Re-ran the identical Phase 0
check at dps=50/80/120: the measured defect drops to ~1e-51/~1e-81/~1e-121
respectively, scaling almost exactly linearly with dps -- i.e. the "1e-36"
number is measuring mpmath's own arithmetic noise at the chosen precision,
not a fixed property of the identity (whose true truncation-limited
accuracy, per the Nwrap/Kwrap=80 tail bound above, is bounded near
`1e-8952`). This does not change the Phase 0 PASS verdict (either reading
clears the `1e-25` bar by a huge margin) but is a real epistemic-precision
correction: the module was, without noticing it, reporting an artifact of
its own arithmetic library's precision setting as if it were a measured
property of the mathematics. Documented in place in both files, marked
`[ADVERSARY, precision-floor note]`.

### Attack 4 -- twin fairness. VERDICT: HOLDS, with the sharpest gap of the round closed

**(a) Matched density.** `M_Beurling / M_zeta` at the tested lambda grid:
{1.5, 1.0, 0.83, 1.18} -- noisy at these tiny counts (M=2 to 11), exactly
what a Poisson-type generalized-prime process should show at small
samples, not a systematic mismatch. Confirmed this tightens at the
extended grid's larger M: {1.04, 0.96, 0.97, 0.97} at M = 25-154.
Density-matched by construction, now confirmed rather than merely
asserted by the spec's own text.

**(b) Identical t-grid and threshold.** Direct code read: the twin loop
consumes `t_grid_by_lambda[lam]` -- Phase 1's own already-computed grid,
passed in verbatim -- and calls `numeric_rank(G)` with the module-global
`RANK_THRESH` (1e-8), the identical constant zeta's cells are graded with.
No independent recomputation, no separate threshold, confirmed by reading
`run_phase2`'s loop structure directly, not inferred from output.

**(c) The sharp one.** Is the twin's own larger raw fluctuation (0.231 at
lambda=6, t=12.84, vs. zeta's 0.182 at the same cell) itself mirage-graded
by the SAME `sig_r`/`sig_r1` gate, or was the `.md`'s "generic SVD-tail
noise, not an arithmetic effect" reading merely asserted by comparing raw
`Delta_rho` magnitudes? **Checked directly: it was merely asserted.** The
original `run_phase2` computed `rG, _ = numeric_rank(G)` for the twin --
discarding the singular values entirely, so no conditioning number for the
twin was ever computed anywhere in the module. Independently computed it
(and then folded the capture into the module itself): the twin's two
raw-gap cells (lambda=6, t=4.743 and t=12.84) have `sig_r` = 1.13e-05 and
1.56e-06 respectively, both far below the 1e-3 bar. **The "mirage, not
arithmetic" reading is correct**, now verified by the identical numeric
criterion rather than argued by analogy to the raw-magnitude comparison
alone -- but it was a real, previously unclosed gap: had the twin's own
`sig_r` come back above 1e-3 (a well-conditioned twin gap alongside a
mirage-graded zeta gap), the `.md`'s "reinforces the mirage reading"
sentence would have been actively wrong, and nothing in the original
module would have caught it. Folded in as new Check `P2a2` (original
grid) and `P2h` (extended grid, where the twin has no raw-gap cells at
all, consistent with `P1e`'s finding there).

### Attack 5 -- standard battery. VERDICT: TWO GENUINE CATCHES (K1 scanner, periodization invariant), rest HOLDS clean

**K1 guard injection test (scratch copy, outside the repo).** Copied the
module to the scratchpad, injected an unguarded
`_sneaky_zero = mp.zetazero(1)` with the comment
`# ADVERSARY INJECTION: unguarded, no K1-ALLOW` (not a genuine exemption)
into `run_phase0`. Ran the module's own `P2d` source-scan logic (copied
verbatim) against the injected source: **MISSED** -- `hits: []`. Root
cause: the scan's exemption test was a bare substring check,
`"K1-ALLOW" not in ln`, and my injected comment happens to CONTAIN the
substring "K1-ALLOW" (in the phrase "no K1-ALLOW", discussing the concept
without granting it), so the naive scanner treated the whole line as
exempt. **This is a real, if narrow, gap**, not an artifact of a
contrived test: any future edit that adds an unguarded call on a line
whose comment happens to mention "K1-ALLOW" in prose (not as a genuine
marker) would silently evade the static scan. Then ran the INJECTED
module directly as a subprocess: the RUNTIME guard tripped immediately
(`RuntimeError: K1 guard: zero-list access attempted`, exit code 1) --
defense in depth held; the actual call would never have executed
undetected. **Fix applied**: tightened the exemption to require the
marker as an actual trailing-comment token, `"# K1-ALLOW"`, matching the
two real guard-install lines verbatim. Re-verified: the two legitimate
exemptions still pass (`Case A`), the original crafted injection is now
caught (`Case B`: `hits: ['zetazero']`). Honestly noted, not swept under
the rug: a SECOND-ORDER adversarial comment engineered to contain the
literal substring `"# K1-ALLOW"` without being a genuine exemption
(`# K1-ALLOW is not actually granted here`) still slips past even the
tightened check (`Case C`) -- an inherent limitation of any purely textual
marker, which is exactly why the runtime guard, not the static scan, is
documented (both in-code and in the `.md`) as the load-bearing K1
enforcement layer. This same bare-substring pattern is shared verbatim
across e1o/e1m/e1p/e2al; only e1q's own copy was hardened here (in scope
for this round), and the shared-convention observation is recorded for a
future cross-file pass, not silently fixed elsewhere.

**Falsifiability spot-check: 3 deliberate corruptions, in a scratch copy.**

1. *Phase 0 threshold tightened* (`1e-25` -> `1e-40`, forcing a FAIL given
   the measured ~1e-36 defect): correctly flipped to `[FAIL]`
   (`max rel defect 1.46e-36` against the tightened `1e-40` bar); self-test
   dropped from 14/14 to 13/14 in quick mode. HOLDS.
2. *`is_discovery_candidate`'s `sig_r` comparison direction flipped*
   (`> 1e-3` to `< 1e-3`, a canary corruption): correctly produced 3
   spurious "discoveries" from the 3 previously-mirage cells, flipping
   `P1c` and `P2a` to `[FAIL]` and changing the overall GRADE from tier 3
   (MIRAGE) to tier 2 (MEASURED BUT PARTIAL) -- the entire downstream
   grading pipeline responded consistently and traceably to the poisoned
   input, confirming the checks are genuinely load-bearing, not vacuous.
   HOLDS.
3. *`gram_matrices`' `(G, G0)` return order swapped* (`return G0, G`
   instead of `return G, G0`, i.e. the wrap-free control and the wrapped
   kernel silently trade places everywhere downstream): **self-test still
   showed 14/14 passing in quick mode -- the corruption was NOT caught by
   any pre-existing check.** Diagnosis: since `Delta_rho = rho0 - rho` is
   always >= 0 in the real data (confirmed at 100+ cells across every
   system tested this round), swapping the labels negates every
   `Delta_rho` to <= 0, which trivially satisfies `P1c`'s "no cell reaches
   the discovery bar" condition for the wrong reason -- a real blind spot,
   not a false alarm. **Fix applied**: added a dedicated periodization
   invariant check (`Delta_rho >= 0` at every cell) at all four tested
   systems -- `P1a2` (zeta original), `P1e2` (zeta extended), `P2a3`
   (Beurling twin), `P2h2` (Beurling twin extended) -- which catches this
   exact corruption immediately (100% violation rate) and, independently,
   is itself a genuine structural confirmation worth having: periodization
   (aliasing distant copies back onto the fundamental domain) never
   increases numerical rank relative to the free-space kernel, at any
   tested cell, in any tested system, from M=2 to M=154.

**Em-dash scan.** `rg` (not `grep`, per the task's own instruction) for
U+2014 across `e1q_s4_theta_wrap_rung.py`, `.md`, and the build spec
itself: **zero matches**, both before any change and re-confirmed after
every round of edits in this report.

**Quick/full parity.** Every check name that exists in `--quick` mode is
byte-identical to one that exists in full mode (diffed the two runs'
`[PASS]`/`[FAIL]` name lists directly); the only difference is Phase 0's
2 fewer per-lambda checks in quick mode (quick tests 2 of 4 lambda), the
same +2 gap that existed before this round (14/16) and after it (23/25).
No check's threshold or pass condition differs between quick and full;
only which `(lambda, t)` points get computed differs. (The one genuine
quick-mode bug found this round, `P1f`'s vacuous `orig_max`, was in a
NEW check added during this same attack, caught by this same discipline,
and fixed before being called complete -- see Attack 1.)

**STATUS banner / next-rung line.** The banner states the tier-3 MIRAGE
verdict plainly, with no softening, and (post-fix) correctly reflects the
lambda-extension hardening and the corrected mirage-shape reading. The
"next rung = Cohn-Elkies/Viazovska/Radchenko-Viazovska modular
interpolation" line matches the build spec's own Section (d) closing
paragraph verbatim in substance (the spec's exact phrase: "the one
genuinely unexplored corner the frame audit itself flagged as having zero
repo mentions, the Cohn-Elkies/Viazovska/Radchenko-Viazovska
modular-interpolation corpus"). No overclaim found: the module never
asserts anything about RH itself, keeps PROVEN/NUMERICAL/STRUCTURAL claims
tiered and separated, and the "HONEST SCOPE" section's framing is
unchanged in substance by this round's fixes.

## (d) Fixes applied

All marked `[ADVERSARY, ...]` in place, in
`e1q_s4_theta_wrap_rung.py`/`.md`:

1. **`.py`**: added `LAMBDA_EXT = (10.0, 14.0, 20.0, 30.0)` and two new
   functions, `run_phase1_ext` (Checks `P1e`, `P1e2`, `P1f`) and
   `run_phase2_ext` (Checks `P2h`, `P2h2`), wired into `main()` -- the
   small-M-triviality extension to M ~ 100+ (Attack 1).
2. **`.py`**: added a periodization-invariant Check `P1a2` (zeta original
   grid) and, symmetrically, `P2a3` (Beurling twin) -- closes the
   `gram_matrices` G/G0-swap blind spot found during the falsifiability
   spot-check (Attack 5); `P1e2`/`P2h2` above extend the same invariant to
   the extended grid.
3. **`.py`**: added a full spectrum + consecutive-ratio diagnostic printout
   and Check `P1g` for every Phase-1 raw-gap cell (Attack 2).
4. **`.py`**: captured the Beurling twin's own singular values (previously
   discarded) and added Check `P2a2` confirming the twin's raw-gap cells
   are rejected by the identical conditioning gate (Attack 4).
5. **`.py`**: tightened the K1 source-scan exemption from a bare
   `"K1-ALLOW"` substring test to `"# K1-ALLOW"` (Attack 5), with an
   in-code comment explaining both the injection-test finding and the
   residual, inherent limitation of any textual marker.
6. **`.py`**: fixed the `theta_wrap_np` docstring's erroneous
   `"~1e-2800"` dropped-tail estimate to the independently verified
   `"~2e-8952"` (Attack 3).
7. **`.py`**: added a precision-floor clarification to the RESULT section
   docstring (Phase 0's ~1e-36 figure is the dps=35 rounding floor, not a
   ceiling on the identity's true accuracy) and corrected the "smooth
   monotone decay... at these cells" overgeneralization to the precise,
   ADVERSARY-verified reading (Attacks 2, 3).
8. **`.py`**: fixed a quick-mode-only bug in this round's own new `P1f`
   check (compared against a vacuous quick-mode `orig_max`; gated the
   comparison on `not quick`, matching the existing `P1d` precedent) --
   found by this round's own quick/full parity discipline (Attack 1).
9. **`.md`**: rewrote the header block, STATUS BANNER, Phase 0, Phase 1,
   Phase 2, Grading, Deviations, Limitations, and Handed-forward sections
   throughout, in place, to document every finding above with the
   corrected numbers, the extended-grid table, and pointers to this
   report; updated all check-count and runtime figures (16/16 ~0.1s ->
   25/25 ~1.6s full; 14/14 -> 23/23 quick).
10. **`.md`**: added a header-line pointer and multiple in-place
    cross-references to this adversary record.

No claim was softened and nothing was upgraded past its evidence: every
fix either closes a genuine, demonstrated gap (the twin conditioning
check, the K1 scanner, the periodization invariant), corrects a claim that
was broader than what had actually been shown (the mirage-shape
generalization), fixes a wrong number that never affected any verdict (the
tail-exponent estimate, the precision-floor framing), or extends the
tested range to close a legitimate statistical-weight objection (the
lambda extension) -- and in every one of these cases the extension or
correction left the module's tier-3 (MIRAGE) verdict intact, in most cases
more rigorously supported than before.

## (e) Post-fix re-verification

```
full:  25/25 checks passed, 1.5-1.6s (three consecutive re-runs)
quick: 23/23 checks passed, 0.0s
.npz:  7279 bytes, byte-identical SHA-256 and mtime before/after a
       --quick run (filesystem-verified after every round of .py edits)
em dashes: 0 (rg scan, .py + .md + the build spec)
```

All new checks (`P1a2`, `P1e`, `P1e2`, `P1f`, `P1g`, `P2a2`, `P2a3`,
`P2h`, `P2h2`) PASS. All 16 original checks continue to PASS unchanged.
No stray scratch files were left in `experiments/spectral/`
(`git status --short` shows only the three legitimately new, previously
untracked target files: `.py`/`.md`/`.npz`).

## Verdict: PASS_WITH_FIXES

Headline numbers, post-fix: **25/25 full** (was 16/16; +9 ADVERSARY-added
checks), **23/23 quick** (was 14/14), `.npz` genuinely untouched by
`--quick` at the filesystem level. The sharpest assigned attack (small-M
triviality) was run to completion at M up to 154 (14x the original
ceiling) and the wall **hardened**: this is the single most decisive
result of the round and the honest headline, per the task's own framing,
of "held or broke." Every other attacked claim held up under independent,
from-scratch re-derivation (the theta-wrap tail bound at both mpmath and
float64 precision; the periodization invariant across 100+ cells; the
twin's own conditioning numbers; the K1 injection and 3-corruption
falsifiability tests). Two real, load-bearing gaps were found and closed
(the twin-fairness conditioning check; the K1 scanner's textual-marker
robustness), one real documentation overgeneralization was corrected (the
mirage cells' spectral shape), and two numeric slips were fixed (the
dropped-tail exponent estimate; the precision-floor framing of Phase 0's
defect figure) -- none of which move the module's own tier-3 (MIRAGE)
verdict or its "narrows the search toward genuine modular-form/Hecke
structure" reading, both of which this round leaves more rigorously
supported than the original BUILDER pass.
