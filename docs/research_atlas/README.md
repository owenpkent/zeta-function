# Research Atlas: The Riemann Hypothesis

> A comprehensive catalog of all known approaches, their results, their failures, and the path forward. Written as a working document for ML-assisted mathematical research.

**Purpose:** This document is not a textbook. It is a research map. It catalogs what has been tried, what was learned, what broke, and what's missing — so that future work (human or machine) doesn't repeat dead ends and can identify the most promising gaps.

**Audience:** Researchers and ML systems working on RH or adjacent problems. Assumes graduate-level mathematics but explains the *strategic* landscape, not just the technical details.

---

## Experimental Companion

This atlas has a companion experimental thread in [`experiments/`](../../experiments/) organized around testing the four candidate RH proof architectures from [`docs/solutions/README.md`](../solutions/README.md) §8. The plan and status are in [`experiments/PROOF_ARCHITECTURES_PLAN.md`](../../experiments/PROOF_ARCHITECTURES_PLAN.md). Current state:

| Architecture | Status | Key result |
|---|---|---|
| **3: Direct positivity** (Weil / Li) | 3A-3D, 3B.2, 3D.2-3D.4, 3F-3I complete | Small-n Li-positivity does NOT distinguish zeta from Davenport-Heilbronn (3B), but large-n DOES: 3B.2 witnesses $\lambda_n^{DH} < 0$ at $n = 4 \times 10^5$. Gram-matrix wrong-approach detector: $M^{DH}$ has negative eigenvalues at $K = 30$, $T_{\max} = 200$ (3C, 3D); Selberg-class cross-cut on $\chi_3, \chi_4$ confirms direction-selectivity (3C.3, 3D.2). **3D.3: at $K$ up to 1000, the detector signal saturates structurally — relative min eigenvalue converges to $-2.6\%$ and the number of negative eigenvalues stays FIXED at $4$ = number of off-line zero pairs.** **3D.4: validates the structural prediction across $T_{\max} \in \{200, 300, 350\}$ — D-H gains off-line pairs (4 → 5 → 7) and the negative eigenvalue count tracks exactly (non-trivial double-increment confirmation).** The detector is structurally counting off-line zero pairs via its spectrum. Weil-form duality (3F, 3G, 3H, 3I): the cancellation tightness in the prime side is specifically a feature of $\zeta$'s pole at $s=1$. For $\chi_3$ (Euler product, no pole), cancellation is 100× looser. Tested whether $\chi_3$'s milder cancellation gives unconditional access via Siegel-Walfisz: BLOCKED. The Weil-form route is structurally blocked across the Selberg class. |
| **1: Spectral** (Hilbert-Polya) | 1A, 1B, 1C complete | Berry-Keating $H = (xp+px)/2$ discretization gives constant spectral density $L/(2\pi)$, vs zeta's logarithmically growing density $\log(T/2\pi)/(2\pi)$. Sierra-Townsend-style modifications (centrifugal, Coulomb, modular log $x$) fail individual zero matching (RMS $\sim 88$). After best affine rescaling, all six 1A+1B variants fit zeta and D-H gammas with RMS in $[2.4, 5.1]$; discrimination ratio $\mathrm{RMS}_\zeta / \mathrm{RMS}_{DH}$ spans $[0.50, 1.67]$, factor-3 spread, consistent with random alignment of similar-density sequences. No spectral construction has L-function content; the Hilbert-Pólya search reduces to finding a construction whose H encodes the Euler product or equivalent arithmetic input. |
| **4: Analytic** (zero-free regions) | 4B, 4D, 4D.2, 4E, 4E.2-4E.5 complete | 1D LP saturates Fejér $\cos(\pi/(n+2))$ (4B). Single-coefficient d-variate LPs decompose (4D, 4D.2). **Sum-of-coefficient objectives do NOT decompose (4E, 4E.2):** $\max c_{1,1} + \alpha c_{2,2}$ at bidegree $(2,2)$ peaks at +25% gap to Cauchy-Schwarz tensor bound at $\alpha = 3$. Trivariate (4E.4) and quadvariate (4E.5) extensions: peak gaps $\sim$+50% and $\sim$+62% respectively, with sub-linear growth in dimension. **However (4E.3): the C-S gap does NOT translate into a Mossinghoff-Trudgian zero-free region constant improvement.** Structural lemma: any d-variate non-neg polynomial restricted to a line is a 1D non-neg trig polynomial bounded by 1D Fejér at matched effective degree — so single-zero MT bookkeeping is structurally capped at 1D regardless of the d-variate LP gap. The C-S and MT figures of merit are incompatible; improving the zero-free region via 2D inequalities would require multi-zero coupling (Heath-Brown's AP / Siegel setup), constrained-domain LP, or polynomial-ideal SOS. **Together with R3.5 (NCG no-shortcut theorem) and Arch 3 (analytic circularity wall), this confirms only the geometric route (Arch 2) can break the universal K1 wall on positivity.** |
| **2: Arithmetic-geometric** (Deninger / $\mathbb{F}_1$) | 2A, 2B complete with R1-R5 follow-ups | Weil RH verified for $E: y^2 = x^3 + x + 1$ over $\mathbb{F}_5$: Frobenius eigenvalues at $\alpha = -1.5 \pm \sqrt{11}/2 \, i$ with $\|\alpha\|^2 = 5$ exactly; point counts match Weil formula at $k=1, ..., 6$. **2A: complete evaluation framework with R-series follow-ups.** [Diff doc](../../experiments/arithmetic_geometric/2A_weil_proof_diff.md) traces what Weil's proof uses (Lefschetz + Poincaré + Hodge index) vs the missing structure over $\mathrm{Spec}(\mathbb{Z})$ and lists 17 concrete characteristics the missing mathematics must deliver. [Evaluation doc](../../experiments/arithmetic_geometric/2A_candidate_evaluation.md) operationalizes this: checkable predicates per constraint, submission template, scorecards for six existing candidates (Deitmar / Lorscheid / Borger / Connes / Deninger / Connes-Consani), kill criteria K1-K4. R-series follow-ups: **R1** (all candidates pass D-H exclusion / K2), **R2** (fiber product computed in Borger and Lorscheid; complementary half-candidates), **R2.5** (Λ-blueprint hybrid proposed), **R3** (Connes-Consani positivity classified by K1 status), **R3.5** (no-shortcut theorem: every trace-formula NCG framework has positivity ⟺ RH; the K1 wall is universal), **R3.6** (arithmetic-site / hyperring / characteristic-one machinery sharpens Connes-Consani's verdict to ❌), **R4** (Borger + Connes hybrid analyzed), **R5** (prismatic cohomology identified as the right cohomology for both hybrids), **path forward** (develop both hybrids in parallel, attack Hodge index on whichever reaches it first; 5-10 year program, success probability < 50%). **Central finding: only the geometric route (intersection theory + Hodge index on a constructed surface) can break the K1 wall. All NCG-only approaches fail K1 by structure (R3.5 theorem). Architecture 2's obstruction is constructive, not analytic.** |

The companion uses the **Davenport-Heilbronn L-function** (functional equation, no Euler product, known off-line zeros at $\rho \approx 0.808 + 85.7i$) as a structural wrong-approach detector throughout: any RH-style method that does not distinguish zeta from D-H is wrong.

---

## Table of Contents

1. [The Problem Statement](#1-the-problem-statement)
2. [Catalog of Approaches](#2-catalog-of-approaches)
   - [2.1 Spectral / Hilbert-Polya](#21-spectral--hilbert-polya)
   - [2.2 Arithmetic Geometry / Function Field Analogy](#22-arithmetic-geometry--function-field-analogy)
   - [2.3 Random Matrix Theory](#23-random-matrix-theory)
   - [2.4 Analytic Zero-Free Regions](#24-analytic-zero-free-regions)
   - [2.5 de Bruijn-Newman Constant](#25-de-bruijn-newman-constant)
   - [2.6 Computational Verification](#26-computational-verification)
   - [2.7 Equivalent Reformulations](#27-equivalent-reformulations)
   - [2.8 L-functions and the Langlands Program](#28-l-functions-and-the-langlands-program)
   - [2.9 Subconvexity and Moment Methods](#29-subconvexity-and-moment-methods)
3. [The Five Fundamental Obstructions](#3-the-five-fundamental-obstructions)
4. [What New Mathematics Is Needed](#4-what-new-mathematics-is-needed)
5. [The Case for Machine Learning](#5-the-case-for-machine-learning)
6. [Concrete ML Research Directions](#6-concrete-ml-research-directions)
7. [Data Sources and Computational Resources](#7-data-sources-and-computational-resources)
8. [Open Questions Ranked by Tractability](#8-open-questions-ranked-by-tractability)
9. [References](#9-references)

---

## 1. The Problem Statement

**The [Riemann Hypothesis](https://en.wikipedia.org/wiki/Riemann_hypothesis) (1859):** All non-trivial zeros of the [Riemann zeta function](https://en.wikipedia.org/wiki/Riemann_zeta_function) have real part equal to 1/2.

The zeta function is defined as:

$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad \text{for } \operatorname{Re}(s) > 1$$

Extended to all of $\mathbb{C}$ (except a simple pole at $s=1$) by [analytic continuation](https://en.wikipedia.org/wiki/Analytic_continuation). The "trivial" zeros are at $s = -2, -4, -6, \ldots$ (understood, uninteresting). The non-trivial zeros lie in the critical strip $0 < \operatorname{Re}(s) < 1$.

**RH claims:** Every non-trivial zero satisfies $\operatorname{Re}(s) = 1/2$ exactly.

**Why it matters:** The zeros of zeta control the distribution of prime numbers through the explicit formula. RH gives the tightest possible error bound on the prime counting function. It also connects to cryptography, quantum physics, random matrix theory, and hundreds of conditional theorems across mathematics.

**Status as of 2025:** Unproven after 165+ years. Over 10 trillion zeros verified computationally. No counterexample. One of the seven [Millennium Prize Problems](https://en.wikipedia.org/wiki/Millennium_Prize_Problems).

---

## 2. Catalog of Approaches

Each section follows the same structure: **the idea**, **what was tried**, **what was learned**, **why it failed**, and **what remains open**.

---

### 2.1 Spectral / Hilbert-Polya

**The idea:** Find a [self-adjoint operator](https://en.wikipedia.org/wiki/Self-adjoint_operator) $H$ on a [Hilbert space](https://en.wikipedia.org/wiki/Hilbert_space) whose eigenvalues $\{\lambda_n\}$ satisfy: the non-trivial zeros of $\zeta$ are exactly $\{1/2 + i\lambda_n\}$. Since self-adjoint operators have real eigenvalues ([spectral theorem](https://en.wikipedia.org/wiki/Spectral_theorem)), this would immediately prove RH.

**What was tried:**

| Who | When | Construction | Result |
|-----|------|-------------|--------|
| Berry-Keating | 1999 | $H = xp + px$ (symmetrized position-momentum) | Classical trajectories match; no rigorous quantization with correct boundary conditions |
| Connes | 1999 | Noncommutative geometry on adele class space $\mathbb{A}_\mathbb{Q}/\mathbb{Q}^*$ | Zeros appear as absorption spectrum; reformulates RH as trace formula; does not prove positivity |
| Sierra-Townsend | 2008-2011 | Quantum particle in magnetic field on hyperbolic half-plane | Reproduces zero density and GUE statistics; does not prove RH |

**What was learned:**
- The zeta zeros genuinely *behave* like eigenvalues of a self-adjoint operator. The statistics match [GUE (Gaussian Unitary Ensemble)](https://en.wikipedia.org/wiki/Random_matrix#Gaussian_ensembles) predictions exactly.
- The [Berry–Keating](https://en.wikipedia.org/wiki/Berry%E2%80%93Keating_conjecture) Hamiltonian $H = xp$ has the right classical structure: its periodic orbits correspond to prime powers via the [Gutzwiller trace formula](https://en.wikipedia.org/wiki/Gutzwiller_trace_formula).
- Connes' construction is the deepest reformulation: it places the zeros in a natural geometric/algebraic context. But it shifts the problem to proving positivity of a trace.
- The boundary condition problem for Berry-Keating is not merely technical — different boundary conditions give different spectra. Finding the "right" conditions that produce exactly the zeta zeros is equivalent to the original problem.

**Why it failed:**
Every spectral construction is missing a **positivity argument**. To conclude that eigenvalues are real, you need the operator to be genuinely self-adjoint (not just formally symmetric). In the function field analogy, this positivity comes from the [Riemann–Roch theorem](https://en.wikipedia.org/wiki/Riemann%E2%80%93Roch_theorem) or the [Hodge index theorem](https://en.wikipedia.org/wiki/Hodge_index_theorem). No number-field analogue of this positivity has been found.

**What remains open:**
- Is there a natural Hilbert space on which the zeros appear as a spectrum?
- Can Connes' trace formula be completed with a positivity proof?
- What are the correct boundary conditions for Berry-Keating?
- Can ML discover boundary conditions or operator constructions that match known zeros?

---

### 2.2 Arithmetic Geometry / Function Field Analogy

**The idea:** [Weil](https://en.wikipedia.org/wiki/Andr%C3%A9_Weil) proved RH for curves over [finite fields](https://en.wikipedia.org/wiki/Finite_field) (1948). [Deligne](https://en.wikipedia.org/wiki/Pierre_Deligne) proved the full [Weil conjectures](https://en.wikipedia.org/wiki/Weil_conjectures) (1974). These proofs used powerful geometric tools. Can these techniques be "lifted" from function fields to number fields?

**What was tried:**

| Who | When | Construction | Result |
|-----|------|-------------|--------|
| Weil | 1952 | Explicit formula reformulation | RH equivalent to positivity of a specific quadratic form; clean but unproven for $\mathbb{Q}$ |
| Tits, Manin, Connes-Consani | 1956-present | "Field with one element" $\mathbb{F}_1$ | Attempts to make $\operatorname{Spec}(\mathbb{Z})$ into a curve over $\mathbb{F}_1$; no complete rigorous construction |
| Deninger | 1992-present | Conjectural cohomology theory | Proposed a cohomology where Lefschetz trace formula gives explicit formula and Hodge positivity gives RH; cohomology not constructed |

**How Weil's proof works (function fields) — the template:**
1. Start with a smooth projective curve $C$ over $\mathbb{F}_q$
2. Its zeta function $Z(C, u)$ is a rational function: $P(u)/((1-u)(1-qu))$
3. The zeros of $P(u)$ come from the action of Frobenius on $H^1_{\text{et}}(C, \mathbb{Q}_\ell)$
4. Use Poincare duality + the Hodge index theorem (or Weil pairing on the Jacobian) to force $|\alpha| = \sqrt{q}$ for each root $\alpha$ of $P$
5. This is exactly the RH for function fields

**What was learned:**
- The analogy between [function fields](https://en.wikipedia.org/wiki/Function_field_of_an_algebraic_variety) and [number fields](https://en.wikipedia.org/wiki/Algebraic_number_field) is deep and structural, not superficial. The explicit formula, functional equation, and [Euler product](https://en.wikipedia.org/wiki/Euler_product) all have precise analogues.
- The proof for function fields relies on **four pillars**: (i) a compact smooth curve, (ii) [étale cohomology](https://en.wikipedia.org/wiki/%C3%89tale_cohomology) with [Frobenius](https://en.wikipedia.org/wiki/Frobenius_endomorphism) action, (iii) [Poincaré duality](https://en.wikipedia.org/wiki/Poincar%C3%A9_duality), and (iv) positivity from [Hodge theory](https://en.wikipedia.org/wiki/Hodge_theory). The number field case is missing all four in their standard forms.
- Weil's explicit formula shows RH is *equivalent* to a positivity condition: a specific quadratic form on test functions must be positive semi-definite. This is the cleanest reformulation but proving it is the entire problem.

**Why it failed:**
$\operatorname{Spec}(\mathbb{Z})$ is a one-dimensional arithmetic scheme, but it is **not a smooth compact curve over any field**. It lacks:
- **Compactness:** There's no natural compactification that gives a smooth object. [Arakelov geometry](https://en.wikipedia.org/wiki/Arakelov_theory) provides a partial compactification (adding an "archimedean place") but the resulting object doesn't have the full geometric structure needed.
- **The right cohomology:** No cohomology theory for $\operatorname{Spec}(\mathbb{Z})$ has been constructed that carries a Frobenius-like endomorphism and satisfies Poincare duality with Hodge positivity.
- **Frobenius:** In the function field case, Frobenius $x \mapsto x^q$ is a concrete geometric map. For number fields, there's no obvious analogue acting on a geometric object.

**What remains open:**
- Can $\mathbb{F}_1$-geometry be made rigorous enough to carry Weil's proof?
- What is the correct compactification of $\operatorname{Spec}(\mathbb{Z})$?
- Can Deninger's conjectural cohomology be constructed?
- Is there a "Frobenius" for number fields hiding in the structure of the adeles or in some dynamical system?

---

### 2.3 Random Matrix Theory

**The idea:** The zeros of $\zeta(s)$ have identical statistical properties to eigenvalues of large random unitary matrices (GUE — [Gaussian Unitary Ensemble](https://en.wikipedia.org/wiki/Random_matrix#Gaussian_ensembles)). If this connection can be made rigorous and structural, it might prove RH.

**What was tried:**

| Who | When | Discovery | Status |
|-----|------|-----------|--------|
| Montgomery | 1973 | Pair correlation of zeros matches GUE | Proven conditionally |
| Dyson | 1972 | Immediately recognized connection to quantum physics | Heuristic insight |
| Odlyzko | 1987+ | Computed zeros near $10^{20}$-th; GUE match to extraordinary precision | Numerical verification |
| Rudnick-Sarnak | 1996 | All $n$-point correlations match GUE | Proven conditionally |
| Katz-Sarnak | 1999 | Families of L-functions match classical compact groups | Proven for function fields |
| Keating-Snaith | 2000 | Predicted moments: $I_k(T) \sim a_k g_k T(\log T)^{k^2}$ | Proven for $k=1,2$; open for $k \geq 3$ |

**What was learned:**
- The statistical match between zeta zeros and GUE eigenvalues is essentially perfect. This is not a rough approximation — it holds for pair correlations, $n$-point correlations, nearest-neighbor spacings, and moment statistics.
- For families of L-functions over function fields, Katz-Sarnak proved the match rigorously. The symmetry group of the family (unitary, orthogonal, symplectic) determines the zero statistics.
- The moments of $|\zeta(1/2+it)|$ predicted by random matrix theory have arithmetic corrections ($a_k$, Euler product factors) that encode prime structure. This shows the connection is not purely random — primes matter.
- [Selberg](https://en.wikipedia.org/wiki/Atle_Selberg)'s [central limit theorem](https://en.wikipedia.org/wiki/Central_limit_theorem): $\log|\zeta(1/2+it)|$ is approximately Gaussian with variance $\frac{1}{2}\log\log T$.

**Why it failed:**
RMT describes the **distribution** of zeros, not individual positions. RH is a universal quantifier: "**for all** non-trivial zeros, $\operatorname{Re}(\rho) = 1/2$." Statistics can tell you what happens on average or with high probability. They cannot tell you that every single zero, without exception, lies on a particular line. A statistical proof would need to become an exact structural theorem, and that transition has never been achieved.

**What remains open:**
- Can the RMT connection be made into a structural theorem (not just statistical)?
- What is the operator whose eigenvalues are the zeros? (Connects to 2.1)
- Can moments for $k \geq 3$ be proven?
- Can ML detect structure in the zeros beyond what GUE predicts — departures that might reveal the underlying operator?

---

### 2.4 Analytic Zero-Free Regions

**The idea:** Directly prove that no zeros exist outside the critical line by expanding the known zero-free region.

**What was tried:**

| Who | When | Zero-free region | Significance |
|-----|------|-----------------|--------------|
| Hadamard, de la Vallee Poussin | 1896 | $\zeta(1+it) \neq 0$ | Proved the Prime Number Theorem |
| de la Vallee Poussin | 1899 | $\sigma \geq 1 - c/\log|t|$ | First explicit zero-free region |
| Vinogradov-Korobov | 1958 | $\sigma \geq 1 - c/(\log|t|)^{2/3}(\log\log|t|)^{1/3}$ | Best known; still current |
| (everyone since 1958) | 1958-2025 | No improvement to the exponent $2/3$ | **67 years of stagnation** |

**How the method works:**
1. Use the **zero detector**: $-\operatorname{Re}\frac{\zeta'}{\zeta}(\sigma+it) = \sum_\rho \frac{\sigma - \beta}{|\sigma+it-\rho|^2} + \ldots$
2. This sum is non-negative for $\sigma > 1$, and a zero near $\sigma + it$ makes it large
3. Combine with trigonometric inequalities like $3 + 4\cos\theta + \cos 2\theta \geq 0$ to force zeros away from the line $\sigma = 1$
4. Use [exponential sum](https://en.wikipedia.org/wiki/Exponential_sum) estimates ([Vinogradov](https://en.wikipedia.org/wiki/Ivan_Vinogradov)'s method) to control $\zeta$ in the critical strip

**What was learned:**
- The PNT (1896) was the first major triumph of this approach
- The trigonometric inequality method has a hard theoretical ceiling at the 1D Fejér bound $\cos(\pi/(n+2))$ (4B confirms LP saturation)
- Vinogradov's method of exponential sums dramatically improved bounds but has not been improvable since 1958
- The exponent $2/3$ appears to be a genuine barrier of the method, not a failure of effort
- **Multivariate trig-polynomial inequalities can exceed tensor products of 1D Fejér, but this does NOT improve the zero-free region constant (4E, 4E.2, 4E.3, 4E.4, 4E.5):** the LP for $\max c_{1,1} + 3 c_{2,2}$ at bidegree $(2,2)$ beats the Cauchy-Schwarz tensor bound by +25%, with the gap growing sub-linearly with dimension (+25% / +51% / +62% at d = 2, 3, 4). However, 4E.3 established a structural lemma: any d-variate non-neg polynomial restricted to a line is a 1D non-neg polynomial bounded by 1D Fejér at matched effective degree, so the single-zero Mossinghoff-Trudgian framework is structurally capped at 1D. The C-S figure of merit and the MT figure of merit are incompatible: bivariate LP gaps don't transfer to zero-free region constants. The remaining LP-based directions that bypass this lemma — constrained-domain LP, polynomial-ideal SOS, multi-zero coupling (Heath-Brown's AP setup) — are not yet pursued.

**Why it failed (the classical approach):**
The 1D tools are exhausted. The trigonometric inequalities that drive the classical method (variants of $3 + 4\cos\theta + \cos 2\theta \geq 0$) cannot be improved beyond Fejér. Vinogradov's exponential sum method seems to have a structural ceiling at exponent $2/3$. Reaching $\sigma = 1/2$ from $\sigma \approx 1$ requires not just better estimates but entirely different techniques. The 4E series (4E through 4E.5) shows that the 2D and higher trig-polynomial relaxations produce real new auxiliary inequalities (peak +25% gap at d=2 to +62% at d=4), but per 4E.3 these gaps cannot improve the single-zero zero-free region constant via restriction. The classical 1D ceiling extends to all d-variate restrictions.

The gap between the best known zero-free region ($\sigma \geq 1 - c/(\log|t|)^{2/3}$) and the critical line ($\sigma = 1/2$) is enormous. Even incremental improvements (say, reaching exponent $3/4$) would be major breakthroughs, and none have materialized in 67 years.

**What remains open:**
- Can new exponential sum techniques break the $2/3$ barrier?
- Can automorphic form methods give better zero-free regions?
- Can subconvexity bounds (see 2.9) be leveraged?
- Is there a fundamentally different analytic approach that avoids the classical barriers?

---

### 2.5 de Bruijn-Newman Constant

**The idea:** Parameterize a family of functions $H_\lambda$ where $\lambda = 0$ corresponds to the zeta function. As $\lambda$ increases, zeros "spread" and eventually all become real. The critical value $\Lambda$ where this happens is the de Bruijn-Newman constant. **RH is equivalent to $\Lambda \leq 0$.**

**Precisely:** Define $H_\lambda(z) = \int_0^\infty e^{\lambda t^2} \Phi(t) \cos(zt)\, dt$ where $\Phi$ is related to the Jacobi theta function.

**What was tried:**

| Who | When | Result | Method |
|-----|------|--------|--------|
| de Bruijn | 1950 | $\Lambda \leq 1/2$ | Original definition and upper bound |
| Newman | 1976 | Conjectured $\Lambda \geq 0$ ("RH is barely true") | Heuristic |
| te Riele | 1988 | $\Lambda \geq -50$ | Computational |
| Saouter-Gourdon-Demichel | 2011 | $\Lambda \geq -1.15 \times 10^{-11}$ | Computational |
| Rodgers-Tao (Polymath15) | 2020 | $\Lambda \geq -1.16 \times 10^{-11}$ | Connection to GUE statistics + heat equation analysis |

**What was learned:**
- $\Lambda$ is trapped in a microscopically small interval around 0
- Newman's conjecture ($\Lambda \geq 0$) is widely believed: if RH is true, it's true by the thinnest possible margin
- The Polymath15 project (Tao et al.) connected $\Lambda$ to the evolution of zeros under a heat flow, using GUE statistics — a novel bridge between analysis and random matrix theory
- If $\Lambda > 0$ (even by $10^{-100}$), RH is false. If $\Lambda = 0$ exactly, RH is true by the narrowest possible margin.

**Why it failed:**
Determining the sign of a number that is smaller than $10^{-11}$ in absolute value, without being able to compute it exactly, is extraordinarily difficult. The bounds have been tightened over decades but the last step — from "very close to 0" to "exactly 0 or not" — requires qualitative, not quantitative, insight.

**What remains open:**
- Is $\Lambda = 0$ exactly?
- Can the heat flow / GUE connection be deepened to determine the sign?
- Can ML model the evolution of $H_\lambda$ zeros to predict behavior at the critical threshold?

---

### 2.6 Computational Verification

**What has been done:**

| Year | Height $T$ | Zeros verified | Who | Method |
|------|-----------|----------------|-----|--------|
| 1903 | 15 zeros | manual | [Gram](https://en.wikipedia.org/wiki/J%C3%B8rgen_Pedersen_Gram) | [Euler–Maclaurin](https://en.wikipedia.org/wiki/Euler%E2%80%93Maclaurin_formula) |
| 1936 | 1,041 zeros | hand + machine | Titchmarsh | Riemann-Siegel |
| 1979 | $2 \times 10^9$ | ~$8 \times 10^8$ | van de Lune, te Riele | Riemann-Siegel |
| 2001 | $2.4 \times 10^{12}$ | ~$10^{13}$ | van de Lune et al. | Odlyzko-Schonhage |
| 2004 | $10^{13}$ | ~$10^{13}$ | Wedeniwski (ZetaGrid) | Distributed computing |
| 2011 | $2.4 \times 10^{12}$ | rigorous | Platt | Interval arithmetic |
| 2021 | $3 \times 10^{12}$ | rigorous | Platt-Trudgian | Interval arithmetic |

**All computed zeros lie on the critical line.** Not a single exception in 10+ trillion zeros.

**Methods:**
- **[Riemann–Siegel formula](https://en.wikipedia.org/wiki/Riemann%E2%80%93Siegel_formula):** Efficient approximation of $\zeta(1/2+it)$ for large $t$
- **[Turing's method](https://en.wikipedia.org/wiki/Alan_Turing#Riemann_hypothesis):** Verifies no zeros are missed between computed values (uses [argument principle](https://en.wikipedia.org/wiki/Argument_principle))
- **Odlyzko–Schönhage algorithm:** [FFT](https://en.wikipedia.org/wiki/Fast_Fourier_transform)-based, computes $N$ consecutive zeros in $O(N^{1+\varepsilon})$ time
- **Interval arithmetic (Platt):** Gives rigorous, machine-verified bounds

**What was learned:**
- Extraordinary empirical evidence for RH
- Zero spacing statistics match GUE to high precision
- No "near misses" — zeros don't wander near the edge of the critical strip
- [Gram's law](https://en.wikipedia.org/wiki/Gram%27s_law) (sign changes at [Gram points](https://en.wikipedia.org/wiki/Gram_point)) holds most of the time but fails occasionally — the failures are themselves structured

**Why it cannot prove RH:**
Computation verifies finitely many zeros. RH is a statement about infinitely many. Moreover:
- There are theoretical heuristics (Littlewood's omega theorems) suggesting that if a counterexample exists, it could be at astronomically large height — $10^{10^{100}}$ or beyond
- The zeros become denser as height increases ($\sim \frac{T}{2\pi}\log\frac{T}{2\pi}$ zeros up to height $T$), so verification slows relative to coverage
- A single counterexample would disprove RH, but absence of counterexamples in any finite range proves nothing

**What remains open:**
- Can verification reach $10^{15}$ or beyond? (Mostly an engineering problem)
- Can ML predict zero locations faster than Riemann-Siegel / Odlyzko-Schonhage?
- Can structure in the verified zeros reveal patterns invisible to classical analysis?

---

### 2.7 Equivalent Reformulations

RH has been reformulated in over 300 known equivalent statements. Selected notable ones:

**Analytic equivalences:**
- **Prime counting:** $|\pi(x) - \operatorname{Li}(x)| \leq \frac{1}{8\pi}\sqrt{x}\ln x$ for all $x \geq 2657$
- **[Mertens function](https://en.wikipedia.org/wiki/Mertens_function):** $M(x) = \sum_{n \leq x} \mu(n) = O(x^{1/2+\varepsilon})$ for all $\varepsilon > 0$
- **[Liouville function](https://en.wikipedia.org/wiki/Liouville_function):** $L(x) = \sum_{n \leq x} \lambda(n) = O(x^{1/2+\varepsilon})$

**Algebraic equivalences:**
- **[Robin's inequality](https://en.wikipedia.org/wiki/Robin%27s_inequality) (1984):** $\sigma(n) < e^\gamma n \ln\ln n$ for all $n > 5040$ (where $\sigma$ = [sum-of-divisors](https://en.wikipedia.org/wiki/Divisor_function), $\gamma$ = [Euler–Mascheroni constant](https://en.wikipedia.org/wiki/Euler%E2%80%93Mascheroni_constant))
- **Nicolas' inequality:** $\prod_{p \leq p_k} \frac{p}{p-1} > e^\gamma \ln\theta(p_k)$ for all $k$ (where $\theta$ = Chebyshev function)
- **Lagarias' inequality (2002):** $\sigma(n) \leq H_n + e^{H_n}\ln H_n$ for all $n \geq 1$ (where $H_n$ = $n$-th [harmonic number](https://en.wikipedia.org/wiki/Harmonic_number))

**Linear algebraic:**
- **[Li's criterion](https://en.wikipedia.org/wiki/Li%27s_criterion) (1997):** RH $\iff$ $\lambda_n = \sum_\rho [1 - (1 - 1/\rho)^n] > 0$ for all $n \geq 1$
- Certain Hankel matrices built from $\zeta$ values are positive definite

**Positivity:**
- **Weil positivity:** A specific quadratic form on Schwartz functions is positive semi-definite
- **[Nyman–Beurling](https://en.wikipedia.org/wiki/Nyman%E2%80%93Beurling_criterion) (1955):** RH $\iff$ a specific set of functions is dense in $L^2(0,1)$

**What was learned:**
- RH is deeply entangled with all of mathematics — number theory, analysis, algebra, linear algebra, probability, approximation theory
- Each reformulation reveals a different structural face of the same underlying truth
- Robin's inequality is remarkable: it turns RH into a statement about *integers* and their divisors, with a single explicit exception (5040)
- Li's criterion reduces RH to checking positivity of a sequence — but the sequence grows and positivity becomes harder to verify

**Why reformulations haven't helped:**
Each equivalent statement is exactly as hard to prove as the original. They redistribute the difficulty but don't reduce it. The core obstruction (positivity, or equivalently the precise control of arithmetic oscillations) appears in every formulation, wearing different clothes.

**What remains open:**
- Are there reformulations more amenable to ML pattern detection?
- Can Li's criterion sequence $\lambda_n$ be analyzed by ML to detect structural patterns?
- Can Robin's inequality be approached computationally for structured families of $n$?
- Can ML discover new equivalences that are more tractable?

---

### 2.8 L-functions and the Langlands Program

**The idea:** $\zeta(s)$ is the simplest L-function. There's a vast family — Dirichlet L-functions, Dedekind zeta functions, automorphic L-functions — all conjectured to satisfy GRH. Understanding the structure of this family might prove RH for all of them at once.

**Key structures:**

**[Dirichlet L-functions](https://en.wikipedia.org/wiki/Dirichlet_L-function):** $L(s, \chi) = \sum_{n=1}^\infty \chi(n)/n^s$ for [Dirichlet characters](https://en.wikipedia.org/wiki/Dirichlet_character) $\chi$. GRH: all non-trivial zeros have $\operatorname{Re}(s) = 1/2$.

**The [Selberg class](https://en.wikipedia.org/wiki/Selberg_class) (1992):** Axiomatized the properties shared by all "reasonable" L-functions:
1. Dirichlet series with Euler product
2. Analytic continuation
3. Functional equation of Riemann type
4. Ramanujan hypothesis on coefficients
5. Polynomial Euler product

**The [Langlands program](https://en.wikipedia.org/wiki/Langlands_program):** Predicts that all [automorphic L-functions](https://en.wikipedia.org/wiki/Automorphic_L-function) (from [automorphic representations](https://en.wikipedia.org/wiki/Automorphic_representation) of $GL_n$) are in the Selberg class, and that functoriality relations connect different L-functions. This is the deepest structural framework known.

**What was learned:**
- L-functions form a structured family with internal symmetries
- Selberg's orthogonality conjecture (primitive elements have orthogonal zeros) would give strong constraints
- Langlands functoriality, if fully proven, would transfer information between L-functions
- GRH is believed universally — not just for $\zeta$, but for all L-functions in the Selberg class

**Why it hasn't led to RH:**
- Langlands functoriality itself is only partially proven
- Knowing the structure of the family doesn't directly give positivity for individual zeros
- The Selberg class axiomatization is descriptive, not constructive — it says what L-functions look like, not why their zeros behave well

---

### 2.9 Subconvexity and Moment Methods

**The idea:** Bound the size of $L(1/2+it)$ on the critical line. The [Lindelöf Hypothesis](https://en.wikipedia.org/wiki/Lindel%C3%B6f_hypothesis) (consequence of RH) states $|\zeta(1/2+it)| \ll |t|^\varepsilon$. [Subconvexity](https://en.wikipedia.org/wiki/Subconvexity) means beating the trivial bound.

**Progress:**
- **Convexity bound:** $|\zeta(1/2+it)| \ll |t|^{1/4+\varepsilon}$
- **Best known (Bourgain, 2017):** $|\zeta(1/2+it)| \ll |t|^{53/342+\varepsilon} \approx |t|^{0.1550}$
- **Lindelof Hypothesis (unproven):** $|\zeta(1/2+it)| \ll |t|^\varepsilon$

**Moment results:**
- $I_k(T) = \int_0^T |\zeta(1/2+it)|^{2k} dt$
- Known: $I_1(T) \sim T\log T$, $I_2(T) \sim \frac{1}{2\pi^2}T\log^4 T$
- Open for $k \geq 3$

**Why it hasn't led to RH:**
Subconvexity gives bounds on the *size* of $\zeta$ on the critical line, not on the *location* of its zeros off the line. Even proving the full Lindelof Hypothesis would not prove RH (though RH implies Lindelof). These are important partial results but don't directly address zero positions.

---

## 3. The Five Fundamental Obstructions

Every failed approach hits one or more of these walls. Understanding them is essential for any future attack.

### 3.1 The Positivity Gap

**What it is:** The function field proof of RH rests on positivity — the Hodge index theorem, Riemann-Roch, or the Weil pairing on the Jacobian. These give an inequality that forces eigenvalues to have the right absolute value. No analogue is known for number fields.

**Where it appears:**
- Spectral approach: need to prove the operator is self-adjoint (positivity of inner product)
- Weil's explicit formula: RH $\iff$ a quadratic form is positive semi-definite
- Li's criterion: need positivity of a sequence
- Connes' trace formula: need positivity of a trace

**Why it's hard:** Positivity over $\mathbb{Q}$ would need to "see" all primes simultaneously. Over $\mathbb{F}_q$, there's one Frobenius and you can use geometry. Over $\mathbb{Q}$, each prime gives its own local information and there's no known way to combine them into a single positivity statement.

**This is the single most important obstruction.** If you solve the positivity problem, you likely solve RH.

### 3.2 The Geometry Gap

**What it is:** $\operatorname{Spec}(\mathbb{Z})$ doesn't have the geometric structure needed to run Weil's proof. It's not compact, doesn't have a good cohomology theory with Poincare duality, and lacks a Frobenius endomorphism.

**Where it appears:**
- Function field analogy: the curve $C/\mathbb{F}_q$ is smooth, projective, compact — $\operatorname{Spec}(\mathbb{Z})$ is none of these in the required sense
- $\mathbb{F}_1$-geometry: can't construct the base field
- Deninger's program: can't construct the cohomology

**Why it's hard:** The integers are fundamentally different from polynomial rings over finite fields. The archimedean place (real numbers) introduces analytic structure that doesn't fit into algebraic geometry.

### 3.3 The Exactness Gap

**What it is:** RH is an exact universal statement (ALL zeros satisfy a condition). The strongest evidence is statistical (GUE match) and computational (10 trillion zeros). Neither can bridge the gap to "all."

**Where it appears:**
- Random matrix theory: describes distributions, not individual positions
- Computation: checks finitely many, infinitely many remain
- de Bruijn-Newman: knows $\Lambda$ is close to 0, can't determine the sign

**Why it's hard:** Moving from "almost all" or "with high probability" to "all without exception" typically requires structural/algebraic arguments, not probabilistic or computational ones. The tools that work "on average" fail for the worst case.

### 3.4 The Analytic Ceiling

**What it is:** Classical analytic methods (exponential sums, zero detectors, trigonometric inequalities) have hit provable ceilings that prevent them from reaching the critical line.

**Where it appears:**
- Vinogradov-Korobov: stuck at exponent $2/3$ since 1958
- Trigonometric inequalities: optimal within their class
- Moment methods: known for $k = 1, 2$, blocked for $k \geq 3$

**Why it's hard:** These are not failures of technique within the method — they are provable limitations of the method itself. Better execution of the same approach cannot overcome them.

### 3.5 The Bridge Gap

**What it is:** The spectral world (operators, eigenvalues, Hilbert spaces) and the arithmetic world (primes, integers, divisors) are connected heuristically and statistically, but there is no rigorous bridge between them.

**Where it appears:**
- Berry-Keating: heuristic connection between $xp$ trajectories and primes
- Montgomery-Odlyzko: statistical connection between zeros and GUE
- Connes: partial bridge via adeles, but incomplete

**Why it's hard:** Building this bridge requires simultaneously understanding deep analysis (operator theory), deep algebra (arithmetic), and deep geometry (the shape of number-theoretic spaces). These are traditionally separate fields, and the required synthesis doesn't exist yet.

---

## 4. What New Mathematics Is Needed

Based on the landscape of failures, a proof of RH likely requires some combination of:

### 4.1 A New Cohomology Theory for Arithmetic Schemes

**What:** A cohomology theory $H^i(\operatorname{Spec}(\mathbb{Z}))$ that:
- Has an operator analogous to Frobenius
- Satisfies Poincare duality
- Has a Lefschetz trace formula recovering the explicit formula for zeta zeros
- Carries a Hodge-type structure providing the needed positivity

**Status:** This is Deninger's program. The individual requirements are understood; no single construction satisfies all of them.

**Closest existing work:** Arakelov geometry (Arakelov, Faltings, Soule) provides some of this structure at the archimedean place but doesn't give the full cohomology.

### 4.2 A Rigorous Spectral Realization

**What:** A concrete, rigorously-defined self-adjoint operator $H$ on a specified Hilbert space such that:
- The spectrum of $H$ is exactly $\{\gamma_n : \zeta(1/2 + i\gamma_n) = 0\}$
- Self-adjointness is proven (not assumed or conjectured)
- The connection to primes is explicit

**Status:** Multiple candidates exist heuristically. None are rigorous.

### 4.3 A Number-Field Positivity Principle

**What:** An algebraic or geometric argument that forces a specific quadratic form (Weil's, Li's, or a new one) to be positive definite over $\mathbb{Q}$.

**Status:** This is the core unsolved problem. In function fields, positivity comes from algebraic geometry (intersection theory on surfaces). For $\mathbb{Q}$, no source of positivity is known.

### 4.4 A New Framework for "Almost All" to "All" Arguments

**What:** A method for converting statistical/probabilistic results about zeros (like GUE match, density results) into exact statements about all zeros.

**Status:** No general method exists. In other areas of mathematics, such transitions usually require finding hidden algebraic structure behind the statistical regularity.

### 4.5 New Exponential Sum Techniques

**What:** Methods for estimating exponential sums that break the Vinogradov-Korobov barrier, possibly using algebraic geometry (a la Deligne's proof of the Weil conjectures, which was essentially a deep exponential sum estimate over finite fields).

**Status:** Incremental progress (Bourgain, Heath-Brown) but no breakthrough.

---

## 5. The Case for Machine Learning

### 5.1 Why ML Might Help Where Humans Haven't

**Pattern detection at scale:** The zeta function produces enormous amounts of structured numerical data (zero locations, spacing statistics, L-function coefficients, divisor sums). Humans have found patterns (GUE, pair correlation) through inspired guessing. ML can search systematically for patterns that human intuition misses.

**Conjecture generation:** Mathematics advances through conjecture-then-proof. The conjecture step is creative and pattern-driven — well-suited to ML. Examples of ML-generated conjectures in math are already emerging ([Ramanujan Machine](https://en.wikipedia.org/wiki/Ramanujan_Machine), DeepMind's knot theory work).

**Exploring high-dimensional spaces:** The space of possible operators, boundary conditions, cohomology theories, and positivity arguments is vast. ML can explore it more efficiently than manual construction.

**Cross-domain synthesis:** RH sits at the intersection of analysis, algebra, geometry, and physics. ML models trained across domains might spot connections that specialists in one area miss.

### 5.2 Why ML Alone Cannot Prove RH

**Proofs require logical certainty:** ML produces probabilistic outputs. A proof is a logical chain where every step is certain. ML can conjecture and guide, but the final proof must be verifiable.

**The exactness problem applies to ML too:** Training on 10 trillion zeros teaches the model what typical zeros look like. It doesn't teach why atypical zeros can't exist.

**Mathematical novelty:** If RH requires genuinely new mathematics (as most experts believe), ML must be capable of *inventing* new concepts, not just recombining existing ones. This is at the frontier of what current ML can do.

### 5.3 The Right Role for ML

ML is most likely to contribute by:
1. **Discovering new conjectures** that humans can then attempt to prove
2. **Identifying structural patterns** in zero data, L-function families, or arithmetic sequences
3. **Exploring construction spaces** (operators, boundary conditions, test functions) to find candidates matching known constraints
4. **Guiding proof search** in formal theorem provers ([Lean](https://en.wikipedia.org/wiki/Lean_(proof_assistant)), [Coq](https://en.wikipedia.org/wiki/Coq_(software)), [Isabelle](https://en.wikipedia.org/wiki/Isabelle_(proof_assistant)))
5. **Connecting disparate fields** by finding analogies between mathematical structures

---

## 6. Concrete ML Research Directions

### 6.1 Zero Pattern Analysis

**Goal:** Find structure in zeta zeros beyond GUE statistics.

**Data:** First 10+ billion zeros are publicly available (Odlyzko, LMFDB).

**Approaches:**
- Train models on zero spacings; look for deviations from GUE predictions
- Analyze zeros of different L-functions in families; detect cross-function correlations
- Study the relationship between zeros and primes directly (explicit formula terms)
- Look for patterns in Gram point behavior (where sign changes fail)
- Model the Li criterion sequence $\lambda_n$ — detect growth patterns

**What success looks like:** A new conjecture about zero structure that is (a) not predicted by GUE, (b) verified computationally, and (c) amenable to proof.

### 6.2 Operator Discovery

**Goal:** Find the "right" self-adjoint operator whose spectrum matches zeta zeros.

**Approaches:**
- Parameterize families of operators on $L^2(\mathbb{R}^+)$ and use ML to optimize boundary conditions to match known zeros
- Use neural operators ([DeepONet](https://en.wikipedia.org/wiki/DeepONet), [Fourier Neural Operator](https://en.wikipedia.org/wiki/Fourier_neural_operator)) to learn the operator from spectral data
- Search for operators whose trace formulas match the explicit formula
- Explore quantum Hamiltonians (Berry-Keating variants) with different potentials and boundary conditions

**What success looks like:** An operator whose first $N$ eigenvalues match the first $N$ zeta zeros to high precision, with a clear mathematical structure suggesting self-adjointness.

### 6.3 Positivity Exploration

**Goal:** Find or approximate the missing positivity argument.

**Approaches:**
- Numerically evaluate Weil's quadratic form for large classes of test functions; study the positivity margin
- Use ML to find test functions that minimize the quadratic form (adversarial search for counterexamples to positivity)
- Train models on Li's criterion sequence; predict behavior and identify what drives positivity
- Explore Robin's inequality: study the structure of integers where $\sigma(n)/(n \ln\ln n)$ is largest (colossally abundant numbers)

**What success looks like:** Either (a) a structural explanation for why the quadratic form is always positive, or (b) identification of the "closest" test functions to violating positivity, revealing the mechanism that prevents violation.

### 6.4 Cohomology Construction

**Goal:** Use ML to explore candidate cohomology theories for $\operatorname{Spec}(\mathbb{Z})$.

**Approaches:**
- Formalize the requirements (trace formula, Poincare duality, Hodge positivity) as constraints
- Use ML to search for algebraic structures satisfying these constraints
- Start with known function field cohomologies and use ML to "deform" them toward the number field case
- Explore connections to [topological data analysis](https://en.wikipedia.org/wiki/Topological_data_analysis) — can [persistent homology](https://en.wikipedia.org/wiki/Persistent_homology) reveal the "shape" of prime distributions?

**What success looks like:** A candidate construction satisfying some of the required properties, providing a starting point for rigorous development.

### 6.5 Automated Theorem Proving

**Goal:** Use formal proof assistants augmented by ML to verify partial results or explore proof strategies.

**Approaches:**
- Formalize known equivalences of RH in Lean 4 / Mathlib
- Use ML-guided proof search to attempt subproblems (e.g., proving Robin's inequality for restricted classes of integers)
- Train on existing proofs in analytic number theory to suggest proof strategies
- Verify computational results rigorously (extending Platt's interval arithmetic approach)

**What success looks like:** Machine-verified proofs of partial results; ML-suggested proof strategies that humans hadn't considered.

### 6.6 Cross-Domain Pattern Matching

**Goal:** Find structural analogies between RH and solved problems in other fields.

**Approaches:**
- Train embeddings of mathematical structures; find nearest neighbors to RH-related objects
- Compare the spectral theory of zeta zeros to spectral theory in quantum chaos, condensed matter, string theory
- Look for analogues of the missing positivity in other areas (representation theory, convex optimization, quantum information)
- Explore connections to physics: is there a physical system whose energy levels are zeta zeros?

**What success looks like:** A new analogy that brings tools from a different field to bear on the positivity or geometry gap.

---

## 7. Data Sources and Computational Resources

### 7.1 Zero Databases

| Source | Data | Access |
|--------|------|--------|
| Odlyzko's tables | First $10^{13}$+ zeros, high precision | Public (AT&T archive) |
| [LMFDB](https://en.wikipedia.org/wiki/L-functions_and_modular_forms_database) | Zeros of many L-functions | lmfdb.org |
| Platt-Trudgian | Rigorous verification to $T = 3 \times 10^{12}$ | Published papers |

### 7.2 L-function Data

| Source | Data | Access |
|--------|------|--------|
| LMFDB | Dirichlet, elliptic curve, modular form L-functions | lmfdb.org |
| [PARI/GP](https://en.wikipedia.org/wiki/PARI/GP) | Computational number theory library | Open source |
| [SageMath](https://en.wikipedia.org/wiki/SageMath) | L-function computation | Open source |

### 7.3 Relevant Software

| Tool | Purpose |
|------|---------|
| mpmath (Python) | Arbitrary-precision zeta/L-function computation |
| ARB / Flint | Fast rigorous arithmetic |
| PARI/GP | Number theory computations |
| Lean 4 / Mathlib | Formal proof assistant with growing number theory library |
| manim | Visualization (already in this project) |

### 7.4 Key Computed Objects

- **Robin's inequality**: Verified for all $n \leq 10^{10}$ (at least)
- **Li's criterion**: $\lambda_n > 0$ verified for $n \leq 10^5$ (approximately)
- **Mertens function**: Computed extensively; known to satisfy $|M(x)| < \sqrt{x}$ for $x < 10^{16}$ (at least)
- **[Colossally abundant numbers](https://en.wikipedia.org/wiki/Colossally_abundant_number)**: The integers where Robin's inequality is tightest — these are the "adversarial examples" for RH from the arithmetic side

---

## 8. Open Questions Ranked by Tractability

Ordered from most tractable (ML could plausibly contribute now) to least tractable (requires mathematical breakthrough):

### Tier 1: ML-tractable now

1. **Find new patterns in zero spacings beyond GUE.** Data exists; pattern detection is ML's strength.
2. **Predict Li criterion values $\lambda_n$ for large $n$.** Sequence prediction task with known initial values.
3. **Optimize operator boundary conditions to match known zeros.** Continuous optimization problem.
4. **Characterize colossally abundant numbers.** These are the "hardest cases" for Robin's inequality; understanding their structure is a well-defined arithmetic problem.
5. **Discover new equivalent reformulations.** ML can search for relationships between known mathematical quantities.

### Tier 2: ML-assisted with human guidance

6. **Find the missing operator.** Requires parameterizing operator families and matching spectral data.
7. **Explore the Weil positivity margin.** Requires computing the quadratic form for many test functions and studying when it's smallest.
8. **Connect zero structure to specific prime patterns.** Requires combining analytic and arithmetic data.
9. **Identify candidate cohomology constructions.** Requires formalizing constraints and searching algebraic structures.
10. **Extend zero-free regions using new techniques.** Requires generating and testing new exponential sum estimates.

### Tier 3: Requires mathematical invention

11. **Prove a number-field positivity principle.** The core problem; requires genuinely new ideas.
12. **Construct a rigorous cohomology for $\operatorname{Spec}(\mathbb{Z})$.** Requires new algebraic geometry.
13. **Bridge spectral and arithmetic worlds.** Requires a new framework connecting operators to primes.
14. **Prove RH.** The end goal; likely requires a combination of the above.

---

## 9. References

### Foundational

- Riemann, B. (1859). *Uber die Anzahl der Primzahlen unter einer gegebenen Grosse.* (See `sources/wilkins_translation.txt` for English translation)
- Titchmarsh, E.C. *The Theory of the Riemann Zeta-Function*, 2nd ed. (revised by Heath-Brown). Oxford.
- Edwards, H.M. *Riemann's Zeta Function*. Dover.
- Iwaniec, H. & Kowalski, E. *Analytic Number Theory*. AMS Colloquium Publications.

### Surveys

- Conrey, J.B. (2003). "The Riemann Hypothesis." *Notices AMS* 50(3):341-353. (Best accessible survey)
- Bombieri, E. (2000). "The Riemann Hypothesis." Clay Institute Millennium Problem statement.
- Sarnak, P. (2004). "Problems of the Millennium: The Riemann Hypothesis."
- Mazur, B. & Stein, W. (2016). *Prime Numbers and the Riemann Hypothesis*. Cambridge.

### Spectral Approaches

- Berry, M.V. & Keating, J.P. (1999). "The Riemann zeros and eigenvalue asymptotics." *SIAM Review* 41(2):236-266.
- Connes, A. (1999). "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function." *Selecta Math.* 5(1):29-106.
- Sierra, G. & Townsend, P. (2008). "Landau levels and Riemann zeros." *Phys. Rev. Lett.* 101:110201.

### Arithmetic Geometry

- Weil, A. (1948). *Sur les courbes algebriques et les varietes qui s'en deduisent*. Hermann.
- Deligne, P. (1974). "La conjecture de Weil. I." *Publ. Math. IHES* 43:273-307.
- Deninger, C. (1992). "Local L-factors of motives and regularized determinants." *Invent. Math.* 107:135-150.
- Connes, A. & Consani, C. (2011). "On the notion of geometry over $\mathbb{F}_1$." *J. Algebraic Geom.* 20:525-557.

### Random Matrix Theory

- Montgomery, H.L. (1973). "The pair correlation of zeros of the zeta function." *Proc. Symp. Pure Math.* 24:181-193.
- Odlyzko, A.M. (1987). "On the distribution of spacings between zeros of the zeta function." *Math. Comp.* 48:273-308.
- Keating, J.P. & Snaith, N.C. (2000). "Random matrix theory and $\zeta(1/2+it)$." *Comm. Math. Phys.* 214:57-89.
- Katz, N. & Sarnak, P. (1999). "Zeroes of zeta functions and symmetry." *Bull. AMS* 36:1-26.

### de Bruijn-Newman

- de Bruijn, N.G. (1950). "The roots of trigonometric integrals." *Duke Math. J.* 17:197-226.
- Rodgers, B. & Tao, T. (2020). "The de Bruijn-Newman constant is non-negative." *Forum Math. Pi* 8:e6.

### Computational

- Platt, D. & Trudgian, T. (2021). "The Riemann hypothesis is true up to $3 \times 10^{12}$." *Bull. London Math. Soc.* 53:792-797.
- Odlyzko, A.M. & Schonhage, A. (1988). "Fast algorithms for multiple evaluations of the Riemann zeta function." *Trans. AMS* 309:797-809.

### ML in Mathematics

- Davies, A. et al. (2021). "Advancing mathematics by guiding human intuition with AI." *Nature* 600:70-74.
- Raayoni, G. et al. (2021). "Generating conjectures on fundamental constants with the Ramanujan Machine." *Nature* 590:67-73.
- He, Y.-H. et al. (2017). "Machine-learning the string landscape." *Phys. Lett. B* 774:564-568.
