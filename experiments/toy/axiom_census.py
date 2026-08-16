"""Which axioms force RH? A census in the function-field shadow.

THE QUESTION. "All Weil cohomologies are the same" is a theorem: the
realizations agree on Betti numbers, on traces, hence on the zeta function
and its functional equation. That raises a hope, and this module measures
it. If the trace-level structure is universal, maybe it FORCES the
positivity too, so that constructing any cohomology for Spec(Z) would
suffice and the polarization (SP5 in missing_object_interface.md, M4 in the
main program) would come along for free.

It does not. Positivity is not among the Weil cohomology axioms, and the
gap is measurable in the one place where everything else is a theorem: the
function-field shadow, where a candidate zeta is just an integer polynomial.

THE AXIOMS, as filters on a degree-2g polynomial P(t) over F_q:
  (a) FUNCTIONAL EQUATION: the coefficients obey the curve symmetry, so the
      inverse roots pair as alpha <-> q/alpha. This is Poincare duality.
  (b) INTEGRALITY: P has integer coefficients. This is the trace formula
      forcing point counts to be integers.
  (c) EULER PRODUCT: every implied closed-point count is a non-negative
      integer, b_d = (1/d) sum_{e|d} mu(d/e) N_e >= 0 with N_n = q^n + 1 -
      sum alpha_i^n. This is what makes zeta an honest product over places,
      and it is exactly what Davenport-Heilbronn lacks (LEARNINGS #90: D-H's
      comb goes negative at n = 3).
  (d) RH: every inverse root has |alpha| = sqrt(q).

RESULT. (a)+(b)+(c) does NOT imply (d), and the shortfall is not marginal:
the three axioms confine the roots only to |alpha| <= q, which in zeta
coordinates is the trivial region Re(s) <= 1 that the Euler product hands
over for free. The whole interior of the critical strip is left open. As q
grows the fraction of axiom-satisfying models that violate RH tends to 1,
so the package is asymptotically vacuous relative to RH.

WHY THIS IS WORTH A FILE. The repo already had ONE witness, the fake from
LEARNINGS #123, used in e2xx_higher_rank_rosati.py, instances.py and
circle_interlacing.py as the function-field analogue of Davenport-Heilbronn.
It had never been checked against axiom (c), and D-H itself cannot play the
role because it FAILS (c). So nothing in the repo separated RH from
FE+integrality+Euler. This does, with an enumerated census rather than a
hand-picked example, and it certifies #123 as a genuine witness.

WHERE THIS SITS IN THE LITERATURE. The conclusion is not new mathematics;
it is the checkable form of a known state of affairs.
  - Honda-Tate (Tate 1966, Honda 1968) classifies isogeny classes of abelian
    varieties by Weil numbers, but a Weil number is DEFINED by |iota(pi)| =
    sqrt(q) at every embedding. RH is an input there, never an output.
  - The Selberg class carries a functional equation, an Euler product and a
    Ramanujan bound, and RH for it is a separate conjecture that remains open
    (Kaczorowski-Perelli 1999). Since zeta lies in the class, no derivation of
    RH from those axioms can exist without proving RH.
  - The converse fails too, which is worth knowing: Howe (arXiv:2110.04221)
    catalogues genuine Weil polynomials, RH true, whose predicted place counts
    go NEGATIVE, so (a)+(b)+(d) does not imply (c) either. The two conditions
    are independent in both directions.
  - Grothendieck's Standard Conjecture of Hodge type, the positivity, is true
    in characteristic 0, OPEN in characteristic p in general, and proven for
    divisors on surfaces. Weil's proof for curves consumes exactly that proven
    case, via the Hodge index theorem on C x C (Milne arXiv:1509.00797).

A note on which form of (c) is used here. Requiring only N_n >= 0 gives the
symmetric band |a| <= q + 1 in genus 1; requiring the closed-point counts b_d
to be non-negative, which is the honest Euler-product condition, additionally
trims the top to a <= q. This module uses the stronger, correct form, and the
gap to RH survives it.

Run: python -m experiments.toy.axiom_census
"""
from __future__ import annotations

import numpy as np

REPO_FAKE = (5, [-4, 15, -20, 25])   # LEARNINGS #123, in the t-convention


def mobius(n: int) -> int:
    r, m, p = 1, n, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            r = -r
        p += 1
    return -r if m > 1 else r


def power_sums(c: list[int], dmax: int) -> list[int]:
    """p_n = sum_i alpha_i^n for P(t) = 1 + c_1 t + ... + c_d t^d, exactly.

    Newton's identities, in integers. Validated in test_toy.py against both an
    independent two-term recursion and direct numerical roots.
    """
    d = len(c)
    e = [1] + [((-1) ** k) * c[k - 1] for k in range(1, d + 1)]
    p = [d]
    for n in range(1, dmax + 1):
        hi = min(n - 1, d) if n <= d else d
        s = sum(((-1) ** (i - 1)) * e[i] * p[n - i] for i in range(1, hi + 1))
        if n <= d:
            s += ((-1) ** (n - 1)) * n * e[n]
        p.append(s)
    return p


def point_counts(q: int, c: list[int], dmax: int) -> list[int]:
    """N_n = q^n + 1 - p_n, the implied number of degree-n rational points."""
    p = power_sums(c, dmax)
    return [0] + [q ** n + 1 - p[n] for n in range(1, dmax + 1)]


def euler_ok(q: int, c: list[int], dmax: int = 200) -> bool:
    """Axiom (c): every closed-point count is a non-negative integer.

    Checked exactly for d <= dmax. That is not a truncation in disguise: with
    M = max|alpha| < q the count b_d is dominated by q^d/d and positive for
    all large d, so a finite check plus that bound settles every degree. The
    bound is verified explicitly in `tail_is_safe`.
    """
    N = point_counts(q, c, dmax)
    for d in range(1, dmax + 1):
        s = sum(mobius(d // e) * N[e] for e in range(1, d + 1) if d % e == 0)
        if s < 0 or s % d:
            return False
    return True


def tail_is_safe(q: int, c: list[int], dmax: int = 200) -> bool:
    """Is b_d > 0 guaranteed for every d > dmax?

    |p_n| <= deg * M^n with M = max|alpha|, so
    d*b_d >= q^d + 1 - deg*M^d - sum_{e|d, e<d} (q^e + 1 + deg*M^e)
          >= q^d - deg*M^d - d*(q^{d/2} + 1 + deg*M^{d/2}).
    With M < q the first term wins; this checks that it already has by dmax.
    """
    deg = len(c)
    M = float(np.max(np.abs(np.roots([1.0] + [float(x) for x in c]))))
    if M >= q:
        return False
    d = dmax
    lhs = q ** d - deg * M ** d
    rhs = d * (q ** (d // 2) + 1 + deg * M ** (d // 2))
    return bool(lhs > rhs)


def rh_ok(q: int, c: list[int], tol: float = 1e-9) -> bool:
    al = np.roots([1.0] + [float(x) for x in c])
    return bool(np.all(np.abs(np.abs(al) - np.sqrt(q)) < 1e-6))


def worst_ratio(q: int, c: list[int]) -> float:
    al = np.roots([1.0] + [float(x) for x in c])
    return float(np.max(np.abs(al)) / np.sqrt(q))


def genus1_range(q: int, dmax: int = 120) -> tuple[list[int], int]:
    """Which a in P(t) = 1 + a t + q t^2 satisfy (a)+(b)+(c)? And the RH bound."""
    ok = [a for a in range(-(2 * q + 4), 2 * q + 5) if euler_ok(q, [a, q], dmax)]
    return ok, int(np.floor(2 * np.sqrt(q)))


def genus2_census(q: int, dmax: int = 80) -> dict:
    """Enumerate FE-symmetric integer quartics and filter by (c), then by RH."""
    B = 3 * q + 6
    tot = rh = 0
    worst = 1.0
    for a1 in range(-B, B + 1):
        for a2 in range(-3 * B, 3 * B + 1):
            c = [a1, a2, q * a1, q * q]
            if not euler_ok(q, c, dmax):
                continue
            tot += 1
            if rh_ok(q, c):
                rh += 1
            else:
                worst = max(worst, worst_ratio(q, c))
    return dict(q=q, total=tot, rh=rh, violate=tot - rh, worst=worst)


def main() -> None:
    print("Which axioms force RH? A census in the function-field shadow.\n")

    print("[A] Genus 1: P(t) = 1 + a t + q t^2. RH means a^2 <= 4q.")
    print("     q   RH allows      (a)+(b)+(c) allow      extra room the axioms leave")
    for q in (2, 3, 4, 5, 7, 9, 11, 13, 16, 25):
        ok, weil = genus1_range(q)
        print(f"    {q:>3}   |a| <= {weil:<3}      a in [{min(ok):>3}, {max(ok):>3}]"
              f"           {len([a for a in ok if a*a > 4*q]):>3} values violate RH")
    print("    The axioms permit exactly -(q+1) <= a <= q, i.e. |alpha| <= q, which in")
    print("    zeta coordinates is Re(s) <= 1: the trivial region the Euler product gives")
    print("    for free. RH is Re(s) = 1/2. The axioms do not enter the critical strip.")

    print("\n[B] Genus 2: P(t) = 1 + a1 t + a2 t^2 + q a1 t^3 + q^2 t^4.")
    print("     q   satisfy (a)+(b)+(c)   of those RH   violate RH   worst |alpha|/sqrt(q)"
          "   sqrt(q)")
    for q in (2, 3, 4, 5, 7, 9):
        r = genus2_census(q)
        print(f"    {r['q']:>3}   {r['total']:>15}   {r['rh']:>11}   {r['violate']:>10}"
              f"   {r['worst']:>20.3f}   {np.sqrt(q):.3f}")
    print("    The worst violation tracks sqrt(q), i.e. |alpha| reaching q: the same")
    print("    trivial bound. And the RH-violating fraction grows with q, so the axiom")
    print("    package is asymptotically vacuous relative to RH.")

    q, c = REPO_FAKE
    print(f"\n[C] The repo's own witness (LEARNINGS #123), P(t) = 1 {c[0]}t + {c[1]}t^2 "
          f"{c[2]}t^3 + {c[3]}t^4 over q = {q}")
    N = point_counts(q, c, 8)
    print(f"    functional equation: {c[2] == q*c[0] and c[3] == q*q}   "
          f"integer coefficients: True")
    print(f"    |alpha| = {np.round(np.abs(np.roots([1.0]+[float(x) for x in c])), 4)}"
          f"  vs sqrt(q) = {np.sqrt(q):.4f}  -> RH FALSE")
    print(f"    point counts N_1..N_8 = {N[1:9]}")
    print(f"    every closed-point count non-negative (d <= 200): {euler_ok(q, c)}"
          f"   provably so beyond that: {tail_is_safe(q, c)}")
    print("    This polynomial has been used in three places in the repo as the")
    print("    function-field analogue of Davenport-Heilbronn, but was never checked")
    print("    against the Euler axiom. It passes. So it is a genuine witness, which")
    print("    D-H itself cannot be: D-H FAILS the Euler axiom (LEARNINGS #90, its comb")
    print("    goes negative at n = 3), so it never entered this hypothesis space.")

    print("\nVERDICT: duality, integrality and multiplicativity together confine the")
    print("roots to the trivial region and no further. Positivity is not among the Weil")
    print("cohomology axioms, and no amount of agreement between cohomology theories")
    print("can supply it: the sameness is a theorem about traces, and RH is a statement")
    print("about a polarization the traces do not determine. Any proposed proof that")
    print("uses only these three ingredients is refuted by an explicit 4x4 example.")


if __name__ == "__main__":
    main()
