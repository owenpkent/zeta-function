# Direction 7: Heath-Brown explicit multi-zero MT combined with 4E.2's higher-harmonic gain

> **No parent doc**: this direction is identified in [`../../../experiments/LEARNINGS.md`](../../../experiments/LEARNINGS.md) finding #13 and [`../../../experiments/zero_free/e4e7_multi_zero_lp.md`](../../../experiments/zero_free/e4e7_multi_zero_lp.md) as the research-grade combination of 4E.7's multi-zero LP win with 4E.2's higher-harmonic LP gain. This document is the first dedicated treatment.
>
> **Phase in proof_program.md**: Architecture 4 partial escape. Optional alongside Direction 6.
>
> **Headline**: combine 4E.7's multi-zero LP shape-factor gain (lambda_{1,1} 55-137× larger than lambda_1^2) with 4E.2's higher-harmonic LP gain (+25% over C-S tensor bound at alpha=3, N=2) and Heath-Brown 1992's explicit multi-zero MT bookkeeping. The result, if successful, would be the first non-trivial multi-zero Mossinghoff-Trudgian improvement for the zero-free region of zeta (or for Siegel zeros / least prime in AP).

## 1. Problem statement

The Mossinghoff-Trudgian (MT) approach to zero-free regions uses a non-negative trig polynomial $P(\theta)$ via the explicit formula. The single-zero MT shape factor is:

$$
\lambda_1(P) = \frac{(c_1 - c_0)^2}{4 c_0}
$$

which the 1D Fejér ceiling caps at $\lambda_1 \le (q_1^{1D} - 1)^2 / 4$ where $q_1^{1D} = 2 \cos(\pi/(N+2))$.

The multi-zero generalization (Heath-Brown 1992, Pintz 1976) postulates $d$ putative zeros at heights $\gamma_1, \ldots, \gamma_d$. The polynomial becomes $d$-variate; the joint shape factor is:

$$
\lambda_{1, \ldots, 1}(P) = \frac{(c_{1, \ldots, 1} - c_{0, \ldots, 0})^2}{4 c_{0, \ldots, 0}}
$$

**4E.7 finding**: at $d = 2$ for max $c_{1, 1}$ at bidegree $(N, N)$, the LP value equals $q_1^2$ (tensor product) by 4D-ii's decomposition lemma. So the joint shape factor is $\lambda_{1, 1} = (q_1^2 - 1)^2 / 4$, which is 55-137× LARGER than $\lambda_1^2$ (naive product of two single-zero shape factors). REAL gain at the shape-factor level.

But: the LP-optimal polynomial is RANK 1 (tensor product). No higher-harmonic structure.

**4E.2 finding**: at the higher-harmonic objective max $c_{1, 1} + 3 c_{2, 2}$ at bidegree $(2, 2)$, the LP value EXCEEDS the C-S tensor bound by +25% (4.0 vs 3.2). The LP-optimal polynomial is genuinely 2D (rank 3).

**The combination**: a multi-zero MT improvement for zeta combines:
1. The multi-zero LP gain (4E.7): joint shape factor 55-137× larger than naive product.
2. The higher-harmonic LP gain (4E.2): genuine 2D structure exceeding tensor bound.
3. Heath-Brown 1992's explicit multi-zero MT bookkeeping: the explicit-formula manipulation that translates the LP value into a zero-free region constant.

Question: does the combination produce a non-trivial improvement to the zero-free region constant for zeta (in the asymptotic regime, $\eta \ge C / \log T$)?

## 2. What "done" looks like

A 60-100 page paper "Multi-zero Mossinghoff-Trudgian for zeta via higher-harmonic 2D polynomials" containing:

1. The combined LP setup: $d$-variate polynomial at bidegree $(N, \ldots, N)$ with higher-harmonic objective.
2. Verification that the LP-optimal polynomial has non-trivial structure (rank > 1 at low N).
3. The Heath-Brown 1992 explicit-formula manipulation adapted to the higher-harmonic setting.
4. Translation of the LP value to a zero-free region constant.
5. Comparison with the current best zero-free region:
   - For zeta: V-K 2/3 (current asymptotic), MT 2014 / 2024 (current constant within $C/(\log T)^{2/3}(\log\log T)^{1/3}$).
   - For Siegel zeros: Pintz 1976.
   - For least prime in AP: Heath-Brown 1992.
6. Verification that the improvement is non-trivial: the new constant is provably larger than the current best.

Publishable in Inventiones or Acta Math.

## 3. Prerequisites

- Working knowledge of Mossinghoff-Trudgian explicit-formula manipulation (MT 2014, MT 2024).
- Working knowledge of Heath-Brown 1992's multi-zero approach (least prime in AP).
- Working knowledge of Pintz 1976 (Siegel zero implications).
- Familiarity with 4E series LP results (4E.2, 4E.7).
- Comfort with extensive explicit-formula bookkeeping (the 100+ page proofs of MT and HB papers).

## 4. Sub-problems and milestones

### 4.1 Set up the combined LP

Define the bidegree $(N, N)$ polynomial with objective $c_{1, 1} + \alpha c_{2, 2}$ at bidegree $(2, 2)$ AND constrained by multi-zero MT structure (the explicit-formula bookkeeping of HB 1992).

**Milestone**: explicit LP statement with all constraints, ~10 pages.

### 4.2 Compute the LP value

Solve the LP numerically and identify the structure of the LP-optimal polynomial.

**Milestone**: LP-optimal $P$ with rank analysis, ~5 pages.

### 4.3 Heath-Brown bookkeeping

Adapt HB 1992's explicit-formula manipulation to the higher-harmonic 2D polynomial. The bookkeeping involves:
- Multi-zero explicit formula: $\zeta'/\zeta$ at two zeros $\gamma_1, \gamma_2$.
- Auxiliary sums weighted by the test polynomial.
- Tight bounds on the resulting expressions.

**Milestone**: HB-style explicit formula adapted to 2D + higher harmonic, ~20-30 pages.

### 4.4 Translation to zero-free region constant

Compute the explicit zero-free region constant from the LP value via the HB bookkeeping.

**Milestone**: explicit constant + comparison to current MT 2014 / 2024 values, ~10-15 pages.

### 4.5 Verify non-trivial improvement

Show that the new constant is provably larger than the current best (MT 2014 / 2024 single-zero, or HB 1992 multi-zero with first-harmonic only).

**Milestone**: comparison theorem + explicit gap, ~5-10 pages.

### 4.6 Identify problems to which it applies

- Asymptotic RH for zeta: the gain is in the CONSTANT, not the EXPONENT, since Riemann-von Mangoldt density bounds multi-zero MT scaling.
- Siegel zeros: finite-range problem where multi-zero MT can give exponent improvements (HB 1992).
- Least prime in AP: similar finite-range problem (HB 1992).

**Milestone**: application sections for each, ~10-20 pages.

## 5. Falsifiability

- **4.2 fails (rank-1 LP)**: the higher-harmonic gain combined with multi-zero structure decomposes to rank-1. The combination provides no improvement. Direction 7 closes negative.
- **4.3 fails (HB bookkeeping doesn't adapt)**: the explicit-formula manipulation for higher-harmonic 2D doesn't close. Direction 7 closes negative at the analytic level.
- **4.4 fails (the constant doesn't improve)**: the LP value is non-trivial but the translation produces a constant equal to or worse than the current best. The C-S figure of merit and the MT figure of merit remain incompatible (extending 4E.3 to the multi-zero higher-harmonic setting).
- **4.5 succeeds**: the constant improves. Non-trivial result.

The MOST LIKELY outcome a priori (per the marginal-positivity thesis and 4E.3 + 4E.7 + 4E.8 pattern): 4.4 fails. The C-S vs MT incompatibility extends, and the combined gain doesn't translate.

A BREAKTHROUGH outcome (probability ~15%): 4.5 succeeds for Siegel zeros / least prime in AP. The zero-free region constant for these finite-range problems improves. Major result, not a proof of RH but a substantive Architecture 4 advance.

A MAJOR breakthrough (probability ~5%): 4.5 succeeds for asymptotic zeta. The MT zero-free region constant for zeta improves. Direct Architecture 4 progress.

## 6. Estimated effort

5-10 postdoc-years. Calendar time: 2-4 years for a 2-3 person group with deep analytic number theory expertise.

Most of the effort is in 4.3 (HB bookkeeping adaptation), which is highly technical and requires careful tracking of error terms across the explicit-formula manipulation.

## 7. Connections

- **4E.2** ([`e4e2_sum_sweep.py`](../../../experiments/zero_free/e4e2_sum_sweep.py)): the +25% LP gain.
- **4E.7** ([`e4e7_multi_zero_lp.py`](../../../experiments/zero_free/e4e7_multi_zero_lp.py)): the multi-zero LP shape-factor gain.
- **4E.3** ([`e4e3_mt_translation.py`](../../../experiments/zero_free/e4e3_mt_translation.py)): the line-restriction lemma that single-zero MT translation hits. Direction 7 escapes this via multi-zero structure.
- **Direction 6** (Bombieri variational SOS): parallel Architecture 4 escape route. Could combine with Direction 7 (variational + multi-zero higher-harmonic).
- **LEARNINGS finding #13**: the 4E.7 multi-zero shape-factor result. Direction 7 is its natural continuation.

## 8. References

- Heath-Brown, D.R. (1992). *Zero-free regions for Dirichlet L-functions, and the least prime in an arithmetic progression*. Proc. London Math. Soc. (3) 64.
- Pintz, J. (1976). *Elementary methods in the theory of L-functions, VIII*. Acta Arith. 31.
- Pintz, J. (2017). *Cramér's conjecture and the prime number race*. ...
- Mossinghoff, M.J.; Trudgian, T.S. (2014). *Explicit bounds for primes in arithmetic progressions*. Mathematika 60.
- Mossinghoff, M.J.; Trudgian, T.S. (2024). Most recent MT papers on zero-free regions.
- Bombieri, E. (1965). *Le grand crible dans la théorie analytique des nombres*. Astérisque 18.
- Ford, K. (2002). *Vinogradov's integral and bounds for the Riemann zeta function*. Proc. London Math. Soc. (3) 85.

## 9. Status

This direction is **research-grade, beyond project scope**. The 4E.7 LP result identifies the shape-factor gain; this document provides the operational specification for combining it with 4E.2's higher-harmonic structure and Heath-Brown's multi-zero MT bookkeeping.

Direction 7 is one of the most technically demanding in the proof program: 100+ pages of explicit-formula manipulation. Even partial progress is publishable.

Note: Direction 7 alone does NOT prove RH (per the marginal-positivity thesis and the V-K stagnation analysis). It could improve the zero-free region constant for zeta and the related Siegel-zero / least-prime-in-AP problems. The improvement is structural (multi-zero + higher harmonic) but bounded by the underlying V-K exponent.
