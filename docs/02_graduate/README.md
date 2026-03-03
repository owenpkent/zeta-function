# The Riemann Zeta Function — Graduate Level

> **Level:** Graduate — assumes complex analysis (Cauchy's theorem, contour integration, analytic continuation), and real analysis.

---

## 1. Analytic Continuation via the Gamma Function

The **Gamma function** is the key tool for continuing $\zeta(s)$ beyond $\text{Re}(s) > 1$.

$$\Gamma(s) = \int_0^\infty t^{s-1} e^{-t}\, dt \qquad \text{Re}(s) > 0$$

It satisfies $\Gamma(s+1) = s\,\Gamma(s)$ and $\Gamma(n) = (n-1)!$ for positive integers. It extends meromorphically to all of $\mathbb{C}$ with simple poles at $s = 0, -1, -2, \ldots$

**Key identity:** Substituting $t \mapsto n^s t$ in the Gamma integral:

$$\Gamma(s) = n^s \int_0^\infty t^{s-1} e^{-nt}\, dt \implies \frac{\Gamma(s)}{n^s} = \int_0^\infty t^{s-1} e^{-nt}\, dt$$

Summing over $n$:

$$\Gamma(s)\,\zeta(s) = \int_0^\infty \frac{t^{s-1}}{e^t - 1}\, dt \qquad \text{Re}(s) > 1$$

This integral representation is the starting point for analytic continuation.

---

## 2. The Functional Equation — Proof Sketch

### Via the Theta Function

Define the **Jacobi theta function**:

$$\theta(t) = \sum_{n=-\infty}^{\infty} e^{-\pi n^2 t} \qquad t > 0$$

The **Poisson summation formula** gives the functional equation of theta:

$$\theta(1/t) = \sqrt{t}\;\theta(t)$$

Now define the **completed zeta function** (also called $\xi$ or $\Lambda$):

$$\Lambda(s) = \pi^{-s/2}\,\Gamma\!\left(\tfrac{s}{2}\right)\zeta(s) = \int_0^\infty t^{s/2-1}\,\frac{\theta(t)-1}{2}\, dt$$

Splitting the integral at $t=1$ and applying $\theta(1/t) = \sqrt{t}\,\theta(t)$:

$$\Lambda(s) = \frac{1}{s(s-1)} + \int_1^\infty \left(t^{s/2-1} + t^{(1-s)/2-1}\right)\frac{\theta(t)-1}{2}\, dt$$

The right-hand side is **symmetric under $s \mapsto 1-s$**, so:

$$\boxed{\Lambda(s) = \Lambda(1-s)}$$

This is the functional equation. Unwinding the definition gives Riemann's original form:

$$\zeta(s) = 2^s\,\pi^{s-1}\,\sin\!\left(\tfrac{\pi s}{2}\right)\Gamma(1-s)\,\zeta(1-s)$$

---

## 3. The Hadamard Product

Since $\xi(s) = \frac{1}{2}s(s-1)\Lambda(s)$ is an entire function of order 1, the **Hadamard factorization theorem** gives:

$$\xi(s) = e^{A+Bs}\prod_\rho \left(1 - \frac{s}{\rho}\right)e^{s/\rho}$$

where the product runs over all non-trivial zeros $\rho$. Here:
- $A = \xi(0) = 1/2$
- $B = \xi'(0)/\xi(0) = -\frac{1}{2}\ln(4\pi) - 1 + \frac{\gamma}{2}$ where $\gamma$ is the Euler–Mascheroni constant

Taking the logarithmic derivative:

$$\frac{\zeta'}{\zeta}(s) = B - \frac{1}{s-1} + \frac{1}{2}\ln\pi - \frac{1}{2}\frac{\Gamma'}{\Gamma}\!\left(\tfrac{s}{2}+1\right) + \sum_\rho\left(\frac{1}{s-\rho} + \frac{1}{\rho}\right)$$

This **explicit formula** for $\zeta'/\zeta$ encodes all zeros explicitly and is the analytic engine behind the explicit formula for $\pi(x)$.

---

## 4. The Explicit Formula for $\pi(x)$

Define the von Mangoldt function $\Lambda(n) = \log p$ if $n = p^k$ (prime power), 0 otherwise.

The **Chebyshev function** $\psi(x) = \sum_{n \leq x} \Lambda(n)$ (equivalent to $\pi(x)$ up to lower-order terms).

Via Perron's formula and the Hadamard product:

$$\psi(x) = x - \sum_\rho \frac{x^\rho}{\rho} - \frac{\zeta'}{\zeta}(0) - \frac{1}{2}\log(1-x^{-2})$$

The dominant term is $x$. Each non-trivial zero $\rho = \beta + i\gamma$ contributes:

$$-\frac{x^\rho}{\rho} = -\frac{x^\beta}{\vert\rho\vert} x^{i\gamma} e^{i\,\text{arg}(\rho)}$$

which is an oscillating term of amplitude $x^\beta / |\rho|$.

**If RH holds ($\beta = 1/2$ for all $\rho$):** Every correction term has amplitude $O(x^{1/2})$, giving:

$$\psi(x) = x + O(\sqrt{x}\,\log^2 x)$$

**If RH fails** (some $\rho$ with $\beta > 1/2$): corrections grow faster than $\sqrt{x}$.

---

## 5. Zero-Free Regions

The **classical zero-free region** (de la Vallée Poussin, 1899):

$$\zeta(s) \neq 0 \quad \text{for} \quad \sigma \geq 1 - \frac{c}{\log |t|}, \quad |t| \geq 2$$

for some absolute constant $c > 0$. This is sufficient to prove the PNT with an error term.

**Best known zero-free region** (Vinogradov–Korobov, 1958):

$$\sigma \geq 1 - \frac{c}{(\log |t|)^{2/3}(\log\log|t|)^{1/3}}$$

These zero-free regions are far from the critical line. Getting them to touch $\text{Re}(s) = 1/2$ would prove RH.

---

## 6. The Density Hypothesis and Zero Counting

Define $N(T) = \#\{\rho : 0 < \text{Im}(\rho) < T\}$, the count of zeros up to height $T$.

**Riemann–von Mangoldt formula:**

$$N(T) = \frac{T}{2\pi}\log\frac{T}{2\pi} - \frac{T}{2\pi} + O(\log T)$$

The zeros are countably infinite but densely packed at height $T$: average gap $\sim 2\pi/\log(T/2\pi)$.

**Hardy's theorem (1914):** Infinitely many zeros lie on the critical line.

**Hardy–Littlewood (1921):** At least $cT$ zeros in $[0,T]$ are on the critical line for some $c > 0$.

**Selberg (1942):** A positive proportion of zeros are on the critical line.

**Levinson (1974):** At least 1/3 of all zeros are on the critical line.

**Conrey (1989):** At least 2/5 of all zeros are on the critical line.

**Computational:** All zeros with $|\text{Im}(\rho)| \leq 3 \times 10^{12}$ have $\text{Re}(\rho) = 1/2$ (Platt, 2011).

---

## 7. The Lindelöf Hypothesis

A consequence of RH (but weaker):

**Lindelöf Hypothesis:** For any $\varepsilon > 0$:
$$\zeta\!\left(\tfrac{1}{2} + it\right) = O(t^\varepsilon) \quad \text{as } t \to \infty$$

Best known unconditional bound: $O(t^{13/84})$ (Bourgain, 2017). RH would give essentially $O(t^\varepsilon)$.

---

## 8. Random Matrix Theory Connection

Montgomery (1973) computed the **pair correlation** of the imaginary parts of zeros: for test functions $f$,

$$\sum_{\gamma, \gamma'} f(\gamma - \gamma') \sim \int_{-\infty}^\infty f(t)\left[1 - \left(\frac{\sin\pi t}{\pi t}\right)^2\right] dt$$

This is exactly the **pair correlation of eigenvalues of random unitary matrices** (GUE — Gaussian Unitary Ensemble) from random matrix theory.

Dyson pointed this out to Montgomery immediately. It is one of the deepest unexplained connections in mathematics: **the zeros of $\zeta(s)$ behave like eigenvalues of a random Hermitian matrix.** This is the spectral/operator interpretation of RH.

---

## What's Next?

- **[Research level →](../03_research/README.md)** — Operator approaches, L-functions, arithmetic geometry
- **[Solutions/approaches →](../solutions/README.md)** — Deep dive into proof strategies
- **[Visualizations →](../../visualizations/)** — Contour plots, zero distributions, pair correlation
