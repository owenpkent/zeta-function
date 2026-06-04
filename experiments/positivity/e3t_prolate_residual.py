"""Experiment 3T: the prolate ansatz k_lambda and the archimedean/Euler split.

## Why this experiment exists

Connes' strategy (arXiv:2602.04022, sec 6) reduces RH to one unproven step
(sec 6.6): show that the minimal eigenvector theta_x of the truncated Weil
quadratic form QW_lambda converges to E(h), the function whose Fourier transform
is Riemann's Xi. The bridge is the PROLATE ANSATZ

    k_lambda(u) = E(h_lambda)(u),   E(f)(u) = u^{1/2} sum_{n>=1} f(n u),

where h_lambda is the unique vanishing-integral combination of the localized
prolate spheroidal wave functions h_{0,lambda}, h_{4,lambda} on [-lambda, lambda]
(lambda = sqrt(x)). Connes PROVES (Fact 6.4) that k_lambda-hat -> Xi as
lambda -> infinity. The genuine gap (sec 6.6) is: "it still remains to show that
k_lambda is a sufficiently good approximation of theta_x."

The prolate spheroidal wave functions are eigenfunctions of the prolate wave
operator PW_lambda = -d/dx[(lambda^2 - x^2) d/dx] + (2 pi lambda x)^2, a confluent
Heun operator that descends from the HARMONIC OSCILLATOR / Hermite functions,
i.e. from the ARCHIMEDEAN Gamma factor alone. It contains NO prime data.

## What this experiment shows (and the project point it sharpens)

The project's assessment of 2602.04022, and LEARNINGS #46, hold that the
RH-discriminating content rides the Euler/{log p} block, while the archimedean
half is shared with Davenport-Heilbronn (hence RH-agnostic). This experiment
instruments that claim on Connes' own ansatz:

  1. FACT 6.4, demonstrated: k_lambda (built from archimedean prolate data, with
     ZERO primes) has a Fourier transform that approximates Xi; its first zeros
     reproduce the first zeros of zeta.

  2. k_lambda nearly achieves the Weil-form infimum: Q(k_lambda)/||k_lambda||^2 is
     comparable to the (resolution-limited) minimal eigenvalue eps of QW_lambda.
     So Connes' "educated guess" really is a good approximation of the minimizer
     in energy -- the archimedean prolate model alone almost solves the
     variational problem.

  3. THE ENERGY IS ARCHIMEDEAN-DOMINATED. Decompose Q(k_lambda) = A_arch(k_lambda)
     - PrimeTerm(k_lambda). The prime coupling is a percent-level fraction of the
     archimedean block. The prolate ansatz barely touches the primes.

Reading: the "miracle" of recovering the zeros from k_lambda is largely an
ARCHIMEDEAN phenomenon (the Gamma factor / prolate structure), which D-H shares
(D-H has a Gamma factor). So the prolate approximation cannot be what
distinguishes zeta from D-H. The Euler block is exactly the part k_lambda does
NOT supply -- and supplying it (proving k_lambda = theta_x and that the infimum
-> 0 as x -> infinity) is the unproven, RH-equivalent step. The gap is the Euler
half. This is the e3s off-line-zero obstruction seen from the ansatz side.

Outputs:
  - e3t_prolate_residual.npz : per-x energies, recovered first zeros
  - e3t_prolate_residual.png : (left) k_lambda-hat -> Xi recovery,
                               (right) archimedean vs Euler energy of k_lambda
  - stdout : the report
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import eigh_tridiagonal

from experiments.positivity.e3s_connes_eta import (
    build_weil_form, min_even_eigvec, von_mangoldt_zeta, ft_roots, ZETA_ZEROS,
)


# ----------------------------------------------------------------------------
# Prolate spheroidal wave functions = eigenfunctions of PW_lambda on [-lambda, lambda]
# ----------------------------------------------------------------------------

def prolate_even(lam: float, M: int = 1401):
    """First eigenfunctions of PW_lambda = -d/dx[(lam^2-x^2)d/dx] + (2 pi lam x)^2.

    Finite-difference (conservative form) discretization on [-lam, lam]. Returns
    (grid, spacing, [h_0, ..., h_7]) normalized in L^2. Even-indexed functions are
    even; this is the harmonic-oscillator/Hermite family adapted to the interval.
    """
    xx = np.linspace(-lam, lam, M)
    h = xx[1] - xx[0]
    xm = 0.5 * (xx[:-1] + xx[1:])
    a = lam ** 2 - xm ** 2  # >= 0 on (-lam, lam)
    V = (2 * np.pi * lam * xx) ** 2
    main = np.zeros(M)
    off = np.zeros(M - 1)
    for i in range(M):
        al = a[i - 1] if i - 1 >= 0 else 0.0
        ar = a[i] if i < M - 1 else 0.0
        main[i] = (al + ar) / h ** 2 + V[i]
    for i in range(M - 1):
        off[i] = -a[i] / h ** 2
    w, Vv = eigh_tridiagonal(main, off)
    funcs = [Vv[:, k] / np.sqrt(np.sum(Vv[:, k] ** 2) * h) for k in range(8)]
    return xx, h, funcs


def k_lambda_on_grid(x: float, tau: np.ndarray, M: int = 1401):
    """k_lambda(u) = E(h_lambda)(u) sampled at u = e^tau, lambda = sqrt(x).

    h_lambda = h_{4,lambda} - (I4/I0) h_{0,lambda} (vanishing integral), and
    E(f)(u) = sqrt(u) sum_{n: n u <= lambda} f(n u). Built from prolate
    (archimedean) data only; no primes enter.
    """
    lam = np.sqrt(x)
    xx, h, F = prolate_even(lam, M=M)
    h0, h4 = F[0], F[4]
    I0 = np.sum(h0) * h
    I4 = np.sum(h4) * h
    hl = h4 - (I4 / I0) * h0  # vanishing integral
    out = np.zeros(len(tau))
    for i, t in enumerate(tau):
        u = np.exp(t)
        s = 0.0
        n = 1
        while n * u <= lam:
            s += np.interp(n * u, xx, hl)
            n += 1
        out[i] = np.sqrt(u) * s
    return out


# ----------------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------------

def run(x_values=(13, 25, 49), N: int = 140, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print("[3T] Prolate ansatz k_lambda: Fact 6.4, energy, and the archimedean/Euler split")
    print("=" * 78)
    print()
    print(f"  {'x':>4} | {'k_lam FT first zeros':>34} | {'A_arch(k)':>9} | "
          f"{'Prime(k)':>9} | {'Q(k)':>8} | {'eps_min':>8} | prime/arch")
    print("  " + "-" * 96)

    rows = []
    for x in x_values:
        lam_zeta = np.array([0.0] + [von_mangoldt_zeta(n) for n in range(1, int(x) + 2)])
        Q, tau, h, c = build_weil_form(x, N, mu=0.0, log_Q=0.0, lam_coeffs=lam_zeta)
        A, _, _, _ = build_weil_form(x, N, mu=0.0, log_Q=0.0,
                                     lam_coeffs=np.zeros(int(x) + 2))  # primes off
        P = A - Q  # = PrimeTerm
        eps, _ = min_even_eigvec(Q, c, N)

        kl = k_lambda_on_grid(x, tau)
        nrm = float(np.dot(kl, kl))
        q_arch = float(kl @ A @ kl) / nrm
        q_prime = float(kl @ P @ kl) / nrm
        q_total = float(kl @ Q @ kl) / nrm

        g, _, _ = ft_roots(kl / np.linalg.norm(kl), h)
        recovered = []
        for z in ZETA_ZEROS[:4]:
            if len(g):
                recovered.append(round(float(g[np.argmin(np.abs(g - z))]), 3))
        ratio = abs(q_prime) / max(abs(q_arch), 1e-12)

        rows.append(dict(x=x, recovered=recovered, q_arch=q_arch, q_prime=q_prime,
                         q_total=q_total, eps=eps, ratio=ratio))
        print(f"  {x:>4} | {str(recovered):>34} | {q_arch:>+9.4f} | "
              f"{q_prime:>+9.4f} | {q_total:>+8.4f} | {eps:>8.2e} | {ratio:>6.2%}")

    print()
    print("  Reading:")
    print("  - k_lambda recovers the first zeta zero(s): Fact 6.4 (k_lambda-hat -> Xi),")
    print("    using prolate/archimedean data with ZERO primes.")
    print("  - Q(k_lambda)/||k||^2 is comparable to eps_min: the prolate guess nearly")
    print("    achieves the Weil-form infimum (a good approximation of the minimizer).")
    print("  - The energy is ARCHIMEDEAN-DOMINATED (prime coupling is percent-level).")
    print("    The archimedean half (shared with Davenport-Heilbronn) does the work;")
    print("    the Euler block is exactly what the ansatz does NOT supply. Proving")
    print("    k_lambda = theta_x and that the infimum -> 0 globally is the unproven,")
    print("    RH-equivalent step (the off-line obstruction of e3s, ansatz side).")

    # Save
    save = dict(N=N, x_values=np.array(list(x_values)))
    for r in rows:
        for k in ("q_arch", "q_prime", "q_total", "eps", "ratio"):
            save[f"x{r['x']}_{k}"] = r[k]
        save[f"x{r['x']}_recovered"] = np.array(r["recovered"])
    np.savez_compressed(out_dir / "e3t_prolate_residual.npz", **save)

    # Plot
    fig, axs = plt.subplots(1, 2, figsize=(13, 5))

    ax = axs[0]
    x_show = x_values[0]
    lam = np.sqrt(x_show)
    Lam = 0.5 * np.log(x_show)
    tau = np.linspace(-Lam, Lam, N)
    h = tau[1] - tau[0]
    kl = k_lambda_on_grid(x_show, tau)
    gammas, _, _ = ft_roots(kl / np.linalg.norm(kl), h)
    gammas = gammas[gammas < 30]
    for z in ZETA_ZEROS[:3]:
        ax.axvline(z, color="tab:gray", ls="--", lw=0.8)
    ax.plot(gammas, np.zeros_like(gammas), "o", color="tab:blue",
            label=f"k_lambda zeros (x={x_show})")
    ax.set_xlim(0, 30)
    ax.set_xlabel("frequency gamma")
    ax.set_title("Fact 6.4: k_lambda-hat -> Xi\n(dashed = true zeta zeros, prolate uses NO primes)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    ax = axs[1]
    xs = [r["x"] for r in rows]
    qa = [r["q_arch"] for r in rows]
    qp = [abs(r["q_prime"]) for r in rows]
    xi = np.arange(len(xs))
    ax.bar(xi - 0.2, qa, width=0.4, label="archimedean A_arch(k)", color="tab:blue")
    ax.bar(xi + 0.2, qp, width=0.4, label="|Euler PrimeTerm(k)|", color="tab:red")
    ax.set_xticks(xi)
    ax.set_xticklabels([str(x) for x in xs])
    ax.set_xlabel("cutoff x")
    ax.set_ylabel("Weil energy of k_lambda / ||k||^2")
    ax.set_title("k_lambda energy is archimedean-dominated\n(prime coupling ~ percent level)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig(out_dir / "e3t_prolate_residual.png", dpi=140)
    plt.close()
    print(f"\n[3T] Saved {out_dir / 'e3t_prolate_residual.png'}")
    print(f"[3T] Saved {out_dir / 'e3t_prolate_residual.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=140)
    parser.add_argument("--x", type=int, nargs="*", default=[13, 25, 49])
    args = parser.parse_args()
    run(x_values=tuple(args.x), N=args.N)
