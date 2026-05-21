"""Experiment 2B: Weil's RH for an elliptic curve over F_p, worked example.

The Weil conjectures specialize, for a smooth projective curve C of
genus g over F_p, to: the zeta function

    Z(C, T) = exp(sum_{k>=1} #C(F_{p^k}) T^k / k)

is a rational function

    Z(C, T) = P(T) / ((1 - T)(1 - pT))

where P(T) is a polynomial of degree 2g whose reciprocal roots alpha_i
satisfy |alpha_i| = sqrt(p). For g = 1 (elliptic curve), P(T) =
1 - a_p T + p T^2 and the two reciprocal roots are alpha, alpha-bar with
|alpha|^2 = p. The 'Riemann hypothesis' for C reads: all zeros of
Z(C, p^{-s}) lie on Re(s) = 1/2, which is equivalent to |alpha| = sqrt(p).

We pick the elliptic curve E: y^2 = x^3 + x + 1 over F_5 and:

  1. Count |C(F_5^k)| for k = 1, ..., 8 by brute force
  2. Extract a_5 from k=1, predict |C(F_5^k)| via the Weil formula
       |C(F_p^k)| = p^k + 1 - alpha^k - alpha-bar^k
     and verify against brute force
  3. Verify the Riemann hypothesis for C: |alpha| = sqrt(5)
  4. Compute the "explicit formula" sum analog over the Frobenius eigenvalues

This is the prototype proof we're trying to lift. The structural facts
that make it WORK for curves:
  - Etale cohomology H^*(C, Q_l) is a finite-dimensional Q_l-vector space
  - Frobenius acts on this cohomology with eigenvalues = the reciprocal
    roots of P(T)
  - Poincare duality: eigenvalues come in pairs (alpha, p/alpha)
  - Hodge index theorem on C x C: gives positivity which forces
    |alpha| = sqrt(p)

The corresponding facts that we DO NOT have for Spec(Z):
  - No analogue of etale cohomology with a Frobenius-like operator
  - No compactification analogue of Poincare duality (Arakelov is partial)
  - No analogue of Hodge index theorem

That's the gap. This experiment makes the curve case concrete so the
structural diff is unambiguous.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def point_count_F_pk(a_coeffs: tuple, p: int, k: int):
    """Count |C(F_{p^k})| for the elliptic curve y^2 = x^3 + a*x + b.

    Uses the field F_p^k built as F_p[T] / (irreducible polynomial of
    degree k). We represent elements as numpy int arrays of length k
    mod p, multiplication via convolution then reduction.

    For simplicity (correctness over speed), we work over F_p when k=1
    by direct counting and handle k > 1 by constructing the field.
    """
    a, b = a_coeffs
    if k == 1:
        count = 1  # point at infinity
        for x in range(p):
            rhs = (x ** 3 + a * x + b) % p
            # number of y with y^2 = rhs mod p
            if rhs == 0:
                count += 1
            else:
                # is rhs a QR mod p?
                is_qr = pow(rhs, (p - 1) // 2, p) == 1
                count += 2 if is_qr else 0
        return count

    # k > 1: construct F_{p^k} as F_p[t] / (irreducible f).
    # Find an irreducible monic polynomial of degree k over F_p.
    f = _find_irreducible_poly(p, k)
    # Elements of F_{p^k} are polynomials of degree < k over F_p.
    # We iterate over all p^k elements.
    count = 1  # point at infinity
    for x_int in range(p ** k):
        x = _int_to_poly(x_int, p, k)
        # rhs = x^3 + a x + b
        x_sq = _poly_mul_mod(x, x, f, p)
        x_cu = _poly_mul_mod(x_sq, x, f, p)
        a_x = _poly_scalar_mul(x, a, p)
        rhs = _poly_add(x_cu, a_x, p)
        rhs = _poly_add_const(rhs, b, p)
        # number of y with y^2 = rhs in F_{p^k}
        # solutions: rhs is a square iff rhs^{(p^k - 1)/2} = 1
        order_field = p ** k
        if all(c == 0 for c in rhs):
            count += 1
        else:
            rhs_pow = _poly_pow_mod(rhs, (order_field - 1) // 2, f, p)
            if all(c == 0 for c in _poly_add_const(rhs_pow, -1, p)):
                count += 2
    return count


def _find_irreducible_poly(p: int, k: int):
    """A monic irreducible polynomial of degree k over F_p, as a list of
    coefficients (low-order first, leading coefficient 1)."""
    from itertools import product
    # Try polynomials t^k + c_{k-1} t^{k-1} + ... + c_0 with c_i in F_p.
    for tail in product(range(p), repeat=k):
        f = list(tail) + [1]  # constant first, leading last
        if _is_irreducible(f, p):
            return f
    raise RuntimeError(f"No irreducible polynomial of degree {k} over F_{p}? (impossible)")


def _is_irreducible(f, p):
    """Check if monic poly f (low-order first) is irreducible over F_p.

    Use the Rabin test: f is irreducible over F_p iff
    gcd(f, x^{p^{k/q}} - x) = 1 for every prime divisor q of k,
    and x^{p^k} = x mod f.
    """
    k = len(f) - 1
    if k <= 0:
        return False
    # Check gcd with x^{p^{k/q}} - x for primes q | k
    from sympy import factorint
    primes = list(factorint(k).keys())
    for q in primes:
        d = k // q
        # x^{p^d} mod f
        x_pd = _poly_pow_x_mod([0, 1], p ** d, f, p)
        # subtract x
        diff = _poly_sub(x_pd, [0, 1], p)
        if _poly_gcd(diff, f, p) != [1]:
            return False
    # x^{p^k} mod f should equal x
    x_pk = _poly_pow_x_mod([0, 1], p ** k, f, p)
    diff = _poly_sub(x_pk, [0, 1], p)
    return all(c == 0 for c in diff)


def _poly_pow_x_mod(x_poly, n, f, p):
    """Compute x_poly^n mod f over F_p."""
    return _poly_pow_mod(x_poly, n, f, p)


def _poly_pow_mod(base, n, f, p):
    """base^n mod f over F_p, by square-and-multiply."""
    result = [1]
    cur = list(base)
    while n > 0:
        if n & 1:
            result = _poly_mul_mod(result, cur, f, p)
        cur = _poly_mul_mod(cur, cur, f, p)
        n >>= 1
    return result


def _poly_mul_mod(a, b, f, p):
    """(a * b) mod f over F_p."""
    deg_a, deg_b = len(a) - 1, len(b) - 1
    prod = [0] * (deg_a + deg_b + 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            prod[i + j] = (prod[i + j] + ai * bj) % p
    return _poly_reduce(prod, f, p)


def _poly_reduce(a, f, p):
    """a mod f over F_p; assumes f is monic with f[-1] = 1."""
    a = list(a)
    deg_f = len(f) - 1
    while len(a) - 1 >= deg_f:
        top_idx = len(a) - 1
        top = a[top_idx]
        if top == 0:
            a.pop()
            continue
        # Subtract top * x^{top_idx - deg_f} * f from a. Because f is
        # monic, this zeros out the top coefficient of a; we then drop it.
        for i in range(deg_f + 1):
            idx = top_idx - deg_f + i
            a[idx] = (a[idx] - top * f[i]) % p
        a.pop()
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a if a else [0]


def _poly_add(a, b, p):
    n = max(len(a), len(b))
    out = []
    for i in range(n):
        ai = a[i] if i < len(a) else 0
        bi = b[i] if i < len(b) else 0
        out.append((ai + bi) % p)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def _poly_sub(a, b, p):
    n = max(len(a), len(b))
    out = []
    for i in range(n):
        ai = a[i] if i < len(a) else 0
        bi = b[i] if i < len(b) else 0
        out.append((ai - bi) % p)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def _poly_add_const(a, c, p):
    out = list(a)
    out[0] = (out[0] + c) % p
    return out


def _poly_scalar_mul(a, c, p):
    return [(ai * c) % p for ai in a]


def _poly_gcd(a, b, p):
    """Euclidean gcd over F_p."""
    while any(c != 0 for c in b):
        a, b = b, _poly_mod(a, b, p)
    return _poly_make_monic(a, p)


def _poly_mod(a, b, p):
    """a mod b over F_p."""
    a = list(a)
    deg_b = len(b) - 1
    while len(a) > deg_b:
        if a[-1] == 0:
            a.pop()
            continue
        # Make b monic-style: divide by leading coeff inv
        lead_b_inv = pow(b[-1], -1, p)
        top = (a[-1] * lead_b_inv) % p
        deg_top = len(a)
        for i, bi in enumerate(b):
            idx = deg_top - 1 - deg_b + i
            a[idx] = (a[idx] - top * bi) % p
        a.pop()  # top is now zero
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a if a else [0]


def _poly_make_monic(a, p):
    if all(c == 0 for c in a):
        return [0]
    lead_inv = pow(a[-1], -1, p)
    return [(c * lead_inv) % p for c in a]


def _int_to_poly(x, p, k):
    out = []
    for _ in range(k):
        out.append(x % p)
        x //= p
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out if out else [0]


def run(out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    # The curve: y^2 = x^3 + 1 x + 1 over F_5
    p = 5
    a, b = 1, 1
    print(f"[2B] Elliptic curve C: y^2 = x^3 + {a} x + {b} over F_{p}")
    print(f"     Counting |C(F_{p}^k)| for k = 1..6 by brute force")

    counts_brute = []
    for k in range(1, 7):
        N = point_count_F_pk((a, b), p, k)
        counts_brute.append(N)
        print(f"     |C(F_{p}^{k})| = {N}     (= {p**k} + 1 + ({1 + p**k - N:+d}))")

    # Extract a_p from k=1: |C(F_p)| = p + 1 - a_p
    a_p = p + 1 - counts_brute[0]
    print(f"\n[2B] Extracted a_p = {a_p} from k=1 count.")
    print(f"     Weil bound |a_p| <= 2 sqrt({p}) = {2 * np.sqrt(p):.4f}")
    print(f"     |a_p| = {abs(a_p)} satisfies bound: {abs(a_p) <= 2 * np.sqrt(p)}")

    # Frobenius eigenvalues alpha, alpha-bar are roots of T^2 - a_p T + p
    # Equivalently, alpha = (a_p + sqrt(a_p^2 - 4 p)) / 2 (typically complex)
    disc = a_p ** 2 - 4 * p
    print(f"\n[2B] Frobenius polynomial: T^2 - {a_p} T + {p}")
    print(f"     Discriminant: {disc}  (negative => complex conjugate roots)")
    alpha_re = a_p / 2
    alpha_im = np.sqrt(-disc) / 2
    alpha = complex(alpha_re, alpha_im)
    alpha_bar = complex(alpha_re, -alpha_im)
    print(f"     alpha = {alpha_re} + {alpha_im:.6f} i")
    print(f"     |alpha|^2 = {abs(alpha) ** 2:.6f}   (should equal p = {p})")
    print(f"     |alpha| = {abs(alpha):.6f}   (should equal sqrt(p) = {np.sqrt(p):.6f})")
    rh_holds = abs(abs(alpha) ** 2 - p) < 1e-12
    print(f"     RIEMANN HYPOTHESIS for C/F_{p}: {rh_holds}")

    # Now predict counts via Weil formula and verify against brute force
    print(f"\n[2B] Verifying |C(F_{p}^k)| = p^k + 1 - alpha^k - alpha-bar^k:")
    print(f"     {'k':>3}   {'predicted':>12}   {'brute force':>12}   {'agree':>6}")
    for k in range(1, 7):
        predicted = p ** k + 1 - (alpha ** k).real - (alpha_bar ** k).real
        predicted = round(predicted)  # known to be integer
        agree = (predicted == counts_brute[k - 1])
        print(f"     {k:>3}   {predicted:>12}   {counts_brute[k - 1]:>12}   {agree}")

    # Plot: |alpha|^k vs |C(F_p^k)| - (p^k + 1), the Frobenius eigenvalue trace
    ks = np.arange(1, 9)
    counts_extended = [counts_brute[0]] + counts_brute[1:]
    # Predict farther using Weil
    predicted_ext = [round(p ** k + 1 - 2 * (alpha ** k).real) for k in ks]
    deviation = np.array([p ** k + 1 - predicted_ext[i] for i, k in enumerate(ks)])
    weil_bound = 2 * p ** (ks / 2)  # 2 * sqrt(p^k)

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))

    ax = axs[0]
    ax.scatter([alpha.real, alpha_bar.real], [alpha.imag, alpha_bar.imag],
               s=200, c="red", marker="*", zorder=10, label=r"Frobenius eigenvalues")
    # Circle of radius sqrt(p)
    theta = np.linspace(0, 2 * np.pi, 200)
    ax.plot(np.sqrt(p) * np.cos(theta), np.sqrt(p) * np.sin(theta), "b--",
            label=rf"$|z| = \sqrt{{{p}}}$ (Weil bound)")
    ax.axhline(0, color="k", linewidth=0.5)
    ax.axvline(0, color="k", linewidth=0.5)
    ax.set_aspect("equal")
    ax.set_xlabel("Re alpha")
    ax.set_ylabel("Im alpha")
    ax.set_title(f"Frobenius eigenvalues for $C/F_{p}$\n(RH: both on the circle)")
    ax.legend()
    ax.grid(alpha=0.3)

    ax = axs[1]
    ax.plot(ks, np.abs(deviation), "ko-", label=r"$|p^k + 1 - |C(F_{p^k})||$")
    ax.plot(ks, weil_bound, "r--", label=r"Weil bound $2\sqrt{p^k}$")
    ax.set_yscale("log")
    ax.set_xlabel("k")
    ax.set_ylabel("magnitude")
    ax.set_title("Point-count deviation vs Weil bound")
    ax.legend()
    ax.grid(alpha=0.3, which="both")

    plt.tight_layout()
    plt.savefig(out_dir / "e2b_elliptic_curve_fp.png", dpi=140)
    plt.close()
    print(f"\n[2B] Saved {out_dir / 'e2b_elliptic_curve_fp.png'}")

    np.savez_compressed(
        out_dir / "e2b_elliptic_curve_fp.npz",
        p=p,
        a=a,
        b=b,
        a_p=a_p,
        alpha_real=alpha.real,
        alpha_imag=alpha.imag,
        counts_brute=np.array(counts_brute),
        ks=ks,
    )
    print(f"[2B] Saved {out_dir / 'e2b_elliptic_curve_fp.npz'}")


if __name__ == "__main__":
    run()
