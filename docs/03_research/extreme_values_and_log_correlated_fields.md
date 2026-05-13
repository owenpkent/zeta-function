# Extreme Values, Log-Correlated Fields, and the Riemann Zeta Function

> **Level:** Research. Assumes [Selberg's central limit theorem](https://en.wikipedia.org/wiki/Riemann_zeta_function#Statistics), familiarity with [Gaussian processes](https://en.wikipedia.org/wiki/Gaussian_process), and the [Gaussian Unitary Ensemble](https://en.wikipedia.org/wiki/Gaussian_unitary_ensemble) (GUE) connection. For a softer entry point, see [`../02_graduate/log_correlated_fields_intro.md`](../02_graduate/log_correlated_fields_intro.md). For the catalog framing, see [`../research_atlas/multifractal_and_log_correlated_methods.md`](../research_atlas/multifractal_and_log_correlated_methods.md).

---

## 1. The Object of Study

Fix a height $T$ that is large and a unit window $[T, T+1]$ on the critical line. We are interested in:

1. The pointwise size of $\log|\zeta(\tfrac{1}{2}+it)|$ for $t$ in the window.
2. The integrated moments $\int_0^1 |\zeta(\tfrac{1}{2} + i(T+h))|^{2q}\, dh$ for $q > 0$.
3. The maximum $\max_{|h| \le 1} \log|\zeta(\tfrac{1}{2} + i(T+h))|$.

When $T$ is sampled uniformly in $[T_0, 2 T_0]$ for large $T_0$, all three become random variables. The unifying claim is that $t \mapsto \log|\zeta(\tfrac{1}{2}+it)|$ on such windows behaves like a one-dimensional [log-correlated Gaussian field](https://en.wikipedia.org/wiki/Gaussian_free_field), at leading order. Everything in this document is a consequence, a refinement, or a probabilistic interpretation of that single claim.

This is one of the few places where heuristics from [random matrix theory](https://en.wikipedia.org/wiki/Random_matrix), [Gaussian multiplicative chaos](https://en.wikipedia.org/wiki/Gaussian_free_field#Gaussian_multiplicative_chaos), and [spin glass](https://en.wikipedia.org/wiki/Spin_glass) physics have been converted into theorems about zeta itself.

---

## 2. Selberg's Central Limit Theorem

**Theorem ([Selberg](https://en.wikipedia.org/wiki/Atle_Selberg), 1946; modern proof Radziwill–Soundararajan 2017).** As $T \to \infty$, for $t$ sampled uniformly in $[T, 2T]$,

$$\frac{\log|\zeta(\tfrac{1}{2}+it)|}{\sqrt{\tfrac{1}{2} \log\log T}} \;\xrightarrow{\,d\,}\; \mathcal{N}(0, 1).$$

The variance $\tfrac{1}{2} \log\log T$ is the characteristic signature of a log-correlated field. It is unconditional: it needs neither the [Riemann Hypothesis](https://en.wikipedia.org/wiki/Riemann_hypothesis) nor the [GUE conjecture](https://en.wikipedia.org/wiki/Hilbert%E2%80%93P%C3%B3lya_conjecture#Possible_connection_with_quantum_mechanics). The same statement holds for $\arg \zeta(\tfrac{1}{2}+it)$ with variance $\tfrac{1}{2\pi^2}\log\log T$ (this is essentially Selberg's bound on [$S(T)$](https://en.wikipedia.org/wiki/Riemann_zeta_function#Functional_equation)).

Reference: Radziwill, Soundararajan, "Selberg's central limit theorem for $\log|\zeta(\tfrac{1}{2}+it)|$," *L'Enseignement Mathematique* (2017), [arXiv:1509.06827](https://arxiv.org/abs/1509.06827).

---

## 3. The Log-Correlated Covariance Heuristic

Random matrix calculations for the characteristic polynomial $p_N(\theta) = \det(I - U e^{-i\theta})$ of a [CUE](https://en.wikipedia.org/wiki/Random_matrix#Gaussian_ensembles) Haar-distributed matrix $U \in U(N)$ give

$$\mathrm{Cov}\big(\log|p_N(\theta_1)|, \log|p_N(\theta_2)|\big) = -\tfrac{1}{2}\log|2\sin(\tfrac{\theta_1 - \theta_2}{2})| + O(1).$$

This is the covariance of a log-correlated Gaussian field on the unit circle. Matching the random matrix size $N$ to the local zero density of $\zeta$ at height $T$ gives $N \sim \log T$ and the heuristic prediction

$$\mathrm{Cov}\big(\log|\zeta(\tfrac{1}{2}+i(t+h_1))|,\; \log|\zeta(\tfrac{1}{2}+i(t+h_2))|\big) \;\approx\; \log \min\!\left(\frac{1}{|h_1 - h_2|},\; \log T\right)$$

for $t$ uniform in $[T, 2T]$ and $|h_1 - h_2| \le 1$. The variance is recovered at the diagonal ($h_1 = h_2$): it equals $\log\log T$, half the variance in Selberg's CLT because $\log|\zeta|$ is the real part of $\log \zeta$.

This is a **heuristic**. The Saksman–Webb theorem (section 6) makes it rigorous on mesoscopic scales.

---

## 4. The Fyodorov–Hiary–Keating Conjecture

[Yan Fyodorov](https://en.wikipedia.org/wiki/Yan_V._Fyodorov), [Ghaith Hiary](https://en.wikipedia.org/wiki/Ghaith_Hiary), and [Jon Keating](https://en.wikipedia.org/wiki/Jon_Keating) imported the freezing-transition machinery from [spin glass](https://en.wikipedia.org/wiki/Spin_glass) physics and the theory of [branching random walks](https://en.wikipedia.org/wiki/Branching_random_walk) into the zeta setting.

**Conjecture (Fyodorov–Hiary–Keating 2012, Fyodorov–Keating 2014).** For $t$ sampled uniformly in $[T, 2T]$,

$$\max_{|h| \le 1} \log|\zeta(\tfrac{1}{2} + i(t+h))| \;=\; \log\log T \;-\; \tfrac{3}{4}\log\log\log T \;+\; M_T,$$

where $M_T$ converges in distribution to a randomly shifted [Gumbel distribution](https://en.wikipedia.org/wiki/Gumbel_distribution) (specifically, $M_T \to \mathcal{G} + \log \mathcal{Z}$ where $\mathcal{G}$ is Gumbel and $\mathcal{Z}$ is a positive random variable with explicit law from the derivative martingale of the limiting [Gaussian multiplicative chaos](https://en.wikipedia.org/wiki/Liouville_quantum_gravity#Gaussian_multiplicative_chaos)).

The leading $\log\log T$ is the prediction of "tree" or branching analogy; the $-\tfrac{3}{4}\log\log\log T$ correction is the signature of one-dimensional log-correlated extrema (it would be $-\tfrac{1}{4}\log\log T$ for an iid field and $-\tfrac{3}{2}\log\log T$ for a 2D log-correlated field; the $-\tfrac{3}{4}$ is exactly the 1D log-correlated value).

References:
- Fyodorov, Hiary, Keating, "Freezing transition, characteristic polynomials of random matrices, and the Riemann zeta-function," *Phys. Rev. Lett.* **108** (2012), 170601, [arXiv:1202.4713](https://arxiv.org/abs/1202.4713).
- Fyodorov, Keating, "Freezing transitions and extreme values: random matrix theory, $\zeta(\tfrac{1}{2}+it)$, and disordered landscapes," *Phil. Trans. R. Soc. A* **372** (2014), [arXiv:1211.6063](https://arxiv.org/abs/1211.6063).

---

## 5. Status Table

| Result | Author(s) | Year | Reference | Status |
|---|---|---|---|---|
| Selberg CLT for $\log|\zeta(\tfrac{1}{2}+it)|$ | Selberg | 1946 | (Selberg's collected works) | Theorem |
| Modern proof of Selberg CLT | Radziwill, Soundararajan | 2017 | [arXiv:1509.06827](https://arxiv.org/abs/1509.06827) | Theorem |
| Leading order $\log\log T$ for FHK maximum, conditional on RH | Najnudel | 2018 | [arXiv:1611.05562](https://arxiv.org/abs/1611.05562) | Theorem (under RH) |
| Leading order $\log\log T$, unconditional | Arguin, Belius, Bourgade, Radziwill, Soundararajan | 2019 | [arXiv:1612.08575](https://arxiv.org/abs/1612.08575) | Theorem |
| Tightness with the correct $-\tfrac{3}{4}\log\log\log T$ subtraction (FHK I) | Arguin, Bourgade, Radziwill | 2020 | [arXiv:2007.00988](https://arxiv.org/abs/2007.00988) | Theorem |
| Right-tail asymptotic $y e^{-2y}$ and refined tightness (FHK II) | Arguin, Bourgade, Radziwill | 2023 | [arXiv:2307.00982](https://arxiv.org/abs/2307.00982) | Theorem |
| Convergence in distribution of $M_T$ to randomly shifted Gumbel | (all) | open | --- | Conjecture |
| GMC convergence on mesoscopic scales | Saksman, Webb | 2020 | [arXiv:1609.00027](https://arxiv.org/abs/1609.00027) | Theorem |

The FHK conjecture is now a near-theorem in the sense that two of its three quantitative ingredients (leading order, second order with tightness) have been proved unconditionally. The final ingredient (convergence in distribution of $M_T$) remains open.

---

## 6. Saksman–Webb: Zeta as Gaussian Multiplicative Chaos

The strongest rigorous bridge between zeta and the log-correlated picture is a coupling, not just a statistics match.

**Theorem (Saksman–Webb 2020).** Let $\omega$ be uniform in $[T, 2T]$ and let $\delta_T \to 0$ slowly with $T$. Define the random analytic function

$$Z_T(z) = \zeta\big(\tfrac{1}{2} + i(\omega + \delta_T z)\big), \qquad z \in \mathbb{C}.$$

Then $Z_T$ converges in distribution (in a suitable function space) to an explicit limit of the form $A(z)\,e^{X(z)}$, where $A(z)$ is a deterministic smooth factor and $e^{X(z)}$ is a complex [Gaussian multiplicative chaos](https://en.wikipedia.org/wiki/Liouville_quantum_gravity#Gaussian_multiplicative_chaos) built from a log-correlated complex Gaussian field $X$.

This says zeta, on the right mesoscopic scale, **is** a GMC, not merely a function whose statistics resemble one. The freezing transition predictions, the moment scalings, and the multifractal singularity spectrum of $|\zeta(\tfrac{1}{2}+it)|^{2q}$ on such scales then follow from known GMC theory.

Reference: Saksman, Webb, "The Riemann zeta function and Gaussian multiplicative chaos: Statistics on the critical line," *Ann. Probab.* **48** (2020), 2680–2754, [arXiv:1609.00027](https://arxiv.org/abs/1609.00027).

---

## 7. $S(T)$ and the Mesoscopic Landscape of Zeros

Define $S(T) = \tfrac{1}{\pi} \arg \zeta(\tfrac{1}{2} + iT)$, the fluctuation of the [zero-counting function](https://en.wikipedia.org/wiki/Riemann%E2%80%93von_Mangoldt_formula) about its smooth main term. Two distinct kinds of "multifractal" or scaling structure live here, and they are easy to confuse.

**Pointwise regularity of $T \mapsto S(T)$.** Between zeros, $S$ is real-analytic. At each simple zero, $S$ jumps by $+1$ (Riemann–von Mangoldt formula combined with the [argument principle](https://en.wikipedia.org/wiki/Argument_principle)). The [Holder spectrum](https://en.wikipedia.org/wiki/H%C3%B6lder_condition) is therefore degenerate: exponent $+\infty$ on the complement of the zero set, exponent $0$ on the zero set. This contains zero information beyond the location of zeros.

**Distributional structure under random shifts.** For $T$ sampled in $[T_0, 2T_0]$ and mesoscopic scales $\delta_T \to 0$, the increment process $S(T + \delta_T h) - S(T)$ converges to a log-correlated Gaussian process. This is implicit in Bourgade's work on the microscopic landscape of zeros (Bourgade, *Mesoscopic fluctuations of the zeta zeros*, [arXiv:1504.05456](https://arxiv.org/abs/1504.05456), *Probab. Theory Relat. Fields* (2010); see also Bourgade and collaborators on universality for $\beta$-ensembles). The "multifractal spectrum" of $S(T)$ in this sense is just the imaginary-part version of the log-correlated structure of $\log \zeta$.

Selberg's CLT for $S(T)$ with variance $\tfrac{1}{2\pi^2} \log\log T$ is the macroscopic shadow of this. [Montgomery's pair correlation conjecture](https://en.wikipedia.org/wiki/Montgomery%27s_pair_correlation_conjecture) (1973) and the Rudnick–Sarnak $n$-point correlations (1996) constrain the microscopic ($\sim 1/\log T$) scale and are compatible with, but logically distinct from, the mesoscopic log-correlated picture.

**Takeaway.** $S(T)$ does not contribute an independent "multifractal dimension." The variational structure is the same one from sections 3 and 4, applied to $\mathrm{Im}\, \log \zeta$ instead of $\mathrm{Re}\, \log \zeta$.

---

## 8. Moments and the Multifractal Spectrum

For a log-correlated field $X$ with variance $\sigma^2 = \log T$, the partition function $Z_q = \int e^{q X(t)}\, dt$ over a unit window obeys

$$\mathbb{E}[Z_q] \sim (\log T)^{q^2}$$

for $|q|$ subcritical, with a freezing transition at $q_c = 1$ (for unit-window 1D log-correlated fields with the FHK normalization). The corresponding [Frisch–Parisi](https://en.wikipedia.org/wiki/Multifractal_system) singularity spectrum $D(\alpha)$ is the standard truncated quadratic of GMC theory.

For zeta, the analogue is

$$\int_0^1 \big|\zeta(\tfrac{1}{2} + i(T+h))\big|^{2q}\, dh \;\approx\; (\log T)^{q^2}$$

in the subcritical regime. This is the unit-window cousin of the [Keating–Snaith moment conjecture](https://en.wikipedia.org/wiki/Riemann_zeta_function#Moments_of_the_zeta_function) (which is the analogous statement integrated over a macroscopic $[0, T]$ window, with scaling $(\log T)^{k^2}$ matching after the relevant rescaling). For the random zeta model and for the rigorous Saksman–Webb regime, this prediction is correct. For zeta itself in a fixed unit window, partial moment bounds matching the prediction have been established by Arguin–Ouimet–Radziwill ([arXiv:1906.05098](https://arxiv.org/abs/1906.05098)) and follow-up work.

The supercritical regime ($q > q_c$) is dominated by atypical high points and freezes. This is the regime that controls the FHK maximum.

---

## 9. What This Says About RH, and What It Does Not

**What it does NOT say.** A multifractal estimate on moments is essentially a sharper upper bound on $\int|\zeta|^{2q}$. Such bounds are *consequences* of RH, not equivalents. Even the full [Lindelof Hypothesis](https://en.wikipedia.org/wiki/Lindel%C3%B6f_hypothesis) (the boundary case of pointwise bounds) does not imply RH. There is no known route from a sharp $\tau(q)$ or $D(\alpha)$ bound for the unit-window moments to the placement of any specific zero.

The proofs of Najnudel and Arguin et al. operate in the "typical $t$" regime: they bound the maximum on a unit window around a $t$ chosen uniformly from $[T, 2T]$. RH-relevant bounds would need to be uniform in $t$. The current ceiling on uniform bounds (Soundararajan, Harper) sits well above the FHK prediction. Whether GMC machinery can ever close that gap is open and probably not without genuinely new tools. Harper's *Seminaire Bourbaki* survey ([arXiv:1904.08204](https://arxiv.org/abs/1904.08204)) is the honest accounting.

**What it DOES say.** Conditional on RH, second-order corrections in Selberg's CLT and the freezing transition predictions sharpen. The Saksman–Webb GMC convergence is unconditional, so its consequences hold without RH. The FHK conjecture itself is statistical (over typical $t$) and is being proved without RH.

**Reading of the intersection.** The log-correlated picture is a *structural reformulation of statistical consequences* of RH-like behavior. It is rich, beautiful, and almost certainly not a proof route. It is, however, the most quantitative connection currently known between zeta and an exactly solvable probabilistic theory (GMC), and it has produced new theorems about zeta.

---

## 10. Open Problems

Ranked by tractability, most to least.

1. **Numerical verification of the FHK second order.** Compute $\max_{|h|\le 1} \log|\zeta(\tfrac{1}{2}+i(t+h))|$ for many $t$ at heights $T = 10^k$, $k = 6, 7, \ldots$ Fit to $\log\log T - \tfrac{3}{4}\log\log\log T + \mathrm{const}$. Data is available from Odlyzko and [LMFDB](https://www.lmfdb.org/).
2. **Numerical exploration of the singularity spectrum.** Compute $\int |\zeta|^{2q}$ over windows of varying widths around random heights $T$. Compare to log-correlated GMC predictions for $\tau(q)$ and $D(\alpha)$.
3. **Sharp mesoscopic variance for $S(T+h) - S(T)$.** Partially known; not in the multifractal language.
4. **GMC convergence under varying mesoscopic scaling.** Saksman–Webb handled one regime. The full phase diagram in $\delta_T$ is open.
5. **Convergence in distribution of the centered FHK maximum** to the randomly shifted Gumbel. Open after Arguin–Bourgade–Radziwill 2023.
6. **Almost-sure (every $t$, not just typical $t$) bounds matching log-correlated predictions.** Would tighten what is known about $\max_{t \in [0,T]} |\zeta(\tfrac{1}{2}+it)|$ and is adjacent to the Soundararajan / Harper uniform-bound program.
7. **Joint extremes for families of L-functions.** Arguin–Ouimet–Radziwill and follow-ups have begun this; the full multivariate spectrum is open.
8. **Use FHK / GMC machinery to prove uniform upper bounds on $|\zeta(\tfrac{1}{2}+it)|$** beyond Bourgain's $t^{53/342}$ and below conjectural $t^\varepsilon$ ([Lindelof](https://en.wikipedia.org/wiki/Lindel%C3%B6f_hypothesis)). Hard, possibly out of reach of current tools.

---

## 11. Further Reading

**Core papers (with arXiv links above):**
- Radziwill and Soundararajan (2017): modern Selberg CLT.
- Fyodorov, Hiary, Keating (2012); Fyodorov, Keating (2014): the FHK conjecture.
- Najnudel (2018); Arguin, Belius, Bourgade, Radziwill, Soundararajan (2019): leading order of the FHK maximum.
- Arguin, Bourgade, Radziwill (2020, 2023): FHK I and II.
- Saksman, Webb (2020): zeta as Gaussian multiplicative chaos.
- Harper (2019), *Seminaire Bourbaki*: survey.

**Background:**
- Bourgade (2010), mesoscopic fluctuations of zeta zeros, [arXiv:1504.05456](https://arxiv.org/abs/1504.05456).
- Keating, Snaith (2000), "Random matrix theory and $\zeta(\tfrac{1}{2}+it)$," *Comm. Math. Phys.* **214**, 57–89.
- Montgomery (1973), pair correlation.

**Adjacent docs in this repo:**
- [`../02_graduate/log_correlated_fields_intro.md`](../02_graduate/log_correlated_fields_intro.md): the soft entry point.
- [`../research_atlas/multifractal_and_log_correlated_methods.md`](../research_atlas/multifractal_and_log_correlated_methods.md): the atlas-style status entry.
- [`./README.md`](./README.md) §8: Keating–Snaith moments.
- [`./README.md`](./README.md) §9: Soundararajan and Harper on the maximum of zeta.
