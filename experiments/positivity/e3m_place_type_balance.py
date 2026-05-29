"""Experiment 3M: the INPUT-SIDE place-type decomposition of Weil's quadratic form.

## Why this experiment exists

The project's sharpest positivity result to date is the Schur "two-clock"
decomposition (LEARNINGS #18): split the Weil Gram matrix as M = M_on + M_off
and show the on-line cushion must dominate the off-line obstruction. That split
is ANSWER-SIDE: it sorts each zero's contribution by WHERE the zero sits
(Re rho = 1/2 vs not). As a route to a proof this is circular, since you may
not use the location of the zeros to prove the location of the zeros. Finding
#19 recorded the consequence: the disproof angle in the Gram-matrix family has
"no leverage point", and a productive attack needs a fundamentally different,
non-circular diagnostic.

This experiment provides one. The SAME quadratic form

    M_ij = sum_rho Phi_{b_i}(rho) Phi_{b_j}(rho)              (zero side)

decomposes a SECOND way, by PLACE TYPE, via Weil's explicit formula:

    M = A_arch  +  P_fin  +  B_pole
        |           |          |
     Gamma-factor  Dirichlet   poles of the
     (archimedean  coefficients completed L
      digamma      (Euler /     (zeta & Epstein
      kernel)       prime side)  have them; D-H
                                 is entire -> 0)

Every block here is computable FROM THE GAMMA FACTOR AND THE DIRICHLET
COEFFICIENTS ALONE, without ever locating a single zero. That is the whole
point: it is an input-side decomposition, legitimate for a proof.

A_arch is a manifestly positive-semidefinite quadratic form (a positive kernel
Omega_L(t) integrated against |test|^2). P_fin is the indefinite piece. The
Weil criterion M >= 0 (<=> RH) becomes:

    the archimedean cushion A_arch must dominate the finite obstruction -(P_fin + B_pole).

We quantify domination with the generalized eigenvalue of the pencil
(-(P+B), A):

    lambda_max := max_c  c^T (-(P_fin + B_pole)) c / c^T A_arch c .

Then M >= 0  <=>  lambda_max <= 1. Define the ARCHIMEDEAN BALANCE

    balance := 1 / lambda_max .

balance >= 1  : archimedean cushion wins -> RH-compatible positivity.
balance <  1  : finite obstruction wins in some direction -> M indefinite.

This is the exact analogue of finding #18's "two-clock balance must beat 1.0",
but with the legitimate ARCHIMEDEAN-vs-FINITE split (input-side) in place of the
circular ON-vs-OFF split (answer-side).

## The discriminator and why it engages exact zeta structure

For zeta the finite block is concentrated on prime powers with von Mangoldt
weight Lambda(n) = log p >= 0 (the Euler product). For Davenport-Heilbronn there
is NO Euler product, so the analogue Lambda_DH(n) (coefficients of -f'/f) is
supported on ALL n with mixed signs, and D-H is entire so its pole block
vanishes. Prediction:

    balance(zeta)  >= 1     (input-side certificate of positivity)
    balance(D-H)   <  1     (input-side detection of the off-line failure)

detected WITHOUT inputting any zero. If it holds, this is the project's first
place-type (rather than zero-location) discriminator -- the "fundamentally
different diagnostic" finding #19 said was required.

## Self-consistency check (the experiment validates itself)

Because A + P + B is literally Weil's explicit formula for M, we compute M
independently from the zeros and report the residual ||A + P + B - M|| / ||M||.
A small residual certifies that the archimedean kernel, the conductor, the
finite coefficients, and the pole block are all normalized correctly. The
discriminator is only trustworthy on an L-function whose residual is small.

Test family: Phi_b(s) = 2 sinh((s-1/2) log b)/(s-1/2), the same Mellin-symmetric
boxcar family used in 3C-3J. On the line, Phi_b(1/2+it) = 2 sin(t log b)/t is the
Fourier transform of the additive indicator h_b = 1_{[-log b, log b]}, so the
finite block uses the cross-correlation overlap of two such indicators.

Outputs:
  - e3m_place_type_balance.npz : per-L blocks, residuals, balances
  - e3m_place_type_balance.png : balance bar chart + block spectra
  - stdout : per-L table
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
import scipy.integrate as sint
from scipy.special import digamma as sp_digamma

from experiments._shared import (
    zeta_L,
    DavenportHeilbronn,
    epstein_for_discriminant,
)
from experiments.positivity.e3c_weil_form import phi_b


# ----------------------------------------------------------------------------
# Test-function geometry (additive picture)
# ----------------------------------------------------------------------------

def overlap(Li: float, Lj: float, v: float) -> float:
    """(h_{b_i} * h_{b_j})(v): overlap length of [-Li, Li] and [v-Lj, v+Lj].

    h_b is the indicator of [-log b, log b] (so L = log b). The cross-
    correlation is even in v and supported on |v| <= Li + Lj. At v = 0 it is
    2 min(Li, Lj); its peak.
    """
    lo = max(-Li, v - Lj)
    hi = min(Li, v + Lj)
    return max(0.0, hi - lo)


# ----------------------------------------------------------------------------
# Archimedean block A_arch (digamma kernel, computed from the Gamma factor)
# ----------------------------------------------------------------------------

def arch_kernel_grid(mu_list, log_Q, t):
    """Omega_L(t) = 2 log Q + sum_j [ Re psi(1/4 + mu_j/2 + i t/2) - log pi ],
    vectorized over a numpy array t via scipy's complex digamma.

    This is the archimedean spectral density of the completed L-function with
    Gamma factor  Q^s prod_j Gamma_R(s + mu_j),  Gamma_R(s) = pi^{-s/2} Gamma(s/2).
    Derivation: the explicit-formula archimedean term is
        (1/2pi) int g-hat(t) [ 2 Re (gamma_inf'/gamma_inf)(1/2 + i t) ] dt
    and (gamma_inf'/gamma_inf)(s) = sum_j [ (1/2) psi((s+mu_j)/2) - (1/2) log pi ],
    plus the conductor's log Q (constant). Evaluated at s = 1/2 + i t this gives
    the kernel above.
    """
    log_pi = float(np.log(np.pi))
    omega = np.full_like(t, 2.0 * float(log_Q))
    z_base = 0.25 + 1j * t / 2.0
    for mu in mu_list:
        omega = omega + np.real(sp_digamma(z_base + float(mu) / 2.0)) - log_pi
    return omega


def arch_block(b_vals, mu_list, log_Q, prec: int, t_cap: float, n_grid: int = 200000):
    """A_ij = (1/2pi) int_R Phi_{b_i}(1/2+it) Phi_{b_j}(1/2+it) Omega_L(t) dt.

    Phi_b(1/2+it) = 2 sin(t log b)/t (real, even), so the integrand is even and
    A_ij = (4/pi) int_0^inf sin(t L_i) sin(t L_j) / t^2 * Omega_L(t) dt with
    L = log b. The integrand is finite at t = 0 (-> L_i L_j Omega(0)) and decays
    like Omega(t)/t^2 ~ log t / t^2, so it is integrable.

    Implementation: Omega_L(t) is shared by every matrix entry, so we evaluate it
    once on a dense uniform grid on [0, t_cap] with vectorized complex digamma and
    Simpson-integrate each entry. The grid must resolve the fastest oscillation
    sin(t (L_i + L_j)) (period 2 pi / (2 log b_max)); n_grid is chosen large enough
    that t_cap / n_grid << that period.
    """
    K = len(b_vals)
    Ls = np.array([float(np.log(b)) for b in b_vals])
    t = np.linspace(0.0, float(t_cap), n_grid)
    omega = arch_kernel_grid(mu_list, log_Q, t)

    # sin(t L)/t for each b, with the t=0 limit = L.
    sinc = np.empty((K, n_grid))
    with np.errstate(divide="ignore", invalid="ignore"):
        for k in range(K):
            s = np.sin(t * Ls[k]) / t
            s[0] = Ls[k]
            sinc[k] = s

    A = np.zeros((K, K))
    for i in range(K):
        for j in range(i, K):
            integrand = sinc[i] * sinc[j] * omega   # = sin(tLi)sin(tLj)/t^2 * Omega
            val = sint.simpson(integrand, x=t)
            A_ij = 4.0 / np.pi * val
            A[i, j] = A_ij
            A[j, i] = A_ij
    return A


# ----------------------------------------------------------------------------
# Finite block P_fin (Dirichlet coefficients -> von Mangoldt analogue)
# ----------------------------------------------------------------------------

def von_mangoldt_zeta(n: int):
    """Lambda(n) = log p if n = p^k, else 0."""
    if n < 2:
        return 0.0
    m = n
    p = 2
    factor = None
    while p * p <= m:
        if m % p == 0:
            factor = p
            while m % p == 0:
                m //= p
            break
        p += 1
    if factor is None:
        factor = m
        m = 1
    return float(np.log(factor)) if m == 1 else 0.0


def lambda_coeffs_from_dirichlet(L, n_max: int, prec: int):
    """Lambda_L(n), coefficients of -L'/L(s) = sum Lambda_L(n) n^{-s}, from the
    Dirichlet coefficients a_n via the recursion

        a_n log n = sum_{d | n} Lambda_L(d) a_{n/d}.

    With a_1 = L.dirichlet_coefficient(1) (need not be 1; the recursion handles
    any nonzero a_1). Returns a float array Lambda[1..n_max] (index 0 unused).

    For an L-function WITHOUT an Euler product (D-H, non-principal Epstein), the
    resulting Lambda_L(n) is supported on ALL n (not just prime powers) and has
    mixed signs. That delocalization is exactly the structural fingerprint of the
    missing Euler product that this experiment is built to see.
    """
    mp.mp.dps = prec
    a = [mp.mpf(0)] * (n_max + 1)
    for n in range(1, n_max + 1):
        a[n] = mp.mpc(L.dirichlet_coefficient(n)).real  # real for our targets
    a1 = a[1]
    if abs(a1) < mp.mpf(10) ** (-prec + 5):
        raise ValueError(f"{L.name}: a_1 = {a1} too small to invert")
    Lam = [mp.mpf(0)] * (n_max + 1)
    for n in range(2, n_max + 1):
        acc = a[n] * mp.log(n)
        d = 1
        while d * d <= n:
            if n % d == 0:
                if d >= 2:
                    acc -= Lam[d] * a[n // d]
                e = n // d
                if e != d and e >= 2:
                    acc -= Lam[e] * a[n // e]
            d += 1
        Lam[n] = acc / a1
    return np.array([float(x) for x in Lam])


def finite_block(b_vals, lam, prec: int):
    """P_ij = - sum_n Lambda_L(n) n^{-1/2} * 2 (h_{b_i} * h_{b_j})(log n).

    lam is the array of Lambda_L(n) (von-Mangoldt analogue). The overlap is zero
    for log n > L_i + L_j, i.e. n > b_i b_j, so the sum is finite.
    """
    K = len(b_vals)
    Ls = [float(np.log(b)) for b in b_vals]
    P = np.zeros((K, K))
    n_max = len(lam) - 1
    log_n = np.array([0.0] + [float(np.log(n)) for n in range(1, n_max + 1)])
    inv_sqrt = np.array([0.0] + [1.0 / np.sqrt(n) for n in range(1, n_max + 1)])
    for i in range(K):
        for j in range(i, K):
            cap = Ls[i] + Ls[j]
            s = 0.0
            for n in range(2, n_max + 1):
                if log_n[n] > cap:
                    break
                if lam[n] == 0.0:
                    continue
                s += lam[n] * inv_sqrt[n] * 2.0 * overlap(Ls[i], Ls[j], log_n[n])
            P[i, j] = -s
            P[j, i] = -s
    return P


# ----------------------------------------------------------------------------
# Pole block B_pole (residue-weighted; zero for entire L)
# ----------------------------------------------------------------------------

def pole_block(b_vals, residue: float, prec: int):
    """B_ij = residue * (Phi_{b_i}(1) Phi_{b_j}(1) + Phi_{b_i}(0) Phi_{b_j}(0)).

    For the completed L with simple poles at s = 0, 1 (zeta: residue 1; Epstein:
    its own residue; D-H: entire -> residue 0). Phi_b(0) = Phi_b(1), so this is
    2 * residue * Phi_b_i(1) Phi_b_j(1).
    """
    if residue == 0.0:
        return np.zeros((len(b_vals), len(b_vals)))
    mp.mp.dps = prec
    phi1 = np.array([float(phi_b(mp.mpf(b), mp.mpf(1), prec=prec)) for b in b_vals])
    return residue * 2.0 * np.outer(phi1, phi1)


# ----------------------------------------------------------------------------
# Zero-side Gram matrix M (the independent ground truth for the self-check)
# ----------------------------------------------------------------------------

def gram_zero_side(L, b_vals, T_max: float, prec: int):
    """M_ij = sum_rho Phi_{b_i}(rho) Phi_{b_j}(rho), zeros paired with conjugates."""
    mp.mp.dps = prec
    rhos = L.zeros(T_max=T_max, prec=prec)
    K = len(b_vals)
    table = np.empty((K, len(rhos)), dtype=np.complex128)
    for k, b in enumerate(b_vals):
        b_mp = mp.mpf(b)
        for r, rho in enumerate(rhos):
            table[k, r] = complex(phi_b(b_mp, rho, prec=prec))
    M = np.zeros((K, K))
    for r in range(len(rhos)):
        col = table[:, r]
        M += 2.0 * np.real(np.outer(col, col))  # rho + conjugate
    return 0.5 * (M + M.T), len(rhos)


# ----------------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------------

def numeric_residue_at_one(L, prec: int):
    """Residue of the COMPLETED L at s = 1, via res(L, 1) propagated through the
    Gamma factor. For zeta the completed xi has residue 1 at s=1. We compute the
    raw residue r0 = lim (s-1) L(s) numerically and scale by the archimedean /
    conductor factor so the pole block matches the explicit-formula convention.

    For our purposes we only need this for Epstein; zeta and D-H are handled by
    the known values (1 and 0). Returned value is the coefficient 'residue' that
    multiplies (Phi(0)Phi(0) + Phi(1)Phi(1)) in B_pole.
    """
    mp.mp.dps = prec
    eps = mp.mpf(10) ** (-prec // 3)
    r0 = (eps) * L.evaluate(1 + eps)
    return float(r0.real)


def run(
    K: int = 10,
    b_min: float = 1.3,
    b_max: float = 6.0,
    T_max: float = 200.0,
    prec: int = 30,
    t_cap: float = 500.0,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)
    n_max = int(b_max * b_max) + 2  # overlap support: n <= b_i b_j <= b_max^2

    dh = DavenportHeilbronn()
    eps47 = epstein_for_discriminant(47, principal=False)        # off-line control
    eps47p = epstein_for_discriminant(47, principal=True)        # Selberg-like contrast

    # (L, mu_list, log_Q, residue, has_euler, label)
    targets = [
        ("zeta", zeta_L, [0.0], mp.mpf(0), 1.0, True),
        ("DH",   dh,     [1.0], mp.log(mp.sqrt(5)), 0.0, False),
        ("Eps47_offline",   eps47,  [0.0, 1.0], mp.log(mp.sqrt(47)), None, False),
        ("Eps47_principal", eps47p, [0.0, 1.0], mp.log(mp.sqrt(47)), None, True),
    ]

    print(f"[3M] Input-side place-type decomposition of Weil's form")
    print(f"     K={K}, b in [{b_min}, {b_max}], n_max={n_max}, T_max={T_max}, "
          f"prec={prec}, t_cap={t_cap}")
    print()

    results = {}
    for name, L, mu_list, log_Q, residue, has_euler in targets:
        print(f"  --- {name} (Euler product: {has_euler}) ---")
        t0 = time.time()

        # Finite block from Dirichlet coefficients (input side).
        if has_euler and name == "zeta":
            lam = np.array([0.0] + [von_mangoldt_zeta(n) for n in range(1, n_max + 1)])
        else:
            try:
                lam = lambda_coeffs_from_dirichlet(L, n_max, prec)
            except Exception as e:
                print(f"      finite block FAILED: {e}")
                continue
        P = finite_block(b_vals, lam, prec)

        # Archimedean block from the Gamma factor (input side).
        n_grid = max(200000, int(t_cap * 500))
        A = arch_block(b_vals, mu_list, log_Q, prec, t_cap, n_grid=n_grid)

        # Pole block.
        if residue is None:
            residue = numeric_residue_at_one(L, prec)
        B = pole_block(b_vals, float(residue), prec)

        # Zero side ground truth (used ONLY for the self-consistency residual).
        M_zero, n_zeros = gram_zero_side(L, b_vals, T_max, prec)

        M_recon = A + P + B
        resid = np.linalg.norm(M_recon - M_zero) / max(np.linalg.norm(M_zero), 1e-30)

        # Primary diagnostic: the INPUT-SIDE minimum eigenvalue of the Weil Gram
        # matrix. This is the same positivity test 3C-3J ran on the zero side,
        # now reconstructed purely from the Gamma factor + Dirichlet coefficients.
        # rel_min < 0 with magnitude above the residual = an off-line failure
        # DETECTED WITHOUT LOCATING ANY ZERO.
        eig_M_recon = np.linalg.eigvalsh(M_recon)
        eig_M_zero = np.linalg.eigvalsh(M_zero)
        eig_A = np.linalg.eigvalsh(A)
        eig_P = np.linalg.eigvalsh(P)
        recon_rel_min = eig_M_recon.min() / max(abs(eig_M_recon).max(), 1e-30)
        zero_rel_min = eig_M_zero.min() / max(abs(eig_M_zero).max(), 1e-30)
        # A clean detection requires the input-side negativity to exceed the
        # reconstruction error floor.
        detected_offline = bool(recon_rel_min < -resid)

        lam_beyond = int(
            sum(1 for n in range(2, n_max + 1)
                if abs(lam[n]) > 1e-9 and von_mangoldt_zeta(n) == 0.0)
        )

        results[name] = dict(
            mu_list=mu_list, log_Q=float(log_Q), residue=float(residue),
            has_euler=has_euler, n_zeros=n_zeros, resid=resid,
            recon_rel_min=float(recon_rel_min),
            zero_rel_min=float(zero_rel_min),
            detected_offline=detected_offline,
            A_min=float(eig_A.min()), A_max=float(eig_A.max()),
            P_min=float(eig_P.min()), P_max=float(eig_P.max()),
            lam_neg_count=int((lam < -1e-9).sum()),
            lam_support_beyond_primes=lam_beyond,
        )
        r = results[name]
        print(f"      self-check ||A+P+B - M||/||M|| = {resid:.3e}  "
              f"({'fidelity OK' if resid < 0.02 else 'COARSE'})")
        print(f"      Lambda_L support beyond prime powers: "
              f"{r['lam_support_beyond_primes']} (Euler product => 0)")
        print(f"      zero-side    rel min eig(M)      = {zero_rel_min:+.4e}")
        print(f"      INPUT-SIDE   rel min eig(A+P+B)  = {recon_rel_min:+.4e}  "
              f"(reconstructed from Gamma factor + coefficients, no zeros)")
        print(f"      off-line failure detected input-side: {detected_offline}  "
              f"(needs |rel min| > residual {resid:.2e})   [{time.time()-t0:.1f}s]")
        print()

    # Save
    save = dict(K=K, b_vals=b_vals, T_max=T_max, prec=prec, t_cap=t_cap)
    for name, r in results.items():
        for k, v in r.items():
            if k == "mu_list":
                v = np.array(v)
            save[f"{name}_{k}"] = v
    np.savez_compressed(out_dir / "e3m_place_type_balance.npz", **save)

    # Plot: input-side vs zero-side min eigenvalue + self-consistency residual
    names = list(results.keys())
    fig, axs = plt.subplots(1, 2, figsize=(13, 5))

    ax = axs[0]
    x = np.arange(len(names))
    zr = [results[n]["zero_rel_min"] for n in names]
    rr = [results[n]["recon_rel_min"] for n in names]
    ax.bar(x - 0.2, zr, width=0.4, label="zero side (uses zeros)", color="tab:gray")
    ax.bar(x + 0.2, rr, width=0.4, label="INPUT side (Gamma + coeffs, no zeros)",
           color=["tab:red" if v < 0 else "tab:blue" for v in rr])
    ax.axhline(0.0, color="k", lw=1.0)
    ax.set_xticks(x); ax.set_xticklabels(names, rotation=30)
    ax.set_ylabel("rel min eigenvalue of Weil Gram matrix")
    ax.set_title("Positivity test: zero side vs INPUT side\n(negative = off-line failure; red = detected from structure alone)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    ax = axs[1]
    resids = [results[n]["resid"] for n in names]
    ax.bar(names, resids, color="tab:gray")
    ax.axhline(0.02, color="k", lw=1.0, ls="--", label="fidelity target 2%")
    ax.set_yscale("log")
    ax.set_ylabel("||A + P + B - M|| / ||M||")
    ax.set_title("Self-consistency residual\n(explicit-formula identity; small = blocks normalized correctly)")
    ax.tick_params(axis="x", rotation=30)
    ax.legend()
    ax.grid(alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig(out_dir / "e3m_place_type_balance.png", dpi=140)
    plt.close()
    print(f"[3M] Saved {out_dir / 'e3m_place_type_balance.png'}")
    print(f"[3M] Saved {out_dir / 'e3m_place_type_balance.npz'}")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--K", type=int, default=10)
    parser.add_argument("--b-min", type=float, default=1.3)
    parser.add_argument("--b-max", type=float, default=6.0)
    parser.add_argument("--T-max", type=float, default=200.0)
    parser.add_argument("--prec", type=int, default=30)
    parser.add_argument("--t-cap", type=float, default=500.0)
    args = parser.parse_args()
    run(
        K=args.K,
        b_min=args.b_min,
        b_max=args.b_max,
        T_max=args.T_max,
        prec=args.prec,
        t_cap=args.t_cap,
    )
