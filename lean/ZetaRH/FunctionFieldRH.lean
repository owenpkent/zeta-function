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

This file is now FULLY SORRY-FREE. The chain "Hodge index => RH for the curve" is proved
(`functionfield_RH_elliptic_of_hodge`, `functionfield_RH_elliptic`); the one geometric
input (Castelnuovo-Severi, `t^2 < 4q`) is carried as an explicit hypothesis field of the
`EllipticFrobeniusData` structure, NOT a `sorry`. So the function-field RH chain is a
sorry-free CONDITIONAL theorem whose single assumption is the curve-intersection geometry
Mathlib lacks (a theorem in the literature, ~medium effort to formalize once curves/Chow
groups exist). This also repairs the previous `hodge_index_curve_elliptic`, which admitted
a FALSE proposition (`NegDef 1 q t` for all `q,t`, false when `t^2 ≥ 4q`) via `sorry`.

The eigenvalue extraction proved here is the new sorry-free link: Vieta on the real
quadratic X^2 - tX + q gives alpha * conj(alpha) = q, and alpha * conj(alpha) = |alpha|^2.
-/

import ZetaRH.HodgeIndex
import Mathlib.Data.Complex.Basic

namespace ZetaRH.FunctionFieldRH

open ZetaRH.HodgeIndex.IntersectionSignature

/-! ## M-0 (lever B roadmap): the discriminant bridge lemma

    See `docs/03_research/lever_b_function_field_plan.md`. In the elementary proof of the
    Hasse bound, "every isogeny has non-negative degree" gives
    `deg(m + n φ) = m^2 + m n t + n^2 q ≥ 0`, a positive-(semi)definite binary quadratic
    form, and a positive-(semi)definite form has non-positive discriminant `t^2 ≤ 4q`.
    These two lemmas are that bridge. They are the positive mirror of the keystone #2G-1
    (`negDef_iff_hasseWeil`). The remaining glue for milestone M-3 -- the form is `≥ 0`
    for all *real* m,n, obtained from `≥ 0` for integer m,n by homogeneity and density --
    is not done here; M-0 is just the discriminant step. -/

/-- A positive-semidefinite real binary quadratic form `m^2 + t·m·n + q·n^2 ≥ 0` (for all
    real `m, n`) has non-positive discriminant: `t^2 ≤ 4q`. Proof: evaluate at
    `(m, n) = (-t/2, 1)`, where the form equals `q - t^2/4`. -/
theorem disc_nonpos_of_posSemidef {t q : ℝ}
    (h : ∀ m n : ℝ, 0 ≤ m ^ 2 + t * m * n + q * n ^ 2) : t ^ 2 ≤ 4 * q := by
  have hmin := h (-t / 2) 1
  nlinarith [hmin]

/-- A positive-definite real binary quadratic form (`> 0` off the origin) has negative
    discriminant: `t^2 < 4q` (the strict Hasse bound). This is the form M-0 the chain
    needs: the Frobenius degree form is positive-DEFINITE (`deg ψ = 0 ↔ ψ = 0`), and the
    strict bound feeds `t^2 < 4q ⇒ non-real roots ⇒ |α| = √q`. -/
theorem disc_neg_of_posDef {t q : ℝ}
    (h : ∀ m n : ℝ, (m, n) ≠ (0, 0) → 0 < m ^ 2 + t * m * n + q * n ^ 2) :
    t ^ 2 < 4 * q := by
  have hne : ((-t / 2 : ℝ), (1 : ℝ)) ≠ (0, 0) := by
    intro hc
    exact one_ne_zero (Prod.ext_iff.mp hc).2
  have hmin := h (-t / 2) 1 hne
  nlinarith [hmin]

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

/-- The geometric input for a genus-1 curve, packaged honestly. The Castelnuovo-Severi
    / Hodge-index inequality `t^2 < 4q` (equivalently the primitive intersection form on
    `C × C` is negative-definite, equivalently `|t| < 2 sqrt q`) is a THEOREM over a real
    curve, but Mathlib has no algebraic-curve intersection theory to derive it from the
    curve's definition. So it is carried here as an explicit hypothesis field `hodge_index`
    -- the lever-B gap, made honest: a hypothesis, not a `sorry`.

    (This repairs the previous `hodge_index_curve_elliptic`, which stated `NegDef 1 q t`
    behind a vacuous `True` hypothesis -- a FALSE proposition for `t^2 ≥ 4q`, admitted by
    `sorry`. The constraint must live in the data, and it does, as `hodge_index`.) -/
structure EllipticFrobeniusData where
  q : ℝ
  t : ℝ
  hq : 0 < q
  /-- Castelnuovo-Severi / the Hodge index for the curve: the one geometric input (#FF-geom). -/
  hodge_index : t ^ 2 < 4 * q

/-- The Hodge-index input gives negative-definiteness of the primitive form. SORRY-FREE:
    the geometric content is the explicit `hodge_index` field; the keystone #2G-1 does the
    rest. -/
theorem negDef_of_curve (C : EllipticFrobeniusData) : NegDef 1 C.q C.t := by
  have h : C.t ^ 2 < 4 * 1 ^ 2 * C.q := by nlinarith [C.hodge_index]
  exact (negDef_iff_hasseWeil (by norm_num)).mpr h

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

/-- **The full function-field RH chain (genus 1), SORRY-FREE modulo one explicit
    geometric hypothesis.** Given the curve datum `C` (which carries the Castelnuovo-Severi
    inequality as its `hodge_index` field) and a Frobenius root `α`, the modulus is `√q`.
    The entire chain -- the keystone #2G-1, the eigenvalue extraction, and this assembly --
    is proved; the single unformalized input is `C.hodge_index` (the curve-intersection
    geometry Mathlib lacks), now an explicit, true hypothesis rather than a `sorry`. -/
theorem functionfield_RH_elliptic (C : EllipticFrobeniusData)
    {α : ℂ} (hroot : α ^ 2 - (C.t : ℂ) * α + (C.q : ℂ) = 0) : Complex.normSq α = C.q :=
  functionfield_RH_elliptic_of_hodge C.hq (negDef_of_curve C) hroot

end ZetaRH.FunctionFieldRH
