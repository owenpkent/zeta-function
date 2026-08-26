> Filed 2026-08-26 as regression infrastructure under the #201 closed-bank clause (salvaged from PR #8; LEARNINGS #210): a re-measurement instrument, not a finding; no frame session grading.

# e2bj: the mollifier costume (windowed Li positivity)

**Date**: 2026-08-26. **Status**: EXECUTED, 7/7 full and quick; all four pre-registrations FIRED. **Gallery**: G2 of [`construct_gallery.md`](../../docs/03_research/construct_gallery.md).
**Label (per the #201 derivability check)**: re-measurement of the wall (the uniformity face: #180's margin law, #191's horizon law), new costume. No new coordinate claimed.

## What was built (deliberately wrong)

Li positivity purchased with a Gaussian window: $\lambda_n^\Gamma = \sum_\rho e^{-(\gamma_\rho/\Gamma)^2}\,2\,\mathrm{Re}[1 - (1-1/\rho)^n]$, zeros to $T = 100$, and the tuning $\Gamma^*(N) = $ the largest damping width keeping $\lambda_n^\Gamma \ge 0$ up to horizon $N$ (bisection over the $n$-grid, step 10). Unlike e2bh no zero location is consumed (the window is a legitimate test-function choice); the sin is uniformity, and the run prices it.

## Results

1. **Zeta control is structural.** With $\beta = \tfrac12$ exactly, $|1 - 1/\rho| = 1$, so every on-line zero contributes $2(1-\cos n\varphi) \ge 0$ pointwise: the truncated $\lambda_n$ is nonnegative for ALL $n$ (measured min $1.65$ over the whole grid). Truncation cannot fake negativity for zeta; exactly one genuinely growing mode exists in the D-H list (the $\beta = 0.1915$ member of the landmark pair) and none in zeta's.
2. **The counterexample pays on schedule.** D-H's unmollified $\lambda_n$ first goes negative at the measured $n^* = 80220$ (envelope prediction from $|1-1/\rho|^2 = 1 + (1-2\beta)/|\rho|^2 \approx 1 + 8.4\times10^{-5}$: right order).
3. **Every finite horizon is purchasable.** $\Gamma^*(N)$ exists and decreases: $251.6 / 39.4 / 24.4 / 16.6$ at $N = n^*, 2n^*, 4n^*, 8n^*$.
4. **Every purchase expires.** The last purchased width $\Gamma^*(8n^*) = 16.63$ fails at the measured $n^{**} = 645630$, just $0.6$ percent above its own horizon: the purchased positivity is exactly horizon-deep and no deeper.

## Reading

Positivity-by-mollification buys any finite $n$-range and never all of them: the uniformity clause of M4 in the cheapest instrument in the repo (5 seconds, float64). This is the Li-coordinates face of the same fact #180 measures as the $e^{\gamma_1^2\sigma^2}$ certification price and #191 as the doubly-exponential valley: finite-horizon positivity is cheap, uniform positivity is the theorem. The Beurling control is unposable (no zeros to sum): the counting-side refusal, as in e2bh.

## Prior art and scope correction (filing condition, 2026-08-26)

Arch 3B already owns this axis: [`e3b2_li_dh_extension`](../positivity/e3b2_li_dh_extension.py) established that small-$n$ Li positivity does not distinguish zeta from D-H, and [`e3b3_rigorous`](../positivity/e3b3_rigorous.md) banked the rigorous result $\lambda_n^{\mathrm{DH}} < 0$ at $n = 336{,}000$ with the crossover near $\sim 320{,}000$. This probe's measured $n^* = 80220$ is therefore a $T = 100$ truncation artifact (32 zeros in the sum), NOT the true D-H Li crossover: the truncated sum first goes negative a factor $\sim 4$ below the certified crossover. The meter's value is the $\Gamma^*(N)$ horizon-price ladder, not the location of $n^*$.

## Pre-registrations

- P1 FIRED: truncated zeta $\lambda_n \ge 0$ on the whole grid.
- P2 FIRED: D-H negativity at $n^* \le 4\times10^5$ (measured 80220).
- P3 FIRED: $\Gamma^*(N)$ finite and strictly decreasing along the ladder.
- P4 FIRED: $\Gamma^*(N_{\max})$ fails above $N_{\max}$, below $8N_{\max}$ (measured $645630$ vs $641760$).

## Artifacts

[`e2bj_mollified_li.py`](e2bj_mollified_li.py) (7/7), tracked npz alongside.
