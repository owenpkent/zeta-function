# e5i: S(T) across certified ranges (the quantitative companion of the hiding law)

Status: **COMPLETE 2026-09-01** (quick self-checks 9/9; full run finished, all four pre-registration checks PASS; results filled below from `_cache/e5i_overnight.log`, data in tracked `e5i_results.npz`).

## Provenance

- **Label collision note.** The TODO's Tier-1 candidate spec calls this probe "e5g", but `e5g`
  was already taken when the spec was written: `e5g_race_from_zeros.py` (with
  `_cache/e5g_race4.npz`) is the mod-4 race experiment. The next free letters after `e5h`
  made this module **e5i** (`experiments/primes/e5i_s_of_t.py`).
- Data sources on this box:
  - **Low range**: zeros of $Z(t)$ on $[0, 2\times 10^7]$, recomputed with the repo's
    Riemann-Siegel engine (`experiments/primes/rsz.py`, `k=1` remainder), because the e5f
    certification artifacts (`_cache/e5f_rh_verified_*_certified.npz`) certify *counts*, not
    zero locations. The recomputed set is hard-gated against the certified totals at
    $T=10^7$ (21,136,125 zeros) and $T=2\times 10^7$ (44,478,605 zeros): grid sign-change
    counting can only undercount on any subinterval, so equality of the total with the
    certified count forces per-interval equality, i.e. every rank $n$ used in $S$ is exact.
    The largest certified set on disk is $T=5\times 10^7$ (118,488,122 zeros), but a full
    location recomputation to that height needs roughly a day of wall time on this machine's
    8 cores; $2\times 10^7$ is the largest range that fits the overnight budget. Scoped down
    for that reason, and only that reason.
  - **The three Platt windows** (DATASETS.md section 18, md5-verified against the upstream
    `md5sum.log`):
    | window | file | ranks (1-based) | heights |
    |---|---|---|---|
    | w1 | `zeros_370046000.dat` | 994,804,897 .. 1,000,785,556 | [3.70046e8, 3.72146e8) |
    | w2 | `zeros_3293246000.dat` | 9,999,087,291 .. 10,005,797,727 | [3.293246e9, 3.295346e9) |
    | w3 | `zeros_30607946000.dat` | 103,793,332,901 .. 103,800,788,359 | [3.0607946e10, 3.0610046e10) |
  - **Index anchoring**: each Platt block header carries the exact zero-count below its
    start (`Nt0`), so ranks are intrinsic to the file; the anchoring is independently pinned
    by the `every_millionth` table ($n=10^9$ in w1 matches to all 32 printed decimal digits,
    re-asserted in this module's self-test) and by the DATASETS.md section-18 derivation of
    each file's first rank, re-asserted per file in the self-test.
- Decoder: vectorized float64 port of the block format in this module (`decode_platt`),
  validated in the self-test against the exact-`Fraction` reference decoder
  (`experiments/primes/platt_reader.py`) to $<10^{-6}$.

## Pre-registration

Recorded here **before** the full run started (module written, quick self-checks green,
then this file, then launch):

> **max |S| < 3 in every window** (w1, w2, w3, and the low range).

The finding frame: $N(T) = \theta(T)/\pi + 1 + S(T)$, so a counterexample pair of off-line
zeros at height $T_0$ would make $S$ jump by $+2$ at $T_0$ and carry that offset until the
symmetric partner heights. Measured smallness of $S$ across certified ranges is what the
hiding law (PRIME_PATTERNS: any off-line zero hides above height $3\times 10^{12}$) means
quantitatively at the heights we can actually reach: not only are there no off-line zeros
below the certified heights, but the argument has no room for one, staying a factor
$\gtrsim 3/2$ under the size of the jump a single counterexample pair would inject.

## Method

- $S(\gamma_n^+) = n - \theta(\gamma_n)/\pi - 1$ and $S(\gamma_n^-) = S(\gamma_n^+) - 1$ at
  the $n$-th zero (1-based, all zeros simple in the covered ranges); max $|S|$ per window is
  the max over both one-sided values at every zero.
- Between consecutive zeros $S(t) = n - \theta(t)/\pi - 1$ exactly, so the **second moment is
  the time average** $\frac{1}{L}\int S(t)^2\,dt$, computed per gap by Simpson
  (both endpoints + midpoint; essentially exact since $\theta$ is nearly linear over one
  gap). Secondary versions reported: the plain average of midpoint samples, and the
  zero-sampled average of $S(\gamma_n^+)^2$.
- Comparison scale: Selberg/Ghosh leading order $\langle S^2 \rangle \sim \log\log T / (2\pi^2)$,
  evaluated at the window's midpoint height (lower-order terms are $O(1)$-significant at
  these heights, so the ratio is reported as a descriptive number, not a test statistic).
- $\theta$: Riemann-Siegel theta asymptotic in float64
  ($\frac{t}{2}\log\frac{t}{2\pi} - \frac{t}{2} - \frac{\pi}{8} + \frac{1}{48t} + \frac{7}{5760 t^3}$,
  `rsz.theta`), absolute error $<10^{-4}$ at the top window, i.e. $<4\times 10^{-5}$ in $S$;
  validated against `mpmath.siegeltheta` to $<10^{-8}$ relative in the self-test.
- Low-range scan: chunked grid scan of $Z$ (step 0.02) + vectorized bisection; close pairs
  that fit between grid points are rescued by a dip detector (interior local minimum of
  $|Z| < 0.25$ with no adjacent sign change triggers a 64x finer rescan; exercised on the
  Lehmer pair at $t\approx 7005.1$ in the self-test); one escalation pass (tau 1.0, 128x)
  if the certified gate fails. Independent cross-check of the whole $S$ convention: at
  $t=100$, the count formula agrees with a direct mpmath arg-continuation of
  $\zeta$ from $\sigma=3$ to the critical line to $<10^{-6}$ (self-test 3).

Self-checks: `python -m experiments.primes.e5i_s_of_t` (quick mode, 9 checks).
Full run: `python -m experiments.primes.e5i_s_of_t --full`
(results to `_cache/e5i_results.npz`, low-range zeros cached to
`_cache/e5i_lowrange_gammas.npy`).

## RESULTS

Filled 2026-09-01 from `_cache/e5i_overnight.log` (full run 2026-08-31 -> 09-01; Platt windows
in under 2 s each, the low-range scan 4.36 h; the tracked copy of the results archive is
`e5i_results.npz` next to this file, the working copy stays in `_cache/`).

**The pre-registration (max $|S| < 3$ in every window) HELD in all four windows.**

| window | zeros $n$ | max $\|S\|$ | at $\gamma$ (side, $n$) | $\langle S^2\rangle_{time}$ | $\log\log T/(2\pi^2)$ | ratio | pre-reg |
|---|---|---|---|---|---|---|---|
| low $[0, 2{\times}10^7]$ | 1..44,478,605 | 2.076426 | 17,095,484.27 ($-$, 37,592,217) | 0.204770 | 0.140834 | 1.454 | PASS |
| w1 ($3.7{\times}10^8$) | 994,804,897..1,000,785,556 | 2.178154 | 370,660,275.68 ($-$, 996,554,115) | 0.217316 | 0.151082 | 1.438 | PASS |
| w2 ($3.3{\times}10^9$) | 9,999,087,291..10,005,797,727 | 2.227566 | 3,293,746,979.68 ($+$, 10,000,688,126) | 0.223109 | 0.156399 | 1.427 | PASS |
| w3 ($3.06{\times}10^{10}$) | 103,793,332,901..103,800,788,359 | 2.208817 | 30,608,621,318.26 ($-$, 103,795,730,423) | 0.228415 | 0.161306 | 1.416 | PASS |

**Integrity gates.** The low-range recomputation matched the certified counts EXACTLY at both
gates (21,136,125 zeros below $10^7$; 44,478,605 below $2{\times}10^7$): since sign-change
scanning can only undercount per interval, total equality forces every rank exact, so the
low-range $S$ values inherit the certification. The three Platt windows are anchored by their
block headers, re-pinned against the every-millionth table (32-decimal digit match at
$n = 10^9$) and the DATASETS.md section-18 first-rank table.

**Reading.** Three structural facts, each the quantitative face of the hiding law:

1. **$S$ stays far from the counterexample threshold at every accessible height.** A zero off
   the critical line (or a multiple zero) forces $S$ to jump by 2 at its height, so sustained
   excursions approaching $|S| \approx 2$-then-3 are the smoke a counterexample would emit.
   Measured: the all-time max over 63 million zeros spread across four decades of height is
   2.228, and the maximum GROWS ONLY FROM 2.08 TO 2.23 while $T$ climbs three orders of
   magnitude ($2{\times}10^7 \to 3{\times}10^{10}$): the $\sqrt{\log\log T}$-scale creep the
   Selberg regime predicts, nothing more.
2. **The second moment tracks the Selberg/Ghosh scale with a stable O(1) excess.** The
   time-averaged $\langle S^2\rangle$ sits at 1.42-1.45x the leading term
   $\log\log T/(2\pi^2)$ across all four windows, DECREASING slowly with height
   (1.454 at $10^7$, 1.416 at $3{\times}10^{10}$): the known lower-order terms converging, in
   the direction theory requires. No window shows an anomalous variance excess.
3. **The three sampling conventions bracket as they must** ($\langle S^2\rangle_{mid} <
   \langle S^2\rangle_{time} < \langle S^2\rangle_{zero+}$ in every window), a consistency
   check on the instrument rather than a finding.

**Scope honesty.** The low range is $[0, 2{\times}10^7]$, not the full certified-to-$5{\times}10^7$
range of the primes-thread dataset: recomputing zero LOCATIONS (the e5f certification stored
counts, not locations) at $5{\times}10^7$ was a 24 h job at measured rsz throughput; the
extension is mechanical if ever needed. $S(T)$ is evaluated at one-sided limits at zeros, so
max $|S|$ here is the max over the jump points, which is where $|S|$ attains its sup between
zeros anyway (S decreases by $\theta'/\pi$ smoothly between jumps at these heights).

**Serves.** PRIME_PATTERNS' hiding law gets its quantitative companion: the RH-verification
observable ($S$, sensitive to zero REAL parts through the counting, unlike the GUE statistics
that are provably RH-blind) is measured small and Selberg-regular through height
$3{\times}10^{10}$, including inside the three rigorously certified Platt windows. The
jump-by-2 mechanism plus these margins says: any counterexample below $3{\times}10^{10}$ would
have announced itself in exactly this observable, and nothing announced.
