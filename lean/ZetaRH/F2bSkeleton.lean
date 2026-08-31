/-
F2b statement skeleton: the visibility-floor law over the certificate class.

Companion to docs/03_research/f2b_visibility_floor.md (frame session F2b,
2026-08-28). Originally deliberately unimported (the Section 5 bar's artifact,
statements VERIFIER-drafted with the hypothesis load priced); IMPORTED by
ZetaRH.lean since the 2026-08-31 batch discharged V-F2b-6, making the file
sorry-free (the VerifierQueue precedent: discharged batches join the build).
Register lemmas whose
content is finite arithmetic are PROVED; analytic steps are carried as named
hypotheses in the honest KERNEL style of #VQ-1a/#S4C-2 (the polynomial/analytic
input as hypothesis, the finite inequality as theorem); the one theorem-shape
statement (V-F2b-6) is now PROVED against its carried hypothesis, so the file
is sorry-free.

Model: the horizontal-line multiplicity profile of a C0 window is carried as a
`Multiset ℕ` (the h-profile: one entry per occupied horizontal line). The
extraction of the h-profile from a strip configuration is definitional
bookkeeping (GLSS Section 2 classification) and is NOT re-proved here; every
lemma is stated directly on the profile. E = sum h(h-1), Nstar = sum h^2,
N = sum h, in the GLSS conventions fixed by the theorem document Section 0.

Hypothesis loads, priced per target:
  V-F2b-1 (parity/register)          : none (finite arithmetic, PROVED)
  V-F2b-2 (conversion inequality)    : none (per-line + summation, PROVED)
  V-F2b-3 (PROFILE domination)       : none (per-line + summation, PROVED; the
           h-profile surrogate of V-F2a-4, strictly weaker than the
           sum-register form: see its docstring, session adversary F9)
  V-F2b-4 (monotonicity)             : none (sum over a sub-multiset, PROVED)
  V-F2b-5 (cosh envelope core)       : none (Real.cosh algebra, PROVED)
  V-F2b-6 (second-difference bound)  : carried hypothesis: a two-sided bound on
           the second derivative (Bernstein's inequality for exponential type
           is the in-print source; exponential-type machinery is not in
           Mathlib, so the analytic input rides as `hg''`); the finite MVT
           kernel is PROVED (Cauchy MVT against t^2, then the mean value
           inequality on g'; sharp constant, no factor-2 loss).
  V-F2b-7 (floor statement shape)    : the class quantifier (battery, slack,
           matching) abstracted; carried as a NAMED PROP (a def, not a
           sorry-bodied theorem: the theorem form was refutable at degenerate
           instantiations, session adversary F8); the next batch proves
           instances under the typed discipline, priced at the def.
-/

import Mathlib.Data.Multiset.Basic
import Mathlib.Analysis.Complex.Exponential
import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Tactic

namespace ZetaRH.F2bSkeleton

open Multiset

/-- The completeness functional E = sum over lines of h(h-1). -/
def excess (H : Multiset ℕ) : ℕ := (H.map (fun h => h * (h - 1))).sum

/-- Nstar = sum over lines of h^2 (ordered equal-ordinate pairs, diagonal
included). -/
def nstar (H : Multiset ℕ) : ℕ := (H.map (fun h => h * h)).sum

/-- N = sum over lines of h (the zero count with multiplicity). -/
def ncount (H : Multiset ℕ) : ℕ := H.sum

/-- Lines carrying at least two zeros (every off-line zero and every multiple
zero lives on one: the defective lines). -/
def defectMass (H : Multiset ℕ) : ℕ := (H.filter (2 ≤ ·)).sum

/-- Simple critical lines (h = 1). -/
def simpleLines (H : Multiset ℕ) : ℕ := (H.filter (· = 1)).card

/- ------------------------------------------------------------------------ -/
/- V-F2b-1: the parity/register lemma (E even; E < 2 iff E = 0).            -/
/- ------------------------------------------------------------------------ -/

theorem excess_term_even (h : ℕ) : Even (h * (h - 1)) := by
  rcases h with _ | n
  · simp
  · simpa [Nat.succ_sub_one, Nat.mul_comm] using Nat.even_mul_succ_self n

theorem excess_even (H : Multiset ℕ) : Even (excess H) := by
  unfold excess
  induction H using Multiset.induction_on with
  | empty => simp
  | cons a s ih =>
      simp only [Multiset.map_cons, Multiset.sum_cons]
      exact (excess_term_even a).add ih

/-- V-F2b-1: over any h-profile, E < 2 iff E = 0 (parity plus integrality:
the absolute-count register collapses to exact completeness). -/
theorem excess_lt_two_iff (H : Multiset ℕ) : excess H < 2 ↔ excess H = 0 := by
  constructor
  · intro hlt
    rcases (excess_even H) with ⟨k, hk⟩
    omega
  · intro h0; omega

/- ------------------------------------------------------------------------ -/
/- V-F2b-2: the conversion inequality (#simple-critical >= 2N - Nstar).     -/
/- ------------------------------------------------------------------------ -/

theorem conversion_per_line (h : ℕ) :
    (2 * h : ℤ) - (h * h : ℕ) ≤ (if h = 1 then 1 else 0) := by
  rcases h with _ | _ | h <;> simp <;> nlinarith

/-- V-F2b-2: the GLSS location step as a profile theorem (no arithmetic
consumed): the number of simple critical lines is at least 2N - Nstar. -/
theorem conversion (H : Multiset ℕ) :
    (2 * ncount H : ℤ) - nstar H ≤ simpleLines H := by
  unfold ncount nstar simpleLines
  induction H using Multiset.induction_on with
  | empty => simp
  | cons a s ih =>
      rw [Multiset.filter_cons, Multiset.map_cons, Multiset.sum_cons,
        Multiset.sum_cons, Multiset.card_add]
      by_cases ha : a = 1
      · subst ha
        rw [if_pos rfl, Multiset.card_singleton]
        push_cast at ih ⊢
        linarith
      · rw [if_neg ha, Multiset.card_zero]
        have h2 : a = 0 ∨ 2 ≤ a := by omega
        have h0 : (2 * (a : ℤ)) - (a : ℤ) * a ≤ 0 := by
          rcases h2 with h | h
          · subst h; norm_num
          · have h' : (2 : ℤ) ≤ (a : ℤ) := by exact_mod_cast h
            nlinarith
        push_cast at ih ⊢
        linarith

/- ------------------------------------------------------------------------ -/
/- V-F2b-3: the domination (defective mass <= E).                            -/
/- ------------------------------------------------------------------------ -/

theorem domination_per_line (h : ℕ) (h2 : 2 ≤ h) : h ≤ h * (h - 1) := by
  obtain ⟨k, rfl⟩ : ∃ k, h = k + 2 := ⟨h - 2, by omega⟩
  have hk : k + 2 - 1 = k + 1 := by omega
  rw [hk]
  nlinarith

/-- V-F2b-3 (the PROFILE domination): the total zero mass on defective lines is
at most the excess, `defectMass <= E`. This is the h-profile surrogate of
V-F2a-4, and deliberately WEAKER than the sum-register statement
N_off + N_mult <= E: per-register domination (N_off <= E and N_mult <= E)
follows from it, but the sum register needs the beta-data extraction (the
h = 2 both-defective impossibility from the FE pairing), which lives on the
extraction side exactly like `conversion`'s hypothesis boundary (session
adversary F9: an h = 4 line of two off-line doubles has N_off + N_mult = 8
against defectMass = 4, both under E-term 12, so the surrogate must not be
conflated with the sum form). -/
theorem domination (H : Multiset ℕ) : defectMass H ≤ excess H := by
  unfold defectMass excess
  induction H using Multiset.induction_on with
  | empty => simp
  | cons a s ih =>
      rw [Multiset.filter_cons, Multiset.map_cons, Multiset.sum_cons]
      by_cases ha : 2 ≤ a
      · rw [if_pos ha, Multiset.sum_add, Multiset.sum_singleton]
        exact Nat.add_le_add (domination_per_line a ha) ih
      · rw [if_neg ha, Multiset.zero_add]
        have h0 : a * (a - 1) = 0 := by interval_cases a <;> rfl
        omega

/- ------------------------------------------------------------------------ -/
/- V-F2b-4: monotonicity (E over a window extension only grows).            -/
/- ------------------------------------------------------------------------ -/

/-- V-F2b-4: extending the window (adding lines, or growing a line's h, which
in profile form is adding the difference as new mass then merging, bounded
below by the sub-multiset sum) only grows E. Stated in the sub-multiset form. -/
theorem excess_mono (H K : Multiset ℕ) (hle : H ≤ K) :
    excess H ≤ excess K := by
  obtain ⟨D, rfl⟩ := Multiset.le_iff_exists_add.mp hle
  unfold excess
  rw [Multiset.map_add, Multiset.sum_add]
  exact Nat.le_add_right _ _

/- ------------------------------------------------------------------------ -/
/- V-F2b-5: the cosh envelope core (the split cost identity's algebra).     -/
/- ------------------------------------------------------------------------ -/

/-- V-F2b-5: the split-cost integrand identity
exp(du) + exp(-du) - 2 = 2(cosh(du) - 1), and it is nonnegative: the exact
envelope of L2c is an identity, not an estimate. -/
theorem cosh_envelope (d u : ℝ) :
    Real.exp (d * u) + Real.exp (-(d * u)) - 2
      = 2 * (Real.cosh (d * u) - 1)
    ∧ 0 ≤ 2 * (Real.cosh (d * u) - 1) := by
  constructor
  · rw [Real.cosh_eq]; ring
  · nlinarith [Real.one_le_cosh (d * u)]

/- ------------------------------------------------------------------------ -/
/- V-F2b-6: the second-difference bound (Bernstein carried as hypothesis).  -/
/- ------------------------------------------------------------------------ -/

/-- V-F2b-6 (PROVED; the analytic input rides as `hbound`): if g is twice
differentiable with |g''| <= B everywhere (for exponential type Theta and
sup-norm 1, Bernstein gives B = Theta^2: the in-print source; exponential-type
machinery is not in Mathlib, so the bound is the carried hypothesis), then the
symmetric second difference at half-spacing a obeys the L2b bound.
The first derivative is carried EXPLICITLY as `g'` with its own `HasDerivAt`
hypothesis (session adversary F7: the earlier `deriv g` form was refutable via
junk-value `deriv` at a non-differentiable g, e.g. the indicator of {0} with
B = 0). Route actually used (sharp constant, no factor-2 loss): with
phi(t) = g(x+t) + g(x-t) - 2g(x), Cauchy's mean value theorem
(`exists_ratio_hasDerivAt_eq_ratio_slope`) against v(t) = t^2 on [0, a] gives
c in (0, a) with a^2 * (g'(x+c) - g'(x-c)) = phi(a) * 2c; the mean value
inequality on g' (`Convex.norm_image_sub_le_of_norm_hasDerivWithin_le` on
Set.univ) bounds |g'(x+c) - g'(x-c)| <= B * 2c; divide by 2c > 0. -/
theorem second_difference_bound
    (g g' g'' : ℝ → ℝ) (B a x : ℝ)
    (hg' : ∀ t, HasDerivAt g (g' t) t)
    (hg'' : ∀ t, HasDerivAt g' (g'' t) t)
    (hbound : ∀ t, |g'' t| ≤ B) (ha : 0 ≤ a) :
    |g (x + a) + g (x - a) - 2 * g x| ≤ a ^ 2 * B := by
  rcases eq_or_lt_of_le ha with rfl | hapos
  · have h0 : g (x + 0) + g (x - 0) - 2 * g x = 0 := by simp [two_mul]
    rw [h0, abs_zero]
    norm_num
  · -- WHY a difference quotient: phi(0) = 0 and v(0) = 0 make the Cauchy MVT
    -- ratio exactly the second difference over a^2, with no telescoping loss.
    have hphi : ∀ t : ℝ, HasDerivAt (fun s => g (x + s) + g (x - s) - 2 * g x)
        (g' (x + t) - g' (x - t)) t := by
      intro t
      have h1 : HasDerivAt (fun s : ℝ => g (x + s)) (g' (x + t)) t := by
        simpa [Function.comp_def] using
          (hg' (x + t)).comp t ((hasDerivAt_id t).const_add x)
      have h2 : HasDerivAt (fun s : ℝ => g (x - s)) (-g' (x - t)) t := by
        simpa [Function.comp_def] using
          (hg' (x - t)).comp t ((hasDerivAt_id t).const_sub x)
      simpa [sub_eq_add_neg] using (h1.add h2).sub_const (2 * g x)
    have hcont : Continuous fun s : ℝ => g (x + s) + g (x - s) - 2 * g x :=
      continuous_iff_continuousAt.mpr fun t => (hphi t).continuousAt
    obtain ⟨c, hc, heq⟩ :=
      exists_ratio_hasDerivAt_eq_ratio_slope
        (fun s => g (x + s) + g (x - s) - 2 * g x)
        (fun t => g' (x + t) - g' (x - t)) hapos hcont.continuousOn
        (fun t _ => hphi t) (fun t => t ^ 2) (fun t => 2 * t)
        (continuous_pow 2).continuousOn
        (fun t _ => by simpa using hasDerivAt_pow 2 t)
    have hc0 : (0 : ℝ) < c := hc.1
    have h2c : (0 : ℝ) < 2 * c := by linarith
    have hkey : a ^ 2 * (g' (x + c) - g' (x - c))
        = (g (x + a) + g (x - a) - 2 * g x) * (2 * c) := by
      have h0 : g (x + 0) + g (x - 0) - 2 * g x = 0 := by simp [two_mul]
      calc a ^ 2 * (g' (x + c) - g' (x - c))
          = (a ^ 2 - 0 ^ 2) * (g' (x + c) - g' (x - c)) := by norm_num
        _ = ((g (x + a) + g (x - a) - 2 * g x)
              - (g (x + 0) + g (x - 0) - 2 * g x)) * (2 * c) := heq
        _ = (g (x + a) + g (x - a) - 2 * g x) * (2 * c) := by rw [h0, sub_zero]
    have hlip : |g' (x + c) - g' (x - c)| ≤ B * (2 * c) := by
      have h := Convex.norm_image_sub_le_of_norm_hasDerivWithin_le
        (f := g') (f' := g'') (s := Set.univ)
        (fun t _ => (hg'' t).hasDerivWithinAt)
        (fun t _ => by simpa using hbound t) convex_univ
        (Set.mem_univ (x - c)) (Set.mem_univ (x + c))
      rw [Real.norm_eq_abs, Real.norm_eq_abs] at h
      have hd : x + c - (x - c) = 2 * c := by ring
      rwa [hd, abs_of_pos h2c] at h
    -- WHY cancel rather than divide: the inequality is multiplied through by
    -- the positive 2c the MVT produced, keeping everything in ring form.
    have hmul : |g (x + a) + g (x - a) - 2 * g x| * (2 * c)
        ≤ a ^ 2 * B * (2 * c) := by
      have e1 : |g (x + a) + g (x - a) - 2 * g x| * (2 * c)
          = |(g (x + a) + g (x - a) - 2 * g x) * (2 * c)| := by
        rw [abs_mul, abs_of_pos h2c]
      rw [e1, ← hkey, abs_mul, abs_of_nonneg (sq_nonneg a)]
      calc a ^ 2 * |g' (x + c) - g' (x - c)|
          ≤ a ^ 2 * (B * (2 * c)) :=
            mul_le_mul_of_nonneg_left hlip (sq_nonneg a)
        _ = a ^ 2 * B * (2 * c) := by ring
    exact le_of_mul_le_mul_right hmul h2c

/- ------------------------------------------------------------------------ -/
/- V-F2b-7: the floor statement shape (grant-set-indexed, per the re-posed  -/
/- class definition's Lean sketch; a named Prop, not asserted).              -/
/- ------------------------------------------------------------------------ -/

/-- An abstract read battery over a configuration type: finitely many reads,
one absolute slack (the granted profile's floor, D1/D2 of the theorem doc). -/
structure ReadBattery (Config : Type*) where
  reads : List (Config → ℝ)
  slack : ℝ
  slack_pos : 0 < slack

/-- Z' is invisible to the battery from Z: every read moves within slack. -/
def Invisible {Config : Type*} (B : ReadBattery Config) (Z Z' : Config) :
    Prop :=
  ∀ r ∈ B.reads, |r Z' - r Z| ≤ B.slack

/-- V-F2b-7: the merge-floor TARGET as a named Prop, deliberately NOT asserted
(session adversary F8: the earlier sorry-bodied theorem form was REFUTABLE at
degenerate instantiations, e.g. `Config := Unit` with an empty read list and a
trivial discipline placeholder, so carrying it as a theorem-with-sorry would
have asserted a falsehood-in-general). The next batch proves INSTANCES of this
Prop for configuration types equipped with the move calculus, under the typed
discipline hypotheses.
LOAD, priced: (i) the moves as operations on the configuration type; (ii) the
cost lemmas L2a/L2b (V-F2b-6 supplies the second-difference kernel); (iii) the
site-selection construction L4 in its batch-selection form (the C(R) bound of
the theorem document; needs the resonance-budget bookkeeping L5 at the
unit-resolution pair count, whose mean-value input is Montgomery-Vaughan:
available machine-checked in the zeta-23-lean repository, constant 13: cite,
do not re-prove); (iv) the regime condition and the STANDARD-battery
hypothesis, both as explicit hypotheses of any proved instance; (v) an
on-line-mass hypothesis on the base. -/
def MergeFloorTarget
    {Config : Type*} (profile : Config → Multiset ℕ)
    (B : ReadBattery Config) (Z : Config) (g : ℕ) : Prop :=
  ∃ Z', Invisible B Z Z' ∧ g ≤ excess (profile Z')

end ZetaRH.F2bSkeleton
