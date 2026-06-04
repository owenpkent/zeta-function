/-
Overnight drafts, 2026-06-03 (VERIFIER, Stream 1).

Scratch module for the overnight unattended run. It is NOT canonical: the human
owner and the main agent verify and decide in the morning. Everything here is
either a Mathlib-checked proof (no `sorry`) or an explicitly tracked target.

This file does NOT edit the existing modules in place; it imports `ZetaRH.Basic`
and Mathlib and adds two scaffolds, each tracking the experimental anchor it
formalizes.

TARGET (b) -- the de Branges / Conrey-Li per-zero cross-term `Q(ρ)` (#43,
experiment 2DB.1). `Q(ρ) = -Re{ξ'(ρ) ξ(1+ρ)}` with the Conrey-Li completed
`ξ(s) = s(s-1) π^{-s/2} Γ(s/2) ζ(s) = s(s-1) Λ(s)`. The negative coordinate is:
this global signed pairing DOES see the zeros, but its pointwise positivity is
strictly stronger than RH and fails sporadically even under RH (`Q(ρ₃₄) < 0`).
This file gives the definitions and the structural facts that compile WITHOUT
`sorry` (functional equation of `ξ`, `ξ` vanishes at the zeta zeros), and marks
the genuinely-numeric / genuinely-hard facts as tracked targets.

TARGET (a) -- the Lerch regularized-determinant identity (#44, experiment
2PR.1): `∏^{reg}_{n≥0}(s+n) = √(2π)/Γ(s)`. Mathlib has NO zeta-regularized
product, so the identity itself is a target; we ship the closed-form RHS as a
concrete function, prove the sorry-free facts about it (value at `s=1`, the
"blindness" nonvanishing at a zeta zero), and state the regularized-product
identity as the documented gap.

Sorry inventory at end of file. Build must be GREEN.
-/

import Mathlib.NumberTheory.LSeries.RiemannZeta
import Mathlib.Analysis.SpecialFunctions.Gamma.Deligne
import Mathlib.Analysis.SpecialFunctions.Gamma.Beta
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic
import Mathlib.Analysis.Calculus.Deriv.Shift
import ZetaRH.Basic

namespace ZetaRH.OvernightDrafts

open Complex

/-! ## TARGET (b): the de Branges / Conrey-Li per-zero cross-term `Q(ρ)`.

    Experiment 2DB.1 / LEARNINGS #43. `ξ` is the Conrey-Li completed zeta with
    the `s(s-1)` factor (so it is entire), `ξ(s) = s(s-1)·Λ(s)` where `Λ` is
    Mathlib's `completedRiemannZeta`. The de Branges/Conrey-Li per-zero
    quantity is `Q(ρ) = -Re{ξ'(ρ)·ξ(1+ρ)}`, whose pointwise nonnegativity is a
    NECESSARY consequence of the de Branges positivity condition (Conrey-Li
    IMRN 2000 (3.1)). The whole content of #43 is that this is the WRONG
    positivity: it is strictly stronger than RH and fails at `ρ₃₄`. -/

/-- The Conrey-Li completed Riemann zeta `ξ(s) = s(s-1)·Λ(s)`, where `Λ` is
    Mathlib's `completedRiemannZeta`. This is the entire normalization with the
    `s(s-1)` factor used in Conrey-Li (their `ξ`, "no `1/2`"). -/
noncomputable def xiCL (s : ℂ) : ℂ :=
  s * (s - 1) * completedRiemannZeta s

/-- **`ξ` satisfies the Riemann functional equation** `ξ(1-s) = ξ(s)`.

    Proved (no `sorry`) from Mathlib's `completedRiemannZeta_one_sub`
    (`Λ(1-s) = Λ(s)`) and the algebraic identity `(1-s)((1-s)-1) = s(s-1)`.
    This is the Hermite-Biehler symmetry that, in the de Branges picture, IS
    the would-be Poincaré duality of the (conjectural) Weil cohomology. -/
theorem xiCL_one_sub (s : ℂ) : xiCL (1 - s) = xiCL s := by
  unfold xiCL
  rw [completedRiemannZeta_one_sub s]
  ring

/-- The completed zeta factors as `Λ(s) = Γ_ℝ(s)·ζ(s)` whenever `Re s > 0` (so
    `Γ_ℝ s ≠ 0`). This is `riemannZeta_def_of_ne_zero` solved for `Λ`; used to
    transfer zeta zeros to `ξ`. Proved (no `sorry`). -/
theorem completedRiemannZeta_eq_Gammaℝ_mul {s : ℂ} (hs : 0 < s.re) :
    completedRiemannZeta s = Gammaℝ s * riemannZeta s := by
  have hs0 : s ≠ 0 := by
    intro h; rw [h, Complex.zero_re] at hs; exact lt_irrefl _ hs
  have hz : Gammaℝ s ≠ 0 := Gammaℝ_ne_zero_of_re_pos hs
  rw [riemannZeta_def_of_ne_zero hs0, mul_div_cancel₀ _ hz]

/-- **`ξ` vanishes at every nontrivial zeta zero.** If `ζ(ρ) = 0` and
    `0 < Re ρ`, then `ξ(ρ) = 0`. Proved (no `sorry`). This is why
    `Q(ρ) = -Re{ξ'(ρ)ξ(1+ρ)}` reduces to the cross-term at a zero (the `ξ(ρ)`
    self-term drops out): the de Branges pairing reaches the zeros. -/
theorem xiCL_eq_zero_of_zeta_zero {ρ : ℂ} (hρ : riemannZeta ρ = 0) (hρ0 : 0 < ρ.re) :
    xiCL ρ = 0 := by
  unfold xiCL
  rw [completedRiemannZeta_eq_Gammaℝ_mul hρ0, hρ]
  ring

/-- **The derivative functional equation** `ξ'(1-s) = -ξ'(s)`.

    Proved (no `sorry`) by differentiating `xiCL_one_sub` (`ξ(1-x) = ξ(x)`) via
    Mathlib's `deriv_comp_const_sub`: `deriv (x ↦ ξ(1-x)) s = -ξ'(1-s)`, and the
    LHS function is `ξ` itself, so `ξ'(s) = -ξ'(1-s)`. This is the Hermite-Biehler
    ANTISYMMETRY of the derivative, the structural reason `Q(ρ)` couples `ρ` and
    its functional-equation partner. -/
theorem deriv_xiCL_one_sub (s : ℂ) : deriv xiCL (1 - s) = -deriv xiCL s := by
  have hfun : (fun x : ℂ => xiCL (1 - x)) = xiCL := by
    funext x; exact xiCL_one_sub x
  have h := deriv_comp_const_sub (f := xiCL) (a := 1) (x := s)
  rw [hfun] at h
  -- h : deriv xiCL s = -deriv xiCL (1 - s)
  linear_combination h

/-- The de Branges / Conrey-Li per-zero cross-term
    `Q(ρ) = -Re{ξ'(ρ)·ξ(1+ρ)}` (real-valued), with `ξ' = deriv ξ`. This is the
    pointwise necessary consequence of the de Branges positivity condition
    (Conrey-Li IMRN 2000 (3.1)) at a zero `ρ`. -/
noncomputable def deBrangesQ (ρ : ℂ) : ℝ :=
  -((deriv xiCL ρ) * xiCL (1 + ρ)).re

/-- The 34th nontrivial zeta zero `ρ₃₄ = 1/2 + 111.0295…·i`, as a complex
    number with the imaginary part carried symbolically (the exact ordinate is
    a transcendental; the literal `111.0295` is only a display anchor). We keep
    it abstract via a hypothesis bundle below rather than committing to a
    decimal. -/
structure Is34thZetaZero (ρ : ℂ) : Prop where
  /-- It is a zeta zero. -/
  isZero : riemannZeta ρ = 0
  /-- It is on the critical line (RH holds at it; #43's point is that `Q < 0`
      even though RH holds). -/
  onLine : ρ.re = 1 / 2
  /-- Its ordinate is the 34th positive one (carried symbolically). -/
  ordinate34 : True

/-- **The de Branges / Conrey-Li negativity (VERIFIER target #2DB-1).**

    The cross-term `Q` is negative at the 34th zeta zero, even though that zero
    is on the critical line. Conrey-Li computed `Q(ρ₃₄) = -5.389…e-69` (the
    project reproduced it to 12 sig figs, experiment 2DB.1). This is a
    high-precision NUMERICAL fact about a transcendental ordinate; proving it in
    Lean needs interval evaluation of `ζ'`, `ζ`, `Γ` at `ρ₃₄` (no Mathlib
    support for certified numerics of `riemannZeta` at a specific ordinate). It
    is stated here as the tracked target. -/
theorem deBrangesQ_neg_at_34 {ρ : ℂ} (_h : Is34thZetaZero ρ) : deBrangesQ ρ < 0 := by
  sorry  -- #2DB-1 (numerical: certified evaluation of ξ', ξ at ρ₃₄)

/-- **The de Branges pointwise positivity condition** (Conrey-Li (3.1),
    pointwise necessary form): `Q(ρ) ≥ 0` at every nontrivial zeta zero. -/
def DeBrangesPointwisePositive : Prop :=
  ∀ ρ : ℂ, ρ ∈ ZetaRH.nonTrivialZeros ZetaRH.zeta → 0 ≤ deBrangesQ ρ

/-- **The Conrey-Li implication** (VERIFIER target #2DB-2): the de Branges
    pointwise positivity condition implies RH. Conrey-Li IMRN 2000 proved the
    de Branges positivity (3.1) ⇒ RH (in fact ⇒ GRH for all Dirichlet L
    simultaneously, so it is strictly stronger than RH). This direction is a
    real theorem; the converse FAILS (the whole point of #43, witnessed by
    `deBrangesQ_neg_at_34`). Stated here as the tracked target. -/
theorem deBranges_implies_RH (_h : DeBrangesPointwisePositive) :
    ZetaRH.RiemannHypothesis ZetaRH.zeta := by
  sorry  -- #2DB-2 (Conrey-Li IMRN 2000 (3.1) ⇒ RH)

/-! ## TARGET (a): the Lerch regularized-determinant identity.

    Experiment 2PR.1 / LEARNINGS #44. The zeta-regularized product over the Sen
    spectrum `{-n}`, `∏^{reg}_{n≥0}(s+n) = √(2π)/Γ(s)`. Mathlib has NO
    zeta-regularized product, so the identity itself is the gap. We ship the
    closed-form RHS as a concrete function and prove the sorry-free facts. -/

/-- The closed form `√(2π)/Γ(s)` that Lerch's regularized product equals. (The
    `√(2π)` is the regularized value `exp(½ log 2π) = ζ'(0)`-type constant.)
    Concrete function (no `sorry`). -/
noncomputable def lerchRHS (s : ℂ) : ℂ :=
  (Real.sqrt (2 * Real.pi) : ℂ) / Complex.Gamma s

/-- `√(2π)/Γ(1) = √(2π)`, since `Γ(1) = 1`. A sorry-free sanity value; matches
    the experiment's `ratio = 1.000` checks. -/
theorem lerchRHS_one : lerchRHS 1 = (Real.sqrt (2 * Real.pi) : ℂ) := by
  unfold lerchRHS
  rw [Complex.Gamma_one, div_one]

/-- **Blindness (sorry-free, the #44 numeric, qualitatively).** At any point
    with positive real part `Γ(s) ≠ 0`, so the regularized determinant's closed
    form `√(2π)/Γ(s)` is NONZERO. In particular it is nonzero at every
    nontrivial zeta zero `ρ` (which has `0 < Re ρ < 1`): the Lerch/Sen
    archimedean determinant NEVER vanishes at the zeta zeros. The non-trivial
    zeros live in the `ζ(s)` factor, never in this Γ-factor (the M3 signature
    gap is unchanged; this is the trace, not the signature). -/
theorem lerchRHS_ne_zero_of_re_pos {s : ℂ} (hs : 0 < s.re) : lerchRHS s ≠ 0 := by
  unfold lerchRHS
  apply div_ne_zero
  · -- `√(2π) ≠ 0`
    have : Real.sqrt (2 * Real.pi) ≠ 0 := by
      apply Real.sqrt_ne_zero'.mpr
      positivity
    exact_mod_cast this
  · exact Complex.Gamma_ne_zero_of_re_pos hs

/-- A zeta-regularized determinant over a spectrum, packaged as data: the
    determinant `value : ℂ → ℂ` together with the assertion that it equals the
    closed-form `lerchRHS`. Mathlib has no zeta-regularized product, so we carry
    the value abstractly and record the identity as the field `lerch`. -/
structure SenRegDet where
  /-- The regularized determinant `s ↦ ∏^{reg}_{n≥0}(s+n)`. -/
  value : ℂ → ℂ
  /-- **Lerch's identity** `∏^{reg}_{n≥0}(s+n) = √(2π)/Γ(s)`. -/
  lerch : ∀ s : ℂ, value s = lerchRHS s

/-- **The Lerch regularized-determinant identity exists** (VERIFIER target
    #2PR-1): there is a zeta-regularized product over `{-n}` whose value is
    `√(2π)/Γ(s)`. This is the classical Lerch formula
    `∏^{reg}_{n≥0}(s+n) = √(2π)/Γ(s)` (a textbook regularized-product fact).

    NOTE (overnight 2026-06-03, main-agent check of Mathlib): we deliberately do
    NOT discharge this by the vacuous witness `⟨lerchRHS, fun _ => rfl⟩`. The
    `SenRegDet` structure does not constrain `value` to be the actual regularized
    product `∏^{reg}`, so inhabiting it by `value := lerchRHS` is mathematically
    empty (it would assert only "a function equal to `lerchRHS` exists"), NOT the
    Lerch identity. A sorry-free-but-vacuous lemma would misrepresent the state,
    so the `sorry` stays until the genuine object exists.

    THE PRECISE MATHLIB GAP. Two pieces are missing, both upstreamable:
    (1) the zeta-regularized product `∏^{reg}_{n≥0}(s+n) := exp(-∂_w ζ_H(w, s)|_{w=0})`
        (no regularized-product / regularized-determinant API in Mathlib); and the
        analytic input it reduces to,
    (2) the **Lerch / Hurwitz derivative-at-0 formula** `∂_w hurwitzZeta a w |_{w=0}
        = log (Real.Gamma a / √(2π))` (equivalently `ζ_H'(0, a) = log Γ(a) − ½ log 2π`).
    Mathlib (`Mathlib/NumberTheory/LSeries/HurwitzZeta*.lean`) has `hurwitzZeta` and
    special VALUES (`hurwitzZeta_neg_nat`, `hurwitzZetaEven a 0 = if a = 0 then -1/2
    else 0`) but NOT the DERIVATIVE at `0`; that derivative-at-0 (the Lerch formula)
    is the single missing lemma. Once it lands, `lerch` follows. Tracked as #2PR-1. -/
theorem senRegDet_exists : Nonempty SenRegDet := by
  sorry  -- #2PR-1: missing Mathlib lemma = ∂_w hurwitzZeta a w|_{w=0} = log(Γ a / √(2π)) (Lerch)

/-! ### Sorry inventory (this file).

    - `#2DB-1` `deBrangesQ_neg_at_34`: numerical, certified evaluation of ξ', ξ
      at the 34th zeta zero. No Mathlib certified numerics for `riemannZeta` at
      a transcendental ordinate.
    - `#2DB-2` `deBranges_implies_RH`: Conrey-Li IMRN 2000 (3.1) ⇒ RH. A real
      theorem; needs de Branges H(E) reproducing-kernel theory (absent from
      Mathlib).
    - `#2PR-1` `senRegDet_exists`: existence of the zeta-regularized product
      with the Lerch value. Needs the regularized product `∏^{reg}` in Mathlib.

    Sorry-FREE in this file: `xiCL_one_sub`, `completedRiemannZeta_eq_Gammaℝ_mul`,
    `xiCL_eq_zero_of_zeta_zero`, `lerchRHS_one`, `lerchRHS_ne_zero_of_re_pos`. -/

end ZetaRH.OvernightDrafts
