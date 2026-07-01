/-
The general-degree Cohn criterion (#SC-3 / #SC-4 / #SC-5), built on Gauss-Lucas.

  #SC-3 (Gauss-Lucas): every root of `derivative p` lies in the convex hull of the
        roots of `p`. Mathlib ALREADY HAS THIS as
        `Polynomial.rootSet_derivative_subset_convexHull_rootSet`
        (Mathlib.Analysis.Complex.Polynomial.GaussLucas); we use it directly.
        No new code needed for SC-3.

  #SC-4 (Cohn forward, `derivative_roots_in_disk`): if every root of a nonconstant
        `p : Polynomial C` lies ON the unit circle (`normSq z = 1`), then every root
        of `derivative p` lies in the closed unit disk (`normSq w <= 1`). Proof: the
        closed unit ball is convex and contains the roots, hence their convex hull;
        apply Gauss-Lucas.

  #SC-5 (Cohn converse, `cohn_converse` / `cohn_converse_real` / `cohn_criterion`):
        for self-inversive `p` (`reflect (natDegree p) p = p`) with conj-fixed
        (real) coefficients and `natDegree p >= 1`: if every root of `derivative p`
        has `normSq <= 1`, then every root of `p` has `normSq = 1`. The proof route:
        (i)   the factor identity
              `normSq (1 - conj r * z) - normSq (z - r) = (1 - normSq r)(1 - normSq z)`;
        (ii)  reflection dominance: for `g` with all roots in the closed disk and
              `normSq z <= 1`, `normSq (g.eval z) <= normSq (gStar.eval z)` where
              `gStar = reflect (natDegree g) (g.map conj)`, proved factor-by-factor
              through the eval-level product form
              `gStar.eval z = conj (lead g) * prod (1 - conj r_i * z)`;
        (iii) the pinch: at a root `w` of `p` with `normSq w < 1`, the #SC-2 reversal
              identity gives `gStar.eval w = -(w * g.eval w)` for `g = derivative p`,
              so dominance forces `g.eval w = 0`, hence `gStar.eval w = 0`; but the
              product form shows `gStar` has NO root strictly inside the disk.
              Contradiction, so `p` has no root strictly inside;
        (iv)  self-inversive pairing: a root strictly outside pairs with the root
              `1/z` strictly inside (via `eval₂_reflect_mul_pow`), contradiction.
        Note `p(0) != 0` is automatic: palindromic coefficients give
        `p.coeff 0 = p.leadingCoeff != 0`, so no such hypothesis is needed.

  The capstone `cohn_criterion` is the general-degree statement whose genus-1 shadow
  is #SC-1 (`schur_cohn_certifies_circle`): for real self-inversive `q` of degree
  >= 1, all roots of `q` on the unit circle IFF all roots of `q'` in the closed
  unit disk. This is the certificate the toy grader's higher-genus L-polynomials
  need (the Schur-Cohn test on the derivative decides Weil positivity).
-/

import ZetaRH.SchurCohn
import Mathlib.Analysis.Complex.Polynomial.GaussLucas
import Mathlib.Analysis.Normed.Module.Convex

namespace ZetaRH.SchurCohn

open Polynomial Complex ComplexConjugate

/-! ## #SC-4: Cohn forward (roots on circle force derivative roots in the disk) -/

/-- **Cohn forward (#SC-4).** If every root of a nonconstant `p : Polynomial C` lies on
    the unit circle, then every root of `derivative p` lies in the closed unit disk.
    Immediate from Gauss-Lucas (#SC-3, Mathlib's
    `rootSet_derivative_subset_convexHull_rootSet`): the closed unit ball is convex and
    contains the roots of `p`, hence their convex hull, hence the roots of `p'`. -/
theorem derivative_roots_in_disk {p : ℂ[X]} (hn : 1 ≤ p.natDegree)
    (hroots : ∀ z : ℂ, p.eval z = 0 → normSq z = 1) :
    ∀ w : ℂ, (derivative p).eval w = 0 → normSq w ≤ 1 := by
  intro w hw
  have hdeg : 0 < p.degree := natDegree_pos_iff_degree_pos.mp (by omega)
  have hd0 : derivative p ≠ 0 := by
    intro h
    have h0 := natDegree_eq_zero_of_derivative_eq_zero h
    omega
  have hw' : w ∈ (derivative p).rootSet ℂ := by
    rw [mem_rootSet, coe_aeval_eq_eval]
    exact ⟨hd0, hw⟩
  have hmem : w ∈ convexHull ℝ (p.rootSet ℂ) :=
    rootSet_derivative_subset_convexHull_rootSet hdeg hw'
  have hsub : p.rootSet ℂ ⊆ Metric.closedBall (0 : ℂ) 1 := by
    intro z hz
    rw [mem_rootSet, coe_aeval_eq_eval] at hz
    have h1 : ‖z‖ ^ 2 = 1 := by rw [← normSq_eq_norm_sq]; exact hroots z hz.2
    rw [Metric.mem_closedBall, dist_zero_right]
    nlinarith [norm_nonneg z]
  have hball : w ∈ Metric.closedBall (0 : ℂ) 1 :=
    convexHull_min hsub (convex_closedBall _ _) hmem
  rw [Metric.mem_closedBall, dist_zero_right] at hball
  rw [normSq_eq_norm_sq]
  nlinarith [norm_nonneg w]

/-! ## #SC-5 step (i): the elementary factor identity -/

/-- **The factor identity.** For any `r z : C`,
    `normSq (1 - conj r * z) - normSq (z - r) = (1 - normSq r) * (1 - normSq z)`.
    Pure algebra on real and imaginary parts. This is the Blaschke-factor inequality
    engine: both factors on the right are nonnegative on the closed disk. -/
theorem normSq_factor_identity (r z : ℂ) :
    normSq (1 - conj r * z) - normSq (z - r) = (1 - normSq r) * (1 - normSq z) := by
  simp only [normSq_apply, sub_re, sub_im, mul_re, mul_im, one_re, one_im, conj_re, conj_im]
  ring

/-! ## #SC-5 step (ii): the product form of the conjugate-reflection -/

/-- Reflecting a product of monic linear factors `X - r` turns each factor into
    `1 - r * X`. Proved by multiset induction with `reflect_mul`. -/
theorem reflect_multiset_prod_X_sub_C (s : Multiset ℂ) :
    reflect (Multiset.card s) ((s.map fun r => X - C r).prod)
      = (s.map fun r => 1 - C r * X).prod := by
  induction s using Multiset.induction_on with
  | empty => simp
  | cons a t ih =>
    simp only [Multiset.map_cons, Multiset.prod_cons, Multiset.card_cons]
    rw [add_comm (Multiset.card t) 1,
      reflect_mul _ _ (natDegree_X_sub_C_le a) (natDegree_multiset_prod_X_sub_C_eq_card t).le,
      ih, reflect_sub, reflect_one_X, reflect_C, pow_one]

/-- **The product form of the conjugate-reflection.** For any `g : Polynomial C`,
    `reflect (natDegree g) (g.map conj) = conj (lead g) * prod_i (1 - conj r_i * X)`
    where the `r_i` are the roots of `g` with multiplicity. This is the polynomial
    `gStar` of the classical Cohn argument, with the degree-drop bookkeeping
    (`g(0) = 0` reflecting to a lost degree) handled by the splitting itself. -/
theorem reflect_conj_prod_form (g : ℂ[X]) :
    reflect g.natDegree (g.map (starRingEnd ℂ))
      = C (conj g.leadingCoeff) * ((g.roots.map conj).map fun r => 1 - C r * X).prod := by
  have hcard : Multiset.card (g.roots.map conj) = g.natDegree := by
    rw [Multiset.card_map]
    exact splits_iff_card_roots.mp (IsAlgClosed.splits g)
  have hmap : g.map (starRingEnd ℂ)
      = C (conj g.leadingCoeff) * ((g.roots.map conj).map fun a => X - C a).prod := by
    conv_lhs => rw [(IsAlgClosed.splits g).eq_prod_roots]
    rw [Polynomial.map_mul, map_C]
    congr 1
    calc ((g.roots.map fun a => X - C a).prod).map (starRingEnd ℂ)
        = ((g.roots.map fun a => X - C a).map (Polynomial.map (starRingEnd ℂ))).prod := by
          simpa only [coe_mapRingHom] using
            map_multiset_prod (mapRingHom (starRingEnd ℂ)) (g.roots.map fun a => X - C a)
      _ = ((g.roots.map conj).map fun a => X - C a).prod := by
          rw [Multiset.map_map, Multiset.map_map]
          congr 1
          apply Multiset.map_congr rfl
          intro r _
          simp only [Function.comp_apply, Polynomial.map_sub, map_X, map_C]
  rw [hmap, ← hcard, ← zero_add (Multiset.card (g.roots.map conj)),
    reflect_mul _ _ (natDegree_C _).le (natDegree_multiset_prod_X_sub_C_eq_card _).le,
    reflect_C, pow_zero, mul_one, reflect_multiset_prod_X_sub_C]

/-- Eval form of `reflect_conj_prod_form`:
    `(reflect (natDegree g) (g.map conj)).eval z = conj (lead g) * prod (1 - conj r_i * z)`. -/
theorem reflect_conj_eval (g : ℂ[X]) (z : ℂ) :
    (reflect g.natDegree (g.map (starRingEnd ℂ))).eval z
      = conj g.leadingCoeff * (g.roots.map fun r => 1 - conj r * z).prod := by
  rw [reflect_conj_prod_form, eval_mul, eval_C, eval_multiset_prod, Multiset.map_map,
    Multiset.map_map]
  congr 1
  refine congrArg Multiset.prod (Multiset.map_congr rfl fun r _ => ?_)
  simp only [Function.comp_apply, eval_sub, eval_one, eval_mul, eval_C, eval_X]

/-- Eval-level splitting of `g` itself: `g.eval z = lead g * prod (z - r_i)`. -/
theorem eval_prod_form (g : ℂ[X]) (z : ℂ) :
    g.eval z = g.leadingCoeff * (g.roots.map fun r => z - r).prod := by
  conv_lhs => rw [(IsAlgClosed.splits g).eq_prod_roots]
  rw [eval_mul, eval_C, eval_multiset_prod, Multiset.map_map]
  congr 1
  refine congrArg Multiset.prod (Multiset.map_congr rfl fun r _ => ?_)
  simp only [Function.comp_apply, eval_sub, eval_X, eval_C]

/-- Factor-by-factor dominance over a multiset of roots in the closed disk:
    `prod normSq (z - r) <= prod normSq (1 - conj r * z)` for `normSq z <= 1`.
    Each factor is dominated by step (i). -/
theorem prod_normSq_le {z : ℂ} (hz : normSq z ≤ 1) :
    ∀ s : Multiset ℂ, (∀ r ∈ s, normSq r ≤ 1) →
      (s.map fun r => normSq (z - r)).prod ≤ (s.map fun r => normSq (1 - conj r * z)).prod := by
  intro s
  induction s using Multiset.induction_on with
  | empty => intro _; simp
  | cons a t ih =>
    intro hs
    simp only [Multiset.map_cons, Multiset.prod_cons]
    have ha : normSq a ≤ 1 := hs a (Multiset.mem_cons_self a t)
    have ht : ∀ r ∈ t, normSq r ≤ 1 := fun r hr => hs r (Multiset.mem_cons_of_mem hr)
    have hfac : normSq (z - a) ≤ normSq (1 - conj a * z) := by
      nlinarith [normSq_factor_identity a z]
    refine mul_le_mul hfac (ih ht) ?_ (normSq_nonneg _)
    refine Multiset.prod_nonneg fun x hx => ?_
    obtain ⟨r, _, rfl⟩ := Multiset.mem_map.mp hx
    exact normSq_nonneg _

/-- **Reflection dominance (#SC-5 step (ii)).** If every root of `g` lies in the closed
    unit disk, then for every `z` in the closed unit disk,
    `normSq (g.eval z) <= normSq ((reflect (natDegree g) (g.map conj)).eval z)`. -/
theorem normSq_eval_le_normSq_reflect_eval (g : ℂ[X])
    (hroots : ∀ r ∈ g.roots, normSq r ≤ 1) {z : ℂ} (hz : normSq z ≤ 1) :
    normSq (g.eval z) ≤ normSq ((reflect g.natDegree (g.map (starRingEnd ℂ))).eval z) := by
  rw [reflect_conj_eval g z, eval_prod_form g z, Complex.normSq_mul, Complex.normSq_mul,
    normSq_conj, map_multiset_prod normSq, map_multiset_prod normSq,
    Multiset.map_map, Multiset.map_map]
  refine mul_le_mul_of_nonneg_left ?_ (normSq_nonneg _)
  exact prod_normSq_le hz g.roots hroots

/-- **`gStar` has no root strictly inside the disk.** If `g != 0` has all roots in the
    closed unit disk, then `(reflect (natDegree g) (g.map conj)).eval z != 0` for every
    `z` with `normSq z < 1`: each factor `1 - conj r * z` has
    `normSq (conj r * z) <= normSq z < 1`, and the leading constant is nonzero. -/
theorem reflect_conj_eval_ne_zero (g : ℂ[X]) (hg : g ≠ 0)
    (hroots : ∀ r ∈ g.roots, normSq r ≤ 1) {z : ℂ} (hz : normSq z < 1) :
    (reflect g.natDegree (g.map (starRingEnd ℂ))).eval z ≠ 0 := by
  rw [reflect_conj_eval]
  refine mul_ne_zero ?_ ?_
  · intro h
    exact leadingCoeff_ne_zero.mpr hg (by simpa using congrArg (starRingEnd ℂ) h)
  · rw [Ne, Multiset.prod_eq_zero_iff]
    intro h0
    obtain ⟨r, hr, hr0⟩ := Multiset.mem_map.mp h0
    have hrz : conj r * z = 1 := (sub_eq_zero.mp hr0).symm
    have h1 : normSq r * normSq z = 1 := by
      calc normSq r * normSq z = normSq (conj r * z) := by
            rw [Complex.normSq_mul, normSq_conj]
        _ = 1 := by rw [hrz, normSq_one]
    nlinarith [hroots r hr, hz, normSq_nonneg r, normSq_nonneg z]

/-! ## #SC-5: the Cohn converse -/

/-- **Cohn converse (#SC-5).** Let `p : Polynomial C` be self-inversive
    (`reflect (natDegree p) p = p`) with conj-fixed (i.e. real) coefficients and
    `natDegree p >= 1`. If every root of `derivative p` lies in the closed unit disk,
    then every root of `p` lies ON the unit circle.

    The pinch: at a root `w` with `normSq w < 1`, evaluating the #SC-2 reversal
    identity gives `(p')Star.eval w = -(w * p'.eval w)`; reflection dominance forces
    `p'.eval w = 0`, hence `(p')Star.eval w = 0`, contradicting
    `reflect_conj_eval_ne_zero`. A root with `normSq w > 1` pairs (self-inversivity,
    `eval₂_reflect_mul_pow`) with the root `w⁻¹` strictly inside. Note `p(0) != 0` is
    automatic from palindromic coefficients, so it is not assumed. -/
theorem cohn_converse {p : ℂ[X]} (hn : 1 ≤ p.natDegree)
    (hself : reflect p.natDegree p = p)
    (hreal : p.map (starRingEnd ℂ) = p)
    (hderiv : ∀ w : ℂ, (derivative p).eval w = 0 → normSq w ≤ 1) :
    ∀ z : ℂ, p.eval z = 0 → normSq z = 1 := by
  have hp0 : p ≠ 0 := by
    intro h
    rw [h, natDegree_zero] at hn
    omega
  have hd0 : derivative p ≠ 0 := by
    intro h
    have h0 := natDegree_eq_zero_of_derivative_eq_zero h
    omega
  have hdd : (derivative p).natDegree = p.natDegree - 1 := by
    refine le_antisymm (natDegree_derivative_le p) (le_natDegree_of_ne_zero ?_)
    rw [coeff_derivative]
    refine mul_ne_zero ?_ ?_
    · have e : p.natDegree - 1 + 1 = p.natDegree := by omega
      rw [e, coeff_natDegree]
      exact leadingCoeff_ne_zero.mpr hp0
    · intro hzero
      have hnat : p.natDegree - 1 + 1 = 0 := by exact_mod_cast hzero
      omega
  have hrd : (derivative p).map (starRingEnd ℂ) = derivative p := by
    rw [← derivative_map, hreal]
  have hdroots : ∀ r ∈ (derivative p).roots, normSq r ≤ 1 := by
    intro r hr
    exact hderiv r (mem_roots'.mp hr).2
  -- Step (iii): no root strictly inside the disk.
  have hinside : ∀ w : ℂ, normSq w < 1 → p.eval w ≠ 0 := by
    intro w hw hpw
    have h2 := reflect_derivative_self_inversive p hself
    have h2e : (reflect (p.natDegree - 1) (derivative p)).eval w
        = -(w * (derivative p).eval w) := by
      rw [h2]
      simp only [nsmul_eq_mul, eval_sub, eval_mul, eval_X, eval_natCast]
      rw [hpw, mul_zero, zero_sub]
    have hstar : (reflect (derivative p).natDegree
        ((derivative p).map (starRingEnd ℂ))).eval w = -(w * (derivative p).eval w) := by
      rw [hrd, hdd]
      exact h2e
    have hdom := normSq_eval_le_normSq_reflect_eval (derivative p) hdroots hw.le
    rw [hstar, Complex.normSq_neg, Complex.normSq_mul] at hdom
    have hA : normSq ((derivative p).eval w) = 0 := by
      nlinarith [normSq_nonneg ((derivative p).eval w)]
    have he0 : (derivative p).eval w = 0 := normSq_eq_zero.mp hA
    exact reflect_conj_eval_ne_zero (derivative p) hd0 hdroots hw
      (by rw [hstar, he0, mul_zero, neg_zero])
  -- Step (iv): trichotomy; a root strictly outside pairs with one strictly inside.
  intro z hz
  rcases lt_trichotomy (normSq z) 1 with h | h | h
  · exact absurd hz (hinside z h)
  · exact h
  · have hz0 : z ≠ 0 := by
      intro h0
      rw [h0, normSq_zero] at h
      linarith
    letI : Invertible z := invertibleOfNonzero hz0
    have hpair := eval₂_reflect_mul_pow (RingHom.id ℂ) z p.natDegree p le_rfl
    rw [hself, invOf_eq_inv] at hpair
    simp only [eval₂_id] at hpair
    rw [hz] at hpair
    have hzi : p.eval z⁻¹ = 0 := by
      rcases mul_eq_zero.mp hpair with h' | h'
      · exact h'
      · exact absurd h' (pow_ne_zero _ hz0)
    have hlt : normSq z⁻¹ < 1 := by
      rw [normSq_inv, inv_eq_one_div, div_lt_one (by linarith : (0 : ℝ) < normSq z)]
      exact h
    exact absurd hzi (hinside z⁻¹ hlt)

/-- **Cohn converse over the reals (#SC-5, real-coefficient form).** For
    `q : Polynomial R` self-inversive with `natDegree q >= 1`, mapped to `C` by
    `ofRealHom`: if every complex root of `q'` lies in the closed unit disk, every
    complex root of `q` lies on the unit circle. -/
theorem cohn_converse_real (q : Polynomial ℝ) (hq : 1 ≤ q.natDegree)
    (hself : reflect q.natDegree q = q)
    (hderiv : ∀ w : ℂ, (derivative (q.map Complex.ofRealHom)).eval w = 0 → normSq w ≤ 1) :
    ∀ z : ℂ, (q.map Complex.ofRealHom).eval z = 0 → normSq z = 1 := by
  have hnd : (q.map Complex.ofRealHom).natDegree = q.natDegree :=
    natDegree_map_eq_of_injective Complex.ofReal_injective q
  refine cohn_converse ?_ ?_ ?_ hderiv
  · rw [hnd]
    exact hq
  · rw [hnd, reflect_map, hself]
  · rw [Polynomial.map_map]
    congr 1
    ext x
    simp [Complex.conj_ofReal]

/-- **The general-degree Cohn criterion (#SC-4 + #SC-5).** For real self-inversive `q`
    with `natDegree q >= 1`: every complex root of `q` lies on the unit circle IFF
    every complex root of `derivative q` lies in the closed unit disk. This is the
    degree-n statement whose genus-1 shadow is #SC-1
    (`schur_cohn_certifies_circle`). -/
theorem cohn_criterion (q : Polynomial ℝ) (hq : 1 ≤ q.natDegree)
    (hself : reflect q.natDegree q = q) :
    (∀ z : ℂ, (q.map Complex.ofRealHom).eval z = 0 → normSq z = 1)
      ↔ ∀ w : ℂ, (derivative (q.map Complex.ofRealHom)).eval w = 0 → normSq w ≤ 1 := by
  have hnd : (q.map Complex.ofRealHom).natDegree = q.natDegree :=
    natDegree_map_eq_of_injective Complex.ofReal_injective q
  constructor
  · intro hcirc
    exact derivative_roots_in_disk (by rw [hnd]; exact hq) hcirc
  · exact cohn_converse_real q hq hself

-- Axiom audit: every theorem below must report exactly
-- [propext, Classical.choice, Quot.sound].
#print axioms derivative_roots_in_disk
#print axioms normSq_factor_identity
#print axioms reflect_multiset_prod_X_sub_C
#print axioms reflect_conj_prod_form
#print axioms reflect_conj_eval
#print axioms eval_prod_form
#print axioms prod_normSq_le
#print axioms normSq_eval_le_normSq_reflect_eval
#print axioms reflect_conj_eval_ne_zero
#print axioms cohn_converse
#print axioms cohn_converse_real
#print axioms cohn_criterion

end ZetaRH.SchurCohn
