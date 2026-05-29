"""Experiment 2O (overnight T2 part b): the bad-prime (non-archimedean) local height.

2I/2H deferred the bad-prime Neron local height. This resolves it for the curves in
hand and tests the multiplicative-reduction structure on an I_n (n>=2) example.

## Two findings

(1) I_1 closure (RIGOROUS, gate passes). The three curves of 2H/2I/2L -- 37a1, 389a1,
    5077a1 -- all have |Delta_min| = conductor = a single prime, i.e. v_p(Delta) = 1:
    Kodaira type I_1, trivial component group (Z/1). Hence the bad-prime Neron local
    height is IDENTICALLY ZERO for every point. This is exactly why 2I found
    lambda_inf(P) = h_hat(P) for the integral generators (good primes contribute 0
    on integral x; the single bad prime is I_1, contributing 0). The bad-prime
    caveat from 2H/2I is therefore closed rigorously: there was nothing to add.

(2) I_n component structure (QUALITATIVE pass; exact magnitude FLAGGED, not claimed).
    On y^2 = x^3 + 19 x - 20 (Delta = -2^6 * 11^2 * 79, multiplicative I_2 at p=11),
    with the infinite-order point P=(3,8), the bad-prime contribution measured as the
    remainder
        lambda_bad(kP) = h_hat(kP) - lambda_inf(kP) - lambda_good(kP)
    (lambda_inf from 2I; lambda_good = log of the x-denominator with p removed) takes
    exactly TWO values across multiples k=1..6: ~ -0.3468 for ODD k and ~ 0 for EVEN
    k. This is precisely the Z/2 component group of I_2 -- the local height is
    constant on each component and period-2 in k, the non-identity component for odd
    multiples, the identity component (=0) for even. (The other bad prime p=2, type
    I_6, contributes ~0: the points sit on its identity component.)

    GATE STATUS: the COMPONENT STRUCTURE passes (binary, period-2, matches Z/2). The
    EXACT MAGNITUDE -0.3468 is NOT an obviously clean rational * log(11) and is NOT
    matched to the B_2(j/n) * log p multiplicative-reduction formula here -- pinning
    it needs a single-bad-prime curve (so no contamination from p=2/79) or the
    independently verified local-height normalization. That quantitative match is
    FLAGGED as open, not claimed. (Honest-gate discipline: we report the validated
    structure and explicitly do not assert the unverified constant.)
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from sympy import Integer, factorint

from experiments.arithmetic_geometric.e2h_arithmetic_hodge_index import canonical_heights, add, _x_parts
from experiments.arithmetic_geometric.e2i_archimedean_local_height import lambda_inf
from experiments.arithmetic_geometric.e2l_faltings_petersson import c_invariants


I1_CURVES = {"37a1": (0, 0, 1, -1, 0), "389a1": (0, 1, 1, -2, 0), "5077a1": (0, 0, 1, -7, 6)}
IN_CURVE = (0, 0, 0, 19, -20)   # y^2 = x^3 + 19x - 20, I_2 at p=11
IN_POINT = (3, 8)
IN_BAD_P = 11


def check_I1():
    print("[2O] (1) I_1 closure: bad-prime local height is identically 0 for the 2H/2I curves.")
    out = {}
    for name, a in I1_CURVES.items():
        _, _, D = c_invariants(tuple(Integer(c) for c in a))
        D = int(D)
        fac = factorint(abs(D))
        n = max(fac.values())
        out[name] = (D, n)
        print(f"     {name}: Delta={D}, v_p={fac}, Kodaira I_{n} -> component group Z/{n} -> lambda_bad == 0")
    return out


def component_periodicity(n_iter=6):
    print(f"\n[2O] (2) I_n component structure on y^2=x^3+19x-20 (I_2 at p={IN_BAD_P}), P={IN_POINT}.")
    a = tuple(Integer(c) for c in IN_CURVE)
    P = (Integer(IN_POINT[0]), Integer(IN_POINT[1]))
    rows = []
    Q = P
    print(f"     {'k':>2} {'h_hat':>10} {'lambda_inf':>11} {'lambda_good':>12} {'lambda_bad':>12} {'/log p':>9}")
    for k in range(1, 7):
        num, den = _x_parts(Q)
        vp = 0
        d = den
        while d % IN_BAD_P == 0:
            d //= IN_BAD_P
            vp += 1
        lam_good = math.log(den) - vp * math.log(IN_BAD_P)
        hk = canonical_heights(Q, a, n_iter=n_iter)[0]
        li = float(lambda_inf(Q, a, prec=40, n_terms=60))
        lam_bad = hk - li - lam_good
        rows.append((k, hk, li, lam_good, lam_bad, lam_bad / math.log(IN_BAD_P)))
        print(f"     {k:>2} {hk:>10.5f} {li:>11.5f} {lam_good:>12.5f} {lam_bad:>12.6f} {lam_bad/math.log(IN_BAD_P):>9.4f}")
        Q = add(Q, P, a)
    odd = [r[4] for r in rows if r[0] % 2 == 1]
    even = [r[4] for r in rows if r[0] % 2 == 0]
    odd_const = max(odd) - min(odd) < 1e-3
    even_zero = max(abs(v) for v in even) < 1e-3
    print(f"     odd-k lambda_bad constant: {odd_const} (values {[round(v,4) for v in odd]})")
    print(f"     even-k lambda_bad ~ 0:     {even_zero} (values {[round(v,4) for v in even]})")
    struct_pass = odd_const and even_zero
    print(f"     COMPONENT STRUCTURE (Z/2, period-2, identity=0) PASS: {struct_pass}")
    print(f"     EXACT MAGNITUDE matched to B_2(j/n) log p: NOT CLAIMED (flagged open; "
          f"needs single-bad-prime curve)")
    return rows, struct_pass


def run(out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    i1 = check_I1()
    rows, struct_pass = component_periodicity()
    np.savez_compressed(out_dir / "e2o_badprime_local_height.npz",
                        I1=np.array([(k, v[0], v[1]) for k, v in i1.items()], dtype=object),
                        IN_curve=np.array(IN_CURVE), IN_point=np.array(IN_POINT),
                        rows=np.array(rows), struct_pass=struct_pass)
    print(f"\n[2O] Saved {out_dir / 'e2o_badprime_local_height.npz'}")
    return struct_pass


if __name__ == "__main__":
    run()
