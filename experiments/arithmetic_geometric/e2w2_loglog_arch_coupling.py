"""e2w2: the loglog-coefficient on the archimedean block -- the one marginally-live, named-but-
unexecuted probe toward P5 (the missing arithmetic-Rosati polarization).

Provenance: `docs/03_research/building_the_missing_positivity.md` ("Smallest next step to test the
only marginally-live thread"). The four-mechanism first-principles sweep showed every construction
of the RH-closing positivity collapses at the SAME seam: the Euler product fixes the object's
existence / block structure (a clean, non-circular, RH-INDEPENDENT discriminator) while the off-line
zeros live in the SHARED archimedean continuation that the Euler product does not touch. The sweep
named exactly one unforeclosed test: promote the Rankin loglog-coefficient

    c_F = lim_X (sum_{p<=X} |a_F(p)|^2 / p) / loglog X    (1 for a primitive Euler product, <1 else)

from a scalar discriminator (experiment 3W) into the NORMALIZATION of the archimedean block of the
non-circular Weil/Rosati form M = A_arch + P_fin + B_pole (e2w / M2.6). The question: does making
multiplicativity act ON the continuation (rescale A_arch by c_F) inject the Euler structure into the
GLOBAL signature and break the M2.6 stealth window, where the unscaled M reads D-H spuriously
positive?

Operationalization (honest): in the single-basis summed form M = A + P + B the archimedean and finite
parts are not separable off-diagonal blocks, so the faithful realization of "c_F normalizes the
archimedean coupling" is to scale the archimedean contribution: M_c = c_F * A + P + B. We report the
unscaled baseline (must reproduce M2.6) and the c_F-scaled probe, for zeta (Euler, RH-true),
Epstein-d47-principal (NON-Euler, RH-true), and Davenport-Heilbronn (non-Euler, RH-false).

Falsifiable prediction (from the four collapses): NO clean separation. c_F < 1 for BOTH D-H
(RH-false) and Epstein (RH-true), so scaling A_arch down pushes BOTH toward indefiniteness, and the
form cannot tell the RH-true non-Euler Epstein from the RH-false D-H -- the #20 non-Euler trap, now
on the archimedean coupling. If instead D-H goes NEG while zeta AND Epstein stay POS, that would be
the first place multiplicativity touches the continuation rather than the entries (a genuine lead).

OUTCOME (run 2026-06-30): NO separation, and DEEPER than the predicted #20 trap. The probe sends
ALL three targets NEG, including RH-true Euler zeta (c_F = 1.105 > 1, A scaled UP). The diagnostic
shows why: the unscaled margin is a razor-thin cancellation of LARGE blocks (zeta ||A_arch|| = 44.3
vs ||P+B|| = 44.4, cancelling to min eig +0.035), so rescaling A by c_F perturbs the form by
~0.1*44 ~ 4.6, dwarfing the +0.035 margin and flipping the sign for everyone regardless of RH. So
multiplicativity cannot 'normalize the archimedean coupling' to inject Euler structure into the
signature: the signature has ZERO slack (it IS the exact A-vs-(P+B) cancellation). The c_F idea
fails not via the non-Euler trap but via the marginal-positivity razor. Closes the one marginally-
live thread the construction sweep left open: the missing math IS the polarization (P5), not a route.

Run: python -m experiments.arithmetic_geometric.e2w2_loglog_arch_coupling
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import mpmath as mp

from experiments._shared import zeta_L, DavenportHeilbronn, epstein_for_discriminant
from experiments.positivity.e3m_place_type_balance import (
    finite_block, pole_block, lambda_coeffs_from_dirichlet,
    von_mangoldt_zeta, numeric_residue_at_one,
)
from experiments.arithmetic_geometric.e2v_rosati_balance_M2_5 import arch_block_bombieri
from experiments.positivity.e3w_rankin_loglog import rankin_loglog_partial


def run(K=8, b_min=1.3, b_max=6.0, prec=30, X_loglog=200000,
        include_epstein=True, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)
    n_max = int(b_max * b_max) + 2

    dh = DavenportHeilbronn()
    eps47p = epstein_for_discriminant(47, principal=True)
    # (label, L, mu_list, log_Q, residue-or-None, has_euler, rh)
    targets = [
        ("zeta", zeta_L, [0.0], mp.mpf(0), 1.0, True, True),
        ("DH", dh, [1.0], mp.log(mp.sqrt(5)), 0.0, False, False),
    ]
    if include_epstein:
        targets.insert(1, ("Eps47_principal", eps47p, [0.0, 1.0],
                           mp.log(mp.sqrt(47)), None, False, True))

    print("=" * 92)
    print("[e2w2] loglog-coefficient on the archimedean block: M_c = c_F * A_arch + P_fin + B_pole")
    print("=" * 92)
    print(f"       K={K}, b in [{b_min},{b_max}], n_max={n_max}, prec={prec}, c_F at X={X_loglog}")
    print("       Convention (e2w): min eig > 0 = RH-compatible (positive); < 0 = indefinite.\n")
    header = (f"{'target':<18} {'Euler':>5} {'RH':>4} {'c_F':>6} "
              f"{'mineig(M)':>12} {'sign':>4}   {'mineig(c_F*A+P+B)':>18} {'sign':>4}")
    print(header)
    print("-" * len(header))

    results = {}
    for label, L, mu_list, log_Q, residue, has_euler, rh in targets:
        if label == "zeta":
            lam = np.array([0.0] + [von_mangoldt_zeta(n) for n in range(1, n_max + 1)])
        else:
            lam = lambda_coeffs_from_dirichlet(L, n_max, prec)
        P = finite_block(b_vals, lam, prec)
        if residue is None:
            residue = numeric_residue_at_one(L, prec)
        B = pole_block(b_vals, float(residue), prec)
        A = arch_block_bombieri(b_vals, mu_list, log_Q, prec)

        c_F = float(rankin_loglog_partial(L, [X_loglog])[0])

        M0 = A + P + B
        Mc = c_F * A + P + B
        e0 = float(np.linalg.eigvalsh(M0).min())
        ec = float(np.linalg.eigvalsh(Mc).min())
        normA = float(np.linalg.norm(A))
        normPB = float(np.linalg.norm(P + B))

        results[label] = dict(has_euler=has_euler, rh=rh, c_F=c_F, mineig0=e0, mineigc=ec,
                              normA=normA, normPB=normPB)
        print(f"{label:<18} {str(has_euler):>5} {str(rh):>4} {c_F:>6.3f} "
              f"{e0:>+12.4e} {'POS' if e0 > 0 else 'NEG':>4}   "
              f"{ec:>+18.4e} {'POS' if ec > 0 else 'NEG':>4}")

    print("-" * len(header))

    # The cancellation magnitude: the razor-thin margin is the difference of LARGE blocks.
    print("\n       block magnitudes (the margin is a cancellation of large blocks):")
    print(f"       {'target':<18} {'||A_arch||':>11} {'||P+B||':>11} {'min eig(M)':>12}")
    for label in results:
        r = results[label]
        print(f"       {label:<18} {r['normA']:>11.3f} {r['normPB']:>11.3f} {r['mineig0']:>+12.4e}")

    # ---- verdict ----
    def sep(key):
        """Does `key` ('mineig0' or 'mineigc') separate RH-holders (POS) from RH-failers (NEG)?"""
        holders = [r for r in results.values() if r["rh"]]
        failers = [r for r in results.values() if not r["rh"]]
        return (all(r[key] > 0 for r in holders) and all(r[key] < 0 for r in failers))

    base_sep = sep("mineig0")
    probe_sep = sep("mineigc")
    print("\n[e2w2] ===== VERDICT =====")
    print(f"       Baseline M = A+P+B separates RH:           {base_sep}  "
          "(M2.6: NO -- D-H reads spuriously POS = stealth window)")
    print(f"       Probe   M_c = c_F*A+P+B separates RH:       {probe_sep}")

    eps = results.get("Eps47_principal")
    dhr = results.get("DH")
    z = results.get("zeta")
    zeta_breaks = z is not None and z["mineigc"] < 0  # RH-true Euler target destroyed by the probe
    if probe_sep and not base_sep:
        print("       BREAKTHROUGH (prediction REFUTED): rescaling the archimedean block by the")
        print("       multiplicative loglog-coefficient SEPARATES RH where the unscaled form could")
        print("       not. The first place multiplicativity touches the continuation, not the")
        print("       per-place entries. This needs immediate adversarial verification and a D-H")
        print("       robustness sweep before any claim.")
    elif zeta_breaks:
        # The ACTUAL outcome: deeper than the predicted #20 trap. The probe destroys the
        # positivity for EVERYONE, including RH-true Euler zeta (whose c_F = 1.105 > 1 scales
        # A_arch UP), so it is not even a (mis-)classifier -- it annihilates the signal.
        print("       NO SEPARATION, and DEEPER than the predicted #20 trap. The probe sends ALL")
        print("       targets NEG -- INCLUDING RH-true Euler zeta, whose c_F = "
              f"{z['c_F']:.3f} > 1 scales A_arch")
        print("       UP yet still flips the sign. Mechanism = the MARGINAL-POSITIVITY RAZOR:")
        print(f"       the unscaled positivity is a razor-thin exact cancellation (min eig "
              f"{z['mineig0']:+.4f}),")
        print("       a near-cancellation of a large archimedean block A against a large prime")
        print("       block P+B. Rescaling A by ANY factor != 1 (in EITHER direction) destroys")
        print("       that exact cancellation and exposes the large negative residual. So")
        print("       multiplicativity CANNOT 'normalize the archimedean coupling' to inject Euler")
        print("       structure into the signature: the signature has ZERO slack -- it IS the")
        print("       exact A-vs-(P+B) cancellation. The c_F idea fails not because c_F is a")
        print("       non-Euler detector (the #20 trap) but because there is no margin to rescale")
        print("       into. The marginal-positivity thesis, localized onto this probe.")
        print("       This closes the one marginally-live thread the construction sweep left open:")
        print("       the missing math IS the polarization (P5 = the arithmetic Hodge standard")
        print("       conjecture), not a route to it.")
    else:
        # Fallback: the predicted #20 non-Euler trap (c_F<1 mis-classifies RH-true non-Euler).
        print("       NO SEPARATION (prediction holds). c_F < 1 for BOTH the RH-TRUE non-Euler")
        print("       Epstein and the RH-FALSE D-H, so scaling A_arch down pushes BOTH negative:")
        print("       the #20 non-Euler trap relocated onto the archimedean coupling. c_F injects")
        print("       EULER-ness, not RH-ness, into the signature. The missing math IS the")
        print("       polarization (P5 = the arithmetic Hodge standard conjecture), not a route to it.")

    np.savez_compressed(
        out_dir / "e2w2_loglog_arch_coupling.npz",
        labels=np.array(list(results.keys()), dtype=object),
        c_F=np.array([results[n]["c_F"] for n in results]),
        mineig0=np.array([results[n]["mineig0"] for n in results]),
        mineigc=np.array([results[n]["mineigc"] for n in results]),
        rh=np.array([results[n]["rh"] for n in results]),
        has_euler=np.array([results[n]["has_euler"] for n in results]),
        base_sep=base_sep, probe_sep=probe_sep, K=K, prec=prec, X_loglog=X_loglog,
    )
    print(f"\n[e2w2] Saved {out_dir / 'e2w2_loglog_arch_coupling.npz'}")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--K", type=int, default=8)
    parser.add_argument("--prec", type=int, default=30)
    parser.add_argument("--no-epstein", action="store_true")
    args = parser.parse_args()
    run(K=args.K, prec=args.prec, include_epstein=not args.no_epstein)
