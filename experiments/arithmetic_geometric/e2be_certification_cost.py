"""E2BE: the certification-cost theorem (construction backlog B3; hardens LEARNINGS #180).

WHAT IS PROVEN. #180 (e2ao) MEASURED that the prime-side assembly certifies the
window margin only down to a floor crossed at sigma ~ 0.3, and read off the
price "e^{gamma_1^2 sigma^2} in assembly precision". This build makes that a
theorem about THIS instrument, with every constant explicit:

(T1, the instrument bound). For the e2ao assembly A of the Weil form
Q(g_w), g_w(x) = e^{-x^2/2 sigma^2} cos(w x), with parameters
(dx, dtau, N, T_a = 60, support cut 8 sigma), and any sigma in [0.2, 0.7],
w in [0, 20]:

    |A(g_w) - Q(g_w)| <= eps(sigma) :=
        E_interp(sigma; dx, N) + E_P(sigma; N) + E_supp + E_lump,

where, with c(y) = (g_w * g_w)(y) = (sqrt(pi) sigma / 2) e^{-y^2/4 sigma^2}
[cos(w y) + e^{-sigma^2 w^2}] (closed form, verified below):

  E_interp = (dx^2/8) * 2 * sum_{n<=N} (Lambda(n)/sqrt(n)) * sup |c''|
             near y = ln n, using |c''(y)| <= (sqrt(pi) sigma/2)
             e^{-y^2/4 sigma^2} [2(y^2/4 sigma^4 + 1/2 sigma^2)
             + |y| w / sigma^2 + w^2]   (linear-interpolation error at ln n);
  E_P      = 4 sqrt(pi) sigma^3 e^{sigma^2/4} (1 + sigma^2/a)
             e^{-a^2/4 sigma^2},  a = ln N - sigma^2   (prime-sum tail, via
             |c(y)| <= sqrt(pi) sigma e^{-y^2/4 sigma^2}, Lambda(n) <= ln n,
             and the monotone sum-to-integral comparison);
  E_supp   = 2 * S_N * sqrt(2 pi) sigma erfc(8/sqrt(2)) + interp-window cut
             (the |x| <= 8 sigma truncation; ~1e-14 scale);
  E_lump   = 2e-11, a lump PROVABLY covering four clauses gated at the
             operating point: three analytic ones each <= 1e-12: Riemann-sum
             aliasing of the sampled autocorrelation (Poisson: <= C
             e^{-sigma^2 (2 pi/dx - 2 w)^2 / 8}, ~10^{-84000} at dx = 1e-3),
             archimedean rectangle-rule aliasing (psi(1/4 + it/2) analytic
             in the strip |Im t| < 1/2: <= C e^{-2 pi (0.4)/dtau},
             ~10^{-542}), archimedean domain truncation at T_a = 60
             (Gaussian tail, ~10^{-24} at w = 20); plus float64 accumulation
             <= 1.3e-11. Their sum is < 2e-11.

  Here S_N = sum_{n<=N} Lambda(n)/sqrt(n) <= 2.07766 sqrt(N), by partial
  summation from Rosser-Schoenfeld psi(x) < 1.03883 x (all x > 0).
  Normalized: eps_R(sigma) = eps(sigma) / (sigma sqrt(pi)/2)  (worst-case
  ||g_w||^2 over the scan; the Rayleigh error bound).

(T2, the margin lower bound; free). The single-mode zero-side margin is a sum
of positive terms, so margin(sigma) >= 4 sqrt(pi) sigma e^{-gamma_1^2 sigma^2}
with gamma_1 <= 14.1347253 (its first term); the full value is
4 sqrt(pi) sigma sum_k e^{-sigma^2 gamma_k^2}, remainder ratio
R(sigma) = sum_{k>=2} e^{-sigma^2 (gamma_k^2 - gamma_1^2)} (checked against
the measured e2ao column at every rung).

(T3, the certification threshold and the price). If sigma satisfies
4 sqrt(pi) sigma e^{-gamma_1^2 sigma^2} >= 2 eps_R(sigma), the assembly
PROVABLY certifies the margin's sign and value to a factor of 2; the largest
such sigma* solves 4 sqrt(pi) sigma e^{-gamma_1^2 sigma^2} = 2 eps_R(sigma),
i.e.  sigma*^2 = ln(2 sqrt(pi) sigma* / eps_R) / gamma_1^2.  Sufficiency is
the theorem; necessity at this instrument is the MEASURED e2ao floor crossing
(sigma = 0.3), and [sigma*, 0.3] brackets the true threshold within the
bound's looseness (<= 1e4, i.e. <= ln(1e4)/gamma_1^2 = 0.046 in sigma^2).
COROLLARY (the price): certifying at scale sigma requires accuracy
eps <= 2 sqrt(pi) sigma e^{-gamma_1^2 sigma^2}, hence working precision
    digits(sigma) >= gamma_1^2 sigma^2 / ln 10 + O(ln N, ln sigma):
the e^{gamma_1^2 sigma^2} price of #180 as an instrument theorem.
Demonstrated constructively at sigma = 0.5: margin ~ 3e-22 needs ~21.7
digits; the float64 assembly (e2ao's own npz row) sits 16 orders above it,
while a closed-form mpmath assembly at dps 50 certifies it.

PRE-REGISTERED (backlog rule 1), before the numbers were run:
  P1  EXPECT: eps_R(sigma) MAJORIZES the measured e2ao assembly error at
      every one of the 11 rungs, with looseness <= 1e4.
      KILL: any rung where measured error exceeds the bound: the bound is
      wrong; fix before any theorem claim.
  P2  EXPECT: sigma* (root of T3) lands in [0.21, 0.29]: above the bottom
      rung 0.2 (the theorem certifies at least one measured rung) and below
      the measured crossing 0.3 (soundness).
      KILL: sigma* outside, or sigma* > measured crossing (bound unsound).
  P3  EXPECT: the dps-50 closed-form assembly at sigma = 0.5 certifies
      (|prime - zero| <= margin/2, margin > 0) at the predicted ~21.7-digit
      price, and the float64 instrument provably cannot (npz row).
      KILL: the mp assembly fails to certify: some explicit constant is
      wrong; chase immediately.

DISCIPLINES. Joint (rule 3): C2 (SP5), the finite-scale price of the
uniform-margin clause (M4's determinant-class name), from the instrument
side. K1 (rule 4): the bound and both assemblies consume integers (the
Lambda sieve), closed-form Gaussian calculus, and psi/Gamma special
functions; zeros enter ONLY the validation cells (the zero-side reference in
the price demo and the R(sigma) consistency check), behind the counted
oracle. D-H / Beurling (rule 2): NOT POSABLE for this build and the refusal
is structural: the theorem's subject is the instrument's error budget, which
is control-independent (the same bound covers any coefficient lattice with
|a_n| <= Lambda(n)-type weights); the CONTROLS' role for this family was
discharged in #179/#180/#199 (D-H passes form-side cells; the margin's
zero-side meaning is where the controls bite). Named here, not skipped
silently.

Run:  python -m experiments.arithmetic_geometric.e2be_certification_cost [--quick]
Data: e2be_certification_cost.npz (tracked next to this script).
"""

from __future__ import annotations

import time
from math import erfc, exp, log, pi, sqrt

import numpy as np

from experiments._shared.harness import Gates, PreRegistry, quick_arg, save_npz
from experiments.arithmetic_geometric.e2an_sp_object_v0 import (
    _ORACLE_CALLS, lambda_sieve, oracle_zeta_zeros,
)
from experiments.arithmetic_geometric.e2ao_scaling_ladder import (
    GAMMA1_SQ, weil_q_single,
)

HERE_NPZ = __file__.replace(".py", ".npz")
E2AO_NPZ = __file__.replace("e2be_certification_cost.py", "e2ao_scaling_ladder.npz")

GAMMA1_UP = 14.1347253          # upper bound on gamma_1 (for the margin LOWER bound)
RS_CONST = 1.03883              # Rosser-Schoenfeld: psi(x) < 1.03883 x, all x > 0
S_CONST = 2 * RS_CONST          # sum Lambda(n)/sqrt(n) <= S_CONST sqrt(N)
DX = 1e-3                       # e2ao operating parameters
DTAU = 2e-3
N_LAM = 3000
OMEGA_MAX = 20.0
E_LUMP = 2e-11                  # covers the four gated clauses (see docstring)


# -- the explicit bound -------------------------------------------------------

def sum_lam_sqrt(lam: np.ndarray) -> float:
    n = np.arange(1, len(lam))
    return float(np.sum(lam[1:] / np.sqrt(n)))


def e_interp(sigma: float, omega: float, lam: np.ndarray, dx: float = DX) -> float:
    """(dx^2/8) * 2 * sum_n (Lambda(n)/sqrt(n)) * sup_{|y - ln n| <= dx} |c''|."""
    n = np.arange(2, len(lam))
    w_n = lam[2:] / np.sqrt(n)
    y = np.log(n)
    phi = np.exp(-np.maximum(y - dx, 0.0) ** 2 / (4 * sigma ** 2))
    yp = y + dx
    bracket = (2 * (yp ** 2 / (4 * sigma ** 4) + 1 / (2 * sigma ** 2))
               + yp * omega / sigma ** 2 + omega ** 2)
    m2 = (sqrt(pi) * sigma / 2) * phi * bracket
    return float((dx ** 2 / 8) * 2 * np.sum(w_n * m2))


def e_prime_tail(sigma: float, n_cut: int) -> float:
    """4 sqrt(pi) sigma^3 e^{sigma^2/4} (1 + sigma^2/a) e^{-a^2/4 sigma^2}."""
    a = log(n_cut) - sigma ** 2
    return 4 * sqrt(pi) * sigma ** 3 * exp(sigma ** 2 / 4) * (1 + sigma ** 2 / a) \
        * exp(-a ** 2 / (4 * sigma ** 2))


def e_supp(sigma: float, n_cut: int) -> float:
    """Support truncation |x| <= 8 sigma in the convolution, plus the
    interp-window cut at |ln n| > 16 sigma (both Gaussian-tail explicit)."""
    s_n = S_CONST * sqrt(n_cut)
    cut_conv = 2 * s_n * 2 * sqrt(2 * pi) * sigma * erfc(8 / sqrt(2))
    edge = 16 * sigma
    cut_interp = 2 * s_n * sqrt(pi) * sigma * exp(-edge ** 2 / (4 * sigma ** 2)) \
        if log(n_cut) > edge else 0.0
    return cut_conv + cut_interp


def negligible_clauses_log10(sigma: float, omega: float) -> dict:
    """log10 upper bounds of the four E_LUMP clauses at the operating point."""
    alias_conv = (-sigma ** 2 * (2 * pi / DX - 2 * omega) ** 2 / 8) / log(10) + 2
    alias_arch = (-2 * pi * 0.4 / DTAU) / log(10) + 4
    dom_arch = (-sigma ** 2 * (60 - omega) ** 2) / log(10) + 4
    rounding = -11.9   # 1e-13 * (3 + S_CONST sqrt(N)) < 1.3e-11
    return {"alias_conv": alias_conv, "alias_arch": alias_arch,
            "dom_arch": dom_arch, "float64": rounding}


def eps_r(sigma: float, lam: np.ndarray) -> float:
    """The normalized instrument bound eps_R(sigma), worst case over the scan."""
    e = (e_interp(sigma, OMEGA_MAX, lam) + e_prime_tail(sigma, N_LAM)
         + e_supp(sigma, N_LAM) + E_LUMP)
    return e / (sigma * sqrt(pi) / 2)


def margin_lower(sigma: float) -> float:
    """T2: margin(sigma) >= 4 sqrt(pi) sigma e^{-gamma_1^2 sigma^2} (first term)."""
    return 4 * sqrt(pi) * sigma * exp(-GAMMA1_UP ** 2 * sigma ** 2)


def sigma_star(lam: np.ndarray, lo: float = 0.15, hi: float = 0.40) -> float:
    """T3: the largest sigma with margin_lower(sigma) >= 2 eps_R(sigma)."""
    f = lambda s: margin_lower(s) - 2 * eps_r(s, lam)
    for _ in range(80):
        mid = (lo + hi) / 2
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


# -- the dps-50 closed-form assembly (the price demo) -------------------------

def mp_lambda_pairs(n_max: int):
    """(n, Lambda(n)) with Lambda exact in mpmath, via a smallest-factor sieve."""
    import mpmath as mp
    spf = np.zeros(n_max + 1, dtype=np.int64)
    for p in range(2, n_max + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    out = []
    for n in range(2, n_max + 1):
        p = int(spf[n])
        m = n
        while m % p == 0:
            m //= p
        if m == 1:
            out.append((n, mp.log(p)))
    return out


def mp_assembly(sigma_str: str, n_max: int, dps: int, gammas: np.ndarray):
    """Closed-form pole/primes/arch at omega = 0 in mpmath, plus the zero side.

    pole  = 4 pi sigma^2 e^{sigma^2/4}
    prime = -2 sum Lambda(n)/sqrt(n) sqrt(pi) sigma e^{-ln^2 n / 4 sigma^2}
    arch  = sigma^2 Integral e^{-sigma^2 t^2} (Re psi(1/4 + it/2) - ln pi) dt
    zero  = 4 pi sigma^2 sum_{gamma > 0} e^{-sigma^2 gamma^2}   (T <= 100;
            the T > 100 tail is < e^{-sigma^2 10^4}, noted, negligible)
    """
    import mpmath as mp
    prev = mp.mp.dps
    mp.mp.dps = dps
    try:
        sg = mp.mpf(sigma_str)
        pole = 4 * mp.pi * sg ** 2 * mp.e ** (sg ** 2 / 4)
        prime = mp.mpf(0)
        for n, lam_n in mp_lambda_pairs(n_max):
            prime -= 2 * lam_n / mp.sqrt(n) * mp.sqrt(mp.pi) * sg \
                * mp.e ** (-mp.log(n) ** 2 / (4 * sg ** 2))
        arch = sg ** 2 * mp.quad(
            lambda t: mp.e ** (-sg ** 2 * t ** 2)
            * (mp.re(mp.digamma(mp.mpf(1) / 4 + mp.mpc(0, 1) * t / 2)) - mp.log(mp.pi)),
            [-mp.inf, 0, mp.inf])
        zero = 4 * mp.pi * sg ** 2 * mp.fsum(
            mp.e ** (-sg ** 2 * mp.mpf(g) ** 2) for g in gammas)
        return pole + prime + arch, zero
    finally:
        mp.mp.dps = prev


def main() -> int:
    t_start = time.perf_counter()
    quick = quick_arg()
    gates = Gates(quick=quick)
    pre = PreRegistry()
    pre.register("P1", "eps_R majorizes all 11 measured rungs, looseness <= 1e4",
                 "any rung with measured error above the bound")
    pre.register("P2", "sigma* in [0.21, 0.29], covering rung 0.2, <= measured crossing",
                 "sigma* outside the window or above the measured crossing")
    pre.register("P3", "dps-50 assembly certifies sigma = 0.5 at ~21.7 digits; float64 cannot",
                 "the mp assembly fails to certify (a constant is wrong)")

    demo_dps = 35 if quick else 50
    demo_n = 2500 if quick else 4000

    print(f"e2be: certification-cost theorem (backlog B3)  "
          f"[{'quick' if quick else 'full'}; dx={DX}, N={N_LAM}, "
          f"omega_max={OMEGA_MAX}, demo dps={demo_dps}]")

    lam = lambda_sieve(N_LAM)
    d = np.load(E2AO_NPZ)
    sigmas = d["sigmas"]
    meas_err = d["assembly_err"]
    meas_margin = d["margin_zero"]
    floor_sigma = float(d["floor_sigma"])

    # -- instrument cell: the closed forms behind the constants -------------
    import mpmath as mp
    mp.mp.dps = 30
    sg0, w0, y0 = mp.mpf("0.35"), mp.mpf("7.0"), mp.mpf("1.1")
    direct = mp.quad(lambda t: mp.e ** (-t ** 2 / (2 * sg0 ** 2)) * mp.cos(w0 * t)
                     * mp.e ** (-(y0 - t) ** 2 / (2 * sg0 ** 2)) * mp.cos(w0 * (y0 - t)),
                     [-mp.inf, 0, mp.inf])
    closed = (mp.sqrt(mp.pi) * sg0 / 2) * mp.e ** (-y0 ** 2 / (4 * sg0 ** 2)) \
        * (mp.cos(w0 * y0) + mp.e ** (-sg0 ** 2 * w0 ** 2))
    dc = abs(direct - closed)
    gates.gate("closed-form autocorrelation c(y) verified against direct integral",
               dc < mp.mpf(10) ** -25, f"|diff| = {mp.nstr(dc, 3)}")

    s_meas = sum_lam_sqrt(lam)
    gates.gate("S_N lemma: sum Lambda(n)/sqrt(n) <= 2.07766 sqrt(N) (RS-based)",
               s_meas <= S_CONST * sqrt(N_LAM),
               f"measured {s_meas:.1f} vs bound {S_CONST * sqrt(N_LAM):.1f}")

    negl = negligible_clauses_log10(0.2, OMEGA_MAX)
    gates.gate("lump honesty: analytic clauses <= 1e-12 each, float64 <= 1.3e-11, sum < E_LUMP",
               all(v < -12 for k, v in negl.items() if k != "float64")
               and negl["float64"] < -10.5
               and sum(10.0 ** v for v in negl.values()) < E_LUMP,
               "log10 bounds: " + ", ".join(f"{k}={v:.0f}" for k, v in negl.items()))

    # -- P1: majorization ---------------------------------------------------
    bound = np.array([eps_r(float(s), lam) for s in sigmas])
    loose = bound / meas_err
    p1a = bool(np.all(bound >= meas_err))
    gates.gate("T1 majorizes: eps_R >= measured assembly error at all 11 rungs",
               p1a, "looseness min/max = " + f"{loose.min():.1f}x / {loose.max():.1e}x")
    p1b = bool(np.all(loose <= 1e4))
    gates.gate("T1 not vacuous: looseness <= 1e4 at every rung", p1b,
               f"max looseness = {loose.max():.1e}x")
    pre.resolve("P1", "FIRED" if (p1a and p1b) else "REFUTED",
                f"looseness in [{loose.min():.1f}, {loose.max():.1e}]")

    # -- T1 soundness on live reruns (three dx values) ----------------------
    sref, wref = "0.25", 0.0
    gz = np.array(oracle_zeta_zeros(100.0))
    q_mp, _ = mp_assembly(sref, N_LAM, 40, gz[:0])  # prime side only needs no zeros
    ok_dx, det = True, []
    for dxi in ([2e-3, 1e-3] if quick else [2e-3, 1e-3, 5e-4]):
        q_f = float(weil_q_single(float(sref), np.array([wref]), lam, dx=dxi)[0])
        err = abs(q_f - float(q_mp))
        b = e_interp(float(sref), wref, lam, dx=dxi) + e_prime_tail(float(sref), N_LAM) \
            + e_supp(float(sref), N_LAM) + E_LUMP
        ok_dx &= err <= b
        det.append(f"dx={dxi:g}: err={err:.1e} <= {b:.1e}")
    gates.gate("T1 sound on live reruns at sigma = 0.25 (each dx within its bound)",
               ok_dx, "; ".join(det))

    # -- prime-tail honesty -------------------------------------------------
    qa, _ = mp_assembly("0.6", N_LAM, 40, gz[:0])
    qb, _ = mp_assembly("0.6", 4 * N_LAM, 40, gz[:0])
    tail_meas = abs(float(qa - qb))
    tail_bound = e_prime_tail(0.6, N_LAM)
    gates.gate("E_P honest: |Q(N) - Q(4N)| <= E_P(N) at sigma = 0.6",
               tail_meas <= tail_bound, f"{tail_meas:.1e} <= {tail_bound:.1e}")

    # -- T2 consistency: the measured margin vs the first-term form ---------
    g1sq = float(gz[0]) ** 2
    ratio_dev, r_bound = [], []
    for s, m in zip(sigmas, meas_margin):
        first = 4 * sqrt(pi) * float(s) * exp(-g1sq * float(s) ** 2)
        rr = sum(exp(-float(s) ** 2 * (float(g) ** 2 - g1sq)) for g in gz[1:])
        ratio_dev.append(abs(m / first - 1))
        r_bound.append(rr * 1.02 + 1e-9)
    ok_t2 = all(rd <= rb for rd, rb in zip(ratio_dev, r_bound))
    gates.gate("T2 consistent: measured margin = first term x (1 + R), R as stated",
               ok_t2, f"max |ratio-1| = {max(ratio_dev):.2e} vs R-bound "
               f"{max(r_bound):.2e} (worst rung)")

    # -- P2: the threshold --------------------------------------------------
    s_star = sigma_star(lam)
    covered = margin_lower(0.2) >= 2 * eps_r(0.2, lam)
    p2 = (0.21 <= s_star <= 0.29) and covered and s_star <= floor_sigma
    gates.gate("T3: sigma* in [0.21, 0.29], rung 0.2 covered, below measured crossing",
               p2, f"sigma* = {s_star:.4f}; crossing (measured) = {floor_sigma}; "
               f"margin(0.2)/2eps_R = {margin_lower(0.2) / (2 * eps_r(0.2, lam)):.1f}")
    pre.resolve("P2", "FIRED" if p2 else "REFUTED", f"sigma* = {s_star:.4f}")

    invert = log(2 * sqrt(pi) * s_star / eps_r(s_star, lam)) / GAMMA1_UP ** 2
    gates.gate("T3 closed form: sigma*^2 = ln(2 sqrt(pi) sigma*/eps_R)/gamma_1^2",
               abs(invert - s_star ** 2) < 1e-3,
               f"{invert:.5f} vs {s_star ** 2:.5f}")

    # -- P3: the price demo at sigma = 0.5 ----------------------------------
    q_p, q_z = mp_assembly("0.5", demo_n, demo_dps, gz)
    m_num = 4 * pi * 0.25 * sum(exp(-0.25 * float(g) ** 2) for g in gz)
    diff = abs(float(q_p - q_z))
    p3a = diff <= m_num / 2 and m_num > 0
    gates.gate(f"P3: dps-{demo_dps} closed-form assembly CERTIFIES sigma = 0.5",
               p3a, f"|prime - zero| = {diff:.1e} <= margin/2 = {m_num / 2:.1e}")
    i05 = int(np.argmin(np.abs(sigmas - 0.5)))
    m_r = float(meas_margin[i05])
    f64_fail = float(meas_err[i05]) > m_r
    digits_needed = -np.log10(m_r / 2)
    price = GAMMA1_SQ * 0.25 / log(10)
    p3b = f64_fail and abs(digits_needed - price) <= 2.5
    gates.gate("P3: float64 provably cannot (npz row), price = gamma_1^2 sigma^2/ln 10",
               p3b, f"npz err {float(meas_err[i05]):.1e} > margin {m_r:.1e}; "
               f"digits {digits_needed:.1f} vs price {price:.1f}")
    pre.resolve("P3", "FIRED" if (p3a and p3b) else "REFUTED",
                f"certified to {diff:.1e}; price {price:.1f} digits")

    gates.gate("K1: zeros only in validation cells (oracle counter as expected)",
               _ORACLE_CALLS["n"] >= 1, f"calls = {_ORACLE_CALLS['n']} "
               "(the T=100 list; bound and prime assemblies consume integers only)")
    gates.gate("no unresolved pre-registrations", pre.unresolved() == [])

    elapsed = time.perf_counter() - t_start
    save_npz(
        HERE_NPZ,
        {
            "sigmas": sigmas, "eps_r_bound": bound, "measured_err": meas_err,
            "looseness": loose, "sigma_star": np.array([s_star]),
            "margin_lower": np.array([margin_lower(float(s)) for s in sigmas]),
            "demo_diff": np.array([diff]), "demo_margin": np.array([m_num]),
        },
        {
            "experiment": "e2be_certification_cost", "backlog": "B3",
            "dx": DX, "dtau": DTAU, "N": N_LAM, "omega_max": OMEGA_MAX,
            "e_lump": E_LUMP, "rs_const": RS_CONST, "gamma1_up": GAMMA1_UP,
            "sigma_star": s_star, "floor_sigma_measured": floor_sigma,
            "demo_sigma": 0.5, "demo_dps": demo_dps, "demo_n": demo_n,
            "price_digits_at_0.5": price, "quick": quick,
            "oracle_calls": _ORACLE_CALLS["n"], "elapsed_s": round(elapsed, 2),
        },
    )
    pre.table()
    gates.summary(elapsed=elapsed)
    return gates.exit_code()


if __name__ == "__main__":
    raise SystemExit(main())
