/-
Lever B, O3 wiring: connect the function-field RH chain to Mathlib's elliptic-curve
local L-factor `WeierstrassCurve.localPolynomial`.

See `docs/03_research/lever_b_function_field_plan.md` (the "Discharging `hdeg`" section, obligation
O3). Mathlib already DEFINES the Frobenius trace and point count: for a Weierstrass curve `W` over a
nonarchimedean local field with good reduction,

  `W.localPolynomial = 1 - a·T + q·T²`,   `q = #(residue field)`,  `a = q + 1 - #W(κ)`

(`Mathlib/AlgebraicGeometry/EllipticCurve/LFunction.lean`, T. Browning). This file makes the input
of the eigenvalue chain Mathlib-native: it identifies that polynomial (good-reduction case) and
proves the "RH for the local factor" statement on it.

The local factor `1 - aT + qT²` factors as `(1-αT)(1-βT)` with `α, β` the Frobenius eigenvalues
(roots of `X² - aX + q`, `α+β = a`, `αβ = q`). So a root `γ` of `localPolynomial` is the RECIPROCAL
`1/α` of an eigenvalue, and RH for the curve (`|α| = √q`) is exactly `|γ| = q^{-1/2}`. We reuse the
eigenvalue extraction (`eigenvalue_modulus`, `root_nonreal` from `FunctionFieldRH.lean`) via `α = γ⁻¹`.

The Hasse bound `a² < 4q` is carried as a hypothesis (it is the open geometric input #FF-geom / the
`hdeg` residual; see the plan). Everything else is machine-checked.
-/

import ZetaRH.FunctionFieldRH
import Mathlib.AlgebraicGeometry.EllipticCurve.LFunction

namespace ZetaRH.LocalFactor

open Polynomial

/-- **RH for the local Euler factor (abstract form).** For real `a, q` with `q > 0` and the Hasse
    bound `a² < 4q`, every complex root `β` of the local factor `1 - a·β + q·β² = 0` has
    `|β|² = 1/q`, i.e. lies on the circle `|T| = q^{-1/2}`. Proof: `β ≠ 0`, and `α = β⁻¹` is a root
    of the characteristic polynomial `X² - aX + q`, so by the eigenvalue extraction `|α|² = q`,
    whence `|β|² = 1/q`. This is the `1 - aT + qT²` (L-factor) face of the chain in
    `FunctionFieldRH.lean`, matching Mathlib's `localPolynomial` shape exactly. -/
theorem localFactor_root_normSq {a q : ℝ} (hHasse : a ^ 2 < 4 * q)
    {β : ℂ} (hβ : 1 - (a : ℂ) * β + (q : ℂ) * β ^ 2 = 0) : Complex.normSq β = 1 / q := by
  have hβ0 : β ≠ 0 := by rintro rfl; simp at hβ
  have hroot : β⁻¹ ^ 2 - (a : ℂ) * β⁻¹ + (q : ℂ) = 0 := by
    field_simp
    linear_combination hβ
  have hnr : β⁻¹ ≠ (starRingEnd ℂ) β⁻¹ :=
    ZetaRH.FunctionFieldRH.root_nonreal a q β⁻¹ hroot hHasse
  have hns : Complex.normSq β⁻¹ = q :=
    ZetaRH.FunctionFieldRH.eigenvalue_modulus a q β⁻¹ hroot hnr
  rw [Complex.normSq_inv] at hns
  rw [← hns, one_div, inv_inv]

section LocalField

variable {R : Type*} [CommRing R] [IsDomain R] [IsDiscreteValuationRing R] {K : Type*}
  [Field K] [Algebra R K] [IsFractionRing R K] (W : WeierstrassCurve K)

/-- **The good-reduction local polynomial, unfolded.** In the good-reduction case Mathlib's
    `W.localPolynomial` is literally `1 - C a · X + C q · X²` with `q = #(residue field)` and
    `a = q + 1 - #W(κ)`. This exposes the trace/count as the coefficients the eigenvalue chain
    consumes (obligation O3 made Mathlib-native). -/
theorem localPolynomial_eq_of_goodReduction (hgood : (W.minimal R).HasGoodReduction R) :
    W.localPolynomial R
      = 1 - C ((Nat.card (IsLocalRing.ResidueField R) : ℤ) + 1
          - (Nat.card ((W.minimal R).reduction R).toAffine.Point : ℤ)) * X
        + C (Nat.card (IsLocalRing.ResidueField R) : ℤ) * X ^ 2 := by
  unfold WeierstrassCurve.localPolynomial
  rw [if_pos hgood]

/-- **RH for the local factor on Mathlib's `localPolynomial` (O3 wired).** Given good reduction and
    the Hasse bound `a² < 4q` on the Mathlib-native trace `a = q+1-#W(κ)` and `q = #κ`, every complex
    root of `W.localPolynomial` has `|·|² = 1/q`. The only open input is the Hasse bound (the `hdeg`
    residual); the trace and count are taken directly from Mathlib's definition. -/
theorem localPolynomial_root_normSq (hgood : (W.minimal R).HasGoodReduction R)
    (hHasse : (((Nat.card (IsLocalRing.ResidueField R) : ℤ) + 1
          - (Nat.card ((W.minimal R).reduction R).toAffine.Point : ℤ) : ℤ) : ℝ) ^ 2
        < 4 * ((Nat.card (IsLocalRing.ResidueField R) : ℤ) : ℝ))
    {β : ℂ} (hβ : aeval β (W.localPolynomial R) = 0) :
    Complex.normSq β = 1 / ((Nat.card (IsLocalRing.ResidueField R) : ℤ) : ℝ) := by
  rw [localPolynomial_eq_of_goodReduction W hgood] at hβ
  set q' : ℤ := (Nat.card (IsLocalRing.ResidueField R) : ℤ)
  set a' : ℤ := q' + 1 - (Nat.card ((W.minimal R).reduction R).toAffine.Point : ℤ)
  simp only [map_add, map_sub, map_mul, map_pow, map_one, aeval_X, map_intCast, eq_intCast] at hβ
  apply localFactor_root_normSq hHasse
  push_cast
  linear_combination hβ

end LocalField

end ZetaRH.LocalFactor
