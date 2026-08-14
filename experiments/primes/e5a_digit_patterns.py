"""E5A: last digits of primes across bases, and the consecutive-prime bias.

QUESTION. What can the last digit of a prime be, in any base; are the legal
digits equally used (Dirichlet equidistribution); and do consecutive primes
avoid repeating a last digit (the Lemke Oliver-Soundararajan bias), in every
base, with the bias decaying as x grows?

METHOD. One streaming pass over all primes up to N (primestream.py):
last-digit counts and consecutive-pair transition matrices per base
b in {3, 4, 10, 12, 30}, per-decade breakdowns for b = 3 and 10, plus the
Chebyshev races mod 4 and mod 3 (a last-digit phenomenon in base 4 / base 3:
which legal digit is winning at any finite x). Default N = 10^8 runs in
seconds; the same module ran the deep pass on the research box
(python -m experiments.primes.e5a_digit_patterns 1e11).

READING THE NUMBERS. Legal digits are exactly the phi(b) units mod b
(divisibility kills the rest). Shares converge to 1/phi(b) (prime number
theorem in arithmetic progressions). The repeat share (both of two
consecutive primes ending in the same digit) sits far BELOW the naive
1/phi(b) and crawls up only like (log log x)/log x, the Hardy-Littlewood
k-tuple mechanism quantified by Lemke Oliver-Soundararajan (2016). The mod-4
race leads almost always on the nonresidue side (Chebyshev 1853), first
flipping at x = 26,861 (Leech 1957); the mod-3 race does not flip below
10^11 (first flip known near 6.09e11, Bays-Hudson).
"""
from __future__ import annotations

import sys

import numpy as np

from experiments.primes.primestream import (
    BASES, DECADE_TRANS_BASES, NDEC, flat_primes, stream, units,
)


def _share_table(res: dict, b: int) -> str:
    c = res[f"counts_b{b}"]
    tot = c.sum()
    u = units(b)
    rows = [f"    digit {d:>2}: {int(n):>12}  share {n/tot:.6f}" for d, n in zip(u, c)]
    dev = float(np.abs(c / tot - 1 / len(u)).max())
    rows.append(f"    max |share - 1/{len(u)}| = {dev:.2e}")
    return "\n".join(rows)


def _matrix(res: dict, b: int) -> str:
    m = res[f"trans_b{b}"].astype(float)
    u = units(b)
    rows = ["         " + "".join(f"{d:>8}" for d in u) + "   (next prime ends in)"]
    for i, d in enumerate(u):
        r = m[i] / m[i].sum()
        rows.append(f"    {d:>2} | " + "".join(f"{x:8.4f}" for x in r))
    return "\n".join(rows)


def repeat_share(m: np.ndarray) -> float:
    return float(np.trace(m) / m.sum())


def decade_repeat_shares(res: dict, b: int) -> list[tuple[int, int, float]]:
    """(decade exponent k, pair count, repeat share) for decades [10^k, 10^{k+1})."""
    td = res[f"transdec_b{b}"]
    out = []
    for k in range(NDEC):
        tot = int(td[k].sum())
        if tot >= 1000:
            out.append((k, tot, float(np.trace(td[k]) / tot)))
    return out


def race_summary(res: dict, name: str) -> str:
    fc = int(res[f"{name}_first_cross"])
    n = int(res[f"{name}_n_pos"] + res[f"{name}_n_neg"] + res[f"{name}_n_zero"])
    pos = int(res[f"{name}_n_pos"]) / n
    done = int(res[f"{name}_sample_done"])
    samp = res[f"{name}_sample_lead"][:done]
    logdens = float((samp > 0).mean()) if done else float("nan")
    return (f"    first lead flip at x = {fc if fc else 'none reached'}\n"
            f"    lead range [{int(res[f'{name}_min_lead'])}, {int(res[f'{name}_max_lead'])}]"
            f"   nonresidue leads at {pos:.4%} of prime steps\n"
            f"    log-density estimate of 'nonresidue ahead' "
            f"(equal-weight log-spaced samples): {logdens:.4f}")


def leading_digit_note(limit: int = 10**8) -> str:
    primes = flat_primes(limit)
    ld = primes.copy()
    while (ld >= 10).any():
        big = ld >= 10
        ld[big] //= 10
    c = np.bincount(ld, minlength=10)[1:]
    shares = c / c.sum()
    benford = np.log10(1 + 1 / np.arange(1, 10))
    rows = ["    d    primes    Benford-would-be"]
    for d in range(9):
        rows.append(f"    {d+1}  {shares[d]:.4f}       {benford[d]:.4f}")
    return "\n".join(rows)


def main(N: int = 10**8) -> dict:
    print(f"E5A: prime last-digit patterns up to N = {N:.1e}")
    res = stream(N, log=print)
    pi = int(res["pi_dec"].sum())
    print(f"\npi({N:.0e}) = {pi}   (stream {float(res['elapsed']):.1f}s)")

    print("\n[A] Legal last digits and their shares (Dirichlet equidistribution)")
    print("    base 2: every prime except 2 ends in 1 (the digit says nothing).")
    for b in BASES:
        print(f"  base {b}: phi({b}) = {len(units(b))} legal digits {units(b)}")
        print(_share_table(res, b))

    print("\n[B] Consecutive-prime transition matrices (row = this prime's digit)")
    for b in (10, 3):
        print(f"  base {b}:")
        print(_matrix(res, b))
    print("\n    repeat share vs naive 1/phi(b):")
    for b in BASES:
        m = res[f"trans_b{b}"]
        naive = 1 / len(units(b))
        rs = repeat_share(m)
        print(f"    base {b:>2}:  repeat {rs:.4f}   naive {naive:.4f}   "
              f"deficit {100 * (1 - rs / naive):.1f}%")

    print("\n[C] The bias decays, slowly: repeat share by decade [10^k, 10^(k+1))")
    for b in DECADE_TRANS_BASES:
        naive = 1 / len(units(b))
        print(f"  base {b} (naive {naive:.4f}):")
        for k, tot, s in decade_repeat_shares(res, b):
            print(f"    10^{k:<2} {s:.4f}   ({tot} pairs)")

    print("\n[D] Chebyshev races (which legal digit is ahead)")
    print("  mod 4 (base-4 last digit 3 vs 1):")
    print(race_summary(res, "race4"))
    print("  mod 3 (base-3 last digit 2 vs 1):")
    print(race_summary(res, "race3"))

    print("\n[E] Leading digits, base 10, primes to 1e8 (contrast: NOT Benford,")
    print("    trending flat; the action is in the last digit, not the first)")
    print(leading_digit_note())

    print("\nVERDICT: legal digits = units mod b; shares equidistribute; the")
    print("repeat deficit is present in every base and decays like log log x / log x;")
    print("the races lean nonresidue almost always. All four facts are one story:")
    print("divisibility + PNT-in-progressions + Hardy-Littlewood correlations.")
    return res


if __name__ == "__main__":
    N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8
    main(N)
