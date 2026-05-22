"""Experiment 3H: Weil-form duality for chi_3 (the third data point).

3F found tight cancellation for zeta (Euler product, RH believed):
component magnitudes ~ 10^2, cancellation ratio ~ 10^{-3}.
3G found loose cancellation for D-H (no Euler product, RH false):
components ~ 10^0, cancellation ratio ~ 10^{-1}.

3H tests chi_3 (Dirichlet L-function, Euler product, GRH believed) to
disentangle which feature drives the cancellation:
  - Same Euler product structure as zeta -> tight cancellation predicted?
  - Or coefficient sign cancellation (chi_3(p) = +- 1) loosens it?

The Dirichlet coefficients of -L'(s,chi_3)/L(s,chi_3) are
    a_n = Lambda(n) chi_3(n),
which IS supported only on prime powers (Euler product), but the sign
depends on p mod 3. chi_3(p) = +1 for p == 1 (mod 3), -1 for p == 2
(mod 3), 0 for p = 3.

Prediction: partial sign cancellation in the prime sum because half the
primes have chi_3(p) = +1 and half have -1. So prime sum magnitude
smaller than zeta's by O(sqrt(N_primes)) due to oscillation. Cancellation
ratio intermediate between zeta and D-H.

Structurally:
  - chi_3 has Euler product => prime sum is on prime powers only
  - chi_3 has no pole at s=1 => no boundary terms f-tilde(0) + f-tilde(1)
  - Gamma factor for odd chi mod 3: (3/pi)^{(s+1)/2} Gamma((s+1)/2)
  - Psi_chi3(t) = log(3/pi) + Re psi(3/4 + i t/2)

Same Fourier form as 3G but with primes-only sum.

Output:
  - e3h_chi3_prime_side.npz, .png
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

from experiments._shared import chi3_L
from experiments.positivity.e3c_weil_form import phi_b


def chi3_value(p_int: int) -> int:
    """chi_3(n) = (1 if n=1 mod 3) - (1 if n=2 mod 3); 0 if 3 | n."""
    r = p_int % 3
    if r == 1:
        return 1
    elif r == 2:
        return -1
    return 0


def W_zero_side_chi3(b: float, T_max: float = 200.0, prec: int = 30):
    """W_chi3(b) from zero side, summing over upper-half-plane zeros."""
    mp.mp.dps = prec
    rhos = chi3_L.zeros(T_max=T_max, prec=prec)
    b_mp = mp.mpf(b)
    total = mp.mpf(0)
    for rho in rhos:
        phi_val = phi_b(b_mp, rho, prec=prec)
        total += 2 * (phi_val ** 2).real
    return total


def W_prime_side_chi3(b: float, prec: int = 50, T_int: float = 400.0):
    """Prime side for chi_3 via Fourier-form gamma kernel.

    W_chi3(b) = -2 sum_{p^k < b^2} (log p) chi_3(p^k) / p^{k/2} (2 log b - k log p)
              + (1/(2 pi)) int |Phi_b(1/2+it)|^2 [log(3/pi) + Re psi(3/4 + it/2)] dt

    No boundary terms (chi_3 has no pole). Same Psi structure as D-H but
    with conductor 3 instead of 5.
    """
    mp.mp.dps = prec
    b_mp = mp.mpf(b)
    log_b = mp.log(b_mp)
    b_sq = b_mp ** 2

    # Prime sum: -2 sum over p^k < b^2 of (log p) chi_3(p^k) / p^{k/2} (2 log b - k log p)
    prime_cutoff = int(float(b_sq)) + 1
    prime_sum = mp.mpf(0)
    for p in primerange(2, prime_cutoff + 1):
        chi_p = chi3_value(p)
        if chi_p == 0:
            continue
        log_p = mp.log(mp.mpf(p))
        k = 1
        chi_pk = chi_p  # chi_3(p^k) is chi_p^k for k >= 1
        while True:
            pk = mp.mpf(p) ** k
            if pk >= b_sq:
                break
            term = chi_pk * log_p * 2 * mp.power(pk, -mp.mpf("0.5")) * (2 * log_b - k * log_p)
            prime_sum += term
            k += 1
            chi_pk *= chi_p  # update chi_3(p^k)

    neg_prime = -prime_sum

    # Gamma integral with chi_3's Psi
    log_3_pi = mp.log(mp.mpf(3) / mp.pi)
    def integrand(t):
        if t == 0:
            phi_sq = (2 * log_b) ** 2
        else:
            phi_sq = (2 * mp.sin(t * log_b) / t) ** 2
        psi_val = mp.digamma(mp.mpc(mp.mpf("0.75"), t / 2))
        return phi_sq * (log_3_pi + psi_val.real)

    gamma_integral = 2 * mp.quad(integrand, [0, T_int]) / (2 * mp.pi)

    W_total = neg_prime + gamma_integral
    return W_total, neg_prime, gamma_integral


def run(
    n_b: int = 5,
    b_min: float = 6.0,
    b_max: float = 20.0,
    T_max_zero: float = 200.0,
    prec: int = 50,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), n_b)

    print(f"[3H] chi_3 Weil-form duality (Euler product, GRH believed)")
    print(f"     b in [{b_min}, {b_max}], T_max(zero) = {T_max_zero}, prec = {prec}")
    print()
    print(f"     {'b':>6s} {'W_zero':>12s} {'W_prime':>12s} "
          f"{'-prime':>12s} {'+gamma int':>12s} {'rel diff':>10s}")

    W_zero_arr = []
    W_prime_arr = []
    prime_arr = []
    gamma_arr = []

    for b in b_vals:
        t0 = time.time()
        W_zero = float(W_zero_side_chi3(b, T_max=T_max_zero, prec=prec))
        t_z = time.time() - t0
        t0 = time.time()
        W_prime, neg_p, gamma_int = W_prime_side_chi3(b, prec=prec)
        W_prime = float(W_prime)
        neg_p = float(neg_p)
        gamma_int = float(gamma_int)
        t_p = time.time() - t0

        rel_diff = (W_zero - W_prime) / max(abs(W_zero), 1e-12)

        W_zero_arr.append(W_zero)
        W_prime_arr.append(W_prime)
        prime_arr.append(neg_p)
        gamma_arr.append(gamma_int)

        print(f"     {b:>6.2f} {W_zero:>12.4e} {W_prime:>12.4e} "
              f"{neg_p:>+12.4e} {gamma_int:>+12.4e} "
              f"{rel_diff:>+10.2e}  (z {t_z:.1f}s p {t_p:.1f}s)")

    W_zero_arr = np.array(W_zero_arr)
    W_prime_arr = np.array(W_prime_arr)
    prime_arr = np.array(prime_arr)
    gamma_arr = np.array(gamma_arr)

    np.savez_compressed(
        out_dir / "e3h_chi3_prime_side.npz",
        b=b_vals,
        W_zero=W_zero_arr,
        W_prime=W_prime_arr,
        neg_prime=prime_arr,
        gamma_integral=gamma_arr,
        T_max_zero=T_max_zero,
    )

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))

    ax = axs[0]
    ax.semilogx(b_vals, W_zero_arr, "go-", label=r"$W_{\chi_3}$ from zero side", markersize=7)
    ax.semilogx(b_vals, W_prime_arr, "r.--", label=r"$W_{\chi_3}$ from prime side")
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xlabel("b")
    ax.set_ylabel(r"$W_{\chi_3}(b)$")
    ax.set_title(r"$\chi_3$ Weil form: Euler product, no pole")
    ax.legend()
    ax.grid(alpha=0.3, which="both")

    ax = axs[1]
    ax.semilogx(b_vals, prime_arr, "b-", marker="v",
                label=r"$-2\sum_{p^k<b^2}\frac{\log p\,\chi_3(p^k)}{p^{k/2}}(2\log b - k\log p)$")
    ax.semilogx(b_vals, gamma_arr, "r-", marker="^",
                label=r"gamma integral $\frac{1}{2\pi}\int|\Phi_b|^2[\log(3/\pi) + \mathrm{Re}\,\psi(3/4+it/2)]dt$")
    ax.semilogx(b_vals, W_prime_arr, "k:", linewidth=2, label="sum = W_prime")
    ax.semilogx(b_vals, W_zero_arr, "ks", markersize=5, label="W_zero (target)")
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xlabel("b")
    ax.set_ylabel("contribution")
    ax.set_title(r"$\chi_3$ prime-side decomposition")
    ax.legend(fontsize=7)
    ax.grid(alpha=0.3, which="both")

    plt.tight_layout()
    plt.savefig(out_dir / "e3h_chi3_prime_side.png", dpi=140)
    plt.close()
    print(f"\n[3H] Saved {out_dir / 'e3h_chi3_prime_side.png'}")
    print(f"     Saved {out_dir / 'e3h_chi3_prime_side.npz'}")

    # Cancellation analysis
    print()
    print(f"[3H] Cancellation analysis (chi_3, Euler product + sign oscillation):")
    print(f"     {'b':>6s} {'|prime|':>12s} {'|gamma|':>10s} "
          f"{'|W_prime|':>10s} {'|W_zero|':>10s} {'cancel ratio':>14s}")
    for i, b in enumerate(b_vals):
        ps = abs(prime_arr[i])
        gs = abs(gamma_arr[i])
        ws = abs(W_prime_arr[i])
        wz = abs(W_zero_arr[i])
        cancel = ws / max(ps, gs)
        print(f"     {b:>6.2f} {ps:>12.4e} {gs:>10.3e} "
              f"{ws:>10.3e} {wz:>10.3e} {cancel:>14.4e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-b", type=int, default=5)
    parser.add_argument("--b-min", type=float, default=6.0)
    parser.add_argument("--b-max", type=float, default=20.0)
    parser.add_argument("--T-max-zero", type=float, default=200.0)
    parser.add_argument("--prec", type=int, default=50)
    args = parser.parse_args()
    run(
        n_b=args.n_b,
        b_min=args.b_min,
        b_max=args.b_max,
        T_max_zero=args.T_max_zero,
        prec=args.prec,
    )
