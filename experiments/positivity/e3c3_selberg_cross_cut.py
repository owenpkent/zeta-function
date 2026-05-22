"""Experiment 3C3: Selberg-class cross-cut of the Gram-matrix detector.

We extend the [`e3c2_weil_gram`](e3c2_weil_gram.py) wrong-approach detector
across three L-functions:

  zeta              Selberg class, RH believed   (control: PSD expected)
  chi_3             Selberg class, GRH believed  (cross-cut: PSD expected)
  Davenport-Heilbronn   has FE, no Euler product, RH known false
                        (control: indefinite, witness expected)

The Gram matrix is M_{jk}(L) = sum_rho 2 Re(Phi_{b_j}(rho) Phi_{b_k}(rho))
for the test family Phi_b(s) = 2 sinh((s - 1/2) log b) / (s - 1/2).

When all zeros are on the critical line, Phi_b(rho) is real for every
zero, so M(L) is the Gram matrix of K real vectors in R^N (N = number
of zeros), hence PSD.

This experiment confirms M^chi3 is PSD. If it were not, the Gram-matrix
detector would be flagging a Selberg-class L-function as "wrong", which
would be a false positive and would invalidate the framework. (We expect
no such failure: GRH is believed for Dirichlet L-functions, the first
few hundred zeros are known on the critical line, so the construction
must be Gram-of-real-vectors.)

Why this matters:
  * Arch 3 thesis: the Weil quadratic form is a positivity *test* that
    distinguishes Selberg-class L-functions from non-Euler-product
    look-alikes.
  * If M^chi3 had a negative eigenvalue, the test would not distinguish
    them, and the diagnostic in e3c2 would just be detecting "small q"
    or some other accident rather than "no Euler product".
  * Confirming M^chi3 PSD is the natural completion of the e3c2
    witness: zeta and chi_3 (both Selberg) give PSD, D-H (non-Selberg)
    gives indefinite.

Output:
  - e3c3_selberg_cross_cut.npz: b grid + Gram matrices + spectra for
    zeta, chi_3, and D-H
  - e3c3_selberg_cross_cut.png: 2x3 plot: row 1 = Gram heatmaps,
    row 2 = sorted spectra
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from experiments._shared import zeta_L, DavenportHeilbronn, chi3_L
from experiments.positivity.e3c2_weil_gram import gram_matrix


def run(
    n_b: int = 30,
    b_min: float = 1.1,
    b_max: float = 1000.0,
    T_max: float = 200.0,
    prec: int = 30,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), n_b)
    dh = DavenportHeilbronn()

    print(f"[3C3] Selberg-class cross-cut: zeta vs chi_3 vs D-H")
    print(f"      basis size K = {n_b}, b in [{b_min:.2f}, {b_max:.0f}], T_max = {T_max}")

    print(f"      [zeta]    loading zeros and computing M^zeta...")
    t0 = time.time()
    M_zeta, _ = gram_matrix(zeta_L, b_vals, T_max=T_max, prec=prec)
    n_zeta = len(zeta_L.zeros(T_max=T_max, prec=prec))
    print(f"                {n_zeta} zeros, {time.time() - t0:.1f}s")

    print(f"      [chi_3]   loading zeros and computing M^chi3...")
    t0 = time.time()
    M_chi3, _ = gram_matrix(chi3_L, b_vals, T_max=T_max, prec=prec)
    n_chi3 = len(chi3_L.zeros(T_max=T_max, prec=prec))
    print(f"                {n_chi3} zeros, {time.time() - t0:.1f}s")

    print(f"      [D-H]     loading zeros and computing M^DH...")
    t0 = time.time()
    M_dh, _ = gram_matrix(dh, b_vals, T_max=T_max, prec=prec)
    n_dh = len(dh.zeros(T_max=T_max, prec=prec))
    print(f"                {n_dh} zeros, {time.time() - t0:.1f}s")

    # Symmetrize against rounding asymmetries
    M_zeta = 0.5 * (M_zeta + M_zeta.T)
    M_chi3 = 0.5 * (M_chi3 + M_chi3.T)
    M_dh = 0.5 * (M_dh + M_dh.T)

    eig_zeta = np.linalg.eigvalsh(M_zeta)
    eig_chi3 = np.linalg.eigvalsh(M_chi3)
    eig_dh = np.linalg.eigvalsh(M_dh)

    def report(name, eig):
        neg = int((eig < -1e-10 * abs(eig).max()).sum())
        scale = abs(eig).max()
        return (
            f"      [{name:8s}] min eig = {eig.min():.4e}   max = {eig.max():.4e}\n"
            f"                 strict-negative count: {neg} / {len(eig)}\n"
            f"                 relative min/max = {eig.min() / scale:+.4e}"
        )

    print()
    print(report("zeta", eig_zeta))
    print(report("chi_3", eig_chi3))
    print(report("D-H", eig_dh))

    # Key cross-cut question: chi_3 PSD?
    rel_min_chi3 = float(eig_chi3.min() / abs(eig_chi3).max())
    verdict_chi3 = "PSD" if rel_min_chi3 > -1e-10 else "INDEFINITE"
    print()
    print(f"[3C3] Verdict on M^chi3: {verdict_chi3}")
    if verdict_chi3 == "PSD":
        print(f"      Cross-cut confirmed: Gram-of-real-vectors structure holds")
        print(f"      for chi_3 (Selberg class, GRH believed).")
        print(f"      The detector's witness for D-H is not a false-positive")
        print(f"      against arbitrary L-functions: it specifically responds")
        print(f"      to off-line zeros (presence of which violates the Gram-of-")
        print(f"      real-vectors construction).")
    else:
        print(f"      ANOMALY: M^chi3 has a strict-negative eigenvalue at")
        print(f"      {rel_min_chi3:.4e} (relative). This would refute the")
        print(f"      framework or signal a numerical issue.")

    rel_min_dh = float(eig_dh.min() / abs(eig_dh).max())
    verdict_dh = "PSD" if rel_min_dh > -1e-10 else "INDEFINITE"
    print(f"[3C3] Verdict on M^DH (control): {verdict_dh}")
    if verdict_dh == "INDEFINITE":
        eigvals, eigvecs = np.linalg.eigh(M_dh)
        c_star = eigvecs[:, 0]
        W_dh_witness = float(c_star @ M_dh @ c_star)
        W_zeta_witness = float(c_star @ M_zeta @ c_star)
        W_chi3_witness = float(c_star @ M_chi3 @ c_star)
        print(f"      smallest-eigenvalue witness vector evaluated on all three:")
        print(f"        W_DH(c*)    = {W_dh_witness:+.6e}   (< 0, the witness)")
        print(f"        W_zeta(c*)  = {W_zeta_witness:+.6e}   (>= 0 expected)")
        print(f"        W_chi3(c*) = {W_chi3_witness:+.6e}   (>= 0 expected)")
        ok = W_dh_witness < 0 and W_zeta_witness >= -1e-10 and W_chi3_witness >= -1e-10
        if ok:
            print(f"      => The same c* that witnesses Weil-form failure on D-H")
            print(f"         is non-negative on BOTH zeta and chi_3. The detector")
            print(f"         is direction-selective, not L-function-blind.")

    np.savez_compressed(
        out_dir / "e3c3_selberg_cross_cut.npz",
        b=b_vals,
        M_zeta=M_zeta,
        M_chi3=M_chi3,
        M_dh=M_dh,
        eig_zeta=eig_zeta,
        eig_chi3=eig_chi3,
        eig_dh=eig_dh,
        T_max=T_max,
        prec=prec,
        n_zeros_zeta=n_zeta,
        n_zeros_chi3=n_chi3,
        n_zeros_dh=n_dh,
    )

    fig, axs = plt.subplots(2, 3, figsize=(15, 9))

    cmap = "RdBu_r"
    titles_row1 = [r"$M^\zeta_{jk}$", r"$M^{\chi_3}_{jk}$", r"$M^{DH}_{jk}$"]
    mats = [M_zeta, M_chi3, M_dh]
    for ax, M, title in zip(axs[0], mats, titles_row1):
        v = abs(M).max()
        im = ax.imshow(M, cmap=cmap, aspect="auto", vmin=-v, vmax=v)
        ax.set_title(title)
        ax.set_xlabel("k"); ax.set_ylabel("j")
        plt.colorbar(im, ax=ax, fraction=0.045)

    # Sorted spectra. All three on the same axes for direct comparison.
    ax = axs[1, 0]
    ax.plot(range(len(eig_zeta)), sorted(eig_zeta), "b.-", label=r"$M^\zeta$")
    ax.plot(range(len(eig_chi3)), sorted(eig_chi3), "g.-", label=r"$M^{\chi_3}$")
    ax.plot(range(len(eig_dh)), sorted(eig_dh), "r.-", label=r"$M^{DH}$")
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_yscale("symlog", linthresh=max(1e-6, abs(eig_dh).max() * 1e-10))
    ax.set_xlabel("sorted eigenvalue index")
    ax.set_ylabel("eigenvalue")
    ax.set_title("All three spectra\n(symlog y-axis)")
    ax.legend()
    ax.grid(alpha=0.3)

    # Zoom: lowest 5 eigenvalues only. Shows D-H going negative, Selberg-class staying >= 0.
    ax = axs[1, 1]
    k_low = min(8, n_b)
    ax.plot(range(k_low), sorted(eig_zeta)[:k_low], "bo-", label=r"$M^\zeta$")
    ax.plot(range(k_low), sorted(eig_chi3)[:k_low], "gs-", label=r"$M^{\chi_3}$")
    ax.plot(range(k_low), sorted(eig_dh)[:k_low], "r^-", label=r"$M^{DH}$")
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xlabel("sorted eigenvalue index")
    ax.set_ylabel("eigenvalue (linear)")
    ax.set_title(f"Lowest {k_low} eigenvalues\n(linear y-axis)")
    ax.legend()
    ax.grid(alpha=0.3)

    # Relative min: visualizes "how PSD" each is
    ax = axs[1, 2]
    labels = ["zeta", "chi_3", "D-H"]
    rel_mins = [
        float(eig_zeta.min() / abs(eig_zeta).max()),
        float(eig_chi3.min() / abs(eig_chi3).max()),
        float(eig_dh.min() / abs(eig_dh).max()),
    ]
    colors = ["b", "g", "r"]
    bars = ax.bar(labels, rel_mins, color=colors)
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_ylabel(r"min eig / |max eig|")
    ax.set_title("Relative spectral negativity\n(< 0 = indefinite)")
    ax.grid(alpha=0.3, axis="y")
    for bar, val in zip(bars, rel_mins):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            val,
            f"{val:+.2e}",
            ha="center",
            va="bottom" if val >= 0 else "top",
            fontsize=8,
        )

    plt.tight_layout()
    plt.savefig(out_dir / "e3c3_selberg_cross_cut.png", dpi=140)
    plt.close()
    print()
    print(f"[3C3] Saved {out_dir / 'e3c3_selberg_cross_cut.png'}")
    print(f"[3C3] Saved {out_dir / 'e3c3_selberg_cross_cut.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-b", type=int, default=30)
    parser.add_argument("--b-min", type=float, default=1.1)
    parser.add_argument("--b-max", type=float, default=1000.0)
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
