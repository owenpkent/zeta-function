/-
Three digamma identities not yet in Mathlib, proved against the UPSTREAM
`Complex.digamma` (the verified Tier-1 contribution).

## What this file is

Mathlib master (as of v4.30.0) ships `Mathlib/Analysis/SpecialFunctions/Gamma/Digamma.lean`
with `Complex.digamma := logDeriv Gamma`, the recurrence `digamma_apply_add_one`, and
the special values `digamma_one` / `digamma_one_half`. It does NOT have the reflection,
iterated-recurrence, or duplication formulas. This file proves those three about the
UPSTREAM `Complex.digamma` (not the project's local copy in `ExplicitFormula.lean`),
using only Mathlib lemmas, so it is a self-contained PR-ready unit.

These proofs are kernel-verified GREEN against Lean/Mathlib v4.30.0 (the substrate's
post-bump pin). `#print axioms` for each is exactly `[propext, Classical.choice, Quot.sound]`
(no `sorryAx`). They were lifted from the project's local versions in
`ExplicitFormula.lean` (which used a local `digamma := logDeriv Complex.Gamma`, definitionally
equal to `Complex.digamma`); the only adaptations were the recurrence name
(`digamma_add_one` -> `digamma_apply_add_one`, `1/s` -> `s⁻¹`) and unfolding via `digamma_def`.

To upstream: drop these three theorems into Mathlib's `Digamma.lean` (they already live in
`namespace Complex`). See [`../upstream/digamma_contribution.md`](../upstream/digamma_contribution.md).

No em dashes anywhere in this file (project style rule).
-/

import Mathlib.Analysis.SpecialFunctions.Gamma.Digamma
import Mathlib.Analysis.SpecialFunctions.Gamma.Beta
import Mathlib.Analysis.SpecialFunctions.Gamma.Deriv
import Mathlib.Analysis.Calculus.LogDeriv
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

namespace Complex

/-- **The iterated digamma recurrence** `ψ(s+n) = ψ(s) + ∑_{k<n} 1/(s+k)`, for
    `s ∉ {0, -1, -2, …}`. Proved by induction from `digamma_apply_add_one`. -/
theorem digamma_apply_add_nat {s : ℂ} (hs : ∀ m : ℕ, s ≠ -(m : ℂ)) (n : ℕ) :
    digamma (s + n) = digamma s + ∑ k ∈ Finset.range n, (s + k)⁻¹ := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hsn : ∀ m : ℕ, s + (n : ℂ) ≠ -(m : ℂ) := by
      intro m h
      exact hs (m + n) (by push_cast at h ⊢; linear_combination h)
    have estep : s + ((n + 1 : ℕ) : ℂ) = (s + (n : ℂ)) + 1 := by push_cast; ring
    rw [estep, digamma_apply_add_one _ hsn, ih, Finset.sum_range_succ]
    ring

/-- **The digamma reflection formula** `ψ(1-s) - ψ(s) = π cot(π s)`, for `s ∉ ℤ`.
    Proved from `Complex.Gamma_mul_Gamma_one_sub` by taking logarithmic derivatives. -/
theorem digamma_reflection {s : ℂ} (hs : ∀ m : ℤ, s ≠ m) :
    digamma (1 - s) - digamma s
      = (Real.pi : ℂ) * (Complex.cos ((Real.pi : ℂ) * s) / Complex.sin ((Real.pi : ℂ) * s)) := by
  have hs_not_nat (m : ℕ) : s ≠ -m := by
    intro h
    exact hs (-m) (by push_cast; exact h)
  have hs_one_not_nat (m : ℕ) : 1 - s ≠ -m := by
    intro h
    have : s = 1 + m := by linear_combination -h
    exact hs (1 + m) (by push_cast; exact this)
  have hΓs : Complex.Gamma s ≠ 0 := Complex.Gamma_ne_zero hs_not_nat
  have hΓ1s : Complex.Gamma (1 - s) ≠ 0 := Complex.Gamma_ne_zero hs_one_not_nat
  have hdΓs : DifferentiableAt ℂ Complex.Gamma s := Complex.differentiableAt_Gamma s hs_not_nat
  have h1 : DifferentiableAt ℂ Complex.Gamma (1 - s) := Complex.differentiableAt_Gamma (1 - s) hs_one_not_nat
  have h2 : DifferentiableAt ℂ (fun z : ℂ => 1 - z) s := by fun_prop
  have hdΓ1s : DifferentiableAt ℂ (fun z => Complex.Gamma (1 - z)) s := h1.comp s h2
  have h_mul_deriv := logDeriv_mul s hΓs hΓ1s hdΓs hdΓ1s
  have h_comp_deriv : logDeriv (fun z => Complex.Gamma (1 - z)) s = - digamma (1 - s) := by
    have key := logDeriv_comp (f := Complex.Gamma) (g := fun z : ℂ => 1 - z) h1 h2
    have hd : deriv (fun z : ℂ => 1 - z) s = -1 :=
      ((hasDerivAt_id s).const_sub 1).deriv
    rw [hd, mul_neg_one] at key
    exact key
  have h_LHS : logDeriv (fun z => Complex.Gamma z * Complex.Gamma (1 - z)) s = digamma s - digamma (1 - s) := by
    rw [h_mul_deriv, h_comp_deriv, sub_eq_add_neg]
    rfl
  have h_eq : (fun z => Complex.Gamma z * Complex.Gamma (1 - z)) = fun z => (Real.pi : ℂ) / Complex.sin ((Real.pi : ℂ) * z) := by
    ext z
    exact Complex.Gamma_mul_Gamma_one_sub z
  have hs_sin : Complex.sin ((Real.pi : ℂ) * s) ≠ 0 := by
    intro h
    rw [Complex.sin_eq_zero_iff] at h
    rcases h with ⟨k, hk⟩
    have hk_eq : (Real.pi : ℂ) * s = (Real.pi : ℂ) * k := by
      calc
        (Real.pi : ℂ) * s = (k : ℂ) * (Real.pi : ℂ) := hk
        _ = (Real.pi : ℂ) * (k : ℂ) := mul_comm _ _
    have h_pi : (Real.pi : ℂ) ≠ 0 := by norm_cast; exact Real.pi_ne_zero
    have h_eq_k : s = k := mul_left_cancel₀ h_pi hk_eq
    exact hs k h_eq_k
  have hd_sin_comp : DifferentiableAt ℂ (fun z => Complex.sin ((Real.pi : ℂ) * z)) s := by fun_prop
  have hd_pi : DifferentiableAt ℂ (fun _ : ℂ => (Real.pi : ℂ)) s := by fun_prop
  have h_div_deriv := logDeriv_div s (by norm_cast; exact Real.pi_ne_zero) hs_sin hd_pi hd_sin_comp
  have h_logDeriv_pi : logDeriv (fun _ : ℂ => (Real.pi : ℂ)) s = 0 := by
    rw [logDeriv_apply, deriv_const, zero_div]
  have h_sin_comp_deriv : logDeriv (fun z => Complex.sin ((Real.pi : ℂ) * z)) s = (Real.pi : ℂ) * (Complex.cos ((Real.pi : ℂ) * s) / Complex.sin ((Real.pi : ℂ) * s)) := by
    have h1_sin : DifferentiableAt ℂ Complex.sin ((Real.pi : ℂ) * s) := by fun_prop
    have h2_sin : DifferentiableAt ℂ (fun z : ℂ => (Real.pi : ℂ) * z) s := by fun_prop
    have key := logDeriv_comp (f := Complex.sin) (g := fun z : ℂ => (Real.pi : ℂ) * z) h1_sin h2_sin
    have hd_inner : deriv (fun z : ℂ => (Real.pi : ℂ) * z) s = (Real.pi : ℂ) := by
      rw [deriv_const_mul]
      · simp
      · fun_prop
    rw [hd_inner] at key
    have h_logDeriv_sin : logDeriv Complex.sin ((Real.pi : ℂ) * s) = Complex.cos ((Real.pi : ℂ) * s) / Complex.sin ((Real.pi : ℂ) * s) := by
      rw [logDeriv_apply]
      have hds : deriv Complex.sin ((Real.pi : ℂ) * s) = Complex.cos ((Real.pi : ℂ) * s) := by simp
      rw [hds]
    rw [h_logDeriv_sin] at key
    calc
      logDeriv (fun z => Complex.sin ((Real.pi : ℂ) * z)) s = logDeriv (Complex.sin ∘ fun z => (Real.pi : ℂ) * z) s := rfl
      _ = Complex.cos ((Real.pi : ℂ) * s) / Complex.sin ((Real.pi : ℂ) * s) * (Real.pi : ℂ) := key
      _ = (Real.pi : ℂ) * (Complex.cos ((Real.pi : ℂ) * s) / Complex.sin ((Real.pi : ℂ) * s)) := by ring
  have h_RHS : logDeriv (fun z => (Real.pi : ℂ) / Complex.sin ((Real.pi : ℂ) * z)) s = - ((Real.pi : ℂ) * (Complex.cos ((Real.pi : ℂ) * s) / Complex.sin ((Real.pi : ℂ) * s))) := by
    rw [h_div_deriv, h_logDeriv_pi, h_sin_comp_deriv, zero_sub]
  have h_final : digamma s - digamma (1 - s) = - ((Real.pi : ℂ) * (Complex.cos ((Real.pi : ℂ) * s) / Complex.sin ((Real.pi : ℂ) * s))) := by
    calc
      digamma s - digamma (1 - s) = logDeriv (fun z => Complex.Gamma z * Complex.Gamma (1 - z)) s := h_LHS.symm
      _ = logDeriv (fun z => (Real.pi : ℂ) / Complex.sin ((Real.pi : ℂ) * z)) s := by rw [h_eq]
      _ = - ((Real.pi : ℂ) * (Complex.cos ((Real.pi : ℂ) * s) / Complex.sin ((Real.pi : ℂ) * s))) := h_RHS
  linear_combination -h_final

/-- **The digamma duplication formula** `ψ(2s) = ½(ψ(s) + ψ(s+½)) + log 2`, for
    `s, s+½ ∉ {0, -1, -2, …}`. Proved from Legendre's doubling
    `Complex.Gamma_mul_Gamma_add_half` by taking logarithmic derivatives. -/
theorem digamma_two_mul {s : ℂ} (hs : ∀ m : ℕ, s ≠ -(m : ℂ))
    (hsh : ∀ m : ℕ, s + 1 / 2 ≠ -(m : ℂ)) :
    digamma (2 * s) = (1 / 2) * (digamma s + digamma (s + 1 / 2)) + Complex.log 2 := by
  have h2s : ∀ m : ℕ, 2 * s ≠ -(m : ℂ) := by
    intro m h
    rcases Nat.even_or_odd m with ⟨k, hk⟩ | ⟨k, hk⟩
    · exact hs k (by subst hk; push_cast at h ⊢; linear_combination h / 2)
    · exact hsh k (by subst hk; push_cast at h ⊢; linear_combination h / 2)
  have hΓs : Complex.Gamma s ≠ 0 := Complex.Gamma_ne_zero hs
  have hΓsh : Complex.Gamma (s + 1 / 2) ≠ 0 := Complex.Gamma_ne_zero hsh
  have hdΓs : DifferentiableAt ℂ Complex.Gamma s := Complex.differentiableAt_Gamma s hs
  have hdΓsh : DifferentiableAt ℂ Complex.Gamma (s + 1 / 2) := Complex.differentiableAt_Gamma _ hsh
  have hdΓ2s : DifferentiableAt ℂ Complex.Gamma (2 * s) := Complex.differentiableAt_Gamma _ h2s
  have hsqrt : ((Real.sqrt Real.pi : ℝ) : ℂ) ≠ 0 := by
    simpa using Real.sqrt_ne_zero'.mpr Real.pi_pos
  have hfun : logDeriv (fun z : ℂ => Complex.Gamma z * Complex.Gamma (z + 1 / 2)) s
            = logDeriv (fun z : ℂ => Complex.Gamma (2 * z) * (2 : ℂ) ^ (1 - 2 * z)
                * ((Real.sqrt Real.pi : ℝ) : ℂ)) s := by
    congr 1; funext z; exact Complex.Gamma_mul_Gamma_add_half z
  have hg_sh : DifferentiableAt ℂ (fun z : ℂ => Complex.Gamma (z + 1 / 2)) s :=
    hdΓsh.comp s (by fun_prop)
  have hLHS_comp : logDeriv (fun z : ℂ => Complex.Gamma (z + 1 / 2)) s = digamma (s + 1 / 2) := by
    have key := logDeriv_comp (f := Complex.Gamma) (g := fun z : ℂ => z + 1 / 2) hdΓsh (by fun_prop)
    have hd : deriv (fun z : ℂ => z + 1 / 2) s = 1 := by simp
    rw [hd, mul_one] at key
    simpa [digamma_def, Function.comp_def] using key
  have hLHS : logDeriv (fun z : ℂ => Complex.Gamma z * Complex.Gamma (z + 1 / 2)) s
            = digamma s + digamma (s + 1 / 2) := by
    rw [logDeriv_mul s hΓs hΓsh hdΓs hg_sh, hLHS_comp]; rfl
  have hexp_eq : (fun z : ℂ => (2 : ℂ) ^ (1 - 2 * z))
             = (fun z : ℂ => Complex.exp (Complex.log 2 * (1 - 2 * z))) := by
    funext z; rw [Complex.cpow_def_of_ne_zero (by norm_num : (2 : ℂ) ≠ 0)]
  have hcpow : logDeriv (fun z : ℂ => (2 : ℂ) ^ (1 - 2 * z)) s = -2 * Complex.log 2 := by
    rw [hexp_eq]
    have h2z : HasDerivAt (fun z : ℂ => 2 * z) 2 s := by simpa using (hasDerivAt_id s).const_mul 2
    have h1 : HasDerivAt (fun z : ℂ => 1 - 2 * z) (-2) s := by simpa using h2z.const_sub 1
    have hd : HasDerivAt (fun z : ℂ => Complex.log 2 * (1 - 2 * z)) (Complex.log 2 * -2) s :=
      h1.const_mul (Complex.log 2)
    have hf := hd.cexp
    rw [logDeriv_apply, hf.deriv]
    field_simp
  have hG2 : logDeriv (fun z : ℂ => Complex.Gamma (2 * z)) s = 2 * digamma (2 * s) := by
    have key := logDeriv_comp (f := Complex.Gamma) (g := fun z : ℂ => 2 * z) hdΓ2s (by fun_prop)
    have hd : deriv (fun z : ℂ => 2 * z) s = 2 := by
      simpa using ((hasDerivAt_id s).const_mul 2).deriv
    rw [hd] at key
    simp only [digamma_def, Function.comp_def] at key ⊢
    rw [key]; ring
  have hΓ2s_ne : Complex.Gamma (2 * s) ≠ 0 := Complex.Gamma_ne_zero h2s
  have hcpow_ne : (2 : ℂ) ^ (1 - 2 * s) ≠ 0 := by
    rw [Complex.cpow_def_of_ne_zero (by norm_num : (2 : ℂ) ≠ 0)]; exact Complex.exp_ne_zero _
  have hd1 : DifferentiableAt ℂ (fun z : ℂ => Complex.Gamma (2 * z)) s := hdΓ2s.comp s (by fun_prop)
  have hd2 : DifferentiableAt ℂ (fun z : ℂ => (2 : ℂ) ^ (1 - 2 * z)) s := by
    rw [hexp_eq]
    have h2z : HasDerivAt (fun z : ℂ => 2 * z) 2 s := by simpa using (hasDerivAt_id s).const_mul 2
    have h1 : HasDerivAt (fun z : ℂ => 1 - 2 * z) (-2) s := by simpa using h2z.const_sub 1
    exact ((h1.const_mul (Complex.log 2)).cexp).differentiableAt
  have hRHS : logDeriv (fun z : ℂ => Complex.Gamma (2 * z) * (2 : ℂ) ^ (1 - 2 * z)
                * ((Real.sqrt Real.pi : ℝ) : ℂ)) s = 2 * digamma (2 * s) - 2 * Complex.log 2 := by
    rw [logDeriv_mul_const s ((Real.sqrt Real.pi : ℝ) : ℂ) hsqrt,
        logDeriv_mul (f := fun z : ℂ => Complex.Gamma (2 * z))
          (g := fun z : ℂ => (2 : ℂ) ^ (1 - 2 * z)) s hΓ2s_ne hcpow_ne hd1 hd2,
        hG2, hcpow]
    ring
  have key : digamma s + digamma (s + 1 / 2) = 2 * digamma (2 * s) - 2 * Complex.log 2 := by
    rw [← hLHS, hfun, hRHS]
  linear_combination (-1 / 2 : ℂ) * key

end Complex

-- De-smuggling certificate: each identity depends only on the foundational axioms.
#print axioms Complex.digamma_apply_add_nat
#print axioms Complex.digamma_reflection
#print axioms Complex.digamma_two_mul
