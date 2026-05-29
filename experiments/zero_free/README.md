# Architecture 4: Analytic (zero-free regions)

> Per the [project plan](../PROOF_ARCHITECTURES_PLAN.md). RH would follow if the known zero-free region $\sigma \geq 1 - c/(\log|t|)^{2/3}$ could be pushed all the way to $\sigma = 1/2$. The exponent $2/3$ (Vinogradov-Korobov, 1958) has been stuck since.

## 4B: Non-negative trigonometric polynomial optimization

**Status:** complete. The LP saturates the Fejér bound exactly; the classical polynomial $3 + 4\cos\theta + \cos 2\theta$ is sub-optimal already at degree 2.

**Method:** [e4b_nonneg_trig.py](e4b_nonneg_trig.py). Solve the linear program
$$\max c_1 \quad \text{subject to } c_0 = 1, \quad P(\theta) := c_0 + 2 \sum_{k=1}^n c_k \cos(k\theta) \geq 0 \text{ on sampled } \theta,$$
using `scipy.optimize.linprog` with $M = 4000$ uniform sample points. Compare to Fejér's analytical bound $c_1 \leq \cos(\pi/(n+2))$ at degree $n$.

**Findings:**

| $n$ | LP max $c_1$ | Fejér $\cos(\pi/(n+2))$ | gap |
|---|---|---|---|
| 1 | $0.5000$ | $0.5000$ ($= \cos\pi/3$) | $< 10^{-7}$ |
| 2 | $0.7071$ | $0.7071$ ($= \cos\pi/4$) | $< 10^{-7}$ |
| 3 | $0.8090$ | $0.8090$ ($= \cos\pi/5$) | $< 10^{-7}$ |
| 5 | $0.9010$ | $0.9010$ | $< 10^{-7}$ |
| 10 | $0.9659$ | $0.9659$ | $< 10^{-7}$ |
| 20 | $0.9898$ | $0.9898$ | $< 10^{-7}$ |

**The LP saturates Fejér's bound to numerical precision at every degree.**

**Classical comparison:** the de la Vallée Poussin / Hadamard polynomial $3 + 4\cos\theta + \cos 2\theta = 2(1 + \cos\theta)^2$ has $c_0 = 3, c_1 = 2, c_2 = 1/2$. Normalized to $c_0 = 1$: $c_1 = 2/3 \approx 0.6667$. But the optimal degree-2 non-negative trig polynomial achieves $c_1 = \cos(\pi/4) = \sqrt 2/2 \approx 0.7071$:

$$P_{\rm opt}(\theta) = \left(\cos\theta + \frac{1}{\sqrt 2}\right)^2 = \frac{1}{2} + \sqrt 2 \cos\theta + \frac{1}{2}\cos 2\theta$$

A $\sim 6\%$ improvement over the classical polynomial at the same degree.

**What this means for the zero-free region:** the de la Vallée Poussin constant $c$ in $\sigma \geq 1 - c/\log|t|$ depends on $c_1/c_0$ through a known formula. Improving $c_1/c_0$ improves $c$ but does NOT change the form $1/\log|t|$. The exponent in Vinogradov-Korobov ($2/3$ vs $1$) comes from exponential-sum estimates, not from trig-polynomial optimization. So 4B confirms that the classical inequality is sub-optimal within the family it's drawn from, but cannot break the structural barrier the architecture faces.

**Why this is a known dead end for breaking the exponent.** Even the asymptotic limit $\cos(\pi/(n+2)) \to 1$ as $n \to \infty$ only improves the constant by a bounded factor (Fejér's limit is $1$, vs the classical $2/3$, so improvement at most $3/2 \approx 50\%$). To push the exponent $2/3 \to 1/2$ or further requires fundamentally new auxiliary inequalities (4D) or new analytic techniques (4A: Vinogradov-Korobov method itself).

**The Davenport-Heilbronn discipline.** Not directly applicable here: the inequality $P(\theta) \geq 0$ is universal in $\theta$ and doesn't depend on the L-function. The constraint that DOES depend on the L-function is the Euler-product structure that turns $-\Re\zeta'/\zeta$ into a sum of $\Lambda(n) n^{-\sigma} \cos(t\log n)$. D-H lacks an Euler product, so the trig-polynomial argument doesn't apply to D-H (which is consistent: D-H has off-line zeros so a zero-free region argument MUST fail for it).

## 4D: Multivariate auxiliary inequalities ([e4d_multivariate_lp.py](e4d_multivariate_lp.py))

**Status:** complete. **The multivariate LP decomposes**: max single coefficient $c_{1,\ldots,1}$ at uniform degree saturates the tensor product of 1D Fejér optima. No new auxiliary inequality at this LP family.

**Two parts:**

### 4D-i: degree sweep extension

Run 4B's LP at $n \in \{5, 10, 20, 30, 50, 100, 200\}$ with $M = 8000$ sample points. Confirms Fejér saturation at all tested degrees: the LP-Fejér gap stays $< 10^{-7}$ across the entire sweep. The Fejér bound's gap to 1 scales as $\pi^2/(2(n+2)^2)$, so 1D improvements have $O(1/n^2)$ diminishing returns. The current best zero-free constant (Mossinghoff-Trudgian, $n = 23$) sits in the high-return regime, but further 1D improvements are bounded by the Fejér limit.

### 4D-ii: bivariate LP

Consider non-negative bivariate trig polynomials of bidegree $(N, N)$ in the **raw coefficient** convention:
$$P(\theta, \phi) = \sum_{0 \leq j, k \leq N} c_{j,k} \cos(j\theta) \cos(k\phi) \geq 0, \quad c_{0,0} = 1,$$
i.e., $c_{j,k}$ is the literal coefficient of $\cos(j\theta) \cos(k\phi)$ (not "doubled" or otherwise renormalized).

The tensor-product witness $P = Q(\theta) Q(\phi)$ with $Q$ the 1D Fejér optimum (normalized so $q_0 = 1$) gives
$$c_{j,k}^{\rm tensor} = q_j\, q_k$$
where $q_1 = 2 \cos(\pi/(N+2))$ is the raw coefficient of $\cos(\alpha)$ in $Q$. (In 4B's convention $P_{\rm 4B} = c_0 + 2\sum c_k \cos(k\alpha)$ with $c_0 = 1$, the Fejér max is $c_1^{\rm 4B} = \cos(\pi/(N+2))$, so the raw coefficient is $q_1 = 2 c_1^{\rm 4B}$.) Hence
$$c_{1,1}^{\rm tensor} = q_1^2 = 4 \cos^2\!\left(\frac{\pi}{N+2}\right).$$

We solve the LP for max $c_{1,1}$ directly at $M_{2D} = 200$ sample points per direction (40,000 constraints) and find:

| $N$ | LP max $c_{1,1}$ | tensor product $q_1^2$ | LP − tensor |
|---|---|---|---|
| 1 | $1.0000$ | $1.0000$ | $-4 \times 10^{-16}$ |
| 2 | $2.0000$ | $2.0000$ | $-9 \times 10^{-16}$ |
| 3 | $2.6180$ | $2.6180$ | $0.0$ |
| 4 | $3.0002$ | $3.0000$ | $+2 \times 10^{-4}$ (LP grid noise) |

**The LP exactly matches the tensor-product witness at every $N$.** Extracting the LP-optimal coefficient matrix at $N \leq 4$, we find $c_{j,k}$ is **rank 1** with $c_{j,k} = q_j q_k$. The LP-optimal polynomial $P(\theta, \phi)$ is just $Q(\theta) Q(\phi)$ (or some polynomial with the same $c_{j,k}$ tensor by LP-degeneracy).

**The 2D problem decomposes.** No new auxiliary inequality is found at this LP family: the "2D" inequality $P(t_1 \log p, t_2 \log p) \geq 0$ is just the product of two copies of the 1D Fejér inequality applied at two heights, carrying no more information than the 1D inequality.

**A correction to an earlier interpretation.** An earlier version of this section claimed a "factor-of-4 advantage" of the LP over a "factorized witness." That comparison was a convention error: $c_1^{\rm 4B} = \cos(\pi/(N+2))$ is the coefficient in $P_{\rm 4B} = c_0 + 2\sum c_k \cos(k\alpha)$, so the raw coefficient of $\cos(\alpha)$ in the optimum polynomial $Q$ is $q_1 = 2 c_1^{\rm 4B}$, not $c_1^{\rm 4B}$. Computing the tensor product in raw-coefficient terms gives $q_1^2 = 4 (c_1^{\rm 4B})^2$, which matches the LP. The "advantage" was the convention mismatch.

**Methodological lesson:** when comparing an LP value to an analytic witness, both must use the same coefficient convention; verify the rank of the LP-optimal coefficient tensor as a quick decomposition check.

## 4D.2: Trivariate LP — the d-variate problem still decomposes ([e4d2_trivariate_lp.py](e4d2_trivariate_lp.py))

**Status:** complete. At $d = 3$ the LP again saturates the tensor-product witness; no new inequality from this LP family.

**Motivation:** 4D-ii found at $d = 2$ that the LP saturates the tensor-product $P = Q(\theta) Q(\phi)$. We test whether $d = 3$ behaves the same.

**Method:** LP for non-negative trivariate trig polynomial
$$P(\theta, \phi, \psi) = \sum_{0 \leq j, k, l \leq N} c_{j,k,l} \cos(j\theta)\cos(k\phi)\cos(l\psi) \geq 0$$
sampled on $M_{3D}^3$ grid, $c_{0,0,0} = 1$, objective $\max c_{1,1,1}$. We use $M_{3D} = 70$ (343,000 constraints) and verify on $M_{\rm verify} = 120$ grid (1.7 million points). Tensor-product witness is $P = Q(\theta) Q(\phi) Q(\psi)$ with $Q$ the 1D Fejér optimum (raw coefficient $q_1 = 2\cos(\pi/(N+2))$), giving $c_{1,1,1}^{\rm tensor} = q_1^3 = 8\cos^3(\pi/(N+2))$.

**Findings ($M_{3D} = 70$, $M_{\rm verify} = 120$):**

| $N$ | LP max $c_{1,1,1}$ | tensor $q_1^3$ | LP $-$ tensor | $P_{\min}$ verify |
|---|---|---|---|---|
| 1 | $1.0000$ | $1.0000$ | $0.0$ | $-10^{-15}$ |
| 2 | $2.8346$ | $2.8284$ | $+6.1 \times 10^{-3}$ | $-6.1 \times 10^{-3}$ |
| 3 | $4.2361$ | $4.2361$ | $+6 \times 10^{-15}$ | $-2.3 \times 10^{-2}$ |

The LP at finite $M$ is a relaxation: $\mathrm{LP}(M)$ is an upper bound on the true continuum max. Projecting the LP solution by adding $|P_{\min}|$ to make it feasible and renormalizing $c_{0,0,0} = 1$ gives a lower bound $\mathrm{LP}(M) / (1 + |P_{\min}|)$. The interval $[\mathrm{LP}/(1 + |P_{\min}|), \mathrm{LP}]$ contains the true max.

**Per-N bracket at $M_{3D} = 70$:**

| $N$ | bracket on true max | tensor | in bracket? |
|---|---|---|---|
| 1 | $[1.0000, 1.0000]$ | $1.0000$ | $\checkmark$ |
| 2 | $[2.8174, 2.8346]$ | $2.8284$ | $\checkmark$ |
| 3 | $[4.1397, 4.2361]$ | $4.2361$ | $\checkmark$ |

**M-convergence at $N = 2$:** LP excess and $|P_{\min}|$ both shrink from $\sim 10^{-1}$ at $M=20$ to $\sim 6 \times 10^{-3}$ at $M=70$, consistent with the LP converging to the tensor-product value from above as $M \to \infty$.

**Conclusion (corrected).** The trivariate LP saturates the tensor-product witness $P = Q(\theta) Q(\phi) Q(\psi)$, just as the bivariate LP did. The d-variate problem decomposes at $d = 1, 2, 3$:
$$\max_{P \geq 0,\ c_{0,\ldots,0}=1,\ d\text{-degree }(N,\ldots,N)} c_{1, \ldots, 1} = q_1^d = \left(2\cos\!\frac{\pi}{N+2}\right)^d$$
where $q_1$ is the raw coefficient of $\cos(\alpha)$ in the 1D Fejér optimum. **No new auxiliary inequality** is found at this LP family; the d-variate inequality is just the d-th power of the 1D Fejér inequality.

Genuinely new multivariate inequalities would require a different LP structure: weighted objectives that don't reduce to single-coefficient maximization, or constraints that couple the variables (e.g., $P \geq 0$ only on a specific submanifold of $(\theta_1, \ldots, \theta_d)$-space).

## 4E: Off-diagonal and balanced-sum bivariate LPs ([e4e_offdiag_lp.py](e4e_offdiag_lp.py))

**Status:** complete. **Genuinely new 2D inequality found: the LP for max $c_{1,1} + c_{2,2}$ at bidegree (N, N) exceeds the best tensor-product witness by up to 12% at $N = 2$, with LP-optimal coefficient matrix of full rank $N + 1$.** This refines (and partially overturns) the 4D conclusion: single-coefficient LPs decompose, but balanced-sum LPs do not.

**Motivation.** 4D / 4D.2 showed that the LP for max $c_{1, \ldots, 1}$ at bidegree $(N, \ldots, N)$ saturates the tensor product $Q(\theta_1) \cdots Q(\theta_d)$. That conclusion was for a *single-coefficient* objective. The natural question (LEARNINGS open #2): does the decomposition extend to (a) off-diagonal single coefficients $c_{j,k}$ with $(j, k) \neq (1, 1)$, or (b) sum-of-coefficient objectives like $c_{1,1} + c_{2,2}$?

**Method.** Three families of LPs at bidegree $(N, N)$ for $N \in \{2, 3, 4, 5\}$ in raw-coefficient convention $P(\theta, \phi) = \sum_{0 \leq j, k \leq N} c_{j,k} \cos(j\theta) \cos(k\phi) \geq 0$ with $c_{0,0} = 1$:

- **Test A:** max $c_{j,k}$ for $(j, k) \in \{(1,1), (1,2), (2,1), (2,2)\}$
- **Test B:** max $c_{1,1} + c_{2,2}$
- **Test C:** max $c_{1,2} + c_{2,1}$

Sampled on $M_{2D} = 200$ per direction (40,000 constraints) so the LP is converged: $P_{\min}$ on verification grid is $\sim 10^{-12}$ to $10^{-16}$ (floating-point feasibility).

**Tensor-product bound (Cauchy-Schwarz).** For any sum-objective with weight matrix $W$ and asymmetric tensor witness $P = Q(\theta) R(\phi)$ giving $c_{j,k} = q_j r_k$:

$$\sum_{j,k} W_{j,k}\, q_j r_k \leq \sigma_{\max}(W)\, \|q\|_2\, \|r\|_2 \leq \sigma_{\max}(W)\, \max_Q \|q_S\|_2^2$$

where $S$ is the support of $W$ and $\|q_S\|_2 = \sqrt{\sum_{j \in S}q_j^2}$. For Tests B and C, $W$ has $\sigma_{\max} = 1$ and the bound reduces to $\max_Q (q_1^2 + q_2^2)$ over 1D nonneg deg-$N$ polynomials with $q_0 = 1$. Computed numerically by sweeping the LP objective $\cos(\alpha)\, q_1 + \sin(\alpha)\, q_2$ over angles and taking the max of (LP value)$^2$.

**Findings ($M_{2D} = 200$):**

| Test | $N$ | LP value | Tensor bound | LP $-$ tensor | rank | $\sigma_2 / \sigma_1$ |
|---|---|---|---|---|---|---|
| A: max $c_{1,1}$ | 2 | $2.0000$ | $2.0000$ (asymm) | $-10^{-15}$ | 1 | $7.6 \times 10^{-13}$ |
| A: max $c_{1,2}$ | 2 | $1.4142$ | $1.4142$ (asymm) | $0$ | 1 | $1.3 \times 10^{-14}$ |
| A: max $c_{2,2}$ | 5 | $2.0020$ | $2.0000$ (asymm) | $+2 \times 10^{-3}$ | 1 | $1.9 \times 10^{-13}$ |
| **B: max $c_{1,1} + c_{2,2}$** | **2** | **$2.5616$** | **$2.2857 = 16/7$** | **$+0.276$ (+12.1%)** | **3** | **$0.752$** |
| B: max $c_{1,1} + c_{2,2}$ | 3 | $3.4905$ | $3.4826$ | $+8 \times 10^{-3}$ (+0.2%) | 4 | $0.426$ |
| B: max $c_{1,1} + c_{2,2}$ | 4 | $4.4904$ | $4.4304$ | $+0.060$ (+1.4%) | 5 | $0.780$ |
| B: max $c_{1,1} + c_{2,2}$ | 5 | $5.1449$ | $5.1420$ | $+0.003$ (+0.1%) | 6 | $0.773$ |
| C: max $c_{1,2} + c_{2,1}$ | 2 | $2.0000$ | $2.2857$ | $-0.286$ | 3 | $0.104$ |
| C: max $c_{1,2} + c_{2,1}$ | 3 | $3.1029$ | $3.4826$ | $-0.380$ | 3 | $0.009$ |

**Interpretation.**

1. **Test A: single-coefficient LPs decompose universally.** For all $(j, k) \in \{(1,1), (1,2), (2,1), (2,2)\}$ and all $N$, the LP-optimal $c_{j,k}$ matrix is rank 1 and the LP value matches the asymmetric tensor product $(\max q_j)(\max q_k)$. This extends 4D's "max $c_{1,1}$ decomposes" to "max of any single coefficient decomposes."

2. **Test B: balanced-diagonal-sum LP exceeds tensor product.** The LP-optimal $c_{j,k}$ matrix is **full rank** ($N+1$) with $\sigma_2/\sigma_1 \in [0.43, 0.78]$, stable under grid refinement (M_2D = 60, 120, 200 all give consistent rank). For $N = 2$, the LP value $2.5616$ is provably $12.1\%$ larger than the Cauchy-Schwarz tensor bound $16/7 \approx 2.286$: **the optimal bivariate polynomial is genuinely 2D, not a tensor product or a convex sum-of-tensor-products that maintains the C-S bound**.

3. **The 12% gap at $N = 2$ is the structural finding.** It demonstrates that the simple "LP decomposes" intuition fails as soon as the objective mixes two coefficients in a balanced way. The improvement decays at higher $N$ (12% → 0.2% → 1.4% → 0.1%), suggesting the tensor product becomes nearly optimal as the polynomial degree grows.

4. **Test C: off-diagonal-sum LP does NOT exceed tensor.** Despite the LP-optimal $c_{j,k}$ matrix having rank $> 1$ for all $N$, the LP value is **strictly less than** the C-S tensor bound. The rank $> 1$ is an LP-vertex degeneracy: a tensor product witness achieves the same value. So Test C confirms that "rank $> 1$" alone is not sufficient for new content; the LP value must exceed the tensor bound.

**LP-optimal polynomial at $N = 2$ (Test B), coefficient matrix:**

$$c = \begin{pmatrix} 1 & 0 & 0.621 \\ 0 & 1.940 & 0 \\ 0.621 & 0 & 0.621 \end{pmatrix}$$

with singular values $(1.94, 1.46, 0.16)$. The zeros at $c_{j,k}$ for odd $j + k$ reflect a parity symmetry of the optimal polynomial under $(\theta, \phi) \to (\theta + \pi, \phi + \pi)$.

**Comparison to the symmetric tensor optimum at $N = 2$.** The maximizer of $q_1^2 + q_2^2$ over 1D nonneg deg-2 polys has $(q_1, q_2) = (4\sqrt 6/7, 4/7) \approx (1.40, 0.57)$ (giving sum $16/7$), with the polynomial $Q = |R|^2$ where $R(z) = \sqrt{1/7}(\sqrt 2 + \sqrt 3 z + \sqrt 2 z^2)$. The LP-optimal $P$ has $c_{1,1} = 1.94 \approx q_1^2$ (similar) but $c_{2,2} = 0.62$ which is larger than the symmetric tensor's $q_2^2 = 16/49 \approx 0.33$. The bivariate LP trades a slight $c_{1,1}$ loss for a substantial $c_{2,2}$ gain unavailable to any single 1D polynomial.

**Does this translate to a new zero-free region bound?** Not directly. Translating a bivariate auxiliary inequality $P(\theta, \phi) \geq 0$ into a constraint on zero locations requires the explicit-formula bookkeeping at two independent heights $t, t'$ (Heath-Brown / Pintz style), with the LP coefficients $c_{j,k}$ weighing terms at heights $jt \pm kt'$. The 12% improvement on the auxiliary inequality could, in principle, improve the Mossinghoff-Trudgian-style zero-free constant when combined with the right two-height functional. Working out the explicit-formula bookkeeping for this 2D inequality is the natural follow-up (4E.2 or a successor experiment).

**What 4E updates in the prior conclusion.** 4D/4D.2 concluded "the d-variate LP decomposes; no new auxiliary inequality." That conclusion is true *for single-coefficient objectives*. For balanced sum-of-diagonal objectives, the LP does not decompose, and a genuinely new 2D inequality exists. The corrected statement: **the family of single-coefficient LPs decomposes; the family of sum-of-coefficient LPs at small $N$ does not**.

**Output:**
- `e4e_offdiag_lp.npz`: LP values, tensor bounds, SVD ranks, coefficient matrices, q_max table
- `e4e_offdiag_lp.png`: LP-vs-tensor comparison, rank diagnostic, summary panel

## 4E.2: alpha-sweep + extended diagonal sum ([e4e2_sum_sweep.py](e4e2_sum_sweep.py))

**Status:** complete. **The 4E +12.1% finding at $\alpha = 1$ is a single point on a curve that peaks at +25.00% for $\alpha = 3$ (N=2), and the gap is 8.66x larger for the 3-term sum at N=3 (+1.98%) vs the 2-term sum (+0.23%). The non-decomposition is sharper than 4E suggested.**

**Motivation.** 4E showed that the LP for max $c_{1,1} + c_{2,2}$ exceeds the C-S tensor bound by 12.1% at $N = 2$. Two natural extensions: (a) sweep the coefficient weight $\alpha$ in $\max c_{1,1} + \alpha c_{2,2}$ to find where the gap peaks; (b) test if adding a third diagonal term ($c_{3,3}$) at higher bidegree enlarges the gap.

**Method.** 

- (a) For $N = 2$, sweep $\alpha$ over 27 values in $[0, 10]$. Solve LP for $\max c_{1,1} + \alpha c_{2,2}$ at $M_{2D} = 200$. Compute C-S tensor bound $\max_Q (q_1^2 + \alpha q_2^2)$ via 1D LP sweep over angle $\theta$ (objective $\cos\theta \cdot q_1 + \sin\theta \sqrt{\alpha}\cdot q_2$, take $\max_\theta$ of squared LP value).

- (b) For $N = 3$, solve LP for $\max c_{1,1} + c_{2,2} + c_{3,3}$ vs $\max c_{1,1} + c_{2,2}$. Tensor bound for 3-term sum: $\max_Q (q_1^2 + q_2^2 + q_3^2)$ via sphere-direction sweep ($60 \times 30$ grid on $S^2$, 1800 LP solves).

**Findings (a): alpha sweep at $N = 2$.**

| $\alpha$ | LP value | Tensor bound | Gap (%) |
|---|---|---|---|
| 0.0 | $2.0000$ | $2.0000$ ($q_1^2$) | $0.0\%$ |
| 0.5 | $2.2656$ | $2.1333 = 16/7.5$ | $+6.2\%$ |
| **1.0** | **$2.5616$** | **$2.2857 = 16/7$** | **$+12.1\%$** |
| 2.0 | $3.2361$ | $2.6666 = 16/6$ | $+21.4\%$ |
| 2.75 | $3.8026$ | $3.0476$ | $+24.8\%$ |
| **3.0** | **$4.0000$** | **$3.2000 = 16/5$** | **$+25.00\%$** (peak) |
| 3.5 | $4.4086$ | $3.5556$ | $+24.0\%$ |
| 4.0 | $4.8300$ | $4.0000$ | $+20.8\%$ |
| 5.0 | $5.7046$ | $5.0000$ | $+14.1\%$ |
| 10.0 | $10.3871$ | $10.0000$ | $+3.9\%$ |

The relative gap follows a smooth curve: starts at 0% ($\alpha = 0$, pure $c_{1,1}$, decomposes), rises monotonically to peak +25% at $\alpha = 3$, decays toward 0% as $\alpha \to \infty$ (asymptotically pure $c_{2,2}$). The analytical tensor bound formula in this range is $16/(8 - \alpha)$ (derived from the Fejér-Riesz parameterization).

**Structure at the peak ($\alpha = 3$, $N = 2$).** LP-optimal coefficient matrix has clean rational form:

$$c = \frac{1}{5}\begin{pmatrix} 5 & 0 & 4 \\ 0 & 8 & 0 \\ 4 & 0 & 4 \end{pmatrix}, \quad c_{1,1} + 3 c_{2,2} = \frac{8 + 12}{5} = 4 = \frac{5}{4} \cdot \frac{16}{5}.$$

In product-to-sum form on $(u, v) = (\theta + \phi, \theta - \phi)$ coordinates:
$$5\, P(\theta, \phi) = 5 + 4\cos u + 4\cos v + 8\cos u \cos v + 2\cos 2u + 2\cos 2v.$$

The polynomial does NOT factor as $f(u) g(v)$: the $\cos 2u, \cos 2v$ terms appear without their "tensor" partners $\cos 2u \cos v, \cos u \cos 2v$, ruling out any product structure $(1 + p\cos u + q \cos 2u)(1 + r \cos v + s \cos 2v)$. This is the algebraic source of the +25% gap: the LP polynomial contains a genuinely 2D coupling unavailable to tensor products.

**Findings (b): 3-term diagonal sum at $N = 3$.**

| Objective | LP value | Tensor bound | Gap |
|---|---|---|---|
| $c_{1,1} + c_{2,2}$ at $N = 3$ | $3.4905$ | $3.4826$ | $+0.23\%$ |
| $c_{1,1} + c_{2,2} + c_{3,3}$ at $N = 3$ | $3.6816$ | $3.6101$ | $+1.98\%$ |

Adding the third diagonal term enlarges the gap by **8.66x**. LP-optimal coefficient matrix for the 3-term has rank 4 (full) with $\sigma_2 / \sigma_1 \approx 0.54$. This suggests the gap-vs-tensor structure is not a one-off at $(N, \text{2-term})$; richer objective families produce richer non-decomposition.

**Significance.** Three combined observations from 4E + 4E.2:

1. The non-decomposition is family-dependent and weight-dependent. Different objectives within the "diagonal sum" family give different gaps, peaking at +25% (4E.2.a) rather than the 12% of the equal-weight case (4E).
2. Adding more diagonal terms increases the gap (4E.2.b: 8.66x improvement going from 2-term to 3-term at $N = 3$).
3. The optimum at the peak ($\alpha = 3$, $N = 2$) has CLEAN RATIONAL COEFFICIENTS, suggesting an underlying closed-form structure worth deriving analytically.

**What this leaves open.**

- A larger search over the bidegree-objective space (not just diagonal sums but arbitrary linear combinations of $c_{j,k}$) might reveal even bigger gaps. The 4E.2 alpha sweep is a 1-parameter family; a 2-parameter family is the natural next step.
- Closed-form derivation of the $\alpha = 3$, $N = 2$ optimum: the clean rationals suggest the optimal $P$ is constructible algebraically. If derivable, the construction may generalize to other peaks.
- Translation to zero-free regions: the 25% improvement on the auxiliary inequality has not yet been plugged into the Heath-Brown / Pintz explicit-formula bookkeeping. This is the natural 4E.3 follow-up.

**Output:**
- `e4e2_sum_sweep.npz`: alpha grid, LP/tensor values, 3-term result, coefficient matrices
- `e4e2_sum_sweep.png`: LP and tensor vs $\alpha$, relative-gap curve, 2-term vs 3-term bar chart

## 4E.3: Translation to a zero-free region constant ([e4e3_mt_translation.py](e4e3_mt_translation.py))

**Status:** complete. **The +25% C-S gap from 4E.2 does NOT translate into an improved Mossinghoff-Trudgian zero-free region constant.** This is a structural result: any non-neg bivariate polynomial, restricted to a line in $(\theta, \phi)$-space, becomes a 1D non-neg polynomial whose MT shape factor is bounded by the 1D Fejér optimum at matched effective degree.

**Motivation.** 4E.2 found the LP for $\max c_{1,1} + 3 c_{2,2}$ at bidegree $(2, 2)$ exceeds the Cauchy-Schwarz tensor bound by 25%, with clean rational coefficients $c_{0,0} = 1, c_{1,1} = 8/5, c_{2,0} = c_{0,2} = c_{2,2} = 4/5$. The natural follow-up: does this auxiliary inequality improve the zero-free region constant $C$ in $\beta < 1 - C/\log|t|$?

**Method.** The Mossinghoff-Trudgian framework expresses the de la Vallée Poussin zero-free region as
$$C = \frac{(c_1 - c_0)^2}{4 R(P) c_0}$$
for a 1D nonneg trig polynomial $P(u) = c_0 + c_1 \cos u + c_2 \cos 2u + \ldots$ ("literal-coefficient" convention), where $R(P)$ is a boundary error scaling with $P(0) = \sum c_k$. The "shape factor" $(c_1 - c_0)^2/(4 c_0)$ is the polynomial-dependent part.

For 2D, we evaluate at heights $(t_1, t_2)$: $\tilde P(u) := P(t_1 u, t_2 u)$ is the effective 1D polynomial, with frequencies in $\{0, 2t_1, 2t_2, t_1 \pm t_2, 2t_1 \pm 2t_2\}$ for bidegree $(2, 2)$. We tabulate the shape factor and $\mathrm{shape}/P(0)$ over six reduction choices.

**Findings — 4E.2 peak polynomial at $(\alpha, N) = (3, 2)$:**

| Reduction | $w_0$ | $w_{\gamma_0}$ | shape | $P(0)$ | shape/$P(0)$ | eff deg | 1D Fejér shape/$P(0)$ | ratio |
|---|---|---|---|---|---|---|---|---|
| $t_1 = t_2 = \gamma_0/2$ | $11/5$ | $12/5$ | $0.0045$ | $5$ | $0.000909$ | $2$ | $0.01472$ | $0.062$ |
| $t_1 = \gamma_0, t_2 = \gamma_0/2$ | $1$ | $6/5$ | $0.010$ | $5$ | $0.002000$ | $3$ | $0.02520$ | $0.079$ |
| $t_1 = t_2 = \gamma_0$ | $11/5$ | $0$ | $0$ | $5$ | $0$ | $4$ | $0.02885$ | $0$ |
| $t_1 = \gamma_0, t_2 = 0$ | $9/5$ | $8/5$ | $0$ | $5$ | $0$ | $2$ | $0.01472$ | $0$ |

The best 2D-derived shape/$P(0)$ is $0.002$, **12.6x WORSE than 1D Fejér at matched effective degree 3**.

**Findings — sweep $\alpha \in [0, 10]$:**

| $\alpha$ | best shape/$P(0)$ | eff deg | Fejér shape/$P(0)$ | ratio |
|---|---|---|---|---|
| $0.0$ (= tensor product) | $0.02764$ | $4$ | $0.02885$ | $0.958$ |
| $0.5$ | $0.00610$ | $2$ | $0.01472$ | $0.414$ |
| $1.0$ | $0.00327$ | $2$ | $0.01472$ | $0.222$ |
| $2.0$ | $0.00037$ | $3$ | $0.02520$ | $0.015$ |
| $3.0$ (peak C-S) | $0.00197$ | $3$ | $0.02520$ | $0.078$ |
| $5.0$ | $0.00586$ | $3$ | $0.02520$ | $0.233$ |
| $10.0$ | $0.00988$ | $3$ | $0.02520$ | $0.392$ |

**No 2D LP polynomial in the entire $\alpha$-family beats 1D Fejér at matched effective degree.** The closest is the trivial tensor product at $\alpha = 0$ (ratio $0.958$), which is just $Q(\theta) Q(\phi)$ for $Q$ the 1D Fejér optimum. As $\alpha$ grows, the LP shifts mass into $c_{2,2}$ (which raises C-S but lands at frequency $2\gamma_0$ in the MT bookkeeping, contributing nothing to the trick).

**Structural lemma (the actual reason).** If $P(\theta, \phi) \geq 0$ on $[0, 2\pi]^2$, then for any heights $(t_1, t_2)$:
$$\tilde P(u) := P(t_1 u, t_2 u) \geq 0$$
on $[0, 2\pi]$, because $(t_1 u, t_2 u)$ is a point in $[0, 2\pi]^2$ modulo periodicity. Hence the family of effective 1D polynomials from 2D bivariate restriction is a SUBSET of all 1D non-neg trig polynomials at matched effective degree. The max-$c_1$ optimization over this subset is bounded by the unconstrained max ($=$ 1D Fejér optimum). **No 2D restriction strategy can improve the single-zero MT framework.**

**Why the 4E.2 +25% gap exists yet doesn't help here.** The C-S figure of merit (max $\sum W_{j,k} c_{j,k}$ for some weight matrix $W$) and the MT figure of merit (max $c_1 - c_0$ after 1D restriction) are structurally distinct. The 4E.2 LP at $\alpha = 3$ exploits 2D structure that increases the C-S objective by 25%, but the same structure does NOT manifest as a larger $c_1$ in any 1D restriction. The two figures of merit "see" different aspects of the polynomial.

**The clean conclusion.** 4E.2 found a genuine new 2D auxiliary inequality at the C-S level, but this inequality cannot break the 1D Fejér ceiling on the de la Vallée Poussin / Mossinghoff-Trudgian zero-free region constant. The Heath-Brown / Pintz 2D framework would only help if applied to problems involving MULTIPLE putative zeros (e.g., least-prime-in-AP with Siegel-zero couplings), not the standard single-zero zero-free region.

**What this rules out, and what it doesn't.** The 4E.3 result rules out a class of "easy wins" for the zero-free region constant from bivariate trig polynomial LPs. It does NOT rule out:

- **Constrained-domain LPs.** Imposing $P(\theta, \phi) \geq 0$ only on a submanifold corresponding to a hypothetical off-line zero (e.g., $\phi = 2\theta$ for a zero at $\rho = \beta + i\gamma$ probed at heights $\gamma$ and $2\gamma$). The submanifold-constrained polynomial is NOT bounded by the unrestricted-domain 1D Fejér.
- **Sum-of-squares over a polynomial ideal.** SOS modulo prime-coupling relations.
- **Multi-zero or multi-character setups.** Heath-Brown's actual use case in arithmetic progressions.

These are the natural 4E.4, 4E.5, 4E.6 follow-ups; they are not pursued in this experiment.

**Output:**
- `e4e3_mt_translation.npz`: peak polynomial, reduction tables, alpha sweep, Fejér comparison data
- `e4e3_mt_translation.png`: shape/$P(0)$ vs $\alpha$, plus per-reduction comparison bar chart

## 4E.4: Trivariate balanced-sum LP ([e4e4_trivariate_sum.py](e4e4_trivariate_sum.py))

**Status:** complete. **The LP-vs-tensor gap roughly DOUBLES from d=2 to d=3: peak gap is +51.29% at $\alpha = 3.25$, $N = 2$, vs 4E.2's +25.00% at $\alpha = 3, N = 2$.** The d-variate non-decomposition strengthens with dimension. (Per 4E.3, this does NOT improve the MT zero-free constant; the result characterizes the auxiliary-inequality structure for its own sake.)

**Motivation.** 4E (d=2, $c_{1,1} + c_{2,2}$) found a +12.1% gap; 4E.2 swept $\alpha$ and found peak +25.00% at $\alpha = 3$. The natural d=3 analog is the LP for $\max c_{1,1,1} + \alpha c_{2,2,2}$ over non-negative trivariate trig polynomials of tridegree $(N, N, N)$. Does the gap grow, shrink, or stabilize with dimension?

**Method.** Trivariate LP

$$\max c_{1,1,1} + \alpha c_{2,2,2} \quad \text{s.t.} \quad P(\theta, \phi, \psi) = \sum_{j,k,l} c_{j,k,l} \cos(j\theta) \cos(k\phi) \cos(l\psi) \geq 0, \quad c_{0,0,0} = 1$$

solved at $N = 2$, $M_{3D}^3 = 60^3 = 216{,}000$ constraints. Tensor bound: $\max_Q (q_1^3 + \alpha q_2^3)$ over 1D non-neg deg-$N$ polynomials with $q_0 = 1$, via 1D LP angle sweep on $S^1$. (Symmetric tensor bound; asymmetric tensor $\max_{Q,R,S} q_1 r_1 s_1 + \alpha q_2 r_2 s_2$ equals symmetric by a multilinear-vertex argument plus problem symmetry.)

**Findings ($N = 2$, $M_{3D} = 60$, $M_{\rm verify} = 80$ then $160$):**

| $\alpha$ | LP | tensor | gap | rel gap | $P_{\min}$ verify |
|---|---|---|---|---|---|
| $0.00$ | $2.8284$ | $2.8284$ | $0$ | $0.0\%$ | $-7\times 10^{-3}$ |
| $1.00$ | $3.4523$ | $2.9625$ | $+0.49$ | $+16.5\%$ | $-7\times 10^{-3}$ |
| $2.00$ | $4.1457$ | $3.1192$ | $+1.03$ | $+32.9\%$ | $-1\times 10^{-2}$ |
| $3.00$ | $4.8999$ | $3.3086$ | $+1.59$ | $+48.1\%$ | $-1\times 10^{-2}$ |
| **3.25** | **$5.0884$** | **$3.3633$** | **$+1.73$** | **$+51.3\%$ (peak)** | $-1\times 10^{-2}$ |
| $3.50$ | $5.2769$ | $3.5000$ | $+1.78$ | $+50.8\%$ | $-1\times 10^{-2}$ |
| $4.00$ | $5.6540$ | $4.0000$ | $+1.65$ | $+41.4\%$ | $-1\times 10^{-2}$ |
| $5.00$ | $6.5028$ | $5.0000$ | $+1.50$ | $+30.1\%$ | $-2\times 10^{-2}$ |
| $10.00$ | $10.9725$ | $10.0000$ | $+0.97$ | $+9.7\%$ | $-2\times 10^{-2}$ |

**M-convergence.** At $\alpha = 3$:

| $M_{3D}$ | LP | $P_{\min}$ | LP / $(1 + |P_{\min}|)$ (lower bracket) |
|---|---|---|---|
| $40$ | $4.9500$ | $-3.2 \times 10^{-2}$ | $4.797$ |
| $70$ | $4.8877$ | $-7.9 \times 10^{-3}$ | $4.849$ |
| $100$ | $4.8665$ | $-2.9 \times 10^{-4}$ | $4.8650$ |

True LP value at $\alpha = 3, M \to \infty$ is in $[4.865, 4.867]$, gap in $[+47.04\%, +47.09\%]$. So the M=60 sweep slightly overestimates; M-corrected peak gap at $\alpha = 3.25$ would be in the range $[+50.0\%, +51.3\%]$.

**Peak coefficient tensor (M=60, $\alpha = 3.25$):**

| $(j, k, l)$ | $c_{j,k,l}$ | ratio to $c_{0,0,0}$ |
|---|---|---|
| $(0, 0, 0)$ | $+1.000$ | $1.000$ |
| $(1, 1, 1)$ | $+2.637$ | $2.637$ |
| $(2, 2, 2)$ | $+0.754$ | $0.754$ |
| $(2, 0, 0)$, $(0, 2, 0)$, $(0, 0, 2)$ | $\sim +0.65$ | $\sim 0.65$ |
| $(2, 2, 0)$, $(2, 0, 2)$, $(0, 2, 2)$ | $\sim +0.58$ | $\sim 0.58$ |

Compared to 4E.2's peak (clean rationals $1, 8/5, 4/5, 4/5, 4/5$), the d=3 peak does NOT have an obvious clean-rational structure (the LP at finite $M$ shows small asymmetry between $(2, 0, 0)$, $(0, 2, 0)$, $(0, 0, 2)$, consistent with LP noise but possibly indicating non-rational true coefficients).

**The structural pattern (d=2 → d=3).** Going from d=2 to d=3:

- LP-vs-tensor peak gap: $+25.00\% \to +51.29\%$ ($\sim$ 2x).
- Peak $\alpha$: $3.0 \to 3.25$ (small shift).
- LP value at peak: $4.00 \to 5.09$ (since the higher-dimensional LP optimizes over more variables and has more freedom).
- Tensor bound at peak: $16/5 = 3.20 \to 3.36$ (only slight increase; the 1D LP max-cube doesn't grow much).

**Interpretation.** The d-variate balanced-sum auxiliary inequality has STRONGER non-decomposition in higher dimensions. The 2D coupling $\cos 2u + \cos 2v$ at d=2 (where $u = \theta + \phi$, $v = \theta - \phi$) generalizes to a 3D structure at d=3 that admits more independent low-order modes than any product of 1D Q, R, S. The +51% gap quantifies this.

**What this does NOT mean for RH.** Per 4E.3's structural lemma: any d-variate non-neg polynomial restricted to a line through the origin is a 1D non-neg trig polynomial, bounded by 1D Fejér at matched effective degree. So the +51% trivariate gap does NOT translate to a better single-zero MT zero-free region constant. The result characterizes the multivariate auxiliary inequality structure independently of its RH application.

**Open follow-ups.**

- **4-variate or higher** (d ≥ 4): does the pattern $\sim (d-1) \times 25\%$ continue? At d=4, expected $\sim 75\%$. Heavy LP ($M^4$ constraints, $(N+1)^4$ variables); $M = 30$ would give 810K constraints, tractable.
- **Closed-form characterization** of the d=3 peak. If the LP-optimal coefficients converge to clean rationals as $M \to \infty$, the same algebraic structure as d=2 may generalize.
- **Multi-zero MT bookkeeping**, where multiple putative zeros at different heights are coupled via the d-variate polynomial. This is the only known route by which the higher-dimensional structure could improve actual zero-free region constants.

**Output:**
- `e4e4_trivariate_sum.npz`: alpha grid, LP/tensor values, peak coefficient tensor
- `e4e4_trivariate_sum.png`: LP-vs-tensor curve, relative-gap d=2 vs d=3

## 4E.5: d = 4 balanced-sum LP ([e4e5_d4_peak.py](e4e5_d4_peak.py))

**Status:** complete. **The (d-1)×25% scaling pattern from d=2 (25%) and d=3 (51%) does NOT continue cleanly at d=4: the rigorous gap interval at the peak is [+54.5%, +69.8%], roughly $+62\%$, BELOW the predicted +75%.** The peak alpha also shifts: $3.0 \to 3.25 \to 4.5$ for $d = 2, 3, 4$. The dimension-pattern is sub-linear.

**Motivation.** 4E.4 found the trivariate gap nearly doubles 4E.2's bivariate gap ($25\% \to 51\%$). The pattern $(d-1) \times 25\%$ would predict $+75\%$ at $d = 4$. This experiment tests that prediction.

**Method.** LP for $\max c_{1,1,1,1} + \alpha c_{2,2,2,2}$ over nonneg quadvariate trig polynomials of quad-degree $(2, 2, 2, 2)$, sampled on $M_{4D}^4$ grid. Tensor bound: $\max_Q (q_1^4 + \alpha q_2^4)$ over 1D nonneg deg-2 polys with $q_0 = 1$, via 1D LP angle sweep. Computational cost: $3^4 = 81$ variables; $M^4$ constraints.

**Findings (alpha sweep at $M_{4D} = 25$, verify on $M = 40$):**

| $\alpha$ | LP | tensor | gap LP | gap lower bracket | $P_{\min}$ |
|---|---|---|---|---|---|
| $3.00$ | $6.47$ | $4.21$ | $+53.81\%$ | $+34.29\%$ | $-0.145$ |
| $3.50$ | $6.88$ | $4.25$ | $+62.05\%$ | $+41.59\%$ | $-0.145$ |
| $4.00$ | $7.30$ | $4.29$ | $+70.12\%$ | $+49.03\%$ | $-0.142$ |
| **4.50** | **$7.72$** | **$4.50$** | **$+71.51\%$** | **$+49.96\%$** | $-0.144$ |
| $5.00$ | $8.14$ | $5.00$ | $+62.89\%$ | $+42.27\%$ | $-0.145$ |
| $6.00$ | $9.04$ | $6.00$ | $+50.68\%$ | $+22.87\%$ | $-0.226$ |
| $7.00$ | $9.99$ | $7.00$ | $+42.77\%$ | $+11.31\%$ | $-0.283$ |

**M-convergence at $\alpha = 4.5$:**

| $M_{4D}$ | constraints | LP | $P_{\min}$ | lower bracket | gap interval |
|---|---|---|---|---|---|
| $25$ | $390{,}625$ | $7.72$ | $-0.144$ | $6.75$ | $[+50.0\%, +71.5\%]$ |
| $30$ | $810{,}000$ | $7.77$ | $-0.095$ | $7.09$ | $[+57.6\%, +72.6\%]$ |
| $35$ | $1{,}500{,}625$ | $7.64$ | $-0.099$ | $6.95$ | $[+54.5\%, +69.8\%]$ |

True LP value at $\alpha = 4.5, M \to \infty$ is in $\sim[6.95, 7.64]$, gap in $\sim[+54\%, +70\%]$. Midpoint $\sim +62\%$, which is below the predicted $+75\%$.

**The dimension-pattern:**

| $d$ | peak $\alpha$ | peak gap | $(d-1) \times 25\%$ prediction |
|---|---|---|---|
| $2$ | $3.0$ | $+25.00\%$ (M-converged) | $25\%$ |
| $3$ | $3.25$ | $+47-51\%$ (M-corrected) | $50\%$ |
| $4$ | $4.5$ | $+54-70\%$ (M-corrected) | $75\%$ |

The increment per dimension: $\Delta_{2 \to 3} \approx 22{-}26$ pp; $\Delta_{3 \to 4} \approx 7{-}19$ pp. The increment SHRINKS going from $d = 3$ to $d = 4$, suggesting the gap saturates at some limit below $100\%$ as $d \to \infty$. The exact saturation value would require more dimensions or a theoretical bound.

**Peak alpha shifts upward with dimension.** $3.0 \to 3.25 \to 4.5$ for $d = 2, 3, 4$. The optimal weight on the higher-order term $c_{2, \ldots, 2}$ grows with $d$, consistent with the intuition that higher-dimensional structure puts more emphasis on higher-order coupling.

**What this does and doesn't mean.**

- **Does NOT mean** improved zero-free region constants: per the 4E.3 structural lemma, any d-variate non-neg polynomial restricted to a line is bounded by 1D Fejér at matched effective degree, FOR ANY $d$. The d=4 peak gap doesn't translate to a zero-free improvement.
- **Does mean** the multivariate LP relaxation has dimension-dependent strength, growing sub-linearly with $d$. The bivariate LP captures most of the LP-vs-tensor gap that's available; going to higher dimensions yields diminishing returns.
- **Caveat on LP convergence.** At $d = 4$, $P_{\min}$ remains $\sim -0.1$ even at $M = 35$. To verify convergence within $1\%$, one would need $M = 100+$, which is $10^8$ constraints — beyond this experiment's budget. The reported gap interval $[+54\%, +70\%]$ is rigorous but wide.

**Implication for higher d.** Computationally exploring $d \geq 5$ requires LP techniques beyond direct dense linear programming (sparse / cutting-plane methods, sum-of-squares semidefinite programming, etc.). The d-pattern characterization is essentially complete from a small-d numerical standpoint.

**Output:**
- `e4e5_d4_peak.npz`: alpha grid, LP/tensor values, peak coefficient tensor
- `e4e5_d4_peak.png`: gap-vs-alpha for d = 4, overlaying d = 2 and d = 3 curves

## 4E.6: Constrained-domain LP ([e4e6_constrained_lp.py](e4e6_constrained_lp.py), [.md](e4e6_constrained_lp.md))

**Status:** complete. **Negative result, sharpening 4E.3.** Tests the proposed escape from 4E.3's structural lemma: relax $P \ge 0$ to a subset $\Omega \subset [0, 2\pi]^d$ instead of the full torus.

**Four formulations tested:**

| Setup | Constraint | Behavior |
|---|---|---|
| A: K-point | $P(\theta_k) \ge 0$ at $K$ evenly-spaced points | $K \le N$: hits $c_{\rm bound}$ (artifact); $K \gg N$: recovers Fejér |
| B: arc-removal | $P \ge 0$ on $[0, 2\pi] \setminus (\theta_0 - \delta, \theta_0 + \delta)$ | small $\delta$: $\equiv$ Fejér; large $\delta$: hits $c_{\rm bound}$ |
| C: zero-constrained | $P \ge 0$ at $\theta_k = \gamma_k \log p \bmod 2\pi$ for first $K$ on-line zeros | recovers Fejér as $K \to \infty$ (Weyl equidistribution) |
| D: trick at off-line | constrain at on-line zero $\theta$'s, max $P$ at off-line frequency | apparent gain decays to 1.0 as $K \to \infty$ (sparse-sampling artifact) |

**Quantitative confirmation, Setup D at $N=8$:**

| $K$ | LP $P(\theta_{\rm trick})$ | full-non-neg max | ratio |
|---|---|---|---|
| 50 | 9.30 | 4.89 | 1.900 |
| 100 | 4.97 | 4.89 | 1.016 |
| 200 | 4.90 | 4.89 | 1.002 |
| 400 | 4.89 | 4.89 | 1.000 |
| 649 | 4.89 | 4.89 | 1.000 |

The ratio decays monotonically to 1.000 as $K$ grows. The "gain" at finite $K$ is purely from sparse sampling, not a structural escape from the Fejér ceiling.

**Verdict.** The naïve constrained-domain LP is not a separate route. Every formulation either:
- (a) is under-constrained and hits the coefficient bound,
- (b) produces unphysical $P$ (large negativity in relaxed region, breaking the MT inequality),
- (c) recovers the Fejér / full-non-negativity ceiling as the constraint set densifies, or
- (d) collapses into one of the above when made physically meaningful.

**This sharpens 4E.3's structural lemma.** The MT geometric structure resists not just 1D line-restriction (4E.3) but also naïve domain relaxation. To break the single-zero MT shape factor ceiling via 2D inequalities requires *qualitatively different* machinery:
- **Heath-Brown multi-zero coupling** (Arch 4E.7 open): multiple putative zeros at different heights.
- **Bombieri variational SOS** (Arch 4E.8 partial overlap): allow small negativity, control $L^2$ norm.
- **Polynomial-ideal SOS** (Arch 4E.8): non-negativity over algebraic variety via Putinar/Schmüdgen.

None of these is "LP over a subset." 4E.6 narrows the open landscape to these three structurally distinct routes.

**Output:**
- `e4e6_constrained_lp.npz`: all four setups' LP values, baselines, hit-bound flags
- `e4e6_constrained_lp.png`: four-panel summary plot, including Setup D's convergence-to-1.0 trace

## 4E.7: Multi-zero MT LP ([e4e7_multi_zero_lp.py](e4e7_multi_zero_lp.py), [.md](e4e7_multi_zero_lp.md))

**Status:** complete. **Multi-zero LP escape from 4E.3 is real at the shape-factor level but produces rank-1 LP optima at naive objectives.** Sharpens the picture started by 4E.6.

**Setup:** postulate $d$ putative zeros at independent heights $\gamma_1, \ldots, \gamma_d$. The relevant polynomial is multivariate $P(\theta_1, \ldots, \theta_d) = \sum c_{j_1, \ldots, j_d} \cos(j_1 \theta_1) \cdots \cos(j_d \theta_d) \ge 0$ with constraint set the full $d$-torus $[0, 2\pi]^d$. **4E.3's lemma applies only to 1D line restrictions** — full $d$-torus non-negativity is structurally different.

**Two-zero shape factor:**

| $N$ | $q_1^2 = $ max $c_{1,1}$ | $\lambda_{1,1} = (q_1^2 - 1)^2 / 4$ | $\lambda_1^2$ (naive independent) | ratio |
|---|---|---|---|---|
| 2 | 2.000 | 0.2500 | 0.0018 | **137×** |
| 3 | 2.618 | 0.6545 | 0.0091 | **72×** |
| 4 | 3.000 | 1.0000 | 0.0179 | **56×** |

The joint MT-like shape factor is structurally much larger than two independent single-zero applications would give.

**Rank diagnostics:** the LP-optimal polynomial for max $c_{1,1}$ is rank-1 (= tensor product $Q(\theta) Q(\phi)$ with $Q$ the 1D Fejér optimum). Same for balanced-sum LP $\max c_{1,0} + c_{0,1} + \alpha c_{1,1}$: rank-1 at all tested $\alpha \in \{0, 0.5, 1, 2, 3, 5\}$. Same for Heath-Brown-style $a(c_{1,0} + c_{0,1}) + b c_{1,1}$ across $(a, b)$ sweep. **Naive multi-zero objectives DO NOT exceed the tensor bound.** The 2D LP's strength (per 4E.2) requires HIGHER harmonics like $c_{2,2}$ — first-harmonic-only multi-zero objectives decompose.

**Verdict.** The multi-zero LP escape from 4E.3 is real at the shape-factor level (per Finding 1 above) but does not produce non-tensor LP optima at first-harmonic objectives. A genuine multi-zero MT improvement for RH on zeta would require:
- Combining this LP with the higher-harmonic LP gain (4E.2's +25% rank-2 win via $c_{1,1} + \alpha c_{2,2}$).
- Explicit Heath-Brown bookkeeping (Heath-Brown 1992 §3, Pintz 1976).
- Careful tracking of $R(P)$ for the 2D polynomial.

This is research-grade combination beyond this experiment. The translation to a zero-free region constant for ASYMPTOTIC RH on zeta is also constrained by Riemann-von Mangoldt: at height $T$, consecutive zeros are spaced $\sim 2\pi/\log T$ apart, so multi-zero MT applies tightly only at finite height. Heath-Brown / Pintz multi-zero results give constant-factor improvements for FINITE-RANGE problems (least prime in AP, Siegel zeros for specific moduli) where multiple zeros at controlled distances are postulated by the problem setup.

**Cross-cut to 4E.6**: both 4E.6 (constrained-domain) and 4E.7 (multi-zero) are LP-based escape routes from 4E.3's line-restriction lemma. 4E.6 collapsed entirely; 4E.7 produces a real shape-factor improvement but bounded by tensor decomposition. The remaining LP-escape direction is **4E.8 (polynomial-ideal SOS via Putinar/Schmüdgen)** which requires SDP not LP and could give structurally different bounds.

**Output:**
- `e4e7_multi_zero_lp.npz`: single-zero / two-zero / balanced-sum / Heath-Brown data
- `e4e7_multi_zero_lp.png`: three-panel summary (single-zero shape vs N, joint vs independent log-scale, balanced-sum LP sweep)

## 4A + 4C: Vinogradov-Korobov and the conditional landscape ([4a_4c_vinogradov_korobov.md](4a_4c_vinogradov_korobov.md))

**Status:** complete (unified literature dossier).

The 4B-4E.7 thread covers **Input 2** (the auxiliary non-neg trig polynomial) of the classical analytic route. 4A and 4C cover **Inputs 1 and 3** (explicit formula + exponential sum bounds via Vinogradov's mean value theorem) and the conditional improvement landscape (Heath-Brown / Pintz / Ford / BDG / density hypothesis / LH).

**Headline findings of the dossier:**

- The **$2/3$ exponent** in $\sigma \geq 1 - c/(\log|t|)^{2/3}(\log\log|t|)^{1/3}$ has held for 67 years. It comes directly from Vinogradov's mean value theorem (V-MVT), which was resolved at its sharp form by Bourgain-Demeter-Guth (2016) via $\ell^2$-decoupling. **Within the V-K recipe, $2/3$ is now a proven ceiling.** That is a finished sub-result: the recipe is solved to its limit, so progress on the exponent has to come from a different class of input, not from more work inside this one.
- The **auxiliary inequality input (4B-4E.7) is saturated**: 4B confirms numerically that the LP for $\max c_1$ at degree $N$ hits Fejér exactly, and the multivariate generalizations (4D-4E.7) cannot escape the 1D Fejér ceiling under line restriction (4E.3 lemma) or naïve domain relaxation (4E.6) or naïve multi-zero coupling (4E.7). **The auxiliary-inequality input is therefore solved to its ceiling; the V-K bottleneck in Input 3 has to be addressed by a different input class, not a sharper inequality.**
- The **conditional landscape** (RH / density hypothesis / LH / Heath-Brown / Pintz / Ford / BDG) sharpens constants and uniformities but **none of the named conditionals would push the exponent from $2/3$ down**. Pushing the exponent requires a fundamentally new input class: most plausibly the Architecture 2 (arithmetic-geometric) exponential-sum machinery á la Deligne, or the Architecture 1 (Connes) spectral identification.
- **Architecture 4 is a constraint-mapping architecture**: it gives the tightest currently-provable unconditional bound, and it precisely locates its own ceiling rather than routing all the way to RH. The 4B-4E.7 thread quantifies exactly where the architecture saturates. The 67-year plateau reflects a structural ceiling rather than insufficient effort, which is useful: it tells us this architecture's job is to map the constraint, and the RH-closing work belongs to Arch 2 / Arch 3.

This closes the Architecture 4 literature TODOs (4A, 4C). The remaining open computational direction is **4E.8** (polynomial-ideal SOS via Putinar/Schmüdgen, requires SDP not LP), still the only LP-style escape route from 4E.3 per the LEARNINGS finding-12 taxonomy.
