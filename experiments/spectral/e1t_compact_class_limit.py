"""E1T: the compactness trojan probed at the CCM D_log family (M4 trade test).

WHY THIS EXPERIMENT EXISTS
==========================
The merged frontier (LEARNINGS #154/#158/#160/#161) pins the residual open
step of the CCM D_log arc to ONE statement: the Section-7 uniform
determinant-class limit xihat_lambda -> Xi (= M4, an RH-equivalent positivity
with a rate). This probe asks whether that uniform limit can be TRADED for
three individually cheaper links, the "compactness trojan":
  (i)   certify the finite-lambda objects into a positivity class that is
        COMPACT after renormalization (Montel/Helly: subsequential limits
        then exist for free, no rate needed);
  (ii)  a Carleman-type one-sided determinacy condition (all subsequential
        limits coincide);
  (iii) the #160 Hamburger pin (the unique limit is identified as Xi).
Each link is MEASURED, not assumed. A negative or split verdict is a fully
acceptable outcome; nothing here is tuned toward a positive.

PRE-REGISTERED EXPECTATIONS AND EXITS (stated before the results)
=================================================================
Q1 RENORMALIZATION: three natural normalizations are implemented
   (a: type-rescale z -> z/type with the type measured in-build; b: the
   e1n-style ghost/dressing quotient; c: the lattice-tail-aware coefficient
   measure, justified by the exact e1m tail identity xihat(phi m) = 0 for
   |m| > N). Pre-registered obstacle: the #160 type divergence
   (type ~ 0.93..0.98 x log lambda). Pre-registered exit: if no
   normalization bounds the type without destroying the target, the trojan
   dies at link (i) and THAT is the finding: M4 relocates into the
   normalization, verbatim.
Q2 CLASS CERTIFICATION: Hermite-Biehler-style in-class membership (zero
   reality in the strip) for zeta, the D-H twin and the Beurling fake
   through IDENTICAL code paths, plus the #161 Euler-gated certificate
   (nonnegative comb consumed explicitly as a hypothesis the code checks).
   Pre-registered: reality is CF-manufactured (#158) so all three should
   certify; D-H must be UNPOSABLE at the Euler gate (sign-changing comb);
   the fake must run and fail at a NAMEABLE lattice link.
Q3 DETERMINACY SURROGATE: coefficient/moment sequences along the lambda
   grid + a Carleman-type uniformity read + rate-free pairwise sup
   distances on fixed compacts. Pre-registered (from #160/#161: types
   diverge, floors stagnate): expect NO in-sample Cauchy trend for zeta
   (branch scatter) and window-tracking moment radii; exit: link (ii) is
   then not certified by finite data and the uniformity joint is relocated,
   not removed.
Q4 KILL TESTS: (a) the DMV screen: if the compactness certification behaves
   identically for the Beurling fake it consumes only density/circumference
   data and is structurally wrong as a discriminator; (b) K1 runtime guards
   (no RH-equivalent assumed anywhere); (c) honest accounting of WHERE the
   RH content relocates, with an overclaim tripwire.

WHAT THIS BUILDS
================
The e1k build_float machinery generalized to an explicit frequency comb
(build_comb, verified bit-identical to build_float on the integer streams),
so that ZETA (von Mangoldt comb), D-H (dense sign-changing comb) and the
BEURLING fake (b_p = p e^eps comb on non-integer frequencies, seed 149,
density-matched via zeta's own archimedean density + pole term) all flow
through IDENTICAL code. Standard builds are reused from the e1n cache;
new builds (BEUR all, D-H 2.2/3.0) are cached under _cache/e1t_build_*.

HONEST SCOPE
============
This probe proves nothing about RH. Finite objects come from the faithful
e1k reimplementation (not the paper's exact operator; razor-thin zeta
margin; dps-25 branch, e1n branch-specificity caveat inherited). The
Beurling fake is density-matched only coarsely (theta to ~15 percent), and
its truncated Weil form is O(1)-indefinite (eps ~ -0.9..-1.4), which is a
density-level mismatch, not an RH bit. Thresholds marked "pinned" in the
.md companion were set from a calibration run of the same code, not
pre-registered. Claims are tiered in the .md.

ADVERSARY ROUND (2026-07-22, see _e1t_adversary.md)
===================================================
Verdict PASS_WITH_FIXES. What survived attack: the headline
trojan_trades_M4_away = NO, the harness bit-identity (now verified at a
REAL config, T0d: build_comb reproduces the e1n cache at D-H 2.6/16
exactly), the DMV screen, K1, and the eps question (rebuilt the fake at
eps 0.05/0.01: the Weil margin scales -0.88 -> -0.13 -> -0.025, so the
O(1) indefiniteness is matching-coarseness, not lattice-structural; the
measure-face alternation does NOT scale down (~0.31 at eps=0.01), so THAT
is the lattice-sensitive quantity). What was re-scoped: (1) T1e's "no
family-uniform positive-measure certificate" holds only in the RAW gauges;
in the FE-gated ghost-quotient gauge the ZETA measure face is near-positive
AND tight family-wide (fneg_q <= 0.028, r95_q <= 12.0) while D-H stays
>= 0.05 and BEUR >= 0.24: the dressed alternation is exactly the ghost
polynomial's sign pattern (new check T1f); (2) the Q3 "RH-blind" claim is
scoped to function-face/germ-face coherence surrogates: the eps trajectory
(max consecutive gap 3.4e-4 vs 8.6e-3) and the T1f gauge-positivity face
order ZETA above D-H, and the normalized gauged-measure Kolmogorov face is
mixed; (3) the ZETA 3.0 "13 zeros vs 11 crossings" close-pair anecdote did
NOT reproduce (13 crossings on both the plain and the e1m offset grid; the
close pair 40.86/41.03 has separation 0.178 > the phi/16 step 0.131) and
the strip count itself is dps-branch-dependent (18/13/12 at dps 15/25/35,
all reality-certified, none with |Im| in (0.02, 0.05]).

Run:
  python3 -m experiments.spectral.e1t_compact_class_limit           # full (~4 min cold)
  python3 -m experiments.spectral.e1t_compact_class_limit --quick   # < ~90 s, no npz
Outputs:
  experiments/spectral/e1t_compact_class_limit.npz   (FULL mode only)
  experiments/spectral/_cache/e1t_build_*.npz        (build cache, gitignored)
"""

from __future__ import annotations

import argparse
import math
import time
import warnings
from pathlib import Path

import numpy as np
import mpmath as mp
from scipy.special import loggamma

# Only builders/configs and the reusable instruments: NOT the reference zero
# lists and NOT operator_spectrum. Every claim consumes function VALUES.
from experiments.spectral.e1k_dh_dlog_testbed import (
    make_streams, build_float, ZETA_CFG, DH_CFG,
)
from experiments.spectral.e1n_prime_comb import XihatD, spurious_real_zeros
from experiments.spectral.e1m_hamburger_pin import winding_count, chi_riemann
from experiments._shared.beurling import BeurlingSystem
import experiments._shared.davenport_heilbronn as _dhmod

warnings.filterwarnings("ignore")

OUT = Path(__file__).with_suffix(".npz")
CACHE = Path(__file__).parent / "_cache"
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
# The generalized builder. WHY a copy rather than a wrapper: e1k's build_float
# hard-wires the integer loop n <= lambda^2; the trojan needs the SAME
# operator fed by an arbitrary frequency comb so the Beurling fake can enter
# through the identical assembly. T0a/T0b verify bit-identity on the integer
# streams, which is the "identical code path" claim made checkable.
# --------------------------------------------------------------------------
def _re_psi(a, y, h=1e-5):
    z = complex(a, y)
    return ((loggamma(z + h) - loggamma(z - h)) / (2 * h)).real


def build_comb(N, lam, pairs, dens_a, dens_b, use_pole):
    """e1k build_float with the prime term generalized to comb pairs
    (ell, w) = (log of the comb point, Lambda-weight x point^{-1/2})."""
    L = 2 * np.log(lam)
    phi = 2 * np.pi / L
    idx = list(range(-N, N + 1))
    D = 2 * N + 1

    def Vhat(n, z):
        d = z - phi * n
        if abs(d) < 1e-9:
            return 2 * L ** -0.5 * (L / 2) * np.cos(z * L / 2)
        return 2 * L ** -0.5 * np.sin(z * L / 2) / d

    def dens(t):
        return (_re_psi(dens_a, t / 2) + dens_b) / (2 * np.pi)

    A = np.zeros((D, D))
    cache = {}

    def arch(m, n):
        key = tuple(sorted((m, n)))
        nkey = tuple(sorted((-m, -n)))
        if key in cache:
            return cache[key]
        if nkey in cache:
            return cache[nkey]

        def f(tm):
            t = float(tm)
            return mp.mpf(Vhat(m, t) * Vhat(n, t) * dens(t))

        a, b = sorted([m * phi, n * phi])
        pts = ([mp.mpf("-inf"), mp.mpf(a), mp.mpf("inf")] if abs(a - b) < 1e-9
               else [mp.mpf("-inf"), mp.mpf(a), mp.mpf(b), mp.mpf("inf")])
        v = float(mp.quad(f, pts))
        cache[key] = v
        return v

    for i, m in enumerate(idx):
        for j, n in enumerate(idx):
            if j < i:
                A[i, j] = A[j, i]
            else:
                A[i, j] = arch(m, n)

    P = np.zeros((D, D), complex)
    if use_pole:
        av = np.array([Vhat(n, 0.5j) for n in idx])
        P = 2.0 * np.real(np.outer(np.conj(av), av))

    Ts = np.zeros((D, D), complex)
    for ell, w in pairs:
        if w == 0.0:
            continue
        for i, m in enumerate(idx):
            for j, nn in enumerate(idx):
                k = nn - m
                if k == 0:
                    Ip = Im = (L - ell)
                else:
                    Ip = (np.exp(1j * k * phi * (L - ell)) - 1) / (1j * k * phi)
                    Im = (np.exp(1j * k * phi * L) - np.exp(1j * k * phi * ell)) / (1j * k * phi)
                Ts[i, j] += w * ((1.0 / L) * np.exp(1j * nn * ell * phi) * Ip
                                 + (1.0 / L) * np.exp(-1j * nn * ell * phi) * Im)

    Q = A.astype(complex) + P - Ts
    Q = 0.5 * (Q + Q.conj().T)
    w_, V = np.linalg.eigh(Q)

    def efrac(v):
        vs = np.array([v[idx.index(-n)] for n in idx])
        return float(np.linalg.norm(0.5 * (v + vs)) / np.linalg.norm(v))

    # same even-selection convention as e1k (faithful to the paper's "even
    # ground state" assumption; the offset is recorded, not hidden)
    idx_even = 0
    for j in range(len(w_)):
        if efrac(V[:, j]) > 0.9:
            idx_even = j
            break
    return dict(idx=idx, phi=phi, L=L, Q=Q, eps=float(w_[idx_even]),
                xi=V[:, idx_even], even_frac=efrac(V[:, idx_even]),
                even_first=bool(idx_even == 0))


def int_pairs(stream, lam):
    """Integer comb pairs reproducing e1k's n <= lambda^2 loop exactly."""
    kmax = int(np.floor(lam * lam + 1e-9))
    return [(math.log(n), stream[n] * n ** -0.5)
            for n in range(2, kmax + 1) if stream[n] != 0.0]


def beur_pairs(B, lam):
    """Beurling comb: prime powers b_p^k with k log b_p <= 2 log lambda,
    weight log b_p x (b_p^k)^{-1/2} (the Euler-product log-derivative)."""
    L = 2 * math.log(lam)
    out = []
    for lb in B.logs:
        if lb > L:
            break
        k = 1
        while k * lb <= L + 1e-12:
            out.append((k * lb, lb * math.exp(-0.5 * k * lb)))
            k += 1
    return sorted(out)


# --------------------------------------------------------------------------
# Build inventory. WHY two caches: the six standard (label, lam, N) configs
# were built by e1k build_float for e1m/e1n and are reused bit-identically
# from the e1n cache; new configs (all BEUR, D-H 2.2/3.0) are built once by
# build_comb and cached under e1t_build_*. T0a/T0b justify the mixing.
# --------------------------------------------------------------------------
_STREAMS = None


def streams():
    global _STREAMS
    if _STREAMS is None:
        _STREAMS = make_streams(80, float_out=True)
    return _STREAMS


_BEUR = None


def beurling():
    global _BEUR
    if _BEUR is None:
        # the repo's canonical density-matched fake (beurling.py defaults)
        _BEUR = BeurlingSystem(prime_bound=15000, eps=0.25, seed=149)
    return _BEUR


_BUILDS: dict = {}


def get_build(label, lam, N):
    """Return (XihatD evaluator, meta dict). meta: eps, even_first."""
    key = (label, round(lam, 6), int(N))
    if key in _BUILDS:
        return _BUILDS[key]
    e1n_fn = CACHE / f"e1n_build_{label}_{lam:.4f}_{N}.npz"
    e1t_fn = CACHE / f"e1t_build_{label}_{lam:.4f}_{N}.npz"
    if label in ("ZETA", "D-H") and e1n_fn.exists():
        d = np.load(e1n_fn)
        out = (XihatD(d["idx"], d["phi"], d["L"], d["xi"]),
               dict(eps=float(d["eps"]), even_first=bool(d["even_ok"])))
    elif e1t_fn.exists():
        d = np.load(e1t_fn)
        out = (XihatD(d["idx"], d["phi"], d["L"], d["xi"]),
               dict(eps=float(d["eps"]), even_first=bool(d["even_first"])))
    else:
        if label == "ZETA":
            pairs, cfg = int_pairs(streams()[0], lam), ZETA_CFG
        elif label == "D-H":
            pairs, cfg = int_pairs(streams()[1], lam), DH_CFG
        else:
            # density-matched: zeta's OWN archimedean density and pole term;
            # only the comb differs (that IS the DMV screen configuration)
            pairs, cfg = beur_pairs(beurling(), lam), ZETA_CFG
        t0 = time.time()
        r = build_comb(N, lam, pairs, cfg["dens_a"], cfg["dens_b"], cfg["use_pole"])
        print(f"    [build] {label} lam={lam:.4f} N={N}: {time.time()-t0:.1f}s "
              f"(eps={r['eps']:+.2e}, even_frac={r['even_frac']:.5f})")
        CACHE.mkdir(exist_ok=True)
        np.savez_compressed(e1t_fn, idx=np.array(r["idx"], float), phi=r["phi"],
                            L=r["L"], xi=np.asarray(r["xi"], complex),
                            eps=r["eps"], even_first=r["even_first"])
        out = (XihatD(r["idx"], r["phi"], r["L"], np.asarray(r["xi"], complex)),
               dict(eps=r["eps"], even_first=r["even_first"]))
    _BUILDS[key] = out
    return out


# --------------------------------------------------------------------------
# The ghost/dressing gate (normalization b). WHY FE-gated: classifying a
# low-band real zero as spurious NEEDS the function's own FE-derived RvM
# budget saying that band is empty (zeta: no zeros below 14.13; D-H: below
# 5.09). The Beurling fake has no FE, hence no own-RvM curve, hence no
# "spurious" notion: normalization (b) is UNPOSABLE for it in principle,
# an input-typed gate exactly like the #161 Euler gate.
# --------------------------------------------------------------------------
def ghost_gate(label, xh):
    if label == "ZETA":
        return "POSABLE", spurious_real_zeros(xh, tmax=13.6)
    if label == "D-H":
        return "POSABLE", spurious_real_zeros(xh, tmax=4.9)
    return "UNPOSABLE_NO_FE", []


def qpoly(z, z0s):
    z = np.asarray(z, complex)
    out = np.ones_like(z)
    for z0 in z0s:
        out = out * (1 - z ** 2 / z0 ** 2)
    return out


def type_slope(xh, z0s=(), ys=(30.0, 60.0, 90.0)):
    """Exponential type from the imaginary-axis growth (e1m T3 method),
    optionally after the ghost quotient (polynomials shift the measured
    slope through the fit window even though the true type is unchanged)."""
    ys = np.asarray(ys, float)
    vals = np.log(np.abs(xh(1j * ys) / qpoly(1j * ys, z0s)))
    return float(np.polyfit(ys, vals, 1)[0])


def projd(u, v):
    """Projective sup distance: the pin identifies F = c Xi only up to a
    constant, so distances are measured after LSQ scale alignment."""
    c = np.vdot(v, u) / np.vdot(v, v)
    return float(np.max(np.abs(u - c * v)) / np.max(np.abs(u)))


def lowest_zeros(xh, tmax=8.0, k=3):
    """First k positive real zeros of xihat (object's own sign changes)."""
    xs = np.arange(0.05 + xh.phi / 32, tmax, xh.phi / 32)
    g = np.real(xh(xs))
    sc = np.where(np.diff(np.sign(g)) != 0)[0]
    return [0.5 * (xs[i] + xs[i + 1]) for i in sc[:k]]


# fixed compacts (pre-registered geometry: [0, 6] sits inside the measured
# e1n tracking window t_dir ~ 6..7; the 0.0037 offset dodges exact ghost
# points; the strip [0,10]x[-0.35,0.35] is a closed substrip of |Im z| < 1/2)
ZZ = np.linspace(0.05, 6.0, 240) + 0.0037
ZSTRIP = (np.linspace(0.05, 10.0, 160)[None, :]
          + 1j * np.array([-0.35, 0.0, 0.35])[:, None]).ravel()
ZC08 = np.linspace(1.0, 10.0, 90) + 0.8j
ZC15 = np.linspace(1.0, 10.0, 90) + 1.5j
TH_CIRC = np.linspace(0, 2 * np.pi, 256, endpoint=False)
R_TAYLOR = 2.0
CIRC = R_TAYLOR * np.exp(1j * TH_CIRC)


def m_red(xh, z0s, zc):
    """Type-subtracted Weyl-m proxy (surveyor fold-in): xihat = sin(az) T(z)
    with a = L/2 structural, so m_red = xihat'/xihat - a cot(az) - (ghost
    log-derivative) = T'/T carries NO exponential type: the type-divergence-
    proof reading of the object on a C+ segment."""
    a = xh.L / 2
    v = xh.d(zc) / xh(zc) - a * np.cos(a * zc) / np.sin(a * zc)
    for z0 in z0s:
        v = v - (1.0 / (zc - z0) + 1.0 / (zc + z0))
    return v


def esc_frac(xh, W=12.0):
    """Mass-escape indicator (surveyor fold-in): fraction of |c| coefficient
    mass at frequencies |phi n| > W. W = 12 is the clean-zeta r95 scale."""
    c = np.abs(np.real(xh.coef))
    x = xh.phi * xh.idx
    return float(np.sum(c[np.abs(x) > W]) / np.sum(c))


# --------------------------------------------------------------------------
# Truth evaluators (VALUES only, mpmath dps 30; no zero of any L-function
# is consumed anywhere in this module: K1 ledger + runtime guards in T4b).
# --------------------------------------------------------------------------
def Xi_z(z):
    s = mp.mpf("0.5") + 1j * mp.mpc(z)
    return (s * (s - 1) / 2) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def Phi_dh_z(z):
    s = mp.mpf("0.5") + 1j * mp.mpc(z)
    return ((mp.mpf(5) / mp.pi) ** (s / 2) * mp.gamma((s + 1) / 2)
            * _dhmod.davenport_heilbronn.evaluate(s))


_TRUTH: dict = {}


def truth_on(name, grid):
    key = (name, len(grid), complex(grid[0]), complex(grid[-1]))
    if key not in _TRUTH:
        f = Xi_z if name == "Xi" else Phi_dh_z
        with mp.workdps(30):
            _TRUTH[key] = np.array([complex(f(complex(z))) for z in grid])
    return _TRUTH[key]


# ==========================================================================
# T0: harness fidelity (the "identical code path" claim, made checkable).
# ==========================================================================
def run_t0(results, quick):
    print("\n[T0] HARNESS FIDELITY: build_comb == build_float; tail identity is structural")
    consume("T0", "Lambda / Lambda_DH streams (arithmetic input, no zeros)",
            "tiny fidelity builds (N=4, lam=1.8)")
    lz, ld = streams()
    rf = build_float(4, 1.8, lz, ZETA_CFG["dens_a"], ZETA_CFG["dens_b"], True)
    rc = build_comb(4, 1.8, int_pairs(lz, 1.8), ZETA_CFG["dens_a"], ZETA_CFG["dens_b"], True)
    dq = float(np.max(np.abs(rf["Q"] - rc["Q"])))
    check("T0a build_comb reproduces e1k build_float on the ZETA stream (max|dQ|)",
          dq < 1e-12, f"max|dQ| = {dq:.1e}")
    results["t0_dq_zeta"] = dq
    rf2 = build_float(4, 1.8, ld, DH_CFG["dens_a"], DH_CFG["dens_b"], False)
    rc2 = build_comb(4, 1.8, int_pairs(ld, 1.8), DH_CFG["dens_a"], DH_CFG["dens_b"], False)
    dq2 = float(np.max(np.abs(rf2["Q"] - rc2["Q"])))
    check("T0b build_comb reproduces build_float on the sign-changing D-H stream",
          dq2 < 1e-12, f"max|dQ| = {dq2:.1e}")
    results["t0_dq_dh"] = dq2

    # T0d [ADVERSARY]: the T0a/T0b toy config (N=4, lam=1.8) left the cache
    # mixing (e1n build_float caches + fresh build_comb builds INSIDE one
    # family) verified only at toy scale. Rebuild a REAL mixed-family config
    # (D-H 2.6/16, an e1n cache reuse) via build_comb and require exact
    # agreement. Full mode only (costs ~8 s); skipped when the e1n cache is
    # absent because then no mixing happens (everything comes from build_comb).
    e1n_fn = CACHE / "e1n_build_D-H_2.6000_16.npz"
    if not quick and e1n_fn.exists():
        r = build_comb(16, 2.6, int_pairs(ld, 2.6), DH_CFG["dens_a"],
                       DH_CFG["dens_b"], DH_CFG["use_pole"])
        d = np.load(e1n_fn)
        xi_old = np.asarray(d["xi"], complex)
        xi_new = np.asarray(r["xi"], complex)
        al = np.vdot(xi_new, xi_old) / np.vdot(xi_new, xi_new)
        dxi = float(np.max(np.abs(xi_old - al * xi_new)))
        deps = abs(float(d["eps"]) - r["eps"])
        check("T0d [ADVERSARY] build_comb reproduces the e1n build_float CACHE at a "
              "real mixed-family config (D-H 2.6/16): the cache-mixing claim at scale",
              dxi < 1e-12 and deps < 1e-15,
              f"max|dxi| = {dxi:.1e}, |deps| = {deps:.1e}")
        results["t0_dxi_dh26"] = dxi
    else:
        print("    (T0d skipped: quick mode or no e1n cache; no cache mixing to verify)")


def tail_defect(xh, lam):
    N = int(np.max(np.abs(xh.idx)))
    sc = float(np.max(np.abs(xh(np.linspace(0.5, 2 * np.pi * lam * lam, 200)))))
    mt = np.arange(N + 1, N + 7)
    return float(np.max(np.abs(xh(xh.phi * mt))) / sc)


# ==========================================================================
# T1 (Q1): renormalization. Measures, per build: raw type, ghost gate + list,
# quotiented type, the type-rescaled collapse metric, and the coefficient-
# measure face (sign structure + tightness). The three normalizations:
#   (a) z -> z/type: bounds the type by construction; measured question is
#       what survives (answer: the constant).
#   (b) ghost quotient: removes dressing; measured question is the type.
#   (c) coefficient measure (lattice-tail-aware: T0c shows the object IS its
#       in-band lattice data): measured question is positivity + tightness.
# ==========================================================================
def run_t1(results, grid, quick):
    print("\n[T1/Q1] RENORMALIZATION: type, ghost gate, collapse, measure face")
    consume("T1", "cached/new ground states (xihat values, exact derivative)",
            "object's own sign changes (ghost scan; landmark heights bound windows only)")
    rows = {}
    wc = 2.5 * np.exp(1j * np.linspace(0, 2 * np.pi, 48, endpoint=False))
    for label, lam, N in grid:
        xh, meta = get_build(label, lam, N)
        gate, z0s = ghost_gate(label, xh)
        tau = type_slope(xh)
        tau_q = type_slope(xh, z0s)
        # collapse metric: G(w) = F(w/tau_q)/F(0) on |w| <= 2.5 (normalization
        # a after b); the compact samples |z| <= 2.5/tau_q, inside the
        # low-band of every build
        zc = wc / tau_q
        f0 = complex(xh(np.array([0j]))[0]) / complex(qpoly(np.array([0j]), z0s)[0])
        G = xh(zc) / qpoly(zc, z0s) / f0
        supG1 = float(np.max(np.abs(G - 1)))
        supG = float(np.max(np.abs(G)))
        # measure face: raw sign split, alternating-gauge split, tightness
        c = np.real(xh.coef)
        tot = float(np.sum(np.abs(c)))
        fneg_raw = float(np.sum(np.abs(c[c < 0])) / tot)
        a = ((-1.0) ** xh.idx) * c
        if a[np.argmax(np.abs(a))] < 0:
            a = -a
        fneg_alt = float(np.sum(np.abs(a[a < 0])) / tot)
        order = np.argsort(np.abs(xh.idx))
        cum = np.cumsum(np.abs(c[order])) / tot
        r95 = float(xh.phi * np.abs(xh.idx[order])[np.searchsorted(cum, 0.95)])
        phiN = float(xh.phi * np.max(np.abs(xh.idx)))
        tail = tail_defect(xh, lam)
        esc = esc_frac(xh)
        lo = lowest_zeros(xh)
        # [ADVERSARY] the FE-gated ghost-quotient GAUGE on the measure face:
        # aq_n = a_n / q(phi n) is the lattice-value measure of the quotiented
        # function G = F/q (invertible, object-computable, FE-gated via the
        # ghost gate). Positivity/tightness in THIS gauge is what T1f pins.
        x_lat = xh.phi * np.asarray(xh.idx, float)
        qlat = (np.real(qpoly(x_lat.astype(complex), z0s)) if len(z0s)
                else np.ones_like(x_lat))
        aq = a / qlat
        if aq[np.argmax(np.abs(aq))] < 0:
            aq = -aq
        tvq = float(np.sum(np.abs(aq)))
        fneg_q = float(np.sum(np.abs(aq[aq < 0])) / tvq)
        cum_q = np.cumsum(np.abs(aq[order])) / tvq
        r95q = float(xh.phi * np.abs(xh.idx[order])[np.searchsorted(cum_q, 0.95)])
        escq = float(np.sum(np.abs(aq)[np.abs(x_lat) > 12.0]) / tvq)
        rows[(label, lam)] = dict(tau=tau, tau_q=tau_q, gate=gate, nghost=len(z0s),
                                  z0s=z0s, supG1=supG1, supG=supG, fneg_raw=fneg_raw,
                                  fneg_alt=fneg_alt, r95=r95, phiN=phiN, tail=tail,
                                  esc=esc, eps=meta["eps"], lo=lo,
                                  even_first=meta["even_first"],
                                  fneg_q=fneg_q, r95q=r95q, escq=escq, tvq=tvq)
        tag = f"t1_{label.replace('-', '')}_{lam:.3f}"
        for k in ("tau", "tau_q", "supG1", "supG", "fneg_raw", "fneg_alt",
                  "r95", "phiN", "tail", "esc", "eps",
                  "fneg_q", "r95q", "escq", "tvq"):
            results[f"{tag}_{k}"] = rows[(label, lam)][k]
        results[f"{tag}_ghosts"] = np.array(z0s)
        print(f"    {label:5s} lam={lam:.3f} N={N}: tau={tau:.3f} ({tau/math.log(lam):.3f} x log lam) "
              f"tau_q={tau_q:.3f} gate={gate} ghosts={len(z0s)} eps={meta['eps']:+.2e}")
        print(f"      sup|G-1|={supG1:.4f}  fneg_raw={fneg_raw:.3f} fneg_alt={fneg_alt:.3f} "
              f"r95x={r95:.1f}/{phiN:.1f} esc12={esc:.3f} tail={tail:.1e} "
              f"lowzeros={[round(z, 2) for z in lo]}")
        print(f"      gauge: fneg_q={fneg_q:.4f} r95_q={r95q:.1f} esc12_q={escq:.3f} "
              f"sum|aq|={tvq:.4f}")

    # T0c lives here (needs builds): the tail identity holds for ALL streams,
    # including the fake: the lattice-tail clause is basis-structural and
    # carries no arithmetic bits; the discriminating lattice clause must live
    # at the LIMIT level (T2c theta FE), not in the finite tail.
    worst_tail = max(r["tail"] for r in rows.values())
    check("T0c exact lattice tail xihat(phi m) = 0, |m| > N, for ALL three streams "
          "(basis-structural, arithmetic-free)", worst_tail < 1e-12,
          f"max defect {worst_tail:.1e} (incl. BEUR)")
    results["t0_tail_worst"] = worst_tail

    # ---- T1a: the pre-registered obstacle stands: raw type ~ log lambda ----
    ratios = {k: r["tau"] / math.log(k[1]) for k, r in rows.items()}
    fam = {}
    for (label, lam), r in rows.items():
        fam.setdefault(label, []).append((lam, r))
    inc_raw = all(all(a[1]["tau"] < b[1]["tau"] for a, b in zip(sorted(v), sorted(v)[1:]))
                  for v in fam.values())
    check("T1a type divergence CONFIRMED family-wide: tau/log lam in [0.85, 1.05] and "
          "tau strictly increasing along every family's grid (no free bound)",
          all(0.85 < x < 1.05 for x in ratios.values()) and inc_raw,
          f"ratios in [{min(ratios.values()):.3f}, {max(ratios.values()):.3f}]")

    # ---- T1b: normalization (b) does not bound the type; gate is FE-typed --
    inc_q = all(all(a[1]["tau_q"] < b[1]["tau_q"] for a, b in zip(sorted(v), sorted(v)[1:]))
                for v in fam.values())
    gates = {label: {rows[(label, lam)]["gate"] for lam in [k[1] for k in rows if k[0] == label]}
             for label in fam}
    gate_ok = (gates["ZETA"] == {"POSABLE"} and gates.get("D-H", {"POSABLE"}) == {"POSABLE"}
               and gates["BEUR"] == {"UNPOSABLE_NO_FE"})
    check("T1b ghost quotient (b) leaves the divergence intact (tau_q still increasing, "
          ">= 0.8 x log lam at dressed builds) and the gate is FE-typed "
          "(BEUR UNPOSABLE: no FE => no own-RvM low band => no 'spurious' notion)",
          inc_q and gate_ok
          and all(r["tau_q"] / math.log(k[1]) > 0.80 for k, r in rows.items() if r["nghost"]),
          f"tau_q zeta: {[round(rows[(('ZETA'), l)]['tau_q'], 3) for l in sorted([k[1] for k in rows if k[0] == 'ZETA'])]}")

    # ---- T1c: normalization (a) is compact in-sample (bounded on |w|<=2.5) --
    supGs = {k: r["supG"] for k, r in rows.items()}
    check("T1c type-rescale (a) certifies in-sample compactness: sup|G| on |w| <= 2.5 "
          "bounded across every build of every family", max(supGs.values()) < 8.0,
          f"max sup|G| = {max(supGs.values()):.2f} (BEUR largest)")

    # ---- T1d: and collapses to the CONSTANT for all three families ----------
    if not quick:
        zc_clean = [rows[("ZETA", 2.2)]["supG1"], rows[("ZETA", 3.0)]["supG1"]]
        dh_seq = [rows[("D-H", l)]["supG1"] for l in sorted(k[1] for k in rows if k[0] == "D-H")]
        be_seq = [rows[("BEUR", l)]["supG1"] for l in sorted(k[1] for k in rows if k[0] == "BEUR")]
        cond = (zc_clean[1] < zc_clean[0]
                and all(a > b for a, b in zip(dh_seq, dh_seq[1:]))
                and all(a > b for a, b in zip(be_seq, be_seq[1:])))
        detail = (f"zeta clean {zc_clean[0]:.3f}->{zc_clean[1]:.3f}, "
                  f"D-H {'->'.join(f'{x:.2f}' for x in dh_seq)}, "
                  f"BEUR {'->'.join(f'{x:.2f}' for x in be_seq)}")
    else:
        cond = rows[("ZETA", 2.2)]["supG1"] < 0.15 and rows[("BEUR", 2.2)]["supG1"] < 6.0
        detail = (f"quick levels: zeta 2.2 {rows[('ZETA', 2.2)]['supG1']:.3f}, "
                  f"BEUR {rows[('BEUR', 2.2)]['supG1']:.2f}")
    check("T1d the rescaled family COLLAPSES toward the constant 1 for ALL three "
          "streams (sup|G-1| decreasing in lambda): compactness of (a) is real but "
          "information-free; the identification content moved into the discarded "
          "factor tau_lambda", cond, detail)

    # ---- T1e: measure face (c): positivity + tightness are branch-fragile ---
    zd = [k for k in rows if k[0] == "ZETA" and rows[k]["nghost"] > 0]
    zcl = [k for k in rows if k[0] == "ZETA" and rows[k]["nghost"] == 0]
    raw_split = all(0.40 < rows[k]["fneg_raw"] < 0.60 for k in rows if k[0] != "BEUR")
    alt_clean = all(rows[k]["fneg_alt"] < 0.10 for k in zcl) if zcl else False
    alt_bad = (all(rows[k]["fneg_alt"] > 0.20 for k in zd) if zd else True) \
        and all(rows[k]["fneg_alt"] > 0.20 for k in rows if k[0] == "BEUR")
    check("T1e measure face (c), RAW/ALTERNATING gauges only (see T1f for the "
          "gauge re-scope): raw mass split ~50/50 (structural alternating gauge), "
          "near-positivity of the alternating gauge holds ONLY on the clean "
          "branch (< 10 percent negative mass) and fails on dressed + BEUR builds "
          "(> 20 percent): no RAW-gauge family-uniform positive-measure certificate",
          raw_split and alt_clean and alt_bad,
          f"fneg_alt clean {[round(rows[k]['fneg_alt'], 3) for k in zcl]} vs dressed "
          f"{[round(rows[k]['fneg_alt'], 3) for k in zd]} vs BEUR "
          f"{[round(rows[k]['fneg_alt'], 3) for k in rows if k[0] == 'BEUR']}")

    # ---- T1f [ADVERSARY]: the FE-gated ghost-quotient gauge re-scopes T1e ---
    # The dressed builds' alternation is EXACTLY the ghost polynomial's sign
    # pattern: dividing the lattice values by q(phi n) drives the zeta family
    # to near-positivity AND tightness (dressed 2.6: 0.598 -> 0.0002; dressed
    # sqrt13: 0.283 -> 0.0005; r95 51.4 -> 7.3) while D-H (no ghosts, quotient
    # trivial) stays at 0.05-0.12 and BEUR at 0.24-0.39. So measure-face
    # positivity is gauge-relative, and in this gauge it is family-SEPARATING
    # (an output-level separator, not an input-typed gate). Caveats, priced:
    # the gauge is FE-gated (unposable for the fake in principle, trivial for
    # it in practice: no ghosts), the un-normalized mass collapses on the
    # deep-dressed branch (sum|aq| spans ~2.9 down to ~0.002, so Helly without
    # renormalization can hit the zero measure), and the D-H sequence
    # decreases along the grid, so the separation is in-sample, not a limit
    # statement. Handed-forward item 2 answered: the Helly positivity clause
    # DOES revive, in exactly the branch-sensitive FE-gated step.
    fq_z = {k: rows[k]["fneg_q"] for k in rows if k[0] == "ZETA"}
    rq_z = {k: rows[k]["r95q"] for k in rows if k[0] == "ZETA"}
    fq_d = [rows[k]["fneg_q"] for k in rows if k[0] == "D-H"]
    fq_b = [rows[k]["fneg_q"] for k in rows if k[0] == "BEUR"]
    check("T1f [ADVERSARY] FE-gated ghost-quotient gauge: ZETA measure face "
          "near-positive AND tight family-wide (fneg_q < 0.03, r95_q < 12.5, "
          "dressed branches the cleanest) while D-H >= 0.04 and BEUR >= 0.20: "
          "the dressed alternation is ghost dressing, not structure; positivity "
          "is gauge-relative and family-separating in this gauge (re-scopes T1e)",
          all(v < 0.03 for v in fq_z.values()) and all(v < 12.5 for v in rq_z.values())
          and all(v >= 0.04 for v in fq_d) and all(v >= 0.20 for v in fq_b),
          f"fneg_q zeta {[round(v, 4) for v in fq_z.values()]}, D-H "
          f"{[round(v, 3) for v in fq_d]}, BEUR {[round(v, 3) for v in fq_b]}")

    print("    => Q1 VERDICT (measured, ADVERSARY-scoped): the trojan's FUNCTION-face")
    print("       compactness dies at link (i) as pre-registered: (a) bounds the type")
    print("       but the limit is the CONSTANT (T1d); (b) removes dressing, not")
    print("       divergence (T1b). The MEASURE face is gauge-relative: raw gauges")
    print("       fail positivity (T1e) but the FE-gated quotient gauge revives it")
    print("       for zeta, family-separating in-sample (T1f). M4 still relocates")
    print("       into the normalization (which gauge, and its lambda-uniform")
    print("       control) rather than being removed.")
    return rows


# ==========================================================================
# T2 (Q2): class certification through identical code paths.
# ==========================================================================
def euler_gated_certificate(name, freqs, lamvals):
    """The #161 Q3 certificate shape. The nonnegative comb is consumed as an
    explicit HYPOTHESIS the code checks; if it fails, the certificate is
    UNPOSABLE and nothing downstream is computed (D-H must exit here, not
    return a different number). The lattice clause tests low-band frequency
    membership in {log m} (low band only: at height log n the integer-lattice
    spacing is ~1/n, so raw distance is meaningless for large n).

    [ADVERSARY note] The gate is a TYPE-level refusal: nothing downstream in
    THIS function consumes nonnegativity (gate-stripped, the signed D-H comb
    passes the lattice clause with disp exactly 0.0 and fails only the
    truncation-sensitive convergence clause, 0.098 vs the pinned 0.05; the
    |comb| rearrangement likewise fails only convergence). The genuine
    positivity CONSUMER the gate stands in for is e1n T5's Abel-summation
    one-sided upgrade, which is pin-side (#161). The UNPOSABLE verdict is
    honest as input typing, not as a downstream computation."""
    freqs = np.asarray(freqs, float)
    lamvals = np.asarray(lamvals, float)
    if float(np.min(lamvals)) < -1e-12:
        return dict(status="UNPOSABLE_EULER_GATE",
                    min_weight=float(np.min(lamvals)), certificate=None)
    # convergence clause at sigma = 1.5 (abscissa fuel): tail stabilization
    terms = lamvals * np.exp(-1.5 * freqs)
    order = np.argsort(freqs)
    s_sorted = np.cumsum(terms[order])
    s_full, s_half = float(s_sorted[-1]), float(s_sorted[len(s_sorted) // 2])
    conv = abs(s_full - s_half) / abs(s_full)
    # lattice membership clause, low band ell <= log 50
    low = freqs[freqs <= math.log(50.0)]
    logm = np.log(np.arange(1, 60, dtype=float))
    disp = float(np.mean([np.min(np.abs(logm - f)) for f in low])) if len(low) else 0.0
    status = "CERTIFIED" if (conv < 0.05 and disp < 1e-9) else \
        ("FAIL_LATTICE_CLAUSE" if disp >= 1e-9 else "FAIL_CONVERGENCE")
    return dict(status=status, min_weight=float(np.min(lamvals)),
                conv_defect=conv, lattice_disp=disp, certificate=(status == "CERTIFIED"))


def run_t2(results, rows, grid, quick):
    print("\n[T2/Q2] CLASS CERTIFICATION: HB reality, Euler gate, lattice fuel, D-H type")
    consume("T2", "xihat values on contours + grids (object data)",
            "sieved Lambda(n) (arithmetic input, no zeros)",
            "Beurling comb + generalized integers", "D-H L-VALUES (own/Riemann FE residuals)")

    # ---- T2a: HB in-class membership (zero reality in the strip), identical
    # code for all three. WHY band-shrink winding: a sign-change grid CAN miss
    # close real pairs inside one step, so the certificate must not rely on a
    # real-axis grid; comparing the strip count at band 0.4 with the count
    # at band 0.05 certifies every strip zero lies within 0.05 of the axis
    # (0.05 sits above e1k's documented ~1e-2 zeta ghost scale).
    # [ADVERSARY correction] the earlier "observed at ZETA 3.0: 13 zeros, 11
    # grid crossings" anecdote did NOT reproduce: both the plain phi/16 grid
    # and the e1m offset grid count 13 crossings (the close pair 40.86/41.03
    # has separation 0.178 > the phi/16 step 0.131, so it is resolved). The
    # instrument is kept for its in-principle robustness, not that anecdote.
    # Cross-branch note: the ZETA 3.0 strip count is dps-branch-dependent
    # (18/13/12 at dps 15/25/35), reality-certified at every branch, with no
    # zero at |Im| in (0.02, 0.05] at any branch. ----
    real_cert = {}
    reality_grid = [g for g in grid if not (quick and g[0] == "ZETA" and g[1] > 2.5)]
    for label, lam, N in reality_grid:
        xh, _ = get_build(label, lam, N)
        Twin = 2 * math.pi * lam * lam
        f = lambda z: complex(xh(np.array([z]))[0])
        w_wide, r1, _ = winding_count(
            f, [0.6 - 0.4j, Twin + 0.4 - 0.4j, Twin + 0.4 + 0.4j, 0.6 + 0.4j], n0=256)
        w_thin, r2, _ = winding_count(
            f, [0.6 - 0.05j, Twin + 0.4 - 0.05j, Twin + 0.4 + 0.05j, 0.6 + 0.05j], n0=256)
        ok = (r1 < 0.05) and (r2 < 0.05) and round(w_wide) == round(w_thin)
        real_cert[(label, lam)] = ok
        results[f"t2_real_{label.replace('-', '')}_{lam:.3f}"] = np.array([w_wide, w_thin])
        print(f"    {label:5s} lam={lam:.3f}: strip count {w_wide:.2f} vs |Im| <= 0.05 "
              f"count {w_thin:.2f} -> {'REAL' if ok else 'NOT REAL'}")
    eps_z = [rows[k]["eps"] for k in rows if k[0] == "ZETA"]
    eps_b = [rows[k]["eps"] for k in rows if k[0] == "BEUR"]
    check("T2a HB certification is FAMILY-BLIND: all strip zeros real for ZETA, D-H "
          "AND the fake, although the fake's Weil form is O(1)-INDEFINITE (eps ~ -1) "
          "while zeta sits at the +-1e-4 margin: reality is CF-manufactured, not "
          "positivity-sourced, and carries no arithmetic bits (#158 extended)",
          all(real_cert.values()) and max(abs(e) for e in eps_z) < 1e-3
          and max(eps_b) < -0.5,
          f"certified {sum(real_cert.values())}/{len(real_cert)}; eps_zeta max|.| "
          f"{max(abs(e) for e in eps_z):.1e}, eps_BEUR {max(eps_b):+.2f}")

    # ---- T2b: the Euler-gated certificate (#161 Q3 shape) ------------------
    lz, ld = streams()
    NM = 20000
    lam_arr = np.zeros(NM + 1)
    sieve = np.ones(NM + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(NM ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    for p in np.nonzero(sieve)[0]:
        pk = p
        while pk <= NM:
            lam_arr[pk] = math.log(p)
            pk *= p
    nz = np.nonzero(lam_arr)[0]
    cert_z = euler_gated_certificate("ZETA", np.log(nz.astype(float)), lam_arr[nz])
    dn = np.arange(2, 80)
    cert_d = euler_gated_certificate("D-H", np.log(dn.astype(float)),
                                     np.array([ld[n] for n in dn]))
    B = beurling()
    bf, bw = [], []
    for lb in B.logs:
        k = 1
        while k * lb <= math.log(NM):
            bf.append(k * lb)
            bw.append(lb)
            k += 1
    cert_b = euler_gated_certificate("BEUR", bf, bw)
    check("T2b Euler gate consumed as a checked hypothesis: ZETA CERTIFIED; D-H "
          "UNPOSABLE at the gate (sign-changing comb, nothing downstream computed); "
          "BEUR passes the gate, runs, and fails at the NAMED lattice clause",
          cert_z["status"] == "CERTIFIED" and cert_d["status"] == "UNPOSABLE_EULER_GATE"
          and cert_d["certificate"] is None and cert_b["status"] == "FAIL_LATTICE_CLAUSE"
          and cert_b["lattice_disp"] > 0.02,
          f"zeta disp {cert_z['lattice_disp']:.1e}, D-H min weight "
          f"{cert_d['min_weight']:+.3f}, BEUR low-band displacement "
          f"{cert_b['lattice_disp']:.3f}")
    results["t2_beur_disp"] = cert_b["lattice_disp"]
    results["t2_dh_minw"] = cert_d["min_weight"]

    # ---- T2c: limit-level lattice fuel (theta FE): the pin's engine --------
    with mp.workdps(35):
        th = lambda t: 1 + 2 * mp.nsum(lambda n: mp.e ** (-mp.pi * n * n * t), [1, 80])
        worst_z = max(float(abs(th(1 / mp.mpf(t)) - mp.sqrt(mp.mpf(t)) * th(mp.mpf(t))))
                      for t in ("0.7", "1.3", "2.0"))
    small = [lv for lv in B.gen_integers(40)]
    th_b = lambda u: 1 + 2 * sum(math.exp(-math.pi * math.exp(2 * lv) * u)
                                 for lv in small if lv > 0)
    worst_b = max(abs(th_b(1 / t) - math.sqrt(t) * th_b(t)) / th_b(1 / t)
                  for t in (0.7, 1.3, 2.0))
    check("T2c limit-level lattice fuel: Z theta FE exact (< 1e-25) vs fake defect "
          "O(1): link (iii)'s Poisson/theta engine is UNFUELED for the fake: the "
          "nameable failure sits at the pin, not in the compactness links",
          worst_z < 1e-25 and worst_b > 1e-3,
          f"Z defect {worst_z:.1e}, fake defect {worst_b:.2f}")
    results["t2_theta_z"] = worst_z
    results["t2_theta_beur"] = worst_b

    # ---- T2d: D-H's link-(iii) failure is TYPE (Riemann-FE data), and its
    # posability failure is the gate (T2b): two independent input-level exits.
    dh = _dhmod.davenport_heilbronn
    with mp.workdps(30):
        pts = (mp.mpc("0.3", 5), mp.mpc("0.7", 12), mp.mpc("1.5", 3))
        own = max(float(abs(dh.functional_equation_residual(s)) / abs(dh.evaluate(s)))
                  for s in pts)
        rie = min(float(abs(dh.evaluate(s) - chi_riemann(s) * dh.evaluate(1 - s))
                        / abs(dh.evaluate(s))) for s in pts)
    check("T2d D-H exits link (iii) by TYPE: own conductor-5 FE exact (< 1e-20) but "
          "Riemann-type FE fails at O(1): the pin's H1 data excludes it (e1m T2 re-verified)",
          own < 1e-20 and rie > 0.1, f"own {own:.1e}, Riemann-type defect {rie:.2f}")
    results["t2_dh_own_fe"] = own
    results["t2_dh_rie_fe"] = rie

    # ---- T2e: the certified class MOVES (no fixed PW class), and the
    # 0-normalized strip bound is gauge-fragile exactly for the fake ---------
    strip = {}
    for label, lam, N in grid:
        xh, _ = get_build(label, lam, N)
        _, z0s = ghost_gate(label, xh)
        f0 = complex(xh(np.array([0j]))[0]) / complex(qpoly(np.array([0j]), z0s)[0])
        strip[(label, lam)] = float(np.max(np.abs(xh(ZSTRIP) / qpoly(ZSTRIP, z0s) / f0)))
        results[f"t2_strip_{label.replace('-', '')}_{lam:.3f}"] = strip[(label, lam)]
    zs = [v for k, v in strip.items() if k[0] in ("ZETA", "D-H")]
    bs = [v for k, v in strip.items() if k[0] == "BEUR"]
    cond_b = (max(bs) > 2.0) if not quick else (max(bs) < 2.0)
    detail_b = (f"BEUR max {max(bs):.2f} (2.6 instability: low zero near the "
                f"normalization point)" if not quick else
                f"BEUR 2.2 {max(bs):.2f} (instability appears at 2.6, full mode)")
    check("T2e substrip 0-normalized bound: flat ~1.00-1.05 for ZETA/D-H across the "
          "grid (in-sample local boundedness on substrips = the open growth clause, "
          "consistent) but GAUGE-FRAGILE for the fake: no certification component "
          "here either", all(0.95 < v < 1.10 for v in zs) and cond_b,
          f"ZETA/D-H in [{min(zs):.3f}, {max(zs):.3f}]; " + detail_b)
    print("    => Q2 VERDICT (measured): certification into the class succeeds for")
    print("       ALL THREE streams identically (reality, tail, type shape): the")
    print("       in-class certificate is information-free. The clauses that DO")
    print("       discriminate are input-typed gates (Euler nonnegativity, FE type,")
    print("       lattice membership/theta fuel) and they all belong to link (iii),")
    print("       the pin: not to compactness.")
    return strip


# ==========================================================================
# T3 (Q3): the determinacy surrogate, rate-free.
# ==========================================================================
def run_t3(results, rows, grid, quick):
    print("\n[T3/Q3] DETERMINACY SURROGATE: coefficients, moments, rate-free coincidence")
    consume("T3", "xihat values on fixed compacts (object data)",
            "Xi / Phi_DH truth VALUES (mp dps 30; diagnostics only, no zeros)")

    fam = {}
    for label, lam, N in grid:
        fam.setdefault(label, []).append(lam)
    for v in fam.values():
        v.sort()

    # normalized (b)-quotiented values on the compacts, per build
    FZZ, TAY, MR15, MR08 = {}, {}, {}, {}
    for label, lam, N in grid:
        xh, _ = get_build(label, lam, N)
        _, z0s = ghost_gate(label, xh)
        FZZ[(label, lam)] = xh(ZZ) / qpoly(ZZ, z0s)
        fc = xh(CIRC) / qpoly(CIRC, z0s)
        a0 = complex(np.mean(fc))
        TAY[(label, lam)] = [complex(np.mean(fc * np.exp(-1j * k * TH_CIRC))
                                     / R_TAYLOR ** k / a0) for k in (2, 4)]
        MR15[(label, lam)] = m_red(xh, z0s, ZC15)
        MR08[(label, lam)] = m_red(xh, z0s, ZC08)

    # ---- T3a: Taylor trajectories: input-faithful, non-convergent ----------
    a2 = {k: v[0].real for k, v in TAY.items()}
    for k, v in a2.items():
        results[f"t3_a2_{k[0].replace('-', '')}_{k[1]:.3f}"] = v
    with mp.workdps(30):
        XiC = truth_on("Xi", CIRC)
        PhC = truth_on("Phi", CIRC)
    a2_xi = float(np.real(np.mean(XiC * np.exp(-2j * TH_CIRC)) / R_TAYLOR ** 2
                          / np.mean(XiC)))
    a2_ph = float(np.real(np.mean(PhC * np.exp(-2j * TH_CIRC)) / R_TAYLOR ** 2
                          / np.mean(PhC)))
    az = [a2[k] for k in a2 if k[0] == "ZETA"]
    ad = [a2[k] for k in a2 if k[0] == "D-H"]
    ab = [a2[k] for k in a2 if k[0] == "BEUR"]
    sep = max(az) < min(ad) or min(az) > max(ad)
    faith = (abs(np.mean(az) - a2_xi) < abs(np.mean(az) - a2_ph)
             and abs(np.mean(ad) - a2_ph) < abs(np.mean(ad) - a2_xi))
    beur_wild = (max(ab) - min(ab) > 0.1) if len(ab) >= 2 else abs(ab[0]) > 0.1
    print(f"    a2: zeta {[round(x, 4) for x in az]} (Xi {a2_xi:+.4f}), "
          f"D-H {[round(x, 4) for x in ad]} (Phi {a2_ph:+.4f}), "
          f"BEUR {[round(x, 4) for x in ab]}")
    check("T3a Taylor trajectory a_2(lambda): family ranges DISJOINT and each family "
          "orbits its OWN truth (input-faithful) but with branch scatter straddling "
          "it (non-convergent in-sample); BEUR scatters at O(1) with no target",
          sep and faith and beur_wild,
          f"zeta in [{min(az):.4f}, {max(az):.4f}] vs Xi {a2_xi:.4f}; "
          f"D-H in [{min(ad):.4f}, {max(ad):.4f}] vs Phi {a2_ph:.4f}")
    results["t3_a2_xi_truth"] = a2_xi
    results["t3_a2_phi_truth"] = a2_ph

    # ---- T3b: rate-free Cauchy read on K = [0, 6] ---------------------------
    gaps = {}
    for label, lams in fam.items():
        gaps[label] = [projd(FZZ[(label, a)], FZZ[(label, b)])
                       for a, b in zip(lams, lams[1:])]
        results[f"t3_gaps_{label.replace('-', '')}"] = np.array(gaps[label])
        print(f"    consecutive projective gaps on [0,6], {label}: "
              f"{[round(g, 4) for g in gaps[label]]}")
    if not quick:
        z_not_cauchy = not all(a > b for a, b in zip(gaps["ZETA"], gaps["ZETA"][1:]))
        dh_coherent = max(gaps["D-H"]) < min(gaps["ZETA"])
        beur_o1 = min(gaps["BEUR"]) > 0.5
        cond = z_not_cauchy and dh_coherent and beur_o1
        detail = (f"zeta {[round(g, 3) for g in gaps['ZETA']]} not monotone; "
                  f"max D-H {max(gaps['D-H']):.3f} < min zeta {min(gaps['ZETA']):.3f}; "
                  f"min BEUR {min(gaps['BEUR']):.3f}")
    else:
        cond = 0.1 < gaps["ZETA"][0] < 0.6
        detail = f"quick: single zeta gap {gaps['ZETA'][0]:.3f} (>> the e1n 3e-2 line floor)"
    check("T3b coincidence NOT certified in-sample, and the surrogate is RH-BLIND: "
          "the zeta gaps are non-Cauchy (branch scatter) while the D-H family, whose "
          "TRUE limit is off-class at 85.7, is the MOST coherent of the three",
          cond, detail)

    # ---- T3c: truth-anchored floors (diagnostic): branch-selected, not
    # lambda-monotone (the e1n dressing-migration finding on the compact face)
    XiZZ = truth_on("Xi", ZZ)
    PhZZ = truth_on("Phi", ZZ)
    dz = {lam: projd(FZZ[("ZETA", lam)], XiZZ) for lam in fam["ZETA"]}
    results["t3_dist_xi"] = np.array([dz[lam] for lam in fam["ZETA"]])
    print(f"    zeta -> Xi distances: {[round(dz[lam], 4) for lam in fam['ZETA']]}")
    if "D-H" in fam:
        dd = {lam: projd(FZZ[("D-H", lam)], PhZZ) for lam in fam["D-H"]}
        dx = {lam: projd(FZZ[("D-H", lam)], XiZZ) for lam in fam["D-H"]}
        results["t3_dh_dist_phi"] = np.array([dd[lam] for lam in fam["D-H"]])
        print(f"    D-H -> Phi: {[round(dd[lam], 4) for lam in fam['D-H']]}, "
              f"-> Xi (cross): {[round(dx[lam], 4) for lam in fam['D-H']]}")
        faith_dh = all(dx[lam] > 3 * dd[lam] for lam in fam["D-H"])
    else:
        faith_dh = True
    best = min(dz, key=dz.get)
    dressed = [k[1] for k in rows if k[0] == "ZETA" and rows[k]["nghost"] > 0]
    check("T3c convergence is BRANCH-SELECTED, not lambda-monotone: the closest-to-Xi "
          "zeta build is a DRESSED branch (ghost-quotiented), not the largest lambda; "
          "D-H stays 3x+ closer to its own Phi than to Xi (input-faithful)",
          (best in dressed) and (quick or best != max(fam["ZETA"])) and faith_dh,
          f"argmin d(., Xi) = lam {best:.2f} (dressed: {sorted(dressed)}), "
          f"largest lam {max(fam['ZETA']):.2f}")

    # ---- T3d: Carleman/moment uniformity read on the measure face ----------
    R6 = {}
    for label, lam, N in grid:
        xh, _ = get_build(label, lam, N)
        c = np.abs(np.real(xh.coef))
        x = xh.phi * xh.idx
        R6[(label, lam)] = float((np.sum(c * x ** 12) / np.sum(c)) ** (1.0 / 12))
        results[f"t3_R6_{label.replace('-', '')}_{lam:.3f}"] = R6[(label, lam)]
    ratio = {k: R6[k] / rows[k]["phiN"] for k in R6}
    print(f"    R6 radii: " + ", ".join(f"{k[0]} {k[1]:.2f}: {v:.1f} ({ratio[k]:.2f} x phiN)"
                                        for k, v in R6.items()))
    if not quick:
        growth = {label: R6[(label, lams[-1])] / R6[(label, lams[0])]
                  for label, lams in fam.items()}
        cond = (all(g > 1.4 for g in growth.values())
                and max(ratio.values()) / min(ratio.values()) > 1.5)
        detail = ("within-family R6 growth " +
                  ", ".join(f"{lab} {g:.2f}x" for lab, g in growth.items()) +
                  f"; R6/phiN spread {min(ratio.values()):.2f}..{max(ratio.values()):.2f}")
    else:
        cond = max(ratio.values()) / min(ratio.values()) > 1.3
        detail = f"quick: R6/phiN spread {min(ratio.values()):.2f}..{max(ratio.values()):.2f}"
    check("T3d moment radii TRACK THE WINDOW: R6 grows ~ with phiN inside every "
          "family and R6/phiN has no family-uniform profile: each finite object is "
          "trivially determinate but NO lambda-uniform Carleman bound is certified",
          cond, detail)

    # ---- T3e: canonical-system germ read (surveyor fold-in) ----------------
    mgap15, mgap08 = {}, {}
    for label, lams in fam.items():
        mgap15[label] = [float(np.max(np.abs(MR15[(label, a)] - MR15[(label, b)])))
                         for a, b in zip(lams, lams[1:])]
        mgap08[label] = [float(np.max(np.abs(MR08[(label, a)] - MR08[(label, b)])))
                         for a, b in zip(lams, lams[1:])]
        results[f"t3_mgap15_{label.replace('-', '')}"] = np.array(mgap15[label])
        print(f"    m_red gaps {label}: Im=1.5 {[round(g, 3) for g in mgap15[label]]}, "
              f"Im=0.8 {[round(g, 3) for g in mgap08[label]]}")
    escs = {label: [rows[(label, lam)]["esc"] for lam in lams]
            for label, lams in fam.items()}
    if not quick:
        no_improve = (mgap15["ZETA"][-1] > 0.8 * mgap15["ZETA"][0]
                      and all(g > 0.3 for g in mgap15["ZETA"]))
        ordering = (np.mean(mgap15["D-H"]) < np.mean(mgap15["ZETA"])
                    < np.mean(mgap15["BEUR"]))
        esc_cond = (max(escs["D-H"]) < 0.10
                    and any(e > 0.5 for e in escs["ZETA"])
                    and min(e for k, e in
                            [((l), rows[("ZETA", l)]["esc"]) for l in fam["ZETA"]
                             if rows[("ZETA", l)]["nghost"] == 0]) < 0.05
                    and max(escs["BEUR"]) > 0.3)
        cond = no_improve and ordering and esc_cond
        detail = (f"zeta m-gaps flat at ~{np.mean(mgap15['ZETA']):.2f} (scale ~1); "
                  f"esc: D-H max {max(escs['D-H']):.3f}, zeta clean/dressed "
                  f"{min(escs['ZETA']):.3f}/{max(escs['ZETA']):.3f}, BEUR max "
                  f"{max(escs['BEUR']):.2f}")
    else:
        cond = (0.3 < mgap15["ZETA"][0] < 1.0 and rows[("ZETA", 2.2)]["esc"] < 0.05
                and rows[("ZETA", 2.6)]["esc"] > 0.3
                and rows[("D-H", 2.6)]["esc"] < 0.10
                and rows[("BEUR", 2.2)]["esc"] > 0.2)
        detail = (f"quick: zeta m-gap {mgap15['ZETA'][0]:.3f}, esc z2.2 "
                  f"{rows[('ZETA', 2.2)]['esc']:.3f} / z2.6 {rows[('ZETA', 2.6)]['esc']:.3f}")
    check("T3e canonical-germ read (surveyor fold-in): the type-subtracted m-proxy "
          "is NO more Cauchy than the function face (zero-microstructure-bound, "
          "D-H again most coherent) and the no-mass-escape clause is branch-"
          "dominated + RH-blind (D-H cleanest, zeta dressed escapes, BEUR erratic): "
          "the canonical-system route stays deferred to the chain level (e1u)",
          cond, detail)
    print("    => Q3 VERDICT (measured): per-object determinacy is trivial; the")
    print("       lambda-UNIFORM inputs (tight moments, Cauchy trend, stable germ)")
    print("       are all absent in-sample, and every absence is branch-dominated")
    print("       or RH-blind: link (ii) relocates the uniformity joint, unchanged.")
    return gaps


# ==========================================================================
# T4 (Q4): kill tests.
# ==========================================================================
def run_t4(results, rows, grid, guards, quick):
    print("\n[T4/Q4] KILL TESTS: DMV screen, K1 audit, relocation accounting")

    # ---- T4a: the DMV screen on the certification vector -------------------
    # components: (reality certified, tail exactness, type ratio, collapse
    # direction). Excluded BY DESIGN: eps (density-level), strip gauge (T2e),
    # a2 scatter (Q3 diagnostics): those are either density data or gauge.
    consume("T4", "certification vector components measured in T1/T2")
    tz = rows[("ZETA", 2.2)]["tau"] / math.log(2.2)
    tb = rows[("BEUR", 2.2)]["tau"] / math.log(2.2)
    comp_type = abs(tz - tb) < 0.10
    comp_tail = rows[("ZETA", 2.2)]["tail"] < 1e-12 and rows[("BEUR", 2.2)]["tail"] < 1e-12
    if not quick:
        bl = sorted(k[1] for k in rows if k[0] == "BEUR")
        be_seq = [rows[("BEUR", l)]["supG1"] for l in bl]
        comp_collapse = (rows[("ZETA", 3.0)]["supG1"] < rows[("ZETA", 2.2)]["supG1"]
                         and all(a > b for a, b in zip(be_seq, be_seq[1:])))
    else:
        comp_collapse = True
    screen_fired = comp_type and comp_tail and comp_collapse
    check("T4a DMV SCREEN FIRED: the compactness-certification vector (reality, "
          "tail, type shape, collapse direction) is INDISTINGUISHABLE between zeta "
          "and the density-matched fake: links (i)-(ii) consume only density/"
          "growth data and are structurally non-discriminating; discrimination "
          "in THIS vector sits in the input-typed gates of link (iii) (the one "
          "measured output-level exception is the T1f gauge-positivity face, "
          "excluded here as gauge-relative and in-sample-trending)",
          screen_fired,
          f"|type ratio diff| = {abs(tz - tb):.3f}, tails < 1e-12 both, collapse "
          f"monotone both")
    results["t4_screen_fired"] = screen_fired

    # ---- T4b: K1 audit ------------------------------------------------------
    src = Path(__file__).read_text(encoding="utf-8")
    forbidden = ["zeta" + "zero", "ZETA_" + "ZEROS", "DH_" + "ZEROS", ".zeros" + "("]
    # numpy array allocation is not zero DATA; the token scan targets the
    # L-function zero scanners (mp.zetazero, LFunction .zeros methods, lists)
    scan = [ln.replace("np." + "zeros(", "np_alloc(") for ln in src.splitlines()
            if not ln.strip().startswith("#") and "K1-ALLOW" not in ln]
    hits = [tok for tok in forbidden if any(tok in ln for ln in scan)]
    check("T4b K1 audit: no zero-list access in any path (source scan clean, runtime "
          "guards installed and never tripped)",
          not hits and guards["installed"] and not guards["tripped"],
          f"forbidden tokens: {hits}" if hits else "clean")
    print("    input ledger (what each test consumed):")
    for test in sorted(LEDGER):
        for item in LEDGER[test]:
            print(f"      {test}: {item}")

    # ---- T4c: relocation accounting + overclaim tripwire --------------------
    links = {
        "i_compactness": dict(
            certified_with_content=False,
            relocation="type divergence kills fixed-class Montel (T1a/T1b); the "
                       "type-rescale is compact but collapses to the constant "
                       "(T1d): content -> control of tau_lambda = the #160 growth "
                       "clause; measure-face positivity/tightness branch-fragile "
                       "(T1e/T3e)"),
        "ii_determinacy": dict(
            certified_with_content=False,
            relocation="window-tracking moment radii (T3d) + non-Cauchy branch "
                       "scatter (T3b) + RH-blind coherence ordering (D-H most "
                       "coherent): the lambda-uniformity joint, unchanged"),
        "iii_pin": dict(
            certified_with_content=False,
            relocation="the pin is lattice-consuming (T2c theta fuel; T2b lattice "
                       "clause; T2d FE type) and by #160 its open clause is "
                       "conditionally EQUIVALENT to the identification = M4 "
                       "(given the limit + growth package, per e1m)"),
    }
    # the tripwire: if every link were certified with arithmetic content the
    # trojan would have proven Section 7 => RH, which a finite probe cannot:
    # any such state is a K1 alarm, not a success.
    all_free = all(v["certified_with_content"] for v in links.values())
    if all_free:
        raise RuntimeError("K1 tripwire: all trojan links reported certified")
    check("T4c relocation accounting consistent + overclaim tripwire armed: no link "
          "is certified-with-arithmetic-content; each carries a named relocation "
          "site and all three point at the same uniformity/lattice joint (= M4)",
          not all_free and all(v["relocation"] for v in links.values()),
          "links i/ii/iii all relocate, none removed")
    print("    RELOCATION TABLE (the honest outcome of the trade):")
    for name, v in links.items():
        print(f"      link ({name}): {v['relocation']}")
    return links


# ==========================================================================
# main
# ==========================================================================
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true",
                    help="cached builds only + one cheap BEUR build; NO npz output")
    args = ap.parse_args()
    t_start = time.time()
    mp.mp.dps = 25   # e1l/e1m-characterized build regime; truth values raise locally

    # K1 runtime guards: any zero-list access in this process raises.
    guards = {"installed": True, "tripped": False}

    def _forbid(*a, **k):
        guards["tripped"] = True
        raise RuntimeError("K1 guard: zero-list access attempted")
    mp.zetazero = _forbid                            # K1-ALLOW (guard install)
    _dhmod.davenport_heilbronn.zeros = _forbid       # K1-ALLOW (guard install)

    if args.quick:
        grid = [("ZETA", 2.2, 12), ("ZETA", 2.6, 16),
                ("D-H", 2.6, 16), ("BEUR", 2.2, 12)]
    else:
        grid = [("ZETA", 2.2, 12), ("ZETA", 2.6, 16), ("ZETA", 3.0, 32),
                ("ZETA", SQRT13, 48),
                ("D-H", 2.2, 12), ("D-H", 2.6, 16), ("D-H", 3.0, 32),
                ("D-H", SQRT13, 48),
                ("BEUR", 2.2, 12), ("BEUR", 2.6, 16), ("BEUR", 3.0, 32)]

    results = {}
    print("=" * 78)
    print("E1T: the compactness trojan at the CCM D_log family (can the uniform")
    print("     det-class limit be traded for compactness + determinacy + pin?)")
    print("=" * 78)

    run_t0(results, args.quick)
    rows = run_t1(results, grid, args.quick)
    run_t2(results, rows, grid, args.quick)
    run_t3(results, rows, grid, args.quick)
    run_t4(results, rows, grid, guards, args.quick)

    print("\n" + "=" * 78)
    print("VERDICT (tiered; details and honest statement in e1t_compact_class_limit.md)")
    print("  trojan_trades_M4_away = NO (split verdict, all three links measured):")
    print("  link (i) compactness: type divergence confirmed family-wide (T1a/T1b);")
    print("    the one type-bounding normalization collapses the limit to the")
    print("    constant for zeta, D-H AND the fake (T1d): compactness is free")
    print("    exactly where it is information-free; the measure face fails")
    print("    positivity in the raw gauges (T1e) and revives, family-separating,")
    print("    in the FE-gated quotient gauge (T1f, ADVERSARY): the gauge choice")
    print("    itself is the relocated content.")
    print("  link (ii) determinacy: no in-sample Cauchy trend (branch scatter),")
    print("    window-tracking moment radii, and the RH-false D-H twin is the")
    print("    MOST coherent family on the function/germ faces (T3b/T3d/T3e);")
    print("    the eps and gauge-positivity faces order zeta first (ADVERSARY),")
    print("    so the blindness claim is face-scoped, and no face certifies")
    print("    coincidence.")
    print("  link (iii) pin: the input-typed gates live here (Euler nonnegativity:")
    print("    D-H unposable; integer-lattice/theta fuel: the fake fails nameably;")
    print("    FE type: D-H excluded), and by #160 the pin's open clause is")
    print("    conditionally EQUIVALENT to the identification = M4 (given the")
    print("    limit + growth package).")
    print("  net: the trojan RELOCATES M4 (into the rescaling gauge tau_lambda,")
    print("    the uniformity joint, and the pin's lattice clause); it does not")
    print("    remove it. The negative is a coordinate: any compactness-based")
    print("    route must make its NORMALIZATION carry the arithmetic, or it")
    print("    certifies nothing.")
    print("=" * 78)

    n_ok = sum(1 for _, ok in CHECKS if ok)
    print(f"\nSELF-TEST: {n_ok}/{len(CHECKS)} passed")
    for name, ok in CHECKS:
        if not ok:
            print(f"  FAILED: {name}")

    if not args.quick:
        np.savez_compressed(OUT, **{k: v for k, v in results.items()})
        print(f"Saved -> {OUT}")
    else:
        print("(quick mode: no npz saved)")
    print(f"Total time {round(time.time() - t_start, 1)}s")
    if n_ok != len(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
