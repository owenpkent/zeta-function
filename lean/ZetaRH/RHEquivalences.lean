/-
RH equivalence hub: the classical number-theoretic reformulations of the
Riemann Hypothesis, plus the Π⁰₁ arithmetic kernel witness.

## What this module is

Entry point A of the "RH logical status" excursion
(`docs/03_research/rh_logical_status.md` §7). It collects the equivalent
reformulations of RH that live in elementary / analytic number theory, as Lean
`Prop`s over the project's `zeta : LFunction`, each with an `iff`-to-`RiemannHypothesis`
theorem and a fresh VERIFIER target ID. The point is to make the LOGICAL
landscape legible the way `HodgeIndex.lean` makes the geometric landscape legible.

This is deliberately DISTINCT from `ExplicitFormula.lean`: that module owns the
Weil explicit-formula quadratic-form positivity criterion (#EF-2), the
Architecture-3 analytic face. This module owns the elementary/criterion faces
(Robin, Lagarias, Mertens, Li/Keiper, Nyman-Beurling) and the single object the
whole excursion is about: the Π⁰₁ arithmetic surrogate `RH_arith`.

## Status (2026-06-04)

The CONCRETE reformulations are fully wired against Mathlib:
  - `robinInequality`   uses `ArithmeticFunction.sigma 1` (σ) and `Real.eulerMascheroniConstant`.
  - `lagariasInequality` uses σ and Mathlib's `harmonic : ℕ → ℚ`.
  - `mertensBound`       uses `ArithmeticFunction.moebius` (μ).
The Li/Keiper and Nyman-Beurling criteria bundle the analytic data Mathlib does
not yet provide (sum-over-zeros theory, the L²(0,1) closure), mirroring how
`ExplicitFormula.WeilExplicitFormula` bundles its functionals.

PROVED (no sorry): the definitional reformulation, the Mathlib-bridge re-export,
and `lagarias_holds_at_one` (the n = 1 equality case, which is exactly why
Lagarias's criterion must use ≤ and not strict <). The deep equivalences
(Robin/Lagarias/Mertens/Li/Nyman-Beurling ⟺ RH) are documented `sorry`s; each is
a full RH-equivalence theorem, unformalized in any prover.

## The decidability caveat (matches the math)

`lagariasInequalityAt n` is a comparison of REAL numbers, so it is NOT
`Decidable` in Lean's typeclass sense. This is faithful to the mathematics: the
Π⁰₁ matrix is "decidable" only via effective approximation (σ and the harmonic
number are computable, the constants are computable reals, and the comparison is
strict for n ≥ 2 / equality only at n = 1), not as a literal decidable predicate
on `ℝ`. See `docs/03_research/rh_logical_status.md` §1.

No em dashes anywhere in this file (project style rule).
-/

import Mathlib.NumberTheory.ArithmeticFunction
import Mathlib.NumberTheory.Harmonic.Defs
import Mathlib.NumberTheory.Harmonic.EulerMascheroni
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Data.Complex.ExponentialBounds
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import ZetaRH.Basic

namespace ZetaRH.RHEquivalences

open scoped ArithmeticFunction

/-! ### Robin's criterion (Robin 1984).

    RH ⟺ for all n ≥ 5041, σ(n) < e^γ · n · log log n, where σ = sum of divisors
    and γ is the Euler-Mascheroni constant. The threshold 5041 carries a finite
    known exception set (the 27 numbers up to 5040); it does not affect the Π⁰₁
    complexity class, only the truth value. -/

/-- The per-n Robin inequality `σ(n) < e^γ · n · log log n`. Concrete: `σ 1 n` is
    Mathlib's sum-of-divisors arithmetic function, `Real.eulerMascheroniConstant`
    is γ. -/
noncomputable def robinInequalityAt (n : ℕ) : Prop :=
  (σ 1 n : ℝ) < Real.exp Real.eulerMascheroniConstant * (n : ℝ) * Real.log (Real.log (n : ℝ))

/-- **Robin's criterion** as a `Prop`: the inequality holds for every n ≥ 5041. -/
def robinInequality : Prop := ∀ n : ℕ, 5041 ≤ n → robinInequalityAt n

/-! ### Lagarias's criterion (Lagarias 2002).

    RH ⟺ for all n ≥ 1, σ(n) ≤ H_n + exp(H_n) · log(H_n), where H_n is the n-th
    harmonic number. LOAD-BEARING: the inequality is `≤`, with equality at n = 1
    (`lagarias_holds_at_one`). A strict `<` would make the n = 1 check FALSE and
    break the formalization. -/

/-- The per-n Lagarias inequality `σ(n) ≤ H_n + exp(H_n) · log(H_n)`. Concrete:
    `harmonic n : ℚ` is Mathlib's harmonic number, cast to `ℝ`. -/
noncomputable def lagariasInequalityAt (n : ℕ) : Prop :=
  (σ 1 n : ℝ) ≤ (harmonic n : ℝ) + Real.exp (harmonic n : ℝ) * Real.log (harmonic n : ℝ)

/-- **Lagarias's criterion** as a `Prop`: the inequality holds for every n ≥ 1. -/
def lagariasInequality : Prop := ∀ n : ℕ, 1 ≤ n → lagariasInequalityAt n

/-! ### Mertens-function bound.

    RH ⟺ M(x) = O(x^{1/2 + ε}) for every ε > 0, where M(x) = ∑_{n ≤ x} μ(n) is the
    Mertens function and μ is the Möbius function. -/

/-- The Mertens function `M(x) = ∑_{n=1}^{x} μ(n)`, using Mathlib's
    `ArithmeticFunction.moebius` (μ). -/
noncomputable def mertens (x : ℕ) : ℤ := ∑ n ∈ Finset.Icc 1 x, μ n

/-- **The Mertens bound** as a `Prop`: `|M(x)| ≤ C · x^{1/2 + ε}` for every ε > 0
    (with a constant C depending on ε). The exponent uses `Real.rpow`. -/
def mertensBound : Prop :=
  ∀ ε : ℝ, 0 < ε → ∃ C : ℝ, ∀ x : ℕ, |(mertens x : ℝ)| ≤ C * (x : ℝ) ^ ((1 : ℝ) / 2 + ε)

/-! ### Li / Keiper coefficients (Li 1997, Keiper 1992, Bombieri-Lagarias 1999).

    RH ⟺ λ_n ≥ 0 for all n ≥ 1, where the Li coefficients have the Keiper-Li
    sum-over-zeros representation `λ_n = ∑_ρ [1 - (1 - 1/ρ)^n]` over the
    non-trivial zeros ρ of ζ. Mathlib has no sum-over-zeros theory, so we bundle
    the sequence together with its defining representation (mirroring
    `ExplicitFormula.WeilExplicitFormula`). The convergent symmetric-pairing form
    is the deep content (#LI-def). -/

/-- Li / Keiper data: a coefficient sequence together with its Keiper-Li
    representation against the non-trivial zeros of ζ. The representation field
    ties `lambda` to the zeros, so the criterion below is not vacuous; the
    precise convergence (symmetric ρ ↔ 1-ρ pairing) is target #LI-def. -/
structure LiData where
  /-- The Li / Keiper coefficient sequence. -/
  lambda : ℕ → ℝ
  /-- Keiper-Li representation `λ_n = ∑_ρ [1 - (1 - 1/ρ)^n]` over the non-trivial
      zeros of ζ (stated in ℂ via the real-to-complex cast of `lambda`). -/
  keiperLi : ∀ n : ℕ, 1 ≤ n →
    (lambda n : ℂ) = ∑' ρ : ↥(nonTrivialZeros zeta), (1 - (1 - 1 / (ρ : ℂ)) ^ n)

/-- **Li's positivity criterion** (VERIFIER target #LI-1): for the Keiper-Li
    coefficients of ζ, non-negativity of every λ_n is equivalent to RH. -/
theorem li_criterion (L : LiData) :
    (∀ n : ℕ, 1 ≤ n → 0 ≤ L.lambda n) ↔ RiemannHypothesis zeta := by
  sorry  -- #LI-1

/-! ### Nyman-Beurling / Báez-Duarte criterion.

    RH ⟺ the L²(0,1) distance from the indicator of (0,1] to the span of dilated
    fractional parts {ρ_θ(x) = {θ/x}} tends to 0 (Báez-Duarte form: the
    approximation distances d_N → 0). Mathlib's L²-closure machinery is not wired
    here, so we bundle the distance sequence with its true nonnegativity and
    antitonicity; the tie to the actual L²(0,1) approximation is target #NB-def. -/

/-- Nyman-Beurling-Báez-Duarte data: the approximation-distance sequence `dist N`
    (the L²(0,1) distance using dilations by 1, …, N), carried as opaque data with
    its genuine properties (nonnegative, antitone). The tie to the actual L²(0,1)
    closure is target #NB-def. -/
structure NymanBeurlingData where
  /-- The Báez-Duarte approximation distances `d_N ≥ 0`. -/
  dist : ℕ → ℝ
  /-- Distances are nonnegative. -/
  dist_nonneg : ∀ N, 0 ≤ dist N
  /-- Distances are antitone in N (more dilations cannot increase the distance). -/
  dist_antitone : Antitone dist

/-- **The Nyman-Beurling criterion** (VERIFIER target #NB-1): the approximation
    distances tend to 0 iff RH holds for ζ. -/
theorem nymanBeurling_criterion (NB : NymanBeurlingData) :
    Filter.Tendsto NB.dist Filter.atTop (nhds (0 : ℝ)) ↔ RiemannHypothesis zeta := by
  sorry  -- #NB-1

/-! ### The deep elementary equivalences (documented sorries). -/

/-- **Robin's criterion ⟺ RH** (VERIFIER target #RB-1). -/
theorem robin_criterion : robinInequality ↔ RiemannHypothesis zeta := by
  sorry  -- #RB-1

/-- **Lagarias's criterion ⟺ RH** (VERIFIER target #LG-1). -/
theorem lagarias_criterion : lagariasInequality ↔ RiemannHypothesis zeta := by
  sorry  -- #LG-1

/-- **The Mertens bound ⟺ RH** (VERIFIER target #MT-1). -/
theorem mertens_criterion : mertensBound ↔ RiemannHypothesis zeta := by
  sorry  -- #MT-1

/-! ### The Π⁰₁ arithmetic kernel witness.

    This is the object the whole "RH logical status" excursion is about: a single
    universal quantifier over ℕ with a (effectively) decidable matrix. We take the
    Lagarias predicate as the practical primitive-recursive surrogate (Mathlib's
    Hilbert-10 / DPRM coverage is partial, so the single-polynomial Diophantine
    form is out of reach). `RH_arith` turns the prose claim "RH is Π⁰₁, so a false
    RH is finitely refutable" into a formal object: its negation is a Σ⁰₁
    existence of a single refuting n. -/

/-- **The Π⁰₁ arithmetic surrogate of RH**: `∀ n, lagariasInequalityAt n` (for
    n ≥ 1). Definitionally the Lagarias criterion; named separately because it is
    the canonical `Π⁰₁` witness whose refutability is the content of
    `docs/03_research/rh_logical_status.md` §1-§2. -/
def RH_arith : Prop := lagariasInequality

/-- `RH_arith ↔ RiemannHypothesis zeta`. Reuses #LG-1 (no new sorry):
    `RH_arith` is definitionally `lagariasInequality`. -/
theorem RH_arith_iff_RiemannHypothesis : RH_arith ↔ RiemannHypothesis zeta :=
  lagarias_criterion

/-! ### Proved-now content (no sorry).

    The definitional reformulation, the Mathlib-bridge re-export, and the n = 1
    equality case of Lagarias. These are the green anchors of the scaffold. -/

/-- RH for ζ is definitionally "every non-trivial zero has real part 1/2". -/
theorem riemannHypothesis_zeta_iff_nonTrivialZeros :
    RiemannHypothesis zeta ↔ ∀ ρ ∈ nonTrivialZeros zeta, ρ.re = 1 / 2 :=
  Iff.rfl

/-- Re-export of the Mathlib-native bridge from `Basic.lean`. -/
theorem riemannHypothesisMathlib_iff_zeta :
    RiemannHypothesisMathlib ↔ RiemannHypothesis zeta :=
  RiemannHypothesisMathlib_iff_RiemannHypothesis_zeta

/-- **The n = 1 equality case of Lagarias** (no sorry): `σ(1) = 1`, `H_1 = 1`, and
    `1 ≤ 1 + e^1 · log 1 = 1`. This is exactly why the criterion uses `≤`, not
    strict `<`: at n = 1 the two sides are equal. -/
theorem lagarias_holds_at_one : lagariasInequalityAt 1 := by
  have hσn : σ 1 1 = 1 := by simp [ArithmeticFunction.sigma_one_apply]
  have hσ : (σ 1 1 : ℝ) = 1 := by rw [hσn]; norm_num
  have hHq : harmonic 1 = 1 := by simp [harmonic, Finset.sum_range_one]
  have hH : (harmonic 1 : ℝ) = 1 := by rw [hHq]; norm_num
  unfold lagariasInequalityAt
  rw [hσ, hH, Real.log_one, mul_zero, add_zero]

/-- **A worked n = 3 instance of Lagarias** (no sorry): `σ(3) = 4 ≤ 11/6 + e^{11/6}·log(11/6) ≈ 4.08`.

    This is the first instance with n > 1, where the right-hand side is genuinely
    transcendental. It is proved by EFFECTIVE BOUNDS on the constants, concretely
    witnessing the §1 claim that the Π⁰₁ matrix is decidable by effective
    approximation (not as a literal `Decidable` real predicate):
      `e^{11/6} = e · e^{5/6} ≥ e · (11/6) ≥ 2.7 · (11/6)` (from `add_one_le_exp`
      applied to 5/6, and `exp_one_gt_d9`), and
      `log(11/6) ≥ 5/11` (from `log_le_sub_one_of_pos` applied to 6/11, via `log_inv`).
    The product bound gives RHS ≥ 11/6 + 2.25 = 49/12 ≈ 4.083 ≥ 4. Margin ≈ 0.08. -/
theorem lagarias_holds_at_three : lagariasInequalityAt 3 := by
  have hσ : (σ 1 3 : ℝ) = 4 := by
    have h : σ 1 3 = 4 := by rw [ArithmeticFunction.sigma_one_apply]; decide
    rw [h]; norm_num
  have hH : (harmonic 3 : ℝ) = 11 / 6 := by
    have h : harmonic 3 = 11 / 6 := by
      simp only [harmonic, Finset.sum_range_succ, Finset.sum_range_zero]; norm_num
    rw [h]; norm_num
  unfold lagariasInequalityAt
  rw [hσ, hH]
  -- goal: (4 : ℝ) ≤ 11/6 + Real.exp (11/6) * Real.log (11/6)
  -- (rationals, not decimals: linarith does not recognise `OfScientific` numerals)
  have he : (27 / 10 : ℝ) ≤ Real.exp 1 :=
    le_of_lt (lt_of_le_of_lt (by norm_num) Real.exp_one_gt_d9)
  have hexp56 : (11 / 6 : ℝ) ≤ Real.exp (5 / 6) := by
    have h := Real.add_one_le_exp (5 / 6 : ℝ); linarith
  have hexp_split : Real.exp (11 / 6 : ℝ) = Real.exp 1 * Real.exp (5 / 6) := by
    rw [show (11 / 6 : ℝ) = 1 + 5 / 6 by norm_num, Real.exp_add]
  have h1pos : (0 : ℝ) < Real.exp 1 := Real.exp_pos 1
  have hexp : (27 / 10 : ℝ) * (11 / 6) ≤ Real.exp (11 / 6) := by
    rw [hexp_split]
    have step1 : (27 / 10 : ℝ) * (11 / 6) ≤ Real.exp 1 * (11 / 6) :=
      mul_le_mul_of_nonneg_right he (by norm_num)
    have step2 : Real.exp 1 * (11 / 6 : ℝ) ≤ Real.exp 1 * Real.exp (5 / 6) :=
      mul_le_mul_of_nonneg_left hexp56 (le_of_lt h1pos)
    linarith
  have hlog : (5 / 11 : ℝ) ≤ Real.log (11 / 6) := by
    have hk : Real.log (6 / 11 : ℝ) ≤ (6 / 11 : ℝ) - 1 := Real.log_le_sub_one_of_pos (by norm_num)
    have hinv : Real.log (11 / 6 : ℝ) = - Real.log (6 / 11 : ℝ) := by
      rw [show (11 / 6 : ℝ) = (6 / 11 : ℝ)⁻¹ by norm_num, Real.log_inv]
    rw [hinv]; linarith
  have hprod : (27 / 10 * (11 / 6)) * (5 / 11) ≤ Real.exp (11 / 6) * Real.log (11 / 6) :=
    mul_le_mul hexp hlog (by norm_num) (le_of_lt (Real.exp_pos _))
  have hval : (27 / 10 * (11 / 6 : ℝ)) * (5 / 11) = 9 / 4 := by norm_num
  linarith [hprod, hval]

/-! ### Refutability and the computable matrix (entry point B).

    The formal content of `docs/03_research/rh_logical_status.md` §2: because
    `RH_arith` is `∀ n, …`, its negation is a Σ⁰₁ existence of a single refuting
    n. `rh_arith_refutable` makes "a false RH has one finite counterexample"
    a theorem (no sorry). The σ computations below witness that the arithmetic
    half of the matrix (the sum-of-divisors side) is concretely COMPUTABLE in
    Lean, which is the "effective approximability" half of why the matrix is
    decidable, even though the full real-number predicate `lagariasInequalityAt`
    is not Lean-`Decidable`. -/

/-- **The Σ⁰₁ refutability structure** (no sorry): `RH_arith` fails iff there is a
    single n ≥ 1 violating the Lagarias inequality. This is the formal statement
    that a false Π⁰₁ RH is refutable by one finite witness (the dual in §2:
    "false but not refutable" is impossible). -/
theorem rh_arith_refutable :
    ¬ RH_arith ↔ ∃ n : ℕ, 1 ≤ n ∧ ¬ lagariasInequalityAt n := by
  unfold RH_arith lagariasInequality
  constructor
  · intro h
    by_contra hc
    push_neg at hc
    exact h hc
  · rintro ⟨n, hn, hcontra⟩ h
    exact hcontra (h n hn)

/-- `σ(6) = 12` (6 is perfect: the proper divisors 1, 2, 3 sum to 6, so the full
    divisor sum is 12). A sorry-free witness that the σ side of the matrix is
    kernel-computable. -/
theorem sigma_one_six : σ 1 6 = 12 := by
  rw [ArithmeticFunction.sigma_one_apply]; decide

/-- `σ(12) = 28` (divisors 1, 2, 3, 4, 6, 12). A non-perfect-number witness that
    the σ computation is not special to perfect numbers. -/
theorem sigma_one_twelve : σ 1 12 = 28 := by
  rw [ArithmeticFunction.sigma_one_apply]; decide

/-! ### De-smuggling check (mirrors `AccidentAudit.lean`).

    The proved anchors depend only on the foundational axioms (no `sorryAx`); the
    criterion theorems carry `sorryAx`. The verbatim output is recorded in the
    VERIFIER report. -/

#print axioms riemannHypothesis_zeta_iff_nonTrivialZeros
#print axioms lagarias_holds_at_one
#print axioms rh_arith_refutable
#print axioms sigma_one_six
#print axioms lagarias_holds_at_three

end ZetaRH.RHEquivalences
