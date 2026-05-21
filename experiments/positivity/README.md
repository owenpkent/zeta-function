# Architecture 3: Direct Positivity (Weil / Li)

> Per the [project plan](../PROOF_ARCHITECTURES_PLAN.md), this is the most computationally tractable of the four proof architectures. RH is equivalent to **positivity** of certain quantities. Two main flavors:
>
> - **Li coefficients** $\lambda_n = \sum_\rho [1 - (1 - 1/\rho)^n]$: RH iff $\lambda_n \geq 0$ for all $n \geq 1$ (Li 1997).
> - **Weil quadratic form** $Q(f) = \sum_\rho \hat f(\rho)\overline{\hat f(\bar\rho)}$: RH iff $Q$ is positive semi-definite on Schwartz functions (Weil 1952).

## 3A: Zeta Li coefficients

**Status:** complete; positivity confirmed for $n = 1, \ldots, 500$.

**Method:** [e3a_zeta_li.py](e3a_zeta_li.py). Incremental product algorithm: precompute $w_\rho = 1 - 1/\rho$ for each zero, maintain `power[k] = w_k^n`, advance by multiplication. Total work $O(n_{\max} \cdot |\text{zeros}|)$ multiplications; on the critical line $|w_\rho| = 1$ exactly so precision is preserved.

**Findings (T_max = 2000, 1517 zeros, n_max = 500):**

| Quantity | Computed | Theory | Note |
|---|---|---|---|
| Positivity | $\lambda_n > 0$ for all $n \in [1, 500]$ | $\lambda_n > 0$ under RH (Li 1997) | Pass |
| $\lambda_1$ | $0.02256$ | $0.02310$ (Brent 2003) | $-2.3\%$, truncation |
| $\lambda_{10}$ | $2.226$ | $2.243$ (Brent 2003 extrapolated) | $-0.8\%$, truncation |
| Leading slope | $0.344$ | $0.500$ | Truncation-limited |
| Linear constant | $-0.405$ | $-0.708$ | Truncation-limited |

**Truncation analysis:** Missing tail (zeros with $\gamma > T$) contributes $\Delta_n \sim \frac{n^2 \log T}{2\pi T}$. For our parameters at $n = 500$: $\Delta_{500} \sim 290$ vs $\lambda_{500} \sim 1700$ true value, so truncation is around 17%. The slope error in the asymptotic fit scales similarly. To reach slope accuracy 0.01 via the zero-sum method, we would need $T \gtrsim 10^4$, requiring $\sim 12{,}000$ zeros at $\sim 0.25$ seconds each via `mp.zetazero`, hence about an hour. Feasible but not pursued: the qualitative result (positivity) is already established.

**What this proves and what it does not:**

- Proves nothing about RH directly; it merely **confirms RH-consistent behavior** in the regime tested.
- Validates the computational framework end-to-end (`LFunction` interface, incremental product algorithm, zero loader).
- Establishes a baseline against which 3B (D-H control) and 3D (adversarial search) will be measured.

**Output:**
- `e3a_zeta_li.npz`: arrays of $n$, $\lambda_n$, leading-order prediction, residual
- `e3a_zeta_li.png`: three-panel plot (values, residual, log-log growth)

## 3B: Davenport-Heilbronn Li coefficients (per-zero diagnostic)

**Status:** complete; central negative result documented.

**Method:** [e3b_dh_li.py](e3b_dh_li.py). Computes Li coefficients for both zeta and D-H over the same $n$ range with the same $T_{\max}$. Also computes $|w_\rho| - 1$ for every zero of both functions.

**Findings (T_max = 200, n_max = 300):**

| Quantity | zeta | D-H |
|---|---|---|
| zeros below $T = 200$ | 79 | 69 |
| off-line zeros | 0 | 8 (four quadruples) |
| max $|w_\rho| - 1$ | $1.1 \times 10^{-16}$ (float noise) | $4.20 \times 10^{-5}$ |
| $\lambda_n$ negative count (n=1..300) | 0 | 0 |

**Central negative result:** at $n \leq 300$, both zeta and D-H satisfy $\lambda_n > 0$. **The small-n Li-positivity test does not distinguish zeta from D-H.** It is *not* a valid wrong-approach detector at computationally tractable $n$.

**Why:** the first D-H off-line zero has

$$|w_\rho|^2 - 1 = \frac{1 - 2\beta}{\beta^2 + \gamma^2} \approx -8.4 \times 10^{-5}$$

so $|w_\rho| \approx 1 - 4.2 \times 10^{-5}$. The off-line contribution to $\lambda_n$ grows like $|w|^n - 1 \sim n \cdot |w-1|$, becoming order 1 only at $n \sim 1/|w-1| \approx 23{,}800$. The eight off-line zeros below $T=200$ all have similar magnitudes; the largest forces $n \approx 23{,}800$ as the crossover.

**Two implications:**

1. **The Weil quadratic form, not Li coefficients, is the right diagnostic** (covered in 3C). The Weil form picks up phase information from $\hat f(\rho)\overline{\hat f(\bar\rho)}$ that is sensitive to $\rho \neq \bar\rho^*$ even at small "$n$" (test function support).
2. **For Li coefficients themselves**, distinguishing the cases requires the **xi-derivative formula** $\lambda_n = \frac{1}{(n-1)!} \frac{d^n}{ds^n}[s^{n-1}\log\xi(s)]_{s=1}$. This avoids the zero sum entirely and could reach $n \sim 25{,}000$ where D-H negativity is expected. Implementation requires care: at that order, Taylor coefficients $T_k$ decay like $85.7^{-k}$ while binomial weights grow like $e^n$, so the sum is a delicate cancellation needing $\geq 100$-digit precision. Tracked as a separate todo (3B-extension).

**Output:**
- `e3b_dh_li.npz`: arrays of $\lambda_n$ for both, $|w|$ diagnostics, per-zero contributions
- `e3b_dh_li.png`: 4-panel plot (|w| distribution, $\lambda_n$ comparison, difference, per-zero contributions at $n = 100$)

## 3C: Weil quadratic form on Mellin-symmetric test functions

**Status:** complete; wrong-approach detector found via Gram-matrix extension.

### 3C.1: parameterized sweep ([e3c_weil_form.py](e3c_weil_form.py))

**Method:** test family $\Phi_b(s) = 2\sinh((s - \tfrac{1}{2})\log b) / (s - \tfrac{1}{2})$. Symmetric under $s \to 1-s$. On the critical line, $\Phi_b(\tfrac{1}{2} + i\gamma) = 2\sin(\gamma\log b)/\gamma$, real. Off the critical line, complex. The quadratic form is $W(b) := \sum_\rho \Phi_b(\rho)^2$.

**Findings (T_max = 200, b sweep over $[1.1, 100]$, 50 values):**

| Quantity | Range |
|---|---|
| $W_\zeta(b)$ | $[0.043, 0.113]$ (always positive) |
| $W_{DH}(b)$ | $[0.116, 0.549]$ (always positive) |
| D-H off-line zero contribution alone | $[-6.4 \times 10^{-3}, +1.0 \times 10^{-2}]$ |
| Sign changes of off-line contribution over $b$ sweep | 22 |
| Off-line / total ratio | up to $\sim 2\%$ |

**Conclusion:** off-line zeros DO contribute negatively for some $b$, but in the simple one-parameter $\Phi_b$ family the on-line contribution dominates by a factor of $\sim 50$. The sweep alone does not produce $W_{DH}(b) < 0$.

### 3C.2: Gram-matrix extension ([e3c2_weil_gram.py](e3c2_weil_gram.py))

**Method:** pick a basis grid $\{b_1, \ldots, b_K\}$. Any linear combination $\hat f = \sum_k c_k \Phi_{b_k}$ gives $W(\vec c) = \vec c^\top M \vec c$ where $M_{jk} = \sum_\rho 2\,\mathrm{Re}(\Phi_{b_j}(\rho)\Phi_{b_k}(\rho))$. Eigenvalue analysis: $M^\zeta$ is the Gram matrix of REAL vectors $\{\Phi_{b_k}(\rho)\}_k$ over zeros $\rho$, hence positive semi-definite. $M^{DH}$ has complex contributions from off-line zeros and may have negative eigenvalues.

**Findings (K = 30 basis points, $b \in [1.1, 1000]$, T_max = 200):**

| Quantity | $M^\zeta$ | $M^{DH}$ |
|---|---|---|
| Eigenvalue range | $[3.7 \times 10^{-3}, 0.69]$ | $[-0.0913, 4.78]$ |
| Negative eigenvalues | 0 (PSD) | 2 (witness) |

**Witness vector** $\vec c$ (smallest-eigenvalue eigenvector of $M^{DH}$):

- $W_{DH}(\vec c) = -0.0913 < 0$ — violates Weil positivity
- $W_\zeta(\vec c) = +0.0918 \geq 0$ — consistency check passes
- Magnitudes essentially equal, signs opposite

**This is the wrong-approach detector in finite-dimensional form.** Any RH-style argument that would prove $W(\hat f) \geq 0$ uniformly over $\hat f$ in the span of $\{\Phi_{b_k}\}$ for D-H is wrong: we have a finite-computation finite-dimensional witness that it fails.

The mechanism: on-line zeros contribute $\Phi_b(\rho) \in \mathbb{R}$, so they form a real Gram structure (automatically PSD). Off-line zeros contribute $\Phi_b(\rho) \in \mathbb{C}$, breaking the real-vector structure and permitting indefinite eigenvalues.

## 3D: scaling of the witness ([e3d_scaling.py](e3d_scaling.py))

**Status:** complete. The witness is robust and scales with basis size.

**K scaling** (basis size, fixed $T_{\max} = 200$):

| $K$ | $\lambda_{\min}(M^\zeta)$ | $\lambda_{\min}(M^{DH})$ |
|---|---|---|
| 10 | $+0.022$ | $+0.011$ (no witness yet) |
| 20 | $+9.8 \times 10^{-3}$ | $-0.024$ (first witness) |
| 30 | $+3.7 \times 10^{-3}$ | $-0.091$ |
| 50 | $+6.5 \times 10^{-5}$ | $-0.091$ |
| 75 | $+6.7 \times 10^{-9}$ | $-0.164$ |
| 100 | $-1 \times 10^{-16}$ | $-0.370$ |
| 150 | $-3 \times 10^{-16}$ | $-0.599$ |

The witness in $M^{DH}$ DEEPENS as $K$ grows (the adversarial linear combination becomes more effective). $M^\zeta$ trends toward singularity as the basis becomes redundant (the $\Phi_b$ functions span only a rank-bounded subspace of entire-function values at zeros), but remains PSD within numerical noise.

**T_max scaling** (fixed $K = 30$):

| $T_{\max}$ | D-H off-line zeros | $\lambda_{\min}(M^{DH})$ |
|---|---|---|
| 50 | 0 | $\sim 0$ (M^DH trivially PSD; no off-line yet) |
| 100 | 2 | $-0.095$ |
| 150 | 4 | $-0.094$ |
| 200 | 8 | $-0.091$ |
| 300 | 10 | $-0.088$ |

The witness appears as soon as the first off-line zero ($\gamma = 85.7$) is included, then stabilizes. Adding more on-line zeros doesn't dilute the signature, and adding more off-line zeros doesn't significantly compound it (the first off-line pair is already enough).

**Structural conclusion (3A-3D):** The Weil quadratic form with Gram-matrix eigenvalue analysis IS a valid wrong-approach detector for D-H, in stark contrast to small-n Li positivity (3B), which fails. The witness arises from a finite-dimensional spectral test in a basis of test functions, and its magnitude scales meaningfully with basis size while remaining stable under zero-count changes.

## 3E

Literature-and-analysis task connecting Li coefficients to the de Bruijn-Newman constant; deferred.
