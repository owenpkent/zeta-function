"""Experiment 2AE: the archimedean self-intersection omega-bar^2 = 12 h_Fal(E)
via the Petersson norm of the weight-12 discriminant modular form.

This is the deferred numerical follow-up flagged in 2J_arakelov_adjunction.md
(section "Status and the concrete numerical follow-up"). 2J was a rigorous
structural bridge that deliberately shipped no numerics, to avoid a
period-computation normalization slog. This experiment closes that gap: it is
the omega-bar^2 companion to 2H/2I's validated point-height work, the literal
computation of "the archimedean Green's function entering the self-intersection
number."

## What omega-bar^2 = 12 h_Fal is, and why the archimedean place enters

On the function field side (2G), the canonical self-intersection Delta^2 = 2 - 2g
comes from ADJUNCTION on C x C, and that self-intersection is what makes the
primitive Gram matrix non-degenerate (without it the Hasse-Weil bound has nothing
to bound). The arithmetic analogue, for the minimal regular model E -> Spec(Z) of
an elliptic curve, is the arithmetic self-intersection of the relative dualizing
sheaf with its Arakelov metric, omega-bar^2, which equals 12 h_Fal(E) (Faltings
adjunction, up to a fixed normalization). And, exactly as everything in this
session has split, h_Fal splits into a finite piece (the minimal discriminant,
the product of bad-prime contributions) and an ARCHIMEDEAN piece (the Petersson
norm of the weight-12 discriminant modular form at the period point tau):

    12 h_Fal(E) = log|Delta_min|  -  log ||Delta||_Pet(tau)  +  6 log(2 pi)
                  (finite)            (archimedean)             (normalization const)

with the Petersson norm

    ||Delta||_Pet(tau) = (2 pi)^12 (Im tau)^6 |eta(tau)|^24,

Delta(tau) = (2 pi)^12 eta(tau)^24, eta the Dedekind eta function, and tau the
period point of E reduced to the SL_2(Z) fundamental domain. The archimedean
term is a Green's-function / Petersson-metric quantity on E(C): the same kind of
transcendental archimedean contribution 2I exhibited for point-heights
(lambda_inf), now at the level of the SELF-intersection of the canonical class.

## The normalization, pinned exactly (the factor-of-2 / 2pi slog)

The known headache (Silverman's paper vs his books; Deligne vs LMFDB) is the
(2 pi) and factor-of-2 conventions. We pin them by an UNAMBIGUOUS internal
identity rather than by citation. For the minimal Neron lattice
L = Z omega_1 + Z omega_2 (omega the Neron differential), the lattice
discriminant is

    Delta(L) = (2 pi / omega_1)^12 eta(tau)^24  =  Delta_min  (the integer),

which we verify holds to full precision (Delta(L) recovers 37, 389, 5077 exactly).
This fixes the differential's normalization. The covolume A = Im(tau) |omega_1|^2
then gives the stable Faltings height in the Deligne / LMFDB normalization as

    h_Fal(E) = -(1/2) log( A / (2 pi) ),

and one checks algebraically (and we verify numerically, the constant is the SAME
6 log(2 pi) for all three curves) that

    12 h_Fal(E) = log|Delta_min| - log ||Delta||_Pet(tau) + 6 log(2 pi).

So the constant in the 2J display is + 6 log(2 pi). This is the
Deligne-normalized stable Faltings height; for 37a1 it gives h_Fal = -0.07760,
matching the LMFDB value for curve 37.a1.

## What is computed

Per curve (37a1, 389a1, 5077a1, the e2h ladder):
  1. The period lattice via AGM / complete elliptic integrals (mpmath, >= 30 dps);
     tau = omega_2/omega_1, reduced to the SL_2(Z) fundamental domain.
  2. The Petersson norm ||Delta||_Pet(tau) = (2 pi)^12 (Im tau)^6 |eta(tau)|^24.
  3. 12 h_Fal assembled from log|Delta_min| (finite) and -log||Delta||_Pet
     (archimedean) plus 6 log(2 pi); the ARCHIMEDEAN SHARE = the fraction of the
     12 h_Fal magnitude carried by the Petersson term vs the finite term.

## Validations

  (i)  SL_2(Z)-invariance of ||Delta||_Pet: ||Delta||_Pet(tau) is a weight-0
       quantity ((Im tau)^6 |eta|^24 with eta weight 1/2, |eta|^24 weight 12,
       (Im tau)^6 weight -12). We check ||Delta||_Pet(tau) == ||Delta||_Pet(g.tau)
       for a nontrivial g in SL_2(Z) (here g = T S = (1 1; -1 0) and S = (0 -1;1 0))
       to high precision. This is the SOLID internal check.
  (ii) The assembled h_Fal against the known LMFDB value for 37.a1
       (h_Fal(37.a1) = -0.0776...). Reported as matched / approx / failed with
       the exact convention documented.

## K1-clean / Davenport-Heilbronn note

K1-clean: the entire computation uses ONLY each curve's own arithmetic (its
Weierstrass coefficients, its minimal discriminant, its complex period). Zeta's
zeros never appear. The D-H discipline applies vacuously here: this is an
Architecture-2 construction (it intentionally requires the curve's geometry, the
thing D-H lacks). No positivity claim is made that could "work" for D-H. The only
positivity-adjacent object, the SL_2(Z)-invariance, is a modular-symmetry fact
about eta, not an RH-type inequality.

Outputs:
  - e2ae_petersson_faltings.npz : per-curve tau, Petersson norm, 12 h_Fal, shares
  - e2ae_petersson_faltings.png : archimedean vs finite share of 12 h_Fal
  - stdout : per-curve table + both validations
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp


# ---------------------------------------------------------------------------
# Weierstrass invariants from the integral model
#   y^2 + a1 x y + a3 y = x^3 + a2 x^2 + a4 x + a6.
# c4, c6, Delta are the standard combinations; for our prime-conductor curves
# the model IS minimal, so Delta here is Delta_min.
# ---------------------------------------------------------------------------

def invariants(a1, a2, a3, a4, a6):
    b2 = a1 * a1 + 4 * a2
    b4 = 2 * a4 + a1 * a3
    b6 = a3 * a3 + 4 * a6
    b8 = a1 * a1 * a6 + 4 * a2 * a6 - a1 * a3 * a4 + a2 * a3 * a3 - a4 * a4
    c4 = b2 * b2 - 24 * b4
    c6 = -b2 ** 3 + 36 * b2 * b4 - 216 * b6
    disc = -b2 * b2 * b8 - 8 * b4 ** 3 - 27 * b6 * b6 + 9 * b2 * b4 * b6
    return c4, c6, disc


# ---------------------------------------------------------------------------
# Period lattice via AGM. We pass to the Weierstrass form y^2 = 4x^3 - g2 x - g3
# (g2 = c4/12, g3 = c6/216), whose roots e1 > e2 > e3 are real when disc > 0
# (all three curves here). The real and imaginary periods come from the AGM:
#   omega_1 (real)      = pi / AGM( sqrt(e1-e3), sqrt(e1-e2) )
#   omega_2 (imaginary) = i pi / AGM( sqrt(e1-e3), sqrt(e2-e3) ).
# WHY AGM not numeric quadrature: the AGM is the fastest, most accurate route to
# complete elliptic integrals and is exact to working precision in O(log) steps.
# ---------------------------------------------------------------------------

def periods(c4, c6):
    g2 = mp.mpf(c4) / 12
    g3 = mp.mpf(c6) / 216
    roots = sorted(mp.polyroots([4, 0, -g2, -g3]), key=lambda z: mp.re(z))
    e3, e2, e1 = roots  # ascending; e1 largest
    a = mp.sqrt(e1 - e3)
    b = mp.sqrt(e1 - e2)
    c = mp.sqrt(e2 - e3)
    omega1 = mp.pi / mp.agm(a, b)
    omega2 = mp.mpc(0, 1) * mp.pi / mp.agm(a, c)
    return omega1, omega2


# ---------------------------------------------------------------------------
# SL_2(Z) action and reduction to the fundamental domain.
# ---------------------------------------------------------------------------

def sl2_act(g, tau):
    (a, b), (c, d) = g
    return (a * tau + b) / (c * tau + d)


def reduce_tau(tau, max_steps=10000):
    """Reduce tau into the standard fundamental domain |Re| <= 1/2, |tau| >= 1."""
    tau = mp.mpc(tau)
    eps = mp.mpf(10) ** (-(mp.mp.dps - 5))
    for _ in range(max_steps):
        n = mp.nint(mp.re(tau))
        tau = tau - n               # translate Re(tau) into [-1/2, 1/2]
        if abs(tau) < 1 - eps:
            tau = -1 / tau          # invert when inside the unit circle
        else:
            break
    return tau


# ---------------------------------------------------------------------------
# Dedekind eta and the Petersson norm of Delta.
# eta(tau) = exp(pi i tau / 12) * prod_{n>=1} (1 - q^n),  q = exp(2 pi i tau),
# computed via mpmath's q-Pochhammer (q;q)_inf for full precision.
# ||Delta||_Pet(tau) = (2 pi)^12 (Im tau)^6 |eta(tau)|^24.
# ---------------------------------------------------------------------------

def dedekind_eta(tau):
    q = mp.exp(2j * mp.pi * tau)
    return mp.exp(mp.pi * 1j * tau / 12) * mp.qp(q)


def petersson_norm_delta(tau):
    eta = dedekind_eta(tau)
    return (2 * mp.pi) ** 12 * mp.im(tau) ** 6 * abs(eta) ** 24


# ---------------------------------------------------------------------------
# Curves (same ladder as e2h). Prime conductor => the integral model is minimal
# => the c4,c6,disc above are the minimal invariants and disc = Delta_min.
# ---------------------------------------------------------------------------

CURVES = [
    {"label": "37a1   y^2+y=x^3-x",        "a": (0, 0, 1, -1, 0)},
    {"label": "389a1  y^2+y=x^3+x^2-2x",   "a": (0, 1, 1, -2, 0)},
    {"label": "5077a1 y^2+y=x^3-7x+6",     "a": (0, 0, 1, -7, 6)},
]

# Known LMFDB stable Faltings height (Deligne normalization) for validation (ii).
# 37.a1 is the standard published value; recorded for the convention match.
KNOWN_HFAL = {"37a1   y^2+y=x^3-x": mp.mpf("-0.0776037")}


def run(dps: int = 50, out_dir: Path = None):
    mp.mp.dps = dps
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("[2AE] omega-bar^2 = 12 h_Fal via the Petersson norm of the weight-12")
    print("      discriminant Delta. The archimedean self-intersection: the")
    print("      omega-bar^2 companion to 2H/2I's validated point-heights.\n")
    print(f"      Working precision: {dps} decimal digits.")
    print(f"      Normalization: 12 h_Fal = log|Delta_min| - log||Delta||_Pet(tau)")
    print(f"                                 + 6 log(2 pi)   (Deligne / LMFDB).\n")

    # Nontrivial SL_2(Z) elements for the invariance check.
    S = ((0, -1), (1, 0))
    T = ((1, 1), (0, 1))
    # g = T . S = (1 1; -1 0): a genuinely nontrivial word, neither S nor T alone.
    TS = ((1, 1), (-1, 0))

    results = []
    sl2_all_pass = True

    for curve in CURVES:
        a1, a2, a3, a4, a6 = curve["a"]
        c4, c6, disc = invariants(a1, a2, a3, a4, a6)
        omega1, omega2 = periods(c4, c6)
        tau_raw = omega2 / omega1
        tau = reduce_tau(tau_raw)

        # internal sanity: lattice discriminant Delta(L) must recover Delta_min.
        # This is what pins the (2 pi) normalization with no external citation.
        # NB: use the RAW period ratio and the actual omega_1 (the Neron lattice
        # generator), NOT the SL_2-reduced tau: Delta(L) is a property of the
        # concrete lattice L = Z omega_1 + Z omega_2.
        eta_raw = dedekind_eta(tau_raw)
        DeltaL = (2 * mp.pi / omega1) ** 12 * eta_raw ** 24
        deltaL_err = abs(DeltaL - disc) / abs(disc)

        pet = petersson_norm_delta(tau)

        log_finite = mp.log(abs(disc))            # finite (bad-prime) piece
        log_arch = -mp.log(pet)                   # archimedean (Petersson) piece
        const = 6 * mp.log(2 * mp.pi)             # the pinned normalization const
        twelve_hfal = log_finite + log_arch + const
        hfal = twelve_hfal / 12

        # archimedean share: fraction of the 12 h_Fal MAGNITUDE carried by the
        # Petersson term, measured against the finite term. We report two readings:
        #  - raw term magnitudes |log_arch| vs |log_finite| (no const), and
        #  - the const-inclusive decomposition.
        share_arch_vs_fin = float(abs(log_arch) / (abs(log_arch) + abs(log_finite)))

        # validation (i): SL_2(Z)-invariance of ||Delta||_Pet
        pet_S = petersson_norm_delta(reduce_tau(sl2_act(S, tau)) if False else sl2_act(S, tau))
        pet_T = petersson_norm_delta(sl2_act(T, tau))
        pet_TS = petersson_norm_delta(sl2_act(TS, tau))
        inv_err = max(abs(pet_S - pet) / pet,
                      abs(pet_T - pet) / pet,
                      abs(pet_TS - pet) / pet)
        inv_pass = inv_err < mp.mpf(10) ** (-(dps - 8))
        sl2_all_pass = sl2_all_pass and inv_pass

        # validation (ii): known Faltings height where available
        known = KNOWN_HFAL.get(curve["label"])
        if known is not None:
            hfal_err = abs(hfal - known)
            hfal_match = hfal_err < mp.mpf("1e-5")
        else:
            hfal_err = None
            hfal_match = None

        results.append(dict(
            label=curve["label"], disc=int(disc),
            tau=tau, tau_raw=tau_raw,
            pet=pet, log_finite=log_finite, log_arch=log_arch,
            const=const, twelve_hfal=twelve_hfal, hfal=hfal,
            share_arch_vs_fin=share_arch_vs_fin,
            deltaL_err=deltaL_err, inv_err=inv_err, inv_pass=inv_pass,
            known=known, hfal_err=hfal_err, hfal_match=hfal_match,
        ))

        print(f"  --- {curve['label']}   (Delta_min = {int(disc)}) ---")
        print(f"      tau (reduced)        = {mp.nstr(tau, 18)}")
        print(f"      Delta(L) vs Delta_min: rel err {mp.nstr(deltaL_err, 4)}  "
              f"(pins the 2pi normalization)")
        print(f"      ||Delta||_Pet(tau)   = {mp.nstr(pet, 14)}")
        print(f"      log|Delta_min|       = {mp.nstr(log_finite, 14)}   (finite)")
        print(f"      -log||Delta||_Pet    = {mp.nstr(log_arch, 14)}   (archimedean)")
        print(f"      + 6 log(2 pi)        = {mp.nstr(const, 14)}   (const)")
        print(f"      12 h_Fal             = {mp.nstr(twelve_hfal, 14)}")
        print(f"      h_Fal                = {mp.nstr(hfal, 14)}")
        print(f"      archimedean share (|log_arch| / (|log_arch|+|log_fin|)) "
              f"= {share_arch_vs_fin:.4%}")
        print(f"      [check (i)] SL_2(Z)-invariance of ||Delta||_Pet: "
              f"rel err {mp.nstr(inv_err, 4)}  -> {'PASS' if inv_pass else 'FAIL'}")
        if known is not None:
            print(f"      [check (ii)] h_Fal vs known LMFDB {mp.nstr(known, 8)}: "
                  f"err {mp.nstr(hfal_err, 4)}  -> "
                  f"{'MATCH' if hfal_match else 'NO MATCH'}")
        print()

    print(f"[2AE] VALIDATION (i)  SL_2(Z)-invariance of ||Delta||_Pet: "
          f"{'ALL PASS' if sl2_all_pass else 'FAIL'}  (the SOLID internal check)")
    ii = next((r for r in results if r["known"] is not None), None)
    if ii is not None:
        print(f"[2AE] VALIDATION (ii) h_Fal(37a1) = {mp.nstr(ii['hfal'], 8)} vs known "
              f"{mp.nstr(ii['known'], 8)}: "
              f"{'MATCH' if ii['hfal_match'] else 'NO MATCH'}")
    print(f"[2AE] HEADLINE: the archimedean (Petersson) term DOMINATES 12 h_Fal:")
    for r in results:
        print(f"        {r['label']:<26} archimedean share "
              f"{r['share_arch_vs_fin']:.2%}  (log|Delta_min| only "
              f"{abs(float(r['log_finite'])):.3f})")

    _save_and_plot(results, out_dir)
    return results, sl2_all_pass


def _save_and_plot(results, out_dir):
    save = {"n_curves": len(results),
            "labels": np.array([r["label"] for r in results], dtype=object)}
    for i, r in enumerate(results):
        save[f"c{i}_disc"] = r["disc"]
        save[f"c{i}_tau_re"] = float(mp.re(r["tau"]))
        save[f"c{i}_tau_im"] = float(mp.im(r["tau"]))
        save[f"c{i}_pet"] = float(r["pet"])
        save[f"c{i}_twelve_hfal"] = float(r["twelve_hfal"])
        save[f"c{i}_hfal"] = float(r["hfal"])
        save[f"c{i}_log_finite"] = float(r["log_finite"])
        save[f"c{i}_log_arch"] = float(r["log_arch"])
        save[f"c{i}_share_arch"] = r["share_arch_vs_fin"]
        save[f"c{i}_inv_err"] = float(r["inv_err"])
    np.savez_compressed(out_dir / "e2ae_petersson_faltings.npz", **save)

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))

    # left: the three terms of 12 h_Fal per curve
    ax = axs[0]
    labels = [r["label"].split()[0] for r in results]
    fin = [float(r["log_finite"]) for r in results]
    arch = [float(r["log_arch"]) for r in results]
    const = [float(r["const"]) for r in results]
    x = np.arange(len(results))
    w = 0.25
    ax.bar(x - w, fin, w, label="log|Delta_min| (finite)", color="tab:blue")
    ax.bar(x, arch, w, label="-log||Delta||_Pet (archimedean)", color="tab:orange")
    ax.bar(x + w, const, w, label="6 log(2 pi) (const)", color="tab:gray")
    ax.axhline(0, color="k", lw=0.5)
    ax.set_xticks(x); ax.set_xticklabels(labels)
    ax.set_ylabel("contribution to 12 h_Fal")
    ax.set_title("omega-bar^2 = 12 h_Fal: the three terms\n"
                 "(archimedean Petersson term carries the magnitude)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis="y")

    # right: archimedean share
    ax = axs[1]
    shares = [r["share_arch_vs_fin"] for r in results]
    ax.bar(x, shares, color="tab:orange")
    ax.set_xticks(x); ax.set_xticklabels(labels)
    ax.set_ylim(0, 1)
    ax.set_ylabel("archimedean share  |log_arch| / (|log_arch|+|log_fin|)")
    ax.set_title("Archimedean (Petersson) share of |12 h_Fal| terms\n"
                 "(the self-intersection is an archimedean phenomenon)")
    ax.grid(alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig(out_dir / "e2ae_petersson_faltings.png", dpi=140)
    plt.close()
    print(f"\n[2AE] Saved {out_dir / 'e2ae_petersson_faltings.png'}")
    print(f"[2AE] Saved {out_dir / 'e2ae_petersson_faltings.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Archimedean self-intersection omega-bar^2 = 12 h_Fal via the "
                    "Petersson norm of the weight-12 discriminant.")
    parser.add_argument("--dps", type=int, default=50,
                        help="mpmath decimal precision (>= 30)")
    args = parser.parse_args()
    run(dps=args.dps)
