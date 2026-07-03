/-
The rational root theorem with multiplicity: the denominator-power floor on the
leading coefficient, in Mathlib's `IsFractionRing.den` idiom.

Mathlib's rational root theorem (`Mathlib/RingTheory/Polynomial/RationalRoot.lean`,
`num_dvd_of_is_root` / `den_dvd_of_is_root`) is the multiplicity-one statement: if
`r` in the fraction field `K` of a UFD `A` is a root of `p : A[X]`, then
`den A r ∣ p.leadingCoeff`. This module proves the multiplicity generalization in
the same typeclass context (`UniqueFactorizationMonoid A`, `IsFractionRing A K`),
so the declarations can be lifted into that file nearly verbatim. This is the P10
FORMAL-axis deliverable; the prior-art check (2026-07-02, SURVEYOR:
`scratchpad/counting_roads_followup/02_surveyor_mathlib_prior_art.md`) found no
multiplicity-aware or multi-point variant in Mathlib master, open PRs, or indexed
Zulip, with a Loogle absence certificate. Verdict there: CLEAR-TO-PR.

Targets (all sorry-free, axiom-clean):
  #RR-1  den_pow_rootMultiplicity_dvd_leadingCoeff : for `p : A[X]` and `r : K`,
         `(den A r)^(rootMultiplicity r (p.map (algebraMap A K))) ∣ p.leadingCoeff`.
         Unconditional: at multiplicity 0 (non-root, or `p = 0`) it is trivial, and
         at multiplicity 1 it recovers `den_dvd_of_is_root` (guard `example` below).
  #RR-2  prod_den_pow_rootMultiplicity_dvd_leadingCoeff : the multi-point version
         over any `s : Finset K`. NOTE: the denominators of distinct points need
         NOT be coprime in `A` (over `ℤ`: `1/4` and `3/4` share the denominator 4),
         so the product cannot be recombined on the `A` side as in GaussFloor #GF-3;
         the honest route is the polynomial side, where the root factors `X - C r`
         at distinct points are pairwise coprime over the field `K`.

Proof route (the GaussFloor.lean route generalized from `ℤ` to a UFD): the reduced
linear factor `C (den A r) * X - C (num A r)` is primitive because num and den are
reduced (`num_den_reduced`); over `K` it is a unit multiple of `X - C r`, so its
`rootMultiplicity` power divides `p.map (algebraMap A K)`; Gauss's lemma descends
the divisibility to `A[X]` (one-sided: only the divisor needs to be primitive,
`dvd_of_fraction_map_dvd` below, routing `p` through its primitive part); and
multiplicativity of the leading coefficient finishes. The `NormalizedGCDMonoid`
structure that Mathlib's content/primitive-part machinery uses is obtained inside
the proofs from the instance `Nonempty (NormalizedGCDMonoid A)` (available for any
UFD), so the public statements assume only `UniqueFactorizationMonoid A`, exactly
matching RationalRoot.lean.

Companion: `GaussFloor.lean` (#GF-1..#GF-6) instantiates this floor at the prime
points `1/p` (the vF disc-model no-Siegel-lemma floor; log form = Chebyshev psi).
-/

import Mathlib.RingTheory.Polynomial.RationalRoot
import Mathlib.RingTheory.Polynomial.GaussLemma
import Mathlib.Algebra.Polynomial.BigOperators
import Mathlib.Algebra.Polynomial.Div
import Mathlib.Algebra.Polynomial.RingDivision
import Mathlib.RingTheory.Coprime.Lemmas

namespace ZetaRH.RationalRootFloor

open Polynomial IsFractionRing

variable {A K : Type*} [CommRing A] [IsDomain A] [UniqueFactorizationMonoid A]
variable [Field K] [Algebra A K] [IsFractionRing A K]

/-! ## Primitivity helpers (Mathlib target: `RingTheory/Polynomial/Content.lean`) -/

-- The linter flags `IsDomain A` as unused in the two primitivity helpers, but it
-- cannot be omitted: it is needed to state `UniqueFactorizationMonoid A` (via
-- `CancelCommMonoidWithZero A`).
set_option linter.unusedSectionVars false in
/-- Powers of a primitive polynomial over a UFD are primitive.
Intended Mathlib name: `Polynomial.IsPrimitive.pow`. -/
theorem isPrimitive_pow {q : A[X]} (hq : q.IsPrimitive) (n : ℕ) :
    (q ^ n).IsPrimitive := by
  letI : NormalizedGCDMonoid A := Nonempty.some inferInstance
  induction n with
  | zero => rw [pow_zero]; exact isPrimitive_one
  | succ k ih => rw [pow_succ]; exact ih.mul hq

set_option linter.unusedSectionVars false in
/-- Finite products of primitive polynomials over a UFD are primitive.
Intended Mathlib name: `Polynomial.isPrimitive_prod`. -/
theorem isPrimitive_prod {ι : Type*} (t : Finset ι) (f : ι → A[X])
    (h : ∀ i ∈ t, (f i).IsPrimitive) : (∏ i ∈ t, f i).IsPrimitive := by
  letI : NormalizedGCDMonoid A := Nonempty.some inferInstance
  exact Finset.prod_induction f IsPrimitive (fun a b ha hb => ha.mul hb)
    isPrimitive_one h

/-! ## One-sided Gauss descent
(Mathlib target: `RingTheory/Polynomial/GaussLemma.lean`) -/

/-- **One-sided Gauss descent.** If a primitive `g : A[X]` divides `f` over the
fraction field, it divides `f` over `A`. This relaxes the two-sided primitivity
hypothesis of `Polynomial.IsPrimitive.dvd_of_fraction_map_dvd_fraction_map` by
routing `f` through its primitive part (the content becomes a unit in `K[X]`).
Intended Mathlib name: `Polynomial.IsPrimitive.dvd_of_fraction_map_dvd`. -/
theorem dvd_of_fraction_map_dvd {g f : A[X]} (hg : g.IsPrimitive)
    (h : g.map (algebraMap A K) ∣ f.map (algebraMap A K)) : g ∣ f := by
  letI : NormalizedGCDMonoid A := Nonempty.some inferInstance
  rcases eq_or_ne f 0 with rfl | hf
  · exact dvd_zero g
  · have hcont0 : f.content ≠ 0 := fun h0 => hf (content_eq_zero_iff.mp h0)
    have hcont : algebraMap A K f.content ≠ 0 := fun h0 =>
      hcont0 (IsFractionRing.injective A K (h0.trans (map_zero (algebraMap A K)).symm))
    have hmap : f.map (algebraMap A K)
        = C (algebraMap A K f.content) * f.primPart.map (algebraMap A K) := by
      conv_lhs => rw [f.eq_C_content_mul_primPart]
      rw [Polynomial.map_mul, map_C]
    have hunit : IsUnit (C (algebraMap A K f.content)) :=
      isUnit_C.mpr (isUnit_iff_ne_zero.mpr hcont)
    have h' : g.map (algebraMap A K) ∣ f.primPart.map (algebraMap A K) := by
      rwa [hmap, hunit.dvd_mul_left] at h
    exact (hg.dvd_of_fraction_map_dvd_fraction_map f.isPrimitive_primPart h').trans
      f.primPart_dvd

/-! ## The reduced linear factor of `r : K`
(Mathlib target: `RingTheory/Polynomial/RationalRoot.lean`) -/

/-- The reduced linear factor `C (den A r) * X - C (num A r)` is primitive: a
constant divisor divides both `den A r` (the coefficient of `X`) and `num A r` (up
to sign, the constant coefficient), and num/den are reduced (`num_den_reduced`). -/
theorem isPrimitive_den_mul_X_sub_C_num (r : K) :
    (C (den A r : A) * X - C (num A r)).IsPrimitive := by
  intro c hc
  have h1 : c ∣ (den A r : A) := by
    have h := (C_dvd_iff_dvd_coeff c _).mp hc 1
    simpa using h
  have h0 : c ∣ num A r := by
    have h := (C_dvd_iff_dvd_coeff c _).mp hc 0
    simpa using h
  exact num_den_reduced A r h0 h1

/-- Over `K`, the reduced linear factor of `r` is the unit multiple
`C (den A r) * (X - C r)` of the root factor at `r`. -/
theorem map_den_mul_X_sub_C_num (r : K) :
    (C (den A r : A) * X - C (num A r)).map (algebraMap A K)
      = C (algebraMap A K (den A r : A)) * (X - C r) := by
  have hden0 : algebraMap A K (den A r : A) ≠ 0 :=
    IsFractionRing.to_map_ne_zero_of_mem_nonZeroDivisors (den A r).2
  have hnum : algebraMap A K (num A r) = r * algebraMap A K (den A r : A) :=
    (div_eq_iff hden0).mp (mk'_num_den' A r)
  rw [Polynomial.map_sub, Polynomial.map_mul, map_C, map_C, Polynomial.map_X,
    hnum, C_mul]
  ring

/-- The leading coefficient of the reduced linear factor is `den A r`. -/
theorem leadingCoeff_den_mul_X_sub_C_num (r : K) :
    (C (den A r : A) * X - C (num A r)).leadingCoeff = (den A r : A) := by
  have h : C (den A r : A) * X - C (num A r)
      = C (den A r : A) * X + C (-(num A r)) := by
    rw [map_neg, sub_eq_add_neg]
  rw [h, leadingCoeff_linear (nonZeroDivisors.coe_ne_zero _)]

/-- The `rootMultiplicity` power of the reduced linear factor divides `p` over `A`:
over `K` the factor is a unit multiple of `X - C r`, whose `rootMultiplicity` power
divides `p.map (algebraMap A K)`, and primitivity descends the divisibility. -/
theorem den_mul_X_sub_C_num_pow_rootMultiplicity_dvd (p : A[X]) (r : K) :
    (C (den A r : A) * X - C (num A r))
      ^ rootMultiplicity r (p.map (algebraMap A K)) ∣ p := by
  refine dvd_of_fraction_map_dvd (K := K)
    (isPrimitive_pow (isPrimitive_den_mul_X_sub_C_num r) _) ?_
  rw [Polynomial.map_pow, map_den_mul_X_sub_C_num, mul_pow]
  have hunit : IsUnit (C (algebraMap A K (den A r : A))
      ^ rootMultiplicity r (p.map (algebraMap A K))) :=
    (isUnit_C.mpr (isUnit_iff_ne_zero.mpr
      (IsFractionRing.to_map_ne_zero_of_mem_nonZeroDivisors (den A r).2))).pow _
  rw [hunit.mul_left_dvd]
  exact pow_rootMultiplicity_dvd _ r

/-! ## The main statements -/

/-- **Rational root theorem with multiplicity** (#RR-1). If `r : K` is a root of
`p : A[X]` over the fraction field `K` of the UFD `A` with multiplicity `m`, then
`(den A r) ^ m` divides the leading coefficient of `p`. Stated unconditionally with
`m = rootMultiplicity r (p.map (algebraMap A K))`; at `m = 1` it recovers
`den_dvd_of_is_root`. Intended Mathlib name:
`Polynomial.den_pow_rootMultiplicity_dvd_leadingCoeff`
(`RingTheory/Polynomial/RationalRoot.lean`). -/
theorem den_pow_rootMultiplicity_dvd_leadingCoeff (p : A[X]) (r : K) :
    (den A r : A) ^ rootMultiplicity r (p.map (algebraMap A K))
      ∣ p.leadingCoeff := by
  have h := leadingCoeff_dvd_leadingCoeff
    (den_mul_X_sub_C_num_pow_rootMultiplicity_dvd p r)
  rwa [leadingCoeff_pow, leadingCoeff_den_mul_X_sub_C_num] at h

/-- **Multi-point rational root theorem with multiplicities** (#RR-2). For any
finite set `s` of points of the fraction field, the product over `r ∈ s` of
`(den A r) ^ rootMultiplicity r` divides the leading coefficient of `p`. The
denominators need NOT be pairwise coprime in `A`; the recombination happens on the
polynomial side, where the root factors at distinct points are pairwise coprime
over the field `K`. Intended Mathlib name:
`Polynomial.prod_den_pow_rootMultiplicity_dvd_leadingCoeff`. -/
theorem prod_den_pow_rootMultiplicity_dvd_leadingCoeff (p : A[X]) (s : Finset K) :
    (∏ r ∈ s, (den A r : A) ^ rootMultiplicity r (p.map (algebraMap A K)))
      ∣ p.leadingCoeff := by
  have hgdvd : (∏ r ∈ s, (C (den A r : A) * X - C (num A r))
      ^ rootMultiplicity r (p.map (algebraMap A K))) ∣ p := by
    refine dvd_of_fraction_map_dvd (K := K)
      (isPrimitive_prod _ _ fun r _ =>
        isPrimitive_pow (isPrimitive_den_mul_X_sub_C_num r) _) ?_
    have hmap : (∏ r ∈ s, (C (den A r : A) * X - C (num A r))
          ^ rootMultiplicity r (p.map (algebraMap A K))).map (algebraMap A K)
        = (∏ r ∈ s, C (algebraMap A K (den A r : A))
              ^ rootMultiplicity r (p.map (algebraMap A K)))
            * ∏ r ∈ s, (X - C r) ^ rootMultiplicity r (p.map (algebraMap A K)) := by
      rw [Polynomial.map_prod, ← Finset.prod_mul_distrib]
      refine Finset.prod_congr rfl fun r _ => ?_
      rw [Polynomial.map_pow, map_den_mul_X_sub_C_num, mul_pow]
    have hunit : IsUnit (∏ r ∈ s, C (algebraMap A K (den A r : A))
        ^ rootMultiplicity r (p.map (algebraMap A K))) :=
      Finset.prod_induction _ IsUnit (fun a b ha hb => ha.mul hb) isUnit_one
        fun r _ => (isUnit_C.mpr (isUnit_iff_ne_zero.mpr
          (IsFractionRing.to_map_ne_zero_of_mem_nonZeroDivisors (den A r).2))).pow _
    rw [hmap, hunit.mul_left_dvd]
    refine Finset.prod_dvd_of_coprime ?_ fun r _ => pow_rootMultiplicity_dvd _ r
    intro a _ b _ hab
    exact (isCoprime_X_sub_C_of_isUnit_sub (sub_ne_zero_of_ne hab).isUnit).pow
  have hleadeq : (∏ r ∈ s, (C (den A r : A) * X - C (num A r))
        ^ rootMultiplicity r (p.map (algebraMap A K))).leadingCoeff
      = ∏ r ∈ s, (den A r : A) ^ rootMultiplicity r (p.map (algebraMap A K)) := by
    rw [leadingCoeff_prod]
    exact Finset.prod_congr rfl fun r _ => by
      rw [leadingCoeff_pow, leadingCoeff_den_mul_X_sub_C_num]
  rw [← hleadeq]
  exact leadingCoeff_dvd_leadingCoeff hgdvd

/-! ## Consistency and instantiation guards -/

/-- Guard: #RR-1 recovers the multiplicity-one theorem `den_dvd_of_is_root`. -/
example {p : A[X]} (hp : p ≠ 0) {r : K} (hr : aeval r p = 0) :
    (den A r : A) ∣ p.leadingCoeff := by
  have hmap0 : p.map (algebraMap A K) ≠ 0 :=
    (Polynomial.map_ne_zero_iff (IsFractionRing.injective A K)).mpr hp
  have hroot : IsRoot (p.map (algebraMap A K)) r := by
    show eval r (p.map (algebraMap A K)) = 0
    rw [eval_map, ← aeval_def]
    exact hr
  have hpos : 0 < rootMultiplicity r (p.map (algebraMap A K)) :=
    (rootMultiplicity_pos hmap0).mpr hroot
  exact (dvd_pow_self _ hpos.ne').trans
    (den_pow_rootMultiplicity_dvd_leadingCoeff p r)

/-- Guard: the `ℤ/ℚ` instantiation typechecks (the classical rational root floor). -/
example (p : ℤ[X]) (r : ℚ) :
    (den ℤ r : ℤ) ^ rootMultiplicity r (p.map (algebraMap ℤ ℚ))
      ∣ p.leadingCoeff :=
  den_pow_rootMultiplicity_dvd_leadingCoeff p r

-- Axiom audits (expected: [propext, Classical.choice, Quot.sound], no sorryAx):
#print axioms dvd_of_fraction_map_dvd
#print axioms den_pow_rootMultiplicity_dvd_leadingCoeff
#print axioms prod_den_pow_rootMultiplicity_dvd_leadingCoeff

end ZetaRH.RationalRootFloor
