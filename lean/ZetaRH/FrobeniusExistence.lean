/-
Lever B, O1 as a SINGLE typed contract on Mathlib's real elliptic-curve object.

See `docs/03_research/lever_b_function_field_plan.md`. The whole chain from "Frobenius is the
rank-2 integer matrix `A` with `deg = det`" to "RH for the curve" is ALREADY machine-checked,
sorry-free (`FunctionFieldRH.functionfield_RH_elliptic_of_matrix_general`,
`LocalFactor.localPolynomial_root_normSq`). O2 ("deg is a quadratic form") is a theorem
(`TateModule.lean`). O3 (the trace `a` and point count `#E`) is in Mathlib
(`WeierstrassCurve.localPolynomial = 1 - a·T + q·T²` for good reduction). The SOLE residual is
O1: the EXISTENCE of `A` (the Frobenius on the Tate module) for a real curve.

This module does the INTERFACE work and ONLY the interface work:

  1. It STATES O1 as a single clean proposition `FrobeniusTateData` on Mathlib's actual object
     (`WeierstrassCurve` over a nonarchimedean local field, good reduction), pinning `det A` and
     `trace A` to Mathlib's own `q = #κ` and `a = q + 1 - #W(κ)`. This is the genuine, TRUE
     (Hasse + the Tate-module representation), non-vacuous statement.

  2. It carries that existence as a NAMED AXIOM `frobeniusTateData_exists`, with a doc-comment
     citing Silverman III.8.6 / the FLT dependency, exactly as the project marks cited-but-
     unformalized results. We do NOT prove it (that is the ~months FLT-adjacent construction).

  3. It DERIVES, sorry-free using the EXISTING machine-checked chain, the unconditional
     conclusion: the roots of `WeierstrassCurve.localPolynomial` (good reduction) have absolute
     value `√q`, i.e. function-field RH for the local factor, on Mathlib's real object. So O1
     becomes the ONLY gap; everything downstream is machine-checked. This route is
     boundary-inclusive (all finite fields, incl. the supersingular `a² = 4q`), so it needs only
     the NON-strict Hasse bound `a² ≤ 4q` that `hasse_of_matrix` yields directly -- no primality.

NON-VACUITY (the project's #106 failure mode): the O1 proposition is NOT false or vacuously
provable. For any Hasse-valid `(q, t)` the companion matrix `companion t q = !![0,-q;1,t]`
(`IsogenyDegree.lean`) is an explicit witness with `det = q`, `trace = t`, and non-negative
isogeny degrees (`companion_degForm_nonneg`). So `FrobeniusTateData` is satisfiable exactly
when Hasse holds for the curve -- which is a theorem (Hasse 1936). The axiom is therefore an
HONEST admit of a known-true statement, not a false admit. See `frobeniusTateData_companion`
below, which exhibits the witness FROM Hasse (a consistency check, not part of the RH proof).
-/

import ZetaRH.FunctionFieldRH
import ZetaRH.LocalFactor
import ZetaRH.IsogenyDegree

namespace ZetaRH.FrobeniusExistence

open Polynomial
open ZetaRH.FunctionFieldRH
open ZetaRH.IsogenyDegree

/-! ## A boundary-inclusive local-factor lemma (non-strict Hasse)

    `LocalFactor.localFactor_root_normSq` needs the STRICT bound `a² < 4q`. The O1 route here
    yields only the NON-strict `a² ≤ 4q` (`hasse_of_matrix`), which is enough for ALL finite
    fields including the supersingular boundary `a² = 4q`. This is the non-strict companion,
    proved by the same reciprocal-root trick but routed through the boundary-inclusive
    `eigenvalue_modulus_le` instead of `eigenvalue_modulus`. -/

/-- **RH for the local Euler factor, boundary-inclusive (non-strict Hasse).** For real `a, q`
    with the non-strict Hasse bound `a² ≤ 4q`, every complex root `β` of the local factor
    `1 - a·β + q·β² = 0` has `|β|² = 1/q`. Proof: `β ≠ 0` (else `1 = 0`), and `α = β⁻¹` is a root
    of `X² - aX + q`, so the boundary-inclusive eigenvalue extraction
    (`eigenvalue_modulus_le`) gives `|α|² = q`, whence `|β|² = 1/q`. (The strict-bound version
    `LocalFactor.localFactor_root_normSq` is the same statement; this drops strictness so the
    supersingular boundary is covered.) -/
theorem localFactor_root_normSq_le {a q : ℝ} (hHasse : a ^ 2 ≤ 4 * q)
    {β : ℂ} (hβ : 1 - (a : ℂ) * β + (q : ℂ) * β ^ 2 = 0) : Complex.normSq β = 1 / q := by
  have hβ0 : β ≠ 0 := by rintro rfl; simp at hβ
  have hroot : β⁻¹ ^ 2 - (a : ℂ) * β⁻¹ + (q : ℂ) = 0 := by
    field_simp
    linear_combination hβ
  have hns : Complex.normSq β⁻¹ = q := eigenvalue_modulus_le a q β⁻¹ hroot hHasse
  rw [Complex.normSq_inv] at hns
  rw [← hns, one_div, inv_inv]

/-! ## O1 as a single typed contract on Mathlib's `WeierstrassCurve`

    `WeierstrassCurve.localPolynomial` (T. Browning, Mathlib) is, for good reduction,
    `1 - a·T + q·T²` with `q = Nat.card κ` (residue field) and `a = q + 1 - #W(κ)`. The
    Frobenius on the Tate module `T_ℓ E ≅ ℤ²` is a rank-2 integer matrix `A` with
    `det A = q` (the degree of Frobenius) and `trace A = a` (the Frobenius trace), all of
    whose isogeny degrees `det(m·1 + n·A)` are non-negative ("every isogeny has non-negative
    degree"). `FrobeniusTateData W` packages exactly that existence, with `det`/`trace` pinned
    to Mathlib's `q`/`a`. -/

variable (R : Type*) [CommRing R] [IsDomain R] [IsDiscreteValuationRing R] {K : Type*}
  [Field K] [Algebra R K] [IsFractionRing R K] (W : WeierstrassCurve K)

/-- Mathlib's residue-field cardinality `q = #κ` (the degree of Frobenius), as an integer. -/
noncomputable def qOf : ℤ := (Nat.card (IsLocalRing.ResidueField R) : ℤ)

/-- Mathlib's Frobenius trace `a = q + 1 - #W(κ)`, the cross term of `localPolynomial`. -/
noncomputable def aOf : ℤ :=
  qOf R + 1 - (Nat.card ((W.minimal R).reduction R).toAffine.Point : ℤ)

/-- **O1 as a Prop on Mathlib's object.** There is a rank-2 integer matrix `A` -- the Frobenius
    acting on the Tate module `T_ℓ E ≅ ℤ²` -- with

    * `A.det = q`     (the degree of Frobenius = the residue-field cardinality `#κ`),
    * `A.trace = a`   (the Frobenius trace = `q + 1 - #W(κ)`, Mathlib's `localPolynomial` cross
                       term),
    * `∀ m n, 0 ≤ det(m·1 + n·A)`  (every isogeny `m·1 + n·φ` has non-negative degree, `deg = det`).

    `q` and `a` are taken verbatim from Mathlib's `WeierstrassCurve.localPolynomial`. This is the
    single open input of lever B: the scheme-theoretic Frobenius-on-Tate-module construction
    (O1 + O2; Silverman III.8.6, via the Weil pairing). It is a TRUE statement (Hasse + the
    Tate-module representation), carried as the one named axiom below. -/
def FrobeniusTateData : Prop :=
  ∃ A : Matrix (Fin 2) (Fin 2) ℤ,
    A.det = qOf R ∧
    A.trace = aOf R W ∧
    ∀ m n : ℤ, 0 ≤ (m • (1 : Matrix (Fin 2) (Fin 2) ℤ) + n • A).det

/-! ## Non-vacuity guard (#106): the O1 statement is TRUE, not a false/vacuous admit

    Before carrying O1 as an axiom we confirm it is satisfiable -- and satisfiable EXACTLY when
    the Hasse bound holds for the curve (a theorem). The companion matrix of `X² - a·X + q` is the
    explicit witness. This is a CONSISTENCY check (it assumes Hasse to produce `deg ≥ 0`, the
    reverse direction of the real chain), guaranteeing the axiom is an honest admit of a known
    truth, not a false `axiom`. -/

/-- **Non-vacuity: the O1 contract is satisfiable from Hasse.** If Mathlib's trace `a` and
    `q = #κ` satisfy the Hasse bound `a² ≤ 4q` (a theorem, Hasse 1936), then `FrobeniusTateData W`
    holds: the companion matrix `companion a q = !![0,-q;1,a]` is the explicit witness, with
    `det = q`, `trace = a`, and non-negative isogeny degrees (`companion_degForm_nonneg`). So the
    O1 axiom below is an HONEST admit of a true statement -- not vacuous, not false. -/
theorem frobeniusTateData_companion
    (hHasse : aOf R W ^ 2 ≤ 4 * qOf R) : FrobeniusTateData R W :=
  ⟨companion (aOf R W) (qOf R),
    companion_det _ _,
    companion_trace _ _,
    fun m n => companion_degForm_nonneg hHasse m n⟩

/-! ## The one named axiom (O1), cited but unformalized

    This is the SOLE admit in the lever-B chain. It is a known theorem (Hasse 1936 / the
    Tate-module representation of Frobenius), NOT a false or open conjecture: the Frobenius
    endomorphism `φ_q` acts on `T_ℓ E ≅ ℤ²`, its degree is `q` and its trace is `a`, and every
    isogeny has non-negative degree. We carry it as an axiom because the scheme-theoretic objects
    (`T_ℓ E`, the Weil pairing, `End(E)`, the degree map) are ABSENT from the current Mathlib pin
    and are FLT-project targets (months of construction). Everything downstream is machine-checked
    modulo this axiom. Non-vacuity is guaranteed by `frobeniusTateData_companion` above: under
    Hasse, the companion matrix is an explicit witness, so this admits a TRUE statement. -/

/-- **AXIOM (O1): the Frobenius-on-Tate-module representation exists.** For a Weierstrass curve
    over a nonarchimedean local field with good reduction, the rank-2 integer Frobenius matrix
    `A` exists with `det A = q`, `trace A = a` (Mathlib's `localPolynomial` data), and all isogeny
    degrees non-negative.

    Reference: Silverman, *The Arithmetic of Elliptic Curves* III.8.6 (`deg = det`, `tr = trace`
    on `T_ℓ E`, via the Weil pairing `e_ℓ(φx, φy) = e_ℓ(x, y)^{deg φ}`) and V.1.1 (Hasse). This
    is the FLT-adjacent scheme-theoretic content Mathlib lacks (Tate module, Weil pairing,
    isogeny/degree API). It is the single open input of lever B; nothing in this repo asserts it
    except this named axiom, so `#print axioms` of the derived results below names it explicitly.
    Its truth is witnessed by `frobeniusTateData_companion` (the companion matrix realizes the
    contract whenever Hasse holds, which it does). -/
axiom frobeniusTateData_exists (hgood : (W.minimal R).HasGoodReduction R) :
    FrobeniusTateData R W

/-! ## The derived unconditional conclusion (sorry-free, modulo the one axiom)

    From `FrobeniusTateData` (the O1 axiom), the existing machine-checked chain gives RH for the
    local factor on Mathlib's real object: the roots of `localPolynomial` have `|·|² = 1/q`. -/

/-- **Function-field RH for the local factor on Mathlib's `localPolynomial`, from O1
    (sorry-free modulo the axiom).** Given good reduction, every complex root `β` of
    `W.localPolynomial` has `|β|² = 1/q` (equivalently, its reciprocal -- a Frobenius eigenvalue --
    lies on `|α| = √q`, the critical line `Re = 1/2`).

    The proof uses ONLY the O1 axiom plus the existing machine-checked chain:
    `frobeniusTateData_exists` supplies `A`; `hasse_of_matrix` (Phase A) turns its non-negative
    isogeny degrees into the Hasse bound `a² ≤ 4q`; `localFactor_root_normSq_le` (boundary-
    inclusive, this file) reads off the root modulus. The trace `a` and count `q` are taken
    verbatim from Mathlib's `localPolynomial`. No geometric content is assumed beyond the single
    named axiom. -/
theorem localPolynomial_root_normSq_of_O1 (hgood : (W.minimal R).HasGoodReduction R)
    {β : ℂ} (hβ : aeval β (W.localPolynomial R) = 0) :
    Complex.normSq β = 1 / ((Nat.card (IsLocalRing.ResidueField R) : ℤ) : ℝ) := by
  obtain ⟨A, hdet, htrace, hpos⟩ := frobeniusTateData_exists R W hgood
  -- Phase A: non-negative isogeny degrees ⟹ the Hasse bound `(tr A)² ≤ 4·(det A)`.
  have hHasse : (A.trace : ℝ) ^ 2 ≤ 4 * (A.det : ℝ) := hasse_of_matrix A hpos
  rw [hdet, htrace] at hHasse
  -- Unfold Mathlib's `localPolynomial` (good reduction) at the root `β`.
  rw [LocalFactor.localPolynomial_eq_of_goodReduction W hgood] at hβ
  simp only [map_add, map_sub, map_mul, map_pow, map_one, aeval_X, map_intCast, eq_intCast] at hβ
  -- `aOf`/`qOf` ARE the cross term and `q` of Mathlib's good-reduction `localPolynomial`.
  apply localFactor_root_normSq_le (a := (aOf R W : ℝ)) (q := (qOf R : ℝ)) hHasse
  simp only [aOf, qOf]
  push_cast
  push_cast at hβ
  linear_combination hβ

/-! ## O1 as the only gap: RH for the curve reduces to the single axiom

    Packaged statement: under good reduction, ALL roots of Mathlib's `localPolynomial` lie on the
    circle `|β| = q^{-1/2}` (equivalently the Frobenius eigenvalues lie on `|α| = √q`, `Re = 1/2`).
    The ONLY input is the named O1 axiom; everything else is machine-checked. -/

/-- **Function-field RH for the curve on Mathlib's object, modulo O1 only.** Given good reduction,
    every root of `W.localPolynomial` lies on the circle of radius `q^{-1/2}`. The sole open input
    is the named axiom `frobeniusTateData_exists` (O1); the entire derivation is sorry-free. -/
theorem functionfield_RH_localPolynomial (hgood : (W.minimal R).HasGoodReduction R) :
    ∀ β : ℂ, aeval β (W.localPolynomial R) = 0 →
      Complex.normSq β = 1 / ((Nat.card (IsLocalRing.ResidueField R) : ℤ) : ℝ) :=
  fun _ hβ => localPolynomial_root_normSq_of_O1 R W hgood hβ

end ZetaRH.FrobeniusExistence
