/-
MathlibBridge: collected lemmas needed from Mathlib, with explicit upstream
status flags.

This module is the "wish list" of Mathlib lemmas needed by the ZetaRH
project. Each lemma is either:

  - **PRESENT**: already in Mathlib (may need a relocation or a small
    convenience wrapper, marked with `-- WRAP:`).
  - **PR**: in flight as a Mathlib PR (with PR number).
  - **TODO**: not yet contributed; needs to be proved here as `sorry` and
    eventually upstreamed.

This file is the SYNTHESIZER-maintained interface between project-local
content and Mathlib upstream. VERIFIER agents should attempt each `sorry`
here as a first checkpoint before tackling project-local theorems that
depend on them.
-/

import Mathlib.NumberTheory.LSeries.RiemannZeta
import Mathlib.NumberTheory.DirichletCharacter.Basic
import Mathlib.NumberTheory.LSeries.Dirichlet
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace ZetaRH.MathlibBridge

open Complex Real

/-! ### Riemann zeta function: present in Mathlib. -/

/-- The Riemann zeta function (re-export for visibility in this namespace).
    PRESENT in `Mathlib.NumberTheory.LSeries.RiemannZeta`. -/
noncomputable def riemannZeta : ℂ → ℂ := _root_.riemannZeta

/-- ζ has a simple pole at s = 1: `(s - 1) ζ(s) → 1` as `s → 1`.
    PRESENT in Mathlib as `riemannZeta_residue_one`. VERIFIER target #MB-1
    DISCHARGED (no sorry). -/
theorem zeta_pole_at_one :
    Filter.Tendsto (fun s ↦ (s - 1) * riemannZeta s) (nhdsWithin 1 {1}ᶜ) (nhds 1) :=
  riemannZeta_residue_one

/-- ζ(s) ≠ 0 for Re(s) > 1.
    PRESENT in Mathlib as `riemannZeta_ne_zero_of_one_lt_re`
    (`Mathlib.NumberTheory.LSeries.Dirichlet`). VERIFIER target #MB-2
    DISCHARGED (no sorry). -/
theorem zeta_ne_zero_re_gt_one : ∀ s : ℂ, 1 < s.re → riemannZeta s ≠ 0 :=
  fun _ hs => riemannZeta_ne_zero_of_one_lt_re hs

/-! ### Dirichlet characters mod q. -/

/-- A Dirichlet character mod q is a `MulChar (ZMod q) ℂ` extended by 0
    outside the unit group, packaged as `DirichletCharacter ℂ q`.
    PRESENT in `Mathlib.NumberTheory.DirichletCharacter.Basic`. -/
example (q : ℕ) [NeZero q] (_χ : DirichletCharacter ℂ q) : Prop := True

/-! ### Hurwitz zeta (for D-H continuation). -/

/-- The Hurwitz zeta function `ζ(s, a) = ∑_{n ≥ 0} 1 / (n + a)^s` is
    PRESENT in Mathlib as `Complex.hurwitzZeta` (in
    `Mathlib.NumberTheory.LSeries.HurwitzZeta`). VERIFIER target #MB-3:
    pin the exact import and name. -/
theorem hurwitz_zeta_available : True := trivial  -- WRAP target

/-- The decomposition `L(s, χ) = q^{-s} ∑_{r=1}^{q-1} χ(r) ζ(s, r/q)`.
    This is the bridge needed to give the Davenport-Heilbronn L-function
    a meromorphic continuation in Lean. TODO; VERIFIER target #MB-4. -/
theorem L_function_hurwitz_decomposition : True := by
  -- ∀ q ≥ 1, ∀ χ : DirichletCharacter ℂ q, ∀ s : ℂ, 1 < s.re →
  --   LFunction χ s = (q : ℂ)^(-s) * ∑ r in Finset.Ioo 0 q, χ r * hurwitzZeta s (r / q)
  sorry  -- WRAP target

/-! ### Fejér's classical inequality (for line-restriction lemma). -/

/-- Fejér 1915: any non-negative trig polynomial of degree N normalised by
    constant term 1 has `c_1 ≤ cos(π / (N + 2))`.

    TODO: not currently in Mathlib in this exact form. VERIFIER target
    #MB-5: prove this as a Mathlib upstream candidate, or reduce to
    existing positivity-of-trig-polynomial lemmas. -/
theorem fejer_classical : True := by sorry  -- WRAP target

/-! ### Functional equation for ζ. -/

/-- The functional equation of the completed zeta function:
    `Λ(1 - s) = Λ(s)` where `Λ = completedRiemannZeta`. PRESENT in Mathlib as
    `completedRiemannZeta_one_sub`. VERIFIER target #MB-6 DISCHARGED (no sorry). -/
theorem zeta_functional_equation (s : ℂ) :
    completedRiemannZeta (1 - s) = completedRiemannZeta s :=
  completedRiemannZeta_one_sub s

/-! ### Selberg class scaffolding (TODO).

    None of the following is in Mathlib as of 2026-05:

      - The Selberg class as a `Type`.
      - Membership predicate.
      - Degree of a Selberg-class L-function.
      - Conjectures about Selberg-class structure (multiplicativity, primitivity).

    These are all SYNTHESIZER targets for upstream contribution after the
    project-local definitions stabilise. -/

end ZetaRH.MathlibBridge
