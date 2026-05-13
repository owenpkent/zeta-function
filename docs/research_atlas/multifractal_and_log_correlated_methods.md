# Multifractal and Log-Correlated Methods

> **Status:** Active research area. Load-bearing for extremal statistics of $|\zeta(\tfrac{1}{2}+it)|$ on short intervals; **not** a route to RH itself. See `../03_research/extreme_values_and_log_correlated_fields.md` for the precise statements.

This atlas entry catalogs three distinct ways the words "[multifractal](https://en.wikipedia.org/wiki/Multifractal_system)" and "[log-correlated](https://en.wikipedia.org/wiki/Gaussian_free_field)" enter zeta-function research. The three threads are commonly conflated. Only one of them is rigorously connected to $\zeta(s)$.

---

## 1. The Idea

A [multifractal](https://en.wikipedia.org/wiki/Multifractal_system) object is one whose local scaling exponents vary across space, with the level sets of a given exponent themselves carrying a nontrivial Hausdorff dimension. The Frisch–Parisi formalism encodes this in a [Legendre duality](https://en.wikipedia.org/wiki/Legendre_transformation) between a partition-function exponent $\tau(q)$ and a singularity spectrum $D(\alpha)$:

$$D(\alpha) = \inf_q\, \bigl(q \alpha - \tau(q)\bigr).$$

Three claims surface in the zeta literature:

1. **$\log|\zeta(\tfrac{1}{2}+it)|$ on short intervals behaves like a log-correlated Gaussian field**, and log-correlated fields are the paradigmatic continuous multifractals. (Real connection, now partially a theorem.)
2. **The Selberg zeta function on hyperbolic surfaces** is genuinely entangled with fractal limit sets via [Patterson–Sullivan theory](https://en.wikipedia.org/wiki/Patterson%E2%80%93Sullivan_theory). (Real connection, but on the *geometric* side, not on $\zeta(s)$ directly.)
3. **Jaffard-style pointwise [Holder regularity](https://en.wikipedia.org/wiki/H%C3%B6lder_condition) of Dirichlet and lacunary series.** (Often invoked, but the multifractal theory here applies to [Riemann's nondifferentiable function](https://en.wikipedia.org/wiki/Weierstrass_function#Other_examples) $\sum \sin(\pi n^2 x)/n^2$, not to $\zeta(s)$. Naming collision; commonly confused.)

The atlas entries below cover each separately.

---

## 2. Thread A: Log-Correlated Fields and the FHK Conjecture (the load-bearing one)

**The idea:** On a unit window $[T, T+1]$ at large height, $t \mapsto \log|\zeta(\tfrac{1}{2}+it)|$ is heuristically a 1D log-correlated Gaussian field with variance $\log\log T$. Apply the multifractal formalism and the freezing-transition technology from [spin glass](https://en.wikipedia.org/wiki/Spin_glass) physics to predict extremes and moments.

**What was tried:**

| Who | When | Construction | Result |
|---|---|---|---|
| Selberg | 1946 | Central limit theorem for $\log|\zeta|$ | Theorem: variance $\tfrac{1}{2}\log\log T$ |
| Keating, Snaith | 2000 | Moment conjecture via CUE characteristic polynomials | Conjecture, proven for $k = 1, 2$ |
| Fyodorov, Hiary, Keating | 2012 | Freezing-transition prediction for $\max_{|h|\le 1} \log|\zeta(\tfrac{1}{2}+i(t+h))|$ | Conjecture: leading $\log\log T$, second $-\tfrac{3}{4}\log\log\log T$, fluctuations randomly shifted Gumbel |
| Najnudel | 2018 | Leading order of FHK max | Theorem under RH |
| Arguin, Belius, Bourgade, Radziwill, Soundararajan | 2019 | Leading order | Theorem unconditional |
| Saksman, Webb | 2020 | Coupling to Gaussian multiplicative chaos on mesoscopic scales | Theorem |
| Arguin, Bourgade, Radziwill | 2020, 2023 | FHK I and II: tightness with correct second order, right-tail $y e^{-2y}$ | Theorem |

**What was learned:**

- The log-correlated heuristic is not just statistics matching: Saksman–Webb gave a genuine *coupling* of zeta to a [Gaussian multiplicative chaos](https://en.wikipedia.org/wiki/Liouville_quantum_gravity#Gaussian_multiplicative_chaos) limit on mesoscopic scales.
- The FHK conjecture has been verified at two of three quantitative orders (leading constant $\log\log T$, second-order constant $-\tfrac{3}{4}\log\log\log T$). Convergence in distribution of the centered max remains open.
- Physics intuition from spin glasses (freezing transition, derivative martingale) genuinely transferred and produced theorems.
- The multifractal singularity spectrum of $|\zeta(\tfrac{1}{2}+it)|^{2q}$ on unit windows is predicted by GMC theory and confirmed in the rigorous Saksman–Webb regime.

**Why this is not a route to RH:**

A multifractal moment bound on $|\zeta|^{2q}$ is a sharper [Keating–Snaith](https://en.wikipedia.org/wiki/Keating%E2%80%93Snaith_conjecture)-style estimate. Such bounds are *consequences* of RH, not equivalents. The [Lindelof Hypothesis](https://en.wikipedia.org/wiki/Lindel%C3%B6f_hypothesis) itself, the boundary case of these size bounds, is strictly weaker than RH. There is no known mechanism by which a $\tau(q)$ or $D(\alpha)$ bound constrains the placement of any individual zero. The proofs operate in the typical-$t$ regime, while RH-relevant bounds need to be uniform in $t$.

The deeper reason: the prime-zero Fourier duality (see [`../02_graduate/log_correlated_fields_intro.md`](../02_graduate/log_correlated_fields_intro.md) §5) holds whether or not RH is true. The multifractal lives on the *spectral side* of that duality. RH is a separate statement about *where* the zero frequencies sit (all on $\mathrm{Re}(s) = 1/2$, equivalently all amplitudes decay at exactly the rate $\sqrt{x}$ on the prime side). Spectral structure is downstream of that placement, not equivalent to it. Worse, RH in its sharpest form (Weil, Li) is a **positivity** statement, and multifractal analysis gives access to size and oscillation but not naturally to positivity. That gap is structural, not just technical.

**What remains open:**

See `../03_research/extreme_values_and_log_correlated_fields.md` §10. Most tractable: numerical verification of the FHK second-order constant against zero data from Odlyzko or [LMFDB](https://www.lmfdb.org/). Least tractable: leveraging GMC machinery to tighten *uniform* upper bounds on $|\zeta(\tfrac{1}{2}+it)|$.

---

## 3. Thread B: Selberg Zeta, Hyperbolic Surfaces, Patterson–Sullivan

**The idea:** For a finite-volume hyperbolic surface $\Gamma \backslash \mathbb{H}^2$, the [Selberg zeta function](https://en.wikipedia.org/wiki/Selberg_zeta_function) is an entire function whose zeros encode Laplace eigenvalues and primitive closed geodesic lengths via the [Selberg trace formula](https://en.wikipedia.org/wiki/Selberg_trace_formula). For infinite-volume convex cocompact hyperbolic surfaces or [Kleinian groups](https://en.wikipedia.org/wiki/Kleinian_group), the picture involves a fractal [limit set](https://en.wikipedia.org/wiki/Limit_set) $\Lambda(\Gamma)$ on the boundary at infinity. Multifractal analysis of conformal measures on $\Lambda(\Gamma)$ via [thermodynamic formalism](https://en.wikipedia.org/wiki/Thermodynamic_formalism) is the natural language; its spectrum is directly tied to the meromorphic structure of the Selberg zeta function.

**Key facts:**

- **Sullivan (1979)**: the critical exponent $\delta(\Gamma)$ of the Poincare series equals the [Hausdorff dimension](https://en.wikipedia.org/wiki/Hausdorff_dimension) of $\Lambda(\Gamma)$.
- **Patterson (1976)**: this $\delta$ is also the location of the rightmost zero or pole of the Selberg zeta function for convex cocompact groups.
- **Naud, Pollicott, Borthwick, Patterson–Perry**: meromorphic extension of Selberg zeta via thermodynamic formalism; resonance-free regions tied to the multifractal spectrum of $\Lambda(\Gamma)$.

**Why this does not directly help RH:**

- The Selberg zeta function for, say, $\mathrm{SL}_2(\mathbb{Z}) \backslash \mathbb{H}$ satisfies an analogue of RH **automatically**, because the trace formula gives a genuinely spectral interpretation. The trade-off: rich arithmetic is replaced by rich geometry. There is no recipe to go back the other way.
- $\operatorname{Spec}(\mathbb{Z})$ has no equivalent of a fractal limit set with a Patterson–Sullivan dimension theory. The closest aspirational object is the Connes adele class space (see `../03_research/new_mathematics.md` §2.3 and §4), where one might hope a multifractal measure plays a structural role. This is speculation.
- The transfer is **by analogy only**. Selberg zeta is a parallel object, not a stepping stone.

**Where it might pay off:**

A toy model. Concrete Schottky-group Selberg zeta functions admit rigorous multifractal analyses and resonance counts; they can be used to test heuristics that one would like to import to Riemann zeta. This is methodologically useful even though the transfer is not literal.

---

## 4. Thread C: The Jaffard Naming Collision

**The idea:** [Stephane Jaffard](https://en.wikipedia.org/wiki/St%C3%A9phane_Jaffard) (1996, 1997) developed a rigorous multifractal regularity theory for the [Riemann nondifferentiable function](https://en.wikipedia.org/wiki/Weierstrass_function#Other_examples)

$$R(x) = \sum_{n=1}^\infty \frac{\sin(\pi n^2 x)}{n^2}.$$

He showed $R$ has pointwise [Holder exponent](https://en.wikipedia.org/wiki/H%C3%B6lder_condition) varying continuously with $x$ over a nontrivial range, and the Hausdorff dimensions of the level sets $\{x : h_R(x) = \alpha\}$ form a nontrivial multifractal spectrum $d(\alpha)$ satisfying the Frisch–Parisi formalism. Aubry and others extended this to broad families of lacunary and arithmetic Dirichlet series.

**The trap:** $R(x)$ is **not** $\zeta(s)$. They share only the name "Riemann." This confusion appears in the literature with surprising frequency.

**Why Jaffard's theory does not apply to $\zeta(\tfrac{1}{2}+it)$:**

- $\zeta$ is meromorphic on $\mathbb{C}$ with only a pole at $s = 1$. The function $t \mapsto \zeta(\tfrac{1}{2}+it)$ is real-analytic on $\mathbb{R}$.
- Pointwise [Holder exponent](https://en.wikipedia.org/wiki/H%C3%B6lder_condition) is $+\infty$ everywhere. The Holder spectrum is trivial.
- Multifractality of $\zeta$, if you want to call it that, is a **statistical scaling** phenomenon under random shifts (Thread A), not a pointwise regularity phenomenon (Jaffard's setting).

**Genuine adjacency:** Aubry–Jaffard methods do apply to random Dirichlet series with iid unit-modulus coefficients (the standard probabilistic model $\sum_p X_p p^{-s}$). On the critical line this model is exactly the complex log-correlated process whose modulus is the GMC limit appearing in Saksman–Webb. So Jaffard's intuition lives next door to the rigorous zeta picture, but it gets there through a probabilistic model, not through $\zeta$ itself.

---

## 5. The Five Obstructions, Applied

Mapping these threads to the obstructions in [`README.md`](README.md) §3:

| Obstruction | Effect on log-correlated / multifractal approach |
|---|---|
| 3.1 Positivity gap | Untouched. GMC and freezing transitions do not produce a positivity argument. |
| 3.2 Geometry gap | Patterson–Sullivan multifractal theory is the *answer* on the geometric side (hyperbolic surfaces), not on the arithmetic side. |
| 3.3 Exactness gap | This is exactly where the program is weakest for RH. All theorems are about typical $t$. |
| 3.4 Analytic ceiling | GMC has not been used to push past Bourgain or to break the Vinogradov–Korobov regime. |
| 3.5 Bridge gap | The bridge between primes and spectral data here goes through random matrix heuristics and Selberg's CLT, not through a new operator. |

Net assessment: this is **structural reformulation of consequences of RH-like behavior**, similar in spirit to (but more dynamic than) the [Selberg class](https://en.wikipedia.org/wiki/Selberg_class) axioms.

---

## 6. Code and Experiments

The repo has a working MFDFA pipeline at [`../../experiments/multifractal/`](../../experiments/multifractal/) for testing the threads above on real data:

- **E0** calibrates MFDFA on synthetic white noise, fGn, and a binomial multiplicative cascade. Establishes the noise floor for spurious multifractality (currently $\Delta\alpha \approx 0.05$ in this pipeline).
- **E1** runs MFDFA on $\log|\zeta(\tfrac{1}{2}+it)|$ in unit windows at heights $T = 10^4, 10^6, 10^8$. Tests Thread A directly.
- **E2** fits the Fyodorov-Hiary-Keating second-order constant $-\tfrac{3}{4}$ for $E[\max]$ over unit windows. Tests the most concrete FHK prediction.
- **E3** runs MFDFA on the normalized Chebyshev fluctuation $(\psi(e^u) - e^u)/e^{u/2}$. Tests whether the prime distribution itself carries the same multifractal structure as $\log|\zeta|$ via the explicit formula.

First-run findings, summarized:
- E0 calibrated. Pipeline gives the right answers on known monofractals (white noise $h \approx 0.5$, fGn at $H = 0.7$ gives $h \approx 0.69$) and known multifractals (binomial cascade matches theory curve).
- E3 shows a real multifractal signal ($\Delta\alpha \approx 2.8$, well above floor) but with $h(q) > 1$ indicating that the right object to feed MFDFA is not $Y(u) = (\psi(e^u) - e^u)/e^{u/2}$ at fixed range. Mesoscopic windowing or increment analysis is the next move.
- E1 and E2 are coded but not yet run.

---

## 7. Open Questions Ranked by Tractability

### Tier 1: tractable now (numerical or partial-theory)

1. Numerical fit of the FHK second-order constant $-\tfrac{3}{4}$ against zero-data-derived $\max_{|h|\le 1}\log|\zeta(\tfrac{1}{2}+i(t+h))|$ at heights $T = 10^k$. Data available from Odlyzko, LMFDB.
2. Compute the multifractal singularity spectrum $D(\alpha)$ for $|\zeta(\tfrac{1}{2}+it)|^{2q}$ over varying window widths; compare to GMC predictions.
3. Sharp mesoscopic variance estimates for $S(T+h) - S(T)$, repackaged in the multifractal language.
4. Joint multifractal spectra for pairs of L-functions on the critical line.

### Tier 2: requires substantial new analytic input

5. Convergence in distribution (not just tightness) of the centered FHK maximum to randomly shifted Gumbel.
6. GMC convergence under the full range of mesoscopic scalings $\delta_T$, completing Saksman–Webb.
7. Almost-sure (every $t$) bounds matching the typical-$t$ FHK prediction.

### Tier 3: mathematical breakthrough territory

8. Use GMC or freezing-transition machinery to push uniform pointwise bounds on $|\zeta(\tfrac{1}{2}+it)|$ closer to Lindelof.
9. Identify a multifractal or thermodynamic-formalism object on a putative arithmetic space (Connes' adele class space, $\mathbb{F}_1$-geometry) that produces the FHK predictions structurally rather than statistically.
10. (Dream / probably wrong tool) Convert a sharp multifractal estimate into a constraint on individual zero locations.

---

## 8. Further Reading

**For the rigorous probabilistic side:**
- See `../03_research/extreme_values_and_log_correlated_fields.md` for full references and status.
- Saksman, Webb (2020), [arXiv:1609.00027](https://arxiv.org/abs/1609.00027), zeta as Gaussian multiplicative chaos.
- Arguin, Bourgade, Radziwill, FHK I ([arXiv:2007.00988](https://arxiv.org/abs/2007.00988)) and FHK II ([arXiv:2307.00982](https://arxiv.org/abs/2307.00982)).
- Harper, *Seminaire Bourbaki* (2019), [arXiv:1904.08204](https://arxiv.org/abs/1904.08204).

**For the geometric side (Selberg zeta, Patterson–Sullivan):**
- Sullivan, D. (1979), "The density at infinity of a discrete group of hyperbolic motions," *Publ. Math. IHES* **50**, 171–202.
- Patterson, S. J. (1976), "The limit set of a Fuchsian group," *Acta Math.* **136**, 241–273.
- Borthwick, D., *Spectral Theory of Infinite-Area Hyperbolic Surfaces*, 2nd ed. (2016).
- Naud, F., resonance-free regions for convex cocompact surfaces (multiple papers).

**For Jaffard-style multifractal regularity (Thread C, careful: this is about $R(x)$, not $\zeta(s)$):**
- Jaffard, S. (1996), "The spectrum of singularities of Riemann's function," *Rev. Mat. Iberoamericana* **12**, 441–460.
- Jaffard, S. (1997), "Old friends revisited: the multifractal nature of some classical functions," *J. Fourier Anal. Appl.* **3**, 1–22.

**Background on multifractal formalism:**
- Frisch, U., Parisi, G. (1985), origin of the formalism in turbulence.
- Rhodes, R., Vargas, V. (2014), "Gaussian multiplicative chaos and applications: a review," *Probab. Surveys* **11**, 315–392.
