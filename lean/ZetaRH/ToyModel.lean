/-
The toy sandbox, Lean face: genus-1 grader correctness, BOTH directions.

Companion to `experiments/toy/` (the Python sandbox). The toy grades a candidate M4
construction by whether it certifies the RH-true curves (PSD) and rejects the RH-false
fakes (indefinite). At genus 1 both directions are now Lean theorems:

  reproduce-Weil : an RH-true instance (Hasse bound `t² ≤ 4q`) has every Frobenius root ON
                   the circle, `|α|² = q`. This reuses the lever-B chain
                   (`FunctionFieldRH.eigenvalue_modulus_le`), which is sorry-free.

  reject-fakes   : an RH-false instance (`t² > 4q`, the off-circle / off-line case) has a
                   Frobenius root OFF the circle, `|α|² ≠ q`. This is the NEW off-line
                   witness proved here, and it is the formal content of the toy grader's
                   `rejects_fakes` check at genus 1.

Together they say: at genus 1, the moment/Hasse polarization is PSD iff RH for the instance,
with an explicit off-circle eigenvalue exhibited on the fake side. This is exactly what the
Python grader checks numerically; here it is a theorem. (The honest caveat from the Python
README applies: this is the genus-1 / single-circle face. The lift to Z is M4, untouched.)
-/

import ZetaRH.FunctionFieldRH
import Mathlib.Analysis.SpecialFunctions.Sqrt

namespace ZetaRH.ToyModel

open ZetaRH.FunctionFieldRH

/-- **Reproduce-Weil (genus 1).** Under the Hasse bound `t² ≤ 4q` (an RH-true toy instance),
    every Frobenius root `α` of `X² − tX + q` lies on the circle: `|α|² = q`. This is the
    lever-B eigenvalue extraction (`eigenvalue_modulus_le`), re-exported in the toy framing;
    it covers the supersingular boundary `t² = 4q` as well. -/
theorem toy_reproduce_weil {t q : ℝ} (hHasse : t ^ 2 ≤ 4 * q) {α : ℂ}
    (hroot : α ^ 2 - (t : ℂ) * α + (q : ℂ) = 0) : Complex.normSq α = q :=
  eigenvalue_modulus_le t q α hroot hHasse

/-- **Reject-fakes (genus 1), the off-line witness (NEW).** On an RH-false toy instance
    (`q > 0` and `t² > 4q`, i.e. the off-circle / real-root half of the discriminant), there
    is a Frobenius root `α` of `X² − tX + q` OFF the circle: `|α|² ≠ q`.

    Witness: the real root `α = (t + √(t²−4q))/2`. It is a genuine root, and its modulus²
    equals `q` only if `q = 0`; since `q > 0` it is off the circle. Equivalently: the two real
    roots multiply to `q > 0`, so if both had modulus `√q` they would be equal, contradicting
    that the discriminant is strictly positive. This is the formal `rejects_fakes` content. -/
theorem toy_reject_fake {t q : ℝ} (hq : 0 < q) (hfake : 4 * q < t ^ 2) :
    ∃ α : ℂ, α ^ 2 - (t : ℂ) * α + (q : ℂ) = 0 ∧ Complex.normSq α ≠ q := by
  set d : ℝ := Real.sqrt (t ^ 2 - 4 * q) with hd_def
  have hdisc : 0 < t ^ 2 - 4 * q := by linarith
  have hd2 : d ^ 2 = t ^ 2 - 4 * q := Real.sq_sqrt (le_of_lt hdisc)
  have hd_pos : 0 < d := Real.sqrt_pos.mpr hdisc
  refine ⟨(((t + d) / 2 : ℝ) : ℂ), ?_, ?_⟩
  · -- α is a root: cast the real identity `((t+d)/2)² − t·((t+d)/2) + q = 0`.
    have hroot_real : ((t + d) / 2) ^ 2 - t * ((t + d) / 2) + q = 0 := by
      linear_combination (1 / 4 : ℝ) * hd2
    have hcast :
        (((t + d) / 2 : ℝ) : ℂ) ^ 2 - (t : ℂ) * (((t + d) / 2 : ℝ) : ℂ) + (q : ℂ)
          = ((((t + d) / 2) ^ 2 - t * ((t + d) / 2) + q : ℝ) : ℂ) := by
      push_cast; ring
    rw [hcast, hroot_real]; simp
  · -- |α|² = ((t+d)/2)², which equals q only if q = 0.
    rw [Complex.normSq_ofReal]
    intro heq
    have e1 : (t + d) ^ 2 = 4 * q := by linear_combination 4 * heq
    have e2 : d ^ 2 + t * d = 0 := by linear_combination (1 / 2 : ℝ) * e1 + (1 / 2 : ℝ) * hd2
    have e3 : d * (d + t) = 0 := by linear_combination e2
    have e4 : d + t = 0 := by
      rcases mul_eq_zero.mp e3 with h | h
      · exact absurd h (ne_of_gt hd_pos)
      · exact h
    have hq0 : q = 0 := by linear_combination (1 / 4 : ℝ) * hd2 + ((t - d) / 4) * e4
    linarith [hq, hq0]

/-- **The toy genus-1 grader correctness, both directions in one statement.** For `q > 0`:
    if the Hasse bound holds (`t² ≤ 4q`, RH-true) every root is on the circle; if it fails
    strictly (`4q < t²`, RH-false) some root is off the circle. The reference candidate (the
    moment/Hasse form) is therefore correct on both halves of the battery at genus 1. -/
theorem toy_grader_genus1_correct {t q : ℝ} (hq : 0 < q) :
    (t ^ 2 ≤ 4 * q →
        ∀ α : ℂ, α ^ 2 - (t : ℂ) * α + (q : ℂ) = 0 → Complex.normSq α = q)
    ∧ (4 * q < t ^ 2 →
        ∃ α : ℂ, α ^ 2 - (t : ℂ) * α + (q : ℂ) = 0 ∧ Complex.normSq α ≠ q) :=
  ⟨fun hHasse _α hroot => toy_reproduce_weil hHasse hroot, fun hfake => toy_reject_fake hq hfake⟩

end ZetaRH.ToyModel
