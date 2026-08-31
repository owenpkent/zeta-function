/-
STAGING DRAFT -- DO NOT SUBMIT AS WRITTEN. See `arcosh_pr_body.md` in this directory: a
build-verified check against the pinned Mathlib checkout (`lean/.lake/packages/mathlib`,
commit `c5ea00351c`, tag `v4.30.0`) found that `Real.arcosh` already exists in Mathlib
(`Mathlib/Analysis/SpecialFunctions/Arcosh.lean`, authored by Yuval Filmus, merged
2026-03-23, i.e. before this project's own v4.30.0 pin). The gap this file was drafted
to fill is closed upstream already. This file is kept as a staged record of the
independent derivation (every declaration below elaborates and type-checks against the
pinned toolchain, `lake env lean` on this file, confirmed this session) and is
deliberately NOT imported by `ZetaRH.lean` and NOT wired into the `lake build` target.

Namespace note: this file declares `namespace Real` / `def arcosh` to mirror the naming
a from-scratch PR draft would use (matching `Real.arsinh`'s sibling placement, as
requested). Because Mathlib's own `Real.arcosh` already occupies that name, this file
would NOT build if it were ever added to a project that imports Mathlib's
`Analysis.SpecialFunctions.Arcosh` -- another reason it stays unwired.

Source of the ported core: `arcoshReal` / `cosh_arcoshReal` in
`../ZetaRH/VerifierQueue.lean` (lines 139-151 at the time of this port), themselves
proved sorry-free and used by `bandGreen` / `v2_germ_bound` (#VQ-2, LEARNINGS #172/#202).
The extra lemmas below (the set a Mathlib reviewer would expect by analogy with
`Real.arsinh`) were derived fresh this session and build-checked; see the PR body for
which are proved vs. TODO-staged.
-/

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp

/-!
# Inverse of the cosh function

Draft port of an inverse for `Real.cosh`, as a function from `[1, ∞)` (real behavior;
junk values elsewhere from the underlying `log`/`sqrt`). Modeled on
`Mathlib.Analysis.SpecialFunctions.Arsinh`.

## Main definitions

- `Real.arcosh`: `arcosh x = log (x + sqrt (x ^ 2 - 1))`, the standard closed form.

## Main results (this draft)

- `Real.cosh_arcosh`: `1 ≤ x → cosh (arcosh x) = x` (the ported core; ORIGINAL SOURCE:
  `cosh_arcoshReal` in `VerifierQueue.lean`).
- `Real.arcosh_cosh`: `0 ≤ x → arcosh (cosh x) = x`.
- `Real.arcosh_one`, `Real.arcosh_nonneg`, `Real.arcosh_pos`.
- `Real.strictMonoOn_arcosh`, `Real.arcosh_le_arcosh`, `Real.arcosh_lt_arcosh`.
- `Real.continuousOn_arcosh`.
- `Real.hasDerivAt_arcosh`, `Real.differentiableAt_arcosh`, `Real.differentiableOn_arcosh`.

All of the above are PROVED sorry-free in this draft (see the PR body for the
elaboration log). Two further items a full Mathlib port would carry -- `ContDiffOn` /
analyticity, and the `PartialEquiv` / `OpenPartialHomeomorph` bundling that Mathlib's own
`Real.arsinh` file provides -- are stated only as TODO comments below (not as `sorry`d
declarations): they need more than a short adaptation of what is here.

## Tags

arcosh, arccosh, argcosh, acosh
-/

noncomputable section

namespace Real

variable {x y : ℝ}

/-- `arcosh` is defined using a logarithm: `arcosh x = log (x + sqrt (x ^ 2 - 1))`.
    (Draft name; collides with Mathlib's own `Real.arcosh` -- see the file header.) -/
def arcosh (x : ℝ) : ℝ :=
  Real.log (x + Real.sqrt (x ^ 2 - 1))

/-- **The defining property of `arcosh` (PROVED).** For `1 ≤ x`, `cosh (arcosh x) = x`.
    This is the repo's own already-proved `cosh_arcoshReal`
    (`ZetaRH/VerifierQueue.lean`), renamed to the Mathlib-facing name and otherwise
    verbatim: the ported core of this PR. -/
theorem cosh_arcosh {x : ℝ} (hx : 1 ≤ x) : Real.cosh (arcosh x) = x := by
  have hsq : Real.sqrt (x ^ 2 - 1) ^ 2 = x ^ 2 - 1 := Real.sq_sqrt (by nlinarith)
  have hy : 0 < x + Real.sqrt (x ^ 2 - 1) :=
    lt_of_lt_of_le zero_lt_one (le_add_of_le_of_nonneg hx (Real.sqrt_nonneg _))
  have hinv : (x + Real.sqrt (x ^ 2 - 1))⁻¹ = x - Real.sqrt (x ^ 2 - 1) := by
    refine inv_eq_of_mul_eq_one_right ?_
    nlinarith [hsq]
  rw [arcosh, Real.cosh_eq, Real.exp_log hy, Real.exp_neg, Real.exp_log hy, hinv]
  ring

/-- **`arcosh 1 = 0` (PROVED).** The base case: `arcosh` of `cosh`'s minimum. -/
theorem arcosh_one : arcosh 1 = 0 := by
  simp [arcosh]

/-- **Nonnegativity (PROVED).** For `1 ≤ x`, `0 ≤ arcosh x`. -/
theorem arcosh_nonneg {x : ℝ} (hx : 1 ≤ x) : 0 ≤ arcosh x := by
  apply Real.log_nonneg
  have h0 : (0 : ℝ) ≤ Real.sqrt (x ^ 2 - 1) := Real.sqrt_nonneg _
  linarith

/-- **Strict positivity (PROVED).** For `1 < x`, `0 < arcosh x`. -/
theorem arcosh_pos {x : ℝ} (hx : 1 < x) : 0 < arcosh x := by
  apply Real.log_pos
  have h0 : (0 : ℝ) ≤ Real.sqrt (x ^ 2 - 1) := Real.sqrt_nonneg _
  linarith

/-- **The left-inverse property (PROVED).** For `0 ≤ x`, `arcosh (cosh x) = x`. Route:
    `cosh x ^ 2 - 1 = sinh x ^ 2` and `sinh x ≥ 0` give
    `sqrt (cosh x ^ 2 - 1) = sinh x`, so `cosh x + sqrt (cosh x ^ 2 - 1) = cosh x + sinh x
    = exp x` by the defining sum/difference-of-exponentials forms, and `log (exp x) = x`. -/
theorem arcosh_cosh {x : ℝ} (hx : 0 ≤ x) : arcosh (Real.cosh x) = x := by
  have hsinh_nonneg : 0 ≤ Real.sinh x := Real.sinh_nonneg_iff.mpr hx
  have hsq : Real.cosh x ^ 2 - 1 = Real.sinh x ^ 2 := by
    nlinarith [Real.cosh_sq x, Real.sinh_sq x]
  have hsqrt : Real.sqrt (Real.cosh x ^ 2 - 1) = Real.sinh x := by
    rw [hsq, Real.sqrt_sq hsinh_nonneg]
  rw [arcosh, hsqrt, Real.cosh_eq, Real.sinh_eq]
  have hsum : (Real.exp x + Real.exp (-x)) / 2 + (Real.exp x - Real.exp (-x)) / 2
      = Real.exp x := by ring
  rw [hsum, Real.log_exp]

/-- **Monotonicity (PROVED).** `arcosh` is strictly monotone on `[1, ∞)`. -/
theorem strictMonoOn_arcosh : StrictMonoOn arcosh (Set.Ici (1 : ℝ)) := by
  intro x hx y hy hxy
  simp only [Set.mem_Ici] at hx hy
  apply Real.log_lt_log
  · have h0 : (0 : ℝ) ≤ Real.sqrt (x ^ 2 - 1) := Real.sqrt_nonneg _
    linarith
  · have h2 : Real.sqrt (x ^ 2 - 1) ≤ Real.sqrt (y ^ 2 - 1) := by
      apply Real.sqrt_le_sqrt; nlinarith
    linarith

/-- **Comparison, weak form (PROVED).** On `[1, ∞)`, `arcosh x ≤ arcosh y ↔ x ≤ y`. -/
theorem arcosh_le_arcosh {x y : ℝ} (hx : 1 ≤ x) (hy : 1 ≤ y) :
    arcosh x ≤ arcosh y ↔ x ≤ y :=
  strictMonoOn_arcosh.le_iff_le hx hy

/-- **Comparison, strict form (PROVED).** On `[1, ∞)`, `arcosh x < arcosh y ↔ x < y`. -/
theorem arcosh_lt_arcosh {x y : ℝ} (hx : 1 ≤ x) (hy : 1 ≤ y) :
    arcosh x < arcosh y ↔ x < y :=
  strictMonoOn_arcosh.lt_iff_lt hx hy

/-- **Continuity (PROVED).** `arcosh` is continuous on `[1, ∞)`. -/
theorem continuousOn_arcosh : ContinuousOn arcosh (Set.Ici (1 : ℝ)) := by
  have hpos : ∀ x ∈ Set.Ici (1 : ℝ), 0 < x + Real.sqrt (x ^ 2 - 1) := by
    intro x hx
    simp only [Set.mem_Ici] at hx
    have h0 : (0 : ℝ) ≤ Real.sqrt (x ^ 2 - 1) := Real.sqrt_nonneg _
    linarith
  apply ContinuousOn.log
  · fun_prop
  · intro x hx
    exact (hpos x hx).ne'

/-- **Differentiability, with derivative (PROVED).** For `1 < x`,
    `HasDerivAt arcosh (sqrt (x ^ 2 - 1))⁻¹ x`. Route: `arcosh = log ∘ (id + sqrt ∘
    (·² - 1))`; chain rule via `HasDerivAt.sqrt` and `HasDerivAt.log`, then simplify the
    resulting `(1 + x / s) / (x + s) = s⁻¹` (`s = sqrt (x^2-1) ≠ 0`) by `field_simp; ring`. -/
theorem hasDerivAt_arcosh {x : ℝ} (hx : 1 < x) :
    HasDerivAt arcosh (Real.sqrt (x ^ 2 - 1))⁻¹ x := by
  have hxpos : (0 : ℝ) < x ^ 2 - 1 := by nlinarith
  have hfne : x ^ 2 - 1 ≠ 0 := hxpos.ne'
  have hspos : 0 < Real.sqrt (x ^ 2 - 1) := Real.sqrt_pos.mpr hxpos
  have hpow : HasDerivAt (fun y : ℝ => y ^ 2 - 1) (2 * x) x := by
    have h := (hasDerivAt_pow 2 x).sub_const (1 : ℝ)
    simpa using h
  have hsqrt : HasDerivAt (fun y : ℝ => Real.sqrt (y ^ 2 - 1))
      ((2 * x) / (2 * Real.sqrt (x ^ 2 - 1))) x := hpow.sqrt hfne
  have hsum : HasDerivAt (fun y : ℝ => y + Real.sqrt (y ^ 2 - 1))
      (1 + (2 * x) / (2 * Real.sqrt (x ^ 2 - 1))) x := (hasDerivAt_id x).add hsqrt
  have hinner_ne : x + Real.sqrt (x ^ 2 - 1) ≠ 0 := by
    have h0 : (0 : ℝ) ≤ Real.sqrt (x ^ 2 - 1) := Real.sqrt_nonneg _
    positivity
  have hlog := hsum.log hinner_ne
  have hval : (1 + (2 * x) / (2 * Real.sqrt (x ^ 2 - 1))) / (x + Real.sqrt (x ^ 2 - 1))
      = (Real.sqrt (x ^ 2 - 1))⁻¹ := by
    have hsne : Real.sqrt (x ^ 2 - 1) ≠ 0 := hspos.ne'
    field_simp
    ring
  rw [hval] at hlog
  unfold arcosh
  exact hlog

/-- **Differentiability at a point (PROVED).** Immediate from `hasDerivAt_arcosh`. -/
theorem differentiableAt_arcosh {x : ℝ} (hx : 1 < x) : DifferentiableAt ℝ arcosh x :=
  (hasDerivAt_arcosh hx).differentiableAt

/-- **Differentiability on `(1, ∞)` (PROVED).** -/
theorem differentiableOn_arcosh : DifferentiableOn ℝ arcosh (Set.Ioi (1 : ℝ)) :=
  fun _ hx => (differentiableAt_arcosh hx).differentiableWithinAt

/- TODO (not proved in this draft; not a `sorry`, just not attempted -- real extra work
   beyond a short adaptation of the above):

   theorem contDiffOn_arcosh {n : WithTop ℕ∞} : ContDiffOn ℝ n arcosh (Set.Ioi 1) := ...
   theorem analyticAt_arcosh {x : ℝ} (hx : 1 < x) : AnalyticAt ℝ arcosh x := ...

   Route: iterate `hasDerivAt_arcosh` / build a `ContDiffAt` witness the way Mathlib's
   own `Real.arsinh` file does via `HasStrictFDerivAt` + induction on `n`, or (easier)
   route through the `OpenPartialHomeomorph` below and its `contDiffAt_symm_deriv`
   machinery once that bundling exists.

   def coshPartialEquiv : PartialEquiv ℝ ℝ where
     toFun := Real.cosh; invFun := arcosh; source := Set.Ici 0; target := Set.Ici 1
     map_source' / map_target' / left_inv' / right_inv' := (from the lemmas above) ...

   Route: every field is exactly one of `Real.one_le_cosh`, `arcosh_nonneg`,
   `arcosh_cosh`, `cosh_arcosh` above; this is genuinely a "short adaptation" that was
   simply not reached this session (time-boxed after the duplicate finding made further
   proof effort moot for submission purposes -- see `arcosh_pr_body.md`). -/

end Real

end
