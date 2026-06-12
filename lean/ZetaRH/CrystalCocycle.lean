/-
The crystal cocycle lemmas of the LCC/BC transport (LEARNINGS #82) and the
B1 G_log rigidity follow-on (LEARNINGS #86).

## What this module is

The Lean side of `docs/03_research/lcc_bc_transport.md` section 1.3 (Lemmas 1
and 2) and section 6 (the VERIFIER handoff V1-V3), plus the open target V4 from
`docs/03_research/b1_glog_rigidity.md`. The mathematical context:

The Lonely Crystal Conjecture (LCC, LEARNINGS #76) cone of positive
log-crystals was transported through the Bost-Connes uniqueness template
(LEARNINGS #81). Two elementary facts carry the whole discrete leg:

  Lemma 1 (V2): the literal BC quasi-invariance axiom on a comb
  `c : ℕ → ℝ`, namely `c (m * n) = m^(-β) * c n`, collapses the comb to
  the flat ray `c n = c 1 * n^(-β)` (the comb of `ζ(s)`, the WRONG ray:
  the named failure of the literal transport). The prime-generated form
  suffices, by induction along the factorization.

  Lemma 2 (V1): the repaired condition lives one Moebius twist up. With
  `B = 1 * b` the integrated comb (`B n = ∑_{d ∣ n} b d`), the additive
  cocycle identity `B (p * n) - B n = log p` for all primes `p` and all
  `n ≥ 1` holds IFF `b` is the von Mangoldt comb away from the unit atom
  (`b n = Λ n` for `n ≥ 2`, with `b 1` free). This is the exact statement
  that composite pinching = "mixed cumulants vanish" calibrates the crystal
  to `Λ`.

  V3: increment nonnegativity. For `b ≥ 0` the increments
  `B (p * n) - B n` are automatically nonnegative, because the divisors of
  `n` embed into the divisors of `p * n`.

## Status of the targets

  V1  `increments_eq_log_iff_eq_vonMangoldt`   PROVED (sorry-free).
  V2  `flat_ray_of_quasiInvariance` (full semigroup form) and
      `flat_ray_of_prime_quasiInvariance` (prime-generated form)
                                               PROVED (sorry-free).
  V3  `divisorSum_le_divisorSum_mul_of_nonneg` PROVED (sorry-free).
  V4  the G_log dense-translate rigidity lemma (`b1_glog_rigidity.md`):
      OPEN, not attempted here. See the feasibility note at the end of
      this file. It needs measure twisting, density of non-cyclic
      subgroups of ℝ, vague continuity of translation, and Haar
      uniqueness; all four ingredients exist in Mathlib (pointers below)
      but assembling them is a medium-size measure-theory development.

The proofs use only Finset divisor-sum manipulation, Mathlib's
`ArithmeticFunction.vonMangoldt_sum` (`∑_{d ∣ n} Λ d = log n`), and a
positive strong-induction principle along minimal prime factors. No zero of
any L-function appears anywhere (K1-clean by construction): the only inputs
are `ℕ`, its divisor lattice, and `Real.log`.

No em dashes anywhere in this file (project style rule).
-/

import Mathlib.NumberTheory.ArithmeticFunction.VonMangoldt
import Mathlib.NumberTheory.Divisors
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace ZetaRH.CrystalCocycle

open scoped ArithmeticFunction
open Finset

/-! ### The integrated comb `B = 1 * b` (Dirichlet convolution with `ζ`). -/

/-- The integrated comb: `divisorSum b n = ∑_{d ∣ n} b d`, the Dirichlet
    convolution `(1 * b) n`. This is the `B` of the transport dossier
    (Definition 5 of `lcc_bc_transport.md`); for `b = Λ` it equals `log n`
    by `ArithmeticFunction.vonMangoldt_sum`. -/
noncomputable def divisorSum (b : ℕ → ℝ) (n : ℕ) : ℝ :=
  ∑ d ∈ n.divisors, b d

/-! ### Induction infrastructure.

    Both Lemma 1 (prime-generated form) and Lemma 2 (forward direction) run
    the same induction: every `n ≥ 2` splits off its minimal prime factor,
    so every `n ≥ 1` is reachable from `1` by repeated prime multiplication.
    We package the two ingredients once. -/

/-- Strong induction on the positive naturals: to prove `P n` for all
    `n ≥ 1` it suffices to prove `P n` given `P m` for all `1 ≤ m < n`. -/
theorem pos_strong_induction (P : ℕ → Prop)
    (step : ∀ n : ℕ, 1 ≤ n → (∀ m : ℕ, 1 ≤ m → m < n → P m) → P n) :
    ∀ n : ℕ, 1 ≤ n → P n := by
  have main : ∀ N n : ℕ, n ≤ N → 1 ≤ n → P n := by
    intro N
    induction N with
    | zero => intro n hn h1; omega
    | succ N ih =>
      intro n hn h1
      exact step n h1 fun m hm hmn => ih m (by omega) hm
  intro n hn
  exact main n n le_rfl hn

/-- Every `n > 1` splits as `n = p * q` with `p` prime and `1 ≤ q < n`
    (take `p` to be the minimal prime factor). This is the single
    factorization step that drives the inductions below. -/
theorem exists_prime_mul_eq {n : ℕ} (hn : 1 < n) :
    ∃ p q : ℕ, p.Prime ∧ 1 ≤ q ∧ q < n ∧ n = p * q := by
  have hn1 : n ≠ 1 := by omega
  have hp : (n.minFac).Prime := Nat.minFac_prime hn1
  refine ⟨n.minFac, n / n.minFac, hp, ?_, ?_, ?_⟩
  · have := Nat.div_pos (Nat.minFac_le (by omega)) hp.pos
    omega
  · exact Nat.div_lt_self (by omega) hp.one_lt
  · exact (Nat.mul_div_cancel' (Nat.minFac_dvd n)).symm

/-! ### V2: Lemma 1 (quasi-invariance collapse, the O2 computation).

    The literal BC axiom `c (m * n) = m^(-β) * c n` pins the comb to the
    flat ray `c n = c 1 * n^(-β)`. At `β = 1/2` this is the comb of
    `c 1 * ζ(s)`, full support, NOT the von Mangoldt comb: the sharp
    failure of the literal transport (`lcc_bc_transport.md` Lemma 1). -/

/-- **V2, full-semigroup form.** Quasi-invariance over all of `ℕ×` collapses
    to the flat ray: specialize the hypothesis at `(m, n) = (n, 1)`. -/
theorem flat_ray_of_quasiInvariance (c : ℕ → ℝ) (β : ℝ)
    (h : ∀ m n : ℕ, 1 ≤ m → 1 ≤ n → c (m * n) = (m : ℝ) ^ (-β) * c n) :
    ∀ n : ℕ, 1 ≤ n → c n = c 1 * (n : ℝ) ^ (-β) := by
  intro n hn
  have h1 := h n 1 hn le_rfl
  rw [mul_one] at h1
  rw [h1]
  ring

/-- **V2, prime-generated form.** Quasi-invariance under the prime scaling
    maps alone already collapses to the flat ray, by strong induction along
    the minimal prime factor: every `n ≥ 1` is reachable from `1` by
    repeated prime multiplication, and each step contributes one exact
    cocycle factor `p^(-β)`. -/
theorem flat_ray_of_prime_quasiInvariance (c : ℕ → ℝ) (β : ℝ)
    (h : ∀ p n : ℕ, p.Prime → 1 ≤ n → c (p * n) = (p : ℝ) ^ (-β) * c n) :
    ∀ n : ℕ, 1 ≤ n → c n = c 1 * (n : ℝ) ^ (-β) := by
  refine pos_strong_induction _ fun n h1 ih => ?_
  rcases h1.eq_or_lt with rfl | h2
  · simp
  · obtain ⟨p, q, hp, hq1, hqlt, hq⟩ := exists_prime_mul_eq h2
    have hcq := ih q hq1 hqlt
    calc c n = c (p * q) := by rw [hq]
      _ = (p : ℝ) ^ (-β) * c q := h p q hp hq1
      _ = (p : ℝ) ^ (-β) * (c 1 * (q : ℝ) ^ (-β)) := by rw [hcq]
      _ = c 1 * ((p : ℝ) ^ (-β) * (q : ℝ) ^ (-β)) := by ring
      _ = c 1 * (((p : ℝ) * (q : ℝ)) ^ (-β)) := by
          rw [Real.mul_rpow (Nat.cast_nonneg p) (Nat.cast_nonneg q)]
      _ = c 1 * (n : ℝ) ^ (-β) := by rw [← Nat.cast_mul, ← hq]

/-! ### V3: increment nonnegativity.

    For `b ≥ 0` the integrated comb is monotone under prime multiplication:
    the divisors of `n` embed into the divisors of `p * n`, and the new
    divisors contribute nonnegatively. This is the "automatic" half of the
    cocycle condition (Definition 5 of the dossier). -/

/-- **V3.** If `b ≥ 0` then `B n ≤ B (p * n)` for every prime `p` and
    `n ≥ 1`. (No vanishing-at-0 hypothesis is needed: `0` is never a
    divisor, so `b 0` is invisible to `divisorSum`.) -/
theorem divisorSum_le_divisorSum_mul_of_nonneg (b : ℕ → ℝ)
    (hb : ∀ k : ℕ, 0 ≤ b k) {p : ℕ} (hp : p.Prime) {n : ℕ} (hn : 1 ≤ n) :
    divisorSum b n ≤ divisorSum b (p * n) := by
  simp only [divisorSum]
  refine Finset.sum_le_sum_of_subset_of_nonneg
    (Nat.divisors_subset_of_dvd
      (Nat.mul_ne_zero hp.ne_zero (by omega)) (dvd_mul_left n p))
    fun i _ _ => hb i

/-! ### V1: Lemma 2 (cocycle rigidity equivalence).

    The main content. Three helper lemmas:

      (A) any comb agreeing with `Λ` from 2 on has integrated comb
          `b 1 + log n` (downstream of `vonMangoldt_sum`);
      (B) constant increments `log p` force the integrated comb to be
          `b 1 + log n` (induction along the factorization);
      (C) a comb is determined by its integrated comb (Moebius inversion
          in its cheapest form: strong induction, isolating the top
          divisor `n` against the strictly smaller ones).

    Then V1 composes: increments are `log p` iff the integrated comb is
    `b 1 + log n` iff `b` agrees with `Λ` from 2 on. -/

/-- Helper (A): if `g` agrees with the von Mangoldt function for all
    arguments `≥ 2`, its divisor sum is `g 1 + log n`. The von Mangoldt
    term at `d = 1` is zero, so the unit atom `g 1` rides along freely. -/
theorem divisorSum_eq_add_log_of_eq_vonMangoldt (g : ℕ → ℝ)
    (hg : ∀ m : ℕ, 2 ≤ m → g m = Λ m) {n : ℕ} (hn : 1 ≤ n) :
    divisorSum g n = g 1 + Real.log (n : ℝ) := by
  have h1 : (1 : ℕ) ∈ n.divisors := Nat.one_mem_divisors.mpr (by omega)
  have hsplit : g 1 + ∑ d ∈ n.divisors.erase 1, g d = ∑ d ∈ n.divisors, g d :=
    Finset.add_sum_erase _ g h1
  have htail : ∑ d ∈ n.divisors.erase 1, g d = Real.log (n : ℝ) := by
    have hcong : ∑ d ∈ n.divisors.erase 1, g d
        = ∑ d ∈ n.divisors.erase 1, Λ d := by
      refine Finset.sum_congr rfl fun d hd => ?_
      have hd1 : d ≠ 1 := Finset.ne_of_mem_erase hd
      have hdpos : 0 < d := Nat.pos_of_mem_divisors (Finset.mem_of_mem_erase hd)
      exact hg d (by omega)
    rw [hcong, Finset.sum_erase _ ArithmeticFunction.vonMangoldt_apply_one,
      ArithmeticFunction.vonMangoldt_sum]
  simp only [divisorSum]
  rw [← hsplit, htail]

/-- Helper (B): constant increments `log p` force `B n = b 1 + log n`,
    by strong induction along the minimal prime factor. Each factorization
    step `n = p * q` converts one increment hypothesis into one `log p`,
    and the logs assemble through `Real.log_mul`. -/
theorem divisorSum_eq_add_log_of_increments (b : ℕ → ℝ)
    (h : ∀ p n : ℕ, p.Prime → 1 ≤ n →
      divisorSum b (p * n) - divisorSum b n = Real.log (p : ℝ)) :
    ∀ n : ℕ, 1 ≤ n → divisorSum b n = b 1 + Real.log (n : ℝ) := by
  refine pos_strong_induction _ fun n h1 ih => ?_
  rcases h1.eq_or_lt with rfl | h2
  · simp [divisorSum]
  · obtain ⟨p, q, hp, hq1, hqlt, hq⟩ := exists_prime_mul_eq h2
    have hstep := h p q hp hq1
    rw [← hq] at hstep
    have hqsum := ih q hq1 hqlt
    have hlogn : Real.log (n : ℝ) = Real.log (p : ℝ) + Real.log (q : ℝ) := by
      rw [hq]
      push_cast
      exact Real.log_mul (Nat.cast_ne_zero.mpr hp.ne_zero)
        (Nat.cast_ne_zero.mpr (by omega))
    rw [hlogn]
    linarith

/-- Helper (C): a comb is determined by its integrated comb. This is
    Moebius inversion in its cheapest constructive form: at each `n` the
    divisor sum isolates `b n` against divisors `d < n`, which are handled
    by strong induction. -/
theorem eq_of_divisorSum_eq (g g' : ℕ → ℝ)
    (h : ∀ n : ℕ, 1 ≤ n → divisorSum g n = divisorSum g' n) :
    ∀ n : ℕ, 1 ≤ n → g n = g' n := by
  refine pos_strong_induction _ fun n h1 ih => ?_
  have hn0 : n ≠ 0 := by omega
  have hmem : n ∈ n.divisors := Nat.mem_divisors_self n hn0
  have hsum := h n h1
  simp only [divisorSum] at hsum
  rw [← Finset.add_sum_erase _ g hmem, ← Finset.add_sum_erase _ g' hmem] at hsum
  have htail : ∑ d ∈ n.divisors.erase n, g d
      = ∑ d ∈ n.divisors.erase n, g' d := by
    refine Finset.sum_congr rfl fun d hd => ?_
    have hdn : d ≠ n := Finset.ne_of_mem_erase hd
    have hdmem := Finset.mem_of_mem_erase hd
    have hdpos : 0 < d := Nat.pos_of_mem_divisors hdmem
    have hdle : d ≤ n := Nat.le_of_dvd (by omega) (Nat.mem_divisors.mp hdmem).1
    exact ih d hdpos (by omega)
  rw [htail] at hsum
  linarith

/-- The reference comb: the von Mangoldt comb with the unit atom set to
    `b1`. Lemma 2 leaves the unit atom free (the divisor-sum increments
    never see it), so the rigidity target is this one-parameter family. -/
noncomputable def refComb (b1 : ℝ) : ℕ → ℝ :=
  fun n => if n = 1 then b1 else Λ n

@[simp]
theorem refComb_one (b1 : ℝ) : refComb b1 1 = b1 := by
  simp [refComb]

theorem refComb_of_two_le (b1 : ℝ) {n : ℕ} (hn : 2 ≤ n) :
    refComb b1 n = Λ n := by
  have h1 : n ≠ 1 := by omega
  simp [refComb, h1]

/-- **V1 (Lemma 2, cocycle rigidity equivalence).** With
    `B = divisorSum b` the integrated comb: the additive cocycle identity

      `B (p * n) - B n = log p`  for all primes `p` and all `n ≥ 1`

    holds IFF `b n = Λ n` for all `n ≥ 2` (the unit atom `b 1` stays
    free). Forward: constant increments force `B n = b 1 + log n`
    (helper B), the reference comb `refComb (b 1)` produces the same
    integrated comb (helper A), and combs with equal integrated combs are
    equal (helper C). Reverse: `B n = b 1 + log n` by helper A, and
    `log (p * n) - log n = log p`.

    This is the repaired BC axiom of the transport: the KMS cocycle
    condition on the integrated comb lands exactly on the von Mangoldt
    crystal, where the literal quasi-invariance axiom (V2) lands on the
    flat ray. -/
theorem increments_eq_log_iff_eq_vonMangoldt (b : ℕ → ℝ) :
    (∀ p n : ℕ, p.Prime → 1 ≤ n →
        divisorSum b (p * n) - divisorSum b n = Real.log (p : ℝ)) ↔
      ∀ n : ℕ, 2 ≤ n → b n = Λ n := by
  constructor
  · intro h n hn
    have hB := divisorSum_eq_add_log_of_increments b h
    have hB' : ∀ m : ℕ, 1 ≤ m →
        divisorSum (refComb (b 1)) m = b 1 + Real.log (m : ℝ) := by
      intro m hm
      rw [divisorSum_eq_add_log_of_eq_vonMangoldt (refComb (b 1))
        (fun k hk => refComb_of_two_le (b 1) hk) hm, refComb_one]
    have key := eq_of_divisorSum_eq b (refComb (b 1))
      (fun m hm => by rw [hB m hm, hB' m hm]) n (by omega)
    rw [key, refComb_of_two_le (b 1) hn]
  · intro h p n hp hn
    have hpn : 1 ≤ p * n :=
      Nat.one_le_iff_ne_zero.mpr (Nat.mul_ne_zero hp.ne_zero (by omega))
    rw [divisorSum_eq_add_log_of_eq_vonMangoldt b h hpn,
      divisorSum_eq_add_log_of_eq_vonMangoldt b h hn]
    have hlog : Real.log ((p * n : ℕ) : ℝ)
        = Real.log (p : ℝ) + Real.log (n : ℝ) := by
      push_cast
      exact Real.log_mul (Nat.cast_ne_zero.mpr hp.ne_zero)
        (Nat.cast_ne_zero.mpr (by omega))
    rw [hlog]
    ring

/-! ### The axiom audit.

    All four proved targets should report exactly the three foundational
    Mathlib axioms `[propext, Classical.choice, Quot.sound]`: no `sorryAx`,
    no zero data, no RH input. The verbatim output is recorded in the
    VERIFIER report. -/

#print axioms flat_ray_of_quasiInvariance
#print axioms flat_ray_of_prime_quasiInvariance
#print axioms divisorSum_le_divisorSum_mul_of_nonneg
#print axioms increments_eq_log_iff_eq_vonMangoldt

/-! ### V4 (OPEN): the G_log dense-translate rigidity lemma.

    Statement (`docs/03_research/b1_glog_rigidity.md`): a positive Radon
    measure `ν` on ℝ with `ν (A + log p) = p^(-β) * ν A` for every prime
    `p` and Borel `A` is `c * exp (-β x) dx`. Proof shape: twist by
    `exp (β x)` to make the cocycle an invariance, use density of the
    subgroup generated by `{log p}` (two primes suffice, via
    `log 2 / log 3` irrational from unique factorization), upgrade dense
    invariance to full invariance by vague continuity, and finish by Haar
    uniqueness on ℝ.

    Feasibility (the Mathlib ingredients all exist):
      - density of non-cyclic subgroups of ℝ: `AddSubgroup.dense_or_cyclic`
        (additive version of `Subgroup.dense_or_cyclic`,
        `Mathlib.Topology.Algebra.Order.Archimedean`) plus
        `Nat.Prime.factorization`-style unique-factorization input to rule
        out cyclicity;
      - measure twisting: `MeasureTheory.Measure.withDensity` and its
        translation behaviour;
      - Haar uniqueness on ℝ:
        `MeasureTheory.Measure.isAddLeftInvariant_eq_smul`
        (`Mathlib.MeasureTheory.Measure.Haar.Unique`) together with
        `Real.isAddHaarMeasure_volume`;
      - vague continuity of translation: assemble from
        `MeasureTheory.integral` continuity against `C_c(ℝ)` test
        functions (`HasCompactSupport`, uniform continuity on compacts).
    The assembly is a medium-size measure-theory development (the
    dense-invariance-to-full-invariance step needs a Riesz-type argument
    that invariance can be tested against `C_c`), estimated well above the
    budget of this pass; deferred as open target V4. -/

end ZetaRH.CrystalCocycle
