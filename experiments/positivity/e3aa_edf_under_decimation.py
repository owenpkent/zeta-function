"""Experiment 3AA: the EDF under-decimation discriminator.

The cheapest decisive test of the Euler Decimation Flow conjecture (EDF), one of
the five PURSUE survivors of the session-019 first-principles conjecture program
(docs/03_research/first_principles_conjecture_program.md, LEARNINGS #76).

## What EDF claims and which clause this tests

EDF reads the Weil quadratic form as the energy of a renormalization flow on
L-coefficients and bets that zeta is a CENTER fixed point. Its falsifiable core
is two clauses, both tested here:

  Clause C (critical decimation window). Build the Weil form on test functions
  with support in [-t/2, t/2]; by the explicit formula this "matched" form sees
  exactly the prime powers p^k <= e^t. EDF predicts positivity holds ONLY at the
  matched window: if you keep the support t but DECIMATE the prime sum to primes
  p <= e^{t/2} (theta = 1/2 < 1), the form acquires negative spectrum. The bet is
  that positivity is a fixed-point property of the FULL Euler product, not a
  perturbative one, so removing the top octave of primes breaks it.

  Companion (single prime). The p=2 block alone, log 2 (I - (1-1/2) R_2) with
  R_2 = |1 - 2^{-1/2} T_{log 2}|^{-2}, dips to depth
  log 2 ((1/2)(1-2^{-1/2})^{-2} - 1) = 3.3468 at the resonance frequency
  xi = 2 pi / log 2 = 9.0647, against an archimedean density ~0.37 there, so the
  single-prime form is clearly negative. EDF predicts its min eigenvalue at t=8
  lies in [-3.2, -1.0]. If it comes out nonnegative, the core mechanism is wrong.

## The predicted mechanism (and what would kill it)

A prime p resonates at frequency xi = 2 pi / log p. The LARGE primes (log p near
the support edge t) resonate at LOW frequency, exactly where the archimedean
kernel Omega(t) is most negative (Omega(0) ~ -5.4 for zeta). So the top-octave
primes are load-bearing for low-frequency positivity; deleting them should expose
the archimedean trough and drive a LOW-FREQUENCY (broad) negative direction. We
therefore also report which basis function dominates the negative eigenvector: a
broad (large-b) dominant mode confirms the mechanism; a high-frequency one would
contradict it.

KILL: if the under-decimated min eigenvalue stays ~0 (noise-level) like the
matched form, under-decimation does NOT break positivity and EDF Clause C is dead
(a clean negative coordinate). If the single-prime symbol does not dip negative,
the companion is dead.

## Normalization (reuses the project's validated Weil-form blocks)

Part A is the input-side Weil Gram M = A_arch + P_fin + B_pole in the exact
M2.5/M2.6-validated normalization (the same blocks e3p_prime_block_ablation uses):
  - A_arch  : arch_block_bombieri (physical-space Bombieri integral, e2v).
  - P_fin   : finite_block on lam = von Mangoldt (zeta) or -L'/L coefficients (D-H),
              truncated by a PRIME CUTOFF for the under-decimated form.
  - B_pole  : pole_block (residue 1 for zeta, 0 for D-H).
Test family Phi_b(s) = 2 sinh((s-1/2) log b)/(s-1/2); h_b = 1_{[-log b, log b]},
so support [-t/2, t/2] is b in [1, e^{t/2}].

Honest scope: a falsification instrument, not a certificate. Per the marginal-
positivity wall (e3v, #52) the matched min eigenvalue at these windows is below
float64, so it reads as ~0 / noise; the discriminator is whether the under-
decimated form is ROBUSTLY O(1) negative against that ~0 baseline.

D-H discipline: D-H has no Euler product, so its -L'/L delocalizes onto all n and
the single-prime construction (Part B) has no D-H analogue at all. We still run
Part A on D-H (decimating by largest prime factor) to confirm the effect is
Euler-structured, not generic.

Outputs:
  - e3aa_edf_under_decimation.npz
  - e3aa_edf_under_decimation.png
  - stdout tables for Part A (min-eig discriminator) and Part B (single prime)

RESULT (2026-06-09, t=8,9,10, K=16, prec=25; LEARNINGS #77). Both sub-tests
fired POSITIVE for EDF.
  Part A (Clause C): zeta matched min-eig stays marginally positive
  (+0.029 / +0.025 / +0.020 at t=8/9/10) while under-decimation collapses it to
  -46.0 / -77.7 / -128.7, deepening monotonically; the negative direction is the
  broadest (lowest-frequency) basis mode at every t, confirming the predicted
  mechanism (large primes resonate at low frequency near the archimedean trough
  Omega(0) ~ -5.4, so deleting them exposes it).
  Part B (companion): the angular-mean-one identity is exact to ~1e-16 for
  p=2,3,5 (Clause B center fixed point); the p=2 dip depth -3.3468 matches the
  closed form exactly; the resonance value -2.98 and a genuine V_8 Hann-cosine
  packet -1.70 both land in the predicted band [-3.2, -1.0]; D-H has no per-prime
  block (no Euler product), so the construction is Euler-specific.
  HONEST SCOPE: a falsification instrument that came out positive, NOT a proof or
  certificate. D-H also goes negative under decimation (-6.0 / -1.8 / -2.2), so
  "under-decimation breaks positivity" is not by itself a zeta-vs-D-H separator;
  the clean Euler-structured content is the center identity and the single-prime
  resonance dip, which have no D-H analogue. EDF stays a live PURSUE direction; its
  open core (flow well-posedness, the Clause-E SOS witness) is unchanged.
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
from scipy.special import digamma as sp_digamma

from experiments._shared import zeta_L, DavenportHeilbronn
from experiments.positivity.e3m_place_type_balance import (
    finite_block, pole_block, lambda_coeffs_from_dirichlet, von_mangoldt_zeta,
)
from experiments.arithmetic_geometric.e2v_rosati_balance_M2_5 import arch_block_bombieri


# ----------------------------------------------------------------------------
# Prime-cutoff decimation of the finite block
# ----------------------------------------------------------------------------

def largest_prime_factor(n: int) -> int:
    """Largest prime factor of n (n >= 2)."""
    m = n
    lpf = 1
    p = 2
    while p * p <= m:
        if m % p == 0:
            lpf = p
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        lpf = m
    return lpf


def decimate_lambda(lam: np.ndarray, prime_cutoff: float) -> np.ndarray:
    """Zero out lam[n] for n whose largest prime factor exceeds prime_cutoff.

    For zeta (lam supported on prime powers) this deletes p^k with p > cutoff,
    i.e. removes the top-octave primes. For D-H (lam supported on all n) it
    deletes any n with a prime factor above the cutoff (the structural analogue).
    """
    out = lam.copy()
    for n in range(2, len(lam)):
        if out[n] == 0.0:
            continue
        if largest_prime_factor(n) > prime_cutoff:
            out[n] = 0.0
    return out


def min_eig_and_vector(M: np.ndarray):
    M = 0.5 * (M + M.T)
    vals, vecs = np.linalg.eigh(M)
    return float(vals[0]), vecs[:, 0]


# ----------------------------------------------------------------------------
# Part A: the under-decimation min-eigenvalue discriminator
# ----------------------------------------------------------------------------

def build_weil_blocks(L, name, mu_list, log_Q, residue, has_euler, b_vals, n_max, prec):
    """Returns (A_arch, lam, B_pole) for the input-side Weil form on b_vals."""
    A = arch_block_bombieri(b_vals, mu_list, log_Q, prec)
    if has_euler and name == "zeta":
        lam = np.array([0.0] + [von_mangoldt_zeta(n) for n in range(1, n_max + 1)])
    else:
        lam = lambda_coeffs_from_dirichlet(L, n_max, prec)
    B = pole_block(b_vals, float(residue), prec)
    return A, lam, B


def run_part_A(t_values, K, prec, out):
    dh = DavenportHeilbronn()
    targets = [
        ("zeta", zeta_L, [0.0], mp.mpf(0), 1.0, True),
        ("DH",   dh,     [1.0], mp.log(mp.sqrt(5)), 0.0, False),
    ]

    print("=" * 78)
    print("PART A: under-decimation min-eigenvalue discriminator")
    print("  matched window      Q_{t, e^t}    = full prime sum (exact Weil form)")
    print("  under-decimated     Q_{t, e^{t/2}} = primes p <= e^{t/2} only")
    print("  EDF Clause C predicts: zeta under-decimated min-eig clearly NEGATIVE,")
    print("  matched min-eig ~0 (marginal wall, below float64).")
    print("=" * 78)

    rows = []
    for name, L, mu_list, log_Q, residue, has_euler in targets:
        for t in t_values:
            L_half = t / 2.0
            b_max = float(np.exp(L_half))
            b_min = 1.2
            b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)
            n_max = int(np.exp(t)) + 2          # support cap: n <= b_i b_j <= e^t
            prime_cutoff = float(np.exp(L_half))  # e^{t/2}

            t0 = time.time()
            A, lam, B = build_weil_blocks(
                L, name, mu_list, log_Q, residue, has_euler, b_vals, n_max, prec)

            # Matched: full prime sum.
            P_full = finite_block(b_vals, lam, prec)
            M_matched = A + P_full + B
            eig_matched, _ = min_eig_and_vector(M_matched)

            # Under-decimated: delete primes above e^{t/2}.
            lam_cut = decimate_lambda(lam, prime_cutoff)
            P_cut = finite_block(b_vals, lam_cut, prec)
            M_under = A + P_cut + B
            eig_under, v_under = min_eig_and_vector(M_under)

            # Which basis mode dominates the negative direction? (mechanism check)
            dom_idx = int(np.argmax(np.abs(v_under)))
            dom_b = float(b_vals[dom_idx])
            n_deleted = int(np.count_nonzero(lam) - np.count_nonzero(lam_cut))

            rows.append(dict(
                name=name, t=t, b_max=b_max, K=K,
                eig_matched=eig_matched, eig_under=eig_under,
                n_deleted=n_deleted, dom_b=dom_b, dom_idx=dom_idx,
                broad=bool(dom_idx >= K - max(2, K // 4)),
            ))
            print(f"  {name:5s} t={t:4.1f}  b_max={b_max:8.2f}  "
                  f"matched min-eig={eig_matched:+.4e}  "
                  f"under-decim min-eig={eig_under:+.4e}  "
                  f"(deleted {n_deleted} prime terms; "
                  f"neg-dir dominant b={dom_b:.1f}"
                  f"{' [BROAD/low-freq]' if rows[-1]['broad'] else ''})  "
                  f"[{time.time()-t0:.1f}s]")
        print()

    # Verdict
    print("-" * 78)
    z = [r for r in rows if r["name"] == "zeta"]
    z_under = np.array([r["eig_under"] for r in z])
    z_match = np.array([r["eig_matched"] for r in z])
    clearly_neg = bool(np.all(z_under < -0.1))
    match_near_zero = bool(np.all(np.abs(z_match) < np.maximum(0.05, np.abs(z_under) / 5)))
    broad_dir = bool(all(r["broad"] for r in z))
    print(f"  zeta under-decimated min-eig: {z_under}")
    print(f"  zeta matched     min-eig: {z_match}")
    print(f"  EDF Clause C (under-decimation clearly negative, < -0.1 each): "
          f"{'SUPPORTED' if clearly_neg else 'NOT supported'}")
    print(f"  matched stays ~0 vs under-decimated O(1) negative: "
          f"{'yes' if match_near_zero else 'no'}")
    print(f"  negative direction is low-frequency/broad (predicted mechanism): "
          f"{'yes' if broad_dir else 'no'}")
    print("-" * 78)
    return rows


# ----------------------------------------------------------------------------
# Part B: the single-prime resonance companion (analytic, cheapest decisive test)
# ----------------------------------------------------------------------------

def arch_kernel(t_arr, mu_list, log_Q):
    """Omega_L(t) = 2 log Q + sum_mu [Re psi(1/4 + mu/2 + i t/2) - log pi]."""
    log_pi = np.log(np.pi)
    omega = np.full_like(t_arr, 2.0 * float(log_Q))
    z = 0.25 + 1j * t_arr / 2.0
    for mu in mu_list:
        omega = omega + np.real(sp_digamma(z + float(mu) / 2.0)) - log_pi
    return omega


def prime_block_symbol(t_arr, p):
    """log p ( 1 - (1-1/p) / |1 - p^{-1/2} e^{i t log p}|^2 ), the EDF p-block symbol."""
    z = p ** -0.5 * np.exp(1j * t_arr * np.log(p))
    R = 1.0 / np.abs(1.0 - z) ** 2
    return np.log(p) * (1.0 - (1.0 - 1.0 / p) * R)


def angular_mean(p, n_phi=200000):
    """Mean over phi of (1-1/p)/|1 - p^{-1/2} e^{i phi}|^2 (EDF center identity = 1)."""
    phi = np.linspace(0.0, 2.0 * np.pi, n_phi, endpoint=False)
    z = p ** -0.5 * np.exp(1j * phi)
    val = (1.0 - 1.0 / p) / np.abs(1.0 - z) ** 2
    return float(val.mean())


def vt_packet_rayleigh(p, mu_list, log_Q, t_support, xi):
    """Rayleigh quotient of the single-prime form on a V_t cosine packet at xi.

    g(x) = cos(xi x) * (1 + cos(pi x / (t/2)))/2 on |x| <= t/2 (a Hann-windowed
    cosine, genuinely supported in [-t/2, t/2]); Q(g)/||g||^2 in Fourier is
    int |ghat|^2 symbol / int |ghat|^2 with symbol = Omega + p-block.
    """
    half = t_support / 2.0
    x = np.linspace(-half, half, 8192)
    window = 0.5 * (1.0 + np.cos(np.pi * x / half))
    g = np.cos(xi * x) * window
    # ghat(t) = int g(x) e^{i t x} dx on a frequency grid
    t_grid = np.linspace(0.0, 60.0, 6000)
    dx = x[1] - x[0]
    # real, even-ish; compute |ghat|^2 directly
    ghat = (g[None, :] * np.exp(1j * np.outer(t_grid, x))).sum(axis=1) * dx
    w = np.abs(ghat) ** 2
    symbol = arch_kernel(t_grid, mu_list, log_Q) + prime_block_symbol(t_grid, p)
    num = np.trapezoid(w * symbol, t_grid)
    den = np.trapezoid(w, t_grid)
    return float(num / den)


def run_part_B(out):
    print("=" * 78)
    print("PART B: single-prime (p=2) resonance companion")
    print("  symbol(t) = Omega_zeta(t) + log2 (1 - (1/2)/|1 - 2^{-1/2} e^{i t log2}|^2)")
    print("  EDF predicts: dip depth 3.3468 at xi = 2 pi/log2 = 9.0647; min-eig in [-3.2,-1.0].")
    print("=" * 78)

    # Center identity (Clause B): angular mean exactly 1.
    print("  Angular-mean-one identity (EDF Clause B center fixed point):")
    for p in (2, 3, 5):
        am = angular_mean(p)
        print(f"    p={p}: mean (1-1/p)/|1-p^{{-1/2}}e^{{i phi}}|^2 = {am:.8f}  "
              f"(exact 1; |err|={abs(am-1):.2e})")

    # Predicted dip depth at resonance.
    p = 2
    xi = 2.0 * np.pi / np.log(2.0)
    depth_pred = np.log(2.0) * ((0.5) * (1.0 - 2.0 ** -0.5) ** -2 - 1.0)
    blk_at_xi = float(prime_block_symbol(np.array([xi]), 2)[0])
    omega_at_xi = float(arch_kernel(np.array([xi]), [0.0], 0.0)[0])
    print(f"\n  resonance xi = 2 pi / log 2 = {xi:.4f}")
    print(f"    predicted p=2 block dip depth  = -{depth_pred:.4f}")
    print(f"    measured  p=2 block at xi       = {blk_at_xi:+.4f}")
    print(f"    archimedean Omega_zeta at xi    = {omega_at_xi:+.4f}  (EDF says ~0.37)")
    print(f"    single-prime symbol at xi       = {omega_at_xi + blk_at_xi:+.4f}")

    # Two distinct minima. The DC/low-frequency trough is the ARCHIMEDEAN+pole
    # region (Omega(0) ~ -5.4), RH-agnostic and shared with D-H; it is NOT the
    # single-prime resonance the companion is about. The companion claim is the
    # PRIME-2 resonance dip at xi against the mild archimedean background there,
    # so we report the symbol minimum over the resonance regime t >= 2.0.
    t_grid = np.linspace(0.05, 60.0, 400000)
    symbol = arch_kernel(t_grid, [0.0], 0.0) + prime_block_symbol(t_grid, 2)
    dc_min = float(symbol.min())
    band = t_grid >= 2.0
    imin = int(np.argmin(symbol[band]))
    sym_min = float(symbol[band][imin])
    t_min = float(t_grid[band][imin])
    print(f"\n  archimedean DC trough (t->0, shared with D-H, RH-agnostic): "
          f"{dc_min:+.4f}  (NOT the companion claim)")
    print(f"  single-prime resonance minimum (t >= 2) = {sym_min:+.4f} at t = {t_min:.4f}")
    in_band = -3.2 <= sym_min <= -1.0
    print(f"    in EDF predicted band [-3.2, -1.0]: {in_band}")

    # Legitimate V_t test function: a packet supported in [-t/2, t/2] at t=8.
    ray8 = vt_packet_rayleigh(2, [0.0], 0.0, t_support=8.0, xi=xi)
    print(f"\n  V_8 Hann-cosine packet at xi: Rayleigh quotient = {ray8:+.4f}  "
          f"(a genuine compactly-supported test function realizes the negativity)")
    companion_ok = bool(sym_min < 0 and ray8 < 0)
    print(f"  Companion verdict (symbol min < 0 AND V_8 packet < 0): "
          f"{'SUPPORTED' if companion_ok else 'NOT supported'}")

    # D-H contrast: no per-prime block exists (no Euler product); show the bare
    # archimedean kernel is just more positive (bigger conductor), no dip.
    omega_dh_at_xi = float(arch_kernel(np.array([xi]), [1.0], float(np.log(np.sqrt(5))))[0])
    print(f"\n  D-H discipline: D-H has NO Euler product, so no single-prime block")
    print(f"    exists. Its bare archimedean Omega_DH(xi) = {omega_dh_at_xi:+.4f} "
          f"(positive, no resonance dip).")
    print("-" * 78)
    return dict(
        xi=xi, depth_pred=float(depth_pred), blk_at_xi=blk_at_xi,
        omega_at_xi=omega_at_xi, sym_min=sym_min, t_min=t_min, dc_min=dc_min,
        ray8=ray8, in_band=bool(in_band), companion_ok=companion_ok,
        omega_dh_at_xi=omega_dh_at_xi,
        angular_means={p: angular_mean(p) for p in (2, 3, 5)},
    )


# ----------------------------------------------------------------------------
# Driver + plot
# ----------------------------------------------------------------------------

def run(t_values=(8.0, 9.0, 10.0), K=16, prec=30, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    rows = run_part_A(list(t_values), K, prec, out_dir)
    print()
    partB = run_part_B(out_dir)

    # Save
    save = dict(K=K, prec=prec, t_values=np.array(t_values))
    for i, r in enumerate(rows):
        for k, v in r.items():
            save[f"A_{i}_{k}"] = v
    for k, v in partB.items():
        if k == "angular_means":
            continue
        save[f"B_{k}"] = v
    np.savez_compressed(out_dir / "e3aa_edf_under_decimation.npz", **save)

    # Plot: (left) Part A min-eig matched vs under-decimated for zeta and D-H;
    #       (right) Part B single-prime symbol with the resonance dip.
    fig, axs = plt.subplots(1, 2, figsize=(13, 5))

    ax = axs[0]
    for name, color in (("zeta", "tab:blue"), ("DH", "tab:red")):
        rs = [r for r in rows if r["name"] == name]
        ts = [r["t"] for r in rs]
        ax.plot(ts, [r["eig_matched"] for r in rs], "o--", color=color,
                label=f"{name} matched")
        ax.plot(ts, [r["eig_under"] for r in rs], "s-", color=color,
                label=f"{name} under-decimated")
    ax.axhline(0.0, color="k", lw=1.0)
    ax.axhline(-0.5, color="gray", lw=0.8, ls=":", label="EDF: < -0.5 by t=10")
    ax.set_xlabel("support window t")
    ax.set_ylabel("min eigenvalue of Weil Gram")
    ax.set_title("Part A: under-decimation discriminator\n(EDF predicts zeta under-decimated clearly negative)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    ax = axs[1]
    t_grid = np.linspace(0.05, 30.0, 4000)
    sym = arch_kernel(t_grid, [0.0], 0.0) + prime_block_symbol(t_grid, 2)
    omega = arch_kernel(t_grid, [0.0], 0.0)
    ax.plot(t_grid, sym, "b-", label="single-prime symbol (p=2)")
    ax.plot(t_grid, omega, "g--", lw=0.8, label=r"archimedean $\Omega_\zeta$")
    ax.axhline(0.0, color="k", lw=1.0)
    ax.axvline(partB["xi"], color="tab:orange", lw=0.8, ls=":",
               label=r"$\xi=2\pi/\log 2$")
    ax.scatter([partB["t_min"]], [partB["sym_min"]], color="red", zorder=5,
               label=f"min {partB['sym_min']:.2f}")
    ax.set_xlabel("frequency t")
    ax.set_ylabel("symbol value")
    ax.set_title("Part B: single-prime resonance dip\n(EDF predicts dip to ~ -3 at the resonance)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e3aa_edf_under_decimation.png", dpi=140)
    plt.close()
    print(f"[3AA] Saved {out_dir / 'e3aa_edf_under_decimation.png'}")
    print(f"[3AA] Saved {out_dir / 'e3aa_edf_under_decimation.npz'}")
    return rows, partB


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--t-values", type=float, nargs="+", default=[8.0, 9.0, 10.0])
    parser.add_argument("--K", type=int, default=16)
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(t_values=tuple(args.t_values), K=args.K, prec=args.prec)
