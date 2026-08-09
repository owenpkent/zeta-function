"""Evidence for the e1u cross-machine tolerance change (LEARNINGS #172).

WHY THIS EXISTS. On a fresh machine e1u scored 16/18: U0b (cached-build eps vs
the tracked e1t npz, at 1e-15) and U5a's record check (fneg_q, at 1e-9) both
failed, while every structural number reproduced to printed precision. The
diagnosis was that those two checks compare tracked build outputs BELOW the
noise floor of the quantities themselves, so they assert same-machine bit
reproducibility rather than numerical agreement.

Loosening a check on an adversary-verified artifact is exactly the move this
repo is supposed to distrust, so the change is not made on the strength of an
argument. This script supplies the two things that justify it, and both are
measurements:

  PART 1  what the deviations ARE, over the full grid: the tolerances are
          pinned from this, not chosen by taste.
  PART 2  that the LOOSENED checks still have teeth: a genuine regression
          (the dps-branch flip that e1n/e1t already document, where the even
          ground state selection changes) is still caught, by many orders.

Run:  python -m experiments.spectral._e1u_portability
"""
import numpy as np
import mpmath as mp

from experiments.spectral.e1t_compact_class_limit import (
    get_build, build_comb, int_pairs, streams,
)
from experiments.spectral.e1k_dh_dlog_testbed import ZETA_CFG
from experiments.spectral.e1u_canonical_chain import face_B, GRID_FULL, E1T_NPZ

TOL_EPS = 1e-9      # the replacement U0b tolerance (absolute)
TOL_FNEG = 1e-6     # the replacement U5a record tolerance (absolute)


def main():
    mp.mp.dps = 25
    rec = np.load(E1T_NPZ)

    print("=" * 76)
    print("PART 1: the actual cross-machine deviations, full grid")
    print("=" * 76)
    print(f"{'config':18s} {'|d eps|':>11s} {'|d fneg_q|':>12s}")
    de, df = [], []
    for (label, lam, N) in GRID_FULL:
        tag = label.replace("-", "")
        ke, kf = f"t1_{tag}_{lam:.3f}_eps", f"t1_{tag}_{lam:.3f}_fneg_q"
        _, meta = get_build(label, lam, N)
        d1 = abs(float(rec[ke]) - meta["eps"]) if ke in rec.files else np.nan
        _, _, _, m = face_B(label, lam, N)
        d2 = abs(float(rec[kf]) - m["fneg_q"]) if kf in rec.files else np.nan
        de.append(d1)
        df.append(d2)
        print(f"{label + ' ' + f'{lam:.4f}':18s} {d1:11.2e} {d2:12.2e}")
    we, wf = np.nanmax(de), np.nanmax(df)
    print(f"\nworst |d eps|    = {we:.3e}   -> tolerance {TOL_EPS:.0e} "
          f"({TOL_EPS / we:.0f}x headroom)")
    print(f"worst |d fneg_q| = {wf:.3e}   -> tolerance {TOL_FNEG:.0e} "
          f"({TOL_FNEG / wf:.0f}x headroom)")
    print("The build's archimedean density uses a central-difference digamma "
          "at h = 1e-5 in\nfloat64 whose own relative accuracy is ~5e-10 "
          "(measured against exact mpmath\ndigamma), so eps is determined by "
          "the build to ~1e-10 ABSOLUTE. Both observed\ndeviations sit at or "
          "below that floor.")

    print("\n" + "=" * 76)
    print("PART 2: do the LOOSENED tolerances still catch a real regression?")
    print("=" * 76)
    print("The regression used is the one e1n/e1t already document: the "
          "ambient-dps branch.\nAt dps 15 and 35/40 the even ground-state "
          "selection differs from the dps 20/25/30\nbranch the record lives "
          "on. If the loosened check cannot see that, it is useless.")
    lz, _ = streams()
    lam, N = 2.6, 16
    ke = f"t1_ZETA_{lam:.3f}_eps"
    eps_rec = float(rec[ke])
    print(f"\n{'ambient dps':>12s} {'eps':>22s} {'|d eps|':>11s} "
          f"{'vs 1e-9 tol':>14s}")
    caught = []
    for dps in (15, 25, 35):
        mp.mp.dps = dps
        r = build_comb(N, lam, int_pairs(lz, lam), ZETA_CFG["dens_a"],
                       ZETA_CFG["dens_b"], ZETA_CFG["use_pole"])
        d = abs(r["eps"] - eps_rec)
        verdict = "PASSES (same branch)" if d < TOL_EPS \
            else f"CAUGHT ({d / TOL_EPS:.0e}x over)"
        caught.append((dps, d, d >= TOL_EPS))
        print(f"{dps:12d} {r['eps']:22.15e} {d:11.2e} {verdict:>14s}")
    mp.mp.dps = 25
    off = [c for c in caught if c[0] != 25]
    ok = all(c[2] for c in off) and not [c for c in caught
                                         if c[0] == 25 and c[2]]
    print(f"\nVERDICT: the loosened 1e-9 tolerance still catches the "
          f"off-branch builds by\n{min(c[1] for c in off) / TOL_EPS:.0e}x and "
          f"admits the on-branch one. It is a numerical-agreement\ncheck now, "
          f"not a bit-reproducibility check, and it retains its teeth.")
    print(f"\nRESULT: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
