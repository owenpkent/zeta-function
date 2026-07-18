"""E1K: the CCM D_log spectral-triple family as a Davenport-Heilbronn testbed.

WHY THIS EXPERIMENT EXISTS
==========================
The Nov-2025 papers arXiv:2511.22755 (Connes-Consani-Moscovici, "Zeta Spectral
Triples") and arXiv:2511.23257 (Connes-van Suijlekom, the Caratheodory-Fejer
self-adjointness engine) build a rank-one perturbation D_log^(lambda,N) of the
scaling Dirac on a log-circle whose regularized determinant is exactly
det_reg(D_log^(lambda,N) - z) = -i lambda^{-iz} xihat(z), with xihat the Fourier
transform of the ground state of the truncated Weil quadratic form. Theorem
5.10(iii) asserts, UNCONDITIONALLY, that all zeros of xihat are real at every
finite cutoff. The claimed route to RH is Section 7: as lambda -> inf the
xihat_lambda converge uniformly on closed substrips of Im(z) < 1/2 to the
Riemann Xi-function, which by Hurwitz would force RH. The authors call the
identification of the true ground state with the prolate ansatz "the main
remaining obstacle."

The project's Davenport-Heilbronn discipline asks: does this machine
DISCRIMINATE zeta from Davenport-Heilbronn (D-H: same functional equation, NO
Euler product, KNOWN off-line zero near 0.808 + 85.699 i)? If a finite-cutoff
construction "proves reality" for D-H too, that reality carries zero bits about
RH (the information-free-finiteness / stealth-window finding, LEARNINGS
#153/#154). The reading note docs/03_research/reading_notes/CCM-2025-Dlog-family.md
predicts: the finite machine is D-H-BLIND and the entire zeta-vs-D-H
discrimination is quarantined to the (unproven, RH-equivalent) Section-7 limit.

WHAT THIS BUILDS
================
A faithful, self-contained mpmath/numpy reimplementation of the truncated Weil
form and the D_log operator, then runs it side by side on a ZETA stream and a
D-H stream. The two streams enter through IDENTICAL code; only the arithmetic
coefficient comb (and the pole term) differ. The unifying object is the
logarithmic-derivative coefficient stream Lambda(n) obtained from the Dirichlet
recursion sum_{d|n} Lambda(d) c_{n/d} = c_n log n:
  - ZETA: c_n = 1 for all n  =>  Lambda = von Mangoldt, supported on prime
    powers only (the Euler product).
  - D-H:  c_n period-5 = (1, kappa, -kappa, -1, 0)  =>  Lambda_DH supported on
    ALL n >= 2, non-multiplicative, sign-changing (no Euler product).

The Weil form in the orthonormal basis V_n (transported Fourier modes on the
log-circle of circumference L = 2 log lambda) is
  QW = A_arch + [pole] - sum_{2 <= n <= lambda^2} Lambda(n) T(n),
with closed forms derived and verified against the paper's eq (5.25):
  Vhat_n(z) = 2 L^{-1/2} sin(zL/2) / (z - 2 pi n / L)     (verified to 1e-31).
A_arch uses the L-function's OWN archimedean density (zeta: (1/2pi)(Re psi(1/4 +
it/2) - log pi); D-H, an odd character mod 5: (1/2pi)(log(5/pi) + Re psi(3/4 +
it/2))). The pole term 2 Re(conj(a_m) a_n), a_n = Vhat_n(i/2), is present ONLY
for zeta (D-H is entire and has no pole; a rank-<=2 structural difference).

WHAT IS TESTED (the four schema tasks)
======================================
K2 / CF-on-D-H feasibility: does the Caratheodory-Fejer self-adjointness engine
  even RUN on the D-H coefficient stream? (It needs only real + even +
  lower-bounded + simple, none of which references an Euler product.)
Finite-cutoff reality: are the finite determinant zeros of the D-H twin real
  (Thm 5.10(iii))? Reported side by side with the zeta twin.
Uniformity / off-line signal: does the off-line zero at ~85.7 appear ONLY as a
  Section-7 convergence non-uniformity, never at finite cutoff?
C3 reading: is the Section-7 log-line limit the archimedean injection, with D-H
  failing uniformity exactly there?

HONEST SCOPE (read before quoting any number)
=============================================
This is a testbed, not a re-derivation of the paper's exact operator. The
construction reproduces the low zeros of BOTH functions to 4-5 digits (zeta:
14.135, 21.024; D-H: 5.094, 8.940, 12.134, 14.406), which validates the
structure. Two honest caveats are reported in-code and in the .md:
  (1) The truncated Weil form sits on a razor-thin positivity margin (smallest
      eigenvalue ~ 1e-6, a near-degenerate cluster: the documented zero-margin).
  (2) The zeta pole-term realization is not exactly the CF normal form, so the
      operator is G-self-adjoint (w.r.t. the Weil inner product Q - eps I) only
      to ~5e-2 relative and a few "ghost" eigenvalues go complex; the D-H twin,
      which has NO pole term, is G-self-adjoint to ~1e-6 and its finite spectrum
      is real to ~1e-29 at 30-digit precision. The DISCIPLINE conclusion is
      robust to this because both twins run identical code: reality is
      manufactured by finite self-adjointness, not by arithmetic.
It proves nothing about RH. It confirms and sharpens the D-H discipline.

Run:
  python -m experiments.spectral.e1k_dh_dlog_testbed
Outputs:
  experiments/spectral/e1k_dh_dlog_testbed.npz
"""

from __future__ import annotations

import argparse
import time
import warnings
from pathlib import Path

import numpy as np
import mpmath as mp
from scipy.special import loggamma

warnings.filterwarnings("ignore")

OUT = Path(__file__).with_suffix(".npz")

# Reference low zeros (imaginary parts) for validation.
ZETA_ZEROS = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
              37.586178, 40.918719, 43.327073, 48.005151, 49.773832]
DH_ZEROS = [5.0941598, 8.9399144, 12.133545, 14.404003, 17.130239,
            22.159708, 23.345370, 26.094967, 27.923799]
# The first D-H OFF-LINE zero (Davenport-Heilbronn 1936; the discipline anchor):
DH_OFFLINE = complex(0.8085, 85.699)   # s-plane; in the z = (s - 1/2)/i plane: 85.699 - 0.3085 i


# --------------------------------------------------------------------------
# Coefficient streams. The Dirichlet log-derivative recursion unifies zeta and
# D-H so the SAME code path builds both: this is the concrete K2 statement that
# CF is input-agnostic (no Euler product is referenced anywhere).
# --------------------------------------------------------------------------
def kappa_dh(dps=40):
    prev = mp.mp.dps
    mp.mp.dps = max(dps, prev)
    try:
        s5 = mp.sqrt(5)
        return (mp.sqrt(10 - 2 * s5) - 2) / (s5 - 1)
    finally:
        mp.mp.dps = prev


def make_streams(kmax, float_out=True):
    """Return (Lambda_zeta, Lambda_dh) as lists indexed 0..kmax.

    Lambda(n) solves sum_{d|n} Lambda(d) c_{n/d} = c_n log n, c_1 = 1. For zeta
    (c_n = 1) this IS von Mangoldt (support = prime powers, the Euler product);
    for D-H (c_n period-5) it is dense, non-multiplicative and sign-changing.
    """
    k = kappa_dh()
    dh_period = [mp.mpf(1), k, -k, mp.mpf(-1), mp.mpf(0)]
    cz = [mp.mpf(1)] * (kmax + 1)
    cd = [mp.mpf(0)] + [dh_period[(n - 1) % 5] for n in range(1, kmax + 1)]

    def lam_from_c(c):
        Lam = [mp.mpf(0)] * (kmax + 1)
        for n in range(2, kmax + 1):
            s = c[n] * mp.log(n)
            for d in range(2, n):
                if n % d == 0:
                    s -= Lam[d] * c[n // d]
            Lam[n] = s
        return Lam

    lz, ld = lam_from_c(cz), lam_from_c(cd)
    if float_out:
        return [float(x) for x in lz], [float(x) for x in ld]
    return lz, ld


# --------------------------------------------------------------------------
# Fast float builder of the truncated Weil form and the D_log operator.
# Archimedean term: mpmath tanh-sinh over the whole line (correct handling of
# the slowly decaying sin^2 tail), with a fast complex-digamma density.
# --------------------------------------------------------------------------
def _re_psi(a, y, h=1e-5):
    # Re psi(a + i y) via a central difference of the C-level complex loggamma;
    # this is ~500x faster than mpmath.psi and accurate to ~1e-9, which is all
    # the float matrix needs.
    z = complex(a, y)
    return ((loggamma(z + h) - loggamma(z - h)) / (2 * h)).real


def build_float(N, lam, stream, dens_a, dens_b, use_pole):
    """Assemble the (2N+1)x(2N+1) Weil form Q and return the ground state + D_log.

    dens(t) = (Re psi(dens_a + i t/2) + dens_b) / (2 pi) is the L-function's
    archimedean zero density (zeta: dens_a=1/4, dens_b=-log pi; D-H: dens_a=3/4,
    dens_b=log(5/pi)). use_pole toggles the zeta pole term.
    """
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

    # Archimedean matrix (real symmetric). Reuse A[m,n]=A[-m,-n]=A[n,m].
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

    # Pole term (zeta only): rank-2, +(|Fhat(i/2)|^2 + |Fhat(-i/2)|^2).
    P = np.zeros((D, D), complex)
    if use_pole:
        av = np.array([Vhat(n, 0.5j) for n in idx])
        P = 2.0 * np.real(np.outer(np.conj(av), av))

    # Prime / coefficient term: closed-form multiplicative-shift correlation.
    Ts = np.zeros((D, D), complex)
    kmax = int(np.floor(lam * lam + 1e-9))
    for kk_n in range(2, kmax + 1):
        ck = stream[kk_n]
        if ck == 0.0:
            continue
        ell = np.log(kk_n)
        pref = ck * (kk_n ** -0.5)
        for i, m in enumerate(idx):
            for j, nn in enumerate(idx):
                k = nn - m
                if k == 0:
                    Ip = Im = (L - ell)
                else:
                    Ip = (np.exp(1j * k * phi * (L - ell)) - 1) / (1j * k * phi)
                    Im = (np.exp(1j * k * phi * L) - np.exp(1j * k * phi * ell)) / (1j * k * phi)
                corr_n = (1.0 / L) * np.exp(1j * nn * ell * phi) * Ip
                corr_ninv = (1.0 / L) * np.exp(-1j * nn * ell * phi) * Im
                Ts[i, j] += pref * (corr_n + corr_ninv)

    Q = A.astype(complex) + P - Ts
    Q = 0.5 * (Q + Q.conj().T)   # Hermitian symmetrize (kills rounding asymmetry)

    w, V = np.linalg.eigh(Q)

    def efrac(v):
        vs = np.array([v[idx.index(-n)] for n in idx])
        return float(np.linalg.norm(0.5 * (v + vs)) / np.linalg.norm(v))

    # The paper ASSUMES the ground state is even. We select the lowest EVEN
    # eigenvector (faithful to that assumption) and separately record whether
    # the GLOBAL minimum is even, so a violation of the assumption is flagged
    # rather than silently producing a degenerate xihat (Remark 2.3 caveat).
    even_frac_global = efrac(V[:, 0])
    idx_even = 0
    for j in range(len(w)):
        if efrac(V[:, j]) > 0.9:
            idx_even = j
            break
    xi = V[:, idx_even]
    eps = w[idx_even]
    even_assumption_ok = (idx_even == 0)
    # simplicity: gap from the chosen even ground state to the next EVEN state
    gap_even = np.inf
    for j in range(idx_even + 1, len(w)):
        if efrac(V[:, j]) > 0.9:
            gap_even = w[j] - w[idx_even]
            break

    return dict(idx=idx, phi=phi, L=L, Q=Q, w=w, eps=float(eps),
                eps_global=float(w[0]), gap=float(w[1] - w[0]),
                gap_even=float(gap_even), xi=xi,
                even_frac=efrac(xi), even_frac_global=even_frac_global,
                even_assumption_ok=bool(even_assumption_ok))


def operator_spectrum(res):
    """Zeros of xihat = spectrum of D_log^(lambda,N).

    D' = D_log - |D_log xi><delta_N|, delta_N = L^{-1/2} sum V_n. Its eigenvalues
    equal the zeros of xihat by Thm 5.10(ii)-(iii). Also returns the
    G-self-adjointness residual ||G M - M^H G|| / (||G|| ||M||) with G = Q - eps I
    the Weil inner product: this quantifies how exactly the reconstruction
    realizes the CF self-adjoint structure that FORCES reality.
    """
    idx, phi, L = res["idx"], res["phi"], res["L"]
    xi, Q, eps = res["xi"], res["Q"], res["eps"]
    D = len(idx)
    delta = np.array([L ** -0.5] * D)
    xin = xi / (delta @ xi)
    Dlog = np.diag([phi * n for n in idx]).astype(complex)
    M = Dlog - np.outer(Dlog @ xin, delta.conj())
    ev = np.linalg.eigvals(M)
    ev = np.array(sorted(ev, key=lambda z: z.real))
    G = Q - eps * np.eye(D)
    R = G @ M - M.conj().T @ G
    denom = (np.linalg.norm(G) * np.linalg.norm(M)) or 1.0
    sa_res = float(np.linalg.norm(R) / denom)
    return ev, sa_res


# --------------------------------------------------------------------------
# High-precision even-block build (mpmath) for the clean reality confirmation.
# --------------------------------------------------------------------------
def build_hp(N, lam, stream_mp, dens_a, dens_b, use_pole, dps=30):
    prev = mp.mp.dps
    mp.mp.dps = dps
    try:
        L = 2 * mp.log(lam)
        phi = 2 * mp.pi / L
        idx = list(range(-N, N + 1))
        D = 2 * N + 1
        TINY = mp.mpf(10) ** -20

        def Vhat(n, z):
            d = z - phi * n
            if abs(d) < TINY:
                return 2 * L ** mp.mpf("-0.5") * (L / 2) * mp.cos(z * L / 2)
            return 2 * L ** mp.mpf("-0.5") * mp.sin(z * L / 2) / d

        def dens(t):
            return (mp.re(mp.psi(0, mp.mpc(dens_a, t / 2))) + dens_b) / (2 * mp.pi)

        A = mp.zeros(D, D)
        done = {}

        def arch(m, n):
            f = lambda t: Vhat(m, t) * Vhat(n, t) * dens(t)
            a, b = sorted([m * phi, n * phi])
            pts = ([mp.mpf("-inf"), a, mp.mpf("inf")] if abs(a - b) < TINY
                   else [mp.mpf("-inf"), a, b, mp.mpf("inf")])
            return mp.quad(f, pts)

        for i, m in enumerate(idx):
            for j, n in enumerate(idx):
                if j < i:
                    A[i, j] = A[j, i]
                    continue
                nkey = (-m, -n)
                if nkey in done:
                    A[i, j] = done[nkey]
                else:
                    v = arch(m, n)
                    A[i, j] = v
                    done[(m, n)] = v

        P = mp.zeros(D, D)
        if use_pole:
            av = [Vhat(n, mp.mpc(0, mp.mpf("0.5"))) for n in idx]
            for i in range(D):
                for j in range(D):
                    P[i, j] = 2 * mp.re(mp.conj(av[i]) * av[j])

        Ts = mp.zeros(D, D)
        kmax = int(mp.floor(lam * lam + mp.mpf("1e-9")))
        for kk_n in range(2, kmax + 1):
            ck = stream_mp[kk_n]
            if ck == 0:
                continue
            ell = mp.log(kk_n)
            pref = ck * (kk_n ** mp.mpf("-0.5"))
            for i, m in enumerate(idx):
                for j, nn in enumerate(idx):
                    k = nn - m
                    if k == 0:
                        Ip = Im = (L - ell)
                    else:
                        Ip = (mp.e ** (1j * k * phi * (L - ell)) - 1) / (1j * k * phi)
                        Im = (mp.e ** (1j * k * phi * L) - mp.e ** (1j * k * phi * ell)) / (1j * k * phi)
                    cn = (1 / L) * mp.e ** (1j * nn * ell * phi) * Ip
                    cni = (1 / L) * mp.e ** (-1j * nn * ell * phi) * Im
                    Ts[i, j] += pref * (cn + cni)

        Qh = mp.zeros(D, D)
        for i in range(D):
            for j in range(D):
                q = A[i, j] + P[i, j] - Ts[i, j]
                Qh[i, j] = q
        # Hermitian symmetrize
        Q2 = mp.zeros(D, D)
        for i in range(D):
            for j in range(D):
                Q2[i, j] = (Qh[i, j] + mp.conj(Qh[j, i])) / 2

        # even block real symmetric
        m = N + 1
        sq = mp.sqrt(2)
        gi = idx.index

        def ev_entry(j, k):
            if j == 0 and k == 0:
                return Q2[gi(0), gi(0)]
            if j == 0:
                return (Q2[gi(0), gi(k)] + Q2[gi(0), gi(-k)]) / sq
            if k == 0:
                return (Q2[gi(j), gi(0)] + Q2[gi(-j), gi(0)]) / sq
            return (Q2[gi(j), gi(k)] + Q2[gi(j), gi(-k)] +
                    Q2[gi(-j), gi(k)] + Q2[gi(-j), gi(-k)]) / 2

        Ereal = mp.matrix([[mp.re(ev_entry(i, j)) for j in range(m)] for i in range(m)])
        evals, evecs = mp.eigsy(Ereal)
        order = sorted(range(m), key=lambda i: evals[i])
        eps = evals[order[0]]
        gap = evals[order[1]] - evals[order[0]]
        dvec = [evecs[i, order[0]] for i in range(m)]

        xi = mp.zeros(D, 1)
        xi[gi(0), 0] = dvec[0]
        for kk in range(1, N + 1):
            xi[gi(kk), 0] = dvec[kk] / sq
            xi[gi(-kk), 0] = dvec[kk] / sq
        delta = [L ** mp.mpf("-0.5")] * D
        s = sum(delta[i] * xi[i, 0] for i in range(D))
        for i in range(D):
            xi[i, 0] /= s

        M = mp.zeros(D, D)
        for i, n in enumerate(idx):
            M[i, i] = phi * n
        Dxi = [phi * idx[i] * xi[i, 0] for i in range(D)]
        for i in range(D):
            for j in range(D):
                M[i, j] -= Dxi[i] * mp.conj(delta[j])
        ev = mp.eig(M, left=False, right=False)
        ev = sorted(ev, key=lambda z: mp.re(z))
        return dict(eps=complex(eps), gap=complex(gap),
                    ev=[complex(z) for z in ev], idx=idx)
    finally:
        mp.mp.dps = prev


# Twin configuration: (label, dens_a, dens_b, use_pole).
ZETA_CFG = dict(dens_a=0.25, dens_b=-float(np.log(np.pi)), use_pole=True)
DH_CFG = dict(dens_a=0.75, dens_b=float(np.log(5.0 / np.pi)), use_pole=False)


def match_known(ev, known):
    """Nearest-real-eigenvalue match to a list of known zero heights."""
    reals = sorted([z.real for z in ev if abs(z.imag) < 1e-4 and z.real > 0.3])
    out = []
    for g in known:
        if not reals:
            break
        nearest = min(reals, key=lambda x: abs(x - g))
        out.append((g, nearest, abs(nearest - g)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=10)
    ap.add_argument("--lam", type=float, default=float(np.sqrt(13.0)))
    ap.add_argument("--hp-N", type=int, default=6)
    ap.add_argument("--offline-N", type=int, default=36)
    ap.add_argument("--offline-lam", type=float, default=3.7)
    ap.add_argument("--skip-hp", action="store_true")
    ap.add_argument("--skip-offline", action="store_true")
    args = ap.parse_args()

    t_start = time.time()
    results = {}

    kmax_needed = int(np.floor(max(args.lam, args.offline_lam, 6.0) ** 2)) + 1
    lz, ld = make_streams(max(kmax_needed, 40), float_out=True)
    lz_mp, ld_mp = make_streams(max(kmax_needed, 40), float_out=False)

    print("=" * 74)
    print("E1K: CCM D_log family as a Davenport-Heilbronn testbed")
    print("=" * 74)

    # --- Task 1: K2 / CF-on-D-H feasibility -------------------------------
    print("\n[1] K2 / CF-on-D-H FEASIBILITY (does the machine even RUN on D-H?)")
    kcut = int(np.floor(args.lam ** 2))
    zeta_support = [n for n in range(2, kcut + 1) if abs(lz[n]) > 1e-12]
    dh_support = [n for n in range(2, kcut + 1) if abs(ld[n]) > 1e-12]
    print(f"    cutoff n <= lambda^2 = {kcut}")
    print(f"    ZETA stream support (prime powers only): {zeta_support}")
    print(f"    D-H  stream support (ALL n, dense)      : {dh_support}")
    print(f"    ZETA Lambda[2..8] = {[round(lz[n],4) for n in range(2,9)]}")
    print(f"    D-H  Lambda[2..8] = {[round(ld[n],4) for n in range(2,9)]}  (sign-changing, non-mult)")
    print("    => CF needs only real+even+lower-bounded+simple; NONE reference the")
    print("       Euler product. Both matrices assemble by identical code. RUNS on D-H.")
    results["zeta_support"] = np.array(zeta_support)
    results["dh_support"] = np.array(dh_support)
    results["lz"] = np.array(lz[:kmax_needed])
    results["ld"] = np.array(ld[:kmax_needed])

    # --- Task 2: finite-cutoff reality, side by side (float) --------------
    print("\n[2] FINITE-CUTOFF REALITY  (Thm 5.10(iii): all xihat zeros real)")
    print(f"    N={args.N}  lambda={args.lam:.4f}  (float / numpy.eigh)")
    for label, cfg, stream, known in [("ZETA", ZETA_CFG, lz, ZETA_ZEROS),
                                       ("D-H", DH_CFG, ld, DH_ZEROS)]:
        r = build_float(args.N, args.lam, stream, cfg["dens_a"], cfg["dens_b"], cfg["use_pole"])
        ev, sa = operator_spectrum(r)
        maximag = float(max(abs(z.imag) for z in ev))
        n_real = int(sum(1 for z in ev if abs(z.imag) < 1e-6))
        phys = [z for z in ev if abs(z.real) > 1.0]
        phys_maximag = float(max((abs(z.imag) for z in phys), default=0.0))
        matches = match_known(ev, known[:6])
        flag = "" if r["even_assumption_ok"] else "  [WARN: global min is ODD; using lowest EVEN state]"
        print(f"  {label:5s}: eps_even={r['eps']:+.3e}  gap_even={r['gap_even']:.3e}  even_frac={r['even_frac']:.4f}{flag}")
        print(f"         G-self-adjoint residual={sa:.2e}   real eigs={n_real}/{len(ev)}   max|Im|(phys |re|>1)={phys_maximag:.2e}")
        print(f"         zero matches (known -> operator, err):")
        for g, got, err in matches:
            print(f"             {g:9.4f} -> {got:9.4f}   ({err:.1e})")
        results[f"{label}_ev_re"] = np.array([z.real for z in ev])
        results[f"{label}_ev_im"] = np.array([z.imag for z in ev])
        results[f"{label}_eps"] = r["eps"]
        results[f"{label}_gap_even"] = r["gap_even"]
        results[f"{label}_sa_res"] = sa
        results[f"{label}_even_frac"] = r["even_frac"]
        results[f"{label}_even_ok"] = r["even_assumption_ok"]
        results[f"{label}_phys_maximag"] = phys_maximag

    # --- Task 2b: high-precision reality confirmation ---------------------
    if not args.skip_hp:
        print(f"\n[2b] HIGH-PRECISION reality confirmation (mpmath dps=30, N={args.hp_N})")
        for label, cfg, stream_mp, known in [("ZETA", ZETA_CFG, lz_mp, ZETA_ZEROS),
                                             ("D-H", DH_CFG, ld_mp, DH_ZEROS)]:
            rh = build_hp(args.hp_N, mp.sqrt(13), stream_mp, cfg["dens_a"],
                          -mp.log(mp.pi) if label == "ZETA" else mp.log(5 / mp.pi),
                          cfg["use_pole"], dps=30)
            ev = rh["ev"]
            maximag = max(abs(z.imag) for z in ev)
            phys = [z for z in ev if abs(z.real) > 1.0]
            phys_maximag = max((abs(z.imag) for z in phys), default=0.0)
            n_real = sum(1 for z in ev if abs(z.imag) < 1e-8)
            print(f"  {label:5s}: eps={rh['eps'].real:+.3e}  gap={rh['gap'].real:.3e}")
            print(f"         real eigs={n_real}/{len(ev)}   max|Im|(physical |re|>1)={phys_maximag:.2e}   max|Im|(all)={maximag:.2e}")
            m = match_known(ev, known[:5])
            print(f"         zero matches: " + ", ".join(f"{g:.3f}->{got:.3f}" for g, got, _ in m))
            results[f"{label}_hp_ev_re"] = np.array([z.real for z in ev])
            results[f"{label}_hp_ev_im"] = np.array([z.imag for z in ev])
            results[f"{label}_hp_phys_maximag"] = phys_maximag

    # --- Task 3: lambda-sweep (lower-boundedness + simplicity probe) ------
    print("\n[3] LAMBDA SWEEP  (lower-boundedness sign of eps; simplicity via gap)")
    lam_grid = [1.6, 2.0, 2.5, 3.0, 3.6, 4.2, 5.0]
    Nsweep = 8
    sweep = {"lam": [], "ZETA_eps": [], "ZETA_gap": [], "DH_eps": [], "DH_gap": [],
             "ZETA_even_ok": [], "DH_even_ok": []}
    print(f"    N={Nsweep}   (eps>0 = locally lower-bounded; gap = distance to 2nd eigenvalue;")
    print("                   'o' flags global min ODD = 'assumed even' hypothesis fails)")
    print("     lam    kmax   ZETA_eps    ZETA_gap    DH_eps      DH_gap")
    for lam in lam_grid:
        rz = build_float(Nsweep, lam, lz, ZETA_CFG["dens_a"], ZETA_CFG["dens_b"], ZETA_CFG["use_pole"])
        rd = build_float(Nsweep, lam, ld, DH_CFG["dens_a"], DH_CFG["dens_b"], DH_CFG["use_pole"])
        sweep["lam"].append(lam)
        sweep["ZETA_eps"].append(rz["eps_global"]); sweep["ZETA_gap"].append(rz["gap"])
        sweep["DH_eps"].append(rd["eps_global"]); sweep["DH_gap"].append(rd["gap"])
        sweep["ZETA_even_ok"].append(rz["even_assumption_ok"])
        sweep["DH_even_ok"].append(rd["even_assumption_ok"])
        fz = " " if rz["even_assumption_ok"] else "o"
        fd = " " if rd["even_assumption_ok"] else "o"
        print(f"    {lam:4.2f}   {int(lam*lam):3d}   {rz['eps_global']:+.3e}{fz} {rz['gap']:.3e}  {rd['eps_global']:+.3e}{fd} {rd['gap']:.3e}")
    for k, v in sweep.items():
        results[f"sweep_{k}"] = np.array(v)

    # --- Task 4: off-line-zero probe (reach the height ~85.7) -------------
    if not args.skip_offline:
        print(f"\n[4] OFF-LINE PROBE  (N={args.offline_N}, lambda={args.offline_lam}: spectral range covers 85.7)")
        print("    D-H off-line zero: s=0.808+85.699i  =>  z-plane 85.699 - 0.308 i (COMPLEX)")
        for label, cfg, stream in [("D-H", DH_CFG, ld), ("ZETA", ZETA_CFG, lz)]:
            r = build_float(args.offline_N, args.offline_lam, stream, cfg["dens_a"], cfg["dens_b"], cfg["use_pole"])
            ev, sa = operator_spectrum(r)
            top = max(z.real for z in ev)
            near = [z for z in ev if 70 < z.real < 100]
            print(f"  {label:5s}: eps={r['eps']:+.3e}  top eig re={top:.1f}  G-sa res={sa:.2e}")
            print(f"         eigenvalues in (70,100):")
            for z in sorted(near, key=lambda z: z.real):
                fl = "" if abs(z.imag) < 1e-4 else "  <-COMPLEX"
                print(f"             re={z.real:9.4f}  im={z.imag:+.3e}{fl}")
            results[f"offline_{label}_ev_re"] = np.array([z.real for z in ev])
            results[f"offline_{label}_ev_im"] = np.array([z.imag for z in ev])

    results["meta_N"] = args.N
    results["meta_lam"] = args.lam
    results["dh_offline_re"] = DH_OFFLINE.real
    results["dh_offline_im"] = DH_OFFLINE.imag

    np.savez_compressed(OUT, **results)
    print(f"\nSaved -> {OUT}")
    print(f"Total time {round(time.time()-t_start,1)}s")


if __name__ == "__main__":
    main()
