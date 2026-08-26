"""e2bj: the mollifier costume. Buy Li positivity with a Gaussian window
and measure the horizon every purchase expires at.

Gallery entry G2 (docs/03_research/construct_gallery.md). This is a
DELIBERATELY WRONG build of SP5's positivity readout: damp the Li
zero-sum with a Gaussian weight w_Gamma(gamma) = exp(-(gamma/Gamma)^2)
and tune Gamma until lambda_n >= 0 up to a chosen horizon N. The damping
is a legitimate test-function choice (a windowed Weil form), so unlike
e2bh no zero LOCATION is consumed; the sin is UNIFORMITY, and the run
prices it:

  1. Zeta control: with zeros truncated at T = 100 every on-line zero
     contributes 2(1 - cos(n phi)) >= 0 pointwise, so the truncated
     lambda_n is nonnegative for ALL n (a structure fact, not a numerical
     accident; gate P1). Truncation cannot fake negativity for zeta.
  2. D-H: the off-line pair at beta ~ 0.1915 (|1 - 1/rho| > 1 exactly
     when beta < 1/2) drives lambda_n negative at a measured n*.
  3. The purchase: Gamma*(N) = the largest damping width keeping
     lambda_n >= 0 for all n <= N exists for every finite N and
     DECREASES as the horizon grows: every finite horizon is purchasable.
  4. The expiry: the same Gamma*(N) fails at a measured n** > N: no
     purchased horizon is uniform. Positivity-by-mollification buys any
     finite n-range and never all of them: the uniformity clause of M4
     (#180's margin law, #191's horizon law) in the cheapest instrument
     in the repo. Per the #201 derivability check this is a
     re-measurement of the wall (uniformity face), new costume.

The Beurling control is unposable (no zeros to sum over): the
counting-side refusal, same as e2bh.

Run:  python -m experiments.arithmetic_geometric.e2bj_mollified_li
      (--quick halves the horizon ladder)
"""

from __future__ import annotations

import time
from pathlib import Path

import numpy as np
import mpmath as mp

from experiments._shared.harness import Gates, PreRegistry, quick_arg, save_npz
from experiments._shared.zeta import zeta as zeta_L
from experiments._shared.davenport_heilbronn import DavenportHeilbronn
from experiments._shared.beurling import BeurlingSystem

HERE = Path(__file__).resolve().parent

T_MAX = 100.0
PREC = 30
N_STEP = 10
N_SCAN = 400_000          # unmollified D-H negativity search horizon
GAMMA_CAP = 300.0         # bisection upper end ("no mollification")


def li_terms(zeros_upper):
    """Per-zero data for lambda_n = sum_rho w(gamma) * 2 Re[1-(1-1/rho)^n]:
    returns (c, gamma) with c = log(1 - 1/rho) so that the n-th term is
    2 Re[1 - exp(n c)]."""
    rho = np.array(zeros_upper, dtype=complex)
    c = np.log(1.0 - 1.0 / rho)
    return c, np.abs(rho.imag)


def lambda_min_on_grid(c, gam, Gamma, n_lo, n_hi, chunk=200_000):
    """min over the n-grid [n_lo, n_hi] (step N_STEP) of the mollified
    lambda_n, computed in chunks with early growth handled per chunk (the
    off-line exponent stays < 30 for every horizon used here)."""
    w = np.exp(-((gam / Gamma) ** 2))
    best = np.inf
    n_at = n_lo
    for start in range(n_lo, n_hi + 1, chunk):
        n = np.arange(start, min(start + chunk - N_STEP, n_hi) + 1, N_STEP,
                      dtype=float)
        lam = np.zeros_like(n)
        for ci, wi in zip(c, w):
            lam += wi * 2.0 * (1.0 - np.exp(n * ci).real)
        i = int(np.argmin(lam))
        if lam[i] < best:
            best, n_at = float(lam[i]), int(n[i])
    return best, n_at


def first_negative(c, gam, Gamma, n_hi):
    """Smallest grid n with mollified lambda_n < 0, or None."""
    w = np.exp(-((gam / Gamma) ** 2))
    for start in range(N_STEP, n_hi + 1, 200_000):
        n = np.arange(start, min(start + 200_000 - N_STEP, n_hi) + 1, N_STEP,
                      dtype=float)
        lam = np.zeros_like(n)
        for ci, wi in zip(c, w):
            lam += wi * 2.0 * (1.0 - np.exp(n * ci).real)
        neg = np.where(lam < 0.0)[0]
        if len(neg):
            return int(n[neg[0]])
    return None


def gamma_star(c, gam, N, lo=1.0, hi=GAMMA_CAP, iters=40):
    """Largest Gamma with lambda_n >= 0 on the grid up to N (bisection).
    Returns None if even Gamma = hi passes (no mollification needed)."""
    ok_hi, _ = lambda_min_on_grid(c, gam, hi, N_STEP, N)
    if ok_hi >= 0.0:
        return None
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        mn, _ = lambda_min_on_grid(c, gam, mid, N_STEP, N)
        if mn >= 0.0:
            lo = mid
        else:
            hi = mid
    return lo


def main():
    quick = quick_arg()
    t0 = time.time()
    gates = Gates(quick=quick)
    pre = PreRegistry()
    pre.register("P1", "truncated zeta lambda_n >= 0 on the whole grid "
                       "(on-line terms are pointwise >= 0: structure, not luck)",
                 "any negative zeta lambda_n")
    pre.register("P2", "D-H unmollified lambda_n goes negative at some "
                       f"n* <= {N_SCAN}",
                 "stays nonnegative on the whole scan")
    pre.register("P3", "Gamma*(N) exists (finite) for every horizon at and "
                       "beyond n*, and is strictly decreasing along the ladder",
                 "missing, or non-monotone")
    pre.register("P4", "every purchased horizon expires: Gamma*(N_max) fails "
                       "at a measured n** <= 8 N_max",
                 "no failure found by 8 N_max")

    print("e2bj: the mollifier costume (windowed Li positivity)")
    mp.mp.dps = PREC
    zz = [complex(r) for r in zeta_L.zeros(T_MAX, prec=PREC)]
    dz = [complex(r) for r in DavenportHeilbronn().zeros(T_MAX, prec=PREC)]
    cz, gz = li_terms(zz)
    cd, gd = li_terms(dz)
    # threshold 1e-8: on-line zeros found by root refinement sit at
    # beta = 1/2 +- eps_num, giving |Re log(1-1/rho)| ~ eps_num; only a
    # genuinely off-line beta < 1/2 clears 1e-8
    n_grow = sum(1 for ci in cd if ci.real > 1e-8)
    n_grow_zeta = sum(1 for ci in cz if ci.real > 1e-8)
    print(f"  zeta: {len(zz)} zeros; D-H: {len(dz)} zeros, "
          f"{n_grow} genuinely growing Li mode(s) (beta < 1/2)")
    gates.gate("D-H has a growing Li mode, zeta has none",
               n_grow >= 1 and n_grow_zeta == 0,
               f"dh={n_grow}, zeta={n_grow_zeta}")

    # --- 1. zeta control
    zmin, zat = lambda_min_on_grid(cz, gz, GAMMA_CAP, N_STEP, N_SCAN)
    ok1 = zmin > -1e-9
    gates.gate("zeta: truncated lambda_n >= 0 over the whole grid", ok1,
               f"min={zmin:.3e} at n={zat}")
    pre.resolve("P1", "FIRED" if ok1 else "REFUTED", f"min={zmin:.3e}")

    # --- 2. D-H unmollified negativity
    n_star = first_negative(cd, gd, GAMMA_CAP, N_SCAN)
    ok2 = n_star is not None
    gates.gate(f"D-H: unmollified lambda_n < 0 at n* <= {N_SCAN}", ok2,
               f"n*={n_star}")
    pre.resolve("P2", "FIRED" if ok2 else "REFUTED", f"n*={n_star}")
    if not ok2:
        n_star = N_SCAN   # keep the ladder runnable for the summary

    # --- 3. the purchase ladder
    ladder = [n_star, 2 * n_star, 4 * n_star] if quick else \
             [n_star, 2 * n_star, 4 * n_star, 8 * n_star]
    gstars = []
    for N in ladder:
        g = gamma_star(cd, gd, N)
        gstars.append(g)
        print(f"  horizon N={N:>8}: Gamma*(N) = "
              f"{'(none needed)' if g is None else f'{g:.3f}'}")
    ok3 = all(g is not None for g in gstars) and \
        all(gstars[i] > gstars[i + 1] for i in range(len(gstars) - 1))
    gates.gate("Gamma*(N) finite and strictly decreasing along the ladder",
               ok3, "Gamma*: " + ", ".join(
                   "-" if g is None else f"{g:.2f}" for g in gstars))
    pre.resolve("P3", "FIRED" if ok3 else "REFUTED")

    # --- 4. the expiry
    n_fail = None
    if gstars[-1] is not None:
        n_fail = first_negative(cd, gd, gstars[-1], 8 * ladder[-1])
    ok4 = n_fail is not None and n_fail > ladder[-1]
    gates.gate("every purchased horizon expires (Gamma*(N_max) fails above "
               "N_max, below 8 N_max)", ok4,
               f"n**={n_fail} vs N_max={ladder[-1]}")
    pre.resolve("P4", "FIRED" if ok4 else "REFUTED", f"n**={n_fail}")

    b = BeurlingSystem(prime_bound=100, eps=0.2, seed=149)
    gates.gate("Beurling refusal: no zeros to sum over (Li unposable)",
               not hasattr(b, "zeros"))
    gates.gate("no unresolved pre-registrations", pre.unresolved() == [])

    pre.table()
    elapsed = time.time() - t0
    save_npz(HERE / "e2bj_mollified_li.npz",
             dict(ladder=np.array(ladder, dtype=float),
                  gamma_star=np.array([g if g is not None else -1.0
                                       for g in gstars]),
                  n_star=np.array([n_star], dtype=float),
                  n_fail=np.array([n_fail if n_fail else -1.0]),
                  zeta_min=np.array([zmin])),
             dict(experiment="e2bj_mollified_li", T_max=T_MAX, prec=PREC,
                  n_step=N_STEP, n_scan=N_SCAN, quick=quick,
                  n_zeta=len(zz), n_dh=len(dz), elapsed_s=round(elapsed, 1)))
    gates.summary(elapsed)
    raise SystemExit(gates.exit_code())


if __name__ == "__main__":
    main()
