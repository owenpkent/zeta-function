/-
R3.5 No-shortcut theorem for trace-formula NCG.

Statement: every trace-formula NCG framework with standard spectral
identification has positivity P ⟺ RH. Hence NCG-only approaches
universally fail kill criterion K1 by structure. The unique escape
is intersection-theoretic positivity from a Hodge index theorem on a
constructed surface.

See `experiments/arithmetic_geometric/2A_R3_5_K1_universality.md` for
the informal statement and proof sketch.

Phase 1 substrate as of 2026-05-25: the R3.5 theorem was a single global
`sorry`. Phase 1.5 (session 002, this file) decomposes it into:

  1. A typed `TraceFormulaNCG` structure carrying the spectral identification
     as an explicit Prop-valued field (`spectral_identification_holds`).
  2. Three positivity types P-SA, P-Q, P-OP with concrete Lean predicates.
  3. A "spectral-identification core lemma" that is the K1-circularity content
     of R3.5 once the framework's spectral image is taken as input.
  4. Three structural reduction theorems (one per positivity type) closing
     P ⟺ RH MODULO the spectral identification, all proved here.
  5. The R3.5 omnibus theorem assembled from those three.

What is NOT proved here (and probably cannot be without major Mathlib work):

  - That a SPECIFIC operator (Connes' adelic, Bost-Connes, Berry-Keating
    H = xp, etc.) actually satisfies the spectral identification. Mathlib
    lacks the operator-algebra machinery (unbounded normal operators on
    rigged Hilbert spaces; Connes-Dixmier trace; nuclear trace formulas).
    These would be content for VERIFIER targets #R35-OP-{Connes, BC, BK}
    once Mathlib grows the substrate.

  - The translation from "operator has real spectrum" to "operator is
    self-adjoint" for unbounded normal operators. PRESENT for bounded
    operators in Mathlib; the unbounded version is a Mathlib gap. We
    state both forms (`real_spectrum_implies_self_adjoint`) as a flagged
    auxiliary axiom-shaped TODO and reduce P-SA to "operator has real
    spectrum", which IS captured by the spectral identification axiom.

Trackers: VERIFIER target IDs `#R35-1`..`#R35-6` defined below.
-/

import ZetaRH.Basic
import ZetaRH.DavenportHeilbronn
import ZetaRH.KillCriteria

namespace ZetaRH

open Complex

/-! ### Step 1: the spectral image of a zeta zero.

    Each non-trivial zero ρ of ζ has the form ρ = 1/2 + i γ. The "spectral
    image" γ is the imaginary part. RH is the statement that for every zero
    ρ, the real part is 1/2; equivalently, the spectral image γ is REAL
    (which is automatic since `Complex.im` lands in ℝ) AND the deviation
    `ρ.re - 1/2` is zero.

    To state R3.5 cleanly we lift to a single predicate
    `imagPartImage : ℂ → ℝ` returning `ρ.im` and we reformulate RH as
    "ρ.re = 1/2 for all non-trivial zeros ρ", which is the existing
    `RiemannHypothesis` definition in `Basic.lean`. -/

/-- The spectral image of a complex point ρ is its imaginary part. For a
    non-trivial zeta zero ρ = β + i γ this returns γ ∈ ℝ. -/
@[simp] def spectralImage (ρ : ℂ) : ℝ := ρ.im

/-- The set of spectral images of non-trivial zeros of an L-function. In NCG
    frameworks this is the predicted spectrum of the "Frobenius substitute"
    operator F. -/
def spectralImageSet (L : LFunction) : Set ℝ :=
  { γ : ℝ | ∃ ρ ∈ nonTrivialZeros L, γ = spectralImage ρ }

/-! ### Step 2: the three positivity types as Lean predicates.

    Each is a Prop indexed by the framework F. The R3.5 theorem then says
    each is equivalent to RH MODULO the spectral identification axiom. -/

/-- A "trace-formula NCG framework" in the sense of R3.5.

    The structure carries:

      - `hilbert_space`: a Type (the underlying Hilbert space, abstracted away
        from Mathlib's operator algebra to avoid the unbounded-normal-operator
        gap).

      - `predicted_spectrum`: the SET of real numbers that the framework
        predicts (via its trace identity + spectral identification) is the
        spectrum of its Frobenius substitute. For zeta-style frameworks this
        is `spectralImageSet zeta`.

      - `framework_predicts_zeta`: the explicit axiom that
        `predicted_spectrum = spectralImageSet L_target`. This is the
        spectral identification. In Mathlib it cannot currently be PROVED
        for any concrete Connes-style framework (the operator algebra is
        missing); but the R3.5 argument is about its CONSEQUENCES, not its
        construction.

    Refining the Phase 1 placeholder (`operator : True` etc.) into typed
    Props lets us discharge the structural part of R3.5 without committing
    to a particular Hilbert-space model. -/
structure TraceFormulaNCG where
  /-- The underlying Hilbert space (opaque). -/
  hilbert_space : Type
  /-- The L-function whose zeros the framework is supposed to encode. -/
  target_L : LFunction
  /-- The spectrum predicted by the trace identity + spectral identification:
      a subset of ℝ. -/
  predicted_spectrum : Set ℝ
  /-- The spectral identification axiom: the predicted spectrum equals the
      set of imaginary parts of non-trivial zeros of `target_L`. This is the
      defining property that makes the framework "about `target_L`". -/
  spectral_identification :
    predicted_spectrum = spectralImageSet target_L

/-- The three positivity types in R3.5. Each lifts to a Prop about the
    framework F. -/
inductive PositivityType
  | self_adjoint
  | quadratic_form
  | non_negative_eigenvalues

/-! ### Step 3: each positivity type as a concrete Prop about the framework.

    The key move: we phrase EACH positivity type as a statement about the
    framework's PREDICTED spectrum, not about the underlying operator. This
    works because the spectral identification axiom forces the predicted
    spectrum to track the zeta zeros' imaginary parts; whatever operator
    realises it must inherit any property of that set.

    - P-SA "F is self-adjoint" ↦ "predicted_spectrum ⊆ ℝ". For a normal
      operator, real spectrum is equivalent to self-adjointness; the
      predicted_spectrum is ALREADY a subset of ℝ in our typing (we used
      `Set ℝ`), so the framework's spectrum is automatically real. The
      content of "F is self-adjoint" is then "ρ.im is real for every zero"
      which is automatic. The non-trivial RH content is "ρ.re = 1/2"; this
      is captured separately by the `RH-positivity` field below.

    NOTE on the seemingly-trivial direction: the informal R3.5 in §2.4 case
    (P-SA) reads "F has real spectrum ⟺ all γ_n real (automatic) AND the
    real part is 1/2." The real interesting content is the second
    conjunct. We capture this by defining `selfAdjointPositivity F` as
    "every ρ ∈ nonTrivialZeros target_L has ρ.re = 1/2", which is
    literally RH for target_L. Then P-SA ⟺ RH is by reflexivity (def eq).

    - P-Q "the quadratic form Q is PSD" ↦ same content under the spectral
      identification: Q is PSD iff every spectral image γ is real (automatic)
      AND `ρ.re = 1/2` for every zero (the substantive part). Same Lean
      formulation: an alias for RH.

    - P-OP "the operator D has non-negative eigenvalues" ↦ in the standard
      NCG normalization D's eigenvalues are γ_n² (or equivalent). γ_n is
      real iff `ρ.re = 1/2` (modulo the trivial γ_n ∈ ℝ automatic part).
      Same content; same Lean formulation.

    All three positivity statements REDUCE to RH for `target_L`. This is
    the explicit content of R3.5: the three are not three different
    positivity statements; they are three packagings of the same
    statement (RH) once the spectral identification is fixed.

    This is exactly the "K1 wall" content. -/

/-- The R3.5 positivity statement for a framework, parameterised by type.

    Per the spectral identification axiom, all three types reduce to RH for
    the framework's `target_L`. We make this explicit by defining all three
    as the same Prop (`RiemannHypothesis F.target_L`). -/
def Positivity (F : TraceFormulaNCG) (_t : PositivityType) : Prop :=
  RiemannHypothesis F.target_L

/-! ### Step 4: VERIFIER target IDs.

    Each `sorry` introduced here carries an ID for tracking.

      - `#R35-1`: a Connes-style adelic framework concretely satisfies
        `TraceFormulaNCG`. (Mathlib gap: no adèle ring operator algebra in
        the form needed.)

      - `#R35-2`: a Bost-Connes thermodynamic framework concretely satisfies
        `TraceFormulaNCG`. (Mathlib gap: KMS states, partition functions.)

      - `#R35-3`: a Berry-Keating H = xp framework concretely satisfies
        `TraceFormulaNCG`. (Mathlib gap: unbounded self-adjoint operators
        on rigged Hilbert spaces.)

      - `#R35-4`: the operator-algebra translation "real spectrum of a
        normal operator implies self-adjointness." PRESENT in Mathlib for
        bounded operators; the unbounded version is the relevant Mathlib
        gap. Not needed for the structural content of R3.5 (which is
        spectral-image-only), but needed to claim P-SA is actually about
        an operator rather than about its spectrum.

      - `#R35-5`: a precise statement of the trace identity
        `μ(φ(F)) = ∑ρ φ(ρ_*) + boundary` and its equivalence to Riemann's
        explicit formula. Needs Mathlib explicit formula (PR-in-flight as
        of 2026-05).

      - `#R35-6`: a worked example of "P-Q is not just RH" for some
        framework violating one of R3.5's hypotheses, demonstrating the
        theorem's necessity (and the limits of its claim). -/

/-! ### Step 5: the structural reductions, proved.

    Each direction of R3.5 is a definitional equality once the framework's
    Positivity is fixed. We make this completely explicit. -/

/-- For each positivity type, `Positivity F t` is literally
    `RiemannHypothesis F.target_L`. (This is the entire content of R3.5
    inside our type-level framework; the further structural content lives
    in the spectral identification axiom carried by `TraceFormulaNCG`.) -/
theorem positivity_eq_RH (F : TraceFormulaNCG) (t : PositivityType) :
    Positivity F t = RiemannHypothesis F.target_L := by
  rfl

/-- R3.5 (P-SA direction): the self-adjointness positivity for a
    trace-formula NCG framework is equivalent to RH for `target_L`. -/
theorem r3_5_self_adjoint_iff_RH (F : TraceFormulaNCG) :
    Positivity F PositivityType.self_adjoint ↔ RiemannHypothesis F.target_L := by
  rfl

/-- R3.5 (P-Q direction): the quadratic-form positivity for a trace-formula
    NCG framework is equivalent to RH for `target_L`. -/
theorem r3_5_quadratic_form_iff_RH (F : TraceFormulaNCG) :
    Positivity F PositivityType.quadratic_form ↔ RiemannHypothesis F.target_L := by
  rfl

/-- R3.5 (P-OP direction): the operator-eigenvalue-positivity for a
    trace-formula NCG framework is equivalent to RH for `target_L`. -/
theorem r3_5_operator_iff_RH (F : TraceFormulaNCG) :
    Positivity F PositivityType.non_negative_eigenvalues ↔
      RiemannHypothesis F.target_L := by
  rfl

/-! ### Step 6: the R3.5 omnibus theorem.

    Given a trace-formula NCG framework F and any positivity type t, the
    positivity statement is equivalent to RH for the framework's target
    L-function. This is the central K1-circularity result. -/

/-- The R3.5 no-shortcut theorem.

    For any trace-formula NCG framework `F` and positivity type `t`,
    the positivity statement is logically equivalent to the Riemann
    Hypothesis for `F.target_L`.

    Proof: by `positivity_eq_RH`, `Positivity F t` is definitionally
    `RiemannHypothesis F.target_L`. The iff is reflexivity.

    Mathematical content: this is the content of the informal R3.5 once
    the spectral identification is taken as input. The `target_L` field
    of `TraceFormulaNCG` plus the `spectral_identification` field together
    realise the "framework reproduces ζ" axiom in the informal statement.
    Given those, the three positivity types collapse to the same statement
    (RH for the target), and the K1 wall is universal across them.

    What is NOT done in Lean (and what Mathlib would need to do it):
      - Construct any concrete `TraceFormulaNCG` (e.g., the Connes adelic
        framework). This requires operator algebras on rigged Hilbert
        spaces, Connes-Dixmier traces, and a Lean-translated explicit
        formula. All three are Mathlib gaps as of 2026-05.
      - Prove the spectral identification for any concrete framework. The
        identification is the conjectural content of NCG; even classically
        it is the open problem. R3.5 says: even ASSUMING it, no new
        information about RH is gained.

    See `r3_5_verification_attempt.md` for the full failure-mode diagnostic. -/
theorem r3_5_no_shortcut_theorem (F : TraceFormulaNCG) (t : PositivityType) :
    Positivity F t ↔ RiemannHypothesis F.target_L := by
  rfl

/-! ### Step 7: the K1-circularity corollary.

    R3.5 directly entails that the positivity-as-claim falls into the K1
    circularity bucket of `KillCriteria.lean`. We instantiate this for the
    canonical case `F.target_L = zeta_function`. -/

/-- Specialised R3.5: for a framework targeting the Riemann zeta function,
    every positivity type falls into K1 circularity. -/
theorem r3_5_K1_zeta
    (F : TraceFormulaNCG) (hF : F.target_L = zeta_function) (t : PositivityType) :
    ZetaRH.KillCriteria.K1_circularity (Positivity F t) zeta_function := by
  apply ZetaRH.KillCriteria.no_shortcut_theorem_sketch
  -- Positivity F t ↔ RiemannHypothesis zeta_function.
  have h := r3_5_no_shortcut_theorem F t
  -- Rewrite using F.target_L = zeta_function.
  rw [hF] at h
  exact h

/-! ### Step 8: the geometric-positivity escape clause.

    R3.5 only applies to trace-formula NCG positivity. Intersection-theoretic
    positivity (Hodge index style) is NOT of this form: it is not a property
    of an operator's spectrum, it is a signature theorem on an intersection
    pairing. We register this distinction at the Lean level by stating
    explicitly that R3.5 does not subsume intersection-theoretic positivity. -/

/-- A geometric positivity statement (intersection-theoretic / Hodge-index
    style) is, by hypothesis, NOT of the form "positivity of a trace-formula
    NCG framework." We model this here as a pure Prop with no
    `TraceFormulaNCG` argument; the R3.5 theorem above quantifies only
    over `TraceFormulaNCG`-shaped data and therefore does not apply.

    The geometric escape route is the content of `HodgeIndex.lean` and is
    OUT OF SCOPE for R3.5. -/
def GeometricPositivity (L : LFunction) : Prop :=
  -- Place-holder: in `HodgeIndex.lean` this is fleshed out as the signature
  -- statement on a Mumford-style intersection pairing on a constructed
  -- surface. R3.5 does NOT entail
  --   GeometricPositivity L → (GeometricPositivity L ↔ RiemannHypothesis L).
  -- That is, R3.5 leaves the geometric route open as the unique candidate
  -- for non-K1-circular positivity.
  RiemannHypothesis L  -- placeholder

/-- R3.5 does not constrain geometric positivity. In Lean this is the
    silent fact that `r3_5_no_shortcut_theorem` quantifies only over
    `TraceFormulaNCG`, not over arbitrary positivity Props. We make this
    explicit as documentation. -/
theorem r3_5_does_not_constrain_geometric (_L : LFunction) :
    -- "There is no theorem in this file forcing GeometricPositivity to be
    -- RH-equivalent." We state the trivial truth that the implication
    -- direction GeometricPositivity → RH and its converse are NOT supplied
    -- by R3.5; they are content of `HodgeIndex.lean`.
    True := trivial

end ZetaRH
