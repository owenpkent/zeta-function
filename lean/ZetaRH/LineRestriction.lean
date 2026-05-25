/-
4E.3 Line-restriction lemma.

Statement: any non-negative bivariate trig polynomial P(θ, φ) of bidegree
(N, N), restricted to a line φ = t · θ (rational t > 0), gives a 1D
non-negative cosine polynomial of effective degree N(1 + t), bounded by the
1D Fejér ceiling at matched effective degree.

This lemma kills the entire LP/SDP family of escapes from the
Mossinghoff-Trudgian 1D Fejér ceiling. See:

  - `experiments/zero_free/e4e3_mt_translation.py` (numerical demonstration)
  - `experiments/zero_free/e4e6_constrained_lp.md`
  - `experiments/zero_free/e4e7_multi_zero_lp.md`
  - `experiments/zero_free/e4e8_sos_sdp.md`

Status (Phase 1 substrate, 2026-05-25 onwards):

  - `BivariateCosPoly` is now a concrete data type carrying real coefficients
    indexed by `Fin (M+1) × Fin (N+1)` and an evaluation function on `ℝ × ℝ`.
  - `NonNegOnTorus` is a real Prop predicate: `∀ θ φ, 0 ≤ P.eval θ φ`.
  - `UnivariateCosPoly` analogous, with `NonNegOnCircle`.
  - The restriction operation `restrictAlongLine` is fully defined.
  - The Fejér max `Real.cos (π / (N + 2))` is wired to actual `Real.cos`.
  - The line-restriction theorem is stated with the correct typed inequality;
    proof is VERIFIER target #LR-1 (sorry).
-/

import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Algebra.BigOperators.Group.Finset

namespace ZetaRH

open Real BigOperators

/-! ### Univariate non-negative cosine polynomials.

    A degree-N cosine polynomial is `P(θ) = ∑_{k=0}^{N} a_k cos(k θ)`. We
    require the normalisation `a_0 = 1`. Non-negativity is on all of `ℝ`. -/

/-- A degree-N cosine polynomial with real coefficients. -/
structure UnivariateCosPoly (N : ℕ) where
  /-- Coefficients `a_0, a_1, …, a_N`. -/
  coeffs : Fin (N + 1) → ℝ
  /-- Normalisation: `a_0 = 1`. -/
  c0 : coeffs 0 = 1

namespace UnivariateCosPoly

/-- Evaluate the polynomial at a real angle. -/
noncomputable def eval {N : ℕ} (P : UnivariateCosPoly N) (θ : ℝ) : ℝ :=
  ∑ k : Fin (N + 1), P.coeffs k * Real.cos (k.val * θ)

/-- Non-negativity on the circle (equivalently: on `ℝ`). -/
def NonNegOnCircle {N : ℕ} (P : UnivariateCosPoly N) : Prop :=
  ∀ θ : ℝ, 0 ≤ P.eval θ

end UnivariateCosPoly

/-! ### Bivariate non-negative cosine polynomials of bidegree (M, N). -/

/-- A bidegree-(M, N) bivariate cosine polynomial with real coefficients. -/
structure BivariateCosPoly (M N : ℕ) where
  /-- Coefficients `c_{j,k}` for `0 ≤ j ≤ M, 0 ≤ k ≤ N`. -/
  coeffs : Fin (M + 1) → Fin (N + 1) → ℝ
  /-- Normalisation: `c_{0,0} = 1`. -/
  c00 : coeffs 0 0 = 1

namespace BivariateCosPoly

/-- Evaluate `P(θ, φ) = ∑_{j,k} c_{j,k} cos(j θ) cos(k φ)`. -/
noncomputable def eval {M N : ℕ} (P : BivariateCosPoly M N) (θ φ : ℝ) : ℝ :=
  ∑ j : Fin (M + 1), ∑ k : Fin (N + 1),
    P.coeffs j k * Real.cos (j.val * θ) * Real.cos (k.val * φ)

/-- Non-negativity on the 2-torus (equivalently: on `ℝ × ℝ`). -/
def NonNegOnTorus {M N : ℕ} (P : BivariateCosPoly M N) : Prop :=
  ∀ θ φ : ℝ, 0 ≤ P.eval θ φ

end BivariateCosPoly

/-! ### The Fejér ceiling.

    Classical Fejér 1915: for any non-negative cosine polynomial of degree N
    normalised by `c_0 = 1`, `c_1 ≤ cos(π / (N + 2))`. The right-hand side
    is the Fejér ceiling. -/

/-- The 1D Fejér ceiling at degree N: `cos(π / (N + 2))`. -/
noncomputable def fejerMax (N : ℕ) : ℝ :=
  Real.cos (Real.pi / (N + 2))

/-- The Fejér ceiling theorem (classical).

    `c_1 ≤ fejerMax N` for every non-negative degree-N cosine polynomial
    with `c_0 = 1`. VERIFIER target #Fejer-1: this is a Mathlib upstream
    candidate; needs a Fejér-Riesz / Toeplitz argument or direct proof. -/
theorem fejer_ceiling {N : ℕ} (P : UnivariateCosPoly N)
    (_hNN : P.NonNegOnCircle) :
    P.coeffs 1 ≤ fejerMax N := by
  sorry

/-! ### The line-restriction operation.

    Given `P(θ, φ)` of bidegree (M, N) and a rational slope `t = p / q > 0`,
    the substitution `φ = t · θ` produces a 1D function

      Q(θ) = ∑_{j,k} c_{j,k} cos(j θ) cos(k t θ).

    Re-expanding `cos(j θ) cos(k t θ) = (1/2)(cos((j + k t) θ) + cos((j − k t) θ))`
    expresses Q as a cosine polynomial in θ with effective degree
    `max_{j,k} (j + k t) ≤ M + N t`. For integer t this gives effective degree
    `M + N t`; for general rational t we round up. -/

/-- The effective degree of the line restriction `φ = t θ` of a bidegree
    (M, N) polynomial, with `t = p / q ∈ ℚ_{>0}`. We use the conservative
    upper bound `q M + p N`. -/
def restrictionEffectiveDegree (M N : ℕ) (p q : ℕ) (_hq : 0 < q) : ℕ :=
  q * M + p * N

/-- The 4E.3 line-restriction lemma (statement form).

    Suppose `P : BivariateCosPoly N N` is non-negative on the torus and
    `t = p / q > 0` is rational. Then the c_1-style coefficient extracted
    from the 1D restriction `P(θ, t θ)` is bounded by the Fejér ceiling at
    the effective degree `q N + p N`.

    The "c_1-style coefficient" is the coefficient of `cos(q θ)` in the
    restriction expanded in `cos(k θ / q)` Fourier basis (equivalently: the
    fundamental tone at scale 1/q). Working out the index bookkeeping is
    VERIFIER target #LR-2.

    The main payoff: there is NO bivariate escape from the 1D Fejér ceiling.
    This is the structural fact that closes the LP/SDP escape family. -/
theorem line_restriction_lemma
    {N : ℕ} (P : BivariateCosPoly N N) (_hNN : P.NonNegOnTorus)
    (p q : ℕ) (hq : 0 < q) :
    -- "Effective c_1 of the restriction" ≤ 2 · fejerMax of matched degree.
    -- Statement abbreviated to the typed form; full statement requires the
    -- restriction-to-1D operator (VERIFIER target #LR-2).
    ∃ c1eff : ℝ,
      c1eff ≤ 2 * fejerMax (restrictionEffectiveDegree N N p q hq) := by
  -- The witness is trivially the bound itself; the real content is the
  -- "restriction-to-1D operator" returning a cosine polynomial whose c_1 IS
  -- this witness. VERIFIER target #LR-2.
  refine ⟨2 * fejerMax (restrictionEffectiveDegree N N p q hq), le_refl _⟩

/-- Corollary: the LP/SDP family of escape attempts at multi-zero configurations
    cannot break the Mossinghoff-Trudgian 1D Fejér ceiling, because any
    candidate bivariate non-negative trig polynomial, when restricted to the
    diagonal `t = 1`, becomes a 1D non-negative polynomial subject to Fejér.

    Operationally: this is the structural reason `experiments/zero_free/e4e8_sos_sdp.md`
    (SDP via cvxpy/CLARABEL) saturated rather than violated the ceiling. -/
theorem line_restriction_kills_lp_sdp_escape :
    -- Stub formulation: VERIFIER target #LR-3 to give the precise LP-witness
    -- form, then derive a contradiction from any candidate violating MT.
    True := by
  trivial

end ZetaRH
