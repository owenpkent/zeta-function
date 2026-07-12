/-
The S4 skeleton on the CCM carrier: the five classical VERIFIER targets of e1o
(the S4/R1 arc, LEARNINGS #162).

Companion probe: `experiments/spectral/e1o_s4_carrier.md`. That probe posed
Stepanov's S4 move (cheap multiplicity buying a one-sided COUNT bound) on the
CCM prolate/PW carrier and measured the slot empty in every testable direction.
The five verification targets it flagged (`.md` Section "Verification targets")
are deliberately CLASSICAL (finite linear algebra, Chebyshev prime blocks, the
trig Vandermonde), and are formalized here in ascending difficulty order.

  #S4C-1  Prime-side inequality (the Euler gate). For nonnegative coefficients
          and a pointwise majorant `chi <= sel` with `0 <= chi`, the paired sum
          over a smaller support is dominated by the paired sum with the
          majorant over a larger support (horizon extension). Nonnegativity of
          the coefficients is the EXPLICIT, load-bearing hypothesis (the Euler
          gate; the CORRECTED / nonnegativity-explicit form per LEARNINGS #161).
          Specialization: von Mangoldt `Λ >= 0` discharges the gate for `ψ`.
          D-H control: `Λ_DH` is sign-changing, so `hw` fails and the route is
          unposable for Davenport-Heilbronn (`.md` T5a).

  #S4C-2  Tail divergence via Chebyshev blocks (KERNEL, one classical input as
          hypothesis). Against the FULL von Mangoldt comb the band-limited
          majorant pairing DIVERGES at every type: the comb density `e^u` beats
          the majorant's `(δ(u-L))^{-2}` tails. Formalized as: if the e-adic
          block masses dominate `c·e^k` (the Chebyshev lower bound `ψ(x) ≳ x`,
          taken as a hypothesis since Mathlib lacks a clean Chebyshev ψ-bound)
          and the block weights dominate `1/(A(k+1)^2)` (the majorant tail
          decay), then the block-summed series is NOT summable (its terms tend
          to `+∞`). This is T2a's ill-posedness clause: the classical skeleton
          needs a horizon device.

  #S4C-3  Structural nil (the change-of-basis atom). Over ℂ the exponential
          pair `{e^{+iθ}, e^{-iθ}}` and the real trig pair `{cos θ, sin θ}` span
          the SAME 2-dimensional space of functions (Euler). With `θ = 2πk·/L`
          this is the per-frequency statement behind claim (a): the carrier's
          function space at a fixed type is the generic trig space, so no
          carrier-native majorant beats the generic extremal.

  #S4C-4  Decimation rank-1 collapse. For nodes `u_j = u_0 + j·(L/K)` every
          function in the decimated space `V_K = span{e^{2πi K m ·/L} : m ∈ ℤ}`
          takes the SAME value at every `u_j` as at `u_0`: all K evaluation
          functionals coincide (rank 1). This is the clean Lean-sized kernel of
          T4c's control (the F_q "Frobenius" avatar; over ℤ the log-prime comb
          is incommensurate, so this collapse does not fire there).

  #S4C-5  Full price at incommensurable points. Distinct points on the circle
          give a nonsingular Vandermonde for the full trig space
          (`Matrix.det_vandermonde_ne_zero_iff`): the evaluation matrix
          `z_j^k` is nonsingular iff the `z_j` are distinct. This is the
          measured "cost ratio 1.000" of T4c: distinct nodes pay full price.

  All theorems below are sorry-free; `#print axioms` at the end must report a
  subset of `[propext, Classical.choice, Quot.sound]`.
-/

import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.NumberTheory.ArithmeticFunction.VonMangoldt
import Mathlib.LinearAlgebra.Vandermonde
import Mathlib.LinearAlgebra.Span.Basic

namespace ZetaRH.S4Carrier

open Filter
open scoped Topology

/-! ## #S4C-1: the prime-side inequality (the Euler gate) -/

/-- **Prime-side inequality (#S4C-1).** With NONNEGATIVE coefficients `w` (the
    Euler gate, stated explicitly), a pointwise majorant `chi i ≤ sel i`, and
    `0 ≤ chi i`, the paired sum over a smaller support `S` is dominated by the
    majorant-paired sum over any larger support `T ⊇ S`. The two ingredients:
    the majorant step (`chi ≤ sel`, weighted by `w ≥ 0`) and the horizon
    extension (adding nonnegative terms `w·sel ≥ 0`). This is the pairing
    `ψ(x) = ∑ Λ(n)·chi(log n) ≤ ∑_{n≤Xh} Λ(n)·S(log n)` written abstractly. -/
theorem prime_side_inequality {ι : Type*} (S T : Finset ι) (hST : S ⊆ T)
    (w chi sel : ι → ℝ) (hw : ∀ i ∈ T, 0 ≤ w i)
    (hcs : ∀ i, chi i ≤ sel i) (hchi : ∀ i, 0 ≤ chi i) :
    ∑ i ∈ S, w i * chi i ≤ ∑ i ∈ T, w i * sel i := by
  calc ∑ i ∈ S, w i * chi i
      ≤ ∑ i ∈ S, w i * sel i := by
        refine Finset.sum_le_sum ?_
        intro i hi
        exact mul_le_mul_of_nonneg_left (hcs i) (hw i (hST hi))
    _ ≤ ∑ i ∈ T, w i * sel i := by
        refine Finset.sum_le_sum_of_subset_of_nonneg hST ?_
        intro i hiT _
        exact mul_nonneg (hw i hiT) (le_trans (hchi i) (hcs i))

/-- **The Euler gate, discharged for `ψ` (#S4C-1).** The nonnegativity
    hypothesis of `prime_side_inequality` holds for the von Mangoldt weights
    (`ArithmeticFunction.vonMangoldt_nonneg`): this is exactly the "coefficient
    nonnegativity is an Euler-product face" clause. The specialization is what
    makes the pairing unconditional for the true prime comb (and inapplicable
    to the sign-changing `Λ_DH`). -/
theorem prime_side_inequality_vonMangoldt (S T : Finset ℕ) (hST : S ⊆ T)
    (chi sel : ℕ → ℝ) (hcs : ∀ i, chi i ≤ sel i) (hchi : ∀ i, 0 ≤ chi i) :
    ∑ n ∈ S, ArithmeticFunction.vonMangoldt n * chi n
      ≤ ∑ n ∈ T, ArithmeticFunction.vonMangoldt n * sel n :=
  prime_side_inequality S T hST (fun n => ArithmeticFunction.vonMangoldt n) chi sel
    (fun _ _ => ArithmeticFunction.vonMangoldt_nonneg) hcs hchi

/-! ## #S4C-2: tail divergence via Chebyshev blocks (KERNEL) -/

/-- Exponential-over-quadratic growth: `e^k / (k+1)^2 → +∞`. The engine of the
    divergence (density `e^u` beats the majorant's polynomial tail). -/
theorem tendsto_exp_div_succ_sq_atTop :
    Tendsto (fun k : ℕ => Real.exp (k : ℝ) / ((k : ℝ) + 1) ^ 2) atTop atTop := by
  have hbase : Tendsto (fun k : ℕ => Real.exp (k : ℝ) / (k : ℝ) ^ 2) atTop atTop :=
    (Real.tendsto_exp_div_pow_atTop 2).comp tendsto_natCast_atTop_atTop
  have hquarter :
      Tendsto (fun k : ℕ => (1 / 4 : ℝ) * (Real.exp (k : ℝ) / (k : ℝ) ^ 2)) atTop atTop :=
    Tendsto.const_mul_atTop (by norm_num) hbase
  refine tendsto_atTop_mono' atTop ?_ hquarter
  filter_upwards [eventually_ge_atTop 1] with k hk
  have hk1 : (1 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hkpos : (0 : ℝ) < (k : ℝ) := by linarith
  have hexp : (0 : ℝ) < Real.exp (k : ℝ) := Real.exp_pos _
  have hd1 : (0 : ℝ) < 4 * (k : ℝ) ^ 2 := by positivity
  have hd2 : (0 : ℝ) < ((k : ℝ) + 1) ^ 2 := by positivity
  have hrw : (1 / 4 : ℝ) * (Real.exp (k : ℝ) / (k : ℝ) ^ 2)
      = Real.exp (k : ℝ) / (4 * (k : ℝ) ^ 2) := by ring
  rw [hrw, div_le_div_iff₀ hd1 hd2]
  nlinarith [hexp, hk1, mul_nonneg hexp.le (mul_nonneg (by linarith : (0:ℝ) ≤ 3 * (k:ℝ) + 1)
    (by linarith : (0:ℝ) ≤ (k:ℝ) - 1))]

/-- **Tail divergence (#S4C-2, KERNEL).** Suppose the e-adic block masses of the
    comb dominate `c·e^k` (the Chebyshev lower bound `ψ ≳ x`, a classical input
    carried here as a hypothesis: Mathlib lacks a directly usable `ψ(x) ≥ c·x`)
    and the majorant tail weights dominate `1/(A(k+1)^2)`. Then the block-paired
    series `b` is NOT summable: its terms tend to `+∞`, so the naive
    band-limited majorant pairing against the full comb DIVERGES (T2a). The
    classical skeleton is ill-posed without a horizon device. -/
theorem tail_pairing_not_summable {c A : ℝ} (hc : 0 < c) (hA : 0 < A)
    {b : ℕ → ℝ} (hb : ∀ k : ℕ, c * Real.exp (k : ℝ) / (A * ((k : ℝ) + 1) ^ 2) ≤ b k) :
    ¬ Summable b := by
  have hCA : (0 : ℝ) < c / A := div_pos hc hA
  have hlow : Tendsto (fun k : ℕ => c * Real.exp (k : ℝ) / (A * ((k : ℝ) + 1) ^ 2)) atTop
      atTop := by
    have : Tendsto (fun k : ℕ => (c / A) * (Real.exp (k : ℝ) / ((k : ℝ) + 1) ^ 2)) atTop
        atTop := Tendsto.const_mul_atTop hCA tendsto_exp_div_succ_sq_atTop
    refine this.congr fun k => ?_
    rw [div_mul_div_comm]
  have hbtop : Tendsto b atTop atTop := tendsto_atTop_mono hb hlow
  intro hsum
  have h0 : Tendsto b atTop (𝓝 0) := hsum.tendsto_atTop_zero
  have hmem : Set.Iio (1 : ℝ) ∈ 𝓝 (0 : ℝ) := isOpen_Iio.mem_nhds (by norm_num)
  have e1 : ∀ᶠ n in atTop, b n < 1 :=
    h0.eventually (Filter.eventually_of_mem hmem fun _ hx => hx)
  have e2 : ∀ᶠ n in atTop, (1 : ℝ) ≤ b n := hbtop.eventually_ge_atTop 1
  obtain ⟨n, hn1, hn2⟩ := (e1.and e2).exists
  linarith

/-! ## #S4C-3: the structural nil (the change-of-basis atom) -/

open Complex in
/-- `e^{+iθ(u)}` as a function of `u`; with `θ u = 2πk u / L` this is the
    carrier's exponential basis function at frequency `k`. -/
noncomputable def expPos (θ : ℝ → ℂ) : ℝ → ℂ := fun u => Complex.exp (θ u * Complex.I)

/-- `e^{-iθ(u)}`, the negative-frequency partner. -/
noncomputable def expNeg (θ : ℝ → ℂ) : ℝ → ℂ := fun u => Complex.exp (-(θ u) * Complex.I)

/-- `cos θ(u)`. -/
noncomputable def cosPhase (θ : ℝ → ℂ) : ℝ → ℂ := fun u => Complex.cos (θ u)

/-- `sin θ(u)`. -/
noncomputable def sinPhase (θ : ℝ → ℂ) : ℝ → ℂ := fun u => Complex.sin (θ u)

/-- **Structural nil (#S4C-3).** Over ℂ the exponential pair `{e^{+iθ}, e^{-iθ}}`
    and the real trig pair `{cos θ, sin θ}` span the SAME subspace of functions
    (`ℝ → ℂ`). This is the per-frequency change-of-basis atom (Euler): with
    `θ u = 2πk u / L`, `span{e^{2πi k u/L}, e^{-2πi k u/L}} = span{cos, sin}` of
    frequency `k`, so the carrier's degree-`N` exponential space (the direct sum
    over `k ≤ N` of these, plus the constant) IS the generic degree-`N` trig
    space. No carrier-native majorant can beat the generic extremal at a fixed
    type, because the extremal problem is over the same space. -/
theorem span_exp_pair_eq_span_trig (θ : ℝ → ℂ) :
    Submodule.span ℂ ({expPos θ, expNeg θ} : Set (ℝ → ℂ))
      = Submodule.span ℂ ({cosPhase θ, sinPhase θ} : Set (ℝ → ℂ)) := by
  apply le_antisymm
  · rw [Submodule.span_le]
    intro f hf
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hf
    rw [SetLike.mem_coe]
    obtain rfl | rfl := hf
    · exact Submodule.mem_span_pair.mpr ⟨1, Complex.I, by
        funext u
        simp only [expPos, cosPhase, sinPhase, Pi.add_apply, Pi.smul_apply, smul_eq_mul,
          Complex.exp_mul_I]
        ring⟩
    · exact Submodule.mem_span_pair.mpr ⟨1, -Complex.I, by
        funext u
        simp only [expNeg, cosPhase, sinPhase, Pi.add_apply, Pi.smul_apply, smul_eq_mul,
          Complex.exp_mul_I, Complex.cos_neg, Complex.sin_neg]
        ring⟩
  · rw [Submodule.span_le]
    intro f hf
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hf
    rw [SetLike.mem_coe]
    obtain rfl | rfl := hf
    · exact Submodule.mem_span_pair.mpr ⟨1 / 2, 1 / 2, by
        funext u
        simp only [expPos, expNeg, cosPhase, Pi.add_apply, Pi.smul_apply, smul_eq_mul,
          Complex.exp_mul_I, Complex.cos_neg, Complex.sin_neg]
        ring⟩
    · exact Submodule.mem_span_pair.mpr ⟨-Complex.I / 2, Complex.I / 2, by
        funext u
        simp only [expPos, expNeg, sinPhase, Pi.add_apply, Pi.smul_apply, smul_eq_mul,
          Complex.exp_mul_I, Complex.cos_neg, Complex.sin_neg]
        linear_combination (-(Complex.sin (θ u))) * Complex.I_sq⟩

/-! ## #S4C-4: decimation rank-1 collapse -/

/-- The decimated generator `e^{2πi (K m) u / L}` (a function through the K-fold
    cover of the log-circle `ℝ/Lℤ`). `V_K = span{decGen K L m : m ∈ ℤ}`. -/
noncomputable def decGen (K : ℤ) (L : ℝ) (m : ℤ) (u : ℝ) : ℂ :=
  Complex.exp ((2 * (Real.pi : ℂ) * ((K : ℂ) * (m : ℂ)) * (u : ℂ) / (L : ℂ)) * Complex.I)

/-- **Per-generator coincidence (#S4C-4 core).** Sampling `e^{2πi(Km)u/L}` at
    `u_j = u_0 + j·(L/K)` returns its value at `u_0`: the phase advances by
    `2π m j ∈ 2πℤ`, invisible to the exponential. -/
theorem decGen_eval_eq (K : ℤ) (L : ℝ) (hK : K ≠ 0) (hL : L ≠ 0)
    (u0 : ℝ) (m j : ℤ) :
    decGen K L m (u0 + (j : ℝ) * (L / (K : ℝ))) = decGen K L m u0 := by
  have hKc : (K : ℂ) ≠ 0 := Int.cast_ne_zero.mpr hK
  have hLc : (L : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr hL
  have hexp :
      (2 * (Real.pi : ℂ) * ((K : ℂ) * (m : ℂ))
          * ((u0 + (j : ℝ) * (L / (K : ℝ)) : ℝ) : ℂ) / (L : ℂ)) * Complex.I
        = (2 * (Real.pi : ℂ) * ((K : ℂ) * (m : ℂ)) * ((u0 : ℝ) : ℂ) / (L : ℂ)) * Complex.I
          + ((m * j : ℤ) : ℂ) * (2 * (Real.pi : ℂ) * Complex.I) := by
    push_cast
    field_simp
  simp only [decGen]
  rw [hexp, Complex.exp_add, Complex.exp_int_mul_two_pi_mul_I, mul_one]

/-- **Decimation rank-1 collapse (#S4C-4).** Every function in the decimated
    space `V_K = span{decGen K L m : m ∈ ℤ}` takes the same value at every
    decimation node `u_0 + j·(L/K)` as at `u_0`. So the K evaluation
    functionals at the nodes `{u_j}` all COINCIDE: the evaluation map has rank 1.
    This is T4c's control kernel (the F_q "Frobenius" of the K-fold cover); over
    ℤ the log-prime comb is Q-linearly independent, so no such AP structure
    exists and the collapse does not fire (cost ratio 1.000, #S4C-5). -/
theorem decimation_rank_one (K : ℤ) (L : ℝ) (hK : K ≠ 0) (hL : L ≠ 0)
    (u0 : ℝ) (j : ℤ) {f : ℝ → ℂ}
    (hf : f ∈ Submodule.span ℂ (Set.range (decGen K L))) :
    f (u0 + (j : ℝ) * (L / (K : ℝ))) = f u0 := by
  refine Submodule.span_induction
    (p := fun g _ => g (u0 + (j : ℝ) * (L / (K : ℝ))) = g u0) ?_ ?_ ?_ ?_ hf
  · rintro g ⟨m, rfl⟩
    exact decGen_eval_eq K L hK hL u0 m j
  · rfl
  · intro a b _ _ ha hb
    simp only [Pi.add_apply]
    rw [ha, hb]
  · intro c a _ ha
    simp only [Pi.smul_apply]
    rw [ha]

/-! ## #S4C-5: full price at incommensurable points (the trig Vandermonde) -/

/-- **Full price at distinct nodes (#S4C-5).** If the images `z_j = e^{2πi u_j/L}`
    of the nodes are DISTINCT points on the circle (`z` injective), then the
    evaluation matrix `z_j ^ k` (the trig / exponential Vandermonde) is
    nonsingular. So distinct incommensurable points pay FULL PRICE for
    interpolation: no rank collapse (the measured "cost ratio 1.000" of T4c).
    Direct consequence of `Matrix.det_vandermonde_ne_zero_iff`. -/
theorem trig_vandermonde_nonsingular {n : ℕ} (z : Fin n → ℂ) (hz : Function.Injective z) :
    (Matrix.vandermonde z).det ≠ 0 :=
  Matrix.det_vandermonde_ne_zero_iff.mpr hz

/-- The trig-Vandermonde entries are the frequency-`k` evaluations
    `e^{2πi k u_j / L} = z_j ^ k` (`Matrix.vandermonde_apply`), tying the
    abstract nonsingularity to the carrier's exponential basis at distinct
    nodes on the circle. -/
theorem vandermonde_entry_eq_freq (L : ℝ) (u : ℝ) (k : ℕ) :
    (Complex.exp (2 * (Real.pi : ℂ) * (u : ℂ) / (L : ℂ) * Complex.I)) ^ k
      = Complex.exp (2 * (Real.pi : ℂ) * (k : ℂ) * (u : ℂ) / (L : ℂ) * Complex.I) := by
  rw [← Complex.exp_nat_mul]
  ring_nf

-- Axiom audit: every theorem above must report a subset of
-- [propext, Classical.choice, Quot.sound].
#print axioms prime_side_inequality
#print axioms prime_side_inequality_vonMangoldt
#print axioms tendsto_exp_div_succ_sq_atTop
#print axioms tail_pairing_not_summable
#print axioms span_exp_pair_eq_span_trig
#print axioms decGen_eval_eq
#print axioms decimation_rank_one
#print axioms trig_vandermonde_nonsingular
#print axioms vandermonde_entry_eq_freq

end ZetaRH.S4Carrier
