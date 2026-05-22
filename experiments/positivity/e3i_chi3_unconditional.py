"""Experiment 3I: Toward an unconditional Weil positivity for chi_3.

3H showed that chi_3's prime-side cancellation is "mild" (ratio ~4%) vs
zeta's "tight" (~0.1%). The conjectured path: if the chi_3 prime sum can
be bounded unconditionally (via Siegel-Walfisz / Page-style estimates,
which are weaker than full PNT-strength), the inequality

    -prime_sum_chi_3(b) + gamma_int_chi_3(b) >= 0  (Weil positivity)

might follow without using GRH for chi_3 as an input.

This experiment puts that idea under load:

  1. Compute prime_sum_chi_3(b) and gamma_int_chi_3(b) at b = 10, 15, 25,
     40, 65, 100. Plot the cancellation margin W = -prime_sum + gamma_int.

  2. Apply the strongest unconditional bound on psi(x, chi_3) =
     sum_{n <= x} Lambda(n) chi_3(n): the Page/Siegel-Walfisz bound
         |psi(x, chi_3)| <= C x exp(-c sqrt(log x))
     For chi_3 specifically (conductor 3), explicit constants exist in
     the literature (Trudgian, Schoenfeld). Use a representative value.

  3. Bound prime_sum_chi_3 in terms of psi(x, chi_3) via partial
     summation, then bound that via the Siegel-Walfisz estimate. Get
     an unconditional upper bound on |prime_sum_chi_3(b)|.

  4. Compare to the actual prime_sum and to gamma_int. Verdict: does
     the unconditional bound suffice to prove -prime_sum >= |gamma_int|
     (i.e., W >= 0) unconditionally?

We expect a NEGATIVE result: the bound likely won't be tight enough.
This would identify exactly where the gap lies (numerical constant gap
or fundamental scaling gap).

Background formulas:

  The boxcar prime sum:
    prime_sum_chi_3(b) = 2 sum_{p^k < b^2} (log p) chi_3(p^k) / p^{k/2} (2 log b - k log p)

  By partial summation (with phi(u) = (2 log b - log u)/sqrt(u)):
    prime_sum_chi_3 = 2 integral_2^{b^2} phi(u) d psi(u, chi_3)
                    = 2 [phi(b^2) psi(b^2, chi_3) - phi(2) psi(2, chi_3)
                         - integral_2^{b^2} psi(u, chi_3) phi'(u) du]

  At u = b^2: phi(b^2) = (2 log b - 2 log b)/b = 0, so boundary at top vanishes.
  At u = 2: phi(2) psi(2, chi_3) = (2 log b - log 2)/sqrt(2) * (-log 2)
            (since psi(2, chi_3) = Lambda(2) chi_3(2) = (log 2)(-1) = -log 2)

  phi'(u) = -(2 + 2 log b - log u) / (2 u^{3/2})

So:
    prime_sum_chi_3 = -2 (2 log b - log 2)/sqrt(2) * (-log 2)
                    + integral_2^{b^2} psi(u, chi_3) (2 + 2 log b - log u) / u^{3/2} du

  Bound via |psi(u, chi_3)| <= S(u) where S(u) is the Siegel-Walfisz bound:
    |prime_sum_chi_3| <= 2 (2 log b - log 2) log 2 / sqrt(2)
                      + integral_2^{b^2} S(u) (2 + 2 log b - log u) / u^{3/2} du

Output:
  - e3i_chi3_unconditional.npz: data
  - e3i_chi3_unconditional.png: actual vs bound vs gamma_int
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

from experiments.positivity.e3h_chi3_prime_side import (
    W_prime_side_chi3, chi3_value,
)
from experiments._shared import chi3_L
from experiments.positivity.e3c_weil_form import phi_b as phi_b_func


def psi_chi3_exact(x: float, prec: int = 50):
    """Exact psi(x, chi_3) = sum_{n <= x} Lambda(n) chi_3(n).
    Sums over prime powers up to x.
    """
    mp.mp.dps = prec
    total = mp.mpf(0)
    for p in primerange(2, int(x) + 1):
        chi_p = chi3_value(p)
        if chi_p == 0:
            continue
        log_p = mp.log(mp.mpf(p))
        k = 1
        chi_pk = chi_p
        while mp.mpf(p) ** k <= x:
            total += log_p * chi_pk
            k += 1
            chi_pk *= chi_p
    return total


def siegel_walfisz_bound(x: float, C: float = 5.0, c: float = 0.5):
    """Heuristic Siegel-Walfisz upper bound on |psi(x, chi)| for small conductor.

    |psi(x, chi_3)| <= C * x * exp(-c * sqrt(log x))

    Constants C, c are illustrative. The Page / Schoenfeld / Trudgian
    explicit results for q = 3 give effective bounds with specific
    constants. Trudgian's recent bounds: c ~ 0.05 - 0.1, C ~ a few
    for x >= some explicit threshold (e.g., 10^4). For small x we may
    have to use a different bound. This function uses C = 5, c = 0.5
    as a representative middle-of-the-road choice for the high-x regime.
    """
    if x < 2:
        return 0.0
    return C * x * np.exp(-c * np.sqrt(np.log(x)))


def integrand_for_bound(u, b, S_func):
    """The integrand of int psi(u, chi_3) (2 + 2 log b - log u) / u^{3/2} du,
    upper-bounded by S(u) (2 + 2 log b - log u) / u^{3/2}."""
    return S_func(u) * (2 + 2 * np.log(b) - np.log(u)) / u ** 1.5


def prime_sum_chi3_via_psi(b: float, n_quad: int = 5000, prec: int = 50,
                            S_func=None):
    """Bound |prime_sum_chi_3(b)| using partial summation against psi(x, chi_3) bounds.

    Returns:
      lower_actual: the BOUNDARY contribution to prime_sum (an exact value)
      bound_integral: the upper bound on the integral term (computed via numerical
                      quadrature against the S_func bound on |psi|)
      upper_bound_total: |prime_sum| upper bound
    """
    if S_func is None:
        S_func = siegel_walfisz_bound

    # Boundary contribution at u = 2:
    # prime_sum = -2 phi(2) psi(2, chi_3) + (integral term)
    # = -2 (2 log b - log 2)/sqrt(2) * (-log 2) + ...
    # = 2 log 2 (2 log b - log 2) / sqrt(2)
    boundary_contrib = 2 * np.log(2) * (2 * np.log(b) - np.log(2)) / np.sqrt(2)

    # Integral: int_2^{b^2} psi(u, chi_3) (2 + 2 log b - log u) / u^{3/2} du
    # We bound |psi(u, chi_3)| <= S(u), so integral magnitude <= int S(u) (2+2 log b - log u)/u^{3/2} du
    from scipy.integrate import quad
    integral_bound, _ = quad(
        lambda u: S_func(u) * (2 + 2 * np.log(b) - np.log(u)) / u ** 1.5,
        2, b ** 2, limit=200,
    )
    integral_bound = abs(integral_bound)

    # Triangle inequality: |prime_sum| <= |boundary| + |integral|
    total_upper = abs(boundary_contrib) + integral_bound

    return boundary_contrib, integral_bound, total_upper


def gamma_int_chi3(b: float, prec: int = 50, T_int: float = 400.0):
    """Compute the chi_3 gamma integral (Fourier form)."""
    mp.mp.dps = prec
    b_mp = mp.mpf(b)
    log_b = mp.log(b_mp)
    log_3_pi = mp.log(mp.mpf(3) / mp.pi)
    def integrand(t):
        if t == 0:
            phi_sq = (2 * log_b) ** 2
        else:
            phi_sq = (2 * mp.sin(t * log_b) / t) ** 2
        psi_val = mp.digamma(mp.mpc(mp.mpf("0.75"), t / 2))
        return phi_sq * (log_3_pi + psi_val.real)
    return float(2 * mp.quad(integrand, [0, T_int]) / (2 * mp.pi))


def actual_prime_sum_chi3(b: float, prec: int = 50):
    """Compute the actual prime_sum_chi_3(b) by direct summation."""
    mp.mp.dps = prec
    _, neg_prime, _ = W_prime_side_chi3(b, prec=prec)
    return -float(neg_prime)  # neg_prime = -prime_sum, so prime_sum = -neg_prime


def run(
    b_vals=(10.0, 15.0, 25.0, 40.0, 65.0, 100.0),
    prec: int = 50,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"[3I] Toward an unconditional Weil positivity bound for chi_3")
    print(f"     b values: {b_vals}, prec = {prec}")
    print()

    actual_prime = []
    actual_gamma = []
    actual_W = []
    bound_prime = []
    margins = []

    print(f"     {'b':>6s} {'prime_sum':>12s} {'gamma_int':>12s} {'W = sum':>12s} "
          f"{'|S-W bound|':>12s} {'enough?':>8s}")
    for b in b_vals:
        ps = actual_prime_sum_chi3(b, prec=prec)
        gi = gamma_int_chi3(b, prec=prec)
        W = -ps + gi  # W_prime side
        bnd, ib, total_bnd = prime_sum_chi3_via_psi(b)

        # Is |bound| <= -prime_sum? If so, the bound's WORST CASE doesn't break positivity.
        # We need -prime_sum >= |gamma_int| (in the boxcar's negative-prime-sum regime).
        # If we only know |prime_sum| <= total_bnd, then we know -prime_sum in [-total_bnd, total_bnd].
        # For positivity, we need -prime_sum >= |gamma_int|, which is guaranteed iff
        #   total_bnd <= |gamma_int| AND prime_sum < 0  (insufficient: total_bnd is only ABS bound)
        # OR we have a one-sided bound that locks the sign.
        #
        # Conservative test: is |total_bnd| <= |gamma_int|? If yes, then |prime_sum| < |gamma_int|
        # and the sign of W is set by gamma_int (which is negative). So W is negative — that's WRONG.
        # Actually, gamma_int < 0 always here (we computed it).
        # If prime_sum can be either sign with |prime_sum| < |gamma_int|, then W could be anything.
        # The "bound suffices" if we can prove prime_sum <= -|gamma_int| (negative enough). That's
        # a SIGNED lower bound, which Siegel-Walfisz alone can't give.

        # We report the absolute bound magnitude for now.
        actual_prime.append(ps)
        actual_gamma.append(gi)
        actual_W.append(W)
        bound_prime.append(total_bnd)

        # Margin: how much margin the actual prime_sum has over the boundary
        # condition -prime_sum >= |gamma_int|.
        # Required: -prime_sum >= |gamma_int|, i.e., prime_sum <= -|gamma_int|.
        # Margin = (-|gamma_int|) - prime_sum = -|gamma_int| - prime_sum
        # If margin >= 0, condition holds.
        margin = -abs(gi) - ps
        margins.append(margin)
        enough = "YES" if total_bnd <= abs(gi) else "NO"

        print(f"     {b:>6.1f} {ps:>+12.4e} {gi:>+12.4e} {W:>+12.4e} "
              f"{total_bnd:>12.4e} {enough:>8s}")

    actual_prime = np.array(actual_prime)
    actual_gamma = np.array(actual_gamma)
    actual_W = np.array(actual_W)
    bound_prime = np.array(bound_prime)
    margins = np.array(margins)
    b_arr = np.array(b_vals)

    print()
    print(f"[3I] Diagnosis:")
    if all(bound_prime <= abs(actual_gamma)):
        print(f"     S-W bound is tight enough to dominate gamma_int unconditionally.")
        print(f"     Implication: |prime_sum| < |gamma_int| guaranteed, so positivity")
        print(f"     would require prime_sum to be SIGNED appropriately (negative).")
        print(f"     This requires a signed bound, not just absolute Siegel-Walfisz.")
    else:
        ratios = bound_prime / np.abs(actual_gamma)
        print(f"     S-W bound is LOOSER than gamma_int. Ratio |bound| / |gamma_int|:")
        for i, b in enumerate(b_vals):
            print(f"       b = {b}: ratio = {ratios[i]:.2f} (need ratio <= 1 for bound to suffice)")
        print(f"     => The Siegel-Walfisz absolute bound is too weak. Either need")
        print(f"        a sharper bound (better constants, better dependence on x), or")
        print(f"        a signed bound on prime_sum that distinguishes sign from |sum|.")

    np.savez_compressed(
        out_dir / "e3i_chi3_unconditional.npz",
        b=b_arr,
        prime_sum=actual_prime,
        gamma_int=actual_gamma,
        W=actual_W,
        sw_bound=bound_prime,
        margins=margins,
    )

    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.plot(b_arr, np.abs(actual_prime), "bo-", label=r"$|$actual prime sum$|$")
    ax.plot(b_arr, np.abs(actual_gamma), "ro-", label=r"$|$gamma integral$|$")
    ax.plot(b_arr, bound_prime, "kx--", label=r"Siegel-Walfisz upper bound on $|$prime sum$|$")
    ax.plot(b_arr, np.abs(actual_W), "gs:", label=r"$|W|$ = $|$gap$|$")
    ax.set_xlabel("b")
    ax.set_ylabel("magnitude")
    ax.set_title(r"$\chi_3$ Weil-form: actual vs unconditional Siegel-Walfisz bound")
    ax.legend()
    ax.grid(alpha=0.3, which="both")
    ax.set_yscale("log")
    plt.tight_layout()
    plt.savefig(out_dir / "e3i_chi3_unconditional.png", dpi=140)
    plt.close()

    print()
    print(f"[3I] Saved {out_dir / 'e3i_chi3_unconditional.png'}")
    print(f"     Saved {out_dir / 'e3i_chi3_unconditional.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--b-vals", type=float, nargs="+",
                        default=[10.0, 15.0, 25.0, 40.0, 65.0, 100.0])
    parser.add_argument("--prec", type=int, default=50)
    args = parser.parse_args()
    run(b_vals=tuple(args.b_vals), prec=args.prec)
