/-
The #143 Schur-Cohn kernel: Cohn's criterion at genus 1, and the reversal identity
behind Cohn's derivative trick.

The Schur-Cohn test decides whether a polynomial has all roots in the closed unit disk;
Cohn's refinement decides all-roots-ON-the-circle for self-inversive polynomials by
running the test on the derivative. At genus 1 the normalized L-polynomial of an
elliptic curve over F_p is

  phi(z) = z^2 - c z + 1,   c = t / sqrt(p)   (self-inversive),

and the toy grader's genus-1 certificate `4 - t^2/p >= 0` is exactly the 1x1 Schur-Cohn
quantity of phi'(z) = 2z - c. Two targets, both sorry-free:

  #SC-1 (Cohn's criterion at genus 1): `c^2 <= 4` iff every root of `z^2 - c z + 1` lies
        ON the unit circle (`normSq z = 1`). Forward direction = the lever-B eigenvalue
        extraction (`eigenvalue_modulus_le` at `q = 1`, the circle-vs-line mechanism);
        converse = the explicit off-circle real root `(c + sqrt(c^2-4))/2` (the same
        witness as `ToyModel.toy_reject_fake`). The gate `schur_cohn_gate` chains the
        three equivalent propositions: `0 <= SchurCohn_1(phi')` iff the root `c/2` of
        `phi'` lies in the closed unit disk iff `c^2 <= 4`; and
        `schur_cohn_certifies_circle` states that the certificate IS the window.
        `schurCohn1_normalized` + `certificate_iff_hasse` tie it to the un-normalized
        toy certificate `4 - t^2/q` and the Hasse window `t^2 <= 4q`.

  #SC-2 (the reversal identity): for a self-inversive polynomial
        (`reflect n p = p`, `n = natDegree p`) over any commutative ring,

          reflect (n-1) (derivative p) = n • p - X * derivative p.

        This is the algebraic identity that lets Cohn run the Schur-Cohn recursion on
        p' instead of p: the reversal of the derivative is expressible in p and p'
        alone. Proved coefficient-wise (`coeff_reflect` / `revAt` + `coeff_derivative`),
        with the natural-number subtraction at the boundary handled by explicit casing
        (`j <= n-1` reverses, `j = n` cancels, `j > n` vanishes).
-/

import ZetaRH.FunctionFieldRH
import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.Algebra.Polynomial.Reverse

namespace ZetaRH.SchurCohn

open Polynomial ZetaRH.FunctionFieldRH

/-! ## #SC-1: Cohn's criterion at genus 1

    `phi(z) = z^2 - c z + 1` (real `c`) is the normalized genus-1 L-polynomial: the
    Frobenius polynomial `X^2 - tX + q` with roots scaled by `1/sqrt q`, so the Weil
    circle `|alpha| = sqrt q` becomes the unit circle and the Hasse window `t^2 <= 4q`
    becomes `c^2 <= 4`. -/

/-- **Roots on the circle from the window (Cohn forward direction).** If `c^2 <= 4`,
    every complex root of `z^2 - c z + 1` has `|z|^2 = 1`. The two roots multiply to `1`
    and sum to the real `c`; the nonpositive discriminant forces a conjugate pair, so
    `z * conj z = 1`. This is the lever-B eigenvalue extraction
    (`eigenvalue_modulus_le`) at `q = 1`, boundary `c^2 = 4` included. -/
theorem roots_on_circle_of_window {c : ℝ} (hc : c ^ 2 ≤ 4) {z : ℂ}
    (hroot : z ^ 2 - (c : ℂ) * z + 1 = 0) : Complex.normSq z = 1 := by
  have h1 : z ^ 2 - (c : ℂ) * z + ((1 : ℝ) : ℂ) = 0 := by
    rw [Complex.ofReal_one]; exact hroot
  exact eigenvalue_modulus_le c 1 z h1 (by linarith)

/-- **The window from roots on the circle (Cohn converse direction).** If every root of
    `z^2 - c z + 1` has `|z|^2 = 1`, then `c^2 <= 4`. Contrapositive: if `c^2 > 4` the
    explicit real root `r = (c + sqrt(c^2-4))/2` exists; on-circle forces `r^2 = 1`,
    hence `c r = 2` from the root equation, hence `c^2 = c^2 r^2 = 4`, a contradiction.
    (Same witness mechanism as `ToyModel.toy_reject_fake`.) -/
theorem window_of_roots_on_circle {c : ℝ}
    (h : ∀ z : ℂ, z ^ 2 - (c : ℂ) * z + 1 = 0 → Complex.normSq z = 1) :
    c ^ 2 ≤ 4 := by
  by_contra hcon
  rw [not_le] at hcon
  set d : ℝ := Real.sqrt (c ^ 2 - 4)
  have hd2 : d ^ 2 = c ^ 2 - 4 := Real.sq_sqrt (by linarith)
  have hroot_real : ((c + d) / 2) ^ 2 - c * ((c + d) / 2) + 1 = 0 := by
    linear_combination (1 / 4 : ℝ) * hd2
  have hcast : (((c + d) / 2 : ℝ) : ℂ) ^ 2 - (c : ℂ) * (((c + d) / 2 : ℝ) : ℂ) + 1
      = ((((c + d) / 2) ^ 2 - c * ((c + d) / 2) + 1 : ℝ) : ℂ) := by
    push_cast; ring
  have hrootC : (((c + d) / 2 : ℝ) : ℂ) ^ 2 - (c : ℂ) * (((c + d) / 2 : ℝ) : ℂ) + 1
      = 0 := by
    rw [hcast, hroot_real]; simp
  have hns := h _ hrootC
  rw [Complex.normSq_ofReal] at hns
  have hcr : c * ((c + d) / 2) = 2 := by linear_combination hns - hroot_real
  have hc4 : c ^ 2 = 4 := by
    linear_combination (c * ((c + d) / 2) + 2) * hcr - c ^ 2 * hns
  linarith

/-- The 1x1 Schur-Cohn quantity of a degree-1 polynomial `a z + b`: leading coefficient
    squared minus constant coefficient squared. Nonnegativity says the single root
    `-b/a` lies in the closed unit disk. -/
def schurCohn1 (a b : ℝ) : ℝ := a ^ 2 - b ^ 2

/-- The 1x1 Schur-Cohn quantity of the Cohn derivative `phi'(z) = 2z - c` is `4 - c^2`:
    leading coefficient `2`, constant coefficient `-c`. -/
theorem schurCohn1_two_neg (c : ℝ) : schurCohn1 2 (-c) = 4 - c ^ 2 := by
  unfold schurCohn1; ring

/-- `c/2` is the root of the Cohn derivative `phi'(z) = 2z - c`. -/
theorem cohn_deriv_root (c : ℝ) : (2 : ℂ) * ((c : ℂ) / 2) - (c : ℂ) = 0 := by ring

/-- **The Schur-Cohn gate (#SC-1), the three-way equivalence.** For `phi' = 2z - c`:
    the 1x1 Schur-Cohn quantity `4 - c^2` is nonnegative iff the root `c/2` of `phi'`
    lies in the closed unit disk iff `c^2 <= 4` (the Hasse window in normalized form).
    Read together with `schur_cohn_certifies_circle`, this is the machine-checked
    statement that the toy grader's genus-1 certificate `[4 - t^2/p]` IS the window. -/
theorem schur_cohn_gate (c : ℝ) :
    (0 ≤ schurCohn1 2 (-c) ↔ Complex.normSq ((c : ℂ) / 2) ≤ 1)
      ∧ (Complex.normSq ((c : ℂ) / 2) ≤ 1 ↔ c ^ 2 ≤ 4) := by
  have hcast : ((c : ℂ) / 2) = ((c / 2 : ℝ) : ℂ) := by norm_cast
  have hns : Complex.normSq ((c : ℂ) / 2) = c / 2 * (c / 2) := by
    rw [hcast, Complex.normSq_ofReal]
  rw [hns, schurCohn1_two_neg]
  constructor
  · constructor <;> intro h <;> nlinarith
  · constructor <;> intro h <;> nlinarith

/-- **The certificate IS the circle condition.** The 1x1 Schur-Cohn quantity of the Cohn
    derivative is nonnegative iff every root of `phi(z) = z^2 - c z + 1` lies on the
    unit circle. Combines both directions of Cohn's criterion at genus 1. -/
theorem schur_cohn_certifies_circle (c : ℝ) :
    0 ≤ schurCohn1 2 (-c)
      ↔ ∀ z : ℂ, z ^ 2 - (c : ℂ) * z + 1 = 0 → Complex.normSq z = 1 := by
  rw [schurCohn1_two_neg]
  constructor
  · intro h z hz
    exact roots_on_circle_of_window (by linarith) hz
  · intro h
    have h4 := window_of_roots_on_circle h
    linarith

/-- Un-normalizing: with `c = t / sqrt q` the Schur-Cohn quantity is the toy grader's
    genus-1 certificate `4 - t^2/q` exactly. -/
theorem schurCohn1_normalized {t q : ℝ} (hq : 0 < q) :
    schurCohn1 2 (-(t / Real.sqrt q)) = 4 - t ^ 2 / q := by
  unfold schurCohn1
  rw [neg_sq, div_pow, Real.sq_sqrt hq.le]
  norm_num

/-- The un-normalized certificate is the Hasse window: `0 <= 4 - t^2/q` iff `t^2 <= 4q`
    (for `q > 0`). Together with `schurCohn1_normalized` and `schur_cohn_gate`, the toy
    grader's genus-1 certificate `[4 - t^2/p]` is, provably, nothing other than the
    Hasse bound. -/
theorem certificate_iff_hasse {t q : ℝ} (hq : 0 < q) :
    0 ≤ 4 - t ^ 2 / q ↔ t ^ 2 ≤ 4 * q := by
  have hq' : q ≠ 0 := ne_of_gt hq
  constructor
  · intro h
    have h2 : 0 ≤ (4 - t ^ 2 / q) * q := mul_nonneg h hq.le
    have e2 : (4 - t ^ 2 / q) * q = 4 * q - t ^ 2 := by
      rw [sub_mul, div_mul_cancel₀ _ hq']
    linarith [e2 ▸ h2]
  · intro h
    by_contra hcon
    rw [not_le] at hcon
    have h3 : 4 * q < t ^ 2 / q * q :=
      mul_lt_mul_of_pos_right (by linarith) hq
    rw [div_mul_cancel₀ _ hq'] at h3
    linarith

/-! ## #SC-2: the reversal identity behind Cohn's derivative trick

    For self-inversive `p` (that is `reflect n p = p` with `n = natDegree p`, i.e.
    palindromic coefficients `a_k = a_{n-k}`), the reversal of the derivative is

      reflect (n-1) (derivative p) = n • p - X * derivative p.

    Coefficient check at `X^j`: the left side is `(n-j) a_{n-j}`, the right side is
    `n a_j - j a_j = (n-j) a_j`, and self-inversivity identifies them. This identity is
    what allows the Schur-Cohn recursion to run on `p'` in Cohn's criterion: on the
    unit circle `|reflect (n-1) p'| = |p'|` combinations control root placement. -/

/-- **The reversal identity (#SC-2).** If `p` is self-inversive
    (`reflect (natDegree p) p = p`), then
    `reflect (natDegree p - 1) (derivative p) = natDegree p • p - X * derivative p`.
    Proved coefficient-wise over any commutative ring: for `j <= n-1` the reflected
    coefficient is `(n-j) a_{n-j} = (n-j) a_j`; at `j = n` the right side cancels; for
    `j > n` everything vanishes. -/
theorem reflect_derivative_self_inversive {R : Type*} [CommRing R] (p : R[X])
    (hp : reflect p.natDegree p = p) :
    reflect (p.natDegree - 1) (derivative p) = p.natDegree • p - X * derivative p := by
  simp only [nsmul_eq_mul]
  have hder : ∀ m : ℕ, (derivative p).coeff m = p.coeff (m + 1) * ((m + 1 : ℕ) : R) := by
    intro m
    rw [coeff_derivative, Nat.cast_add, Nat.cast_one]
  rcases Nat.eq_zero_or_pos p.natDegree with h0 | hnpos
  · -- degree 0: p is constant, both sides are 0
    rw [derivative_of_natDegree_zero h0, h0]
    simp [reflect_zero]
  · -- the palindrome law a_j = a_{n-j} from self-inversivity
    have hcoeff : ∀ j, j ≤ p.natDegree → p.coeff j = p.coeff (p.natDegree - j) := by
      intro j hj
      conv_lhs => rw [← hp]
      rw [coeff_reflect, revAt_le hj]
    ext j
    rw [coeff_reflect, coeff_sub, ← C_eq_natCast, coeff_C_mul]
    rcases le_or_gt j (p.natDegree - 1) with hj | hj
    · -- in range: the reflected coefficient is (n-j) a_{n-j} = (n-j) a_j
      rw [revAt_le hj]
      have hjn : j ≤ p.natDegree := le_trans hj (Nat.sub_le _ _)
      have e1 : p.natDegree - 1 - j + 1 = p.natDegree - j := by omega
      rw [hder, e1, Nat.cast_sub hjn, ← hcoeff j hjn]
      rcases Nat.eq_zero_or_pos j with rfl | hjpos
      · rw [mul_coeff_zero, coeff_X_zero, zero_mul, sub_zero]
        push_cast
        ring
      · obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero hjpos.ne'
        rw [coeff_X_mul, hder]
        push_cast
        ring
    · -- out of range: the left side vanishes; the right side cancels at j = n and
      -- vanishes for j > n
      have hjn : p.natDegree ≤ j := by omega
      rw [revAt_eq_self_of_lt hj, hder,
        coeff_eq_zero_of_natDegree_lt (by omega : p.natDegree < j + 1), zero_mul]
      obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : j ≠ 0)
      rw [coeff_X_mul, hder]
      rcases eq_or_lt_of_le hjn with heq | hlt
      · rw [heq]
        push_cast
        ring
      · rw [coeff_eq_zero_of_natDegree_lt hlt]
        simp

end ZetaRH.SchurCohn
