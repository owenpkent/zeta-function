"""EAC.3 - Reverse-engineering ingredient (iii): the bound-halving energy form.

Step 3 of the acoustic thread. EAC.1/EAC.2 localized the missing M4 polarization
to ONE ingredient: a Lorentzian energy form whose signature makes the arithmetic
medium contractive. This script reverse-engineers what that form must DO, by
contrasting the bound that PASSIVITY alone gives (free, unconditional) with the
bound RH requires.

THE HALVING. There are two bounds on the resonances/zeros:

  - PASSIVE (trivial) bound, FREE from the Euler product:
        function field : |alpha_i| <= q          (exponent 1)
        zeta           : no zeros in Re(s) > 1    (abscissa 1)
    For zeta this is exactly because Z = -zeta'/zeta = sum Lambda(n) n^{-s} is a
    convergent Dirichlet series with a NON-NEGATIVE (passive) comb for Re > 1, so
    zeta has no zeros there. Passivity = no zeros right of the abscissa of
    absolute convergence. Unconditional. NOT RH.

  - RH bound, the SHARPENED one:
        function field : |alpha_i| = sqrt(q)      (exponent 1/2)
        zeta           : Re(s) = 1/2              (abscissa 1/2)

So RH is exactly the statement that the passive bound is HALVED: exponent 1 -> 1/2,
q -> sqrt(q), abscissa 1 -> 1/2. In the function field the halving is a THEOREM:
the Hodge index theorem on C x C (the Lorentzian (1, n-1) intersection form)
performs it (EAC.2: passive + reciprocal => lossless). The missing ingredient (iii)
over Spec(Z) is precisely an energy form that performs the SAME halving. This is a
sharp, reverse-engineered specification of the target: not "prove a positivity" but
"supply the structure that halves the passive exponent 1 -> 1/2."

It also explains the analytic ceiling: zero-free-region methods try to chip the
abscissa down from 1 toward 1/2 analytically and stall at the Vinogradov-Korobov
2/3 exponent. They stall because they attempt the halving WITHOUT the structural
energy form; the halving is geometric (a signature), not analytic.

THE ALL-PASS MECHANISM (why passivity is necessary but not sufficient). The
functional equation makes the completed L a LOSSLESS ALL-PASS / para-unitary
system, for BOTH zeta and D-H. An off-line zero rho = beta + i gamma (beta != 1/2)
comes with a full FE+conjugate ORBIT {rho, 1-rho, rho_bar, 1-rho_bar}: a genuine
4-point all-pass section (mirror-image poles/zeros straddling the line). An on-line
zero degenerates: 1 - rho = rho_bar, so the orbit collapses to the 2-point pair
{rho, rho_bar} ON the axis. Thus:

    RH  <=>  every all-pass section is DEGENERATE (pinned to the axis).

Passivity (positive comb / Euler product) forbids off-axis sections only in
Re > 1 (no zeros there at all). The strip 1/2 < beta < 1 is the GAP: passivity
permits genuine all-pass quads there; only the halving energy form (iii) closes it.
D-H, with an ACTIVE impedance (signed comb, EAC.1), carries a genuine all-pass quad
at beta ~ 0.808, which this script exhibits.

Outputs:
  - eac3_halving_and_allpass.npz
  - stdout : the halving table (FF) + the all-pass orbit contrast (zeta vs D-H)
"""

from __future__ import annotations

import argparse
from pathlib import Path

import mpmath as mp
import numpy as np

from experiments.acoustic.eac2_ff_passive_lossless import frobenius_eigenvalues
from experiments.arithmetic_geometric.e2f_hodge_index_sweep import (
    elliptic_family,
    genus2_family,
)


def halving_table(primes_elliptic=(5, 7, 11, 13, 17, 19), primes_genus2=(5, 7, 11)):
    """For each curve: the passive exponent (1, bound |alpha|<=q) vs the realized
    RH exponent log|alpha|/log q (= 1/2). The gap between them is the halving the
    Hodge-index energy form performs."""
    curves = elliptic_family(list(primes_elliptic))
    if primes_genus2:
        curves += genus2_family(list(primes_genus2))
    rows = []
    for c in curves:
        q = c["p"]
        alpha = frobenius_eigenvalues(c)
        mods = np.abs(alpha)
        realized_exp = float(np.mean(np.log(mods) / np.log(q)))  # = 1/2 under RH
        passive_exp = 1.0                                        # |alpha| <= q free
        rows.append(dict(label=c["label"], q=q, g=c["g"],
                         realized_exp=realized_exp,
                         passive_exp=passive_exp,
                         halving=passive_exp - realized_exp))
    return rows


def allpass_orbit(rho):
    """The FE + conjugate orbit {rho, 1-rho, rho_bar, 1-rho_bar} of a zero.
    Returns the distinct points and whether the section is DEGENERATE (on axis)."""
    rho = mp.mpc(rho)
    orbit = [rho, 1 - rho, mp.conj(rho), 1 - mp.conj(rho)]
    # dedupe to ~1e-9
    distinct = []
    for z in orbit:
        if not any(abs(z - w) < mp.mpf("1e-9") for w in distinct):
            distinct.append(z)
    degenerate = all(abs(mp.re(z) - mp.mpf("0.5")) < mp.mpf("1e-9") for z in distinct)
    return distinct, degenerate


def run(out_dir: Path = None, dps: int = 30):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    mp.mp.dps = dps

    print("[EAC.3] Reverse-engineering ingredient (iii): the bound-HALVING form.\n")

    # ---- Part 1: the halving, function field ----
    print("  [Part 1] The halving (function field): passive |alpha|<=q (exp 1) vs")
    print("           RH |alpha|=sqrt(q) (exp 1/2). The Hodge index performs it.\n")
    rows = halving_table()
    print(f"        {'curve':<28} {'q':>3} {'passive exp':>11} {'realized exp':>12} {'halving':>8}")
    for r in rows:
        print(f"        {r['label']:<28} {r['q']:>3} {r['passive_exp']:>11.3f} "
              f"{r['realized_exp']:>12.5f} {r['halving']:>8.5f}")
    mean_realized = float(np.mean([r["realized_exp"] for r in rows]))
    print(f"\n        mean realized exponent = {mean_realized:.6f}  (= 1/2 exactly under RH)")
    print(f"        the Hodge-index energy form HALVES the passive exponent 1 -> 1/2.")
    print(f"        Spec(Z) analogue: passive abscissa 1 (Euler product, no zeros")
    print(f"        right of Re=1) must be halved to 1/2. (iii) IS that halving form.\n")

    # ---- Part 2: the all-pass orbit contrast ----
    print("  [Part 2] All-pass degeneracy: off-line zero = genuine 4-point section,")
    print("           on-line zero = degenerate pair on the axis.\n")

    # a zeta on-line zero (first one): rho = 1/2 + i*14.1347...
    gamma1 = mp.im(mp.zetazero(1))
    rho_zeta = mp.mpc(mp.mpf("0.5"), gamma1)
    orb_z, deg_z = allpass_orbit(rho_zeta)
    print(f"        zeta zero rho = 0.5 + {float(gamma1):.4f}i  (on-line):")
    print(f"          orbit has {len(orb_z)} distinct point(s); DEGENERATE = {deg_z}")
    for z in orb_z:
        print(f"            {complex(z):.4f}")

    # D-H off-line zero (repo landmark): rho ~ 0.8085 + 85.699 i
    rho_dh = mp.mpc(mp.mpf("0.8085"), mp.mpf("85.699"))
    orb_d, deg_d = allpass_orbit(rho_dh)
    print(f"\n        D-H zero rho ~ 0.8085 + 85.699i  (OFF-line):")
    print(f"          orbit has {len(orb_d)} distinct point(s); DEGENERATE = {deg_d}")
    for z in orb_d:
        print(f"            {complex(z):.4f}")
    print(f"\n        => off-line = genuine all-pass quad (mirror pairs straddling the")
    print(f"           line); on-line = degenerate. RH <=> every section degenerate.")
    print(f"           Passivity forbids sections only in Re>1; the strip 1/2<beta<1")
    print(f"           is the gap (iii) must close. D-H's active impedance permits the")
    print(f"           quad; zeta's passive impedance does not (in Re>1) but passivity")
    print(f"           alone cannot reach Re=1/2 -- that needs the halving form.\n")

    print("  [SYNTHESIS] Reverse-engineered specification of the missing M4 object:")
    print("    (iii) = a Lorentzian energy form on arithmetic divisor classes whose")
    print("    SIGNATURE halves the free passive bound (abscissa 1 -> 1/2, q -> sqrt q),")
    print("    exactly as the Hodge index theorem does on C x C. It is OFF-SHELL (on")
    print("    divisor classes, Lorentzian (1,n-1)), distinct from the circular")
    print("    on-shell Weil Gram (definite under RH). The analytic 2/3 ceiling is what")
    print("    happens when you attempt the halving WITHOUT this structure.")

    np.savez_compressed(
        out_dir / "eac3_halving_and_allpass.npz",
        ff_q=np.array([r["q"] for r in rows]),
        ff_realized_exp=np.array([r["realized_exp"] for r in rows]),
        ff_passive_exp=np.array([r["passive_exp"] for r in rows]),
        mean_realized_exp=mean_realized,
        zeta_orbit_size=len(orb_z), zeta_degenerate=deg_z,
        dh_orbit_size=len(orb_d), dh_degenerate=deg_d,
        dh_orbit_re=np.array([float(mp.re(z)) for z in orb_d]),
        dh_orbit_im=np.array([float(mp.im(z)) for z in orb_d]),
    )
    print(f"\n[EAC.3] Saved {out_dir / 'eac3_halving_and_allpass.npz'}")
    return rows, (deg_z, deg_d)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Bound-halving + all-pass reverse-engineering of ingredient (iii).")
    ap.add_argument("--dps", type=int, default=30)
    args = ap.parse_args()
    run(dps=args.dps)
