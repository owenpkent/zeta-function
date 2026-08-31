/-
#e2bd-1: the D-H invisibility floor certificate, Lean shadow (LEARNINGS #199,
dossier `experiments/arithmetic_geometric/e2bd_dh_invisibility.md`, its Section 5
item 2: "the certificate's skeleton (finite covering + per-ball rational bounds)
is a finite conjunction").

WHAT IS PROVED HERE (the skeleton, sorry-free): given ANY function `F : ℝ → ℝ`
satisfying the finite per-ball lower bounds of the witness table below, the floor
constant `c = 3303/10000` (the minimum of the table's floors) satisfies
`1/20 < c` and `c ≤ F t` for every `t` in the window `[85.2, 86.2]`. The Lean
content is exactly the finite conjunction: the 32 intervals COVER the window
(rational interval arithmetic, discharged by `norm_num` through the chain
checker), the floor constant is the table minimum and exceeds `1/20`, and the
glue (every window point lies in some ball, so `F t ≥` that ball's floor `≥ c`).

WHAT IS CARRIED, NOT PROVED (the honest KERNEL style of #S4C-2 / #VQ-1a): the
analytic identification `F t = |f_DH(1/2 + it)|` and the per-ball bounds
themselves. Those are ball-arithmetic theorems (python-flint / arb, enclosure
radius ~1e-96) recorded in the e2bd dossier; they enter as the named EXTERNAL
hypothesis `PerBallBounds F`. Lean checks the skeleton, not the arb enclosures.

WITNESS DATA SOURCE: `experiments/arithmetic_geometric/e2bd_dh_invisibility.npz`
(tracked, full-mode run 2026-08-25), arrays `dh_win_mids` / `dh_win_lowers`:
1024 covering balls of half-width 2^-10 on `[852/10, 862/10]`, certified
minimum `c_DH = 0.3303200732743...` at `t ≈ 85.709`. COARSENING (so that
`norm_num` terminates fast): the 1024 balls are merged into 32 groups of 32
consecutive balls; group `j` covers `[852/10 + j/32, 852/10 + (j+1)/32]`
(center `(27269 + 10j)/320`, radius `1/64`) and its floor is the MINIMUM of the
group's 32 certified lower bounds, rounded DOWN to a multiple of `1/10000`
(with a 1e-12 pad against the float64 round of the stored arb bound), so each
merged floor is implied by the npz's per-ball certificates. The table minimum
`3303/10000 = 0.3303` sits just under the certified `c_DH = 0.33032...`, in
group 16 (the argmin group, containing the off-line pair's height 85.699 and
the certified argmin 85.709: the dossier's "lowest essentially AT the off-line
height" reading survives the coarsening).
-/

import Mathlib

namespace ZetaRH.DHFloorCertificate

/-- One covering ball of the certificate: a rational interval
    `[center - radius, center + radius]` on the critical line's `t`-axis and a
    rational lower bound (`floor`) certified for `|f_DH(1/2 + it)|` on it. -/
structure BallWitness where
  center : ℚ
  radius : ℚ
  floor  : ℚ

namespace BallWitness

/-- Validity: a ball is a real interval with a positive certified floor.
    Positivity of the floor is what makes the certificate a BLINDNESS statement
    (no cokernel dip can open below it). -/
def Valid (b : BallWitness) : Prop := 0 < b.radius ∧ 0 < b.floor

/-- Left endpoint. -/
def lo (b : BallWitness) : ℚ := b.center - b.radius

/-- Right endpoint. -/
def hi (b : BallWitness) : ℚ := b.center + b.radius

end BallWitness

/-- The coarsened witness table: 32 merged groups of the npz's 1024 certified
    balls (see the file header for the coarsening rule). Each comment records
    the group's real-interval reading and the npz group minimum the rational
    floor rounds down. Generated from `e2bd_dh_invisibility.npz`. -/
def witnessTable : List BallWitness := [
  ⟨27269/320, 1/64, 11245/10000⟩,  -- group 0:  [85.200000, 85.231250], npz min 1.124577
  ⟨27279/320, 1/64, 10271/10000⟩,  -- group 1:  [85.231250, 85.262500], npz min 1.027161
  ⟨27289/320, 1/64, 9351/10000⟩,   -- group 2:  [85.262500, 85.293750], npz min 0.935171
  ⟨27299/320, 1/64, 8489/10000⟩,   -- group 3:  [85.293750, 85.325000], npz min 0.848949
  ⟨27309/320, 1/64, 7689/10000⟩,   -- group 4:  [85.325000, 85.356250], npz min 0.768936
  ⟨27319/320, 1/64, 6952/10000⟩,   -- group 5:  [85.356250, 85.387500], npz min 0.695250
  ⟨27329/320, 1/64, 6280/10000⟩,   -- group 6:  [85.387500, 85.418750], npz min 0.628022
  ⟨27339/320, 1/64, 5675/10000⟩,   -- group 7:  [85.418750, 85.450000], npz min 0.567566
  ⟨27349/320, 1/64, 5141/10000⟩,   -- group 8:  [85.450000, 85.481250], npz min 0.514147
  ⟨27359/320, 1/64, 4679/10000⟩,   -- group 9:  [85.481250, 85.512500], npz min 0.467924
  ⟨27369/320, 1/64, 4289/10000⟩,   -- group 10: [85.512500, 85.543750], npz min 0.428904
  ⟨27379/320, 1/64, 3967/10000⟩,   -- group 11: [85.543750, 85.575000], npz min 0.396786
  ⟨27389/320, 1/64, 3702/10000⟩,   -- group 12: [85.575000, 85.606250], npz min 0.370266
  ⟨27399/320, 1/64, 3497/10000⟩,   -- group 13: [85.606250, 85.637500], npz min 0.349777
  ⟨27409/320, 1/64, 3365/10000⟩,   -- group 14: [85.637500, 85.668750], npz min 0.336550
  ⟨27419/320, 1/64, 3306/10000⟩,   -- group 15: [85.668750, 85.700000], npz min 0.330648
  ⟨27429/320, 1/64, 3303/10000⟩,   -- group 16: [85.700000, 85.731250], npz min 0.330320 (argmin: c_DH)
  ⟨27439/320, 1/64, 3322/10000⟩,   -- group 17: [85.731250, 85.762500], npz min 0.332248
  ⟨27449/320, 1/64, 3410/10000⟩,   -- group 18: [85.762500, 85.793750], npz min 0.341033
  ⟨27459/320, 1/64, 3568/10000⟩,   -- group 19: [85.793750, 85.825000], npz min 0.356811
  ⟨27469/320, 1/64, 3794/10000⟩,   -- group 20: [85.825000, 85.856250], npz min 0.379427
  ⟨27479/320, 1/64, 4085/10000⟩,   -- group 21: [85.856250, 85.887500], npz min 0.408551
  ⟨27489/320, 1/64, 4439/10000⟩,   -- group 22: [85.887500, 85.918750], npz min 0.443913
  ⟨27499/320, 1/64, 4828/10000⟩,   -- group 23: [85.918750, 85.950000], npz min 0.482829
  ⟨27509/320, 1/64, 5273/10000⟩,   -- group 24: [85.950000, 85.981250], npz min 0.527321
  ⟨27519/320, 1/64, 5771/10000⟩,   -- group 25: [85.981250, 86.012500], npz min 0.577122
  ⟨27529/320, 1/64, 6318/10000⟩,   -- group 26: [86.012500, 86.043750], npz min 0.631847
  ⟨27539/320, 1/64, 6911/10000⟩,   -- group 27: [86.043750, 86.075000], npz min 0.691144
  ⟨27549/320, 1/64, 7546/10000⟩,   -- group 28: [86.075000, 86.106250], npz min 0.754641
  ⟨27559/320, 1/64, 8218/10000⟩,   -- group 29: [86.106250, 86.137500], npz min 0.821893
  ⟨27569/320, 1/64, 8924/10000⟩,   -- group 30: [86.137500, 86.168750], npz min 0.892420
  ⟨27579/320, 1/64, 9657/10000⟩]   -- group 31: [86.168750, 86.200000], npz min 0.965775

/-- The window's left endpoint, `85.2`. -/
def windowLo : ℚ := 852/10

/-- The window's right endpoint, `86.2` (contains the off-line pair's height 85.699). -/
def windowHi : ℚ := 862/10

/-- The floor constant of record: the minimum of the table's floors (group 16,
    the coarsened image of the certified `c_DH = 0.33032...`). Stated as a
    literal; `floorConst_is_min` proves it IS the table minimum. -/
def floorConst : ℚ := 3303/10000

/-- The chain covering checker: walking the list left to right, each ball must
    start at or before the covered frontier, and the walk succeeds once some
    ball's right end reaches `hi`. Kept as a Prop (not Bool) so that `norm_num`
    can evaluate the concrete instance by unfolding: the whole covering check
    is then finite rational interval arithmetic. -/
def ChainCovers (frontier hi : ℚ) : List BallWitness → Prop
  | [] => False
  | b :: rest => b.lo ≤ frontier ∧ (hi ≤ b.hi ∨ ChainCovers b.hi hi rest)

/-- Soundness of the chain checker over ℝ: if the rational walk succeeds, every
    REAL point of `[frontier, hi]` lies in some listed ball. This is the only
    inductive argument in the file; everything else is literal arithmetic. -/
theorem chainCovers_sound (L : List BallWitness) :
    ∀ frontier hi : ℚ, ChainCovers frontier hi L →
      ∀ t : ℝ, (frontier : ℝ) ≤ t → t ≤ (hi : ℝ) →
        ∃ b ∈ L, (b.lo : ℝ) ≤ t ∧ t ≤ (b.hi : ℝ) := by
  induction L with
  | nil =>
      intro frontier hi h
      exact absurd h (by simp [ChainCovers])
  | cons b rest ih =>
      intro frontier hi h t hlo hhi
      simp only [ChainCovers] at h
      obtain ⟨h1, h2⟩ := h
      have hblo : (b.lo : ℝ) ≤ t :=
        le_trans (by exact_mod_cast h1) hlo
      rcases h2 with h2 | h2
      · -- this ball already reaches the window's end, so it contains t
        exact ⟨b, List.mem_cons_self .., hblo, le_trans hhi (by exact_mod_cast h2)⟩
      · by_cases hc : t ≤ (b.hi : ℝ)
        · exact ⟨b, List.mem_cons_self .., hblo, hc⟩
        · -- t lies past this ball; the frontier has advanced to b.hi, recurse
          obtain ⟨b', hb', hlo', hhi'⟩ :=
            ih b.hi hi h2 t (le_of_lt (not_le.mp hc)) hhi
          exact ⟨b', List.mem_cons_of_mem b hb', hlo', hhi'⟩

/-- THE COVERING CHECK (proved content, finite ℚ interval arithmetic): the 32
    witness intervals cover `[852/10, 862/10]`. Consecutive endpoints agree
    exactly (each `lo` equals the previous `hi`), so `norm_num` closes every
    link of the chain. -/
theorem witnessTable_covers : ChainCovers windowLo windowHi witnessTable := by
  norm_num [ChainCovers, witnessTable, windowLo, windowHi,
    BallWitness.lo, BallWitness.hi]

/-- Every listed ball is valid: positive radius, positive floor. -/
theorem witnessTable_valid : ∀ b ∈ witnessTable, b.Valid := by
  intro b hb
  simp only [witnessTable] at hb
  fin_cases hb <;> exact ⟨by norm_num, by norm_num⟩

/-- The floor constant is a lower bound for every floor in the table (half of
    "c is the table minimum"; the other half is `floorConst_attained`). -/
theorem floorConst_le_floors : ∀ b ∈ witnessTable, floorConst ≤ b.floor := by
  intro b hb
  simp only [witnessTable] at hb
  fin_cases hb <;> norm_num [floorConst]

/-- The floor constant is attained (group 16), so it IS the minimum of the
    table's floors, not merely a lower bound. -/
theorem floorConst_attained : ∃ b ∈ witnessTable, b.floor = floorConst := by
  refine ⟨⟨27429/320, 1/64, 3303/10000⟩, ?_, rfl⟩
  simp [witnessTable]

/-- The 1/20 comparison of the statement-level target: `1/20 < 3303/10000`. -/
theorem one_twentieth_lt_floorConst : (1 : ℚ)/20 < floorConst := by
  norm_num [floorConst]

/-- EXTERNAL (carried, not proved): the per-ball certified lower bounds, with
    `F` standing for `t ↦ |f_DH(1/2 + it)|`. The e2bd dossier's arb run
    certifies this hypothesis for the D-H modulus (enclosure radius ~1e-96 per
    ball, 1024 balls, coarsened here to 32); Lean consumes it abstractly. -/
def PerBallBounds (F : ℝ → ℝ) : Prop :=
  ∀ b ∈ witnessTable, ∀ t : ℝ, (b.lo : ℝ) ≤ t → t ≤ (b.hi : ℝ) → (b.floor : ℝ) ≤ F t

/-- THE SKELETON THEOREM (the glue): under the per-ball bounds, the table
    minimum floors `F` on the whole window `[85.2, 86.2]`. Chain: every window
    point lies in some ball (`witnessTable_covers` + `chainCovers_sound`), the
    ball's floor bounds `F` there (the EXTERNAL hypothesis), and the table
    minimum bounds the ball's floor (`floorConst_le_floors`). -/
theorem dh_floor_from_perBall (F : ℝ → ℝ) (hF : PerBallBounds F) :
    ∀ t : ℝ, 852/10 ≤ t → t ≤ 862/10 → (floorConst : ℝ) ≤ F t := by
  intro t ht1 ht2
  obtain ⟨b, hb, hlo, hhi⟩ :=
    chainCovers_sound witnessTable windowLo windowHi witnessTable_covers t
      (by push_cast [windowLo]; linarith) (by push_cast [windowHi]; linarith)
  calc (floorConst : ℝ) ≤ (b.floor : ℝ) := by
        exact_mod_cast floorConst_le_floors b hb
    _ ≤ F t := hF b hb t hlo hhi

/-- #e2bd-1, THE STATEMENT-LEVEL TARGET OF RECORD (LEARNINGS #199 / e2bd
    Section 5 item 2): the floor constant exists and exceeds `1/20`, uniformly
    on the window containing the off-line pair's height. The witness is the
    table minimum `3303/10000 = 0.3303` (the coarsened certified
    `c_DH = 0.33032...`). Contrast constant for the reading: on-line zeros of
    either function drive the same meter below `5·10^-4` (dossier table), so a
    floor above `1/20` is three orders of selective blindness. -/
theorem dh_floor_exceeds_one_twentieth (F : ℝ → ℝ) (hF : PerBallBounds F) :
    ∃ c : ℝ, 1/20 < c ∧ ∀ t : ℝ, 852/10 ≤ t → t ≤ 862/10 → c ≤ F t := by
  refine ⟨(floorConst : ℝ), ?_, dh_floor_from_perBall F hF⟩
  have := one_twentieth_lt_floorConst
  push_cast [floorConst]
  norm_num

end ZetaRH.DHFloorCertificate
