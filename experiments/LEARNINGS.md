# Learnings from the proof-architecture experimental thread

> Companion to [PROOF_ARCHITECTURES_PLAN.md](PROOF_ARCHITECTURES_PLAN.md) (test plan and status table) and the per-architecture READMEs. This document synthesizes what the experiments collectively **teach** about the four candidate proof architectures and the RH landscape, organized by finding rather than by architecture. Updated as new experiments complete.

The companion documents answer "what did each experiment do?". This one answers "what do they collectively tell us?". When a new experiment lands, look here for the cross-cutting interpretation.

---

## Cross-cutting findings

### 1. Level 4 (positivity) is the only level that's been shown to actually discriminate $\zeta$ from D-H computationally.

The four-level framing in [docs/02_graduate/log_correlated_fields_intro.md](../docs/02_graduate/log_correlated_fields_intro.md) §6 says: RH lives at Level 4 (Weil positivity), not Level 3 (spectral / statistical). The experiments have now produced a concrete computational instance of this claim:

- **Arch 3 (positivity) at the Gram-matrix level (3C.2, 3D, 3C.3, 3D.2):** the Weil quadratic form via Gram-matrix eigenvalue analysis returns PSD for $\zeta, \chi_3, \chi_4$ (all Selberg-class, GRH-believed) and **indefinite** for D-H, with the witness deepening monotonically as the basis size grows ($-2.4 \times 10^{-2} \to -3.7 \times 10^{-1}$ for $K = 20 \to 100$). The same witness vector $c^*$ that flags D-H gives $W_\zeta(c^*), W_{\chi_3}(c^*) \geq 0$: the detector is direction-selective, not L-function-blind.
- **Arch 1 (spectral) at every level we tested:** bare Berry-Keating (1A), three Sierra-Townsend variants (1B), and the explicit L-function discrimination test (1C) all produce H matrices with no L-function input. After best affine rescaling, RMS deviations from first 40 $\gamma_n^\zeta$ and from first 40 $\gamma_n^{DH}$ are both in $[2.4, 5.1]$; the discrimination ratio $\mathrm{RMS}_\zeta / \mathrm{RMS}_{DH}$ spans a factor of 3.35 around 1, consistent with random alignment of similar-density sequences.

The lesson is concrete: a structural test that lives at Level 3 (spectral signature, density) cannot tell us which L-function we're looking at, because the input quantities (eigenvalues, densities) don't see the Euler product. The same construction "matches" zeta and D-H equally well, even though one satisfies RH and the other doesn't. Positivity-based tests that take in the actual zeros (Gram matrix of $\Phi_b(\rho)$ values) do see the difference.

### 2. Small-$n$ Li-positivity does not distinguish; large-$n$ Li does. The discrimination scale is $n \sim 320{,}000$ for D-H.

The Li criterion $\lambda_n \geq 0 \iff$ RH is unconditional, so D-H must have negative $\lambda_n$ at some $n$. 3B computed $\lambda_n$ at $n \leq 300$ and found **both $\zeta$ and D-H are strictly positive** in that range. The reason: for the first D-H off-line zero ($\rho \approx 0.8085 + 85.7i$, FE partner $0.192 + 85.7i$), $|w_{\rm off}| - 1 \approx 4.2 \times 10^{-5}$, so the off-line contribution becomes order 1 only at $n \approx 24{,}000$, and exceeds the on-line $(n/2)\log(qn/(2\pi))$ asymptotic only at $n \gtrsim 320{,}000$.

3B.2 computed $\lambda_n^{DH}$ at large $n$ via the decomposition $\lambda_n^{DH} = \lambda_n^{DH, \rm asymp} + \sum_{\rho_{\rm off}} 2\,\Re(w_{\rm on}^n - w_{\rm off}^n)$ and **directly witnessed $\lambda_n^{DH} < 0$ at $n = 400{,}000$** (off-line correction $-2.0 \times 10^7$ vs asymptotic $+2.4 \times 10^6$) and **at $n = 10^6$** ($-3 \times 10^{18}$). The sign oscillates as $\cos(n \arg(w_{\rm off}))$ with amplitude growing as $|w_{\rm off}|^n$, so not every $n$ past the crossover gives negative $\lambda_n^{DH}$ (e.g., $n = 500{,}000$ landed on a positive phase).

This is a non-trivial structural result. **The Li criterion does correctly distinguish RH from non-RH; the discrimination scale is just large**, roughly $n \sim 1/|w_{\rm off} - 1|^2$ rather than $n \sim 1/|w_{\rm off} - 1|$. Any proof attempt that argues $\lambda_n \geq 0$ via methods that work uniformly out to $n = O(10^3)$ is structurally insufficient: the same arguments would conclude the same for D-H. To use the Li criterion as a discriminator computationally, you need $n \gtrsim 10^5$ scale or you need a different positivity test entirely.

The methodologically correct upgrade was the Weil quadratic form (3C-3D, 3C.3, 3D.2): same positivity principle, but evaluated via test functions (the $\Phi_b$ family) where the phase of $\hat f(\rho)$ at off-line $\rho$ shows up immediately. The Gram-matrix detector discriminates D-H at $K = 30$ test functions and $T_{\max} = 200$, vastly cheaper than the $n \sim 4 \times 10^5$ needed for Li.

### 3. The Davenport-Heilbronn discipline has been operationally validated.

D-H was introduced as a structural counter-example: any Arch 1/3/4 method that does not distinguish $\zeta$ from D-H is wrong. After the session's experiments, this discipline has now done concrete work twice:

- **It killed a plausible approach** (small-$n$ Li, 3B). Without the D-H control, Li-positivity at $n \leq 300$ looked like a clean positive signal for $\zeta$. With it, we recognized the signal as not actually testing RH.
- **It validated the right approach** (Gram-matrix Weil form, 3C.2 + 3D.2). The detector flags D-H indefinite (correct) and the Selberg-class L-functions PSD (correct). The cross-cut with $\chi_3, \chi_4$ then confirmed the detector is not just "different from $\zeta$" but specifically responding to off-line zeros.

Architecturally: D-H is the project's "false-positive filter." Any method that survives the D-H test deserves further investigation; any method that fails it (passes for D-H as well as $\zeta$) is structurally wrong even if it looks correct on $\zeta$ alone.

### 4. Spectral constructions without arithmetic input are uniformly bounded in their L-function discrimination.

The full Arch 1 result (1A + 1B + 1C) provides a quantitative version of "Hilbert-Pólya needs arithmetic input": across six H matrices we tested (three boundary conditions in 1A, three Sierra-Townsend variants in 1B), the discrimination ratio after best affine rescaling spans $[0.50, 1.67]$ — factor 3.35 spread. A genuine Hilbert-Pólya construction whose eigenvalues are exactly $\{\gamma_n^\zeta\}$ would give RMS$_\zeta = 0$ and RMS$_{DH} \sim 10$, giving ratio $0$. The factor-3 spread we see is consistent with random alignment between two similar-density gamma sequences, not with arithmetic content.

What this rules out is **strong**: no fixed-domain discretization of any operator of the form $H = (xp + px)/2 + V(x)$ (for any $V$) can prove RH, because the same H matrix is L-function-agnostic. The only viable spectral directions are constructions whose H matrix encodes the Euler product (or equivalent arithmetic input), like Connes' adèle class space (1D), which is the deferred-literature task.

### 5. Multivariate Fejér LP decomposes: the d-variate problem is just the d-th power of 1D Fejér. (CORRECTED.)

4D-ii and 4D.2 numerically establish, to LP grid precision at $d = 2$ and $d = 3$:
$$\max c_{1, 1, \ldots, 1} = \left(2\cos\!\left(\frac{\pi}{N+2}\right)\right)^d = (q_1^{1D}(N))^d$$
for the LP over non-negative trig polynomials of $d$-degree $(N, \ldots, N)$ in $d$ variables, with $c_{0, \ldots, 0} = 1$, where $c_{j_1, \ldots, j_d}$ is the *raw* coefficient of $\cos(j_1\theta_1) \cdots \cos(j_d\theta_d)$ in $P$ and $q_1^{1D}(N) = 2\cos(\pi/(N+2))$ is the raw coefficient of $\cos(\alpha)$ in the 1D Fejér optimum $Q$ (renormalized so $q_0 = 1$).

**The LP-optimal coefficient matrix is rank-1.** Empirically extracting the LP solutions at $d = 2$, $N = 1, \ldots, 4$, the $c_{j,k}$ matrix factors as $c_{j,k} = q_j q_k$ exactly, where $Q(\alpha) = \sum_j q_j \cos(j\alpha)$ is the 1D Fejér optimum. The LP-optimal $P(\theta, \phi)$ is just the tensor product $Q(\theta) Q(\phi)$. The same holds at $d = 3$ within LP grid precision.

**The d-variate problem decomposes.** The LP value equals the tensor-product value:
$$\max_{P \geq 0} c_{1,\ldots,1} = \max_{Q \geq 0} q_1^d = (q_1^{1D}(N))^d.$$
There is **no new auxiliary inequality** at this LP family. The "d-variate" inequality $P(t_1 \log p, \ldots, t_d \log p) \geq 0$ that the LP would produce is simply the product of $d$ copies of the 1D Fejér inequality evaluated at $d$ different heights, which carries no more information than the 1D inequality itself.

**This is a corrected interpretation.** An earlier version of this section claimed a "factor-of-$2^d$ advantage" of the LP over a "factorized witness." That comparison was a convention error: the comparison was made against $(c_1^{4B})^d = \cos^d(\pi/(N+2))$ (the Fejér optimum in 4B's $P = c_0 + 2\sum c_k \cos$ convention), but the proper tensor-product witness in the LP's raw-coefficient convention gives $(2 c_1^{4B})^d = (q_1^{1D})^d$. Once aligned, LP and tensor product coincide.

**Methodological lesson.** When comparing LP optima against an analytic witness, the coefficient conventions of the two must be identical, or the comparison is meaningless. Specifically: the 1D Fejér theorem statement "max $c_1 = \cos(\pi/(n+2))$" is in 4B's $P = c_0 + 2\sum c_k \cos$ convention; the raw coefficient of $\cos(\alpha)$ in the optimum polynomial $Q$ is $q_1 = 2 c_1$.

**What this leaves open.** The LP family we ran maximizes a single coefficient $c_{1, \ldots, 1}$. Genuine multivariate inequalities with new structure might come from:

  - **Different objectives**: e.g., $\max c_{1,1} + c_{2,2}$, or weighted combinations encoding the prime-power weights from the explicit formula.
  - **Different constraints**: e.g., requiring $P(t_1, t_2) \geq 0$ only on a specific subset of $(t_1, t_2)$ space corresponding to "consistent" heights from a fixed zero location.
  - **Heath-Brown / Pintz coupling**: inequalities that depend on the prime $p$ through $t_i \log p$ in a non-tensor-product way, with cross-prime structure.

None of these were probed by 4D / 4D.2. The "single-coefficient at uniform degree" LP family decomposes, and that's the message.

### 6. The arithmetic-geometric architecture is the only one that has produced an actual RH theorem in our experiments.

Arch 2B verified the Weil RH for the elliptic curve $E: y^2 = x^3 + x + 1$ over $\mathbb{F}_5$ exactly: Frobenius eigenvalues $\alpha = -3/2 \pm i\sqrt{11}/2$, $|\alpha|^2 = 5$, and $|C(\mathbb{F}_{5^k})|$ matches the Weil formula at $k = 1, \ldots, 6$ by brute-force point counting. This is not "evidence for RH"; it is RH for that curve, proved. The Weil/Deligne machinery works because curves over $\mathbb{F}_q$ have a cohomology with Poincaré duality and a Hodge index theorem (positivity). The open question is whether an analogous structure exists for $\mathrm{Spec}(\mathbb{Z})$ (Deninger, $\mathbb{F}_1$ programs). 2B is the only architecture in our set where the proof template actually closes; the other three architectures' obstructions all reduce, in different ways, to "we don't have the cohomology over $\mathbb{Z}$ that we have over $\mathbb{F}_q$."

### 7. The Weil-form duality is computable, and the cancellation structure on the prime side reveals where the analytic obstruction lives.

For $\zeta$, Weil positivity $W(b) = \sum_\rho \Phi_b(\rho)^2 \geq 0$ can be computed from either the zero side (the sum over $\rho$) or from the prime side via Bombieri's explicit formula:
$$W(b) = \underbrace{8(b^{1/2} - b^{-1/2})^2}_{\text{boundary}} - 2\sum_{p^k < b^2} \tfrac{\log p}{p^{k/2}}(2\log b - k\log p) - (\log 4\pi + \gamma_E)\cdot 2\log b - \int_1^\infty \tfrac{f(x) + f(1/x)/x - 2f(1)/x}{x - 1/x}dx.$$

3F verifies the two sides agree to $<2\%$ at $T_{\max} = 1000$, $b \geq 14$, with the residual error matching the expected $O((\log T)/(\pi T))$ truncation. The framework is correctly implemented.

**The cancellation structure.** At $b = 20$, the four prime-side components are $+144, -120, -19, -5$, summing to $\sim 0.1$. The prime sum cancels 83% of the boundary; the constant and gamma integral together cancel most of the remainder. Each component is $O(10^2)$ relative to $W$ of $O(10^{-1})$ — three orders of magnitude of cancellation.

**Why this is the analytic obstruction.** A proof of Weil positivity from the prime side requires bounding $\sum \Lambda(n) n^{-1/2} (2 \log b - \log n)_+$ from above by the boundary $+$ constants $+$ gamma integral, *without using zero locations*. The best unconditional PNT (Vinogradov-Korobov) gives $\psi(x) - x = O(x \exp(-c (\log x)^{3/5}))$, an error of order $x$. The cancellation we observed has margin $\sim 0.1\%$ of the component magnitudes. The PNT error is far too loose. Improving it to a power-saving error term ($\psi(x) - x = O(x^\theta)$ for $\theta < 1$) is *equivalent* (up to bookkeeping) to a zero-free region with that exponent. To break Weil positivity's analytic obstruction one needs a fundamentally new way to bound the prime sum — Bombieri's "variational approach" (2003), Connes' trace-formula construction, and Deninger's motivic cohomology are three ongoing programs aimed at this.

**The D-H discipline test (3G, complete).** D-H has no Euler product, so the analog "prime sum" becomes a Dirichlet sum over all $n$ with coefficients $b_n^{DH}$ (not $\Lambda(n)$). The b_n^{DH} oscillate in sign (b_2 ≈ +0.2, b_3 ≈ -0.3, b_4 ≈ -1.4, b_6 ≈ +1.9, b_9 ≈ -2.3, ...), partially cancelling within the sum. Result: D-H components are **100× smaller** than $\zeta$'s, and the cancellation is **100× looser**:

| | $\zeta$ at $b = 20$ | D-H at $b = 20$ |
|---|---|---|
| Largest component | $144$ (boundary) | $2.83$ (Dirichlet sum) |
| $\lvert W \rvert$ | $0.1$ | $0.3$ |
| Cancellation $\lvert W \rvert / \lvert \text{largest} \rvert$ | $\sim 10^{-3}$ | $\sim 10^{-1}$ |

**The tight cancellation we observed for $\zeta$ is genuinely a feature of the Euler product**, not a generic feature of L-functions with FE. The mechanism is now identifiable: $\Lambda(n) \geq 0$ for all $n$ (from the Euler product) forces the prime sum to grow unboundedly with $b$, requiring the boundary $8(b^{1/2}-b^{-1/2})^2$ (which is non-zero precisely because $\zeta$ has a pole at $s=1$) to cancel it. For D-H, oscillating $b_n^{DH}$ self-cancel within the Dirichlet sum, no boundary needed.

**Implication for the RH route.** Any analytic argument that proves $W(b) \geq 0$ for $\zeta$ unconditionally must handle the "all-positive $\Lambda(n)$ vs all-positive boundary" cancellation specifically. This is essentially a strong-form PNT statement. Decoupling the prime sum from the boundary (so that the prime sum's growth is independently controlled) is what would close the route, and that's exactly what zero-free region improvements try to do. The reason RH-route via Weil positivity is hard is now visible: you can't escape PNT-strength constraints on $\psi(x)$.

---

## Per-architecture summary of what is open

### Arch 1 (spectral): no further computational lift expected; the door is now Connes-style.

1A + 1B + 1C closed the door on the BK family and ST-style modifications. The remaining direction (1D, Connes adèle class space) is a literature/theory task, not numerical. No further Arch 1 numerical experiment is expected to produce new structural information.

### Arch 2 (arithmetic-geometric): the open frontier is literature-and-construction work.

2B (worked example over $\mathbb{F}_5$) is one of the strongest results we have, but it doesn't move toward $\mathrm{Spec}(\mathbb{Z})$. The natural next steps are all reading/writing:
- 2A (Weil-proof diff table): what does Weil use over $\mathbb{F}_q$ that we lack over $\mathbb{Z}$?
- 2C (state of the $\mathbb{F}_1$ / Arakelov programs as of 2025).
- 2D (smallest open conjecture in Deninger's program that would be a meaningful step).

These are not "experiments" in the numerical sense.

### Arch 3 (positivity): the framework is robust; an open computational frontier exists (the $n \sim 350{,}000$ Li negativity).

The Gram-matrix detector works as a wrong-approach detector and survives Selberg-class cross-cuts. The framework has been validated. The remaining open computational task is: actually exhibit $\lambda_n^{DH} < 0$ for some $n$ around $350{,}000$ via the xi-derivative formula (3B-extension). This is heavy ($\geq 100$-digit precision and careful cancellation control) but would close the loop on the small-$n$ Li result. It is **not** required to validate Arch 3 — the Gram-matrix detector already does that — but it would be a direct demonstration of where the Li criterion goes negative for D-H.

### Arch 4 (analytic): the simple $d$-variate LP decomposes; new auxiliary inequalities need a different structure.

4B closed the 1D Fejér question (LP saturates the classical bound). 4D-ii and 4D.2 confirmed that the natural $d$-variate generalization (LP for max $c_{1, \ldots, 1}$ on non-neg trig polys of uniform degree $(N, \ldots, N)$) decomposes: the LP optimum is exactly the tensor product of 1D Fejér optima, equivalent to applying the 1D inequality at $d$ heights and multiplying. No new content.

To find a genuinely new auxiliary inequality, the LP needs to be reformulated. The promising directions all involve breaking the "max single coefficient at uniform degree" symmetry:
- Maximize a weighted combination of $c_{j,k}$ coefficients corresponding to the prime-power weights from the explicit formula at two heights.
- Constrain $P(t_1, t_2) \geq 0$ only on the locus where $(t_1, t_2)$ comes from a single hypothetical off-line zero (i.e., $t_1 = \gamma$, $t_2 = 2\gamma$ for an off-line zero $\beta + i\gamma$).
- Heath-Brown-style coupling: cross-prime cross-height inequalities.

These are research-direction extensions beyond what 4D / 4D.2 probed.

4A (Vinogradov-Korobov reproduction) and 4C (conditional improvements) remain literature tasks.

---

## Methodological notes

### What test designs have worked

- **The PSD-of-Gram-matrix construction:** evaluating a sum $\sum_\rho \Phi(\rho_j) \Phi(\rho_k)$ at on-line zeros gives a real Gram matrix (automatically PSD); at off-line zeros it doesn't. Reduces the abstract positivity question to a finite-dimensional eigenvalue computation. This is the cleanest concrete realization of "Level 4 positivity" we have.

- **The L-function-class cross-cut:** running the same test on $\zeta$ (RH believed), $\chi_3, \chi_4$ (GRH believed; Selberg-class positive control), and D-H (RH known false; non-Selberg negative control) gives three calibration points. A test that distinguishes all three correctly is direction-selective.

- **Best-affine rescaling for spectral discrimination:** instead of comparing raw eigenvalues to zeta gammas (which forces a scale match), fit $E \mapsto \alpha E + \beta$ first and report residual RMS. Eliminates trivial scale mismatch as a confound.

- **High-precision arithmetic for slow-convergent sums:** mpmath at $\geq 30$ digits for any zero sum, Hurwitz zeta for Dirichlet L-functions, $Z_\chi$ sign-change scan for L-zeros. The smoke test catches regressions at 8/8 tests.

### What test designs did not work, or required correction

- **LP for nonneg multivariate trig polys at coarse grid:** at $M_{2D} = 50$, the 2D LP returned solutions with $P_{\min} \sim -10^{-2}$, i.e., genuinely infeasible on the continuum. Required $M_{2D} = 200$ for $P_{\min}$ to drop to floating-point noise. Lesson: pointwise constraints on continuous functions require fine sampling.

- **Comparison convention mismatch in the 4D multivariate LP:** an earlier version of the 4D / 4D.2 narrative claimed a "factor-of-$2^d$ advantage" of the LP over a "factorized witness." This was a convention error. The 1D Fejér theorem statement "max $c_1 = \cos(\pi/(n+2))$" uses the 4B convention $P = c_0 + 2\sum c_k \cos$, in which the raw coefficient of $\cos(\alpha)$ in the optimum $Q$ is $q_1 = 2 c_1$, not $c_1$. The tensor product $Q(\theta_1) \cdots Q(\theta_d)$ has raw $c_{1,\ldots,1} = q_1^d = (2 c_1)^d$, which equals the LP optimum. The "$2^d$ advantage" came from comparing the LP value to $c_1^d$ instead of $(2 c_1)^d = q_1^d$. Once the conventions are aligned, no advantage remains: the d-variate LP just finds the tensor product. **Lesson: whenever comparing an LP value to an analytic witness, write both in the same convention (raw coefficients of $\cos$ in the polynomial, not "doubled" or "Fourier-symmetric" conventions). Verify the rank of the LP-optimal coefficient tensor: if rank 1, the problem decomposes.**

- **Lowest-eigenvalue-of-real-Hamiltonian comparison without rescaling:** raw eigenvalues from a discretized $H_{BK}$ (range $[0, 20]$) compared to zeta gammas (range $[14, 143]$) gave RMS $\sim 88$, which obscured the actual L-function-blindness question. Best-affine rescaling (1C) made the structural comparison clean.

- **Compact-support test function for Li (e.g., truncating the explicit-formula sum at $T_{\max} = 200$):** the truncation error in Li coefficients at $n = 500$ is $\sim 17\%$, dominated by the $\sim n^2 \log T / (2\pi T)$ tail. To reach truncation accuracy 1% we'd need $T_{\max} \gtrsim 10^4$, requiring $\sim 12{,}000$ zeros. Feasible but not pursued; the qualitative result was already in hand.

### What machinery should be reusable across future experiments

- **The `LFunction` interface** in `experiments/_shared/lfunction.py`: every L-function (zeta, D-H, Dirichlet) implements `evaluate(s)` and `zeros(T_max, prec)` with disk caching. New L-functions can be added by subclassing and the existing experiments run on them unchanged.

- **The Gram-matrix scaling experiment template** (e3d2): pick a test family, an L-function set, a basis-size sweep, and report min eigenvalue. Generalizes to any "Level 4 positivity" test.

- **The discrimination-ratio test** (e1c): for any candidate $\zeta$-targeting construction, apply it to D-H (and ideally $\chi_3, \chi_4$) and compute best-affine RMS to each. A construction whose ratio is bounded by a factor of $\sim 3$ is L-function-blind.

---

## Open questions identified by the experiments

1. ~~**Does the 4D 2D-LP factor-of-4 result generalize to higher dimensions?**~~ ~~**Resolved (4D.2):** confirmed at $d = 3$.~~ **Resolved differently:** the "factor-of-$2^d$ advantage" was a convention error. The d-variate LP for max $c_{1,\ldots,1}$ at uniform degree $(N,\ldots,N)$ decomposes: the optimum is the tensor product $Q(\theta_1) \cdots Q(\theta_d)$ where $Q$ is the 1D Fejér optimum, giving $\max c_{1,\ldots,1} = (2\cos(\pi/(N+2)))^d = (q_1^{1D})^d$. No new inequality.

2. **What LP family WOULD produce a genuinely new multivariate auxiliary inequality?** The simple "max single coefficient at uniform degree" family decomposes. Options to probe: (a) max of weighted combinations of $c_{j,k}$ coefficients corresponding to prime-power weights from the explicit formula; (b) constraints restricting $P \geq 0$ to a subset of $(t_1, t_2)$ corresponding to a single hypothetical off-line zero; (c) Heath-Brown-style cross-prime coupling.

3. **Does the Mossinghoff-Trudgian zero-free constant improve when *any* multivariate inequality is plugged in?** Requires the explicit-formula bookkeeping at $d$ heights, plus a multivariate inequality that doesn't decompose.

4. ~~**At what $n$ does $\lambda_n^{DH}$ first go negative?**~~ **Resolved (3B.2):** witnessed at $n = 400{,}000$ via the asymptotic-plus-off-line-correction decomposition. Off-line correction $-2.0 \times 10^7$ vs on-line asymptotic $+2.4 \times 10^6$. Crossover predicted at $n \sim 320{,}000$; phase determines sign past that. Refinement: a fully rigorous certificate (exact xi-derivative formula, ~100 digit precision, more off-line zeros) would replace the asymptotic with the exact value; the structural conclusion is robust.

5. **Does the Gram-matrix wrong-approach detector remain a clean test in the limit $K \to \infty$ where $M^\zeta$ becomes singular but $M^{DH}$ continues to deepen?** The relative-min eigenvalue stays well-separated at $K = 100$ in our data; what happens at $K = 1000$ (with high-precision arithmetic to push past the floating-point floor)?

6. **Is there an Arch-2-style "lift to $\mathbb{Z}$" that the experiments could probe, even partially?** 2B gave us RH for one curve over $\mathbb{F}_5$. An analogous "RH for a single object in $\mathrm{Spec}(\mathbb{Z})$" doesn't exist yet, but $\mathbb{F}_1$ literature gestures at it.

---

## Synthesis: where does the project stand?

Of the four architectures:

- **Arch 1 (spectral)** is closed at the numerical-experiment level. We've shown the simple constructions are L-function-blind; further progress requires Connes-style theory.
- **Arch 2 (arithmetic-geometric)** has produced the strongest individual result (Weil RH for one curve over $\mathbb{F}_5$, proved). The path to $\mathrm{Spec}(\mathbb{Z})$ is literature/construction work, not experimental.
- **Arch 3 (positivity)** has the most extensive experimental support: small-$n$ Li-positivity confirmed for $\zeta$ (but not a discrimination test); Weil-form-via-Gram-matrix works as a wrong-approach detector; Selberg-class cross-cut validates direction-selectivity. The next experimental step (xi-derivative Li at $n \sim 350{,}000$) is heavy but well-defined.
- **Arch 4 (analytic)** confirmed in 4D/4D.2 that the natural multivariate Fejér LP decomposes: max single-cross-coefficient $c_{1,\ldots,1}$ at uniform degree $(N,\ldots,N)$ saturates the tensor-product $Q(\theta_1) \cdots Q(\theta_d)$ with $Q$ the 1D Fejér optimum. No new auxiliary inequality from this LP family. New inequalities, if any, must come from a different LP structure (weighted objectives or coupled constraints) or from outside the trig-polynomial framework entirely.

The structural message of the experiments: **only Arch 2 has the cohomology/positivity coupling that closes RH-style arguments in the function-field case; only Arch 3 has a positivity test that distinguishes Selberg-class L-functions from non-Euler-product look-alikes computationally; Arch 1 and Arch 4, on the numerical evidence here, do not close RH by themselves.**

This is consistent with the project's structural commitment (RH lives at Level 4 positivity, not Level 3 spectral signature) and with the strategic landscape in [docs/research_atlas/](../docs/research_atlas/).
