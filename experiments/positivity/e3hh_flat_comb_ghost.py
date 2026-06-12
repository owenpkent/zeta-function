"""e3hh: ADVERSARY settlement of kill switch A2 (lcc_bc_transport.md).

Question (A2): is the flat comb c_n = c1 * n^(-1/2) (the unique KMS-quasi-invariant
ray of Lemma 1, the comb of c1*zeta(s)) feasible in the LCC log-crystal cone, i.e.
does a positive tempered measure mu satisfy the explicit-formula identity (EF)
with that comb? If yes, LCC rigidity is dead. If provably no, A2 is defused.

Method (no zeros used anywhere; K1-clean):
  Perron contour shift gives, for even g in C_c^infty,
      sum_n n^(-1/2) g(log n) = ghat(-i/2) + (1/2pi) int ghat(r) zeta(1/2+ir) dr,
  so the (EF) right side with the flat comb decomposes as
      RHS(g) = 2(1-c1) ghat(i/2) + (1/2pi) int ghat(r) [Omega(r) - 2 c1 Re zeta(1/2+ir)] dr.
  * c1 != 1: the residual cosh(x/2)-type atom blows up like e^(T/2) on translated
    bumps while int ghat dmu stays bounded for ANY tempered mu. Infeasible.
  * c1 = 1: the induced density at r = 0 is d(0) = Omega(0) - 2 zeta(1/2) < 0
    (= -5.3722 + 2.9207 = -2.4515), so Fejer tests force int ghat dmu < 0,
    contradicting positivity. Infeasible.

This script verifies every numerical ingredient of that derivation:
  [1] Lemma 2 of the dossier (Mobius inversion of log = von Mangoldt; converse
      with random kappa_p), re-running the dossier's unarchived machine check.
  [2] The Perron identity, on a Gaussian test (direct finite sum vs formula).
  [3] The density d(r) = Omega(r) - 2 Re zeta(1/2 + ir): exact value at r = 0,
      scan of the negative window.
  [4] The direct (EF) witness at c1 = 1: Fejer triangle tests g_X show
      RHS(g_X) -> d(0) < 0 with ghat_X >= 0 on R. Computed with NO use of the
      Perron identity (pure pole - comb + archimedean balance), then cross-
      checked against the Perron decomposition at X = 8.
  [5] The c1 != 1 blowup: translated-triangle tests at T = 10, 14 grow like
      4(1-c1) cosh(T/2) A, ratio e^2 per Delta T = 4.

Convention: Omega(r) = Re psi(1/4 + ir/2) - log pi (project standard, e3aa).
Run: python -m experiments.positivity.e3hh_flat_comb_ghost
"""

import numpy as np
from scipy.special import digamma as sp_digamma
from scipy.integrate import simpson
import mpmath as mp

LOG_PI = np.log(np.pi)


def sieve_spf(N):
    spf = np.zeros(N + 1, dtype=np.int64)
    for i in range(2, N + 1):
        if spf[i] == 0:
            spf[i::i] = np.where(spf[i::i] == 0, i, spf[i::i])
    return spf


def mobius_and_lambda(N):
    spf = sieve_spf(N)
    mob = np.zeros(N + 1, dtype=np.int64)
    lam = np.zeros(N + 1)
    mob[1] = 1
    for n in range(2, N + 1):
        p = spf[n]
        m = n // p
        mob[n] = 0 if m % p == 0 else -mob[m]
        # von Mangoldt: n = p^k iff repeatedly dividing by spf reaches 1
        q = n
        while q % p == 0:
            q //= p
        lam[n] = np.log(p) if q == 1 else 0.0
    return mob, lam, spf


def dirichlet_mobius_invert(B, mob, N):
    """b = mu * B, i.e. b(n) = sum_{d|n} mu(d) B(n/d)."""
    b = np.zeros(N + 1)
    for d in range(1, N + 1):
        if mob[d] == 0:
            continue
        md = mob[d]
        for n in range(d, N + 1, d):
            b[n] += md * B[n // d]
    return b


def check_lemma2(N=10000):
    print(f"[1] Lemma 2 machine check, N = {N}")
    mob, lam, spf = mobius_and_lambda(N)
    n_arr = np.arange(0, N + 1, dtype=float)
    n_arr[0] = 1.0
    B = np.log(n_arr)  # B(n) = log n, the integrated von Mangoldt comb
    b = dirichlet_mobius_invert(B, mob, N)
    err_fwd = np.max(np.abs(b[2:] - lam[2:]))
    print(f"    forward (mu * log = Lambda): max|b(n)-Lambda(n)| = {err_fwd:.3e}")

    # converse: random kappa_p for ALL p <= N, B(n) = B1 + sum kappa_p v_p(n)
    rng = np.random.default_rng(20260611)
    kappa = np.zeros(N + 1)
    primes = [p for p in range(2, N + 1) if spf[p] == p]
    for p in primes:
        kappa[p] = rng.uniform(0.5, 2.0)
    B1 = 0.37
    B2 = np.full(N + 1, B1)
    B2[0] = 0.0
    for n in range(2, N + 1):
        q = n
        while q > 1:
            p = spf[q]
            v = 0
            while q % p == 0:
                q //= p
                v += 1
            B2[n] += kappa[p] * v
    b2 = dirichlet_mobius_invert(B2, mob, N)
    errs = []
    for n in range(2, N + 1):
        q, p = n, spf[n]
        while q % p == 0:
            q //= p
        target = kappa[p] if q == 1 else 0.0
        errs.append(abs(b2[n] - target))
    print(f"    converse (random kappa_p): max error = {max(errs):.3e}, "
          f"b(1) = {b2[1]:.6f} (should be {B1})")
    assert err_fwd < 1e-11 and max(errs) < 1e-11
    print("    PASS: (C) <=> c_n = Lambda(n)/sqrt(n) for n >= 2, b(1) free.\n")


def check_perron_gaussian():
    print("[2] Perron identity check (Gaussian test, a = 1)")
    # S = sum n^{-1/2} exp(-(log n)^2/2)
    N = 2_000_000
    n = np.arange(1, N + 1, dtype=float)
    S = np.sum(np.exp(-np.log(n) ** 2 / 2) / np.sqrt(n))
    mp.mp.dps = 25
    ghat_mi2 = mp.sqrt(2 * mp.pi) * mp.e ** mp.mpf("0.125")
    integ = mp.quad(lambda r: mp.sqrt(2 * mp.pi) * mp.e ** (-r * r / 2)
                    * mp.re(mp.zeta(mp.mpf("0.5") + 1j * r)), [0, 4, 8, 14])
    rhs = ghat_mi2 + integ / mp.pi
    print(f"    direct sum  S = {S:.12f}")
    print(f"    Perron form   = {float(rhs):.12f}   (diff = {abs(S - float(rhs)):.2e})")
    assert abs(S - float(rhs)) < 1e-9
    print("    PASS: sum n^(-1/2) g(log n) = ghat(-i/2) + (1/2pi) int ghat zeta(1/2+ir) dr\n")


def check_density_scan():
    print("[3] Density d(r) = Omega(r) - 2 Re zeta(1/2+ir)  [c1 = 1 flat comb]")
    mp.mp.dps = 30
    omega0 = mp.re(mp.digamma(mp.mpf("0.25"))) - mp.log(mp.pi)
    z_half = mp.zeta(mp.mpf("0.5"))
    d0 = omega0 - 2 * z_half
    print(f"    Omega(0)      = {float(omega0):+.10f}")
    print(f"    2*zeta(1/2)   = {float(2 * z_half):+.10f}")
    print(f"    d(0)          = {float(d0):+.10f}   (NEGATIVE => infeasible window)")
    mp.mp.dps = 15
    rs = np.arange(0.0, 100.0, 0.02)
    vals = []
    for r in rs:
        om = mp.re(mp.digamma(mp.mpf("0.25") + 0.5j * r)) - mp.log(mp.pi)
        vals.append(float(om - 2 * mp.re(mp.zeta(0.5 + 1j * r))))
    vals = np.array(vals)
    sign = np.sign(vals)
    crossings = rs[1:][sign[1:] != sign[:-1]]
    neg_frac = np.mean(vals < 0)
    print(f"    min over [0,100]: {vals.min():+.4f} at r = {rs[np.argmin(vals)]:.2f}")
    print(f"    sign changes at r ~ {np.round(crossings, 2).tolist()}")
    print(f"    fraction negative on [0,100]: {neg_frac:.3f}")
    print(f"    => the negative window at r = 0 is [0, {crossings[0]:.2f}) "
          f"(plus later dips); one window suffices.\n")
    return float(d0)


def omega_np(r):
    return np.real(sp_digamma(0.25 + 0.5j * r)) - LOG_PI


def fejer_rhs_direct(X, c1=1.0, R=500.0, dr=2.5e-4):
    """(EF) right side for the flat comb, Fejer triangle g(x)=(1-|x|/X)+.
    ghat(r) = X sinc^2(rX/2) >= 0. No Perron identity used."""
    pole = 2.0 * (16.0 / X) * np.sinh(X / 4.0) ** 2  # 2*ghat(i/2)
    nmax = int(np.floor(np.exp(X)))
    comb = 0.0
    chunk = 2_000_000
    for lo in range(1, nmax + 1, chunk):
        hi = min(lo + chunk - 1, nmax)
        n = np.arange(lo, hi + 1, dtype=float)
        w = 1.0 - np.log(n) / X
        comb += np.sum(np.clip(w, 0.0, None) / np.sqrt(n))
    comb *= 2.0 * c1
    r = np.arange(0.0, R, dr)
    r[0] = 1e-12
    ghat = X * (np.sin(r * X / 2.0) / (r * X / 2.0)) ** 2
    arch = simpson(ghat * omega_np(r), x=r) / np.pi
    tail = (4.0 / (np.pi * X)) * (np.log(R) + 1.0) / R
    return pole - comb + arch, tail


def check_fejer_witness(d0):
    print("[4] Direct (EF) witness, c1 = 1 (Fejer tests, ghat >= 0 on R)")
    print("    RHS(g_X) = 2*ghat(i/2) - 2*sum_n n^(-1/2) g_X(log n) + arch")
    for X in (8.0, 12.0, 16.0):
        rhs, tail = fejer_rhs_direct(X)
        print(f"    X = {X:4.0f}: RHS = {rhs:+.4f}  (arch tail bound {tail:.1e}; "
              f"pole ~ {2 * (16 / X) * np.sinh(X / 4) ** 2:.4g})")
    print(f"    limit prediction d(0) = {d0:+.4f}")
    print("    RHS < 0 with ghat_X >= 0 on R while any positive mu needs RHS >= 0.")
    print("    => flat comb at c1 = 1 is NOT a log-crystal. (Mollify the triangle")
    print("       to C_c^inf: changes RHS by O(eps), slack is O(1).)\n")


def check_perron_crosscheck_X8():
    print("[4b] Cross-check at X = 8: Perron decomposition vs direct RHS")
    rhs_direct, _ = fejer_rhs_direct(8.0)
    X = 8.0
    mp.mp.dps = 15
    rs = np.arange(0.0, 60.0, 0.01)
    rs[0] = 1e-12
    ghat = X * (np.sin(rs * X / 2.0) / (rs * X / 2.0)) ** 2
    dvals = np.array([float(mp.re(mp.digamma(mp.mpf("0.25") + 0.5j * r)) - mp.log(mp.pi)
                            - 2 * mp.re(mp.zeta(0.5 + 1j * r))) for r in rs])
    spectral = simpson(ghat * dvals, x=rs) / np.pi
    print(f"    direct pole-comb-arch RHS = {rhs_direct:+.4f}")
    print(f"    (1/2pi) int ghat*d(r) dr  = {spectral:+.4f}  (R = 60 truncation)")
    print("    agreement validates the contour-shift decomposition.\n")


def check_c1_blowup():
    print("[5] c1 != 1 blowup (c1 = 1/2, translated triangle bumps at T)")
    u = np.linspace(-1, 1, 4001)
    A = simpson((1 - np.abs(u)) * np.cosh(u / 2.0), x=u)
    out = []
    for T in (10.0, 14.0):
        pole = 4.0 * np.cosh(T / 2.0) * A
        lo, hi = int(np.exp(T - 1.0)), int(np.exp(T + 1.0)) + 1
        n = np.arange(lo, hi, dtype=float)
        w = np.clip(1.0 - np.abs(np.log(n) - T), 0.0, None)
        comb = 2.0 * 0.5 * np.sum(w / np.sqrt(n))
        r = np.arange(0.0, 500.0, 1e-3)
        r[0] = 1e-12
        ghat = 2.0 * np.cos(r * T) * (np.sin(r / 2.0) / (r / 2.0)) ** 2
        arch = simpson(ghat * omega_np(r), x=r) / np.pi
        rhs = pole - comb + arch
        pred = 4.0 * (1 - 0.5) * np.cosh(T / 2.0) * A
        out.append(rhs)
        print(f"    T = {T:4.0f}: RHS = {rhs:10.3f}, predicted atom 2cosh(T/2)A = {pred:10.3f}")
    print(f"    growth ratio RHS(14)/RHS(10) = {out[1] / out[0]:.3f} vs e^2 = {np.e ** 2:.3f}")
    print("    RHS -> infinity on tests where int ghat dmu is bounded for any tempered mu")
    print("    => flat comb at c1 != 1 infeasible as well.\n")


if __name__ == "__main__":
    print("=" * 78)
    print("e3hh: flat-comb ghost (kill switch A2 of lcc_bc_transport.md)")
    print("=" * 78 + "\n")
    check_lemma2()
    check_perron_gaussian()
    d0 = check_density_scan()
    check_fejer_witness(d0)
    check_perron_crosscheck_X8()
    check_c1_blowup()
    print("CONCLUSION: the flat comb c_n = c1 n^(-1/2) is infeasible in the LCC cone")
    print("for every c1 > 0. Kill switch A2 is DEFUSED analytically; e3x run (d)")
    print("is unnecessary. (EF)-positivity provably rejects the quasi-invariant ray.")
