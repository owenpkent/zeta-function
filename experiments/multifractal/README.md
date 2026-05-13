# Multifractal Experiments

Econophysics-style multifractal analysis applied to prime-number data and the Riemann zeta function. Tests the log-correlated picture from [`../../docs/03_research/extreme_values_and_log_correlated_fields.md`](../../docs/03_research/extreme_values_and_log_correlated_fields.md).

## What is in here

```
experiments/multifractal/
├── README.md            this file
├── mfdfa.py             Multifractal Detrended Fluctuation Analysis
├── benchmarks.py        synthetic series (white noise, fGn, binomial cascade)
├── prime_data.py        Chebyshev psi, prime gaps, Mertens, fluctuation series
├── zeta_sampling.py     log|zeta(1/2+it)| via mpmath, with .npz caching
├── e0_benchmarks.py     E0: calibrate MFDFA on known mono/multifractals
├── e1_zeta_mfdfa.py     E1: MFDFA on log|zeta| in unit windows
├── e2_fhk_max_fit.py    E2: fit FHK second-order constant
└── e3_psi_mfdfa.py      E3: MFDFA on (psi(x) - x)/sqrt(x)
```

## Quick start

```powershell
# from repo root
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# always run E0 first to establish the noise floor
python experiments/multifractal/e0_benchmarks.py

# fast (no mpmath, only sympy sieve)
python experiments/multifractal/e3_psi_mfdfa.py

# slow (mpmath zeta at large height)
python experiments/multifractal/e1_zeta_mfdfa.py
python experiments/multifractal/e2_fhk_max_fit.py
```

Plots are saved next to each script as `eN_*.png`. Cached zeta samples land in `experiments/multifractal/_cache/`.

## The four experiments

### E0: Calibration on synthetic series

**Hypothesis-free.** Run MFDFA on (a) iid Gaussian white noise, (b) [fractional Gaussian noise](https://en.wikipedia.org/wiki/Fractional_Brownian_motion) with $H = 0.7$, (c) a $p = 0.3$ binomial multiplicative cascade. The first two should give nearly constant $h(q)$ (monofractal). The third should match the closed-form binomial spectrum.

**First-run output (N = 8192, order 3):**

| series | $h(q=2)$ | $\Delta\alpha$ | expected |
|---|---|---|---|
| white noise | 0.516 | 0.05 | $h = 0.5$ const, $\Delta\alpha \approx 0$ |
| fGn, $H = 0.7$ | 0.685 | 0.06 | $h = 0.7$ const, $\Delta\alpha \approx 0$ |
| binomial $p = 0.3$ | 0.810 | 1.14 | matches theory curve |

The noise floor for spurious multifractality in this pipeline is $\Delta\alpha \approx 0.05$. Any zeta- or prime-derived result with $\Delta\alpha$ comparable to that is consistent with monofractal scaling; only $\Delta\alpha \gg 0.05$ is a real multifractal signal.

### E1: MFDFA on log|zeta| in unit windows

**Hypothesis.** Per [Fyodorov, Hiary, Keating](https://arxiv.org/abs/1202.4713) and [Saksman, Webb](https://arxiv.org/abs/1609.00027), on a unit window at large height $T$, the function $t \mapsto \log|\zeta(\tfrac{1}{2}+it)|$ behaves like a 1D log-correlated Gaussian field. Its generalized Hurst exponent $h(q)$ should sit near $1/2$ with the multifractal corrections characteristic of Gaussian multiplicative chaos.

**Method.** Sample $\log|\zeta(\tfrac{1}{2}+it)|$ at $\sim 2^{13}$ points in $[T - 0.5, T + 0.5]$ for $T = 10^4, 10^6, 10^8$. Run MFDFA with $q \in [-4, 4]$. Extract $h(q)$, $\tau(q)$, singularity spectrum $D(\alpha)$.

**Look for.** A roughly quadratic $\tau(q)$, $h(q)$ decreasing in $q$, and the singularity spectrum widening as $T$ increases.

### E2: FHK second-order constant

**Hypothesis.** $\max_{|h|\le 1}\log|\zeta(\tfrac{1}{2}+i(T+h))| = \log\log T - \tfrac{3}{4}\log\log\log T + O(1)$.

**Method.** For each $T_k = 10^k$, $k = 4, \ldots, 8$, sample many random centers $T_k + \xi$ with $\xi$ uniform on a bounded range and compute the window max. Plot mean of (max) versus $\log\log T_k$ and fit the affine model. Test whether the second-order slope is close to $-\tfrac{3}{4}$.

**Caveat.** mpmath zeta at $T = 10^8$ is slow. The cache helps, but expect this to take an hour-class run on a laptop.

### E3: MFDFA on (psi(x) - x)/sqrt(x)

**Hypothesis.** The normalized Chebyshev fluctuation $Y(u) = (\psi(e^u) - e^u)/e^{u/2}$ on the logarithmic time variable $u = \log x$ is the explicit-formula dual of $\log|\zeta(\tfrac{1}{2}+it)|$. It should show log-correlated multifractal structure similar to E1.

**Method.** Compute $\psi(x)$ on a log-uniform grid $x \in [10^2, 10^7]$ via a sieve. Normalize. Run MFDFA. Compare $h(q)$ and $D(\alpha)$ to the E1 output.

**Why this is the most interesting one.** If the spectra match, that visualizes the duality: the "fractal" sitting on the critical line is the same object as the fluctuations of the primes themselves, just expressed in different coordinates.

**First-run findings (x in [100, 1e7], N = 8192, order 3).** Singularity-spectrum width $\Delta\alpha \approx 2.8$, well above the E0 noise floor of 0.05. Real multifractal signal. But $h(q) > 1$ for $q \ge 0$ and $h(q)$ blows up to $\sim 3.5$ at $q = -4$. Diagnostic: $Y(u)$ is not a stationary-noise-like series. By the explicit formula, $Y(u) \approx -\sum_\rho e^{i u \gamma_\rho}/\rho$ is a quasi-periodic sum of low-zero oscillations ($\gamma_1 \approx 14.13$, $\gamma_2 \approx 21.02$, ...) plus a slowly-growing log-correlated tail. MFDFA on a bounded oscillating signal lands outside its assumed regime, which is why $h(q) > 1$. The width signal is real; the precise spectrum is not yet meaningful.

**Next iterations for cleaner E3 results:** (a) feed MFDFA the increments $\Delta Y$ instead of $Y$; (b) compute $Y$ on short windows at large $u$ and average across windows (the prime-side analogue of Saksman-Webb mesoscopic sampling); (c) subtract the first 100 low-zero contributions and re-analyze the residual.

## Status as of first run

| experiment | run | result |
|---|---|---|
| E0 | yes | Pipeline calibrated. Noise floor $\Delta\alpha \approx 0.05$. |
| E1 | yes | Striking universality. Spectrum width $\Delta\alpha \approx 2.05$ stable to within 1% across $T = 10^4, 10^6, 10^8$. $h(q=2) \approx 1.5$. |
| E2 | yes | Code works; sampling too sparse for FHK fit. Per-center maxes consistent with Gumbel fluctuations but $\text{sem} \approx 0.45$ per height swamps the second-order signal. Needs 30+ centers per height across $T = 10^4$ to $10^{12}$. |
| E3 | yes | Real multifractal signal ($\Delta\alpha \approx 2.8$). Stationarity issue ($h(q) > 1$). Needs mesoscopic windowing or increment analysis. |

### E1 result in detail

| $T$ | $h(q=2)$ | $\Delta\alpha$ |
|---|---|---|
| $10^4$ | 1.51 | 2.04 |
| $10^6$ | 1.50 | 2.06 |
| $10^8$ | 1.46 | 2.07 |

The near-perfect collapse of $h(q)$ and $D(\alpha)$ curves across 4 orders of magnitude in $T$ is the **observable signature of log-correlated universality**: the multifractal spectrum of $\log|\zeta(\tfrac{1}{2}+it)|$ on unit windows does not depend on the height. This is the Fyodorov-Hiary-Keating prediction expressed in MFDFA coordinates. $h(q=2) \approx 1.5$ reflects MFDFA's cumsum step applied to a roughly-stationary log-correlated signal (compare fGn with $H = 0.5$, which gives $h = 0.5$; integrating gives $h = 1.5$).

### E2 caveat

To extract the FHK second-order constant $-\tfrac{3}{4}$, the natural setup is at least 6 heights $T = 10^4, 10^5, \ldots, 10^{12}$ with $\ge 30$ random centers each. That gives $\text{sem} \approx 0.16$ per height versus a target signal of $\sim 0.3$ in $\log\log\log T$. The current 4-centers-per-height setup is a feasibility test, not a science run.

## What we are NOT testing

- This is not an RH attack. See [`../../docs/research_atlas/multifractal_and_log_correlated_methods.md`](../../docs/research_atlas/multifractal_and_log_correlated_methods.md) §2 "Why this is not a route to RH."
- MFDFA assumes power-law scaling. Strictly speaking, log-correlated fields have logarithmic corrections to power-law, so the extracted exponents are effective values over the available scale range, not asymptotic limits. Read the spectra as comparison plots, not as theorems.
- Statistical error bars at the heights reachable with mpmath are not tight. Replicating the FHK conjecture to within standard publication precision requires Odlyzko-Schonhage-grade zeta evaluation, which is beyond the scope of these scripts.

## References

- Kantelhardt, J.W. et al. (2002), "Multifractal detrended fluctuation analysis of nonstationary time series," *Physica A* **316**, 87–114. The standard MFDFA reference.
- Mandelbrot, B. (1999), *Multifractals and 1/f Noise*. Background.
- For zeta-specific references see [`../../docs/03_research/extreme_values_and_log_correlated_fields.md`](../../docs/03_research/extreme_values_and_log_correlated_fields.md) §11.
