/-
2M (the Arakelov-side M4 construction attempt): the two isolable, RH-INDEPENDENT
targets VT1 and VT2 that Front 3 (`e2af_adelic_assembly.py`) isolated.

See `experiments/arithmetic_geometric/2M_arakelov_construction_attempt.md` (LEARNINGS
#132). The 2M attempt walled at the already-named gap (R1 + M4 + PROP-global). What it
isolated, and the dossier flagged for Lean, are two facts that are theorems on their own,
K1-clean (only Frobenius point counts enter, never zeta's zeros) and disconnected from the
open kernel:

  VT1 (per-prime Hasse sign). The per-prime `(1,p)`-bidegree primitive Gram
       `G_p = !![ -2g, -t ; -t, -2g·p ]` is negative definite  ⟺  `t² < 4g²p`.
       This is EXACTLY `HodgeIndex.IntersectionSignature.negDef_iff_hasseWeil` at `q = p`.
       Honest flag (per the e2ad caution): VT1 is a SPECIALIZATION of an existing theorem,
       not new content. It is recorded here as the per-prime statement, and as the fact that
       under per-prime Hasse EVERY per-prime form is definite.

  VT2 (no single scale assembles the per-prime forms). The genuinely new content. The
       per-prime forms are each definite (VT1), yet there is NO single positive scaling of
       the second coordinate that puts them all in a common normalization. The
       diagonal-equalizing scale for prime `p` solves `p·s² = 1` (`s = 1/√p`), which is
       irreducibly p-dependent; and for any FIXED scale `s` the forced diagonal asymmetry
       `p·s²` is unbounded over `p`. This is the #25 place-dependent `(1,p)`-bidegree
       obstruction, exhibited as an intersection-pairing ASSEMBLY failure (the lift of
       e2ad's per-prime computation from a moment matrix to the signed pairing).

This file does NOT close M4. Proving the SIGN of the single regularized adelic scalar into
which the per-prime couplings relocate is M4, open. These are only the isolable residues,
machine-checked sorry-free.

D-H discipline: every `t = t_p` here is a Frobenius point-count trace `t_p = p + 1 - #X(𝔽_p)`,
which Davenport-Heilbronn lacks (no Euler product ⟹ no `Frob_p` ⟹ no per-prime form). So
none of this is buildable for D-H (survival by non-mimicry); no positivity asserted here
would "work" for D-H.
-/

import ZetaRH.HodgeIndex
import Mathlib.Tactic

namespace ZetaRH.ArakelovAssembly

open ZetaRH.HodgeIndex.IntersectionSignature

/-! ## VT1: the per-prime `(1,p)`-bidegree form is definite iff per-prime Hasse

    A SPECIALIZATION of the 2G keystone `negDef_iff_hasseWeil` at `q = p`. Recorded for the
    assembly statement; not new content. -/

/-- **VT1 (VERIFIER target #2M-VT1): per-prime Hasse sign.** The per-prime primitive Gram
    `G_p = !![ -2g, -t ; -t, -2g·p ]` is negative definite iff `t² < 4g²p`. This is the
    function-field Hodge-index keystone `negDef_iff_hasseWeil` evaluated at `q = p`. -/
theorem perPrime_negDef_iff_hasse {g p t : ℝ} (hg : 0 < g) :
    NegDef g p t ↔ t ^ 2 < 4 * g ^ 2 * p :=
  negDef_iff_hasseWeil hg

/-- Under per-prime Hasse (`t² < 4g²p`, the bound `|t_p| < 2g√p` that holds for the
    Frobenius trace of a curve at a good prime), the per-prime form is negative definite. So
    EVERY per-prime form is definite; the assembly failure (VT2) is not a failure of any
    single fibre. -/
theorem perPrime_negDef_of_hasse {g p t : ℝ} (hg : 0 < g) (hHasse : t ^ 2 < 4 * g ^ 2 * p) :
    NegDef g p t :=
  negDef_of_hasseWeil hg hHasse

/-! ## VT2: no single scale assembles the per-prime forms (the new content) -/

/-- Diagonal scaling of the second coordinate by `s`: `D_s = diag(1, s)`. Conjugating the
    per-prime form by `D_s` is the only freedom in renormalizing the `(1,p)` bidegree toward
    a common scale. -/
def Dscale (s : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := !![1, 0; 0, s]

/-- The lower-right entry of the `D_s`-conjugated per-prime form is `-2g·p·s²`. (Conjugating
    by a diagonal matrix scales entry `(i,j)` by `D_ii · D_jj`; the upper-left entry stays
    `-2g`.) So equalizing the two diagonal entries to the uniform `-2g` requires `p·s² = 1`,
    which grounds `NormalizesDiag` below. -/
theorem conj_lowerRight (g p t s : ℝ) :
    (Dscale s * Gprim g p t * Dscale s) 1 1 = -2 * g * p * s ^ 2 := by
  simp [Dscale, Gprim, Matrix.mul_apply, Fin.sum_univ_two]
  ring

/-- The diagonal-equalizing condition for prime `p` at scale `s`: by `conj_lowerRight` the
    conjugated lower-right entry is `-2g·p·s²` and the upper-left is `-2g`, so the two
    diagonal entries agree exactly when `p·s² = 1` (i.e. `s = 1/√p`). -/
def NormalizesDiag (p s : ℝ) : Prop := p * s ^ 2 = 1

/-- **VT2a (VERIFIER target #2M-VT2, no single scale).** For two DISTINCT primes (or any
    distinct positive reals) `p ≠ q`, there is NO single scale `s` normalizing both
    per-prime forms' diagonals: `p·s² = 1` and `q·s² = 1` force `p = q`. The per-prime
    equalizing scale `s = 1/√p` is irreducibly p-dependent. This is the #25 place-dependent
    `(1,p)`-bidegree obstruction, as an assembly failure. -/
theorem no_single_normalizing_scale {p q : ℝ} (hpq : p ≠ q) :
    ¬ ∃ s : ℝ, NormalizesDiag p s ∧ NormalizesDiag q s := by
  rintro ⟨s, hp, hq⟩
  unfold NormalizesDiag at hp hq
  have hs2 : s ^ 2 ≠ 0 := by
    intro h; rw [h, mul_zero] at hp; exact zero_ne_one hp
  exact hpq (mul_right_cancel₀ hs2 (hp.trans hq.symm))

/-- **VT2b (forced-single-scale asymmetry is unbounded).** For ANY fixed scale `s > 0`, the
    forced diagonal asymmetry `n·s²` of the `D_s`-normalized form is unbounded over `n`: for
    every bound `M` there is an `n` with `n·s² > M`. So no single scale even keeps the
    per-prime family bounded, let alone uniform. -/
theorem forced_scale_asymmetry_unbounded {s : ℝ} (hs : 0 < s) (M : ℝ) :
    ∃ n : ℕ, M < (n : ℝ) * s ^ 2 := by
  have hs2 : 0 < s ^ 2 := by positivity
  have hne : s ^ 2 ≠ 0 := ne_of_gt hs2
  obtain ⟨n, hn⟩ := exists_nat_gt (M / s ^ 2)
  have key := mul_lt_mul_of_pos_right hn hs2
  have heq : M / s ^ 2 * s ^ 2 = M := by field_simp
  exact ⟨n, by rw [heq] at key; exact key⟩

/-- **The e2af assembly no-go (combined VT1 + VT2a).** Given two distinct good primes with
    per-prime Hasse-valid traces, BOTH per-prime forms are negative definite (each a genuine
    `(1,1)`-signature polarization, VT1), yet NO single scale normalizes both diagonals
    (VT2a). So the per-prime polarizations do not assemble into one common-scale form: the
    `(1,p)` bidegree obstructs the assembly. The remaining content (the SIGN of the single
    regularized adelic scalar into which the per-prime couplings relocate) is M4, open. -/
theorem assembly_obstruction {g p q tp tq : ℝ} (hg : 0 < g) (hpq : p ≠ q)
    (hHp : tp ^ 2 < 4 * g ^ 2 * p) (hHq : tq ^ 2 < 4 * g ^ 2 * q) :
    NegDef g p tp ∧ NegDef g q tq ∧
      ¬ ∃ s : ℝ, NormalizesDiag p s ∧ NormalizesDiag q s :=
  ⟨perPrime_negDef_of_hasse hg hHp, perPrime_negDef_of_hasse hg hHq,
    no_single_normalizing_scale hpq⟩

end ZetaRH.ArakelovAssembly
