"""Experiment 3D: scaling of the Weil-positivity witness with basis size and T_max.

3C found that the Gram matrix M^DH has negative eigenvalue ~ -0.091 with
K = 30 basis vectors and T_max = 200. We ask:

  (1) Basis scaling: does the smallest eigenvalue get more negative as K
      grows (witness strengthens) or saturate (off-line zeros provide a
      bounded negativity budget)?

  (2) T_max scaling: as we add more zeros (more on-line, possibly more
      off-line), does the witness get sharper or wash out?

Both questions probe the structural robustness of the wrong-approach
detector. The expected behavior:

  - Basis K: the witness magnitude should saturate. The off-line zeros'
    contribution to the Gram matrix is bounded above by the number of
    off-line zeros times the maximum |Phi_b(rho)|^2 over the basis.
    Adding more basis directions can only redistribute existing
    negativity, not create new.

  - T_max: more on-line zeros add more positive Gram structure
    (real-vector Gram is PSD). More off-line zeros add MORE negative
    eigenvalue magnitude. Net effect depends on D-H's off-line zero
    density vs on-line.

Output:
  - e3d_scaling.npz: arrays of K, T_max sweeps; smallest eigenvalues
  - e3d_scaling.png: two-panel scaling plot
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
from experiments.positivity.e3c2_weil_gram import gram_matrix


def run(out_dir: Path = None, prec: int = 30):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    dh = DavenportHeilbronn()

    # Part 1: K-scaling at fixed T_max = 200
    Ks = [10, 20, 30, 50, 75, 100, 150]
    T_max_fixed = 200.0
    print(f"[3D.1] K scaling at T_max = {T_max_fixed}")
    eig_min_zeta_K = []
    eig_min_dh_K = []
    for K in Ks:
        b_vals = np.logspace(np.log10(1.1), np.log10(1000.0), K)
        t0 = time.time()
        M_zeta, _ = gram_matrix(zeta_L, b_vals, T_max=T_max_fixed, prec=prec)
        M_dh, _ = gram_matrix(dh, b_vals, T_max=T_max_fixed, prec=prec)
        M_zeta = 0.5 * (M_zeta + M_zeta.T)
        M_dh = 0.5 * (M_dh + M_dh.T)
        eig_z = float(np.linalg.eigvalsh(M_zeta).min())
        eig_d = float(np.linalg.eigvalsh(M_dh).min())
        eig_min_zeta_K.append(eig_z)
        eig_min_dh_K.append(eig_d)
        print(f"     K = {K:>3}: min eig zeta = {eig_z:+.4e}, "
              f"min eig D-H = {eig_d:+.4e}  ({time.time() - t0:.1f}s)")

    # Part 2: T_max scaling at fixed K = 30
    T_maxes = [50.0, 100.0, 150.0, 200.0, 300.0]
    K_fixed = 30
    print(f"[3D.2] T_max scaling at K = {K_fixed}")
    eig_min_zeta_T = []
    eig_min_dh_T = []
    for T in T_maxes:
        b_vals = np.logspace(np.log10(1.1), np.log10(1000.0), K_fixed)
        t0 = time.time()
        M_zeta, _ = gram_matrix(zeta_L, b_vals, T_max=T, prec=prec)
        M_dh, _ = gram_matrix(dh, b_vals, T_max=T, prec=prec)
        M_zeta = 0.5 * (M_zeta + M_zeta.T)
        M_dh = 0.5 * (M_dh + M_dh.T)
        eig_z = float(np.linalg.eigvalsh(M_zeta).min())
        eig_d = float(np.linalg.eigvalsh(M_dh).min())
        eig_min_zeta_T.append(eig_z)
        eig_min_dh_T.append(eig_d)
        n_off = sum(1 for r in dh.zeros(T_max=T, prec=prec)
                    if abs(float(r.real) - 0.5) > 1e-6)
        print(f"     T_max = {T:>5.0f}: min eig zeta = {eig_z:+.4e}, "
              f"min eig D-H = {eig_d:+.4e}, D-H off-line count = {n_off} "
              f"({time.time() - t0:.1f}s)")

    np.savez_compressed(
        out_dir / "e3d_scaling.npz",
        Ks=np.array(Ks),
        T_maxes=np.array(T_maxes),
        eig_min_zeta_K=np.array(eig_min_zeta_K),
        eig_min_dh_K=np.array(eig_min_dh_K),
        eig_min_zeta_T=np.array(eig_min_zeta_T),
        eig_min_dh_T=np.array(eig_min_dh_T),
        prec=prec,
    )

    fig, axs = plt.subplots(1, 2, figsize=(12, 4.5))

    ax = axs[0]
    ax.semilogx(Ks, eig_min_zeta_K, "bo-", label=r"$M^\zeta$")
    ax.semilogx(Ks, eig_min_dh_K, "ro-", label=r"$M^{DH}$")
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xlabel("K (basis size)")
    ax.set_ylabel(r"smallest eigenvalue")
    ax.set_title(f"K scaling (T_max = {T_max_fixed:.0f})")
    ax.legend()
    ax.grid(alpha=0.3, which="both")

    ax = axs[1]
    ax.plot(T_maxes, eig_min_zeta_T, "bo-", label=r"$M^\zeta$")
    ax.plot(T_maxes, eig_min_dh_T, "ro-", label=r"$M^{DH}$")
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xlabel(r"$T_{\max}$")
    ax.set_ylabel(r"smallest eigenvalue")
    ax.set_title(f"T_max scaling (K = {K_fixed})")
    ax.legend()
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e3d_scaling.png", dpi=140)
    plt.close()
    print(f"[3D] Saved {out_dir / 'e3d_scaling.png'}")
    print(f"[3D] Saved {out_dir / 'e3d_scaling.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(prec=args.prec)
