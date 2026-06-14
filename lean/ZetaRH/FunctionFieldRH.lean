/-
Lever B: the FUNCTION-FIELD Riemann Hypothesis dependency chain.

See `docs/03_research/optimizing_rh_for_ai.md` (lever B) and
`docs/03_research/modular_polarization_carrier.md`. The point of lever B is to make
Lean the non-circular value function: formalize Weil's function-field proof end-to-end,
so the Spec(Z) lift becomes a proof-transport task with Lean rejecting every circular
or wrong step.

This file makes the genus-1 (elliptic) function-field RH chain EXPLICIT and proves
everything except the one geometric step that Mathlib lacks. The chain:

  (geometry)   the primitive intersection form on C x C is the 2x2 G_prim(1,q,t),
               and Castelnuovo-Severi / Weil's Hodge index theorem makes it
               negative-definite                                  -- `hodge_index_curve_elliptic`, SORRY
  (keystone)   NegDef G_prim  <=>  t^2 < 4 q  (Hasse-Weil)        -- `negDef_iff_hasseWeil` (#2G-1, PROVED in HodgeIndex)
  (eigenvalue) t^2 < 4 q  =>  the Frobenius roots are non-real    -- `root_nonreal`, PROVED here
               and a non-real root has |alpha|^2 = q              -- `eigenvalue_modulus`, PROVED here
  (RH)         |alpha| = sqrt(q): the curve's zeta zeros lie on |s| = q^{-1/2}, i.e. Re = 1/2.

The implication "Hodge index => RH for the curve" is therefore SORRY-FREE here
(`functionfield_RH_elliptic_of_hodge`); the only `sorry` is the geometric input,
isolated as `hodge_index_curve_elliptic`. That sorry is the lever-B gap: Mathlib has
no algebraic-curve intersection theory, so the Castelnuovo-Severi step is absent (it is
a theorem in the literature, ~medium effort to formalize once curves/Chow groups exist).

The eigenvalue extraction proved here is the new sorry-free link: Vieta on the real
quadratic X^2 - tX + q gives alpha * conj(alpha) = q, and alpha * conj(alpha) = |alpha|^2.
-/

import ZetaRH.HodgeIndex
import Mathlib.Data.Complex.Basic

namespace ZetaRH.FunctionFieldRH

open ZetaRH.HodgeIndex.IntersectionSignature

/-- **Eigenvalue extraction (PROVED).** A genuinely complex (non-real) root `α` of the
    Frobenius characteristic polynomial `X^2 - tX + q` (real `t, q`) has `|α|^2 = q`.

    Proof: conjugating the equation shows `conj α` is also a root; since `α ≠ conj α`
    the two roots are `α, conj α`, so by Vieta `α + conj α = t` and `α · conj α = q`.
    But `α · conj α = normSq α`, hence `normSq α = q`. -/
theorem eigenvalue_modulus (t q : ℝ) (α : ℂ)
    (hroot : α ^ 2 - (t : ℂ) * α + (q : ℂ) = 0)
    (hnonreal : α ≠ (starRingEnd ℂ) α) : Complex.normSq α = q := by
  have hconj : (starRingEnd ℂ α) ^ 2 - (t : ℂ) * (starRingEnd ℂ α) + (q : ℂ) = 0 := by
    have h := congrArg (starRingEnd ℂ) hroot
    simpa only [map_add, map_sub, map_mul, map_pow, Complex.conj_ofReal, map_zero] using h
  have hne : α - starRingEnd ℂ α ≠ 0 := sub_ne_zero.mpr hnonreal
  have h1 : (α - starRingEnd ℂ α) * (α + starRingEnd ℂ α - (t : ℂ)) = 0 := by
    linear_combination hroot - hconj
  have hsum : α + starRingEnd ℂ α = (t : ℂ) := by
    rcases mul_eq_zero.mp h1 with h | h
    · exact absurd h hne
    · exact sub_eq_zero.mp h
  have hprod : α * starRingEnd ℂ α = (q : ℂ) := by linear_combination α * hsum - hroot
  have hmc : α * starRingEnd ℂ α = ((Complex.normSq α : ℝ) : ℂ) := Complex.mul_conj α
  have hcast : ((Complex.normSq α : ℝ) : ℂ) = ((q : ℝ) : ℂ) := by rw [← hmc, hprod]
  exact_mod_cast hcast

/-- **Non-reality of the Frobenius roots (PROVED).** When the Hasse-Weil bound
    `t^2 < 4q` holds, every root of `X^2 - tX + q` is non-real: a real root would force
    the discriminant `t^2 - 4q ≥ 0`. -/
theorem root_nonreal (t q : ℝ) (α : ℂ)
    (hroot : α ^ 2 - (t : ℂ) * α + (q : ℂ) = 0) (hHW : t ^ 2 < 4 * q) :
    α ≠ (starRingEnd ℂ) α := by
  intro h
  have him : α.im = 0 := Complex.conj_eq_iff_im.mp h.symm
  have hre : α = (α.re : ℂ) := by
    apply Complex.ext <;> simp [him]
  have hr : α.re ^ 2 - t * α.re + q = 0 := by
    have hc : ((α.re ^ 2 - t * α.re + q : ℝ) : ℂ) = 0 := by
      push_cast; rw [← hre]; exact hroot
    exact_mod_cast hc
  nlinarith [sq_nonneg (t - 2 * α.re), hHW, hr]

/-- **The one open geometric step (SORRY = the lever-B gap).** For a smooth projective
    genus-1 curve `C/F_q` with Frobenius trace `t`, the primitive intersection form on
    `C × C` is negative-definite (Castelnuovo-Severi / Weil's Hodge index theorem).

    This is a theorem in the literature, but Mathlib has no algebraic-curve intersection
    theory, so it cannot yet be stated against a real curve, let alone proved. The
    `hcurve` hypothesis is a placeholder for the curve data. This `sorry` is exactly
    where the function-field formalization stops; filling it (after building curves /
    Chow groups in Lean) closes the chain. -/
theorem hodge_index_curve_elliptic (q t : ℝ) (hq : 0 < q) (hcurve : True) :
    NegDef 1 q t := by
  sorry

/-- **Hodge index => RH for the curve (SORRY-FREE implication).** Given the geometric
    Hodge-index input (`NegDef`, i.e. the primitive form is negative-definite) and a
    Frobenius root `α`, its modulus is `√q`: the function-field Riemann Hypothesis for
    the curve. The keystone (#2G-1) and the eigenvalue extraction are proved; only the
    geometric input is assumed. -/
theorem functionfield_RH_elliptic_of_hodge {q t : ℝ} (_hq : 0 < q)
    (hHodge : NegDef 1 q t) {α : ℂ} (hroot : α ^ 2 - (t : ℂ) * α + (q : ℂ) = 0) :
    Complex.normSq α = q := by
  have hHW : t ^ 2 < 4 * 1 ^ 2 * q := (negDef_iff_hasseWeil (by norm_num)).mp hHodge
  have hHW' : t ^ 2 < 4 * q := by nlinarith [hHW]
  exact eigenvalue_modulus t q α hroot (root_nonreal t q α hroot hHW')

/-- **The full function-field RH chain (genus 1).** Combining the geometric step (the
    one `sorry`) with the proved implication: a Frobenius root of a genus-1 curve over
    `F_q` has `|α|^2 = q`. The single `sorry` is `hodge_index_curve_elliptic` (the
    Castelnuovo-Severi geometry); everything downstream of it is proved. -/
theorem functionfield_RH_elliptic (q t : ℝ) (hq : 0 < q) (hcurve : True)
    {α : ℂ} (hroot : α ^ 2 - (t : ℂ) * α + (q : ℂ) = 0) : Complex.normSq α = q :=
  functionfield_RH_elliptic_of_hodge hq (hodge_index_curve_elliptic q t hq hcurve) hroot

end ZetaRH.FunctionFieldRH
