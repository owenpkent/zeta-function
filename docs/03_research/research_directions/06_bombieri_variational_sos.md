# Direction 6: Bombieri variational SOS (outside the LP/SDP framework)

> **No parent doc**: this direction is identified in [`../../../experiments/LEARNINGS.md`](../../../experiments/LEARNINGS.md) finding #12 as the one of three remaining escape routes from the 4E.3 line-restriction lemma not pursued in the LP/SDP family. Brief mention in [`../../../experiments/zero_free/e4e8_sos_sdp.md`](../../../experiments/zero_free/e4e8_sos_sdp.md). This document is the first dedicated treatment.
>
> **Phase in proof_program.md**: Alternative escape route from Architecture 4's LP/SDP family. Optionally Phase 4 sibling.
>
> **Headline**: develop a variational sum-of-squares approach to Weil positivity that allows the test polynomial to be NEGATIVE on a controlled set, with the negativity penalized by an L^2 norm. This is structurally outside the LP/SDP relaxation family (which requires strict non-negativity); it might escape the 4E.3 line-restriction wall that captures all LP/SDP relaxations.

## 1. Problem statement

The 4E.3 line-restriction lemma says: any non-negative bivariate trig polynomial restricted to a line gives a 1D non-negative trig polynomial, bounded by 1D Fejér at matched effective degree. This applies to all LP/SDP relaxations of the non-negative cone (confirmed across 4E.6 constrained-domain, 4E.7 multi-zero, 4E.8 polynomial-ideal SOS).

The Bombieri variational SOS approach RELAXES non-negativity: allow the test polynomial $P$ to be slightly negative, but penalize via an $L^2$ norm. Concretely:

$$
\text{min}_P \quad ||P_-||_{L^2}^2 \text{ subject to } \int P > 0, \quad c_1(P) \ge c_1^{\text{target}}
$$

where $P_-(\theta) = \max(0, -P(\theta))$ is the negative part of $P$. The penalty is QUADRATIC in negativity, so small violations of non-negativity are allowed with small cost.

This is NOT an LP or SDP relaxation in the standard sense. It is a quadratic programming (QP) with non-linear objective and non-linear constraint. The feasible set of test polynomials is LARGER than the LP/SDP non-negative cone.

**Question**: does this expanded feasible set produce non-negative trig polynomials $P$ (or "almost-non-negative" in the variational sense) whose 1D line-restriction beats the 1D Fejér ceiling at matched effective degree?

If yes: the 4E.3 line-restriction lemma is escaped, opening a path to improved Mossinghoff-Trudgian zero-free region constants.

If no: 4E.3 is robust under the broader variational relaxation, sharpening the conclusion that single-zero MT zero-free region constants are structurally capped at 1D Fejér.

## 2. Origin: Bombieri 2003

E. Bombieri proposed a variational approach in unpublished lectures (~2003) and in subsequent correspondence. The key idea: instead of requiring $P \ge 0$ pointwise, work with the FUNCTIONAL minimization above. The variational form has been used in adjacent contexts (Beurling-Selberg minorants, Logan's problem) but not, to the project's knowledge, applied systematically to RH-relevant test polynomials.

## 3. What "done" looks like

A 50-80 page paper "Variational sum-of-squares for the Mossinghoff-Trudgian shape factor" containing:

1. Precise formulation of the variational problem.
2. Existence theorems for the optimal $P$ in appropriate function spaces.
3. Characterization of optimal $P$ via Euler-Lagrange equations.
4. Numerical optimization at low bidegree to compute the optimal $P$ explicitly.
5. Comparison of the optimal shape factor to:
   - The 1D Fejér ceiling (4B).
   - The 4E.2 LP value (+25% gap to C-S).
   - The 4E.8 SDP value (saturating Fejér).
6. Verification of whether the optimal variational $P$ is non-negative (in which case it lives in the LP cone) or strictly negative on a small set (in which case the variational approach is genuinely different).
7. Translation to a zero-free region constant via the MT explicit-formula manipulation.

Publishable in Compositio, JAMS, or Inventiones.

## 4. Prerequisites

- Working knowledge of LP/SDP relaxations and the 4E.6-4E.8 family of LP escapes.
- Working knowledge of Beurling-Selberg minorants and extremal problems in Fourier analysis.
- Working knowledge of Mossinghoff-Trudgian explicit formula manipulation.
- Comfort with infinite-dimensional optimization, variational calculus, and Sobolev spaces.

## 5. Sub-problems and milestones

### 5.1 Define the variational problem precisely

Choose the function space (e.g., $H^s([0, 2\pi])$ for appropriate $s$), the penalty functional (L^2 norm of negative part, or alternative), and the constraint set.

**Milestone**: precise statement with existence of minimizers in the chosen function space, ~10 pages.

### 5.2 Euler-Lagrange characterization

Derive necessary conditions for the optimal $P$. These give an integral / differential equation that the optimum satisfies.

**Milestone**: Euler-Lagrange equations + analysis, ~10 pages.

### 5.3 Numerical optimization at low bidegree

For bidegree $(2, 2)$ (matching 4E.2 / 4E.8), set up the variational problem as a finite-dimensional QP and solve numerically (cvxpy works for QP, not just LP/SDP).

**Milestone**: numerical results for bidegree $(2, 2)$ alpha-sweep, ~5-10 pages.

### 5.4 Comparison with LP / SDP values

Compute the variational optimum's shape factor and compare to 4E.8's SDP value (4.0 at alpha=3) and 4E.2's LP value (4.0 at alpha=3). Determine whether the variational optimum:
- Equals the SDP/LP value (variational ≡ non-negative; no escape).
- Strictly exceeds (variational has a real edge).
- Strictly less than (penalty makes the problem harder, somehow).

**Milestone**: comparison table with sign of the gap, ~5 pages.

### 5.5 Line-restriction test

If the variational optimum is genuinely different, test its line-restriction at phi = 2 theta:
- Compute c_1 of the restriction.
- Compare to 1D Fejér at effective degree 6 (= 1.848 in raw convention).
- If c_1 / c_0 exceeds 1.848, the 4E.3 lemma is ESCAPED.

**Milestone**: line-restriction values + comparison to Fejér, ~5 pages.

### 5.6 Translation to zero-free region constant

If 5.5 escapes Fejér, translate the gain via the Mossinghoff-Trudgian explicit-formula manipulation to a concrete zero-free region constant improvement.

**Milestone**: explicit zero-free region constant + comparison to current best (de la Vallée Poussin / MT 2014), ~10-15 pages.

## 6. Falsifiability

- **5.4 fails**: variational optimum equals SDP value. Indicates the SOS relaxation is already pushing the bound out as far as variational methods can. The 4E.3 lemma is robust under variational relaxation. Direction 6 closes negative.
- **5.4 succeeds, 5.5 fails**: variational optimum is genuinely different but the line-restriction is still bounded by 1D Fejér. The 4E.3 lemma somehow extends to variational settings. Direction 6 closes negative but with a structural sharpening.
- **5.5 succeeds, 5.6 fails to translate**: variational escapes the Fejér ceiling on the LP side but doesn't translate to a zero-free region constant. Reveals that the C-S and MT figures of merit remain incompatible (extending 4E.3's structural lemma to the variational setting).
- **5.6 succeeds**: the V-K 2/3 exponent (or the constant) is improved. MAJOR result.

The most likely outcome a priori (per the marginal-positivity thesis): 5.4 succeeds with a small gap; 5.5 fails (the gap doesn't translate to line-restriction improvement); 5.6 doesn't apply. The 4E.3 lemma extends to variational SOS, sharpening the marginal-positivity picture.

A breakthrough outcome (probability ~10%): 5.5 + 5.6 succeed. Improved zero-free region constant. Not a proof of RH but a substantial advance in Architecture 4.

## 7. Estimated effort

6-12 postdoc-years. Calendar time: 3-5 years.

The numerical work (5.3) is relatively quick (~3 months for a strong PhD student); the analytical work (5.1, 5.2, 5.6) is the bulk of the effort.

## 8. Connections

- **4E.3** ([`e4e3_mt_translation.py`](../../../experiments/zero_free/e4e3_mt_translation.py)): the structural lemma Direction 6 attempts to escape.
- **4E.6, 4E.7, 4E.8** ([`e4e6_constrained_lp.py`](../../../experiments/zero_free/e4e6_constrained_lp.py), [`e4e7_multi_zero_lp.py`](../../../experiments/zero_free/e4e7_multi_zero_lp.py), [`e4e8_sos_sdp.py`](../../../experiments/zero_free/e4e8_sos_sdp.py)): the LP/SDP escapes that failed. Direction 6 is the variational alternative.
- **LEARNINGS finding #12, #15**: the pattern that 4E.3 is robust under LP/SDP relaxation. Direction 6 tests whether variational SOS extends the pattern.
- **4A + 4C** ([`4a_4c_vinogradov_korobov.md`](../../../experiments/zero_free/4a_4c_vinogradov_korobov.md)): the V-K exponent landscape. If Direction 6 succeeds, this is updated.
- **Direction 7** (Heath-Brown multi-zero MT + 4E.2): an alternative angle on Architecture 4 improvement. Directions 6 and 7 could combine.

## 9. References

- Bombieri, E. (~2003). Unpublished lectures and correspondence on variational SOS.
- Beurling, A.; Selberg, A. (1940s-50s). Beurling-Selberg majorants and minorants in extremal Fourier analysis.
- Logan, B. (1983). *An interpolation problem suggested by a theorem of Beurling*. J. Approx. Theory 39.
- Vaaler, J. (1985). *Some extremal functions in Fourier analysis*. Bull. AMS 12.
- Mossinghoff, M.; Trudgian, T. (2014, 2024). Mossinghoff-Trudgian zero-free region papers (the explicit-formula bookkeeping side).

## 10. Status

This direction is **research-grade, beyond project scope**. No parent dossier exists; this document is the first detailed treatment.

The direction is qualitatively distinct from the LP/SDP family attempted in 4E.6-4E.8. Its outcome would either:
- Confirm the marginal-positivity thesis at the variational level (most likely), OR
- Produce a substantive improvement to the V-K zero-free region constant (less likely but possible).

Either outcome is publishable and contributes to the architectural understanding of Architecture 4.
