"""E2AN: SP-object v0. The first ASSEMBLED instance of the five-component
missing-object interface (docs/03_research/missing_object_interface.md),
built wrong on purpose so that its wrongness has coordinates.

WHAT THIS IS. Every prior probe inhabited SP components one at a time
(e2ai: the base; e2aj: per-prime W6; e2ak: the Beurling clause; e1f-e1h:
the archimedean prolate harness). This module builds ONE object
X = (H, Fr, (B, Delta), TF, pol) at finite scale and scores all five
components on zeta AND on both controls through identical code:

  SP1 carrier      H = L^2 of the circle C_L = R/(L Z), L = log lambda,
                   with the lattice map E(f)(u) = u^{1/2} sum_n a_n f(nu)
                   descending to it (the CCM rung-4 door). The circle's
                   Fourier grid tau_k = 2 pi k / L is the Mellin grid
                   c_k = 1/2 + i tau_k: critical sampling.
  SP2 endomorphism Fr = the scaling flow, compressed to the COKERNEL of
                   the lattice map. Muntz's formula makes the map act
                   diagonally with multiplier m(tau) = L(1/2 + i tau)
                   computed FROM THE INTEGERS ONLY (no L-evaluation, no
                   zero is ever consumed: K1-clean). The cokernel is
                   where |m| dips: literally an H^1, and the flow
                   spectrum on it is the emergent zeros.
  SP3 base+diag    the diagonal knows the primes: the log-derivative
                   coefficients b_n extracted by Dirichlet division from
                   a_n. For zeta b_n = Lambda(n) exactly (prime-power
                   support); supports and growth are the Euler
                   witnesses.
  SP4 trace fmla   the Weil explicit formula evaluated two-sidedly at
                   finite scale: zero side = the object's own emergent
                   spectrum, prime side = Lambda-sums + archimedean
                   digamma integral + pole term. The residual is the
                   measured two-sidedness defect.
  SP5 polarization the Weil quadratic form assembled PRIME-SIDE ONLY
                   (same explicit-formula kernel), bottom eigenvalue on
                   a modulated-Gaussian window: positivity observed with
                   a measured margin, not proved. That gap IS M4.

THE BRACKET, run through one pipeline. D-H (FE, no Euler product): the
lattice map exists (it has Dirichlet coefficients), the completed
multiplier is real on the line (duality PASSES), the emergent spectrum
finds its on-line zeros, and it MISSES the off-line pair at
gamma = 85.699 (|m| stays order 1 there: the completeness failure that
IS the RH-sensitivity), while the Euler witnesses fail (b_6 != 0:
support leaks off prime powers). Beurling (Euler, no lattice): the
Euler witnesses pass (free semigroup, exact von Mangoldt identity), but
the descent breaks: the regularized lattice sum does not decay (the
x^theta counting error), the multiplier DRIFTS with the truncation
scale (there is no critical line to converge to), and the borrowed
Gamma-factor leaves a measured duality defect. Zeta alone passes both
sides. The pole is seen lattice-side as the exact e^{S/2} divergence of
the unregularized descent, with the residue extracted from the growth
coefficient (zeta: 1; D-H: 0; Beurling: its own density A).

WHAT IS HONESTLY WRONG WITH v0 (the point). (i) SP2's completeness
(emergent spectrum = ALL zeros) is exactly RH and is not provided, only
probed at finite resolution. (ii) SP4 is two-sided only up to a
measured finite-scale residual. (iii) SP5's positivity is empirical on
a finite window; the uniform L -> infinity statement is M4 and is not
touched. The object is wrong at exactly the two open joints (C1, C2)
of the interface document, now with numbers attached.

Run:
  python -m experiments.arithmetic_geometric.e2an_sp_object_v0          (full)
  python -m experiments.arithmetic_geometric.e2an_sp_object_v0 --quick  (skips D-H zero-list validation)

Outputs: e2an_sp_object_v0.npz next to this file (tracked: evidence rule).
"""

from __future__ import annotations

import argparse
import time
from math import isqrt, log, pi
from pathlib import Path

import numpy as np
from scipy.signal import fftconvolve
from scipy.special import digamma, gamma as cgamma

from experiments._shared.beurling import BeurlingSystem

HERE = Path(__file__).resolve().parent

S_MIN, S_MAX, DELTA = -6.0, 80.0, 0.002
PAD_POW = 22

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


# validation-only oracle usage counter; the K1 guard asserts it is 0 until the
# build phase has finished
_ORACLE_CALLS = {"n": 0}


def _primes_upto(x: int) -> list[int]:
    s = bytearray([1]) * (x + 1)
    s[0:2] = b"\x00\x00"
    for p in range(2, isqrt(x) + 1):
        if s[p]:
            s[p * p:: p] = bytearray(len(s[p * p:: p]))
    return [i for i in range(2, x + 1) if s[i]]


def lambda_sieve(N: int) -> np.ndarray:
    """von Mangoldt Lambda(n) for n <= N (index 0 unused)."""
    lam = np.zeros(N + 1)
    for p in _primes_upto(N):
        pk = p
        while pk <= N:
            lam[pk] = log(p)
            pk *= p
    return lam


# ----------------------------------------------------------------------------
# lattice data: the ONLY inputs the construction is allowed to consume
# (coefficient sequence on a multiset of log-points, pole residue, Gamma kind)
# ----------------------------------------------------------------------------

class Lattice:
    def __init__(self, name, log_n, a_n, residue, gamma_kind):
        self.name = name
        self.log_n = np.asarray(log_n, dtype=float)     # includes the unit log 1 = 0
        self.a_n = np.asarray(a_n, dtype=float)
        self.residue = float(residue)                   # residue of sum a_n n^{-s} at s = 1
        self.gamma_kind = gamma_kind                    # 'zeta' | 'dh' | 'borrowed'


def build_zeta_lattice(N: int) -> Lattice:
    n = np.arange(1, N + 1)
    return Lattice("zeta", np.log(n), np.ones(N), 1.0, "zeta")


def dh_kappa() -> float:
    # kappa = (sqrt(10 - 2 sqrt(5)) - 2) / (sqrt(5) - 1), Davenport-Heilbronn 1936
    return (np.sqrt(10 - 2 * np.sqrt(5)) - 2) / (np.sqrt(5) - 1)


def dh_coeffs(N: int) -> np.ndarray:
    k = dh_kappa()
    pat = np.array([1.0, k, -k, -1.0, 0.0])
    n = np.arange(1, N + 1)
    return pat[(n - 1) % 5]


def build_dh_lattice(N: int) -> Lattice:
    n = np.arange(1, N + 1)
    return Lattice("dh", np.log(n), dh_coeffs(N), 0.0, "dh")


def build_beurling_lattice(system: BeurlingSystem, X: float, A_density: float) -> Lattice:
    logs = np.array(system.gen_integers(X), dtype=float)
    return Lattice("beurling", logs, np.ones(len(logs)), A_density, "borrowed")


# ----------------------------------------------------------------------------
# the engine. Muntz's formula: for f smooth, compactly supported in (0, inf),
#   int_R [ sum_nu a_nu f(nu e^s) - R * I1 * e^{-s} ] e^{(1/2 + i tau) s} ds
#     = m(tau) * ftilde(1/2 + i tau),
# with m(tau) = the L-function on the critical line. Everything on the left is
# integer data; m is EXTRACTED, never evaluated. The s-grid runs to S_MAX = 80
# so the subtraction term itself has decayed below machine epsilon at the right
# endpoint and the rectangle rule is spectrally accurate (integrand dead at
# both ends; for zeta/Beurling the left end is dead by pole cancellation).
# ----------------------------------------------------------------------------

class Probe:
    """Gaussian probe f(u) with F(s) = f(e^s) = exp(-(s - c)^2 / (2 sigma^2))."""

    def __init__(self, c: float, sigma: float):
        self.c, self.sigma = float(c), float(sigma)

    def F(self, s: np.ndarray) -> np.ndarray:
        return np.exp(-((s - self.c) ** 2) / (2 * self.sigma ** 2))

    def I1(self) -> float:
        # I1 = int f(u) du = int F(s) e^s ds, Gaussian closed form
        return np.sqrt(2 * pi) * self.sigma * np.exp(self.c + self.sigma ** 2 / 2)

    def ftilde(self, tau) -> np.ndarray:
        # ftilde(1/2 + i tau) = int F(s) e^{(1/2 + i tau) s} ds
        z = 0.5 + 1j * np.asarray(tau, dtype=complex)
        return np.sqrt(2 * pi) * self.sigma * np.exp(z * self.c + z * z * self.sigma ** 2 / 2)


def s_grid(s_min: float = S_MIN, s_max: float = S_MAX, delta: float = DELTA) -> np.ndarray:
    return np.arange(s_min, s_max + delta / 2, delta)


def g_reg_on_grid(lat: Lattice, probe: Probe, s: np.ndarray) -> np.ndarray:
    """G_reg(s) = sum_nu a_nu F(s + log nu) - R * I1 * e^{-s} on the grid.

    Each lattice point contributes only where F is non-negligible
    (|s + log nu - c| <= 8 sigma), so the accumulation is windowed."""
    G = -lat.residue * probe.I1() * np.exp(-s)
    w = 8.0 * probe.sigma
    lo, hi = probe.c - w, probe.c + w
    ds = s[1] - s[0]
    s0 = s[0]
    n_pts = len(s)
    for ln, a in zip(lat.log_n, lat.a_n):
        if a == 0.0:
            continue
        i0 = int(np.ceil((lo - ln - s0) / ds))
        i1 = int(np.floor((hi - ln - s0) / ds))
        i0, i1 = max(i0, 0), min(i1, n_pts - 1)
        if i0 > i1:
            continue
        seg = s[i0:i1 + 1]
        G[i0:i1 + 1] += a * probe.F(seg + ln)
    return G


def line_integrand(lat: Lattice, probe: Probe, s_min: float = S_MIN,
                   s_max: float = S_MAX, delta: float = DELTA):
    s = s_grid(s_min, s_max, delta)
    return s, g_reg_on_grid(lat, probe, s) * np.exp(0.5 * s)


def multiplier(lat: Lattice, probe: Probe, s_min: float = S_MIN,
               tau_max: float = 105.0, integrand=None):
    """m(tau) on a fine uniform tau grid via one padded FFT."""
    if integrand is None:
        s, integrand = line_integrand(lat, probe, s_min)
    npad = 1 << PAD_POW
    spec = np.fft.rfft(integrand, n=npad) * DELTA
    tau = 2 * pi * np.fft.rfftfreq(npad, d=DELTA)
    # want M(tau) = int g(s) e^{+i tau s} ds with g real:
    # rfft gives e^{-i tau (s - s_min)}, so conjugate and shift the phase
    M = np.conj(spec) * np.exp(1j * tau * s_min)
    sel = tau <= tau_max
    return tau[sel], M[sel] / probe.ftilde(tau[sel])


def multiplier_at(lat: Lattice, probe: Probe, taus, s_min: float = S_MIN,
                  integrand=None):
    """Exact-frequency version (direct quadrature) for arbitrary tau values."""
    if integrand is None:
        s, integrand = line_integrand(lat, probe, s_min)
    else:
        s = s_grid(s_min)
    taus = np.asarray(taus, dtype=float)
    M = np.exp(1j * np.outer(taus, s)) @ integrand * DELTA
    return M / probe.ftilde(taus)


# ----------------------------------------------------------------------------
# SP-component probes
# ----------------------------------------------------------------------------

def residue_from_divergence(lat: Lattice, probe: Probe, S_list=(5.0, 6.0, 7.0),
                            delta: float = DELTA) -> tuple[float, float]:
    """The pole seen lattice-side: the UNregularized descent integral
    I(S) = int_{-S}^{s_max} sum_nu a_nu F(s + log nu) e^{s/2} ds grows like
    2 R I1 e^{S/2}. Returns (extracted residue, fitted growth exponent)."""
    s_top = probe.c + 8 * probe.sigma

    def I(S):
        s = np.arange(-S, s_top, delta)
        G = g_reg_on_grid(lat, probe, s) + lat.residue * probe.I1() * np.exp(-s)
        return float(np.sum(G * np.exp(0.5 * s)) * delta)

    Is = [I(S) for S in S_list]
    d21, d32 = Is[1] - Is[0], Is[2] - Is[1]
    e21 = 2 * (np.exp(S_list[1] / 2) - np.exp(S_list[0] / 2))
    e32 = 2 * (np.exp(S_list[2] / 2) - np.exp(S_list[1] / 2))
    R_hat = d32 / e32 / probe.I1()
    if d32 * d21 > 0 and abs(d21) > 1e-12 * max(1.0, abs(Is[2])):
        # successive increments scale by e^{expo * step}
        expo = float(np.log(d32 / d21) / (S_list[1] - S_list[0]))
    else:
        expo = 0.0
    return float(R_hat), expo


def detect_zeros(tau: np.ndarray, absm: np.ndarray, tau_lo: float = 5.0,
                 tau_hi: float = 100.0, rel_thresh: float = 0.03,
                 window: float = 8.0):
    """Emergent spectrum: local minima of |m| dipping below rel_thresh times
    the running median scale. Parabolic refinement in log |m|."""
    sel = (tau >= tau_lo) & (tau <= tau_hi)
    t, y = tau[sel], absm[sel]
    out = []
    dt = t[1] - t[0]
    wpts = max(3, int(window / dt))
    logy = np.log(np.maximum(y, 1e-300))
    for i in range(1, len(t) - 1):
        if y[i] <= y[i - 1] and y[i] < y[i + 1]:
            j0, j1 = max(0, i - wpts), min(len(t), i + wpts)
            scale = float(np.median(y[j0:j1]))
            if y[i] < rel_thresh * scale:
                den = logy[i - 1] - 2 * logy[i] + logy[i + 1]
                d = 0.5 * (logy[i - 1] - logy[i + 1]) / den if den != 0 else 0.0
                d = float(np.clip(d, -0.6, 0.6))
                out.append((float(t[i] + d * dt), float(y[i] / scale)))
    return out


def dirichlet_log_derivative(a: np.ndarray) -> np.ndarray:
    """b_n with sum_{d | n} a_{n/d} b_d = a_n log n (requires a_1 = 1).
    For zeta (a_n = 1) this returns Lambda(n) exactly. Sieve-style division."""
    N = len(a)
    b = np.zeros(N + 1)
    aa = np.concatenate([[0.0], a])
    rhs = np.concatenate([[0.0], a * np.log(np.arange(1, N + 1))])
    for d in range(2, N + 1):
        b[d] = rhs[d]
        if b[d] != 0.0:
            for m in range(2 * d, N + 1, d):
                rhs[m] -= aa[m // d] * b[d]
    return b[1:]


def beurling_vonmangoldt_defect(system: BeurlingSystem, X: float) -> float:
    """max over gen-integers nu <= X of | sum_{d | nu} Lambda_B(d) - log nu |,
    computed exactly on exponent vectors (free semigroup: divisors are
    sub-vectors, so the sum telescopes to sum_i e_i log b_i)."""
    gi = system.gen_integers(X, with_factorization=True)
    worst = 0.0
    for ln, fac in gi:
        if not fac:
            continue
        s = sum(e * system.logs[i] for i, e in fac)
        worst = max(worst, abs(s - ln))
    return worst


# ----------------------------------------------------------------------------
# SP4 / SP5: the Weil explicit formula, prime side and zero side.
# Conventions: hcap even, real, compactly supported; h(t) = int hcap(x) e^{i x t} dx;
#   sum_rho h(gamma_rho) = 2 h(i/2)
#                          - 2 sum_n Lambda(n) n^{-1/2} hcap(log n)
#                          + (1/2 pi) int_R h(t) [Re psi(1/4 + i t/2) - log pi] dt
# (rho over ALL nontrivial zeros, gamma of both signs; h even makes both
# pole terms equal and the archimedean integral 2x its half-line value).
# ----------------------------------------------------------------------------

def bump_hcap(x: np.ndarray, x0: float = 4.0) -> np.ndarray:
    out = np.zeros_like(x)
    inside = np.abs(x) < x0
    z = x[inside] / x0
    out[inside] = np.exp(-1.0 / (1.0 - z * z))
    return out


def h_from_hcap(hcap_grid: np.ndarray, x: np.ndarray, pad_pow: int = PAD_POW):
    dx = x[1] - x[0]
    npad = 1 << pad_pow
    spec = np.fft.rfft(hcap_grid, n=npad) * dx
    t = 2 * pi * np.fft.rfftfreq(npad, d=dx)
    h = np.conj(spec) * np.exp(1j * t * x[0])
    return t, np.real(h)   # hcap even real => h real


def ef_prime_side(hcap_grid: np.ndarray, x: np.ndarray, lam: np.ndarray,
                  t_half: np.ndarray, h_half: np.ndarray) -> dict:
    """Prime side of the explicit formula. t_half/h_half live on t >= 0."""
    dx = x[1] - x[0]
    pole = 2.0 * float(np.sum(hcap_grid * np.cosh(0.5 * x)) * dx)
    n_arr = np.arange(1, len(lam))
    hcap_at = np.interp(np.log(n_arr), x, hcap_grid, left=0.0, right=0.0)
    primes_term = -2.0 * float(np.sum(lam[1:] / np.sqrt(n_arr) * hcap_at))
    psi_re = np.real(digamma(0.25 + 0.5j * t_half))
    # even integrand: int_R = 2 int_0^inf (trapezoid; t = 0 endpoint half-weighted)
    arch = float(np.trapezoid(h_half * (psi_re - log(pi)), t_half)) / pi
    return {"pole": pole, "primes": primes_term, "arch": arch,
            "total": pole + primes_term + arch}


def weil_gram_prime_side(omegas, sig_g: float, lam: np.ndarray,
                         x_max: float = 6.0, dx: float = 1e-3,
                         tau_max: float = 160.0, dtau: float = 0.01):
    """Q_{jk} = sum_rho ghat_j(gamma) ghat_k(gamma) computed WITHOUT zeros:
    the explicit-formula prime side applied to h = ghat_j ghat_k, with
    g_j(x) = exp(-x^2 / 2 sig^2) cos(omega_j x). ghat has the closed form
    ghat(t) = sig sqrt(pi/2) [e^{-sig^2 (t-w)^2/2} + e^{-sig^2 (t+w)^2/2}]."""
    x = np.arange(-x_max, x_max + dx / 2, dx)
    gs = [np.exp(-x * x / (2 * sig_g ** 2)) * np.cos(w * x) for w in omegas]
    tau = np.arange(-tau_max, tau_max + dtau / 2, dtau)
    psi_re = np.real(digamma(0.25 + 0.5j * tau))
    n_arr = np.arange(1, len(lam))
    ln_n = np.log(n_arr)

    def ghat_exact(w, t):
        sg = sig_g
        t = np.asarray(t, dtype=complex)
        v = sg * np.sqrt(pi / 2) * (np.exp(-sg * sg * (t - w) ** 2 / 2)
                                    + np.exp(-sg * sg * (t + w) ** 2 / 2))
        return np.real(v) if np.isrealobj(t) or np.all(np.imag(t) == 0) else v

    ghat_i2 = [float(np.real(ghat_exact(w, np.array([0.5j]))[0])) for w in omegas]
    K = len(omegas)
    Q = np.zeros((K, K))
    for j in range(K):
        gh_j = ghat_exact(omegas[j], tau)
        for k in range(j, K):
            h_tau = gh_j * ghat_exact(omegas[k], tau)
            conv = fftconvolve(gs[j], gs[k]) * dx        # hcap = g_j * g_k
            xc = np.arange(len(conv)) * dx + 2 * x[0]
            hcap_at = np.interp(ln_n, xc, conv, left=0.0, right=0.0)
            pole = 2.0 * ghat_i2[j] * ghat_i2[k]
            primes_term = -2.0 * float(np.sum(lam[1:] / np.sqrt(n_arr) * hcap_at))
            arch = float(np.sum(h_tau * (psi_re - log(pi))) * dtau / (2 * pi))
            Q[j, k] = Q[k, j] = pole + primes_term + arch
    return Q, ghat_exact


# ----------------------------------------------------------------------------
# validation oracles (the ONLY code allowed to look at L-values / zeros)
# ----------------------------------------------------------------------------

def oracle_zeta_line(taus):
    import mpmath as mp
    _ORACLE_CALLS["n"] += 1
    mp.mp.dps = 25
    return np.array([complex(mp.zeta(mp.mpc(0.5, t))) for t in taus])


def oracle_zeta_zeros(T: float):
    import mpmath as mp
    _ORACLE_CALLS["n"] += 1
    mp.mp.dps = 25
    out, k = [], 1
    while True:
        g = float(mp.im(mp.zetazero(k)))
        if g > T:
            break
        out.append(g)
        k += 1
    return out


def oracle_dh_line(taus):
    from experiments._shared.davenport_heilbronn import DavenportHeilbronn
    import mpmath as mp
    _ORACLE_CALLS["n"] += 1
    mp.mp.dps = 25
    dh = DavenportHeilbronn()
    return np.array([complex(dh.evaluate(mp.mpc(0.5, t))) for t in taus])


def oracle_dh_zeros(T: float, prec: int = 30):
    from experiments._shared.davenport_heilbronn import DavenportHeilbronn
    _ORACLE_CALLS["n"] += 1
    return DavenportHeilbronn().zeros(T_max=T, prec=prec)


# ----------------------------------------------------------------------------
# the run
# ----------------------------------------------------------------------------

def run(quick: bool = False) -> dict:
    t0 = time.time()
    report: dict = {}
    print("== E2AN: SP-object v0 (assembly of the five-component interface) ==")

    # ---------------- build phase (K1-clean: integers only) -----------------
    print("\n-- build phase: lattices, probes, multipliers (no oracle calls) --")
    N_ZETA = 70000
    lat_z = build_zeta_lattice(N_ZETA)
    lat_d = build_dh_lattice(N_ZETA)

    B = BeurlingSystem(prime_bound=40000, eps=0.25, seed=149)
    gi_sorted = np.array(B.gen_integers(25000.0), dtype=float)
    A_windows = [float(np.searchsorted(gi_sorted, log(xx), side="right") / xx)
                 for xx in (8000.0, 16000.0, 24000.0)]
    A_B = float(np.mean(A_windows))
    lat_b = build_beurling_lattice(B, 67000.0, A_B)
    print(f"  zeta lattice N = {N_ZETA}; beurling gen-integers = {len(lat_b.log_n)}"
          f" (A = {A_B:.4f}, windows {[f'{a:.4f}' for a in A_windows]})")

    probeA = Probe(c=1.9, sigma=0.04)
    probeB = Probe(c=2.6, sigma=0.15)

    s_ref, integ_z = line_integrand(lat_z, probeA)
    _, integ_d = line_integrand(lat_d, probeA)
    _, integ_b = line_integrand(lat_b, probeA)

    tau_z, m_z = multiplier(lat_z, probeA, integrand=integ_z)
    tau_d, m_d = multiplier(lat_d, probeA, integrand=integ_d)
    tau_b, m_b = multiplier(lat_b, probeA, integrand=integ_b)

    # cross-probe consistency: is the extracted operator well-defined?
    # (restricted to tau <= 25 where the wide probe still has signal;
    # beyond that its ftilde underflows and the quotient just amplifies noise)
    _, m_z2 = multiplier(lat_z, probeB)
    sel25 = tau_z <= 25.0
    cross_z = float(np.max(np.abs(m_z[sel25] - m_z2[sel25]) / (1 + np.abs(m_z[sel25]))))

    # truncation-scale drift: s_min -6 vs -7.5 (does the descent converge?)
    _, m_z_ext = multiplier(lat_z, probeA, s_min=-7.5)
    _, m_b_ext = multiplier(lat_b, probeA, s_min=-7.5)
    sel60 = tau_z <= 60.0
    drift_z = float(np.median(np.abs(m_z_ext[sel60] - m_z[sel60]) / (1 + np.abs(m_z[sel60]))))
    drift_b = float(np.median(np.abs(m_b_ext[sel60] - m_b[sel60]) / (1 + np.abs(m_b[sel60]))))

    # the pole seen lattice-side (H^0): divergence rate + extracted residue
    R_z, expo_z = residue_from_divergence(lat_z, probeA)
    R_d, expo_d = residue_from_divergence(lat_d, probeA)
    R_b, expo_b = residue_from_divergence(lat_b, probeA)

    # duality (SP1c): completed multiplier real on the critical line
    def completed(kind, tau, m):
        z = 0.5 + 1j * tau
        if kind == "dh":
            fac = (np.pi / 5) ** (-z / 2) * cgamma((z + 1) / 2)
        else:   # zeta's own factor; also the borrowed attempt for Beurling
            fac = 0.5 * z * (z - 1) * np.pi ** (-z / 2) * cgamma(z / 2)
        return fac * m

    sel_dual = (tau_z >= 2.0) & (tau_z <= 60.0)
    dual_def = {}
    for kind, tt, mm in (("zeta", tau_z, m_z), ("dh", tau_d, m_d), ("beurling", tau_b, m_b)):
        xi = completed("dh" if kind == "dh" else "zeta", tt[sel_dual], mm[sel_dual])
        dual_def[kind] = float(np.median(np.abs(np.imag(xi)) / (np.abs(xi) + 1e-300)))

    # emergent spectra (SP2): the cokernel dips
    em_z = detect_zeros(tau_z, np.abs(m_z))
    em_d = detect_zeros(tau_d, np.abs(m_d))
    em_b = detect_zeros(tau_b, np.abs(m_b))

    # scale-stability of the emergent spectrum (two data scales via probe center)
    def emergent_at(lat, c):
        p = Probe(c=c, sigma=0.04)
        tt, mm = multiplier(lat, p)
        return detect_zeros(tt, np.abs(mm), tau_hi=60.0)

    def match_shift(e1, e2):
        if not e1 or not e2:
            return np.inf
        a2 = np.array([g for g, _ in e2])
        return float(np.median([np.min(np.abs(a2 - g)) for g, _ in e1]))

    em_z_lo, em_z_hi = emergent_at(lat_z, 1.3), emergent_at(lat_z, 2.5)
    em_b_lo, em_b_hi = emergent_at(lat_b, 1.3), emergent_at(lat_b, 2.5)
    stab_z = max(match_shift(em_z_lo, em_z_hi), match_shift(em_z_hi, em_z_lo))
    stab_b = max(match_shift(em_b_lo, em_b_hi), match_shift(em_b_hi, em_b_lo))

    # the D-H off-line landmark window (CLAUDE.md: rho ~ 0.8085 + 85.6993 i)
    win = (tau_d >= 85.2) & (tau_d <= 86.2)
    win_wide = (tau_d >= 82.0) & (tau_d <= 90.0)
    dh_offline_rel = float(np.min(np.abs(m_d[win])) / np.median(np.abs(m_d[win_wide])))
    dh_med_dip = float(np.median([d for _, d in em_d])) if em_d else np.nan

    # SP3: the diagonal knows the primes (log-derivative extraction)
    NB = 5000
    lam_ref = lambda_sieve(NB)[1:]
    b_zeta = dirichlet_log_derivative(np.ones(NB))
    b_err = float(np.max(np.abs(b_zeta - lam_ref)))
    b_dh = dirichlet_log_derivative(dh_coeffs(NB))
    is_pp = lam_ref > 0
    dh_leak = int(np.sum(np.abs(b_dh[~is_pp]) > 1e-8))
    dh_b6 = float(b_dh[5])          # n = 6
    beur_vm_defect = beurling_vonmangoldt_defect(B, 3000.0)

    # SP1 <-> SP2 joint: the circle carrier at scale L (critical sampling).
    # Fold the line integrand onto the circle and compare Fourier coefficients
    # with the sampled multiplier: the exactness of the descent.
    L_CIR = 10.0
    n_cir = int(round(L_CIR / DELTA))                    # 5000, exact alignment
    ks = np.arange(1, 161)
    tau_cir = 2 * pi * ks / L_CIR
    m_cir = multiplier_at(lat_z, probeA, tau_cir, integrand=integ_z)
    H = np.zeros(n_cir)
    idx0 = int(round((0.0 - S_MIN) / DELTA)) % n_cir     # position of s = s_min on the circle
    positions = (np.arange(len(integ_z)) + (n_cir - (int(round(-S_MIN / DELTA)) % n_cir))) % n_cir
    np.add.at(H, positions, integ_z)
    Xf = np.fft.fft(H)
    hk_pos = Xf[(-ks) % n_cir] * DELTA
    pred = m_cir * probeA.ftilde(tau_cir)
    circle_dev = float(np.max(np.abs(hk_pos - pred) / (np.abs(pred) + 1e-300)))

    build_oracle_calls = _ORACLE_CALLS["n"]

    # ---------------- SP4: two-sided trace formula at finite scale ----------
    print("-- SP4: explicit-formula two-sidedness (prime side vs object spectrum) --")
    x0 = 4.0
    dxh = 5e-4
    xh = np.arange(-x0 - 0.1, x0 + 0.1 + dxh / 2, dxh)
    hcap = bump_hcap(xh, x0)
    t_h, h_t = h_from_hcap(hcap, xh)
    hsel = t_h <= 1500.0
    lam_55 = lambda_sieve(int(np.exp(x0)) + 1)
    prime_side = ef_prime_side(hcap, xh, lam_55, t_h[hsel], h_t[hsel])
    ef_scale = max(abs(prime_side["pole"]), abs(prime_side["primes"]),
                   abs(prime_side["arch"]), 0.5)
    # zero-side tail above T = 100 from the Riemann-von Mangoldt density
    tsel = (t_h > 100.0) & (t_h <= 1500.0)
    tail_rvm = float(np.trapezoid(h_t[tsel] * np.log(t_h[tsel] / (2 * pi)), t_h[tsel])) / pi

    def zero_side(gammas):
        return 2.0 * float(np.sum(np.interp(gammas, t_h, h_t))) + tail_rvm

    sp4_resid_emergent = abs(zero_side(np.array([g for g, _ in em_z]))
                             - prime_side["total"])

    # ---------------- SP5: the polarization, prime-side only ----------------
    print("-- SP5: Weil form assembled from the prime side --")
    omegas = [0.0, 6.0, 10.0, 14.1347, 16.75, 21.022, 25.0]
    sig_g = 0.6
    lam_3k = lambda_sieve(3000)
    Q, ghat_exact = weil_gram_prime_side(omegas, sig_g, lam_3k)
    q_eigs = np.linalg.eigvalsh(Q)
    q_min, q_max = float(q_eigs[0]), float(q_eigs[-1])

    # ---------------- validation phase (oracles allowed) --------------------
    print("-- validation phase: oracles (L-values, zeros) --")
    taus_probe = np.array([2.5, 7.0, 13.0, 21.5, 33.0, 47.0, 61.0, 77.0, 93.0])
    zeta_true = oracle_zeta_line(taus_probe)
    m_at = multiplier_at(lat_z, probeA, taus_probe, integrand=integ_z)
    muntz_err = float(np.max(np.abs(m_at - zeta_true) / (1 + np.abs(zeta_true))))

    dh_true = oracle_dh_line(taus_probe[:6])
    md_at = multiplier_at(lat_d, probeA, taus_probe[:6], integrand=integ_d)
    muntz_err_dh = float(np.max(np.abs(md_at - dh_true) / (1 + np.abs(dh_true))))

    gz = oracle_zeta_zeros(100.0)
    loc_err = [min(abs(g - gg) for gg in gz) for g, _ in em_z]
    loc_err_max = float(np.max(loc_err)) if loc_err else np.inf
    found_of_first10 = sum(1 for gg in gz[:10]
                           if any(abs(g - gg) < 0.05 for g, _ in em_z))
    spurious = sum(1 for d in loc_err if d > 0.05)

    sp4_resid_true = abs(zero_side(np.array(gz)) - prime_side["total"])

    # SP5 zero-side validation of the Gram matrix
    ghz = np.array(gz)
    Qz = np.zeros_like(Q)
    for j in range(len(omegas)):
        vj = ghat_exact(omegas[j], ghz)
        for k in range(j, len(omegas)):
            Qz[j, k] = Qz[k, j] = 2.0 * float(np.sum(vj * ghat_exact(omegas[k], ghz)))
    q_abs_err = float(np.max(np.abs(Q - Qz)))
    q_dev = q_abs_err / max(1e-12, float(np.max(np.abs(Qz))))
    qz_eigs = np.linalg.eigvalsh(Qz)
    qz_min, qz_max = float(qz_eigs[0]), float(qz_eigs[-1])

    dh_online_hit = -1.0
    if not quick:
        rhos = [complex(r) for r in oracle_dh_zeros(92.0)]
        on_line = [r.imag for r in rhos if abs(r.real - 0.5) < 0.01 and r.imag > 5.0]
        off_line = [r for r in rhos if abs(r.real - 0.5) >= 0.01]
        hits = sum(1 for gg in on_line if any(abs(g - gg) < 0.06 for g, _ in em_d))
        dh_online_hit = hits / max(1, len(on_line))
        report["dh_on_line"] = on_line
        report["dh_off_line"] = [(r.real, r.imag) for r in off_line]

    # ---------------- checks ------------------------------------------------
    print("\n-- checks --")
    check("K1 guard: zero oracle calls during the build phase",
          build_oracle_calls == 0, f"calls = {build_oracle_calls}")
    check("Muntz engine, zeta: extracted m(tau) = zeta(1/2 + i tau) to 1e-6",
          muntz_err < 1e-6, f"max rel err = {muntz_err:.2e}")
    check("Muntz engine, D-H: extracted m matches DH(1/2 + i tau) to 1e-6",
          muntz_err_dh < 1e-6, f"max rel err = {muntz_err_dh:.2e}")
    check("operator well-defined: cross-probe agreement (zeta, tau <= 25)",
          cross_z < 1e-7, f"max rel dev = {cross_z:.2e}")
    check("H^0 / pole, zeta: divergence exponent 1/2 and residue 1",
          abs(expo_z - 0.5) < 0.02 and abs(R_z - 1.0) < 0.02,
          f"expo = {expo_z:.4f}, R = {R_z:.4f}")
    check("H^0 / pole, D-H: no pole (unregularized descent converges)",
          abs(R_d) < 0.02, f"R = {R_d:.2e}")
    check("H^0 / pole, Beurling: residue = its own measured density A",
          abs(R_b - A_B) / A_B < 0.08, f"R = {R_b:.4f} vs A = {A_B:.4f}")
    check("SP1c duality, zeta: completed multiplier real on the line (< 1e-5)",
          dual_def["zeta"] < 1e-5, f"median |Im|/|xi| = {dual_def['zeta']:.2e}")
    check("SP1c duality, D-H: real with ITS OWN Gamma factor (FE side intact)",
          dual_def["dh"] < 1e-5, f"median = {dual_def['dh']:.2e}")
    check("SP1c duality, Beurling: borrowed Gamma factor leaves a defect (> 1e-2)",
          dual_def["beurling"] > 1e-2, f"median = {dual_def['beurling']:.2e}")
    check("descent converges, zeta: truncation drift at machine scale",
          drift_z < 1e-10, f"median drift = {drift_z:.2e}")
    check("descent DIVERGES, Beurling: drift > 1e4 x zeta's (no critical line)",
          drift_b > 1e4 * max(drift_z, 1e-300), f"drift_B = {drift_b:.2e} vs {drift_z:.2e}")
    check("SP2 emergent spectrum: all first 10 zeta zeros found",
          found_of_first10 == 10, f"{found_of_first10}/10")
    check("SP2 no spurious detections (every dip is a true zero)",
          spurious == 0, f"spurious = {spurious} of {len(em_z)}")
    check("SP2 localization: emergent zeros within 5e-3 of true",
          loc_err_max < 5e-3, f"max = {loc_err_max:.2e}")
    check("SP2 scale-stability, zeta: emergent set stable across data scales",
          stab_z < 2e-3, f"median shift = {stab_z:.2e}")
    check("SP2 completeness FAILS for D-H: the off-line pair is invisible",
          dh_offline_rel > 0.1 and dh_offline_rel > 10 * dh_med_dip,
          f"|m| rel at 85.7 = {dh_offline_rel:.3f} vs median dip {dh_med_dip:.4f}")
    check("SP3 diagonal, zeta: b_n = Lambda(n) exactly (n <= 5000)",
          b_err < 1e-8, f"max |b - Lambda| = {b_err:.2e}")
    check("SP3 Euler failure, D-H: support leaks off prime powers (b_6 != 0)",
          abs(dh_b6) > 0.05 and dh_leak > 100,
          f"b_6 = {dh_b6:.4f}, leaked n count = {dh_leak}")
    check("SP3 Euler holds, Beurling: exact von Mangoldt identity on the semigroup",
          beur_vm_defect < 1e-9, f"max defect = {beur_vm_defect:.2e}")
    check("SP1<->SP2 joint: circle descent identity (fold = sampled multiplier)",
          circle_dev < 1e-9, f"max rel dev = {circle_dev:.2e}")
    check("SP4 normalization: explicit formula two-sided on TRUE zeros",
          sp4_resid_true < 5e-3 * ef_scale,
          f"|resid| = {sp4_resid_true:.2e}, scale = {ef_scale:.3f}")
    check("SP4 on the OBJECT: two-sided on the emergent spectrum",
          sp4_resid_emergent < 5e-2 * ef_scale,
          f"|resid| = {sp4_resid_emergent:.2e}")
    check("SP5 sourcing: prime-side Gram = zero-side Gram (< 1e-4 rel)",
          q_dev < 1e-4, f"max rel dev = {q_dev:.2e}")
    check("SP5 positivity: zero-side Gram strictly PSD (the window margin)",
          qz_min > -1e-12 * max(1.0, qz_max),
          f"margin = {qz_min:.3e} on lambda_max = {qz_max:.3f}")
    check("SP5 marginality: prime-side lambda_min = margin WITHIN assembly error",
          abs(q_min - qz_min) <= 5 * q_abs_err,
          f"lambda_min = {q_min:.3e} vs margin {qz_min:.3e}, resolution {q_abs_err:.1e}")
    if not quick:
        check("SP2, D-H: its on-line zeros ARE found (> 70 percent)",
              dh_online_hit > 0.7, f"hit rate = {dh_online_hit:.2f}")

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print(f"\n{npass}/{len(CHECKS)} passed  ({time.time() - t0:.1f} s)")

    # ---------------- save --------------------------------------------------
    out = HERE / "e2an_sp_object_v0.npz"
    sub = slice(None, None, 10)   # decimate the fine tau grid for the npz
    np.savez_compressed(
        out,
        tau=tau_z[sub], m_zeta=m_z[sub], m_dh=m_d[sub], m_beurling=m_b[sub],
        emergent_zeta=np.array(em_z), emergent_dh=np.array(em_d),
        emergent_beurling=np.array(em_b) if em_b else np.zeros((0, 2)),
        residues=np.array([R_z, R_d, R_b]), expos=np.array([expo_z, expo_d, expo_b]),
        A_beurling=A_B, drift=np.array([drift_z, drift_b]),
        duality=np.array([dual_def["zeta"], dual_def["dh"], dual_def["beurling"]]),
        stab=np.array([stab_z, stab_b]), dh_offline_rel=dh_offline_rel,
        b_dh=b_dh, dh_leak=dh_leak, beur_vm_defect=beur_vm_defect,
        circle_dev=circle_dev, circle_tau=tau_cir, circle_m=m_cir,
        sp4_prime_side=np.array([prime_side["pole"], prime_side["primes"],
                                 prime_side["arch"], prime_side["total"]]),
        sp4_resid=np.array([sp4_resid_true, sp4_resid_emergent]),
        Q_prime=Q, Q_zero=Qz, q_eigs=q_eigs, qz_eigs=qz_eigs, q_abs_err=q_abs_err,
        muntz_err=np.array([muntz_err, muntz_err_dh]),
        dh_online_hit=dh_online_hit,
        checks_passed=npass, checks_total=len(CHECKS),
    )
    print(f"saved {out.name}")
    report.update(dict(
        em_z=em_z, em_d=em_d, em_b=em_b, stab_z=stab_z, stab_b=stab_b,
        drift_z=drift_z, drift_b=drift_b, dual=dual_def, residues=(R_z, R_d, R_b),
        q_min=q_min, q_eigs=list(q_eigs), sp4=prime_side,
        sp4_resid=(sp4_resid_true, sp4_resid_emergent),
        npass=npass, ntot=len(CHECKS)))
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true",
                    help="skip the D-H zero-list validation (slow on first run)")
    args = ap.parse_args()
    run(quick=args.quick)


if __name__ == "__main__":
    main()
