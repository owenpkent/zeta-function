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

## 4A, 4C, 4D

- **4A** (Vinogradov-Korobov reproduction): substantial literature work; deferred.
- **4C** (conditional improvements: Heath-Brown, Pintz, Ford): literature mapping; deferred.
- **4D** (structurally new auxiliary inequalities beyond non-neg trig polys): the real way to break the exponent; open research direction.
