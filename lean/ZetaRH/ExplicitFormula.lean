/-
Weil's explicit formula and the Weil positivity criterion.

This module is the highest-leverage Mathlib target identified by the project
(LEARNINGS #17): the Weil explicit formula relating a sum over the non-trivial
zeros of ζ to a sum over prime powers plus an archimedean term and the pole
contribution, and the Weil positivity criterion `RH ⟺ the Weil quadratic form
is positive`. Architecture 3 (positivity) lives here; the experimental thread's
3F/3M decomposition `M = A_arch + P_fin + B_pole` is exactly the place-type
decomposition of the RHS below.

Status (2026-05-29). Mathlib v4.13.0 has `riemannZeta`, its functional equation
(`completedRiemannZeta`, `riemannZeta_one_sub`), the pole residue
(`riemannZeta_residue_one`), and the von Mangoldt function
(`ArithmeticFunction.vonMangoldt`, notation `Λ`). It does NOT have: the explicit
formula itself, the digamma / Γ-factor logarithmic derivative as the archimedean
kernel, or any sum-over-zeros infrastructure. So this module ships a faithful
TYPED SCAFFOLD:

  - `primeSum` is CONCRETE (a `tsum` against `Λ`), the one side Mathlib supports.
  - the zero side, archimedean term, and pole term are bundled into
    `WeilExplicitFormula` as data; the explicit formula is the assertion that
    such a bundle exists for ζ (`weil_explicit_formula_zeta`, target #EF-1).
  - the Weil positivity criterion is stated against `RiemannHypothesis zeta`
    (`weil_positivity_criterion`, target #EF-2).

The statements typecheck and the build is green; the content is the documented
`sorry` set (#EF-1, #EF-2, #EF-arch). This is the Architecture-3 face of the same
positivity whose Architecture-2 (signature) face is in `HodgeIndex.lean`.
-/

import Mathlib.NumberTheory.LSeries.RiemannZeta
import Mathlib.NumberTheory.VonMangoldt
import ZetaRH.Basic

namespace ZetaRH.ExplicitFormula

open Complex
open scoped ArithmeticFunction

/-! ### The admissible test-function class.

    Weil's formula holds for an even test function `g` on `ℝ` (the "additive" /
    log variable) that is smooth with sufficient decay, equivalently a function
    `h = ĝ` holomorphic in a horizontal strip. We carry only the data and the
    evenness here; the analytic side-conditions (smoothness, decay, the strip of
    holomorphy of the transform) are VERIFIER target #EF-class and are what make
    the three analytic functionals below well-defined and the identity true. -/

/-- An admissible test function for the explicit formula: an even `g : ℝ → ℂ`.
    Analytic side-conditions (decay / holomorphy of the transform) are elided and
    tracked as #EF-class. -/
structure AdmissibleTest where
  /-- The test function on the additive (log) variable. -/
  g : ℝ → ℂ
  /-- Evenness: `g(-x) = g(x)`. The explicit formula pairs `n` and `1/n`. -/
  even' : ∀ x : ℝ, g (-x) = g x

/-! ### The prime side (concrete).

    The one functional Mathlib fully supports. Up to the symmetrisation supplied
    by `even'`, this is `2 ∑_{n} Λ(n) n^{-1/2} g(log n)`, i.e. `∑_{p,k} (log p)
    p^{-k/2} (g(k log p) + g(-k log p))` after expanding `Λ` on prime powers. This
    is the `P_fin` block of the experimental 3M decomposition. -/

/-- The prime side of the explicit formula, `∑_n Λ(n) n^{-1/2} (g(log n) +
    g(-log n))`, as a `tsum` over `ℕ`. `Λ 0 = Λ 1 = 0`, so the `n = 0, 1` terms
    vanish; on prime powers `n = p^k`, `Λ(p^k) = log p`. Concrete (no `sorry`). -/
noncomputable def primeSum (T : AdmissibleTest) : ℂ :=
  ∑' n : ℕ,
    Complex.ofReal (Λ n) / Complex.ofReal (Real.sqrt (n : ℝ))
      * (T.g (Real.log (n : ℝ)) + T.g (-(Real.log (n : ℝ))))

/-! ### The explicit formula as a bundle of functionals.

    The zero side, archimedean term, and pole term are the analytic functionals
    Mathlib does not yet provide. We bundle them with the identity that ties them
    to the concrete `primeSum`. The explicit formula (target #EF-1) is then the
    assertion that such a bundle exists for ζ. -/

/-- Weil's explicit formula for ζ, packaged as data: the three analytic
    functionals plus the identity relating them to the concrete `primeSum`.

      `zeroSum T`  : `∑_ρ ĝ(ρ)` over the non-trivial zeros (`H¹`, the spectral side).
      `archTerm T` : the archimedean integral `(1/2π) ∫ ĝ · (Γ-factor log-deriv)`
                     (the `A_arch` block; needs digamma, target #EF-arch).
      `poleTerm T` : the contribution of the pole of ζ at `s = 1` (the `B_pole`
                     block, the hyperbolic direction in the 2K dictionary).

    `identity` is the explicit formula: spectral side = archimedean + pole − prime. -/
structure WeilExplicitFormula where
  /-- The sum over non-trivial zeros (spectral side). -/
  zeroSum : AdmissibleTest → ℂ
  /-- The archimedean term (Γ-factor logarithmic derivative). -/
  archTerm : AdmissibleTest → ℂ
  /-- The pole-at-`s = 1` contribution (the hyperbolic block). -/
  poleTerm : AdmissibleTest → ℂ
  /-- Weil's explicit formula: `∑_ρ ĝ(ρ) = arch + pole − prime`. -/
  identity : ∀ T : AdmissibleTest, zeroSum T = archTerm T + poleTerm T - primeSum T

/-- **The Weil explicit formula for ζ** (VERIFIER target #EF-1).

    Existence of a `WeilExplicitFormula` bundle for the Riemann zeta function:
    the spectral side equals the archimedean term plus the pole term minus the
    (concrete) prime side. This is the classical Riemann-Weil-Guinand explicit
    formula. Proving it in Lean requires (a) the digamma archimedean kernel
    (#EF-arch), (b) a sum-over-zeros convergence theory, and (c) the contour-shift
    argument; none is in Mathlib v4.13.0. -/
theorem weil_explicit_formula_zeta : Nonempty WeilExplicitFormula := by
  sorry  -- #EF-1

/-! ### The Weil positivity criterion (the high-leverage object).

    Applying the explicit formula to a test function of positive type `f ⋆ f̃`
    turns the spectral side into a Hermitian quadratic form `W(f) = ∑_ρ f̂(ρ)
    \overline{f̂(\bar ρ)}`. Weil's criterion: RH for ζ ⟺ `W(f) ≥ 0` for every
    admissible `f`. By the explicit formula `W` equals the (computable)
    `arch + pole − prime` side, which is the content the experimental 3M/3F
    decomposition exhibits numerically. -/

/-- The Weil quadratic form built from an explicit-formula bundle: the
    real-valued Hermitian functional `W(f) = ∑_ρ f̂(ρ) \overline{f̂(\bar ρ)}`,
    obtained by applying `zeroSum` to the positive-type test associated to `f`.
    Its construction from `W` is target #EF-2a (needs the positive-type/self-dual
    test construction). -/
noncomputable def weilForm (_W : WeilExplicitFormula) (_T : AdmissibleTest) : ℝ := by
  sorry  -- #EF-2a

/-- **Weil's positivity criterion** (VERIFIER target #EF-2).

    For ζ, the positivity of the Weil quadratic form on every admissible test
    function is equivalent to the Riemann Hypothesis. This is the Architecture-3
    centerpiece and the project's primary positivity reformulation; its
    Architecture-2 (signature) counterpart is `HodgeIndex.negDef_iff_hasseWeil`.
    The forward direction is the explicit-formula computation; the reverse is the
    standard Weil argument (a single off-line zero produces a test function with
    `W(f) < 0`). -/
theorem weil_positivity_criterion (W : WeilExplicitFormula) :
    (∀ T : AdmissibleTest, 0 ≤ weilForm W T) ↔ RiemannHypothesis zeta := by
  sorry  -- #EF-2

/-! ### K2 / Davenport-Heilbronn discipline.

    The criterion above must NOT certify RH for Davenport-Heilbronn, which has a
    functional equation but no Euler product and known off-line zeros. The
    structural reason, in the language of this module: D-H's analogue of
    `primeSum` is built from a von Mangoldt function that DELOCALISES off prime
    powers (no Euler product ⇒ `Λ_DH` is supported on composites; experiment 3M
    finding #20). So the `arch + pole − prime` side is not a positive-type form in
    the same way, and the `weilForm`-positivity ⟺ RH equivalence FAILS to hold for
    D-H. Stating this faithfully needs the D-H explicit formula (a D-H instance of
    `WeilExplicitFormula`) and is tracked as #EF-K2; the experimental side is in
    `experiments/positivity/e3m_place_type_balance.md` and the D-H control in
    `experiments/_shared/davenport_heilbronn.py`. -/

end ZetaRH.ExplicitFormula
