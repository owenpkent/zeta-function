"""Experiment 1C: L-function discrimination test for spectral constructions.

1A and 1B both noted in passing that their Hamiltonians have no L-function
input, so the same spectrum is being "compared to" zeta gammas and to D-H
gammas with no mechanism to prefer one over the other. 1C makes this
quantitative.

For each H matrix from 1A (three boundary conditions) and 1B (three
Sierra-Townsend variants, fixed coupling a = 1), we:

  (i)  diagonalize and extract the lowest-N positive eigenvalues
  (ii) fit a best AFFINE map E -> alpha E + beta to minimize RMS deviation
       from the first N zeta gammas (least-squares)
  (iii) apply the SAME affine map to compare against D-H on-line gammas
  (iv) repeat with the optimum fitted to D-H instead
  (v)  report the "discrimination ratio"
            r := min(RMS_zeta) / min(RMS_DH)
       and the symmetry of the residuals

If a spectral construction has genuine L-function information, the ratio
should differ from 1: the spectrum should be much closer to one of the
two targets. If r is approximately 1 across all variants, the
construction is L-function-agnostic.

The Davenport-Heilbronn discipline interpretation: a candidate $H$ that
predicts D-H on-line zeros AS WELL AS it predicts zeta zeros is
structurally insufficient. Off-line D-H zeros (rho = 0.8085 + 85.7i and
partners) are at known positions; we also check whether any variant's
spectrum approaches the OFF-LINE D-H gammas after best fit. If a
construction is genuinely Hilbert-Polya, it should NOT predict eigenvalues
at the off-line gammas (because off-line zeros have complex 1/2 + i*gamma
that doesn't correspond to a real eigenvalue of a self-adjoint H).

Output:
  - e1c_lfunction_discrimination.npz: per-variant residuals
  - e1c_lfunction_discrimination.png: residual plots, discrimination
    ratios
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as la

from experiments._shared import zeta_L, DavenportHeilbronn
from experiments.spectral.e1a_berry_keating import build_H_finite_diff
from experiments.spectral.e1b_sierra_townsend import (
    VARIANTS as ST_VARIANTS,
    build_H_st,
    real_spectrum,
)


def best_affine(spec, target):
    """Find alpha, beta that minimize sum_i (alpha * spec[i] + beta - target[i])^2.

    Closed-form least squares: solves [[s_i, 1]; ...] [alpha, beta] = target_i.
    Returns (alpha, beta, rms).
    """
    n = min(len(spec), len(target))
    if n < 2:
        return float("nan"), float("nan"), float("nan")
    A = np.column_stack([spec[:n], np.ones(n)])
    sol, *_ = np.linalg.lstsq(A, target[:n], rcond=None)
    alpha, beta = sol
    pred = alpha * np.array(spec[:n]) + beta
    rms = float(np.sqrt(np.mean((pred - target[:n]) ** 2)))
    return float(alpha), float(beta), rms


def get_spectrum_1A(bc: str, N: int, L: float):
    """Lowest positive real eigenvalues of the 1A bare BK with given BC."""
    u_a, u_b = -L / 2, L / 2
    H = build_H_finite_diff(N, u_a, u_b, bc=bc)
    eigs = la.eigvals(H)
    spec = real_spectrum(eigs)
    return np.array(sorted(s for s in spec if s > 0))


def get_spectrum_1B(V_func, a: float, N: int, L: float):
    """Lowest positive real eigenvalues of a 1B Sierra-Townsend variant."""
    u_a, u_b = 0.0, L
    H = build_H_st(N, u_a, u_b, V_func, a, bc="periodic")
    eigs = la.eigvals(H)
    spec = real_spectrum(eigs)
    return np.array(sorted(s for s in spec if s > 0))


def run(
    N: int = 200,
    L_1A: float = 10.0,
    L_1B: float = 15.0,
    n_compare: int = 40,
    prec: int = 30,
    a_1B: float = 1.0,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"[1C] L-function discrimination test")
    print(f"     n_compare = {n_compare}, N = {N}")

    print(f"[1C] Loading targets...")
    zeta_g = np.array(sorted(float(r.imag) for r in zeta_L.zeros(T_max=300.0, prec=prec)[:n_compare]))
    dh = DavenportHeilbronn()
    dh_all = dh.zeros(T_max=300.0, prec=prec)
    dh_online = np.array(sorted(float(r.imag) for r in dh_all if abs(float(r.real) - 0.5) < 1e-4)[:n_compare])
    dh_offline = np.array(sorted(float(r.imag) for r in dh_all if abs(float(r.real) - 0.5) > 1e-2))
    print(f"     zeta:        {len(zeta_g)} gammas, range [{zeta_g[0]:.2f}, {zeta_g[-1]:.2f}]")
    print(f"     D-H on-line: {len(dh_online)} gammas, range [{dh_online[0]:.2f}, {dh_online[-1]:.2f}]")
    print(f"     D-H off-line: {len(dh_offline)} gammas (at gamma ~ {dh_offline[0]:.2f})")

    # Build the candidate H spectra
    variants = []
    print(f"\n[1C] Building 1A bare BK spectra (L = {L_1A})...")
    for bc in ("dirichlet", "periodic", "open"):
        t0 = time.time()
        spec = get_spectrum_1A(bc, N, L_1A)
        print(f"     1A-{bc:>10s}: {len(spec)} positive eigs, range [{spec.min():.2f}, {spec.max():.2f}] ({time.time() - t0:.1f}s)")
        variants.append((f"1A-{bc}", spec))

    print(f"\n[1C] Building 1B Sierra-Townsend spectra (L = {L_1B}, a = {a_1B})...")
    for variant_name, V_func in ST_VARIANTS.items():
        t0 = time.time()
        spec = get_spectrum_1B(V_func, a_1B, N, L_1B)
        short_name = variant_name.split()[0]
        print(f"     1B-{short_name:>5s}: {len(spec)} positive eigs, range [{spec.min():.2f}, {spec.max():.2f}] ({time.time() - t0:.1f}s)")
        variants.append((f"1B-{short_name}", spec))

    # Run the discrimination analysis
    print(f"\n[1C] Best-affine fits and discrimination ratios:")
    print(f"     {'variant':<20s}  {'alpha_z':>9s} {'beta_z':>8s} {'RMS_z':>8s}  "
          f"{'alpha_d':>9s} {'beta_d':>8s} {'RMS_d':>8s}  {'r=RMSz/RMSd':>14s}")
    results = []
    for name, spec in variants:
        a_z, b_z, rms_z = best_affine(spec, zeta_g)
        a_d, b_d, rms_d = best_affine(spec, dh_online)
        ratio = rms_z / rms_d if rms_d > 0 else float("nan")
        # Also: apply zeta-best fit to D-H and vice versa for cross-comparison
        n = min(len(spec), len(zeta_g), len(dh_online))
        cross_z_to_d = np.sqrt(np.mean((a_z * spec[:n] + b_z - dh_online[:n]) ** 2))
        cross_d_to_z = np.sqrt(np.mean((a_d * spec[:n] + b_d - zeta_g[:n]) ** 2))
        results.append({
            "name": name, "spec": spec,
            "alpha_z": a_z, "beta_z": b_z, "rms_z": rms_z,
            "alpha_d": a_d, "beta_d": b_d, "rms_d": rms_d,
            "ratio": ratio,
            "cross_z_to_d": float(cross_z_to_d),
            "cross_d_to_z": float(cross_d_to_z),
        })
        print(f"     {name:<20s}  {a_z:>9.3f} {b_z:>+8.2f} {rms_z:>8.3f}  "
              f"{a_d:>9.3f} {b_d:>+8.2f} {rms_d:>8.3f}  {ratio:>14.4f}")

    # Summary verdict
    ratios = np.array([r["ratio"] for r in results])
    print(f"\n[1C] Discrimination ratio statistics:")
    print(f"     min = {ratios.min():.4f}, max = {ratios.max():.4f}, "
          f"mean = {ratios.mean():.4f}, std = {ratios.std():.4f}")
    print(f"     If all ratios are ~1, none of the constructions discriminates")
    print(f"     zeta from D-H. A genuine Hilbert-Polya construction would")
    print(f"     give ratio far from 1 (and the cross fits would be poor).")
    spread = float(ratios.max() / ratios.min()) if ratios.min() > 0 else float("nan")
    print(f"     max/min spread = {spread:.4f}")

    # Off-line D-H test: does any spectrum predict eigenvalues near the
    # D-H off-line gammas? Per the Hilbert-Polya thesis, a real
    # self-adjoint spectrum CANNOT realize a complex zero
    # (1/2 + i gamma with beta != 1/2). But the imaginary parts of
    # off-line zeros are still real numbers; if a spectral construction
    # happens to have eigenvalues near those gammas, it's a false signal.
    print(f"\n[1C] Off-line D-H gamma matching test:")
    print(f"     D-H off-line gammas: {[f'{g:.2f}' for g in dh_offline]}")
    for r in results:
        # For each off-line gamma, find best-fit position from zeta-aligned spectrum
        spec_aligned = r["alpha_z"] * r["spec"] + r["beta_z"]
        nearest = [float(np.abs(spec_aligned - g).min()) for g in dh_offline]
        print(f"     {r['name']:<20s}  nearest |E - gamma_off|: "
              f"min = {min(nearest):.3f}, mean = {np.mean(nearest):.3f}")

    # Save and plot
    save_dict = {
        "n_compare": n_compare,
        "zeta_gammas": zeta_g,
        "dh_online_gammas": dh_online,
        "dh_offline_gammas": dh_offline,
        "variant_names": np.array([r["name"] for r in results]),
        "ratios": ratios,
        "rms_zeta": np.array([r["rms_z"] for r in results]),
        "rms_dh": np.array([r["rms_d"] for r in results]),
        "cross_z_to_d": np.array([r["cross_z_to_d"] for r in results]),
        "cross_d_to_z": np.array([r["cross_d_to_z"] for r in results]),
    }
    for i, r in enumerate(results):
        save_dict[f"spec_{i}"] = r["spec"]
    np.savez_compressed(out_dir / "e1c_lfunction_discrimination.npz", **save_dict)

    # Plot: 2 rows, 3 cols
    fig, axs = plt.subplots(2, 3, figsize=(15, 8.5))

    # Top row: best-fit comparison for each variant (one per col, only first 3)
    for col, r in enumerate(results[:3]):
        ax = axs[0, col]
        n = min(len(r["spec"]), n_compare)
        x = np.arange(1, n + 1)
        ax.plot(x, zeta_g[:n], "k.-", label="zeta gammas", markersize=4)
        ax.plot(x, dh_online[:n], "r.-", label="D-H gammas (on-line)", alpha=0.7, markersize=4)
        ax.plot(x, r["alpha_z"] * r["spec"][:n] + r["beta_z"], "b-",
                label=f"{r['name']}: best fit to zeta", alpha=0.7)
        ax.plot(x, r["alpha_d"] * r["spec"][:n] + r["beta_d"], "g--",
                label=f"{r['name']}: best fit to D-H", alpha=0.7)
        ax.set_xlabel("index")
        ax.set_ylabel("value")
        ax.set_title(f"{r['name']}\nRMS_z = {r['rms_z']:.2f}, RMS_d = {r['rms_d']:.2f}")
        ax.legend(fontsize=7)
        ax.grid(alpha=0.3)

    # Bottom row left: RMS comparison bar chart
    ax = axs[1, 0]
    labels = [r["name"] for r in results]
    x_pos = np.arange(len(labels))
    width = 0.4
    ax.bar(x_pos - width / 2, [r["rms_z"] for r in results], width, label="RMS vs zeta", color="b", alpha=0.7)
    ax.bar(x_pos + width / 2, [r["rms_d"] for r in results], width, label="RMS vs D-H on-line", color="r", alpha=0.7)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("best-affine RMS")
    ax.set_title("Best-affine RMS to each target")
    ax.legend()
    ax.grid(alpha=0.3, axis="y")

    # Bottom row middle: discrimination ratio
    ax = axs[1, 1]
    bars = ax.bar(x_pos, ratios, color=["b" if r < 1 else "r" for r in ratios])
    ax.axhline(1, color="k", linestyle="--", label="r = 1 (no discrimination)")
    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=8)
    ax.set_ylabel(r"$r = \mathrm{RMS}_\zeta / \mathrm{RMS}_{DH}$")
    ax.set_title("Discrimination ratio\n(= 1 if construction is L-function-blind)")
    for bar, val in zip(bars, ratios):
        ax.text(bar.get_x() + bar.get_width() / 2, val, f"{val:.3f}",
                ha="center", va="bottom" if val >= 1 else "top", fontsize=8)
    ax.legend()
    ax.grid(alpha=0.3, axis="y")

    # Bottom row right: cross-RMS — apply zeta-fit to D-H, and D-H-fit to zeta
    ax = axs[1, 2]
    ax.bar(x_pos - width / 2, [r["cross_z_to_d"] for r in results], width,
           label="(zeta-fit) applied to D-H", color="b", alpha=0.5, hatch="//")
    ax.bar(x_pos + width / 2, [r["cross_d_to_z"] for r in results], width,
           label="(D-H-fit) applied to zeta", color="r", alpha=0.5, hatch="\\\\")
    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("RMS")
    ax.set_title("Cross-application RMS\n(swap targets after best fit)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig(out_dir / "e1c_lfunction_discrimination.png", dpi=140)
    plt.close()
    print(f"\n[1C] Saved {out_dir / 'e1c_lfunction_discrimination.png'}")
    print(f"[1C] Saved {out_dir / 'e1c_lfunction_discrimination.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=200)
    parser.add_argument("--L-1A", type=float, default=10.0)
    parser.add_argument("--L-1B", type=float, default=15.0)
    parser.add_argument("--n-compare", type=int, default=40)
    parser.add_argument("--a-1B", type=float, default=1.0)
    args = parser.parse_args()
    run(
        N=args.N,
        L_1A=args.L_1A,
        L_1B=args.L_1B,
        n_compare=args.n_compare,
        a_1B=args.a_1B,
    )
