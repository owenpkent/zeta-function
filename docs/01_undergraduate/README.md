# The Riemann Zeta Function — Undergraduate Level

> **Level:** Undergraduate — assumes calculus, basic series, and introductory complex numbers.

---

## 1. The Zeta Function as a Series

The [Riemann zeta function](https://en.wikipedia.org/wiki/Riemann_zeta_function) is defined for real $s > 1$ by the **[Dirichlet series](https://en.wikipedia.org/wiki/Dirichlet_series)**:

$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} = \frac{1}{1^s} + \frac{1}{2^s} + \frac{1}{3^s} + \cdots$$

**Convergence:** This series [converges absolutely](https://en.wikipedia.org/wiki/Absolute_convergence) for $\text{Re}(s) > 1$. For $s = 1$, it becomes the [harmonic series](https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)) $\sum 1/n$, which diverges. For $s \leq 1$ (real), the series diverges.

### Special Values (real $s$)

| $s$ | $\zeta(s)$ | Notes |
|-----|-----------|-------|
| 2 | $\pi^2/6 \approx 1.6449$ | [Basel problem](https://en.wikipedia.org/wiki/Basel_problem) (Euler, 1734) |
| 4 | $\pi^4/90 \approx 1.0823$ | |
| 6 | $\pi^6/945$ | |
| Even integers | $\zeta(2n) = \frac{(-1)^{n+1} B_{2n} (2\pi)^{2n}}{2(2n)!}$ | $B_{2n}$ = [Bernoulli numbers](https://en.wikipedia.org/wiki/Bernoulli_number) |
| Odd integers ≥ 3 | Unknown closed form | $\zeta(3) \approx 1.202$ ([Apéry's constant](https://en.wikipedia.org/wiki/Ap%C3%A9ry%27s_constant)) |

---

## 2. The Euler Product Formula

[Euler](https://en.wikipedia.org/wiki/Leonhard_Euler) discovered a stunning connection between the zeta function and the prime numbers:

$$\zeta(s) = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}} = \frac{1}{1-2^{-s}} \cdot \frac{1}{1-3^{-s}} \cdot \frac{1}{1-5^{-s}} \cdots$$

**Why this works:** Each factor $\frac{1}{1-p^{-s}} = 1 + p^{-s} + p^{-2s} + \cdots$ is a [geometric series](https://en.wikipedia.org/wiki/Geometric_series). The [fundamental theorem of arithmetic](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic) (unique prime factorization) guarantees that multiplying all these together reproduces every term $n^{-s}$ exactly once.

This is the first bridge between $\zeta(s)$ and the primes. The zeta function **encodes all prime numbers** in its Euler product.

**Corollary:** Since $\zeta(1)$ diverges (harmonic series), and $\zeta(s) \neq 0$ for $s > 1$, the Euler product implies there are infinitely many primes. (If only finitely many, the product would be finite and couldn't diverge.)

---

## 3. Complex Numbers — Brief Review

A complex number $s = \sigma + it$ where $\sigma, t \in \mathbb{R}$ and $i^2 = -1$.

- $\sigma = \text{Re}(s)$ is the **real part**
- $t = \text{Im}(s)$ is the **imaginary part**
- The complex plane: $\sigma$ on the horizontal axis, $t$ on the vertical axis

For $\text{Re}(s) > 1$, the Dirichlet series converges absolutely even when $s$ is complex. So $\zeta(s)$ is a well-defined **complex function** on the half-plane $\{s : \text{Re}(s) > 1\}$.

The modulus: $|n^{-s}| = n^{-\sigma}$, so absolute convergence depends only on the real part.

---

## 4. Analytic Continuation — The Big Idea

The series $\sum n^{-s}$ only converges for $\text{Re}(s) > 1$. But there is a unique way to **extend** $\zeta(s)$ to (almost) the entire [complex plane](https://en.wikipedia.org/wiki/Complex_plane) while preserving differentiability (analyticity). This is called **[analytic continuation](https://en.wikipedia.org/wiki/Analytic_continuation)**.

The key idea: two analytic functions that agree on an open set must agree everywhere they're both defined. So there's at most one way to continue $\zeta(s)$ beyond $\text{Re}(s) > 1$.

**The result:** $\zeta(s)$ extends to all of $\mathbb{C}$ except for a **[simple pole](https://en.wikipedia.org/wiki/Pole_(complex_analysis)) at $s = 1$** with residue 1.

One useful intermediate step — valid for $\text{Re}(s) > 0$, $s \neq 1$:

$$\zeta(s) = \frac{1}{s-1} + \sum_{n=1}^{\infty} \left(\frac{1}{n^s} - \int_n^{n+1} \frac{dt}{t^s}\right)$$

Another approach uses the **[Dirichlet eta function](https://en.wikipedia.org/wiki/Dirichlet_eta_function)** (alternating Dirichlet series):

$$\eta(s) = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^s} = 1 - \frac{1}{2^s} + \frac{1}{3^s} - \cdots$$

This converges for $\text{Re}(s) > 0$. And $\eta(s) = (1 - 2^{1-s})\,\zeta(s)$, so:

$$\zeta(s) = \frac{\eta(s)}{1 - 2^{1-s}} \qquad \text{for } \text{Re}(s) > 0,\; s \neq 1$$

---

## 5. The Functional Equation

The fully continued zeta function satisfies a beautiful symmetry called the **[functional equation](https://en.wikipedia.org/wiki/Riemann_zeta_function#The_functional_equation)**:

$$\zeta(s) = 2^s \pi^{s-1} \sin\!\left(\frac{\pi s}{2}\right) \Gamma(1-s)\, \zeta(1-s)$$

Or equivalently, defining the **completed zeta function** using the [gamma function](https://en.wikipedia.org/wiki/Gamma_function) $\Gamma$:

$$\xi(s) = \frac{1}{2} s(s-1)\,\pi^{-s/2}\,\Gamma\!\left(\frac{s}{2}\right)\zeta(s)$$

the functional equation becomes simply:

$$\xi(s) = \xi(1-s)$$

This is a **reflection symmetry** around the vertical line $\text{Re}(s) = 1/2$. The function is symmetric about the critical line.

**Consequence for zeros:**
- If $\zeta(\rho) = 0$, then $\zeta(1 - \rho) = 0$. Zeros come in pairs reflected across $\text{Re}(s) = 1/2$.
- The trivial zeros at $s = -2, -4, -6, \ldots$ come from the $\sin(\pi s/2)$ factor.
- All other zeros (non-trivial) must lie in the **critical strip** $0 < \text{Re}(s) < 1$.

---

## 6. The Critical Strip and the Riemann Hypothesis

The **critical strip** is the region $0 < \text{Re}(s) < 1$.

The **critical line** is $\text{Re}(s) = 1/2$.

We know:
- $\zeta(s) \neq 0$ on the line $\text{Re}(s) = 1$ (proved by [Hadamard](https://en.wikipedia.org/wiki/Jacques_Hadamard) and [de la Vallée Poussin](https://en.wikipedia.org/wiki/Charles_Jean_de_la_Vall%C3%A9e_Poussin) in 1896 — this was enough to prove the [Prime Number Theorem](https://en.wikipedia.org/wiki/Prime_number_theorem))
- $\zeta(s) \neq 0$ on $\text{Re}(s) = 0$ (by functional equation symmetry with $\text{Re}(s) = 1$)
- All non-trivial zeros have $0 < \text{Re}(s) < 1$

The first few non-trivial zeros (computed):

| Zero | Approximate location |
|------|---------------------|
| $\rho_1$ | $1/2 + 14.134725\ldots i$ |
| $\rho_2$ | $1/2 + 21.022040\ldots i$ |
| $\rho_3$ | $1/2 + 25.010858\ldots i$ |
| $\rho_4$ | $1/2 + 30.424876\ldots i$ |
| $\rho_5$ | $1/2 + 32.935062\ldots i$ |

All real parts are exactly $1/2$.

**The [Riemann Hypothesis](https://en.wikipedia.org/wiki/Riemann_hypothesis):** Every non-trivial zero $\rho$ satisfies $\text{Re}(\rho) = 1/2$.

---

## 7. Connection to Prime Counting

Define $\pi(x)$ = number of primes $\leq x$ (the [prime-counting function](https://en.wikipedia.org/wiki/Prime-counting_function)).

The **Prime Number Theorem** (PNT): $\pi(x) \sim \frac{x}{\ln x}$ as $x \to \infty$.

Riemann's explicit formula makes this precise using the zeros $\rho$:

$$\pi(x) = \text{Li}(x) - \sum_{\rho} \text{Li}(x^\rho) - \ln 2 + \int_x^\infty \frac{dt}{t(t^2-1)\ln t}$$

where $\text{Li}(x) = \int_2^x \frac{dt}{\ln t}$ (the [logarithmic integral](https://en.wikipedia.org/wiki/Logarithmic_integral_function)) and the sum is over non-trivial zeros.

**Each zero $\rho$ contributes an oscillatory correction term $\text{Li}(x^\rho)$** to the count of primes. The zeros are literally the "harmonics" that shape how primes are distributed.

If the Riemann Hypothesis is true, the error in the PNT approximation is as small as possible:

$$|\pi(x) - \text{Li}(x)| = O(\sqrt{x}\,\ln x)$$

If false (some zero off the critical line), the error is larger.

---

## What's Next?

- **[Graduate level →](../02_graduate/README.md)** — Gamma function, contour integrals, proof of the functional equation
- **[Visualizations →](../../visualizations/)** — See analytic continuation and the critical strip in action
- **[Implications →](../implications/README.md)** — PNT, error bounds, and beyond
