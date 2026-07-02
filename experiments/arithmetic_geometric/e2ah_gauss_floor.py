"""e2ah: the Gauss-lemma height floor in van Frankenhuijsen's disc model (no Siegel slot).

WHY THIS PROBE EXISTS
---------------------
van Frankenhuijsen's Nevanlinna model of Spec(Z) x Spec(Z) (arXiv:0806.0044, Section 4;
reading note docs/03_research/reading_notes/vanFrankenhuijsen-2008-Nevanlinna-RH.md)
models the auxiliary function of the Stepanov-Bombieri engine as an integer-coefficient
function on the unit disc, with primes entering as prescribed zeros at z = 1/p. The
counting layer is exact: for the canonical product

    f_x(z) = prod_{p <= x} (p z - 1)^{m_p},    m_p = floor(log_p x),

the Nevanlinna counting function equals Chebyshev psi(x). This probe verifies the
model's HEIGHT FLOOR, the reason a pigeonhole (Siegel's lemma) can never produce a
cheap auxiliary function in this model:

    GAUSS-LEMMA FLOOR. If f in Z[z], f != 0, vanishes at z = 1/p with multiplicity
    at least m_p for each prime p in a finite set P, then (p z - 1)^{m_p} divides f
    in Z[z] (each p z - 1 is primitive, so Gauss's lemma descends the Q[z]
    divisibility), the factors are pairwise non-associated irreducibles, hence

        |lead(f)| >= prod_{p in P} p^{m_p},  i.e.  log|lead(f)| >= sum_P m_p log p.

    With vF's multiplicities the right side is EXACTLY psi(x), and f_x attains
    equality. Integer-exact form: exp(psi(x)) = lcm(1, ..., x) = |lead(f_x)|.

INTERPRETATION (the no-go this probe pins down): in the disc model the minimal height
of a prime-forced vanisher IS the quantity the engine is supposed to bound (psi(x)).
There is zero slack for a Siegel-lemma / pigeonhole construction (S3); the model's
only open slot is the S4/R1 cheap-multiplicity operator, the missing Frobenius /
derivation (see docs/03_research/stepanov_engine_audit.md). PNT itself is the
statement that the floor is ~ x.

WHAT IS CHECKED (all integer-exact; sympy expansion vs python-int arithmetic as two
independent code paths)
  A. Canonical product: |lead(f_x)| == prod p^{m_p} == lcm(1..x) for a sweep of x
     (log lead = psi(x) exactly, checked at the integer level), plus a float sanity
     check of sum m_p log p against log lcm(1..x).
  B. Cofactor stress: random g in Z[z], f = g * prod (p z - 1)^{m_p}; the prescribed
     vanishing is re-verified by exact division; the floor holds; equality holds
     iff |lead(g)| = 1.
  C. Naive-interpolation stress: integer polynomials forced to vanish at {1/p} with
     the prescribed multiplicities, built from the rational nullspace of the
     vanishing conditions (integerized to primitive vectors), NOT as cofactor times
     product. Random lattice combinations obey the floor, and at the minimal degree
     D = sum m_p the primitive integer vanisher is EXACTLY +-(canonical product): a
     complete no-lower-height certificate at degree D, since the rational kernel is
     1-dimensional and an integral rational multiple of a primitive vector has an
     integer scalar.

Lean companion: lean/ZetaRH/GaussFloor.lean (#GF-1..#GF-5) proves the divisibility
floor sorry-free and axiom-clean; this probe is the mechanical-computation layer of
the verification stack for the same claim.

Run:
  python -m experiments.arithmetic_geometric.e2ah_gauss_floor
"""

from __future__ import annotations

import math
import random
import sys

import sympy as sp
from sympy import Rational

z = sp.Symbol("z")


def vf_multiplicity(p: int, x: int) -> int:
    """m_p = floor(log_p x), computed in exact integer arithmetic (no floats)."""
    m, q = 0, p
    while q <= x:
        m += 1
        q *= p
    return m


def canonical_product(m: dict[int, int]) -> sp.Poly:
    """The vF canonical product prod_p (p z - 1)^{m_p} as an exact ZZ polynomial."""
    f = sp.Integer(1)
    for p, mp in m.items():
        f *= (p * z - 1) ** mp
    return sp.Poly(sp.expand(f), z, domain="ZZ")


def floor_value(m: dict[int, int]) -> int:
    """The Gauss-lemma floor prod_p p^{m_p} as an exact integer."""
    out = 1
    for p, mp in m.items():
        out *= p**mp
    return out


# ---------------------------------------------------------------------------
# A. Canonical product: log lead = psi(x) exactly (integer form: lead = lcm(1..x)).
# ---------------------------------------------------------------------------

def check_canonical(xs: list[int]) -> bool:
    ok = True
    print("A. Canonical product f_x: |lead| == prod p^{m_p} == lcm(1..x) (= e^{psi(x)})")
    for x in xs:
        primes = list(sp.primerange(2, x + 1))
        m = {p: vf_multiplicity(p, x) for p in primes}
        f = canonical_product(m)
        lead = abs(int(f.LC()))                      # path 1: sympy expansion
        prod_pm = floor_value(m)                     # path 2: integer arithmetic
        lcm_val = math.lcm(*range(1, x + 1))         # path 3: e^{psi(x)} = lcm(1..x)
        # Float sanity: psi(x) = sum m_p log p vs log lcm(1..x).
        psi_float = sum(mp * math.log(p) for p, mp in m.items())
        float_ok = math.isclose(psi_float, math.log(lcm_val), rel_tol=1e-12)
        good = (lead == prod_pm == lcm_val) and float_ok
        ok &= good
        print(f"   x={x:4d}  deg f = {f.degree():3d}  psi(x) = {psi_float:10.4f}  "
              f"lead == prod == lcm: {lead == prod_pm == lcm_val}  "
              f"[{'ok' if good else 'FAIL'}]")
    return ok


# ---------------------------------------------------------------------------
# B. Cofactor stress: f = g * prod (p z - 1)^{m_p}, random integer cofactor g.
# ---------------------------------------------------------------------------

def check_cofactor(trials: int, rng: random.Random) -> bool:
    pool = [2, 3, 5, 7, 11, 13]
    fails = 0
    eq_cases = 0
    for _ in range(trials):
        P = rng.sample(pool, rng.randint(1, 4))
        m = {p: rng.randint(1, 3) for p in P}
        deg_g = rng.randint(0, 5)
        coeffs = [rng.randint(-9, 9) for _ in range(deg_g + 1)]
        while coeffs[0] == 0:
            coeffs[0] = rng.randint(-9, 9)
        g = sum(c * z ** (deg_g - i) for i, c in enumerate(coeffs))
        f = sp.Poly(sp.expand(g * canonical_product(m).as_expr()), z, domain="ZZ")
        # Re-verify the prescribed vanishing by exact division over QQ.
        for p, mp in m.items():
            _, r = sp.div(f.as_expr(), sp.expand((p * z - 1) ** mp), z, domain="QQ")
            if sp.simplify(r) != 0:
                fails += 1
                break
        else:
            lead = abs(int(f.LC()))
            fv = floor_value(m)
            if lead < fv:
                fails += 1
            elif lead == fv:
                eq_cases += 1
                if abs(coeffs[0]) != 1:
                    fails += 1  # equality is only possible for a unit cofactor lead
            elif abs(coeffs[0]) == 1:
                fails += 1      # unit cofactor lead must give exact equality
    ok = fails == 0
    print(f"B. Cofactor stress: {trials} trials, floor violations/inconsistencies: "
          f"{fails}, equality cases (|lead g| = 1): {eq_cases}  "
          f"[{'ok' if ok else 'FAIL'}]")
    return ok


# ---------------------------------------------------------------------------
# C. Naive interpolation: vanishers from the nullspace of the derivative conditions.
# ---------------------------------------------------------------------------

def kernel_basis(m: dict[int, int], deg: int) -> list[list[int]]:
    """Primitive integer vectors spanning the rational kernel of the vanishing
    conditions f^{(j)}(1/p) = 0 (j < m_p) on f = sum_{i<=deg} b_i z^i."""
    n = deg + 1
    rows = []
    for p, mp in m.items():
        a = Rational(1, p)
        for j in range(mp):
            rows.append([sp.ff(i, j) * a ** (i - j) if i >= j else Rational(0)
                         for i in range(n)])
    null = sp.Matrix(rows).nullspace()
    basis = []
    for v in null:
        den = math.lcm(*[int(sp.Rational(t).q) for t in v])
        vi = [int(t * den) for t in v]
        g = math.gcd(*[abs(c) for c in vi])
        basis.append([c // g for c in vi])
    return basis


def poly_from_vec(vec: list[int]) -> sp.Poly | None:
    expr = sum(c * z**i for i, c in enumerate(vec))
    if expr == 0:
        return None
    return sp.Poly(expr, z, domain="ZZ")


def check_interpolation(configs: list[dict[int, int]], rng: random.Random,
                        combos_per_config: int) -> bool:
    ok = True
    print("C. Naive interpolation (nullspace lattice), floor + minimal-degree rigidity")
    for m in configs:
        D = sum(m.values())
        fv = floor_value(m)
        # C1: minimal degree D. The rational kernel must be 1-dim and its primitive
        # integer generator must be +-(canonical product): NO cheaper vanisher exists.
        basis = kernel_basis(m, D)
        canon = [int(c) for c in reversed(canonical_product(m).all_coeffs())]
        rigid = (len(basis) == 1
                 and (basis[0] == canon or [-c for c in basis[0]] == canon))
        ok &= rigid
        # C2: degrees D+1 .. D+3, random integer lattice combinations obey the floor.
        viol = 0
        checked = 0
        for extra in (1, 2, 3):
            bas = kernel_basis(m, D + extra)
            for _ in range(combos_per_config):
                vec = [0] * (D + extra + 1)
                for b in bas:
                    c = rng.randint(-5, 5)
                    vec = [u + c * w for u, w in zip(vec, b)]
                f = poly_from_vec(vec)
                if f is None:
                    continue
                checked += 1
                # Spot-verify the forced vanishing (exact rational evaluation).
                p0, mp0 = next(iter(m.items()))
                fq = sp.Poly(f.as_expr(), z, domain="QQ")
                for j in range(mp0):
                    if fq.diff((z, j)).eval(Rational(1, p0)) != 0:
                        viol += 1
                        break
                else:
                    if abs(int(f.LC())) < fv:
                        viol += 1
        ok &= viol == 0
        print(f"   P^m = {m}: minimal-degree D={D} kernel is 1-dim and == +-canonical:"
              f" {rigid}; {checked} random lattice vanishers, floor violations: {viol}"
              f"  [{'ok' if rigid and viol == 0 else 'FAIL'}]")
    return ok


def main() -> int:
    rng = random.Random(20260701)
    results = {
        "A_canonical_psi": check_canonical([2, 3, 5, 10, 20, 30, 50, 100]),
        "B_cofactor": check_cofactor(300, rng),
        "C_interpolation": check_interpolation(
            [{2: 1, 3: 1}, {2: 2, 3: 1}, {2: 1, 3: 1, 5: 1}, {2: 2, 5: 2},
             {3: 1, 7: 2}, {2: 1, 3: 2, 5: 1}],
            rng, combos_per_config=25),
    }
    print()
    all_ok = all(results.values())
    for name, res in results.items():
        print(f"  {name:20s} {'PASS' if res else 'FAIL'}")
    print(f"\ne2ah GAUSS-LEMMA FLOOR: {'PASS' if all_ok else 'FAIL'} "
          f"(floor = psi(x) exactly; equality attained by the canonical product; "
          f"no Siegel-lemma savings in the vF disc model)")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
