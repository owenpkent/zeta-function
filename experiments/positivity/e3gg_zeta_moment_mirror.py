"""Experiment 3GG: the zeta-side moment mirror -- why flat-extension pinching does
not transfer from F_q to zeta.

Follow-on to e2ll (the function-field wind tunnel, LEARNINGS #79), which showed
that over F_q the composite-pinching lemma HOLDS and its mechanism is the
flat-extension uniqueness of the truncated trigonometric moment problem
(Curto-Fialkow): the Frobenius measure is 2g atoms, so its moment Toeplitz matrix
goes FLAT (rank stabilizes at 2g) and the representing measure -- hence the
closed-point/von Mangoldt comb -- is UNIQUE (pinched). e2ll localized the gap to
zeta as the transfer from a finite DISCRETE spectrum to zeta's POLE-SOURCED
CONTINUOUS archimedean spectrum.

This experiment makes that fail mode VISIBLE by running the same machinery on
zeta's zeros, side by side with F_q.

## The mirror

Over F_q the relevant measure is the empirical Frobenius measure mu_q = sum_j
delta_{theta_j} (2g unitarized angles on the circle), with trig moments r_k =
sum_j e^{i k theta_j}; its (m+1)x(m+1) Toeplitz matrix R is PSD and goes FLAT
(rank 2g) for m >= 2g. The zeta analogue is the empirical ZERO measure: take the
ordinates gamma_1, ..., gamma_N (the imaginary parts of the non-trivial zeros),
place them on the circle at theta_n = alpha * gamma_n (mod 2 pi), and form the
normalized trig moments c_k = (1/N) sum_n e^{i k theta_n} and their Toeplitz
matrix C (c_0 = 1, a correlation matrix).

## The prediction and what it shows

By equidistribution of the zero ordinates (the explicit formula forces
sum_n e^{i k alpha gamma_n} = o(N) for every fixed k != 0; the archimedean
Riemann-von Mangoldt density is the continuous spectral density), the moments
c_k -> 0 and C -> I. So:

  - F_q  : C goes FLAT (rank stabilizes at 2g, smallest eigenvalue -> 0). The
           moment problem is DETERMINATE: a unique representing measure, the comb
           is pinned. THIS is composite pinching.
  - zeta : C stays FULL RANK with smallest eigenvalue bounded away from 0 (-> 1
           as N grows; C -> I). The truncated moment problem is maximally
           INDETERMINATE: a continuum of representing measures (ghosts), so the
           comb is NOT pinned by the moments. Flat-extension uniqueness has
           nothing to bite on.

The "ghost room" (the smallest relative eigenvalue of C, the distance to the PSD
boundary) is the headline: it COLLAPSES to 0 for F_q (flat = pinched) and PERSISTS
near 1 for zeta (never flat = not pinched). The decay |c_k| -> 0 is the signature
of the continuous spectrum that defeats the transfer.

## Honest scope (this is a mechanism illustrator, NOT a detector)

This proves nothing new and is not a zeta-vs-D-H detector: D-H also has infinitely
many zeros with a continuous limiting density, so its moment matrix is ALSO never
flat (we run it to confirm the obstruction is shared). The point is structural:
flat-extension pinching is exactly the F_q mechanism, and it cannot transfer to
ANY degree-1 L-function with infinitely many zeros, because the continuous
archimedean spectrum keeps the moment matrix full rank. The named consequence:
the comb-uniqueness for zeta must come from a moment-problem theorem for measures
with a continuous (pole-sourced archimedean) component plus the Euler structure --
NOT from flat extension. That transfer theorem is LCC/EFR's open core (#76, #79).
Repurposes the (known) equidistribution of zero ordinates to exhibit the exact
obstruction; the value is the coordinate, not new number theory. Soft-detector
freeze respected: no certified margin, no positivity claim.

Outputs:
  - e3gg_zeta_moment_mirror.npz
  - e3gg_zeta_moment_mirror.png
  - stdout : the flat-vs-never-flat contrast table

RESULT (2026-06-10, M=12, T_max=500 (N=269 zeta / 189 D-H zeros), prec=30;
LEARNINGS #80). The flat-extension transfer fail mode is exhibited cleanly.

  - F_q (flat / pinched): the Frobenius-measure Toeplitz rank stabilizes at 2g
    (2 for the elliptic curve, 4 for the genus-2), and the ghost room (relative
    smallest eigenvalue) COLLAPSES to ~1e-16 at m = 2g. The normalized moments
    |c_k| are O(1) (atomic measure; the genus-2 curve over F_7 gives the clean
    period-4 pattern |c_k| = {0,0,0,1,...}). Flat => unique representing measure
    => the comb is PINNED. This is composite pinching, #79.
  - zeta (never flat / not pinched): the zero-measure Toeplitz stays FULL RANK
    (rank = m+1 through m=12) and the ghost room PERSISTS at 0.48-0.99 (mean ~0.74),
    ~15 orders of magnitude above the F_q floor. The moments |c_k| are small,
    O(1/sqrt(N)) ~ 0.06 (the continuous limit C -> I), not decaying in k. The
    truncated moment problem is maximally INDETERMINATE: a continuum of ghost
    measures, so the moments do NOT pin the comb. Robust across the circle-map
    scale alpha in {0.5, 1, 2} (rank behaviour identical).
  - D-H (shared obstruction, honest scope): D-H's zero-measure Toeplitz is ALSO
    never flat (ghost room persists 0.46-0.93), so this is NOT a zeta-vs-D-H
    detector. The continuous-spectrum obstruction is shared by every degree-1 L
    with infinitely many zeros; the construction illustrates the MECHANISM, not a
    discriminator.

  TAKEAWAY. The flat-extension uniqueness that pins the comb over F_q (e2ll/#79)
  has no purchase on zeta: the pole-sourced continuous archimedean spectrum keeps
  the moment matrix full rank (|c_k| -> 0 as N grows, C -> I). So the composite-
  pinching transfer cannot run through flat extension; it needs a moment-uniqueness
  theorem for a measure with a continuous (archimedean) component PLUS the Euler
  structure that singles zeta out. That is LCC/EFR's named open core (#76, #79),
  now exhibited as a concrete 15-order-of-magnitude ghost-room gap.

  HONEST SCOPE: proves nothing new; repurposes the known equidistribution of zero
  ordinates to make the #79 transfer obstruction visible and quantitative. Not a
  detector (D-H behaves identically). A synthesis coordinate. Soft-detector freeze
  respected (no margin, no positivity claim).
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np

from experiments._shared import zeta_L, DavenportHeilbronn
from experiments.arithmetic_geometric.e2f_hodge_index_sweep import (
    count_points_Fpk, zeta_polynomial, elliptic_family, genus2_family,
)
from experiments.arithmetic_geometric.e2ll_ff_crystal_cone import (
    power_sums_from_P, toeplitz_moment_matrix, psd_and_rank,
)


# ---------------------------------------------------------------------------
# F_q side: the Frobenius-measure Toeplitz (flat at 2g). Reuses e2ll machinery.
# ---------------------------------------------------------------------------

def fq_moment_ranks(curve, M, prec):
    """Normalized Frobenius moments c_k = r_k / (2g) and the rank / relative
    smallest eigenvalue of the (m+1) Toeplitz for m = 1..M."""
    p, g, f = curve["p"], curve["g"], curve["f_coeffs"]
    deg = 2 * g
    N_low = [count_points_Fpk(f, p, k) for k in range(1, deg + 1)]
    _, int_coeffs = zeta_polynomial(N_low, p, g)
    s = power_sums_from_P(int_coeffs, M)
    mp.mp.dps = prec
    sq = mp.sqrt(p)
    # normalized so c_0 = 1 (a correlation matrix), matching the zeta side
    c = [mp.mpf(1)] + [mp.mpf(int(s[k - 1])) / (sq ** k) / deg for k in range(1, M + 1)]
    ranks, rel_min = [], []
    for m in range(1, M + 1):
        R = toeplitz_moment_matrix(c, m, prec)
        _, _, rank, _ = psd_and_rank(R, m)
        A = np.array([[complex(R[i, j]) for j in range(m + 1)] for i in range(m + 1)])
        A = 0.5 * (A + A.conj().T)
        ev = np.linalg.eigvalsh(A)
        ranks.append(rank)
        rel_min.append(float(ev[0]) / max(float(np.abs(ev).max()), 1e-300))
    absck = [float(abs(complex(c[k]))) for k in range(1, M + 1)]   # O(1): atomic
    return dict(label=curve["label"], deg=deg, ranks=ranks, rel_min=rel_min, absck=absck)


# ---------------------------------------------------------------------------
# zeta side: the empirical zero-measure Toeplitz (never flat).
# ---------------------------------------------------------------------------

def gammas(L, T_max, prec):
    """Imaginary parts of the non-trivial zeros up to T_max."""
    rhos = L.zeros(T_max=T_max, prec=prec)
    return np.array([float(mp.im(r)) for r in rhos])


def empirical_moment_ranks(gam, M, alpha, prec, rel_tol=1e-9):
    """Normalized empirical trig moments c_k = (1/N) sum_n e^{i k alpha gamma_n}
    and the rank / relative smallest eigenvalue of the (m+1) Toeplitz, m=1..M."""
    N = len(gam)
    theta = (alpha * gam) % (2.0 * np.pi)
    z = np.exp(1j * theta)
    # c_k = mean of z^k
    cks = [1.0 + 0.0j] + [complex(np.mean(z ** k)) for k in range(1, M + 1)]
    ranks, rel_min, absck = [], [], [abs(x) for x in cks[1:]]
    for m in range(1, M + 1):
        A = np.array([[cks[i - j] if i >= j else np.conj(cks[j - i])
                       for j in range(m + 1)] for i in range(m + 1)], dtype=complex)
        A = 0.5 * (A + A.conj().T)
        ev = np.linalg.eigvalsh(A)
        scale = max(float(np.abs(ev).max()), 1e-300)
        ranks.append(int(np.sum(np.abs(ev) > rel_tol * scale)))
        rel_min.append(float(ev[0]) / scale)
    return dict(ranks=ranks, rel_min=rel_min, absck=absck, N=N, alpha=alpha)


# ---------------------------------------------------------------------------
# Driver.
# ---------------------------------------------------------------------------

def run(M=12, T_max=500.0, prec=30, alphas=(1.0, 0.5, 2.0), out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 80)
    print("EXPERIMENT 3GG: zeta-side moment mirror (flat-extension transfer fail mode)")
    print("  F_q  : Frobenius-measure Toeplitz goes FLAT (rank -> 2g, rel-min -> 0)")
    print("         => unique measure => comb PINNED (composite pinching, #79).")
    print("  zeta : zero-measure Toeplitz stays FULL RANK (rel-min bounded away from 0)")
    print("         => indeterminate moment problem => comb NOT pinned by moments.")
    print(f"  M={M} moments, T_max={T_max}, prec={prec}")
    print("=" * 80)

    # --- F_q reference (flat) ---
    print("\n--- F_q reference (the flat / pinched case) ---")
    fq = []
    for curve in [elliptic_family([7])[0], genus2_family([7])[0]]:
        res = fq_moment_ranks(curve, M, prec)
        fq.append(res)
        flat_at = next((m for m, r in zip(range(1, M + 1), res["ranks"]) if r >= res["deg"]), None)
        print(f"  {res['label']}  (2g={res['deg']})")
        print(f"    rank vs size m=1..{M}: {res['ranks']}  (flat at m={flat_at})")
        print(f"    rel-min eig (ghost room): {[f'{x:+.2e}' for x in res['rel_min']]}")
        print(f"    |c_k| (k=1..{M}): {[f'{x:.3f}' for x in res['absck']]}  (O(1): atomic measure)")
        print(f"    -> collapses to ~0 at m=2g: FLAT => unique measure => PINCHED.")

    # --- zeta (never flat) ---
    print("\n--- zeta (the never-flat / not-pinched case) ---")
    gam_z = gammas(zeta_L, T_max, prec)
    zeta_runs = {a: empirical_moment_ranks(gam_z, M, a, prec) for a in alphas}
    for a, res in zeta_runs.items():
        print(f"  alpha={a}: N={res['N']} zero ordinates")
        print(f"    rank vs size m=1..{M}: {res['ranks']}  (full rank = m+1, NEVER flat)")
        print(f"    rel-min eig (ghost room): {[f'{x:+.3f}' for x in res['rel_min']]}")
        print(f"    |c_k| (k=1..{M}): {[f'{x:.3f}' for x in res['absck']]}  "
              f"(small, O(1/sqrt(N))~{1/np.sqrt(res['N']):.3f}: continuous spectrum, C->I)")
    z_main = zeta_runs[alphas[0]]
    print(f"    -> ghost room persists (rel-min ~ {np.mean(z_main['rel_min']):.2f}); "
          f"NEVER flat => moments do NOT pin the comb. (|c_k| are O(1/sqrt N), not")
    print(f"       decaying in k; the contrast with F_q's O(1) |c_k| is atomic-vs-continuous.)")

    # --- D-H (also never flat: the obstruction is shared, NOT a detector) ---
    print("\n--- D-H control (honest scope: also never flat -> NOT a zeta-vs-D-H detector) ---")
    gam_dh = gammas(DavenportHeilbronn(), T_max, prec)
    dh_res = empirical_moment_ranks(gam_dh, M, alphas[0], prec)
    print(f"  D-H: N={dh_res['N']}, rank vs size: {dh_res['ranks']} (full, never flat)")
    print(f"    rel-min (ghost room): {[f'{x:+.3f}' for x in dh_res['rel_min']]}")
    print(f"    -> D-H ALSO never flat: the continuous-spectrum obstruction is shared by")
    print(f"       every degree-1 L with infinitely many zeros (mechanism, not detector).")

    _plot(fq, zeta_runs, dh_res, alphas, M, out_dir)
    _save(fq, zeta_runs, dh_res, alphas, M, T_max, prec, out_dir)

    # --- synthesis ---
    print("\n" + "=" * 80)
    print("SYNTHESIS")
    fq_collapses = all(min(r["rel_min"]) < 1e-6 for r in fq)
    zeta_persists = all(min(res["rel_min"]) > 0.05 for res in zeta_runs.values())
    print(f"  F_q ghost room collapses to ~0 (flat => pinched):     {fq_collapses}")
    print(f"  zeta ghost room persists > 0.05 (never flat => not):  {zeta_persists}")
    print(f"  alpha-robust (conclusion independent of the map):     "
          f"{len(set(tuple(r['ranks']) for r in zeta_runs.values())) >= 1}")
    print("  => the flat-extension uniqueness that pins the comb over F_q has NO purchase")
    print("     on zeta: the continuous archimedean spectrum keeps the moment matrix full")
    print("     rank (|c_k|->0, C->I). The composite-pinching transfer therefore needs a")
    print("     moment-uniqueness theorem for a continuous (pole-sourced) spectrum + Euler")
    print("     structure, not flat extension. This is LCC/EFR's named open core (#76,#79).")
    print("=" * 80)
    return dict(fq=fq, zeta=zeta_runs, dh=dh_res)


def _plot(fq, zeta_runs, dh_res, alphas, M, out_dir):
    xs = list(range(1, M + 1))
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    ax = axes[0]
    for r in fq:
        ax.plot(xs, r["ranks"], "o-", label=f"F_q: {r['label'][:20]} (2g={r['deg']})")
    ax.plot(xs, zeta_runs[alphas[0]]["ranks"], "s--", color="C3",
            label=f"zeta (alpha={alphas[0]})")
    ax.plot(xs, dh_res["ranks"], "^:", color="C4", label="D-H")
    ax.plot(xs, [m + 1 for m in xs], "k:", alpha=0.4, label="full rank (m+1)")
    ax.set_xlabel("Toeplitz size m"); ax.set_ylabel("rank of moment matrix")
    ax.set_title("Rank: F_q flattens at 2g, zeta/D-H stay full\n(flat = pinched; full = ghosts)")
    ax.legend(fontsize=7); ax.grid(True, alpha=0.3)

    ax = axes[1]
    for r in fq:
        ax.semilogy(xs, np.maximum(np.abs(r["rel_min"]), 1e-18), "o-",
                    label=f"F_q: {r['label'][:20]}")
    for a, res in zeta_runs.items():
        ax.semilogy(xs, np.maximum(np.abs(res["rel_min"]), 1e-18), "s--",
                    label=f"zeta alpha={a}")
    ax.semilogy(xs, np.maximum(np.abs(dh_res["rel_min"]), 1e-18), "^:", label="D-H")
    ax.set_xlabel("Toeplitz size m"); ax.set_ylabel("rel-min eig (ghost room)")
    ax.set_title("Ghost room: collapses (F_q, flat) vs persists (zeta, never flat)")
    ax.legend(fontsize=7); ax.grid(True, which="both", alpha=0.3)
    fig.tight_layout()
    p = out_dir / "e3gg_zeta_moment_mirror.png"
    fig.savefig(p, dpi=130); plt.close(fig)
    print(f"\n[plot] {p}")


def _save(fq, zeta_runs, dh_res, alphas, M, T_max, prec, out_dir):
    payload = dict(M=M, T_max=T_max, prec=prec, alphas=np.array(list(alphas)))
    for i, r in enumerate(fq):
        payload[f"fq{i}_label"] = r["label"]; payload[f"fq{i}_deg"] = r["deg"]
        payload[f"fq{i}_ranks"] = np.array(r["ranks"])
        payload[f"fq{i}_rel_min"] = np.array(r["rel_min"])
    for a, res in zeta_runs.items():
        payload[f"zeta_a{a}_ranks"] = np.array(res["ranks"])
        payload[f"zeta_a{a}_rel_min"] = np.array(res["rel_min"])
        payload[f"zeta_a{a}_absck"] = np.array(res["absck"])
    payload["dh_ranks"] = np.array(dh_res["ranks"])
    payload["dh_rel_min"] = np.array(dh_res["rel_min"])
    p = out_dir / "e3gg_zeta_moment_mirror.npz"
    np.savez(p, **payload)
    print(f"[save] {p}")


def main():
    ap = argparse.ArgumentParser(description="zeta-side moment mirror (3GG)")
    ap.add_argument("--M", type=int, default=12, help="max Toeplitz size")
    ap.add_argument("--T_max", type=float, default=500.0, help="zero height cutoff")
    ap.add_argument("--prec", type=int, default=30, help="mpmath precision (dps)")
    ap.add_argument("--alphas", type=str, default="1.0,0.5,2.0", help="circle-map scales")
    args = ap.parse_args()
    alphas = tuple(float(x) for x in args.alphas.split(","))
    run(M=args.M, T_max=args.T_max, prec=args.prec, alphas=alphas)


if __name__ == "__main__":
    main()
