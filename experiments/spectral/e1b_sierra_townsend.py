"""Experiment 1B: Sierra-Townsend-style modifications of Berry-Keating.

The Sierra-Townsend program (Sierra arXiv:0712.0427, Sierra-Townsend
arXiv:0805.4847, Sierra arXiv:1601.01797) proposes augmenting the bare
Berry-Keating Hamiltonian H_BK = (xp + px)/2 with a position-dependent
correction so that the spectral density acquires the logarithmic growth
of Riemann-von Mangoldt:

    rho_zeta(T) = log(T / (2 pi)) / (2 pi)

vs the BK constant L/(2 pi) result from 1A. The original ST construction
lives on the hyperbolic upper half plane with a magnetic field; after
LLL projection the effective 1D operator has the form

    H_ST(x, p) = (1/2)(xp + px) + V(x)

with V chosen to mimic the running coupling induced by the hyperbolic
curvature. The exact V varies across the literature. We discretize three
representative choices on the same log-grid as 1A:

    ST-A:  V(x) = +a / (2 x^2)        (centrifugal: B field on hyperbolic plane)
    ST-B:  V(x) = -a / (2 x)          (Coulomb-like: 1/x potential)
    ST-C:  V(x) = +a * log(x)         (linear in u = log x; "modular" form)

For each variant we sweep over coupling a in {0.0, 0.5, 1.0, 2.0} and
compare:

  (i) the real part of the lowest 50 eigenvalues to the first 50 zeta
      and on-line D-H gammas
  (ii) the empirical density rho(E) = dN/dE to rho_zeta(E) and the BK
      baseline

Architectural purpose: 1A showed that bare BK gives constant density
L/(2 pi) and cannot reproduce zeta's log-growth. 1B asks whether the
natural Sierra-Townsend corrections fix this. We expect:

  - Some variant with the right sign of a will bend the density upward
    at large E, partially matching the zeta log-growth.
  - No variant will produce eigenvalues that match individual
    {gamma_n} to better than O(1) — the construction has no arithmetic
    input.
  - All variants give the same spectrum whether we "target" zeta or
    D-H, since the Hamiltonian is L-function-agnostic. This is the
    Arch 1 obstruction at a more sophisticated level than 1A.

A model that genuinely closed RH would have to import arithmetic
information (the Euler product) into the operator, which no purely
spectral construction does.

Output:
  - e1b_sierra_townsend.npz: spectra for all (variant, a) combos
  - e1b_sierra_townsend.png: 3-row (one per variant) x 3-col panel
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


VARIANTS = {
    "ST-A (centrifugal: a/2x^2)": lambda u, a: 0.5 * a / np.exp(2 * u),
    "ST-B (Coulomb: -a/2x)":      lambda u, a: -0.5 * a / np.exp(u),
    "ST-C (modular: a log x)":     lambda u, a: a * u,
}


def build_H_st(N: int, u_a: float, u_b: float, V_func, a: float, bc: str = "periodic"):
    """H = -i(d/du + 1/2) + V(u; a) on uniform u-grid.

    Same finite-difference framework as 1A; periodic BC by default
    because it gives the cleanest real spectrum at small a.
    """
    du = (u_b - u_a) / (N - 1)
    u_grid = np.linspace(u_a, u_b, N)
    D1 = np.zeros((N, N))
    for k in range(N):
        if 0 < k < N - 1:
            D1[k, k - 1] = -1 / (2 * du)
            D1[k, k + 1] = +1 / (2 * du)
    if bc == "periodic":
        D1[0, 1] = +1 / (2 * du)
        D1[0, N - 1] = -1 / (2 * du)
        D1[N - 1, 0] = +1 / (2 * du)
        D1[N - 1, N - 2] = -1 / (2 * du)
    else:
        raise ValueError(f"BC {bc} not implemented here")

    I = np.eye(N)
    H_BK = -1j * (D1 + 0.5 * I)
    V_diag = np.diag(V_func(u_grid, a))
    return H_BK + V_diag


def real_spectrum(eigs, im_tol: float = 0.05, im_shift: float = -0.5):
    """Real eigenvalues, sorted, after removing the systematic -0.5i shift.

    H_BK = -i (D1 + 0.5 I) has a c-number constant -0.5i inside; with
    periodic BC every eigenvalue picks up Im = -0.5 exactly. We shift
    back by +0.5i and then filter to Im ~ 0 to within im_tol.
    """
    mask = np.abs(eigs.imag - im_shift) < im_tol
    return np.sort(eigs.real[mask])


def run(
    N: int = 200,
    L: float = 10.0,
    a_values=(0.0, 0.5, 1.0, 2.0),
    n_compare: int = 50,
    prec: int = 30,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    # Standard BK domain x in [1, e^L] so u = log x in [0, L]. Keeps
    # 1/x and 1/x^2 corrections regular.
    u_a, u_b = 0.0, L

    print(f"[1B] Sierra-Townsend modifications of BK")
    print(f"     N = {N}, u in [{u_a}, {u_b}], coupling a in {list(a_values)}")

    print(f"[1B] Loading first {n_compare} zeta zeros + D-H on-line zeros...")
    zeta_gammas = sorted(float(r.imag) for r in zeta_L.zeros(T_max=200.0, prec=prec)[:n_compare])
    dh = DavenportHeilbronn()
    dh_all = dh.zeros(T_max=200.0, prec=prec)
    dh_online = sorted(float(r.imag) for r in dh_all if abs(float(r.real) - 0.5) < 1e-4)[:n_compare]
    print(f"     zeta: {len(zeta_gammas)} gammas in [{zeta_gammas[0]:.2f}, {zeta_gammas[-1]:.2f}]")
    print(f"     D-H on-line: {len(dh_online)} gammas in [{dh_online[0]:.2f}, {dh_online[-1]:.2f}]")

    rho_BK = L / (2 * np.pi)

    results = {}  # variant -> {a -> spectrum}
    for variant, V_func in VARIANTS.items():
        results[variant] = {}
        print(f"\n[1B] {variant}")
        for a in a_values:
            t0 = time.time()
            H = build_H_st(N, u_a, u_b, V_func, a, bc="periodic")
            eigs = la.eigvals(H)
            spec = real_spectrum(eigs)
            pos_spec = spec[spec > 0]
            results[variant][a] = pos_spec
            print(f"     a = {a:.1f}: {len(spec)} real eigs, {len(pos_spec)} positive; "
                  f"E range [{(pos_spec.min() if len(pos_spec) else 0):.2f}, "
                  f"{(pos_spec.max() if len(pos_spec) else 0):.2f}] "
                  f"({time.time() - t0:.1f}s)")

    # Save
    npz_kwargs = {
        "N": N, "L": L, "u_a": u_a, "u_b": u_b,
        "zeta_gammas": np.array(zeta_gammas),
        "dh_online": np.array(dh_online),
        "rho_BK": rho_BK,
        "a_values": np.array(a_values),
    }
    for variant, by_a in results.items():
        for a, spec in by_a.items():
            key = f"spec_{variant.split()[0].replace('-', '_')}_a{a:.2f}".replace(".", "p")
            npz_kwargs[key] = spec
    np.savez_compressed(out_dir / "e1b_sierra_townsend.npz", **npz_kwargs)

    # Plot: 3 rows (variants) x 3 cols (spectrum vs index, density, zoom vs zeta)
    fig, axs = plt.subplots(len(VARIANTS), 3, figsize=(15, 12))
    cmap = plt.get_cmap("viridis")
    a_colors = {a: cmap(i / max(len(a_values) - 1, 1)) for i, a in enumerate(a_values)}

    for row, (variant, by_a) in enumerate(results.items()):
        # Column 1: low-positive eigenvalues vs index, with zeta and D-H overlay
        ax = axs[row, 0]
        for a, spec in by_a.items():
            n_show = min(len(spec), n_compare)
            ax.plot(range(1, n_show + 1), spec[:n_show], "o-",
                    color=a_colors[a], alpha=0.7, markersize=3,
                    label=f"a = {a:.1f}")
        ax.plot(range(1, n_compare + 1), zeta_gammas, "k.--", label="zeta gamma", markersize=5)
        ax.plot(range(1, len(dh_online) + 1), dh_online, "r.--", label="D-H (on-line)", markersize=4, alpha=0.6)
        ax.set_xlabel("index n")
        ax.set_ylabel("eigenvalue / gamma")
        ax.set_title(f"{variant}\nlowest positive eigenvalues vs zeta, D-H gammas")
        ax.legend(fontsize=7)
        ax.grid(alpha=0.3)
        ax.set_ylim(0, max(max(zeta_gammas), max(dh_online)) * 1.2)

        # Column 2: empirical density rho(E) = dN/dE, vs BK constant and zeta log
        ax = axs[row, 1]
        Ts = np.linspace(2, 50, 200)
        rho_zeta_curve = np.log(np.maximum(Ts / (2 * np.pi), 1.0)) / (2 * np.pi)
        ax.plot(Ts, np.full_like(Ts, rho_BK), "k--",
                label=f"BK constant {rho_BK:.3f}")
        ax.plot(Ts, rho_zeta_curve, "k-", label="zeta log-density")
        for a, spec in by_a.items():
            if len(spec) < 3:
                continue
            spec_in_range = spec[(spec >= 2) & (spec <= 50)]
            if len(spec_in_range) < 3:
                continue
            # Empirical density via running index/window
            window = 5
            kernel_E = np.zeros(len(Ts))
            for E in spec_in_range:
                kernel_E += np.exp(-((Ts - E) ** 2) / (2 * window ** 2))
            kernel_E /= (window * np.sqrt(2 * np.pi))
            ax.plot(Ts, kernel_E, "-", color=a_colors[a], alpha=0.7,
                    label=f"a = {a:.1f}")
        ax.set_xlabel("E")
        ax.set_ylabel(r"$\rho(E) = dN/dE$")
        ax.set_title("Spectral density vs BK and zeta")
        ax.legend(fontsize=7)
        ax.grid(alpha=0.3)
        ax.set_ylim(0, max(rho_BK, rho_zeta_curve.max()) * 2)

        # Column 3: residual (spec - zeta_gamma) per index, showing systematic gap
        ax = axs[row, 2]
        for a, spec in by_a.items():
            n_show = min(len(spec), n_compare)
            if n_show == 0:
                continue
            res = np.array(spec[:n_show]) - np.array(zeta_gammas[:n_show])
            ax.plot(range(1, n_show + 1), res, "o-",
                    color=a_colors[a], alpha=0.7, markersize=3,
                    label=f"a = {a:.1f}")
        ax.axhline(0, color="k", linewidth=0.5)
        ax.set_xlabel("index n")
        ax.set_ylabel(r"$E_n - \gamma_n^\zeta$")
        ax.set_title("Residual from zeta gammas\n(zero line = exact match)")
        ax.legend(fontsize=7)
        ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e1b_sierra_townsend.png", dpi=140)
    plt.close()
    print(f"\n[1B] Saved {out_dir / 'e1b_sierra_townsend.png'}")
    print(f"[1B] Saved {out_dir / 'e1b_sierra_townsend.npz'}")

    # Summary table: per (variant, a), best-match metric
    print()
    print(f"[1B] Summary (best match to first {n_compare} zeta gammas):")
    print(f"     variant                                  a     RMS(E_n - gamma_n)   density(E=30)")
    for variant, by_a in results.items():
        for a, spec in by_a.items():
            n = min(len(spec), n_compare)
            if n == 0:
                rms = float("nan")
            else:
                diffs = np.array(spec[:n]) - np.array(zeta_gammas[:n])
                rms = float(np.sqrt(np.mean(diffs ** 2)))
            # estimate density at E=30: count eigenvalues in [27, 33] / 6
            in_window = (spec >= 27) & (spec <= 33)
            rho_30 = float(in_window.sum() / 6.0) if len(spec) else float("nan")
            print(f"     {variant:40s}   {a:.1f}   {rms:>12.4f}        {rho_30:>6.3f}")
    print(f"     zeta target density at E=30:                                   "
          f"{np.log(30/(2*np.pi))/(2*np.pi):.3f}")

    # L-function-agnostic check: same spectrum predicts same gammas for any L
    print()
    print(f"[1B] L-function discrimination check:")
    print(f"     The H matrix has no L-function input. Same spectrum is being")
    print(f"     compared to zeta gammas and to D-H on-line gammas; no variant")
    print(f"     can distinguish them by construction.")
    print(f"     zeta first 10 gammas: {[f'{g:.2f}' for g in zeta_gammas[:10]]}")
    print(f"     D-H  first 10 gammas: {[f'{g:.2f}' for g in dh_online[:10]]}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=200)
    parser.add_argument("--L", type=float, default=10.0)
    parser.add_argument("--n-compare", type=int, default=50)
    parser.add_argument("--a-values", type=float, nargs="+", default=[0.0, 0.5, 1.0, 2.0])
    args = parser.parse_args()
    run(N=args.N, L=args.L, a_values=tuple(args.a_values), n_compare=args.n_compare)
