/-
The Davenport-Heilbronn L-function and its known off-line zeros.

D-H is defined as the linear combination

  L_DH(s) = c * L(s, χ) + c̄ * L(s, χ̄)

where χ is a fixed non-real Dirichlet character mod 5 and c is chosen so that
the combination satisfies the functional equation of the SAME shape as ζ(s)
(real coefficients in the Dirichlet series, conductor 5, weight 0) WITHOUT
admitting an Euler product. The explicit normalisation:

  with χ(1)=1, χ(2)=i, χ(3)=-i, χ(4)=-1 (mod 5),
  c = (1 - i tan(θ)) / 2  with  tan(θ) = (√10 - √(10 - 2√5)) / (√5 - 1).

(See Titchmarsh 1986 §10.25 and Conrey-Ghosh 1988 for the explicit constant.)

The first off-line zero is approximately ρ ≈ 0.8085 + 85.6993 i, with the
functional-equation partner at 0.1915 + 85.6993 i.

D-H is the project's "wrong-approach detector": any Arch 1 / 3 / 4 method that
does not distinguish ζ from D-H is structurally wrong.

Status (Phase 1 substrate, 2026-05-25 onwards):

  - `chi_5` is the chosen non-real Dirichlet character mod 5, expressed via a
    `ZMod 5 → ℂ` function lifted to `ℕ → ℂ`.
  - `dhCoefficient` is the c-shaped linear-combination scalar (concrete real
    number; VERIFIER target #DH-c to verify against Conrey-Ghosh 1988).
  - `davenportHeilbronnTerm` is the Dirichlet-series coefficient sequence
    `n ↦ c · χ(n) + c̄ · χ̄(n)`, which is real-valued.
  - `davenportHeilbronnSeries` is the formal Dirichlet series; convergence on
    `Re s > 1` is VERIFIER target #DH-conv.
  - `davenport_heilbronn` is the `LFunction` wrapper.
  - `dh_first_offline_zero` is the numerical zero (constants pulled from
    `experiments/_shared/davenport_heilbronn.py`).
  - `dh_RH_false` is the structural negation of RH for D-H; the proof needs
    `dh_first_offline_zero ∈ nonTrivialZeros davenport_heilbronn`, which is
    VERIFIER target #DH-zero (currently `sorry`, but the proof skeleton is in
    place).
-/

import ZetaRH.Basic
import Mathlib.NumberTheory.DirichletCharacter.Basic
import Mathlib.NumberTheory.LSeries.Dirichlet
import Mathlib.Data.Complex.Exponential
import Mathlib.Data.ZMod.Basic

namespace ZetaRH

open Complex Real

/-! ### The Dirichlet character χ mod 5.

    `χ(0) = 0, χ(1) = 1, χ(2) = i, χ(3) = -i, χ(4) = -1`. This is one of the
    two non-real characters mod 5; the other is its conjugate `χ̄`. -/

/-- The defining values of χ on `ZMod 5`. -/
def chi5Fun : ZMod 5 → ℂ
  | 0 => 0
  | 1 => 1
  | 2 => I
  | 3 => -I
  | 4 => -1

/-- χ as a `ℕ → ℂ` function, lifted through `ZMod 5`. -/
noncomputable def chi5 : ℕ → ℂ := fun n => chi5Fun (n : ZMod 5)

/-- The conjugate character χ̄. -/
noncomputable def chi5Bar : ℕ → ℂ := fun n => star (chi5 n)

/-! ### The D-H linear-combination scalar c.

    Conrey-Ghosh 1988 give `c = (1 - i tan(θ)) / 2` with
    `tan(θ) = (√10 - √(10 - 2√5)) / (√5 - 1)`. The key property of c is that
    `c · χ(n) + c̄ · χ̄(n) ∈ ℝ` for all n (automatic) and the combined
    Dirichlet series satisfies the functional equation of the same shape as
    ζ at conductor 5. -/

/-- The Conrey-Ghosh constant `tan(θ)` for D-H. -/
noncomputable def dhTanTheta : ℝ :=
  (Real.sqrt 10 - Real.sqrt (10 - 2 * Real.sqrt 5)) / (Real.sqrt 5 - 1)

/-- The D-H linear-combination scalar `c = (1 - i tan(θ)) / 2`. -/
noncomputable def dhCoefficient : ℂ :=
  (1 - I * (dhTanTheta : ℂ)) / 2

/-- The Dirichlet-series coefficient sequence of D-H:
    `a_n = c · χ(n) + c̄ · χ̄(n)`. This sequence is real-valued (the
    imaginary parts cancel by construction). -/
noncomputable def davenportHeilbronnTerm (n : ℕ) : ℂ :=
  dhCoefficient * chi5 n + star dhCoefficient * chi5Bar n

/-- The D-H Dirichlet series, as the partial sum function `s ↦ ∑' n, a_n / n^s`.

    Convergence on `Re s > 1` is VERIFIER target #DH-conv. The continuation
    to the rest of `ℂ` is constructed from the Hurwitz zeta function via the
    standard decomposition `L(s, χ) = q^{-s} ∑_{r=1}^{q-1} χ(r) ζ(s, r/q)`. -/
noncomputable def davenportHeilbronnSeries : ℂ → ℂ :=
  fun s => ∑' n : ℕ, davenportHeilbronnTerm n / (n : ℂ) ^ s

/-- The Davenport-Heilbronn L-function. -/
noncomputable def davenport_heilbronn : LFunction where
  evaluate := davenportHeilbronnSeries
  conductor := 5
  poles := ∅  -- D-H is entire (no pole at s = 1, unlike ζ).
  functional_equation := trivial
  has_euler_product := False

/-- The Riemann zeta function packaged as an `LFunction`.

    Alias for `ZetaRH.zeta` (from `Basic.lean`) for compatibility with prior
    callers. -/
noncomputable def zeta_function : LFunction := zeta

/-- The first off-line D-H zero (height ≈ 85.7).

    Numerical constants pulled from `experiments/_shared/davenport_heilbronn.py`.
    To 4 decimal places: ρ ≈ 0.8085 + 85.6993 i. The decimal expansion is
    intentionally low-precision here; high-precision verification lives in the
    Python control. -/
noncomputable def dh_first_offline_zero : ℂ :=
  ⟨0.8085, 85.6993⟩

/-- Functional-equation partner of `dh_first_offline_zero`: ρ ↦ 1 - ρ̄. -/
noncomputable def dh_first_offline_zero_partner : ℂ :=
  1 - star dh_first_offline_zero

/-- D-H has at least one zero with `Re ≠ 1/2`, hence RH for D-H is FALSE.

    Proof skeleton: `dh_first_offline_zero` is in `nonTrivialZeros
    davenport_heilbronn` (VERIFIER target #DH-zero) and has `Re ≈ 0.8085 ≠
    1/2`. -/
theorem dh_RH_false : ¬ RiemannHypothesis davenport_heilbronn := by
  intro hRH
  -- The first off-line zero has Re = 0.8085 ≠ 1/2.
  have hmem : dh_first_offline_zero ∈ nonTrivialZeros davenport_heilbronn := by
    refine ⟨?_, ?_, ?_, ?_⟩
    · -- evaluate dh_first_offline_zero = 0 (VERIFIER target #DH-zero).
      sorry
    · -- 0 < Re ≈ 0.8085.
      show (0 : ℝ) < 0.8085
      norm_num
    · -- Re ≈ 0.8085 < 1.
      show (0.8085 : ℝ) < 1
      norm_num
    · -- D-H has no poles.
      simp [davenport_heilbronn]
  have hre : dh_first_offline_zero.re = 1 / 2 := hRH _ hmem
  -- But Re = 0.8085 ≠ 1/2.
  have : (0.8085 : ℝ) = 1 / 2 := hre
  norm_num at this

/-! ### Hurwitz-zeta decomposition (sketch).

    The continuation of `davenportHeilbronnSeries` to `ℂ \ {1}` (and in fact
    to all of `ℂ`, since the pole at s = 1 cancels in the combination) goes
    via the standard formula

      L(s, χ) = q^{-s} * ∑_{r=1}^{q-1} χ(r) * ζ(s, r/q)

    where `ζ(s, a)` is the Hurwitz zeta function. Mathlib has the Hurwitz
    zeta function under `Mathlib.NumberTheory.LSeries.HurwitzZeta`; building
    out the decomposition lemma is VERIFIER target #DH-cont. -/

end ZetaRH
