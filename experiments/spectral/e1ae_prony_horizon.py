"""E1AE: the horizon-optimality probe (e1ad adversary case 3, executed as a
build; audit falsifier 4's decision instrument; session 5 of the #201 order).

THE QUESTION (#188's sharpest residue). The truncated Szego register certifies
non-membership in the scale-D lattice only at the collision horizon: ~sqrt(2DL)
ATOMS (the birthday scale; measured termination law, e1ad R4). Is that scale
optimal among ALL functionals of the first n moments, or does a
super-resolution register (Prony / matrix-pencil / annihilating-polynomial
root recovery) beat it? The audit's falsifier 4 rides on the answer: if a
super-resolution register beats the birthday AND precision scales, the #188
ceiling is a family artifact and the counting-side obstruction weakens.

THE REGISTER BUILT HERE. For an M-atom circle measure, the first M+1 moments
determine the measure exactly: the monic OPUC Phi_M(z) = prod (z - z_j) is the
annihilating polynomial, its coefficients solve the M x M Toeplitz system
sum_m coef_m c_{m-k} = -c_{M-k} (k = 0..M-1) on the SAME moment data the
Szego functional consumes, and its roots are the atoms. Recovery precision is
limited by the working precision through the moment-system conditioning
(kappa(T_M) ~ e^{S}: the Szego rate S IS the log-conditioning of this very
recovery: the two registers are two faces of one quantity). The lattice
detector then reads the recovered angles directly: s_j = dist(D theta_j, Z)
(theta in turns, L = 1): SNAP concentrates at 0, matched jitter sits at
median ~0.25.

PRE-REGISTERED (rule 1), before any recovery was run:
  P1  EXPECT: the register DETECTS the scale-D lattice at M = 78 atoms and
      n = M+1 moments for D up to 1e6, i.e. far below the birthday scale
      (sqrt(2D) = 1414 atoms at D = 1e6, where e1ad's register is provably
      blind, zero collisions): the ATOM-currency horizon is
      FUNCTIONAL-RELATIVE, a property of the Szego register, not of moment
      data. KILL: no detection at any dps <= 640: the birthday scale binds
      even for super-resolution at exact moments; falsifier 4 resolves in
      the strengthening direction.
  P2  EXPECT: the price moves to the DIGITS currency with an
      information-theoretic floor: dps*(D) grows with D (at least
      lg10(D) - lg10(M) - 2, the moment-visibility floor) and is bounded by
      the conditioning estimate lg10 kappa(T_M) + lg10 D + 40. Certifying
      genuine Q-linear independence (D -> infinity) then costs unbounded
      DIGITS: the #172/#188 obstruction survives as a two-currency theorem
      (atoms for rate registers, digits for recovery registers), and the
      birthday pricing is re-scoped, not the obstruction.
      KILL: detection at D = 1e6 with dps* <= lg10(D) - lg10(M) - 2 or
      flat-in-D dps*: the wall is beaten in BOTH currencies: audit
      falsifier 4 FIRES in the escalation direction (the ceiling quantifiers
      are family artifacts; frontier-adjacent; reopen).
  P3  CONTROLS: TRUE and matched-jitter JIT are NOT detected at dps* (no
      false positives; median s >= 0.1 for both). KILL: false positive: the
      detector is broken; fix before any claim.

DISCIPLINES. Joint: the counting-side S4/R1 coordinate (the Q-linear
independence of {log p}: #162/#169/#172/#188's axis); this is an instrument
probe on the fake-vs-true LATTICE question, no zeta zeros anywhere (same
posture as e1ad: no L-function data consumed; the Beurling/D-H bracket was
run at the e1ad level and this register consumes the identical moment data).
K1: does not arise (no truth value about zeros asserted or consumed).

Run:  python -m experiments.spectral.e1ae_prony_horizon [--quick]
Data: e1ae_prony_horizon.npz (tracked next to this script).
"""

from __future__ import annotations

import math
import time

import numpy as np
from mpmath import mp

from experiments._shared.harness import Gates, PreRegistry, quick_arg, save_npz
from experiments.spectral.e1ad_sum_rules import (
    cfg_float, cfg_snap, cfg_true, materialize, snap_sites, true_pk,
)

N_SIZE = 300                 # M = 78 atoms (the e1ad small size)
DS_FULL = [10 ** 4, 10 ** 6]
DS_QUICK = [10 ** 4]
DPS_LADDER = [14, 16, 18, 20, 22, 24, 26, 28, 32, 40, 64, 128, 320, 640]
DETECT = 0.01                # median dist(D theta, Z) below this = detected
CLEAN = 0.10                 # controls must sit above this
JIT_SEED = 20260825


def moments(cfg, n, dps):
    """c_m = sum_j w_j e^{2 pi i m theta_j}, m = 0..n, at working precision."""
    th, w = materialize(cfg, dps)
    with mp.workdps(dps):
        two_pi = 2 * mp.pi
        return [mp.fsum((mp.mpf(wj) * mp.e ** (mp.mpc(0, 1) * two_pi * m * tj)
                         for tj, wj in zip(th, w)), absolute=False)
                for m in range(n + 1)], len(th)


def recover(cfg, dps):
    """(angles_turns, lg_cond_proxy). Consumes moments only."""
    # first materialize once just to learn M (atom count), then moments
    th0, _ = materialize(cfg, 40)
    M = len(th0)
    with mp.workdps(dps):
        c, _ = moments(cfg, M, dps)
        cneg = [mp.conj(x) for x in c]

        def cm(l):
            return c[l] if l >= 0 else cneg[-l]

        A = mp.matrix(M, M)
        b = mp.matrix(M, 1)
        for k in range(M):
            for m in range(M):
                A[k, m] = cm(m - k)
            b[k] = -cm(M - k)
        coef = mp.lu_solve(A, b)
        # honest conditioning meter: Cholesky of the Hermitian PD Toeplitz
        # block; lg10 kappa ~ (2/ln 10)(max - min) of lg|L_kk| (the same
        # determinant-ratio quantity the Szego rate S measures)
        try:
            Lc = mp.cholesky(A)
            dlg = [mp.log10(abs(Lc[i, i])) for i in range(M)]
            lg_cond = float(2 * (max(dlg) - min(dlg)))
        except Exception:
            lg_cond = float("nan")
        poly = [mp.mpf(1)] + [coef[M - 1 - i] for i in range(M)]
        roots = mp.polyroots(poly, maxsteps=300, extraprec=80)
        th = sorted((mp.arg(r) / (2 * mp.pi)) % 1 for r in roots)
        offc = max(abs(abs(r) - 1) for r in roots)
        return [mp.mpf(x) for x in th], lg_cond, float(offc)


def lattice_stat(th_turns, D, dps):
    """median_j dist(D theta_j, Z) in units of one site."""
    with mp.workdps(dps):
        s = sorted(abs(D * t - mp.nint(D * t)) for t in th_turns)
        return float(s[len(s) // 2])


def recovery_error(th_hat, cfg, dps):
    """Diagnostic only (oracle-free: compares to the config's own angles)."""
    th, _ = materialize(cfg, dps)
    th = sorted(th)
    with mp.workdps(dps):
        errs = [min(abs(a - b), 1 - abs(a - b)) for a, b in zip(th_hat, th)]
        return float(max(errs))


def main() -> int:
    t_start = time.perf_counter()
    quick = quick_arg()
    gates = Gates(quick=quick)
    pre = PreRegistry()
    pre.register("P1", "detection at M = 78 atoms, n = M+1 moments, D up to 1e6",
                 "no detection at any dps <= 640: the birthday scale binds")
    pre.register("P2", "the price is in DIGITS: dps*(D) grows with D within the "
                       "conditioning+lg D bound; the obstruction re-prices, not breaks",
                 "detection at the information floor or flat-in-D: falsifier 4 FIRES")
    pre.register("P3", "no false positives on TRUE / matched JIT at dps*",
                 "false positive: detector broken")

    Ds = DS_QUICK if quick else DS_FULL
    ladder = [d for d in DPS_LADDER if quick is False or d <= 160]
    print(f"e1ae: Prony horizon probe (e1ad case 3; falsifier 4)  "
          f"[{'quick' if quick else 'full'}; N={N_SIZE}, D={Ds}, dps ladder {ladder}]")

    pk = true_pk(N_SIZE)
    M = len(pk)
    birthday = {D: math.sqrt(2 * D) for D in Ds}
    print(f"   M = {M} atoms, n = {M + 1} moments; birthday scale: "
          + ", ".join(f"D={D:g}: {birthday[D]:.0f}" for D in Ds))

    rows = []
    rng = np.random.default_rng(JIT_SEED)
    t_true = np.array([k * math.log(p) for (p, k) in pk])
    colls = {}
    for D in Ds:
        sites, counts, ncoll = snap_sites(pk, D)
        colls[D] = ncoll
        print(f"   D={D:g}: collision census {ncoll} (M_d = {len(sites)})")
        snap = cfg_snap(sites, counts, D, 1.0)
        jit = cfg_float(np.sort((t_true + rng.uniform(-0.5 / D, 0.5 / D, M)) % 1.0),
                        1.0, f"JIT{D:g}")
        dps_star, rec_err, lg_cond, s_hist = None, None, None, []
        for dps in ladder:
            try:
                th_hat, lc, offc = recover(snap, dps)
            except Exception as e:
                print(f"   D={D:g} dps={dps}: recovery failed ({type(e).__name__})")
                s_hist.append((dps, 1.0))
                continue
            s = lattice_stat(th_hat, D, dps)
            s_hist.append((dps, s))
            print(f"   D={D:g} dps={dps}: SNAP med s = {s:.4f} "
                  f"(off-circle {offc:.1e}, cond-proxy lg {lc:.1f})")
            if s < DETECT:
                dps_star, lg_cond = dps, lc
                rec_err = recovery_error(th_hat, snap, dps)
                break
        row = {"D": D, "dps_star": dps_star, "lg_cond": lg_cond,
               "rec_err": rec_err, "s_hist": s_hist}
        if dps_star is not None:
            row["s_wrongD"] = lattice_stat(th_hat, 999983 if D == 10 ** 6 else 9973,
                                           dps_star)
            row["s_multD"] = lattice_stat(th_hat, 2 * D, dps_star)
        if dps_star is not None:
            th_t, _, _ = recover(cfg_true(pk, 1.0), dps_star)
            th_j, _, _ = recover(jit, dps_star)
            row["s_true"] = lattice_stat(th_t, D, dps_star)
            row["s_jit"] = lattice_stat(th_j, D, dps_star)
            print(f"   D={D:g}: DETECTED at dps* = {dps_star} "
                  f"(recovery err {rec_err:.1e}); controls: TRUE {row['s_true']:.3f}, "
                  f"JIT {row['s_jit']:.3f}")
        rows.append(row)

    gates.gate("the headline rung is Szego-blind (zero collisions at max D)",
               colls[max(Ds)] == 0,
               "census: " + ", ".join(f"D={D:g}: {colls[D]}" for D in Ds))
    det = [r for r in rows if r["dps_star"] is not None]
    p1 = len(det) == len(rows) and all(M + 1 < birthday[r["D"]] for r in det)
    gates.gate("P1: detection FAR below the birthday scale at every D",
               p1, "; ".join(f"D={r['D']:g}: dps*={r['dps_star']}, "
                             f"{M + 1} moments vs birthday {birthday[r['D']]:.0f}"
                             for r in det) or "no detections")
    pre.resolve("P1", "FIRED" if p1 else "REFUTED",
                f"{len(det)}/{len(rows)} rungs detected at M = {M}")

    floors = {r["D"]: math.log10(r["D"]) - math.log10(M) - 2 for r in det}
    p2_floor = all(r["dps_star"] >= floors[r["D"]] for r in det)
    p2_grow = (len(det) < 2) or (det[-1]["dps_star"] >= det[0]["dps_star"])
    p2_bound = all(r["dps_star"] <= max(r["lg_cond"], 0) + math.log10(r["D"]) + 40
                   for r in det)
    p2_grow_strict = (len(det) < 2) or (det[-1]["dps_star"] > det[0]["dps_star"])
    p2 = p2_floor and p2_bound and p2_grow_strict
    gates.gate("P2: the price re-locates to digits (floor <= dps* <= cond + lg D + 40)",
               p2, "; ".join(f"D={r['D']:g}: floor {floors[r['D']]:.1f} <= "
                             f"dps* {r['dps_star']} (cond lg {r['lg_cond']:.1f})"
                             for r in det) or "n/a")
    pre.resolve("P2", "FIRED" if p2 else "REFUTED",
                "dps*: " + ", ".join(f"D={r['D']:g}: {r['dps_star']}" for r in det))

    # the 2D statistic doubles in site units at the same absolute precision
    spec = all(r.get("s_wrongD", 1) >= CLEAN and r.get("s_multD", 1) < 2.5 * DETECT
               for r in det)
    gates.gate("detector specificity: wrong modulus reads clean, compatible 2D detects",
               spec, "; ".join(f"D={r['D']:g}: wrongD {r.get('s_wrongD', -1):.3f}, "
                               f"2D {r.get('s_multD', -1):.4f} (site-unit doubling)"
                               for r in det))
    p3 = all(r.get("s_true", 1) >= CLEAN and r.get("s_jit", 1) >= CLEAN for r in det)
    gates.gate("P3: TRUE and matched JIT stay undetected at dps* (no false positives)",
               p3, "; ".join(f"D={r['D']:g}: TRUE {r.get('s_true', -1):.3f}, "
                             f"JIT {r.get('s_jit', -1):.3f}" for r in det) or "n/a")
    pre.resolve("P3", "FIRED" if p3 else "REFUTED", "controls clean" if p3 else "FALSE POSITIVE")

    gates.gate("falsifier 4 disposition recorded",
               True,
               ("ATOM horizon functional-relative (beaten at n = M+1); DIGITS floor "
                "persists: two-currency theorem, obstruction re-priced not broken"
                if (p1 and p2) else
                "see pre-registration table: escalation path documented"))
    gates.gate("no unresolved pre-registrations", pre.unresolved() == [])

    elapsed = time.perf_counter() - t_start
    save_npz(
        __file__.replace(".py", ".npz"),
        {
            "Ds": np.array([r["D"] for r in rows], dtype=float),
            "dps_star": np.array([-1 if r["dps_star"] is None else r["dps_star"]
                                  for r in rows], dtype=float),
            "lg_cond": np.array([np.nan if r["lg_cond"] is None else r["lg_cond"]
                                 for r in rows]),
            "rec_err": np.array([np.nan if r["rec_err"] is None else r["rec_err"]
                                 for r in rows]),
            "s_true": np.array([r.get("s_true", np.nan) for r in rows]),
            "s_jit": np.array([r.get("s_jit", np.nan) for r in rows]),
            "M": np.array([M]),
        },
        {
            "experiment": "e1ae_prony_horizon", "provenance": "e1ad case 3 / falsifier 4",
            "N": N_SIZE, "M": M, "detect_thresh": DETECT, "clean_thresh": CLEAN,
            "dps_ladder": ladder, "jit_seed": JIT_SEED, "quick": quick,
            "elapsed_s": round(elapsed, 1),
        },
    )
    pre.table()
    gates.summary(elapsed=elapsed)
    return gates.exit_code()


if __name__ == "__main__":
    raise SystemExit(main())
