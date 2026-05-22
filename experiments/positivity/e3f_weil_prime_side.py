"""Experiment 3F: Weil quadratic form via the prime side.

3C-3D computed the Weil quadratic form W(b) = sum_rho Phi_b(rho)^2 by
summing over zeros. The explicit formula gives the same quantity as a
sum involving primes and a gamma integral:

    W(b) = (boundary terms at s=0, 1)
         - 2 sum_{p^k < b^2} (log p / p^{k/2}) (2 log b - k log p)
         + (gamma integral over critical line)

This experiment computes BOTH sides for the same b values and verifies
numerical agreement (modulo truncation errors). The point is not just
to verify the explicit formula (we know it's true) but to:

  1. Calibrate a dual perspective: every zero-side quantity has a
     prime-side equivalent. The Weil positivity criterion in
     prime-side form is a STATEMENT ABOUT PRIMES that, if proved
     analytically without RH inputs, would prove RH.

  2. Expose the cancellation structure: the gamma integral is large
     positive, the prime sum is large negative, and the boundary is
     small. Weil positivity = the gamma integral dominates the
     (negated) prime sum. Numerical study of HOW MUCH cancellation
     occurs informs the structural difficulty of an analytic proof.

  3. Provide a sanity check on the previous Weil-form computations:
     if the prime side disagrees with the zero side, something is
     off in either computation.

For our boxcar test family f_b(u) = 1_{[-log b, log b]}(u), the
autocorrelation (f_b * f_b)(v) = max(0, 2 log b - |v|) is a tent
function, giving the clean prime sum above.

Derivation sketch: the Weil-Riesel-Guinand explicit formula for zeta
states
    sum_rho f-hat(gamma_rho) = (boundary) + (gamma int.) - 2 sum (Lambda(n)/sqrt(n)) f(log n)
for f a Schwartz test function on R with f-hat its Fourier transform.
Applied to f_b * f_b (whose Fourier transform is |f-hat_b|^2 = Phi_b^2
on the critical line), this gives sum_rho |Phi_b(rho)|^2 in terms of
the prime-side data.

The gamma integral involves Re psi(1/4 + i t / 2) where psi = Gamma'/Gamma.

Output:
  - e3f_weil_prime_side.npz: per-b zero-side, prime-side breakdown
  - e3f_weil_prime_side.png: agreement plot + cancellation visualization
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
from sympy import primerange

from experiments._shared import zeta_L
from experiments.positivity.e3c_weil_form import phi_b


def W_zero_side(b: float, T_max: float = 200.0, prec: int = 30):
    """Zero-side computation: W(b) = sum_rho 2 Re(Phi_b(rho)^2) over
    upper-half-plane non-trivial zeros (paired with conjugates).

    For zeta with RH, Phi_b is real on the critical line, so this
    equals 2 sum_{gamma > 0} Phi_b(1/2 + i gamma)^2.
    """
    mp.mp.dps = prec
    rhos = zeta_L.zeros(T_max=T_max, prec=prec)
    b_mp = mp.mpf(b)
    total = mp.mpf(0)
    for rho in rhos:
        phi_val = phi_b(b_mp, rho, prec=prec)
        # rho + conjugate gives 2 Re(Phi^2). For Phi real on critical
        # line, this is 2 Phi^2.
        total += 2 * (phi_val ** 2).real
    return total


def W_prime_side(b: float, prec: int = 30, gamma_cap: float = None):
    """Prime-side computation via Bombieri's form of the Weil explicit formula.

    Following Bombieri (Clay millennium write-up, page 8):
    For f in the test class W with Mellin transform f-tilde(s),

        f-tilde(0) - sum_rho f-tilde(rho) + f-tilde(1) =
            sum_n Lambda(n) {f(n) + f(1/n)/n}
            + (log 4 pi + gamma_E) f(1)
            + integral_1^inf {f(x) + f(1/x)/x - 2 f(1)/x} dx / (x - 1/x).

    For our boxcar g_b(x) = x^{-1/2} 1_{[1/b, b]}(x), the autocorrelation
        f(x) = integral_0^inf g_b(x y) g_b(y) dy
    has Mellin transform f-tilde(s) = Phi_b(s)^2 (since Phi_b = Mellin of
    g_b is FE-symmetric). So sum_rho f-tilde(rho) = W(b).

    The explicit f:
        f(x) = x^{-1/2} max(0, 2 log b - |log x|) for x in [1/b^2, b^2],
        0 elsewhere.
    Then f(1) = 2 log b.

    Solving for W(b):
        W(b) = Phi_b(0)^2 + Phi_b(1)^2
             - sum_n Lambda(n) {f(n) + f(1/n)/n}
             - (log 4 pi + gamma_E) * 2 log b
             - gamma_integral

    Returns (W_total, boundary, neg_prime_sum, neg_const, neg_gamma_int).
    """
    mp.mp.dps = prec
    b_mp = mp.mpf(b)
    log_b = mp.log(b_mp)
    b_sq = b_mp ** 2

    # Boundary
    boundary = 8 * (mp.sqrt(b_mp) - 1 / mp.sqrt(b_mp)) ** 2

    # Prime sum: f(n) + f(1/n)/n = 2 n^{-1/2} max(0, 2 log b - log n).
    # See derivation:
    #   f(n)   = n^{-1/2} (2 log b - log n)_+
    #   f(1/n) = n^{+1/2} (2 log b - log n)_+
    #   f(1/n)/n = n^{-1/2} (2 log b - log n)_+
    #   sum   = 2 n^{-1/2} (2 log b - log n)_+
    # Lambda(p^k) = log p; non-zero for p^k < b^2.
    prime_cutoff = int(float(b_sq)) + 1
    primes = list(primerange(2, prime_cutoff + 1))
    prime_sum = mp.mpf(0)
    for p in primes:
        log_p = mp.log(mp.mpf(p))
        k = 1
        while True:
            pk = mp.mpf(p) ** k
            if pk >= b_sq:
                break
            term = log_p * 2 * mp.power(pk, -mp.mpf("0.5")) * (2 * log_b - k * log_p)
            prime_sum += term
            k += 1

    neg_prime_sum = -prime_sum

    # Constant: -(log 4 pi + gamma_E) * f(1)
    const_factor = mp.log(4 * mp.pi) + mp.euler
    neg_const = -const_factor * 2 * log_b

    # Gamma integral: integral_1^inf {f(x) + f(1/x)/x - 2 f(1)/x} dx/(x - 1/x).
    # Integrand inside [1, b^2]: 2 x^{-1/2} (2 log b - log x) - 4 log b / x,
    # all divided by x - 1/x.
    # Past x = b^2: integrand = -4 log b / x divided by x - 1/x.
    # At x=1: 0/0; limit is log b - 1 (computed analytically).
    # The integral is convergent; tail decays like 1/x^2 at infinity.

    def integrand(x):
        if x == 1:
            return log_b - 1
        u = mp.log(x)
        if u < 2 * log_b:
            fx_term = 2 * mp.power(x, -mp.mpf("0.5")) * (2 * log_b - u)
        else:
            fx_term = mp.mpf(0)
        f1_term = 4 * log_b / x
        numerator = fx_term - f1_term
        denominator = x - 1 / x
        return numerator / denominator

    # Integrate from 1 to b^2 (interior) and b^2 to infinity (tail).
    # The integrand decays as 1/x^2 at infinity, so cap at b^4 (very safe).
    if gamma_cap is None:
        gamma_cap = float(b_sq) * 10
    gamma_inner = mp.quad(integrand, [1, b_sq])
    gamma_tail = mp.quad(integrand, [b_sq, gamma_cap])
    gamma_integral = gamma_inner + gamma_tail
    neg_gamma_int = -gamma_integral

    W_total = boundary + neg_prime_sum + neg_const + neg_gamma_int
    return W_total, boundary, neg_prime_sum, neg_const, neg_gamma_int


def run(
    n_b: int = 12,
    b_min: float = 1.5,
    b_max: float = 30.0,
    T_max_zero: float = 500.0,
    prec: int = 30,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), n_b)

    print(f"[3F] Weil quadratic form: zero side vs prime side (Bombieri's form)")
    print(f"     b in [{b_min}, {b_max}], n_b = {n_b}, T_max(zero) = {T_max_zero}, prec = {prec}")
    print()

    print(f"     {'b':>6s} {'W_zero':>12s} {'W_prime':>12s} "
          f"{'boundary':>10s} {'-prime':>12s} {'-const':>10s} {'-gamma_int':>12s} "
          f"{'rel diff':>10s}")

    W_zero_arr = []
    W_prime_arr = []
    boundary_arr = []
    prime_arr = []
    const_arr = []
    gamma_arr = []

    for b in b_vals:
        t0 = time.time()
        W_zero = float(W_zero_side(b, T_max=T_max_zero, prec=prec))
        t_z = time.time() - t0
        t0 = time.time()
        W_prime, boundary, neg_prime, neg_const, neg_gamma = W_prime_side(b, prec=prec)
        W_prime = float(W_prime)
        boundary = float(boundary)
        neg_prime = float(neg_prime)
        neg_const = float(neg_const)
        neg_gamma = float(neg_gamma)
        t_p = time.time() - t0

        rel_diff = (W_zero - W_prime) / max(abs(W_zero), 1e-12)

        W_zero_arr.append(W_zero)
        W_prime_arr.append(W_prime)
        boundary_arr.append(boundary)
        prime_arr.append(neg_prime)
        const_arr.append(neg_const)
        gamma_arr.append(neg_gamma)

        print(f"     {b:>6.2f} {W_zero:>12.4e} {W_prime:>12.4e} "
              f"{boundary:>10.3e} {neg_prime:>+12.4e} {neg_const:>+10.3e} {neg_gamma:>+12.4e} "
              f"{rel_diff:>+10.2e}  (z {t_z:.1f}s p {t_p:.1f}s)")

    W_zero_arr = np.array(W_zero_arr)
    W_prime_arr = np.array(W_prime_arr)
    boundary_arr = np.array(boundary_arr)
    prime_arr = np.array(prime_arr)
    const_arr = np.array(const_arr)
    gamma_arr = np.array(gamma_arr)

    np.savez_compressed(
        out_dir / "e3f_weil_prime_side.npz",
        b=b_vals,
        W_zero=W_zero_arr,
        W_prime=W_prime_arr,
        boundary=boundary_arr,
        neg_prime=prime_arr,
        neg_const=const_arr,
        neg_gamma_int=gamma_arr,
        T_max_zero=T_max_zero,
    )

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))

    ax = axs[0]
    ax.semilogx(b_vals, W_zero_arr, "ko-", label="W from zero side", markersize=7)
    ax.semilogx(b_vals, W_prime_arr, "r.--", label="W from prime side")
    ax.set_xlabel("b")
    ax.set_ylabel("W(b)")
    ax.set_title("Weil form: zero side vs prime side\n(Bombieri's explicit formula)")
    ax.legend()
    ax.grid(alpha=0.3, which="both")

    ax = axs[1]
    ax.semilogx(b_vals, boundary_arr, "g-", label=r"boundary $8(b^{1/2}-b^{-1/2})^2$", marker="s")
    ax.semilogx(b_vals, prime_arr, "b-", label=r"$-2\sum \log p / p^{k/2} (2\log b - k\log p)$", marker="v")
    ax.semilogx(b_vals, const_arr, "m-", label=r"$-(\log 4\pi + \gamma_E) \cdot 2\log b$", marker="d")
    ax.semilogx(b_vals, gamma_arr, "r-", label=r"$-\int_1^\infty\{f+f(1/x)/x-2f(1)/x\}dx/(x-1/x)$", marker="^")
    ax.semilogx(b_vals, W_prime_arr, "k:", label="sum = W", linewidth=2)
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xlabel("b")
    ax.set_ylabel("contribution")
    ax.set_title("Prime-side decomposition (Bombieri's form)")
    ax.legend(fontsize=7)
    ax.grid(alpha=0.3, which="both")

    plt.tight_layout()
    plt.savefig(out_dir / "e3f_weil_prime_side.png", dpi=140)
    plt.close()

    # Cancellation analysis
    print()
    print(f"[3F] Cancellation analysis:")
    print(f"     {'b':>8s}  {'gamma/|prime|':>14s}  {'(gamma + prime)/W':>20s}  {'agreement':>10s}")
    for i, b in enumerate(b_vals):
        ratio_cancel = gamma_arr[i] / abs(prime_arr[i]) if abs(prime_arr[i]) > 0 else float("inf")
        residual_frac = (gamma_arr[i] + prime_arr[i]) / W_prime_arr[i] if abs(W_prime_arr[i]) > 0 else 0
        rel_diff = abs(W_zero_arr[i] - W_prime_arr[i]) / max(abs(W_zero_arr[i]), 1e-12)
        agreement_marker = "AGREE" if rel_diff < 0.05 else "DISAGREE"
        print(f"     {b:>8.3f}  {ratio_cancel:>14.4f}  {residual_frac:>20.4f}  {agreement_marker:>10s}")

    print()
    print(f"[3F] Saved {out_dir / 'e3f_weil_prime_side.png'}")
    print(f"     Saved {out_dir / 'e3f_weil_prime_side.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-b", type=int, default=12)
    parser.add_argument("--b-min", type=float, default=1.5)
    parser.add_argument("--b-max", type=float, default=30.0)
    parser.add_argument("--T-max-zero", type=float, default=500.0)
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(
        n_b=args.n_b,
        b_min=args.b_min,
        b_max=args.b_max,
        T_max_zero=args.T_max_zero,
        prec=args.prec,
    )
