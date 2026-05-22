"""Experiment 3D.2: K-scaling of the Gram-matrix detector across L-functions.

3D found that as the basis size K grows, M^DH's smallest eigenvalue gets
MORE negative (witness deepens), while M^zeta's smallest eigenvalue
trends to 0+ from above (Gram-of-real-vectors structure preserved; the
Phi_b family spans a rank-bounded subspace so larger K just adds
near-redundant directions). 3C3 added chi_3 as a single-K positive
control.

This experiment is the K-scaling analogue of 3C3: it runs the same
K sweep as 3D but across all four L-functions
    {zeta, chi_3, chi_4, D-H}
and asks: do chi_3 and chi_4 track zeta as K grows (both staying
PSD with smallest eigenvalue trending to 0+), or do they at some K
develop a strict-negative eigenvalue that the framework would have
to interpret as a "false positive"?

If chi_3 and chi_4 stay PSD at all K we test, the Selberg-class
cross-cut is robust: the wrong-approach signal really is responding
to off-line zeros and not to L-function specifics. If they go
indefinite at high K, that would either expose numerical-noise
limits of the test or, in the worst case, undermine the framework.

Output:
  - e3d2_cross_cut_scaling.npz: arrays of K, smallest eigenvalues for
    each L-function, basic L-function metadata
  - e3d2_cross_cut_scaling.png: 2-panel plot
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from experiments._shared import zeta_L, DavenportHeilbronn, chi3_L, chi4_L
from experiments.positivity.e3c2_weil_gram import gram_matrix


L_FUNCTIONS = [
    ("zeta", zeta_L, "C0"),
    ("chi_3", chi3_L, "C2"),
    ("chi_4", chi4_L, "C1"),
    ("D-H", DavenportHeilbronn(), "C3"),
]


def run(
    Ks=(10, 20, 30, 50, 75, 100),
    T_max: float = 200.0,
    prec: int = 30,
    b_min: float = 1.1,
    b_max: float = 1000.0,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"[3D.2] K-scaling cross-cut over {[name for name, _, _ in L_FUNCTIONS]}")
    print(f"       T_max = {T_max}, K in {list(Ks)}")

    # Pre-load zeros (warms cache once per L-function)
    for name, L, _ in L_FUNCTIONS:
        t0 = time.time()
        rhos = L.zeros(T_max=T_max, prec=prec)
        n_off = sum(1 for r in rhos if abs(float(r.real) - 0.5) > 1e-4)
        print(f"       [{name:6s}] {len(rhos)} zeros (off-line: {n_off}) [{time.time() - t0:.1f}s]")

    # K sweep
    n_L = len(L_FUNCTIONS)
    eig_min = np.full((n_L, len(Ks)), np.nan)
    eig_max = np.full((n_L, len(Ks)), np.nan)
    rel_min = np.full((n_L, len(Ks)), np.nan)

    for ki, K in enumerate(Ks):
        b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)
        print(f"\n[3D.2] K = {K}")
        for li, (name, L, _) in enumerate(L_FUNCTIONS):
            t0 = time.time()
            M, _ = gram_matrix(L, b_vals, T_max=T_max, prec=prec)
            M = 0.5 * (M + M.T)
            eigs = np.linalg.eigvalsh(M)
            mn, mx = float(eigs.min()), float(eigs.max())
            eig_min[li, ki] = mn
            eig_max[li, ki] = mx
            rel_min[li, ki] = mn / abs(mx) if abs(mx) > 0 else 0.0
            verdict = "PSD" if rel_min[li, ki] > -1e-10 else "indef"
            print(f"       [{name:6s}] min = {mn:+.4e}, max = {mx:.4e}, "
                  f"rel = {rel_min[li, ki]:+.4e} -> {verdict}  ({time.time() - t0:.1f}s)")

    # Save
    np.savez_compressed(
        out_dir / "e3d2_cross_cut_scaling.npz",
        Ks=np.array(Ks),
        T_max=T_max,
        prec=prec,
        names=np.array([name for name, _, _ in L_FUNCTIONS]),
        eig_min=eig_min,
        eig_max=eig_max,
        rel_min=rel_min,
    )

    # Plot
    fig, axs = plt.subplots(1, 2, figsize=(12, 4.8))

    # Panel 1: absolute smallest eigenvalue vs K, symlog
    ax = axs[0]
    for li, (name, _, color) in enumerate(L_FUNCTIONS):
        ax.plot(Ks, eig_min[li], "o-", color=color, label=name)
    ax.axhline(0, color="k", linewidth=0.5)
    linthresh = max(1e-12, np.abs(eig_min).min() * 0.1)
    ax.set_yscale("symlog", linthresh=linthresh)
    ax.set_xscale("log")
    ax.set_xlabel("K (basis size)")
    ax.set_ylabel("smallest eigenvalue")
    ax.set_title(f"K-scaling of min eig (T_max = {T_max:.0f})\n"
                 f"symlog y, zero line marked")
    ax.legend()
    ax.grid(alpha=0.3, which="both")

    # Panel 2: relative min (eig_min / |eig_max|) vs K, linear
    ax = axs[1]
    for li, (name, _, color) in enumerate(L_FUNCTIONS):
        ax.plot(Ks, rel_min[li], "s-", color=color, label=name)
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xscale("log")
    ax.set_xlabel("K (basis size)")
    ax.set_ylabel("min eig / |max eig|")
    ax.set_title(f"Relative min eigenvalue vs K\n"
                 f"< 0 = indefinite; -> 0+ = Gram redundancy")
    ax.legend()
    ax.grid(alpha=0.3, which="both")

    plt.tight_layout()
    plt.savefig(out_dir / "e3d2_cross_cut_scaling.png", dpi=140)
    plt.close()
    print(f"\n[3D.2] Saved {out_dir / 'e3d2_cross_cut_scaling.png'}")
    print(f"[3D.2] Saved {out_dir / 'e3d2_cross_cut_scaling.npz'}")

    # Summary verdict
    print()
    print(f"[3D.2] Summary:")
    for li, (name, _, _) in enumerate(L_FUNCTIONS):
        worst_rel = float(np.nanmin(rel_min[li]))
        verdict = "PSD across all K" if worst_rel > -1e-10 else f"indefinite at some K (worst rel = {worst_rel:+.2e})"
        print(f"       [{name:6s}] {verdict}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--Ks", type=int, nargs="+", default=[10, 20, 30, 50, 75, 100])
    parser.add_argument("--T-max", type=float, default=200.0)
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(Ks=tuple(args.Ks), T_max=args.T_max, prec=args.prec)
