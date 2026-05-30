"""Gap B check (Direction 10B): is the Mobius factor intrinsic to the cyclotomic
combinatorics of THH?

The THH(Z) -> TC(Z) reduction is built from the cyclotomic structure: the cyclic
bar construction's C_n-fixed points decompose into components indexed by
NECKLACES (aperiodic cyclic words). The count of aperiodic necklaces of length n
on q letters is the necklace polynomial
    M(q, n) = (1/n) sum_{d|n} mu(n/d) q^d,
which is LITERALLY Mobius inversion of  q^n = sum_{d|n} d M(q,d).

Direction 10's first pass (e_thh_vonmangoldt) showed the von Mangoldt sum is the
Mobius transform (factor 1/zeta) of the THH log-order series -zeta'. The open
question (Gap B) is whether the THH -> TC reduction supplies that mu. This
experiment shows mu is already present in the cyclotomic indexing itself:

  (a) M(q,n) is a non-negative integer for integer q >= 1 (it counts necklaces).
  (b) sum_{d|n} d M(q,d) = q^n exactly  (the Mobius-inverse pair; THIS is the
      same Mobius inversion as Lambda = mu * log, over the divisor lattice).
  (c) The cyclotomic identity (Metropolis-Rota)
          1/(1 - q t) = prod_{n>=1} (1 - t^n)^{-M(q,n)}
      holds as a formal power series in t. The necklace polynomials are the
      exponents organizing the free/cyclotomic structure -- the combinatorial
      avatar of the cyclotomic (tom Dieck-style) splitting that the C_n-fixed
      points of THH realize.
  (d) Bridge: the necklace inversion (b) and the Dirichlet inversion
      Lambda = mu * log are the SAME Mobius inversion. So the mu that turns the
      THH log-order series -zeta' into the von Mangoldt sum -zeta'/zeta is the
      same mu that governs the cyclotomic C_n-fixed-point decomposition. The
      Mobius factor is INTRINSIC to the cyclotomic geometry, not imported.

This does not prove the TC Euler characteristic equals -zeta'/zeta (that needs
tracking the necklace weights through the regularized trace; see 10B step 1
proper). It establishes that the mu has a structural home in the cyclotomic
data, which is the substance of Gap B's plausibility.

Outputs:
  - e_necklace_mobius.npz
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path

import numpy as np


def mobius(n: int) -> int:
    if n == 1:
        return 1
    m, result, p = n, 1, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            result = -result
        p += 1
    if m > 1:
        result = -result
    return result


def divisors(n: int):
    ds = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            ds.append(d)
            if d != n // d:
                ds.append(n // d)
        d += 1
    return sorted(ds)


def necklace_polynomial(q: int, n: int) -> Fraction:
    """M(q,n) = (1/n) sum_{d|n} mu(n/d) q^d  (exact rational; integer for q>=1)."""
    s = sum(mobius(n // d) * q ** d for d in divisors(n))
    return Fraction(s, n)


def cyclotomic_identity_check(q: int, T: int):
    """Verify 1/(1-qt) = prod_{n=1}^T (1-t^n)^{-M(q,n)} as power series mod t^{T+1}.

    Returns max abs coefficient difference (exact, should be 0 up to truncation).
    LHS coefficients of 1/(1-qt) are q^k. We build the RHS product of
    (1-t^n)^{-M(q,n)} via exact integer/rational power-series arithmetic.
    """
    # RHS as a list of Fraction coefficients, index 0..T.
    rhs = [Fraction(0)] * (T + 1)
    rhs[0] = Fraction(1)
    for n in range(1, T + 1):
        e = necklace_polynomial(q, n)  # exponent M(q,n)
        if e == 0:
            continue
        # multiply current rhs by (1 - t^n)^{-e}.
        # (1 - t^n)^{-e} = sum_{k>=0} C(e+k-1, k) t^{nk}  (generalized binomial,
        # valid for integer e>=1 since M(q,n) is a non-negative integer for q>=1).
        e_int = int(e)
        assert e == e_int and e_int >= 0, f"M({q},{n})={e} not a non-negative integer"
        factor = [Fraction(0)] * (T + 1)
        k = 0
        while n * k <= T:
            # coefficient C(e_int + k - 1, k)
            num = 1
            for j in range(k):
                num *= (e_int + j)
            from math import factorial
            factor[n * k] = Fraction(num, factorial(k))
            k += 1
        # convolve rhs *= factor (mod t^{T+1})
        new = [Fraction(0)] * (T + 1)
        for i in range(T + 1):
            if rhs[i] == 0:
                continue
            for j in range(0, T + 1 - i):
                if factor[j] != 0:
                    new[i + j] += rhs[i] * factor[j]
        rhs = new
    lhs = [Fraction(q) ** k for k in range(T + 1)]
    diffs = [abs(lhs[k] - rhs[k]) for k in range(T + 1)]
    return max(diffs), lhs, rhs


def run(n_max: int = 30, T: int = 24, q_values=(2, 3, 5), out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("[NM] (a) Necklace polynomials M(q,n) are non-negative integers (counts):")
    all_int = True
    for q in q_values:
        vals = [necklace_polynomial(q, n) for n in range(1, 13)]
        ok = all(v.denominator == 1 and v >= 0 for v in vals)
        all_int = all_int and ok
        print(f"     q={q}: M(q,1..12) = {[int(v) for v in vals]}  integer&>=0: {ok}")

    print("\n[NM] (b) Mobius-inverse pair: sum_{d|n} d M(q,d) = q^n (exact)")
    max_b_err = 0
    for q in q_values:
        for n in range(1, n_max + 1):
            lhs = sum(d * necklace_polynomial(q, d) for d in divisors(n))
            rhs = Fraction(q) ** n
            max_b_err = max(max_b_err, abs(lhs - rhs))
    print(f"     max|sum_{{d|n}} d M(q,d) - q^n| over q in {q_values}, n<= {n_max}: {max_b_err}")

    print("\n[NM] (c) Cyclotomic identity 1/(1-qt) = prod_n (1-t^n)^{-M(q,n)} (mod t^%d):" % (T + 1))
    max_c_err = Fraction(0)
    for q in q_values:
        err, _, _ = cyclotomic_identity_check(q, T)
        max_c_err = max(max_c_err, err)
        print(f"     q={q}: max coeff diff = {err}")

    print("\n[NM] (d) BRIDGE: necklace inversion (b) and Lambda = mu*log are the SAME Mobius")
    print("     inversion over the divisor lattice. Demonstrate Lambda(n) = sum_{d|n} mu(n/d) log d")
    print("     reproduces von Mangoldt (log p on prime powers, else 0):")
    import math
    bridge_ok = True
    examples = []
    for n in [2, 3, 4, 6, 8, 9, 12, 16, 30]:
        lam = sum(mobius(n // d) * math.log(d) for d in divisors(n))
        # expected von Mangoldt
        m, p0 = n, 0
        is_pp, base = True, None
        for p in range(2, n + 1):
            if m % p == 0:
                base = p
                while m % p == 0:
                    m //= p
                is_pp = (m == 1)
                break
        expected = math.log(base) if is_pp else 0.0
        ok = abs(lam - expected) < 1e-12
        bridge_ok = bridge_ok and ok
        examples.append((n, lam, expected, ok))
        tag = "prime power" if is_pp else "composite -> 0"
        print(f"     n={n:2d}: (mu*log)(n)={lam:+.6f}  vonMangoldt={expected:+.6f}  [{tag}]  ok={ok}")

    print("\n[NM] ===== VERDICT (Gap B plausibility) =====")
    verdict = all_int and max_b_err == 0 and max_c_err == 0 and bridge_ok
    if verdict:
        print("     The necklace polynomials (the cyclotomic C_n-fixed-point indexing) ARE")
        print("     Mobius inversion (b,c), and that is the SAME Mobius inversion as the")
        print("     Lambda = mu*log that produces the von Mangoldt sum from the THH log-orders (d).")
        print("     => The mu factor Gap B needs is INTRINSIC to the cyclotomic combinatorics,")
        print("     not imported by hand. This is structural support for the conjecture that the")
        print("     THH -> TC reduction supplies 1/zeta. (NOT yet a proof that TC's Euler char =")
        print("     -zeta'/zeta; that needs the necklace weights tracked through the regularized")
        print("     trace -- 10B step 1 proper.)")
    else:
        print("     A check FAILED; inspect above. Gap B's combinatorial support is not clean.")

    np.savez_compressed(
        out_dir / "e_necklace_mobius.npz",
        q_values=np.array(q_values),
        max_b_err=float(max_b_err),
        max_c_err=float(max_c_err),
        bridge_ok=bridge_ok,
        n_max=n_max, T=T,
    )
    print(f"\n[NM] Saved {out_dir / 'e_necklace_mobius.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=30)
    parser.add_argument("--T", type=int, default=24)
    args = parser.parse_args()
    run(n_max=args.n_max, T=args.T)
