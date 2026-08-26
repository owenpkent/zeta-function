"""e2bi: the function-field costume. Snap {log p} onto (1/D)Z so the
Frobenius structure exists literally, and measure the exact price.

Gallery entry G3 (docs/03_research/construct_gallery.md). This is a
DELIBERATELY WRONG build of SP2+SP3: over F_q every place's circumference
is a multiple of log q (one common circle, literal Frobenius, and the Weil
proof goes through). Over Q the {log p} are Q-linearly independent. The
costume: quantize, b_p = exp(round(D log p)/D), so every log b_p lies on
(1/D)Z and the system is fully commensurable, i.e. a function-field-like
generalized-prime system with "q" = e^{1/D}. Its truncated Euler product
is then EXACTLY periodic in t with period 2 pi D (Frobenius structure,
verified to machine precision below, and absent for the true primes).

The price is a one-line theorem this run verifies numerically: the max
snap jitter is at most 1/(2D) (and attains it up to sampling), while the
imported structure lives at height H(D) = 2 pi D, so

    (max jitter) x (structure height)  =  pi,   independent of D.

To see the imported F_q periodicity below zeta's first zero
(gamma_1 = 14.13) one needs D <= 2.25, where the bound 1/(2D) = 0.222 is
at the scale of the default Beurling fake's epsilon = 0.25 (e2ak). Full
fidelity pushes the structure above every fixed height. This is the
Q-linear-independence wall (#162, #172, #188) measured along the
quantization axis; per the
#201 derivability check it is a re-measurement of the wall, with one new
closed-form constant (pi) for the trade.

The additive-lattice cost rides along: the snapped system's generalized
integers are counted against the best linear fit (the e2ak drift meter),
and the drift falls as D grows (the #198 ramp along the quantization
axis) while the true integers sit at drift < 1 (the x + O(1) lattice).

Run:  python -m experiments.arithmetic_geometric.e2bi_commensurabilization
      (--quick drops the two largest x in the drift meter)
"""

from __future__ import annotations

import time
from math import isqrt, log, pi
from pathlib import Path

import numpy as np

from experiments._shared.harness import Gates, PreRegistry, quick_arg, save_npz
from experiments._shared.beurling import BeurlingSystem

HERE = Path(__file__).resolve().parent

P_BOUND = 10000
D_LADDER = [2, 4, 8, 16, 32, 64, 128]
X_DRIFT = 3000          # drift meter horizon
GAMMA_1 = 14.134725     # zeta's first zero: the height budget


def primes_upto(x):
    sieve = bytearray([1]) * (x + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(x) + 1):
        if sieve[p]:
            sieve[p * p::p] = bytearray(len(sieve[p * p::p]))
    return [i for i in range(2, x + 1) if sieve[i]]


def snapped_system(logs_p, D):
    """A BeurlingSystem whose primes are the D-quantized rational primes.

    Reuses the shared control class as substrate (eps=0 gives the true
    primes; we then overwrite the log table with the snapped values, so
    gen_integers / count_integers / theta run unchanged on the fake)."""
    B = BeurlingSystem(prime_bound=2, eps=0.0, seed=0)   # minimal init
    B.logs = sorted(round(D * lp) / D for lp in logs_p)
    B.labels = list(range(len(B.logs)))
    B.eps = 0.5 / D
    return B


def euler_log_sum(logs, s):
    """log of the truncated Euler product: -sum_p log(1 - e^{-l s})."""
    l = np.asarray(logs, dtype=float)
    return complex(-np.sum(np.log1p(-np.exp(-l * s))))


def count_drift(B, x_max):
    """Best-linear-fit residual of N_B(x) over a log-spaced x grid (the
    e2ak lattice meter): < 1 for Z, grows once the lattice is destroyed."""
    gi = B.gen_integers(x_max)
    xs = np.exp(np.linspace(log(20.0), log(float(x_max)), 60))
    counts = np.array([B.count_integers(gi, x) for x in xs], dtype=float)
    A = np.vstack([xs, np.ones_like(xs)]).T
    coef, *_ = np.linalg.lstsq(A, counts, rcond=None)
    resid = counts - A @ coef
    return float(np.max(np.abs(resid))), len(gi)


def main():
    quick = quick_arg()
    t0 = time.time()
    gates = Gates(quick=quick)
    pre = PreRegistry()
    pre.register("P1", "trade law: measured (max jitter) x (2 pi D) lands in "
                       "[0.85 pi, pi] for every D >= 4 (the bound is 1/(2D), "
                       "attained up to sampling over ~1200 primes)",
                 "any D >= 4 with the product outside [0.85 pi, pi]")
    pre.register("P2", "Frobenius costume is real: snapped Euler product "
                       "exactly periodic with period 2 pi D (< 1e-10), true "
                       "primes aperiodic at the same offset (> 1e-3)",
                 "either side fails at any D")
    pre.register("P3", "lattice cost falls along the ladder: "
                       "drift(D=2) > 3 x drift(D=128), and the unsnapped "
                       "integers sit at drift < 1",
                 "ratio <= 3, or integer drift >= 1")

    print("e2bi: the function-field costume (commensurabilization)")
    ps = primes_upto(P_BOUND)
    logs_p = [log(p) for p in ps]
    print(f"  {len(ps)} primes to {P_BOUND}; D ladder {D_LADDER}; drift horizon x <= {X_DRIFT}")

    # --- true-integer control (D = infinity: no snapping)
    B_true = snapped_system(logs_p, 10**9)   # snap step 1e-9: numerically the integers
    B_true.logs = sorted(logs_p)
    drift_true, n_true = count_drift(B_true, X_DRIFT)
    gates.gate("control: true integers are a lattice (drift < 1)",
               drift_true < 1.0, f"drift={drift_true:.3f} over {n_true} integers")

    jit_prod = {}
    period_snap = {}
    period_true = {}
    drift = {}
    collisions = {}
    s_probe = 2.0 + 1.7j   # inside absolute convergence; t0 arbitrary

    for D in D_LADDER:
        B = snapped_system(logs_p, D)
        jit = [abs(round(D * lp) / D - lp) for lp in logs_p]
        maxjit = max(jit)
        jit_prod[D] = maxjit * 2 * pi * D
        collisions[D] = len(logs_p) - len(set(B.logs))

        # exact periodicity of the snapped Euler product vs true primes
        offset = 2 * pi * D
        e1 = euler_log_sum(B.logs, s_probe)
        e2 = euler_log_sum(B.logs, s_probe + 1j * offset)
        period_snap[D] = abs(e1 - e2)
        f1 = euler_log_sum(logs_p, s_probe)
        f2 = euler_log_sum(logs_p, s_probe + 1j * offset)
        period_true[D] = abs(f1 - f2)

        if D in (2, 128):
            drift[D], _ = count_drift(B, X_DRIFT)
        print(f"  D={D:>3}: maxjit={maxjit:.5f}  jit*2piD={jit_prod[D]:.4f}"
              f"  (pi={pi:.4f})  collisions={collisions[D]}"
              f"  |dEuler|snap={period_snap[D]:.2e} true={period_true[D]:.2e}")

    ok1 = all(0.85 * pi <= jit_prod[D] <= pi + 1e-12 for D in D_LADDER if D >= 4)
    gates.gate("trade law: jitter x height = pi (within sampling) for D >= 4",
               ok1, "products: " + ", ".join(f"{jit_prod[D]:.3f}" for D in D_LADDER))
    pre.resolve("P1", "FIRED" if ok1 else "REFUTED",
                f"min={min(jit_prod[D] for D in D_LADDER if D >= 4):.4f}")

    ok2 = all(period_snap[D] < 1e-10 for D in D_LADDER) and \
          all(period_true[D] > 1e-3 for D in D_LADDER)
    gates.gate("Frobenius costume: snapped product exactly 2piD-periodic, "
               "true primes aperiodic", ok2,
               f"snap max={max(period_snap.values()):.2e}, "
               f"true min={min(period_true.values()):.2e}")
    pre.resolve("P2", "FIRED" if ok2 else "REFUTED")

    # the height budget: periodicity visible below gamma_1 needs D <= 2.25,
    # where the jitter bound is the default Beurling fake's epsilon
    D_max_visible = GAMMA_1 / (2 * pi)
    eps_at_budget = 1.0 / (2 * D_max_visible)
    gates.gate("height budget: structure below gamma_1 forces jitter bound "
               ">= 0.222 (the e2ak default fake's scale 0.25)",
               0.20 <= eps_at_budget <= 0.25,
               f"D<= {D_max_visible:.3f} -> jitter bound {eps_at_budget:.4f}")

    ok3 = (drift[2] > 3.0 * drift[128]) and (drift_true < 1.0)
    gates.gate("lattice cost falls along the ladder (drift(2) > 3x drift(128))",
               ok3, f"drift(2)={drift[2]:.2f}, drift(128)={drift[128]:.2f}, "
                    f"integers={drift_true:.3f}")
    pre.resolve("P3", "FIRED" if ok3 else "REFUTED",
                f"ratio={drift[2]/max(drift[128],1e-12):.1f}")

    gates.gate("collisions monotone: more merging at coarser D",
               collisions[2] > collisions[128],
               f"c(2)={collisions[2]}, c(128)={collisions[128]}")
    gates.gate("no unresolved pre-registrations", pre.unresolved() == [])

    pre.table()
    elapsed = time.time() - t0
    if not quick:
        # quick must never overwrite the tracked full-run artifact (the
        # banked --quick npz clobber catch; salvage guard, LEARNINGS #210)
        save_npz(HERE / "e2bi_commensurabilization.npz",
                 dict(D_ladder=np.array(D_LADDER, dtype=float),
                      jit_prod=np.array([jit_prod[D] for D in D_LADDER]),
                      period_snap=np.array([period_snap[D] for D in D_LADDER]),
                      period_true=np.array([period_true[D] for D in D_LADDER]),
                      collisions=np.array([collisions[D] for D in D_LADDER], dtype=float),
                      drift_endpoints=np.array([drift[2], drift[128], drift_true])),
                 dict(experiment="e2bi_commensurabilization", prime_bound=P_BOUND,
                      D_ladder=D_LADDER, x_drift=X_DRIFT, s_probe=[2.0, 1.7],
                      elapsed_s=round(elapsed, 1)))
    gates.summary(elapsed)
    raise SystemExit(gates.exit_code())


if __name__ == "__main__":
    main()
