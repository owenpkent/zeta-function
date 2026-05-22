"""Experiment 3B.2: witness lambda_n^DH < 0 at large n via off-line correction.

3B established that small-n Li-positivity does not distinguish zeta from
D-H: lambda_n stays positive for both at n <= 300 because the first off-
line zero (rho ~ 0.808 + 85.7i) has |w| - 1 ~ 4.2e-5, so the off-line
contribution becomes order 1 only at n ~ 24,000 and dominates the
on-line asymptotic only at n ~ 320,000-350,000.

This experiment WITNESSES the negativity at large n. We avoid the
intractable T_max-to-infinity zero sum by using an exact decomposition:

    lambda_n^DH = lambda_n^DH,RH + sum_{off-line rho} (w_on(gamma)^n - w_off^n)

where:
  - lambda_n^DH,RH is what lambda_n^DH would be if all zeros were on the
    critical line. By the Riemann-von Mangoldt asymptotic for D-H
    (conductor q = 5, gamma factor for odd character mod 5):
        lambda_n^DH,RH ~ (n/2)(log(q n / (2 pi)) + gamma_E - 1)
                        + O(sqrt(n) log n)
    The leading-order term comes from on-line zeros at density
    (1/(2 pi)) log(q T / (2 pi)).

  - For each off-line zero rho_off with gamma > 0:
        w_off = 1 - 1/rho_off,   w_on(gamma) = 1 - 1/(1/2 + i gamma)
    The "missing on-line" zero at the same gamma is replaced by the
    off-line one; the contribution difference is exactly
        (1 - w_off^n) - (1 - w_on^n) = w_on^n - w_off^n.
    Summing over upper-half-plane off-line zeros (each paired with
    conjugate) gives 2 Re(w_on(gamma)^n - w_off^n).

For D-H, the off-line zeros come in quadruples {rho, 1-rho, conj(rho),
conj(1-rho)}. The one with beta < 1/2 (FE partner) has |w| > 1, giving
exponential growth |w|^n. The one with beta > 1/2 has |w| < 1, decaying.
The dominant signal is from the beta < 1/2 partners.

The known D-H off-line zeros up to T = 300 (5 quadruples) give the
dominant off-line correction. Higher off-line zeros have |w|-1 ~ 1/gamma^2,
so they're sub-dominant.

For lambda_n^DH to go negative:
    -2 Re(w_off^n) > lambda_n^DH,RH + 2 Re(w_on^n) + 4 (constant term)
which requires |w_off|^n > (n/4) log(qn/(2pi)) approximately.
For q = 5 and |w_off| = 1.0000421, this happens around n ~ 320,000.

Output:
  - e3b2_li_dh_extension.npz: lambda_n estimates at sweep n values
  - e3b2_li_dh_extension.png: lambda_n^DH and lambda_n^zeta vs n on log scale
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

from experiments._shared import zeta_L, DavenportHeilbronn


def li_RH_asymptotic(n, q=1):
    """Leading-order Riemann-von Mangoldt asymptotic for lambda_n.

    For an L-function with conductor q and on-line zero density
    rho(T) = (1/(2 pi)) log(q T / (2 pi)), the Li coefficient satisfies
        lambda_n ~ (n/2)(log(qn/(2 pi)) + gamma_E - 1) + O(sqrt(n) log n)
    in the leading-order Bombieri-Lagarias asymptotic.

    For zeta, q = 1.
    For D-H, q = 5 (odd character mod 5).
    """
    n = mp.mpf(n)
    q = mp.mpf(q)
    return (n / 2) * (mp.log(q * n / (2 * mp.pi)) + mp.euler - 1)


def offline_correction(n, offline_zeros, prec=50):
    """Off-line correction to lambda_n: sum 2 Re(w_on^n - w_off^n).

    For each off-line zero rho_off = beta + i*gamma in the upper half plane,
    paired with conjugate, the contribution to lambda_n above its
    "missing on-line" counterpart is
        2 Re((1 - 1/(1/2 + i gamma))^n - (1 - 1/rho_off)^n).

    Returns the total correction.
    """
    mp.mp.dps = prec
    n = mp.mpf(n)
    total = mp.mpf(0)
    for rho in offline_zeros:
        gamma = rho.imag
        rho_on = mp.mpc(mp.mpf(1) / 2, gamma)
        w_off = 1 - 1 / rho
        w_on = 1 - 1 / rho_on
        # paired with conjugate => 2 Re
        diff = w_on ** n - w_off ** n
        total += 2 * diff.real
    return total


def run(
    n_values=(1000, 10000, 50000, 100000, 200000, 320000, 400000, 500000, 1000000),
    T_max: float = 300.0,
    prec: int = 50,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    mp.mp.dps = prec

    dh = DavenportHeilbronn()
    print(f"[3B.2] Computing lambda_n^DH via on-line asymptotic + off-line correction")
    print(f"       T_max = {T_max}, precision = {prec} digits")

    print(f"[3B.2] Loading D-H zeros up to T = {T_max}...")
    t0 = time.time()
    dh_zeros = dh.zeros(T_max=T_max, prec=prec)
    print(f"       {len(dh_zeros)} D-H zeros in {time.time() - t0:.1f}s")

    offline = [z for z in dh_zeros if abs(float(z.real) - 0.5) > 1e-4]
    print(f"       {len(offline)} off-line zeros (upper half plane):")
    for z in offline:
        beta = float(z.real)
        gamma = float(z.imag)
        rho_on = mp.mpc(mp.mpf(1) / 2, mp.mpf(gamma))
        w_off = 1 - 1 / z
        w_on = 1 - 1 / rho_on
        log_grow_rate = float(mp.log(abs(w_off)))
        print(f"         rho = {beta:.4f} + {gamma:.4f} i, "
              f"|w_off| = {float(abs(w_off)):.10f}, log|w_off| = {log_grow_rate:+.4e}")

    print()
    print(f"[3B.2] Sweep over n:")
    print(f"       {'n':>10}  {'lambda_n^DH,RH':>15}  {'offline corr':>15}  "
          f"{'lambda_n^DH':>15}  {'sign':>6}  {'magnitude':>10}")
    results = []
    for n in n_values:
        t0 = time.time()
        lam_RH = li_RH_asymptotic(n, q=5)
        off_corr = offline_correction(n, offline, prec=prec)
        lam_DH = lam_RH + off_corr
        dt = time.time() - t0
        sign = "POSITIVE" if lam_DH > 0 else "NEGATIVE"
        magnitude = float(mp.log10(abs(lam_DH))) if abs(lam_DH) > 0 else float("-inf")
        results.append({
            "n": int(n),
            "lam_RH": float(lam_RH),
            "off_corr": float(off_corr),
            "lam_DH": float(lam_DH),
            "sign": sign,
        })
        print(f"       {n:>10}  {float(lam_RH):>15.4e}  {float(off_corr):>+15.4e}  "
              f"{float(lam_DH):>+15.4e}  {sign:>8s}  10^{magnitude:>5.2f}  ({dt:.1f}s)")

    # Also estimate zeta for comparison (no off-line zeros, so lam_n^zeta ~ lam_n^zeta,RH)
    print()
    print(f"[3B.2] For comparison, zeta (no off-line zeros): lambda_n^zeta ~ asymptotic")
    print(f"       {'n':>10}  {'lambda_n^zeta':>15}")
    for n in n_values:
        lam_zeta = li_RH_asymptotic(n, q=1)
        print(f"       {n:>10}  {float(lam_zeta):>15.4e}")

    # Save
    np.savez_compressed(
        out_dir / "e3b2_li_dh_extension.npz",
        n_values=np.array(n_values),
        lambda_RH=np.array([r["lam_RH"] for r in results]),
        offline_corr=np.array([r["off_corr"] for r in results]),
        lambda_DH=np.array([r["lam_DH"] for r in results]),
        T_max=T_max,
        prec=prec,
        n_offline_zeros=len(offline),
    )

    # Plot
    ns = np.array([r["n"] for r in results], dtype=float)
    lam_RH = np.array([r["lam_RH"] for r in results])
    off_corr = np.array([r["off_corr"] for r in results])
    lam_DH = np.array([r["lam_DH"] for r in results])
    lam_zeta = np.array([float(li_RH_asymptotic(n, q=1)) for n in ns])

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))

    ax = axs[0]
    ax.semilogx(ns, lam_zeta, "b-", label=r"$\lambda_n^\zeta$ (RH asymp., q=1)", marker="o")
    ax.semilogx(ns, lam_RH, "g-", label=r"$\lambda_n^{DH,RH}$ (asymp. with q=5)", marker="s")
    ax.semilogx(ns, lam_DH, "r-", label=r"$\lambda_n^{DH}$ (asymp. + off-line corr.)", marker="^", markersize=8)
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xlabel("n")
    ax.set_ylabel(r"$\lambda_n$")
    ax.set_title("Li coefficients: zeta vs D-H (RH asymp. + correction)")
    ax.legend()
    ax.grid(alpha=0.3, which="both")

    ax = axs[1]
    ax.semilogx(ns, lam_RH, "g-", label=r"$\lambda_n^{DH,RH}$ (asymp.)")
    ax.semilogx(ns, off_corr, "r-", label="off-line correction")
    ax.semilogx(ns, lam_DH, "k:", label=r"$\lambda_n^{DH} = $ sum", linewidth=2)
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xlabel("n")
    ax.set_ylabel(r"$\lambda_n$ components")
    ax.set_title("D-H: on-line asymp. vs off-line correction")
    ax.legend()
    ax.grid(alpha=0.3, which="both")
    # Use symlog on y for the right panel since off_corr can be negative or huge
    max_abs = max(abs(lam_RH).max(), abs(off_corr).max(), abs(lam_DH).max())
    ax.set_yscale("symlog", linthresh=max(1, max_abs * 1e-8))

    plt.tight_layout()
    plt.savefig(out_dir / "e3b2_li_dh_extension.png", dpi=140)
    plt.close()
    print(f"\n[3B.2] Saved {out_dir / 'e3b2_li_dh_extension.png'}")
    print(f"[3B.2] Saved {out_dir / 'e3b2_li_dh_extension.npz'}")

    # Negativity report
    print()
    print(f"[3B.2] Negativity report:")
    negative_ns = [r["n"] for r in results if r["lam_DH"] < 0]
    if negative_ns:
        print(f"       lambda_n^DH < 0 found at n in {negative_ns}")
        print(f"       => Witnesses D-H violation of Li positivity. RH for D-H is")
        print(f"          known false; this is the n at which the Li criterion")
        print(f"          DIRECTLY exhibits the violation.")
    else:
        print(f"       lambda_n^DH > 0 at all tested n.")
        print(f"       The off-line correction oscillates; we may have hit unfavorable")
        print(f"       phases of the cos(n arg(w_off)) factor.")
        # Estimate when |w_off|^n > lambda_n^DH,RH/2
        # which would be the crossover for ANY phase.
        if offline:
            log_w_off_max = max(float(mp.log(abs(1 - 1/z))) for z in offline if abs(1 - 1/z) > 1)
            for n in range(100000, 2000000, 50000):
                w_pow = mp.exp(log_w_off_max * n)
                lam_asymp = li_RH_asymptotic(n, q=5)
                if w_pow > lam_asymp / 2:
                    print(f"       Generic crossover (|w_off|^n > asymp/2) at n ~ {n}")
                    break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-values", type=int, nargs="+",
                        default=[1000, 10000, 50000, 100000, 200000, 320000, 400000, 500000, 1000000])
    parser.add_argument("--T-max", type=float, default=300.0)
    parser.add_argument("--prec", type=int, default=50)
    args = parser.parse_args()
    run(n_values=tuple(args.n_values), T_max=args.T_max, prec=args.prec)
