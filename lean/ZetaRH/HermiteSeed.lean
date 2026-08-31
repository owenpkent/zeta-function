/-
The e2aw seed facts (E1 of e2aw_energy_gap.md): with alpha = 2*sqrt(6)/3 the
seed h = psi0 - alpha * psi4 has integral 0 and h(0) = 0 EXACTLY, and the two
conditions coincide because `integral psi_n = sqrt(2*pi) * psi_n(0)` for the
Fourier-self-dual Hermite functions of eigenvalue +1 (n = 0 mod 4).

CONVENTION, pinned and verified here: physicists' Hermite polynomials at
argument x with Gaussian weight exp(-x^2/2) and L2 normalization, i.e.
  psi_n(x) = (2^n n! sqrt(pi))^(-1/2) H_n(x) exp(-x^2/2),
  H_0 = 1, H_4(x) = 16 x^4 - 48 x^2 + 12,
so psi0 = pi^(-1/4) exp(-x^2/2) and
  psi4 = pi^(-1/4)/(8 sqrt 6) * (16 x^4 - 48 x^2 + 12) exp(-x^2/2)
(since (2^4 4! sqrt(pi))^(-1/2) = (384 sqrt pi)^(-1/2) = pi^(-1/4)/(8 sqrt 6)).
In THIS convention the dossier's alpha = 2*sqrt(6)/3 is exact:
psi0(0) = pi^(-1/4), psi4(0) = (sqrt 6/4) pi^(-1/4), and their ratio is
4/sqrt 6 = 2 sqrt 6/3. Verified formally below (#HS-3 with #HS-6 uniqueness).
The dossier's mechanism identity "integral psi_n = psi_n(0)" is stated there
in the unitary-Fourier normalization ((2 pi)^(-1/2) times Lebesgue); against
plain Lebesgue measure, as formalized here, the constant is sqrt(2*pi)
(#HS-4). Convention note, not a discrepancy.

No Fourier theory is consumed anywhere: the self-duality mechanism enters
only through the Gaussian moment identities, all discharged from Mathlib
(integral_gaussian, integral_rpow_mul_exp_neg_mul_rpow, Gamma at half
integers). NO carried analytic hypotheses in this module.

  #HS-0  The three Gaussian moments against exp(-x^2/2) on the full line:
         m0 = sqrt(2 pi), m2 = sqrt(2 pi), m4 = 3 sqrt(2 pi); plus their
         integrability. Even moments reduce to the half line by evenness
         (integral_comp_abs) and evaluate through Gamma(3/2), Gamma(5/2).

  #HS-1  (B1) The explicit seed data: psi0, psi4, alphaSeed, hermiteSeed.

  #HS-2  (B2) integral_hermiteSeed_zero : the seed has integral 0. Proved
         outright, via #HS-4 and #HS-3.

  #HS-3  (B3) hermiteSeed_apply_zero : hermiteSeed 0 = 0. Pure algebra in
         sqrt 6.

  #HS-4  (B4) The mechanism, exact for this pair: for EVERY mixing a,
         integral (psi0 - a psi4) = sqrt(2 pi) * (psi0(0) - a psi4(0)),
         hence vanishing integral IFF vanishing value at 0. This is the
         dossier's "the vanishing-integral condition IS h(0) = 0" made
         exact, with the explicit positive constant c = sqrt(2 pi).

  #HS-6  alphaSeed is the UNIQUE mixing with h(0) = 0 (so also the unique
         one with integral 0): the dossier's closed form checks out exactly.

Axiom footprint target: [propext, Classical.choice, Quot.sound].
-/

import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import Mathlib.MeasureTheory.Integral.Gamma
import Mathlib.MeasureTheory.Measure.Lebesgue.Integral

namespace ZetaRH.HermiteSeed

open MeasureTheory Set

/-! ## #HS-0: Gaussian moments against exp(-x^2/2), full line -/

/-- Bridge between the rpow exponent of the Mathlib moment lemmas and the
    monomial power. Unconditional (`Real.rpow_natCast` holds for all reals). -/
private theorem rpow_two_eq (t : ℝ) : t ^ (2 : ℝ) = t ^ (2 : ℕ) := by
  rw [show (2 : ℝ) = ((2 : ℕ) : ℝ) by norm_num, Real.rpow_natCast]

private theorem rpow_four_eq (t : ℝ) : t ^ (4 : ℝ) = t ^ (4 : ℕ) := by
  rw [show (4 : ℝ) = ((4 : ℕ) : ℝ) by norm_num, Real.rpow_natCast]

/-- `(1/2)^(-y) = 2^y`: the moment lemmas produce inverse powers of the
    Gaussian rate `b = 1/2`; this flips them to powers of 2. -/
private theorem rpow_half_neg_eq (y : ℝ) : (1 / 2 : ℝ) ^ (-y) = (2 : ℝ) ^ y := by
  rw [show (1 / 2 : ℝ) = 2⁻¹ by norm_num, Real.inv_rpow (by norm_num : (0 : ℝ) ≤ 2),
    Real.rpow_neg (by norm_num : (0 : ℝ) ≤ 2), inv_inv]

/-- Even fourth powers pass through the absolute value. -/
private theorem abs_pow_four (t : ℝ) : |t| ^ 4 = t ^ 4 := by
  rw [pow_abs, abs_of_nonneg (by positivity : (0 : ℝ) ≤ t ^ 4)]

/-- The integrand normal forms: Mathlib states Gaussians as `exp (-b * x^2)`,
    this module as `exp (-x^2/2)`. -/
private theorem gaussianFun_eq :
    (fun x : ℝ => Real.exp (-(1 / 2 : ℝ) * x ^ 2))
      = fun x : ℝ => Real.exp (-x ^ 2 / 2) := by
  funext x
  rw [show (-(1 / 2 : ℝ)) * x ^ 2 = -x ^ 2 / 2 by ring]

private theorem momentFun2_sq_eq :
    (fun x : ℝ => x ^ (2 : ℝ) * Real.exp (-(1 / 2 : ℝ) * x ^ 2))
      = fun x : ℝ => x ^ 2 * Real.exp (-x ^ 2 / 2) := by
  funext x
  rw [rpow_two_eq x, show (-(1 / 2 : ℝ)) * x ^ 2 = -x ^ 2 / 2 by ring]

private theorem momentFun2_rpow_eq :
    (fun x : ℝ => x ^ (2 : ℝ) * Real.exp (-(1 / 2 : ℝ) * x ^ (2 : ℝ)))
      = fun x : ℝ => x ^ 2 * Real.exp (-x ^ 2 / 2) := by
  funext x
  rw [rpow_two_eq x, show (-(1 / 2 : ℝ)) * x ^ 2 = -x ^ 2 / 2 by ring]

private theorem momentFun4_sq_eq :
    (fun x : ℝ => x ^ (4 : ℝ) * Real.exp (-(1 / 2 : ℝ) * x ^ 2))
      = fun x : ℝ => x ^ 4 * Real.exp (-x ^ 2 / 2) := by
  funext x
  rw [rpow_four_eq x, show (-(1 / 2 : ℝ)) * x ^ 2 = -x ^ 2 / 2 by ring]

private theorem momentFun4_rpow_eq :
    (fun x : ℝ => x ^ (4 : ℝ) * Real.exp (-(1 / 2 : ℝ) * x ^ (2 : ℝ)))
      = fun x : ℝ => x ^ 4 * Real.exp (-x ^ 2 / 2) := by
  funext x
  rw [rpow_four_eq x, rpow_two_eq x, show (-(1 / 2 : ℝ)) * x ^ 2 = -x ^ 2 / 2 by ring]

/-- **#HS-0 (m0).** `∫ exp(-x²/2) = √(2π)`. -/
theorem integral_moment_zero :
    ∫ x : ℝ, Real.exp (-x ^ 2 / 2) = Real.sqrt (2 * Real.pi) := by
  have h := integral_gaussian (1 / 2 : ℝ)
  rw [gaussianFun_eq, show Real.pi / (1 / 2 : ℝ) = 2 * Real.pi by ring] at h
  exact h

theorem integrable_moment_zero : Integrable fun x : ℝ => Real.exp (-x ^ 2 / 2) := by
  have h := integrable_exp_neg_mul_sq (by norm_num : (0 : ℝ) < 1 / 2)
  rwa [gaussianFun_eq] at h

theorem integrable_moment_two :
    Integrable fun x : ℝ => x ^ 2 * Real.exp (-x ^ 2 / 2) := by
  have h := integrable_rpow_mul_exp_neg_mul_sq (by norm_num : (0 : ℝ) < 1 / 2)
    (by norm_num : (-1 : ℝ) < 2)
  rwa [momentFun2_sq_eq] at h

theorem integrable_moment_four :
    Integrable fun x : ℝ => x ^ 4 * Real.exp (-x ^ 2 / 2) := by
  have h := integrable_rpow_mul_exp_neg_mul_sq (by norm_num : (0 : ℝ) < 1 / 2)
    (by norm_num : (-1 : ℝ) < 4)
  rwa [momentFun4_sq_eq] at h

/-- **#HS-0 (m2).** `∫ x² exp(-x²/2) = √(2π)`: evenness folds the line onto
    the half line, where the Gamma-integral lemma evaluates through Γ(3/2). -/
theorem integral_moment_two :
    ∫ x : ℝ, x ^ 2 * Real.exp (-x ^ 2 / 2) = Real.sqrt (2 * Real.pi) := by
  have h := integral_rpow_mul_exp_neg_mul_rpow (p := 2) (q := 2) (b := 1 / 2)
    (by norm_num) (by norm_num) (by norm_num)
  rw [momentFun2_rpow_eq] at h
  calc ∫ x : ℝ, x ^ 2 * Real.exp (-x ^ 2 / 2)
      = ∫ x : ℝ, ((fun t : ℝ => t ^ 2 * Real.exp (-t ^ 2 / 2)) |x|) := by
        congr 1
        funext x
        simp [sq_abs]
    _ = 2 * ∫ x in Ioi (0 : ℝ), x ^ 2 * Real.exp (-x ^ 2 / 2) :=
        integral_comp_abs (f := fun t : ℝ => t ^ 2 * Real.exp (-t ^ 2 / 2))
    _ = 2 * ((1 / 2 : ℝ) ^ (-((2 : ℝ) + 1) / 2) * (1 / 2)
          * Real.Gamma (((2 : ℝ) + 1) / 2)) := by rw [h]
    _ = Real.sqrt (2 * Real.pi) := by
        rw [show -((2 : ℝ) + 1) / 2 = -(3 / 2 : ℝ) by norm_num,
          show ((2 : ℝ) + 1) / 2 = 1 / 2 + 1 by norm_num,
          rpow_half_neg_eq, Real.Gamma_add_one (by norm_num : (1 / 2 : ℝ) ≠ 0),
          Real.Gamma_one_half_eq,
          show (3 / 2 : ℝ) = 1 + 1 / 2 by norm_num,
          Real.rpow_add (by norm_num : (0 : ℝ) < 2), Real.rpow_one,
          ← Real.sqrt_eq_rpow, Real.sqrt_mul (by norm_num : (0 : ℝ) ≤ 2)]
        ring

/-- **#HS-0 (m4).** `∫ x⁴ exp(-x²/2) = 3√(2π)`: same route through Γ(5/2). -/
theorem integral_moment_four :
    ∫ x : ℝ, x ^ 4 * Real.exp (-x ^ 2 / 2) = 3 * Real.sqrt (2 * Real.pi) := by
  have h := integral_rpow_mul_exp_neg_mul_rpow (p := 2) (q := 4) (b := 1 / 2)
    (by norm_num) (by norm_num) (by norm_num)
  rw [momentFun4_rpow_eq] at h
  calc ∫ x : ℝ, x ^ 4 * Real.exp (-x ^ 2 / 2)
      = ∫ x : ℝ, ((fun t : ℝ => t ^ 4 * Real.exp (-t ^ 2 / 2)) |x|) := by
        congr 1
        funext x
        simp [sq_abs, abs_pow_four]
    _ = 2 * ∫ x in Ioi (0 : ℝ), x ^ 4 * Real.exp (-x ^ 2 / 2) :=
        integral_comp_abs (f := fun t : ℝ => t ^ 4 * Real.exp (-t ^ 2 / 2))
    _ = 2 * ((1 / 2 : ℝ) ^ (-((4 : ℝ) + 1) / 2) * (1 / 2)
          * Real.Gamma (((4 : ℝ) + 1) / 2)) := by rw [h]
    _ = 3 * Real.sqrt (2 * Real.pi) := by
        rw [show -((4 : ℝ) + 1) / 2 = -(5 / 2 : ℝ) by norm_num,
          show ((4 : ℝ) + 1) / 2 = 3 / 2 + 1 by norm_num,
          rpow_half_neg_eq, Real.Gamma_add_one (by norm_num : (3 / 2 : ℝ) ≠ 0),
          show (3 / 2 : ℝ) = 1 / 2 + 1 by norm_num,
          Real.Gamma_add_one (by norm_num : (1 / 2 : ℝ) ≠ 0),
          Real.Gamma_one_half_eq,
          show (5 / 2 : ℝ) = 1 + (1 + 1 / 2) by norm_num,
          Real.rpow_add (by norm_num : (0 : ℝ) < 2),
          Real.rpow_add (by norm_num : (0 : ℝ) < 2), Real.rpow_one,
          ← Real.sqrt_eq_rpow, Real.sqrt_mul (by norm_num : (0 : ℝ) ≤ 2)]
        ring

/-! ## #HS-1: the seed data (B1) -/

/-- Hermite function `ψ0` in the pinned convention: `π^(-1/4) e^(-x²/2)`. -/
noncomputable def psi0 (x : ℝ) : ℝ :=
  Real.pi ^ (-(1 / 4 : ℝ)) * Real.exp (-x ^ 2 / 2)

/-- Hermite function `ψ4` in the pinned convention:
    `(2⁴·4!·√π)^(-1/2) H₄(x) e^(-x²/2)` with the physicists' polynomial
    `H₄(x) = 16x⁴ - 48x² + 12`; the normalization constant simplifies to
    `π^(-1/4)/(8√6)`. -/
noncomputable def psi4 (x : ℝ) : ℝ :=
  Real.pi ^ (-(1 / 4 : ℝ)) / (8 * Real.sqrt 6) *
    ((16 * x ^ 4 - 48 * x ^ 2 + 12) * Real.exp (-x ^ 2 / 2))

/-- The dossier's closed-form mixing `α = 2√6/3`. -/
noncomputable def alphaSeed : ℝ := 2 * Real.sqrt 6 / 3

/-- The e2aw seed `h = ψ0 - α ψ4`. -/
noncomputable def hermiteSeed (x : ℝ) : ℝ := psi0 x - alphaSeed * psi4 x

/-- `ψ4(0) = 12·π^(-1/4)/(8√6)`: the value the whole seed identity pivots on. -/
private theorem psi4_zero_eq :
    psi4 0 = Real.pi ^ (-(1 / 4 : ℝ)) / (8 * Real.sqrt 6) * 12 := by
  norm_num [psi4, Real.exp_zero]

/-- `ψ4` split into the three moment monomials; the Gaussian factor is shared
    so linearity of the integral applies termwise. -/
private theorem psi4_rep : psi4 = fun x : ℝ =>
    16 * (Real.pi ^ (-(1 / 4 : ℝ)) / (8 * Real.sqrt 6)) * (x ^ 4 * Real.exp (-x ^ 2 / 2))
      + ((-48) * (Real.pi ^ (-(1 / 4 : ℝ)) / (8 * Real.sqrt 6))
          * (x ^ 2 * Real.exp (-x ^ 2 / 2))
        + 12 * (Real.pi ^ (-(1 / 4 : ℝ)) / (8 * Real.sqrt 6)) * Real.exp (-x ^ 2 / 2)) := by
  funext x
  simp only [psi4]
  ring

theorem integrable_psi0 : Integrable psi0 := by
  unfold psi0
  exact integrable_moment_zero.const_mul _

theorem integrable_psi4 : Integrable psi4 := by
  rw [psi4_rep]
  exact (integrable_moment_four.const_mul _).add
    ((integrable_moment_two.const_mul _).add (integrable_moment_zero.const_mul _))

/-- `∫ ψ0 = √(2π)·ψ0(0)`: the eigenvalue-(+1) self-duality identity for `ψ0`,
    obtained here from the Gaussian integral alone. -/
theorem integral_psi0 : ∫ x : ℝ, psi0 x = Real.sqrt (2 * Real.pi) * psi0 0 := by
  have h0 : psi0 0 = Real.pi ^ (-(1 / 4 : ℝ)) := by
    norm_num [psi0, Real.exp_zero]
  calc ∫ x : ℝ, psi0 x
      = ∫ x : ℝ, Real.pi ^ (-(1 / 4 : ℝ)) * Real.exp (-x ^ 2 / 2) := rfl
    _ = Real.pi ^ (-(1 / 4 : ℝ)) * ∫ x : ℝ, Real.exp (-x ^ 2 / 2) :=
        integral_const_mul _ _
    _ = Real.sqrt (2 * Real.pi) * psi0 0 := by
        rw [integral_moment_zero, h0]
        ring

/-- Linearity contraction of the three moments, for arbitrary coefficients:
    isolated so the `Integrable` side conditions can be given the exact
    pointwise-lambda types the `rw` patterns need. -/
private theorem integral_three_moments (a b c : ℝ) :
    ∫ x : ℝ, (a * (x ^ 4 * Real.exp (-x ^ 2 / 2))
        + (b * (x ^ 2 * Real.exp (-x ^ 2 / 2)) + c * Real.exp (-x ^ 2 / 2)))
      = a * (3 * Real.sqrt (2 * Real.pi))
        + (b * Real.sqrt (2 * Real.pi) + c * Real.sqrt (2 * Real.pi)) := by
  have hA : Integrable (fun x : ℝ => a * (x ^ 4 * Real.exp (-x ^ 2 / 2))) :=
    integrable_moment_four.const_mul _
  have hB : Integrable (fun x : ℝ => b * (x ^ 2 * Real.exp (-x ^ 2 / 2))) :=
    integrable_moment_two.const_mul _
  have hC : Integrable (fun x : ℝ => c * Real.exp (-x ^ 2 / 2)) :=
    integrable_moment_zero.const_mul _
  have hBC : Integrable (fun x : ℝ => b * (x ^ 2 * Real.exp (-x ^ 2 / 2))
      + c * Real.exp (-x ^ 2 / 2)) := hB.add hC
  rw [integral_add hA hBC, integral_add hB hC, integral_const_mul, integral_const_mul,
    integral_const_mul, integral_moment_four, integral_moment_two, integral_moment_zero]

/-- `∫ ψ4 = √(2π)·ψ4(0)`: the same identity for `ψ4`. The Fourier
    self-duality mechanism appears numerically: the moment contraction
    `16·3 - 48·1 + 12·1 = 12` equals the constant term of `H₄`, i.e. the
    `48 - 48` cancellation IS the eigenvalue-(+1) structure. -/
theorem integral_psi4 : ∫ x : ℝ, psi4 x = Real.sqrt (2 * Real.pi) * psi4 0 := by
  rw [psi4_zero_eq]
  simp only [psi4_rep]
  rw [integral_three_moments]
  ring

/-! ## #HS-3: the value identity h(0) = 0 (B3) -/

/-- **#HS-3 (B3).** `hermiteSeed 0 = 0` EXACTLY: `ψ0(0) = α·ψ4(0)` at
    `α = 2√6/3`. Pure algebra in `√6` (only linear cancellation; no squaring
    of the radical is needed). This verifies the dossier's closed form in the
    pinned convention. -/
theorem hermiteSeed_apply_zero : hermiteSeed 0 = 0 := by
  have h6 : Real.sqrt 6 ≠ 0 := ne_of_gt (Real.sqrt_pos.mpr (by norm_num))
  simp only [hermiteSeed, alphaSeed]
  norm_num [psi0, psi4, Real.exp_zero]
  field_simp
  ring

/-! ## #HS-4: the mechanism, exact for this pair (B4) -/

/-- **#HS-4 (B4, the mechanism).** For EVERY mixing `a`,
    `∫ (ψ0 - a·ψ4) = √(2π) · (ψ0(0) - a·ψ4(0))`: on the span of `ψ0, ψ4` the
    integral functional and the evaluation-at-0 functional are proportional
    with the explicit positive constant `√(2π)`. This is the dossier's
    "the vanishing-integral condition IS h(0) = 0", made exact. -/
theorem integral_seed (a : ℝ) :
    ∫ x : ℝ, (psi0 x - a * psi4 x)
      = Real.sqrt (2 * Real.pi) * (psi0 0 - a * psi4 0) := by
  rw [integral_sub integrable_psi0 (integrable_psi4.const_mul a),
    integral_const_mul, integral_psi0, integral_psi4]
  ring

/-- **#HS-4 (iff form).** Vanishing integral iff vanishing value at 0. -/
theorem integral_seed_eq_zero_iff (a : ℝ) :
    (∫ x : ℝ, (psi0 x - a * psi4 x)) = 0 ↔ psi0 0 - a * psi4 0 = 0 := by
  have hne : Real.sqrt (2 * Real.pi) ≠ 0 :=
    ne_of_gt (Real.sqrt_pos.mpr (by positivity))
  rw [integral_seed a, mul_eq_zero, or_iff_right hne]

/-! ## #HS-2: the integral identity for the seed (B2) -/

/-- **#HS-2 (B2).** `∫ hermiteSeed = 0` EXACTLY, with no carried analytic
    hypotheses: the mechanism #HS-4 plus the value identity #HS-3. -/
theorem integral_hermiteSeed_zero : ∫ x : ℝ, hermiteSeed x = 0 := by
  have h0 : psi0 0 - alphaSeed * psi4 0 = 0 := hermiteSeed_apply_zero
  calc ∫ x : ℝ, hermiteSeed x
      = ∫ x : ℝ, (psi0 x - alphaSeed * psi4 x) := rfl
    _ = Real.sqrt (2 * Real.pi) * (psi0 0 - alphaSeed * psi4 0) := integral_seed alphaSeed
    _ = 0 := by rw [h0, mul_zero]

/-! ## #HS-6: uniqueness of the mixing -/

/-- **#HS-6.** `α = 2√6/3` is the UNIQUE mixing annihilating the value at 0
    (equivalently, by #HS-4, the integral): the dossier's closed form is not
    just sufficient but forced in the pinned convention. -/
theorem alphaSeed_unique (a : ℝ) (ha : psi0 0 - a * psi4 0 = 0) : a = alphaSeed := by
  have h4 : psi4 0 ≠ 0 := by
    have hpos : (0 : ℝ) < psi4 0 := by
      rw [psi4_zero_eq]
      positivity
    exact ne_of_gt hpos
  have h0 : psi0 0 - alphaSeed * psi4 0 = 0 := hermiteSeed_apply_zero
  have h1 : a * psi4 0 = alphaSeed * psi4 0 := by linarith
  exact mul_right_cancel₀ h4 h1

end ZetaRH.HermiteSeed
