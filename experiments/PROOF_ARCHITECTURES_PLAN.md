# Plan: Testing the Four RH Proof Architectures

> Companion to [`docs/solutions/README.md`](../docs/solutions/README.md) and the four-level framing in [`docs/02_graduate/log_correlated_fields_intro.md`](../docs/02_graduate/log_correlated_fields_intro.md) §6. This document is the test plan; the code lives in [`experiments/_shared/`](_shared/) plus per-architecture subdirectories.

## Current status (snapshot)

| Item | Status | Detail |
|---|---|---|
| Phase 0 shared infrastructure | ✅ | [`_shared/`](_shared/): LFunction interface, zeta, Davenport-Heilbronn, smoke test 5/5 |
| Arch 3A (zeta Li coefficients) | ✅ | Positivity confirmed for $n = 1, \ldots, 500$; truncation-limited at zero-sum |
| Arch 3B (D-H Li per-zero diagnostic) | ✅ | Central negative result: small-n Li positivity does NOT distinguish zeta from D-H |
| Arch 3C (Weil quadratic form + Gram) | ✅ | Wrong-approach detector witness: $M^{DH}$ has negative eigenvalues, $W_{DH}(\vec c) < 0 < W_\zeta(\vec c)$ |
| Arch 3D (witness scaling) | ✅ | Witness deepens with K, stable in T_max once first off-line zero is included |
| Arch 3B.2 (Li at large $n$ via off-line correction) | ✅ | Witnesses $\lambda_n^{DH} < 0$ at $n = 4 \times 10^5$ (off-line correction $-2.0 \times 10^7$ dwarfs asymptotic $+2.4 \times 10^6$) and $n = 10^6$ ($-3 \times 10^{18}$). Uses Bombieri-Lagarias asymptotic for on-line part + exact off-line correction; crossover predicted at $n \sim 320{,}000$, witnessed at $n = 400{,}000$. Sign oscillates with $|w_{\rm off}|^n$ amplitude. |
| Arch 3F (Weil-form duality, $\zeta$) | ✅ | Bombieri's explicit formula implemented and verified. Zero side = prime side to $<2\%$ at $T_{\max} = 1000$, $b \geq 14$. Decomposition: boundary $+144$, prime sum $-120$, constant $-19$, gamma $-5$ at $b=20$, cancelling to $W \sim 0.1$. Three orders of magnitude of cancellation — the analytic obstruction to RH lives here. |
| Arch 3G (Weil-form duality, D-H) | ✅ | D-H has no Euler product, so analog "prime sum" becomes a Dirichlet sum with oscillating coefficients $b_n^{DH}$ (recursion $\sum_{d \mid n} b_d c_{n/d} = c_n \log n$). Fourier-form gamma kernel with $\psi(3/4 + it/2)$. Zero side = prime side to sign + 10-30% at $T_{\max} = 200$. D-H components 100× smaller than $\zeta$'s; cancellation 100× looser. |
| Arch 3H (Weil-form duality, $\chi_3$) | ✅ | Refines 3G: tight cancellation is **not** a generic feature of Euler-product L-functions. It's specifically $\zeta$'s pole at $s=1$. $\chi_3$ (Euler product, no pole, GRH believed): mild cancellation $\sim 4\%$, intermediate between $\zeta$ ($0.1\%$) and D-H ($13\%$). Zero side = prime side to $<4\%$. |
| Arch 3I (unconditional Siegel-Walfisz bound for $\chi_3$) | ✅ | The "use $\chi_3$'s milder cancellation for unconditional proof" path is **blocked**. S-W bound on $|\psi(x, \chi_3)|$ applied via partial summation is too loose by 33× at $b=10$, 122× at $b=100$. Partial summation kills the cancellation. Same circularity wall as $\zeta$. |
| Arch 3E (Li / de Bruijn-Newman) | ⏳ | Pending; literature-and-analysis |
| Arch 1A (Berry-Keating discretization) | ✅ | All eigenvalues at $\Im E = -1/2$; density mismatch with zeta documented |
| Arch 1B (Sierra-Townsend) | ✅ | Three position-dependent corrections to $H_{BK}$ tested (centrifugal, Coulomb, modular log $x$). RMS vs first 50 $\gamma_n^\zeta$ stays $\sim 88$ across all variants. Modular form bends density but overshoots. Same H matrix predicts same spectrum for zeta and D-H comparison: L-function-agnostic by construction. |
| Arch 1C (operators on D-H) | ✅ | Best-affine fits of six 1A+1B spectra to first 40 $\gamma_n^\zeta$ and $\gamma_n^{DH}$: discrimination ratio $r := \mathrm{RMS}_\zeta / \mathrm{RMS}_{DH}$ spans $[0.50, 1.67]$, factor-3 spread, consistent with random alignment of similar-density sequences. No construction predicts off-line D-H gammas; the one apparent "match" (ST-C, min 0.11) is a spectral-density artifact. |
| Arch 1D (Connes literature) | ⏳ | Pending |
| Arch 4A (Vinogradov-Korobov) | ⏳ | Pending; literature |
| Arch 4B (non-negative trig polys) | ✅ | LP saturates Fejér bound $\cos(\pi/(n+2))$; classical $3+4\cos+\cos 2$ is sub-optimal at degree 2 |
| Arch 4C (conditional improvements) | ⏳ | Pending; literature |
| Arch 4D (new auxiliary inequalities) | ✅ | The d-variate LP for $\max c_{1, \ldots, 1}$ at uniform degree $(N, \ldots, N)$ saturates the tensor-product witness $P = Q(\theta_1)\cdots Q(\theta_d)$ where $Q$ is the 1D Fejér optimum. Confirmed at $d = 2$ (rank-1 coefficient matrix, exact to FP precision) and $d = 3$ (LP bracket contains tensor value at $N \leq 3$). The d-variate problem **decomposes** for single-coefficient objectives; no new inequality at this LP family. An earlier "factor-of-$2^d$ advantage" was a convention error. |
| Arch 4E (off-diagonal & balanced-sum LPs) | ✅ | Single-coefficient LPs decompose universally (Test A: max $c_{j,k}$ for any $(j,k)$ is rank-1 and matches asymmetric tensor product). **Balanced-diagonal-sum LP does NOT decompose:** max $c_{1,1} + c_{2,2}$ at bidegree $(N,N)$ exceeds the Cauchy-Schwarz tensor bound by **+12.1% at $N=2$** (LP = 2.562, tensor = 16/7 = 2.286), with full-rank optimal $c_{j,k}$ matrix. Improvement decays at higher $N$: 0.2%/1.4%/0.1% at $N = 3/4/5$. Off-diagonal-sum $c_{1,2}+c_{2,1}$ does NOT exceed tensor bound. **First genuinely 2D auxiliary inequality found in this thread.** |
| Arch 4E.2 (alpha sweep + extended diagonal) | ✅ | **Peak LP-vs-tensor gap is +25.00% at $\alpha = 3, N = 2$**, much larger than 4E's +12.1% at $\alpha = 1$. LP-optimal $P$ has clean rational coefficients ($c_{1,1} = 8/5, c_{2,2} = c_{0,2} = c_{2,0} = 4/5$) and genuine 2D structure ($\cos 2u, \cos 2v$ without tensor partners in $(u, v) = (\theta + \phi, \theta - \phi)$ coordinates). **3-term diagonal sum at $N = 3$ gives +1.98% (8.66x the 2-term gap)**. The non-decomposition is weight-sensitive and benefits from larger diagonal-sum objective families. |
| Arch 4E.3 (MT translation of 4E.2 gap) | ✅ | **The +25% C-S gap does NOT translate to an improved Mossinghoff-Trudgian zero-free region constant.** At the 4E.2 peak, best shape/$P(0)$ is **12.6x WORSE** than 1D Fejér at matched effective degree (3). Across $\alpha \in [0, 10]$, the BEST 2D polynomial (tensor product at $\alpha = 0$) gives ratio $0.958$ to 1D Fejér; no $\alpha$ exceeds the 1D bound. **Structural lemma:** any $P(\theta, \phi) \geq 0$ on $[0, 2\pi]^2$ restricted to a line gives a 1D non-neg trig poly, so 2D restriction CANNOT beat the 1D Fejér ceiling at matched degree. The C-S and MT figures of merit are structurally distinct. Improving the ZFR constant via 2D would require multi-zero coupling (Heath-Brown's AP / Siegel setup), constrained-domain LP, or polynomial-ideal SOS. |
| Arch 4E.4 (trivariate balanced-sum LP) | ✅ | **The LP-vs-tensor gap roughly DOUBLES from d=2 to d=3.** Trivariate LP $\max c_{1,1,1} + \alpha c_{2,2,2}$ at tridegree $(2, 2, 2)$ has peak gap **+51.29% at $\alpha = 3.25$** (M-corrected: in $[+50.0\%, +51.3\%]$), vs 4E.2's +25.00% at $\alpha = 3$. Peak LP value 5.09 vs symmetric tensor bound 3.36. The d-variate non-decomposition strengthens with dimension. Per 4E.3 structural lemma, this still does NOT improve the single-zero MT zero-free region constant. |
| Arch 4E.5 (d=4 balanced-sum LP) | ✅ | **The $(d-1) \times 25\%$ scaling pattern DOES NOT continue cleanly at d=4.** Quadvariate LP $\max c_{1,1,1,1} + \alpha c_{2,2,2,2}$ at quad-degree $(2,2,2,2)$ has peak at $\alpha = 4.5$ with gap interval **$[+54.5\%, +69.8\%]$** (M-converged at $M_{4D} = 35$, 1.5M constraints, $P_{\min} \sim -0.1$). Midpoint $\sim +62\%$, BELOW the $(d-1) \times 25\% = +75\%$ prediction. The peak $\alpha$ shifts upward: $3.0 \to 3.25 \to 4.5$ for $d = 2, 3, 4$. Increment per dimension: $\Delta_{2\to3} \approx 25$pp, $\Delta_{3\to4} \approx 15$pp — the gap grows SUB-LINEARLY in $d$, suggesting saturation at some limit below 100% as $d \to \infty$. |
| Arch 2A (Weil-proof diff table) | ⏳ | Pending; literature |
| Arch 2B (worked example, E/F_5) | ✅ | $\alpha = -1.5 \pm i\sqrt{11}/2$, $|\alpha|^2 = 5$; point counts match Weil formula at $k = 1, \ldots, 6$ |
| Arch 2C (F_1 / Arakelov survey) | ⏳ | Pending; literature |
| Arch 2D (Deninger micro-target) | ⏳ | Pending |
| Cross-cut: Selberg-class comparison | ✅ | Fixed K: $M^{\chi_3}$ PSD (min eig $+1.08\times 10^{-2}$); same witness gives $W_{DH}(c^*) < 0 < W_\zeta(c^*), W_{\chi_3}(c^*)$. K scaling: $\chi_3, \chi_4$ PSD across $K \in [10, 100]$ (redundancy pattern), D-H deepens monotonically to $-3.7\times 10^{-1}$. |
| Arch 3D.3 (K-scaling extended to K=1000) | ✅ | **The detector signal saturates structurally.** Across $K \in [100, 1000]$: D-H's relative min eigenvalue converges to a constant $\boldsymbol{-2.62\%}$ (asymptotic, dimension-independent). **Negative eigenvalue count is FIXED at $4$** = number of off-line zero pairs (8 off-line zeros forming 4 conjugate pairs in UHP). Each off-line pair contributes exactly 1 negative eigenvalue. Selberg-class L-functions ($\zeta, \chi_3, \chi_4$) stay PSD to floating-point noise at $K = 1000$. The detector is effectively counting off-line zero pairs via its eigenvalue spectrum. Closes LEARNINGS open #5. |

---

## Premise

We cannot test "does this approach prove RH". We can test the **intermediate claims** each architecture must produce, and we can build **kill criteria** that would falsify the approach. Two non-negotiable disciplines:

1. **Positivity, not just spectral match.** A method that derives only from log-correlated structure, Selberg CLT, GUE statistics, or moments lives at Level 3 and is provably insufficient: those statements are compatible with worlds where RH fails for a single zero at $\beta = 0.51$.
2. **The Davenport-Heilbronn discipline.** Any architecture-1, -3, or -4 method must distinguish $\zeta$ from Davenport-Heilbronn (functional equation, no Euler product, known off-line zeros). Anything that "proves RH" for D-H is wrong.

The four architectures from `docs/solutions/README.md` §8, with concrete test programs below.

---

## Phase 0: Shared infrastructure

Before any architecture-specific work, everything depends on:

1. **Zero data pipeline.** mpmath-derived $\zeta$ zeros at 30+ digit precision, with disk caching; downloads of Odlyzko's high-precision tables for zeros up to height $10^{22}$; LMFDB low-lying zeros for selected L-functions. Uniform API: `LFunction.zeros(T_max, prec)`.
2. **Control L-functions.**
   - **Davenport-Heilbronn** (1936): functional equation, no Euler product, off-line zeros known. The "wrong-approach detector".
   - Selected Dirichlet L-functions for $\chi$ mod small $q$ (Euler product + functional equation, GRH believed).
   - A "fake" Selberg-class object built by hand (Euler product but contrived functional equation) for sanity testing.
3. **Precision pipeline.** mpmath at $\geq 50$ digits, validated against known constants.

Deliverable: [`experiments/_shared/`](_shared/) with documented API.

---

## Architecture 1: Spectral (Hilbert-Pólya)

**Object to test:** does any candidate operator reproduce the zero spectrum *and* fail on D-H (proving it's using something arithmetic)?

| ID | Experiment | Kill criterion |
|---|---|---|
| 1A | Numerical Berry-Keating: discretize $H = xp + px$ on various domains and boundary conditions; compare spectral density to $\tfrac{1}{2\pi}\log(T/2\pi)$ | No boundary condition matches density at scale $\Rightarrow$ heuristic does not survive discretization |
| 1B | Sierra-Townsend hyperbolic-half-plane model: reproduce reported low-eigenvalue match against first 100 zeros | Reproduction fails $\Rightarrow$ this line is weaker than claimed |
| 1C | Same construction applied to D-H; confirm it does *not* spuriously give D-H "on-line" zeros | A candidate $H$ that would predict on-line zeros for D-H is structurally insufficient |
| 1D | Literature: Connes adele-class space. Pin down the smallest missing positivity claim and a toy version we could probe | None (literature) |

**Where a proof would come from:** a self-adjointness theorem with verified domain. Numerical 1A-1C give confidence or rule a candidate out.

---

## Architecture 2: Arithmetic-geometric (Deninger, $\mathbb{F}_1$)

Mostly literature and notation; the proof is a construction. Preparatory work:

| ID | Task | Output |
|---|---|---|
| 2A | Read the Weil proof for curves over $\mathbb{F}_q$ in full detail. Identify each step's analogue (or missing analogue) over $\mathbb{Z}$ | A "diff table": what Weil uses vs what we have over $\mathbb{Z}$, with the gap highlighted |
| 2B | Worked example: a genus-1 curve over $\mathbb{F}_5$. Compute its zeta, its zeros, verify Weil bound. Make the cohomology explicit | Reference notebook other architectures can compare against |
| 2C | Survey state of $\mathbb{F}_1$ and Arakelov-cohomology programs as of 2025 | Status document in `docs/03_research/` |
| 2D | Identify the smallest open conjecture in Deninger's program that would, if proved, be a meaningful step | A target |

**Where a proof would come from:** the missing cohomology construction. We probably can't construct it here, but we can clarify the target.

---

## Architecture 3: Direct positivity (Weil / Li)

**Most computationally tractable architecture.**

| ID | Experiment | Kill criterion |
|---|---|---|
| 3A | Compute Li coefficients $\lambda_n = \sum_\rho \big(1 - (1 - 1/\rho)^n\big)$ for $n = 1, \ldots, 10^4$ at $\geq 30$-digit precision. Check positivity. Fit asymptotic $\lambda_n \sim \tfrac{n}{2}\log n + cn + \ldots$ | A reproducibly negative $\lambda_n$ would refute RH (will not happen). An anomalous growth pattern shapes conjectures |
| 3B | Same for Davenport-Heilbronn. **Expect** $\lambda_n$ to go negative at some computable $n$. Establish where | Positive control: if our setup cannot see D-H going negative, it is broken |
| 3C | Weil quadratic form $Q(f) = \sum_\rho \hat f(\rho)\overline{\hat f(\bar\rho)}$ on parameterized test-function families; track minimum eigenvalue | $Q(f) < 0$ would refute RH. Quantifies how close to zero the minimum gets |
| 3D | ML / gradient-based search for adversarial $f$ minimizing $Q(f)$ over a neural-net-parameterized Schwartz space | Adversarial $f$ found with $Q(f) < 0$ $\Rightarrow$ refutes RH. Tight $Q \geq \varepsilon > 0$ on a wide family $\Rightarrow$ progress |
| 3E | Bombieri-Lagarias structure: relation between Li coefficients and the de Bruijn-Newman constant | Sharpens what positive results would mean |

**Where a proof would come from:** an analytic argument showing $\lambda_n \geq 0$ uniformly, or $Q(f) \geq 0$ on a dense subspace.

---

## Architecture 4: Analytic (zero-free regions)

| ID | Experiment | Kill criterion |
|---|---|---|
| 4A | Reproduce Vinogradov-Korobov; identify where the $2/3$ exponent appears. Probe with numerical exponential sums | Confirms literature; localizes the bottleneck |
| 4B | Non-negative trigonometric polynomial search: $\sum c_k \cos(k\theta) \geq 0$ with $c_0 > 0$ and $c_1$ as large as possible. Improves zero-free-region constants | A better polynomial at small degree shifts constants. Does not break the exponent but is a clean micro-target |
| 4C | Literature: Heath-Brown, Pintz, Ford on conditional improvements; identify which conditional results, unconditionalized, would push the exponent | Map the conditional landscape |
| 4D | Numerical search for "auxiliary inequalities" beyond non-negative trig polynomials: multivariate, weighted, non-classical test functions | A structurally new inequality becomes an active program |

**Where a proof would come from:** a new auxiliary inequality replacing $3 + 4\cos\theta + \cos 2\theta \geq 0$.

---

## Cross-cutting

- **Selberg class as test bed.** Every "Euler product + functional equation gives positivity" claim should be tested across Selberg-class members. Claims that distinguish $\zeta$ from a generic Selberg L-function are the ones with proof potential. Status: positive control via $\chi_3$ now in place ([`e3c3_selberg_cross_cut.py`](positivity/e3c3_selberg_cross_cut.py)): the Gram-matrix detector returns PSD for $\zeta$ and $\chi_3$, indefinite only for D-H.
- **D-H unit test.** Codify "this method does not falsely confirm RH for Davenport-Heilbronn" as an explicit unit test in `experiments/_shared/tests/`.
- **Atlas integration.** Each architecture gets a status row in [`docs/research_atlas/README.md`](../docs/research_atlas/README.md), updated as work proceeds.

---

## Execution order

1. **Phase 0 (shared infrastructure)** — prerequisite for everything.
2. **Architecture 3 (positivity)** — most computationally tractable; immediately produces verifiable artifacts (Li coefficients, Weil form). Highest learning rate per unit effort.
3. **Architecture 1 (spectral)** — rich numerical playground; partial machinery already from multifractal work.
4. **Architecture 4 (zero-free)** — sharp computational micro-target (trig polynomials), small but well-defined.
5. **Architecture 2 (arithmetic-geometric)** — mostly literature, longest arc. Save for when other work has clarified what we need.

Per-architecture work lives in `experiments/positivity/`, `experiments/spectral/`, `experiments/zero_free/`, `experiments/arithmetic_geometric/`. The task list is tracked in this repo's TODO and the harness's todo state.
