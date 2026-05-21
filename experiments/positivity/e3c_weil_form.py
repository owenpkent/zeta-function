"""Experiment 3C: Weil-style quadratic form on Mellin-symmetric test functions.

Test family: Phi_b(s) = 2 sinh((s - 1/2) log b) / (s - 1/2).

Properties:
  - Phi_b(1 - s) = Phi_b(s) (symmetric under functional equation)
  - Phi_b(bar s) = conj(Phi_b(s)) for real b
  - On the critical line (s = 1/2 + i gamma):
        Phi_b(s) = 2 sin(gamma log b) / gamma   (real)
  - Off the critical line (s = beta + i gamma):
        Phi_b(s) is complex; Re(Phi_b(s)^2) can be positive or negative

Quadratic form:
    W(b) := sum_rho Phi_b(rho)^2
where the sum is over non-trivial zeros, each paired with its conjugate
(since rhos() returns upper-half-plane representatives).

  For zeta (RH): every zero rho has Phi_b(rho) real => Phi_b(rho)^2 >= 0.
                 So W(b) >= 0 automatically; zero of an architecture
                 is a NULL signal but a consistency check.

  For D-H: off-line zeros give complex Phi_b(rho). The contribution
           2 Re(Phi_b(rho)^2) can be negative, and the totalled W(b)
           can in principle go below the corresponding zeta value, or
           even below zero, for some b. This experiment searches for
           such a b.

Output:
  - e3c_weil_form.npz: arrays b, W_zeta(b), W_DH(b), W_DH - W_zeta
  - e3c_weil_form.png: 3-panel plot
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


def phi_b(b, s, prec: int = 30):
    """Phi_b(s) = 2 sinh((s - 1/2) log b) / (s - 1/2)."""
    mp.mp.dps = prec
    half = mp.mpf(1) / 2
    shift = s - half
    if abs(shift) < mp.mpf(10) ** (-prec + 5):
        return 2 * mp.log(b)  # limit as s -> 1/2
    return 2 * mp.sinh(shift * mp.log(b)) / shift


def weil_sum(L, b_vals, T_max: float = 200.0, prec: int = 30):
    """W(b) := sum_rho Phi_b(rho)^2, summed over zeros paired with conjugates.

    For an upper-half-plane zero rho, the conjugate bar(rho) is also a
    zero; together they contribute 2 * Re(Phi_b(rho)^2).
    """
    mp.mp.dps = prec
    rhos = L.zeros(T_max=T_max, prec=prec)
    is_offline = np.array([abs(float(r.real) - 0.5) > 1e-6 for r in rhos])

    W = np.zeros(len(b_vals))
    W_offline_part = np.zeros(len(b_vals))  # contribution from off-line zeros only

    for i, b in enumerate(b_vals):
        b_mp = mp.mpf(b)
        total = mp.mpf(0)
        offline_only = mp.mpf(0)
        for k, rho in enumerate(rhos):
            phi_val = phi_b(b_mp, rho, prec=prec)
            contribution = 2 * (phi_val ** 2).real  # rho + conjugate
            total += contribution
            if is_offline[k]:
                offline_only += contribution
        W[i] = float(total)
        W_offline_part[i] = float(offline_only)
    return W, W_offline_part, int(is_offline.sum())


def run(
    n_b: int = 50,
    b_min: float = 1.1,
    b_max: float = 100.0,
    T_max: float = 200.0,
    prec: int = 30,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), n_b)

    dh = DavenportHeilbronn()

    print(f"[3C] Loading zeros (T_max = {T_max}, prec = {prec})...")
    t0 = time.time()
    zeta_rhos = zeta_L.zeros(T_max=T_max, prec=prec)
    dh_rhos = dh.zeros(T_max=T_max, prec=prec, scan_step=0.5)
    print(f"     zeta: {len(zeta_rhos)} zeros, D-H: {len(dh_rhos)} zeros in {time.time() - t0:.1f}s")

    print(f"[3C] Computing W(b) for {n_b} values of b in [{b_min}, {b_max}]...")
    t0 = time.time()
    W_zeta, _, n_off_zeta = weil_sum(zeta_L, b_vals, T_max=T_max, prec=prec)
    W_dh, W_dh_off, n_off_dh = weil_sum(dh, b_vals, T_max=T_max, prec=prec)
    print(f"     done in {time.time() - t0:.1f}s")
    print(f"     zeta off-line zeros: {n_off_zeta}; D-H off-line zeros: {n_off_dh}")

    # Diagnostics
    zeta_neg = int((W_zeta < 0).sum())
    dh_neg = int((W_dh < 0).sum())
    dh_below_zeta = int((W_dh < W_zeta).sum())
    print(f"[3C] Positivity report:")
    print(f"     W_zeta(b) < 0 count: {zeta_neg} / {n_b}    (expect 0; sum of squares)")
    print(f"     W_DH(b) < 0 count:   {dh_neg} / {n_b}")
    print(f"     W_DH(b) < W_zeta(b) count: {dh_below_zeta} / {n_b}")
    if dh_neg > 0:
        idx = np.argmin(W_dh)
        print(f"     LOWEST W_DH: b = {b_vals[idx]:.4f}, W_DH = {W_dh[idx]:.6e}")
        if W_dh[idx] < 0:
            print(f"     WITNESS FOUND: W_DH(b={b_vals[idx]:.4f}) = {W_dh[idx]:.6e} < 0")
            print(f"     => Weil positivity violated for D-H at this b.")
            print(f"     => 3C diagnostic works as a wrong-approach detector.")

    # Offline-only contribution stats
    print(f"[3C] D-H off-line contribution range: "
          f"[{W_dh_off.min():.6e}, {W_dh_off.max():.6e}]")
    sign_changes = int(np.sum(np.diff(np.sign(W_dh_off)) != 0))
    print(f"     off-line contribution sign changes over b sweep: {sign_changes}")

    np.savez_compressed(
        out_dir / "e3c_weil_form.npz",
        b=b_vals,
        W_zeta=W_zeta,
        W_dh=W_dh,
        W_dh_offline=W_dh_off,
        T_max=T_max,
        prec=prec,
    )

    fig, axs = plt.subplots(1, 3, figsize=(15, 4.5))

    ax = axs[0]
    ax.semilogx(b_vals, W_zeta, "b-", label=r"$W_\zeta(b)$ (sum of squares)")
    ax.semilogx(b_vals, W_dh, "r-", label=r"$W_{DH}(b)$")
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xlabel("b")
    ax.set_ylabel(r"$W(b) = \sum_\rho \Phi_b(\rho)^2$")
    ax.set_title(f"Weil-style quadratic form\n(T_max={T_max:.0f})")
    ax.legend()
    ax.grid(alpha=0.3, which="both")

    ax = axs[1]
    diff = W_dh - W_zeta
    ax.semilogx(b_vals, diff, "g-")
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xlabel("b")
    ax.set_ylabel(r"$W_{DH}(b) - W_\zeta(b)$")
    ax.set_title("D-H excess over zeta\n(off-line zero signature)")
    ax.grid(alpha=0.3, which="both")

    ax = axs[2]
    ax.semilogx(b_vals, W_dh_off, "m-")
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xlabel("b")
    ax.set_ylabel(r"$W_{DH}^{\text{off-line zeros only}}(b)$")
    ax.set_title("Off-line zeros' contribution\n(sign can change with b)")
    ax.grid(alpha=0.3, which="both")

    plt.tight_layout()
    plt.savefig(out_dir / "e3c_weil_form.png", dpi=140)
    plt.close()
    print(f"[3C] Saved {out_dir / 'e3c_weil_form.png'}")
    print(f"[3C] Saved {out_dir / 'e3c_weil_form.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-b", type=int, default=50)
    parser.add_argument("--b-min", type=float, default=1.1)
    parser.add_argument("--b-max", type=float, default=100.0)
    parser.add_argument("--T-max", type=float, default=200.0)
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(
        n_b=args.n_b,
        b_min=args.b_min,
        b_max=args.b_max,
        T_max=args.T_max,
        prec=args.prec,
    )
