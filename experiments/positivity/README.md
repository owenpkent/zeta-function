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

## 3C, 3D, 3E

Planned per the [project plan](../PROOF_ARCHITECTURES_PLAN.md). 3C and 3D depend on a working Weil-quadratic-form evaluator (to be built in `e3c_weil_form.py`); 3E is a literature-and-analysis task connecting Li coefficients to the de Bruijn-Newman constant.
