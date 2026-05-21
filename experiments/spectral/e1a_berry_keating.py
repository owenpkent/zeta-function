"""Experiment 1A: Berry-Keating discretization with various BCs.

The Berry-Keating Hamiltonian is

    H = (1/2)(xp + px) = -i (x d/dx + 1/2)

on x > 0. Classical orbits xp = E are hyperbolas with period log(L/l)
at energy E in a domain [l, L]. Bohr-Sommerfeld then predicts

    rho_BK(E) = log(L/l) / (2 pi)     (constant in E)

The Riemann-von Mangoldt density at zeta-zero height T is

    rho_zeta(T) = log(T / (2 pi)) / (2 pi)     (grows logarithmically in T)

These can match locally if we choose l, L such that log(L/l) = log(T/2pi),
i.e., L/l = T/(2pi). For a FIXED domain, however, BK density is constant
and cannot reproduce the growing zeta density. That mismatch is one
fundamental obstacle to a literal Hilbert-Polya realization of H = xp.

We discretize on a uniform grid in u = log x with N points, build H as
a finite-difference matrix, and explore three boundary conditions:

  - Dirichlet: psi = 0 at endpoints (hard wall, breaks the dilation
    symmetry strongly)
  - Periodic: psi(u_a) = psi(u_b) (closes the domain, gives clean
    plane-wave modes)
  - Sierra-like: a specific phase BC chosen so the WKB phase matches
    classical orbit period (only sketched here)

We then plot:
  (1) The eigenvalue spectrum in the complex plane (real and imaginary
      parts; eigenvalues with significant imaginary part indicate the
      operator is not self-adjoint with the chosen BC).
  (2) The density of real eigenvalues vs the BK and zeta predictions.
  (3) The lowest 50 eigenvalues compared to the first 50 zeta zeros.

Conclusion drawn: this is a 'spectral signature check'. A literal
Hilbert-Polya proof would require an operator whose spectrum is
exactly {gamma_n}. Naive discretizations give approximate density
agreement but no individual zero match. The experimentation tells us
how close the simple BK setup is to the actual zero spectrum.
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import scipy.linalg as la

from experiments._shared import zeta_L


def build_H_finite_diff(N: int, u_a: float, u_b: float, bc: str = "dirichlet"):
    """Build N x N matrix for H = -i (d/du + 1/2) on uniform u-grid.

    bc: 'dirichlet', 'periodic', or 'open' (free endpoints).
    Returns a dense numpy array (N x N) for diagonalization.
    """
    du = (u_b - u_a) / (N - 1)
    # Central difference for d/du: (psi_{k+1} - psi_{k-1}) / (2 du)
    # Endpoints: forward / backward difference, or BC-specific.
    D1 = np.zeros((N, N))
    for k in range(N):
        if 0 < k < N - 1:
            D1[k, k - 1] = -1 / (2 * du)
            D1[k, k + 1] = +1 / (2 * du)

    if bc == "dirichlet":
        # psi_{-1} = psi_N = 0; the rows for k=0 and k=N-1 use one-sided
        # differences that implicitly assume the ghost points are zero.
        D1[0, 1] = +1 / (2 * du)   # psi_{-1} = 0 contributes nothing
        D1[N - 1, N - 2] = -1 / (2 * du)
    elif bc == "periodic":
        D1[0, 1] = +1 / (2 * du)
        D1[0, N - 1] = -1 / (2 * du)
        D1[N - 1, 0] = +1 / (2 * du)
        D1[N - 1, N - 2] = -1 / (2 * du)
    elif bc == "open":
        # forward difference at 0, backward at N-1
        D1[0, 0] = -1 / du
        D1[0, 1] = +1 / du
        D1[N - 1, N - 2] = -1 / du
        D1[N - 1, N - 1] = +1 / du
    else:
        raise ValueError(f"unknown BC: {bc}")

    I = np.eye(N)
    H = -1j * (D1 + 0.5 * I)
    return H


def run(
    N: int = 200,
    L: float = 10.0,
    n_compare: int = 50,
    prec: int = 30,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    u_a, u_b = -L / 2, L / 2  # symmetric domain in u = log x

    print(f"[1A] Building H matrices (N = {N}, domain u in [{u_a}, {u_b}])...")
    eigs_dict = {}
    for bc in ("dirichlet", "periodic", "open"):
        H = build_H_finite_diff(N, u_a, u_b, bc=bc)
        t0 = time.time()
        eigs = la.eigvals(H)
        eigs_dict[bc] = eigs
        print(f"     [{bc}] diagonalized in {time.time() - t0:.1f}s, "
              f"max |Im eig| = {np.abs(eigs.imag).max():.4f}, "
              f"|Re eig| range = [{np.abs(eigs.real).min():.4f}, "
              f"{np.abs(eigs.real).max():.4f}]")

    # Compare to first zeta zeros
    print(f"[1A] Loading first {n_compare} zeta zeros for comparison...")
    rhos = zeta_L.zeros(T_max=200.0, prec=prec)
    zeta_gammas = sorted(float(r.imag) for r in rhos[:n_compare])

    # Predicted BK density and zeta density at E = 50
    rho_BK = L / (2 * np.pi)
    rho_zeta_50 = np.log(50.0 / (2 * np.pi)) / (2 * np.pi)
    print(f"[1A] Predicted BK density (constant): rho_BK = L/(2 pi) = {rho_BK:.4f}")
    print(f"     Riemann-von Mangoldt rho_zeta(T=50) = {rho_zeta_50:.4f}")
    print(f"     Ratio at this energy: {rho_BK / rho_zeta_50:.2f}")

    np.savez_compressed(
        out_dir / "e1a_berry_keating.npz",
        N=N,
        L=L,
        u_a=u_a,
        u_b=u_b,
        eigs_dirichlet=eigs_dict["dirichlet"],
        eigs_periodic=eigs_dict["periodic"],
        eigs_open=eigs_dict["open"],
        zeta_gammas=np.array(zeta_gammas),
        rho_BK=rho_BK,
    )

    # Plot
    fig, axs = plt.subplots(2, 2, figsize=(13, 9))

    # (1) complex spectrum for each BC
    ax = axs[0, 0]
    colors = {"dirichlet": "b", "periodic": "g", "open": "r"}
    for bc, eigs in eigs_dict.items():
        ax.scatter(eigs.real, eigs.imag, s=12, c=colors[bc], alpha=0.6, label=bc)
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xlabel("Re E")
    ax.set_ylabel("Im E")
    ax.set_title("Eigenvalues in complex plane\n(self-adjoint => all real)")
    ax.legend()
    ax.grid(alpha=0.3)

    # (2) density of real eigenvalues vs predicted BK density
    ax = axs[0, 1]
    for bc, eigs in eigs_dict.items():
        real_eigs = eigs.real[np.abs(eigs.imag) < 0.1]
        ax.hist(real_eigs, bins=40, alpha=0.4, color=colors[bc], label=f"{bc} (n={len(real_eigs)})")
    # Predicted BK density: constant rho_BK
    e_range = np.linspace(-50, 50, 100)
    bk_count = rho_BK * (e_range[1] - e_range[0]) * 2  # per bin
    ax.axhline(rho_BK * (100 / 40) * 2, color="k", linestyle="--",
               label=f"BK density {rho_BK:.3f}")
    ax.set_xlabel("E (real part)")
    ax.set_ylabel("count per bin")
    ax.set_title("Spectral density (real eigenvalues)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (3) compare lowest positive eigenvalues to zeta gammas
    ax = axs[1, 0]
    for bc, eigs in eigs_dict.items():
        real_eigs = sorted(eigs.real[(np.abs(eigs.imag) < 0.1) & (eigs.real > 0)])
        n_show = min(len(real_eigs), n_compare)
        ax.plot(range(1, n_show + 1), real_eigs[:n_show], "o-",
                color=colors[bc], alpha=0.7, label=f"{bc}")
    ax.plot(range(1, n_compare + 1), zeta_gammas, "ko-", label="zeta gammas", markersize=4)
    ax.set_xlabel("index n")
    ax.set_ylabel("eigenvalue / zeta gamma")
    ax.set_title(f"Lowest {n_compare} positive eigenvalues\nvs zeta zero imaginary parts")
    ax.legend()
    ax.grid(alpha=0.3)

    # (4) density at high E
    ax = axs[1, 1]
    Ts = np.linspace(1, 50, 100)
    rho_BK_curve = np.full_like(Ts, rho_BK)
    rho_zeta_curve = np.log(np.maximum(Ts / (2 * np.pi), 1.0)) / (2 * np.pi)
    ax.plot(Ts, rho_BK_curve, "k-", label=f"BK: rho = L/(2 pi) = {rho_BK:.3f}")
    ax.plot(Ts, rho_zeta_curve, "r-", label="zeta: rho(T) = log(T/2 pi)/(2 pi)")
    ax.set_xlabel("T (energy / zeta height)")
    ax.set_ylabel("density (per unit T)")
    ax.set_title("Density mismatch: BK (constant) vs zeta (log)")
    ax.legend()
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e1a_berry_keating.png", dpi=140)
    plt.close()
    print(f"[1A] Saved {out_dir / 'e1a_berry_keating.png'}")
    print(f"[1A] Saved {out_dir / 'e1a_berry_keating.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=200)
    parser.add_argument("--L", type=float, default=10.0)
    parser.add_argument("--n-compare", type=int, default=50)
    args = parser.parse_args()
    run(N=args.N, L=args.L, n_compare=args.n_compare)
