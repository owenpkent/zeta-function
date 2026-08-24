/-
C4: the missing-object interface as a Lean structure (backlog C4; LEARNINGS #197).

`docs/03_research/missing_object_interface.md` types the missing object as ONE interface
with five components (SP1 carrier / SP2 endomorphism / SP3 base+diagonal / SP4 trace
formula / SP5 polarization). This file makes that a first-class term at the genus-1 /
rank-2 register, where every clause is exactly formalizable against the existing lever-B
chain (`FunctionFieldRH`, `IsogenyDegree`, `ToyModel`):

  SP1  the carrier lattice: divisor/integer counts `b : ℕ → ℤ`, `b 0 = 1`;
  SP2  the endomorphism: an ACTUAL rank-2 integer operator `A` (Frobenius on the Tate
       module) with `det A = q`;
  SP3  the base's diagonal: fixed-point counts `N n = q^n + 1 - trace (A^n)` (the
       Lefschetz shape: H⁰ + H² − H¹);
  SP4  the two-sided trace formula, coefficient-wise at genus 1: the lattice counts are
       the coefficients of `P_A(T)/((1-T)(1-qT))` (fields `sp4_b1`, `sp4_b2`, `sp4_rec`);
  SP5  the polarization: nonnegative degree on the endomorphism lattice
       (`det(m·1 + n·A) ≥ 0`): the Hodge-index / Castelnuovo source.

THE PAYOFF, machine-checked: `SPInterface.rh`: every instance of the full interface
satisfies its Riemann Hypothesis (`|α|² = q` for every Frobenius eigenvalue). The
e2b/e2ay curve (`y² = x³ + x + 1` over `𝔽₅`) inhabits the interface SORRY-FREE
(`curveF5`), with the e2ay-measured column as witness theorems (counts 9, 27, 108, 675;
divisor counts 9, 54, 279; the place-count Euler anchor at n = 4).

THE FOUR-OF-FIVE AND THE TYPED REFUSALS (the satisfiability matrix, machine-checked):
  - `SPInterfaceSans5` is the interface minus SP5 (the four-of-five shape of the finite
    zeta-side object v0); `sans5_sp5_iff_hasse` proves the missing fifth field is
    EQUIVALENT to the Hasse bound: at this register, supplying SP5 IS the RH content
    (M4's genus-1 shadow as an iff). At Spec(Z) even SP2's field is open (R1: no
    integer Frobenius operator is known for zeta), so the zeta column is represented
    honestly by `Sans5` + this iff, not by a fake instance.
  - Davenport-Heilbronn: `dh_no_euler_point` / `dh_euler_defect`: the real FE-pencil
    `[1, κ, −κ, −1, 0]` has NO Euler member: multiplicativity at (2,3)·= 6 demands
    `κ² = −1`, and the defect is ≤ −1 for every real κ (LEARNINGS #196's closed form
    `b₆(κ) = (κ²+1)·log 6`, integer face). The SP3/Euler field is uninhabitable for the
    class: the refusal as a theorem.
  - Beurling/jitter: `beurling_refusal`: the interface QUANTIZES lattice counts
    (`b_determined`: `b` is forced to `(q+1−t)·(1 + q + … + q^{n−1})`), so a jittered
    count (`b 2 = 55` at `q = 5`) admits NO instance: the lattice clause as a type
    error, exactly the backlog's wording.

Everything here is sorry-free; the single open input of the register is unchanged and
lives upstream (`FunctionFieldRH.FrobeniusMatrixExists`: that a real curve SUPPLIES the
SP2 matrix, the O1 residual). The interface adds no new axioms: it packages the proven
chain so that "the missing object" is a term whose Spec(Z) inhabitation is the problem.
-/

import ZetaRH.FunctionFieldRH
import ZetaRH.ToyModel

namespace ZetaRH

open ZetaRH.IsogenyDegree ZetaRH.FunctionFieldRH

/-- The five-component missing-object interface at the genus-1 / rank-2 register.
    See the file header for the SP1-SP5 reading of each field. -/
structure SPInterface where
  /-- The field size (the base's cardinality datum). -/
  q : ℕ
  q_pos : 0 < q
  /-- SP1: the carrier lattice: counts by degree. -/
  b : ℕ → ℤ
  b_zero : b 0 = 1
  /-- SP2: the endomorphism, an actual rank-2 integer operator. -/
  A : Matrix (Fin 2) (Fin 2) ℤ
  det_eq : A.det = (q : ℤ)
  /-- SP3: the diagonal's fixed-point counts (Lefschetz shape). -/
  N : ℕ → ℤ
  sp3_diagonal : ∀ n : ℕ, N n = (q : ℤ) ^ n + 1 - (A ^ n).trace
  /-- SP4 (initial coefficient): `b 1 = q + 1 − t = N 1`. -/
  sp4_b1 : b 1 = (q : ℤ) + 1 - A.trace
  /-- SP4 (second coefficient): `b 2 = (q+1)(q+1−t)`. -/
  sp4_b2 : b 2 = ((q : ℤ) + 1) * ((q : ℤ) + 1 - A.trace)
  /-- SP4 (the rational-function recursion): `b` has generating function
      `P_A(T)/((1−T)(1−qT))`: the genus-1 trace formula, coefficient-wise. -/
  sp4_rec : ∀ n : ℕ, b (n + 3) = (1 + (q : ℤ)) * b (n + 2) - (q : ℤ) * b (n + 1)
  /-- SP5: the polarization: nonnegative degree on the endomorphism lattice. -/
  sp5_polarization :
    ∀ m n : ℤ, 0 ≤ (m • (1 : Matrix (Fin 2) (Fin 2) ℤ) + n • A).det

namespace SPInterface

/-- **The interface implies the Hasse bound** (via the SP5 field and Phase A's
    `hasse_of_matrix`). -/
theorem hasse (X : SPInterface) : (X.A.trace : ℝ) ^ 2 ≤ 4 * (X.q : ℝ) := by
  have h := hasse_of_matrix X.A X.sp5_polarization
  rw [X.det_eq] at h
  exact_mod_cast h

/-- **THE PAYOFF: every inhabitant of the interface satisfies its Riemann Hypothesis.**
    Every Frobenius eigenvalue (the complex spectrum of SP2's operator) lies on the
    circle `|α|² = q`. Machine-checked consequence of the five fields; the proof is the
    lever-B chain applied to SP5. -/
theorem rh (X : SPInterface) {α : ℂ}
    (hα : α ∈ spectrum ℂ (X.A.map (Int.castRingHom ℂ))) :
    Complex.normSq α = (X.q : ℝ) := by
  have h := functionfield_RH_elliptic_of_matrix_general X.sp5_polarization hα
  rw [X.det_eq] at h
  exact_mod_cast h

/-- **The lattice is quantized by the trace formula**: SP4 forces
    `b (n+1) = (q + 1 − t) · (1 + q + ⋯ + qⁿ)`. This is the rigidity the Beurling
    refusal below consumes: an interface instance has NO freedom in its counts. -/
theorem b_determined (X : SPInterface) :
    ∀ n : ℕ, X.b (n + 1)
      = ((X.q : ℤ) + 1 - X.A.trace) * ∑ i ∈ Finset.range (n + 1), (X.q : ℤ) ^ i
  | 0 => by simpa using X.sp4_b1
  | 1 => by
      have h := X.sp4_b2
      rw [h]
      simp [Finset.sum_range_succ]
      ring
  | (n + 2) => by
      have ih1 := b_determined X (n + 1)
      have ih0 := b_determined X n
      have hrec := X.sp4_rec n
      rw [hrec, ih1, ih0]
      have hs2 : (∑ i ∈ Finset.range (n + 3), (X.q : ℤ) ^ i)
          = (∑ i ∈ Finset.range (n + 2), (X.q : ℤ) ^ i) + (X.q : ℤ) ^ (n + 2) :=
        Finset.sum_range_succ _ _
      have hs1 : (∑ i ∈ Finset.range (n + 2), (X.q : ℤ) ^ i)
          = (∑ i ∈ Finset.range (n + 1), (X.q : ℤ) ^ i) + (X.q : ℤ) ^ (n + 1) :=
        Finset.sum_range_succ _ _
      rw [hs2, hs1]
      ring

end SPInterface

/-! ## The four-of-five: the interface minus the polarization, and what the missing
    field is worth. `SPInterfaceSans5` is the shape of the finite zeta-side object
    (e2an's v0 inhabits SP1-SP4 at finite scale with SP5 empirically marginal); at this
    register the missing field is EXACTLY the Hasse/RH content. -/

/-- The interface without SP5: the four-of-five shape. -/
structure SPInterfaceSans5 where
  q : ℕ
  q_pos : 0 < q
  b : ℕ → ℤ
  b_zero : b 0 = 1
  A : Matrix (Fin 2) (Fin 2) ℤ
  det_eq : A.det = (q : ℤ)
  N : ℕ → ℤ
  sp3_diagonal : ∀ n : ℕ, N n = (q : ℤ) ^ n + 1 - (A ^ n).trace
  sp4_b1 : b 1 = (q : ℤ) + 1 - A.trace
  sp4_b2 : b 2 = ((q : ℤ) + 1) * ((q : ℤ) + 1 - A.trace)
  sp4_rec : ∀ n : ℕ, b (n + 3) = (1 + (q : ℤ)) * b (n + 2) - (q : ℤ) * b (n + 1)

/-- Forgetting the polarization. -/
def SPInterface.toSans5 (X : SPInterface) : SPInterfaceSans5 :=
  { X with }

/-- **The missing fifth field IS the Hasse content (M4's genus-1 shadow, as an iff).**
    For a four-of-five datum, supplying the SP5 field is EQUIVALENT to the Hasse bound
    `t² ≤ 4q`. Forward: Phase A (`hasse_of_matrix`). Backward: the degree form
    `det(m·1 + n·A) = m² + t·m·n + q·n²` (Cayley-Hamilton at rank 2) and the completed
    square `4·(m² + tmn + qn²) = (2m + tn)² + (4q − t²)n²`. -/
theorem sans5_sp5_iff_hasse (Y : SPInterfaceSans5) :
    (∀ m n : ℤ, 0 ≤ (m • (1 : Matrix (Fin 2) (Fin 2) ℤ) + n • Y.A).det)
      ↔ (Y.A.trace : ℝ) ^ 2 ≤ 4 * (Y.q : ℝ) := by
  constructor
  · intro hpos
    have h := hasse_of_matrix Y.A hpos
    rw [Y.det_eq] at h
    exact_mod_cast h
  · intro hHasse m n
    rw [det_smul_one_add_smul, Y.det_eq]
    have ht : (Y.A.trace : ℝ) ^ 2 ≤ 4 * (Y.q : ℝ) := hHasse
    have hreal : (0 : ℝ) ≤ (m : ℝ) ^ 2 + (Y.A.trace : ℝ) * m * n + (Y.q : ℝ) * n ^ 2 := by
      nlinarith [sq_nonneg (2 * (m : ℝ) + (Y.A.trace : ℝ) * n), sq_nonneg (n : ℝ),
        mul_nonneg (by linarith : (0 : ℝ) ≤ 4 * (Y.q : ℝ) - (Y.A.trace : ℝ) ^ 2)
          (sq_nonneg (n : ℝ))]
    exact_mod_cast hreal

/-- Completing a four-of-five datum to the full interface from the Hasse bound: the
    constructive face of the iff. -/
def SPInterfaceSans5.complete (Y : SPInterfaceSans5)
    (hHasse : (Y.A.trace : ℝ) ^ 2 ≤ 4 * (Y.q : ℝ)) : SPInterface :=
  { Y with sp5_polarization := (sans5_sp5_iff_hasse Y).mpr hHasse }

/-! ## The function-field instance: the e2b/e2ay curve over 𝔽₅, sorry-free.
    `y² = x³ + x + 1` over `𝔽₅`: `N₁ = 9`, trace `t = −3`, class number `h = 9`;
    divisor counts `b n = 9·(1 + 5 + ⋯ + 5^{n−1})`; SP2's operator is the companion
    matrix of `X² + 3X + 5` (the Frobenius on the Tate module in the canonical basis). -/

/-- The divisor-count sequence of the curve: `b 0 = 1`, `b n = 9·∑_{i<n} 5^i`. -/
def curveF5_b (n : ℕ) : ℤ :=
  if n = 0 then 1 else 9 * ∑ i ∈ Finset.range n, (5 : ℤ) ^ i

/-- **The 𝔽₅ curve inhabits the interface, sorry-free.** -/
def curveF5 : SPInterface where
  q := 5
  q_pos := by norm_num
  b := curveF5_b
  b_zero := rfl
  A := companion (-3) 5
  det_eq := by simp
  N := fun n => 5 ^ n + 1 - ((companion (-3) 5) ^ n).trace
  sp3_diagonal := fun n => by norm_num
  sp4_b1 := by simp [curveF5_b]
  sp4_b2 := by
    norm_num [curveF5_b, Finset.sum_range_succ]
  sp4_rec := fun n => by
    simp only [curveF5_b, if_neg (Nat.succ_ne_zero _)]
    rw [Finset.sum_range_succ (n := n + 2), Finset.sum_range_succ (n := n + 1)]
    push_cast
    ring
  sp5_polarization := companion_degForm_nonneg (by norm_num)

/-- **RH for the instance, via the interface**: every Frobenius eigenvalue of the 𝔽₅
    curve datum has `|α|² = 5`. -/
theorem curveF5_rh {α : ℂ}
    (hα : α ∈ spectrum ℂ (curveF5.A.map (Int.castRingHom ℂ))) :
    Complex.normSq α = 5 := by
  have h := curveF5.rh hα
  norm_num [curveF5] at h
  exact h

/-! ### The e2ay column as witness theorems (the measured cells, machine-checked). -/

/-- The point counts through degree 4: `9, 27, 108, 675` (e2ay's direct-count anchor). -/
theorem curveF5_counts :
    curveF5.N 1 = 9 ∧ curveF5.N 2 = 27 ∧ curveF5.N 3 = 108 ∧ curveF5.N 4 = 675 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    norm_num [curveF5, companion, pow_succ, Matrix.trace_fin_two, Matrix.mul_fin_two]

/-- The divisor counts through degree 3: `9, 54, 279` (e2ay's lattice anchor). -/
theorem curveF5_divisor_counts :
    curveF5.b 1 = 9 ∧ curveF5.b 2 = 54 ∧ curveF5.b 3 = 279 := by
  refine ⟨?_, ?_, ?_⟩ <;> norm_num [curveF5, curveF5_b, Finset.sum_range_succ]

/-- The Euler/place anchor at degree 4: `N 4 = 1·a₁ + 2·a₂ + 4·a₄` with the e2ay place
    counts `a₁ = 9, a₂ = 9, a₄ = 162` (all nonnegative: the free-semigroup face). -/
theorem curveF5_places_degree4 :
    curveF5.N 4 = 1 * 9 + 2 * 9 + 4 * 162 ∧ (0 : ℤ) ≤ 9 ∧ (0 : ℤ) ≤ 162 := by
  refine ⟨?_, by norm_num, by norm_num⟩
  norm_num [curveF5, companion, pow_succ, Matrix.trace_fin_two, Matrix.mul_fin_two]

/-! ## The typed refusals: which field each control cannot fill. -/

/-- The Davenport-Heilbronn real pencil's coefficient pattern `[1, κ, −κ, −1, 0]`
    (5-periodic, `n ≥ 1`). -/
def dhPat (κ : ℝ) (n : ℕ) : ℝ :=
  match n % 5 with
  | 1 => 1
  | 2 => κ
  | 3 => -κ
  | 4 => -1
  | _ => 0

/-- **The D-H refusal (SP3/Euler field uninhabitable): the real pencil has no Euler
    point.** Multiplicativity at the first composite, `a 2 · a 3 = a 6`, demands
    `κ² = −1`: impossible for real `κ`. (LEARNINGS #196: the Euler points sit at
    `κ = ±i`, off the real pencil: why D-H exists.) -/
theorem dh_no_euler_point (κ : ℝ) : dhPat κ 2 * dhPat κ 3 ≠ dhPat κ 6 := by
  show κ * (-κ) ≠ 1
  intro h
  nlinarith [sq_nonneg κ]

/-- **The D-H refusal, quantified**: the multiplicativity defect at `(2, 3)` is at most
    `−1` for EVERY real pencil member: `a₂a₃ − a₆ = −(κ² + 1) ≤ −1`. (The analytic face
    is e2an's measured Euler leak `b₆ = (κ² + 1)·log 6 = 1.936` at the D-H point.) -/
theorem dh_euler_defect (κ : ℝ) : dhPat κ 2 * dhPat κ 3 - dhPat κ 6 ≤ -1 := by
  show κ * (-κ) - 1 ≤ -1
  nlinarith [sq_nonneg κ]

/-- **The Beurling/jitter refusal (the lattice clause as a type error).** The interface
    quantizes counts (`b_determined`), so a jittered divisor count (`b 2 = 55` over
    `q = 5`; the true value is `54`) admits NO instance: `b 2 = 6·(6 − t)` is divisible
    by 6, and 55 is not. -/
theorem beurling_refusal : ¬ ∃ X : SPInterface, X.q = 5 ∧ X.b 2 = 55 := by
  rintro ⟨X, hq, hb⟩
  have h2 := X.sp4_b2
  rw [hq] at h2
  rw [hb] at h2
  omega

end ZetaRH
