# 4E.7 — Multi-Zero Mossinghoff-Trudgian LP

> Probe of the second proposed escape route from [4E.3's structural lemma](e4e3_mt_translation.py): postulate **multiple putative zeros** at independent heights γ_1, γ_2, ... so the LP becomes multivariate with full d-dim non-negativity rather than a 1D line restriction. The 4E.3 lemma doesn't directly apply because the constraint set is no longer a line.
>
> **Headline**: the LP escape is *real at the shape-factor level*: λ_{1,1} ranges from 55× to 137× larger than λ_1² (naive two-independent-zero MT) for N ∈ {2, 3, 4}. But the LP-optimal polynomial is **rank-1 (tensor product)** — the multi-zero objective max c_{1,1} alone does not exceed the tensor bound q_1². For a non-trivial multi-zero MT improvement to RH on zeta, you'd need to combine this with higher-harmonic objectives (per 4E.2's +25% rank-2 LP gain) and explicit Heath-Brown bookkeeping — research-grade work beyond this experiment.

## 1. The setup

The single-zero MT trick uses a 1D non-negative trig polynomial $P(\theta) = c_0 + 2 \sum c_k \cos(k\theta) \ge 0$ with $c_0 = 1$, evaluated at $\theta = \gamma_0 \log p$ for the putative zero ordinate $\gamma_0$. The resulting MT shape factor is

$$\lambda_1(P) := \frac{(c_1 - c_0)^2}{4 c_0} = \frac{(c_1 - 1)^2}{4}$$

bounded by 1D Fejér: $\max c_1 = \cos(\pi/(N+2))$ in the 4B convention, or $q_1 = 2\cos(\pi/(N+2))$ in the raw-coefficient convention. So $\lambda_1 \le (q_1 - 1)^2 / 4 < 1/4$.

The multi-zero generalization (Heath-Brown 1992, Pintz 1976, and earlier): postulate $d$ putative zeros at heights $\gamma_1, \ldots, \gamma_d$. The relevant polynomial is now $d$-variate, $P(\theta_1, \ldots, \theta_d) = \sum c_{j_1, \ldots, j_d} \cos(j_1 \theta_1) \cdots \cos(j_d \theta_d) \ge 0$. The MT-style shape factor for the JOINT contribution is

$$\lambda_{1,\ldots,1}(P) := \frac{(c_{1,\ldots,1} - c_{0,\ldots,0})^2}{4 c_{0,\ldots,0}} = \frac{(c_{1,\ldots,1} - 1)^2}{4}.$$

The constraint set for the LP is the FULL $d$-torus $[0, 2\pi]^d$, not a 1D line, so 4E.3's lemma does not apply: it's possible in principle to get LP values that exceed what line-restriction would allow.

## 2. The naive multi-zero LP at $d = 2$

From [4D-ii](e4d_multivariate_lp.py): the LP for $\max c_{1,1}$ over 2D non-neg trig polys at bidegree $(N, N)$ with $c_{0,0} = 1$ saturates the tensor-product bound

$$\max c_{1,1} = q_1^2 = (2 \cos(\pi/(N+2)))^2$$

with rank-1 LP-optimal polynomial (= tensor product $P(\theta, \phi) = Q(\theta) Q(\phi)$). So at the LP-value level, the naive multi-zero objective decomposes — no new structure beyond two independent 1D Fejérs.

Two-zero joint shape factor:

$$\lambda_{1,1} = \frac{(q_1^2 - 1)^2}{4}.$$

| $N$ | $q_1$ | $q_1^2$ | $\lambda_{1,1}$ | $\lambda_1$ | $\lambda_1^2$ | $\lambda_{1,1} / \lambda_1^2$ |
|---|---|---|---|---|---|---|
| 2 | 1.4142 | 2.000 | 0.2500 | 0.0429 | 0.0018 | 137.4× |
| 3 | 1.6180 | 2.618 | 0.6545 | 0.0955 | 0.0091 | 71.8× |
| 4 | 1.7321 | 3.000 | 1.0000 | 0.1340 | 0.0179 | 55.7× |

**The joint shape factor $\lambda_{1,1}$ is structurally much larger than the naive product $\lambda_1^2$.** This is the multi-zero version of "zeros interact in the explicit-formula sum, not just add" — the joint constraint is much tighter than two independent applications of single-zero MT.

## 3. Why this is real but limited

The factor 55–137× gap is genuine — it reflects the fact that imposing the 2D LP constraint $\max c_{1,1}$ is much more permissive than imposing two single-zero constraints separately. But:

1. **The LP-optimal polynomial is rank-1** (singular value spectrum has rank exactly 1 at all tested $N$). The optimum IS the tensor product $Q(\theta) Q(\phi)$.

2. **So the LP-value (= $q_1^2$) decomposes by 4D-ii's lemma**: the 2D LP for max $c_{1,1}$ saturates the tensor bound. The shape factor $\lambda_{1,1} = (q_1^2 - 1)^2/4$ is correctly bounded by 4D-ii's tensor bound, not by a stronger 2D-genuine bound.

3. **A genuinely new 2D LP win** requires HIGHER harmonics: per 4E, 4E.2's balanced sum $\max c_{1,1} + \alpha c_{2,2}$ produces rank-2 LP optima exceeding the tensor bound by up to +25%. The $c_{2,2}$ cross-cross term is essential.

So the multi-zero LP escape from 4E.3 is split into two regimes:
- **Naive (first harmonic only)**: rank-1, decomposes, gives a multiplicative shape-factor improvement but no exponent change.
- **Higher-harmonic (including $c_{2,2}$, $c_{2,2,2}$, ...)**: rank > 1, exceeds tensor bound by up to ~+62% in 4D (per 4E.5), produces genuinely 2D auxiliary inequalities — but per 4E.3 these don't translate to MT under the single-zero, single-line-restriction setting.

The genuine multi-zero MT improvement of Heath-Brown / Pintz combines both: the higher-harmonic 4E.2 LP value AND the multi-zero MT bookkeeping. Whether this combination produces an asymptotic improvement to the single-zero MT constant for RH on zeta is non-trivial.

## 4. Balanced-sum LP probe

Tested objective $\max c_{1,0} + c_{0,1} + \alpha c_{1,1}$ at bidegree $(3, 3)$, sweeping $\alpha$:

| $\alpha$ | LP value | $c_{1,0}$ | $c_{0,1}$ | $c_{1,1}$ | rank |
|---|---|---|---|---|---|
| 0.0 | 3.2361 | 1.6180 | 1.6180 | 2.6180 | 1 |
| 0.5 | 4.5451 | 1.6180 | 1.6180 | 2.6180 | 1 |
| 1.0 | 5.8541 | 1.6180 | 1.6180 | 2.6180 | 1 |
| 2.0 | 8.4721 | 1.6180 | 1.6180 | 2.6180 | 1 |
| 5.0 | 16.3262 | 1.6180 | 1.6180 | 2.6180 | 1 |

**Rank 1 at every tested $\alpha$.** The LP-optimal polynomial is the tensor product $Q(\theta) Q(\phi)$ with $Q$ the 1D Fejér optimum. The balanced-sum objective with equal weights on $(1, 0)$ and $(0, 1)$ has symmetry that reduces to a 1D-like problem in the symmetrized basis — explaining the consistent decomposition.

Heath-Brown-style $(a, b)$ sweep with objective $a(c_{1,0} + c_{0,1}) + b c_{1,1}$: also rank 1 at all $(a, b)$ tested. So naive multi-zero objectives are all rank-1.

## 5. Translation to zero-free region constants (not done here)

The LP shape factor $\lambda_{1,1}$ is the **input** to the multi-zero MT bookkeeping. To translate to an actual zero-free region constant, one would need:

1. The exact multi-zero MT explicit-formula manipulation (Heath-Brown 1992 §3, Pintz 1976).
2. Careful tracking of the "remainder term" $R(P)$ for the 2D polynomial — which scales like $P(0, 0)$ but with different constants than 1D.
3. Combination of multi-zero LP gain (this experiment) with the higher-harmonic LP gain (4E.2's +25%).

For RH on zeta specifically: Riemann-von Mangoldt says zero density at height $T$ is $\log(T/(2\pi)) / (2\pi)$, so the gap between consecutive zeros at height $T$ is $\sim 2\pi / \log T \to 0$ as $T \to \infty$. Multi-zero MT is therefore *less* directly relevant to asymptotic RH than to FINITE-RANGE problems where zeros at controlled distances are postulated by the problem setup (least prime in AP, Siegel zeros for specific moduli, exceptional zeros of $L$-functions).

The classical multi-zero MT improvements are for these finite-range problems, where the LP gain translates to constant-factor improvements in the zero-free region constant. For asymptotic RH on zeta, multi-zero MT can in principle improve the **constant** in $\eta \ge C / \log T$, but the **scaling** stays $1/\log T$.

## 6. Outputs

- **Code**: [e4e7_multi_zero_lp.py](e4e7_multi_zero_lp.py)
- **Figure**: [e4e7_multi_zero_lp.png](e4e7_multi_zero_lp.png) — three panels: single-zero shape vs N, joint vs independent (log scale), balanced-sum LP sweep.
- **Data**: `e4e7_multi_zero_lp.npz` — all LP values, shape factors, rank diagnostics.

## 7. Connections

- **4E.3** ([e4e3_mt_translation.py](e4e3_mt_translation.py)): the structural lemma that bounds single-line restrictions. 4E.7 uses non-restriction (full 2D) to bypass.
- **4E.6** ([e4e6_constrained_lp.py](e4e6_constrained_lp.py)): the previous attempted escape (constrained-domain LP), which collapsed to Fejér. 4E.7 is the second of the three escape routes identified by 4E.6.
- **4E** / **4E.2** / **4E.4** / **4E.5** ([e4e_offdiag_lp.py](e4e_offdiag_lp.py) and companions): the higher-harmonic LP gain. To get a non-trivial multi-zero MT improvement, this needs to combine with 4E.7's multi-zero LP.
- **4E.8** (open): polynomial-ideal SOS via Putinar/Schmüdgen. The remaining LP-escape direction, requires SDP not LP.

## 8. Verdict

The multi-zero LP IS a real escape from 4E.3's line-restriction lemma at the LP-value level — the constraint set is full 2D, not a line, and 4E.3 doesn't apply. But the naive multi-zero objective max $c_{1,1}$ produces a rank-1 LP optimum (tensor product), so the LP value decomposes; no new 2D structure beyond what 4D-ii already characterized.

The structural finding: **the multi-zero LP escape is real at the shape-factor level (Finding 1: $\lambda_{1,1}$ is 55-137× larger than $\lambda_1^2$) but does not produce non-tensor LP optima at first-harmonic objectives (Finding 2).** A genuine multi-zero MT win for RH on zeta requires the higher-harmonic structure of 4E.2 combined with multi-zero MT bookkeeping — research-grade combination beyond the scope of this experiment.

**Status**: Arch 4E.7 complete. The multi-zero LP escape from 4E.3 is real at the shape-factor level but does not exceed the tensor bound at naive objectives. The combination with higher-harmonic structure (4E.2) and explicit Heath-Brown bookkeeping is the natural followup but is research-grade work.
