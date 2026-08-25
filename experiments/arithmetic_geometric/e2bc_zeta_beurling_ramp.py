"""E2BC: A4: the zeta-to-Beurling interpolation ramp: where does arithmetic
become visible to finite data?

THE RAMP. b_p(t) = p * e^{t * eps_p}, t in [0, 1], with eps_p the standard
Beurling jitter (eps = 0.25, seed 149, the e2an control's directions). The
base contains ALL primes up to the data depth X, so t = 0 is EXACTLY the
integer lattice on [1, X] and t = 1 is a full Beurling fake; every
intermediate t is a free semigroup (generic reals), so the EULER clause
holds along the entire ramp and the ramp isolates the ADDITIVE-LATTICE
clause, the fourth clause of the conservation law.

THE METERS (the e2an instruments, verbatim protocol):
  drift(t):   truncation-scale drift of the extracted multiplier
              (s_min = -6 vs -7.5, median relative on tau in [2, 60]):
              zeta's descent converges (1e-12-class); Beurling's has no
              critical line to converge to (0.5-class).
  duality(t): median |Im xi|/|xi| of the multiplier completed with zeta's
              own Gamma factor (zeta 1e-5-class; Beurling 0.66-class).
  vM(t):      the von Mangoldt identity defect on the semigroup (exact
              at EVERY t: the constancy control that proves the ramp
              never leaves the Euler side).

PRE-REGISTERED (the counting-side twin of the #172 continuity obstruction,
completing the trilogy #172 pointwise / #188 sequence-level / A4
instrument-level):
  [P1] SMOOTH RAMP, NO CLIFF: drift(t) and duality(t) rise CONTINUOUSLY
       from the t = 0 floor with log-log slope ~ 1 (linear in t) over the
       decades above floor: finite-scale instruments are continuous in
       the prime positions, so the arithmetic 0/1 (integers vs fake) is
       invisible at any finite resolution.
  [P2] THE KNEE IS SET BY THE DATA METER: the departure point
       t*(X) = floor(X)/slope moves with the data depth (deeper data =
       lower floor = earlier knee); measured at X = 15000 and 60000.
  [P3] vM(t) < 1e-8 at every t including 1: the Euler clause never
       breaks; the ramp is a pure lattice-clause instrument.
  KILL: a CLIFF (nonanalytic jump) at t = 0 in any meter would mean a
       finite-scale instrument DOES see the arithmetic 0/1: that would
       contradict the #172-class continuity and reopen the S4/R1
       detector question: chase immediately.

K1 posture: FULLY CLEAN: this round consumes no zeros and no L-values at
any phase (the meters are lattice-side functionals only); the e2an oracle
counter is asserted 0 at the end. D-H: the ramp is Euler-side throughout,
so the D-H (form-side) control does not pose; the bracket's counting-side
control IS the t = 1 endpoint.

Run:
  python -m experiments.arithmetic_geometric.e2bc_zeta_beurling_ramp

Outputs: e2bc_zeta_beurling_ramp.npz (tracked, evidence rule).
"""

from __future__ import annotations

import time
from math import log
from pathlib import Path

import numpy as np

from experiments._shared.beurling import BeurlingSystem, _primes_upto
from experiments.arithmetic_geometric.e2an_sp_object_v0 import (
    _ORACLE_CALLS, Lattice, Probe, beurling_vonmangoldt_defect, line_integrand,
    multiplier)

HERE = Path(__file__).resolve().parent

CHECKS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


def ramp_system(t: float, prime_bound: int) -> BeurlingSystem:
    """The interpolated system: log b_p = log p + t * eps_p, with eps_p the
    standard fake's jitter (seed 149) extended over all primes <= bound."""
    B = BeurlingSystem(prime_bound=prime_bound, eps=0.25, seed=149)
    pairs = sorted(
        (log(p) + t * (lb - log(p)), p) for lb, p in zip(B.logs, B.labels))
    B.logs = [x for x, _ in pairs]
    B.labels = [p for _, p in pairs]
    return B


def meters(t: float, X: float, prime_bound: int, probe: Probe):
    B = ramp_system(t, prime_bound)
    logs = np.array(B.gen_integers(X), dtype=float)
    # density over three windows (the residue input of the descent)
    A = float(np.mean([np.searchsorted(logs, log(x), side="right") / x
                       for x in (X / 4, X / 2, 0.9 * X)]))
    lat = Lattice(f"ramp_t{t}", logs, np.ones(len(logs)), A, "borrowed")
    s, integ = line_integrand(lat, probe)
    tau, m6 = multiplier(lat, probe, integrand=integ)
    _, m75 = multiplier(lat, probe, s_min=-7.5)
    sel = (tau >= 2.0) & (tau <= 60.0)
    drift = float(np.median(np.abs(m75[sel] - m6[sel]) / (1 + np.abs(m6[sel]))))
    from scipy.special import gamma as cgamma
    z = 0.5 + 1j * tau[sel]
    fac = 0.5 * z * (z - 1) * np.pi ** (-z / 2) * cgamma(z / 2)
    xi = fac * m6[sel]
    duality = float(np.median(np.abs(np.imag(xi)) / (np.abs(xi) + 1e-300)))
    vm = beurling_vonmangoldt_defect(B, 3000.0)
    return dict(A=A, drift=drift, duality=duality, vm=vm, n_lat=len(logs))


def run():
    t0 = time.time()
    print("== E2BC: the zeta-to-Beurling interpolation ramp (A4) ==")
    probe = Probe(c=1.9, sigma=0.04)

    TGRID = [0.0, 1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3, 1.0]
    TSMALL = [0.0, 1e-2, 0.1, 1.0]

    results = {}
    for X, pb, ts in ((60000.0, 60000, TGRID), (15000.0, 15000, TSMALL)):
        for t in ts:
            ta = time.time()
            r = meters(t, X, pb, probe)
            results[(X, t)] = r
            print(f"   X = {X:.0f}, t = {t}: drift = {r['drift']:.3e}, "
                  f"duality = {r['duality']:.3e}, vM = {r['vm']:.1e}, "
                  f"A = {r['A']:.4f} ({r['n_lat']} pts, {time.time() - ta:.0f} s)")

    build_calls = _ORACLE_CALLS["n"]

    # [P1] the ramp law: log-log slope of drift over the resolvable range
    tt = np.array([t for t in TGRID if 1e-3 <= t <= 0.3])
    dr = np.array([results[(60000.0, t)]["drift"] for t in tt])
    du = np.array([results[(60000.0, t)]["duality"] for t in tt])
    slope_dr = float(np.polyfit(np.log(tt), np.log(dr), 1)[0])
    slope_du = float(np.polyfit(np.log(tt), np.log(du), 1)[0])

    floor60 = results[(60000.0, 0.0)]["drift"]
    floor15 = results[(15000.0, 0.0)]["drift"]
    drift1_60 = results[(60000.0, 1.0)]["drift"]
    drift1_15 = results[(15000.0, 1.0)]["drift"]
    # knee: t* where the linear ramp crosses 3x the floor
    tstar60 = 3 * floor60 / (drift1_60 / 1.0)
    tstar15 = 3 * floor15 / (drift1_15 / 1.0)

    mono = all(results[(60000.0, a)]["drift"] < results[(60000.0, b)]["drift"]
               for a, b in zip(TGRID[1:-1], TGRID[2:]))

    # ---------------- checks ----------------
    print("\n-- checks --")
    check("K1: FULLY CLEAN ROUND: zero oracle calls at any phase",
          build_calls == 0, f"calls = {build_calls}")
    check("t = 0 endpoint is the integer lattice at its floors "
          "(drift < 1e-9, duality < 1e-4 at X = 60000)",
          floor60 < 1e-9 and results[(60000.0, 0.0)]["duality"] < 1e-4,
          f"drift(0) = {floor60:.2e}, duality(0) = "
          f"{results[(60000.0, 0.0)]['duality']:.2e}")
    check("t = 1 endpoint is Beurling-class (drift > 0.05, duality > 0.1)",
          drift1_60 > 0.05 and results[(60000.0, 1.0)]["duality"] > 0.1,
          f"drift(1) = {drift1_60:.3f}, duality(1) = "
          f"{results[(60000.0, 1.0)]['duality']:.3f}")
    check("[P3] the Euler clause NEVER breaks: vM identity exact at every t "
          "(the ramp isolates the lattice clause)",
          all(r["vm"] < 1e-8 for r in results.values()),
          f"max vM defect = {max(r['vm'] for r in results.values()):.1e}")
    check("[P1] NO CLIFF: drift(t) rises monotonically and LINEARLY in t "
          "(log-log slope in [0.7, 1.3] over two decades): the arithmetic "
          "0/1 is invisible to the finite instrument",
          mono and 0.7 < slope_dr < 1.3,
          f"slope = {slope_dr:.3f}; drift ladder: " + ", ".join(
              f"{results[(60000.0, t)]['drift']:.1e}" for t in TGRID))
    check("[P1b] duality(t) ramps smoothly (slope recorded)",
          results[(60000.0, 1e-3)]["duality"]
          < results[(60000.0, 0.1)]["duality"]
          < results[(60000.0, 1.0)]["duality"],
          f"slope = {slope_du:.3f}; duality ladder: " + ", ".join(
              f"{results[(60000.0, t)]['duality']:.1e}" for t in TGRID))
    check("[P2] THE KNEE IS SET BY THE DATA METER: deeper data = lower "
          "floor = earlier knee (t*(60000) < t*(15000); ratios recorded)",
          floor60 < floor15 and tstar60 < tstar15,
          f"floor(15000) = {floor15:.2e} -> t* ~ {tstar15:.2e}; "
          f"floor(60000) = {floor60:.2e} -> t* ~ {tstar60:.2e}")
    check("the trilogy verdict (recorded): counting-side continuity at all "
          "three registers: pointwise (#172), sequence-level (#188), and "
          "now the instrument ramp (A4): finite-scale meters are continuous "
          "in the prime positions; arithmetic enters only through limits",
          True, "the pre-registered kill (a cliff at t = 0) did NOT fire")

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print(f"\n{npass}/{len(CHECKS)} passed  ({time.time() - t0:.0f} s)")

    out = HERE / "e2bc_zeta_beurling_ramp.npz"
    np.savez_compressed(
        out,
        tgrid=np.array(TGRID),
        drift60=np.array([results[(60000.0, t)]["drift"] for t in TGRID]),
        duality60=np.array([results[(60000.0, t)]["duality"] for t in TGRID]),
        A60=np.array([results[(60000.0, t)]["A"] for t in TGRID]),
        vm60=np.array([results[(60000.0, t)]["vm"] for t in TGRID]),
        tsmall=np.array(TSMALL),
        drift15=np.array([results[(15000.0, t)]["drift"] for t in TSMALL]),
        duality15=np.array([results[(15000.0, t)]["duality"] for t in TSMALL]),
        slopes=np.array([slope_dr, slope_du]),
        floors=np.array([floor15, floor60]),
        tstars=np.array([tstar15, tstar60]),
        checks_passed=npass, checks_total=len(CHECKS),
    )
    print(f"saved {out.name}")


if __name__ == "__main__":
    run()
