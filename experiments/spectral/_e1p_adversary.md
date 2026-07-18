# ADVERSARY report: e1p rank-one interlacing

> ADVERSARY attack on `experiments/spectral/e1p_rank_one_interlacing.py` /
> `.md` / `.npz`, 2026-07-17. Target: the probe measuring LEARNINGS #154
> upgrade-spec ingredient (2), "rank-one interlacing", the last of the four
> named ingredients. Grading precedent: `e1l_absorption_count.md`
> ("count_genuine=false, installed by the window, lands on the #143 side").
> All synthetic checks were RUN (not reasoned in the abstract); scripts lived
> in the session scratchpad, not the repo, and were deleted after use except
> where noted.

## (a) One-paragraph verdict

e1p **holds up**. The two headline mechanical claims (the boundary-escape
fix in `slot_shifts`, and the "D-H reproduces exact numbers under scrambling"
finding) are both correct, verified independently of the probe's own code:
the boundary-escape formula matches a hand-derived generalization of the
classical Weyl bound exactly on five synthetic cases (including a graduated
multi-slot escape run, not just a single top-slot case), and the comb
scramble is a genuine non-identity permutation (9/12 support positions
change value, multiset preserved, different seeds give different
permutations), so the D-H invariance finding is real, not a no-op artifact.
The $P_{\text{pole}} = 2(pp^{\mathsf T}+qq^{\mathsf T})$ claim is exact to
float precision ($\sim 10^{-16}$ residual) with a numerically sharp rank-2
cutoff (third singular value exactly `0.0`, not just small). The K1 scanner
survives an injected-violation stress test (flags a real `mp.zetazero` call
immediately) while staying clean on the real module and not false-positiving
on `np.zeros`/`mp.zeros` array constructors. Grading language matches the
e1l precedent's tier ("installed... lands on the #143 side") with no
over-claim, and the #164 consonance is correctly marked `[OBSERVATION,
cross-reference only]`, not an identity claim. Full-vs-quick parity is
structurally clean: quick's 16 checks are the exact same `check()` call
sites as 19 of full's, evaluated at fewer Q3 grid points (no quick-only
check, no quick-only relaxed threshold). One genuine documentation gap was
found and fixed: the central-band "shift is guaranteed algebraically" claim
proved only half its own assertion (that $D$ has an exact zero eigenvalue),
not the other half (that the zero eigenvalue lands at the *central sorted
position*, which needs an evenness/negation-symmetry argument the original
text skipped straight past with "see Q1 table"). Verdict: **PASS_WITH_FIXES**.

## (b) Reproduction

| run | expected | observed |
|---|---|---|
| full (`python -m experiments.spectral.e1p_rank_one_interlacing`) | 19/19, ~2 min | **19/19 passed, 111.0s** |
| quick (`--quick`) | 16/16 | **16/16 passed, 31.3s** (33.8s on re-run after the .py fix) |
| `.npz` untouched by quick | mtime/size unchanged | size **50705 bytes** before and after quick; mtime **identical to the last full run** in both cases (confirmed via filesystem `stat`, not just the printed message) |

Both runs printed all `[PASS]` lines with no `[FAIL]`s, matching the .md's
claimed headline numbers exactly before any adversary changes were made.

## (c) Attack axes

### Axis 1 -- the shift=3 point vs the narrative. VERDICT: HOLDS (minor consistency fix applied)

The "3" does not come from Q1's own 7-point grid (which maxes at 2, confirmed
in the full run's printed table); it comes from Q2/Q3's separate point
$(\lambda,N)=(\sqrt{13},24)$, the *same cached build* reused across both
(confirmed: `get_build` caches by `(label, lam, N, use_pole)`, and Q3's own
text says "matching Q2's ZETA measurement at the identical point exactly,
since it is the same cached build" -- verified true by reading the cache-key
construction). This is legitimately still "the ingredient" (same
`slot_shifts(d0_spectrum, d_spectrum)` object Q1 measures), just at a point
outside Q1's own tested grid, and the `.md`'s STATUS BANNER (the file's own
"read before quoting any number" gate) states it up front and unambiguously:
"interlacing HOLDS, empirically, at a small ($\le 2$--$3$)... bound -- but
only as a *measurement*" with the non-manifestly-satisfied-hypothesis caveat
in the same sentence. The "One-line result" section repeats it: "at most 2
sorted slots across the primary grid (3 at one additional point)". Not
buried in the .md. **Fix applied**: the `.py`'s own terminal `VERDICT` print
block (the summary a CI log or terminal session would show, as opposed to
the `.md`) stated only "small, family-uniform" without the specific figure,
which was an inconsistency between the two artifacts (not a lie, but a real
reader who only sees console output would miss the "3"). Patched to read
"a small (<=2 across the Q1 grid, 3 at the separate lambda=sqrt13 point
measured in Q2/Q3)". Re-run confirms 16/16 quick still passes with the new
wording displayed correctly.

### Axis 2 -- the boundary-escape fix. VERDICT: HOLDS (independently verified correct)

Read `slot_shifts` line by line. The fix's rule -- if `v` escapes the entire
base range `[d0[0], d0[-1]]`, report `r[i] = (n-1)-i` (distance from the top
slot) or `r[i] = i` (distance from the bottom slot), instead of an unbounded
symmetric-window search -- is not an ad hoc clip. It is the exact limit of
the *same* growing-window search once the window's edge hits the array
boundary: past that point the classical one-sided Weyl bound treats the
missing neighbor as an unbounded ceiling/floor, so the minimal satisfying
radius *is* the index distance to the boundary, not a search that never
terminates. Verified with five hand-computable synthetic cases
(`adversary_checks.py`, run and confirmed, then deleted with the rest of the
scratch scripts):

- **Case A** (diagonal rank-1 PSD addition concentrated on the top basis
  vector, `d0=[1,2,3,4,5]`, top eigenvalue blown up to 105): `slot_shifts`
  returns `[0,0,0,0,0]` exactly -- the bottom four slots are untouched
  (matches theory: a PSD rank-1 addition aligned with one eigenvector leaves
  the others exactly fixed) and the escaping top slot reads shift 0
  (correctly recognizing "the top slot is allowed to escape unboundedly" as
  the *expected*, not anomalous, case).
- **Case B** (generic random `w`, moderate weight): classical two-sided
  Cauchy bound `d0[i] <= dB[i] <= d0[i+1]` (`i<n-1`) verified by hand
  alongside `slot_shifts`; max shift `<=1` in both, matching Q1-0's own
  harness-sanity check.
- **Case C** (generic random `w`, weight $\times 1000$, forcing a dramatic
  top escape to $\sim 2.8\times 10^6$): the escape is still exactly at
  index `n-1` (never elsewhere, matching Weyl monotonicity: a PSD addition
  can only ever push the *top* eigenvalue past the base range), and
  `slot_shifts` reads shift 0 there, `<=1` everywhere else.
- **Case D** (synthetic, non-PSD-realizable, direct formula stress test:
  three trailing values `[500,501,502]` against `d0=[1,2,3,4,5]`, exercising
  the general (non-PSD, as Q1's actual `P1` is) case of a *run* of escaped
  values): `slot_shifts` returns `[0,0,2,1,0]`, exactly the hand-derived
  `(n-1)-i` graduated sequence -- **not** clipped to a flat 0/1, correctly
  distinguishing "how far past the boundary slot" by index, which is the
  only sense of "distance" available once the value itself is outside the
  base range's comparison window.
- **Case E**: symmetric bottom-escape run, same graduated-formula match.

(My first attempt at Case D used a wrong hand-derived expected value --
caught by the assertion failing -- and on inspection the bug was in my own
test's arithmetic, not the code: I had mis-tracked which sorted index held
which value. Corrected and re-verified; recorded here as part of the
adversarial process, not swept under the rug.)

No clipping, no fabricated small numbers: the fix correctly and exactly
implements the boundary limit of the same window-search rule used in the
interior, which is why it produces graduated (not saturating) shifts for
runs of escaped eigenvalues.

### Axis 3 -- the scrambling claim. VERDICT: HOLDS (genuine permutation, not a no-op)

Reproduced "D-H reproduces its exact original numbers under scrambling"
directly from the full run's own printed output: `Q2-D-H reweighting-blind`
check shows `orig max/mean=2/0.980  scrambled max/mean=2/0.980`, unchanged
to three decimals, exactly as the `.md` states. Independently verified
`scramble_stream` is a real, non-trivial permutation (`adversary_checks.py`,
Attack 3 section): built a synthetic 30-length stream with 12 support
positions, scrambled with seed 7, and found 9 of 12 positions changed value
(3 fixed points is unsurprising for a random permutation of 12 elements),
the value *multiset* at support positions was exactly preserved (a valid
permutation, not corruption), and a different seed (8) produced a visibly
different permutation. The D-H exact-reproduction finding is therefore a
real (if striking) empirical fact about the operator's insensitivity to
which value sits where in its comb, not an artifact of a broken or
identity-mapping scrambler.

### Axis 4 -- the PSD rank<=2 pole claim. VERDICT: HOLDS (exact, not approximate)

Built `Q_full`/`Q_noPole` directly via `e1k.build_float` at two independent
grid points (`adversary_attack4.py`, not reusing any of e1p's own Q3 code)
and independently reconstructed $2(pp^{\mathsf T}+qq^{\mathsf T})$ from
$\widehat V_n(i/2) = p+iq$ using a hand-written closed form (not imported
from either e1k or e1p). Result: `max|dQ - 2(pp^T+qq^T)|` = `9.0e-17` at
$\lambda=2.6,N=8$ and `4.9e-16` at $\lambda=3.606,N=12$ -- machine epsilon,
i.e. the formula is *exact*, not merely close. The singular-value spectrum
of `dQ` is `[4.126, 0.282, 0.0, 0.0, 0.0, ...]` and `[5.894, 0.724, 0.0, ...]`
respectively: the third singular value is *literally* `0.0` in the printed
output, not just below a tolerance -- the rank-2 cutoff is as sharp as
floating point allows, confirming both the algebraic identity and the rank
bound with no slack needed, matching the `.md`'s "provable, verified" tier
language for this case (as opposed to Q1's operator-level "measurement"
tier, which is correctly kept separate).

### Axis 5 -- the K1 scanner reword. VERDICT: HOLDS (catches real violations, no regressions)

Copied the real module to a scratch directory (outside the repo),
injected `_sneaky_zero = mp.zetazero(1)` (not marked `K1-ALLOW`, not a
comment), and ran the *exact* scanner logic (copied verbatim from
`run_disciplines`) against the modified source (`adversary_attack5.py`):

1. **Injected violation**: flagged immediately, `hits: ['mp.zetazero']`. PASS.
2. **Real module**: scans clean, `hits: []`, matching the probe's own
   `DISC K1 source scan` result. PASS.
3. **Regression check** (the false positives the builder already fixed --
   bare `np.zeros(10, dtype=int)`, `mp.zeros(5,5)`, and the word "zetazero"
   appearing in a comment): no false positive. PASS.
4. **K1-ALLOW exemption sanity**: a `mp.zetazero(1)` call marked
   `# K1-ALLOW (guard install)` is correctly exempted -- this is the
   documented behavior (used only at the two guard-install lines in the
   real module), not a scanner gap, confirmed by Test 2 showing the real
   module's two `K1-ALLOW`-marked guard-install lines do not trip it while
   nothing else does either.

Also grepped the real module directly for `ZETA_ZEROS|DH_ZEROS|DH_OFFLINE|
match_known|zetazero|\.zeros\(` -- the only hits are the scanner's own
comments explaining its logic, the (concatenation-built, non-self-matching)
forbidden-token list definition, and the two `K1-ALLOW`-marked guard-install
lines. e1p's import list from e1k (`make_streams, build_float,
operator_spectrum, ZETA_CFG, DH_CFG`) does not include `ZETA_ZEROS`,
`DH_ZEROS`, `DH_OFFLINE`, or `match_known`, so no zero location or
zero-derived reference constant is reachable from e1p at all, by import
graph, independent of the source-scan. Scratch copy deleted after the test.

### Axis 6 -- grading consistency. VERDICT: HOLDS

Compared the `.md`'s Q2 verdict ("LANDS ON THE #143 SIDE... a generic
operator-theory fact... not a Betti-type invariant the construction computes
by its own symmetry") against e1l's precedent tier ("#143 shell CONFIRMED
(spectrum budget installed, not computed)... a generic operator-theory
fact"). Same tier, same hedge words, no stronger claim. The #164 consonance
is stated as `[OBSERVATION, cross-reference only, per LEARNINGS #164]... No
claim is made that these are the same object; the consonance is noted and
left there` in both the `.md` and the `.py`'s printed Q3 summary
("consonant with but not claimed identical to #164's codim-2 observation").
Matches the required citation-only, non-identity framing throughout.

### Axis 7 -- full-vs-quick parity. VERDICT: HOLDS

Counted every `check()` call site: Q1 contributes 5 checks (`Q1-0` through
`Q1-4`) computed once per run regardless of grid size (the grid only feeds
the aggregate statistics those 5 checks test); Q2 contributes 4 (2 labels
x 2 checks), independent of `quick`; Q3 contributes 3 checks *per grid
point*, with quick using 1 point (`(2.6,16)`) and full using 2
(`(2.6,16), (sqrt13,24)`) -- the only place quick and full differ in check
*count*; Disciplines contribute 4, independent of `quick`. Total:
full `5+4+6+4=19`, quick `5+4+3+4=16`, matching both runs' self-reported
counts exactly. Every check name/threshold that exists in quick mode is the
*identical* code path in full mode (no `if quick:` branch changes a pass/
fail threshold; the only `if quick:` branches select which `(lambda,N)`
points or grid rows get *computed*, not how they get graded). Quick's own
Q1 sub-grid (`(2.6,8),(2.6,16)`) is not just "in spirit" a subset of full's
7-point grid -- it uses the exact same `(lambda,N)` pairs, so quick never
exercises a parameter combination full doesn't also cover. No check exists
that only runs (or only passes) in quick mode.

### Axis 8 (found during the attack, not on the assigned list) -- the central-slot "guaranteed algebraically" claim. VERDICT: INCOMPLETE, FIXED

The `.md` claimed: "$M\xi_n = D_0\xi_n - (D_0\xi_n)(\delta_N\cdot\xi_n) = 0$,
so $D$ has an exact zero eigenvalue by construction, matching $D_0$'s exact
zero at $n=0$ -- the central slot's shift of $0$... is therefore guaranteed
algebraically, not just observed." The shown algebra proves only that *a*
zero eigenvalue exists somewhere in $\mathrm{spec}(D)$; it does not show
that eigenvalue lands at the *central sorted position* (the actual
requirement for `slot_shifts` to report shift 0 there), and the text jumped
straight to "see Q1 table" for that half -- an assertion from data, not a
derivation, dressed as "guaranteed algebraically."

Investigated whether the stronger claim is even true, and if so, why.
Derived the missing step: let $J$ be the index flip $n\mapsto -n$. Since
$D_0=\mathrm{diag}(\phi n)$, $JD_0J^{-1}=-D_0$; since the CF ground state
$\xi_n$ is selected even and $\delta_N$ is manifestly even (a constant
vector), $J\xi_n=\xi_n$ and $J\delta_N=\delta_N$, giving $JMJ^{-1}=-M$
exactly. $M$ and $-M$ are therefore similar, so $\mathrm{spec}(M)$ is
symmetric under negation; with $D=2N+1$ odd and one confirmed zero, the
remaining $2N$ eigenvalues must split exactly $N$-below/$N$-above, which is
what actually places the zero at the central slot.

Verified this numerically at all 14 of Q1's own grid points (both twins,
`adversary_attack_central.py`): `n_below == n_above == N` exactly at every
point, and the real part at the true middle sorted index is
$\le 3\times 10^{-10}$ even at the noisiest tested point (ZETA
$\lambda=3.0$, where $\xi_n$'s own evenness is weakest at
$\|\xi_n-J\xi_n\|_\infty\approx 4\times 10^{-6}$, producing a small
near-degenerate *cluster* of eigenvalues around 0 there instead of one
clean zero -- itself consistent with, not a violation of, the symmetry
argument, since the cluster stays balanced and the sorted-middle value
stays commensurately tiny). So the stronger claim is **true**, just
under-derived in the original text.

**Fix applied**: completed the derivation in place in the `.md` (the
$J$-conjugation argument above, with the 14-point verification cited),
marked `[ADVERSARY, completed derivation]`. This does not change the
conclusion (central shift is 0, exactly as the Q1 table already showed) or
any check's pass/fail status; it closes a real gap between "guaranteed
algebraically" and what was actually shown.

## (d) Fixes applied

1. **`e1p_rank_one_interlacing.md`**: completed the central-slot derivation
   (Axis 8) with the missing negation-symmetry argument, marked
   `[ADVERSARY, completed derivation]` in place.
2. **`e1p_rank_one_interlacing.py`**: patched the terminal `VERDICT` print
   block's Q1 line to state the "<=2 across the Q1 grid, 3 at the separate
   lambda=sqrt13 point" figure explicitly (Axis 1), for consistency with
   the `.md`'s STATUS BANNER. Print-string only, no logic or data change.

No other defects found. Nothing was softened, and nothing was upgraded past
its evidence: both fixes make honestly-true claims more *completely*
justified or more *consistently visible*, they do not change what is
claimed.

## (e) Post-fix re-verification

Re-ran quick mode immediately after the `.py` edit: **16/16 passed**, new
VERDICT wording displayed correctly, 33.8s. Re-ran full mode after both
edits to refresh the tracked artifact from the final source (the edits are
print/prose-only, so the underlying `results` dict and hence the `.npz`
content are unaffected; this run is a hygiene re-confirmation, not a
correctness necessity): **19/19 passed, 110.5s**, `.npz` re-saved at
identical size (50705 bytes) to the pre-fix run, confirming the fixes
changed no computed data, only wording.

## Verdict: PASS_WITH_FIXES

Headline numbers, post-fix: **19/19 full, 16/16 quick**, `.npz` genuinely
untouched by `--quick` (byte-identical size and mtime, filesystem-verified).
Every attacked claim held up under independent, from-scratch verification
(hand-computed synthetic cases for the boundary-escape fix; an independently
built formula check for $P_{\text{pole}}$; an injected-violation stress test
for the K1 scanner; direct multiset/permutation checks for the comb
scramble). The one real defect found (Axis 8, the under-derived central-slot
claim) was a documentation completeness gap, not a wrong result or a
disguised bug, and is now fixed in place with the missing step supplied and
numerically checked at every one of Q1's 14 grid points. The probe's own
self-graded tier (measurement, not theorem, for Q1/operator-level; provable
and verified for Q3/form-level; lands on the #143 side for the W6-vs-#143
gate; input-faithful-but-RH-blind for the pole-block angle) is accurate and
consistent with the e1l precedent throughout.
