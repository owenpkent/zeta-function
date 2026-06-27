/-
VT-NP1: finite Euler-product zero-freeness + the M4-reduction (NP-1, LEARNINGS #128 / e2vv).

The probe NP-1 asked whether the finite-prime Euler data carries any zero into the critical
strip that detects the off-line obstruction. The answer is NO, and the clean half is a
theorem: every FINITE Euler product is zero-free on Re(s) > 0, because each local factor
`1 - p^{-s}` is nonzero there (|p^{-s}| = p^{-Re s} < 1 for p ≥ 2). The off-line obstruction
can therefore only appear in the INFINITE-product limit, which is exactly the M4 coupling
(#104) -- the local-to-global step (#42/#25) that no finite truncation reaches.

This is the analytic-side companion of `HodgeIndex.IntersectionSignature.negDef_iff_hasseWeil`
(the per-local-factor Weil positivity over F_q): the local factors are individually harmless;
the entire RH content is in their global assembly. The finite-truncation zero-freeness proved
here is the sorry-free skeleton of the proposed VERIFIER target VT-NP1.

What is NOT done (and is exactly M4): the passage to the infinite product and the appearance
of the strip obstruction in the limit. That is the arithmetic Hodge standard conjecture; this
file proves only that no finite stage of the product can exhibit it.
-/

import ZetaRH.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Complex
import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace ZetaRH.VTNP1

open Complex

/-- The local Euler factor at `p`, as a function of `s`: `1 - p^{-s}`. The reciprocal of the
    local factor `(1 - p^{-s})⁻¹` of the Euler product; this is the `1/ζ`-side ("inverse zeta")
    local factor, whose vanishing would be a zero of the truncated product. -/
noncomputable def localFactor (p : ℕ) (s : ℂ) : ℂ := 1 - (p : ℂ) ^ (-s)

/-- **The local factor is nonzero on Re(s) > 0.** For a prime base `p ≥ 2`, `1 - p^{-s} ≠ 0`
    whenever `Re(s) > 0`, because `|p^{-s}| = p^{-Re s} < 1`, so `p^{-s} ≠ 1`. This is the
    per-prime core of VT-NP1: every local factor is harmless in the strip. -/
theorem localFactor_ne_zero {p : ℕ} (hp : 2 ≤ p) {s : ℂ} (hs : 0 < s.re) :
    localFactor p s ≠ 0 := by
  intro h
  -- `1 - p^{-s} = 0` forces `p^{-s} = 1`, hence `‖p^{-s}‖ = 1`.
  have hval : (p : ℂ) ^ (-s) = 1 := (sub_eq_zero.mp h).symm
  have hnorm1 : ‖(p : ℂ) ^ (-s)‖ = 1 := by rw [hval, norm_one]
  -- But `‖p^{-s}‖ = (p : ℝ) ^ (-(s.re)) < 1`.
  have hp0 : (0 : ℝ) < (p : ℝ) := by exact_mod_cast Nat.lt_of_lt_of_le Nat.zero_lt_two hp
  have hp1 : (1 : ℝ) < (p : ℝ) := by exact_mod_cast Nat.lt_of_lt_of_le Nat.one_lt_two hp
  have hcast : ((p : ℝ) : ℂ) = (p : ℂ) := by push_cast; ring
  have hnorm : ‖(p : ℂ) ^ (-s)‖ = (p : ℝ) ^ (-s).re := by
    rw [← hcast, Complex.norm_cpow_eq_rpow_re_of_pos hp0]
  have hlt : (p : ℝ) ^ (-s).re < 1 :=
    Real.rpow_lt_one_of_one_lt_of_neg hp1 (by simp only [Complex.neg_re]; linarith)
  rw [hnorm] at hnorm1
  linarith [hnorm1, hlt]

/-- The truncated inverse-zeta product over a finite set `S` of primes:
    `∏_{p ∈ S} (1 - p^{-s})`. (Its reciprocal is the truncated Euler product `ζ_S(s)`.) -/
noncomputable def finiteEulerProductInv (S : Finset ℕ) (s : ℂ) : ℂ :=
  ∏ p ∈ S, localFactor p s

/-- **Finite Euler-product zero-freeness (VT-NP1 skeleton).** For a finite set `S` of primes
    (each `≥ 2`), the truncated product `∏_{p ∈ S} (1 - p^{-s})` has NO zeros on `Re(s) > 0`.
    A finite product of nonzero factors is nonzero. So no finite truncation of the Euler
    product reaches the critical strip with a zero. -/
theorem finiteEulerProductInv_ne_zero {S : Finset ℕ} (hS : ∀ p ∈ S, 2 ≤ p)
    {s : ℂ} (hs : 0 < s.re) : finiteEulerProductInv S s ≠ 0 := by
  rw [finiteEulerProductInv, Finset.prod_ne_zero_iff]
  intro p hp
  exact localFactor_ne_zero (hS p hp) hs

/-- **The M4-reduction (NP-1 = NO), stated as a corollary.** The truncated inverse-zeta
    product is zero-free on `Re(s) > 0` for EVERY finite set of primes. Hence any zero in the
    strip (any off-line obstruction) is a property of the infinite-product limit alone, i.e.
    of the local-to-global assembly = M4 (#104, #42/#25). No finite-prime certificate can see
    it. This is the sense in which NP-1 "reduces precisely to M4": the firewall is exact at
    every finite stage, and what remains is exactly the limit M4 governs. -/
theorem np1_reduction (s : ℂ) (hs : 0 < s.re) :
    ∀ S : Finset ℕ, (∀ p ∈ S, 2 ≤ p) → finiteEulerProductInv S s ≠ 0 :=
  fun _S hS => finiteEulerProductInv_ne_zero hS hs

end ZetaRH.VTNP1
