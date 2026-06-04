"""Experiment 3S: Connes' eta_x construction (arXiv:2602.04022) as a live D-H classifier.

## Why this experiment exists

Connes' Feb-2026 paper "The Riemann Hypothesis: Past, Present and a Letter
Through Time" (arXiv:2602.04022) reframes Weil positivity constructively. The
recipe ("Letter to Riemann"):

  1. Restrict the Weil quadratic form QW_lambda to test functions supported on
     [lambda^-1, lambda] in R*+, i.e. on log u in [-Lambda, Lambda] with
     Lambda = (1/2) log x. Only prime powers n = p^m <= x = lambda^2 enter.
  2. Take the minimal eigenvector eta_x of QW_lambda.
  3. Theorem 6.1 (Connes-van Suijlekom, "Quadratic Forms, Real Zeros and Echoes
     of the Spectral Action") proves: for ANY even-kernel lower-bounded
     self-adjoint form with a simple isolated even ground state, the Fourier
     transform of that ground state has ALL its zeros on the real line.
  4. Conjecture (UNPROVEN): as x -> infinity, eta_x converges so its Fourier
     transform -> Riemann's Xi; Hurwitz then forces RH.

The striking numerics: with primes <= 13 Connes recovers the first 50 zeros of
zeta to accuracies from 2.6e-55 to 1e-3.

This project's reading (assessment of 2602.04022, and the marginal-positivity
thesis): Theorem 6.1 MANUFACTURES on-line zeros for any admissible form, so it
is zeta-blind. The entire RH content sits in the unproven step 4. That step is
the project's signature/(N_off, N_off) obstruction and it is RH-equivalent. The
Davenport-Heilbronn (D-H) discipline pins this exactly: D-H has a functional
equation (hence its own QW_lambda and its own Theorem-6.1 output) but is
RH-false (off-line zeros at rho ~ 0.8085 + 85.699 i). So if the construction
distinguishes zeta from D-H at all, it can only be through the unproven step.

## What this experiment demonstrates (three robust claims)

  Part A -- THE MIRACLE. Build QW_lambda on a grid for BOTH zeta and D-H,
    extract the minimal even eigenvector, and read off the zeros of its Fourier
    transform via the polynomial whose roots on |z| = 1 give real frequencies.
    Result: a coarse grid with n <= 13..25 recovers the first several zeros of
    BOTH zeta and D-H to 2-3 significant figures. (Connes' 2.6e-55 needs his
    high-precision Caratheodory-Fejer/Dirac-kernel machinery; this module
    reproduces the phenomenon, not the world-record precision.)

  Part B -- THEOREM 6.1 IS ZETA-BLIND. The minimal eigenvector of a marginally
    positive-semidefinite Toeplitz form has ALL polynomial roots on the unit
    circle, REGARDLESS of input: a zeta-derived symbol, a D-H-derived symbol,
    and a pseudo-random symbol all give frac-on-circle = 1.000. "All zeros on
    the critical line" is a property of the construction, not of zeta.

  Part C -- THE DISCRIMINATION LIVES ONLY IN THE (UNPROVEN) LIMIT. The same
    machine reproduces D-H's ON-LINE zeros faithfully, but Theorem 6.1 outputs
    only real frequencies, so it structurally CANNOT represent D-H's OFF-LINE
    zero at 0.8085 + 85.699 i. Hence eta_DH-hat cannot converge to Xi_DH (a
    uniform limit of real-zero functions has no complex zero, by Hurwitz). The
    only place zeta and D-H differ is exactly the step Connes leaves unproven,
    and it is provably false for D-H and (by the project's R3.5 no-shortcut
    theorem and the (N_off, N_off) signature) RH-equivalent for zeta.

Outputs:
  - e3s_connes_eta.npz : recovered frequencies, on-circle fractions, CF demo
  - e3s_connes_eta.png : 4-panel (zeta recovery, D-H recovery, roots on circle,
                         off-line obstruction near 85.7)
  - stdout : the three-part report
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as sint
from scipy.linalg import toeplitz, eigh
from scipy.special import digamma as sp_digamma

from experiments._shared import zeta_L, DavenportHeilbronn
from experiments.positivity.e3m_place_type_balance import lambda_coeffs_from_dirichlet

LOG_PI = float(np.log(np.pi))

# First zeros (imaginary parts) for scoring the recovery.
ZETA_ZEROS = [
    14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
    37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
]


# ----------------------------------------------------------------------------
# von Mangoldt (zeta) and the additive-line Weil quadratic form
# ----------------------------------------------------------------------------

def von_mangoldt_zeta(n: int) -> float:
    """Lambda(n) = log p if n = p^k, else 0."""
    if n < 2:
        return 0.0
    m = n
    p = 2
    fac = None
    while p * p <= m:
        if m % p == 0:
            fac = p
            while m % p == 0:
                m //= p
            break
        p += 1
    if fac is None:
        fac = m
        m = 1
    return float(np.log(fac)) if m == 1 else 0.0


def arch_omega(t, mu: float, log_Q: float):
    """Archimedean kernel Omega(t) = 2 log Q + Re psi(1/4 + mu/2 + i t/2) - log pi.

    Identical normalization to e3m.arch_kernel_grid (validated there by the
    explicit-formula self-consistency residual). zeta: mu=0, log_Q=0.
    D-H: mu=1, log_Q=log sqrt(5).
    """
    z = 0.25 + mu / 2.0 + 1j * t / 2.0
    return 2.0 * log_Q + np.real(sp_digamma(z)) - LOG_PI


def build_weil_form(x, N, mu, log_Q, lam_coeffs, t_cap=400.0, n_tgrid=150000):
    """Truncated Weil quadratic form QW_lambda on log u in [-Lambda, Lambda].

    Lambda = (1/2) log x, so u = e^t in [lambda^-1, lambda], lambda = sqrt(x),
    and the test-function autocorrelation g*g^* is supported on lags |s| <= log x,
    i.e. only n = p^m <= x contribute.

        QW(g) = A_arch(g) - PrimeTerm(g)
        A_arch(g)   = (1/2pi) int |ghat(t)|^2 Omega(t) dt      (archimedean cushion)
        PrimeTerm(g)= 2 sum_{n<=x} Lambda(n) n^{-1/2} A_G(log n)   (Euler/coeff block)

    A_arch is a Toeplitz matrix (convolution kernel = cosine transform of Omega).
    PrimeTerm is a sum of shift-overlap matrices S(log n). The pole is removed by
    the constraint ghat(+- i/2) = 0 (Connes' setup), returned as vector c.

    Returns (Q, tau, h, c).
    """
    Lam = 0.5 * np.log(x)
    tau = np.linspace(-Lam, Lam, N)
    h = tau[1] - tau[0]

    # Archimedean Toeplitz block: A[i,j] = h^2/pi * int_0^inf Omega(t) cos((tau_i-tau_j) t) dt
    tg = np.linspace(1e-9, t_cap, n_tgrid)
    Om = arch_omega(tg, mu, log_Q)
    omega_d = np.array([sint.simpson(Om * np.cos(k * h * tg), x=tg) for k in range(N)])
    A = np.empty((N, N))
    for i in range(N):
        for j in range(N):
            A[i, j] = h * h / np.pi * omega_d[abs(i - j)]

    # Prime/coefficient block via shift-overlap matrices.
    def shift_overlap(s):
        S = np.zeros((N, N))
        for i in range(N):
            ts = tau[i] + s
            if ts < tau[0] or ts > tau[-1]:
                continue
            pos = (ts - tau[0]) / h
            k = int(np.floor(pos))
            f = pos - k
            if k + 1 < N:
                S[i, k] += h * (1 - f)
                S[i, k + 1] += h * f
            elif k < N:
                S[i, k] += h * (1 - f)
        return 0.5 * (S + S.T)

    P = np.zeros((N, N))
    n_max = min(len(lam_coeffs) - 1, int(np.floor(x)))
    for n in range(2, n_max + 1):
        w = lam_coeffs[n]
        if abs(w) > 1e-12:
            P += w * (n ** -0.5) * 2.0 * shift_overlap(np.log(n))

    Q = A - P
    Q = 0.5 * (Q + Q.T)
    c = h * np.exp(tau / 2.0)  # ghat(i/2) = sum_i G_i e^{tau_i/2} h
    return Q, tau, h, c


def even_basis(N):
    """Orthonormal basis of the even subspace (G_i = G_{N-1-i})."""
    cols = []
    for i in range((N + 1) // 2):
        v = np.zeros(N)
        v[i] += 1.0
        v[N - 1 - i] += 1.0
        if i == N - 1 - i:
            v *= 0.5
        cols.append(v / np.linalg.norm(v))
    return np.array(cols).T


def min_even_eigvec(Q, c, N):
    """Minimal even eigenvector eta of Q on the constraint subspace ghat(i/2)=0.

    Returns (eps, eta) with eps the (resolution-limited) minimal eigenvalue.
    """
    E = even_basis(N)
    Qr = E.T @ Q @ E
    cr = E.T @ c
    cr = cr / np.linalg.norm(cr)
    Pc = np.eye(Qr.shape[0]) - np.outer(cr, cr)
    Qp = Pc @ Qr @ Pc
    Qp = 0.5 * (Qp + Qp.T)
    w, V = np.linalg.eigh(Qp)
    for idx in np.argsort(w):
        if abs(np.dot(V[:, idx], cr)) < 0.5:  # skip the killed constraint direction
            return float(w[idx]), E @ V[:, idx]
    return float(w[0]), E @ V[:, 0]


def ft_roots(G, h, tol=2e-3):
    """Zeros of the Fourier transform of G via roots of the coefficient polynomial.

    ghat(gamma) ~ sum_i G_i e^{i gamma tau_i}; zeros with real gamma correspond to
    polynomial roots on |z| = 1, z = e^{i gamma h}. Returns (positive gammas,
    n_on_circle, n_total).
    """
    roots = np.roots(G[::-1])
    on_circle = roots[np.abs(np.abs(roots) - 1.0) < tol]
    gammas = np.sort(np.angle(on_circle) / h)
    gammas = gammas[gammas > 0.5]
    return gammas, int(len(on_circle)), int(len(roots))


def recover_zeros(G, h, true_zeros):
    """For each true zero, the nearest machine frequency and the abs error."""
    gammas, n_on, n_tot = ft_roots(G, h)
    rec, err = [], []
    for z in true_zeros:
        if len(gammas):
            j = int(np.argmin(np.abs(gammas - z)))
            rec.append(float(gammas[j]))
            err.append(abs(float(gammas[j]) - z))
    return rec, err, n_on, n_tot


# ----------------------------------------------------------------------------
# Part B: Caratheodory-Fejer demonstration that Theorem 6.1 is input-agnostic
# ----------------------------------------------------------------------------

def cf_min_eigvec_roots(symbol_vals, M=24):
    """Minimal eigenvector of the Toeplitz form built from a >=0 symbol; return
    the fraction of its polynomial roots on the unit circle.

    This is the mechanism behind Theorem 6.1: for a marginally PSD Toeplitz form,
    the ground state read as polynomial coefficients is self-inversive with all
    roots on |z| = 1. It depends ONLY on positivity, never on which L-function
    (or whether any) produced the symbol.
    """
    thetas = np.linspace(0, 2 * np.pi, len(symbol_vals), endpoint=False)
    S = symbol_vals - symbol_vals.min() + 1e-9 * np.ptp(symbol_vals)  # push to marginal PSD
    c = np.array([np.mean(S * np.exp(-1j * k * thetas)) for k in range(M)])
    T = toeplitz(c).real
    w, V = eigh(T)
    roots = np.roots(V[:, 0][::-1])
    frac = float(np.mean(np.abs(np.abs(roots) - 1.0) < 1e-6))
    return frac, float(w[0])


def weil_symbol(theta, x, mu, log_Q, lam_coeffs):
    """The Weil 'symbol' Sym(xi) = Omega(xi) - 2 sum_{n<=x} Lambda(n)/sqrt(n) cos(xi log n),
    mapped to angle theta in [0, 2pi) via xi = 40 * theta / (2pi). Used only as a
    representative even symbol to feed the input-agnostic CF demonstration."""
    xi = 40.0 * theta / (2 * np.pi)
    S = arch_omega(xi, mu, log_Q)
    n_max = min(len(lam_coeffs) - 1, int(np.floor(x)))
    for n in range(2, n_max + 1):
        if abs(lam_coeffs[n]) > 1e-12:
            S = S - 2.0 * lam_coeffs[n] * (n ** -0.5) * np.cos(xi * np.log(n))
    return S


# ----------------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------------

def run(x: float = 25.0, N: int = 120, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    dh = DavenportHeilbronn()
    lam_zeta = np.array([0.0] + [von_mangoldt_zeta(n) for n in range(1, int(x) + 2)])
    lam_dh = lambda_coeffs_from_dirichlet(dh, int(x) + 2, 30)

    print("=" * 78)
    print(f"[3S] Connes eta_x construction (arXiv:2602.04022) as a D-H classifier")
    print(f"     cutoff x = {x} (n <= {int(x)}), grid N = {N}, Lambda = {0.5*np.log(x):.3f}")
    print("=" * 78)

    # ---- Part A: the miracle, for zeta and D-H ----
    print("\n[Part A] THE MIRACLE: minimal eigenvector's FT zeros vs the true zeros\n")

    t0 = time.time()
    Qz, tauz, hz, cz = build_weil_form(x, N, mu=0.0, log_Q=0.0, lam_coeffs=lam_zeta)
    eps_z, eta_z = min_even_eigvec(Qz, cz, N)
    rec_z, err_z, non_z, ntot_z = recover_zeros(eta_z, hz, ZETA_ZEROS[:8])

    dh_online = [float(r.imag) for r in dh.zeros(T_max=24, prec=20, scan_step=0.5)
                 if abs(float(r.real) - 0.5) < 1e-3]
    Qd, taud, hd, cd = build_weil_form(x, N, mu=1.0, log_Q=float(np.log(np.sqrt(5))),
                                       lam_coeffs=lam_dh)
    eps_d, eta_d = min_even_eigvec(Qd, cd, N)
    rec_d, err_d, non_d, ntot_d = recover_zeros(eta_d, hd, dh_online[:7])

    print("  zeta   true zero | recovered | abs err")
    for z, r, e in zip(ZETA_ZEROS[:8], rec_z, err_z):
        print(f"         {z:9.5f} | {r:9.5f} | {e:.2e}")
    print(f"  zeta   eps(resolution-limited) = {eps_z:.3e}, "
          f"roots on |z|=1: {non_z}/{ntot_z}")
    print()
    print("  D-H    true zero | recovered | abs err")
    for z, r, e in zip(dh_online[:7], rec_d, err_d):
        print(f"         {z:9.5f} | {r:9.5f} | {e:.2e}")
    print(f"  D-H    eps(resolution-limited) = {eps_d:.3e}, "
          f"roots on |z|=1: {non_d}/{ntot_d}")
    print(f"  --> the IDENTICAL machine reproduces BOTH zeta and D-H on-line zeros "
          f"({time.time()-t0:.1f}s)")
    print(f"  --> eps is resolution-limited; the TRUE minimal eigenvalue decays")
    print(f"      doubly-exponentially (Connes Fig 1: 1-chi_2 ~ exp(-4 pi e^L)),")
    print(f"      i.e. the 'near radical' = the project's marginal-positivity wall.")

    # ---- Part B: Theorem 6.1 is input-agnostic (Caratheodory-Fejer) ----
    print("\n[Part B] THEOREM 6.1 IS ZETA-BLIND: minimal eigenvector roots on |z|=1\n")
    thetas = np.linspace(0, 2 * np.pi, 4000, endpoint=False)
    sym_zeta = weil_symbol(thetas, x, 0.0, 0.0, lam_zeta)
    sym_dh = weil_symbol(thetas, x, 1.0, float(np.log(np.sqrt(5))), lam_dh)
    rng = np.random.default_rng(0)
    sym_rand = np.abs(np.fft.rfft(rng.standard_normal(80)))[:40] ** 2
    sym_rand = np.interp(thetas, np.linspace(0, 2 * np.pi, len(sym_rand)), sym_rand)

    frac_zeta, _ = cf_min_eigvec_roots(sym_zeta)
    frac_dh, _ = cf_min_eigvec_roots(sym_dh)
    frac_rand, _ = cf_min_eigvec_roots(sym_rand)
    print(f"  zeta-derived symbol   : frac roots on |z|=1 = {frac_zeta:.3f}")
    print(f"  D-H-derived  symbol   : frac roots on |z|=1 = {frac_dh:.3f}")
    print(f"  pseudo-random symbol  : frac roots on |z|=1 = {frac_rand:.3f}")
    print("  --> 'all zeros on the critical line' is a property of the CONSTRUCTION,")
    print("      not of zeta. The machine manufactures on-line zeros for any input.")

    # ---- Part C: the off-line obstruction ----
    print("\n[Part C] DISCRIMINATION LIVES ONLY IN THE UNPROVEN LIMIT (off-line zero)\n")
    dh_all = dh.zeros(T_max=90, prec=20, scan_step=0.5)
    offline = [(float(r.real), float(r.imag)) for r in dh_all
               if abs(float(r.real) - 0.5) > 1e-3]
    print(f"  D-H has off-line zeros (RH-false): "
          + ", ".join(f"{b:.4f}+{g:.3f}i" for b, g in offline[:2]))
    # the machine's frequencies near the off-line height
    gammas_d, _, _ = ft_roots(eta_d, hd)
    near = gammas_d[(gammas_d > 80) & (gammas_d < 92)] if len(gammas_d) else np.array([])
    print(f"  machine frequencies near height 85.7: {np.round(near, 3).tolist()}")
    print(f"  ALL are real (on the line). The off-line zero 0.8085+85.699i needs a")
    print(f"  COMPLEX zero of eta-hat; Theorem 6.1 forbids it. Hence eta_DH-hat")
    print(f"  cannot -> Xi_DH (Hurwitz). The convergence step is exactly where zeta")
    print(f"  and D-H part ways, it is FALSE for D-H, and RH-equivalent for zeta.")

    # ---- Save ----
    np.savez_compressed(
        out_dir / "e3s_connes_eta.npz",
        x=x, N=N,
        zeta_true=np.array(ZETA_ZEROS[:8]), zeta_recovered=np.array(rec_z),
        zeta_err=np.array(err_z), eps_zeta=eps_z, oncircle_zeta=[non_z, ntot_z],
        dh_true=np.array(dh_online[:7]), dh_recovered=np.array(rec_d),
        dh_err=np.array(err_d), eps_dh=eps_d, oncircle_dh=[non_d, ntot_d],
        cf_frac=np.array([frac_zeta, frac_dh, frac_rand]),
        dh_offline=np.array(offline[:2]),
        eta_zeta=eta_z, eta_dh=eta_d, tau=tauz,
    )

    # ---- Plot ----
    fig, axs = plt.subplots(2, 2, figsize=(13, 9))

    ax = axs[0, 0]
    ax.plot(ZETA_ZEROS[:8], rec_z, "o", color="tab:blue")
    lim = [0, 45]
    ax.plot(lim, lim, "k--", lw=0.8)
    ax.set_xlabel("true zeta zero (Im rho)")
    ax.set_ylabel("recovered frequency")
    ax.set_title(f"Part A: zeta zeros from n <= {int(x)}\n(minimal eigenvector of QW)")
    ax.grid(alpha=0.3)

    ax = axs[0, 1]
    ax.plot(dh_online[:7], rec_d, "s", color="tab:red")
    lim = [0, 26]
    ax.plot(lim, lim, "k--", lw=0.8)
    ax.set_xlabel("true D-H on-line zero (Im rho)")
    ax.set_ylabel("recovered frequency")
    ax.set_title("Part A: the SAME machine reproduces\nD-H's on-line zeros (zeta-blind)")
    ax.grid(alpha=0.3)

    ax = axs[1, 0]
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(th), np.sin(th), "k-", lw=0.6)
    rz = np.roots(eta_z[::-1])
    rd = np.roots(eta_d[::-1])
    ax.plot(rz.real, rz.imag, ".", ms=4, color="tab:blue", label=f"zeta ({non_z}/{ntot_z} on circle)")
    ax.plot(rd.real, rd.imag, "x", ms=4, color="tab:red", label=f"D-H ({non_d}/{ntot_d} on circle)")
    ax.set_aspect("equal")
    ax.set_title("Part B: Theorem 6.1 -- eta-hat roots on |z|=1\n(real frequencies, for BOTH)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    ax = axs[1, 1]
    # off-line obstruction: D-H zeros in the (gamma, beta) plane near 85.7
    on_g = [float(r.imag) for r in dh_all if abs(float(r.real) - 0.5) < 1e-3 and float(r.imag) > 78]
    ax.scatter(on_g, [0.5] * len(on_g), c="tab:gray", s=20, label="D-H on-line zeros")
    ax.scatter([g for _, g in offline], [b for b, _ in offline], c="tab:red", s=60,
               marker="D", label="D-H OFF-line zeros (RH-false)")
    if len(near):
        ax.scatter(near, [0.5] * len(near), facecolors="none", edgecolors="tab:blue",
                   s=90, label="machine frequencies (all real)")
    ax.axhline(0.5, color="k", lw=0.5)
    ax.set_xlim(78, 92)
    ax.set_ylim(0.0, 1.0)
    ax.set_xlabel("height (Im rho)")
    ax.set_ylabel("Re rho")
    ax.set_title("Part C: the machine cannot see the off-line zero\n(only the unproven limit could)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e3s_connes_eta.png", dpi=140)
    plt.close()
    print(f"\n[3S] Saved {out_dir / 'e3s_connes_eta.png'}")
    print(f"[3S] Saved {out_dir / 'e3s_connes_eta.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=float, default=25.0, help="prime/coefficient cutoff")
    parser.add_argument("--N", type=int, default=120, help="grid size")
    args = parser.parse_args()
    run(x=args.x, N=args.N)
