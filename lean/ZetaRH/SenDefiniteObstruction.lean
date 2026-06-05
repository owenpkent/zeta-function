/-
Class A no-go: the definite-cup-form obstruction (Direction 8E ledger, Class A;
the Lean form of Direction 8D / LEARNINGS #72).

A nonzero nilpotent cannot be an infinitesimal isometry of a definite form. This
is the compact-group obstruction of
`docs/03_research/research_directions/08D_sen_nonsemisimplicity_obstruction.md`,
formalized by an ELEMENTARY trace argument (no spectral theorem):

  if `N` is skew (`Nᵀ = -N`) and nilpotent, then
  `trace(Nᴴ N) = -trace(N²) = 0`, hence `N = 0`.

Consequence for the Sen route: a non-semisimple Sen operator `Θ = Θ_ss + ν`
with `ν ≠ 0` (Petrov, arXiv:2302.11389) cannot admit a positive-definite
invariant cup form solving `Θᵀ B + B Θ = -w B`. This prunes the "polarize the
Sen module" sub-branch of M4. It is a CONDITIONAL no-go (K5-clean): it kills the
archimedean-Sen source only and relocates the polarization demand to the
Frobenius / F half, where it remains open. It does NOT disprove RH.

This file extends `ZetaRH.EulerSenLinearAlgebra`, which already supplies the
finite Jordan-block witness `theta_nilpotent_part_ne_zero` (`ν ≠ 0`).
-/

import ZetaRH.EulerSenLinearAlgebra
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.Charpoly.Coeff
import Mathlib.Data.Real.StarOrdered
import Mathlib.Analysis.Matrix.Order

namespace ZetaRH.SenDefiniteObstruction

open Matrix

open scoped MatrixOrder

variable {n : Type*} [Fintype n] [DecidableEq n]

/-! ### The elementary kernel: skew + nilpotent ⟹ zero -/

/-- A real skew-symmetric nilpotent matrix is zero.

In an orthonormal frame the definite cup form is the identity, and an
infinitesimal isometry of it is skew-symmetric (`Nᵀ = -N`). A nonzero nilpotent
skew matrix is impossible: over `ℝ` the star is trivial so `Nᴴ = Nᵀ = -N`, hence
`trace(Nᴴ N) = -trace(N²)`; `N²` is nilpotent so its trace is a nilpotent real,
i.e. `0`; and `trace(Nᴴ N) = 0` forces `N = 0`. -/
theorem skew_nilpotent_eq_zero {N : Matrix n n ℝ} (hskew : Nᵀ = -N)
    (hnil : IsNilpotent N) : N = 0 := by
  have hconj : Nᴴ = -N := by
    rw [conjTranspose_eq_transpose_of_trivial]; exact hskew
  rw [← trace_conjTranspose_mul_self_eq_zero_iff, hconj, neg_mul, trace_neg,
    neg_eq_zero]
  have h2 : IsNilpotent (N * N) := (Commute.refl N).isNilpotent_mul_right hnil
  exact (Matrix.isNilpotent_trace_of_isNilpotent h2).eq_zero

/-! ### The Sen corollary (standard frame)

The Tate-equivariant cup-duality equation for a definite form `B` is, after
shifting to the Tate center `M := Θ + (w/2)•1`, exactly `Mᵀ B + B M = 0`. In the
orthonormal frame of the definite form (`B = 1`) this reads `Mᵀ = -M`: the
Tate-centered Sen operator is skew. So if its nilpotent (Jordan) part is itself
nilpotent, the kernel lemma forces it to vanish, i.e. `Θ` is the pure scalar
`-(w/2)•1` (semisimple). A genuine nonzero nilpotent part (`ν ≠ 0`, the Petrov
case witnessed by `EulerSenLinearAlgebra.theta_nilpotent_part_ne_zero`) is
therefore incompatible with a definite invariant cup form. -/
theorem sen_no_nilpotent_part {Θ : Matrix n n ℝ} {w : ℝ}
    (hcup : Θᵀ + Θ = (-w) • (1 : Matrix n n ℝ))
    (hnil : IsNilpotent (Θ + (w / 2) • (1 : Matrix n n ℝ))) :
    Θ + (w / 2) • (1 : Matrix n n ℝ) = 0 := by
  refine skew_nilpotent_eq_zero ?_ hnil
  have hΘt : Θᵀ = (-w) • (1 : Matrix n n ℝ) - Θ := by rw [← hcup]; abel
  rw [transpose_add, transpose_smul, transpose_one, hΘt]
  match_scalars <;> ring

/-- Contrapositive: a nonzero Tate-centered nilpotent Sen part admits no definite
invariant cup form (in the standard frame). This is the Class A no-go: the
polarization cannot be sourced from a non-semisimple Sen module. -/
theorem sen_nilpotent_part_not_isNilpotent {Θ : Matrix n n ℝ} {w : ℝ}
    (hcup : Θᵀ + Θ = (-w) • (1 : Matrix n n ℝ))
    (hne : Θ + (w / 2) • (1 : Matrix n n ℝ) ≠ 0) :
    ¬ IsNilpotent (Θ + (w / 2) • (1 : Matrix n n ℝ)) :=
  fun hnil => hne (sen_no_nilpotent_part hcup hnil)

/-! ### The Gram-factor reduction

Every positive-definite real cup form factors as `B = Sᵀ S` with `S` invertible
(for instance the symmetric square root). The next theorem makes the congruence
argument fully formal: given any such factorization with `S` a unit, a
`B`-skew nilpotent `M` is conjugated by `S` to a standard skew nilpotent
`N = S M S⁻¹`, which `skew_nilpotent_eq_zero` forces to vanish, hence `M = 0`.
This removes the change-of-basis hand-wave from the remark below: the only input
beyond the elementary kernel is the existence of an invertible Gram factor. -/

/-- Gram-factor reduction of the Class A no-go. If a real `B` factors as
`B = Sᵀ S` with `S.det` a unit, then a `B`-skew nilpotent `M` (i.e.
`Mᵀ B + B M = 0` with `M` nilpotent) is zero. The proof conjugates by `S`: the
matrix `N = S M S⁻¹` is nilpotent and skew (`Nᵀ = -N`), so the elementary kernel
`skew_nilpotent_eq_zero` gives `N = 0`, whence `M = 0`. -/
theorem bskew_nilpotent_eq_zero_of_gram {B M S : Matrix n n ℝ}
    (hSdet : IsUnit S.det) (hBfac : B = Sᵀ * S)
    (hskew : Mᵀ * B + B * M = 0) (hnil : IsNilpotent M) : M = 0 := by
  have hSSi : S * S⁻¹ = 1 := Matrix.mul_nonsing_inv S hSdet
  have hSiS : S⁻¹ * S = 1 := Matrix.nonsing_inv_mul S hSdet
  set N : Matrix n n ℝ := S * M * S⁻¹ with hN
  -- Conjugation powers: N ^ k = S * M ^ k * S⁻¹.
  have hpow : ∀ k : ℕ, N ^ k = S * M ^ k * S⁻¹ := by
    intro k
    induction k with
    | zero => simp [hN, hSSi]
    | succ p ih =>
        rw [pow_succ, ih, hN, pow_succ]
        have key : (S * M ^ p * S⁻¹) * (S * M * S⁻¹)
            = S * M ^ p * (S⁻¹ * S) * M * S⁻¹ := by
          simp only [mul_assoc]
        rw [key, hSiS, mul_one]
        simp only [mul_assoc]
  -- N is nilpotent: the witness k for M gives N ^ k = S * 0 * S⁻¹ = 0.
  have hNnil : IsNilpotent N := by
    obtain ⟨k, hk⟩ := hnil
    exact ⟨k, by rw [hpow k, hk, mul_zero, zero_mul]⟩
  -- N is skew: Nᵀ = -N.
  have hskewN : Nᵀ = -N := by
    -- Rewrite the B-skew condition with B = Sᵀ S.
    have hskew' : Mᵀ * (Sᵀ * S) + (Sᵀ * S) * M = 0 := by rw [← hBfac]; exact hskew
    have hMSS : Mᵀ * (Sᵀ * S) = -((Sᵀ * S) * M) := eq_neg_of_add_eq_zero_left hskew'
    -- Right-multiply by S⁻¹ and cancel S * S⁻¹ = 1 on the left of the RHS.
    have hMS : Mᵀ * Sᵀ = -(Sᵀ * N) := by
      have hcong : (Mᵀ * (Sᵀ * S)) * S⁻¹ = (-((Sᵀ * S) * M)) * S⁻¹ :=
        congrArg (fun x => x * S⁻¹) hMSS
      have hL : (Mᵀ * (Sᵀ * S)) * S⁻¹ = Mᵀ * Sᵀ * (S * S⁻¹) := by
        simp only [mul_assoc]
      have hR : (-((Sᵀ * S) * M)) * S⁻¹ = -(Sᵀ * N) := by
        rw [hN]; simp only [neg_mul, mul_assoc]
      rw [hL, hR, hSSi, mul_one] at hcong
      exact hcong
    -- Transpose N and substitute.
    calc Nᵀ = (S * M * S⁻¹)ᵀ := by rw [hN]
      _ = S⁻¹ᵀ * (Mᵀ * Sᵀ) := by
            rw [transpose_mul, transpose_mul]
      _ = S⁻¹ᵀ * (-(Sᵀ * N)) := by rw [hMS]
      _ = -((S⁻¹ᵀ * Sᵀ) * N) := by rw [mul_neg]; simp only [mul_assoc]
      _ = -((S * S⁻¹)ᵀ * N) := by rw [← transpose_mul]
      _ = -N := by rw [hSSi, transpose_one, one_mul]
  -- Apply the kernel and pull M back.
  have hNz : N = 0 := skew_nilpotent_eq_zero hskewN hNnil
  have hMeq : M = S⁻¹ * N * S := by
    rw [hN]
    calc M = (S⁻¹ * S) * M * (S⁻¹ * S) := by rw [hSiS, one_mul, mul_one]
      _ = S⁻¹ * (S * M * S⁻¹) * S := by simp only [mul_assoc]
  rw [hMeq, hNz, mul_zero, zero_mul]

/-! ### The unconditional positive-definite no-go

Theorem 1 needs only an invertible Gram factor `S` with `B = Sᵀ S`. Any
positive-definite real `B` supplies one: its continuous-functional-calculus
square root `S = CFC.sqrt B` is positive semidefinite, hence Hermitian, and over
`ℝ` Hermitian means symmetric (`Sᵀ = S`); it satisfies `S * S = B`, so
`B = Sᵀ * S`; and `det B = det S * det S` is nonzero, so `S` is positive
definite and a unit. Feeding this into `bskew_nilpotent_eq_zero_of_gram` makes
the Class A no-go unconditional in `B.PosDef`. -/

/-- Unconditional Class A no-go in cup form. For a positive-definite real cup
form `B`, a `B`-skew nilpotent `M` is zero. The Gram factor is the
functional-calculus square root `S = CFC.sqrt B`, which is symmetric over `ℝ`,
squares to `B`, and is a unit; the result is then `bskew_nilpotent_eq_zero_of_gram`. -/
theorem bskew_nilpotent_eq_zero {B M : Matrix n n ℝ}
    (hB : B.PosDef) (hskew : Mᵀ * B + B * M = 0) (hnil : IsNilpotent M) : M = 0 := by
  set S : Matrix n n ℝ := CFC.sqrt B with hSdef
  have hBnn : (0 : Matrix n n ℝ) ≤ B := hB.posSemidef.nonneg
  -- S is positive semidefinite, hence Hermitian; over ℝ that means symmetric.
  have hSpsd : S.PosSemidef := (CFC.sqrt_nonneg B).posSemidef
  have hSherm : Sᴴ = S := hSpsd.1
  have hStrans : Sᵀ = S := by
    rw [← conjTranspose_eq_transpose_of_trivial S]; exact hSherm
  -- S squares to B.
  have hSS : S * S = B := CFC.sqrt_mul_sqrt_self B hBnn
  have hBfac : B = Sᵀ * S := by rw [hStrans, hSS]
  -- det B = det S * det S, and det B > 0, so det S is a unit.
  have hdetB : B.det = S.det * S.det := by rw [← hSS, det_mul]
  have hdetSne : S.det ≠ 0 := by
    intro h
    have : B.det = 0 := by rw [hdetB, h, mul_zero]
    exact (hB.det_pos).ne' this
  have hSpd : S.PosDef := hSpsd.posDef_iff_det_ne_zero.mpr hdetSne
  have hSdet : IsUnit S.det := (Matrix.isUnit_iff_isUnit_det S).mp hSpd.isUnit
  exact bskew_nilpotent_eq_zero_of_gram hSdet hBfac hskew hnil

/-! ### The general positive-definite cup form (remark)

The three results above carry the full geometric content of the Class A no-go,
because every positive-definite real form is congruent to the identity: in the
orthonormal frame of any positive-definite cup form `B = Sᵀ S` (with `S`
invertible, e.g. the symmetric square root), the `B`-skew condition
`Mᵀ B + B M = 0` becomes the standard skew condition `Nᵀ = -N` for the congruate
`N = S M S⁻¹`, which is also nilpotent whenever `M` is. So
`skew_nilpotent_eq_zero` gives `N = 0`, hence `M = 0`. The general statement
`(B.PosDef) → (Mᵀ B + B M = 0) → IsNilpotent M → M = 0` therefore adds no
mathematical content beyond a change of basis; it is recorded here as a remark
rather than re-proved, to keep this file free of the matrix square-root API.
The contrapositive is the no-go used by Direction 8E:

  a nonzero nilpotent (`ν ≠ 0`, Petrov) admits no positive-definite invariant
  cup form, so the RH polarization cannot be sourced from the Sen module; the
  demand relocates to the Frobenius / F half and stays open (K5-clean). -/

end ZetaRH.SenDefiniteObstruction
