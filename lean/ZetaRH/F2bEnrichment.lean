/-
F2b enrichment: the configuration-side layer under the profile skeleton.

Companion to ZetaRH/F2bSkeleton.lean and to the F2a/F2b dossiers
(docs/03_research/f2a_certificate_class.md Section 8 hand-off,
docs/03_research/f2b_visibility_floor.md Sections 0-2). DELIBERATELY UNIMPORTED
by ZetaRH.lean, same house pattern as the skeleton. The skeleton works at the
h-profile register (Multiset N); this file works one level down, at a minimal
ZERO-CONFIGURATION model (finite multiset of strip points with multiplicity),
and proves the two Section 8 targets that need beta-data the profile cannot
see, plus the first non-vacuous instance of the skeleton's MergeFloorTarget,
plus the L4 statement shape. NO sorry anywhere in this file.

Model honesty, priced once: coordinates live in Q, not R or C. The finite
combinatorics of the registers is field-blind (nothing below consumes
completeness or topology of the coordinate field), and Q keeps every example
decide-checkable. The FE pairing rides as the hypothesis `FESymmetric`
(invariance of the multiset under beta |-> 1 - beta at fixed gamma): that is
the model form of the functional-equation zero pairing, exactly the C0-frame
clause the dossier's V-F2a-3 and V-F2a-4 statements consume. Multiplicity is carried in
the `mult` field; the `Reduced` predicate (entries are pairwise-distinct strip
points) is the encoding discipline that makes `multMass` read the dossier's
N_mult. Positivity of multiplicities (`hm`) is definitional in the dossier's
multiset convention and explicit here.

Hypothesis loads, priced per target:
  E1 (V-F2a-3, register collapse)    : carried: hm (mult >= 1), FESymmetric,
        Reduced. PROVED: C4 (excess of the derived h-profile = 0) iff every
        zero is simple AND on the line. Forward consumes hm + FE only (an
        off-line zero forces a distinct FE partner on its line, h >= 2);
        Reduced is consumed exactly once, in the backward direction (two
        on-line simple entries at one ordinate would be one point listed
        twice). C4 => C4-loc rides as a corollary of E2; C4 => C4-fin is
        stated in windowed form via the configuration-level monotonicity
        lemma (in a single finite window the O(1) register is bookkeeping,
        which is the dossier's own verdict on C4-fin).
  E2 (V-F2a-4, sum-register form)    : carried: hm, FESymmetric. PROVED:
        N_off + N_mult <= E, by a per-zero charge argument (each zero of
        multiplicity m on a line of mass h pays m per register it defects in,
        against capacity m*(h-1); FE gives h >= 2m off the line, membership
        gives h >= m at multiplicity >= 2). Strictly stronger than the
        skeleton's profile surrogate `domination`; the session adversary's F9
        configuration (two off-line doubles on one line: 4 + 4 = 8 <= 12) is
        decide-checked below. A zero both off-line and multiple pays BOTH
        registers, as required.
  E3 (V-F2b-7, first instance)       : PROVED, two layers: a conditional
        instance theorem (any battery whose reads factor through the profile
        sum N is blind to the two-simple-lines merge, which raises E by
        exactly 2), and a fully concrete end-to-end example (base {1,1},
        one-read battery, g = 2) with decide-checked non-vacuity. The
        analytic load the skeleton's docstring prices (moves calculus, L2
        costs, L4, regime + STANDARD hypotheses) is MIRRORED here by the
        `hreads` factoring hypothesis: that is the honest simplified form,
        not a discharge of the analytic content.
  E4 (L4, site selection)            : statement shape ONLY, as a named Prop
        (the V-F2b-7 discipline: a def, not a sorry-bodied theorem). Load
        priced at the def: Montgomery-Vaughan is the named mean-value input
        (in-print MV 1974; the zeta-23-lean repository proves the needed
        instance with constant 13: cite, do not re-prove); R is the L5
        unit-resolution resonance budget; the batch-selection constant C(R)
        replaces the refuted per-step invariant (session adversary F5(a));
        the regime condition rides as the Prop's antecedent, honest scope.
-/

import Mathlib
import ZetaRH.F2bSkeleton

namespace ZetaRH.F2bEnrichment

open ZetaRH.F2bSkeleton

/- ------------------------------------------------------------------------ -/
/- The zero-configuration model.                                            -/
/- ------------------------------------------------------------------------ -/

/-- A zero in the strip window: real part `beta`, ordinate `gamma`,
multiplicity `mult`. Coordinates in Q (see the header: the register
combinatorics is field-blind and Q keeps examples decide-checkable). -/
structure StripZero where
  beta : ℚ
  gamma : ℚ
  mult : ℕ
deriving DecidableEq, Repr

/-- The functional-equation involution on strip points: beta |-> 1 - beta at
fixed ordinate and multiplicity. -/
def feMap (z : StripZero) : StripZero :=
  ⟨1 - z.beta, z.gamma, z.mult⟩

/-- The configuration is functional-equation symmetric: the multiset is
invariant under `feMap`. The model form of the FE zero pairing (C0 frame). -/
def FESymmetric (Z : Multiset StripZero) : Prop :=
  Z.map feMap = Z

/-- The encoding discipline: entries are pairwise-distinct strip POINTS, so
multiplicity is carried in `mult`, never by duplicate listing. -/
def Reduced (Z : Multiset StripZero) : Prop :=
  (Z.map fun z => (z.beta, z.gamma)).Nodup

/-- The occupied ordinates (horizontal lines) of a configuration. -/
def ordinates (Z : Multiset StripZero) : Finset ℚ :=
  Z.toFinset.image fun z => z.gamma

/-- The multiplicity mass h(gamma) on one horizontal line. -/
def lineMass (Z : Multiset StripZero) (γ : ℚ) : ℕ :=
  ((Z.filter fun z => z.gamma = γ).map fun z => z.mult).sum

/-- The derived h-profile: one entry per occupied line. This is the extraction
the skeleton's header defers ("definitional bookkeeping"); here it is the
definition, so the skeleton's profile theorems apply to configurations. -/
def hprofile (Z : Multiset StripZero) : Multiset ℕ :=
  (ordinates Z).val.map (lineMass Z)

/-- N_off: total multiplicity carried by off-line zeros. -/
def offMass (Z : Multiset StripZero) : ℕ :=
  ((Z.filter fun z => z.beta ≠ 1 / 2).map fun z => z.mult).sum

/-- N_mult: total multiplicity carried by multiple zeros. A zero both off-line
and multiple counts in BOTH registers (session adversary F9). -/
def multMass (Z : Multiset StripZero) : ℕ :=
  ((Z.filter fun z => 2 ≤ z.mult).map fun z => z.mult).sum

/- ------------------------------------------------------------------------ -/
/- Finite bookkeeping helpers (multiset sums, fibers, line masses).         -/
/- ------------------------------------------------------------------------ -/

private lemma sum_le_sum_of_le {s t : Multiset ℕ} (h : s ≤ t) :
    s.sum ≤ t.sum := by
  obtain ⟨u, rfl⟩ := Multiset.le_iff_exists_add.mp h
  rw [Multiset.sum_add]
  exact Nat.le_add_right _ _

/-- A filtered-map sum as an indicator sum over the whole configuration. -/
private lemma filter_map_sum (p : StripZero → Prop) [DecidablePred p]
    (f : StripZero → ℕ) (Z : Multiset StripZero) :
    ((Z.filter p).map f).sum = (Z.map fun z => if p z then f z else 0).sum := by
  induction Z using Multiset.induction_on with
  | empty => simp
  | cons z Z' ih =>
      by_cases h : p z
      · simp [h, ih]
      · simp [h, ih]

/-- Regrouping a configuration sum by horizontal line. WHY by hand: Mathlib's
fiberwise lemmas live on Finset sums; the configuration is a multiset, so the
decomposition is a one-induction lemma here rather than an import. -/
private lemma fiber_sum (f : StripZero → ℕ) (S : Finset ℚ) :
    ∀ Z : Multiset StripZero, (∀ z ∈ Z, z.gamma ∈ S) →
      (Z.map f).sum
        = ∑ γ ∈ S, ((Z.filter fun z => z.gamma = γ).map f).sum := by
  intro Z
  induction Z using Multiset.induction_on with
  | empty => intro _; simp
  | cons z Z' ih =>
      intro hmem
      have hz : z.gamma ∈ S := hmem z (Multiset.mem_cons_self z Z')
      have ih' := ih fun w hw => hmem w (Multiset.mem_cons_of_mem hw)
      rw [Multiset.map_cons, Multiset.sum_cons, ih']
      have hsplit : ∀ γ ∈ S,
          (((z ::ₘ Z').filter fun w => w.gamma = γ).map f).sum
            = (if z.gamma = γ then f z else 0)
              + ((Z'.filter fun w => w.gamma = γ).map f).sum := by
        intro γ _
        by_cases h : z.gamma = γ
        · simp [h]
        · simp [h]
      rw [Finset.sum_congr rfl hsplit, Finset.sum_add_distrib,
        Finset.sum_ite_eq S z.gamma fun _ => f z, if_pos hz]

private lemma sum_map_mult_mul (s : Multiset StripZero) (c : ℕ) :
    (s.map fun z => z.mult * c).sum = (s.map fun z => z.mult).sum * c := by
  induction s using Multiset.induction_on with
  | empty => simp
  | cons z s ih => simp [ih, add_mul]

private lemma gamma_mem_ordinates {Z : Multiset StripZero} {z : StripZero}
    (hz : z ∈ Z) : z.gamma ∈ ordinates Z :=
  Finset.mem_image.mpr ⟨z, Multiset.mem_toFinset.mpr hz, rfl⟩

/-- The profile excess as a Finset sum over occupied lines. -/
private lemma excess_hprofile (Z : Multiset StripZero) :
    excess (hprofile Z)
      = ∑ γ ∈ ordinates Z, lineMass Z γ * (lineMass Z γ - 1) := by
  unfold excess hprofile
  rw [Multiset.map_map, Finset.sum_eq_multiset_sum]
  rfl

/-- Membership bounds the line mass below (Fact B of the charge argument). -/
private lemma le_lineMass_of_mem {Z : Multiset StripZero} {z : StripZero}
    (hz : z ∈ Z) : z.mult ≤ lineMass Z z.gamma := by
  unfold lineMass
  apply Multiset.le_sum_of_mem
  exact Multiset.mem_map_of_mem _ (Multiset.mem_filter.mpr ⟨hz, rfl⟩)

/-- Two DISTINCT entries on one line bound its mass by the sum of their
multiplicities. -/
private lemma pair_le_lineMass {Z : Multiset StripZero} {z w : StripZero}
    (hz : z ∈ Z) (hw : w ∈ Z) (hgam : w.gamma = z.gamma) (hne : w ≠ z) :
    z.mult + w.mult ≤ lineMass Z z.gamma := by
  have hzF : z ∈ Z.filter fun v => v.gamma = z.gamma :=
    Multiset.mem_filter.mpr ⟨hz, rfl⟩
  have hwF : w ∈ Z.filter fun v => v.gamma = z.gamma :=
    Multiset.mem_filter.mpr ⟨hw, hgam⟩
  have hwE : w ∈ (Z.filter fun v => v.gamma = z.gamma).erase z :=
    (Multiset.mem_erase_of_ne hne).mpr hwF
  have hle : w.mult
      ≤ (((Z.filter fun v => v.gamma = z.gamma).erase z).map
          fun v => v.mult).sum :=
    Multiset.le_sum_of_mem (Multiset.mem_map_of_mem _ hwE)
  have hcons : z ::ₘ (Z.filter fun v => v.gamma = z.gamma).erase z
      = Z.filter fun v => v.gamma = z.gamma := Multiset.cons_erase hzF
  unfold lineMass
  calc z.mult + w.mult
      ≤ z.mult + (((Z.filter fun v => v.gamma = z.gamma).erase z).map
          fun v => v.mult).sum := Nat.add_le_add_left hle _
    _ = ((z ::ₘ (Z.filter fun v => v.gamma = z.gamma).erase z).map
          fun v => v.mult).sum := by rw [Multiset.map_cons, Multiset.sum_cons]
    _ = ((Z.filter fun v => v.gamma = z.gamma).map fun v => v.mult).sum := by
        rw [hcons]

/-- Fact A of the charge argument: an off-line zero drags a DISTINCT FE
partner of equal multiplicity onto its own line, so h >= 2m there. This is
the single place the functional equation is consumed. -/
private lemma offline_forces_partner {Z : Multiset StripZero}
    (hfe : FESymmetric Z) {z : StripZero} (hz : z ∈ Z)
    (hoff : z.beta ≠ 1 / 2) : 2 * z.mult ≤ lineMass Z z.gamma := by
  have hfz : feMap z ∈ Z := by
    rw [← hfe]
    exact Multiset.mem_map_of_mem feMap hz
  have hne : feMap z ≠ z := by
    intro h
    have hb : (1 : ℚ) - z.beta = z.beta := congrArg StripZero.beta h
    exact hoff (by linarith)
  have hp := pair_le_lineMass hz hfz rfl hne
  have hmm : (feMap z).mult = z.mult := rfl
  rw [hmm] at hp
  omega

/-- The per-zero charge bound: a zero of multiplicity m on a line of mass h
pays m for each register it defects in, against capacity m*(h-1). WHY this
shape: summed over the line it gives off + mult <= h(h-1) with no case surgery
on h = 2 (the FE partner kills the off-line-double-alone corner via h >= 2m),
and the F9 both-registers double-count comes out correct by construction. -/
private lemma per_zero_charge {Z : Multiset StripZero} (hfe : FESymmetric Z)
    {z : StripZero} (hz : z ∈ Z) (hm1 : 1 ≤ z.mult) :
    (if z.beta ≠ 1 / 2 then z.mult else 0)
        + (if 2 ≤ z.mult then z.mult else 0)
      ≤ z.mult * (lineMass Z z.gamma - 1) := by
  have hB := le_lineMass_of_mem hz
  by_cases hoff : z.beta ≠ 1 / 2
  · have hA := offline_forces_partner hfe hz hoff
    rw [if_pos hoff]
    by_cases hmul : 2 ≤ z.mult
    · rw [if_pos hmul]
      have h3 : 2 ≤ lineMass Z z.gamma - 1 := by omega
      calc z.mult + z.mult = z.mult * 2 := by ring
        _ ≤ z.mult * (lineMass Z z.gamma - 1) := Nat.mul_le_mul le_rfl h3
    · rw [if_neg hmul]
      have h1 : z.mult = 1 := by omega
      rw [h1] at hA ⊢
      omega
  · rw [if_neg hoff]
    by_cases hmul : 2 ≤ z.mult
    · rw [if_pos hmul]
      have h1 : 1 ≤ lineMass Z z.gamma - 1 := by omega
      calc 0 + z.mult = z.mult * 1 := by ring
        _ ≤ z.mult * (lineMass Z z.gamma - 1) := Nat.mul_le_mul le_rfl h1
    · rw [if_neg hmul]
      simp

/- ------------------------------------------------------------------------ -/
/- E2 = V-F2a-4: the sum-register domination N_off + N_mult <= E.           -/
/- ------------------------------------------------------------------------ -/

/-- V-F2a-4 in its full SUM-REGISTER form: over any FE-symmetric configuration
with positive multiplicities, N_off + N_mult <= E. Strictly stronger than the
skeleton's profile surrogate `domination` (which cannot see beta-data); the
extra input is exactly the FE pairing, consumed once in
`offline_forces_partner`. `Reduced` is NOT needed here: with duplicate-listing
encodings the theorem stays true, only the reading of `multMass` as the
dossier's N_mult presumes reduced encodings (header pricing). -/
theorem sum_register_domination (Z : Multiset StripZero)
    (hfe : FESymmetric Z) (hm : ∀ z ∈ Z, 1 ≤ z.mult) :
    offMass Z + multMass Z ≤ excess (hprofile Z) := by
  have hoffZ : offMass Z
      = (Z.map fun z => if z.beta ≠ 1 / 2 then z.mult else 0).sum :=
    filter_map_sum _ _ Z
  have hmultZ : multMass Z
      = (Z.map fun z => if 2 ≤ z.mult then z.mult else 0).sum :=
    filter_map_sum _ _ Z
  have hsum : (Z.map fun z => (if z.beta ≠ 1 / 2 then z.mult else 0)
        + (if 2 ≤ z.mult then z.mult else 0)).sum
      ≤ (Z.map fun z => z.mult * (lineMass Z z.gamma - 1)).sum :=
    Multiset.sum_map_le_sum_map _ _ fun z hz =>
      per_zero_charge hfe hz (hm z hz)
  have hfib : (Z.map fun z => z.mult * (lineMass Z z.gamma - 1)).sum
      = excess (hprofile Z) := by
    rw [fiber_sum _ (ordinates Z) Z fun z hz => gamma_mem_ordinates hz,
      excess_hprofile Z]
    refine Finset.sum_congr rfl fun γ hγ => ?_
    have hcongr : (Z.filter fun z => z.gamma = γ).map
          (fun z => z.mult * (lineMass Z z.gamma - 1))
        = (Z.filter fun z => z.gamma = γ).map
          (fun z => z.mult * (lineMass Z γ - 1)) :=
      Multiset.map_congr rfl fun z hz => by
        rw [(Multiset.mem_filter.mp hz).2]
    rw [hcongr, sum_map_mult_mul]
    rfl
  calc offMass Z + multMass Z
      = (Z.map fun z => (if z.beta ≠ 1 / 2 then z.mult else 0)
          + (if 2 ≤ z.mult then z.mult else 0)).sum := by
        rw [hoffZ, hmultZ, ← Multiset.sum_map_add]
    _ ≤ (Z.map fun z => z.mult * (lineMass Z z.gamma - 1)).sum := hsum
    _ = excess (hprofile Z) := hfib

/-- Session adversary F9's configuration: one line (gamma = 0) made of two
off-line double zeros (an FE pair). Both registers read 4, the line's E-term
is 12, and 4 + 4 = 8 <= 12: the both-defective double count comes out TRUE,
decide-checked, as the hand-off demanded. -/
def f9Config : Multiset StripZero :=
  {⟨7 / 10, 0, 2⟩, ⟨3 / 10, 0, 2⟩}

-- WHY norm_num rather than decide: Rat literal arithmetic does not
-- kernel-reduce (Nat.gcd normalization), so the checks run through simp.
example : FESymmetric f9Config := by
  unfold FESymmetric f9Config
  rw [Multiset.insert_eq_cons, Multiset.map_cons, Multiset.map_singleton,
    show feMap ⟨7 / 10, 0, 2⟩ = (⟨3 / 10, 0, 2⟩ : StripZero) by
      norm_num [feMap],
    show feMap ⟨3 / 10, 0, 2⟩ = (⟨7 / 10, 0, 2⟩ : StripZero) by
      norm_num [feMap]]
  exact Multiset.cons_swap _ _ _

example : offMass f9Config = 4 := by
  unfold offMass f9Config
  rw [Multiset.insert_eq_cons, Multiset.filter_cons,
    Multiset.filter_singleton,
    if_pos (show (⟨7 / 10, 0, 2⟩ : StripZero).beta ≠ 1 / 2 by norm_num),
    if_pos (show (⟨3 / 10, 0, 2⟩ : StripZero).beta ≠ 1 / 2 by norm_num)]
  rfl

example : multMass f9Config = 4 := by
  unfold multMass f9Config
  rw [Multiset.insert_eq_cons, Multiset.filter_cons,
    Multiset.filter_singleton,
    if_pos (show 2 ≤ (⟨7 / 10, 0, 2⟩ : StripZero).mult by norm_num),
    if_pos (show 2 ≤ (⟨3 / 10, 0, 2⟩ : StripZero).mult by norm_num)]
  rfl

example : excess (hprofile f9Config) = 12 := by
  have hord : ordinates f9Config = {0} := by
    unfold ordinates f9Config
    rw [Multiset.insert_eq_cons, Multiset.toFinset_cons,
      Multiset.toFinset_singleton, Finset.image_insert,
      Finset.image_singleton]
    exact Finset.insert_eq_self.mpr (Finset.mem_singleton_self _)
  have hline : lineMass f9Config 0 = 4 := by
    unfold lineMass f9Config
    rw [Multiset.insert_eq_cons, Multiset.filter_cons,
      Multiset.filter_singleton,
      if_pos (show (⟨7 / 10, 0, 2⟩ : StripZero).gamma = 0 from rfl),
      if_pos (show (⟨3 / 10, 0, 2⟩ : StripZero).gamma = 0 from rfl)]
    rfl
  rw [excess_hprofile, hord, Finset.sum_singleton, hline]

/- ------------------------------------------------------------------------ -/
/- E1 = V-F2a-3: the register-collapse lemma (C4 iff simple-and-on-line).   -/
/- ------------------------------------------------------------------------ -/

/-- V-F2a-3, the register-collapse lemma: C4 (excess of the derived h-profile
vanishes) holds iff every zero is simple AND on the critical line. Hypotheses
priced in the header: `hm` and `hfe` power the forward direction (an off-line
zero's FE partner forces h >= 2 on its line); `hred` is consumed exactly once,
in the backward direction. -/
theorem register_collapse (Z : Multiset StripZero)
    (hfe : FESymmetric Z) (hm : ∀ z ∈ Z, 1 ≤ z.mult) (hred : Reduced Z) :
    excess (hprofile Z) = 0 ↔ ∀ z ∈ Z, z.mult = 1 ∧ z.beta = 1 / 2 := by
  constructor
  · intro h0
    have hline : ∀ γ ∈ ordinates Z, lineMass Z γ ≤ 1 := by
      intro γ hγ
      have hmem : lineMass Z γ * (lineMass Z γ - 1)
          ∈ (hprofile Z).map fun h => h * (h - 1) :=
        Multiset.mem_map_of_mem _
          (Multiset.mem_map_of_mem _ (Finset.mem_val.mpr hγ))
      have hzero := Multiset.sum_eq_zero_iff.mp h0 _ hmem
      rcases Nat.mul_eq_zero.mp hzero with h | h <;> omega
    intro z hz
    have h1 : lineMass Z z.gamma ≤ 1 := hline _ (gamma_mem_ordinates hz)
    have hB := le_lineMass_of_mem hz
    have hm1 := hm z hz
    refine ⟨by omega, ?_⟩
    by_contra hoff
    have hA := offline_forces_partner hfe hz hoff
    omega
  · intro hall
    have hline : ∀ γ ∈ ordinates Z, lineMass Z γ ≤ 1 := by
      intro γ hγ
      by_contra hgt
      rw [not_le] at hgt
      -- WHY Reduced fires here: with every zero simple and on the line, a
      -- line of mass >= 2 must list the point (1/2, gamma) at least twice.
      have hlm : lineMass Z γ = (Z.filter fun z => z.gamma = γ).card := by
        unfold lineMass
        have hone : (Z.filter fun z => z.gamma = γ).map (fun z => z.mult)
            = Multiset.replicate (Z.filter fun z => z.gamma = γ).card 1 := by
          rw [Multiset.eq_replicate]
          refine ⟨by rw [Multiset.card_map], ?_⟩
          intro m hm'
          obtain ⟨z, hzF, rfl⟩ := Multiset.mem_map.mp hm'
          exact (hall z (Multiset.mem_filter.mp hzF).1).1
        rw [hone, Multiset.sum_replicate, nsmul_eq_mul, mul_one, Nat.cast_id]
      have hrep : (Z.filter fun z => z.gamma = γ).map
            (fun z => (z.beta, z.gamma))
          = Multiset.replicate (Z.filter fun z => z.gamma = γ).card
              ((1 / 2 : ℚ), γ) := by
        rw [Multiset.eq_replicate]
        refine ⟨by rw [Multiset.card_map], ?_⟩
        intro p hp
        obtain ⟨z, hzF, rfl⟩ := Multiset.mem_map.mp hp
        obtain ⟨hzZ, hzg⟩ := Multiset.mem_filter.mp hzF
        rw [(hall z hzZ).2, hzg]
      have hnd : ((Z.filter fun z => z.gamma = γ).map
          fun z => (z.beta, z.gamma)).Nodup :=
        Multiset.nodup_of_le (Multiset.map_le_map (Multiset.filter_le _ Z))
          hred
      rw [hrep] at hnd
      have hcount := Multiset.nodup_iff_count_le_one.mp hnd ((1 / 2 : ℚ), γ)
      rw [Multiset.count_replicate] at hcount
      simp at hcount
      omega
    refine Multiset.sum_eq_zero_iff.mpr fun x hx => ?_
    obtain ⟨h, hh, rfl⟩ := Multiset.mem_map.mp hx
    obtain ⟨γ, hγ, rfl⟩ := Multiset.mem_map.mp hh
    have hle := hline γ (Finset.mem_val.mp hγ)
    show lineMass Z γ * (lineMass Z γ - 1) = 0
    rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hle with h | h <;> simp [h]

/-- C4 => C4-loc (and the simplicity register too): exact completeness kills
both defect registers. The FE pairing is consumed through E2. -/
theorem c4_implies_c4loc (Z : Multiset StripZero)
    (hfe : FESymmetric Z) (hm : ∀ z ∈ Z, 1 ≤ z.mult)
    (h0 : excess (hprofile Z) = 0) : offMass Z = 0 ∧ multMass Z = 0 := by
  have h := sum_register_domination Z hfe hm
  omega

/-- Window monotonicity at the CONFIGURATION level (the skeleton's V-F2b-4 is
the profile form; sub-multisets of zeros do not correspond to sub-multisets of
profiles, so this is a separate finite lemma). -/
theorem excess_hprofile_mono (W Z : Multiset StripZero) (hle : W ≤ Z) :
    excess (hprofile W) ≤ excess (hprofile Z) := by
  rw [excess_hprofile W, excess_hprofile Z]
  have hsub : ordinates W ⊆ ordinates Z := by
    intro γ hγ
    obtain ⟨z, hz, rfl⟩ := Finset.mem_image.mp hγ
    exact gamma_mem_ordinates (Multiset.mem_of_le hle
      (Multiset.mem_toFinset.mp hz))
  have hlm : ∀ γ, lineMass W γ ≤ lineMass Z γ := fun γ =>
    sum_le_sum_of_le (Multiset.map_le_map (Multiset.filter_le_filter _ hle))
  calc ∑ γ ∈ ordinates W, lineMass W γ * (lineMass W γ - 1)
      ≤ ∑ γ ∈ ordinates W, lineMass Z γ * (lineMass Z γ - 1) :=
        Finset.sum_le_sum fun γ _ =>
          Nat.mul_le_mul (hlm γ) (Nat.sub_le_sub_right (hlm γ) 1)
    _ ≤ ∑ γ ∈ ordinates Z, lineMass Z γ * (lineMass Z γ - 1) :=
        Finset.sum_le_sum_of_subset hsub

/-- C4 => C4-fin, in the only form with content on a single finite window:
exact completeness propagates to EVERY sub-window (in a fixed window E is a
fixed natural number, so the O(1) register is bookkeeping, the dossier's own
verdict; the windowed statement is what monotonicity actually buys). -/
theorem c4_implies_c4fin (Z : Multiset StripZero)
    (h0 : excess (hprofile Z) = 0) (W : Multiset StripZero) (hle : W ≤ Z) :
    excess (hprofile W) = 0 := by
  have h := excess_hprofile_mono W Z hle
  omega

/- ------------------------------------------------------------------------ -/
/- E3 = V-F2b-7: the first proved MergeFloorTarget instance.                -/
/- ------------------------------------------------------------------------ -/

/-- The merge move at the profile register: remove lines `a` and `b`, add the
merged line `a + b`. At a = b = 1 this is the theorem document's (M) event
pair (two simple lines to one double line). -/
def mergeLines (H : Multiset ℕ) (a b : ℕ) : Multiset ℕ :=
  (a + b) ::ₘ (H.erase a).erase b

/-- The two-simple-lines merge preserves the profile sum N (the merge moves
mass, never creates it). -/
lemma mergeLines_ncount (H : Multiset ℕ) (h1 : 1 ∈ H)
    (h2 : 1 ∈ H.erase 1) : ncount (mergeLines H 1 1) = ncount H := by
  have e1 : (1 : ℕ) ::ₘ H.erase 1 = H := Multiset.cons_erase h1
  have e2 : (1 : ℕ) ::ₘ (H.erase 1).erase 1 = H.erase 1 :=
    Multiset.cons_erase h2
  unfold ncount mergeLines
  calc ((1 + 1 : ℕ) ::ₘ (H.erase 1).erase 1).sum
      = 1 + 1 + ((H.erase 1).erase 1).sum := Multiset.sum_cons _ _
    _ = 1 + (1 + ((H.erase 1).erase 1).sum) := by ring
    _ = 1 + ((1 : ℕ) ::ₘ (H.erase 1).erase 1).sum := by
        rw [Multiset.sum_cons]
    _ = 1 + (H.erase 1).sum := by rw [e2]
    _ = ((1 : ℕ) ::ₘ H.erase 1).sum := (Multiset.sum_cons _ _).symm
    _ = H.sum := by rw [e1]

/-- The two-simple-lines merge raises the excess by exactly 2 (the L2 cost
identity at the profile register: two h = 1 lines pay 0, one h = 2 line pays
2). -/
lemma mergeLines_excess (H : Multiset ℕ) (h1 : 1 ∈ H)
    (h2 : 1 ∈ H.erase 1) : excess (mergeLines H 1 1) = excess H + 2 := by
  have e1 : (1 : ℕ) ::ₘ H.erase 1 = H := Multiset.cons_erase h1
  have e2 : (1 : ℕ) ::ₘ (H.erase 1).erase 1 = H.erase 1 :=
    Multiset.cons_erase h2
  have hH : excess H
      = (((H.erase 1).erase 1).map fun h => h * (h - 1)).sum := by
    conv_lhs => rw [← e1, ← e2]
    unfold excess
    rw [Multiset.map_cons, Multiset.sum_cons, Multiset.map_cons,
      Multiset.sum_cons]
    norm_num
  calc excess (mergeLines H 1 1)
      = (1 + 1) * (1 + 1 - 1)
          + (((H.erase 1).erase 1).map fun h => h * (h - 1)).sum := by
        unfold mergeLines excess
        rw [Multiset.map_cons, Multiset.sum_cons]
    _ = 2 + (((H.erase 1).erase 1).map fun h => h * (h - 1)).sum := by
        norm_num
    _ = excess H + 2 := by rw [hH]; omega

/-- The CONDITIONAL first instance of the skeleton's `MergeFloorTarget`: any
battery whose reads all factor through the profile sum N is blind to the
two-simple-lines merge, which raises E by exactly 2. The `hreads` factoring
hypothesis is the priced simplified mirror of the skeleton's load items
(i)-(iii) (moves calculus + L2 costs + L4 site selection); items (iv)-(v)
(regime, STANDARD battery, on-line mass) degenerate at the profile register
because the move is EXACTLY invisible (cost 0 < any slack), which is why this
instance is provable outright. It is not degenerate-vacuous: the example
below instantiates it with a nonempty read list and g = 2 (session adversary
F8's demand). -/
theorem merge_floor_instance (H : Multiset ℕ) (B : ReadBattery (Multiset ℕ))
    (h1 : 1 ∈ H) (h2 : 1 ∈ H.erase 1)
    (hreads : ∀ r ∈ B.reads, ∀ K K' : Multiset ℕ,
      ncount K = ncount K' → r K = r K') :
    MergeFloorTarget id B H (excess H + 2) := by
  refine ⟨mergeLines H 1 1, fun r hr => ?_, ?_⟩
  · rw [hreads r hr (mergeLines H 1 1) H (mergeLines_ncount H h1 h2),
      sub_self, abs_zero]
    exact le_of_lt B.slack_pos
  · exact le_of_eq (by rw [id_eq, mergeLines_excess H h1 h2])

/-- The one-read battery whose single read is the profile sum N (the
zero-counting read: the C0 frame's own functional). Nonempty read list. -/
def exampleBattery : ReadBattery (Multiset ℕ) where
  reads := [fun H => (ncount H : ℝ)]
  slack := 1
  slack_pos := one_pos

private lemma exampleBattery_reads_factor :
    ∀ r ∈ exampleBattery.reads, ∀ K K' : Multiset ℕ,
      ncount K = ncount K' → r K = r K' := by
  intro r hr K K' hKK
  have hr' : r = fun H => (ncount H : ℝ) := List.mem_singleton.mp hr
  subst hr'
  show ((ncount K : ℕ) : ℝ) = ((ncount K' : ℕ) : ℝ)
  exact_mod_cast hKK

/-- The first END-TO-END proved instance of `MergeFloorTarget`: base {1, 1}
(two simple critical lines), the one-read N battery, floor g = 2. The merge
{1,1} -> {2} moves the only read by exactly 0 < slack and raises the excess
from 0 to 2. -/
theorem example_merge_floor :
    MergeFloorTarget id exampleBattery ({1, 1} : Multiset ℕ) 2 := by
  have h := merge_floor_instance {1, 1} exampleBattery (by decide) (by decide)
    exampleBattery_reads_factor
  have hE : excess ({1, 1} : Multiset ℕ) = 0 := by decide
  rwa [hE, zero_add] at h

-- Non-vacuity witnesses, decide-checked (session adversary F8): the base and
-- the merged configuration are concrete, the read is unmoved, the excess
-- jumps 0 -> 2, and the read list is nonempty.
example : excess ({1, 1} : Multiset ℕ) = 0 := by decide
example : excess (mergeLines ({1, 1} : Multiset ℕ) 1 1) = 2 := by decide
example : ncount (mergeLines ({1, 1} : Multiset ℕ) 1 1)
    = ncount ({1, 1} : Multiset ℕ) := by decide
example : exampleBattery.reads.length = 1 := rfl

/- ------------------------------------------------------------------------ -/
/- E4 = L4: the site-selection statement shape (typed Prop, no assertion).  -/
/- ------------------------------------------------------------------------ -/

/-- The abstract move calculus a proved L4 instance must supply: a type of
positioning-and-merge EVENTS (one disjoint on-line pair each), the
disjointness discipline, and batch application. Abstract on purpose: the
skeleton's V-F2b-7 load item (i). -/
structure MoveCalculus (Config : Type*) where
  Event : Type
  disjoint : Finset Event → Prop
  apply : Config → Finset Event → Config

/-- L4 (site selection under resonance families) as a TYPED statement shape,
per the V-F2b-7 discipline: a named Prop, deliberately NOT asserted (the
theorem form would be refutable at degenerate instantiations, session
adversary F8's lesson). Reading: IF the regime condition holds (the
antecedent: the slack floor epsG*T*L dominates the resonance budget R plus
the coherent-placement residual sigSup*vbar at the batch-selection constant
C = C(R); honest scope, not decoration), THEN for every k up to the slack
budget c1*epsG*T*L there is a disjoint batch of k events moving every granted
read within HALF its family slack.
LOAD, priced: (i) R is the L5 resonance budget, whose mean-value input is
Montgomery-Vaughan at the UNIT-RESOLUTION pair count (session adversary F6):
in-print MV 1974, and the zeta-23-lean repository proves the needed instance
machine-checked with constant 13: cite, do not re-prove; (ii) the
batch-selection constant C(R) replaces the per-step partial-sums invariant
refuted by session adversary F5(a); (iii) any proved instance must supply the
rigid-base aligned-site identity (v_e = 0 on lattice-respecting merges) and
the generic-base small-gap selection, the e1ag build's stages E and C; (iv)
`granted` abstracts the family data as read batteries with per-family slacks
(delta-check edits 1-3 fix the normalizations). -/
def SiteSelectionL4 {Config : Type*} (M : MoveCalculus Config)
    (granted : List (ReadBattery Config)) (Z0 : Config)
    (epsG T L R c1 C sigSup vbar : ℝ) : Prop :=
  C * (R + sigSup * vbar) ≤ epsG * (T * L) →
    ∀ k : ℕ, (k : ℝ) ≤ c1 * (epsG * (T * L)) →
      ∃ S : Finset M.Event, M.disjoint S ∧ S.card = k ∧
        ∀ B ∈ granted, ∀ r ∈ B.reads,
          |r (M.apply Z0 S) - r Z0| ≤ B.slack / 2

end ZetaRH.F2bEnrichment
