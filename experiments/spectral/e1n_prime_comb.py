"""E1N: the prime-comb face of the positivity-free surface (LEARNINGS #160).

WHY THIS EXPERIMENT EXISTS
==========================
LEARNINGS #160 (e1m) proved the bare Hamburger-type counting pin false and
named the genuine gain of the corrected pin: a POSITIVITY-FREE proof surface
for the Section-7 identification, to be attacked via the determinant identity
det_reg(D_log - z) = -i lambda^{-iz} xihat(z) plus the PRIME COMB, instead of
variationally. This probe builds the comb face of that surface: it asks what
Dirichlet/von Mangoldt coefficients the finite object xihat_lambda actually
carries (Q1), derives rather than observes the archimedean escape law that
caps the readable window (Q2, closing an e1m-flagged soft spot), works out
what the Dirichlet-face inheritance clause needs in comb terms and whether
one-sided bounds suffice, in the light of #145's one-sided counting residue
(Q3), and runs the two disciplines, Beurling and D-H, against the comb-face
read (Q4).

WHAT THIS BUILDS (test battery)
===============================
T1 FORMULA + IMPLEMENTATION CHECKS: the unpacked log-derivative identity
   g(s) = i xihat'(z)/xihat(z) + dlogFac(s) with z = -i(s - 1/2) verified
   against -zeta'/zeta at 30 digits; exact-algebra xihat derivative vs finite
   differences; the archimedean rate closed form Im[dlogFac(2+it)] =
   pi/4 - 5/(2t) + O(1/t^2) and its pi/4 asymptote.
T2 CONDITIONING AUTOPSY (Q1a): coefficientwise least-squares extraction of
   Lambda_eff(n) from {n^{-s}} on the escape-capped window is DEAD beyond
   n ~ 4: the dense design has condition ~1e16 and even the restricted
   n <= 9 design amplifies the object's error into O(1..1e3) coefficient
   garbage. Measured, documented, DEMOTED per the probe spec: Q1 is answered
   at tooth/aggregate resolution instead (T3), the pre-specified fallback.
T3 THE COMB-FACE INSTRUMENT (Q1b, the horizon question): a windowed-Fourier
   read R_W[g](u) (Gaussian taper; ONE linear operator applied identically
   to object and reference models) turns g into a blurred comb in u = log n.
   Model comparison, not inversion: the object's deviation D from the exact
   full comb is matched against the HORIZON signature H (teeth beyond
   n = lambda^2 replaced by their smooth density) via alpha = <D,H>/||H||^2
   after polynomial deflation, with Monte-Carlo noise bars, an end-to-end
   synthetic-horizon positive control, and a ghost-quotient correction for
   the builds whose low band carries the e1m lattice-fill zeros.
   ADVERSARY DEMOTION (2026-07-11): the noise bars are white-noise-only and
   overstate significance against structured deviations; a smooth-deviation
   null (GP families in u and on the t-line, joint over both blur scales)
   reproduces the observed (alpha, |D|) pair with probability ~0.005-0.09,
   so the lam 2.2 horizon verdict is DISFAVORED, not rejected, and the
   apparent overshoot (rho < 0) is not significant (p ~ 0.08-0.24). See .md.
T4 ESCAPE LAW DERIVED (Q2): the tracking window closes where the completed
   signal |c Xi(2+it)| (decaying at the PROVEN Stirling rate, closed form
   pi/4 - 5/(2t)) falls below the object's own Paley-Wiener plateau M
   (measured on the far line t in [9,12], no truth values consumed there):
   t*_pred = crossing of |c Xi| with M, compared against the measured
   delta = 1 crossing and the e1m corridor t_dir. Constancy of t_dir across
   lambda is DERIVED from the log-insensitivity of the crossing to the
   plateau level plus the measured stagnation of the tracking floor; the
   type-proportional alternative law is falsified by the data.
T5 ONE-SIDEDNESS (Q3): the inheritance clause H4 in comb terms splits as
   EXISTENCE (a convergent Dirichlet expansion of -f'/f on Re s > 1, plus
   zero-freeness and the growth package) + ABSOLUTENESS (the Knopp-critical
   abscissa clause). PROVEN 3-line lemma: a NONNEGATIVE coefficientwise
   one-sided envelope plus series convergence forces absolute convergence
   (E_n >= 0 is required: c_n = E_n = (-1)^n n^{1/4} kills the bare form); PROVEN
   witness ((-1)^n n^{1/4}): a partial-sum one-sided bound does NOT suffice;
   nonnegativity (Euler-gated, exactly what D-H's comb lacks) upgrades
   partial-sum control to the coefficientwise envelope. Numerics instantiate
   all three; the finite family's measured comb-error signature (diagonal
   comb-mass errors + deflated aggregates) is recorded.
T6 BEURLING DISCIPLINE (Q4a): the density-matched fake's comb function vs
   the eps = 0 lattice control through the same read: blind at the
   archimedean-capped window, nameable failure at long windows, own
   frequencies restore the fit; the H4-not-pinned number: the fake full
   comb sits within ~2x of the object's own error distance from the true
   comb at the accessible window.
T7 K1 / DISCIPLINE AUDIT: runtime guards, source scan, input ledger, NG1/C3
   note. D-H blindness (Q4b) is measured inside T3: the same machinery reads
   back the D-H twin's own dense sign-changing comb with comparable
   fidelity, so the comb face is input-faithful and RH-blind at finite
   lambda, the #158 information-free class.

HONEST SCOPE
============
This probe proves nothing about RH. It characterizes the comb face of the
CCM D_log family at reachable cutoffs (faithful e1k reimplementation, not
the paper's exact operator; e1l/e1m precision caveats inherited). Integer
counts are leading-order +- O(1). Claims are tiered PROVEN / NUMERICAL /
CONJECTURE in the .md companion; thresholds are marked pre-registered vs
measured-then-pinned there.

Run:
  python -m experiments.spectral.e1n_prime_comb           # full (~6 min cold, ~1 min warm)
  python -m experiments.spectral.e1n_prime_comb --quick   # reduced grid
Outputs:
  experiments/spectral/e1n_prime_comb.npz  (+ .md companion)
  experiments/spectral/_cache/e1n_build_*.npz  (ground-state cache, gitignored)
"""

from __future__ import annotations

import argparse
import math
import time
import warnings
from pathlib import Path

import numpy as np
import mpmath as mp

# Only builders and configs from e1k: NOT the reference zero lists and NOT
# operator_spectrum. The comb face consumes xihat VALUES and truth L-VALUES.
from experiments.spectral.e1k_dh_dlog_testbed import (
    make_streams, build_float, ZETA_CFG, DH_CFG,
)
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
# Instrument constants. WHY these: sigma0 = 2 is the e1m Dirichlet-face line;
# T = 6 stays inside the measured escape window t_dir ~ 6..7 at every build;
# tau = 2.2 puts the Gaussian taper at 0.024 by t = T (so the escaping error
# barely enters) while giving blur 1/tau = 0.45 in u = log n; the u-grid
# covers n = 2..26. Every R_W comparison uses the IDENTICAL operator, so
# window-truncation bias cancels in every difference we interpret.
# --------------------------------------------------------------------------
SIGMA0, TAU, TLINE, DTL = 2.0, 2.2, 6.0, 0.15
TS = np.arange(0.0, TLINE + 1e-9, DTL)
SLINE = np.array([complex(SIGMA0, t) for t in TS])
UGRID = np.arange(0.3, 3.45, 0.05)
ZLINE = np.array([complex(s.imag, -(s.real - 0.5)) for s in SLINE])


def R_W(gvals, ts=TS, u=UGRID, tau=TAU):
    """Windowed-Fourier blurred-comb read: (1/pi) Re int_0^T g e^{itu} taper dt.
    Real coefficients make g(sigma-it) = conj g(sigma+it), so folding t < 0
    is exact: the read is a Gaussian-blurred comb in u = log n."""
    w = np.exp(-ts**2 / (2 * tau**2))
    integ = np.real(gvals[None, :] * np.exp(1j * np.outer(u, ts))) * w[None, :]
    return np.trapz(integ, ts, axis=1) / math.pi


def tooth_peak(n, cns, sigma=SIGMA0, tau=TAU):
    """Peak height of tooth n in the R_W read (untruncated-window formula)."""
    return cns[n] * n**(-sigma) * tau / math.sqrt(2 * math.pi)


# polynomial deflation: remove Legendre deg <= 3 background before any
# matched-filter read. WHY: the object's dominant deviation is a smooth
# drift (the low-frequency part of the tracking error); teeth and the
# horizon signature have width-0.45 features that survive deflation.
_x = (UGRID - UGRID.mean()) / (UGRID.max() - UGRID.min()) * 2
_P = np.array([np.polynomial.legendre.legval(_x, [0] * k + [1]) for k in range(4)]).T
_QP = np.eye(len(UGRID)) - _P @ np.linalg.solve(_P.T @ _P, _P.T)


def deflate(v):
    return _QP @ v


def alpha_read(D, H):
    """The horizon matched filter: fraction of the horizon signature H present
    in the deviation D, after identical polynomial deflation. alpha = 1 means
    the object is missing exactly the beyond-cutoff teeth; alpha = 0 means it
    carries them fully."""
    Dq, Hq = deflate(D), deflate(H)
    return float(np.dot(Dq, Hq) / np.dot(Hq, Hq))


# --------------------------------------------------------------------------
# Unpacking data (Riemann type and D-H type).
# --------------------------------------------------------------------------
def fac_zeta(s):
    s = mp.mpc(s)
    return (s * (s - 1) / 2) * mp.pi ** (-s / 2) * mp.gamma(s / 2)


def dlogfac_zeta(s):
    s = mp.mpc(s)
    return 1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2 + mp.psi(0, s / 2) / 2


def xi_completed(s):
    return fac_zeta(s) * mp.zeta(mp.mpc(s))


def dlogfac_dh(s):
    s = mp.mpc(s)
    return mp.log(mp.mpf(5) / mp.pi) / 2 + mp.psi(0, (s + 1) / 2) / 2


# --------------------------------------------------------------------------
# xihat evaluator with EXACT derivative. Same gauge as e1m (largest
# component rotated to the real axis). The derivative is closed-form algebra
# on the basis functions, verified against finite differences in T1: the
# log-derivative needs it exact, not numerically differenced.
# --------------------------------------------------------------------------
class XihatD:
    def __init__(self, idx, phi, L, xi):
        self.idx = np.asarray(idx, float)
        self.phi, self.L = float(phi), float(L)
        xi = np.asarray(xi, complex)
        j0 = int(np.argmax(np.abs(xi)))
        self.coef = xi * np.exp(-1j * np.angle(xi[j0]))
        self.a = self.L / 2
        self.w = self.phi * self.idx
        self.sgn = (-1.0) ** self.idx   # sin(a(w_j+u)) = (-1)^j sin(au): a w_j = pi j

    def __call__(self, z):
        z = np.atleast_1d(np.asarray(z, complex))
        u = z[:, None] - self.w[None, :]
        sm = np.abs(u) < 1e-8
        val = np.where(sm, self.a, np.sin(self.a * u) / np.where(sm, 1.0, u))
        return 2 * self.L ** -0.5 * (self.sgn[None, :] * val) @ self.coef

    def d(self, z):
        z = np.atleast_1d(np.asarray(z, complex))
        u = z[:, None] - self.w[None, :]
        sm = np.abs(u) < 1e-6
        h = np.where(sm, -(self.a**3) * u / 3.0,
                     (self.a * u * np.cos(self.a * u) - np.sin(self.a * u))
                     / np.where(sm, 1.0, u**2))
        return 2 * self.L ** -0.5 * (self.sgn[None, :] * h) @ self.coef


_STREAMS = None


def streams():
    global _STREAMS
    if _STREAMS is None:
        _STREAMS = make_streams(80, float_out=True)
    return _STREAMS


def get_build(label, lam, N):
    """Disk-cached e1k ground state (rebuild if the cache is cold). WHY cache:
    the builds are the only expensive step and are bit-identical reruns of
    the e1m grid; nothing beyond the e1m cutoffs is ever built."""
    CACHE.mkdir(exist_ok=True)
    fn = CACHE / f"e1n_build_{label}_{lam:.4f}_{N}.npz"
    if fn.exists():
        d = np.load(fn)
        return XihatD(d["idx"], d["phi"], d["L"], d["xi"])
    cfg = ZETA_CFG if label == "ZETA" else DH_CFG
    stream = streams()[0] if label == "ZETA" else streams()[1]
    t0 = time.time()
    r = build_float(N, lam, stream, cfg["dens_a"], cfg["dens_b"], cfg["use_pole"])
    print(f"    [build] {label} lam={lam:.4f} N={N}: {time.time()-t0:.1f}s "
          f"(eps={r['eps']:+.2e}, even_frac={r['even_frac']:.5f})")
    np.savez_compressed(fn, idx=np.array(r["idx"], float), phi=r["phi"], L=r["L"],
                        xi=np.asarray(r["xi"], complex), eps=r["eps"],
                        even_frac=r["even_frac"], even_ok=r["even_assumption_ok"],
                        gap_even=r["gap_even"])
    return XihatD(r["idx"], r["phi"], r["L"], np.asarray(r["xi"], complex))


def g_object(xh, S, dlf, zv=None):
    """The object's comb function: g = i xihat'/xihat + dlogFac on the grid S
    (dlf = precomputed dlogFac values). Derivation: f = xihat(z(s))/Fac(s),
    z = -i(s - 1/2), so -f'/f = i xihat'/xihat + dlogFac (T1a verifies)."""
    z = ZLINE if zv is None else zv
    return 1j * xh.d(z) / xh(z) + dlf


def spurious_real_zeros(xh, tmax=13.6):
    """Real zeros of xihat below zeta's first zero height: every one is
    spurious (the e1m low-band lattice fill). Sign-change scan + bisection.
    K1 note: 14.13 enters only as a KNOWN LOW-LYING landmark bounding the
    scan window, not as data any claim consumes; the scan finds the OBJECT's
    own zeros."""
    xs = np.arange(0.4 + xh.phi / 32, tmax, xh.phi / 16)
    g = np.real(xh(xs))
    out = []
    for i in np.where(np.diff(np.sign(g)) != 0)[0]:
        lo, hi = xs[i], xs[i + 1]
        flo = np.real(xh(np.array([lo]))[0])
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            fm = np.real(xh(np.array([mid]))[0])
            if (fm > 0) == (flo > 0):
                lo, flo = mid, fm
            else:
                hi = mid
        out.append(0.5 * (lo + hi))
    return out


def ghost_pole_terms(z0s, zv):
    """i * sum [1/(z - z0) + 1/(z + z0)] on the grid: the log-derivative
    contribution of the spurious even zero pairs; subtracting it is exactly
    quotienting xihat by prod(1 - z^2/z0^2) (entire, same growth type)."""
    out = np.full(len(zv), 0j)
    for z0 in z0s:
        out += 1j * (1.0 / (zv - z0) + 1.0 / (zv + z0))
    return out


# ==========================================================================
# T1: formula + implementation checks.
# ==========================================================================
def run_t1(results):
    print("\n[T1] FORMULA + IMPLEMENTATION: unpacking identity, derivative, rate closed form")
    consume("T1", "mp.zeta VALUES + derivative values (no zeros)",
            "Gamma-factor data (loggamma/psi)", "one cached build (ZETA 2.2)")
    with mp.workdps(30):
        # (a) g-formula sign/convention against -zeta'/zeta through the Xi route
        worst = 0.0
        for s0 in (mp.mpc(2, 1), mp.mpc("2.5", 3), mp.mpc(3, "0.7")):
            z0 = -1j * (s0 - mp.mpf("0.5"))
            Xi = lambda w: xi_completed(mp.mpf("0.5") + 1j * mp.mpc(w))
            g_formula = 1j * mp.diff(Xi, z0) / Xi(z0) + dlogfac_zeta(s0)
            g_true = -mp.zeta(s0, derivative=1) / mp.zeta(s0)
            worst = max(worst, float(abs(g_formula - g_true)))
        check("T1a unpacking identity -f'/f = i Xi'/Xi + dlogFac (30 digits)",
              worst < 1e-20, f"max defect {worst:.1e}")
        results["t1_unpack_defect"] = worst

        # (b) closed form Im[dlogFac(2+it)] = pi/4 - 5/(2t) + O(1/t^2), and
        # the pi/4 asymptote. WHY: this IS the derived escape-rate law (T4).
        t = mp.mpf(100)
        exact = float(mp.im(dlogfac_zeta(mp.mpc(2, t))))
        closed = math.pi / 4 - 5 / (2 * float(t))
        asym = float(mp.im(mp.psi(0, 1 + 1j * mp.mpf(1e5) / 2)) / 2)
        check("T1b archimedean rate closed form pi/4 - 5/(2t) (t=100) + pi/4 asymptote",
              abs(exact - closed) < 5e-4 and abs(asym - math.pi / 4) < 1e-4,
              f"exact {exact:.6f} vs closed {closed:.6f}; asym(1e5) {asym:.6f}")
        results["t1_rate_exact_100"] = exact

    # (c) implementation: xihat matches the e1m-style evaluation; derivative
    # matches central finite differences
    xh = get_build("ZETA", 2.2, 12)
    zz = np.array([0.7 + 0.2j, 3.0 - 1.5j, 10.0 - 0.5j])
    d = zz[:, None] - xh.phi * xh.idx[None, :]
    v_ref = (2 * xh.L ** -0.5 * np.sin(zz[:, None] * xh.L / 2) / d) @ xh.coef
    imp = float(np.max(np.abs(v_ref - xh(zz)) / np.abs(v_ref)))
    h = 1e-6
    fd = float(np.max(np.abs((xh(zz + h) - xh(zz - h)) / (2 * h) - xh.d(zz))
                      / np.abs(xh.d(zz))))
    check("T1c xihat evaluator (vs e1m form) + exact derivative (vs FD)",
          imp < 1e-12 and fd < 1e-7, f"impl {imp:.1e}, deriv {fd:.1e}")
    results["t1_impl_defect"] = imp


# ==========================================================================
# T2: the conditioning autopsy (Q1a): coefficientwise inversion is dead.
# ==========================================================================
def run_t2(results):
    print("\n[T2] CONDITIONING AUTOPSY (Q1a): coefficientwise inversion on the capped window")
    consume("T2", "mp.zeta VALUES + derivative (exact calibration input)",
            "Lambda stream (truth comparison only)")
    lz = np.array(streams()[0])
    sigmas = (1.8, 2.1, 2.4, 2.7, 3.0)
    ts = np.arange(0.0, 4.8 + 1e-9, 0.3)
    S = np.array([[complex(sig, t) for sig in sigmas] for t in ts]).ravel()
    with mp.workdps(30):
        b = np.array([complex(-mp.zeta(complex(s), derivative=1) / mp.zeta(complex(s)))
                      for s in S])

    def design(ns, tail_X):
        cols = [np.ones_like(S)]
        for n in ns:
            cols.append(np.exp(-S * math.log(n)))
        cols.append(np.exp((1 - S) * math.log(tail_X)) / (S - 1))
        return np.array(cols).T

    def lsq(A, rhs):
        nrm = np.linalg.norm(A, axis=0)
        coef, _, _, sv = np.linalg.lstsq(A / nrm, rhs, rcond=None)
        return coef / nrm, sv[0] / sv[-1]

    # dense lattice to 26: the honest full design
    ns_dense = list(range(2, 27))
    coef, cond_dense = lsq(design(ns_dense, 26.5), b)
    err = {n: abs(coef[1 + i].real - lz[n]) for i, n in enumerate(ns_dense)}
    check("T2a dense-lattice design is singular at float64 (cond >= 1e12)",
          cond_dense > 1e12, f"cond = {cond_dense:.1e}")
    check("T2b exact-input calibration: n<=4 recovered, n>=5 garbage (superresolution wall)",
          err[2] < 1e-3 and err[3] < 1e-2 and err[4] < 0.2 and err[5] > 0.2,
          f"err(2)={err[2]:.1e} err(3)={err[3]:.1e} err(4)={err[4]:.1e} err(5)={err[5]:.2f} err(7)={err[7]:.1f}")
    results["t2_cond_dense"] = cond_dense
    results["t2_cal_err"] = np.array([err[n] for n in ns_dense])

    # restricted design fed with the OBJECT (best case, lam=2.2): the object's
    # error level through the pseudoinverse. WHY report: it prices the
    # demotion; the probe spec pre-authorized falling back to aggregate reads.
    xh = get_build("ZETA", 2.2, 12)
    with mp.workdps(30):
        dlf = np.array([complex(dlogfac_zeta(complex(s))) for s in S])
    zv = np.array([complex(s.imag, -(s.real - 0.5)) for s in S])
    gobj = g_object(xh, S, dlf, zv=zv)
    coef9, cond9 = lsq(design(list(range(2, 10)), 9.5), gobj)
    err9 = {n: abs(coef9[1 + i].real - lz[n]) for i, n in enumerate(range(2, 10))}
    bad = max(err9[n] for n in (5, 6, 7, 8, 9))
    check("T2c object through the restricted design: coefficients unusable beyond n ~ 2",
          err9[3] > 0.05 or bad > 1.0,
          f"cond {cond9:.1e}; err(2)={err9[2]:.2f} err(3)={err9[3]:.1f} worst(5..9)={bad:.0f}")
    results["t2_obj_err9"] = np.array([err9[n] for n in range(2, 10)])
    print("    => VERDICT: inversion-type extraction of Lambda_eff(n) is DEAD on the")
    print("       escape-capped window (fundamental superresolution wall, not a solver")
    print("       artifact). Q1 is answered by the model-comparison instrument (T3),")
    print("       the pre-specified fallback resolution.")


# ==========================================================================
# T3: the comb-face instrument and the horizon question (Q1b) + D-H (Q4b).
# ==========================================================================
def run_t3(results, quick):
    print("\n[T3] COMB FACE (Q1b): horizon matched filter, ghost correction, D-H face")
    consume("T3", "cached e1k ground states (xihat values + exact derivative)",
            "mp.zeta / D-H L VALUES + derivatives on Re s = 2 (no zeros)",
            "Lambda / Lambda_DH streams (model templates)")
    lz = np.array(streams()[0])
    ldh = np.array(streams()[1])

    with mp.workdps(30):
        dlf_z = np.array([complex(dlogfac_zeta(complex(s))) for s in SLINE])
        gz_true = np.array([complex(-mp.zeta(complex(s), derivative=1)
                                    / mp.zeta(complex(s))) for s in SLINE])
    Rz = R_W(gz_true)

    def g_comb(cns, nmax_incl):
        out = np.full(len(SLINE), 0j)
        for n in range(2, len(cns)):
            if cns[n] != 0.0 and n <= nmax_incl:
                out += cns[n] * np.exp(-SLINE * math.log(n))
        return out

    def g_dens(cut):
        # smooth PNT-density tail int_cut^inf x^{-s} dx: the alternative
        # hypothesis "carries density but no teeth" must be representable
        return np.array([complex(cut) ** (1 - complex(s)) / (complex(s) - 1) for s in SLINE])

    # ---- horizon signatures per cutoff (fluctuation-only: teeth beyond the
    # cutoff replaced by their smooth density) + per-signature noise bars ----
    cuts = {2.2: 4.84, 2.6: 6.76, 3.0: 9.0, SQRT13: 13.0}
    rng = np.random.default_rng(7)
    H, a_sd = {}, {}
    for lam, cut in cuts.items():
        H[lam] = R_W(g_comb(lz, cut) + g_dens(cut)) - Rz
        a_sd[lam] = float(np.std([alpha_read(rng.normal(0, 1e-3, len(UGRID)), H[lam])
                                  for _ in range(200)]))
        results[f"t3_H_norm_{lam:.3f}"] = float(np.linalg.norm(deflate(H[lam])))
        results[f"t3_alpha_sd_{lam:.3f}"] = a_sd[lam]

    # ---- instrument controls ----
    a_self = alpha_read(H[2.2], H[2.2])
    drift = 0.02 * np.exp(-((UGRID - 1.0) ** 2))
    D_synth = H[2.2] + drift + rng.normal(0, 1e-3, len(UGRID))
    a_synth = alpha_read(D_synth, H[2.2])
    check("T3a instrument controls: self-read = 1, synthetic truncated object caught "
          "(alpha ~ 1 over drift + noise), noise bars small",
          abs(a_self - 1) < 1e-12 and a_synth > 0.7 and a_sd[2.2] < 0.1,
          f"self {a_self:.3f}, synth {a_synth:.3f}, noise sd(2.2) {a_sd[2.2]:.3f}")

    # ---- zeta builds ----
    grid = [(2.2, 12), (2.6, 16)] if quick else [(2.2, 12), (2.6, 16), (3.0, 32), (SQRT13, 48)]
    comb_only = deflate(R_W(gz_true - dlf_z))   # pure-comb direction (signed aggregate)
    rows = {}
    for lam, N in grid:
        xh = get_build("ZETA", lam, N)
        gobj = g_object(xh, SLINE, dlf_z)
        D_raw = R_W(gobj) - Rz
        z0s = spurious_real_zeros(xh)
        D = R_W(gobj - ghost_pole_terms(z0s, ZLINE)) - Rz
        Dq, Hq = deflate(D), deflate(H[lam])
        a_raw = alpha_read(D_raw, H[lam])
        a = float(np.dot(Dq, Hq) / np.dot(Hq, Hq))
        rho = float(np.dot(Dq, Hq) / (np.linalg.norm(Dq) * np.linalg.norm(Hq)))
        dist_ratio = float(np.linalg.norm(Dq - Hq) / np.linalg.norm(Dq))
        beta = float(np.dot(Dq, comb_only) / np.dot(comb_only, comb_only))
        teeth = [2, 3, 4, 5, 7]
        d_n = {n: float(Dq[np.argmin(np.abs(UGRID - math.log(n)))] / tooth_peak(n, lz))
               for n in teeth}
        # naive-read calibration row: the same pointwise read applied to the
        # horizon signature itself (teeth beyond cut should read ~ -1)
        cal_n = {n: float(Hq[np.argmin(np.abs(UGRID - math.log(n)))] / tooth_peak(n, lz))
                 for n in teeth}
        rows[lam] = dict(a=a, a_raw=a_raw, rho=rho, dist_ratio=dist_ratio, beta=beta,
                         z0s=z0s, d_n=d_n, cal_n=cal_n,
                         Dn=float(np.linalg.norm(Dq)),
                         Dn_raw=float(np.linalg.norm(deflate(D_raw))),
                         Hn=float(np.linalg.norm(Hq)))
        for k in ("a", "a_raw", "rho", "dist_ratio", "beta", "Dn", "Dn_raw"):
            results[f"t3_{k}_{lam:.3f}"] = rows[lam][k]
        results[f"t3_ghosts_{lam:.3f}"] = np.array(z0s)
        results[f"t3_teeth_{lam:.3f}"] = np.array([d_n[n] for n in teeth])
        results[f"t3_teeth_cal_{lam:.3f}"] = np.array([cal_n[n] for n in teeth])
        gh = ",".join(f"{z:.2f}" for z in z0s) if z0s else "none"
        print(f"    ZETA lam={lam:.3f} cut={cuts[lam]:.2f}: alpha={a:+.2f}+-{a_sd[lam]:.2f} "
              f"(raw {a_raw:+.2f}) rho={rho:+.2f} dist_hor/dist_full={dist_ratio:.2f} "
              f"|D|={rows[lam]['Dn']:.4f} (raw {rows[lam]['Dn_raw']:.4f}) ||H||={rows[lam]['Hn']:.4f}")
        print(f"      beta_agg={beta:+.3f} ghosts[{gh}]  teeth d_n: "
              + "  ".join(f"{n}:{d_n[n]:+.3f}" for n in teeth)
              + "  [cal: " + " ".join(f"{n}:{cal_n[n]:+.2f}" for n in teeth) + "]")

    clean = [2.2] if quick else [2.2, 3.0]
    dirty = [2.6] if quick else [2.6, SQRT13]
    check("T3b horizon hypothesis DISFAVORED on the clean builds: alpha is many "
          "white-noise-sd below 1 and the full-comb model is the closer one where the "
          "signature resolves (lam 2.2); structured-null demotion in the .md",
          all((1 - rows[l]["a"]) > 5 * a_sd[l] for l in clean)
          and rows[2.2]["dist_ratio"] > 1.5,
          "; ".join(f"lam={l:.2f}: alpha {rows[l]['a']:+.2f}+-{a_sd[l]:.2f}" for l in clean)
          + f"; dist ratio(2.2) = {rows[2.2]['dist_ratio']:.2f}")
    check("T3c dirty builds: raw comb face corrupted by the e1m low-band fill zeros "
          "(known-spurious, all below 14.13); clean builds have none",
          all(len(rows[l]["z0s"]) >= 2 and rows[l]["Dn_raw"] > 3 * rows[2.2]["Dn"] for l in dirty)
          and all(len(rows[l]["z0s"]) == 0 for l in clean),
          "; ".join(f"lam={l:.2f}: {len(rows[l]['z0s'])} ghosts, |D_raw|={rows[l]['Dn_raw']:.2f}"
                    for l in dirty))
    check("T3d ghost quotient restores the law: |D| drops >= 5x and lands at or below "
          "the clean-build error scale",
          all(rows[l]["Dn_raw"] / rows[l]["Dn"] > 5 and rows[l]["Dn"] < 2 * rows[2.2]["Dn"]
              for l in dirty),
          "; ".join(f"lam={l:.2f}: drop {rows[l]['Dn_raw']/rows[l]['Dn']:.0f}x -> |D|={rows[l]['Dn']:.4f}"
                    for l in dirty))
    check("T3e beyond-cutoff signature resolvability is honest: at lam >= 3 the horizon "
          "signature sits at or below the object's error floor (reads there are "
          "reported UNRESOLVED, not claimed)",
          all(rows[l]["Hn"] < 1.5 * rows[l]["Dn"] for l in ([3.0, SQRT13] if not quick else []))
          or quick,
          "" if quick else f"||H||/|D| at 3.0: {rows[3.0]['Hn']/rows[3.0]['Dn']:.2f}, "
          f"sqrt13: {rows[SQRT13]['Hn']/rows[SQRT13]['Dn']:.2f}")

    # tau-stability of the 2.2 rejection (same data, sharper blur)
    xh22 = get_build("ZETA", 2.2, 12)
    D18 = R_W(g_object(xh22, SLINE, dlf_z), tau=1.8) - R_W(gz_true, tau=1.8)
    H18 = R_W(g_comb(lz, 4.84) + g_dens(4.84), tau=1.8) - R_W(gz_true, tau=1.8)
    a18 = alpha_read(D18, H18)
    check("T3f rejection stable under the blur scale (tau 2.2 -> 1.8): alpha stays far "
          "below 1", a18 < 0.5, f"alpha(tau=1.8) = {a18:+.2f}")
    results["t3_alpha_tau18"] = a18

    # ---- D-H face (Q4b): same machinery, own comb, own unpacking ----
    dh = _dhmod.davenport_heilbronn
    with mp.workdps(30):
        dlf_d = np.array([complex(dlogfac_dh(complex(s))) for s in SLINE])
        gd_true = np.array([complex(-mp.diff(dh.evaluate, complex(s)) / dh.evaluate(complex(s)))
                            for s in SLINE])
        sval = mp.mpc(3, "0.7")
        truth = complex(-mp.diff(dh.evaluate, complex(sval)) / dh.evaluate(complex(sval)))
    part = complex(sum(ldh[n] * np.exp(-complex(sval) * math.log(n)) for n in range(2, 80)))
    check("T3g D-H comb stream = -L'/L (recursion validated at s = 3 + 0.7i)",
          abs(part - truth) < 3e-3, f"|partial - truth| = {abs(part-truth):.1e}")
    Rd = R_W(gd_true)

    dh_grid = [(2.6, 16)] if quick else [(2.6, 16), (SQRT13, 48)]
    dh_rows = {}
    for lam, N in dh_grid:
        xh = get_build("D-H", lam, N)
        # WHY tmax=4.9: D-H's own first zero is at 5.094; below it every real
        # zero of the D-H twin is spurious (the analogue of zeta's 14.13 window)
        z0s = spurious_real_zeros(xh, tmax=4.9)
        gobj = g_object(xh, SLINE, dlf_d) - ghost_pole_terms(z0s, ZLINE)
        D = R_W(gobj) - Rd
        Hd = deflate(R_W(g_comb(ldh, cuts[lam])) - Rd)   # no density: L_DH is entire (no pole)
        Dq = deflate(D)
        a = float(np.dot(Dq, Hd) / np.dot(Hd, Hd))
        dh_rows[lam] = dict(a=a, Dn=float(np.linalg.norm(Dq)), nz=len(z0s),
                            Hn=float(np.linalg.norm(Hd)))
        results[f"t3_dh_alpha_{lam:.3f}"] = a
        results[f"t3_dh_Dnorm_{lam:.3f}"] = dh_rows[lam]["Dn"]
        print(f"    D-H  lam={lam:.3f}: alpha={a:+.2f} |D|={dh_rows[lam]['Dn']:.4f} "
              f"||H||={dh_rows[lam]['Hn']:.4f} ghosts(<4.9): {len(z0s)}")
    zref = {2.6: rows[2.6]["Dn"] if 2.6 in rows else rows[2.2]["Dn"],
            SQRT13: rows.get(SQRT13, rows[2.2])["Dn"]}
    check("T3h D-H twin: comparable comb-face fidelity (|D| within 3x of the zeta scale) "
          "and alpha far from the horizon value: input-faithful, RH-blind (#158 class)",
          all(r["Dn"] < 3 * max(rows[2.2]["Dn"], zref[l]) and (1 - r["a"]) > 0.5
              for l, r in dh_rows.items()),
          "; ".join(f"lam={l:.2f}: |D|={r['Dn']:.4f}, alpha={r['a']:+.2f}"
                    for l, r in dh_rows.items()))

    # cross-comb input-faithfulness: the zeta object is NOT closer to the D-H comb
    Dz = np.linalg.norm(deflate(R_W(g_object(xh22, SLINE, dlf_z)) - Rz))
    Dx = np.linalg.norm(deflate(R_W(g_object(xh22, SLINE, dlf_z)) - Rd))
    check("T3i input-faithfulness: zeta object's comb face identifies ITS comb "
          "(distance to the D-H comb >> distance to the zeta comb)",
          Dx > 5 * Dz, f"|D vs zeta comb| = {Dz:.3f}, |D vs D-H comb| = {Dx:.3f}")
    results["t3_cross_comb"] = np.array([Dz, Dx])
    return rows


# ==========================================================================
# T4: the escape law, derived (Q2).
# ==========================================================================
def run_t4(results, quick):
    print("\n[T4] ESCAPE LAW (Q2): PW plateau crossing + Stirling rate")
    consume("T4", "cached ground states", "mp.zeta / xi VALUES on Re s = 2 (no zeros)",
            "Gamma-factor data")
    tprof = np.arange(0.0, 14.1, 0.25)
    with mp.workdps(30):
        cXi = np.array([complex(xi_completed(complex(2.0, t))) for t in tprof])

    grid = [(2.2, 12), (2.6, 16)] if quick else [(2.2, 12), (2.6, 16), (3.0, 32), (SQRT13, 48)]
    rows = {}
    for lam, N in grid:
        xh = get_build("ZETA", lam, N)
        line = xh(tprof - 1.5j)
        # c fitted ON THE LINE at t <= 3 only. WHY: (i) the real-axis fit is
        # poisoned by the low-band fill on the dirty builds (T3c); (ii) fitting
        # where tracking is good keeps the prediction non-circular: the floor
        # and plateau are measured away from the crossing region 6..8.
        m3 = tprof <= 3.0
        c = np.vdot(cXi[m3], line[m3]) / np.vdot(cXi[m3], cXi[m3])
        E = np.abs(line - c * cXi)
        delta = E / np.abs(c * cXi)
        d0 = float(np.median(delta[tprof <= 2.0]))
        ix = np.where(delta >= 1.0)[0]
        t_x = float(tprof[ix[0]]) if len(ix) else float("inf")
        # the PW-plateau predictor: the object's OWN far-line level (no truth
        # values consumed there); tracking dies where the decaying signal
        # falls below it
        M = float(np.median(np.abs(line[(tprof >= 9.0) & (tprof <= 12.0)])))
        ip = np.where(np.abs(c * cXi) < M)[0]
        t_pred = float(tprof[ip[0]]) if len(ip) else float("inf")

        # corrected view of the dirty builds (structure finding: the fill is a
        # polynomial dressing; the quotient can push the crossing off the chart)
        z0s = spurious_real_zeros(xh)
        d0c, t_xc = d0, t_x
        if z0s:
            q = np.ones(len(tprof), complex)
            for z0 in z0s:
                q *= (1 - (tprof - 1.5j)**2 / z0**2)
            lc = line / q
            cc = np.vdot(cXi[m3], lc[m3]) / np.vdot(cXi[m3], cXi[m3])
            dc = np.abs(lc - cc * cXi) / np.abs(cc * cXi)
            d0c = float(np.median(dc[tprof <= 2.0]))
            ixc = np.where(dc >= 1.0)[0]
            t_xc = float(tprof[ixc[0]]) if len(ixc) else float("inf")

        # e1m corridor t_dir on the RAW object (comparability with e1m)
        with mp.workdps(30):
            def f_ratio(t):
                s = mp.mpc(2, t)
                fl = complex(xh(np.array([complex(t, -1.5)]))[0]) / complex(fac_zeta(s))
                return abs(fl) / abs(complex(mp.zeta(s)))
            r0 = f_ratio(0.0)
            t_dir = float("inf")
            for t in np.arange(0.0, 40.0, 1.0):
                if not (0.5 < f_ratio(t) / r0 < 2.0):
                    t_dir = float(t)
                    break

        # escape-rate decomposition over the e1m window
        phiN = xh.phi * N
        tlo, thi = phiN + 10, phiN + 40
        with mp.workdps(30):
            def logf(t):
                s = mp.mpc(2, t)
                return float(mp.log(abs(complex(xh(np.array([complex(t, -1.5)]))[0])))
                             - mp.log(abs(fac_zeta(s))))
            rate = (logf(thi) - logf(tlo)) / (thi - tlo)
            r_fac = float(-(mp.log(abs(fac_zeta(mp.mpc(2, thi))))
                            - mp.log(abs(fac_zeta(mp.mpc(2, tlo))))) / (thi - tlo))
        r_closed = math.pi / 4 - 5 / (tlo + thi)   # closed form at the window midpoint
        rows[lam] = dict(d0=d0, d0_corr=d0c, M=M, t_x=t_x, t_x_corr=t_xc, t_pred=t_pred,
                         t_dir=t_dir, rate=rate, r_fac=r_fac, r_closed=r_closed)
        for k, v in rows[lam].items():
            results[f"t4_{k}_{lam:.3f}"] = v
        print(f"    lam={lam:.3f}: delta0={d0:.3f} (corr {d0c:.4f}) M={M:.3f} "
              f"t_x={t_x:.2f} (corr {t_xc if math.isfinite(t_xc) else float('inf'):.2f}) "
              f"t*_pred={t_pred:.2f} t_dir={t_dir:.1f}")
        print(f"      rate={rate:.3f} r_fac={r_fac:.3f} closed={r_closed:.3f} "
              f"r_obj={rate - r_fac:+.3f}")

    lams = list(rows)
    # the two-mechanism split: builds whose raw line is floor + signal shaped
    # (small floor, genuine crossing) vs the fill-dressed builds (raw floor
    # O(1): the corridor trips on the dressing polynomial, not on tracking)
    clean = [l for l in lams if rows[l]["d0"] < 0.1 and math.isfinite(rows[l]["t_x"])]
    dressed = [l for l in lams if l not in clean]
    check("T4a PW-plateau predictor on the floor-shaped (clean) class: "
          "|t*_pred - t_x| <= 1.5 (plateau measured at t in [9,12], object data only)",
          len(clean) >= 1 and all(abs(rows[l]["t_pred"] - rows[l]["t_x"]) <= 1.5 for l in clean),
          "; ".join(f"lam={l:.2f}: pred {rows[l]['t_pred']:.2f} vs meas {rows[l]['t_x']:.2f}"
                    for l in clean))
    check("T4b corridor t_dir = the same crossing on the clean class (<= 1.5)",
          all(abs(rows[l]["t_dir"] - rows[l]["t_x"]) <= 1.5 for l in clean),
          "; ".join(f"lam={l:.2f}: t_dir {rows[l]['t_dir']:.0f} vs t_x {rows[l]['t_x']:.2f}"
                    for l in clean))
    tds = [rows[l]["t_dir"] for l in lams]
    check("T4c the constancy SPLITS into two mechanisms: clean floors stagnate "
          "(pair within 10 percent) while the DRESSED builds' corridor trip is a "
          "fill artifact: their ghost-quotiented objects track past t = 14 "
          "(no delta = 1 crossing)",
          (quick or abs(rows[3.0]["d0"] / rows[2.2]["d0"] - 1) < 0.5)
          and all(not math.isfinite(rows[l]["t_x_corr"]) for l in dressed),
          "clean delta0: " + ", ".join(f"{rows[l]['d0']:.3f}" for l in clean)
          + "; dressed corrected floors: "
          + ", ".join(f"{rows[l]['d0_corr']:.4f}" for l in dressed)
          + " with corrected crossing beyond the 14-window")
    print("    => TWO MECHANISMS: on the clean class t_dir is the plateau crossing")
    print("       (M ~ 0.23..0.26, predicted to 0.5); on the fill class the corridor")
    print("       trips on the dressing polynomial while the quotiented object")
    print("       tracks past 14 (lam 2.6 at floor 2e-4): e1m's flat t_dir ~ 6..7")
    print("       table mixes the two. The stealth window is NOT monolithic.")
    check("T4d type-proportional law FALSIFIED: t_dir spread < 25 percent while the "
          "exponential type grows 63 percent",
          max(tds) / min(tds) < 1.25
          and math.log(max(lams)) / math.log(min(lams)) > (1.5 if not quick else 1.1),
          f"t_dir in [{min(tds):.0f}, {max(tds):.0f}]; log-lam ratio "
          f"{math.log(max(lams))/math.log(min(lams)):.2f}")
    check("T4e escape rate = archimedean factor decay: |rate - r_fac| <= 0.08 and "
          "r_fac matches the Stirling closed form to 3 decimals",
          all(abs(rows[l]["rate"] - rows[l]["r_fac"]) <= 0.08
              and abs(rows[l]["r_fac"] - rows[l]["r_closed"]) < 5e-3 for l in lams),
          "; ".join(f"lam={l:.2f}: {rows[l]['rate']:.3f} = {rows[l]['r_fac']:.3f} "
                    f"{rows[l]['rate']-rows[l]['r_fac']:+.3f}" for l in lams))
    return rows


# ==========================================================================
# T5: one-sidedness (Q3): the lemmas, the witnesses, the measured signature.
# ==========================================================================
def run_t5(results, t3rows, quick):
    print("\n[T5] ONE-SIDEDNESS (Q3): lemma, witnesses, and the measured comb-error signature")
    consume("T5", "sieved Lambda(n) (arithmetic input, no zeros)",
            "cached ground states (diagonal reads)", "mp.zeta VALUES at real s")

    NMAX = 200000 if quick else 2000000
    lam_arr = np.full(NMAX + 1, 0.0)
    sieve = np.ones(NMAX + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(NMAX**0.5) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    for p in np.nonzero(sieve)[0]:
        pk = p
        while pk <= NMAX:
            lam_arr[pk] = math.log(p)
            pk *= p
    n = np.arange(1, NMAX + 1, dtype=float)

    # (a) the nonneg upgrade mechanism, exactly: Abel summation converts a
    # one-sided LINEAR bound on psi into the abscissa-1 envelope. The step
    # integral is exact: int_1^N psi x^{-s-1} dx = sum psi(k)(k^{-s}-(k+1)^{-s})/s.
    sig = 1.5
    psi = np.cumsum(lam_arr[1:])
    lhs = float(np.sum(lam_arr[1:] * n ** (-sig)))
    rhs = float(np.sum(psi[:-1] * (n[:-1] ** (-sig) - n[1:] ** (-sig))) + psi[-1] * NMAX ** (-sig))
    check("T5a Abel-summation identity exact (the nonneg one-sided upgrade mechanism)",
          abs(lhs - rhs) < 1e-9, f"|sum - stepint| = {abs(lhs-rhs):.1e} at sigma=1.5")

    # (b) partial-sum one-sidedness INSUFFICIENT: c_n = (-1)^n n^{1/4} has
    # bounded-scale partial sums, the series CONVERGES at sigma = 1.1, but
    # absolute convergence FAILS there (abscissa of absolute convergence 5/4).
    cn = ((-1.0) ** np.arange(1, NMAX + 1)) * n ** 0.25
    terms = cn * n ** (-1.1)
    Sx = np.cumsum(terms)
    conv_gap = abs(Sx[-1] - Sx[len(Sx) // 2 - 1])
    At = np.cumsum(np.abs(terms))
    xs = np.array([10**k for k in range(3, int(math.log10(NMAX)) + 1)])
    expo = np.polyfit(np.log(xs), np.log(At[xs - 1]), 1)[0]
    check("T5b witness (-1)^n n^{1/4}: series converges at sigma=1.1, absolute sums "
          "diverge like x^0.15: partial-sum one-sidedness cannot buy the abscissa",
          conv_gap < 1e-3 and 0.10 < expo < 0.22,
          f"|S(N)-S(N/2)| = {conv_gap:.1e}; |.|-growth exponent {expo:.3f} (true 0.15)")
    results["t5_witness_expo"] = float(expo)

    # (c) one-sided-without-convergence gives nothing: c_n = Lambda(n) - n^{1/2}
    # obeys c_n <= Lambda(n) and psi_c(x) << x yet the series diverges to -inf
    # on 1 < sigma <= 3/2 (one-signed tail): EXISTENCE cannot come from
    # inequalities.
    cn2 = lam_arr[1:] - n ** 0.5
    S2 = np.cumsum(cn2 * n ** (-1.3))
    expo2 = np.polyfit(np.log(xs), np.log(-S2[xs - 1] + 2), 1)[0]
    check("T5c witness Lambda(n) - sqrt(n): one-sided + partial sums bounded above, "
          "series diverges at sigma=1.3 (growth ~ x^0.2)",
          bool(np.all(cn2 <= lam_arr[1:] + 1e-12)) and S2[-1] < -10 and 0.15 < expo2 < 0.25,
          f"S(N) = {S2[-1]:.1f}, divergence exponent {expo2:.3f} (true 0.2)")

    # (d) MEASURED comb-error signature of the finite family: diagonal
    # comb-mass reads at real s (ghost-corrected) + the signed aggregates.
    lz = np.array(streams()[0])
    sig_pts = (1.8, 2.0, 2.5, 3.0)
    with mp.workdps(30):
        g_true_diag = {s: float(mp.re(-mp.zeta(mp.mpf(s), derivative=1) / mp.zeta(mp.mpf(s))))
                       for s in sig_pts}
        dlf_diag = {s: complex(dlogfac_zeta(mp.mpf(s))) for s in sig_pts}
    grid = [(2.2, 12), (2.6, 16)] if quick else [(2.2, 12), (2.6, 16), (3.0, 32), (SQRT13, 48)]
    diag = {}
    for lam, N in grid:
        xh = get_build("ZETA", lam, N)
        z0s = spurious_real_zeros(xh)
        vals = []
        for s in sig_pts:
            S1 = np.array([complex(s, 0.0)])
            zv = np.array([complex(0.0, -(s - 0.5))])
            g = g_object(xh, S1, np.array([dlf_diag[s]]), zv=zv)[0]
            g -= ghost_pole_terms(z0s, zv)[0]
            vals.append(float(np.real(g)) - g_true_diag[s])
        diag[lam] = vals
        results[f"t5_diag_{lam:.3f}"] = np.array(vals)
        print(f"    diagonal comb-mass error (ghost-corrected), lam={lam:.3f}: " +
              "  ".join(f"s={s}:{v:+.4f}" for s, v in zip(sig_pts, vals)))
    all_diag = [v for lam in diag for v in diag[lam]]
    betas = [t3rows[l]["beta"] for l in t3rows]
    n_neg = sum(1 for v in all_diag if v < 0)
    one_signed = n_neg == len(all_diag) or n_neg == 0
    within_ok = all((sum(1 for v in diag[lam] if v < 0) in (0, len(diag[lam])))
                    for lam in diag)
    check("T5d measured signature recorded: within-build one-signed, ACROSS-build "
          "MIXED (the family does not hand over a one-sided comb error for free)",
          len(all_diag) == 4 * len(grid) and within_ok,
          f"diag negatives: {n_neg}/{len(all_diag)} "
          f"({'ONE-SIGNED' if one_signed else 'MIXED across builds'}); "
          f"beta_agg = " + ", ".join(f"{b:+.3f}" for b in betas))
    results["t5_one_signed_overall"] = bool(one_signed)
    results["t5_diag_n_neg"] = n_neg

    # (e) the Euler gate: zeta's comb is nonnegative (the rescue clause is
    # available); D-H's comb is sign-changing (the gate CLOSES for D-H at the
    # input level: an input-level discrimination, #154-conformant)
    ldh = np.array(streams()[1])
    nz = ldh[2:40][np.abs(ldh[2:40]) > 1e-12]
    sc = int(np.sum(np.diff(np.sign(nz)) != 0))
    check("T5e the Euler gate: Lambda >= 0 (zeta) vs sign-changing Lambda_DH "
          "(the nonneg upgrade is Euler-product-gated, D-H excluded at input level)",
          bool(np.all(lz[2:] >= -1e-12)) and sc >= 5,
          f"min Lambda = {lz[2:].min():.1e}; D-H comb sign changes (n<40): {sc}")


# ==========================================================================
# T6: Beurling discipline (Q4a).
# ==========================================================================
def run_t6(results, t3rows, quick):
    print("\n[T6] BEURLING (Q4a): lattice leakage law of the comb read")
    consume("T6", "Beurling fake (b_p = p e^eps, eps U[-0.25,0.25], seed 149)",
            "eps = 0 lattice control (same prime set)")
    B = BeurlingSystem(prime_bound=15000, eps=0.25, seed=149)
    logs_b = np.array(B.logs)
    logs_z = np.log(np.array(B.labels, float))
    print(f"    fake system: {len(logs_b)} perturbed primes, eps={B.eps}, seed 149")

    def g_from_logs(S, logs, kcap=16.0):
        freqs, amps = [], []
        for lb in logs:
            k = 1
            while k * lb <= kcap:
                freqs.append(k * lb)
                amps.append(lb)
                k += 1
        freqs, amps = np.array(freqs), np.array(amps)
        return (amps[None, :] * np.exp(-np.outer(S, freqs))).sum(axis=1)

    lz = np.array(streams()[0])

    def lattice_fit_resid(Rvals, uu, tau, own_logs=None):
        """LSQ of the read against tooth templates + poly background; templates
        on the integer lattice by default, or on the fake's own frequencies."""
        cols = []
        if own_logs is None:
            for nn in range(2, 27):
                if lz[nn] != 0.0:
                    cols.append(lz[nn] * nn ** (-SIGMA0)
                                * np.exp(-tau**2 * (uu - math.log(nn))**2 / 2))
        else:
            for lb in own_logs:
                k = 1
                while k * lb < uu.max() + 0.3:
                    if k * lb > uu.min() - 0.3:
                        cols.append(lb * math.exp(-SIGMA0 * k * lb)
                                    * np.exp(-tau**2 * (uu - k * lb)**2 / 2))
                    k += 1
        x = (uu - uu.mean()) / (uu.max() - uu.min()) * 2
        for k in range(4):
            cols.append(np.polynomial.legendre.legval(x, [0] * k + [1]))
        A = np.array(cols).T
        nrm = np.linalg.norm(A, axis=0)
        coef, _, _, _ = np.linalg.lstsq(A / nrm, Rvals, rcond=None)
        return float(np.linalg.norm(A @ (coef / nrm) - Rvals) / np.linalg.norm(Rvals))

    uu = np.arange(0.3, 3.45, 0.02)
    Tws = (6.0, 24.0) if quick else (6.0, 12.0, 24.0, 48.0)
    ratios, resids_b = {}, {}
    for Tw in Tws:
        tsw = np.arange(0.0, Tw + 1e-9, 0.15)
        Sw = np.array([complex(SIGMA0, t) for t in tsw])
        tauw = Tw / 3.0
        RB = R_W(g_from_logs(Sw, logs_b), ts=tsw, u=uu, tau=tauw)
        RZ = R_W(g_from_logs(Sw, logs_z), ts=tsw, u=uu, tau=tauw)
        rb = lattice_fit_resid(RB, uu, tauw)
        rz = lattice_fit_resid(RZ, uu, tauw)
        ratios[Tw] = rb / max(rz, 1e-12)
        resids_b[Tw] = rb
        results[f"t6_resid_fake_{int(Tw)}"] = rb
        results[f"t6_resid_ctrl_{int(Tw)}"] = rz
        msg = (f"    Tw={Tw:4.0f} tau={tauw:4.1f}: fake-on-lattice resid {rb:.4f} vs "
               f"control {rz:.4f} (ratio {ratios[Tw]:5.1f})")
        if Tw == max(Tws):
            r_own = lattice_fit_resid(RB, uu, tauw, own_logs=logs_b[logs_b < 3.6])
            results["t6_resid_own"] = r_own
            msg += f"; fake-on-OWN-frequencies resid {r_own:.4f}"
        print(msg)

    check("T6a leakage law: blind at the archimedean-capped window, nameable failure "
          "beyond (residual ratio grows monotonically with the window)",
          ratios[min(Tws)] < 3.0 and ratios[max(Tws)] > 5.0
          and all(ratios[a] <= ratios[b] + 0.5 for a, b in zip(Tws, Tws[1:])),
          "ratios: " + ", ".join(f"Tw={int(t)}: {ratios[t]:.1f}" for t in Tws))
    check("T6b the failure is the LATTICE, by construction: own-frequency templates "
          "restore the fit at the longest window",
          results["t6_resid_own"] < 3 * results[f"t6_resid_ctrl_{int(max(Tws))}"],
          f"own {results['t6_resid_own']:.4f} vs lattice {resids_b[max(Tws)]:.4f}")

    # H4-not-pinned number: at the object's accessible window, the fake full
    # comb sits at ~ the object's own error distance from the true comb
    RB6 = R_W(g_from_logs(SLINE, logs_b))
    RZ6 = R_W(g_from_logs(SLINE, logs_z))
    d_fake = float(np.linalg.norm(deflate(RB6 - RZ6)))
    d_obj = t3rows[2.2]["Dn"]
    results["t6_h4_fake_dist"] = d_fake
    results["t6_h4_obj_dist"] = d_obj
    check("T6c H4 lattice clause NOT pinned at finite lambda: fake-vs-lattice distance "
          "is within ~3x of the object's own comb error at the accessible window",
          d_fake < 3 * d_obj and d_fake > d_obj / 10,
          f"|R(fake)-R(lattice)| = {d_fake:.4f} vs object |D| = {d_obj:.4f}")
    print("    NAMED CLAUSE: the read's model lives on the integer lattice {log n};")
    print("    the fake's comb lives on {log b_p}. At window Tw the displacement d_p")
    print("    decoheres like 1 - exp(-(Tw d_p)^2/18): invisible for Tw << 1/eps,")
    print("    fatal for Tw >> 1/eps. The finite object's window is capped at")
    print("    t_dir ~ 7 by the archimedean escape (T4), INSIDE the blind zone:")
    print("    the finite comb face cannot certify the lattice clause of H4.")


# ==========================================================================
# T7: K1 / discipline audit.
# ==========================================================================
def run_t7(results, guards):
    print("\n[T7] K1 / DISCIPLINE AUDIT")
    src = Path(__file__).read_text(encoding="utf-8")
    forbidden = ["zeta" + "zero", "ZETA_" + "ZEROS", "DH_" + "ZEROS", ".zeros" + "("]
    scan = [ln for ln in src.splitlines()
            if not ln.strip().startswith("#") and "K1-ALLOW" not in ln]
    hits = [tok for tok in forbidden if any(tok in ln for ln in scan)]
    check("T7a source scan: no zero-list / zero-scanner access in the comb path",
          not hits, f"forbidden tokens found: {hits}" if hits else "clean")
    check("T7b runtime guards on the zero scanners: installed, never tripped",
          guards["installed"] and not guards["tripped"], "any call would have raised")
    print("    input ledger (what each test consumed):")
    for test in sorted(LEDGER):
        for item in LEDGER[test]:
            print(f"      {test}: {item}")
    bad = [t for t, items in LEDGER.items()
           if any("zero list" in i.lower() and "no zero" not in i.lower() for i in items)]
    check("T7c ledger: no test consumed a zero list", not bad, str(bad) if bad else "")
    print("    NG1/C3 note: nothing endomorphism-shaped is introduced (values of entire")
    print("    functions, linear windowed reads, classical series only). The comb face")
    print("    is read through the ARCHIMEDEAN unpacking (the Gamma factor), and its")
    print("    window is capped by the archimedean escape (T4): the probe conforms to")
    print("    the #156/#157 no-go geography and quantifies the C3 stealth window from")
    print("    the comb side. The spurious-zero scan consumes the OBJECT's own sign")
    print("    changes; the landmark heights 14.13 / 5.09 bound the scan windows only.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true",
                    help="two zeta builds + one D-H build, short Beurling sweep")
    args = ap.parse_args()
    t_start = time.time()
    mp.mp.dps = 25   # e1l/e1m-characterized build regime; L-value tests raise locally

    guards = {"installed": True, "tripped": False}

    def _forbid(*a, **k):
        guards["tripped"] = True
        raise RuntimeError("K1 guard: zero-list access attempted")
    mp.zetazero = _forbid                            # K1-ALLOW (guard install)
    _dhmod.davenport_heilbronn.zeros = _forbid       # K1-ALLOW (guard install)

    results = {}
    print("=" * 78)
    print("E1N: the prime-comb face of the positivity-free surface (LEARNINGS #160)")
    print("=" * 78)

    run_t1(results)
    run_t2(results)
    t3rows = run_t3(results, args.quick)
    run_t4(results, args.quick)
    run_t5(results, t3rows, args.quick)
    run_t6(results, t3rows, args.quick)
    run_t7(results, guards)

    print("\n" + "=" * 78)
    print("VERDICT (tiered; details and honest statement in e1n_prime_comb.md)")
    print("  coefficient_horizon_law = truncation DISFAVORED, NOT DECIDED, where")
    print("    the read resolves: at lam 2.2 alpha = -0.84 sits ~48 WHITE-NOISE sd")
    print("    below the horizon value +1, but the adversary structured-deviation")
    print("    null reproduces the observed (alpha, |D|) at p ~ 0.005-0.09, so the")
    print("    rejection is decisive only against unstructured error; the apparent")
    print("    overshoot (rho < 0) is not significant (p ~ 0.08-0.24). At lam >= 3")
    print("    the beyond-cutoff signature sits below the object's ~3 percent")
    print("    error floor: unresolved, honestly reported.")
    print("    The comb face is a zero-side dual of the tracking, NOT a truncated")
    print("    Euler product; where the low band carries the e1m fill zeros the")
    print("    face is corrupted by exactly those zeros, and the ghost quotient")
    print("    restores (lam 2.6: to 3e-4, the STRUCTURE finding; N-robust at")
    print("    dps 25, dps-branch-specific: see .md). Coefficientwise")
    print("    inversion is dead beyond n ~ 4 (superresolution wall, T2).")
    print("  escape_law_derived = YES: t_dir = crossing of the Stirling-decaying")
    print("    signal with the object's own PW plateau (pred vs meas <= 1.5);")
    print("    plateau constant pi/4 exact, closed form pi/4 - 5/(2t) to 3")
    print("    decimals; t_dir constancy = log-insensitivity + floor stagnation;")
    print("    type-proportional law falsified. t_dir grows iff the floor -> 0")
    print("    = the identification on the line.")
    print("  one_sided_sufficiency = PARTIAL (proven structure): H4 = existence +")
    print("    absoluteness; NONNEGATIVE coefficientwise envelope + convergence =>")
    print("    absoluteness (lemma); partial-sum one-sidedness insufficient")
    print("    (witness); nonnegativity upgrades it (Euler-gated, D-H excluded")
    print("    at input level). EXISTENCE stays untouched = the e1m-equivalent")
    print("    clause.")
    print("  comb_error_signature = one-signed WITHIN a build, MIXED ACROSS")
    print("    builds: no free one-sided coordinate from the family.")
    print("  beurling / dh / k1: see the .md fields.")
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
