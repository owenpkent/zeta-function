/-
Front A (the real Lean floor), milestone 1: the C x C divisor / intersection-form scaffold.

See `docs/03_research/optimizing_rh_for_ai.md` (lever B) and `FunctionFieldRH.lean`. The goal of
Front A is to formalize Weil's function-field RH end-to-end; the geometry Mathlib lacks (curves,
divisors, Chow groups, the intersection product on C x C, the Frobenius correspondence) is the gap.

This file builds the Neron-Severi intersection data of C x C ABSTRACTLY -- as the intersection
NUMBERS, which is the geometric content -- and DERIVES the primitive intersection Gram matrix
`G_prim` from them. This machine-checks the one step that `HodgeIndex.lean` (block 2G) previously
only ASSERTED in a comment: "after projecting out the hyperbolic plane {f1,f2} the primitive form on
{Delta, Gamma} is G_prim". With this, Weil's Hodge index theorem (`negDef_iff_hasseWeil`, the proved
keystone #2G-1) reads the Hasse-Weil bound off the intersection numbers.

The classes on C x C for a smooth projective curve C of genus g over F_q:
  f1 = C x pt,  f2 = pt x C    -- the hyperbolic plane: f1^2 = f2^2 = 0, f1 . f2 = 1
  Delta = the diagonal          -- the graph of the identity
  Gamma = the graph of the q-power Frobenius  -- a degree-q correspondence

The intersection numbers (the geometric input; the scheme-theoretic content Mathlib lacks):
  Delta . f1 = Delta . f2 = 1,    Delta^2 = 2 - 2g           -- adjunction on C x C (Delta = C)
  Gamma . f1 = q,  Gamma . f2 = 1,  Gamma^2 = 2q(1 - g)      -- adjunction (Gamma = C, deg q):
                                                                2g-2 = Gamma^2 + Gamma.K, K = (2g-2)(f1+f2),
                                                                Gamma.K = (2g-2)(1+q), so Gamma^2 = 2q(1-g)
  Gamma . Delta = #C(F_q) = q + 1 - t                        -- Lefschetz fixed points = the trace t

The primitive pairing (orthogonal projection off the hyperbolic plane):
  <D,E>_prim = D.E - (D.f1)(E.f2) - (D.f2)(E.f1).

Plugging the numbers in gives exactly `G_prim = [[-2g, -t], [-t, -2gq]]` (`primGram_eq_Gprim`,
proved sorry-free below). The remaining gap is purely that these intersection numbers hold for a
real curve (the Frobenius correspondence / curve intersection theory Mathlib lacks); everything
algebraic -- the reduction to `G_prim` and thence to the Hasse bound -- is now machine-checked.
-/

import ZetaRH.HodgeIndex

namespace ZetaRH.CurveSquare

open ZetaRH.HodgeIndex.IntersectionSignature

/-- The primitive intersection pairing on `C x C`: project off the hyperbolic plane `{f1, f2}`
    (`f1^2 = f2^2 = 0`, `f1 . f2 = 1`). For classes `D, E` with intersection number `DE` and fiber
    degrees `(Df1, Df2)`, `(Ef1, Ef2)`:
      `<D,E>_prim = D.E - (D.f1)(E.f2) - (D.f2)(E.f1)`. -/
def primPair (DE Df1 Df2 Ef1 Ef2 : ℝ) : ℝ := DE - Df1 * Ef2 - Df2 * Ef1

/-- The four primitive intersection numbers on `{Delta, Gamma}`, from the standard `C x C`
    numbers. Each is a one-line `ring` identity; together they are the entries of `G_prim`. -/
theorem prim_DeltaDelta (g : ℝ) : primPair (2 - 2 * g) 1 1 1 1 = -2 * g := by
  unfold primPair; ring

theorem prim_DeltaGamma (q t : ℝ) : primPair (q + 1 - t) 1 1 q 1 = -t := by
  unfold primPair; ring

theorem prim_GammaDelta (q t : ℝ) : primPair (q + 1 - t) q 1 1 1 = -t := by
  unfold primPair; ring

theorem prim_GammaGamma (g q : ℝ) : primPair (2 * q - 2 * g * q) q 1 q 1 = -2 * g * q := by
  unfold primPair; ring

/-- The `2 x 2` primitive intersection Gram matrix on `{Delta, Gamma}`, assembled from the
    standard `C x C` intersection numbers for a genus-`g` curve over `F_q` with Frobenius trace `t`
    (so `Gamma . Delta = q + 1 - t`). -/
def primGram (g q t : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![ primPair (2 - 2 * g) 1 1 1 1     , primPair (q + 1 - t) 1 1 q 1 ;
      primPair (q + 1 - t) q 1 1 1     , primPair (2 * q - 2 * g * q) q 1 q 1 ]

/-- **Milestone 1 (the geometry → `G_prim` reduction, machine-checked).** The primitive
    intersection Gram on `{Delta, Gamma}`, assembled from the raw `C x C` intersection numbers,
    equals the primitive form `Gprim g q t = [[-2g, -t], [-t, -2gq]]` that `HodgeIndex.lean` (2G)
    previously only asserted in a comment. Proof: substitute the four primitive intersection
    numbers (`prim_*`), then the two `!![...]` literals coincide. -/
theorem primGram_eq_Gprim (g q t : ℝ) : primGram g q t = Gprim g q t := by
  simp only [primGram, Gprim, prim_DeltaDelta, prim_DeltaGamma, prim_GammaDelta, prim_GammaGamma]

/-- The determinant of the primitive Gram, from the intersection numbers, is the Hasse-Weil
    discriminant `4 g^2 q - t^2`. (Via `primGram_eq_Gprim` and `Gprim_det`.) -/
theorem primGram_det (g q t : ℝ) : (primGram g q t).det = 4 * g ^ 2 * q - t ^ 2 := by
  rw [primGram_eq_Gprim, Gprim_det]

/-- **Milestone 1 endpoint: the `C x C` Hodge index reads off the Hasse bound, from the
    intersection numbers.** For `g > 0`, the primitive intersection form on `{Delta, Gamma}`
    (assembled from the `C x C` intersection numbers, `primGram_eq_Gprim`) is negative definite iff
    `t^2 < 4 g^2 q`. The geometry → `G_prim` step is now proved; the keystone `negDef_iff_hasseWeil`
    supplies the signature ⟺ bound. So Weil's Hodge index on `C x C` IS the Hasse-Weil bound, with
    only the intersection numbers themselves left as the (isolated) scheme-theoretic input. -/
theorem curveSquare_negDef_iff_hasseWeil {g q t : ℝ} (hg : 0 < g) :
    NegDef g q t ↔ t ^ 2 < 4 * g ^ 2 * q :=
  negDef_iff_hasseWeil hg

/-- Genus-1 (elliptic) specialization, the form `FunctionFieldRH.lean` consumes: the primitive
    `C x C` form for an elliptic curve is `Gprim 1 q t`, negative definite iff `t^2 < 4q` (the
    `EllipticFrobeniusData.hodge_index` input). So that input is exactly the Hodge index of the
    primitive intersection form on `E x E`. -/
theorem primGram_elliptic (q t : ℝ) : primGram 1 q t = Gprim 1 q t := primGram_eq_Gprim 1 q t

theorem curveSquare_elliptic_negDef_iff (q t : ℝ) :
    NegDef 1 q t ↔ t ^ 2 < 4 * q := by
  rw [negDef_iff_hasseWeil (by norm_num : (0:ℝ) < 1)]
  constructor <;> intro h <;> nlinarith [h]

end ZetaRH.CurveSquare
