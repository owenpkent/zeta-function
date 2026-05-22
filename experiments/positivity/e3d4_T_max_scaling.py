"""Experiment 3D.4: T_max scaling — validates the "neg count = # off-line
gammas" structural prediction.

3D.3 found that for D-H at T_max = 200 (8 off-line zeros, 4 distinct
off-line gammas in UHP), the Gram-matrix detector has exactly 4 negative
eigenvalues, stable across K in [100, 1000]. The structural interpretation:
each off-line gamma (i.e., each "horizontal pair" (beta + i*gamma,
(1-beta) + i*gamma)) contributes exactly 1 negative eigenvalue.

This experiment tests the prediction by varying T_max. As T_max grows,
D-H accumulates more off-line zeros at higher heights. The prediction:
the number of negative eigenvalues in M^DH should track the number of
distinct off-line gammas below T_max.

Specifically, at T_max in {200, 300, 500, 800}, count distinct off-line
gammas and check that n_neg matches.

The relative min eigenvalue should also stay near -2.6% (the asymptotic
constant from 3D.3), since each off-line pair contributes a similar
amount of negative signal scaled by the matrix size.

Output:
  - e3d4_T_max_scaling.npz: T_max, # off-line gammas, n_neg, eigenvalues
  - e3d4_T_max_scaling.png: prediction vs measurement
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


def count_off_line_gammas(L, T_max: float, prec: int = 30,
                          gamma_round: int = 3):
    """Count distinct off-line gammas in the UHP up to height T_max.

    Off-line: |Re(rho) - 1/2| > 1e-4.
    Distinct gammas: round to gamma_round decimal places to merge near-equal.
    """
    rhos = L.zeros(T_max=T_max, prec=prec)
    off = [r for r in rhos if abs(float(r.real) - 0.5) > 1e-4]
    gammas = sorted(set(round(float(r.imag), gamma_round) for r in off))
    return len(gammas), gammas, len(rhos)


def run(
    T_maxs=(200.0, 300.0, 500.0, 800.0),
    K: int = 300,
    prec: int = 30,
    b_min: float = 1.1,
    b_max: float = 1000.0,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print(f"[3D.4] T_max scaling validation: n_neg = # off-line gammas?")
    print("=" * 78)
    print(f"  Fixed K = {K}, sweep T_max in {list(T_maxs)}")
    print()

    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)

    n_L = len(L_FUNCTIONS)
    n_T = len(T_maxs)
    n_off_gammas = np.full((n_L, n_T), -1, dtype=int)
    n_neg_eig = np.full((n_L, n_T), -1, dtype=int)
    rel_min_eig = np.full((n_L, n_T), np.nan)
    abs_min_eig = np.full((n_L, n_T), np.nan)
    abs_max_eig = np.full((n_L, n_T), np.nan)
    n_zeros_total = np.full((n_L, n_T), -1, dtype=int)

    for ti, T_max in enumerate(T_maxs):
        print(f"\n[3D.4] T_max = {T_max}")
        for li, (name, L, _) in enumerate(L_FUNCTIONS):
            t0 = time.time()

            n_g, gammas, n_total = count_off_line_gammas(L, T_max=T_max, prec=prec)
            n_off_gammas[li, ti] = n_g
            n_zeros_total[li, ti] = n_total

            M, _ = gram_matrix(L, b_vals, T_max=T_max, prec=prec)
            M = 0.5 * (M + M.T)
            eigs = np.linalg.eigvalsh(M)
            mn, mx = float(eigs.min()), float(eigs.max())
            thresh = max(abs(mx) * 1e-10, 1e-14)
            n_neg = int((eigs < -thresh).sum())
            rel = mn / abs(mx) if abs(mx) > 0 else 0
            n_neg_eig[li, ti] = n_neg
            abs_min_eig[li, ti] = mn
            abs_max_eig[li, ti] = mx
            rel_min_eig[li, ti] = rel
            dt = time.time() - t0

            match = "MATCH" if (n_neg == n_g) else "MISMATCH"
            verdict = "PSD" if rel > -1e-10 else "indef"
            print(f"       [{name:6s}] n_total={n_total:>4d}, "
                  f"off_gammas={n_g:>2d}, n_neg={n_neg:>3d} "
                  f"{('('+match+')' if name=='D-H' else ''):<11s} "
                  f"rel={rel:+.3e} -> {verdict}  ({dt:.1f}s)")

    np.savez_compressed(
        out_dir / "e3d4_T_max_scaling.npz",
        T_maxs=np.array(T_maxs),
        K=K,
        prec=prec,
        names=np.array([name for name, _, _ in L_FUNCTIONS]),
        n_zeros_total=n_zeros_total,
        n_off_gammas=n_off_gammas,
        n_neg_eig=n_neg_eig,
        abs_min_eig=abs_min_eig,
        abs_max_eig=abs_max_eig,
        rel_min_eig=rel_min_eig,
    )

    # Plot
    fig, axs = plt.subplots(1, 3, figsize=(15, 4.5))

    ax = axs[0]
    # Focus on D-H: prediction (off gammas) vs measurement (neg count)
    dh_idx = next(i for i, (name, _, _) in enumerate(L_FUNCTIONS) if name == "D-H")
    ax.plot(T_maxs, n_off_gammas[dh_idx], "o-", color="black",
            label="# off-line gammas (prediction)", markersize=8)
    ax.plot(T_maxs, n_neg_eig[dh_idx], "x-", color="red",
            label="# negative eigenvalues (measured)", markersize=12)
    ax.set_xlabel("T_max")
    ax.set_ylabel("count")
    ax.set_title("D-H: prediction vs measurement")
    ax.legend()
    ax.grid(alpha=0.3)
    ax.set_yticks(range(0, int(n_off_gammas[dh_idx].max()) + 2))

    ax = axs[1]
    for li, (name, _, color) in enumerate(L_FUNCTIONS):
        ax.plot(T_maxs, rel_min_eig[li], "s-", color=color, label=name)
    ax.axhline(0, color="k", linewidth=0.5)
    ax.axhline(-0.0262, color="purple", linestyle=":", alpha=0.5,
               label="3D.3 asymptote: -2.62%")
    ax.set_xlabel("T_max")
    ax.set_ylabel("min eig / |max eig|")
    ax.set_title("Relative min eigenvalue vs T_max")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    ax = axs[2]
    for li, (name, _, color) in enumerate(L_FUNCTIONS):
        ax.plot(T_maxs, n_neg_eig[li], "v-", color=color, label=name)
    ax.set_xlabel("T_max")
    ax.set_ylabel("# negative eigenvalues")
    ax.set_title("Negative eigenvalue count vs T_max")
    ax.legend()
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e3d4_T_max_scaling.png", dpi=140)
    plt.close()
    print(f"\n[3D.4] Saved {out_dir / 'e3d4_T_max_scaling.png'}")
    print(f"[3D.4] Saved {out_dir / 'e3d4_T_max_scaling.npz'}")

    # Summary
    print()
    print("=" * 78)
    print("[3D.4] Summary: testing the structural prediction n_neg = # off-line gammas")
    print("=" * 78)
    dh_idx = next(i for i, (name, _, _) in enumerate(L_FUNCTIONS) if name == "D-H")
    all_match = True
    for ti, T_max in enumerate(T_maxs):
        ng = n_off_gammas[dh_idx, ti]
        nn = n_neg_eig[dh_idx, ti]
        match = (ng == nn)
        all_match = all_match and match
        rel = rel_min_eig[dh_idx, ti]
        print(f"  T_max = {T_max:>6.0f}: off-gammas = {ng}, n_neg = {nn} "
              f"({'MATCH' if match else 'MISMATCH'}), rel min = {rel:+.3e}")
    print()
    if all_match:
        print(f"==> Prediction CONFIRMED across all tested T_max values.")
        print(f"    Each off-line gamma in D-H contributes exactly 1 negative")
        print(f"    eigenvalue to the Gram-matrix detector.")
    else:
        print(f"==> Prediction PARTIALLY CONFIRMED. Some T_max values show mismatch.")

    # Selberg-class consistency
    print()
    psd_all = True
    for li, (name, _, _) in enumerate(L_FUNCTIONS):
        if name == "D-H":
            continue
        worst_rel = float(np.min(rel_min_eig[li]))
        psd = bool(np.all(n_neg_eig[li] == 0))
        psd_all = psd_all and psd
        if not psd:
            print(f"  [{name}] has negative eigenvalues at some T_max")
        else:
            print(f"  [{name}] PSD at all T_max (worst rel = {worst_rel:+.2e})")
    if psd_all:
        print(f"==> All Selberg-class L-functions stay PSD across T_max sweep.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--T-maxs", type=float, nargs="+",
                        default=[200.0, 300.0, 350.0])
    parser.add_argument("--K", type=int, default=300)
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(T_maxs=tuple(args.T_maxs), K=args.K, prec=args.prec)
