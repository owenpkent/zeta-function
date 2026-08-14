"""Regression tests for the primes thread (e5a/e5b/e5c).

Standalone module per repo convention: prints "N/N passed", exit 0 iff all
pass. Fast path: everything runs at 10^6 scale plus two small zero sets
(T = 60 and T = 100, disk-cached after first run). Exact integer anchors
(pi, twin/cousin/sexy counts, the 26861 race flip) are external literature
values; tolerances on shares and formula errors are pinned from measurement
with ~1.5x margin.
"""
from __future__ import annotations

import numpy as np

from experiments.primes.primestream import flat_primes, stream, units
from experiments.primes.e5b_twin_primes import MERTENS, twin_prime_constant
from experiments.primes.e5c_explicit_formula import psi_exact, psi_formula, zero_gammas

N = 10**6


def main() -> int:
    res = stream(N)
    checks: list[tuple[str, bool]] = []

    pi_cum = np.cumsum(res["pi_dec"])
    checks.append(("pi(10^4) = 1229 and pi(10^6) = 78498 (external anchors)",
                   int(pi_cum[3]) == 1229 and int(pi_cum[5]) == 78498))

    ps = flat_primes(10**5)
    legal = all(bool(np.all(np.gcd(ps[ps > b] % b, b) == 1)) for b in (3, 4, 10, 12, 30))
    checks.append(("legal last digits are exactly the units mod b", legal))

    dev10 = float(np.abs(res["counts_b10"] / res["counts_b10"].sum() - 0.25).max())
    dev30 = float(np.abs(res["counts_b30"] / res["counts_b30"].sum() - 0.125).max())
    checks.append(("equidistribution at 10^6: max share dev < 2e-3 (meas 5.2e-4)",
                   dev10 < 2e-3 and dev30 < 2e-3))

    reps = {b: float(np.trace(res[f"trans_b{b}"]) / res[f"trans_b{b}"].sum())
            for b in (3, 10, 30)}
    checks.append(("repeat-digit deficit present in bases 3/10/30 "
                   "(meas 0.418/0.154/0.026)",
                   0.36 < reps[3] < 0.47 and 0.10 < reps[10] < 0.20
                   and 0.01 < reps[30] < 0.06))
    checks.append(("repeat share sits well below naive 1/phi(b)",
                   reps[3] < 0.9 * (1 / 2) and reps[10] < 0.8 * (1 / 4)
                   and reps[30] < 0.5 * (1 / 8)))

    twins = int(res["pair2_dec"].sum())
    checks.append(("pair counts at 10^6: twins 8169 (external), cousins 8144, "
                   "sexy 16386",
                   twins == 8169 and int(res["pair4_dec"].sum()) == 8144
                   and int(res["pair6_dec"].sum()) == 16386))

    c2 = twin_prime_constant()
    checks.append(("twin prime constant C2 to 2e-6 (Wrench value 0.6601618158)",
                   abs(c2 - 0.6601618158468696) < 2e-6))

    import mpmath as mp
    mp.mp.dps = 30
    li2_1e6 = float(mp.quad(lambda t: 1 / mp.log(t) ** 2, [2, 4, 16, 256, 65536, 10**6]))
    checks.append(("HL twin prediction within 3% at 10^6 (meas ratio 0.9904)",
                   0.97 < twins / (2 * c2 * li2_1e6) < 1.01))

    checks.append(("Chebyshev mod-4 race first flips at exactly x = 26861; "
                   "mod-3 never flips below 10^6",
                   int(res["race4_first_cross"]) == 26861
                   and int(res["race3_first_cross"]) == 0))

    mert = abs(float(res["recip_dec"].sum()) - (np.log(np.log(N)) + MERTENS))
    checks.append(("sum 1/p matches log log x + Mertens to 5e-4 (meas 3.9e-5)",
                   mert < 5e-4))

    x = np.arange(2.25, 100, 0.5)
    psi = psi_exact(x)
    e13 = np.abs(psi_formula(x, zero_gammas(60.0)) - psi)
    e29 = np.abs(psi_formula(x, zero_gammas(100.0)) - psi)
    checks.append(("explicit formula, 13 zeros: max err < 3.5, mean < 0.9 "
                   "(meas 2.55/0.66)",
                   float(e13.max()) < 3.5 and float(e13.mean()) < 0.9))
    checks.append(("more zeros track psi better: mean err 29 zeros < 13 zeros "
                   "(meas 0.49 < 0.66)",
                   float(e29.mean()) < float(e13.mean()) and float(e29.mean()) < 0.7))

    n_ok = 0
    for name, ok in checks:
        print(f"  [{'ok' if ok else 'FAIL'}] {name}")
        n_ok += ok
    print(f"{n_ok}/{len(checks)} passed")
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
