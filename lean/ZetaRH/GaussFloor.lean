/-
The Gauss-lemma height floor for prime-forced integer vanishers: the vF disc model
has no Siegel-lemma slot.

van Frankenhuijsen's Nevanlinna model of Spec(Z) x Spec(Z) (arXiv:0806.0044, Sec. 4;
reading note docs/03_research/reading_notes/vanFrankenhuijsen-2008-Nevanlinna-RH.md)
prescribes zeros of an integer-coefficient auxiliary function at z = 1/p for primes p.
This module machine-checks the model's height floor: any f in Z[z], f != 0, with
(pz - 1)^{m p} dividing f for each prime p in a finite set P satisfies

    prod_{p in P} p^{m p}  divides  lead(f),   hence   prod p^{m p} <= |lead(f)|,

and the canonical product prod (pz - 1)^{m p} attains the bound. With the vF
multiplicities m_p = floor(log_p x) the log of the floor is exactly Chebyshev psi(x),
so the minimal height of a prime-forced vanisher IS the quantity the transferred
Stepanov engine is supposed to bound: a pigeonhole (Siegel's lemma, S3) can never
construct below the floor, and the model's only open slot is the S4/R1
cheap-multiplicity operator (docs/03_research/stepanov_engine_audit.md).

Targets (all sorry-free, axiom-clean):
  #GF-1  leadingCoeff_linearFactor_pow : lead((pX - 1)^m) = p^m.
  #GF-2  pow_dvd_leadingCoeff : (pX - 1)^m | f  ==>  p^m | lead f. (Per-prime floor,
         via multiplicativity of the leading coefficient; no polynomial coprimality
         is needed anywhere: the primes are recombined on the INTEGER side.)
  #GF-3  prod_primePow_dvd_leadingCoeff : the divisibility floor over a finite set of
         primes (Finset.prod_dvd_of_coprime on pairwise-coprime prime powers).
  #GF-4  gauss_floor : the height form, prod p^{m p} <= |lead f| for f != 0, plus the
         equality witness canonical_leadingCoeff / canonical_attains_floor (the vF
         canonical product attains the floor, so it is sharp: log-form = psi(x)).
  #GF-5  gauss_floor_of_vanishing : the capstone from VANISHING data. The hypothesis
         is root multiplicity of f at 1/p over Q (where 1/p lives); the descent to
         Z[X]-divisibility is Gauss's lemma (linearFactor_pow_isPrimitive +
         dvd_of_map_dvd through the primitive part), then #GF-4.
  #GF-6  gauss_floor_rank_one : minimal-degree rigidity (the e2ah rank-one clause).
         canonical_dvd_of_vanishing shows the canonical product divides EVERY
         prime-forced vanisher (the root factors at the distinct points 1/p are
         pairwise coprime over Q; the linear factors pX - 1 are NOT coprime in
         Z[X], so the recombination is on the polynomial side), and any vanisher of
         degree at most D = sum m_p is an integer multiple of the canonical
         product: the vanisher lattice at the minimal degree has rank 1.

The floor is RH-independent, K1-clean (no zeros of zeta appear), and elementary; its
role in the program is a NO-GO coordinate, not a positivity statement. Numerical
companion: experiments/arithmetic_geometric/e2ah_gauss_floor.py (integer-exact;
canonical-product equality, cofactor stress, naive-interpolation stress all PASS).
-/

import Mathlib.Algebra.Polynomial.BigOperators
import Mathlib.Algebra.Polynomial.Div
import Mathlib.Algebra.Polynomial.RingDivision
import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.RingTheory.Polynomial.GaussLemma
import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Data.Nat.Prime.Basic

namespace ZetaRH.GaussFloor

open Polynomial

/-! ## #GF-1: the leading coefficient of the prime-forced factor -/

/-- The linear factor `p·X - 1` has leading coefficient `p` (for `p ≠ 0`). -/
lemma leadingCoeff_linearFactor {p : ℤ} (hp : p ≠ 0) :
    (C p * X - 1 : ℤ[X]).leadingCoeff = p := by
  have h : (C p * X - 1 : ℤ[X]) = C p * X + C (-1) := by
    rw [map_neg, map_one, sub_eq_add_neg]
  rw [h, leadingCoeff_linear hp]

/-- **#GF-1.** `lead((p·X - 1)^m) = p^m`: the leading coefficient is multiplicative
    over `ℤ[X]` (a domain), so the power of the primitive linear factor carries
    exactly the prime power. -/
lemma leadingCoeff_linearFactor_pow {p : ℤ} (hp : p ≠ 0) (m : ℕ) :
    ((C p * X - 1 : ℤ[X]) ^ m).leadingCoeff = p ^ m := by
  rw [leadingCoeff_pow, leadingCoeff_linearFactor hp]

/-! ## #GF-2: the single-prime floor -/

/-- **#GF-2.** If `(p·X - 1)^m ∣ f` in `ℤ[X]` then `p^m ∣ lead f`. The leading
    coefficient is a monoid hom on `ℤ[X]`, so divisibility of polynomials transfers
    to divisibility of leading coefficients. -/
theorem pow_dvd_leadingCoeff {p : ℤ} (hp : p ≠ 0) {m : ℕ} {f : ℤ[X]}
    (h : (C p * X - 1) ^ m ∣ f) : p ^ m ∣ f.leadingCoeff := by
  have hd := leadingCoeff_dvd_leadingCoeff h
  rwa [leadingCoeff_linearFactor_pow hp] at hd

/-! ## #GF-3: recombining the primes on the integer side -/

/-- Distinct prime powers are coprime in `ℤ`. -/
lemma isCoprime_primePow {p q : ℕ} (hp : p.Prime) (hq : q.Prime) (hne : p ≠ q)
    (a b : ℕ) : IsCoprime ((p : ℤ) ^ a) ((q : ℤ) ^ b) :=
  (Nat.isCoprime_iff_coprime.mpr ((Nat.coprime_primes hp hq).mpr hne)).pow

/-- **#GF-3 (the divisibility floor).** If `f ∈ ℤ[X]` is divisible by
    `(p·X - 1)^{m p}` for every prime `p` in a finite set `P`, then the full product
    `∏_{p ∈ P} p^{m p}` divides `lead f`. Each prime contributes through #GF-2, and
    the contributions recombine because distinct prime powers are coprime INTEGERS:
    no coprimality of the polynomial factors is needed. -/
theorem prod_primePow_dvd_leadingCoeff (f : ℤ[X]) (P : Finset ℕ) (m : ℕ → ℕ)
    (hP : ∀ p ∈ P, Nat.Prime p)
    (hdvd : ∀ p ∈ P, (C (p : ℤ) * X - 1) ^ m p ∣ f) :
    (∏ p ∈ P, (p : ℤ) ^ m p) ∣ f.leadingCoeff := by
  refine Finset.prod_dvd_of_coprime ?_ ?_
  · intro p hp q hq hne
    exact isCoprime_primePow (hP p (Finset.mem_coe.mp hp)) (hP q (Finset.mem_coe.mp hq))
      hne (m p) (m q)
  · intro p hp
    exact pow_dvd_leadingCoeff
      (Int.natCast_ne_zero.mpr (hP p hp).ne_zero) (hdvd p hp)

/-! ## #GF-4: the height floor and its equality case -/

/-- **#GF-4 (the height floor).** A nonzero `f ∈ ℤ[X]` divisible by the prime-forced
    factors has `|lead f| ≥ ∏_{p ∈ P} p^{m p}`. In log form with the vF multiplicities
    `m p = ⌊log_p x⌋` the right side is exactly Chebyshev `ψ(x)`: the minimal height
    of a prime-forced vanisher is the quantity to be bounded, so there is no
    Siegel-lemma slack in the disc model. -/
theorem gauss_floor (f : ℤ[X]) (hf : f ≠ 0) (P : Finset ℕ) (m : ℕ → ℕ)
    (hP : ∀ p ∈ P, Nat.Prime p)
    (hdvd : ∀ p ∈ P, (C (p : ℤ) * X - 1) ^ m p ∣ f) :
    (∏ p ∈ P, (p : ℤ) ^ m p) ≤ |f.leadingCoeff| :=
  Int.le_of_dvd (abs_pos.mpr (leadingCoeff_ne_zero.mpr hf))
    ((dvd_abs _ _).mpr (prod_primePow_dvd_leadingCoeff f P m hP hdvd))

/-- The canonical product's leading coefficient is exactly the floor. -/
theorem canonical_leadingCoeff (P : Finset ℕ) (m : ℕ → ℕ) (hP : ∀ p ∈ P, p ≠ 0) :
    (∏ p ∈ P, (C (p : ℤ) * X - 1) ^ m p).leadingCoeff = ∏ p ∈ P, (p : ℤ) ^ m p := by
  rw [leadingCoeff_prod]
  exact Finset.prod_congr rfl fun p hp =>
    leadingCoeff_linearFactor_pow (Int.natCast_ne_zero.mpr (hP p hp)) (m p)

/-- The canonical product is a genuine (nonzero) witness. -/
theorem canonical_ne_zero (P : Finset ℕ) (m : ℕ → ℕ) (hP : ∀ p ∈ P, p ≠ 0) :
    (∏ p ∈ P, (C (p : ℤ) * X - 1) ^ m p) ≠ 0 := by
  rw [← leadingCoeff_ne_zero, canonical_leadingCoeff P m hP]
  exact Finset.prod_ne_zero_iff.mpr fun p hp =>
    pow_ne_zero _ (Int.natCast_ne_zero.mpr (hP p hp))

/-- **The equality case**: the vF canonical product ATTAINS the floor,
    `|lead(∏ (p·X - 1)^{m p})| = ∏ p^{m p}`. The floor of #GF-4 is sharp; with the
    vF multiplicities, `log` of both sides is `ψ(x)`. -/
theorem canonical_attains_floor (P : Finset ℕ) (m : ℕ → ℕ) (hP : ∀ p ∈ P, p ≠ 0) :
    |(∏ p ∈ P, (C (p : ℤ) * X - 1) ^ m p).leadingCoeff| = ∏ p ∈ P, (p : ℤ) ^ m p := by
  rw [canonical_leadingCoeff P m hP, abs_of_nonneg]
  exact Finset.prod_nonneg fun p _ => pow_nonneg (Int.natCast_nonneg p) _

/-! ## #GF-5: from vanishing data to the floor (the Gauss's-lemma step)

    The model prescribes VANISHING at `z = 1/p`, which lives over `ℚ`; the floor
    needs divisibility over `ℤ`. The descent is Gauss's lemma: `(p·X - 1)^m` is
    primitive, so `ℚ[X]`-divisibility of `f` implies `ℤ[X]`-divisibility. -/

/-- `p·X - 1` is primitive: any constant divisor divides the constant coefficient
    `-1`, hence is a unit. -/
lemma linearFactor_isPrimitive (p : ℤ) : (C p * X - 1 : ℤ[X]).IsPrimitive := by
  intro r hr
  have h0 : r ∣ (C p * X - 1 : ℤ[X]).coeff 0 := (C_dvd_iff_dvd_coeff r _).mp hr 0
  have hc : (C p * X - 1 : ℤ[X]).coeff 0 = -1 := by simp
  rw [hc] at h0
  exact isUnit_of_dvd_unit h0 isUnit_one.neg

/-- Powers of the primitive linear factor are primitive (Gauss: content is
    multiplicative). -/
lemma linearFactor_pow_isPrimitive (p : ℤ) (m : ℕ) :
    ((C p * X - 1 : ℤ[X]) ^ m).IsPrimitive := by
  induction m with
  | zero => rw [pow_zero]; exact isPrimitive_one
  | succ n ih => rw [pow_succ]; exact ih.mul (linearFactor_isPrimitive p)

/-- **Gauss descent with only the divisor primitive.** If a primitive `g ∈ ℤ[X]`
    divides `f` over `ℚ`, it divides `f` over `ℤ`. (Mathlib's
    `IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast` needs both sides primitive; we
    route `f` through its primitive part, absorbing the content into a `ℚ`-unit.) -/
theorem dvd_of_map_dvd {g f : ℤ[X]} (hg : g.IsPrimitive)
    (h : g.map (Int.castRingHom ℚ) ∣ f.map (Int.castRingHom ℚ)) : g ∣ f := by
  rcases eq_or_ne f 0 with rfl | hf
  · exact dvd_zero g
  · have hcont : (f.content : ℚ) ≠ 0 := by
      exact_mod_cast content_eq_zero_iff.not.mpr hf
    have hmap : f.map (Int.castRingHom ℚ)
        = C (f.content : ℚ) * f.primPart.map (Int.castRingHom ℚ) := by
      conv_lhs => rw [f.eq_C_content_mul_primPart]
      rw [Polynomial.map_mul, map_C]
      norm_num
    have hunit : IsUnit (C (f.content : ℚ)) :=
      isUnit_C.mpr (isUnit_iff_ne_zero.mpr hcont)
    have h' : g.map (Int.castRingHom ℚ) ∣ f.primPart.map (Int.castRingHom ℚ) := by
      rwa [hmap, hunit.dvd_mul_left] at h
    exact ((IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast g f.primPart hg
      f.isPrimitive_primPart).mpr h').trans f.primPart_dvd

/-- **#GF-5 (the Gauss's-lemma step).** If `f ∈ ℤ[X]` vanishes at `1/p` over `ℚ`
    with multiplicity at least `m` (stated via `rootMultiplicity`), then
    `(p·X - 1)^m ∣ f` in `ℤ[X]`. Over `ℚ`, `p·X - 1 = C p · (X - C p⁻¹)` is a unit
    multiple of the root factor; primitivity descends the divisibility to `ℤ`. -/
theorem linearFactor_pow_dvd_of_rootMultiplicity {p : ℕ} (hp : p ≠ 0) {f : ℤ[X]}
    {m : ℕ} (h : m ≤ rootMultiplicity ((p : ℚ)⁻¹) (f.map (Int.castRingHom ℚ))) :
    (C (p : ℤ) * X - 1) ^ m ∣ f := by
  have hpQ : (p : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hp
  have h1 : (X - C ((p : ℚ)⁻¹)) ^ m ∣ f.map (Int.castRingHom ℚ) :=
    (pow_dvd_pow _ h).trans (pow_rootMultiplicity_dvd _ _)
  have hfac : ((C (p : ℤ) * X - 1 : ℤ[X]) ^ m).map (Int.castRingHom ℚ)
      = C ((p : ℚ) ^ m) * (X - C ((p : ℚ)⁻¹)) ^ m := by
    rw [Polynomial.map_pow, Polynomial.map_sub, Polynomial.map_mul, map_C,
      Polynomial.map_X, Polynomial.map_one, C_pow, ← mul_pow]
    congr 1
    rw [mul_sub, ← C_mul, mul_inv_cancel₀ hpQ, C_1]
    norm_num
  have hunit : IsUnit (C ((p : ℚ) ^ m)) :=
    isUnit_C.mpr (isUnit_iff_ne_zero.mpr (pow_ne_zero m hpQ))
  refine dvd_of_map_dvd (linearFactor_pow_isPrimitive _ m) ?_
  rw [hfac, hunit.mul_left_dvd]
  exact h1

/-- **The capstone: the Gauss-lemma floor from vanishing data.** If a nonzero
    `f ∈ ℤ[X]` vanishes at `1/p` (over `ℚ`) with multiplicity at least `m p` for
    every prime `p ∈ P`, then `∏_{p ∈ P} p^{m p} ≤ |lead f|`. With the vF
    multiplicities `m p = ⌊log_p x⌋`, the log form reads
    `log |lead f| ≥ ψ(x)`: in the disc model, ANY auxiliary function with the
    required vanishing already has height at least the quantity the engine must
    bound. No Siegel-lemma savings exist; the only open slot is the S4/R1
    cheap-multiplicity operator. -/
theorem gauss_floor_of_vanishing (f : ℤ[X]) (hf : f ≠ 0) (P : Finset ℕ) (m : ℕ → ℕ)
    (hP : ∀ p ∈ P, Nat.Prime p)
    (hvan : ∀ p ∈ P,
      m p ≤ rootMultiplicity ((p : ℚ)⁻¹) (f.map (Int.castRingHom ℚ))) :
    (∏ p ∈ P, (p : ℤ) ^ m p) ≤ |f.leadingCoeff| :=
  gauss_floor f hf P m hP fun p hp =>
    linearFactor_pow_dvd_of_rootMultiplicity (hP p hp).ne_zero (hvan p hp)

/-! ## #GF-6: minimal-degree rigidity (the rank-one clause)

    At the minimal degree `D = ∑ m p` the integer vanisher lattice is rank 1: the
    canonical product divides every prime-forced vanisher (the root factors at the
    distinct points `1/p` are pairwise coprime over `ℚ`, and the product descends
    by primitivity), so any vanisher of degree at most `D` is an integer multiple
    of the canonical product. Numerical companion: the minimal-degree rigidity
    probe in `experiments/arithmetic_geometric/e2ah_gauss_floor.py`. -/

/-- The `ℚ`-factorization of the mapped prime factor: `(p·X - 1)^m` maps to the
unit `C (p^m)` times the root factor `(X - C (1/p))^m`. (The `hfac` step of #GF-5,
extracted as a standalone lemma.) -/
lemma map_linearFactor_pow {p : ℕ} (hp : p ≠ 0) (m : ℕ) :
    ((C (p : ℤ) * X - 1 : ℤ[X]) ^ m).map (Int.castRingHom ℚ)
      = C ((p : ℚ) ^ m) * (X - C ((p : ℚ)⁻¹)) ^ m := by
  have hpQ : (p : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hp
  rw [Polynomial.map_pow, Polynomial.map_sub, Polynomial.map_mul, map_C,
    Polynomial.map_X, Polynomial.map_one, C_pow, ← mul_pow]
  congr 1
  rw [mul_sub, ← C_mul, mul_inv_cancel₀ hpQ, C_1]
  norm_num

/-- **The canonical product divides every prime-forced vanisher.** If `f ∈ ℤ[X]`
vanishes at `1/p` over `ℚ` with multiplicity at least `m p` for every prime
`p ∈ P`, then `∏_{p ∈ P} (p·X - 1)^{m p} ∣ f` in `ℤ[X]`. The root factors at the
distinct points `1/p` are pairwise coprime over `ℚ` (the recombination is on the
POLYNOMIAL side; the linear factors `p·X - 1` themselves are NOT pairwise coprime
in `ℤ[X]`, e.g. `2X - 1 ≡ 5X - 1 mod 3`), and the product descends to `ℤ[X]` by
primitivity. -/
theorem canonical_dvd_of_vanishing (f : ℤ[X]) (P : Finset ℕ) (m : ℕ → ℕ)
    (hP : ∀ p ∈ P, Nat.Prime p)
    (hvan : ∀ p ∈ P,
      m p ≤ rootMultiplicity ((p : ℚ)⁻¹) (f.map (Int.castRingHom ℚ))) :
    (∏ p ∈ P, (C (p : ℤ) * X - 1) ^ m p) ∣ f := by
  refine dvd_of_map_dvd
    (Finset.prod_induction _ IsPrimitive (fun a b ha hb => ha.mul hb)
      isPrimitive_one fun p _ => linearFactor_pow_isPrimitive _ (m p)) ?_
  have hmap : (∏ p ∈ P, (C (p : ℤ) * X - 1) ^ m p).map (Int.castRingHom ℚ)
      = (∏ p ∈ P, C ((p : ℚ) ^ m p))
        * ∏ p ∈ P, (X - C ((p : ℚ)⁻¹)) ^ m p := by
    rw [Polynomial.map_prod, ← Finset.prod_mul_distrib]
    exact Finset.prod_congr rfl fun p hp =>
      map_linearFactor_pow (hP p hp).ne_zero (m p)
  have hunit : IsUnit (∏ p ∈ P, C ((p : ℚ) ^ m p)) :=
    Finset.prod_induction _ IsUnit (fun a b ha hb => ha.mul hb) isUnit_one
      fun p hp => isUnit_C.mpr (isUnit_iff_ne_zero.mpr
        (pow_ne_zero _ (Nat.cast_ne_zero.mpr (hP p hp).ne_zero)))
  rw [hmap, hunit.mul_left_dvd]
  refine Finset.prod_dvd_of_coprime ?_ fun p hp =>
    (pow_dvd_pow _ (hvan p hp)).trans (pow_rootMultiplicity_dvd _ _)
  intro p hp q hq hne
  have hinv : ((p : ℚ))⁻¹ ≠ ((q : ℚ))⁻¹ := fun h =>
    hne (Nat.cast_injective (inv_injective h))
  exact (isCoprime_X_sub_C_of_isUnit_sub (sub_ne_zero_of_ne hinv).isUnit).pow

/-- The canonical product has degree exactly `∑ m p`. -/
theorem canonical_natDegree (P : Finset ℕ) (m : ℕ → ℕ) (hP : ∀ p ∈ P, p ≠ 0) :
    (∏ p ∈ P, (C (p : ℤ) * X - 1) ^ m p).natDegree = ∑ p ∈ P, m p := by
  have hne : ∀ p ∈ P, ((C (p : ℤ) * X - 1 : ℤ[X]) ^ m p) ≠ 0 := fun p hp =>
    pow_ne_zero _ (leadingCoeff_ne_zero.mp (by
      rw [leadingCoeff_linearFactor (Int.natCast_ne_zero.mpr (hP p hp))]
      exact Int.natCast_ne_zero.mpr (hP p hp)))
  rw [natDegree_prod (h := hne)]
  refine Finset.sum_congr rfl fun p hp => ?_
  have h1 : (C (p : ℤ) * X - 1 : ℤ[X]).natDegree = 1 := by
    have h : (C (p : ℤ) * X - 1 : ℤ[X]) = C (p : ℤ) * X + C (-1) := by
      rw [map_neg, map_one, sub_eq_add_neg]
    rw [h, natDegree_linear (Int.natCast_ne_zero.mpr (hP p hp))]
  rw [natDegree_pow, h1, mul_one]

/-- **#GF-6 (minimal-degree rigidity: the vanisher lattice at degree `D` has rank
one).** If a prime-forced vanisher `f` has degree at most `D = ∑_{p ∈ P} m p` (the
degree of the canonical product), then `f` IS an integer multiple of the canonical
product. Together with #GF-4 (the height floor, attained exactly by the canonical
product) this pins the minimal-degree stratum completely: one lattice generator,
height exactly `ψ(x)` in the vF reading. -/
theorem gauss_floor_rank_one (f : ℤ[X]) (P : Finset ℕ) (m : ℕ → ℕ)
    (hP : ∀ p ∈ P, Nat.Prime p)
    (hvan : ∀ p ∈ P,
      m p ≤ rootMultiplicity ((p : ℚ)⁻¹) (f.map (Int.castRingHom ℚ)))
    (hdeg : f.natDegree ≤ ∑ p ∈ P, m p) :
    ∃ n : ℤ, f = C n * ∏ p ∈ P, (C (p : ℤ) * X - 1) ^ m p := by
  obtain ⟨h, hh⟩ := canonical_dvd_of_vanishing f P m hP hvan
  rcases eq_or_ne f 0 with rfl | hf
  · exact ⟨0, by simp⟩
  · have hP0 : ∀ p ∈ P, p ≠ 0 := fun p hp => (hP p hp).ne_zero
    have hcan0 : (∏ p ∈ P, (C (p : ℤ) * X - 1) ^ m p) ≠ 0 :=
      canonical_ne_zero P m hP0
    have hh0 : h ≠ 0 := fun h0 => hf (by rw [hh, h0, mul_zero])
    have hdeg' : f.natDegree = (∑ p ∈ P, m p) + h.natDegree := by
      rw [hh, natDegree_mul hcan0 hh0, canonical_natDegree P m hP0]
    have hd0 : h.natDegree = 0 := by omega
    refine ⟨h.coeff 0, ?_⟩
    have hC : h = C (h.coeff 0) := eq_C_of_natDegree_eq_zero hd0
    conv_lhs => rw [hh, hC]
    exact mul_comm _ _

-- Axiom audits (expected: [propext, Classical.choice, Quot.sound], no sorryAx):
#print axioms prod_primePow_dvd_leadingCoeff
#print axioms gauss_floor
#print axioms canonical_attains_floor
#print axioms gauss_floor_of_vanishing
#print axioms canonical_dvd_of_vanishing
#print axioms gauss_floor_rank_one

end ZetaRH.GaussFloor
