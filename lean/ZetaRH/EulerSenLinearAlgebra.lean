/-
Finite Euler-Sen linear algebra.

This module formalizes the pure matrix core of experiment 2LL:

  B      symmetric/Euler-Rosati input form on P,
  Ω      = [[0, B], [-B, 0]] on P ⊕ NP,
  N      = [[0, 0], [I, 0]],
  Θ      = -1/2 I + N = [[-1/2 I, 0], [I, -1/2 I]].

The point is not to prove RH. The point is to isolate the reusable linear
algebra that makes the Euler-Sen proposal different from 2KK's diagonal-star
hyperbolic form: the primitive monodromy form is the top-left block of ΩN,
and it is exactly B.
-/

import ZetaRH.HodgeIndex
import Mathlib.Data.Matrix.Block

namespace ZetaRH.EulerSenLinearAlgebra

open Matrix

noncomputable section

/-! ### The finite Euler-Sen package on `P ⊕ NP` -/

/-- The alternating cup form `Ω = [[0, B], [-B, 0]]` on `P ⊕ NP`. -/
def omega {ι α : Type} [Neg α] [Zero α] (B : Matrix ι ι α) : Matrix (ι ⊕ ι) (ι ⊕ ι) α :=
  Matrix.fromBlocks 0 B (-B) 0

/-- The nilpotent monodromy `N(top_i)=lower_i`, `N(lower_i)=0`. -/
def monodromy (ι : Type) [DecidableEq ι] [Zero α] [One α] : Matrix (ι ⊕ ι) (ι ⊕ ι) α :=
  Matrix.fromBlocks 0 0 1 0

/-- The Tate-centered Sen operator `Θ = -1/2 I + N`. -/
def theta (ι : Type) [DecidableEq ι] : Matrix (ι ⊕ ι) (ι ⊕ ι) ℝ :=
  Matrix.fromBlocks (-(1 / 2 : ℝ) • (1 : Matrix ι ι ℝ)) 0 1
    (-(1 / 2 : ℝ) • (1 : Matrix ι ι ℝ))

/-- The primitive monodromy form on the top piece: the top-left block of `ΩN`. -/
def primitiveForm {ι : Type} [Fintype ι] [DecidableEq ι] (B : Matrix ι ι ℝ) : Matrix ι ι ℝ :=
  ((omega B) * (monodromy ι : Matrix (ι ⊕ ι) (ι ⊕ ι) ℝ)).toBlocks₁₁

/-! ### Core identities -/

/-- `N^2 = 0`. -/
theorem monodromy_sq_zero (ι : Type) [Fintype ι] [DecidableEq ι] :
    (monodromy ι : Matrix (ι ⊕ ι) (ι ⊕ ι) ℝ) *
        (monodromy ι : Matrix (ι ⊕ ι) (ι ⊕ ι) ℝ) = 0 := by
  rw [monodromy, Matrix.fromBlocks_multiply]
  simp

/-- The Tate-centered operator differs from scalar `-1/2` by the nilpotent `N`. -/
theorem theta_sub_scalar (ι : Type) [DecidableEq ι] :
    theta ι - (-(1 / 2 : ℝ)) • (1 : Matrix (ι ⊕ ι) (ι ⊕ ι) ℝ)
      = (monodromy ι : Matrix (ι ⊕ ι) (ι ⊕ ι) ℝ) := by
  ext i j
  cases i <;> cases j <;> simp [theta, monodromy, Matrix.fromBlocks, Matrix.one_apply]

/-- The nilpotent part of `Theta` is nonzero as soon as the primitive space has a point.
    This is the finite Jordan-block witness used by 2LL. -/
theorem monodromy_ne_zero [DecidableEq ι] [Nonempty ι] :
    (monodromy ι : Matrix (ι ⊕ ι) (ι ⊕ ι) ℝ) ≠ 0 := by
  classical
  rcases ‹Nonempty ι› with ⟨i⟩
  intro h
  have hentry := congr_fun (congr_fun h (Sum.inr i)) (Sum.inl i)
  simp [monodromy, Matrix.fromBlocks] at hentry

/-- The nilpotent part of `Theta` squares to zero. -/
theorem theta_nilpotent_part_sq_zero (ι : Type) [Fintype ι] [DecidableEq ι] :
    (theta ι - (-(1 / 2 : ℝ)) • (1 : Matrix (ι ⊕ ι) (ι ⊕ ι) ℝ)) *
        (theta ι - (-(1 / 2 : ℝ)) • (1 : Matrix (ι ⊕ ι) (ι ⊕ ι) ℝ)) = 0 := by
  rw [theta_sub_scalar, monodromy_sq_zero]

/-- If `P` is nonempty, the Tate-centered operator has a nonzero nilpotent
    part. Together with `theta_nilpotent_part_sq_zero`, this is the finite
    Jordan-block witness. -/
theorem theta_nilpotent_part_ne_zero [DecidableEq ι] [Nonempty ι] :
    theta ι - (-(1 / 2 : ℝ)) • (1 : Matrix (ι ⊕ ι) (ι ⊕ ι) ℝ) ≠ 0 := by
  rw [theta_sub_scalar]
  exact monodromy_ne_zero

/-- The cup/derivation equation: `Theta^T Ω + Ω Theta = -Ω`.

This is the exact Tate-weight `-1` equation from the finite Euler-Sen model. -/
theorem theta_cup_derivation {ι : Type} [Fintype ι] [DecidableEq ι] (B : Matrix ι ι ℝ) :
    (theta ι)ᵀ * omega B + omega B * theta ι = -omega B := by
  rw [theta, omega, Matrix.fromBlocks_transpose, Matrix.fromBlocks_multiply,
    Matrix.fromBlocks_multiply, Matrix.fromBlocks_add, Matrix.fromBlocks_neg]
  apply Matrix.fromBlocks_inj.mpr
  constructor
  · simp
  · constructor
    · ext i j
      simp
      ring
    · constructor
      · ext i j
        simp
        ring
      · simp

/-- The primitive monodromy form is exactly the input Euler/Rosati matrix `B`. -/
theorem primitiveForm_eq {ι : Type} [Fintype ι] [DecidableEq ι] (B : Matrix ι ι ℝ) :
    primitiveForm B = B := by
  rw [primitiveForm, omega, monodromy, Matrix.fromBlocks_multiply,
    Matrix.toBlocks_fromBlocks₁₁]
  simp

/-! ### The function-field 2x2 specialization -/

namespace FunctionField

/-- The positive Rosati matrix `B_E = -G_prim` from the 2G function-field model. -/
def BE (g q t : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![2 * g, t; t, 2 * g * q]

/-- `B_E` is `-G_prim`, the sign flip from primitive intersection to Rosati form. -/
theorem BE_eq_neg_Gprim (g q t : ℝ) :
    BE g q t = -ZetaRH.HodgeIndex.IntersectionSignature.Gprim g q t := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [BE, ZetaRH.HodgeIndex.IntersectionSignature.Gprim]

/-- The quadratic form associated to `B_E`. -/
def BEQ (g q t x y : ℝ) : ℝ :=
  2 * g * x ^ 2 + 2 * t * x * y + 2 * g * q * y ^ 2

/-- Elementwise positive-definiteness of the 2x2 Rosati form. -/
def RosatiPos (g q t : ℝ) : Prop :=
  ∀ x y : ℝ, (x, y) ≠ (0, 0) -> 0 < BEQ g q t x y

/-- `B_E` positivity is the sign-flipped version of the existing primitive
    negative-definiteness theorem. -/
theorem rosatiPos_iff_negDef (g q t : ℝ) :
    RosatiPos g q t ↔ ZetaRH.HodgeIndex.IntersectionSignature.NegDef g q t := by
  constructor
  · intro h x y hxy
    have hpos := h x y hxy
    dsimp [BEQ, ZetaRH.HodgeIndex.IntersectionSignature.Qform] at hpos ⊢
    linarith
  · intro h x y hxy
    have hneg := h x y hxy
    dsimp [BEQ, ZetaRH.HodgeIndex.IntersectionSignature.Qform] at hneg ⊢
    linarith

/-- Function-field specialization: Euler-Sen primitive positivity recovers the
    Hasse-Weil/Rosati bound, using the already-proved 2G theorem. -/
theorem rosatiPos_iff_hasseWeil {g q t : ℝ} (hg : 0 < g) :
    RosatiPos g q t ↔ t ^ 2 < 4 * g ^ 2 * q := by
  rw [rosatiPos_iff_negDef, ZetaRH.HodgeIndex.IntersectionSignature.negDef_iff_hasseWeil hg]

/-- The primitive monodromy matrix of the Euler-Sen package is the function-field
    Rosati matrix `B_E`. -/
theorem primitiveForm_BE (g q t : ℝ) :
    primitiveForm (BE g q t) = BE g q t :=
  primitiveForm_eq _

end FunctionField

end

end ZetaRH.EulerSenLinearAlgebra
