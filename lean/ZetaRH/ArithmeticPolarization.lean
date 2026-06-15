/-
M4: the arithmetic polarization face of RH (the Spec(ℤ) lift of the function-field eigenvalue
extraction).

See `docs/03_research/research_directions/08A_rosati_standard_conjecture.md` (the M1-M5 ladder) and
`docs/03_research/all_roads_to_the_signature.md`. The program's one target is **M4**: RH for ζ is the
positivity of an arithmetic Rosati / cup polarization on the Frobenius algebra of Spec(ℤ) -- the
arithmetic Hodge standard conjecture. The function-field rehearsal is in `FunctionFieldRH.lean` /
`TateModule.lean`: there the Weil pairing's positivity (`deg ≥ 0`) forces the Frobenius eigenvalues
onto the circle `|α|² = q` (`eigenvalue_modulus`). This file states the ARITHMETIC analogue at the
level of the zeros, and isolates exactly which half is free and which half is M4.

The structure is the same "a conjugate/dual pairing coincides" mechanism:

  * function field:  the two roots of `X² − tX + q` are `α` and `conj α` (Vieta), and the polarization
                     `deg ≥ 0` forces `α·conj α = q`, i.e. `|α| = √q` -- zeros on the CIRCLE.
  * arithmetic:      the functional equation pairs a nontrivial zero `ρ` with `1 − ρ` (a genuine zero,
                     `fe_partner_mem_nonTrivialZeros`), and RH is the condition that this FE-partner is
                     the CONJUGATE, `1 − ρ = conj ρ`, i.e. `Re ρ = 1/2` -- zeros on the LINE.

So the cup pairing's PERFECTNESS is free (the functional equation, proved here as
`fe_partner_mem_nonTrivialZeros`, and it holds even for Davenport-Heilbronn), while its POSITIVITY --
that the FE pairing IS conjugation -- is exactly RH. This is the #61/2HH decomposition
("perfectness is free, positivity is the entire gap, and it is the arithmetic Hodge standard
conjecture") made machine-checked at the zero level. The deep content -- WHY a polarization forces
`1 − ρ = conj ρ` -- is M4 itself and is not in this file.

Reflection (now proved): `conj ρ` is also a zero, because ζ has real Dirichlet coefficients, giving
`ζ(s̄) = conj ζ(s)` (`riemannZeta_conj`, proved here from the L-series on `Re s > 1` plus the identity
principle, since Mathlib carries the functional equation but not this reflection). So both `1 − ρ` and
`conj ρ` are genuine nontrivial zeros (`fe_partner_mem_nonTrivialZeros`,
`reflection_mem_nonTrivialZeros`), and the polarization condition `1 − ρ = conj ρ` is literally "the
FE-partner zero and the conjugate zero coincide".
-/

import ZetaRH.Basic
import ZetaRH.RiemannZetaConj
import Mathlib.NumberTheory.LSeries.RiemannZeta

namespace ZetaRH.ArithmeticPolarization

open Complex

/-- **The critical line is the FE-duality polarization condition.** A point `ρ` has real part `1/2`
    iff its functional-equation partner `1 − ρ` equals its conjugate `conj ρ`. (The imaginary parts of
    `1 − ρ` and `conj ρ` always agree, `= −ρ.im`; equality of the real parts is `1 − ρ.re = ρ.re`,
    i.e. `Re ρ = 1/2`.) This is the arithmetic analogue of the function-field
    `eigenvalue_modulus` conclusion: a conjugate pairing pinned to the symmetry locus. -/
theorem critical_line_iff_fe_reflection (ρ : ℂ) :
    1 - ρ = (starRingEnd ℂ) ρ ↔ ρ.re = 1 / 2 := by
  constructor
  · intro h
    have hre : (1 - ρ).re = ((starRingEnd ℂ) ρ).re := by rw [h]
    simp only [Complex.sub_re, Complex.one_re, Complex.conj_re] at hre
    linarith
  · intro h
    apply Complex.ext
    · simp only [Complex.sub_re, Complex.one_re, Complex.conj_re]; linarith
    · simp only [Complex.sub_im, Complex.one_im, Complex.conj_im]; ring

/-- **The functional equation provides the perfect pairing `ρ ↔ 1 − ρ` (free, K2-blind).** If `ρ` is a
    nontrivial zero of ζ, so is `1 − ρ`. This is the "perfectness" of the FE-duality cup product: the
    pairing of zeros is genuine, with no positivity input. Proof: Mathlib's functional equation
    `riemannZeta_one_sub` writes `ζ(1 − ρ) = (factor)·ζ(ρ)`, which vanishes since `ζ(ρ) = 0`; and
    `1 − ρ` stays in the critical strip (`Re(1 − ρ) = 1 − Re ρ ∈ (0,1)`). The hypotheses of the FE
    (`ρ ∉ −ℕ`, `ρ ≠ 1`) hold because `0 < Re ρ < 1`. -/
theorem fe_partner_mem_nonTrivialZeros {ρ : ℂ} (hρ : ρ ∈ nonTrivialZeros zeta) :
    (1 - ρ) ∈ nonTrivialZeros zeta := by
  obtain ⟨hzero, hpos, hlt, _⟩ := hρ
  have hz : riemannZeta ρ = 0 := hzero
  have hsn : ∀ n : ℕ, ρ ≠ -(n : ℂ) := by
    intro n h
    rw [h, Complex.neg_re, Complex.natCast_re] at hpos
    linarith [(Nat.cast_nonneg n : (0 : ℝ) ≤ (n : ℝ))]
  have hs1 : ρ ≠ 1 := by
    intro h; rw [h, Complex.one_re] at hlt; exact lt_irrefl 1 hlt
  have hfe : riemannZeta (1 - ρ) = 0 := by
    rw [riemannZeta_one_sub hsn hs1, hz, mul_zero]
  refine ⟨hfe, ?_, ?_, ?_⟩
  · rw [Complex.sub_re, Complex.one_re]; linarith
  · rw [Complex.sub_re, Complex.one_re]; linarith
  · intro hmem
    have h1 : (1 - ρ) = 1 := hmem
    have hre : (1 - ρ).re = (1 : ℂ).re := congrArg Complex.re h1
    rw [Complex.sub_re, Complex.one_re] at hre
    linarith

/-! ### Reflection `ζ(s̄) = conj ζ(s)`

    The reflection symmetry `riemannZeta_conj` (`ζ(s̄) = conj ζ(s)` for `s ≠ 1`) lives in its own
    Mathlib-style, dependency-free unit [`RiemannZetaConj.lean`](RiemannZetaConj.lean) (staged for
    upstreaming; Mathlib has the functional equation but not this reflection). Here we only use it to
    show the conjugate of a nontrivial zero is a nontrivial zero. -/

/-- **Reflection provides the other pairing `ρ ↔ conj ρ` (free).** If `ρ` is a nontrivial zero of ζ,
    so is its conjugate `conj ρ` (via `riemannZeta_conj`: `ζ(conj ρ) = conj(ζ ρ) = 0`). Together with
    `fe_partner_mem_nonTrivialZeros` this makes the polarization condition `1 − ρ = conj ρ` literally
    "two genuine zeros (the FE-partner and the conjugate) coincide". -/
theorem reflection_mem_nonTrivialZeros {ρ : ℂ} (hρ : ρ ∈ nonTrivialZeros zeta) :
    (starRingEnd ℂ) ρ ∈ nonTrivialZeros zeta := by
  obtain ⟨hzero, hpos, hlt, _⟩ := hρ
  have hρ1 : ρ ≠ 1 := by intro h; rw [h, Complex.one_re] at hlt; exact lt_irrefl 1 hlt
  have hz : riemannZeta ρ = 0 := hzero
  have hconj : riemannZeta ((starRingEnd ℂ) ρ) = 0 := by
    rw [riemannZeta_conj hρ1, hz, map_zero]
  refine ⟨hconj, ?_, ?_, ?_⟩
  · rw [Complex.conj_re]; exact hpos
  · rw [Complex.conj_re]; exact hlt
  · intro hmem
    have h1 : (starRingEnd ℂ) ρ = 1 := hmem
    have hre : ((starRingEnd ℂ) ρ).re = (1 : ℂ).re := congrArg Complex.re h1
    rw [Complex.conj_re, Complex.one_re] at hre
    linarith

/-- **RH for ζ is the FE-duality polarization condition (M4 face, the Spec(ℤ) lift of
    `eigenvalue_modulus`).** RH holds iff every nontrivial zero `ρ` satisfies `1 − ρ = conj ρ` -- i.e.
    the functional-equation pairing (perfect and free, `fe_partner_mem_nonTrivialZeros`) coincides
    with conjugation. This is the zero-level recasting of "the FE-duality cup product is a
    polarization iff Re = 1/2" (#61/2HH): perfectness is the functional equation, positivity is this
    coincidence, and positivity is the entire gap = the arithmetic Hodge standard conjecture (M4).
    Proved sorry-free as an equivalence; the deep content (a polarization FORCES this) is M4, not here. -/
theorem riemannHypothesis_zeta_iff_fe_polarization :
    RiemannHypothesis zeta ↔ ∀ ρ ∈ nonTrivialZeros zeta, 1 - ρ = (starRingEnd ℂ) ρ := by
  constructor
  · intro h ρ hρ
    exact (critical_line_iff_fe_reflection ρ).mpr (h ρ hρ)
  · intro h ρ hρ
    exact (critical_line_iff_fe_reflection ρ).mp (h ρ hρ)

end ZetaRH.ArithmeticPolarization
