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

## 4A, 4C

- **4A** (Vinogradov-Korobov reproduction): substantial literature work; deferred.
- **4C** (conditional improvements: Heath-Brown, Pintz, Ford): literature mapping; deferred.
