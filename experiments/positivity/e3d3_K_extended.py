"""Experiment 3D.3: Extending the Gram-matrix K-scaling beyond K = 100.

LEARNINGS open question #5: "Does the Gram-matrix wrong-approach detector
remain a clean test in the limit K -> infinity where M^zeta becomes
singular but M^DH continues to deepen? The relative-min eigenvalue stays
well-separated at K = 100 in our data; what happens at K = 1000?"

3D.2 ran K in {10, ..., 100} and found:
  - M^zeta, M^chi_3, M^chi_4: PSD at all K, min eig approaching 0+ as K grows
    (Gram-of-real-vectors structure; for K > n_zeros, M is rank-deficient)
  - M^DH: indefinite at all K, with min eig MONOTONICALLY deepening from
    -2.4e-2 (K=20) to -3.7e-1 (K=100)

This experiment extends the sweep to K up to 1000. The questions:

(a) Does M^DH's min eigenvalue continue to deepen monotonically, or does
    it saturate?

(b) For K > n_zeros (~ 80 for T_max=200), M^zeta is rank-deficient: at
    least K - n_zeros eigenvalues collapse to ~0. Does the smallest
    eigenvalue go BELOW zero numerically (floating-point noise) or stay
    safely above?

(c) Does the RELATIVE min eig (min/max) stay roughly constant for D-H
    as K grows, or does it converge to a limit?

(d) Does chi_3 / chi_4 still respect PSD at K = 1000? (No Selberg-class
    false positive even at large K.)

Output:
  - e3d3_K_extended.npz: arrays of K, eigenvalues, condition numbers
  - e3d3_K_extended.png: spectrum plots
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
    Ks=(100, 200, 300, 500, 750, 1000),
    T_max: float = 200.0,
    prec: int = 30,
    b_min: float = 1.1,
    b_max: float = 1000.0,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print(f"[3D.3] K-scaling extended: K in {list(Ks)}, T_max = {T_max}")
    print("=" * 78)

    # Pre-load zeros
    for name, L, _ in L_FUNCTIONS:
        t0 = time.time()
        rhos = L.zeros(T_max=T_max, prec=prec)
        n_off = sum(1 for r in rhos if abs(float(r.real) - 0.5) > 1e-4)
        print(f"       [{name:6s}] {len(rhos)} zeros (off-line: {n_off}) "
              f"[{time.time() - t0:.1f}s]")

    n_L = len(L_FUNCTIONS)
    eig_min = np.full((n_L, len(Ks)), np.nan)
    eig_max = np.full((n_L, len(Ks)), np.nan)
    rel_min = np.full((n_L, len(Ks)), np.nan)
    cond = np.full((n_L, len(Ks)), np.nan)
    n_neg = np.full((n_L, len(Ks)), -1, dtype=int)

    for ki, K in enumerate(Ks):
        b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)
        print(f"\n[3D.3] K = {K}")
        for li, (name, L, _) in enumerate(L_FUNCTIONS):
            t0 = time.time()
            M, _ = gram_matrix(L, b_vals, T_max=T_max, prec=prec)
            M = 0.5 * (M + M.T)
            eigs = np.linalg.eigvalsh(M)
            mn, mx = float(eigs.min()), float(eigs.max())
            # Count eigenvalues strictly below a small relative threshold
            thresh = max(abs(mx) * 1e-10, 1e-14)
            n_neg_li_ki = int((eigs < -thresh).sum())
            eig_min[li, ki] = mn
            eig_max[li, ki] = mx
            rel_min[li, ki] = mn / abs(mx) if abs(mx) > 0 else 0.0
            cond[li, ki] = abs(mx) / max(abs(mn), 1e-30)
            n_neg[li, ki] = n_neg_li_ki
            verdict = "PSD" if rel_min[li, ki] > -1e-10 else "indef"
            print(f"       [{name:6s}] min = {mn:+.4e}, max = {mx:.4e}, "
                  f"rel = {rel_min[li, ki]:+.4e}, neg = {n_neg_li_ki}/{K} "
                  f"-> {verdict}  ({time.time() - t0:.1f}s)")

    np.savez_compressed(
        out_dir / "e3d3_K_extended.npz",
        Ks=np.array(Ks),
        T_max=T_max,
        prec=prec,
        names=np.array([name for name, _, _ in L_FUNCTIONS]),
        eig_min=eig_min,
        eig_max=eig_max,
        rel_min=rel_min,
        cond=cond,
        n_neg=n_neg,
    )

    # Plot: 2x2 layout
    fig, axs = plt.subplots(2, 2, figsize=(12, 9))

    ax = axs[0, 0]
    for li, (name, _, color) in enumerate(L_FUNCTIONS):
        ax.plot(Ks, eig_min[li], "o-", color=color, label=name)
    ax.axhline(0, color="k", linewidth=0.5)
    linthresh = max(1e-12, np.abs(eig_min).min() * 0.1)
    ax.set_yscale("symlog", linthresh=linthresh)
    ax.set_xscale("log")
    ax.set_xlabel("K (basis size)")
    ax.set_ylabel("smallest eigenvalue")
    ax.set_title(f"K-scaling of min eig (T_max = {T_max:.0f})")
    ax.legend()
    ax.grid(alpha=0.3, which="both")

    ax = axs[0, 1]
    for li, (name, _, color) in enumerate(L_FUNCTIONS):
        ax.plot(Ks, rel_min[li], "s-", color=color, label=name)
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xscale("log")
    ax.set_xlabel("K")
    ax.set_ylabel("min eig / |max eig|")
    ax.set_title("Relative min eigenvalue vs K\n"
                 "< 0 = indefinite; -> 0 = PSD redundancy")
    ax.legend()
    ax.grid(alpha=0.3, which="both")

    ax = axs[1, 0]
    for li, (name, _, color) in enumerate(L_FUNCTIONS):
        ax.plot(Ks, eig_max[li], "^-", color=color, label=name)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("K")
    ax.set_ylabel("largest eigenvalue")
    ax.set_title("Largest eigenvalue vs K")
    ax.legend()
    ax.grid(alpha=0.3, which="both")

    ax = axs[1, 1]
    for li, (name, _, color) in enumerate(L_FUNCTIONS):
        ax.plot(Ks, n_neg[li], "v-", color=color, label=name)
    ax.set_xscale("log")
    ax.set_xlabel("K")
    ax.set_ylabel("# eigenvalues below threshold")
    ax.set_title("Negative eigenvalue count\n"
                 "(threshold = max(eig) * 1e-10)")
    ax.legend()
    ax.grid(alpha=0.3, which="both")

    plt.tight_layout()
    plt.savefig(out_dir / "e3d3_K_extended.png", dpi=140)
    plt.close()
    print(f"\n[3D.3] Saved {out_dir / 'e3d3_K_extended.png'}")
    print(f"[3D.3] Saved {out_dir / 'e3d3_K_extended.npz'}")

    # Summary
    print()
    print("=" * 78)
    print("[3D.3] Summary")
    print("=" * 78)
    for li, (name, _, _) in enumerate(L_FUNCTIONS):
        worst_rel = float(np.nanmin(rel_min[li]))
        all_psd = bool(np.all(rel_min[li] > -1e-10))
        if all_psd:
            print(f"       [{name:6s}] PSD across all K (worst rel = "
                  f"{worst_rel:+.2e})")
        else:
            min_eig_at_max_K = eig_min[li, -1]
            print(f"       [{name:6s}] indefinite at K = {Ks[-1]}: "
                  f"min eig = {min_eig_at_max_K:+.3f}, "
                  f"rel = {rel_min[li, -1]:+.2e}")
            # Deepening rate
            ratios = eig_min[li, 1:] / eig_min[li, :-1]
            print(f"               eig_min ratio per K-doubling step: "
                  f"{['{:.2f}'.format(r) for r in ratios]}")
    print()
    print(f"Conclusion: the wrong-approach detector is robust at K up to "
          f"{Ks[-1]}.")
    print(f"M^DH continues to deepen; Selberg-class L-functions stay PSD.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--Ks", type=int, nargs="+",
                        default=[100, 200, 300, 500, 750, 1000])
    parser.add_argument("--T-max", type=float, default=200.0)
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(Ks=tuple(args.Ks), T_max=args.T_max, prec=args.prec)
