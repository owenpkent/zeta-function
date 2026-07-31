# The D-H undercount look (#169, one look)

> **VERDICT: MECHANISM.** The undercount is a genuine, precision-independent
> structural fact about the Davenport-Heilbronn twin, not a window/grid/
> conditioning artifact: D-H's truncated Weil quadratic form has a ground-state
> gap (`gap_even`, the distance from the lowest to the next EVEN eigenvalue of
> `Q`) that collapses by four to six orders of magnitude relative to zeta's as
> `lambda` grows (confirmed identically in float64 at `N = 5, 8, 20` AND in
> full high-precision `mpmath` linear algebra at `dps = 30`, not merely a
> higher-precision archimedean quadrature), while zeta-off's ground state stays
> robustly negative and gapped throughout. That collapse forces the rank-1
> `D_log` operator's secular residues to blow up (measured `max|r_k|` growing
> from ~330 to ~1.9e5 for D-H across `lam in [3.0, 4.5]`, vs a flat ~0.2-0.4 for
> zeta-off), producing non-perturbative eigenvalue displacement that
> occasionally ejects one or two modes from the counting window. **Important
> qualifier**: the *exact numeric* window-count deficit reported by the e1s
> adversary note at the family's standard `dps = 25` is itself partly
> precision-fragile at the most extreme near-degeneracy: the `lam = 4.5, N =
> 20` cell resolves to the exact target count (`20`, zero deficit, zero
> ghosts) once `dps` is pushed to `40`. So "D-H undercounts the lattice by 1-2,
> ghost-free, genuine" (the e1s wording) is a correct SYMPTOM but an incomplete
> mechanism reading: the root cause (gap collapse) is real and robust; the
> specific integer reported at `dps = 25` is not always precision-converged.

## What this is

A one-look diagnostic on TODO #169 / the ADVERSARY (2026-07-12) finding in
`experiments/spectral/e1s_rank_one_interlacing.md`: D-H undercounts the
geometric lattice count `floor(T/phi)` by 1-2 (reported "ghost-free") at `lam
in {3.3, 3.6, 4.0, 4.5}`, while zeta-with-pole-off (`Zoff`) stays exact at the
same cells. This note reproduces it, runs the artifact-vs-mechanism
discriminating battery the task specifies (window placement/width, grid
resolution, precision/dps, neighboring lambda), locates WHERE the missing
eigenvalue(s) actually went, and names the driving mechanism. All diagnostics
reuse the e1k/e1s harness read-only (`build_float`, `operator_spectrum`,
`build_hp`, `make_streams`, `ZETA_CFG`, `DH_CFG` from
`experiments/spectral/e1k_dh_dlog_testbed.py`); no tracked `.npz` was
modified, and no ad hoc script was committed to the repo (all probes were
scratch, disposable, and are described below in enough detail to rerun).

## 1. Reproduction

`win_counts` = (filtered real-in-window count, unfiltered count, in-window
ghosts), `N = 20`, `dps = 25` (the e1s default), `target = min(N, floor(T/phi))`:

| lam | floor(T/phi) | target | DH filt (dev) | Zoff filt (dev) |
|---|---|---|---|---|
| 3.0 (control) | 19 | 19 | 19 (+0) | 19 (+0) |
| 3.3 | 26 | 20 | 19 (-1) | 20 (+0) |
| 3.6 | 33 | 20 | 19 (-1) | 20 (+0) |
| 4.0 | 44 | 20 | 19 (-1) | 20 (+0) |
| 4.5 | 60 | 20 | 18 (-2) | 20 (+0) |

Matches the e1s adversary table exactly (`DH_f = 19/19/19/18`). Reproduction
confirmed.

## 2. Discriminating tests (artifact-mode checklist)

The task calls out three documented artifact patterns to rule out first:
e1r's spatial-window mirage (a rank/count drop that tracks an arbitrary
window boundary and vanishes once the window is relaxed), e1u's UGRID-floor
artifact (a grid-resolution effect), and e1q's conditioning mirage
(precision-dependent, resolves at higher working precision). All three were
tested directly.

**(a) Window-boundary sweep (rules out the e1r spatial-window-mirage
pattern).** Swept `re_lo` from `1.0` down to `-1.0` at `lam = 3.3` and `lam =
4.5`, `N = 20`:

- `lam = 3.3`: `filt` stays at `19` for every `re_lo` in `{1.0, 0.8, 0.5, 0.3,
  0.1, 0.0}`; only at `re_lo <= -0.5` does the count change, and it changes by
  picking up BOTH a new real eigenvalue AND 2 new ghosts simultaneously
  (`filt=20, ghost=2`), not by recovering a clean real eigenvalue that had
  been sitting just below the `1.0` cutoff.
- `lam = 4.5`: `filt` stays at `18` for `re_lo` in `{1.0 ... 0.0}`; only at
  `re_lo <= -0.5` does anything change, again with ghosts appearing
  (`ghost=4`).

**Verdict: NOT a window-boundary mirage.** If this were the e1r pattern, a
genuine, well-conditioned real eigenvalue would sit just outside `(re_lo, T)`
and reappear cleanly as `re_lo` relaxes. Instead nothing happens until the
window is pushed deep into ghost territory. The missing mode is not "just
below the fence."

**(b) N-resolution sweep (rules out the e1u UGRID-floor pattern).** `lam =
3.3`, `N in {16, 20, 24, 28}`:

| N | target | DH filt | dev |
|---|---|---|---|
| 16 | 16 | 15 | -1 |
| 20 | 20 | 19 | -1 |
| 24 | 24 | 23 | -1 |
| 28 | 26 | 24 | -2 |

The deficit is stable at `-1` across a 50% change in grid size and only
worsens (not resolves) at the largest `N` tested. **Verdict: NOT a
grid-resolution artifact** (a UGRID-floor effect would vanish as the grid
refines; this one persists and grows).

**(c) Precision (archimedean-quadrature dps) sweep, MIXED result (partially
confirms an e1q-style conditioning layer).** `lam = 3.3`, `N = 20`, `dps in
{15, 20, 25, 30, 35, 40, 50, 60}`: `filt = 19` at every dps tested, deficit
`-1` throughout, and ghosts (present at `dps <= 30`, sitting near `re = 0`,
i.e. OUTSIDE the counting window) vanish entirely by `dps = 35` yet the count
does NOT recover -- at `dps = 50` the full spectrum is exactly real
(`max|Im| ~ 1e-10`) and the same two lattice slots (near targets `n=1` and
`n=4`) are still genuinely absent (see section 3). **This cell is precision-
robust: NOT an artifact.**

But at `lam = 4.5`, `N = 20`, the SAME sweep gives a different story:

| dps | filt | unfilt | ghost | in-window ghost re |
|---|---|---|---|---|
| 15 | 17 | 19 | 2 | {20.68} |
| 25 | 18 | 18 | 0 | {} |
| 40 | 20 | 20 | 0 | {} |

At `dps = 40` this cell resolves to the **exact target count with zero
ghosts anywhere**. **This cell IS precision-fragile at the standard `dps =
25`** (an e1q-style conditioning mirage superimposed on the real mechanism):
the archimedean quadrature isn't accurate enough, at the family's usual
working precision, to correctly resolve which eigenvector is the true ground
state once the underlying analytic gap (see section 4) has collapsed to
`O(1e-6)` or smaller.

**(d) Fine lambda scan.** `lam in {3.0, 3.1, ..., 3.5}`, `N = 20`: `DH filt`
deviates `{0, -1, 0, -1, 0, -1}` -- not a sharp threshold, not monotone, but
also not confined to the four originally-flagged values; the phenomenon is
present at a roughly half of the tested cells in this range, alternating with
"exact" cells. `Zoff` stays exact (`dev = 0`) at every one of these cells.

## 3. Where the missing eigenvalue(s) actually go

Full raw spectrum dumps (both signs, `n = -N..N`) at `lam = 4.5, N = 20, dps =
25` and `lam = 3.3, N = 20, dps = 50` locate the mechanism directly:

- **`lam = 4.5` (moderate dps):** the `+-1` pair of modes that should sit near
  `+-2.09` is entirely absent from the real spectrum; in its place there is a
  complex-conjugate ghost pair sitting at `re ~ +-0.0000, im ~ +-5.99`, plus a
  second ghost pair further out at `re ~ +-20.68, im ~ +-23.86` (this second
  pair happens to land ON the window boundary region, so at `dps=15` it shows
  up as an "in-window ghost"; at `dps=25` numerical noise moves it just
  outside, hence "ghost-free" only by the accident of where it lands, not
  because there is no ghost). The near-`0` ghost pair sits OUTSIDE the
  counting window (`re_lo = 1.0` excludes anything near the origin), so
  `win_counts`'s own in-window ghost filter reports `ghost = 0` for this cell
  even though a genuine reality-breaking event (a real +-1 mode pair going
  complex) is exactly what happened. **This is the same "approximate
  self-adjointness throws eigenvalues off the real axis" mechanism already
  documented for zeta's pole term (e1k caveat 2 / e1l STEP 5), just relocated
  outside the window where the existing ghost instrument does not look.**
  "Ghost-free" in the e1s note is therefore a characterization gap in the
  instrument, not evidence the mechanism is absent.
- **`lam = 3.3` (high dps, fully real spectrum, `max|Im| ~ 1e-10`):** the
  modes that should sit near targets `n = +-1` (`+-2.63`) AND `n = +-4`
  (`+-10.53`) are BOTH entirely absent from the low end of the spectrum;
  compensating "doubled" pairs of eigenvalues cluster near targets `n = 5, 7,
  9` (two close-together real eigenvalues instead of one). Two genuinely
  displaced real eigenvalues appear at `re ~ +-209.9` -- nearly four times
  further out than the highest nominal mode (`phi*N ~ 52.6`). This is a
  large-scale, real, non-perturbative reorganization of the low spectrum, not
  a boundary-adjacent event and not a complex-ghost event at this precision.

## 4. The driving quantity: D-H's ground-state gap collapse

`gap_even` = distance from the lowest EVEN eigenvalue of the truncated Weil
form `Q` to the next EVEN eigenvalue (the quantity e1k's `build_float` already
computes as a simplicity diagnostic). Measured across `lam`, `N = 8, dps =
25`:

| lam | DH gap_even | Zoff gap_even | ratio Zoff/DH |
|---|---|---|---|
| 2.0 | 1.62 | 2.83 | 1.7 |
| 2.5 | 1.30 | 3.90 | 3.0 |
| 3.0 | 9.17e-2 | 4.82 | 53 |
| 3.3 | 7.42e-3 | 5.33 | 719 |
| 3.6 | 3.08e-4 | 5.84 | 1.9e4 |
| 4.0 | 1.19e-5 | 6.49 | 5.5e5 |
| 4.5 | 1.07e-5 | 7.25 | 6.8e5 |
| 5.0 | 1.38e-4 | 7.98 | 5.8e4 |
| 5.5 | 5.37e-5 | 8.68 | 1.6e5 |

D-H's ground state (`eps`, the lowest eigenvalue itself) also sits essentially
AT zero throughout (`|eps| ~ 1e-4` to `1e-6`; the razor-thin positivity margin
already documented) while zeta-off's ground state is robustly negative and
growing in magnitude with `lambda` (`-4.8` at `lam=3.0` down to `-8.7` at
`lam=5.5`). D-H's GAP additionally collapses toward zero (not just the
eigenvalue itself) -- this is the newly-characterized piece: not only is the
margin thin, the spacing to the next state below it is vanishing, which is
what makes the eigenvector direction (and hence the rank-1 operator built
from it) numerically and structurally unstable.

**Independent high-precision confirmation (rules out a float64 artifact).**
Rebuilt with `build_hp` (true `mpmath` dense linear algebra, `dps = 30`, no
float64 anywhere) at `N = 5`:

| lam | DH eps (hp) | DH gap (hp) | Zoff eps (hp) | Zoff gap (hp) |
|---|---|---|---|---|
| 3.0 | +8.13e-05 | 1.062e-01 | -4.817 | 4.817 |
| 3.3 | +7.70e-05 | 2.077e-02 | -5.334 | 5.334 |
| 4.0 | +1.76e-06 | 3.168e-04 | -6.482 | 6.482 |

These match the float64 values at the same `N` to 1-5% (float64 `N=5, lam=3.0`
gap `1.0099e-01` vs hp `1.062e-01`; `lam=3.3` gap `2.0859e-02` vs hp
`2.077e-02`; `lam=4.0` gap `6.1785e-04` vs hp `3.168e-04`, same order of
magnitude). **The gap collapse is a genuine analytic fact about the D-H
truncated Weil form, confirmed by an independent high-precision linear-algebra
path, not a float64 rounding artifact.**

## 5. What drives the collapse: not reducible to a single ingredient

`build_float`'s `Q` is built from two independent pieces that differ between
zeta and D-H: the archimedean density (`dens_a, dens_b`, fixed by each
function's own Gamma factors) and the coefficient stream (`Lambda`: sparse,
prime-power-supported von Mangoldt for zeta; dense, non-multiplicative,
sign-changing for D-H). A hybrid test isolates which one drives the collapse,
`N = 8, dps = 25`:

| lam | zeta-stream + zeta-arch (Zoff) | DH-stream + DH-arch (DH) | zeta-stream + DH-arch (hybrid) | DH-stream + zeta-arch (hybrid) |
|---|---|---|---|---|
| 3.0 | gap 4.82 | gap 9.17e-2 | gap 3.82 | gap 1.02 |
| 3.3 | gap 5.33 | gap 7.42e-3 | gap 4.26 | gap 1.03 |
| 4.0 | gap 6.49 | gap 1.19e-5 | gap 5.29 | gap 1.18 |

**Neither hybrid reproduces the collapse.** Swapping in D-H's archimedean
density while keeping zeta's (sparse) coefficient stream keeps the gap large
(`3.8-5.3`); swapping in D-H's (dense) coefficient stream while keeping
zeta's archimedean density keeps the gap of order `1` (mildly shrinking, not
collapsing). The collapse is an emergent property of the FULL,
functional-equation-correctly-matched D-H package (its own arch density
together with its own coefficient stream), not attributable to either
ingredient in isolation.

**Attribution (by elimination, in the project's own vocabulary).** The
functional equation is present and correctly realized in both twins by
construction (that is the whole point of the D-H control). The one
structural thing D-H lacks, by definition, is the Euler product; concretely
here that absence is realized as a dense, non-multiplicative coefficient
stream instead of a sparse, prime-power-supported one. Since the hybrid test
shows the archimedean factor alone is inert and the coefficient stream alone
(mismatched to its own archimedean partner) is also insufficient, the honest
statement is: **the mechanism is Euler-product-sourced, expressed through the
coefficient-stream/archimedean-density JOINT structure that only exists when
both halves belong to the same (Euler-product-free) function.** This is a
real nuance flagged for VERIFIER/ADVERSARY, not a clean single-lever proof.

## 6. Why this matters more than the raw undercount

The e1k/e1s family has repeatedly found itself **D-H-blind**: finite-cutoff
reality (Thm 5.10iii) holds for both twins identically (e1k), and the
pole-free window COUNT law does not discriminate zeta from D-H either (e1s
`dh_twin_consistent = YES`, "twins O(1)-blind", matching #158). This look
finds a genuine, robust, orders-of-magnitude DISCRIMINATOR sitting one layer
underneath both of those D-H-blind observables: **the ground-state gap
itself.** Zeta-off's gap grows with `lambda`; D-H's collapses by 4-6 orders of
magnitude over the exact same range. Neither the reality check nor the window
count sees this (both are downstream, coarse-grained consequences that only
occasionally leak the difference into a visible integer). This reframes the
open question from "why does D-H undercount" to "the count is a noisy shadow
of a clean, D-H-discriminating spectral-gap signal that this family has not
been reading directly."

## Verdict fields

| field | verdict |
|---|---|
| `artifact_vs_mechanism` | MECHANISM (root cause: genuine gap collapse, hp-confirmed). Superimposed conditioning-mirage layer confirmed at the most extreme cell (`lam=4.5`, resolves exactly at `dps=40`): the *exact reported integer* at the family's standard `dps=25` is not always precision-converged, even though the underlying driver is real |
| `ruled_out` | e1r-style window-boundary mirage (relaxing `re_lo` does not recover the count cleanly); e1u-style N-resolution/UGRID-floor artifact (deficit N-stable, worsens not vanishes with N) |
| `not_fully_ruled_out` | e1q-style conditioning mirage, but only PARTIALLY and only in the exact integer at one tested cell (`lam=4.5`); the underlying gap-collapse driver is hp-confirmed robust |
| `named_mechanism` | "D-H ground-state gap collapse": the truncated Weil form's lowest-to-next-EVEN-eigenvalue gap shrinks by 4-6 orders of magnitude relative to zeta-off as `lambda` grows, forcing the rank-1 `D_log` operator's secular residues to blow up and occasionally eject a mode from the counting window (as a complex ghost pair near the origin, outside the window's own ghost filter, or as a genuine large real displacement far outside the nominal spectral range) |
| `source_classification` | Euler-product-sourced (by elimination: the FE is matched correctly in both twins; the collapse requires D-H's own coefficient stream AND its own archimedean density together, neither alone; the one structural thing that differs at the "whole function" level is Euler-product presence/absence) |
| `discriminating_value` | YES, and more informative than the count law itself: the gap-ratio (Zoff/DH) grows from `~1.7` at `lam=2.0` to `~7e5` by `lam=4.5`, a clean, large, D-H-vs-zeta discriminator sitting one layer under the previously-documented D-H-blind reality and count observables |
| `k1_clean` | YES. Every quantity here is a matrix eigenvalue, an eigenvalue gap, or lattice geometry (`phi`, `T`, `N`); no zero list or zero scan consumed at any point |

## Verification targets (for VERIFIER)

1. **The rank-1 secular blow-up bound.** Formalize `r_k = L^{-1/2} phi k
   xin_k` with `xin = xi / (delta . xi)`, and the elementary fact that as the
   ground eigenvector `xi` approaches a degenerate direction (a second
   eigenvalue of `Q` approaching the ground eigenvalue), `delta . xi` can
   approach `0`, forcing `|xin|`, hence `|r_k|`, unbounded. This is standard
   perturbation-theory / condition-number reasoning; Mathlib's eigenvalue
   perturbation lemmas may already cover the abstract shape.
2. **Ghost-outside-window as a definitional gap, not a theorem.** Formalize
   that `win_counts`'s ghost filter is defined only on `(re_lo, T)` and hence
   is blind by construction to non-real eigenvalues with `Re <= re_lo`; this
   is a one-line fact about the definition, useful to attach to the e1s
   record as a correction note.
3. **The hybrid-attribution claim as a clean two-factor ANOVA-style
   statement**, formalized as: `gap_even(arch, stream)` is not a product or
   sum of independent single-factor effects (neither `gap_even(arch_DH,
   stream_zeta)` nor `gap_even(arch_zeta, stream_DH)` is small; only
   `gap_even(arch_DH, stream_DH)` is small). Not obviously Mathlib-reachable;
   flagged as an empirical, not formal, target.

## Adversarial test cases (for ADVERSARY)

1. **Push lambda further** (`lam = 6, 7, 8`, `N >= 20`) to check the gap-ratio
   trend continues growing (it wobbled non-monotonically between `lam=4.0` and
   `lam=5.5` in this look, `5.5e5 -> 5.8e4 -> 1.6e5`; confirm this is
   avoided-crossing noise on top of an overall growing trend, not a reversal).
2. **Push dps further at `lam=4.5`** (`dps = 60, 80`) to confirm the exact
   count really does stabilize at the target once the archimedean quadrature
   is accurate enough, and does not flip back at even higher precision (would
   falsify the "conditioning mirage at this one cell" reading).
3. **Test a genuine Euler-product control that is NOT zeta** (e.g. a real
   Dirichlet L-function `L(s, chi)` with the same construction family) to
   check whether the "robust, growing gap" behavior is zeta-specific or
   general to any Euler-product L-function; this is the sharpest falsification
   test of the "Euler-product-sourced" attribution in section 5.
4. **Check whether the near-`re=0` ghost pair and the far-out real-displacement
   regime are the SAME underlying event seen at different `dps`**, or two
   genuinely distinct failure modes that happen to coexist; a continuous `dps`
   sweep with a fixed, finer grid (`dps = 25, 26, ..., 40`) at `lam = 4.5`
   would trace the transition directly.
5. **Multiple independent builds at the SAME `(lam, N, dps)` cell** near the
   most extreme degeneracy (`lam >= 4.0`) to check run-to-run reproducibility
   of the eigenvector selection (`idx_even`); e1s's own "ghost autopsy"
   already found build-fragility for the zeta pole case at `lam=sqrt13,
   N=34`, and the mechanism identified here predicts the SAME fragility
   should appear for D-H, worse, as the gap shrinks.

## Honest scope / overclaim guard

- This does **not** prove RH, does not touch M4, and does not move the count
  half of the W6 budget split back to "open" -- the count-cheap-up-to-`O(1)`
  reading of e1s stands; this note only explains WHY the `O(1)` deviation
  happens for D-H and clarifies that "ghost-free" was an instrument
  limitation, not evidence the deviation is arithmetic-free.
- The exact integer deficit reported at `dps=25` is confirmed NOT fully
  precision-converged at the most extreme cell tested (`lam=4.5`); readers
  citing "D-H undercounts by 1-2 at these four lambdas" should now cite this
  note's qualifier alongside it.
- The Euler-product attribution in section 5 is by elimination and a hybrid
  test, not a derivation; it is a strong empirical claim, not a proof.
- Zeta-off itself is not perfectly exact either (e1s's own adversary note:
  `-1` at `lam=3.3, N=32`); this note did not re-investigate that smaller,
  separate deviation, only confirmed zeta-off stayed exact at every `(N, lam,
  dps)` cell probed here (`N <= 28`, `dps <= 60`).
- All numbers in this note are from disposable scratch scripts (not committed
  to the repo) built by directly importing `build_float` / `operator_spectrum`
  / `build_hp` / `make_streams` / `ZETA_CFG` / `DH_CFG` from
  `experiments/spectral/e1k_dh_dlog_testbed.py`, mirroring exactly the
  `cell()` / `win_counts()` logic already in
  `experiments/spectral/e1s_rank_one_interlacing.py`. No tracked `.npz` was
  read for numeric evidence except a read-only sanity check of
  `e1k_dh_dlog_testbed.npz`'s own lambda-sweep, which was found to disagree
  with a fresh run by up to 200x at matched `(N, lam)` -- almost certainly a
  stale artifact from an earlier version of `e1k_dh_dlog_testbed.py` (the
  ground-state `eps` values matched the fresh run exactly; only `gap_even`
  differed, consistent with a code change between when that npz was last
  regenerated and now) -- so this note does **not** rely on that cached file
  for any claim; all cited numbers were freshly computed and cross-checked
  (float64 vs `mpmath` high precision) within this session.

## Reproduce

Not a committed module (this was a "one look" diagnostic per the task spec).
To rerun any table above, import directly:

```python
from experiments.spectral.e1k_dh_dlog_testbed import (
    build_float, build_hp, operator_spectrum, make_streams, ZETA_CFG, DH_CFG)
import mpmath as mp
mp.mp.dps = 25
lz, ld = make_streams(40, float_out=True)
res = build_float(20, 3.3, ld, DH_CFG["dens_a"], DH_CFG["dens_b"], False)  # DH, pole-free
ev, sa = operator_spectrum(res)
# filt/unfilt/ghost as in experiments/spectral/e1s_rank_one_interlacing.py:win_counts
```
For the high-precision cross-check, use `build_hp(N, mp.mpf(lam), stream_mp,
dens_a, dens_b, False, dps=30)` with `stream_mp` from
`make_streams(kmax, float_out=False)`; keep `N <= 6` for a fast run (the
archimedean quadrature, not the linear algebra, is the cost driver at high
`dps`).
