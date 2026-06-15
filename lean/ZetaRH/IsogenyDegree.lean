/-
Lever B, milestone M-1: the isogeny DEGREE quadratic form and the Hasse bridge.

See `docs/03_research/lever_b_function_field_plan.md`. The elementary proof of the Hasse
bound (the function-field RH for an elliptic curve) routes through ONE structural fact:

  the degree map on endomorphisms is a POSITIVE quadratic form.

For Frobenius `φ` of `E/𝔽_q` with trace `t = q + 1 - #E(𝔽_q)`, every endomorphism
`m·1 + n·φ` is an isogeny, so its degree is a non-negative integer, and

  deg(m·1 + n·φ) = m² + t·m·n + q·n²              (`degForm`)

is therefore non-negative on the lattice `ℤ·1 ⊕ ℤ·φ`. The Hasse bound is the
discriminant inequality of that positive form:

  deg ≥ 0 on the lattice   ⟹   t² ≤ 4q.            (`disc_nonpos_of_int_nonneg`)

This is the same completing-the-square / Cauchy-Schwarz mechanism as the keystone #2G-1
(`negDef_iff_hasseWeil`), now run in the POSITIVE direction on the degree form. It is the
algebraic heart of milestones M-1/M-2/M-3 of the lever-B plan, proved SORRY-FREE here.

What this file does NOT do (the residual M-1 gap): it does not construct the degree map
from a real curve. That `deg : End(E) → ℤ` exists, is additive on the binary form, and is
non-negative (every isogeny has non-negative degree) is genuine scheme-theoretic
arithmetic geometry that Mathlib lacks (coordinate with the FLT project). Here those facts
are the HYPOTHESES (`degForm ≥ 0` on the lattice); everything downstream is machine-checked.
So the lever-B gap #FF-geom is pushed from a bare numeric inequality (`t² < 4q`, assumed)
back to its true geometric source (`deg` is a non-negative quadratic form), and the bridge
between them is now a theorem.

The faithful endpoint over a PRIME field is `functionfield_RH_elliptic_of_degree`
(in `FunctionFieldRH.lean`): from `deg ≥ 0` on the lattice, the Frobenius roots have
modulus `√p`, the function-field Riemann Hypothesis for the curve.
-/

import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.LinearAlgebra.QuadraticForm.Basic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic

namespace ZetaRH.IsogenyDegree

/-- The Frobenius DEGREE form: `deg(m·1 + n·φ)` for an elliptic curve whose Frobenius has
    trace `t` and degree `q` (so `deg 1 = 1`, `deg φ = q`, and the cross term is the trace
    `t = q + 1 - #E`). Equals `m² + t·m·n + q·n²`. The discriminant `t² − 4q` is unchanged
    by the sign of the cross term, so this matches the characteristic polynomial
    `X² − tX + q` used in the eigenvalue extraction. -/
def degForm (t q m n : ℝ) : ℝ := m ^ 2 + t * m * n + q * n ^ 2

/-! ## The Hasse bridge: a positive degree form has discriminant `≤ 0`

    The geometric input is non-negativity of `deg` on the integer lattice. We extend it to
    the rationals by homogeneity (`degForm` is a quadratic form: scaling `(m,n)` by `1/k`
    scales the value by `1/k²`), then to the reals by density and continuity, and finally
    read off `t² ≤ 4q` by evaluating the completed square at the real point `m = −t/2`. -/

/-- **Rational positivity ⟹ Hasse bound.** If the single-variable degree polynomial
    `g(x) = x² + t·x + q` is non-negative at every rational `x`, then `t² ≤ 4q`.

    Proof: if `t² > 4q`, set `ε = t²/4 − q > 0`. Completing the square,
    `g(x) = (x + t/2)² − ε`. Choose (density of `ℚ`) a rational `x` with
    `−t/2 < x < −t/2 + √ε`, so `0 < x + t/2 < √ε` and `(x + t/2)² < ε`, giving `g(x) < 0`,
    a contradiction. -/
theorem disc_nonpos_of_rat_nonneg {t q : ℝ}
    (h : ∀ x : ℚ, 0 ≤ ((x : ℝ)) ^ 2 + t * (x : ℝ) + q) : t ^ 2 ≤ 4 * q := by
  by_contra hcon
  rw [not_le] at hcon
  set ε : ℝ := t ^ 2 / 4 - q with hε
  have hεpos : 0 < ε := by rw [hε]; linarith
  set d : ℝ := Real.sqrt ε with hd
  have hdpos : 0 < d := Real.sqrt_pos.mpr hεpos
  have hd2 : d ^ 2 = ε := Real.sq_sqrt hεpos.le
  obtain ⟨x, hx1, hx2⟩ := exists_rat_btwn (show (-t / 2 : ℝ) < -t / 2 + d by linarith)
  have hpos : 0 < (x : ℝ) + t / 2 := by linarith
  have hltd : (x : ℝ) + t / 2 < d := by linarith
  have hsqlt : ((x : ℝ) + t / 2) ^ 2 < ε := by
    have hlt : ((x : ℝ) + t / 2) ^ 2 < d ^ 2 := by nlinarith [hpos, hltd, hdpos]
    rwa [hd2] at hlt
  have hgx := h x
  have hid : ((x : ℝ)) ^ 2 + t * (x : ℝ) + q = ((x : ℝ) + t / 2) ^ 2 - ε := by rw [hε]; ring
  rw [hid] at hgx
  linarith [hgx, hsqlt]

/-- **The Hasse bridge (M-1): a non-negative degree form has `t² ≤ 4q`.** If the Frobenius
    degree form is non-negative on the endomorphism lattice `ℤ·1 ⊕ ℤ·φ` -- the geometric
    content "every isogeny has non-negative degree" -- then the trace and degree satisfy the
    Hasse bound `t² ≤ 4q`.

    Proof: restrict to `n = 1` and use homogeneity to pass from integers to rationals
    (`degForm t q (m/k) 1 = degForm t q m k / k²`), then apply `disc_nonpos_of_rat_nonneg`. -/
theorem disc_nonpos_of_int_nonneg {t q : ℝ}
    (h : ∀ m n : ℤ, 0 ≤ degForm t q (m : ℝ) (n : ℝ)) : t ^ 2 ≤ 4 * q := by
  apply disc_nonpos_of_rat_nonneg
  intro x
  have hden : (0 : ℝ) < (x.den : ℝ) := by exact_mod_cast x.den_pos
  have hd2 : (0 : ℝ) < (x.den : ℝ) ^ 2 := by positivity
  have key : (x : ℝ) * (x.den : ℝ) = (x.num : ℝ) := by
    rw [Rat.cast_def]; field_simp
  have H := h x.num (x.den : ℤ)
  simp only [degForm, Int.cast_natCast] at H
  have hexp : (((x : ℝ)) ^ 2 + t * (x : ℝ) + q) * (x.den : ℝ) ^ 2
      = ((x : ℝ) * (x.den : ℝ)) ^ 2 + t * ((x : ℝ) * (x.den : ℝ)) * (x.den : ℝ)
        + q * (x.den : ℝ) ^ 2 := by ring
  rw [key] at hexp
  have hposmul : 0 ≤ (((x : ℝ)) ^ 2 + t * (x : ℝ) + q) * (x.den : ℝ) ^ 2 := by
    rw [hexp]; linarith [H]
  by_contra hneg
  exact absurd hposmul (not_le.mpr (mul_neg_of_neg_of_pos (not_le.mp hneg) hd2))

/-! ## Strictness over a prime field (the boundary case `t² = 4q`)

    The eigenvalue chain needs the STRICT bound `t² < 4q` (real, distinct-from-real roots).
    Hasse gives `t² ≤ 4q`; the boundary `t² = 4q` requires `4q` to be a perfect square,
    which never happens for `q = p` prime. So over a prime field the strict bound is free. -/

/-- `4p` is not a perfect square when `p` is prime: if `a² = 4p` then `a = 2b` and `b² = p`,
    so `b ∣ p` forces `b = 1` (giving `p = 1`) or `b = p` (giving `p = 1`), both absurd. -/
theorem four_mul_prime_not_isSquare {p : ℕ} (hp : p.Prime) :
    ¬ ∃ a : ℕ, a ^ 2 = 4 * p := by
  rintro ⟨a, ha⟩
  have h2a2 : 2 ∣ a ^ 2 := ⟨2 * p, by rw [ha]; ring⟩
  have h2a : 2 ∣ a := Nat.prime_two.dvd_of_dvd_pow h2a2
  obtain ⟨b, rfl⟩ := h2a
  have h4 : 4 * b ^ 2 = 4 * p := by rw [← ha]; ring
  have hb : b ^ 2 = p := Nat.eq_of_mul_eq_mul_left (by norm_num) h4
  have hbdvd : b ∣ p := ⟨b, by rw [← hb]; ring⟩
  rcases hp.eq_one_or_self_of_dvd b hbdvd with h1 | hpb
  · rw [h1, one_pow] at hb; exact hp.ne_one hb.symm
  · rw [hpb] at hb; nlinarith [hb, hp.two_le, hp.pos]

/-- **Strict Hasse over a prime field.** For `q = p` prime and integral trace `t`, the Hasse
    bound `t² ≤ 4p` upgrades to the strict `t² < 4p` (the boundary `t² = 4p` is impossible:
    `4p` is not a perfect square). This is exactly the input the eigenvalue extraction needs. -/
theorem hasse_strict_of_prime {tz : ℤ} {p : ℕ} (hp : p.Prime)
    (h : (tz : ℝ) ^ 2 ≤ 4 * (p : ℝ)) : (tz : ℝ) ^ 2 < 4 * (p : ℝ) := by
  rcases h.lt_or_eq with hlt | heq
  · exact hlt
  · exfalso
    have hz : tz ^ 2 = 4 * (p : ℤ) := by exact_mod_cast heq
    have hnat : (tz.natAbs) ^ 2 = 4 * p := by
      have e1 : ((tz.natAbs : ℤ)) ^ 2 = tz ^ 2 := by
        rw [← Int.abs_eq_natAbs]; exact sq_abs tz
      exact_mod_cast e1.trans hz
    exact four_mul_prime_not_isSquare hp ⟨tz.natAbs, hnat⟩

/-! ## M-1.5: the quadratic-form contract (reducing `hdeg` to its honest minimum)

    The geometric obligation is not "deg has the explicit form `m²+t·mn+q·n²`" but the weaker,
    structural "deg is a NON-NEGATIVE QUADRATIC FORM with deg(1)=1, deg(φ)=q". The explicit form
    is then FORCED. We model `End(E)`'s rank-2 lattice `ℤ·1 ⊕ ℤ·φ` as `ℤ × ℤ` (with `1 ↦ (1,0)`,
    `φ ↦ (0,1)`), and a Mathlib `QuadraticForm ℤ (ℤ × ℤ)` as the degree map. The trace is the polar
    `t = polar Q (1,0) (0,1)`.

    This is the precise contract the scheme-theoretic work (the dual isogeny / the Tate-module
    determinant; see `docs/03_research/lever_b_function_field_plan.md`) must instantiate: build
    `End(E)` with a degree `QuadraticForm` that is non-negative on the lattice, with `deg 1 = 1` and
    `deg φ_Frob = q`. Everything downstream (the Hasse bound, RH for the curve) is then machine-checked. -/

/-- **A quadratic form on `ℤ²` is determined on the lattice by its basis values and its polar.**
    `Q(m,n) = m²·Q(1,0) + (polar Q (1,0) (0,1))·m·n + n²·Q(0,1)`. So once `deg` is known to be a
    quadratic form (the additivity-of-the-dual content), the explicit degree polynomial is forced;
    no separate proof of the polynomial shape is needed. -/
theorem quadratic_eq_basis (Q : QuadraticForm ℤ (ℤ × ℤ)) (m n : ℤ) :
    Q (m, n) = m ^ 2 * Q ((1 : ℤ), (0 : ℤ))
        + QuadraticMap.polar Q ((1 : ℤ), (0 : ℤ)) ((0 : ℤ), (1 : ℤ)) * m * n
        + n ^ 2 * Q ((0 : ℤ), (1 : ℤ)) := by
  have hv : ((m : ℤ), (n : ℤ)) = m • ((1 : ℤ), (0 : ℤ)) + n • ((0 : ℤ), (1 : ℤ)) := by
    ext <;> simp
  rw [hv, QuadraticMap.map_add (⇑Q) (m • ((1 : ℤ), (0 : ℤ))) (n • ((0 : ℤ), (1 : ℤ))),
    QuadraticMap.map_smul, QuadraticMap.map_smul,
    QuadraticMap.polar_smul_left, QuadraticMap.polar_smul_right]
  simp only [smul_eq_mul]
  ring

/-- **M-1.5: the Hasse bound from the quadratic-form contract.** If the degree map is a quadratic
    form on the endomorphism lattice `ℤ·1 ⊕ ℤ·φ ≅ ℤ²` that is non-negative on the lattice, with
    `deg(1) = 1` and `deg(φ) = q := Q(0,1)`, then its trace `t := polar Q (1,0) (0,1)` satisfies the
    Hasse bound `t² ≤ 4q`. This is the honest minimal restatement of `hdeg`: the geometry owes only
    that `deg` is a non-negative quadratic form with two pinned values (O2 + O3 + O4 of the plan),
    never the explicit polynomial. Proof: `quadratic_eq_basis` forces the form, then the Hasse bridge
    `disc_nonpos_of_int_nonneg` closes it. -/
theorem hasse_of_quadratic (Q : QuadraticForm ℤ (ℤ × ℤ)) (h1 : Q ((1 : ℤ), (0 : ℤ)) = 1)
    (hnn : ∀ v : ℤ × ℤ, 0 ≤ Q v) :
    ((QuadraticMap.polar Q ((1 : ℤ), (0 : ℤ)) ((0 : ℤ), (1 : ℤ)) : ℤ) : ℝ) ^ 2
      ≤ 4 * ((Q ((0 : ℤ), (1 : ℤ)) : ℤ) : ℝ) := by
  apply disc_nonpos_of_int_nonneg
  intro m n
  have hge : 0 ≤ Q (m, n) := hnn (m, n)
  rw [quadratic_eq_basis Q m n, h1] at hge
  have hge' : (0 : ℝ) ≤ ((m ^ 2 * 1
      + QuadraticMap.polar Q ((1 : ℤ), (0 : ℤ)) ((0 : ℤ), (1 : ℤ)) * m * n
      + n ^ 2 * Q ((0 : ℤ), (1 : ℤ)) : ℤ) : ℝ) := by
    exact_mod_cast hge
  simp only [degForm]
  push_cast at hge'
  nlinarith [hge']

/-! ## Phase A (M-1 residual): deg = det, the rank-2 representation bridge

    See `docs/03_research/lever_b_function_field_plan.md` (M-1, Phase A). The deepest route to
    "deg is a quadratic form" is the Tate-module/representation one: an endomorphism `φ` of a rank-2
    free module has `deg φ = det φ`, `trace = tr`, and `det` of a 2×2 is AUTOMATICALLY a quadratic
    form. We package that route-agnostic linear-algebra core here over `Matrix (Fin 2) (Fin 2) ℤ`
    (the Frobenius represented on a rank-2 integer lattice / the Tate module).

    The mixed-determinant identity `det(m·1 + n·A) = m² + tr(A)·m·n + det(A)·n²` shows the degree
    form IS `degForm` with `t = tr A`, `q = det A`. So if every isogeny `m·1 + n·φ` has non-negative
    degree (`det(m·1 + n·A) ≥ 0` on the lattice), the Hasse bound `t² ≤ 4q` follows. This SHARPENS
    the M-1 residual to: construct the rank-2 integer Frobenius representation `A` with
    `det(m·1 + n·A) ≥ 0`, `det A = q`, `trace A = t = q+1-#E` (the open scheme-theoretic content;
    routes A′/B in the plan). -/

/-- **The 2×2 mixed-determinant identity.** `det(m·1 + n·A) = m² + tr(A)·m·n + det(A)·n²`. This is
    why `deg = det` is a quadratic form in `(m, n)`: the degree of `m·1 + n·φ` is exactly `degForm`
    with `t = tr A`, `q = det A`. -/
theorem det_smul_one_add_smul (A : Matrix (Fin 2) (Fin 2) ℤ) (m n : ℤ) :
    (m • (1 : Matrix (Fin 2) (Fin 2) ℤ) + n • A).det
      = m ^ 2 + A.trace * m * n + A.det * n ^ 2 := by
  have o00 : (1 : Matrix (Fin 2) (Fin 2) ℤ) 0 0 = 1 := Matrix.one_apply_eq 0
  have o11 : (1 : Matrix (Fin 2) (Fin 2) ℤ) 1 1 = 1 := Matrix.one_apply_eq 1
  have o01 : (1 : Matrix (Fin 2) (Fin 2) ℤ) 0 1 = 0 := Matrix.one_apply_ne (by decide)
  have o10 : (1 : Matrix (Fin 2) (Fin 2) ℤ) 1 0 = 0 := Matrix.one_apply_ne (by decide)
  simp only [Matrix.det_fin_two, Matrix.trace_fin_two, Matrix.add_apply, Matrix.smul_apply,
    smul_eq_mul, o00, o11, o01, o10]
  ring

/-- **Hasse bound from a rank-2 representation (deg = det).** If Frobenius is represented by an
    integer 2×2 matrix `A` whose degree form `det(m·1 + n·A)` is non-negative on the lattice -- the
    content "every isogeny `m·1 + n·φ` has non-negative degree" with `deg = det` -- then the Hasse
    bound `(tr A)² ≤ 4·(det A)` holds. With `tr A = t` (the Frobenius trace) and `det A = q` (the
    degree of Frobenius), this is exactly `t² ≤ 4q`. Proof: `det_smul_one_add_smul` turns the degree
    form into `degForm`, then the Hasse bridge `disc_nonpos_of_int_nonneg` closes it. The "deg is a
    quadratic form" step (the crux of M-1, route B's O2) is here free: `det` of a 2×2 is quadratic. -/
theorem hasse_of_matrix (A : Matrix (Fin 2) (Fin 2) ℤ)
    (hpos : ∀ m n : ℤ, 0 ≤ (m • (1 : Matrix (Fin 2) (Fin 2) ℤ) + n • A).det) :
    (A.trace : ℝ) ^ 2 ≤ 4 * (A.det : ℝ) := by
  apply disc_nonpos_of_int_nonneg
  intro m n
  have h := hpos m n
  rw [det_smul_one_add_smul] at h
  simp only [degForm]
  exact_mod_cast h

end ZetaRH.IsogenyDegree
