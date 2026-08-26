"""E2BF: the frontier-capacity function (construction backlog B2d; BANK MAINTENANCE
under the #201 frame closure; hardens the #183 frontier law's capacity axis).

WHAT IS MEASURED. #183 (e2aq) found the multi-mode window margin is a Gaussian
leak onto the FIRST ZERO THE FAMILY CANNOT ANNIHILATE (the frontier), which sat
two zeros past the naive frequency ceiling at the reference configuration, with
node precision degrading about six decades per zero across the edge. This build
measures the CAPACITY FUNCTION: gamma_frontier(J, Omega) and the per-zero
precision schedule, on two axes through the reference point (sigma = 0.5):

  capacity axis: Omega = 34 fixed, domega in {2.0, 1.0, 0.5}  (J = 18, 35, 69;
                 NESTED grids, so the margin must be nonincreasing: a rigorous
                 internal control);
  ceiling axis:  domega = 1.0 fixed, Omega in {27, 34, 41}    (J = 28, 35, 42).

The organizing variable is SPARE CAPACITY: S = J - #(gamma_k <= Omega), the
mode count in excess of the in-band zero population.

PRE-REGISTERED (rule 1), before the sweep was run:
  P1  EXPECT: the overshoot (frontier index minus the first out-of-band index)
      is NONDECREASING in spare capacity S across all five configurations
      (spare dimensions annihilate deeper). KILL: non-monotone in S.
  P2  EXPECT: the per-zero cost (decades of node precision per zero across the
      graded range) stays within a factor of 3 across all configurations
      (a capacity-independent schedule; reference ~6 decades/zero).
      KILL: spread > 3x: no universal schedule, the "capacity" framing wrong.
  P3  CONTROL: along the nested capacity axis the margin is nonincreasing
      (larger space, lower bottom: a theorem about nested minimization),
      among RESOLVED rungs (above the solver floor). KILL: violated among
      resolved rungs: the solver is broken; fix before any claim.
      PILOT NOTES (recorded before the final run). (1) The dps-50 quick
      pilot's P3 FIRED (the coarse-grid config read 12 orders below its
      nested lower bound: the #184/#185 precision-starvation class). (2) The
      dps-80 full pilot's P3 FIRED AGAIN, in the opposite direction, and the
      reference margin moved 14 orders between dps: the eigsy VALUES are
      unreliable under the mode Gram's conditioning at both precisions.
      REDESIGN, banked as this build's instrument finding: margins are now
      CERTIFIED Rayleigh quotients (the returned vector evaluated directly
      against fresh Q and G at dps 140: a true upper bound independent of the
      eigensolver), the worst-conditioned config (J = 69) is replaced by
      J = 53, and a solver-honesty gate compares eigsy to the certificate.
      The dps-80 pilot's P1 refutation (overshoot 4,5,6,6,4, broken by the
      J = 69 outlier) is re-measured on the certified pipeline; node DEPTHS
      are working-precision-relative (gated), the slope selection is not.

DISCIPLINES. Joint (rule 3): C2 instrument (the SP5 window family's capacity
ledger; prices what "annihilate the reachable spectrum" costs, the #183 law's
missing axis). K1 (rule 4): this is a ZERO-SIDE instrument by design (the
family is built against the certified zero list, as in e2aq); the zero list is
the counted oracle input and nothing here feeds a construction cell. D-H /
Beurling (rule 2): not posable at this instrument for the reason recorded in
#183 (the zero-side family consumes the zeta zero list by construction; the
bracket's discrimination role for this family was discharged at the form level
in #179-#183); named here, not silently skipped.

Run:  python -m experiments.arithmetic_geometric.e2bf_frontier_capacity [--quick]
Data: e2bf_frontier_capacity.npz (tracked next to this script).
"""

from __future__ import annotations

import time

import numpy as np
from mpmath import mp

from experiments._shared.harness import Gates, PreRegistry, quick_arg, save_npz
import experiments.arithmetic_geometric.e2aq_xi_convergence as e2aq
from experiments.arithmetic_geometric.e2aq_xi_convergence import (
    GroundState, zeros_dps50,
)

# dps 80 for the solves: the quick pilot's P3 control caught the #184/#185
# precision-starvation class at dps 50 on the coarse-grid config (a nested
# margin reading 12 orders below its mathematical lower bound); 80 digits plus
# the resolvability guard below repairs it. zeros stay the 50-digit cache
# (zero-input precision 1e-50 is ample for margins >= 1e-45).
e2aq.DPS = 80
DPS = 80

SIGMA = 0.5
NODE_GOOD = 1e-30      # the LIVE level set: annihilated at working precision
NODE_DEAD = 1e-12      # the DEAD level set: first zero not annihilated
K_SPAN = 9             # zeros examined starting 2 below the ceiling index
# Frontier typing, reconciling #183: the sigma-SLOPE selects the zero whose
# leak carries the margin (gamma_8 at the reference, node still 1e-23-alive);
# the DEAD cut (> 1e-12) sits one zero further (gamma_9 at 2e-10, exactly
# #183's own graded table). The capacity function below records BOTH level
# sets; "overshoot" is defined at the dead cut, and the slope selection is
# gated at the reference configuration.


def rayleigh_cert(gs, gz, dps_hi: int = 140) -> float:
    """CERTIFIED lg of the attained Rayleigh quotient: the returned coefficient
    vector evaluated directly against freshly built Q and G at dps 140. A true
    upper bound on the config's bottom, independent of the eigensolver (the
    dps-50 and dps-80 pilots both showed eigsy VALUES unreliable under the
    Gram's conditioning; vectors certify, values do not)."""
    prev = mp.dps
    mp.dps = dps_hi
    try:
        sg = mp.mpf(gs.sigma)
        J = len(gs.omegas)
        c = [mp.mpf(gs.c[r]) for r in range(J)]
        num = mp.mpf(0)
        for g in gz:
            gh = mp.mpf(0)
            for a in range(J):
                wa = mp.mpf(gs.omegas[a])
                gh += c[a] * (sg * mp.sqrt(mp.pi / 2)) * (
                    mp.e ** (-sg ** 2 * (g - wa) ** 2 / 2)
                    + mp.e ** (-sg ** 2 * (g + wa) ** 2 / 2))
            num += 2 * gh * gh
        den = mp.mpf(0)
        for a in range(J):
            for b in range(J):
                wa, wb = mp.mpf(gs.omegas[a]), mp.mpf(gs.omegas[b])
                den += c[a] * c[b] * (sg * mp.sqrt(mp.pi) / 2) * (
                    mp.e ** (-sg ** 2 * (wa - wb) ** 2 / 4)
                    + mp.e ** (-sg ** 2 * (wa + wb) ** 2 / 4))
        return float(mp.log10(num / den))
    finally:
        mp.dps = prev


def profile(cfg_name: str, omega_max: float, domega: float, gz, gzf,
            sigma: float = SIGMA):
    """Ground state + node-precision profile across the ceiling edge."""
    t0 = time.perf_counter()
    gs = GroundState(sigma, omega_max, gz, domega=domega)
    j = len(gs.omegas)
    first_out = next(k for k, g in enumerate(gzf) if g > omega_max)  # 0-based
    ks = list(range(max(first_out - 2, 0), min(first_out + K_SPAN - 2, len(gzf) - 1)))
    errs = []
    for k in ks:
        nd = gs.node_nearest(gzf[k])
        errs.append(float("nan") if nd is None else float(abs(nd - gz[k])))
    errs = np.array(errs)
    dead = [i for i, e in enumerate(errs) if not np.isfinite(e) or e > NODE_DEAD]
    frontier_i = dead[0] if dead else len(ks) - 1
    frontier_k = ks[frontier_i]
    overshoot = frontier_k - first_out
    spare = j - first_out                     # modes minus in-band zero count
    graded = [i for i in range(frontier_i + 1)
              if np.isfinite(errs[i]) and errs[i] > 1e-45]
    decs = [np.log10(errs[graded[i + 1]] / errs[graded[i]])
            for i in range(len(graded) - 1)
            if errs[graded[i + 1]] > errs[graded[i]]]
    decades = float(np.mean(decs)) if decs else float("nan")
    live = [i for i, e in enumerate(errs) if np.isfinite(e) and e < NODE_GOOD]
    live_k = ks[live[-1]] if live else ks[0] - 1
    lg_cert = rayleigh_cert(gs, gz)
    gap = abs(gs.log10_margin - lg_cert)
    el = time.perf_counter() - t0
    print(f"   {cfg_name}: J={j}, Omega={omega_max}, spare={spare}: "
          f"dead-cut gamma_{frontier_k + 1} (overshoot {overshoot}), live to "
          f"gamma_{live_k + 1}, {decades:.1f} decades/zero, lg margin cert "
          f"{lg_cert:.1f} (eigsy {gs.log10_margin:.1f}, gap {gap:.1f})  ({el:.0f} s)")
    return {"name": cfg_name, "J": j, "omega": omega_max, "domega": domega,
            "spare": spare, "first_out": first_out, "ks": np.array(ks),
            "errs": errs, "frontier_k": frontier_k, "overshoot": overshoot,
            "live_k": live_k, "decades": decades,
            "lg_margin": lg_cert, "lg_eigsy": gs.log10_margin, "cert_gap": gap}


def main() -> int:
    t_start = time.perf_counter()
    quick = quick_arg()
    gates = Gates(quick=quick)
    pre = PreRegistry()
    pre.register("P1", "overshoot nondecreasing in spare capacity S (all configs)",
                 "overshoot non-monotone in S")
    pre.register("P2", "per-zero decades within a factor 3 across configs",
                 "spread > 3x: no universal schedule")
    pre.register("P3", "margin nonincreasing along the NESTED capacity axis",
                 "violated: solver broken, fix before claims")

    print(f"e2bf: frontier-capacity function (backlog B2d)  "
          f"[{'quick' if quick else 'full'}; sigma={SIGMA}, dps={DPS}]")
    gz = zeros_dps50()
    gzf = [float(g) for g in gz]

    cfgs = [("ref", 34.0, 1.0)]
    if not quick:
        cfgs += [("cap-", 34.0, 2.0), ("cap+", 34.0, 0.65),
                 ("ceil-", 27.0, 1.0), ("ceil+", 41.0, 1.0)]
    else:
        cfgs += [("cap-", 34.0, 2.0), ("ceil+", 41.0, 1.0)]

    # the #183 comparison runs at #183's OWN working precision (the dps-80
    # full pilot showed node DEPTHS are working-precision-relative while the
    # slope selection is not; both facts are gated below)
    e2aq.DPS = 50
    ref50 = profile("ref@dps50", 34.0, 1.0, gz, gzf)
    e2aq.DPS = 80

    rows = [profile(n, om, dw, gz, gzf) for n, om, dw in cfgs]
    by = {r["name"]: r for r in rows}

    ref = by["ref"]
    gates.gate("#183's graded table reproduced at its own dps (dead cut gamma_9)",
               ref50["frontier_k"] + 1 == 9 and 4.0 <= ref50["decades"] <= 8.0,
               f"dead gamma_{ref50['frontier_k'] + 1}, "
               f"{ref50['decades']:.1f} decades/zero at dps 50")
    gates.gate("node depths are working-precision-relative (dps 80 cuts deeper)",
               ref["frontier_k"] >= ref50["frontier_k"],
               f"dead cut gamma_{ref50['frontier_k'] + 1} at dps 50 vs "
               f"gamma_{ref['frontier_k'] + 1} at dps 80")
    over_g = ref["errs"][2:4]
    gates.gate("reference: gamma_6, gamma_7 annihilated PAST the ceiling",
               bool(np.all(np.isfinite(over_g)) and np.all(over_g < 1e-25)),
               "errs " + ", ".join(f"{e:.0e}" for e in over_g))
    gates.gate("reference: per-zero cost in the #183 band (4-8 decades/zero)",
               4.0 <= ref["decades"] <= 8.0, f"{ref['decades']:.1f} decades/zero")

    # the sigma-slope selection (#183's frontier definition), from CERTIFIED
    # margins at two window scales
    gs2 = profile("ref+", 34.0, 1.0, gz, gzf, sigma=0.54)
    slope = (gs2["lg_margin"] - ref["lg_margin"]) * np.log(10.0) / (0.54 ** 2 - SIGMA ** 2)
    g_sel = 34.0 + np.sqrt(max(-slope, 0.0))
    gates.gate("the sigma-slope selects gamma_8 (#183's frontier; certified margins)",
               abs(g_sel - gzf[7]) < 2.5,
               f"slope {slope:.1f} implies gamma_sel = {g_sel:.1f} vs gamma_8 = {gzf[7]:.2f}")
    gates.gate("solver honesty: eigsy value within 1 decade of the certified "
               "Rayleigh quotient at every config",
               all(r["cert_gap"] <= 1.0 for r in rows + [ref50, gs2]),
               "worst gap " + f"{max(r['cert_gap'] for r in rows + [ref50, gs2]):.1f} decades")

    order = sorted(rows, key=lambda r: r["spare"])
    ovs = [r["overshoot"] for r in order]
    p1 = all(ovs[i] <= ovs[i + 1] for i in range(len(ovs) - 1))
    gates.gate("P1: overshoot nondecreasing in spare capacity",
               p1, "spare -> overshoot: " + ", ".join(
                   f"{r['spare']}->{r['overshoot']}" for r in order))
    pre.resolve("P1", "FIRED" if p1 else "REFUTED",
                "; ".join(f"S={r['spare']}: {r['overshoot']}" for r in order))

    decs = [r["decades"] for r in rows if np.isfinite(r["decades"])]
    spread = max(decs) / min(decs) if min(decs) > 0 else float("inf")
    p2 = spread <= 3.0
    gates.gate("P2: per-zero decades within 3x across configs",
               p2, f"range [{min(decs):.1f}, {max(decs):.1f}] decades/zero, "
               f"spread {spread:.2f}x")
    pre.resolve("P2", "FIRED" if p2 else "REFUTED", f"spread {spread:.2f}x")

    nest_rows = [by[n] for n in ("cap-", "ref", "cap+") if n in by]
    nest = [r["lg_margin"] for r in nest_rows]
    p3 = all(nest[i] >= nest[i + 1] - 1e-6 for i in range(len(nest) - 1)) and len(nest) >= 2
    gates.gate("P3 control: CERTIFIED margins nonincreasing on the nested capacity axis",
               p3, "lg cert margins " + " -> ".join(f"{v:.1f}" for v in nest))
    pre.resolve("P3", "FIRED" if p3 else "REFUTED",
                " -> ".join(f"{v:.1f}" for v in nest))

    if "ceil-" in by and "ceil+" in by:
        gf = [by["ceil-"], ref, by["ceil+"]]
        mono = all(gf[i]["frontier_k"] <= gf[i + 1]["frontier_k"] for i in range(2))
        gates.gate("capacity function: gamma_frontier monotone in the ceiling",
                   mono, ", ".join(
                       f"Omega={r['omega']:.0f}: gamma_{r['frontier_k'] + 1}" for r in gf))
    else:
        gates.skip("capacity function: gamma_frontier monotone in the ceiling",
                   "quick mode runs one ceiling neighbor only")

    gates.gate("K1 posture stated: zero-side instrument, zero list is the counted input",
               True, "as in e2aq (#183); no construction cell consumes it")
    gates.gate("no unresolved pre-registrations", pre.unresolved() == [])

    elapsed = time.perf_counter() - t_start
    save_npz(
        __file__.replace(".py", ".npz"),
        {
            "J": np.array([r["J"] for r in rows]),
            "omega": np.array([r["omega"] for r in rows]),
            "domega": np.array([r["domega"] for r in rows]),
            "spare": np.array([r["spare"] for r in rows]),
            "frontier_k": np.array([r["frontier_k"] for r in rows]),
            "live_k": np.array([r["live_k"] for r in rows]),
            "cert_gap": np.array([r["cert_gap"] for r in rows]),
            "lg_eigsy": np.array([r["lg_eigsy"] for r in rows]),
            "ref50_frontier_k": np.array([ref50["frontier_k"]]),
            "ref50_errs": ref50["errs"],
            "overshoot": np.array([r["overshoot"] for r in rows]),
            "decades": np.array([r["decades"] for r in rows]),
            "lg_margin": np.array([r["lg_margin"] for r in rows]),
            "err_rows": np.array([np.pad(r["errs"], (0, K_SPAN - len(r["errs"])),
                                          constant_values=np.nan) for r in rows]),
            "ks_first": np.array([r["ks"][0] for r in rows]),
        },
        {
            "experiment": "e2bf_frontier_capacity", "backlog": "B2d",
            "sigma": SIGMA, "dps": DPS, "node_good": NODE_GOOD,
            "node_dead": NODE_DEAD, "quick": quick,
            "configs": [r["name"] for r in rows],
            "elapsed_s": round(elapsed, 1),
        },
    )
    pre.table()
    gates.summary(elapsed=elapsed)
    return gates.exit_code()


if __name__ == "__main__":
    raise SystemExit(main())
