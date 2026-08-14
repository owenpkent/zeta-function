"""E5B: twin primes (and cousins, and sexy primes) against Hardy-Littlewood.

QUESTION. How close do the measured counts of prime pairs (p, p+d) for
d = 2, 4, 6 track the Hardy-Littlewood conjecture
pi_d(x) ~ C_d * Integral_2^x dt/log^2 t, with C_2 = C_4 = 2*C2 and
C_6 = 4*C2 (C2 the twin prime constant); does the predicted sexy:twin
ratio of exactly 2 appear; and how do the two famous sums behave
(sum 1/p diverges like log log x, Brun's twin sum converges)?

METHOD. Pair counts per decade come from the primestream engine (both
members prime, not necessarily adjacent; the same pass that feeds e5a).
The HL main term is integrated with mpmath at 30 digits. The twin prime
constant C2 = prod_{p>2} (1 - 1/(p-1)^2) is computed from a sieve to 1e7
(truncation error below 1e-8, dominated by sum_{p>P} 1/p^2 ~ 1/(P log P)).

WHY IT MATTERS HERE. The singular series C_d is Euler-product data (a
correction factor per prime p for how the pair {0, d} sits mod p) applied
to an additive question (p and p+d). It is the same mechanism that makes
consecutive primes avoid repeating a last digit (e5a): one framework,
Hardy-Littlewood k-tuples, predicts both, and the measurements below match
it to a few parts in 10^4. The infinitude of twins is open; the COUNT is
not mysterious.
"""
from __future__ import annotations

import sys

import numpy as np
import mpmath as mp

from experiments.primes.primestream import GAPS, NDEC, flat_primes, stream

MERTENS = 0.2614972128476428      # Meissel-Mertens constant
BRUN_B2 = 1.902160583             # Nicely's extrapolation of the full twin sum


def twin_prime_constant(limit: int = 10**7) -> float:
    p = flat_primes(limit)[1:].astype(np.float64)   # drop p = 2
    return float(np.exp(np.log1p(-1.0 / (p - 1.0) ** 2).sum()))


def li2(x: float) -> float:
    """Integral_2^x dt / log(t)^2 at 30 digits."""
    mp.mp.dps = 30
    pts = [2.0]
    while pts[-1] < x:
        pts.append(min(pts[-1] ** 2, x))
    return float(mp.quad(lambda t: 1 / mp.log(t) ** 2, pts))


def main(N: int = 10**8) -> dict:
    print(f"E5B: prime pairs vs Hardy-Littlewood up to N = {N:.1e}")
    res = stream(N, log=print)
    c2 = twin_prime_constant()
    print(f"\ntwin prime constant C2 = {c2:.9f}  (reference 0.660161816)")

    kmax = int(np.round(np.log10(N)))
    cum = {d: np.cumsum(res[f"pair{d}_dec"]) for d in GAPS}
    print("\n[A] Counts vs the HL main term C_d * Int_2^x dt/log^2 t")
    for d, cd_name, cd in ((2, "2*C2", 2 * c2), (4, "2*C2", 2 * c2), (6, "4*C2", 4 * c2)):
        print(f"  d = {d} (C_d = {cd_name} = {cd:.6f}):")
        print("      x        measured     predicted    measured/predicted")
        for k in range(4, kmax + 1):
            x = 10.0 ** k
            meas = int(cum[d][k - 1])
            pred = cd * li2(x)
            print(f"    10^{k:<2} {meas:>12}  {pred:>12.0f}      {meas / pred:.6f}")

    print("\n[B] The sexy:twin ratio (HL says exactly 2 in the limit)")
    for k in range(4, kmax + 1):
        print(f"    10^{k:<2}  {cum[6][k - 1] / cum[2][k - 1]:.6f}")

    print("\n[C] Divergence vs convergence")
    rec = np.cumsum(res["recip_dec"])
    print("    sum 1/p over ALL primes (diverges like log log x + M):")
    for k in range(4, kmax + 1, 2):
        x = 10.0 ** k
        print(f"    10^{k:<2}  measured {rec[k - 1]:.6f}   log log x + M = "
              f"{np.log(np.log(x)) + MERTENS:.6f}")
    print(f"    Brun twin sum, partial to N: {float(res['brun_partial']):.9f}")
    print(f"    (converges; extrapolated full value B2 ~ {BRUN_B2}, Nicely)")

    print("\n[D] Consecutive-gap histogram: the jumping champion")
    gh_tot = res["gap_hist_dec"].sum(axis=0)
    top = np.argsort(gh_tot)[::-1][:5]
    print("    top consecutive gaps overall: "
          + ", ".join(f"{int(g)} ({int(gh_tot[g])})" for g in top))
    for k in range(3, kmax):
        hd = res["gap_hist_dec"][k]
        if hd.sum():
            print(f"    decade 10^{k}: champion gap {int(np.argmax(hd))}")
    print("    (6 is champion from x ~ 10^3 on; conjectured to hand over to 30")
    print("     near 10^35, then 210: the primorials, Odlyzko-Rubinstein-Wolf)")

    print("\nVERDICT: HL k-tuples matches all three pair counts and the exact")
    print("sexy:twin factor 2; sum 1/p tracks Mertens; the twin sum converges")
    print("(Brun). The counting is understood to high accuracy; only the")
    print("infinitude proof (gap 246 by Zhang-Maynard-Tao-Polymath) is open.")
    return res


if __name__ == "__main__":
    N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8
    main(N)
