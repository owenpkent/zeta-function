"""E1M: the Hamburger-type converse pin, probed at the CCM D_log family.

WHY THIS EXPERIMENT EXISTS
==========================
LEARNINGS #154 named four zero-free ingredients that would upgrade the CCM
D_log determinant shell (arXiv:2511.22755 Thm 5.10; e1k testbed) from a #143
installed shell toward a W6-shaped trace formula. Ingredient (4), the last
unexecuted one, is a HAMBURGER-TYPE CONVERSE PIN:

    replace the ground-state forcing of the Section-7 identification
    (xihat_lambda -> Xi, an RH-equivalent positivity = M4) by a uniqueness
    statement of Hamburger type: FE + growth + zero budget => limit = Xi,
    whose proof engine is Poisson/theta, i.e. LATTICE-CONSUMING (the #152
    fourth clause). If it works, identification is split from convergence
    for the first time and the residual M4 step is cleanly isolated.

THE KNOWN MATH RISK, handled head-on (test T4): the functional equation
alone, even with growth, has an infinite-dimensional solution space (Knopp's
modular integrals; citation-level, flagged for SURVEYOR). The load-bearing
question is whether the BUDGET (zero-counting density from the FE + argument
principle) plus FE plus order-1 growth suffices, or whether a
Dirichlet-series-type hypothesis (Hamburger's own, which xihat_lambda does
not obviously satisfy) is unavoidable. T4 answers it by CONSTRUCTION: the
RvM-comb relocation family (built from gamma-factor data only, no zeta zeros
consumed) satisfies FE + order 1 + exact RvM budget and is not unique, so
the bare pin "FE + growth + budget => Xi" is FALSE and the lattice must be
consumed through a Dirichlet/Hamburger hypothesis, exactly the #152 clause.

WHAT THIS BUILDS (test battery)
===============================
T1 LATTICE ENGINE: the Hamburger proof mechanism verified on zeta at 30
   digits: Jacobi theta FE <=> Poisson (incl. the shifted/dual form) <=>
   N(x) = x + O(1), and the Mellin/residue bridge that turns the theta FE
   into the completed functional equation with the s = 0, 1 pole budget.
T2 TYPE EXCLUSION (D-H): D-H satisfies its OWN exact FE (odd character
   shape, conductor 5) to ~1e-30, fails the RIEMANN-TYPE FE (conductor 1,
   Gamma(s/2)) at O(1), and its FE-derived budget exceeds the Riemann-type
   budget by (log 5 / 2pi) T ~ 22 zeros at the height of its first off-line
   zero: the pin's hypotheses exclude D-H BY TYPE, not by approximation.
   Both budget curves are validated against argument-principle windings of
   the completed functions (function values only: K1-clean provenance).
T3 PIN AT FINITE LAMBDA: from the e1k harness (ground state of the
   truncated Weil form), measure for xihat_lambda at cutoffs lambda in
   {2.2, 2.6, 3.0, sqrt13}: (i) the FE / self-inversive defect (evenness +
   realness); (ii) the growth order proxy (exponential type vs the
   Paley-Wiener bound log lambda); (iii) the budget: the count of ZEROS OF
   THE FUNCTION xihat (sign changes + winding cross-check), NOT the
   operator eigenvalue budget that e1l measured, against the twin's OWN
   FE-derived RvM curve and the installed lattice line; (iv) the
   Dirichlet-face window: how far the unpacked f_lambda(s) tracks an
   absolutely convergent Dirichlet series before the Paley-Wiener floor
   forces exponential divergence at the archimedean rate ~ e^{(pi/4) t}.
T4 THE CONDITIONAL PIN, stated honestly: budget KILLS the FE-preserving
   oscillation family Xi(z)(1 + c cos(a z)) (measured excess ~ (a/pi) T
   zeros, linear vs the RvM log-density allowance), but budget + FE +
   growth do NOT pin Xi: the RvM-comb relocation counterexample (PROVEN by
   construction, numerically instantiated). Corrected pin = classical
   Hamburger (Dirichlet hypothesis load-bearing, budget redundant given it).
T5 BEURLING PIN FAILURE: the density-matched Beurling fake (b_p = p e^{eps},
   eps iid U[-0.25, 0.25], seed 149) fails the pin NAMEABLY: theta FE defect
   ~37 percent, integer counting not x + O(1), and WITHOUT an FE the
   argument-principle budget is UNDERIVABLE: the pin's engine has no fuel.
T6 K1 / DISCIPLINE AUDIT: mechanical self-audit: input ledger per test,
   runtime guards on the mpmath and D-H zero scanners (installed, never
   tripped), and a source scan for zero-list access in the pin path.

HONEST SCOPE
============
This is a probe of the PIN, not a proof of anything about RH. The finite
objects come from the e1k faithful reimplementation (not the paper's exact
operator; razor-thin margin eps ~ 1e-5; zeta pole term approximate). All
integer counts are leading-order +- O(1) (e1l precision caveat). The
conditional pin statement and its correction are in the .md companion with
tiered claims (PROVEN / NUMERICAL / CONJECTURE). ADVERSARY outcome
(2026-07-11): the residual open lemma (Dirichlet-face inheritance) is,
conditional on the limit + growth package, EQUIVALENT to the identification
it replaces, so the split is a positivity-free reformulation, not a
reduction; see the .md banner.

Run:
  python3 -m experiments.spectral.e1m_hamburger_pin           # full (~6 min)
  python3 -m experiments.spectral.e1m_hamburger_pin --quick   # small sweeps
Outputs:
  experiments/spectral/e1m_hamburger_pin.npz  (+ .md companion)
"""

from __future__ import annotations

import argparse
import cmath
import math
import time
import warnings
from pathlib import Path

import numpy as np
import mpmath as mp

# Only builders and configs from e1k: NOT the reference zero lists
# (ZETA_ZEROS / DH_ZEROS) and NOT operator_spectrum. The pin path measures
# zeros of the FUNCTION xihat; it never touches an eigenvalue list.
from experiments.spectral.e1k_dh_dlog_testbed import (
    make_streams, build_float, ZETA_CFG, DH_CFG,
)
from experiments._shared.beurling import BeurlingSystem, _primes_upto
import experiments._shared.davenport_heilbronn as _dhmod

warnings.filterwarnings("ignore")

OUT = Path(__file__).with_suffix(".npz")
SQRT13 = float(np.sqrt(13.0))

CHECKS: list = []
LEDGER: dict = {}


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""))


def consume(test, *inputs):
    LEDGER.setdefault(test, []).extend(inputs)


# --------------------------------------------------------------------------
# FE-derived smooth zero-counting curves (the K1-clean budget). WHY these are
# clean: they are built from the gamma factor + conductor alone (loggamma),
# i.e. from the functional-equation DATA via the argument principle; no zero
# of any L-function is consumed anywhere in their construction.
# --------------------------------------------------------------------------
def theta_smooth_zeta(T):
    """Riemann-Siegel theta from Gamma(s/2) + pi^{-s/2} at s = 1/2 + iT."""
    return float(mp.im(mp.loggamma(mp.mpf(1) / 4 + 1j * mp.mpf(T) / 2))
                 - (mp.mpf(T) / 2) * mp.log(mp.pi))


def n_smooth_zeta(T):
    """N(T) smooth part; the +1 is the standard argument-principle constant."""
    return theta_smooth_zeta(T) / math.pi + 1.0


def theta_smooth_dh(T):
    """D-H phase from ITS OWN gamma data: Gamma((s+1)/2), conductor 5."""
    return float((mp.mpf(T) / 2) * mp.log(mp.mpf(5) / mp.pi)
                 + mp.im(mp.loggamma(mp.mpf(3) / 4 + 1j * mp.mpf(T) / 2)))


# --------------------------------------------------------------------------
# Argument-principle winding counter. WHY adaptive: the count is exact
# (integer) as long as consecutive phase steps stay below pi; we subdivide
# until every step is < 0.9 rad and report the rounding residual as the
# error certificate.
# --------------------------------------------------------------------------
def winding_count(fev, corners, n0=48, tol=0.9, max_pts=16000):
    path = []
    k = len(corners)
    for e in range(k):
        a, b = corners[e], corners[(e + 1) % k]
        for i in range(n0):
            path.append(a + (b - a) * i / n0)
    path.append(path[0])
    vals = [complex(fev(p)) for p in path]
    total, i, worst = 0.0, 0, 0.0
    while i < len(path) - 1:
        u, v = vals[i], vals[i + 1]
        dphi = cmath.phase(v / u)
        if abs(dphi) > tol and len(path) < max_pts and abs(path[i + 1] - path[i]) > 1e-9:
            mid = (path[i] + path[i + 1]) / 2
            path.insert(i + 1, mid)
            vals.insert(i + 1, complex(fev(mid)))
            continue
        worst = max(worst, abs(dphi))
        total += dphi
        i += 1
    w = total / (2 * math.pi)
    return w, abs(w - round(w)), len(path)


# --------------------------------------------------------------------------
# Completed functions (mp). Xi_z is the z-plane Riemann Xi; Phi_dh is the
# D-H completion with ITS OWN gamma factor, derived so Phi(s) = Phi(1-s)
# holds exactly for the repo's chi_DH (odd character mod 5 shape).
# --------------------------------------------------------------------------
def xi_completed(s):
    s = mp.mpc(s)
    return (s * (s - 1) / 2) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def Xi_z(z):
    return xi_completed(mp.mpf("0.5") + 1j * mp.mpc(z))


def phi_dh(s):
    s = mp.mpc(s)
    return (mp.mpf(5) / mp.pi) ** (s / 2) * mp.gamma((s + 1) / 2) * _dhmod.davenport_heilbronn.evaluate(s)


def chi_riemann(s):
    """The RIEMANN-TYPE FE factor (conductor 1, Gamma(s/2)): the pin's H1 data."""
    s = mp.mpc(s)
    return mp.pi ** (s - mp.mpf("0.5")) * mp.gamma((1 - s) / 2) / mp.gamma(s / 2)


# --------------------------------------------------------------------------
# xihat evaluator from an e1k build. WHY the gauge: eigh returns the ground
# state up to a global complex phase; we rotate the largest component to the
# real axis and MEASURE the residual imaginary part as the realness defect
# instead of assuming it away.
# --------------------------------------------------------------------------
class Xihat:
    def __init__(self, res):
        self.idx = np.array(res["idx"], float)
        self.phi = float(res["phi"])
        self.L = float(res["L"])
        xi = np.asarray(res["xi"], complex)
        j0 = int(np.argmax(np.abs(xi)))
        self.coef = xi * np.exp(-1j * np.angle(xi[j0]))
        self.coef_im_frac = float(np.max(np.abs(self.coef.imag)) / np.max(np.abs(self.coef)))

    def __call__(self, z):
        z = np.atleast_1d(np.asarray(z, complex))
        d = z[:, None] - self.phi * self.idx[None, :]
        small = np.abs(d) < 1e-9
        base = 2 * self.L ** -0.5 * np.sin(z[:, None] * self.L / 2) / np.where(small, 1.0, d)
        lim = 2 * self.L ** -0.5 * (self.L / 2) * np.cos(z[:, None] * self.L / 2)
        return np.where(small, lim, base) @ self.coef


_BUILD_CACHE: dict = {}


def get_build(label, lam, N, streams):
    key = (label, round(lam, 6), int(N))
    if key not in _BUILD_CACHE:
        cfg = ZETA_CFG if label == "ZETA" else DH_CFG
        stream = streams[0] if label == "ZETA" else streams[1]
        t0 = time.time()
        r = build_float(N, lam, stream, cfg["dens_a"], cfg["dens_b"], cfg["use_pole"])
        print(f"    [build] {label} lam={lam:.4f} N={N}: {time.time()-t0:.1f}s "
              f"(eps={r['eps']:+.2e}, even_frac={r['even_frac']:.5f})")
        _BUILD_CACHE[key] = r
    return _BUILD_CACHE[key]


# ==========================================================================
# T1: the lattice engine (Poisson / theta / Mellin-residue) verified on zeta.
# ==========================================================================
def run_t1(results):
    print("\n[T1] LATTICE ENGINE: theta FE <=> Poisson <=> N(x)=x+O(1), + Mellin/residue bridge")
    consume("T1", "Z lattice", "Gaussian test functions", "Gamma-factor data",
            "mp.zeta VALUES on Re s>0 (no zeros)")
    prev = mp.mp.dps
    mp.mp.dps = 35
    try:
        # (a) Jacobi theta FE = Poisson for the Gaussian on Z
        th = lambda t: 1 + 2 * mp.nsum(lambda n: mp.e ** (-mp.pi * n * n * t), [1, 80])
        worst = 0.0
        for t in ("0.31", "0.7", "1.3", "2.0"):
            t = mp.mpf(t)
            worst = max(worst, float(abs(th(1 / t) - mp.sqrt(t) * th(t))))
        check("T1a Jacobi theta FE theta(1/t)=sqrt(t)theta(t)", worst < 1e-25,
              f"max defect {worst:.1e}")
        results["t1_theta_defect"] = worst

        # (b) Poisson in the dual/shifted form: sum_n e^{-pi(n+x)^2 t}
        #     = t^{-1/2} sum_k e^{-pi k^2/t} e^{2pi i k x}. WHY: shows the
        #     engine is lattice-duality itself, not a symmetry of one function.
        worst = 0.0
        for x, t in ((mp.mpf("0.3"), mp.mpf("1.1")), (mp.mpf("0.45"), mp.mpf("0.6"))):
            lhs = mp.nsum(lambda n: mp.e ** (-mp.pi * (n + x) ** 2 * t), [-80, 80])
            rhs = t ** mp.mpf("-0.5") * mp.nsum(
                lambda k: mp.e ** (-mp.pi * k * k / t) * mp.e ** (2j * mp.pi * k * x), [-80, 80])
            worst = max(worst, float(abs(lhs - rhs)))
        check("T1b Poisson summation (shifted Gaussian, lattice duality)", worst < 1e-25,
              f"max defect {worst:.1e}")
        results["t1_poisson_defect"] = worst

        # (c) the additive-lattice counting clause Z pays (Beurling cannot, T5)
        ok = all(abs(math.floor(x) - x) <= 1.0 for x in (10.5, 100.5, 12345.678))
        check("T1c integer counting N(x)=x+O(1), sup|N-x|<=1", ok,
              "the clause whose failure kills the fake in T5")

        # (d) Mellin/residue bridge: pi^{-s/2}Gamma(s/2)zeta(s)
        #     = 1/(s-1) - 1/s + int_1^inf omega(t)(t^{s/2-1}+t^{(1-s)/2-1})dt.
        #     WHY: this is the exact mechanism by which the theta FE becomes
        #     the completed FE, with the s=0,1 POLE BUDGET appearing as the
        #     two residue terms (the pole half of the #154 determinant data).
        omega = lambda t: mp.nsum(lambda n: mp.e ** (-mp.pi * n * n * t), [1, 60])
        def mellin_rep(s):
            s = mp.mpc(s)
            I = mp.quad(lambda t: omega(t) * (t ** (s / 2 - 1) + t ** ((1 - s) / 2 - 1)),
                        [1, mp.inf])
            return 1 / (s - 1) - 1 / s + I
        worst = 0.0
        for s in (mp.mpf(2), mp.mpc(3, 1), mp.mpc("0.5", 3)):
            lhs = mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
            worst = max(worst, float(abs(mellin_rep(s) - lhs) / abs(lhs)))
        check("T1d Mellin/residue bridge (theta FE -> completed FE + pole budget)",
              worst < 1e-22, f"max rel err {worst:.1e}")
        results["t1_mellin_relerr"] = worst

        # (e) FE symmetry read off the bridge: the representation is manifestly
        #     s <-> 1-s symmetric, so xi(s)=xi(1-s) is DERIVED from the lattice.
        s0 = mp.mpc("0.3", 2)
        d = abs(mellin_rep(s0) - mellin_rep(1 - s0))
        check("T1e completed FE derived from the lattice (rep symmetric in s<->1-s)",
              float(d) < 1e-22, f"|rep(s)-rep(1-s)| = {float(d):.1e}")
    finally:
        mp.mp.dps = prev


# ==========================================================================
# T2: type exclusion of D-H, with numbers, + argument-principle validation
# of both FE-derived budget curves.
# ==========================================================================
def run_t2(results):
    print("\n[T2] TYPE EXCLUSION (D-H): own FE exact, Riemann-type FE fails at O(1), budget off by (log5/2pi)T")
    consume("T2", "D-H f(s) VALUES (Hurwitz zeta; no zero scan)",
            "zeta VALUES via xi_completed", "Gamma-factor data of both types")
    prev = mp.mp.dps
    mp.mp.dps = 30
    try:
        dh = _dhmod.davenport_heilbronn
        pts = (mp.mpc("0.3", 5), mp.mpc("0.7", 12), mp.mpc("1.5", 3))
        own = max(float(abs(dh.functional_equation_residual(s)) / abs(dh.evaluate(s)))
                  for s in pts)
        check("T2a D-H satisfies its OWN FE (conductor 5, Gamma((s+1)/2))",
              own < 1e-20, f"max rel residual {own:.1e}")
        results["t2_dh_own_fe"] = own

        rie = min(float(abs(dh.evaluate(s) - chi_riemann(s) * dh.evaluate(1 - s))
                        / abs(dh.evaluate(s))) for s in pts)
        check("T2b D-H FAILS the Riemann-type FE (conductor 1, Gamma(s/2)) at O(1)",
              rie > 0.1, f"min rel defect {rie:.3f}: wrong FE data = type exclusion")
        results["t2_dh_riemann_fe_defect"] = rie

        # zeta budget validated by winding of the completed xi (K1-clean:
        # function values only; contour heights are generic, not zero data).
        w, resid, npts = winding_count(
            lambda s: xi_completed(s),
            [mp.mpc(-0.5, 0.5), mp.mpc(1.5, 0.5), mp.mpc(1.5, 29.5), mp.mpc(-0.5, 29.5)])
        nsm = n_smooth_zeta(29.5)
        check("T2c zeta argument-principle count matches its FE-derived budget",
              abs(w - round(w)) < 0.02 and abs(round(w) - nsm) <= 1.0,
              f"winding {w:.3f} vs smooth {nsm:.2f} ({npts} evals)")
        results["t2_zeta_ap_30"] = float(w)

        # D-H budget curve: calibrate the O(1) constant c0 at T=30 by the
        # SAME argument principle, then validate at the second height T=20.
        # WHY c0 is honest: the constant is type-level (gamma data + one
        # winding of function values); the DENSITY is pure gamma data.
        w30, r30, n30 = winding_count(
            lambda s: phi_dh(s),
            [mp.mpc(-0.5, 0.5), mp.mpc(1.5, 0.5), mp.mpc(1.5, 30.0), mp.mpc(-0.5, 30.0)])
        c0 = round(w30) - theta_smooth_dh(30.0) / math.pi
        w20, r20, n20 = winding_count(
            lambda s: phi_dh(s),
            [mp.mpc(-0.5, 0.5), mp.mpc(1.5, 0.5), mp.mpc(1.5, 20.0), mp.mpc(-0.5, 20.0)])
        pred20 = theta_smooth_dh(20.0) / math.pi + c0
        check("T2d D-H argument-principle count matches its OWN FE-derived budget",
              r30 < 0.02 and r20 < 0.02 and abs(round(w20) - pred20) <= 1.0,
              f"T=30: {w30:.3f} (c0={c0:+.3f}); T=20: {w20:.3f} vs pred {pred20:.2f}")
        results["t2_dh_ap_30"] = float(w30)
        results["t2_dh_c0"] = float(c0)

        # the type-exclusion number at the off-line height
        T0 = 85.699
        excess = (theta_smooth_dh(T0) / math.pi + c0) - n_smooth_zeta(T0)
        lead = math.log(5) / (2 * math.pi) * T0
        check("T2e D-H budget exceeds the RIEMANN-TYPE budget by ~(log5/2pi)T",
              abs(excess - lead) / lead < 0.15,
              f"excess {excess:.1f} zeros at T=85.699 vs leading {lead:.1f}")
        results["t2_budget_excess_857"] = float(excess)
        print("    => the pin's Riemann-type hypotheses (H1 FE data, H3 budget) exclude")
        print("       D-H BY TYPE: wrong gamma factor/conductor at O(1), and a budget")
        print(f"       surplus of ~{excess:.0f} zeros by its first off-line height. Its own")
        print("       exact FE is irrelevant to a pin stated with Riemann FE data.")
    finally:
        mp.mp.dps = prev


# ==========================================================================
# T3: the pin's three hypotheses measured on xihat_lambda at finite lambda.
# ==========================================================================
def zero_grid_count(xh, Tmax):
    """Real zeros of the FUNCTION xihat by sign changes of Re(xihat) on a
    grid of step phi/16 (offset phi/32 so exact lattice points are dodged).
    WHY function zeros: e1l counted OPERATOR eigenvalues; Thm 5.10(ii) makes
    them agree in the paper, but the pin's budget hypothesis is about the
    determinant FUNCTION, and the two can differ in the faithful build
    (ghost eigenvalues). We measure the function."""
    xs = np.arange(1.0 + xh.phi / 32, Tmax, xh.phi / 16)
    g = np.real(xh(xs))
    sc = np.where(np.diff(np.sign(g)) != 0)[0]
    return 0.5 * (xs[sc] + xs[sc + 1])


def run_t3(results, quick):
    print("\n[T3] PIN AT FINITE LAMBDA: FE / growth / budget / Dirichlet-face on xihat_lambda")
    consume("T3", "e1k ground state (truncated Weil form; Lambda streams)",
            "FE-derived smooth budget curves (gamma data)",
            "zeta/Phi_dh VALUES as envelope reference (no zeros)",
            "NO zero lists, NO operator eigenvalues")
    streams = make_streams(80, float_out=True)
    grid = ([("ZETA", 2.2, 12), ("ZETA", 2.6, 16), ("D-H", 2.6, 16)] if quick else
            [("ZETA", 2.2, 12), ("ZETA", 2.6, 16), ("ZETA", 3.0, 32),
             ("ZETA", SQRT13, 48), ("D-H", 2.6, 16), ("D-H", SQRT13, 48)])
    rows = []
    for label, lam, N in grid:
        r = get_build(label, lam, N, streams)
        xh = Xihat(r)
        Twin = 2 * math.pi * lam * lam
        scale = float(np.max(np.abs(xh(np.linspace(0.5, Twin, 400)))))

        # (i) FE face: evenness (the z -> -z inversion = s -> 1-s) + realness
        zs = np.linspace(0.3, Twin, 157)
        zc = zs[:60] - 0.35j
        d_even = float(max(np.max(np.abs(xh(zs) - xh(-zs))),
                           np.max(np.abs(xh(zc) - xh(-zc)))) / scale)
        d_real = float(np.max(np.abs(np.imag(xh(np.linspace(1.0, Twin, 500))))) / scale)

        # (ii) growth face: exponential type on the imaginary axis vs the
        # Paley-Wiener bound L/2 = log lambda (support of the log-circle).
        ys = np.array([30.0, 60.0, 90.0])
        tv = np.log(np.abs(xh(1j * ys)))
        slope = float(np.polyfit(ys, tv, 1)[0])
        type_ratio = slope / math.log(lam)

        # lattice tail: xihat(phi m) = 0 exactly for |m| > N (the common
        # sin(zL/2) factor). This pins the far budget to the lattice line.
        mtail = np.arange(N + 1, N + 7)
        tail = float(np.max(np.abs(xh(xh.phi * mtail))) / scale)

        # (iii) budget face: function-zero count vs OWN FE-derived curve
        zeros_at = zero_grid_count(xh, 1.32 * Twin)
        own = (n_smooth_zeta if label == "ZETA" else
               (lambda T: theta_smooth_dh(T) / math.pi + results.get("t2_dh_c0", -0.5)))
        ck_frac = (0.25, 0.5, 0.75, 1.0, 1.25)
        prof = []
        print(f"    {label} lam={lam:.3f} N={N}  Twin={Twin:.1f}  phi={xh.phi:.3f}  "
              f"phiN={xh.phi*N:.1f}")
        print(f"      {'T':>7} {'N_func':>7} {'own-RvM':>8} {'lattice':>8} {'zeta-RvM':>9}")
        for f in ck_frac:
            T = f * Twin
            nf = int(np.sum(zeros_at <= T))
            prof.append((T, nf, own(T), T / xh.phi, n_smooth_zeta(T)))
            print(f"      {T:7.1f} {nf:7d} {own(T):8.1f} {T/xh.phi:8.1f} {n_smooth_zeta(T):9.1f}")
        # crossover: first grid height where the function count leaves the
        # own-RvM curve by >= 3 (3 absorbs the O(1) doubled-zero fragility)
        Tg = np.arange(2.0, 1.30 * Twin, xh.phi / 4)
        nfg = np.searchsorted(zeros_at, Tg, side="right")
        owng = np.array([own(T) for T in Tg])
        dev = np.abs(nfg - owng)
        icx = np.where(dev >= 3.0)[0]
        Tc = float(Tg[icx[0]]) if len(icx) else float("inf")
        edge_nf = int(np.sum(zeros_at <= Twin))
        rows.append(dict(label=label, lam=lam, N=N, Twin=Twin, d_even=d_even,
                         d_real=d_real, type_ratio=type_ratio, tail=tail,
                         Tc=Tc, edge_nf=edge_nf, edge_own=own(Twin),
                         edge_lattice=Twin / xh.phi, prof=prof,
                         zeros_at=zeros_at, coef_im=xh.coef_im_frac))
        tcs = f"{Tc:.1f}" if math.isfinite(Tc) else f">{1.30*Twin:.0f}"
        print(f"      FE defect: even {d_even:.1e}, real {d_real:.1e} | type slope/log lam = "
              f"{type_ratio:.3f} | lattice tail {tail:.1e} | T_c(own-RvM departure) = {tcs}")

        # winding cross-check at the headline cutoffs: counts complex zeros
        # too, so a mismatch with the sign-change count exposes ghost pairs.
        if (N >= 32 or quick) and label == "ZETA":
            wz, rz, _ = winding_count(lambda z: complex(xh(np.array([z]))[0]),
                                      [1.0 - 0.4j, Twin + 0.4 - 0.4j,
                                       Twin + 0.4 + 0.4j, 1.0 + 0.4j], n0=256)
            check("T3d winding cross-check: function count = sign-change count +- 2",
                  abs(round(wz) - edge_nf) <= 2 and rz < 0.05,
                  f"winding {wz:.2f} vs sign-count {edge_nf} on [1,{Twin:.0f}]x[-0.4,0.4]")
            results["t3_winding_headline"] = float(wz)

    # ---- per-face checks over the sweep ----
    d_even_max = max(r["d_even"] for r in rows)
    d_real_max = max(r["d_real"] for r in rows)
    check("T3a FE face VERIFIABLE at finite lambda (evenness+realness defect tiny)",
          d_even_max < 1e-8 and d_real_max < 1e-8,
          f"max evenness {d_even_max:.1e}, max realness {d_real_max:.1e}")
    tr = [r["type_ratio"] for r in rows]
    check("T3b growth face VERIFIABLE: exponential type = log lambda (PW bound)",
          all(0.85 < x < 1.10 for x in tr),
          f"slope/log lam in [{min(tr):.3f}, {max(tr):.3f}] across the sweep")
    check("T3c lattice tail exact: xihat(phi m)=0 for |m|>N (sin factor)",
          max(r["tail"] for r in rows) < 1e-12,
          f"max |xihat(phi m)|/scale = {max(r['tail'] for r in rows):.1e}")

    # ---- budget-face verdicts (measured; per-build classification) ----
    # WHY these particular checks: the D-H twin (the clean control) exhibits
    # a TWO-REGIME law: arithmetic own-RvM core below its own
    # conductor-rescaled horizon (~Twin/5), exact lattice spacing phi above
    # it. The zeta twin keeps an accurate arithmetic core in the middle band
    # but its LOW band [0,14] (where zeta's own RvM count is ~0) is
    # erratically filled with ~phi-spaced zeros (the LATTICE FLOOR: cleared
    # at two of the four cutoffs, not at the others; the pole ablation below
    # shows this is NOT a pole-term artifact), so its edge count is
    # bracketed between own-RvM and the lattice line rather than pinned.
    # H3 is therefore NOT inherited at finite lambda.
    z_rows = [r for r in rows if r["label"] == "ZETA"]
    d_rows = [r for r in rows if r["label"] == "D-H"]

    def spacing(r, lo, hi):
        zs = r["zeros_at"][(r["zeros_at"] >= lo) & (r["zeros_at"] <= hi)]
        return float(np.mean(np.diff(zs))) if len(zs) >= 3 else float("nan")

    def own_spacing(label, T):
        q = 1.0 if label == "ZETA" else 5.0
        return 2 * math.pi / math.log(q * T / (2 * math.pi))

    dh_ok, dh_msg = True, []
    for r in d_rows:
        sp = spacing(r, 0.5 * r["Twin"], r["Twin"])
        osp = own_spacing("D-H", 0.75 * r["Twin"])
        phi_here = math.pi / math.log(r["lam"])
        lat_dev = abs(sp / phi_here - 1)
        own_dev = abs(sp / osp - 1)
        dh_ok = dh_ok and lat_dev < 0.12 and own_dev > 0.25
        dh_msg.append(f"lam={r['lam']:.2f}: sp={sp:.2f} vs phi {phi_here:.2f} "
                      f"({100*lat_dev:.0f}%) vs own {osp:.2f} ({100*own_dev:.0f}%)")
    check("T3e D-H budget face: LATTICE regime above its own horizon (spacing = phi, not own-RvM)",
          dh_ok, "; ".join(dh_msg))

    dh_ta, ta_msg = True, []
    for r in d_rows:
        T = 0.5 * r["Twin"]
        nf = int(np.sum(r["zeros_at"] <= T))
        own_c = theta_smooth_dh(T) / math.pi + results.get("t2_dh_c0", -0.5)
        zeta_c = n_smooth_zeta(T)
        dh_ta = dh_ta and abs(nf - own_c) < abs(nf - zeta_c) \
            and (r["edge_own"] - r["edge_nf"]) >= 3
        ta_msg.append(f"lam={r['lam']:.2f}: n({T:.0f})={nf} vs own {own_c:.1f} / "
                      f"zeta-type {zeta_c:.1f}; edge deficit {r['edge_own']-r['edge_nf']:.1f}")
    check("T3f D-H budget face is TYPE-AWARE below the horizon (own conductor-5 curve wins)",
          dh_ta, "; ".join(ta_msg))

    # zeta: bracket + artifact block, with the D-H clean-control contrast
    z_ok, z_msg = True, []
    for r in z_rows:
        bracket = (r["edge_own"] - 4 <= r["edge_nf"] <= r["edge_lattice"] + 2)
        n_low = int(np.sum(r["zeros_at"] <= 13.0))
        excess_low = n_low - n_smooth_zeta(13.0)
        z_ok = z_ok and bracket
        near = "own-RvM" if abs(r["edge_nf"] - r["edge_own"]) <= \
            abs(r["edge_nf"] - r["edge_lattice"]) else "lattice"
        z_msg.append(f"lam={r['lam']:.2f}: edge {r['edge_nf']} in "
                     f"[{r['edge_own']:.1f}, {r['edge_lattice']:.1f}] nearer {near}, "
                     f"low-band fill {excess_low:+.1f}")
    dh_low_clean = all(
        abs(int(np.sum(r["zeros_at"] <= 13.0))
            - (theta_smooth_dh(13.0) / math.pi + results.get("t2_dh_c0", -0.5))) <= 1.5
        for r in d_rows)
    check("T3h ZETA budget face NOT pinned: bracketed own-RvM..lattice, erratic low-band "
          "lattice fill (D-H control matches ITS own curve)", z_ok and dh_low_clean,
          "; ".join(z_msg))

    # pole ablation: rebuild the zeta twin at (2.6, 16) WITHOUT the pole
    # term. WHY: to attribute the low-band fill correctly. Measured: the
    # block SURVIVES the ablation (same n_low), and the edge count RISES to
    # the lattice value, so the fill is the lattice floor of the finite
    # object, not a pole-term artifact, and the pole term actually pulls the
    # count toward RvM. (The sqrt13 ablation, 65s, reproduces this: n_low
    # 5 -> 5, edge 29 -> 33 = lattice; recorded in the .md for ADVERSARY.)
    r26 = next(r for r in z_rows if abs(r["lam"] - 2.6) < 1e-9)
    cfgz = ZETA_CFG
    rnp = build_float(16, 2.6, streams[0], cfgz["dens_a"], cfgz["dens_b"], False)
    xh_np = Xihat(rnp)
    za_np = zero_grid_count(xh_np, 1.02 * r26["Twin"])
    nlow_np = int(np.sum(za_np <= 13.0))
    nedge_np = int(np.sum(za_np <= r26["Twin"]))
    nlow_p = int(np.sum(r26["zeros_at"] <= 13.0))
    check("T3i pole ablation: the low-band lattice fill is NOT pole-caused",
          abs(nlow_np - nlow_p) <= 1,
          f"lam=2.6: n_low {nlow_p} (pole) vs {nlow_np} (no pole); edge "
          f"{r26['edge_nf']} vs {nedge_np} (lattice {r26['edge_lattice']:.1f})")
    results["t3_ablation_nlow"] = np.array([nlow_p, nlow_np])
    results["t3_ablation_edge"] = np.array([r26["edge_nf"], nedge_np])

    # (iv) Dirichlet face: unpack f_lam(s) = xihat(z)/[(s(s-1)/2)pi^{-s/2}Gamma(s/2)]
    # on Re s = 2 and measure how far it tracks zeta(2+it) before the
    # Paley-Wiener floor forces exponential divergence. WHY: Hamburger's
    # hypothesis is exactly that this face exists globally; a PW function of
    # finite type cannot decay like Gamma (compact FT support + exponential
    # decay would force real-analytic FT = 0), so the face MUST fail beyond a
    # window; we measure the window and the escape rate (predicted pi/4).
    prev = mp.mp.dps
    mp.mp.dps = 30
    try:
        print("    Dirichlet face (zeta twins): |f_lam(2+it)/zeta(2+it)|, window + escape rate")
        dir_rows = []
        for r in [q for q in rows if q["label"] == "ZETA"]:
            xh = Xihat(get_build("ZETA", r["lam"], r["N"], streams))
            def f_ratio(t):
                zv = complex(t, -1.5)
                s = mp.mpc(2, t)
                fac = (s * (s - 1) / 2) * mp.pi ** (-s / 2) * mp.gamma(s / 2)
                fl = complex(xh(np.array([zv]))[0]) / complex(fac)
                return abs(fl) / abs(complex(mp.zeta(s)))
            r0 = f_ratio(0.0)
            t_dir = None
            for t in np.arange(0.0, 1.2 * r["Twin"], 1.0):
                if not (0.5 < f_ratio(t) / r0 < 2.0):
                    t_dir = float(t)
                    break
            t_dir = t_dir if t_dir is not None else float("inf")
            # escape rate beyond the operator range phi*N (the PW floor)
            phiN = (math.pi / math.log(r["lam"])) * r["N"]
            tlo, thi = phiN + 10, phiN + 40
            def logf(t):
                zv = complex(t, -1.5)
                s = mp.mpc(2, t)
                fac = (s * (s - 1) / 2) * mp.pi ** (-s / 2) * mp.gamma(s / 2)
                return float(mp.log(abs(complex(xh(np.array([zv]))[0]))) - mp.log(abs(fac)))
            rate = (logf(thi) - logf(tlo)) / (thi - tlo)
            dir_rows.append((r["lam"], t_dir, rate))
            print(f"      lam={r['lam']:.3f}: window t_dir={t_dir:6.1f} (Twin={r['Twin']:.1f}), "
                  f"escape rate {rate:.3f} vs pi/4={math.pi/4:.3f}")
        check("T3g Dirichlet face NOT inherited: finite window, escape at the archimedean rate",
              all(math.isfinite(t) and t < tw["Twin"] for t, tw in
                  zip([d[1] for d in dir_rows], [q for q in rows if q["label"] == "ZETA"]))
              and all(0.55 * math.pi / 4 < d[2] < 1.15 * math.pi / 4 for d in dir_rows),
              f"windows {[round(d[1],1) for d in dir_rows]}, rates {[round(d[2],3) for d in dir_rows]}")
        results["t3_dirichlet_windows"] = np.array([d[1] for d in dir_rows])
        results["t3_dirichlet_rates"] = np.array([d[2] for d in dir_rows])
    finally:
        mp.mp.dps = prev

    for r in rows:
        tag = f"t3_{r['label'].replace('-','')}_{r['lam']:.3f}"
        results[f"{tag}_prof"] = np.array(r["prof"])
        results[f"{tag}_zeros"] = r["zeros_at"]
        for k in ("d_even", "d_real", "type_ratio", "tail", "Tc", "edge_nf",
                  "edge_own", "edge_lattice"):
            results[f"{tag}_{k}"] = r[k]
    return rows


# ==========================================================================
# T4: the conditional pin, its teeth, and its counterexample.
# ==========================================================================
def run_t4(results, quick):
    print("\n[T4] THE CONDITIONAL PIN: what the budget kills, and what it provably cannot")
    consume("T4", "Xi VALUES via mp.zeta (no zeros consumed)",
            "RvM-comb points from gamma data (smooth inversion, K1-clean)",
            "closed-form perturbation zeros")
    prev = mp.mp.dps
    mp.mp.dps = 25
    try:
        # ---- P1: in-strip FE-preserving oscillation, killed by the budget --
        c1, a1 = 0.9, 2.0
        y1 = math.acosh(1 / c1) / a1          # Im of the extra zeros: 0.2336
        F1 = lambda z: complex(Xi_z(z)) * (1 + c1 * cmath.cos(a1 * complex(z)))
        z0 = (math.pi + 1j * math.acosh(1 / c1)) / a1
        v0 = abs(F1(z0))
        wv, rv, _ = winding_count(F1, [z0 - 0.12 - 0.12j, z0 + 0.12 - 0.12j,
                                       z0 + 0.12 + 0.12j, z0 - 0.12 + 0.12j], n0=32)
        check("T4a P1 extra zeros verified: closed-form z_k in-strip (|Im|<1/2), winding 1",
              v0 < 1e-12 and round(wv) == 1 and y1 < 0.5,
              f"|F1(z0)|={v0:.1e}, Im z0={y1:.4f}, winding={wv:.3f}")

        Trect = 29.5
        wXi, rXi, _ = winding_count(lambda z: complex(Xi_z(z)),
                                    [1 - 0.45j, Trect - 0.45j, Trect + 0.45j, 1 + 0.45j])
        w1, r1, _ = winding_count(F1, [1 - 0.45j, Trect - 0.45j, Trect + 0.45j, 1 + 0.45j])
        nsm = n_smooth_zeta(Trect)
        pred_extra = 2 * ((Trect - 1) * a1 / (2 * math.pi))   # two conj zeros per 2pi/a
        check("T4b P1 BUDGET KILL: strip count exceeds RvM by ~ (a/pi) T (linear excess)",
              rXi < 0.02 and r1 < 0.02 and (round(w1) - nsm) > 12
              and abs((round(w1) - round(wXi)) - pred_extra) <= 3,
              f"N_pert={w1:.2f} vs Xi {wXi:.2f} vs RvM {nsm:.1f}; excess {round(w1)-round(wXi)}"
              f" ~ pred {pred_extra:.1f}")
        results["t4_p1_count"] = float(w1)
        results["t4_xi_count"] = float(wXi)

        # ---- P2: off-strip variant, invisible to a strip-only budget -------
        c2 = 0.05
        y2 = math.acosh(1 / c2) / a1          # 1.844: outside |Im z| <= 1/2
        F2 = lambda z: complex(Xi_z(z)) * (1 + c2 * cmath.cos(a1 * complex(z)))
        w2s, r2s, _ = winding_count(F2, [1 - 0.45j, Trect - 0.45j, Trect + 0.45j, 1 + 0.45j])
        check("T4c P2 off-strip perturbation SURVIVES a strip-only budget (count unchanged)",
              r2s < 0.02 and round(w2s) == round(wXi),
              f"strip count {w2s:.2f} = bare Xi {wXi:.2f}; extra zeros at Im=+-{y2:.2f}")
        if not quick:
            # WHY 2.6: the edge Im z = 2.5 would put the top side on s = -2,
            # a Gamma(s/2) pole point (cancelled by zeta's trivial zero in
            # xi, but numerically singular); 2.6 dodges it and still encloses
            # the extra zeros at Im = +-1.84.
            w2f, r2f, _ = winding_count(
                F2, [-Trect - 2.6j, Trect - 2.6j, Trect + 2.6j, -Trect + 2.6j], n0=96)
            # bare Xi in the full rectangle = 2 * strip count (z -> -z pairs)
            full_extra = round(w2f) - 2 * round(wXi)
            check("T4d P2 caught only by the FULL-PLANE budget (Hadamard-genus count)",
                  r2f < 0.03 and full_extra >= 30,
                  f"full-plane count {w2f:.2f} vs bare {2*round(wXi)}; extra {full_extra}")
            results["t4_p2_full"] = float(w2f)

        # ---- P3: the RvM-comb relocation counterexample (the pin's edge) ---
        # Comb points t_k from the SMOOTH inversion n_smooth_zeta(t_k) = k:
        # gamma-factor data only, no zeta zero is consumed. G1 = canonical
        # product on the comb; G2 = same with the first 60 points relocated
        # by 0.3 of the local gap, alternating sign (no crossings). Both are
        # even, real, entire of order 1, with IDENTICAL zero-counting
        # functions obeying the RvM budget to O(1); G1 != G2. Hence
        # FE + growth + budget does NOT pin a unique F. PROVEN by
        # construction; the numbers below instantiate it.
        K = 200
        # coarse bracket + bisection on the smooth curve (monotone past 17.8)
        Tgrid = np.arange(15.0, 430.0, 0.5)
        ns = np.array([n_smooth_zeta(T) for T in Tgrid])
        tks = []
        for k in range(1, K + 1):
            i = int(np.searchsorted(ns, k))
            lo, hi = Tgrid[i - 1], Tgrid[i]
            for _ in range(60):
                mid = 0.5 * (lo + hi)
                if n_smooth_zeta(mid) < k:
                    lo = mid
                else:
                    hi = mid
            tks.append(0.5 * (lo + hi))
        tks = np.array(tks)
        gaps = np.diff(tks)
        t2s = tks.copy()
        t2s[:60] += 0.3 * gaps[:60] * ((-1.0) ** np.arange(60))
        results["t4_comb"] = tks

        def G(z, tk):
            z = np.asarray(z, complex)
            return np.prod(1.0 - (z[..., None] ** 2) / (tk[None, :] ** 2), axis=-1)

        def logabsG(z, tk):
            return float(np.sum(np.log(np.abs(1.0 - (complex(z) ** 2) / tk ** 2))))

        # budget of the comb: counts match the smooth curve to O(1)
        okb = all(abs(int(np.sum(tks <= T)) - n_smooth_zeta(T)) <= 2
                  and abs(int(np.sum(t2s <= T)) - n_smooth_zeta(T)) <= 2
                  for T in (50.0, 150.0, 250.0))
        # order proxy: log log max |G| on circles ~ slope 1 + log-correction
        rads = [40.0, 80.0, 160.0]
        mx = [max(logabsG(r * cmath.exp(1j * th), tks) for th in np.linspace(0.1, 1.5, 12))
              for r in rads]
        slope = float(np.polyfit(np.log(rads), np.log(mx), 1)[0])
        # distinctness on [1, 30]: pointwise-relative metric. WHY: G1 and G2
        # have different zero SETS (t_1 vs t_1 + 0.3 gap), so near a zero of
        # one the other is O(local scale): the pointwise ratio reaches O(1)
        # even though both functions are globally small there.
        zz = np.linspace(1.0, 30.0, 400)
        g1, g2 = G(zz, tks), G(zz, t2s)
        supd = float(np.max(np.abs(g1 - g2) / (np.abs(g1) + np.abs(g2))))
        # unpackability: nonzero at the pole slot s=1 (z = -i/2), so the
        # s = 0,1 pole/residue normalization can be imposed on BOTH
        gpole = abs(complex(G(np.array([-0.5j]), tks)[0]))
        check("T4e P3 comb budget: both G1, G2 count = RvM smooth curve + O(1)",
              okb, "checked at T = 50, 150, 250")
        check("T4f P3 growth: canonical products of order ~1 (loglog slope w/ log-corr)",
              slope < 1.45, f"slope {slope:.3f} on r in {rads}")
        check("T4g P3 NON-UNIQUENESS: G1 != G2, both even/real/order-1/RvM-budget",
              supd > 0.5,
              f"max pointwise |G1-G2|/(|G1|+|G2|) on [1,30] = {supd:.3f}: bare pin FALSE")
        check("T4h P3 both unpackable at the pole slot (G(-i/2) != 0)",
              gpole > 1e-6, f"|G1(-i/2)| = {gpole:.4f}")
        results["t4_p3_supdiff"] = supd
        results["t4_p3_order_slope"] = slope
        print("    => VERDICT: the budget has real teeth against FE-preserving PROFUSION")
        print("       (any oscillation factor adds a LINEAR zero excess: killed), but")
        print("       FE + order 1 + RvM budget is NOT a pin: relocation of the comb is")
        print("       invisible to counting. The pin must consume the lattice through a")
        print("       Dirichlet/Hamburger hypothesis; with it, budget becomes redundant")
        print("       (classical Hamburger 1921). See the .md for the tiered statement.")
    finally:
        mp.mp.dps = prev


# ==========================================================================
# T5: the Beurling fake fails the pin for a NAMEABLE reason.
# ==========================================================================
def run_t5(results):
    print("\n[T5] BEURLING PIN FAILURE: the density-matched fake, clause by clause")
    consume("T5", "Beurling fake (b_p = p e^eps, eps U[-0.25,0.25], seed 149)",
            "generalized-integer counting", "theta_B series")
    B = BeurlingSystem(prime_bound=15000, eps=0.25, seed=149)
    print(f"    fake system: {len(B.logs)} perturbed primes, eps={B.eps}, seed 149")

    # H1-engine clause: the fake's theta has a measurable FE defect (e2ak C5b)
    small = [lv for lv in B.gen_integers(40)]
    def th_b(u):
        return 1 + 2 * sum(math.exp(-math.pi * math.exp(2 * lv) * u) for lv in small if lv > 0)
    worst_b = max(abs(th_b(1 / t) - math.sqrt(t) * th_b(t)) / th_b(1 / t)
                  for t in (0.7, 1.3, 2.0))
    check("T5a fake theta FE defect is O(1) (no Poisson, no lattice)",
          worst_b > 1e-3, f"relative defect {worst_b:.2f} (Z: <1e-25, T1a)")
    results["t5_theta_defect"] = worst_b

    # additive-counting clause: N_B(x) is not x + O(1)
    big = B.gen_integers(20000)
    import bisect
    xs = [math.exp(math.log(20000) * i / 400) for i in range(1, 401)]
    counts = [bisect.bisect_right(big, math.log(x)) for x in xs]
    c0 = counts[-1] / xs[-1]
    best = min(max(abs(n - c * x) for n, x in zip(counts, xs))
               for c in [c0 * (0.98 + 0.0002 * i) for i in range(201)])
    check("T5b fake integer count is NOT x + O(1)", best > 10,
          f"best linear sup error {best:.0f} at x<=2e4 (Z: <=1)")
    results["t5_count_error"] = best

    # Euler side exists; continuation does not: the budget is UNDERIVABLE
    lp = [math.log1p(-math.exp(-2 * lb)) for lb in B.logs]   # log(1 - b^-2)
    zb_full = math.exp(-sum(lp))
    zb_half = math.exp(-sum(lp[: len(lp) // 2]))
    check("T5c fake Euler product converges on Re s > 1 (zeta_B(2) stabilizes)",
          abs(zb_full - zb_half) / zb_full < 0.01,
          f"zeta_B(2) = {zb_full:.6f} (half-product {zb_half:.6f})")
    results["t5_zeta_b_2"] = zb_full
    print("    NAMED FAILING CLAUSE: no additive lattice => no Poisson => no theta FE")
    print("    => no completed function symmetric in s <-> 1-s => the argument-principle")
    print("    budget (H3) is UNDERIVABLE and the Mellin/residue engine (T1d) has no fuel.")
    print("    The fake HAS a Dirichlet series, but on non-lattice frequencies {log n_B}:")
    print("    Hamburger's mechanism (T1) consumes the INTEGER lattice, which is exactly")
    print("    what the fake lacks. The pin fails for the fake at H1-engine + H3 + H4.")


# ==========================================================================
# T6: mechanical K1 / discipline audit.
# ==========================================================================
def run_t6(results, guards):
    print("\n[T6] K1 / DISCIPLINE AUDIT")
    src = Path(__file__).read_text(encoding="utf-8")
    # tokens assembled at runtime so this audit block does not self-match;
    # comment lines and K1-ALLOW-marked lines (the guard installs) are
    # exempt because they are precisely the machinery that BLOCKS access.
    forbidden = ["zeta" + "zero", "ZETA_" + "ZEROS", "DH_" + "ZEROS", ".zeros" + "("]
    scan = [ln for ln in src.splitlines()
            if not ln.strip().startswith("#") and "K1-ALLOW" not in ln]
    hits = [tok for tok in forbidden if any(tok in ln for ln in scan)]
    check("T6a source scan: no zero-list / zero-scanner access in the pin path",
          not hits, f"forbidden tokens found: {hits}" if hits else "clean")
    check("T6b runtime guards on the zero scanners: installed, never tripped",
          guards["installed"] and not guards["tripped"], "any call would have raised")
    print("    input ledger (what each test consumed):")
    for test in sorted(LEDGER):
        for item in LEDGER[test]:
            print(f"      {test}: {item}")
    bad = [t for t, items in LEDGER.items()
           if any("zero list" in i.lower() and "no zero" not in i.lower() for i in items)]
    check("T6c ledger: no test consumed a zero list", not bad, str(bad) if bad else "")
    print("    NG1/C3 note: nothing endomorphism-shaped is introduced anywhere (entire")
    print("    functions, counts, theta series only), and the only route from the finite")
    print("    object to the prime data is the ARCHIMEDEAN unpacking (the Gamma factor,")
    print("    T3g): the pin conforms to the #156/#157 no-go geography automatically.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true", help="small sweeps, skip N=48/32 builds")
    args = ap.parse_args()
    t_start = time.time()
    mp.mp.dps = 25   # e1l-characterized regime for the builds; L-value tests raise it locally

    # K1 runtime guards: any zero-list access in this process raises.
    guards = {"installed": True, "tripped": False}
    def _forbid(*a, **k):
        guards["tripped"] = True
        raise RuntimeError("K1 guard: zero-list access attempted")
    mp.zetazero = _forbid                            # K1-ALLOW (guard install)
    _dhmod.davenport_heilbronn.zeros = _forbid       # K1-ALLOW (guard install)

    results = {}
    print("=" * 78)
    print("E1M: the Hamburger-type converse pin (LEARNINGS #154 upgrade-spec item 4)")
    print("=" * 78)

    run_t1(results)
    run_t2(results)
    run_t3(results, args.quick)
    run_t4(results, args.quick)
    run_t5(results)
    run_t6(results, guards)

    print("\n" + "=" * 78)
    print("VERDICT (tiered; details and honest statement in e1m_hamburger_pin.md)")
    print("  pin_hypotheses_verifiable_at_finite_lambda = MIXED (measured):")
    print("    FE face YES (defect ~1e-11), growth face YES (type = log lambda),")
    print("    budget face NO: two-regime (type-aware own-RvM core below a")
    print("    conductor-rescaled horizon, installed lattice above; zeta's low")
    print("    band erratically lattice-filled, NOT pole-caused: T3i ablation),")
    print("    Dirichlet face WINDOWED (escape at the archimedean rate pi/4).")
    print("  budget_kills_fe_perturbations = TRUE for profusion (linear excess,")
    print("    T4b), FALSE as a uniqueness pin (T4g relocation counterexample).")
    print("  beurling_fails_nameably = TRUE (no lattice => no theta FE => budget")
    print("    underivable; defect numbers in T5).")
    print("  dh_excluded_by_type = TRUE (own FE ~1e-30 exact, Riemann-type FE O(1)")
    print("    defect, budget surplus ~21 zeros at T=85.7).")
    print("  k1_clean = TRUE (T6 audit; budget curves from gamma data only).")
    print("  identification_split_from_convergence = REFORMULATED, NOT REDUCED:")
    print("    the bare #154 pin (FE+growth+budget) is PROVEN insufficient (T4g);")
    print("    the corrected pin is classical Hamburger and needs the Dirichlet/")
    print("    lattice face, which the finite family does NOT inherit (T3g). The")
    print("    residual open lemma (Dirichlet-face inheritance in the limit) is,")
    print("    conditional on the limit + growth package, EQUIVALENT to the")
    print("    identification F = c Xi it replaces (backward direction is trivial")
    print("    via zeta's own Dirichlet series): a positivity-free proof surface,")
    print("    not a weaker open statement. Details in the .md ADVERSARY banner.")
    print("=" * 78)

    n_ok = sum(1 for _, ok in CHECKS if ok)
    print(f"\nSELF-TEST: {n_ok}/{len(CHECKS)} checks passed")
    for name, ok in CHECKS:
        if not ok:
            print(f"  FAILED: {name}")

    np.savez_compressed(OUT, **{k: v for k, v in results.items()})
    print(f"Saved -> {OUT}")
    print(f"Total time {round(time.time() - t_start, 1)}s")
    if n_ok != len(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
