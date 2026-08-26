"""E2BG: the coupled SP4 ladder (construction backlog B1; the BANK'S CLOSING BUILD
under the #201 frame closure; executes the audit's falsifier 2 as its P1).

THE QUESTION. #180 measured the explicit-formula two-sidedness residual FLAT at
2e-8..1e-7 over prime windows x0 = 2..6 at a FIXED spectral meter (the object's
emergent spectrum to T = 100 at ~1e-4 localization): C1 did not bind there.
This build grows BOTH meters together and prices every rung with an e2be-style
instrument budget: where does the residual come from, and does anything remain
when the instrument is paid?

THE INSTRUMENT (sharpened over #180's, so the budget is clean).
- Test function per rung: hcap = the C-infinity bump of support x0_r, with
  hcap(log n) evaluated in CLOSED FORM (no grid interpolation: the #180
  pipeline's dominant error clause is eliminated, per e2be's budget analysis).
- Prime side: pole = 2 int hcap cosh(x/2) (rect rule on a C-infinity
  compactly-supported integrand: aliasing-negligible), the exact Lambda-sum,
  archimedean = (1/pi) int_0^1500 h(t) [Re psi(1/4+it/2) - ln pi] dt on the
  FFT grid (analytic integrand, strip-aliasing negligible).
- Zero side: h(gamma) and h'(gamma) by DIRECT cosine transform at each zero
  (no grid interpolation), plus the Riemann-von Mangoldt density tail above
  the spectral ceiling T_r.
- Spectral meter: the object's emergent spectrum from the e2an line engine
  (integers only), POLISHED per zero by parabolic minimization of |m| via
  direct quadrature (multiplier_at), with the USABLE CEILING T*(X) MEASURED
  per data depth (the largest height at which the emergent spectrum matches
  the certified one in count and order-paired position; a validation-cell
  range decision, like e2bd's windows).
- Coupled rungs: (x0, X) = (4, 70000), (6, 300000), (7, 1000000), each
  evaluated at its measured ceiling T*(X): the ladder couples ALL THREE
  meters (test-function support, data depth, spectral ceiling), which is the
  #198 two-meter law made operational on the SP4 glue. Plus the 2x2 panel
  (x0 in {4,7}) x (X in {min,max}).

FOUR PILOT CATCHES (instrument findings recorded before the final run; two
quick pilots ran and each fired gates by design):
(1) P3 FIRED on a genuine instrument bug: the rect sum excluded the t = 0
    bin, costing ~h(0)kern(0)dt/2pi ~ 2e-3 relative with exactly the
    measured signature (x0-sensitive, T-insensitive): fixed by trapezoid
    including the endpoint. The e2be budget discipline caught a real bug in
    a sibling instrument before any claim was made on it.
(2) The count gate FIRED at fixed-T rungs (86 detected vs 79 certified at
    T = 200; 134 vs 202 at 400, X = 300000): the emergent spectrum's usable
    ceiling is DATA-PRICED, so rungs are now coupled to the measured T*(X).
(3) The second pilot's P3 residue (ratio 16.6 at x0 = 7) was the x-grid
    rect-rule error on the POLE integral (5.2e-11 measured by grid halving):
    the budget now carries a DX-Richardson clause.
(4) The detector emits DUPLICATE dips (doubled at gamma_77, quadrupled at
    gamma_78 in the X = 70000 pilot), which broke the order-pairing and
    capped T* at 195; polish output is now deduped (0.02 clusters), and the
    pairing dev showed zero DISPLACEMENT at height is data-drift, not polish
    error: the obj budget's delta is therefore predicted INTERNALLY by
    data-halving Richardson (X vs X/2 positions, K1-clean), not by the
    polish self-estimate.

THE BUDGET per rung (computed numerically, generously rounded up; the e2be
idiom). For resid_true: rounding (1e-15 x the sum of absolute terms), the
archimedean domain/aliasing lump (1e-12), the quadrature clause (Richardson
on BOTH axes: FFT padding and the x-grid DX), and the density-tail
fluctuation clause (|N(t) - RvM(t)| <= 0.28 ln t + 2, generous
Backlund-grade constant, applied as a Stieltjes bound). For resid_obj: the
same plus the DISPLACEMENT clause sum 2|h'(gamma_em)| (2 delta_int + 3
move_final + 1e-7) with delta_int the internal data-halving meter, and a
count-mismatch clause (zero when counts match).

PRE-REGISTERED (rule 1; P1 is the #201 audit's falsifier 2, verbatim stakes):
  P1  EXPECT: resid_obj tracks its budget at every coupled rung
      (resid_obj <= 10 x budget_obj): C1 does not bind inside the costed
      meters and the bank closes FULLY PRICED.
      KILL: resid_obj floors >= 10x above its budget while resid_true stays
      within its own: C1 BINDS: report the exchange rate, do NOT strike the
      item as priced, and reopen attention.
  P2  EXPECT: the displacement clause dominates budget_obj at every rung
      (the spectral meter is the binding instrument axis, the #180 floor's
      reading). KILL: another clause dominates at some rung.
  P3  SOUNDNESS: resid_true <= budget_true at every rung and every panel
      corner. KILL: the budget is wrong; fix before any claim.

DISCIPLINES. Joint (rule 3): C1 (SP2 wedge SP3, the counting side): the glue's
finite-scale two-sidedness, priced. K1 (rule 4): the construction cells
(lattice, line engine, emergent spectrum, prime side) consume integers only;
the certified zero list (dps-110 cache to T = 1500) enters ONLY the
resid_true validation cell and the polish CONTROL, behind the counter.
D-H / Beurling (rule 2): not posable for SP4 at this instrument, for the
reasons measured in #179 (D-H: the prime side is unbuildable, no Euler
product; Beurling: no Gamma term, the FE side absent); the refusals are the
#179 scorecard's, named here, not silently skipped.

Run:  python -m experiments.arithmetic_geometric.e2bg_coupled_sp4 [--quick]
Data: e2bg_coupled_sp4.npz (tracked next to this script).
"""

from __future__ import annotations

import json
import time
from math import ceil, exp, log, pi
from pathlib import Path

import numpy as np
from scipy.special import digamma

from experiments._shared.harness import Gates, PreRegistry, quick_arg, save_npz
from experiments.arithmetic_geometric.e2an_sp_object_v0 import (
    _ORACLE_CALLS, Probe, build_zeta_lattice, detect_zeros, lambda_sieve,
    line_integrand, multiplier, multiplier_at,
)

T_ARCH = 1500.0
DX = 2.5e-4
# coupled rungs: (x0, X). The spectral ceiling T* is MEASURED per data depth X
# (the quick pilot's count gate fired at fixed-T rungs: the emergent spectrum
# degrades past a data-priced ceiling, the #198 two-meter law surfacing in the
# glue; the ladder therefore couples all three meters (x0, X, T*(X)))
RUNG_SPECS = [(4.0, 70000), (6.0, 300000), (7.0, 1000000)]
RUNG_SPECS_QUICK = [(4.0, 70000), (7.0, 300000)]
CEIL_TOL = 0.05
ZCACHE = Path(__file__).resolve().parent.parent / "_shared" / "_cache" / "zeros_dps110_T1500.json"


def hcap_exact(x, x0):
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    inside = np.abs(x) < x0
    z = x[inside] / x0
    out[inside] = np.exp(-1.0 / (1.0 - z * z))
    return out


class TestFn:
    """The bump of support x0: closed-form hcap, direct-transform h and h'."""

    def __init__(self, x0: float, dx: float = DX):
        self.x0 = x0
        self.dx = dx
        self.x = np.arange(-x0, x0 + dx / 2, dx)
        self.w = hcap_exact(self.x, x0)

    def h(self, t):
        t = np.atleast_1d(np.asarray(t, dtype=float))
        return (np.cos(np.outer(t, self.x)) @ self.w) * self.dx

    def hprime(self, t):
        t = np.atleast_1d(np.asarray(t, dtype=float))
        return -(np.sin(np.outer(t, self.x)) @ (self.x * self.w)) * self.dx

    def pole(self):
        return 2.0 * float(np.sum(self.w * np.cosh(0.5 * self.x)) * self.dx)

    def primes(self, lam):
        n = np.arange(2, len(lam))
        sel = lam[2:] > 0
        ln = np.log(n[sel])
        return -2.0 * float(np.sum(lam[2:][sel] / np.sqrt(n[sel])
                                   * hcap_exact(ln, self.x0)))


def polish(taus0, lat, probe, integrand):
    """Parabolic |m|-minimization per zero via direct quadrature; returns
    (refined positions, per-zero localization estimate)."""
    g = np.asarray(taus0, dtype=float)
    step = 1e-3
    last_move = np.full_like(g, step)
    for _ in range(4):
        pts = np.concatenate([g - step, g, g + step])
        m = np.abs(multiplier_at(lat, probe, pts, integrand=integrand))
        k = len(g)
        ym, y0, yp = (np.log(np.maximum(m[:k], 1e-300)),
                      np.log(np.maximum(m[k:2 * k], 1e-300)),
                      np.log(np.maximum(m[2 * k:], 1e-300)))
        den = ym - 2 * y0 + yp
        d = np.where(np.abs(den) > 1e-12, 0.5 * (ym - yp) / np.where(den == 0, 1, den), 0.0)
        d = np.clip(d, -0.9, 0.9) * step
        g = g + d
        last_move = np.abs(d) + step * 0.05
        step *= 0.2
    # dedupe: detector dips that polish converged onto one zero (clusters
    # within 0.02; the X=70k pilot showed doubled and quadrupled dips at
    # gamma_77 and gamma_78 breaking the order-pairing)
    order = np.argsort(g)
    g_s, mv_s = g[order], last_move[order]
    keep_g, keep_m = [], []
    i = 0
    while i < len(g_s):
        j = i
        while j + 1 < len(g_s) and g_s[j + 1] - g_s[j] < 0.02:
            j += 1
        keep_g.append(float(np.median(g_s[i:j + 1])))
        keep_m.append(float(np.max(mv_s[i:j + 1])))
        i = j + 1
    return np.array(keep_g), np.array(keep_m)


def usable_ceiling(em, tz, tol=CEIL_TOL):
    """Largest height at which the emergent spectrum matches the certified one
    in count AND order-paired position (validation control: sets the
    instrument's usable range; the EF evaluation itself stays lattice-sourced)."""
    em = np.sort(np.asarray(em))
    tz = np.sort(np.asarray(tz))
    n = min(len(em), len(tz))
    k_bad = n
    for k in range(n):
        if abs(em[k] - tz[k]) > tol:
            k_bad = k
            break
    if k_bad == 0:
        return 0.0, 0.0
    dev = float(np.max(np.abs(em[:k_bad] - tz[:k_bad])))
    last = float(min(em[k_bad - 1], tz[k_bad - 1]))
    nxt = []
    if k_bad < len(em):
        nxt.append(float(em[k_bad]))
    if k_bad < len(tz):
        nxt.append(float(tz[k_bad]))
    first_bad = min(nxt) if nxt else last + 1.0
    return 0.5 * (last + first_bad), dev


def s_fluct_bound(fn: TestFn, t_grid, h_grid, hp_grid, T_r):
    """|int_{T_r}^{1500} h d(N - RvM)| via Stieltjes parts with the generous
    zero-count bound Q(t) = 0.28 ln t + 2."""
    sel = (t_grid >= T_r) & (t_grid <= T_ARCH)
    t, h, hp = t_grid[sel], np.abs(h_grid[sel]), np.abs(hp_grid[sel])
    if len(t) < 2:
        return 0.0
    Q = 0.28 * np.log(np.maximum(t, 2.0)) + 2.0
    dt = t[1] - t[0]
    inner = float(np.sum((0.28 / t) * h + Q * hp) * dt)
    return Q[-1] * h[-1] + Q[0] * h[0] + inner


def pair_disp(em, em_half, window: float = 0.5, fallback: float = 0.1):
    """Per-zero internal displacement meter: |position(X) - position(X/2)|
    by nearest-match pairing (K1-clean data-halving Richardson); unmatched
    entries get the conservative fallback."""
    em_half = np.sort(np.asarray(em_half))
    out = np.full(len(em), fallback)
    for i, g in enumerate(em):
        j = np.searchsorted(em_half, g)
        best = fallback
        for jj in (j - 1, j):
            if 0 <= jj < len(em_half):
                best = min(best, abs(g - em_half[jj]))
        if best < window:
            out[i] = best
    return out


def arch_integral(t_fft, h_fft):
    ksel = t_fft <= T_ARCH
    kern = np.real(digamma(0.25 + 0.5j * t_fft[ksel])) - log(pi)
    return float(np.trapezoid(h_fft[ksel] * kern, t_fft[ksel])) / pi


def rung(fn: TestFn, T_r, lam, em_polished, moves, disp, true_z, t_fft, h_fft,
         hp_fft, arch_coarse, dx_clause_abs):
    pole = fn.pole()
    primes = fn.primes(lam)
    # trapezoid INCLUDING the t = 0 endpoint: the quick pilot's P3 fired on
    # exactly this (a rect sum excluding the t = 0 bin costs ~h(0)kern(0)dt/2pi
    # ~ 2e-3 relative, x0-sensitive and T-insensitive, the measured signature).
    # The remaining trapezoid error (the t = 0 Euler-Maclaurin dt^4 term) is
    # budgeted by Richardson: 2 x the fine-vs-coarse-padding difference.
    arch = arch_integral(t_fft, h_fft)
    quad_clause_abs = 2.0 * abs(arch - arch_coarse) + dx_clause_abs
    prime_total = pole + primes + arch
    scale = max(abs(pole), abs(primes), abs(arch), 0.5)

    rho_sel = (t_fft >= T_r) & (t_fft <= T_ARCH)
    rho = np.log(np.maximum(t_fft[rho_sel], 2.0) / (2 * pi)) / (2 * pi)
    tail = 2.0 * float(np.trapezoid(h_fft[rho_sel] * rho, t_fft[rho_sel]))

    def zside(gs):
        gs = gs[gs <= T_r]
        return 2.0 * float(np.sum(fn.h(gs))) + tail, gs

    z_true, gt = zside(true_z)
    z_obj, go = zside(em_polished)
    osel = em_polished <= T_r
    mv, dp = moves[osel], disp[osel]
    resid_true = abs(z_true - prime_total) / scale
    resid_obj = abs(z_obj - prime_total) / scale

    rounding = 1e-15 * (abs(pole) + abs(primes) + abs(arch)
                        + 2 * float(np.sum(np.abs(fn.h(gt)))) + abs(tail)) / scale
    lump = 1e-12 / scale
    quad = quad_clause_abs / scale
    fluct = s_fluct_bound(fn, t_fft, h_fft, hp_fft, T_r) / scale
    budget_true = rounding + lump + quad + fluct
    # the DISPLACEMENT clause: per-zero delta predicted INTERNALLY (K1-clean)
    # by data-halving Richardson (2x the X-vs-X/2 position shift) plus the
    # polish convergence self-estimate (3x the final parabola move)
    loc = 2.0 * float(np.sum(np.abs(fn.hprime(go))
                             * (2.0 * dp + 3.0 * mv + 1e-7))) / scale
    n_mismatch = abs(len(gt) - len(go))
    mismatch = n_mismatch * 2.0 * float(np.max(np.abs(fn.h(gt)))) / scale if n_mismatch else 0.0
    budget_obj = budget_true + loc + mismatch
    return {"x0": fn.x0, "T": T_r, "scale": scale,
            "resid_true": resid_true, "resid_obj": resid_obj,
            "budget_true": budget_true, "budget_obj": budget_obj,
            "loc_clause": loc, "fluct_clause": fluct, "round_clause": rounding,
            "quad_clause": quad,
            "n_true": len(gt), "n_obj": len(go), "mismatch_clause": mismatch}


def main() -> int:
    t_start = time.perf_counter()
    quick = quick_arg()
    gates = Gates(quick=quick)
    pre = PreRegistry()
    pre.register("P1", "resid_obj <= 10x budget_obj at every coupled rung (falsifier 2)",
                 "resid_obj floors >= 10x budget while resid_true is in budget: C1 BINDS")
    pre.register("P2", "the localization clause dominates budget_obj at every rung",
                 "another clause dominates at some rung")
    pre.register("P3", "resid_true <= budget_true everywhere (soundness)",
                 "budget wrong; fix before claims")

    specs = RUNG_SPECS_QUICK if quick else RUNG_SPECS
    print(f"e2bg: coupled SP4 ladder (backlog B1)  "
          f"[{'quick' if quick else 'full'}; dx={DX}, "
          f"rungs (x0, X)={[(x, X) for x, X in specs]}]")

    print("-- validation input: the certified zero list (one counted load) --")
    _ORACLE_CALLS["n"] += 1
    true_z = np.array([float(x) for x in json.loads(ZCACHE.read_text())])
    true_z = true_z[true_z <= 405.0]

    probe = Probe(c=1.9, sigma=0.04)
    engines = {}
    build_calls_total = 0

    def engine(X):
        nonlocal build_calls_total
        if X in engines:
            return engines[X]
        pre = _ORACLE_CALLS["n"]
        lat = build_zeta_lattice(X)
        s, integrand = line_integrand(lat, probe)
        tau_f, m_f = multiplier(lat, probe, tau_max=405.0, integrand=integrand)
        em0 = np.array([g for g, _ in detect_zeros(tau_f, np.abs(m_f),
                                                   tau_lo=5.0, tau_hi=401.0)])
        build_calls_total += _ORACLE_CALLS["n"] - pre
        em_pol, moves = polish(em0, lat, probe, integrand)
        Tstar, dev = usable_ceiling(em_pol, true_z)
        print(f"   X={X}: {len(em0)} dips to 400, {len(em_pol)} after dedupe; "
              f"usable ceiling T* = {Tstar:.1f} (pair dev {dev:.1e})")
        engines[X] = (lat, integrand, em_pol, moves, Tstar)
        return engines[X]

    def fn_transforms(x0):
        fn = TestFn(x0)
        grids = {}
        for npad in (1 << 21, 1 << 22):
            spec = np.fft.rfft(fn.w, n=npad) * DX
            t = 2 * pi * np.fft.rfftfreq(npad, d=DX)
            ph = np.exp(1j * t * fn.x[0])
            grids[npad] = (t, np.real(np.conj(spec) * ph), ph)
        t_fft, h_fft, ph = grids[1 << 22]
        hp_fft = -np.imag(np.conj(np.fft.rfft(fn.x * fn.w, n=1 << 22) * DX) * ph)
        arch_coarse = arch_integral(grids[1 << 21][0], grids[1 << 21][1])
        # DX-Richardson: the x-grid rect-rule error on the pole and arch
        # integrals (the second quick pilot's P3 excess: 5.2e-11 on the
        # x0 = 7 pole), measured by grid halving
        fnh = TestFn(x0, DX / 2)
        spec_h = np.fft.rfft(fnh.w, n=1 << 23) * fnh.dx
        t_h = 2 * pi * np.fft.rfftfreq(1 << 23, d=fnh.dx)
        h_h = np.real(np.conj(spec_h) * np.exp(1j * t_h * fnh.x[0]))
        dx_clause = 2.0 * (abs(fn.pole() - fnh.pole())
                           + abs(arch_integral(t_fft, h_fft)
                                 - arch_integral(t_h, h_h))) + 1e-14
        return fn, t_fft, h_fft, hp_fft, arch_coarse, dx_clause

    print("-- build phase (integers only) + ceiling measurement --")
    lam = lambda_sieve(int(ceil(exp(max(x for x, _ in specs)))) + 2)
    rows = []
    for x0, X in specs:
        lat, integrand, em_pol, moves, Tstar = engine(X)
        em_h = engine(X // 2)[2]
        disp = pair_disp(em_pol, em_h)
        T_r = min(Tstar, 400.0)
        fn, t_fft, h_fft, hp_fft, arch_c, dxc = fn_transforms(x0)
        r = rung(fn, T_r, lam, em_pol, moves, disp, true_z, t_fft, h_fft,
                 hp_fft, arch_c, dxc)
        r["X"], r["Tstar"] = X, Tstar
        rows.append(r)
        print(f"   x0={x0:.0f}, X={X}, T={T_r:.1f}: resid_true {r['resid_true']:.1e} "
              f"(budget {r['budget_true']:.1e}), resid_obj {r['resid_obj']:.1e} "
              f"(budget {r['budget_obj']:.1e}; loc {r['loc_clause']:.1e}), "
              f"zeros {r['n_obj']}/{r['n_true']}")

    panel = []
    Xs = sorted({X for _, X in specs})
    for x0 in (4.0, 7.0):
        for X in (Xs[0], Xs[-1]):
            lat, integrand, em_pol, moves, Tstar = engine(X)
            em_h = engine(X // 2)[2]
            disp = pair_disp(em_pol, em_h)
            fn, t_fft, h_fft, hp_fft, arch_c, dxc = fn_transforms(x0)
            r = rung(fn, min(Tstar, 400.0), lam, em_pol, moves, disp, true_z,
                     t_fft, h_fft, hp_fft, arch_c, dxc)
            r["X"], r["Tstar"] = X, Tstar
            panel.append(r)
    print("-- mismatch panel (x0 in {4,7}) x (X in {min,max}), each at its own T* --")
    for r in panel:
        print(f"   x0={r['x0']:.0f}, X={r['X']}: obj {r['resid_obj']:.2e} "
              f"(budget {r['budget_obj']:.2e})")
    build_calls = build_calls_total

    # -- gates --------------------------------------------------------------
    gates.gate("K1: zero oracle calls through the build phase",
               build_calls == 0, f"build-phase calls = {build_calls}")
    tstars = {X: engines[X][4] for X in Xs}
    gates.gate("the data-to-spectrum exchange rate T*(X) is MEASURED",
               all(tstars[Xs[i]] <= tstars[Xs[i + 1]] for i in range(len(Xs) - 1)),
               "T*: " + ", ".join(f"X={X}: {tstars[X]:.0f}" for X in Xs))
    gates.gate("emergent spectrum matches the certified count at every usable rung",
               all(r["n_obj"] == r["n_true"] for r in rows),
               "counts " + ", ".join(f"{r['n_obj']}/{r['n_true']}" for r in rows))
    p3 = all(r["resid_true"] <= r["budget_true"] for r in rows + panel)
    gates.gate("P3 soundness: resid_true <= budget_true at every rung and corner",
               p3, "worst ratio " + f"{max(r['resid_true'] / r['budget_true'] for r in rows + panel):.2f}")
    pre.resolve("P3", "FIRED" if p3 else "REFUTED",
                f"worst true/budget = {max(r['resid_true'] / r['budget_true'] for r in rows + panel):.2f}")

    ratios = [r["resid_obj"] / r["budget_obj"] for r in rows]
    p1 = all(rr <= 10.0 for rr in ratios)
    gates.gate("P1 (falsifier 2): resid_obj <= 10x its budget at every coupled rung",
               p1, "obj/budget ratios " + ", ".join(f"{rr:.2f}" for rr in ratios))
    pre.resolve("P1", "FIRED" if p1 else "REFUTED",
                "ratios " + ", ".join(f"{rr:.2f}" for rr in ratios)
                + ("; C1 does NOT bind inside the costed meters: the bank closes FULLY PRICED"
                   if p1 else "; C1 BINDS: exchange rate reported, attention reopened"))

    dom = [r["loc_clause"] >= max(r["fluct_clause"], r["round_clause"],
                                  r["quad_clause"], r["mismatch_clause"])
           for r in rows]
    p2 = all(dom)
    gates.gate("P2: the localization clause dominates budget_obj at every rung",
               p2, "loc vs (fluct, quad, round): " + "; ".join(
                   f"{r['loc_clause']:.1e} vs ({r['fluct_clause']:.1e}, "
                   f"{r['quad_clause']:.1e}, {r['round_clause']:.1e})" for r in rows))
    pre.resolve("P2", "FIRED" if p2 else "REFUTED",
                "dominant clause per rung: " + ", ".join(
                    "loc" if d else "other" for d in dom))

    growth = [rows[i + 1]["resid_obj"] / max(rows[i]["resid_obj"], 1e-300)
              for i in range(len(rows) - 1)]
    gates.gate("the exchange rate is RECORDED: obj residual across the coupled ladder",
               True, "resid_obj " + " -> ".join(f"{r['resid_obj']:.1e}" for r in rows)
               + "; step ratios " + ", ".join(f"{g:.2f}" for g in growth))
    dX_ax = abs(panel[1]["resid_obj"] - panel[0]["resid_obj"])
    dx0_ax = abs(panel[2]["resid_obj"] - panel[0]["resid_obj"])
    gates.gate("panel: axis sensitivities recorded (data axis vs test-function axis)",
               True, f"|d resid_obj| along X axis {dX_ax:.1e}, along x0 axis {dx0_ax:.1e}")
    gates.gate("oracle calls confined to validation (the one counted zero-list load)",
               _ORACLE_CALLS["n"] == 1, f"total = {_ORACLE_CALLS['n']}")
    gates.gate("no unresolved pre-registrations", pre.unresolved() == [])

    elapsed = time.perf_counter() - t_start
    save_npz(
        __file__.replace(".py", ".npz"),
        {
            "rung_x0": np.array([r["x0"] for r in rows]),
            "rung_X": np.array([r["X"] for r in rows]),
            "rung_Tstar": np.array([r["Tstar"] for r in rows]),
            "rung_T": np.array([r["T"] for r in rows]),
            "resid_true": np.array([r["resid_true"] for r in rows]),
            "resid_obj": np.array([r["resid_obj"] for r in rows]),
            "budget_true": np.array([r["budget_true"] for r in rows]),
            "budget_obj": np.array([r["budget_obj"] for r in rows]),
            "loc_clause": np.array([r["loc_clause"] for r in rows]),
            "fluct_clause": np.array([r["fluct_clause"] for r in rows]),
            "panel_x0": np.array([r["x0"] for r in panel]),
            "panel_X": np.array([r["X"] for r in panel]),
            "panel_obj": np.array([r["resid_obj"] for r in panel]),
            "panel_budget": np.array([r["budget_obj"] for r in panel]),
            "tstar_X": np.array(Xs, dtype=float),
            "tstar": np.array([tstars[X] for X in Xs]),
        },
        {
            "experiment": "e2bg_coupled_sp4", "backlog": "B1",
            "dx": DX, "rungs": [(x, X) for x, X in specs],
            "ceil_tol": CEIL_TOL, "quick": quick,
            "oracle_calls": _ORACLE_CALLS["n"], "elapsed_s": round(elapsed, 1),
        },
    )
    pre.table()
    gates.summary(elapsed=elapsed)
    return gates.exit_code()


if __name__ == "__main__":
    raise SystemExit(main())
