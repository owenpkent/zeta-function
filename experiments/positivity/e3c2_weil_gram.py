"""Experiment 3C-extended: Gram-matrix analysis of the Weil quadratic form.

Pick a basis grid of b values {b_1, ..., b_K}. Any linear combination
    f_hat(s) = sum_k c_k Phi_{b_k}(s)
gives a Weil sum
    W(c) = sum_rho f_hat(rho)^2 = c^T M c
where the Gram matrix is
    M_{jk} = sum_rho 2 Re(Phi_{b_j}(rho) Phi_{b_k}(rho))
(rho summed over upper-half-plane zeros, paired with conjugates).

For zeta (all rhos on the critical line): Phi_b(rho) is REAL for every
zero, so M^zeta is the Gram matrix of K real vectors {Phi_{b_k}(rho)}_k
indexed by zero rho. A Gram matrix is positive semi-definite; W_zeta >= 0
for any c. This is a consistency check.

For D-H (off-line zeros present): Phi_b(rho) is complex for off-line
rho, so the contribution 2 Re(Phi_j Phi_k) at off-line rho is NOT a
correlation of real vectors. M^DH can have NEGATIVE eigenvalues. If it
does, the smallest-eigenvalue eigenvector c* gives a linear combination
that VIOLATES Weil positivity for D-H.

This is the wrong-approach detector in clean form: M^DH having a
negative eigenvalue is a finite-dimensional finite-computation witness
that D-H does not satisfy the relevant Weil positivity inside this
basis family.
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
from experiments.positivity.e3c_weil_form import phi_b


def gram_matrix(L, b_vals, T_max: float = 200.0, prec: int = 30):
    """M_{jk} = sum_rho 2 Re(Phi_{b_j}(rho) Phi_{b_k}(rho)) for L's zeros."""
    mp.mp.dps = prec
    rhos = L.zeros(T_max=T_max, prec=prec)
    K = len(b_vals)

    # Pre-evaluate Phi_{b_k}(rho) for all (k, rho)
    phi_table = np.empty((K, len(rhos)), dtype=np.complex128)
    for k, b in enumerate(b_vals):
        b_mp = mp.mpf(b)
        for r, rho in enumerate(rhos):
            phi_table[k, r] = complex(phi_b(b_mp, rho, prec=prec))

    # M_{jk} = sum_r 2 Re(phi_table[j, r] * phi_table[k, r])
    # Vectorized: outer product summed and real part taken
    M = np.zeros((K, K))
    for j in range(K):
        for k in range(K):
            M[j, k] = float(2 * np.real(np.sum(phi_table[j] * phi_table[k])))
    return M, phi_table


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

    print(f"[3C-ext] Computing Gram matrices for K = {n_b} basis vectors, "
          f"b in [{b_min:.2f}, {b_max:.0f}], T_max = {T_max}...")
    t0 = time.time()
    M_zeta, _ = gram_matrix(zeta_L, b_vals, T_max=T_max, prec=prec)
    M_dh, _ = gram_matrix(dh, b_vals, T_max=T_max, prec=prec)
    print(f"     done in {time.time() - t0:.1f}s")

    # Symmetrize (should already be symmetric, this guards against rounding)
    M_zeta = 0.5 * (M_zeta + M_zeta.T)
    M_dh = 0.5 * (M_dh + M_dh.T)

    eig_zeta = np.linalg.eigvalsh(M_zeta)
    eig_dh = np.linalg.eigvalsh(M_dh)

    print(f"[3C-ext] Eigenvalue spectra:")
    print(f"     M^zeta: range = [{eig_zeta.min():.4e}, {eig_zeta.max():.4e}]")
    print(f"             negative count: {int((eig_zeta < -1e-12).sum())} / {n_b}")
    print(f"     M^DH:   range = [{eig_dh.min():.4e}, {eig_dh.max():.4e}]")
    print(f"             negative count: {int((eig_dh < -1e-12).sum())} / {n_b}")

    if eig_dh.min() < -1e-12:
        print(f"[3C-ext] WITNESS FOUND: smallest M^DH eigenvalue = {eig_dh.min():.6e}")
        # Reconstruct the witness vector
        eigvals, eigvecs = np.linalg.eigh(M_dh)
        c_star = eigvecs[:, 0]  # eigenvector for smallest eigenvalue
        W_dh_witness = float(c_star @ M_dh @ c_star)
        W_zeta_witness = float(c_star @ M_zeta @ c_star)
        print(f"     witness c (smallest-eigenvalue eigenvector):")
        print(f"     W_DH(c) = {W_dh_witness:.6e}   (< 0)")
        print(f"     W_zeta(c) = {W_zeta_witness:.6e}   (>= 0; consistency check)")
        print(f"     ratio |W_DH| / W_zeta = {abs(W_dh_witness) / max(W_zeta_witness, 1e-30):.4e}")
        print(f"     => Weil positivity violated for D-H in this basis.")
        print(f"     => 3C-extended diagnostic works as a wrong-approach detector.")
    else:
        print("[3C-ext] No negative eigenvalue in M^DH within this basis.")
        print("         The basis may need to be larger or finer to resolve the witness.")
        print("         The off-line contribution exists but is dwarfed by on-line zeros.")

    np.savez_compressed(
        out_dir / "e3c2_weil_gram.npz",
        b=b_vals,
        M_zeta=M_zeta,
        M_dh=M_dh,
        eig_zeta=eig_zeta,
        eig_dh=eig_dh,
        T_max=T_max,
        prec=prec,
    )

    fig, axs = plt.subplots(1, 3, figsize=(15, 4.5))

    ax = axs[0]
    ax.imshow(M_zeta, cmap="RdBu_r", aspect="auto",
              vmin=-abs(M_zeta).max(), vmax=abs(M_zeta).max())
    ax.set_title(r"$M^\zeta_{jk}$")
    ax.set_xlabel("k"); ax.set_ylabel("j")

    ax = axs[1]
    ax.imshow(M_dh, cmap="RdBu_r", aspect="auto",
              vmin=-abs(M_dh).max(), vmax=abs(M_dh).max())
    ax.set_title(r"$M^{DH}_{jk}$")
    ax.set_xlabel("k"); ax.set_ylabel("j")

    ax = axs[2]
    ax.plot(range(len(eig_zeta)), sorted(eig_zeta), "bo-", label=r"$M^\zeta$")
    ax.plot(range(len(eig_dh)), sorted(eig_dh), "ro-", label=r"$M^{DH}$")
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_yscale("symlog", linthresh=1e-6)
    ax.set_xlabel("eigenvalue index (sorted)")
    ax.set_ylabel("eigenvalue")
    ax.set_title("Spectra")
    ax.legend()
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e3c2_weil_gram.png", dpi=140)
    plt.close()
    print(f"[3C-ext] Saved {out_dir / 'e3c2_weil_gram.png'}")
    print(f"[3C-ext] Saved {out_dir / 'e3c2_weil_gram.npz'}")


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
