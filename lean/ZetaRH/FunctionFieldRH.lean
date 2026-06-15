/-
Lever B: the FUNCTION-FIELD Riemann Hypothesis dependency chain.

See `docs/03_research/optimizing_rh_for_ai.md` (lever B) and
`docs/03_research/modular_polarization_carrier.md`. The point of lever B is to make
Lean the non-circular value function: formalize Weil's function-field proof end-to-end,
so the Spec(Z) lift becomes a proof-transport task with Lean rejecting every circular
or wrong step.

This file makes the genus-1 (elliptic) function-field RH chain EXPLICIT and proves
everything except the one geometric step that Mathlib lacks. The chain:

  (geometry)   the primitive intersection form on C x C is the 2x2 G_prim(1,q,t),
               and Castelnuovo-Severi / Weil's Hodge index theorem makes it
               negative-definite                                  -- `hodge_index_curve_elliptic`, SORRY
  (keystone)   NegDef G_prim  <=>  t^2 < 4 q  (Hasse-Weil)        -- `negDef_iff_hasseWeil` (#2G-1, PROVED in HodgeIndex)
  (eigenvalue) t^2 < 4 q  =>  the Frobenius roots are non-real    -- `root_nonreal`, PROVED here
               and a non-real root has |alpha|^2 = q              -- `eigenvalue_modulus`, PROVED here
  (RH)         |alpha| = sqrt(q): the curve's zeta zeros lie on |s| = q^{-1/2}, i.e. Re = 1/2.

This file is now FULLY SORRY-FREE. The chain "Hodge index => RH for the curve" is proved
(`functionfield_RH_elliptic_of_hodge`, `functionfield_RH_elliptic`); the one geometric
input (Castelnuovo-Severi, `t^2 < 4q`) is carried as an explicit hypothesis field of the
`EllipticFrobeniusData` structure, NOT a `sorry`. So the function-field RH chain is a
sorry-free CONDITIONAL theorem whose single assumption is the curve-intersection geometry
Mathlib lacks (a theorem in the literature, ~medium effort to formalize once curves/Chow
groups exist). This also repairs the previous `hodge_index_curve_elliptic`, which admitted
a FALSE proposition (`NegDef 1 q t` for all `q,t`, false when `t^2 ≥ 4q`) via `sorry`.

The eigenvalue extraction proved here is the new sorry-free link: Vieta on the real
quadratic X^2 - tX + q gives alpha * conj(alpha) = q, and alpha * conj(alpha) = |alpha|^2.
-/

import ZetaRH.HodgeIndex
import ZetaRH.IsogenyDegree
import Mathlib.Data.Complex.Basic
import Mathlib.LinearAlgebra.Matrix.Charpoly.Coeff
import Mathlib.LinearAlgebra.Matrix.Charpoly.Eigs

namespace ZetaRH.FunctionFieldRH

open ZetaRH.HodgeIndex.IntersectionSignature
open ZetaRH.IsogenyDegree

/-! ## M-0 (lever B roadmap): the discriminant bridge lemma

    See `docs/03_research/lever_b_function_field_plan.md`. In the elementary proof of the
    Hasse bound, "every isogeny has non-negative degree" gives
    `deg(m + n φ) = m^2 + m n t + n^2 q ≥ 0`, a positive-(semi)definite binary quadratic
    form, and a positive-(semi)definite form has non-positive discriminant `t^2 ≤ 4q`.
    These two lemmas are that bridge. They are the positive mirror of the keystone #2G-1
    (`negDef_iff_hasseWeil`). The remaining glue for milestone M-3 -- the form is `≥ 0`
    for all *real* m,n, obtained from `≥ 0` for integer m,n by homogeneity and density --
    is not done here; M-0 is just the discriminant step. -/

/-- A positive-semidefinite real binary quadratic form `m^2 + t·m·n + q·n^2 ≥ 0` (for all
    real `m, n`) has non-positive discriminant: `t^2 ≤ 4q`. Proof: evaluate at
    `(m, n) = (-t/2, 1)`, where the form equals `q - t^2/4`. -/
theorem disc_nonpos_of_posSemidef {t q : ℝ}
    (h : ∀ m n : ℝ, 0 ≤ m ^ 2 + t * m * n + q * n ^ 2) : t ^ 2 ≤ 4 * q := by
  have hmin := h (-t / 2) 1
  nlinarith [hmin]

/-- A positive-definite real binary quadratic form (`> 0` off the origin) has negative
    discriminant: `t^2 < 4q` (the strict Hasse bound). This is the form M-0 the chain
    needs: the Frobenius degree form is positive-DEFINITE (`deg ψ = 0 ↔ ψ = 0`), and the
    strict bound feeds `t^2 < 4q ⇒ non-real roots ⇒ |α| = √q`. -/
theorem disc_neg_of_posDef {t q : ℝ}
    (h : ∀ m n : ℝ, (m, n) ≠ (0, 0) → 0 < m ^ 2 + t * m * n + q * n ^ 2) :
    t ^ 2 < 4 * q := by
  have hne : ((-t / 2 : ℝ), (1 : ℝ)) ≠ (0, 0) := by
    intro hc
    exact one_ne_zero (Prod.ext_iff.mp hc).2
  have hmin := h (-t / 2) 1 hne
  nlinarith [hmin]

/-- **Eigenvalue extraction (PROVED).** A genuinely complex (non-real) root `α` of the
    Frobenius characteristic polynomial `X^2 - tX + q` (real `t, q`) has `|α|^2 = q`.

    Proof: conjugating the equation shows `conj α` is also a root; since `α ≠ conj α`
    the two roots are `α, conj α`, so by Vieta `α + conj α = t` and `α · conj α = q`.
    But `α · conj α = normSq α`, hence `normSq α = q`. -/
theorem eigenvalue_modulus (t q : ℝ) (α : ℂ)
    (hroot : α ^ 2 - (t : ℂ) * α + (q : ℂ) = 0)
    (hnonreal : α ≠ (starRingEnd ℂ) α) : Complex.normSq α = q := by
  have hconj : (starRingEnd ℂ α) ^ 2 - (t : ℂ) * (starRingEnd ℂ α) + (q : ℂ) = 0 := by
    have h := congrArg (starRingEnd ℂ) hroot
    simpa only [map_add, map_sub, map_mul, map_pow, Complex.conj_ofReal, map_zero] using h
  have hne : α - starRingEnd ℂ α ≠ 0 := sub_ne_zero.mpr hnonreal
  have h1 : (α - starRingEnd ℂ α) * (α + starRingEnd ℂ α - (t : ℂ)) = 0 := by
    linear_combination hroot - hconj
  have hsum : α + starRingEnd ℂ α = (t : ℂ) := by
    rcases mul_eq_zero.mp h1 with h | h
    · exact absurd h hne
    · exact sub_eq_zero.mp h
  have hprod : α * starRingEnd ℂ α = (q : ℂ) := by linear_combination α * hsum - hroot
  have hmc : α * starRingEnd ℂ α = ((Complex.normSq α : ℝ) : ℂ) := Complex.mul_conj α
  have hcast : ((Complex.normSq α : ℝ) : ℂ) = ((q : ℝ) : ℂ) := by rw [← hmc, hprod]
  exact_mod_cast hcast

/-- **Non-reality of the Frobenius roots (PROVED).** When the Hasse-Weil bound
    `t^2 < 4q` holds, every root of `X^2 - tX + q` is non-real: a real root would force
    the discriminant `t^2 - 4q ≥ 0`. -/
theorem root_nonreal (t q : ℝ) (α : ℂ)
    (hroot : α ^ 2 - (t : ℂ) * α + (q : ℂ) = 0) (hHW : t ^ 2 < 4 * q) :
    α ≠ (starRingEnd ℂ) α := by
  intro h
  have him : α.im = 0 := Complex.conj_eq_iff_im.mp h.symm
  have hre : α = (α.re : ℂ) := by
    apply Complex.ext <;> simp [him]
  have hr : α.re ^ 2 - t * α.re + q = 0 := by
    have hc : ((α.re ^ 2 - t * α.re + q : ℝ) : ℂ) = 0 := by
      push_cast; rw [← hre]; exact hroot
    exact_mod_cast hc
  nlinarith [sq_nonneg (t - 2 * α.re), hHW, hr]

/-- The geometric input for a genus-1 curve, packaged honestly. The Castelnuovo-Severi
    / Hodge-index inequality `t^2 < 4q` (equivalently the primitive intersection form on
    `C × C` is negative-definite, equivalently `|t| < 2 sqrt q`) is a THEOREM over a real
    curve, but Mathlib has no algebraic-curve intersection theory to derive it from the
    curve's definition. So it is carried here as an explicit hypothesis field `hodge_index`
    -- the lever-B gap, made honest: a hypothesis, not a `sorry`.

    (This repairs the previous `hodge_index_curve_elliptic`, which stated `NegDef 1 q t`
    behind a vacuous `True` hypothesis -- a FALSE proposition for `t^2 ≥ 4q`, admitted by
    `sorry`. The constraint must live in the data, and it does, as `hodge_index`.) -/
structure EllipticFrobeniusData where
  q : ℝ
  t : ℝ
  hq : 0 < q
  /-- Castelnuovo-Severi / the Hodge index for the curve: the one geometric input (#FF-geom). -/
  hodge_index : t ^ 2 < 4 * q

/-- The Hodge-index input gives negative-definiteness of the primitive form. SORRY-FREE:
    the geometric content is the explicit `hodge_index` field; the keystone #2G-1 does the
    rest. -/
theorem negDef_of_curve (C : EllipticFrobeniusData) : NegDef 1 C.q C.t := by
  have h : C.t ^ 2 < 4 * 1 ^ 2 * C.q := by nlinarith [C.hodge_index]
  exact (negDef_iff_hasseWeil (by norm_num)).mpr h

/-- **Hodge index => RH for the curve (SORRY-FREE implication).** Given the geometric
    Hodge-index input (`NegDef`, i.e. the primitive form is negative-definite) and a
    Frobenius root `α`, its modulus is `√q`: the function-field Riemann Hypothesis for
    the curve. The keystone (#2G-1) and the eigenvalue extraction are proved; only the
    geometric input is assumed. -/
theorem functionfield_RH_elliptic_of_hodge {q t : ℝ} (_hq : 0 < q)
    (hHodge : NegDef 1 q t) {α : ℂ} (hroot : α ^ 2 - (t : ℂ) * α + (q : ℂ) = 0) :
    Complex.normSq α = q := by
  have hHW : t ^ 2 < 4 * 1 ^ 2 * q := (negDef_iff_hasseWeil (by norm_num)).mp hHodge
  have hHW' : t ^ 2 < 4 * q := by nlinarith [hHW]
  exact eigenvalue_modulus t q α hroot (root_nonreal t q α hroot hHW')

/-- **The full function-field RH chain (genus 1), SORRY-FREE modulo one explicit
    geometric hypothesis.** Given the curve datum `C` (which carries the Castelnuovo-Severi
    inequality as its `hodge_index` field) and a Frobenius root `α`, the modulus is `√q`.
    The entire chain -- the keystone #2G-1, the eigenvalue extraction, and this assembly --
    is proved; the single unformalized input is `C.hodge_index` (the curve-intersection
    geometry Mathlib lacks), now an explicit, true hypothesis rather than a `sorry`. -/
theorem functionfield_RH_elliptic (C : EllipticFrobeniusData)
    {α : ℂ} (hroot : α ^ 2 - (C.t : ℂ) * α + (C.q : ℂ) = 0) : Complex.normSq α = C.q :=
  functionfield_RH_elliptic_of_hodge C.hq (negDef_of_curve C) hroot

/-! ## M-1 (lever B roadmap): the curve datum from the genuine degree-positivity input

    The structure `EllipticFrobeniusData` carries the Hasse bound `t² < 4q` as a raw
    numeric field. M-1 (see `IsogenyDegree.lean` and `docs/03_research/lever_b_function_field_plan.md`)
    DERIVES that bound from the true geometric source: the Frobenius degree form is
    non-negative on the endomorphism lattice ("every isogeny has non-negative degree").
    The constructor below builds the curve datum from that input over a prime field, so the
    whole chain to RH now flows from `deg ≥ 0`, not from an assumed inequality. The single
    remaining geometric gap is that `deg` really IS this non-negative quadratic form for a
    real curve (the isogeny/degree API Mathlib lacks), now isolated as the hypothesis `hdeg`. -/

/-- **M-1 constructor (prime field).** Build the curve datum from the genuine Hasse input:
    `p` prime, integral trace `tz`, and the degree form `m² + tz·m·n + p·n²` non-negative on
    the lattice `ℤ·1 ⊕ ℤ·φ`. The strict bound `tz² < 4p` is produced sorry-free by the Hasse
    bridge (`disc_nonpos_of_int_nonneg`) plus the boundary exclusion (`hasse_strict_of_prime`,
    using that `4p` is never a perfect square for prime `p`). -/
def EllipticFrobeniusData.ofDegreeNonneg {p : ℕ} {tz : ℤ} (hp : p.Prime)
    (hdeg : ∀ m n : ℤ, 0 ≤ degForm (tz : ℝ) (p : ℝ) (m : ℝ) (n : ℝ)) :
    EllipticFrobeniusData where
  q := (p : ℝ)
  t := (tz : ℝ)
  hq := by exact_mod_cast hp.pos
  hodge_index := hasse_strict_of_prime hp (disc_nonpos_of_int_nonneg hdeg)

/-- **Function-field RH for an elliptic curve over a prime field, from the genuine geometric
    input (SORRY-FREE).** If `p` is prime, the trace `tz` is integral, and every isogeny
    `m·1 + n·φ` has non-negative degree (`degForm ≥ 0` on the lattice), then any Frobenius
    root `α` of `X² − tz·X + p` has `|α|² = p`: the curve's zeta zeros lie on `Re = 1/2`.

    This is the M-1 endpoint: the Hasse bound is now a THEOREM (derived from degree
    positivity by `disc_nonpos_of_int_nonneg` + `hasse_strict_of_prime`), not a hypothesis.
    The only unformalized input is `hdeg` (that `deg` is this non-negative quadratic form for
    a real curve), the irreducible scheme-theoretic content of M-1 that Mathlib still lacks. -/
theorem functionfield_RH_elliptic_of_degree {p : ℕ} {tz : ℤ} (hp : p.Prime)
    (hdeg : ∀ m n : ℤ, 0 ≤ degForm (tz : ℝ) (p : ℝ) (m : ℝ) (n : ℝ)) {α : ℂ}
    (hroot : α ^ 2 - ((tz : ℝ) : ℂ) * α + ((p : ℝ) : ℂ) = 0) : Complex.normSq α = (p : ℝ) :=
  functionfield_RH_elliptic (EllipticFrobeniusData.ofDegreeNonneg hp hdeg) hroot

/-! ## Phase A endpoint (route B): RH for the curve directly from the Frobenius matrix

    See `docs/03_research/lever_b_function_field_plan.md` (M-1, Phase A; task 5, "Wire"). Phase A
    in `IsogenyDegree.lean` (`hasse_of_matrix`) showed that a rank-2 integer representation `A` of
    Frobenius -- the action on the Tate module `T_ℓ E ≅ ℤ²`, where `deg = det` and `trace = tr` --
    whose isogeny degrees are non-negative (`det(m·1 + n·A) ≥ 0` on the lattice) satisfies the Hasse
    bound `(tr A)² ≤ 4·det A`. This section closes the loop to RH for the curve by grounding the
    Frobenius "roots" of the previous theorems in the genuine eigenvalues of `A`.

    The bridge is Cayley-Hamilton at rank 2: the eigenvalues of `A` (the complex spectrum of the
    complexification `A.map (ℤ → ℂ)`) are exactly the roots of the characteristic polynomial
    `X² − (tr A)·X + (det A)` (`Matrix.charpoly_fin_two`). Feeding those roots through the eigenvalue
    extraction proved above gives `|α|² = det A = q`, the function-field Riemann Hypothesis for the
    curve. The single open input is unchanged: that such an integer matrix `A` (the Frobenius on the
    Tate module, `det A = q`, `tr A = q+1-#E`, non-negative isogeny degrees) EXISTS for a real curve
    -- the scheme-theoretic O1+O2 residual of M-1 (route B), coordinated with the FLT project. -/

/-- **Eigenvalue ⟹ characteristic-polynomial root (rank 2).** A complex number `α` in the spectrum
    of the complexified integer matrix `A.map (ℤ → ℂ)` is a root of `X² − (tr A)·X + (det A)`. This
    grounds the abstract Frobenius-root hypothesis of the chain above in the genuine eigenvalues of
    the rank-2 Frobenius representation. Proof: `Matrix.mem_spectrum_iff_isRoot_charpoly` over the
    field `ℂ`, then `Matrix.charpoly_fin_two`, with `trace`/`det` commuting through the cast. -/
theorem matrix_charpoly_root {A : Matrix (Fin 2) (Fin 2) ℤ} {α : ℂ}
    (hα : α ∈ spectrum ℂ (A.map (Int.castRingHom ℂ))) :
    α ^ 2 - (A.trace : ℂ) * α + (A.det : ℂ) = 0 := by
  have hr : Polynomial.eval α (A.map (Int.castRingHom ℂ)).charpoly = 0 :=
    Matrix.mem_spectrum_iff_isRoot_charpoly.mp hα
  have htr : (A.map (Int.castRingHom ℂ)).trace = (A.trace : ℂ) := by
    rw [← AddMonoidHom.map_trace (Int.castRingHom ℂ) A]; simp
  have hdet : (A.map (Int.castRingHom ℂ)).det = (A.det : ℂ) := by
    rw [← RingHom.mapMatrix_apply, ← RingHom.map_det]; simp
  rw [Matrix.charpoly_fin_two, htr, hdet] at hr
  simpa [Polynomial.eval_add, Polynomial.eval_sub, Polynomial.eval_mul, Polynomial.eval_pow,
    Polynomial.eval_C, Polynomial.eval_X] using hr

/-- **Function-field RH from the Frobenius matrix, abstract-root form.** Over a prime field `q = p`,
    a rank-2 integer Frobenius matrix `A` with `det A = p` and non-negative isogeny degrees
    (`det(m·1 + n·A) ≥ 0` on the lattice) forces any root `α` of `X² − (tr A)·X + p` to have
    `|α|² = p`. Proof: `hasse_of_matrix` (Phase A) gives `(tr A)² ≤ 4p`, `hasse_strict_of_prime`
    upgrades it to the strict bound, then the eigenvalue extraction (`root_nonreal`,
    `eigenvalue_modulus`) closes it. -/
theorem functionfield_RH_elliptic_of_matrix_root {A : Matrix (Fin 2) (Fin 2) ℤ} {p : ℕ}
    (hp : p.Prime) (hdetp : A.det = (p : ℤ))
    (hpos : ∀ m n : ℤ, 0 ≤ (m • (1 : Matrix (Fin 2) (Fin 2) ℤ) + n • A).det)
    {α : ℂ} (hroot : α ^ 2 - (A.trace : ℂ) * α + (p : ℂ) = 0) :
    Complex.normSq α = (p : ℝ) := by
  have hHasse : (A.trace : ℝ) ^ 2 ≤ 4 * (A.det : ℝ) := hasse_of_matrix A hpos
  rw [hdetp] at hHasse
  have hHasse2 : (A.trace : ℝ) ^ 2 ≤ 4 * (p : ℝ) := by push_cast at hHasse ⊢; linarith
  have hstrict : (A.trace : ℝ) ^ 2 < 4 * (p : ℝ) := hasse_strict_of_prime hp hHasse2
  have hroot' : α ^ 2 - (((A.trace : ℝ)) : ℂ) * α + (((p : ℝ)) : ℂ) = 0 := by
    push_cast; linear_combination hroot
  exact eigenvalue_modulus (A.trace : ℝ) (p : ℝ) α hroot'
    (root_nonreal (A.trace : ℝ) (p : ℝ) α hroot' hstrict)

/-- **Function-field RH for an elliptic curve from its Frobenius matrix (route B endpoint).** Let
    `A : Matrix (Fin 2) (Fin 2) ℤ` represent Frobenius on the rank-2 lattice `T_ℓ E ≅ ℤ²` over a
    prime field, with `det A = p` (the degree of Frobenius) and every isogeny `m·1 + n·φ` of
    non-negative degree (`det(m·1 + n·A) ≥ 0`, i.e. `deg = det`). Then every Frobenius eigenvalue
    `α` (the complex spectrum of `A`) has `|α|² = p`: the curve's zeta zeros lie on `Re = 1/2`.

    This is the route-B endpoint of M-1: the literal finite-field rehearsal of the M4 target
    ("`deg = det = norm` is a quadratic form whose positivity is RH", here proved). The whole chain
    -- the deg=det quadratic-form structure (`det_smul_one_add_smul`), the Hasse bridge
    (`disc_nonpos_of_int_nonneg`), the strict prime boundary, the eigenvalue grounding
    (`matrix_charpoly_root`), and the eigenvalue extraction -- is machine-checked. The one open input
    is the EXISTENCE of `A` (the scheme-theoretic Frobenius-on-Tate-module construction, O1+O2;
    coordinate with FLT). -/
theorem functionfield_RH_elliptic_of_matrix {A : Matrix (Fin 2) (Fin 2) ℤ} {p : ℕ}
    (hp : p.Prime) (hdetp : A.det = (p : ℤ))
    (hpos : ∀ m n : ℤ, 0 ≤ (m • (1 : Matrix (Fin 2) (Fin 2) ℤ) + n • A).det)
    {α : ℂ} (hα : α ∈ spectrum ℂ (A.map (Int.castRingHom ℂ))) :
    Complex.normSq α = (p : ℝ) := by
  have hroot0 := matrix_charpoly_root hα
  rw [hdetp] at hroot0
  have hroot : α ^ 2 - (A.trace : ℂ) * α + (p : ℂ) = 0 := by
    push_cast at hroot0; linear_combination hroot0
  exact functionfield_RH_elliptic_of_matrix_root hp hdetp hpos hroot

end ZetaRH.FunctionFieldRH
