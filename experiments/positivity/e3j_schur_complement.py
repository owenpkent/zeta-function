"""Experiment 3J: Schur complement of the Weil-form Gram matrix against the on-line subspace.

This experiment quantifies the "irreducible off-line obstruction" — the
piece of negativity in the Weil Gram matrix M that survives after the
on-line subspace has been used optimally to cancel it.

## Setup

The Weil-form Gram matrix decomposes as
    M = M_on + M_off
where the two terms collect contributions from on-line zeros (Re rho = 1/2)
and off-line zeros respectively. Each off-line zero rho in UHP contributes
a rank-2 indefinite matrix 2 Re(Phi(rho) Phi(rho)^T) with signature (+1, -1).

For a Selberg-class L-function with RH believed (zeta, chi_3 below T_max):
    M_off = 0,    M = M_on PSD.

For D-H (off-line zeros known): M_off has rank 2 * (# off-line gamma values)
with equal positive and negative signature. The question is whether M_on
can "cover" the negative directions.

## The Schur complement

Let Q be an orthonormal basis for range(M_off). Partition R^K as
    R^K = Q + Q^perp,
the off-line subspace + its complement. In this basis:
    M = [ M_QQ      M_QC      ]
        [ M_QC^T   M_CC      ]
with
    M_QQ = Q^T M Q   = Q^T M_on Q + D_off       (D_off diagonal off-line spectrum)
    M_CC = Q^perp^T M Q^perp  = Q^perp^T M_on Q^perp        (PSD)
    M_QC = Q^T M Q^perp  = Q^T M_on Q^perp                  (cross coupling)

The Schur complement of M with respect to M_CC is
    S := M / M_CC = M_QQ - M_QC M_CC^{-1} M_QC^T.

S is an (r x r) matrix on the off-line subspace (r = dim range(M_off)).
By the standard block determinant identity, M is PSD iff M_CC is PSD AND
S is PSD. Since M_CC is always PSD, the signature of S equals the signature
of M (restricted to its non-trivial subspace).

S has a clean structural meaning: it is the off-line obstruction AFTER the
on-line cushion has been deployed optimally. If S has a negative eigenvalue,
that direction is one in which on-line corrections cannot save Weil positivity,
no matter how the basis is refined.

## Predictions

1. For zeta and chi_3: range(M_off) is trivial, S is the empty matrix.
   No obstruction; M_on is PSD on all of R^K. (Trivial Schur.)

2. For D-H: dim range(M_off) = 2 * (# off-line gamma in UHP) = 8 at T_max = 200.
   S is an 8x8 indefinite matrix. The signature of S should equal the
   number of off-line gamma values (= 4 negative, 4 positive at T_max=200).

3. As K grows, S's negative eigenvalues should DEEPEN (more on-line cushion
   means tighter cancellation possible, but the IRREDUCIBLE off-line piece
   becomes more clearly resolved). The smallest eigenvalue of S should
   converge to a finite, negative value as K -> infinity — the asymptotic
   strength of the off-line obstruction.

4. The Schur complement S separates the obstruction from the on-line
   cushion in a way that the raw spectrum of M does not: M's smallest
   eigenvalue is also influenced by the on-line basis becoming redundant
   (= floating-point noise), while S lives on a fixed-dimensional subspace
   pinned to the off-line zeros.

## Test

Run for L in {zeta, chi_3, D-H} at K in {50, 100, 200, 300} with T_max=200.
Report eigenstructure of M, M_on, M_off, and S = M / M_CC.

Outputs:
  - e3j_schur_complement.npz : K grid, eigenvalue stats per L
  - e3j_schur_complement.png : 4-panel summary
  - stdout : per-K table
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

from experiments._shared import zeta_L, DavenportHeilbronn, chi3_L
from experiments.positivity.e3c_weil_form import phi_b


def phi_table_for(L, b_vals, T_max: float, prec: int):
    """Evaluate Phi_b(rho) for every (b, rho) pair. Returns (K x n_rho) complex array."""
    mp.mp.dps = prec
    rhos = L.zeros(T_max=T_max, prec=prec)
    K = len(b_vals)
    table = np.empty((K, len(rhos)), dtype=np.complex128)
    for k, b in enumerate(b_vals):
        b_mp = mp.mpf(b)
        for r, rho in enumerate(rhos):
            table[k, r] = complex(phi_b(b_mp, rho, prec=prec))
    is_on = np.array([abs(float(rho.real) - 0.5) < 1e-6 for rho in rhos])
    return table, is_on, rhos


def split_gram(phi_table, is_on):
    """M = M_on + M_off where each off-line/on-line contribution is
    the rank-<=2 real-symmetric matrix 2 Re(Phi(rho) Phi(rho)^T)."""
    K = phi_table.shape[0]
    M_on = np.zeros((K, K))
    M_off = np.zeros((K, K))
    for r in range(phi_table.shape[1]):
        col = phi_table[:, r]
        outer = 2.0 * np.real(np.outer(col, col))
        if is_on[r]:
            M_on += outer
        else:
            M_off += outer
    M_on = 0.5 * (M_on + M_on.T)
    M_off = 0.5 * (M_off + M_off.T)
    return M_on, M_off


def schur_complement(M_on, M_off, rcond_floor: float = 1e-10):
    """Compute S = M / M_CC, the Schur complement of M = M_on + M_off
    with respect to the orthogonal complement of range(M_off).

    Returns:
      S       : (r x r) Schur complement matrix
      D_off   : (r,)   diagonal of M_off in the range(M_off) basis Q
      M_on_Q  : (r x r) projection of M_on onto range(M_off)
      M_QC    : (r x (K-r)) cross-coupling
      r       : rank of M_off (= dim Schur subspace)
    """
    K = M_off.shape[0]
    # Eigendecompose M_off to find range and its complement.
    eigvals_off, eigvecs_off = np.linalg.eigh(M_off)
    scale = max(abs(eigvals_off).max(), 1.0)
    nontrivial = np.abs(eigvals_off) > rcond_floor * scale
    if not nontrivial.any():
        return np.zeros((0, 0)), np.zeros(0), np.zeros((0, 0)), np.zeros((0, 0)), 0

    Q = eigvecs_off[:, nontrivial]                  # K x r, orthonormal
    Qc = eigvecs_off[:, ~nontrivial]                # K x (K-r), orthonormal
    r = Q.shape[1]

    # Project the full M onto each block.
    M_on_Q  = Q.T @ M_on @ Q                                  # r x r, PSD
    D_off   = np.diag(eigvals_off[nontrivial])                # r x r, diagonal
    M_on_C  = Qc.T @ M_on @ Qc                                # (K-r) x (K-r), PSD
    M_QC    = Q.T  @ M_on @ Qc                                # r x (K-r) (M_off zero off range)

    M_QQ = M_on_Q + D_off                                     # = Q^T M Q
    M_CC = M_on_C                                             # = Qc^T M Qc (M_off is zero on Qc)

    # Schur complement S = M_QQ - M_QC M_CC^{-1} M_QC^T (use pinv for safety).
    # M_CC has dim K-r and is PSD; for K large enough, it is essentially full-rank
    # on Qc (since the on-line zeros span R^K modulo small dim).
    M_CC_pinv = np.linalg.pinv(M_CC, rcond=1e-12)
    S = M_QQ - M_QC @ M_CC_pinv @ M_QC.T
    S = 0.5 * (S + S.T)
    return S, eigvals_off[nontrivial], M_on_Q, M_QC, r


def run(
    K_vals=(50, 100, 200, 300),
    b_min: float = 1.1,
    b_max: float = 1000.0,
    T_max: float = 200.0,
    prec: int = 30,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    dh = DavenportHeilbronn()
    targets = [
        ("zeta", zeta_L),
        ("chi3", chi3_L),
        ("DH",   dh),
    ]

    # Pre-evaluate phi_tables: when K varies, we just resample. Easier to
    # recompute each K than cache (mpmath is cheap relative to the eigen).
    # But we DO load zeros once per L to avoid hitting mpmath.zetazero repeatedly.
    print(f"[3J] Loading zeros for each L (T_max = {T_max}, prec = {prec})...")
    zeros_cache = {}
    for name, L in targets:
        t0 = time.time()
        rhos = L.zeros(T_max=T_max, prec=prec)
        is_on = np.array([abs(float(rho.real) - 0.5) < 1e-6 for rho in rhos])
        zeros_cache[name] = (rhos, is_on)
        print(f"  {name:6s} : {len(rhos)} zeros ({int(is_on.sum())} on-line, "
              f"{int((~is_on).sum())} off-line) in {time.time() - t0:.1f}s")

    results = {name: {} for name, _ in targets}

    for K in K_vals:
        b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)
        print(f"\n[3J] K = {K}, b in [{b_min}, {b_max}]")
        for name, L in targets:
            rhos, is_on = zeros_cache[name]
            t0 = time.time()
            # Evaluate phi_b(rho) for all pairs at the current K.
            phi_table = np.empty((K, len(rhos)), dtype=np.complex128)
            for k, b in enumerate(b_vals):
                b_mp = mp.mpf(b)
                for r_idx, rho in enumerate(rhos):
                    phi_table[k, r_idx] = complex(phi_b(b_mp, rho, prec=prec))
            t_phi = time.time() - t0

            t0 = time.time()
            M_on, M_off = split_gram(phi_table, is_on)
            M = M_on + M_off
            S, d_off, M_on_Q, M_QC, r_dim = schur_complement(M_on, M_off)
            t_lin = time.time() - t0

            # Full M eigenvalues.
            eig_M = np.linalg.eigvalsh(M)
            scale_M = max(abs(eig_M).max(), 1.0)
            eig_on = np.linalg.eigvalsh(M_on)
            eig_off = np.linalg.eigvalsh(M_off)

            # Schur eigenvalues.
            if S.size > 0:
                eig_S = np.linalg.eigvalsh(S)
                scale_S = max(abs(eig_S).max(), 1.0)
                schur_min = float(eig_S.min())
                schur_max = float(eig_S.max())
                schur_rel_min = schur_min / scale_S
                schur_neg = int((eig_S < -1e-10 * scale_S).sum())
                schur_pos = int((eig_S >  1e-10 * scale_S).sum())
                # M restricted to off-line subspace BEFORE the cross-coupling correction.
                eig_eff = np.linalg.eigvalsh(M_on_Q + np.diag(d_off))
                eff_min = float(eig_eff.min())
                eff_rel_min = eff_min / max(abs(eig_eff).max(), 1.0)
                # How much does the cross-coupling correction "cost"?
                # By interlacing, S <= M_QQ in operator order (cross removes positivity).
                # The cost in min-eigenvalue: cost = eff_min - schur_min >= 0
                cushion_cost = eff_min - schur_min
            else:
                eig_S = np.zeros(0)
                schur_min = schur_max = schur_rel_min = 0.0
                schur_neg = schur_pos = 0
                eff_min = eff_rel_min = 0.0
                cushion_cost = 0.0

            results[name][K] = {
                "n_on": int(is_on.sum()),
                "n_off": int((~is_on).sum()),
                "eig_M_min": float(eig_M.min()),
                "eig_M_max": float(eig_M.max()),
                "eig_M_rel_min": float(eig_M.min() / scale_M),
                "eig_M_neg": int((eig_M < -1e-10 * scale_M).sum()),
                "eig_on_min": float(eig_on.min()),
                "eig_on_max": float(eig_on.max()),
                "eig_off_min": float(eig_off.min()),
                "eig_off_max": float(eig_off.max()),
                "schur_dim": r_dim,
                "schur_min": schur_min,
                "schur_max": schur_max,
                "schur_rel_min": schur_rel_min,
                "schur_neg": schur_neg,
                "schur_pos": schur_pos,
                "eff_min": eff_min,
                "eff_rel_min": eff_rel_min,
                "cushion_cost": cushion_cost,
                "t_phi": t_phi,
                "t_lin": t_lin,
            }
            r = results[name][K]
            print(f"  {name:6s}: M eig in [{r['eig_M_min']:+.3e}, {r['eig_M_max']:+.3e}] "
                  f"({r['eig_M_neg']} neg), Schur dim={r_dim}")
            if r_dim > 0:
                print(f"          Schur S: eig in [{r['schur_min']:+.3e}, {r['schur_max']:+.3e}] "
                      f"({r['schur_neg']} neg, {r['schur_pos']} pos), rel min {r['schur_rel_min']:+.4%}")
                print(f"          eff (no cross): rel min {r['eff_rel_min']:+.4%}, "
                      f"cushion cost = {r['cushion_cost']:+.3e}")
            print(f"          [phi {r['t_phi']:.1f}s, lin {r['t_lin']:.2f}s]")

    # Save .npz
    save = {"K_vals": np.asarray(K_vals), "T_max": float(T_max), "prec": int(prec)}
    for name, res in results.items():
        for K, r in res.items():
            for key, val in r.items():
                save[f"{name}_K{K}_{key}"] = val
    np.savez_compressed(out_dir / "e3j_schur_complement.npz", **save)

    # Plot
    fig, axs = plt.subplots(2, 2, figsize=(12, 9))
    colors = {"zeta": "tab:blue", "chi3": "tab:green", "DH": "tab:red"}

    ax = axs[0, 0]
    for name, _ in targets:
        Ks = list(results[name].keys())
        vals = [results[name][k]["eig_M_min"] for k in Ks]
        ax.plot(Ks, vals, "o-", label=name, color=colors[name])
    ax.axhline(0, color="k", lw=0.5)
    ax.set_yscale("symlog", linthresh=1e-12)
    ax.set_xlabel("K (basis size)")
    ax.set_ylabel(r"$\lambda_{\min}(M)$")
    ax.set_title("Full Gram: minimum eigenvalue")
    ax.legend(); ax.grid(alpha=0.3)

    ax = axs[0, 1]
    for name, _ in targets:
        Ks = list(results[name].keys())
        vals = [results[name][k]["schur_dim"] for k in Ks]
        ax.plot(Ks, vals, "o-", label=name, color=colors[name])
    ax.set_xlabel("K (basis size)")
    ax.set_ylabel("dim(Schur subspace)")
    ax.set_title("Off-line subspace dimension\n(= rank of $M_{\\rm off}$)")
    ax.legend(); ax.grid(alpha=0.3)

    ax = axs[1, 0]
    for name, _ in targets:
        Ks = list(results[name].keys())
        vals = [results[name][k]["schur_min"] for k in Ks]
        ax.plot(Ks, vals, "o-", label=name, color=colors[name])
    ax.axhline(0, color="k", lw=0.5)
    ax.set_yscale("symlog", linthresh=1e-6)
    ax.set_xlabel("K (basis size)")
    ax.set_ylabel(r"$\lambda_{\min}(S)$")
    ax.set_title(r"Schur complement: $\lambda_{\min}(S)$" "\n(irreducible off-line obstruction)")
    ax.legend(); ax.grid(alpha=0.3)

    ax = axs[1, 1]
    for name, _ in targets:
        Ks = list(results[name].keys())
        vals = [results[name][k]["schur_neg"] for k in Ks]
        ax.plot(Ks, vals, "o-", label=name, color=colors[name])
    ax.set_xlabel("K (basis size)")
    ax.set_ylabel(r"# negative eigenvalues of $S$")
    ax.set_title("Schur complement: negative count\n(predicted = # off-line $\\gamma$ in UHP)")
    ax.legend(); ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e3j_schur_complement.png", dpi=140)
    plt.close()
    print(f"\n[3J] Saved {out_dir / 'e3j_schur_complement.png'}")
    print(f"[3J] Saved {out_dir / 'e3j_schur_complement.npz'}")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--K", type=int, nargs="+", default=[50, 100, 200, 300])
    parser.add_argument("--T-max", type=float, default=200.0)
    parser.add_argument("--prec", type=int, default=30)
    parser.add_argument("--b-min", type=float, default=1.1)
    parser.add_argument("--b-max", type=float, default=1000.0)
    args = parser.parse_args()
    run(
        K_vals=tuple(args.K),
        b_min=args.b_min,
        b_max=args.b_max,
        T_max=args.T_max,
        prec=args.prec,
    )
