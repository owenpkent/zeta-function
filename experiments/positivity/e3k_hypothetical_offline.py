"""Experiment 3K: hypothetical off-line zero perturbation of zeta in the Schur framework.

Disproof-flavored counterpart to 3J. Ask: if zeta had a hypothetical
off-line zero pair (beta + i*gamma_0, (1 - beta) + i*gamma_0) for some
beta != 1/2 and some gamma_0 in (0, T_max), what Schur complement signal
would the Gram matrix construction produce? For what (beta, gamma_0) is
the signal so small the off-line zero would be "stealth" — indistinguishable
from on-line within the framework's numerical resolution?

## Construction

We use zeta's real (on-line) zeros below T_max as the on-line cushion, and
inject one hypothetical off-line zero pair. The augmented Gram matrix is
    M_aug = M_on(zeta) + M_off(hypothetical pair).
The hypothetical pair contributes a rank-2 indefinite piece
    4 * Re(Phi(rho) Phi(rho)^T)  for rho = beta + i*gamma_0,
with signature (+1, -1). The Schur complement S of M_aug against its
on-line orthogonal complement is then a 2x2 matrix on the off-line
subspace span(Re(Phi(rho)), Im(Phi(rho))) -- typically signature (+1, -1).

The "off-line signal strength" is |lambda_min(S)|, and the relative
signal is |lambda_min(S)| / |lambda_max(S)| in [0, 1].

## Predictions

For epsilon := beta - 1/2 small:
  - Re(Phi_b(rho)) = sin(gamma_0 log b)/gamma_0 + O(epsilon^2)
                    (constant in epsilon to first order)
  - Im(Phi_b(rho)) = -epsilon * log(b) * cos(gamma_0 log b)/gamma_0 + O(epsilon^2)
                    (linear in epsilon)

So the rank-2 indefinite piece has
  - lambda+ ~ 4 * ||Re(Phi)||^2 = O(1)
  - lambda- ~ -4 * ||Im(Phi)||^2 = O(epsilon^2)

Therefore |Schur min eigenvalue| ~ epsilon^2 = (beta - 1/2)^2.

If the framework's numerical noise floor is at the 3D.3 level (~10^-15
relative), the stealth window is epsilon < ~10^-7.5 = 3e-8, far below
current rigorous verification thresholds for zeta zeros (Platt-Trudgian
bound zeros to ~30 digits, ~10^-30 in beta).

The structurally interesting question is the SHAPE of |S_min|(epsilon, gamma_0)
beyond leading order, especially near gamma_0 values where the on-line
cushion has gaps (Lehmer pairs, or near the high boundary T_max).

## Output

  e3k_hypothetical_offline.npz : 2D arrays of Schur stats over (eps, gamma_0)
  e3k_hypothetical_offline.png : heatmap + slice plots
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

from experiments._shared import zeta_L
from experiments.positivity.e3c_weil_form import phi_b
from experiments.positivity.e3j_schur_complement import schur_complement


def augmented_gram(zeta_zeros, b_vals, beta: float, gamma_0: float, prec: int = 30):
    """Build phi_table for zeta's zeros plus an injected off-line pair
    (beta + i*gamma_0, (1 - beta) + i*gamma_0). Returns M_on, M_off."""
    mp.mp.dps = prec
    K = len(b_vals)

    extra = [mp.mpc(beta, gamma_0), mp.mpc(1.0 - beta, gamma_0)]
    augmented = list(zeta_zeros) + extra

    phi_table = np.empty((K, len(augmented)), dtype=np.complex128)
    for k, b in enumerate(b_vals):
        b_mp = mp.mpf(b)
        for r, rho in enumerate(augmented):
            phi_table[k, r] = complex(phi_b(b_mp, rho, prec=prec))

    is_on = np.array([True] * len(zeta_zeros) + [False, False])

    M_on = np.zeros((K, K))
    M_off = np.zeros((K, K))
    for r in range(len(augmented)):
        col = phi_table[:, r]
        outer = 2.0 * np.real(np.outer(col, col))
        if is_on[r]:
            M_on += outer
        else:
            M_off += outer
    M_on = 0.5 * (M_on + M_on.T)
    M_off = 0.5 * (M_off + M_off.T)
    return M_on, M_off


def run(
    eps_log_min: float = -10.0,
    eps_log_max: float = -0.5,
    n_eps: int = 30,
    gamma_vals=(30.0, 60.0, 100.0, 140.0, 180.0),
    K: int = 300,
    b_min: float = 1.1,
    b_max: float = 1000.0,
    T_max: float = 200.0,
    prec: int = 30,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    eps_vals = np.logspace(eps_log_min, eps_log_max, n_eps)
    beta_vals = 0.5 + eps_vals
    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)

    print(f"[3K] Loading zeta zeros (T_max = {T_max}, prec = {prec})...")
    t0 = time.time()
    zeta_zeros = zeta_L.zeros(T_max=T_max, prec=prec)
    print(f"     {len(zeta_zeros)} zeros loaded in {time.time() - t0:.1f}s")

    n_g = len(gamma_vals)
    results = {
        "eps": eps_vals,
        "gamma": np.asarray(gamma_vals),
        "schur_min": np.full((n_eps, n_g), np.nan),
        "schur_max": np.full((n_eps, n_g), np.nan),
        "schur_rel_min": np.full((n_eps, n_g), np.nan),
        "schur_dim": np.zeros((n_eps, n_g), dtype=int),
        "M_min": np.full((n_eps, n_g), np.nan),
        "M_max": np.full((n_eps, n_g), np.nan),
        "M_rel_min": np.full((n_eps, n_g), np.nan),
    }

    total = n_eps * n_g
    done = 0
    for i, eps in enumerate(eps_vals):
        beta = 0.5 + eps
        for j, g0 in enumerate(gamma_vals):
            t0 = time.time()
            M_on, M_off = augmented_gram(zeta_zeros, b_vals, beta, g0, prec=prec)
            M = M_on + M_off
            S, _, _, _, r_dim = schur_complement(M_on, M_off)

            eig_M = np.linalg.eigvalsh(M)
            scale_M = max(abs(eig_M).max(), 1.0)
            results["M_min"][i, j] = float(eig_M.min())
            results["M_max"][i, j] = float(eig_M.max())
            results["M_rel_min"][i, j] = float(eig_M.min() / scale_M)

            if S.size > 0:
                eig_S = np.linalg.eigvalsh(S)
                scale_S = max(abs(eig_S).max(), 1e-300)  # avoid div by zero only
                results["schur_min"][i, j] = float(eig_S.min())
                results["schur_max"][i, j] = float(eig_S.max())
                results["schur_rel_min"][i, j] = float(eig_S.min() / scale_S)
                results["schur_dim"][i, j] = r_dim
            else:
                # M_off had no nontrivial eigenvalues: the injected zero is
                # numerically indistinguishable from on-line within float64.
                results["schur_min"][i, j] = 0.0
                results["schur_max"][i, j] = 0.0
                results["schur_rel_min"][i, j] = 0.0
                results["schur_dim"][i, j] = 0

            done += 1
            dt = time.time() - t0
            if done % 10 == 0 or done == total:
                print(f"  [{done:3d}/{total}] eps = {eps:.3e}, gamma = {g0:6.1f}: "
                      f"Schur rel min = {results['schur_rel_min'][i, j]:+.3e}  ({dt:.2f}s)")

    np.savez_compressed(out_dir / "e3k_hypothetical_offline.npz", **results,
                        T_max=T_max, K=K, prec=prec)

    # Plot: log-log slice plots + heatmap
    fig, axs = plt.subplots(2, 2, figsize=(13, 10))
    colors = plt.cm.viridis(np.linspace(0.1, 0.9, n_g))

    # Panel 1: |Schur rel min| vs epsilon, one curve per gamma
    ax = axs[0, 0]
    for j, g0 in enumerate(gamma_vals):
        vals = np.abs(results["schur_rel_min"][:, j])
        ax.loglog(eps_vals, vals, "o-", color=colors[j], label=f"gamma_0 = {g0:.0f}")
    # Predicted scaling: |Schur rel min| ~ eps^2
    ref_eps = eps_vals
    ref_y = (eps_vals / eps_vals[-1]) ** 2 * np.abs(results["schur_rel_min"][-1, 0])
    ax.loglog(ref_eps, ref_y, "k--", alpha=0.4, label=r"$\propto \varepsilon^2$ (predicted)")
    ax.set_xlabel(r"$\varepsilon = \beta - 1/2$")
    ax.set_ylabel(r"$|\lambda_{\min}(S)| / \lambda_{\max}(S)$")
    ax.set_title(r"Schur signal vs distance from line")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, which="both")

    # Panel 2: absolute |Schur min| vs epsilon (not relative)
    ax = axs[0, 1]
    for j, g0 in enumerate(gamma_vals):
        vals = np.abs(results["schur_min"][:, j])
        ax.loglog(eps_vals, vals, "o-", color=colors[j], label=f"gamma_0 = {g0:.0f}")
    ax.axhline(1e-12, color="r", lw=0.5, ls=":", label="numerical noise floor")
    ax.set_xlabel(r"$\varepsilon = \beta - 1/2$")
    ax.set_ylabel(r"$|\lambda_{\min}(S)|$ (absolute)")
    ax.set_title("Absolute Schur signal (stealth threshold)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, which="both")

    # Panel 3: heatmap of log10(|Schur rel min|)
    ax = axs[1, 0]
    Z = np.log10(np.abs(results["schur_rel_min"]) + 1e-30)
    im = ax.pcolormesh(
        np.log10(eps_vals), gamma_vals, Z.T,
        shading="nearest", cmap="viridis"
    )
    plt.colorbar(im, ax=ax, label=r"$\log_{10}|\lambda_{\min}(S)/\lambda_{\max}(S)|$")
    ax.set_xlabel(r"$\log_{10}(\beta - 1/2)$")
    ax.set_ylabel(r"$\gamma_0$ (height of injected zero)")
    ax.set_title("Stealth map: Schur rel min signal strength")

    # Panel 4: scaling exponent (slope of log|Schur rel min| vs log(eps))
    ax = axs[1, 1]
    # local slope between consecutive eps values
    for j, g0 in enumerate(gamma_vals):
        log_eps = np.log10(eps_vals)
        log_signal = np.log10(np.abs(results["schur_rel_min"][:, j]) + 1e-30)
        slopes = np.diff(log_signal) / np.diff(log_eps)
        eps_mid = np.sqrt(eps_vals[:-1] * eps_vals[1:])
        ax.semilogx(eps_mid, slopes, "o-", color=colors[j], label=f"gamma_0 = {g0:.0f}")
    ax.axhline(2.0, color="k", ls="--", alpha=0.5, label="predicted slope = 2")
    ax.set_xlabel(r"$\varepsilon = \beta - 1/2$")
    ax.set_ylabel("local log-log slope")
    ax.set_title(r"Scaling exponent vs $\varepsilon$ (predicted: 2)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, which="both")
    ax.set_ylim(0, 4)

    plt.tight_layout()
    plt.savefig(out_dir / "e3k_hypothetical_offline.png", dpi=140)
    plt.close()
    print(f"\n[3K] Saved {out_dir / 'e3k_hypothetical_offline.png'}")
    print(f"[3K] Saved {out_dir / 'e3k_hypothetical_offline.npz'}")

    # Summary
    print("\n[3K] Summary:")
    for j, g0 in enumerate(gamma_vals):
        print(f"\n  gamma_0 = {g0:.0f}:")
        for i in [0, n_eps // 4, n_eps // 2, 3 * n_eps // 4, n_eps - 1]:
            print(f"    eps = {eps_vals[i]:.3e}: "
                  f"|Schur rel min| = {abs(results['schur_rel_min'][i, j]):.3e}, "
                  f"|Schur min| = {abs(results['schur_min'][i, j]):.3e}")

    # Stealth threshold: where does |Schur rel min| drop below 1e-3 (10x noise)?
    threshold = 1e-3
    print(f"\n[3K] Stealth threshold (|Schur rel min| < {threshold:.0e}):")
    for j, g0 in enumerate(gamma_vals):
        below = np.abs(results["schur_rel_min"][:, j]) < threshold
        if below.any():
            eps_thresh = eps_vals[below.argmin() if not below.all() else 0]
            # First eps where signal exceeds threshold
            above = ~below
            if above.any():
                first_above = above.argmax()
                eps_critical = eps_vals[first_above]
                print(f"  gamma_0 = {g0:.0f}: stealth for eps < {eps_critical:.3e} "
                      f"(beta - 1/2 < {eps_critical:.3e})")
            else:
                print(f"  gamma_0 = {g0:.0f}: stealth across entire eps range tested")
        else:
            print(f"  gamma_0 = {g0:.0f}: no stealth in tested range "
                  f"(min |rel signal| = {abs(results['schur_rel_min'][:, j]).min():.2e})")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--eps-log-min", type=float, default=-10.0)
    parser.add_argument("--eps-log-max", type=float, default=-0.5)
    parser.add_argument("--n-eps", type=int, default=30)
    parser.add_argument("--gamma", type=float, nargs="+", default=[30.0, 60.0, 100.0, 140.0, 180.0])
    parser.add_argument("--K", type=int, default=300)
    parser.add_argument("--T-max", type=float, default=200.0)
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(
        eps_log_min=args.eps_log_min,
        eps_log_max=args.eps_log_max,
        n_eps=args.n_eps,
        gamma_vals=tuple(args.gamma),
        K=args.K,
        T_max=args.T_max,
        prec=args.prec,
    )
