"""Experiment 3G: Weil-form duality for Davenport-Heilbronn.

3F established the Weil-form duality for zeta: W(b) computed from the
zero side agrees with the prime side via Bombieri's explicit formula
to <2% at sufficient T_max. The cancellation structure (boundary ~ 144,
prime sum ~ -120, constant ~ -19, gamma int ~ -5, summing to ~0.1 at
b=20) is what makes an analytic proof of Weil positivity hard.

This experiment tests the cancellation structure for D-H, which has NO
EULER PRODUCT. The Weil explicit formula generalizes, with two key
differences from zeta:

  (a) The "prime sum" Sum_p Sum_k Lambda(p^k)/p^{k/2} (...) is replaced
      by a "Dirichlet sum" Sum_n b_n^{DH}/sqrt(n) (...) over ALL n,
      with coefficients b_n^{DH} determined by the Dirichlet series of
      -f'_DH / f_DH (s). These b_n live on all n, not just prime powers,
      and they're irrational combinations of log p that can be positive
      or negative.

  (b) D-H has NO POLE (it's entire), so the boundary terms f-tilde(0) +
      f-tilde(1) that came from zeta's pole at s = 1 are ABSENT. The
      formula becomes
          W_DH(b) = - 2 Sum_n b_n^{DH}/sqrt(n) (2 log b - log n)_+
                   - C_DH * 2 log b
                   - I_DH(b)
      where C_DH and I_DH come from the D-H gamma factor (odd character
      mod 5: Gamma((s+1)/2) (5/pi)^{(s+1)/2}).

The b_n^{DH} satisfy the recursion (from -f'/f = (sum c_n log n / n^s)
divided by (sum c_n / n^s)):
    sum_{d | n} b_d^{DH} c_{n/d} = c_n log n,
where c_n is the D-H periodic-mod-5 Dirichlet coefficient with one
period (c_1, c_2, c_3, c_4, c_5) = (1, kappa, -kappa, -1, 0).

Computing b_n^{DH} recursively for n = 1, ..., N is straightforward.

The constant C_DH for the boundary contribution and the gamma integral
I_DH come from -2 d/ds [log gamma_DH(s)] at s=1, where gamma_DH(s) =
(5/pi)^{(s+1)/2} Gamma((s+1)/2) is D-H's gamma factor. Working out:
    C_DH = -(log(5/pi) - gamma_E) = gamma_E + log(pi/5).
(Detailed derivation in the section below.)

The gamma integral I_DH(b) is analogous to Bombieri's for zeta but with
psi((s+1)/2) instead of psi(s/2) (different gamma factor argument).

The KEY QUESTION: does the cancellation we saw for zeta (4 large terms
summing to small) hold for D-H, or does the absence of Euler product
break it?

If cancellation survives: the cancellation is generic, not Euler-product
specific. The route from Weil positivity to RH goes through something
other than the Euler product.

If cancellation breaks (e.g., the b_n^{DH} sum is much larger than
boundary + constants + gamma): the cancellation is specifically a
feature of Euler-product L-functions, and that's the structural
mechanism by which RH would be proved.

Output:
  - e3g_dh_prime_side.npz: b_n coefficients, decomposition components
  - e3g_dh_prime_side.png: cancellation visualization
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

from experiments._shared import DavenportHeilbronn
from experiments.positivity.e3c_weil_form import phi_b


def kappa_DH(prec: int = 50):
    """The Davenport-Heilbronn kappa constant."""
    prev = mp.mp.dps
    mp.mp.dps = max(prec, prev)
    try:
        sqrt5 = mp.sqrt(5)
        return (mp.sqrt(10 - 2 * sqrt5) - 2) / (sqrt5 - 1)
    finally:
        mp.mp.dps = prev


def dh_dirichlet_coeff(n: int, kappa) -> mp.mpf:
    """The n-th Dirichlet coefficient c_n of f_DH (periodic mod 5)."""
    period = [mp.mpf(1), kappa, -kappa, mp.mpf(-1), mp.mpf(0)]
    return period[(n - 1) % 5]


def compute_bn_dh(N: int, prec: int = 50):
    """Compute b_n^{DH} for n = 1, ..., N via the recursion
        sum_{d | n} b_d c_{n/d} = c_n log n
    with c_1 = 1, so b_n = c_n log n - sum_{d|n, d<n} b_d c_{n/d}.
    """
    mp.mp.dps = prec
    kappa = kappa_DH(prec)
    c = [dh_dirichlet_coeff(n, kappa) for n in range(N + 1)]  # c[0] unused; c[1..N]
    b = [mp.mpf(0)] * (N + 1)
    b[1] = mp.mpf(0)  # log 1 = 0
    for n in range(2, N + 1):
        # b[n] = c[n] log n - sum_{d | n, d < n, d >= 1} b[d] c[n/d]
        s = c[n] * mp.log(mp.mpf(n))
        # subtract sum over proper divisors d of n
        for d in range(1, n):
            if n % d == 0:
                s -= b[d] * c[n // d]
        b[n] = s
    return b


def W_zero_side_DH(b: float, T_max: float = 200.0, prec: int = 30):
    """W_DH(b) from zero side: sum over all non-trivial zeros (on + off line)
    paired with conjugates. For each upper-half-plane zero rho:
        contribution = 2 Re(Phi_b(rho)^2).
    On-line zeros: Phi_b(rho) is real, 2 Phi_b^2.
    Off-line zeros: contribution is 2 Re of a complex square."""
    mp.mp.dps = prec
    dh = DavenportHeilbronn()
    rhos = dh.zeros(T_max=T_max, prec=prec)
    b_mp = mp.mpf(b)
    total = mp.mpf(0)
    for rho in rhos:
        phi_val = phi_b(b_mp, rho, prec=prec)
        total += 2 * (phi_val ** 2).real
    return total


def W_prime_side_DH(b: float, N_dirichlet: int = None, prec: int = 50,
                    T_int: float = 400.0):
    """Prime-side analog for D-H using the Fourier (digamma) form.

    W_DH(b) = -2 sum_{n=2}^{b^2-1} b_n^{DH}/sqrt(n) (2 log b - log n)
              + (1/(2 pi)) int_{-infty}^{infty} |Phi_b(1/2+it)|^2 Psi_DH(t) dt

    where Psi_DH(t) = log(5/pi) + Re psi(3/4 + i t/2). This is the
    natural generalization of Wikipedia's Ψ_zeta(t) = -log pi + Re psi(1/4 + it/2)
    to D-H's gamma factor (5/pi)^{(s+1)/2} Gamma((s+1)/2):
        Psi_L(t) = 2 Re(d/ds log gamma_L(1/2 + i t))
    For zeta:  Psi_zeta = 2 Re(-(log pi)/2 + (1/2) psi(1/4 + i t/2))
                       = -log pi + Re psi(1/4 + i t/2)   (Wikipedia)
    For D-H:   Psi_DH   = 2 Re((1/2) log(5/pi) + (1/2) psi(3/4 + i t/2))
                       = log(5/pi) + Re psi(3/4 + i t/2)

    No boundary terms (D-H has no pole; entire completed L-function).

    Returns (W_total, neg_dirichlet, gamma_int).
    """
    mp.mp.dps = prec
    b_mp = mp.mpf(b)
    log_b = mp.log(b_mp)
    b_sq = b_mp ** 2

    if N_dirichlet is None:
        N_dirichlet = int(float(b_sq)) + 1

    b_coeffs = compute_bn_dh(N_dirichlet, prec=prec)

    # Dirichlet sum: -2 sum b_n/sqrt(n) (2 log b - log n) for n < b^2
    dirichlet_sum = mp.mpf(0)
    for n in range(2, N_dirichlet + 1):
        if mp.mpf(n) >= b_sq:
            break
        term = b_coeffs[n] * 2 * mp.power(mp.mpf(n), -mp.mpf("0.5")) * (2 * log_b - mp.log(mp.mpf(n)))
        dirichlet_sum += term

    neg_dirichlet = -dirichlet_sum

    # Gamma integral (Fourier form, D-H gamma factor):
    # gamma_int = (1/(2 pi)) int |Phi_b(1/2+it)|^2 [log(5/pi) + Re psi(3/4 + it/2)] dt
    # Integrand is even in t (since psi has conjugation symmetry and |Phi_b|^2 is even).
    log_5_pi = mp.log(mp.mpf(5) / mp.pi)
    def integrand(t):
        if t == 0:
            phi_sq = (2 * log_b) ** 2
        else:
            phi_sq = (2 * mp.sin(t * log_b) / t) ** 2
        psi_val = mp.digamma(mp.mpc(mp.mpf("0.75"), t / 2))
        return phi_sq * (log_5_pi + psi_val.real)

    gamma_integral = 2 * mp.quad(integrand, [0, T_int]) / (2 * mp.pi)

    W_total = neg_dirichlet + gamma_integral
    return W_total, neg_dirichlet, gamma_integral


def run(
    n_b: int = 6,
    b_min: float = 5.0,
    b_max: float = 20.0,
    T_max_zero: float = 300.0,
    prec: int = 50,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), n_b)

    print(f"[3G] Weil-form duality for Davenport-Heilbronn")
    print(f"     b in [{b_min}, {b_max}], n_b = {n_b}, T_max(zero) = {T_max_zero}, prec = {prec}")
    print(f"     b_n^DH supported on ALL n (no Euler product; no Lambda structure)")
    print()

    # Display first few b_n^DH values for orientation
    b_first = compute_bn_dh(20, prec=prec)
    print(f"     First 12 b_n^DH coefficients:")
    for n in range(1, 13):
        print(f"       b_{n} = {float(b_first[n]):>+10.6f}")
    print()

    print(f"     {'b':>6s} {'W_zero':>12s} {'W_prime':>12s} "
          f"{'-D sum':>12s} {'+gamma int':>12s} "
          f"{'rel diff':>10s}")

    W_zero_arr = []
    W_prime_arr = []
    dirichlet_arr = []
    gamma_arr = []

    for b in b_vals:
        t0 = time.time()
        W_zero = float(W_zero_side_DH(b, T_max=T_max_zero, prec=prec))
        t_z = time.time() - t0
        t0 = time.time()
        W_prime, neg_d, gamma_int = W_prime_side_DH(b, prec=prec)
        W_prime = float(W_prime)
        neg_d = float(neg_d)
        gamma_int = float(gamma_int)
        t_p = time.time() - t0

        rel_diff = (W_zero - W_prime) / max(abs(W_zero), 1e-12)

        W_zero_arr.append(W_zero)
        W_prime_arr.append(W_prime)
        dirichlet_arr.append(neg_d)
        gamma_arr.append(gamma_int)

        print(f"     {b:>6.2f} {W_zero:>12.4e} {W_prime:>12.4e} "
              f"{neg_d:>+12.4e} {gamma_int:>+12.4e} "
              f"{rel_diff:>+10.2e}  (z {t_z:.1f}s p {t_p:.1f}s)")

    W_zero_arr = np.array(W_zero_arr)
    W_prime_arr = np.array(W_prime_arr)
    dirichlet_arr = np.array(dirichlet_arr)
    gamma_arr = np.array(gamma_arr)

    np.savez_compressed(
        out_dir / "e3g_dh_prime_side.npz",
        b=b_vals,
        W_zero=W_zero_arr,
        W_prime=W_prime_arr,
        neg_dirichlet=dirichlet_arr,
        gamma_integral=gamma_arr,
        T_max_zero=T_max_zero,
        b_n_first_20=np.array([float(b_first[n]) for n in range(20)]),
    )

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))

    ax = axs[0]
    ax.semilogx(b_vals, W_zero_arr, "ko-", label="W_DH from zero side", markersize=7)
    ax.semilogx(b_vals, W_prime_arr, "r.--", label="W_DH from prime side (Fourier form)")
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xlabel("b")
    ax.set_ylabel(r"$W_{DH}(b)$")
    ax.set_title("D-H Weil form: zero side vs prime side (no Euler product)")
    ax.legend()
    ax.grid(alpha=0.3, which="both")

    ax = axs[1]
    ax.semilogx(b_vals, dirichlet_arr, "b-", label=r"$-2\sum b_n^{DH}/\sqrt{n}(2\log b - \log n)$", marker="v")
    ax.semilogx(b_vals, gamma_arr, "r-", label=r"gamma integral $\frac{1}{2\pi}\int |\Phi_b|^2 \Psi_{DH}(t) dt$", marker="^")
    ax.semilogx(b_vals, W_prime_arr, "k:", label="sum = W_prime", linewidth=2)
    ax.semilogx(b_vals, W_zero_arr, "ks", label="W_zero (target)", markersize=5)
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xlabel("b")
    ax.set_ylabel("contribution")
    ax.set_title("D-H prime-side decomposition (Fourier form)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")

    plt.tight_layout()
    plt.savefig(out_dir / "e3g_dh_prime_side.png", dpi=140)
    plt.close()
    print(f"\n[3G] Saved {out_dir / 'e3g_dh_prime_side.png'}")
    print(f"     Saved {out_dir / 'e3g_dh_prime_side.npz'}")

    # Cancellation analysis
    print()
    print(f"[3G] Cancellation analysis (D-H, NO Euler product):")
    print(f"     {'b':>6s} {'|D sum|':>12s} {'|gamma|':>10s} "
          f"{'|W_prime|':>10s} {'|W_zero|':>10s} {'cancel ratio':>14s}")
    for i, b in enumerate(b_vals):
        ds = abs(dirichlet_arr[i])
        gs = abs(gamma_arr[i])
        ws = abs(W_prime_arr[i])
        wz = abs(W_zero_arr[i])
        cancel = ws / max(ds, gs)  # ratio of result to largest single term
        print(f"     {b:>6.2f} {ds:>12.4e} {gs:>10.3e} "
              f"{ws:>10.3e} {wz:>10.3e} {cancel:>14.4e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-b", type=int, default=6)
    parser.add_argument("--b-min", type=float, default=5.0)
    parser.add_argument("--b-max", type=float, default=20.0)
    parser.add_argument("--T-max-zero", type=float, default=300.0)
    parser.add_argument("--prec", type=int, default=50)
    args = parser.parse_args()
    run(
        n_b=args.n_b,
        b_min=args.b_min,
        b_max=args.b_max,
        T_max_zero=args.T_max_zero,
        prec=args.prec,
    )
