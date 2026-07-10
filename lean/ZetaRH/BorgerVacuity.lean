import Mathlib.Data.Rat.Cast.Defs
import Mathlib.Data.ZMod.Basic
import Mathlib.FieldTheory.Finite.Basic
import Mathlib.Algebra.Algebra.Defs
import Mathlib.RingTheory.Localization.FractionRing
import Mathlib.RingTheory.Ideal.Span
import Mathlib.RingTheory.Ideal.Quotient.Basic
import Mathlib.LinearAlgebra.SModEq.Basic
import Mathlib.ModelTheory.Ultraproducts

/-!
# The Borger vacuity core and a partial ultraproduct object (LEARNINGS #156, targets T2/T3)

This module carries the VERIFIER discharge of the model-theoretic Frobenius arc's remaining
targets from `docs/03_research/model_theoretic_frobenius.md` Section 11 (as corrected by the
ADVERSARY):

* **#MTF-1 consensus witness #3** (Job 1): a THIRD independent formalization of the NG1 rigidity
  kernel (`ng1_rigidity_w3`), by a proof route distinct from the two prior witnesses
  (`ModelTheoreticFrobenius.ng1_rigidity` via `RingHom.ext_rat`, and
  `TamenessTrade.ng1_rigidity_indep` via explicit `num`/`den` unit cancellation). This witness
  uses the universal property of `ℚ` as the localization / fraction field of `ℤ`
  (`IsLocalization.ringHom_ext`) together with `ℤ` being initial in commutative rings
  (`Int.subsingleton_ringHom`). Three independent formalizations make #MTF-1 canonical under the
  four-layer consensus rule.

* **#MTF-3, the Borger VACUITY** (Job 2, PROVEN-tier): in a commutative `ℚ`-algebra `R` every
  standard prime `q` is invertible, so `Ideal.span {(q : R)} = ⊤`, the quotient `R ⧸ (q)` is
  `Subsingleton`, and the Frobenius-lift congruence `ψ x ≡ x^q [SMOD (q)]` holds for EVERY ring
  endomorphism `ψ` and every `x`. This is the machine-checked form of the corrected #156 finding:
  the ultrafilter TRIVIALIZES (does not destroy) the `Λ`-structure by inverting the primes the
  congruences were about, so the lift condition carries zero descent information.

* **#MTF-2, a PARTIAL ultraproduct object** (Job 3): the coordinatewise Frobenius on the genuine
  dependent ultraproduct `Filter.Product (fun p => ZMod p) l`, proven to fix the diagonal integers
  (the Fermat coordinatewise witness lifted to the ultraproduct). Plus the non-dependent germ ring
  hom `germRingHom` showing a coordinatewise ring endomorphism descends to a ring endomorphism of
  the germ ring. The EXACT wall is recorded in the docstrings below: Mathlib's dependent
  ultraproduct `Filter.Product` carries only a model-theoretic `FirstOrder.Language.Structure`, not
  a `CommRing`/`Field`/`IsAlgClosed` instance, so `productFrobenius` cannot be typed as a `RingHom`,
  and the char-0 / algebraically-closed / ACFA facts need the ring-language transfer that Mathlib
  does not provide automatically.

* **#MTF-4 is BLOCKED-ON-MATHLIB** (Job 3): the NG2(iii) cardinality dichotomy (internal sets are
  finite or of cardinality `≥ 2^{ℵ₀}`) needs a `Saturated` / `κ`-saturation predicate on
  `FirstOrder.Language.Structure` and the type-realization machinery, neither of which exists in
  Mathlib. See the closing comment.
-/

namespace ZetaRH.BorgerVacuity

open Filter

/-! ## Job 1: NG1 rigidity, consensus witness #3 (#MTF-1) -/

/-- **NG1 rigidity kernel, third independent witness (#MTF-1, consensus witness #3).**

Every ring endomorphism `σ` of a commutative `ℚ`-algebra `R` fixes the canonically imported `ℚ`
pointwise: `σ ∘ algebraMap ℚ R = algebraMap ℚ R`.

Re-derived from the dossier statement (`model_theoretic_frobenius.md` Section 3) WITHOUT reading the
two prior formalizations, and by a genuinely distinct route: `σ.comp (algebraMap ℚ R)` and
`algebraMap ℚ R` are two ring homomorphisms `ℚ →+* R`; since `ℚ` is the localization of `ℤ` at its
nonzero divisors (`Rat.isFractionRing`), by the universal property `IsLocalization.ringHom_ext` it
suffices that they agree after restriction along `algebraMap ℤ ℚ`; but any two ring homomorphisms
`ℤ →+* R` are equal (`ℤ` is initial in commutative rings, `Int.subsingleton_ringHom`), so the
restrictions agree automatically. No `RingHom.ext_rat` and no explicit `num`/`den` cancellation
appear, so this is independent of witnesses #1 and #2. -/
theorem ng1_rigidity_w3 {R : Type*} [CommRing R] [Algebra ℚ R] (σ : R →+* R) :
    σ.comp (algebraMap ℚ R) = algebraMap ℚ R := by
  apply IsLocalization.ringHom_ext (nonZeroDivisors ℤ)
  -- Both sides restricted along `algebraMap ℤ ℚ` are ring homs `ℤ →+* R`, hence equal.
  exact Subsingleton.elim _ _

/-- Pointwise form of `ng1_rigidity_w3`: `σ (algebraMap ℚ R q) = algebraMap ℚ R q` for all `q : ℚ`. -/
theorem ng1_rigidity_w3_apply {R : Type*} [CommRing R] [Algebra ℚ R] (σ : R →+* R) (q : ℚ) :
    σ (algebraMap ℚ R q) = algebraMap ℚ R q :=
  RingHom.congr_fun (ng1_rigidity_w3 σ) q

/-! ## Job 2: the Borger vacuity core (#MTF-3) -/

/-- In a commutative `ℚ`-algebra, every nonzero natural number is a unit: `(q : R)` is invertible
because `(q : ℚ)` is a unit in the field `ℚ` and `algebraMap ℚ R` preserves units. This is the
one-line reason "the ultrafilter inverts every standard prime". -/
theorem natCast_isUnit_of_ne_zero {R : Type*} [CommRing R] [Algebra ℚ R] {q : ℕ}
    (hq : q ≠ 0) : IsUnit (q : R) := by
  have h : (q : R) = algebraMap ℚ R (q : ℚ) := by rw [map_natCast]
  rw [h]
  exact (isUnit_iff_ne_zero.mpr (Nat.cast_ne_zero.mpr hq)).map (algebraMap ℚ R)

/-- **The ideal `(q)` is the whole ring** whenever `(q : R)` is a unit. With `q` a standard prime
in a commutative `ℚ`-algebra this says `qR = R`: the ideal the Frobenius-lift congruence is stated
modulo is everything, so the quotient carries no descent data. -/
theorem span_natCast_eq_top {R : Type*} [CommRing R] {q : ℕ} (hq : IsUnit (q : R)) :
    Ideal.span {(q : R)} = ⊤ :=
  Ideal.span_singleton_eq_top.mpr hq

/-- The `ℚ`-algebra specialization of `span_natCast_eq_top` for a standard prime `q`. -/
theorem span_natCast_eq_top_of_prime {R : Type*} [CommRing R] [Algebra ℚ R] {q : ℕ}
    (hq : q.Prime) : Ideal.span {(q : R)} = ⊤ :=
  span_natCast_eq_top (natCast_isUnit_of_ne_zero hq.ne_zero)

/-- **The quotient `R ⧸ (q)` is trivial** when `(q : R)` is a unit. This is the load-bearing core of
the corrected Borger finding: the residue ring at a standard prime is the zero ring `R/qR = 0`, so
every congruence modulo `(q)` is automatically satisfied. -/
theorem quotient_span_natCast_subsingleton {R : Type*} [CommRing R] {q : ℕ}
    (hq : IsUnit (q : R)) : Subsingleton (R ⧸ Ideal.span {(q : R)}) :=
  Ideal.Quotient.subsingleton_iff.mpr (span_natCast_eq_top hq)

/-- **The Frobenius-lift congruence is VACUOUS (#MTF-3).** If `(q : R)` is a unit (in particular for
every standard prime `q` in a commutative `ℚ`-algebra, via `natCast_isUnit_of_ne_zero`), then for
EVERY ring endomorphism `ψ : R →+* R` and every `x : R`,

  `ψ x ≡ x ^ q [SMOD Ideal.span {(q : R)}]`.

Because `Ideal.span {(q : R)} = ⊤` the SMOD relation is on a subsingleton quotient, so the
congruence holds for every `ψ` and every `x` and carries no information. This is the machine-checked
statement "every ring endomorphism is a Frobenius lift at every standard prime; being one carries
zero `𝔽₁`-descent data": the ultrafilter trivializes, rather than destroys, the `Λ`-structure. -/
theorem borger_lift_congruence_vacuous {R : Type*} [CommRing R] {q : ℕ}
    (hq : IsUnit (q : R)) (ψ : R →+* R) (x : R) :
    ψ x ≡ x ^ q [SMOD Ideal.span {(q : R)}] := by
  rw [span_natCast_eq_top hq]
  exact SModEq.top

/-- The two-endomorphism face of the vacuity: modulo a standard prime `q` (a unit), ANY two ring
endomorphisms agree on every input, `ψ₁ x ≡ ψ₂ x [SMOD (q)]`. The Frobenius-lift condition therefore
cannot distinguish endomorphisms: zero descent content. -/
theorem borger_lift_any_two_congruent {R : Type*} [CommRing R] {q : ℕ}
    (hq : IsUnit (q : R)) (ψ₁ ψ₂ : R →+* R) (x : R) :
    ψ₁ x ≡ ψ₂ x [SMOD Ideal.span {(q : R)}] := by
  rw [span_natCast_eq_top hq]
  exact SModEq.top

/-- `ℚ`-algebra + standard prime packaging of `borger_lift_congruence_vacuous`. -/
theorem borger_lift_congruence_vacuous_prime {R : Type*} [CommRing R] [Algebra ℚ R] {q : ℕ}
    (hq : q.Prime) (ψ : R →+* R) (x : R) :
    ψ x ≡ x ^ q [SMOD Ideal.span {(q : R)}] :=
  borger_lift_congruence_vacuous (natCast_isUnit_of_ne_zero hq.ne_zero) ψ x

/-! ## Job 3: partial ultraproduct object (#MTF-2)

### Fragment (A): the non-dependent germ ring hom

A coordinatewise ring endomorphism descends to a ring endomorphism of the germ ring. This is the
non-dependent shadow of "the coordinatewise Frobenius descends to `K = ∏ / 𝒰`": it uses Mathlib's
genuine `CommRing (Filter.Germ l R)` instance and a `RingHom` codomain, but is restricted to a
FIXED coefficient ring `R` at every coordinate (see the wall note for the dependent case). -/

/-- **A coordinatewise ring endomorphism descends to a ring endomorphism of the germ ring.**
Given `φ : R →+* R` and a filter `l`, post-composition `Filter.Germ.map φ` is a ring hom
`Filter.Germ l R →+* Filter.Germ l R`. Instantiating `l := (↑U : Filter α)` for an ultrafilter `U`
gives the ultraproduct-ring version. -/
def germRingHom {α R : Type*} [CommRing R] (l : Filter α) (φ : R →+* R) :
    Filter.Germ l R →+* Filter.Germ l R where
  toFun := Filter.Germ.map φ
  map_one' := by
    rw [← Filter.Germ.coe_one, Filter.Germ.map_coe]
    exact Filter.Germ.coe_eq.mpr (Filter.Eventually.of_forall fun _ => map_one φ)
  map_mul' a b := by
    refine Filter.Germ.inductionOn₂ a b fun f g => ?_
    rw [← Filter.Germ.coe_mul]
    simp only [Filter.Germ.map_coe]
    rw [← Filter.Germ.coe_mul]
    exact Filter.Germ.coe_eq.mpr (Filter.Eventually.of_forall fun x => map_mul φ (f x) (g x))
  map_zero' := by
    rw [← Filter.Germ.coe_zero, Filter.Germ.map_coe]
    exact Filter.Germ.coe_eq.mpr (Filter.Eventually.of_forall fun _ => map_zero φ)
  map_add' a b := by
    refine Filter.Germ.inductionOn₂ a b fun f g => ?_
    rw [← Filter.Germ.coe_add]
    simp only [Filter.Germ.map_coe]
    rw [← Filter.Germ.coe_add]
    exact Filter.Germ.coe_eq.mpr (Filter.Eventually.of_forall fun x => map_add φ (f x) (g x))

@[simp]
theorem germRingHom_coe {α R : Type*} [CommRing R] (l : Filter α) (φ : R →+* R) (f : α → R) :
    germRingHom l φ (f : Filter.Germ l R) = ((fun a => φ (f a) : α → R) : Filter.Germ l R) :=
  rfl

/-- The identity endomorphism descends to the identity on the germ ring. -/
theorem germRingHom_id {α R : Type*} [CommRing R] (l : Filter α) :
    germRingHom l (RingHom.id R) = RingHom.id _ := by
  ext a
  refine Filter.Germ.inductionOn a fun f => ?_
  rfl

/-! ### Fragment (B): the dependent ultraproduct and the Fermat coordinatewise fact

This uses Mathlib's genuine dependent ultraproduct `Filter.Product l ε` (the quotient of
`∀ a, ε a` by `∀ᶠ a in l, · = ·`), which is exactly `K = ∏_p ε_p / 𝒰` when `l = ↑U`. We build the
coordinatewise Frobenius `x_p ↦ x_p^{p}` on `Filter.Product l (fun a => ZMod (P a))` (with `P a` the
prime at coordinate `a`) as a bare FUNCTION, and prove it fixes the diagonal integers. The wall is
that `Filter.Product` carries no ring structure (see the closing note), so this cannot be a
`RingHom`. -/

/-- The coordinatewise Frobenius on the dependent ultraproduct `Filter.Product l (fun a => ZMod (P a))`,
where `P a` is the (prime) modulus at coordinate `a`. It is `[(x_a)_a] ↦ [(x_a ^ {P a})_a]`. This is
a bare function: `Filter.Product` has only a model-theoretic structure, not a `CommRing`. -/
def productFrobenius {α : Type*} (l : Filter α) (P : α → ℕ) [∀ a, Fact (P a).Prime] :
    l.Product (fun a => ZMod (P a)) → l.Product (fun a => ZMod (P a)) :=
  @Quotient.map' _ _ (Filter.productSetoid l _) (Filter.productSetoid l _)
    (fun x a => (x a) ^ (P a))
    (fun _ _ h => h.mono fun a ha => by simp only [ha])

theorem productFrobenius_coe {α : Type*} (l : Filter α) (P : α → ℕ) [∀ a, Fact (P a).Prime]
    (g : ∀ a, ZMod (P a)) :
    productFrobenius l P (g : l.Product (fun a => ZMod (P a)))
      = ((fun a => (g a) ^ (P a) : ∀ a, ZMod (P a)) : l.Product (fun a => ZMod (P a))) :=
  rfl

/-- **The Fermat coordinatewise fact lifted to the ultraproduct.** The coordinatewise Frobenius
fixes every diagonal integer `d(n) = [(n mod p)_p]`, because `(n : ZMod p)^p = (n : ZMod p)` at every
prime `p` (`ZMod.pow_card`). This is NG1's Fermat witness at the level of the genuine dependent
ultraproduct object: the imported arithmetic is Frobenius-fixed. Note the proof uses no property of
the filter `l` (it holds at every coordinate), which is the machine-checked shadow of NG1's
limit-independence. -/
theorem productFrobenius_fixes_diag {α : Type*} (l : Filter α) (P : α → ℕ)
    [∀ a, Fact (P a).Prime] (n : ℤ) :
    productFrobenius l P ((fun a => (n : ZMod (P a)) : ∀ a, ZMod (P a)) :
        l.Product (fun a => ZMod (P a)))
      = ((fun a => (n : ZMod (P a)) : ∀ a, ZMod (P a)) : l.Product (fun a => ZMod (P a))) := by
  rw [productFrobenius_coe]
  rw [funext fun a => ZMod.pow_card (n : ZMod (P a))]

/-- The ultrafilter instantiation: `productFrobenius (↑U) P` is the coordinatewise Frobenius on the
genuine ultraproduct `∏_a ZMod (P a) / U`. Kept as a definitional alias to pin the object. -/
def ultraproductFrobenius {α : Type*} (U : Ultrafilter α) (P : α → ℕ) [∀ a, Fact (P a).Prime] :
    (↑U : Filter α).Product (fun a => ZMod (P a)) →
      (↑U : Filter α).Product (fun a => ZMod (P a)) :=
  productFrobenius (↑U) P

/-!
### The exact Mathlib wall (T2 partial, T4 blocked)

**T2 (#MTF-2), where Mathlib's infrastructure runs out.** The genuine object
`K = ∏_p \overline{𝔽}_p / 𝒰` is typeable as `Filter.Product (fun p => AlgebraicClosure (ZMod p)) (↑U)`
(or `Filter.Product (fun p => ZMod p) (↑U)` for the pseudofinite fixed-field skeleton). Mathlib
(`Mathlib.Order.Filter.Germ.Basic`) DOES provide this dependent quotient, and
`Mathlib.ModelTheory.Ultraproducts` equips it with `FirstOrder.Language.Ultraproduct.Structure`
(a model-theoretic `L.Structure`) plus Łoś's theorem. What is MISSING:

* there is NO `CommRing (Filter.Product l ε)` / `Field` / `IsAlgClosed` instance transported from the
  per-coordinate `CommRing (ZMod (P a))`. Mathlib bundles the ring structure on the NON-dependent
  `Filter.Germ l R` (used in fragment (A)) but not on the dependent `Filter.Product`. Consequently
  `productFrobenius` here is a bare function, NOT a `RingHom`, and "σ is a field automorphism",
  "`K` has characteristic 0", "`Fix σ` is the pseudofinite field `∏ ZMod p / U`" are unstateable at
  the `RingHom`/`Field` level without first transporting the ring structure through
  `FirstOrder.Language.ring` + `CompatibleRing` and Łoś. That transport is the concrete unbuilt
  bridge; it is feasible but multi-day, and is the exact wall for the full T2.

**T4 (#MTF-4), BLOCKED-ON-MATHLIB.** The NG2(iii) cardinality dichotomy ("every internal subset of
`K` is finite or of cardinality `≥ 2^{ℵ₀}`; countably infinite is excluded, so no internal set is
the prime-indexed diagonal") requires, in the model-theoretic phrasing, a notion of INTERNAL SET (a
definable-with-parameters subset, i.e. an ultraproduct of coordinate subsets) and the branching
argument that an ultraproduct of finite sets with unbounded sizes injects `{0,1}^ω`. The general
statement is the `κ`-saturation of ultraproducts over a countable index set. Mathlib has NONE of:

* a `Saturated` / `IsKappaSaturated` predicate on `FirstOrder.Language.Structure`;
* the type-space / type-realization machinery (`CompleteType`, realizing a type in a saturated
  model) needed to state "no countable set is definable over countable parameters";
* the internal-subset (ultraproduct-of-subsets) API on `Filter.Product`.

The bare cardinality lemma (ultraproduct of finite sets, sizes `→ ∞` along `U`, has cardinality
`≥ 2^{ℵ₀}`) is itself formalizable in principle via a branching injection into `Filter.Product`, but
even it needs the dependent-subset bookkeeping that is absent. Per the Pass-1 finding, T4 is marked
BLOCKED-ON-MATHLIB pending these definitions; a precise failure mode is the valid VERIFIER output
here, and building the saturation theory is out of scope for this pass.
-/

end ZetaRH.BorgerVacuity
