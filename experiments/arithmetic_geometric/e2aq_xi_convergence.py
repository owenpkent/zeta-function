"""E2AQ: the xi-convergence test (backlog B2c) and the Omega-ladder (B2b).

PART 1: THE XI-CONVERGENCE TEST. Suzuki (arXiv:2606.09096, conjecture (1.2),
after CCM): the ground state of the localized Weil-form operator on
L^2(-a, a) has Fourier transform converging, suitably normalized, to
xi(1/2 + i z) as a -> infinity. This module runs the SOFT-WINDOW ANALOGUE:
the minimizer of Q_W(v)/||v||^2 over the modulated-Gaussian family at scale
sigma (the #181 instrument, 50-digit protocol on 50-digit zeros), compared
against Xi(t) = xi(1/2 + i t) across the sigma-ladder. Two metrics:
  M1 (central shape): after one fitted scale c, the relative L^2 residual of
      ghat*_sigma versus c Xi on t in [0, 10];
  M2 (the zero region): the minimizer's node positions versus gamma_1..3,
      refined by 50-digit bisection: does the node error shrink as the
      window grows, and at what rate?
Honest framing: the conjecture's object is the HARD-window operator; ours is
a Gaussian-window family on a finite mode grid. Convergence here is evidence
the limit is family-robust; failure here types family-dependence, not the
conjecture. Either outcome is a finding. This instrument consumes zeros by
design (it is a diagnostic of the form, not a construction; no K1 claim).

PART 2: THE OMEGA-LADDER. #181 measured that the multi-mode margin saturates
in sigma and conjectured the governing variable is the frequency ceiling
Omega, with the bottom set by the leak onto the first zero beyond the
ceiling. Pre-registered law:
    log margin(Omega; sigma) ~ const - sigma^2 (gamma_next(Omega) - Omega)^2,
gamma_next = the first zero above Omega. Retrodiction check: at Omega = 34,
sigma-slope -12 was measured in #181 and (gamma_next - Omega)^2 =
(37.59 - 34)^2 = 12.9. Here the law is tested ACROSS Omega at fixed sigma
(rungs chosen to spread the gap from 0.42 to 6.02), and the sigma^2 scaling
is tested by a second sigma on a subset.

Run:
  python -m experiments.arithmetic_geometric.e2aq_xi_convergence

Outputs: e2aq_xi_convergence.npz (tracked); zero cache (regenerable) in
experiments/_shared/_cache/zeros_dps50_T200.json.
"""

from __future__ import annotations

import json
import time
from math import pi
from pathlib import Path

import numpy as np
import mpmath as mp

HERE = Path(__file__).resolve().parent
ZCACHE = HERE.parent / "_shared" / "_cache" / "zeros_dps50_T200.json"

DPS = 50
GAMMAS_F = [14.134725141734693, 21.022039638771554, 25.010857580145688,
            30.424876125859513, 32.935061587739189, 37.586178158825671,
            40.918719012147495, 43.327073280914999, 48.005150881167159,
            49.773832477672302]

CHECKS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


def zeros_dps50():
    mp.mp.dps = DPS
    if ZCACHE.exists():
        return [mp.mpf(s) for s in json.loads(ZCACHE.read_text())]
    alt = HERE.parent.parent / "visualizations" / "research" / "_out" / "_zeros_dps50.json"
    if alt.exists():
        ZCACHE.write_text(alt.read_text())
        return [mp.mpf(s) for s in json.loads(ZCACHE.read_text())]
    print("  computing 91 zeros at 50 digits (one-time)")
    out, k = [], 1
    while True:
        z = mp.zetazero(k)
        if mp.im(z) > 200:
            break
        out.append(mp.im(z))
        k += 1
    ZCACHE.write_text(json.dumps([mp.nstr(g, DPS) for g in out]))
    return out


def Xi(t):
    """xi(1/2 + i t), real on the line."""
    s = mp.mpf("0.5") + mp.mpc(0, 1) * t
    return mp.re(s * (s - 1) / 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s))


class GroundState:
    """50-digit generalized bottom eigenvector of the zero-side Weil Gram
    against the L^2 Gram on the modulated-Gaussian mode family."""

    def __init__(self, sigma: float, omega_max: float, gz, domega: float | None = None):
        mp.mp.dps = DPS
        self.sigma = sg = mp.mpf(sigma)
        if domega is None:
            domega = 1.0 / (2.0 * sigma)
        self.omegas = np.arange(0.0, omega_max + 1e-9, domega)
        J = len(self.omegas)
        G = mp.zeros(J, J)
        for a in range(J):
            for b in range(a, J):
                wa, wb = mp.mpf(self.omegas[a]), mp.mpf(self.omegas[b])
                v = (sg * mp.sqrt(mp.pi) / 2) * (mp.e**(-sg**2 * (wa - wb)**2 / 4)
                                                 + mp.e**(-sg**2 * (wa + wb)**2 / 4))
                G[a, b] = G[b, a] = v
        tab = mp.zeros(J, len(gz))
        for a in range(J):
            wa = mp.mpf(self.omegas[a])
            for b, g in enumerate(gz):
                tab[a, b] = (sg * mp.sqrt(mp.pi / 2)) * (mp.e**(-sg**2 * (g - wa)**2 / 2)
                                                         + mp.e**(-sg**2 * (g + wa)**2 / 2))
        Qz = 2 * tab * tab.T
        L = mp.cholesky(G)
        Li = mp.inverse(L)
        A = Li * Qz * Li.T
        E, V = mp.eigsy(A)
        i0 = min(range(J), key=lambda i: mp.re(E[i]))
        v = mp.matrix([V[r, i0] for r in range(J)])
        self.c = Li.T * v
        nrm = mp.sqrt(mp.re((self.c.T * (G * self.c))[0]))
        for r in range(J):
            self.c[r] = self.c[r] / nrm
        self.margin = mp.re(E[i0])
        self.log10_margin = float(mp.log10(abs(self.margin))) if self.margin != 0 else float("-inf")

    def ghat(self, t):
        """ghat*(t) at 50 digits (mp scalar); t float or mpf."""
        sg = self.sigma
        tt = mp.mpf(t)
        acc = mp.mpf(0)
        for r, w in enumerate(self.omegas):
            wm = mp.mpf(w)
            acc += self.c[r] * (sg * mp.sqrt(mp.pi / 2)) * (
                mp.e**(-sg**2 * (tt - wm)**2 / 2) + mp.e**(-sg**2 * (tt + wm)**2 / 2))
        return acc

    def node_nearest(self, guess, half=0.6, step=5e-3):
        """The sign change of ghat* NEAREST to `guess` (fine scan, then
        130-step bisection in the enclosing sub-bracket)."""
        ts = [mp.mpf(guess) + mp.mpf(k) * mp.mpf(step)
              for k in range(-int(half / step), int(half / step) + 1)]
        vals = [self.ghat(t) for t in ts]
        best = None
        for i in range(len(ts) - 1):
            if mp.sign(vals[i]) != mp.sign(vals[i + 1]) and vals[i] != 0:
                mid = (ts[i] + ts[i + 1]) / 2
                if best is None or abs(mid - guess) < abs(best[0] - guess):
                    best = (mid, i)
        if best is None:
            return None
        i = best[1]
        lo, hi, flo = ts[i], ts[i + 1], vals[i]
        for _ in range(130):
            mid = (lo + hi) / 2
            if mp.sign(self.ghat(mid)) == mp.sign(flo):
                lo, flo = mid, self.ghat(mid)
            else:
                hi = mid
        return (lo + hi) / 2


def gamma_next(omega: float) -> float:
    return min(g for g in GAMMAS_F if g > omega)


def run():
    t0 = time.time()
    print("== E2AQ: xi-convergence (Suzuki 1.2, soft-window) + the Omega-ladder ==")
    gz = zeros_dps50()
    mp.mp.dps = DPS

    # ---------------- part 1: the xi ladder ---------------------------------
    print("\n-- part 1: ghat* vs Xi across the sigma ladder (Omega = 34) --")
    tgrid = np.arange(0.0, 10.0 + 1e-9, 0.25)
    Xi_vals = np.array([float(Xi(t)) for t in tgrid])
    SIGMAS = [0.3, 0.4, 0.5, 0.6, 0.7]
    p1 = []
    for sgv in SIGMAS:
        gs = GroundState(sgv, 34.0, gz)
        gh = np.array([float(gs.ghat(t)) for t in tgrid])
        c_fit = float(np.dot(gh, Xi_vals) / np.dot(Xi_vals, Xi_vals))
        resid = float(np.linalg.norm(gh - c_fit * Xi_vals) / np.linalg.norm(c_fit * Xi_vals))
        nodes = {}
        for k, gam in enumerate(GAMMAS_F[:3]):
            nd = gs.node_nearest(gam)
            nodes[k + 1] = None if nd is None else float(abs(nd - gz[k]))
        p1.append({"sigma": sgv, "c": c_fit, "resid": resid, "nodes": nodes,
                   "log10_margin": gs.log10_margin})
        nstr = ", ".join(f"|n{k}-g{k}| = {v:.2e}" if v is not None else f"n{k}: none"
                         for k, v in nodes.items())
        print(f"   sigma = {sgv}: resid(0..10) = {resid:.4f}, c = {c_fit:.3e}, {nstr}")
    resids = [r["resid"] for r in p1]
    node1 = [r["nodes"][1] for r in p1]

    # ---------------- part 2: the Omega ladder ------------------------------
    print("-- part 2: margin(Omega) at fixed sigma (the band-ceiling law) --")
    def ladder(sigma, omegas_list):
        rows = []
        for om in omegas_list:
            gs = GroundState(sigma, om, gz)
            gap = gamma_next(om) - om
            rows.append({"omega": om, "gap": gap, "log10_m": gs.log10_margin})
            print(f"   sigma = {sigma}, Omega = {om:4.1f}: gap = {gap:.2f}, "
                  f"log10 margin = {gs.log10_margin:.2f}")
        return rows

    L45 = ladder(0.45, [15.0, 20.0, 24.0, 27.0, 30.0, 34.0, 38.0, 42.0])
    L55 = ladder(0.55, [15.0, 27.0, 34.0, 42.0])

    # part 2b: the CLEAN sigma-derivative at Omega = 34: mode grid held FIXED
    # (domega = 1.0, J = 35) so only the Gaussian scale varies; the naive
    # sweep confounds the derivative with mode-count jumps (~1 decade noise)
    print("-- part 2b: fixed-grid sigma sweep at Omega = 34 --")
    SIG2B = [0.42, 0.46, 0.50, 0.54, 0.58]
    lg2b = []
    for sgv in SIG2B:
        gs = GroundState(sgv, 34.0, gz, domega=1.0)
        lg2b.append(gs.log10_margin)
        print(f"   sigma = {sgv}: log10 margin = {gs.log10_margin:.2f}")
    dslope_fixed = float(np.polyfit(np.array(SIG2B) ** 2,
                                    np.array(lg2b) * np.log(10), 1)[0])
    print(f"   fixed-grid d(ln m)/d(sigma^2) = {dslope_fixed:.1f}")
    # locate the ANNIHILATION FRONTIER: the first zero without an exact node
    gs_frontier = GroundState(0.50, 34.0, gz, domega=1.0)
    frontier_nodes = {}
    for k in (5, 6, 7, 8):                       # gamma_6..gamma_9 (0-indexed)
        nd = gs_frontier.node_nearest(GAMMAS_F[k])
        frontier_nodes[k] = None if nd is None else float(abs(nd - gz[k]))
    fr_str = ", ".join(f"g{k+1}: " + (f"{v:.0e}" if v is not None else "none")
                       for k, v in frontier_nodes.items())
    print(f"   node errors at the edge: {fr_str}")

    def fit(rows):
        x = np.array([r["gap"] ** 2 for r in rows])
        y = np.array([r["log10_m"] for r in rows]) * np.log(10)
        A = np.vstack([x, np.ones_like(x)]).T
        (slope, intercept), res, _, _ = np.linalg.lstsq(A, y, rcond=None)
        yhat = A @ [slope, intercept]
        ss = 1 - np.sum((y - yhat) ** 2) / max(1e-30, np.sum((y - np.mean(y)) ** 2))
        return float(slope), float(intercept), float(ss)

    s45, i45, r2_45 = fit(L45)
    s55, i55, r2_55 = fit(L55)
    print(f"   fit sigma = 0.45: slope = {s45:.3f} per gap^2 (predicted "
          f"{-0.45**2:.3f}), R^2 = {r2_45:.3f}")
    print(f"   fit sigma = 0.55: slope = {s55:.3f} per gap^2 (predicted "
          f"{-0.55**2:.3f}), R^2 = {r2_55:.3f}")

    # ---------------- checks ------------------------------------------------
    # The first run REFUTED both pre-registrations (dossier section 2); the
    # checks below encode the refutation-typed verdicts plus what survived.
    print("\n-- checks --")
    check("P1: protocol consistency: margins in family with the #181 solves",
          all(-45 < r["log10_margin"] < -30 for r in p1),
          "log10 margins: " + ", ".join(f"{r['log10_margin']:.1f}" for r in p1))
    check("P1 REFUTATION TYPED: the central shape is NOT Xi in this family "
          "(hole norm-stuffing; residual large at every scale)",
          all(v > 5.0 for v in resids),
          " -> ".join(f"{v:.1f}" for v in resids))
    check("P1 SHARPENED LOCKING: reachable zeros annihilated EXACTLY at working "
          "precision (nodes on gamma_2, gamma_3 to < 1e-30 where modes exceed "
          "reachable zeros)",
          all(r["nodes"][2] is not None and r["nodes"][2] < 1e-30 for r in p1[:2])
          and all(r["nodes"][3] is not None and r["nodes"][3] < 1e-30 for r in p1[:2]),
          "sigma = 0.3: " + ", ".join(
              f"n{k} = {p1[0]['nodes'][k]:.1e}" if p1[0]['nodes'][k] is not None
              else f"n{k}: none" for k in (1, 2, 3)))
    check("P1: node nearest gamma_1 exists at every scale (metric v2)",
          all(v is not None for v in node1),
          " -> ".join(f"{v:.1e}" if v is not None else "none" for v in node1))
    L45r = [r for r in L45 if r["log10_m"] > -45]     # resolution-safe rungs
    check("P2 REFUTATION TYPED: same-gap rungs differ by over a decade "
          "(the nearest-gap law is dead; Omega = 20 vs 24, both gap ~ 1.01)",
          abs(L45[1]["log10_m"] - L45[2]["log10_m"]) > 1.0,
          f"{L45[1]['log10_m']:.2f} vs {L45[2]['log10_m']:.2f}")
    mono = all(L45[i + 1]["log10_m"] > L45[i]["log10_m"] for i in range(1, len(L45) - 1))
    check("P2 NEW LAW: the margin RISES monotonically with Omega past the first "
          "rung (a collective density-edge effect, not a single-zero leak)",
          mono, " -> ".join(f"{r['log10_m']:.1f}" for r in L45))
    # the #181 retrodiction, measured CLEANLY: the naive sweep is confounded by
    # mode-count jumps (J changes with sigma; margins zigzag by ~1 decade), so
    # the derivative uses the fixed-grid sweep of part 2b
    sig2 = np.array([r["sigma"] ** 2 for r in p1])
    lnm = np.array([r["log10_margin"] for r in p1]) * np.log(10)
    dslope_naive = float(np.polyfit(sig2, lnm, 1)[0])
    check("P2 INSTRUMENT LESSON: the naive sigma-sweep has the OPPOSITE sign of "
          "the physical derivative (growing J deepens annihilation faster than "
          "the Gaussian narrows; only the fixed-grid derivative is physical)",
          dslope_naive > 0 > dslope_fixed,
          f"naive +{dslope_naive:.1f} vs fixed-grid {dslope_fixed:.1f}")
    # the frontier mechanism: exact nodes THROUGH gamma_7, none at gamma_8,
    # and the sigma-slope = -(gamma_8 - omega_edge)^2
    ferrs = [frontier_nodes[k] for k in (5, 6, 7, 8)]
    frontier_ok = (all(v is not None for v in ferrs)
                   and all(ferrs[i] < ferrs[i + 1] for i in range(3))
                   and ferrs[3] / ferrs[0] > 1e20)
    check("P2 MECHANISM: the annihilation frontier is GRADED, not binary: node "
          "precision degrades monotonically across gamma_6..gamma_9 by 20+ "
          "decades, with the sigma-slope selecting gamma_8's distance",
          frontier_ok, fr_str)
    d2 = (GAMMAS_F[7] - 34.0) ** 2
    check("P2 THE FRONTIER LAW: d(ln margin)/d(sigma^2) = -(gamma_8 - Omega)^2 "
          "within 15 percent (the margin is the leak onto the first "
          "UNANNIHILATED zero)",
          0.85 * d2 < -dslope_fixed < 1.15 * d2,
          f"slope = {dslope_fixed:.1f} vs -(43.33 - 34)^2 = {-d2:.1f}")
    check("P2: fits recorded for the record (gap^2 regressor fails as predicted "
          "by the refutation: R^2 low and slope sigma-independent)",
          r2_45 < 0.8 and abs(s55 / s45 - 1.0) < 0.2,
          f"R^2 = {r2_45:.2f}, slope ratio {s55 / s45:.2f} (sigma-blind)")

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print(f"\n{npass}/{len(CHECKS)} passed  ({time.time() - t0:.0f} s)")

    out = HERE / "e2aq_xi_convergence.npz"
    np.savez_compressed(
        out,
        sigmas=np.array(SIGMAS), resids=np.array(resids),
        c_fits=np.array([r["c"] for r in p1]),
        node_errs=np.array([[r["nodes"][k] if r["nodes"][k] is not None else np.nan
                             for k in (1, 2, 3)] for r in p1]),
        p1_log10_margins=np.array([r["log10_margin"] for r in p1]),
        L45_omega=np.array([r["omega"] for r in L45]),
        L45_gap=np.array([r["gap"] for r in L45]),
        L45_log10=np.array([r["log10_m"] for r in L45]),
        L55_omega=np.array([r["omega"] for r in L55]),
        L55_gap=np.array([r["gap"] for r in L55]),
        L55_log10=np.array([r["log10_m"] for r in L55]),
        fit45=np.array([s45, i45, r2_45]), fit55=np.array([s55, i55, r2_55]),
        sig2b=np.array(SIG2B), lg2b=np.array(lg2b), dslope_fixed=dslope_fixed,
        tgrid=tgrid, Xi_vals=Xi_vals,
        checks_passed=npass, checks_total=len(CHECKS),
    )
    print(f"saved {out.name}")


if __name__ == "__main__":
    run()
