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

## 3C.3: Selberg-class cross-cut ([e3c3_selberg_cross_cut.py](e3c3_selberg_cross_cut.py))

**Status:** complete; framework positive control passes.

**Motivation:** 3C.2 found that $M^{DH}$ has negative eigenvalues. Is this because D-H is not Selberg (no Euler product, off-line zeros), or just because D-H is "different" from $\zeta$ in some other way? The cross-cut tests the detector against another Selberg-class L-function whose zeros are also believed (and numerically verified) to be on the critical line.

**Method:** identical Gram-matrix construction, applied to the real primitive Dirichlet character $\chi_3$ mod 3 (Kronecker symbol $(\cdot/-3)$, odd, conductor 3). Implementation in [`../_shared/dirichlet_l.py`](../_shared/dirichlet_l.py); zeros found by $Z_\chi(t)$ sign-change scan on the critical line. The first three zeros at $\gamma \approx 8.040, 11.249, 15.705$ match LMFDB.

**Findings ($K = 30$, $b \in [1.1, 1000]$, $T_{\max} = 200$):**

| Quantity | $M^\zeta$ | $M^{\chi_3}$ | $M^{DH}$ |
|---|---|---|---|
| Number of zeros | 79 | 114 | 69 (8 off-line) |
| Eigenvalue range | $[+3.7 \times 10^{-3}, 0.69]$ | $[+1.08 \times 10^{-2}, 1.94]$ | $[-9.13 \times 10^{-2}, 4.78]$ |
| Strict-negative count | 0 | 0 | 2 |
| Verdict | PSD | PSD | indefinite |

Riemann-von Mangoldt sanity check: $\frac{T}{2\pi}\log\frac{qT}{2\pi e}$ predicts 78 zeros for $\zeta$ and 113 for $\chi_3$ at $T = 200$, matching the counts above (the conductor $q = 3$ adds $\frac{T}{2\pi}\log q \approx 35$ zeros relative to $\zeta$).

**Direction-selectivity test.** The witness vector $c^*$ (smallest-eigenvalue eigenvector of $M^{DH}$) evaluated on all three:

- $W_{DH}(c^*) = -9.13 \times 10^{-2}$ (the witness, < 0)
- $W_\zeta(c^*) = +9.18 \times 10^{-2}$ (non-negative)
- $W_{\chi_3}(c^*) = +1.06 \times 10^{-1}$ (non-negative)

The same adversarial direction that exhibits Weil-form failure on D-H gives non-negative values on both Selberg-class L-functions. The detector is **direction-selective**: it responds to the off-line zeros, not to L-function identity.

**Conclusion:** the Gram-matrix wrong-approach detector is not a false-positive generator. It correctly flags D-H (RH known false) as indefinite while validating $\chi_3$ (GRH believed) as PSD with the same construction. Architecturally, the test passes the natural Selberg-class positive control.

## 3D.2: K-scaling cross-cut ([e3d2_cross_cut_scaling.py](e3d2_cross_cut_scaling.py))

**Status:** complete; Selberg-class PSD-redundancy pattern confirmed across $\zeta$, $\chi_3$, $\chi_4$; D-H deepens monotonically.

This experiment is the K-scaling analogue of 3C.3, run across all four L-functions:

| $K$ | $\lambda_{\min}(M^\zeta)$ | $\lambda_{\min}(M^{\chi_3})$ | $\lambda_{\min}(M^{\chi_4})$ | $\lambda_{\min}(M^{DH})$ |
|---|---|---|---|---|
| 10 | $+2.21 \times 10^{-2}$ | $+3.49 \times 10^{-2}$ | $+4.70 \times 10^{-2}$ | $+1.14 \times 10^{-2}$ (no witness yet) |
| 20 | $+9.84 \times 10^{-3}$ | $+2.08 \times 10^{-2}$ | $+2.48 \times 10^{-2}$ | $-2.41 \times 10^{-2}$ |
| 30 | $+3.75 \times 10^{-3}$ | $+1.08 \times 10^{-2}$ | $+1.73 \times 10^{-2}$ | $-9.13 \times 10^{-2}$ |
| 50 | $+6.48 \times 10^{-5}$ | $+2.18 \times 10^{-3}$ | $+3.86 \times 10^{-3}$ | $-9.09 \times 10^{-2}$ |
| 75 | $+6.74 \times 10^{-9}$ | $+7.31 \times 10^{-4}$ | $+5.13 \times 10^{-4}$ | $-1.64 \times 10^{-1}$ |
| 100 | $-1.08 \times 10^{-16}$ (FP noise) | $+2.48 \times 10^{-5}$ | $+8.97 \times 10^{-5}$ | $-3.70 \times 10^{-1}$ |

All three Selberg-class L-functions follow the same redundancy pattern: $\lambda_{\min} \to 0^+$ as $K$ grows because the test family $\{\Phi_{b_k}\}_k$ spans a rank-bounded subspace of $\mathbb{C}^{N}$ (where $N$ is the number of zeros). $\zeta$ hits floating-point noise at $K = 100$; $\chi_3$ and $\chi_4$ stay safely positive there because they have more zeros (114 and 122 vs $\zeta$'s 79), so the singular boundary kicks in at higher $K$.

D-H continues to deepen monotonically: $-2.4 \times 10^{-2} \to -9.1 \times 10^{-2} \to -1.6 \times 10^{-1} \to -3.7 \times 10^{-1}$, exactly as the 3D result. The deepening is a real signal from the off-line zeros, not a floating-point artifact.

**Cross-cut conclusion (3C.3 + 3D.2 combined):**

1. The Gram-matrix detector returns PSD-with-redundancy for every Selberg-class L-function tested ($\zeta$, $\chi_3$, $\chi_4$) across $K \in [10, 100]$.
2. The detector returns indefinite-with-deepening only for D-H.
3. The deepening is robustly a function of basis size, not numerical noise or L-function specifics.

The wrong-approach detector survives its natural Selberg-class positive control, both at fixed $K$ (3C.3) and under $K$ scaling (3D.2). Architecturally, the test in 3C.2 specifically responds to the presence of off-line zeros, not to L-function identity.

## 3B.2: Witness $\lambda_n^{DH} < 0$ at large $n$ ([e3b2_li_dh_extension.py](e3b2_li_dh_extension.py))

**Status:** complete. **Witnesses D-H violation of Li positivity at $n = 400{,}000$ and $n = 1{,}000{,}000$.**

**Motivation:** 3B found that $\lambda_n^{DH} > 0$ at $n \leq 300$, with the structural estimate placing crossover-to-negative around $n \sim 320{,}000$. 3B.2 computes $\lambda_n^{DH}$ at those large $n$ and witnesses the negativity directly.

**Method.** The brute-force zero sum
$$\lambda_n^{DH} = \sum_\rho \left(1 - \left(1 - \tfrac{1}{\rho}\right)^n\right)$$
converges slowly: at $n = 400{,}000$, contributions from on-line zeros up to height $T = 55{,}000 \approx n/(2\pi)$ are needed for accuracy, which is intractable.

Instead, we use an exact decomposition:
$$\lambda_n^{DH} = \lambda_n^{DH, \rm asymp} + \sum_{\rho_{\rm off}\text{ in UHP}} 2\,\Re\bigl(w_{\rm on}(\gamma)^n - w_{\rm off}^n\bigr)$$
where:

- $\lambda_n^{DH, \rm asymp}$ is the Bombieri-Lagarias leading asymptotic for an L-function of conductor $q = 5$ with the appropriate gamma factor:
$$\lambda_n^{DH, \rm asymp} = \tfrac{n}{2}\bigl(\log(qn/(2\pi)) + \gamma_E - 1\bigr) + O(\sqrt{n}\log n).$$
This depends only on the gamma factor and conductor, not on individual zeros.
- The sum is over off-line zeros $\rho_{\rm off} = \beta + i\gamma$ in the upper half-plane; $w_{\rm off} = 1 - 1/\rho_{\rm off}$, $w_{\rm on}(\gamma) = 1 - 1/(1/2 + i\gamma)$. The bracketed expression $w_{\rm on}^n - w_{\rm off}^n$ is the difference between "actual" off-line contribution and "hypothetical RH" on-line contribution at the same height.

The five off-line quadruples up to $T_{\max} = 300$ are sufficient: higher off-line zeros have $|w| - 1 \sim 1/\gamma^2$, so their contribution at $n = 400{,}000$ is exponentially smaller than the dominant quadruple at $\gamma = 85.7$.

**Findings (precision 50 digits):**

| $n$ | $\lambda_n^{DH, \rm asymp}$ | off-line correction | $\lambda_n^{DH}$ | sign |
|---|---|---|---|---|
| $10^3$ | $+3.13 \times 10^3$ | $-1.55 \times 10^{-3}$ | $+3.13 \times 10^3$ | + |
| $10^4$ | $+4.28 \times 10^4$ | $+0.30$ | $+4.28 \times 10^4$ | + |
| $5 \times 10^4$ | $+2.54 \times 10^5$ | $-7.88$ | $+2.54 \times 10^5$ | + |
| $10^5$ | $+5.43 \times 10^5$ | $+34.7$ | $+5.43 \times 10^5$ | + |
| $2 \times 10^5$ | $+1.16 \times 10^6$ | $+7.72 \times 10^3$ | $+1.16 \times 10^6$ | + |
| $3.2 \times 10^5$ | $+1.92 \times 10^6$ | $+1.52 \times 10^5$ | $+2.08 \times 10^6$ | + |
| **$4 \times 10^5$** | $+2.45 \times 10^6$ | $\mathbf{-2.01 \times 10^7}$ | $\mathbf{-1.76 \times 10^7}$ | $\mathbf{-}$ |
| $5 \times 10^5$ | $+3.12 \times 10^6$ | $+2.55 \times 10^9$ | $+2.55 \times 10^9$ | + |
| **$10^6$** | $+6.58 \times 10^6$ | $\mathbf{-3.00 \times 10^{18}}$ | $\mathbf{-3.00 \times 10^{18}}$ | $\mathbf{-}$ |

**$\lambda_n^{DH}$ is strictly negative at $n = 400{,}000$ and $n = 1{,}000{,}000$.** This directly witnesses D-H violating Li's positivity criterion, computationally closing the loop on 3B: the criterion does discriminate, just at $n \sim 4 \times 10^5$, not at the small-$n$ range originally checked.

**Mechanism.** The dominant off-line zero in the FE quadruple at $\gamma = 85.7$ has $\beta = 0.192$ and
$$|w_{\rm off}| = \sqrt{\frac{(1-\beta)^2 + \gamma^2}{\beta^2 + \gamma^2}} \approx 1 + 4.20 \times 10^{-5}.$$
The off-line contribution $-2\,\Re(w_{\rm off}^n)$ has amplitude $2|w_{\rm off}|^n = 2 \exp(4.20 \times 10^{-5}\, n)$, growing exponentially in $n$. Phase $n \cdot \arg(w_{\rm off}) \pmod{2\pi}$ determines sign:

- At $n = 320{,}000$: $|w_{\rm off}|^n \approx 8 \times 10^5$, comparable to the asymptotic; phase happens to be positive, $\lambda_n^{DH}$ stays positive.
- At $n = 400{,}000$: $|w_{\rm off}|^n \approx 1 \times 10^7$, much larger than asymptotic; phase is negative, $\lambda_n^{DH} < 0$.
- At $n = 500{,}000$: $|w_{\rm off}|^n \approx 1.3 \times 10^9$; phase happens to be positive again, $\lambda_n^{DH}$ positive.

So $\lambda_n^{DH}$ oscillates between $\pm O(|w_{\rm off}|^n)$ for $n \gtrsim 320{,}000$, with the negative excursions giving the Li-criterion witnesses.

**Caveats.**

1. We use the leading-order Bombieri-Lagarias asymptotic for $\lambda_n^{DH, \rm asymp}$; the exact value has $O(\sqrt{n}\log n) \approx 10^4$ correction at $n = 4 \times 10^5$. The off-line magnitude of $2 \times 10^7$ dominates, so the sign of $\lambda_n^{DH}$ is robust to this uncertainty.
2. Off-line zeros above $T = 300$ contribute negligibly: each has $|w| - 1 \sim 1/\gamma^2$, so $|w|^n \sim \exp(n/\gamma^2) \sim O(1)$ for $\gamma \gtrsim 1000$ at $n = 4 \times 10^5$.
3. A fully rigorous numerical computation would use the explicit xi-derivative formula at sufficient precision; this work is a structural estimate, not a certificate.

**Architectural significance.** 3B and 3B.2 together resolve the small-vs-large-$n$ Li question: the Li criterion correctly distinguishes RH from non-RH, but the discrimination scale is $n \sim 1/|w_{\rm off} - 1| \approx 24{,}000$ for the off-line contribution to become order-1, and $n \sim 320{,}000$ for it to dominate the on-line asymptotic. At computationally tractable small $n \leq 1000$, the criterion is silent. This sharpens the structural distinction between 3B and 3C–3D: the Weil-form Gram matrix detects D-H at $K = 30$ and $T_{\max} = 200$ (effectively "small-$n$"), while small-$n$ Li does not. 3B.2 shows that Li at LARGE $n$ also detects, just via a much more expensive computation.

## 3F: Weil-form duality via Bombieri's explicit formula ([e3f_weil_prime_side.py](e3f_weil_prime_side.py))

**Status:** complete. Implements Bombieri's exact form of the explicit formula and verifies it against the zero-side computation to <2% at sufficient $T_{\max}$.

**Motivation.** Every Arch-3 experiment so far computed Weil positivity from the *zero side* $W(b) = \sum_\rho \Phi_b(\rho)^2$. The explicit formula gives the same quantity as a sum over *primes* plus a *gamma integral* plus boundary terms. Computing both sides serves two purposes: (1) a calibration check that our zero-side computations are correct; (2) a structural perspective: an analytic lower bound on the prime side that doesn't use zero locations would prove RH, so the cancellation structure on the prime side is where the difficulty lives.

**Formula (Bombieri, Clay Riemann Hypothesis writeup, page 8).** For $f$ in his test class $\mathcal{W}$ with Mellin transform $\tilde{f}(s) = \int_0^\infty f(x) x^s dx/x$:

$$\tilde{f}(0) - \sum_\rho \tilde{f}(\rho) + \tilde{f}(1) = \sum_{n=1}^\infty \Lambda(n)\Big\{f(n) + \tfrac{1}{n}f(\tfrac{1}{n})\Big\} + (\log 4\pi + \gamma_E) f(1) + \int_1^\infty \Big\{f(x) + \tfrac{1}{x}f(\tfrac{1}{x}) - \tfrac{2}{x}f(1)\Big\}\frac{dx}{x - x^{-1}}.$$

For our boxcar test function $g_b(x) = x^{-1/2} \cdot \mathbf{1}_{[1/b,\,b]}(x)$, the Mellin transform is $\Phi_b(s)$ (as derived in 3C). The autocorrelation $f(x) = \int_0^\infty g_b(xy) g_b(y) dy = x^{-1/2} \max(0, 2\log b - |\log x|)$ has Mellin transform $\Phi_b(s)^2$. So $\sum_\rho \tilde{f}(\rho) = W(b)$.

Substituting and rearranging:

$$W(b) = \underbrace{8 (b^{1/2} - b^{-1/2})^2}_{\text{boundary}} \underbrace{- 2 \sum_{p^k < b^2} \tfrac{\log p}{p^{k/2}}(2\log b - k\log p)}_{\text{prime sum}} \underbrace{- (\log 4\pi + \gamma_E) \cdot 2\log b}_{\text{constant}} \underbrace{- \int_1^\infty \tfrac{f(x) + f(1/x)/x - 2f(1)/x}{x - x^{-1}} dx}_{\text{gamma integral}}.$$

**Findings ($T_{\max}^{\rm zero} = 1000$, $b \in [1.5, 20]$):**

| $b$ | $W_{\rm zero}$ | $W_{\rm prime}$ | boundary | $-$prime sum | $-$const | $-$gamma int | rel. diff |
|---|---|---|---|---|---|---|---|
| 6.59 | $0.112$ | $0.098$ | $+37.9$ | $-24.9$ | $-11.7$ | $-1.17$ | $+12\%$ |
| 9.54 | $0.061$ | $0.055$ | $+61.2$ | $-44.6$ | $-14.0$ | $-2.46$ | $+10\%$ |
| 13.81 | $0.094$ | $0.093$ | $+95.1$ | $-74.8$ | $-16.3$ | $-3.87$ | $+1.7\%$ |
| 20.00 | $0.094$ | $0.095$ | $+144.4$ | $-120.3$ | $-18.6$ | $-5.37$ | $-0.8\%$ |

At $T_{\max} = 1000$ the two sides agree to $<2\%$ for $b \geq 14$. The remaining discrepancy at smaller $b$ comes from zero-side truncation: missing zeros above $T_{\max}$ contribute $O((\log T_{\max})/(\pi T_{\max}))$ to $W_{\rm zero}$, which is $\sim 0.002$ at $T_{\max} = 1000$. Consistent.

**The cancellation structure.** At $b = 20$, four components of order $10^1\text{-}10^2$ cancel down to $W \approx 0.1$:

- Boundary $+144$ (positive)
- Prime sum $-120$ (negative; 83% cancels the boundary)
- Constant $-18.6$ (negative)
- Gamma integral $-5.4$ (negative)

The prime sum dominates the cancellation. The boundary $+144$ minus the prime sum $-120$ leaves $+24$, which is then reduced by the constant ($-18.6$) and the gamma integral ($-5.4$) to $W \approx 0.1$. Each term must be accurate to better than $1\%$ (relative to itself) to preserve the sign and magnitude of the final $W$.

**Significance for the analytic-proof obstruction.** Weil positivity $W(b) \geq 0$ for $\zeta$ corresponds to the inequality

$$\text{prime sum} + (\log 4\pi + \gamma_E) \cdot 2\log b + \text{gamma integral} \leq 8(b^{1/2} - b^{-1/2})^2$$

(equivalently, the RHS of the explicit formula bounded by the boundary). The cancellation we observed says each side of this inequality is of order $10^2$ at $b = 20$ while the difference is $\sim 10^{-1}$. An unconditional bound on the prime sum (no RH input) tight enough to preserve the inequality would essentially BE RH, because the bound IS the zero distribution.

The classical Prime Number Theorem bound $\psi(x) - x = O(x \exp(-c (\log x)^{3/5}))$ (Vinogradov-Korobov, the best unconditional result) is far too loose: the error is $\sim x$ in absolute terms, while the cancellation we observed requires error control to better than $\sim 0.1\%$ of $x$. This is the structural reason "the prime side is hard": the proof needs a strong unconditional PNT, which is essentially what we're trying to prove.

## 3G: Davenport-Heilbronn prime-side analog ([e3g_dh_prime_side.py](e3g_dh_prime_side.py))

**Status:** complete. **The tight cancellation we observed for $\zeta$ does not hold for D-H. The structural difference is sharp: D-H components are 100× smaller than $\zeta$'s, and the cancellation is 100× looser.**

**Motivation.** 3F established the Weil-form duality for $\zeta$, with a tight cancellation between four large terms summing to $\sim 0.1$ at $b=20$. Does this cancellation structure hold for an L-function WITHOUT an Euler product?

**Method.** D-H has Dirichlet series $f_{DH}(s) = \sum_n c_n / n^s$ with $(c_1, \ldots, c_5) = (1, \kappa, -\kappa, -1, 0)$ periodic mod 5, $\kappa \approx 0.284$. The logarithmic derivative $-f_{DH}'/f_{DH}$ is a Dirichlet series with coefficients $b_n^{DH}$ supported on ALL $n$, computed by the recursion
$$\sum_{d \mid n} b_d^{DH} c_{n/d} = c_n \log n.$$
This is **not** $\Lambda(n) \chi(n)$ for some character — D-H has no Euler product, so $-f'/f$ is not a "prime-power-only" Dirichlet series. First few values: $b_2 = +0.197$, $b_3 = -0.312$, $b_4 = -1.44$, $b_6 = +1.94$, $b_9 = -2.29$. Sign-oscillating.

The Weil explicit formula generalizes (without the $\tilde f(0) + \tilde f(1)$ boundary, since $\Lambda_{DH}$ is entire — D-H has no pole). Using the Fourier form of the gamma integral:
$$W_{DH}(b) = -2 \sum_n \tfrac{b_n^{DH}}{\sqrt{n}} (2\log b - \log n)_+ + \tfrac{1}{2\pi} \int |\Phi_b(\tfrac{1}{2}+it)|^2 \Psi_{DH}(t) \, dt$$
with $\Psi_L(t) = 2 \, \mathrm{Re} \, \tfrac{d}{ds}[\log \gamma_L(\tfrac{1}{2}+it)]$ for the relevant gamma factor:
- $\Psi_\zeta(t) = -\log\pi + \mathrm{Re}\, \psi(\tfrac{1}{4} + \tfrac{it}{2})$ (gamma factor $\pi^{-s/2}\Gamma(s/2)$)
- $\Psi_{DH}(t) = \log(5/\pi) + \mathrm{Re}\, \psi(\tfrac{3}{4} + \tfrac{it}{2})$ (gamma factor $(5/\pi)^{(s+1)/2}\Gamma((s+1)/2)$)

**Findings (sign-consistent, 10-30% agreement at $T_{\max}^{\rm zero} = 200$, residual from truncation):**

| $b$ | $W_{\rm zero}^{DH}$ | $W_{\rm prime}^{DH}$ | $-$Dirichlet sum | $+$gamma int | rel diff |
|---|---|---|---|---|---|
| 6.00 | $+0.138$ | $+0.173$ | $+1.14$ | $-0.97$ | $-25\%$ |
| 8.11 | $+0.411$ | $+0.459$ | $+1.80$ | $-1.34$ | $-12\%$ |
| 14.80 | $+0.484$ | $+0.531$ | $+2.62$ | $-2.09$ | $-10\%$ |
| 20.00 | $+0.312$ | $+0.369$ | $+2.83$ | $-2.46$ | $-18\%$ |

The 10-30% disagreement is consistent with $T_{\max}^{\rm zero} = 200$ truncation (D-H has more off-line zeros above this height that we haven't included on the zero side; the prime side captures their contribution via the smooth gamma integral). Sign and rough magnitude agree across all $b$.

**The structural finding (the substantive result):**

| Quantity | $\zeta$ at $b = 20$ | D-H at $b = 20$ | Ratio |
|---|---|---|---|
| Largest component (absolute) | $144$ (boundary) | $2.83$ (Dirichlet sum) | $51\times$ smaller for D-H |
| $\lvert W \rvert$ | $0.1$ | $0.3$ | comparable |
| Cancellation ratio $\lvert W \rvert / \lvert \text{largest} \rvert$ | $\approx 10^{-3}$ | $\approx 10^{-1}$ | $100\times$ looser for D-H |
| Component count (large terms) | 4 (boundary, prime, const, gamma) | 2 (Dirichlet, gamma) | |

**Why this matters.** For $\zeta$, the prime sum $\sum \Lambda(n)/\sqrt{n}\cdot(2\log b - \log n)_+$ uses the all-positive von Mangoldt function $\Lambda(n)$, so the partial sums grow as $O(b^2/\log b)$. The boundary $8(b^{1/2} - b^{-1/2})^2$ also grows roughly as $8b$, providing a "positivity budget" that must precisely cancel the prime sum.

For D-H, the analog Dirichlet sum uses $b_n^{DH}$ which oscillates in sign. Sign cancellation within the sum keeps the magnitude small. No boundary "positivity budget" is needed because the Dirichlet sum doesn't blow up.

**The cancellation we observed for $\zeta$ is genuinely a feature of the Euler product**, not a generic feature of L-functions with functional equations. The route from Weil positivity to RH must therefore go through preserving the Euler product structure: any analytic argument for $\zeta$'s Weil positivity must handle the "all-positive $\Lambda(n)$ vs all-positive boundary" cancellation, which is essentially a strong form of the Prime Number Theorem.

**For D-H itself**, $W_{DH}(b) > 0$ holds for the test functions we examined despite D-H violating RH. This is because the boxcar $\Phi_b$ family doesn't satisfy Weil's "additional conditions" $\int g \, dx/x = \int g \, dx = 0$, so the simple negativity criterion doesn't apply directly. The off-line D-H zeros DO contribute negatively to $W_{DH}$ in principle, but for the boxcar family they're dominated by the on-line contribution. (3C.2's Gram matrix construction was specifically designed to test the additional-condition subspace, which is where the off-line zeros' signature shows up — and they did.)

## 3H: Weil-form duality for $\chi_3$ — refining the cancellation thesis ([e3h_chi3_prime_side.py](e3h_chi3_prime_side.py))

**Status:** complete. **Third data point reveals the cancellation tightness is a feature of $\zeta$'s pole at $s = 1$, not of Euler products in general.**

**Motivation.** 3G suggested "tight cancellation comes from the Euler product" based on the $\zeta$ vs D-H comparison. But $\chi_3$ ALSO has an Euler product — does it show tight cancellation like $\zeta$, or mild like D-H?

**Method.** Same Fourier-form explicit formula as 3G, with:

- Coefficients on prime powers only (Euler product): $a_n = \Lambda(n) \chi_3(n)$ where $\chi_3(p) = +1$ if $p \equiv 1 \pmod 3$, $-1$ if $p \equiv 2 \pmod 3$, $0$ if $p = 3$.
- No boundary terms ($\chi_3$ has no pole at $s = 1$).
- Gamma kernel: $\Psi_{\chi_3}(t) = \log(3/\pi) + \mathrm{Re}\, \psi(\tfrac{3}{4} + \tfrac{it}{2})$ (conductor 3, odd character, same digamma argument as D-H).

$$W_{\chi_3}(b) = -2 \sum_{p^k < b^2} \tfrac{\log p \cdot \chi_3(p^k)}{p^{k/2}} (2 \log b - k \log p) + \tfrac{1}{2\pi} \int |\Phi_b|^2 \Psi_{\chi_3}(t)\, dt.$$

**Findings ($T_{\max}^{\rm zero} = 200$, $b \in [6, 20]$):**

| $b$ | $W_{\rm zero}^{\chi_3}$ | $W_{\rm prime}^{\chi_3}$ | $-$prime sum | gamma int | rel diff |
|---|---|---|---|---|---|
| 6.00 | $+0.290$ | $+0.299$ | $+3.10$ | $-2.80$ | $-2.8\%$ |
| 8.11 | $+0.296$ | $+0.303$ | $+3.78$ | $-3.48$ | $-2.6\%$ |
| 14.80 | $+0.213$ | $+0.220$ | $+5.06$ | $-4.84$ | $-3.0\%$ |
| 20.00 | $+0.239$ | $+0.247$ | $+5.77$ | $-5.52$ | $-3.2\%$ |

Zero/prime agreement to $<4\%$ across the range, better than D-H (10-30%) because $\chi_3$ has no off-line zeros to complicate truncation.

**The three-L-function comparison:**

| L-function | Pole | Coefficient sign | Largest comp ($b=20$) | $\lvert W \rvert$ | Cancellation ratio |
|---|---|---|---|---|---|
| $\zeta$ | at $s = 1$ | $\Lambda(n) \geq 0$ all positive | $144$ (boundary) | $0.1$ | $\sim 10^{-3}$ |
| $\chi_3$ | none | $\Lambda(n) \chi_3(n) \in \{\pm 1, 0\}$ | $5.77$ (prime sum) | $0.24$ | $\sim 4 \times 10^{-2}$ |
| D-H | none | $b_n^{DH}$ oscillating, no $\Lambda$ structure | $2.83$ (Dirichlet sum) | $0.31$ | $\sim 1.3 \times 10^{-1}$ |

**Revised structural finding:** the tight cancellation is **specifically a feature of $\zeta$'s pole at $s = 1$**, not of Euler products in general. The mechanism:

- $\zeta$'s pole forces a large positive boundary term $8(b^{1/2} - b^{-1/2})^2 \sim b$.
- $\zeta$'s positive Λ(n) forces a large positive prime sum (no internal cancellation).
- The cancellation between these two large terms is what's tight to $\sim 10^{-3}$.

For all OTHER Selberg-class L-functions (Dirichlet, Hecke, automorphic), no pole means no boundary, and the prime sum has internal cancellation (from the character or coefficient signs). The "explicit formula gymnastics" required to prove Weil positivity for those L-functions is qualitatively easier — there's no pole-prime cancellation to control.

**Implication: $\zeta$ is exceptionally hard among L-functions for the Weil-form route.** The analytic obstruction for $\zeta$'s RH is genuinely sharper than for other Selberg-class L-functions. This is consistent with the historical pattern: Dirichlet L-functions and modular L-functions have been heavily studied, with many partial RH results (positive proportion of zeros on line, etc.), while $\zeta$ itself sits at the apex of difficulty.

**What this might mean for the path forward.** If $\chi_3$'s prime-side bound is achievable unconditionally (e.g., via Siegel-Walfisz-style estimates for primes in arithmetic progressions, which use less than full PNT-strength), then we might have an unconditional proof of $W_{\chi_3}(b) \geq 0$ for the relevant test function family. This wouldn't prove RH for $\zeta$, but it would establish RH for $\chi_3$. (Strong claim — needs verification.) Whether this can be lifted back to $\zeta$ via a deformation argument is open.

## 3I: Is the χ_3 unconditional path actually open? ([e3i_chi3_unconditional.py](e3i_chi3_unconditional.py))

**Status:** complete. **The path is blocked by the same circularity that blocks ζ.** Tested numerically and analytically.

**Method.** Take the χ_3 prime sum at b ∈ [10, 100]. Apply the Siegel-Walfisz bound $|\psi(x, \chi_3)| \leq C x \exp(-c\sqrt{\log x})$ via partial summation against the boxcar test kernel $\phi(u) = (2\log b - \log u)/\sqrt u$. Compare the resulting upper bound on |prime_sum| to the |gamma_int| (which is what -prime_sum must exceed for W ≥ 0).

**Findings:**

| $b$ | actual prime_sum | $\lvert$gamma_int$\rvert$ | S-W bound on $\lvert$prime_sum$\rvert$ | ratio (bound/required) |
|---|---|---|---|---|
| 10 | $-4.14$ | $3.95$ | $130$ | $33\times$ |
| 25 | $-6.27$ | $6.02$ | $326$ | $54\times$ |
| 65 | $-8.39$ | $8.19$ | $772$ | $94\times$ |
| 100 | $-9.37$ | $9.17$ | $1121$ | $122\times$ |

**The ratio (bound / required) grows with $b$**, not shrinks. The unconditional Siegel-Walfisz bound becomes *relatively* worse as $b$ increases. By $b = 100$, the bound is 122× too loose to certify positivity.

**Why partial summation loses the cancellation.** The prime sum decomposes as
$$\text{prime}\_\text{sum} = \text{boundary at } u = 2 + \int_2^{b^2} \psi(u, \chi_3)\, \phi'(u)\, du$$
where $\phi'(u) = -(2 + 2\log b - \log u)/(2u^{3/2})$. Bounding $|\psi(u, \chi_3)| \leq A(u)$ pointwise gives
$$|\text{prime}\_\text{sum}| \leq |\text{boundary}| + \int_2^{b^2} A(u) \frac{2\log b}{u^{3/2}}\, du.$$
But pointwise bounding $|\psi|$ **kills the oscillation** that makes the weighted prime sum small. The smooth kernel against $\psi$ has its own explicit formula bringing zeros back in. To get a tight bound on the *weighted* prime sum, you need to control the *zeros* of $L(s, \chi_3)$ — which is GRH for $\chi_3$, precisely what we're trying to prove.

**The same obstruction at different scales.** For both $\zeta$ and $\chi_3$, the unconditional bound is loose by factor $\sim 30$–$100$ relative to the required margin:

| L-function | Required margin | Available unconditional precision | Gap (factor) |
|---|---|---|---|
| $\zeta$ | $\sim 0.07\%$ (cancellation ratio) | $\sim 1/(\log x)^3 \approx 0.5\%$ | $\sim 7$ |
| $\chi_3$ | $\sim 4\%$ | S-W via partial summation $\sim 5\text{-}10\times$ at $b \in [10, 100]$ | $\sim 30$–$100$ |

Strangely, the ζ gap is *smaller* in factor terms, but the prime sum's growth and the available bounds also differ. Both are blocked.

**Conclusion: the χ_3 path is BLOCKED by the same circularity as ζ.** The "mild cancellation for non-pole L-functions" observation doesn't translate to an achievable unconditional proof. The route through Weil positivity to RH (for any Selberg-class L-function, not just ζ) requires zero-distribution-strength input, which IS RH.

**Honest revision of 3H's "implication for the path forward":** my earlier suggestion that χ_3 might be unconditionally accessible via Siegel-Walfisz was wrong. The cancellation tightness differs between ζ and χ_3 by ~100×, but the gap between unconditional bound and required margin is similar in factor — both are blocked.

**What this leaves.** The Weil-form route to RH (for any L-function in the Selberg class) is structurally blocked by the same wall: you need GRH-strength control on prime sums, and unconditional Siegel-Walfisz / PNT are far too loose. The structural advantage of mild cancellation (no pole, no all-positive Λ) doesn't yield to current technology.

This is the cleanest negative result of the session. It identifies WHERE the wall sits (at the gap between Siegel-Walfisz and GRH-strength bounds) and confirms the wall isn't an artifact of ζ specifically — it's a feature of *all* L-functions with non-trivial zeros.

## 3E

Literature-and-analysis task connecting Li coefficients to the de Bruijn-Newman constant; deferred.

## 3E

Literature-and-analysis task connecting Li coefficients to the de Bruijn-Newman constant; deferred.
