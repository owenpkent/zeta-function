/-
TamenessTrade: the two surviving pinning toys of the tameness/wildness fault line
(LEARNINGS #157, `docs/03_research/tameness_trade.md`), plus an independent second
formalization of the NG1 rigidity kernel (#MTF-1 consensus witness #2).

Context. The tameness-trade dossier records a CORRECTED negative: the general law
"a first-order structure tame enough to carry a definable quantitative fixed-point
theory cannot define a genuine sum over the primes" splits into a saturation leg
(PROVEN, tameness-blind) and a tameness leg (REFUTED as stated; the archimedean ORDER,
not the bare prime set, is the wild ingredient, Kaplan-Shelah arXiv:1601.07099). The
load-bearing content (Lemma P3 saturation, Bateman-Jockusch-Woods, the interpretation
transfer lemma) is beyond current Mathlib (no developed theory of saturation, simplicity,
SOP, or interpretation-transfer). What IS Lean-reachable is the pair of VALUE-PINNING
micro-toys that state the ingredients of the fault line:

- T-TT-1 (#TT-1): multiplication is first-order definable from addition and squaring,
  via the identity `2*x*y = (x+y)^2 - x^2 - y^2`. This is the arithmetic core of the
  "an innocuous multiplicative predicate + addition recovers full multiplication"
  interpretation direction (J. Robinson 1949, the squares toy). We formalize the clean
  algebraic identity `two_mul_mul_eq` (and its subtraction-free companion valid over ℕ),
  NOT the full `Set.Definable` wrapper: stating "the graph of `(· * ·)` is definable in
  the structure with `+` and the perfect-square predicate" against `Mathlib.ModelTheory`
  would require building a bespoke `FirstOrder.Language` and a `Structure` instance on ℕ,
  which is heavy overhead for a pinning toy that carries no RH content. The algebraic
  identity IS the definability mechanism; the model-theoretic wrapper only re-packages it.

- T-TT-2 (#TT-2): the primes are definable from the von Mangoldt function, i.e.
  `n.Prime ↔ Λ n ≠ 0 ∧ ∀ m < n, Λ m ≠ Λ n`. The forward direction: `Λ p = log p ≠ 0`
  and any `m < p` with `Λ m = Λ p = log p` would be a prime power whose minimal prime is
  `p` itself, forcing `p ∣ m` hence `p ≤ m`, a contradiction. The reverse direction: a
  non-prime prime power `n` has minimal prime `p = n.minFac < n` with `Λ p = log p = Λ n`,
  violating the second clause. This is the "weight recovers the support" step (the D1 → D3
  reduction of the dossier) as a machine-checked full `↔`.

- ng1_rigidity_indep (#MTF-1 consensus witness #2): every ring endomorphism of every
  commutative ℚ-algebra fixes the imported ℚ pointwise, `σ.comp (algebraMap ℚ R) =
  algebraMap ℚ R`. This is an INDEPENDENT re-derivation of the NG1 kernel of
  `ModelTheoreticFrobenius.lean` (#MTF-1), from the mathematical statement in
  `docs/03_research/model_theoretic_frobenius.md` Section 3, using a distinct proof route:
  NOT `RingHom.ext_rat`, but the hands-on `map_natCast` / `map_intCast` mechanism
  (`σ` fixes ℤ, and `(q.den : R)` is a unit because `algebraMap` sends the ℚ-unit `q.den`
  to a unit, so the equation `σ(algebraMap q) * q.den = q.num` cancels down to
  `σ(algebraMap q) = algebraMap q`). Serving as consensus witness #2 that the NG1 core is
  proved and axiom-clean.

None of these is the refuted Leg B; they are the ingredients of the fault line, pinned.

D-H discipline: N/A by category. These are meta-level statements about the definability of
arithmetic and the rigidity of ring endomorphisms; no L-function is evaluated, no zero is
manufactured, no positivity is asserted. Same exemption #156/#157 recorded.
-/

import Mathlib.NumberTheory.ArithmeticFunction.VonMangoldt
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Ring.Rat
import Mathlib.Tactic

namespace ZetaRH.TamenessTrade

/-! ## T-TT-1 (#TT-1): multiplication from addition and squaring

The Robinson squares toy, arithmetic core. `ring` closes both; the point is that
multiplication is a `+`/square-polynomial combination, so a language with `+` and the
perfect-square data first-order defines the graph of `·*·`. -/

/-- **T-TT-1, ring form.** Over any commutative ring, `2*x*y` is expressed through squares
and addition: `2*x*y = (x+y)^2 - x^2 - y^2`. This is the arithmetic core of the
definability of multiplication from addition and squaring (J. Robinson's squares toy):
a first-order structure carrying `+` and the values of `(·)^2` defines the graph of
`(· * ·)` via this polynomial identity. -/
theorem two_mul_mul_eq {R : Type*} [CommRing R] (x y : R) :
    2 * x * y = (x + y) ^ 2 - x ^ 2 - y ^ 2 := by
  ring

/-- **T-TT-1, subtraction-free form (valid over ℕ).** The same content phrased without
subtraction, so it holds over any commutative semiring (in particular `ℕ`, the natural
home of the definability-of-arithmetic statement): `2*x*y + (x^2 + y^2) = (x+y)^2`. -/
theorem two_mul_mul_add_sq_eq {R : Type*} [CommSemiring R] (x y : R) :
    2 * x * y + (x ^ 2 + y ^ 2) = (x + y) ^ 2 := by
  ring

/-! ## ng1_rigidity_indep (#MTF-1 consensus witness #2): the NG1 rigidity kernel

Independent re-derivation of `ModelTheoreticFrobenius.ng1_rigidity`, via `map_natCast` /
`map_intCast` and unit cancellation rather than `RingHom.ext_rat`. -/

/-- **NG1 rigidity, pointwise (independent route).** For a commutative ℚ-algebra `R` and any
ring endomorphism `σ : R →+* R`, `σ` fixes every imported rational: `σ (algebraMap ℚ R q) =
algebraMap ℚ R q`.

Proof route (distinct from the `RingHom.ext_rat` one used in `ModelTheoreticFrobenius`):
write `q = q.num / q.den`, so `algebraMap q * (q.den : R) = (q.num : R)`. Applying `σ` and
using that `σ` fixes `ℕ`- and `ℤ`-casts (`map_natCast` / `map_intCast`) gives
`σ (algebraMap q) * (q.den : R) = (q.num : R)`. Since `(q.den : R) = algebraMap (q.den : ℚ)`
and `(q.den : ℚ)` is a unit in the field `ℚ`, it has a right inverse `algebraMap ((q.den)⁻¹)`
in `R`; cancelling it yields `σ (algebraMap q) = algebraMap q`. -/
theorem ng1_rigidity_indep_apply {R : Type*} [CommRing R] [Algebra ℚ R]
    (σ : R →+* R) (q : ℚ) :
    σ (algebraMap ℚ R q) = algebraMap ℚ R q := by
  set A : ℚ →+* R := algebraMap ℚ R with hA
  -- `q * (q.den : ℚ) = (q.num : ℚ)` from `num / den = q`.
  have hd0 : ((q.den : ℕ) : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr q.den_ne_zero
  have hnm : ((q.num : ℤ) : ℚ) = q * ((q.den : ℕ) : ℚ) :=
    (div_eq_iff hd0).mp (Rat.num_div_den q)
  -- Push through `A = algebraMap ℚ R`, collapsing the casts.
  have hstar : A q * ((q.den : ℕ) : R) = ((q.num : ℤ) : R) := by
    rw [← map_natCast A q.den, ← map_intCast A q.num, ← map_mul, ← hnm]
  -- The image of the denominator has an explicit right inverse in `R`.
  have hv : ((q.den : ℕ) : R) * A (((q.den : ℕ) : ℚ)⁻¹) = 1 := by
    rw [← map_natCast A q.den, ← map_mul, mul_inv_cancel₀ hd0, map_one]
  -- Apply `σ`; `σ` fixes the integer and natural casts, giving the same equation for `σ (A q)`.
  have hstar2 : σ (A q) * ((q.den : ℕ) : R) = ((q.num : ℤ) : R) := by
    have hc := congrArg σ hstar
    rwa [map_mul, map_natCast σ q.den, map_intCast σ q.num] at hc
  -- Cancel the unit `(q.den : R)` using its right inverse.
  calc σ (A q)
      = σ (A q) * (((q.den : ℕ) : R) * A (((q.den : ℕ) : ℚ)⁻¹)) := by rw [hv, mul_one]
    _ = (σ (A q) * ((q.den : ℕ) : R)) * A (((q.den : ℕ) : ℚ)⁻¹) := by rw [mul_assoc]
    _ = ((q.num : ℤ) : R) * A (((q.den : ℕ) : ℚ)⁻¹) := by rw [hstar2]
    _ = (A q * ((q.den : ℕ) : R)) * A (((q.den : ℕ) : ℚ)⁻¹) := by rw [hstar]
    _ = A q * (((q.den : ℕ) : R) * A (((q.den : ℕ) : ℚ)⁻¹)) := by rw [mul_assoc]
    _ = A q := by rw [hv, mul_one]

/-- **NG1 rigidity, endomorphism form (independent route, #MTF-1 consensus witness #2).**
Every ring endomorphism of every commutative ℚ-algebra fixes the canonically imported ℚ
pointwise: `σ.comp (algebraMap ℚ R) = algebraMap ℚ R`. Second, independently-written
formalization of the NG1 kernel; see `ng1_rigidity_indep_apply` for the proof route. -/
theorem ng1_rigidity_indep {R : Type*} [CommRing R] [Algebra ℚ R]
    (σ : R →+* R) :
    σ.comp (algebraMap ℚ R) = algebraMap ℚ R :=
  RingHom.ext fun q => by
    rw [RingHom.comp_apply]; exact ng1_rigidity_indep_apply σ q

/-! ## T-TT-2 (#TT-2): the primes are definable from the von Mangoldt function -/

section VonMangoldt

open ArithmeticFunction

/-- **T-TT-2 (#TT-2).** The primes are first-order definable from the von Mangoldt function
in `(ℕ, <, Λ)`: for every `n : ℕ`,
`n.Prime ↔ Λ n ≠ 0 ∧ ∀ m < n, Λ m ≠ Λ n`.

`Λ n ≠ 0` says `n` is a prime power; the minimality clause `∀ m < n, Λ m ≠ Λ n` then pins
`n` down to the prime itself, since for a prime `p` the least `k` with `Λ k = log p` is `p`
(all smaller prime powers of `p` are absent below `p`, and every other prime power has a
different `Λ`-value). This is the "weight recovers the support" (D1 → D3) step of the
tameness-trade dossier, machine-checked as a full `↔`. -/
theorem prime_iff_vonMangoldt (n : ℕ) :
    n.Prime ↔ Λ n ≠ 0 ∧ ∀ m < n, Λ m ≠ Λ n := by
  constructor
  · -- Forward: `n` prime ⟹ `Λ n = log n ≠ 0` and no smaller `m` shares the value.
    intro hp
    refine ⟨?_, ?_⟩
    · rw [vonMangoldt_apply_prime hp]
      exact (Real.log_pos (by exact_mod_cast hp.one_lt)).ne'
    · intro m hm heq
      have hΛn : Λ n = Real.log n := vonMangoldt_apply_prime hp
      have hlogpos : 0 < Real.log (n : ℝ) := Real.log_pos (by exact_mod_cast hp.one_lt)
      have hΛm_ne : Λ m ≠ 0 := by rw [heq, hΛn]; exact hlogpos.ne'
      have hpp : IsPrimePow m := vonMangoldt_ne_zero_iff.mp hΛm_ne
      have hΛm : Λ m = Real.log (m.minFac) := by rw [vonMangoldt_apply, if_pos hpp]
      have hmf_pos : 0 < ((m.minFac : ℕ) : ℝ) := by exact_mod_cast Nat.minFac_pos m
      have hn_pos : 0 < (n : ℝ) := by exact_mod_cast hp.pos
      -- `log (m.minFac) = log n`, and `log` is injective on positives, so `m.minFac = n`.
      have hcast : ((m.minFac : ℕ) : ℝ) = (n : ℝ) := by
        have h1 : Real.log ((m.minFac : ℕ) : ℝ) = Real.log (n : ℝ) := by
          rw [← hΛm, heq, hΛn]
        have h2 := congrArg Real.exp h1
        rwa [Real.exp_log hmf_pos, Real.exp_log hn_pos] at h2
      have hmfn : m.minFac = n := by exact_mod_cast hcast
      -- Then `n = m.minFac ∣ m`, forcing `n ≤ m`, contradicting `m < n`.
      have hdvd : n ∣ m := hmfn ▸ Nat.minFac_dvd m
      exact absurd (Nat.le_of_dvd hpp.pos hdvd) (not_le.mpr hm)
  · -- Reverse: the RHS forces `n` to be its own minimal prime, i.e. prime.
    rintro ⟨hne, h2⟩
    have hpp : IsPrimePow n := vonMangoldt_ne_zero_iff.mp hne
    have hn1 : n ≠ 1 := hpp.ne_one
    have hprime : (n.minFac).Prime := Nat.minFac_prime hn1
    by_contra hnp
    have hΛn : Λ n = Real.log (n.minFac) := by rw [vonMangoldt_apply, if_pos hpp]
    have hΛmf : Λ (n.minFac) = Real.log (n.minFac) := vonMangoldt_apply_prime hprime
    -- If `n` is not prime it is a proper prime power, so `n.minFac < n`.
    have hmf_ne : n.minFac ≠ n := fun h => hnp (h ▸ hprime)
    have hlt : n.minFac < n := lt_of_le_of_ne (Nat.minFac_le hpp.pos) hmf_ne
    -- But `Λ (n.minFac) = log (n.minFac) = Λ n`, violating the minimality clause.
    exact (h2 (n.minFac) hlt) (by rw [hΛmf, hΛn])

end VonMangoldt

end ZetaRH.TamenessTrade
