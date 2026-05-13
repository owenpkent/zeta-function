# Log-Correlated Fields and the Critical Line

> **Level:** Graduate. Assumes [complex analysis](https://en.wikipedia.org/wiki/Complex_analysis), basic [probability theory](https://en.wikipedia.org/wiki/Probability_theory), and [Gaussian process](https://en.wikipedia.org/wiki/Gaussian_process) language ([covariance](https://en.wikipedia.org/wiki/Covariance_function), centered Gaussian fields). No prior random matrix theory required.

This is a soft entry point. For the research-level statements with full references and status, see [`../03_research/extreme_values_and_log_correlated_fields.md`](../03_research/extreme_values_and_log_correlated_fields.md).

---

## 1. What Is a Log-Correlated Gaussian Field?

A centered Gaussian field $X = \{X(t) : t \in D\}$ on a domain $D \subset \mathbb{R}^d$ is **log-correlated** if its covariance has the form

$$\mathbb{E}[X(t_1) X(t_2)] = -\log|t_1 - t_2| + g(t_1, t_2),$$

where $g$ is bounded and continuous on $D \times D$. The pointwise variance diverges as $t_1 \to t_2$, so $X$ is **not** a function in the classical sense. It is a [random distribution](https://en.wikipedia.org/wiki/Generalized_function) (Schwartz distribution), or equivalently a Gaussian field that only makes rigorous sense after a smoothing or regularization.

The canonical 2D example is the [Gaussian free field](https://en.wikipedia.org/wiki/Gaussian_free_field) (GFF) on a planar domain. The canonical 1D example is the restriction of a 2D GFF to a curve, or the trace of the [branching random walk](https://en.wikipedia.org/wiki/Branching_random_walk) at its boundary.

**Key features:**

- The variance over a region of diameter $\varepsilon$ grows like $\log(1/\varepsilon)$.
- The maximum over a unit region of a regularization at scale $\varepsilon$ grows like $\log(1/\varepsilon)$ (logarithmic, not square-root: this is the signature of a log-correlated field).
- The exponential $e^{q X}$ defines, after proper normalization, the [Gaussian multiplicative chaos](https://en.wikipedia.org/wiki/Liouville_quantum_gravity#Gaussian_multiplicative_chaos) random measure, which has a phase transition (the **freezing transition**) at a critical $q_c$.

---

## 2. Why Zeta Should Be Log-Correlated on Short Intervals

Here is the intuition, in three steps.

**Step 1: Variance from Selberg's CLT.** Selberg proved that for $t$ sampled uniformly in $[T, 2T]$,

$$\frac{\log|\zeta(\tfrac{1}{2}+it)|}{\sqrt{\tfrac{1}{2} \log\log T}} \xrightarrow{\,d\,} \mathcal{N}(0,1).$$

So $\mathrm{Var}\, \log|\zeta(\tfrac{1}{2}+it)| \approx \tfrac{1}{2} \log\log T$. The $\log\log$ growth is exactly what a log-correlated field exhibits when the "ultraviolet cutoff" sits at the smallest natural scale. For zeta, that smallest scale is the typical zero spacing $\sim 1/\log T$, so the effective range of scales is $\log T$, and the log of that is $\log\log T$.

**Step 2: Covariance from random matrix theory.** The [characteristic polynomial](https://en.wikipedia.org/wiki/Characteristic_polynomial) $p_N(\theta) = \det(I - U e^{-i\theta})$ of a Haar-random $N \times N$ unitary matrix $U$ has

$$\mathrm{Cov}\big(\log|p_N(\theta_1)|, \log|p_N(\theta_2)|\big) = -\tfrac{1}{2} \log|2\sin\tfrac{\theta_1 - \theta_2}{2}| + O(1).$$

This is the log-correlated covariance on the unit circle.

**Step 3: Match the scales.** Local zero density of zeta at height $T$ is $\tfrac{1}{2\pi}\log T$, matching CUE size $N \sim \log T$. Under that identification, the random-matrix covariance translates into

$$\mathrm{Cov}\big(\log|\zeta(\tfrac{1}{2}+i(t+h_1))|, \log|\zeta(\tfrac{1}{2}+i(t+h_2))|\big) \approx \log \min\!\left(\frac{1}{|h_1 - h_2|}, \log T\right).$$

This is a 1D log-correlated field with ultraviolet cutoff at the typical zero spacing $1/\log T$. The diagonal value $\log \log T$ recovers Selberg's variance.

**Caveat.** This is a heuristic. The first quantitatively rigorous statement of the form "zeta is a Gaussian multiplicative chaos" is the [Saksman–Webb theorem](https://arxiv.org/abs/1609.00027) (2020), which establishes a genuine coupling on mesoscopic scales (window width $\delta_T \to 0$ slowly with $T$).

---

## 3. Why the Maximum Should Be $\sim \log\log T$

For a log-correlated field on a unit window with variance $\log\log T$ at the smallest scale, the typical maximum is

$$\max_{|h|\le 1} X(t+h) \approx \log\log T,$$

not $\sqrt{\log\log T \cdot \log(\text{number of independent points})}$ as it would be for an [iid Gaussian](https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables) sample. The factor of $\sqrt{\log\log T}$ is "lost" because the field's strong long-range correlation forces high points to cluster instead of competing independently.

The heuristic is the same as for the maximum of [branching random walk](https://en.wikipedia.org/wiki/Branching_random_walk), the maximum of the 2D Gaussian free field on a lattice, or the maximum of the [REM](https://en.wikipedia.org/wiki/Random_energy_model) at the right temperature. All of these freeze at the same scale, which Derrida named the **freezing transition** in the 1980s.

Carried over to zeta, this is the leading prediction of the **Fyodorov–Hiary–Keating conjecture**:

$$\max_{|h| \le 1} \log|\zeta(\tfrac{1}{2}+i(t+h))| = \log\log T - \tfrac{3}{4}\log\log\log T + O(1).$$

- The leading $\log\log T$ is the freezing prediction.
- The $-\tfrac{3}{4}\log\log\log T$ is the 1D-log-correlated second-order correction. (For iid, it would be $-\tfrac{1}{4}$; for 2D log-correlated, $-\tfrac{3}{2}$. The $\tfrac{3}{4}$ is exactly the 1D value.)
- The $O(1)$ remainder is conjectured to converge in distribution to a randomly shifted [Gumbel distribution](https://en.wikipedia.org/wiki/Gumbel_distribution).

The first two are now theorems (unconditional). The third is open. See [`../03_research/extreme_values_and_log_correlated_fields.md`](../03_research/extreme_values_and_log_correlated_fields.md) §5 for the status table.

---

## 4. Worked Comparison

Three Gaussian "maxima over a unit region of size with $N$ scales of structure":

| Model | $\mathrm{Var}$ at finest scale | Typical $\max$ | Second-order correction |
|---|---|---|---|
| $N$ iid $\mathcal{N}(0, \log N)$ | $\log N$ | $\log N$ | $-\tfrac{1}{4}\log\log N$ (Bramson–Cox) |
| 1D log-correlated (interval) | $\log N$ | $\log N$ | $-\tfrac{3}{4}\log\log N$ |
| 2D log-correlated (square) | $\log N$ | $2 \log N / \sqrt{d}$ rescaled to $\log N$ | $-\tfrac{3}{2}\log\log N$ |
| $\log|\zeta(\tfrac{1}{2}+i(t+h))|$, $|h|\le 1$ at height $T$, $N = \log T$ | $\log\log T$ | $\log\log T$ | $-\tfrac{3}{4}\log\log\log T$ |

The zeta line matches the 1D log-correlated line exactly. That match is the empirical content of the FHK conjecture.

---

## 5. The Primes-Zeros Duality

Two dual Fourier-like expansions sit at the heart of zeta:

$$\log|\zeta(\tfrac{1}{2}+it)| \;\approx\; \sum_p \frac{\cos(t \log p)}{\sqrt{p}}, \qquad \frac{\psi(e^u) - e^u}{e^{u/2}} \;\approx\; -\sum_\rho \frac{e^{i u \gamma_\rho}}{\rho}.$$

The first comes from the [Euler product](https://en.wikipedia.org/wiki/Euler_product) and writes $\log|\zeta|$ on the critical line as a sum over **primes**, with frequencies $\log p$ and amplitudes $1/\sqrt{p}$. The second is the Riemann [explicit formula](https://en.wikipedia.org/wiki/Explicit_formulae_for_L-functions) and writes the normalized prime fluctuation as a sum over **zeros** $\rho = \tfrac{1}{2} + i\gamma_\rho$, with frequencies $\gamma_\rho$ and amplitudes $1/|\rho|$.

So primes appear as frequencies on one side, zeros as frequencies on the other. Both expansions are spectral representations of $\zeta(s)$. The duality is real but mediated through $\zeta$: it is not the case that primes and zeros are "two coordinates on the same object." The unifying object is $\zeta$ itself; primes determine $\zeta$ via the Euler product, and zeros are properties of the resulting analytic function.

Both expansions converge only distributionally and need smoothing for rigorous statements. The log-correlated behavior we have been discussing emerges from the *interference pattern* of the prime cosines in the first sum, and equivalently from the interference of the zero exponentials in the second.

---

## 6. What This Has to Do With the Riemann Hypothesis

The duality from §5 holds **whether or not RH is true**. RH is a separate statement about *where* the zero frequencies sit. Four levels of connection:

**Level 1 (unconditional, proven 1896).** No zeros on $\mathrm{Re}(s) = 1$ is equivalent to the [Prime Number Theorem](https://en.wikipedia.org/wiki/Prime_number_theorem): $\pi(x) \sim x/\log x$. The leading $1/\log x$ density of primes does not need RH.

**Level 2 (this is RH).** Each zero $\rho = \beta + i\gamma$ contributes a fluctuation of size $x^\beta/|\rho|$ to $\psi(x) - x$. A zero with $\beta > 1/2$ dominates $\sqrt{x}$ at large $x$. So:

$$\text{RH} \;\iff\; |\psi(x) - x| = O\!\big(\sqrt{x}\,\log^2 x\big) \;\iff\; \text{every zero-frequency mode decays at exactly the rate } \sqrt{x}.$$

In Fourier-dual language: RH is the statement that the zero side of $\zeta$ is **one-dimensional**, all amplitudes decaying at the same rate. This is what forces the prime-side fluctuations to be as small as they could possibly be.

**Level 3 (mostly unconditional, where the multifractal lives).** Selberg's CLT, the $\tfrac{1}{2}\log\log T$ variance, the universality across heights observed in our [E1 experiment](../../experiments/multifractal/README.md), the Saksman-Webb GMC coupling: theorems, mostly without needing RH. Sharper statements ([Keating-Snaith](https://en.wikipedia.org/wiki/Keating%E2%80%93Snaith_conjecture) moments, the FHK constant $-\tfrac{3}{4}$) are conjectures compatible with both RH and non-RH worlds. The multifractal structure on the critical line is a **downstream consequence**, not an RH-equivalent: it would still exist if some zero were off the line, with localized perturbations near its height.

**Level 4 (RH again, structural form).** [Weil's reformulation](https://en.wikipedia.org/wiki/Weil%27s_explicit_formula): RH is equivalent to a quadratic form on Schwartz functions being positive semi-definite. [Li's criterion](https://en.wikipedia.org/wiki/Li%27s_criterion): RH is equivalent to an infinite sequence of real numbers being positive. So RH is fundamentally a **positivity** statement, not a spectral one. The multifractal/log-correlated picture gives access to *size* and *oscillation* but does not naturally produce positivity. That is why the spectral approaches cannot close the gap.

**Bottom line.** The log-correlated machinery is on the right side of the duality (the zero side, viewed from the critical line) and is consistent with RH, but cannot test it. Distinguishing a world with RH from a world where some zero has $\beta = 0.51$ would require uniform-in-$t$ estimates that current multifractal tools do not provide. This is the atlas's *bridge gap* (§3.5) and *exactness gap* (§3.3).

---

## 7. Where to Go From Here

| To learn... | Read... |
|---|---|
| The precise statements and status table | [`../03_research/extreme_values_and_log_correlated_fields.md`](../03_research/extreme_values_and_log_correlated_fields.md) |
| The strategic landscape and why this is not an RH attack | [`../research_atlas/multifractal_and_log_correlated_methods.md`](../research_atlas/multifractal_and_log_correlated_methods.md) |
| Selberg's CLT in context | [`./README.md`](./README.md), [`../03_research/README.md`](../03_research/README.md) §8 |
| The Keating–Snaith moment conjecture | [`../03_research/README.md`](../03_research/README.md) §8 |
| The maximum of zeta program (Soundararajan, Harper) | [`../03_research/README.md`](../03_research/README.md) §9 |
| Random matrix theory and zero statistics | [`../research_atlas/README.md`](../research_atlas/README.md) §2.3 |

**Outside this repo:**

- Harper, "The Riemann zeta function in short intervals," *Seminaire Bourbaki* (2019), [arXiv:1904.08204](https://arxiv.org/abs/1904.08204). Best survey.
- Rhodes, Vargas, "Gaussian multiplicative chaos and applications: a review," *Probability Surveys* **11** (2014), 315–392.
- Bovier, A., *Gaussian Processes on Trees: From Spin Glasses to Branching Brownian Motion*, Cambridge, 2017. Background on freezing transitions.
