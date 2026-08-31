/-
Certification nuggets: the four VERIFIER-shaped finite statements handed
forward by the e2ax off-line-implant dossier and the e2be certification-cost
theorem (LEARNINGS #192 and #200).

Source dossiers: `experiments/arithmetic_geometric/e2ax_offline_implant.md`
(Section 2 and hand-off item iii) and
`experiments/arithmetic_geometric/e2be_certification_cost.md` (Section 3,
"Lean-able residue"). Registry rows to be added by the caller; this module is
deliberately NOT imported by `ZetaRH.lean` (the F2bSkeleton convention).

Pricing, target by target:

  #CN-1 (registry e2ax-1, the max-at-zero theorem). A nonnegative cosine
        combination `f(u) = sum_j w_j cos(theta_j u)` obeys
        `|f(u)| <= f(0) = sum_j w_j`. This is the one-line lemma behind the
        e2ax admissibility conjunction (the admissible fake must pay
        `cosh(delta U)` in zero-count because its imitation budget is capped
        at `f(0)` while the target grows like `4 cosh(delta U)`). Fully
        proved: triangle inequality + `|cos| <= 1`; no carried hypotheses.

  #CN-2 (registry e2be-2, the Rosser-Schoenfeld partial summation).
        `sum_{n <= N} Lambda(n)/sqrt(n) <= 2.07766 sqrt(N)` from
        `psi(x) < 1.03883 x`. The analytic input (Rosser-Schoenfeld 1962) is
        NOT in Mathlib and rides as the named hypothesis `hRS`, in the honest
        KERNEL style of `#S4C-2` (which carried Chebyshev's lower bound the
        same way). The finite content proved outright is the discrete Abel
        step, run as strong induction on `N` with the strengthened invariant
        `sum_{n <= N} Lambda(n)/sqrt(n) <= c sqrt(N) + psi(N)/sqrt(N)`
        (the invariant is what makes the induction close: the naive statement
        `<= 2c sqrt(N)` loses the `psi` credit the step needs). Constants are
        the exact rationals `103883/100000` and `207766/100000 = 2 * c`, so
        no real-literal decimal friction anywhere.

  #CN-3 (registry e2be-3, the linear-interpolation error bound). For `g`
        twice differentiable with `|g''| <= B`, the linear interpolant
        between nodes `x0 < x1` errs by at most `(B/8)(x1 - x0)^2`: the
        SHARP classical constant, which is the dossier's `(dx^2/8) sup|c''|`
        clause (E_interp, the dominant clause of the T1 budget). Hypotheses
        carry `g'` and `g''` explicitly with pointwise `HasDerivAt`, the
        F2bSkeleton `second_difference_bound` convention (junk-value `deriv`
        is refutable). Route: the doubled-Rolle auxiliary-function argument
        (`phi = error - K * (t-x0)(t-x1)` vanishes at three points, so
        `phi''` vanishes somewhere, pinning `K = g''(xi)/2`), then AM-GM on
        `(x-x0)(x1-x)`. Fully proved; no carried hypotheses.

  #CN-4 (registry e2be-1, the Gaussian-tail chain behind E_P). The dossier's
        prime-tail clause bounds `int_U^inf u exp(u/2 - u^2/(4 sigma^2)) du`
        by completing the square (`u/2 - u^2/4s^2 = s^2/4 - (u-s^2)^2/4s^2`),
        integrating the shifted-linear part exactly (antiderivative
        `-2 s^2 e^{s^2/4} e^{-(u-s^2)^2/4s^2}`), and majorizing the constant
        part by `(s^2/a) x` the linear part on `u >= U` (`a = U - s^2 > 0`,
        the dossier's `a = ln N - sigma^2`). Total:
        `<= 2 s^2 e^{s^2/4} (1 + s^2/a) e^{-a^2/4s^2}`, which is exactly
        `E_P / (2 sqrt(pi) sigma)` (the remaining prefactor in the dossier is
        the `|c(y)| <= sqrt(pi) sigma e^{-y^2/4s^2}` envelope times
        `Lambda(n) <= ln n`, a cited majorization outside this nugget's
        scope). Fully proved including the improper-integral bookkeeping:
        integrability comes free from `integrableOn_Ioi_deriv_of_nonneg'`
        (nonneg derivative with a limit at infinity), and the comparison uses
        `integral_mono_of_nonneg`, which needs only the UPPER integrand
        integrable. No carried hypotheses.

  All theorems below are sorry-free; `#print axioms` at the end must report a
  subset of `[propext, Classical.choice, Quot.sound]`.
-/

import Mathlib

namespace ZetaRH.CertificationNuggets

open Filter MeasureTheory
open scoped ArithmeticFunction Topology

/-! ## #CN-1: the max-at-zero theorem (e2ax-1) -/

/-- **Max-at-zero, bound half (#CN-1).** A cosine combination with nonnegative
    weights is dominated everywhere by the weight total: triangle inequality
    plus `|cos| <= 1` termwise. -/
theorem cosine_sum_abs_le {ι : Type*} (s : Finset ι) (w θ : ι → ℝ)
    (hw : ∀ j ∈ s, 0 ≤ w j) (u : ℝ) :
    |∑ j ∈ s, w j * Real.cos (θ j * u)| ≤ ∑ j ∈ s, w j := by
  calc |∑ j ∈ s, w j * Real.cos (θ j * u)|
      ≤ ∑ j ∈ s, |w j * Real.cos (θ j * u)| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ j ∈ s, w j := by
        refine Finset.sum_le_sum fun j hj => ?_
        rw [abs_mul, abs_of_nonneg (hw j hj)]
        calc w j * |Real.cos (θ j * u)|
            ≤ w j * 1 := mul_le_mul_of_nonneg_left (Real.abs_cos_le_one _) (hw j hj)
          _ = w j := mul_one _

/-- **Max-at-zero, equality half (#CN-1).** At `u = 0` every cosine is 1, so
    the sum IS the weight total. -/
theorem cosine_sum_at_zero {ι : Type*} (s : Finset ι) (w θ : ι → ℝ) :
    ∑ j ∈ s, w j * Real.cos (θ j * 0) = ∑ j ∈ s, w j := by
  simp

/-- **Max-at-zero, combined (#CN-1, the e2ax hand-off form).** `|f(u)| <= f(0)`
    for every nonnegative cosine combination: the admissible fake's imitation
    budget is capped at its zero-value, which is why matching a
    `4 cosh(delta U)` envelope costs `cosh(delta U)` in total multiplicity. -/
theorem cosine_sum_max_at_zero {ι : Type*} (s : Finset ι) (w θ : ι → ℝ)
    (hw : ∀ j ∈ s, 0 ≤ w j) (u : ℝ) :
    |∑ j ∈ s, w j * Real.cos (θ j * u)| ≤ ∑ j ∈ s, w j * Real.cos (θ j * 0) := by
  rw [cosine_sum_at_zero]
  exact cosine_sum_abs_le s w θ hw u

/-! ## #CN-2: the Rosser-Schoenfeld partial summation (e2be-2) -/

/-- The Chebyshev function `psi(N) = sum_{n <= N} Lambda(n)` as a finite range
    sum over Mathlib's von Mangoldt function (index `n` runs over
    `range (N+1)`; `Lambda(0) = Lambda(1) = 0` so the convention is harmless). -/
noncomputable def chebyshevPsi (N : ℕ) : ℝ := ∑ n ∈ Finset.range (N + 1), Λ n

/-- The one-step exchange inequality of the discrete Abel argument: moving the
    `psi` credit from denominator `a` to denominator `b >= a` costs at most
    `c * (b - a)` when `psi <= c * a^2` (instantiated at `a = sqrt N`,
    `b = sqrt (N+1)`). Isolated so the induction step is a one-liner. -/
theorem abel_step_key {P a b c : ℝ} (hP : 0 ≤ P) (hPa : P ≤ c * a ^ 2)
    (ha : 0 ≤ a) (hab : a ≤ b) (hb : 0 < b) (hc : 0 ≤ c) :
    c * a + P / a ≤ c * b + P / b := by
  rcases ha.eq_or_lt with h0 | h0
  · -- degenerate node a = 0: the hypothesis P <= c * 0 forces P = 0, and
    -- Lean's x / 0 = 0 convention keeps both sides finite
    have hP0 : P = 0 := le_antisymm (by rw [← h0] at hPa; simpa using hPa) hP
    rw [← h0, hP0]
    simpa using mul_nonneg hc hb.le
  · have hab2 : 0 < a * b := mul_pos h0 hb
    have h1 : P / a - P / b = P * (b - a) / (a * b) := by
      rw [div_sub_div _ _ h0.ne' hb.ne']
      ring_nf
    have key : P / a - P / b ≤ c * b - c * a := by
      rw [h1, div_le_iff₀ hab2]
      nlinarith [mul_le_mul_of_nonneg_right hPa (sub_nonneg.mpr hab),
        mul_le_mul_of_nonneg_left hab
          (mul_nonneg (mul_nonneg hc ha) (sub_nonneg.mpr hab))]
    linarith

/-- **The Abel invariant (#CN-2, the load-bearing induction).** Under the
    carried pointwise bound `psi(n) <= c n`, the weighted prime sum obeys
    `sum_{n <= N} Lambda(n)/sqrt(n) <= c sqrt(N) + psi(N)/sqrt(N)`.
    The `psi(N)/sqrt(N)` credit is exactly what the naive induction lacks:
    the step only ever pays `psi(N) * (1/sqrt(N) - 1/sqrt(N+1))`, which
    `abel_step_key` prices at `c * (sqrt(N+1) - sqrt(N))`. -/
theorem vonMangoldt_div_sqrt_invariant (c : ℝ) (hc : 0 ≤ c)
    (hRS : ∀ n : ℕ, chebyshevPsi n ≤ c * n) (N : ℕ) :
    ∑ n ∈ Finset.range (N + 1), Λ n / Real.sqrt n
      ≤ c * Real.sqrt N + chebyshevPsi N / Real.sqrt N := by
  induction N with
  | zero => simp [chebyshevPsi]
  | succ N ih =>
      have hb : (0 : ℝ) < Real.sqrt ((N : ℝ) + 1) :=
        Real.sqrt_pos.mpr (by positivity)
      have hab : Real.sqrt (N : ℝ) ≤ Real.sqrt ((N : ℝ) + 1) :=
        Real.sqrt_le_sqrt (by linarith)
      have hP : 0 ≤ chebyshevPsi N :=
        Finset.sum_nonneg fun n _ => ArithmeticFunction.vonMangoldt_nonneg
      have hPa : chebyshevPsi N ≤ c * Real.sqrt (N : ℝ) ^ 2 := by
        rw [Real.sq_sqrt (Nat.cast_nonneg N)]
        exact hRS N
      have hkey := abel_step_key hP hPa (Real.sqrt_nonneg _) hab hb hc
      have hψ : chebyshevPsi (N + 1) = chebyshevPsi N + Λ (N + 1) := by
        unfold chebyshevPsi
        exact Finset.sum_range_succ _ _
      rw [Finset.sum_range_succ]
      push_cast
      calc (∑ n ∈ Finset.range (N + 1), Λ n / Real.sqrt n)
            + Λ (N + 1) / Real.sqrt ((N : ℝ) + 1)
          ≤ (c * Real.sqrt (N : ℝ) + chebyshevPsi N / Real.sqrt (N : ℝ))
            + Λ (N + 1) / Real.sqrt ((N : ℝ) + 1) := by linarith [ih]
        _ ≤ (c * Real.sqrt ((N : ℝ) + 1) + chebyshevPsi N / Real.sqrt ((N : ℝ) + 1))
            + Λ (N + 1) / Real.sqrt ((N : ℝ) + 1) := by linarith [hkey]
        _ = c * Real.sqrt ((N : ℝ) + 1)
            + chebyshevPsi (N + 1) / Real.sqrt ((N : ℝ) + 1) := by
              rw [hψ, add_div]; ring

/-- **Partial summation, abstract constant (#CN-2).** From `psi(n) <= c n`
    (carried hypothesis) the weighted sum is at most `2 c sqrt(N)`: the
    invariant plus `psi(N)/sqrt(N) <= c N / sqrt(N) = c sqrt(N)`. -/
theorem vonMangoldt_div_sqrt_sum_le (c : ℝ) (hc : 0 ≤ c)
    (hRS : ∀ n : ℕ, chebyshevPsi n ≤ c * n) (N : ℕ) :
    ∑ n ∈ Finset.range (N + 1), Λ n / Real.sqrt n ≤ 2 * c * Real.sqrt N := by
  have h1 := vonMangoldt_div_sqrt_invariant c hc hRS N
  have h2 : chebyshevPsi N / Real.sqrt N ≤ c * Real.sqrt N := by
    have h3 : chebyshevPsi N / Real.sqrt N ≤ c * (N : ℝ) / Real.sqrt N := by
      gcongr
      exact hRS N
    rwa [mul_div_assoc, Real.div_sqrt] at h3
  calc ∑ n ∈ Finset.range (N + 1), Λ n / Real.sqrt n
      ≤ c * Real.sqrt N + chebyshevPsi N / Real.sqrt N := h1
    _ ≤ c * Real.sqrt N + c * Real.sqrt N := by linarith [h2]
    _ = 2 * c * Real.sqrt N := by ring

/-- **The Rosser-Schoenfeld corollary (#CN-2, the dossier's exact constants).**
    EXTERNAL hypothesis `hRS`: `psi(x) < 1.03883 x` for all `x > 0`
    (Rosser-Schoenfeld 1962, Theorem 12; not in Mathlib), carried in the
    weaker `<=`-at-integers form actually consumed. Conclusion: the e2be
    prime-sum constant `S_N <= 2.07766 sqrt(N)`, with `2.07766 = 2 * 1.03883`
    exact as rationals. -/
theorem rosser_schoenfeld_partial_sum
    (hRS : ∀ n : ℕ, chebyshevPsi n ≤ (103883 / 100000 : ℝ) * n) (N : ℕ) :
    ∑ n ∈ Finset.range (N + 1), Λ n / Real.sqrt n
      ≤ (207766 / 100000 : ℝ) * Real.sqrt N := by
  have h := vonMangoldt_div_sqrt_sum_le (103883 / 100000) (by norm_num) hRS N
  have hconst : (207766 / 100000 : ℝ) = 2 * (103883 / 100000) := by norm_num
  rw [hconst]
  exact h

/-! ## #CN-3: the linear-interpolation error bound (e2be-3) -/

/-- **The doubled-Rolle kernel (#CN-3).** For `x` strictly between the nodes,
    the interpolation error equals `g''(xi)/2 * (x - x0)(x - x1)` at some
    interior `xi`: the auxiliary function `phi(t) = g(t) - L(t) - K (t-x0)(t-x1)`
    vanishes at `x0`, `x`, `x1`, so Rolle applied twice hands `phi'` two zeros
    and `phi''` one, and `phi'' = g'' - 2K` pins `K`. -/
theorem interp_error_eq_second_deriv (g g' g'' : ℝ → ℝ) (x0 x1 x : ℝ)
    (hg' : ∀ t, HasDerivAt g (g' t) t) (hg'' : ∀ t, HasDerivAt g' (g'' t) t)
    (h0x : x0 < x) (hx1 : x < x1) :
    ∃ ξ ∈ Set.Ioo x0 x1,
      g x - (g x0 + (g x1 - g x0) / (x1 - x0) * (x - x0))
        = g'' ξ / 2 * ((x - x0) * (x - x1)) := by
  have h01 : x0 < x1 := h0x.trans hx1
  set m : ℝ := (g x1 - g x0) / (x1 - x0) with hm
  set D : ℝ := (x - x0) * (x - x1) with hD
  have hDne : D ≠ 0 := by
    have h1 : 0 < x - x0 := sub_pos.mpr h0x
    have h2 : x - x1 < 0 := sub_neg.mpr hx1
    exact (mul_neg_of_pos_of_neg h1 h2).ne
  set E : ℝ := g x - (g x0 + m * (x - x0)) with hE
  set K : ℝ := E / D with hK
  -- the auxiliary function and its first two derivatives
  have hφ : ∀ t, HasDerivAt
      (fun t => g t - (g x0 + m * (t - x0)) - K * ((t - x0) * (t - x1)))
      (g' t - m - K * ((t - x1) + (t - x0))) t := by
    intro t
    have h := ((hg' t).fun_sub
        ((((hasDerivAt_id t).sub_const x0).const_mul m).const_add (g x0))).fun_sub
      ((((hasDerivAt_id t).sub_const x0).fun_mul
        ((hasDerivAt_id t).sub_const x1)).const_mul K)
    have heq : g' t - m - K * ((t - x1) + (t - x0))
        = g' t - m * 1 - K * (1 * (t - x1) + (t - x0) * 1) := by ring
    rw [heq]
    exact h
  have hφ' : ∀ t, HasDerivAt
      (fun t => g' t - m - K * ((t - x1) + (t - x0)))
      (g'' t - K * 2) t := by
    intro t
    have h := ((hg'' t).sub_const m).fun_sub
      ((((hasDerivAt_id t).sub_const x1).fun_add
        ((hasDerivAt_id t).sub_const x0)).const_mul K)
    have heq : g'' t - K * 2 = g'' t - K * (1 + 1) := by ring
    rw [heq]
    exact h
  have hφcont : Continuous
      (fun t => g t - (g x0 + m * (t - x0)) - K * ((t - x0) * (t - x1))) :=
    continuous_iff_continuousAt.mpr fun t => (hφ t).continuousAt
  have hφ'cont : Continuous
      (fun t => g' t - m - K * ((t - x1) + (t - x0))) :=
    continuous_iff_continuousAt.mpr fun t => (hφ' t).continuousAt
  -- the three vanishing values
  have hφx0 : (fun t => g t - (g x0 + m * (t - x0)) - K * ((t - x0) * (t - x1))) x0
      = 0 := by simp
  have hφx1 : (fun t => g t - (g x0 + m * (t - x0)) - K * ((t - x0) * (t - x1))) x1
      = 0 := by
    show g x1 - (g x0 + m * (x1 - x0)) - K * ((x1 - x0) * (x1 - x1)) = 0
    rw [hm, div_mul_cancel₀ _ (sub_ne_zero.mpr h01.ne')]
    ring
  have hφxx : (fun t => g t - (g x0 + m * (t - x0)) - K * ((t - x0) * (t - x1))) x
      = 0 := by
    show g x - (g x0 + m * (x - x0)) - K * ((x - x0) * (x - x1)) = 0
    rw [← hE, ← hD, hK, div_mul_cancel₀ E hDne, sub_self]
  -- Rolle on [x0, x] and [x, x1], then on [xi1, xi2]
  obtain ⟨ξ1, hξ1mem, hξ1eq⟩ := exists_hasDerivAt_eq_zero h0x
    hφcont.continuousOn (hφx0.trans hφxx.symm) (fun t _ => hφ t)
  obtain ⟨ξ2, hξ2mem, hξ2eq⟩ := exists_hasDerivAt_eq_zero hx1
    hφcont.continuousOn (hφxx.trans hφx1.symm) (fun t _ => hφ t)
  have hξ12 : ξ1 < ξ2 := hξ1mem.2.trans hξ2mem.1
  obtain ⟨ξ, hξmem, hξeq⟩ := exists_hasDerivAt_eq_zero hξ12
    hφ'cont.continuousOn (hξ1eq.trans hξ2eq.symm) (fun t _ => hφ' t)
  refine ⟨ξ, ⟨hξ1mem.1.trans hξmem.1, hξmem.2.trans hξ2mem.2⟩, ?_⟩
  -- phi''(xi) = 0 pins K = g''(xi)/2, and E = K * D by construction
  have hKD : K * D = E := by
    rw [hK]
    exact div_mul_cancel₀ E hDne
  have hK2 : g'' ξ / 2 = K := by linarith
  rw [← hKD, ← hK2]

/-- **The linear-interpolation error bound (#CN-3, sharp constant).** The
    dossier's `(dx^2/8) sup|c''|` clause: for `|g''| <= B` the interpolant
    between `x0 < x1` errs by at most `(B/8)(x1 - x0)^2` on the whole
    interval. Endpoints are exact; interior points pay
    `|g''(xi)|/2 * (x-x0)(x1-x) <= (B/2) * ((x1-x0)/2)^2` by AM-GM. -/
theorem linear_interpolation_error (g g' g'' : ℝ → ℝ) (B x0 x1 x : ℝ)
    (hg' : ∀ t, HasDerivAt g (g' t) t) (hg'' : ∀ t, HasDerivAt g' (g'' t) t)
    (hB : ∀ t, |g'' t| ≤ B) (h01 : x0 < x1) (hx : x ∈ Set.Icc x0 x1) :
    |g x - (g x0 + (g x1 - g x0) / (x1 - x0) * (x - x0))|
      ≤ B / 8 * (x1 - x0) ^ 2 := by
  have hBnn : 0 ≤ B := le_trans (abs_nonneg _) (hB 0)
  have hRHS : 0 ≤ B / 8 * (x1 - x0) ^ 2 :=
    mul_nonneg (div_nonneg hBnn (by norm_num)) (sq_nonneg _)
  obtain ⟨hx0, hx1⟩ := hx
  rcases hx0.eq_or_lt with h0 | h0
  · -- x = x0: the interpolant is exact at the left node
    rw [← h0]
    simp only [sub_self, mul_zero, add_zero, abs_zero]
    exact hRHS
  rcases hx1.eq_or_lt with h1 | h1
  · -- x = x1: exact at the right node
    rw [h1]
    have hzero : g x1 - (g x0 + (g x1 - g x0) / (x1 - x0) * (x1 - x0)) = 0 := by
      rw [div_mul_cancel₀ _ (sub_ne_zero.mpr h01.ne')]
      ring
    rw [hzero, abs_zero]
    exact hRHS
  · -- interior: the doubled-Rolle kernel plus AM-GM
    obtain ⟨ξ, _, hξ⟩ :=
      interp_error_eq_second_deriv g g' g'' x0 x1 x hg' hg'' h0 h1
    rw [hξ, abs_mul]
    have h2 : |g'' ξ / 2| ≤ B / 2 := by
      rw [abs_div, abs_two]
      gcongr
      exact hB ξ
    have h3 : |(x - x0) * (x - x1)| ≤ (x1 - x0) ^ 2 / 4 := by
      rw [abs_mul, abs_of_pos (sub_pos.mpr h0), abs_sub_comm,
        abs_of_pos (sub_pos.mpr h1)]
      nlinarith [sq_nonneg (x1 + x0 - 2 * x)]
    calc |g'' ξ / 2| * |(x - x0) * (x - x1)|
        ≤ B / 2 * ((x1 - x0) ^ 2 / 4) :=
          mul_le_mul h2 h3 (abs_nonneg _) (by linarith)
      _ = B / 8 * (x1 - x0) ^ 2 := by ring

/-! ## #CN-4: the Gaussian-tail chain behind E_P (e2be-1) -/

/-- Completing the square in the E_P exponent (#CN-4, step 1):
    `u/2 - u^2/(4 s^2) = s^2/4 - (u - s^2)^2/(4 s^2)`. -/
theorem exponent_complete_square (σ u : ℝ) (hσ : σ ≠ 0) :
    u / 2 - u ^ 2 / (4 * σ ^ 2) = σ ^ 2 / 4 - (u - σ ^ 2) ^ 2 / (4 * σ ^ 2) := by
  field_simp
  ring

/-- The E_P integrand splits into a shifted-linear part (exactly integrable)
    and a constant part (#CN-4, step 2). -/
theorem tail_integrand_eq (σ u : ℝ) (hσ : σ ≠ 0) :
    u * Real.exp (u / 2 - u ^ 2 / (4 * σ ^ 2))
      = (u - σ ^ 2)
          * (Real.exp (σ ^ 2 / 4) * Real.exp (-((u - σ ^ 2) ^ 2 / (4 * σ ^ 2))))
        + σ ^ 2
          * (Real.exp (σ ^ 2 / 4) * Real.exp (-((u - σ ^ 2) ^ 2 / (4 * σ ^ 2)))) := by
  rw [exponent_complete_square σ u hσ, sub_eq_add_neg, Real.exp_add]
  ring

/-- The closed-form antiderivative of the shifted-linear part (#CN-4, step 3):
    `d/du [-2 s^2 e^{s^2/4} e^{-(u-s^2)^2/4s^2}]
       = (u - s^2) e^{s^2/4} e^{-(u-s^2)^2/4s^2}`. -/
theorem hasDerivAt_gaussian_antideriv (σ : ℝ) (hσ : σ ≠ 0) (u : ℝ) :
    HasDerivAt
      (fun v => -(2 * σ ^ 2) * Real.exp (σ ^ 2 / 4)
        * Real.exp (-((v - σ ^ 2) ^ 2 / (4 * σ ^ 2))))
      ((u - σ ^ 2)
        * (Real.exp (σ ^ 2 / 4) * Real.exp (-((u - σ ^ 2) ^ 2 / (4 * σ ^ 2))))) u := by
  have h := (((((hasDerivAt_id u).sub_const (σ ^ 2)).fun_pow 2).div_const
      (4 * σ ^ 2)).fun_neg.exp).const_mul (-(2 * σ ^ 2) * Real.exp (σ ^ 2 / 4))
  have heq : (u - σ ^ 2)
      * (Real.exp (σ ^ 2 / 4) * Real.exp (-((u - σ ^ 2) ^ 2 / (4 * σ ^ 2))))
      = -(2 * σ ^ 2) * Real.exp (σ ^ 2 / 4)
        * (Real.exp (-((u - σ ^ 2) ^ 2 / (4 * σ ^ 2)))
          * -(2 * (u - σ ^ 2) ^ 1 * 1 / (4 * σ ^ 2))) := by
    field_simp
    ring
  rw [heq]
  exact h

/-- The antiderivative dies at infinity (#CN-4, step 4). -/
theorem tendsto_gaussian_antideriv (σ : ℝ) (hσ : 0 < σ) :
    Tendsto
      (fun v => -(2 * σ ^ 2) * Real.exp (σ ^ 2 / 4)
        * Real.exp (-((v - σ ^ 2) ^ 2 / (4 * σ ^ 2))))
      atTop (𝓝 0) := by
  have h1 : Tendsto (fun v : ℝ => v - σ ^ 2) atTop atTop := by
    simpa [sub_eq_add_neg] using
      tendsto_atTop_add_const_right atTop (-(σ ^ 2)) tendsto_id
  have h2 : Tendsto (fun v : ℝ => (v - σ ^ 2) ^ 2 / (4 * σ ^ 2)) atTop atTop := by
    apply Tendsto.atTop_div_const (by positivity)
    exact (tendsto_pow_atTop two_ne_zero).comp h1
  have h3 : Tendsto (fun v : ℝ => -((v - σ ^ 2) ^ 2 / (4 * σ ^ 2))) atTop atBot :=
    tendsto_neg_atTop_atBot.comp h2
  have h4 : Tendsto (fun v : ℝ => Real.exp (-((v - σ ^ 2) ^ 2 / (4 * σ ^ 2))))
      atTop (𝓝 0) := Real.tendsto_exp_atBot.comp h3
  have h5 := h4.const_mul (-(2 * σ ^ 2) * Real.exp (σ ^ 2 / 4))
  simpa using h5

/-- The shifted-linear part integrates exactly on the tail (#CN-4, step 5):
    `int_U^inf (u - s^2) e^{s^2/4} e^{-(u-s^2)^2/4s^2} du
       = 2 s^2 e^{s^2/4} e^{-(U-s^2)^2/4s^2}`. -/
theorem integral_gaussian_tail_shifted (σ U : ℝ) (hσ : 0 < σ) (hU : σ ^ 2 ≤ U) :
    ∫ u in Set.Ioi U, (u - σ ^ 2)
        * (Real.exp (σ ^ 2 / 4) * Real.exp (-((u - σ ^ 2) ^ 2 / (4 * σ ^ 2))))
      = 2 * σ ^ 2 * Real.exp (σ ^ 2 / 4)
        * Real.exp (-((U - σ ^ 2) ^ 2 / (4 * σ ^ 2))) := by
  have key := integral_Ioi_of_hasDerivAt_of_nonneg'
    (fun u _ => hasDerivAt_gaussian_antideriv σ hσ.ne' u)
    (fun u hu => by
      have huU : U < u := hu
      have : (0 : ℝ) ≤ u - σ ^ 2 := by linarith
      positivity)
    (tendsto_gaussian_antideriv σ hσ)
  rw [key]
  ring

/-- The shifted-linear part is integrable on the tail (#CN-4, step 5'):
    free from nonnegativity of the derivative plus the limit at infinity. -/
theorem integrableOn_gaussian_tail_shifted (σ U : ℝ) (hσ : 0 < σ)
    (hU : σ ^ 2 ≤ U) :
    IntegrableOn
      (fun u => (u - σ ^ 2)
        * (Real.exp (σ ^ 2 / 4) * Real.exp (-((u - σ ^ 2) ^ 2 / (4 * σ ^ 2)))))
      (Set.Ioi U) :=
  integrableOn_Ioi_deriv_of_nonneg'
    (fun u _ => hasDerivAt_gaussian_antideriv σ hσ.ne' u)
    (fun u hu => by
      have huU : U < u := hu
      have : (0 : ℝ) ≤ u - σ ^ 2 := by linarith
      positivity)
    (tendsto_gaussian_antideriv σ hσ)

/-- The pointwise domination of the full integrand by the exactly-integrable
    part (#CN-4, step 6): on `u >= U > s^2` the constant piece is at most
    `s^2/(U - s^2)` times the linear piece. -/
theorem tail_integrand_le (σ U u : ℝ) (hσ : 0 < σ) (hU : σ ^ 2 < U)
    (hu : U ≤ u) :
    u * Real.exp (u / 2 - u ^ 2 / (4 * σ ^ 2))
      ≤ (1 + σ ^ 2 / (U - σ ^ 2))
        * ((u - σ ^ 2)
          * (Real.exp (σ ^ 2 / 4) * Real.exp (-((u - σ ^ 2) ^ 2 / (4 * σ ^ 2))))) := by
  rw [tail_integrand_eq σ u hσ.ne']
  have ha : 0 < U - σ ^ 2 := sub_pos.mpr hU
  have hcoef : σ ^ 2 ≤ σ ^ 2 / (U - σ ^ 2) * (u - σ ^ 2) := by
    rw [div_mul_eq_mul_div, le_div_iff₀ ha]
    exact mul_le_mul_of_nonneg_left (by linarith) (sq_nonneg σ)
  have hexp : (0 : ℝ) < Real.exp (σ ^ 2 / 4)
      * Real.exp (-((u - σ ^ 2) ^ 2 / (4 * σ ^ 2))) := by positivity
  nlinarith [mul_le_mul_of_nonneg_right hcoef hexp.le]

/-- **The Gaussian-tail bound (#CN-4, the E_P chain assembled).** For
    `sigma > 0` and any horizon `U > sigma^2` (the dossier's `U = ln N`,
    `a = ln N - sigma^2 > 0`):
    `int_U^inf u e^{u/2 - u^2/4s^2} du
       <= 2 s^2 e^{s^2/4} (1 + s^2/(U - s^2)) e^{-(U-s^2)^2/4s^2}`,
    which is the dossier's `E_P` up to its cited `2 sqrt(pi) sigma`
    autocorrelation prefactor. -/
theorem gaussian_tail_le (σ U : ℝ) (hσ : 0 < σ) (hU : σ ^ 2 < U) :
    ∫ u in Set.Ioi U, u * Real.exp (u / 2 - u ^ 2 / (4 * σ ^ 2))
      ≤ 2 * σ ^ 2 * Real.exp (σ ^ 2 / 4) * (1 + σ ^ 2 / (U - σ ^ 2))
        * Real.exp (-((U - σ ^ 2) ^ 2 / (4 * σ ^ 2))) := by
  have hint := integrableOn_gaussian_tail_shifted σ U hσ hU.le
  have hval := integral_gaussian_tail_shifted σ U hσ hU.le
  have hupper : IntegrableOn
      (fun u => (1 + σ ^ 2 / (U - σ ^ 2))
        * ((u - σ ^ 2)
          * (Real.exp (σ ^ 2 / 4) * Real.exp (-((u - σ ^ 2) ^ 2 / (4 * σ ^ 2))))))
      (Set.Ioi U) := hint.const_mul _
  have hnn : (0 : ℝ → ℝ)
      ≤ᵐ[volume.restrict (Set.Ioi U)]
        fun u => u * Real.exp (u / 2 - u ^ 2 / (4 * σ ^ 2)) := by
    filter_upwards [ae_restrict_mem measurableSet_Ioi] with u hu
    simp only [Pi.zero_apply]
    have h0u : (0 : ℝ) < u := lt_of_le_of_lt (sq_nonneg σ) (hU.trans hu)
    positivity
  have hle : (fun u => u * Real.exp (u / 2 - u ^ 2 / (4 * σ ^ 2)))
      ≤ᵐ[volume.restrict (Set.Ioi U)]
        fun u => (1 + σ ^ 2 / (U - σ ^ 2))
          * ((u - σ ^ 2)
            * (Real.exp (σ ^ 2 / 4) * Real.exp (-((u - σ ^ 2) ^ 2 / (4 * σ ^ 2))))) := by
    filter_upwards [ae_restrict_mem measurableSet_Ioi] with u hu
    exact tail_integrand_le σ U u hσ hU (Set.mem_Ioi.mp hu).le
  calc ∫ u in Set.Ioi U, u * Real.exp (u / 2 - u ^ 2 / (4 * σ ^ 2))
      ≤ ∫ u in Set.Ioi U, (1 + σ ^ 2 / (U - σ ^ 2))
          * ((u - σ ^ 2)
            * (Real.exp (σ ^ 2 / 4) * Real.exp (-((u - σ ^ 2) ^ 2 / (4 * σ ^ 2))))) :=
        integral_mono_of_nonneg hnn hupper hle
    _ = (1 + σ ^ 2 / (U - σ ^ 2))
          * ∫ u in Set.Ioi U, (u - σ ^ 2)
            * (Real.exp (σ ^ 2 / 4) * Real.exp (-((u - σ ^ 2) ^ 2 / (4 * σ ^ 2)))) :=
        integral_const_mul _ _
    _ = 2 * σ ^ 2 * Real.exp (σ ^ 2 / 4) * (1 + σ ^ 2 / (U - σ ^ 2))
          * Real.exp (-((U - σ ^ 2) ^ 2 / (4 * σ ^ 2))) := by
        rw [hval]; ring

/-! ## Axiom audit: every theorem must use only the Mathlib foundations. -/

#print axioms cosine_sum_abs_le
#print axioms cosine_sum_at_zero
#print axioms cosine_sum_max_at_zero
#print axioms abel_step_key
#print axioms vonMangoldt_div_sqrt_invariant
#print axioms vonMangoldt_div_sqrt_sum_le
#print axioms rosser_schoenfeld_partial_sum
#print axioms interp_error_eq_second_deriv
#print axioms linear_interpolation_error
#print axioms exponent_complete_square
#print axioms tail_integrand_eq
#print axioms hasDerivAt_gaussian_antideriv
#print axioms tendsto_gaussian_antideriv
#print axioms integral_gaussian_tail_shifted
#print axioms integrableOn_gaussian_tail_shifted
#print axioms tail_integrand_le
#print axioms gaussian_tail_le

end ZetaRH.CertificationNuggets
