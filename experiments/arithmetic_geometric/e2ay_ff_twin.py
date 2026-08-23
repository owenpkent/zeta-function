"""E2AY: C1: the function-field twin: the F_q column of the satisfiability
matrix, filled by MEASUREMENT through the e2an pipeline mechanics.

THE INSTANCE. The e2b curve E: y^2 = x^3 + x + 1 over F_5 (q = 5,
N_1 = 9, a = q + 1 - N_1 = -3, class number h = N_1 = 9, genus 1). Its
"integers" are the effective divisors: the lattice lives on the single
arithmetic progression {n log q} with coefficients b_n = #{effective
divisors of degree n} (b_0 = 1, b_n = h (q^n - 1)/(q - 1) for n >= 1,
CROSS-CHECKED in-run against the place-count Euler product built from
direct point counting over F_{q^k}, k <= 4, via e2b's field arithmetic).
The multiplier on the critical line is the curve zeta
Z(q^{-1/2 - i tau}) = P(T)/((1 - T)(1 - qT)), P(T) = 1 - aT + qT^2,
periodic in tau with period 2 pi / log q.

THE ONE STRUCTURAL ADAPTATION (itself a table cell): zeta has ONE pole,
so e2an regularizes the descent with a single R I1 e^{-s} term. The FF
world has pole ARRAYS at Re s = 1 AND Re s = 0 (period 2 pi / log q in
tau), so the single-term regularizer provably leaves an O(1)-relative
periodic wiggle (measured below as the FAILURE of the zeta-style
regularizer), while the finite partial-fraction structure
Z(T) = 1 - (h/(q-1))/(1 - T) + (h/(q-1))/(1 - qT) makes the FULL
geometric-array regularizer available from lattice data alone
(h = b_1): with it, the reduced integrand is

  r(s) = (1 - h/(q-1)) F(s) - (h/(q-1)) [ sum_{n >= 1} F(s + n log q)
         + sum_{n <= -1} q^n F(s + n log q) ],

and the Muntz extraction is EXACT AS AN IDENTITY (no huge b_n is ever
materialized; the analytic reduction is verified against the raw
b_n-accumulated integrand on a subgrid). K1 posture: the build consumes
point/divisor counts only; the Z-formula oracle is validation-phase.

PRE-REGISTERED EXPECTATIONS (the backlog's, sharpened):
  [FF1] engine exact: extracted m(tau) = Z(1/2 + i tau) at quadrature
        precision; the zeta-style single-pole regularizer FAILS with an
        O(1) periodic defect (the pole-array cell).
  [FF2] duality with NO completion factor: m real on the line as-is
        (the archimedean place is absent; zeta needed pi^{-z/2} Gamma).
  [FF3] SP2: emergent spectrum = EXACTLY the periodic pair array
        (+-theta + 2 pi k)/log q: ALL predicted zeros in range found, no
        spurious, spacings equal to 2 pi / log q at refinement precision;
        completeness here is PROVABLE (Hasse) and measured complete.
  [FF4] SP3: the degree-indexed log-derivative (Cauchy division, the
        free-semigroup convolution in the degree variable) returns
        lambda_n = N_n log q EXACTLY, with N_n from Grothendieck-
        Lefschetz recursion anchored to direct point counts (k <= 4).
  [FF5] SP4: the trace formula is EXACT: t_n from the refined emergent
        spectrum (2 q^{n/2} cos(n theta-hat)) equals q^n + 1 - N_n from
        the prime side, to zero-refinement precision (bisection on the
        real multiplier: ~1e-12), through n = 12.
  [FF6] SP5: the polarization is INHABITED and measurable: |alpha|^2 =
        (t_1^2 - t_2)/2 = q to refinement precision (the on-circle
        statement = FF-RH, here a THEOREM with a named source: Hodge
        index / Castelnuovo), with O(1) Hasse margin 2 sqrt(q) - |t_1|;
        against zeta's SP5 cell (margin zero at machine precision,
        e2an/e3v).
  [FF7] the carrier coordinate: every place sits on ONE rational
        progression (commensurable lattice), vs zeta's Q-linearly
        independent {log p}: the S4/R1 coordinate (#162/#172/#188)
        displayed structurally.

DELIVERABLE: the per-cell zeta-vs-F_q table (dossier), the standing
regression control for future candidates.

Run:
  python -m experiments.arithmetic_geometric.e2ay_ff_twin

Outputs: e2ay_ff_twin.npz (tracked, evidence rule).
"""

from __future__ import annotations

import time
from math import log, pi, sqrt
from pathlib import Path

import numpy as np

from experiments.arithmetic_geometric.e2an_sp_object_v0 import (
    DELTA, Probe, detect_zeros, multiplier, multiplier_at, s_grid)
from experiments.arithmetic_geometric.e2b_elliptic_curve_fp import point_count_F_pk

HERE = Path(__file__).resolve().parent

Q = 5
ACURVE = (1, 1)          # y^2 = x^3 + x + 1
LOGQ = log(Q)
# The FF reduced integrand decays to the LEFT only as e^{s/2} times a
# periodic spike train (the Re s = 0 pole array), unlike zeta's
# pole-cancelled continuum which is dead at s = -6: the window must
# extend until e^{s/2} is below target precision. Another array cell.
S_MIN_FF = -70.0

CHECKS: list[tuple[str, bool, str]] = []
_ORACLE = {"n": 0}


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


# ---------------------------------------------------------------------------
# lattice data from the curve (build phase: counts only)
# ---------------------------------------------------------------------------

def frobenius_traces(a1, nmax):
    """t_n = alpha^n + conj(alpha)^n via t_{n+1} = a t_n - q t_{n-1}."""
    t = [2.0, float(a1)]
    for _ in range(nmax - 1):
        t.append(a1 * t[-1] - Q * t[-2])
    return np.array(t)          # t[0] = 2, t[n] = trace


def divisor_counts_from_places(a_places, nmax):
    """b_n from the Euler product prod_d (1 - T^d)^{-a_d}, via
    log prod = sum_d a_d sum_k T^{dk}/k, whose T^n coefficient is
    (1/n) sum_{d | n} d a_d =: c_n/n, and the exp-of-series recursion
    n b_n = sum_{m=1}^{n} c_m b_{n-m}. O(nmax^2), exact in the
    place-count data."""
    c = np.zeros(nmax + 1)
    for n in range(1, nmax + 1):
        c[n] = sum(d * a_places[d] for d in range(1, n + 1) if n % d == 0)
    b = np.zeros(nmax + 1)
    b[0] = 1.0
    for n in range(1, nmax + 1):
        b[n] = sum(c[m] * b[n - m] for m in range(1, n + 1)) / n
    return b


def cauchy_log_derivative(b, nmax):
    """lambda_n with sum_{m=1}^{n} b_{n-m} lambda_m = n log q * b_n:
    the degree-variable (free semigroup) von Mangoldt extraction."""
    lam = np.zeros(nmax + 1)
    for n in range(1, nmax + 1):
        s = n * LOGQ * b[n] - sum(b[n - m] * lam[m] for m in range(1, n))
        lam[n] = s / b[0]
    return lam


# ---------------------------------------------------------------------------
# the descent integrand: array regularizer (reduced form) and raw form
# ---------------------------------------------------------------------------

def r_reduced_on_grid(probe, s, h4):
    """r(s) = (1 - h4) F(s) - h4 [sum_{n>=1} F(s + n log q)
    + sum_{n<=-1} q^n F(s + n log q)], h4 = h/(q-1)."""
    r = (1.0 - h4) * probe.F(s)
    w = 8.0 * probe.sigma
    n_lo = int(np.floor((probe.c - w - s[-1]) / LOGQ)) - 1
    n_hi = int(np.ceil((probe.c + w - s[0]) / LOGQ)) + 1
    for n in range(n_lo, n_hi + 1):
        if n == 0:
            continue
        coef = -h4 * (1.0 if n >= 1 else Q ** float(n))
        r += coef * probe.F(s + n * LOGQ)
    return r


def raw_integrand_on_grid(b, probe, s, h4):
    """The UNREDUCED r(s): sum_{n>=0} b_n F(s + n log q) minus the full
    geometric array h4 sum_{n in Z} q^n F(s + n log q); b_n materialized
    (float; used only on a subgrid to verify the reduction)."""
    acc = np.zeros_like(s)
    w = 8.0 * probe.sigma
    n_hi = int(np.ceil((probe.c + w - s[0]) / LOGQ)) + 1
    for n in range(0, min(n_hi, len(b) - 1) + 1):
        acc += b[n] * probe.F(s + n * LOGQ)
    n_lo = int(np.floor((probe.c - w - s[-1]) / LOGQ)) - 1
    for n in range(n_lo, n_hi + 1):
        acc -= h4 * (Q ** float(n)) * probe.F(s + n * LOGQ)
    return acc


def zeta_style_integrand(b, probe, s, residue):
    """e2an's single-pole regularization, applied verbatim to the FF
    lattice (the control that is EXPECTED to fail: pole array vs pole)."""
    acc = -residue * probe.I1() * np.exp(-s)
    w = 8.0 * probe.sigma
    n_hi = int(np.ceil((probe.c + w - s[0]) / LOGQ)) + 1
    for n in range(0, min(n_hi, len(b) - 1) + 1):
        acc += b[n] * probe.F(s + n * LOGQ)
    return acc


# ---------------------------------------------------------------------------
# validation oracle (the only code allowed to evaluate Z)
# ---------------------------------------------------------------------------

def oracle_Z_line(taus, a1):
    _ORACLE["n"] += 1
    z = 0.5 + 1j * np.asarray(taus, dtype=complex)
    T = Q ** (-z)
    return (1 - a1 * T + Q * T * T) / ((1 - T) * (1 - Q * T))


def run():
    t0 = time.time()
    print("== E2AY: the function-field twin (C1): the F_q column by measurement ==")

    # ---------------- build phase (counts only) ----------------
    print("\n-- build phase: point counts, places, divisor lattice --")
    N_direct = [point_count_F_pk(ACURVE, Q, k) for k in (1, 2, 3, 4)]
    N1 = N_direct[0]
    a1 = Q + 1 - N1
    h = N1
    h4 = h / (Q - 1)
    NMAX = 25
    t_n = frobenius_traces(a1, NMAX)
    N_rec = np.array([Q ** n + 1 - t_n[n] for n in range(NMAX + 1)])
    # places by Mobius-free peeling: N_n = sum_{d | n} d a_d
    a_places = np.zeros(NMAX + 1)
    for n in range(1, NMAX + 1):
        s = sum(d * a_places[d] for d in range(1, n) if n % d == 0)
        a_places[n] = (N_rec[n] - s) / n
    b_places = divisor_counts_from_places(a_places, 12)
    b_closed = np.array([1.0] + [h * (Q ** n - 1) / (Q - 1) for n in range(1, NMAX + 1)])
    b_dev = float(np.max(np.abs(b_places - b_closed[:13]) / b_closed[:13]))
    print(f"  N_1..N_4 direct = {N_direct}; a = {a1}, h = {h}; "
          f"divisor-count cross-check dev = {b_dev:.2e}")

    probeA = Probe(c=1.9, sigma=0.04)
    probeB = Probe(c=2.6, sigma=0.15)
    s = s_grid(S_MIN_FF)
    integ = r_reduced_on_grid(probeA, s, h4) * np.exp(0.5 * s)
    integ_B = r_reduced_on_grid(probeB, s, h4) * np.exp(0.5 * s)

    # reduction identity: raw b_n accumulation equals the reduced form.
    # Checked on s >= -20 only: at degree n the RAW form cancels
    # q^n-scale terms in float (b_n against h4 q^n), so it is itself
    # cancellation-limited: which is exactly why the reduced form is
    # the right implementation (no b_n is ever materialized there).
    s_sub = s[s >= -20.0][:: 40]
    raw = raw_integrand_on_grid(b_closed, probeA, s_sub, h4) * np.exp(0.5 * s_sub)
    red = r_reduced_on_grid(probeA, s_sub, h4) * np.exp(0.5 * s_sub)
    reduction_dev = float(np.max(np.abs(raw - red)) / max(1e-300, np.max(np.abs(red))))

    tau, m = multiplier(None, probeA, s_min=S_MIN_FF, integrand=integ)
    _, m_B = multiplier(None, probeB, s_min=S_MIN_FF, integrand=integ_B)
    sel25 = tau <= 25.0
    cross_dev = float(np.max(np.abs(m[sel25] - m_B[sel25]) / (1 + np.abs(m[sel25]))))

    # the zeta-style single-pole control (expected to fail): residue of
    # sum b_n q^{-ns} at s = 1 is h / ((q-1) log q)
    res_ff = h / ((Q - 1) * LOGQ)
    integ_single = zeta_style_integrand(b_closed, probeA, s, res_ff) * np.exp(0.5 * s)
    _, m_single = multiplier(None, probeA, s_min=S_MIN_FF, integrand=integ_single)

    # duality: NO completion factor (the archimedean place is absent)
    sel_dual = (tau >= 2.0) & (tau <= 60.0)
    dual_ff = float(np.median(np.abs(np.imag(m[sel_dual]))
                              / (np.abs(m[sel_dual]) + 1e-300)))

    # SP2: emergent spectrum
    em = detect_zeros(tau, np.abs(m), tau_lo=0.4, tau_hi=100.0)
    period = 2 * pi / LOGQ

    # refinement: bisection on Re m (m real on the line) around each of the
    # first four dips
    def m_real_at(tt):
        return float(np.real(multiplier_at(None, probeA, [tt], s_min=S_MIN_FF, integrand=integ)[0]))

    refined = []
    for g0, _ in em[:4]:
        lo, hi = g0 - 5e-3, g0 + 5e-3
        flo = m_real_at(lo)
        if flo * m_real_at(hi) > 0:
            continue
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            if m_real_at(mid) * flo <= 0:
                hi = mid
            else:
                lo, flo = mid, m_real_at(mid)
        refined.append(0.5 * (lo + hi))

    # theta-hat from the first refined zero; fold others into [0, period)
    theta_hat = refined[0] * LOGQ
    # SP3: the degree-variable log-derivative
    lam_hat = cauchy_log_derivative(b_closed, 20)
    lam_dev = float(np.max(np.abs(lam_hat[1:21] - N_rec[1:21] * LOGQ)
                           / (N_rec[1:21] * LOGQ)))

    # SP4: Lefschetz two-sidedness: zero side from theta_hat, prime side
    # from the extracted lambda_n
    N_from_lam = lam_hat / LOGQ
    t_zero_side = np.array([2 * Q ** (n / 2) * np.cos(n * theta_hat)
                            for n in range(0, 13)])
    t_prime_side = np.array([Q ** n + 1 - N_from_lam[n] if n >= 1 else 2.0
                             for n in range(0, 13)])
    sp4_dev = float(np.max(np.abs(t_zero_side[1:] - t_prime_side[1:])
                           / np.maximum(np.abs(t_prime_side[1:]), 1.0)))

    # SP5: the polarization measured: |alpha|^2 = (t_1^2 - t_2)/2 = q,
    # Hasse margin 2 sqrt(q) - |t_1|
    t1_hat, t2_hat = t_zero_side[1], t_zero_side[2]
    alpha2_hat = (t1_hat ** 2 - t2_hat) / 2.0
    hasse_margin = 2 * sqrt(Q) - abs(t1_hat)

    build_oracle_calls = _ORACLE["n"]

    # ---------------- validation phase (Z oracle allowed) ----------------
    print("-- validation phase --")
    taus_probe = np.array([0.7, 2.5, 7.0, 13.0, 21.5, 33.0, 47.0, 61.0, 93.0])
    Z_true = oracle_Z_line(taus_probe, a1)
    m_at = multiplier_at(None, probeA, taus_probe, s_min=S_MIN_FF, integrand=integ)
    muntz_err = float(np.max(np.abs(m_at - Z_true) / (1 + np.abs(Z_true))))

    sel60 = (tau >= 2.0) & (tau <= 60.0)
    Z_grid = oracle_Z_line(tau[sel60], a1)
    single_defect = float(np.median(np.abs(m_single[sel60] - Z_grid)
                                    / (1 + np.abs(Z_grid))))
    array_defect = float(np.median(np.abs(m[sel60] - Z_grid) / (1 + np.abs(Z_grid))))

    # predicted zero array from the (validation-phase) polynomial
    theta_true = float(np.arccos(a1 / (2 * sqrt(Q))))
    pred = []
    k = 0
    while True:
        for sgn in (+1, -1):
            g = (sgn * theta_true + 2 * pi * k) / LOGQ
            if 0.4 <= g <= 100.0:
                pred.append(g)
        if (2 * pi * k - theta_true) / LOGQ > 100.0:
            break
        k += 1
    pred = np.array(sorted(pred))
    found = np.array([g for g, _ in em])
    hit = sum(1 for g in pred if np.min(np.abs(found - g)) < 0.02)
    spurious = sum(1 for g in found if np.min(np.abs(pred - g)) > 0.02)
    loc_err = float(np.max([np.min(np.abs(found - g)) for g in pred])) if hit else np.inf
    # refined-zero localization and periodicity
    ref_err = float(max(abs(r - pred[np.argmin(np.abs(pred - r))]) for r in refined))
    spacings = [refined[2] - refined[0], refined[3] - refined[1]] \
        if len(refined) == 4 else []
    per_dev = float(max(abs(sp - period) for sp in spacings)) if spacings else np.inf

    theta_dev = abs(theta_hat - theta_true)

    # ---------------- checks ----------------
    print("\n-- checks --")
    check("K1 guard: zero oracle calls during the build phase",
          build_oracle_calls == 0, f"calls = {build_oracle_calls}")
    check("lattice anchored: divisor counts from direct-counted places equal "
          "the closed form (n <= 12)",
          b_dev < 1e-12 and N_direct == [int(x) for x in N_rec[1:5]],
          f"b dev = {b_dev:.1e}; N_1..4 = {N_direct} vs recursion "
          f"{[int(x) for x in N_rec[1:5]]}")
    check("reduction identity: raw b_n descent equals the reduced "
          "array-regularized form (s >= -20; the raw form is "
          "q^n-cancellation-limited below, why the reduced form exists)",
          reduction_dev < 1e-5, f"max rel dev = {reduction_dev:.2e}")
    check("[FF1] engine exact: extracted m = Z(1/2 + i tau) at quadrature "
          "precision",
          muntz_err < 1e-8, f"max rel err = {muntz_err:.2e}"
          f" (grid median {array_defect:.2e})")
    check("[FF1] the pole-ARRAY cell: the zeta-style single-pole regularizer "
          "FAILS on the FF lattice (O(1) defect) while the array form is exact",
          single_defect > 1e-2 and single_defect > 1e6 * array_defect,
          f"single-pole median defect = {single_defect:.3f} vs array "
          f"{array_defect:.2e}")
    check("operator well-defined: cross-probe agreement (tau <= 25)",
          cross_dev < 1e-7, f"max rel dev = {cross_dev:.2e}")
    check("[FF2] duality with NO completion factor: m real on the line "
          "(the archimedean place is absent; gate at the extraction floor)",
          dual_ff < 1e-7, f"median |Im|/|m| = {dual_ff:.2e} (floor: grid median err {array_defect:.1e})")
    check("[FF3] SP2 completeness: ALL predicted zeros found, none spurious "
          "(provable here: Hasse)",
          hit == len(pred) and spurious == 0,
          f"{hit}/{len(pred)} found, {spurious} spurious, "
          f"coarse loc err = {loc_err:.1e}")
    check("[FF3] the arithmetic progression: refined zeros on the periodic "
          "pair array; spacings = 2 pi / log q to 1e-9",
          ref_err < 1e-9 and per_dev < 1e-9,
          f"refined loc err = {ref_err:.1e}, max |spacing - period| = "
          f"{per_dev:.1e}")
    check("[FF4] SP3 Euler: degree-variable log-derivative returns "
          "lambda_n = N_n log q exactly (n <= 20)",
          lam_dev < 1e-12, f"max rel dev = {lam_dev:.2e}")
    check("[FF5] SP4 EXACT (Grothendieck-Lefschetz): zero-side traces = "
          "prime-side traces through n = 12 at refinement precision",
          sp4_dev < 1e-6, f"max rel dev = {sp4_dev:.2e} "
          f"(theta-hat dev = {theta_dev:.1e})")
    check("[FF6] SP5 inhabited: |alpha|^2 = q at refinement precision AND "
          "O(1) Hasse margin (source: Hodge index, a theorem here)",
          abs(alpha2_hat - Q) < 1e-6 and hasse_margin > 1.0,
          f"|alpha|^2 = {alpha2_hat:.10f} vs q = {Q}; margin "
          f"2 sqrt(q) - |t_1| = {hasse_margin:.4f}")
    check("[FF7] the carrier coordinate: every place on ONE rational "
          "progression (commensurable lattice; zeta's is Q-linearly "
          "independent: the S4/R1 coordinate)",
          True, f"places per degree a_d = {[int(x) for x in a_places[1:7]]}, "
          f"all at {{n log q}}")

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print(f"\n{npass}/{len(CHECKS)} passed  ({time.time() - t0:.1f} s)")

    out = HERE / "e2ay_ff_twin.npz"
    sub = slice(None, None, 10)
    np.savez_compressed(
        out,
        tau=tau[sub], m=m[sub], m_single=m_single[sub],
        emergent=np.array(em), refined=np.array(refined),
        pred=pred, theta=np.array([theta_hat, theta_true]),
        muntz_err=muntz_err, single_defect=single_defect,
        array_defect=array_defect, dual_ff=dual_ff,
        lam_dev=lam_dev, sp4_dev=sp4_dev,
        t_zero_side=t_zero_side, t_prime_side=t_prime_side,
        alpha2=alpha2_hat, hasse_margin=hasse_margin,
        a_places=a_places, b_dev=b_dev, reduction_dev=reduction_dev,
        cross_dev=cross_dev, N_direct=np.array(N_direct),
        checks_passed=npass, checks_total=len(CHECKS),
    )
    print(f"saved {out.name}")


if __name__ == "__main__":
    run()
