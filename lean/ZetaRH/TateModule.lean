/-
Lever B, M-1 route B (the Tate module): the Weil-pairing / determinant mechanism behind deg = det.

See `docs/03_research/lever_b_function_field_plan.md` (the "Discharging `hdeg`" section, Route B). The
deepest and FLT-aligned route to obligation O2 -- "the degree map is a quadratic form" -- is the Tate
module one. For `ℓ ≠ char`, the Tate module `T_ℓ E ≅ ℤ_ℓ²` is free of rank 2, `End(E)` acts on it,
and the Weil pairing `e_ℓ` is an alternating (symplectic) form with the transformation law

  e_ℓ(φ x, φ y) = e_ℓ(x, y) ^ (deg φ)        (Silverman III.8.6 / the Weil-pairing degree formula)

i.e. an isogeny scales the pairing by its degree. Because the pairing is alternating on a rank-2
module, the factor by which ANY endomorphism scales it is exactly its DETERMINANT. So `deg = det` on
`T_ℓ`, and O2 is FREE: `det` of a 2×2 is automatically a quadratic form. This file formalizes that
linear-algebra core -- the symplectic-determinant law and the resulting `deg = det` identity -- and
assembles the route-B function-field RH endpoint stated INTRINSICALLY in terms of the Weil pairing
(no `det` in the hypotheses).

What this file does NOT do (the residual O1, still ~months / FLT-adjacent): construct `T_ℓ E ≅ ℤ²`,
the action of Frobenius on it, the Weil pairing itself, and `deg ≥ 0`. Those are the genuine
scheme-theoretic inputs Mathlib lacks. Here they are the HYPOTHESES (`A`, `degOf`, `hscale`, `hnn`);
everything downstream -- that the Weil-pairing degree is `det`, the Hasse bound, `|α|² = q` -- is
machine-checked. So route B's O2 ("deg is a quadratic form") is now fully internal: it is the
symplectic-determinant law `weilForm_mulVec`, proved here, not an assumption.
-/

import ZetaRH.FunctionFieldRH

namespace ZetaRH.TateModule

open Matrix

variable {R : Type*} [CommRing R]

/-- The standard alternating (symplectic) form on the rank-2 module `Fin 2 → R`:
    `weilForm x y = x₀·y₁ − x₁·y₀`. This is the linear-algebra model of the Weil pairing on the
    Tate module `T_ℓ E ≅ ℤ_ℓ²`. -/
def weilForm (x y : Fin 2 → R) : R := x 0 * y 1 - x 1 * y 0

/-- **The symplectic determinant law (the Weil-pairing mechanism, rank 2).** Any endomorphism `A` of
    the rank-2 module `Fin 2 → R` scales the symplectic form by `det A`:
    `weilForm (A·x) (A·y) = (det A) · weilForm x y`. This is the pure-linear-algebra source of
    "deg = det": the Weil pairing transforms as `e(φx, φy) = e(x,y)^{deg φ}`, so an isogeny scales the
    pairing by its degree, and for an alternating form on a rank-2 module that scaling factor is
    exactly the determinant. -/
theorem weilForm_mulVec (A : Matrix (Fin 2) (Fin 2) R) (x y : Fin 2 → R) :
    weilForm (A.mulVec x) (A.mulVec y) = A.det * weilForm x y := by
  simp only [weilForm, mulVec, dotProduct, Fin.sum_univ_two, Matrix.det_fin_two]
  ring

/-- **The Weil-pairing degree equals the determinant ("deg = det").** If an endomorphism `A` scales
    the symplectic form `weilForm` by a constant `c` (the Weil-pairing degree of the corresponding
    isogeny), then `c = det A`. So once `deg φ` is known to be the factor by which `φ` scales the Weil
    pairing -- the geometric input -- it is FORCED to equal `det` of the rank-2 representation, with no
    further work. Proof: evaluate the scaling law at the standard basis, where `weilForm e₀ e₁ = 1`,
    and compare with `weilForm_mulVec`. -/
theorem scaling_eq_det (A : Matrix (Fin 2) (Fin 2) R) (c : R)
    (h : ∀ x y, weilForm (A.mulVec x) (A.mulVec y) = c * weilForm x y) : c = A.det := by
  have h1 := h (Pi.single 0 1) (Pi.single 1 1)
  rw [weilForm_mulVec] at h1
  have hb : weilForm (Pi.single (0 : Fin 2) (1 : R)) (Pi.single (1 : Fin 2) (1 : R)) = 1 := by
    simp [weilForm]
  rw [hb, mul_one, mul_one] at h1
  exact h1.symm

/-- **Function-field RH via the Weil-pairing degree (route-B assembly, all finite fields).** The
    route-B hypotheses stated INTRINSICALLY -- no `det` appears in them:
    * `A` represents Frobenius on the rank-2 lattice `T_ℓ E ≅ ℤ²`;
    * `degOf m n` is the degree of the isogeny `m·1 + n·φ`, given as the factor by which it scales the
      Weil pairing `weilForm` (`hscale`, the Weil-pairing degree formula);
    * every isogeny has non-negative degree (`hnn`).
    Then every Frobenius eigenvalue `α` (the complex spectrum of `A`) has `|α|² = det A` (= the degree
    of Frobenius `q`): the function-field Riemann Hypothesis for the curve, over EVERY finite field
    `𝔽_q`. Proof: `scaling_eq_det` turns the Weil-pairing scaling `hscale` into `degOf = det`, so
    `hnn` gives `det(m·1 + n·A) ≥ 0`, and `functionfield_RH_elliptic_of_matrix_general` closes it.

    Net: this internalizes route B's O2 entirely (deg=det is `weilForm_mulVec`, a theorem). The only
    open inputs left are route B's O1 -- the existence of `A`, the Weil pairing, the degree, and
    `deg ≥ 0` -- the scheme-theoretic content Mathlib lacks (coordinate with the FLT project). -/
theorem functionfield_RH_of_weil_pairing (A : Matrix (Fin 2) (Fin 2) ℤ) (degOf : ℤ → ℤ → ℤ)
    (hscale : ∀ (m n : ℤ) (x y : Fin 2 → ℤ),
        weilForm ((m • (1 : Matrix (Fin 2) (Fin 2) ℤ) + n • A).mulVec x)
            ((m • (1 : Matrix (Fin 2) (Fin 2) ℤ) + n • A).mulVec y) = degOf m n * weilForm x y)
    (hnn : ∀ m n : ℤ, 0 ≤ degOf m n)
    {α : ℂ} (hα : α ∈ spectrum ℂ (A.map (Int.castRingHom ℂ))) :
    Complex.normSq α = (A.det : ℝ) := by
  apply ZetaRH.FunctionFieldRH.functionfield_RH_elliptic_of_matrix_general _ hα
  intro m n
  have hdeg : degOf m n = (m • (1 : Matrix (Fin 2) (Fin 2) ℤ) + n • A).det :=
    scaling_eq_det _ _ (hscale m n)
  rw [← hdeg]
  exact hnn m n

end ZetaRH.TateModule
