"""2FF -- the two-clock interpolating period made quantitative (organ (b) of M4).

CONTEXT. Probe B (2EE, LEARNINGS #44) named the two missing organs of milestone
M4: (a) a fundamental class H^2 with Poincare duality over Spec(Z), and (b) a
SINGLE interpolating period reconciling the two clocks -- the archimedean place on
the additive/log scale (the Gamma factor) and the finite places on the
multiplicative scale p (the (1,p) bidegree, #25). The candidate-B intuition
(backwards_from_2050.md) was that a single transcendental "global q" interpolates
between them. This experiment attacks organ (b) directly and HONESTLY: it cannot
construct the period (that would be a chunk of RH); it makes the two-clock
structure quantitative, determines WHETHER a single number can play the role, and
names what the period must be if it cannot.

THE FUNCTION-FIELD ANCHOR (real). Over F_q there IS a single clock: log q. The
zeta function zeta_C(s) is a rational function of q^{-s}, so it is PERIODIC in
Im(s) with period 2pi/log q, and the zeros lie on a vertical LATTICE of spacing
2pi/log q on the critical line Re(s)=1/2 (Weil/RH-for-C). Equivalently, the closed-
orbit lengths of the Frobenius flow are {k log q}, all integer multiples of the
single period log q. Additive and multiplicative scales are LOCKED by one number.

THE ARITHMETIC OBSTRUCTION (real, the heart of organ (b)). Over Spec(Z) there is
no single q. Two independent, computable facts show a single PERIOD cannot exist:

  (1) INCOMMENSURABILITY of the prime orbit lengths. The Frobenius/closed-orbit
      lengths over Spec(Z) are {log p} (2R/#26), and these are RATIONALLY
      INDEPENDENT (log p_i / log p_j is irrational: p_i, p_j share no common power).
      So there is NO common period L with all log p in L*Z -- the multiplicative
      clock has no single beat. (Contrast F_q, where all orbit lengths k log q DO
      share the period log q.) We measure the "period defect" D(L) = sum_p
      dist(log p / L, Z)^2 over a fine grid of candidate L and show it is bounded
      away from 0 for the primes but hits exactly 0 at L=log q for the F_q orbits.

  (2) THE RUNNING ARCHIMEDEAN CLOCK. The zeta zeros are NOT on a lattice: their
      mean spacing near height T is 2pi / log(T/2pi) (Riemann-von Mangoldt), which
      SHRINKS as T grows. Define the effective clock log q_eff(T) := 2pi /
      (mean spacing) = log(T/2pi). For F_q this is the CONSTANT log q; for zeta it
      RUNS with height, and its running rate is set by the archimedean Gamma factor
      (the density formula is the argument of the archimedean part). We verify
      log q_eff(T) = log(T/2pi) against actual zeta-zero spacings.

THE READING (what organ (b) must be). The single number log q is replaced over
Spec(Z) by the SCALING FLOW R_+ (Deninger's R-flow, not a Z-action) whose orbit
spectrum is the incommensurable {log p}, with the additive clock = the RUNNING
log q_eff(T) = log(T/2pi) supplied by the archimedean place. So organ (b)'s
"interpolating period" is NOT a transcendental number; it is the pair
    (the R-scaling flow,  the incommensurable spectrum {log p}),
and the obstruction to collapsing it to one number is exactly the transcendence /
rational-independence of {log p} (linking organ (b) to candidate F, the
transcendence shadow). The universal transcendental constant that DOES survive is
2pi (the Mellin-Fourier period relating s to q^{-s} = e^{-s log q}); what fails to
be a single number is the clock log q, which becomes the flow.

THE q -> 1 PICTURE. As q -> 1+, the period 2pi/log q -> infinity: the FF zero
lattice spacing diverges and the discrete lattice opens into the continuum -- the
arithmetic case is the "q=1" limit (Connes-Consani scaling site, Deninger flow).
We plot the period vs q and overlay the running zeta clock to show zeta sits at the
q->1 (continuum) end with a height-dependent effective clock.

D-H DISCIPLINE (K2). Davenport-Heilbronn has no Euler product, hence no closed-orbit
spectrum {log p} (2R/#26: Lambda_DH delocalizes off prime powers), hence no scaling
flow and no clock at all. The two-clock object does not even form for D-H -- the
clean C2 face of organ (b).

HONEST SCOPE. The FF lattice period, the incommensurability of {log p}, and the
running density log(T/2pi) are all rigorous/known facts; this experiment makes the
two-clock structure quantitative and draws the structural conclusion (period = flow,
obstruction = incommensurability). It constructs no arithmetic cohomology and proves
nothing about RH. The value: it determines that organ (b) cannot be a single number,
identifies the replacement (the R-flow with spectrum {log p}), and links organ (b)
to the transcendence of the primes. A sharpening coordinate, no new theorem.

Outputs:
  - e2ff_two_clock_period.npz
  - e2ff_two_clock_period.png
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np

from experiments._shared import zeta_L


def first_primes(n):
    primes, c = [], 2
    while len(primes) < n:
        if all(c % p for p in primes):
            primes.append(c)
        c += 1
    return primes


def period_defect(log_lengths, L_grid, sentinel=1.0):
    """D(L) = mean_i dist(ell_i / L, Z_{>=1})^2: how far the lengths are from sharing
    the common period L, where each length must be a POSITIVE-integer multiple of L.
    Zero exactly when every ell_i is an integer multiple of L. A genuine common period
    must satisfy L <= min(ell) (else the smallest length rounds to the 0th multiple);
    for L > min(ell) we set D = sentinel to remove the trivial L->infinity solution
    (where everything rounds to 0). This is the fix for the naive (ell/L mod 1) metric,
    which vanishes spuriously as L grows."""
    ll = np.asarray(log_lengths, dtype=float)
    out = np.empty_like(L_grid)
    min_ell = ll.min()
    for j, L in enumerate(L_grid):
        if L > min_ell:
            out[j] = sentinel  # no valid period this large
            continue
        n = np.round(ll / L)
        n = np.maximum(n, 1.0)            # forbid the 0th multiple
        d = ll / L - n                    # signed distance to nearest positive multiple
        out[j] = float((d ** 2).mean())
    return out


def run(n_primes=25, T_max=200.0, prec=20, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print("[2FF] The two-clock interpolating period (organ (b) of M4), quantitative.")
    print("      Can a SINGLE number reconcile the additive (archimedean) and")
    print("      multiplicative (prime) clocks? Function-field: yes (log q). Spec(Z): no.")
    print("=" * 78)

    primes = first_primes(n_primes)
    log_p = np.log(np.array(primes, dtype=float))

    # ---- (FF anchor) a single clock log q: orbits {k log q} share the period ---- #
    print("\n(FF ANCHOR) Over F_q there is ONE clock log q.")
    q_demo = 5.0
    logq = np.log(q_demo)
    ff_orbits = logq * np.arange(1, n_primes + 1)  # {log q, 2 log q, ...}
    L_grid = np.linspace(0.05, 3.5, 4000)
    D_ff = period_defect(ff_orbits, L_grid)
    L_best_ff = L_grid[np.argmin(D_ff)]
    print(f"    F_{int(q_demo)} orbit lengths {{k log q}}: best common period L = {L_best_ff:.4f}")
    print(f"    (= log q = {logq:.4f}); period defect there D = {D_ff.min():.2e} (~0: commensurable).")
    print(f"    => zeros lie on a vertical LATTICE of spacing 2pi/log q = {2*np.pi/logq:.4f}.")

    # ---- (1) incommensurability of {log p}: no single multiplicative period ---- #
    D_primes = period_defect(log_p, L_grid)
    L_best_p = L_grid[np.argmin(D_primes)]
    print(f"\n(1) INCOMMENSURABILITY. Prime orbit lengths {{log p}}, p up to {primes[-1]}:")
    print(f"    best common period L = {L_best_p:.4f}, but its defect D = {D_primes.min():.3e}")
    print(f"    is BOUNDED AWAY FROM 0 (min over grid {D_primes.min():.3e} vs FF {D_ff.min():.1e}).")
    # simplest explicit obstruction: log 3 / log 2 irrational (continued-fraction nonterminating)
    ratio = np.log(3) / np.log(2)
    cf = mp.nstr(mp.mpf(ratio), 12)
    print(f"    Simplest obstruction: log3/log2 = {cf} is irrational (3,2 share no common")
    print(f"    power), so no L makes both log2, log3 integer multiples. NO single period.")
    no_single_period = D_primes.min() > 50 * max(D_ff.min(), 1e-12)
    print(f"    VERDICT: a single multiplicative period exists for F_q, NOT for the primes: "
          f"{no_single_period}.")

    # ---- (2) the running archimedean clock log q_eff(T) = log(T/2pi) ---- #
    print(f"\n(2) THE RUNNING CLOCK. Computing zeta zeros up to T={T_max:.0f} ...")
    zeros = zeta_L.zeros(T_max, prec)
    gam = np.array([float(mp.im(z)) for z in zeros])
    gam = gam[gam > 0]
    gam.sort()
    spacings = np.diff(gam)
    mids = 0.5 * (gam[1:] + gam[:-1])
    logq_eff_measured = 2 * np.pi / spacings              # noisy per-gap clock
    logq_eff_theory = np.log(mids / (2 * np.pi))          # Riemann-von Mangoldt
    # smooth the measured clock (running mean) to compare to theory
    def runmean(x, w=8):
        if len(x) < w:
            return x
        k = np.ones(w) / w
        return np.convolve(x, k, mode="valid")
    meas_s = runmean(logq_eff_measured)
    th_s = runmean(logq_eff_theory)
    m = min(len(meas_s), len(th_s))
    rel_err = float(np.mean(np.abs(meas_s[:m] - th_s[:m]) / np.maximum(th_s[:m], 1e-9)))
    print(f"    {len(gam)} zeros; smoothed effective clock log q_eff(T) vs log(T/2pi):")
    print(f"    mean relative error = {rel_err:.3f} (the clock RUNS as log(T/2pi),")
    print(f"    set by the archimedean Gamma factor; it is NOT constant as for F_q).")
    print(f"    At T~{mids[0]:.0f}: clock ~ {logq_eff_theory[0]:.3f}; at T~{mids[-1]:.0f}: "
          f"clock ~ {logq_eff_theory[-1]:.3f} (grows: zeros densify).")

    # ---- conclusion ---- #
    print("\n" + "=" * 78)
    print("[2FF] CONCLUSION on organ (b).")
    print("=" * 78)
    print("  The interpolating 'period' is NOT a single (transcendental) number. Over")
    print("  F_q one number log q locks additive to multiplicative (commensurable orbits,")
    print("  a zero lattice). Over Spec(Z): (1) the prime orbit lengths {log p} are")
    print("  rationally INDEPENDENT (no common period), and (2) the archimedean clock")
    print("  RUNS as log(T/2pi). So organ (b) must be the SCALING FLOW R_+ (Deninger)")
    print("  with the incommensurable spectrum {log p}, and the obstruction to a single")
    print("  number is exactly the transcendence of {log p} -- linking organ (b) to")
    print("  candidate F (the transcendence shadow). The universal constant that DOES")
    print("  survive is 2pi (the Mellin-Fourier period s <-> q^{-s}); the clock log q")
    print("  is what dissolves into the flow.")
    print("  q->1 picture: period 2pi/log q -> infinity as q->1+, the FF lattice opens")
    print("  into the continuum; zeta is the q=1 limit with a height-running clock.")
    print("  K2: D-H has no Euler product => no {log p} orbit spectrum => no flow, no")
    print("  clock; the two-clock object does not form for the counterexample.")
    print("\n  HONEST SCOPE: FF lattice period, incommensurability of {log p}, and the")
    print("  running density log(T/2pi) are known facts; this makes the two-clock")
    print("  structure quantitative and concludes period = flow. It constructs no")
    print("  cohomology and proves nothing about RH. A sharpening coordinate.")

    np.savez_compressed(
        out_dir / "e2ff_two_clock_period.npz",
        primes=np.array(primes), log_p=log_p,
        L_grid=L_grid, D_primes=D_primes, D_ff=D_ff,
        L_best_primes=L_best_p, L_best_ff=L_best_ff,
        gamma=gam, spacings=spacings,
        logq_eff_theory=logq_eff_theory,
        rel_err_running_clock=rel_err,
        no_single_period=bool(no_single_period),
        n_primes=n_primes, T_max=T_max, prec=prec,
    )

    # plot
    fig, axs = plt.subplots(1, 3, figsize=(17, 5))
    ax = axs[0]
    ax.plot(L_grid, D_ff, color="tab:blue", label=f"F_{int(q_demo)} orbits {{k log q}}")
    ax.plot(L_grid, D_primes, color="tab:red", label="primes {log p}")
    ax.axvline(logq, color="tab:blue", ls=":", lw=1)
    ax.set_xlabel("candidate common period L")
    ax.set_ylabel("period defect D(L)")
    ax.set_yscale("log")
    ax.set_title("(1) A single period exists for F_q (D=0 at log q)\nbut NOT for the primes (D bounded > 0)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axs[1]
    ax.plot(mids, logq_eff_theory, color="tab:green", lw=2, label="log(T/2pi) (theory)")
    ax.scatter(mids, logq_eff_measured, s=6, color="gray", alpha=0.5,
               label="2pi / (zeta gap) measured")
    ax.axhline(np.log(q_demo), color="tab:blue", ls="--", label=f"F_{int(q_demo)} clock log q (constant)")
    ax.set_xlabel("height T")
    ax.set_ylabel("effective clock log q_eff(T)")
    ax.set_title("(2) Arithmetic clock RUNS as log(T/2pi)\n(F_q clock is constant)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axs[2]
    qs = np.linspace(1.05, 8, 300)
    ax.plot(qs, 2 * np.pi / np.log(qs), color="tab:purple", lw=2, label="FF zero-lattice period 2pi/log q")
    ax.axvline(1.0, color="k", ls=":", lw=1)
    # overlay zeta mean spacing at a few heights as "effective period"
    for T in (30, 80, 150):
        sp = 2 * np.pi / np.log(T / (2 * np.pi))
        ax.axhline(sp, color="tab:green", ls="--", lw=0.8)
        ax.text(6.5, sp, f"zeta @T={T}", fontsize=7, color="tab:green", va="bottom")
    ax.set_xlabel("q")
    ax.set_ylabel("period / mean zero spacing")
    ax.set_ylim(0, 12)
    ax.set_title("q -> 1: FF period diverges -> continuum\nzeta sits at q=1 with a running clock")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e2ff_two_clock_period.png", dpi=140)
    plt.close()
    print(f"\n[2FF] Saved {out_dir / 'e2ff_two_clock_period.png'}")
    print(f"[2FF] Saved {out_dir / 'e2ff_two_clock_period.npz'}")
    return dict(D_primes=D_primes, D_ff=D_ff, rel_err=rel_err,
                no_single_period=no_single_period)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-primes", type=int, default=25)
    parser.add_argument("--T-max", type=float, default=200.0)
    parser.add_argument("--prec", type=int, default=20)
    args = parser.parse_args()
    run(n_primes=args.n_primes, T_max=args.T_max, prec=args.prec)
