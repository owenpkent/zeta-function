"""Interlacing families: a NON-variety source of the sqrt(q) bound, and why it does
not transfer to Spec(Z).

Motivation. The Ihara world (ihara.py) shows graph-RH <=> Ramanujan <=> |lambda| <= 2 sqrt(q),
the same sqrt(q) as the function-field Weil bound. In arithmetic that bound (the purity
|alpha| = sqrt(q)) is variety-gated: it is Deligne's theorem, sourced from a variety (the
project's R1 sourcing gap, LEARNINGS #130). In the GRAPH world the same bound has a second
source that uses NO variety at all: Marcus-Spielman-Srivastava (Interlacing Families I,
Annals 2015) prove bipartite Ramanujan graphs of every degree exist by the method of
interlacing families / expected characteristic polynomials. So the graph world CROSSES the
R1 sourcing gap by a combinatorial route.

This experiment does two things:

  Part 1. Exhibits the MSS engine on small graphs and confirms it produces the sqrt(q)
          bound with no variety. The three checkable facts:
            (i)  Godsil-Gutman: the average over edge-signings s of the characteristic
                 polynomial of the signed adjacency A_s equals the MATCHING polynomial mu(G).
            (ii) Heilmann-Lieb: mu(G) is REAL-ROOTED and, for a d-regular graph, all its
                 roots lie in [-2 sqrt(d-1), 2 sqrt(d-1)] = the Ramanujan window.
            (iii)Interlacing: the family {char(A_s)}_s has a common interlacer, so SOME
                 signing s* has max root <= max root of the average <= 2 sqrt(d-1). A good
                 signing (hence a Ramanujan 2-lift) exists, sourced combinatorially.

  Part 2. Shows WHY the engine does not transfer to arithmetic. Its fuel is REAL-ROOTEDNESS
          (Heilmann-Lieb, and the interlacing family needs real-rooted polynomials). Real
          roots come from A_s being SYMMETRIC (self-adjoint). The arithmetic analogue, the
          L-polynomial of a curve (the characteristic polynomial of Frobenius on H^1), is
          NOT real-rooted: its roots are the Frobenius eigenvalues on the circle |alpha| =
          sqrt(q), genuinely complex. There is no underlying self-adjoint operator (that is
          Hilbert-Polya, the open problem). So the interlacing engine has no fuel over Z.

Net. The non-variety sqrt(q) source in the graph world is PAID FOR with self-adjointness /
real-rootedness, which is exactly the ingredient the Ihara grader (ihara_grader.py) showed
is free in the graph world and absent over Z. R1 (the sourcing gap) and M4 (the polarization
gap) are two faces of the one missing self-adjoint operator. This deepens #130: R1 is not
merely variety-gated, it is self-adjointness-gated, and MSS is the proof that a non-variety
source exists precisely when self-adjointness is available.
"""

from __future__ import annotations

import itertools

import numpy as np

from experiments.toy.instances import POSITIVE_BATTERY


# ---------------------------------------------------------------------------
# Small bipartite d-regular test graphs (edge lists).
# ---------------------------------------------------------------------------
def k33_edges() -> tuple:
    """K_{3,3}: parts {0,1,2} and {3,4,5}, 3-regular, 9 edges."""
    return tuple((a, b) for a in (0, 1, 2) for b in (3, 4, 5)), 6


def cube_edges() -> tuple:
    """The 3-cube Q_3: 3-regular bipartite, 8 vertices, 12 edges."""
    edges = []
    for v in range(8):
        for bit in (1, 2, 4):
            w = v ^ bit
            if v < w:
                edges.append((v, w))
    return tuple(edges), 8


def signed_adjacency(edges, n, signs) -> np.ndarray:
    A = np.zeros((n, n))
    for (u, v), s in zip(edges, signs):
        A[u, v] = A[v, u] = s
    return A


def degree(edges, n) -> int:
    deg = np.zeros(n, dtype=int)
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    return int(deg[0])


# ---------------------------------------------------------------------------
# Matching polynomial (independent of the signings), by counting k-matchings.
# ---------------------------------------------------------------------------
def matching_counts(edges) -> dict:
    """m_k = number of k-matchings (sets of k pairwise-disjoint edges)."""
    edges = list(edges)

    def rec(es):
        if not es:
            return {0: 1}
        e = es[0]
        u, v = e
        rest = es[1:]
        out = dict(rec(rest))                       # e excluded
        compat = [(a, b) for (a, b) in rest if a not in e and b not in e]
        for k, c in rec(compat).items():            # e included
            out[k + 1] = out.get(k + 1, 0) + c
        return out

    return rec(edges)


def matching_polynomial(edges, n) -> np.ndarray:
    """mu(G, x) = sum_k (-1)^k m_k x^{n - 2k}, returned as numpy poly coefficients
    (highest degree first)."""
    m = matching_counts(edges)
    coeffs = np.zeros(n + 1)
    for k, mk in m.items():
        coeffs[2 * k] = ((-1) ** k) * mk            # coefficient of x^{n-2k}
    return coeffs                                    # index 0 -> x^n


def expected_char_poly(edges, n) -> np.ndarray:
    """Average of char(A_s) over all 2^{|E|} signings (highest degree first)."""
    acc = np.zeros(n + 1)
    count = 0
    for signs in itertools.product((1.0, -1.0), repeat=len(edges)):
        acc += np.poly(signed_adjacency(edges, n, signs))
        count += 1
    return acc / count


def min_max_root_over_signings(edges, n) -> float:
    """min over signings of (max eigenvalue of A_s): the best 2-lift's top new eigenvalue."""
    best = np.inf
    for signs in itertools.product((1.0, -1.0), repeat=len(edges)):
        top = float(np.max(np.abs(np.linalg.eigvalsh(signed_adjacency(edges, n, signs)))))
        best = min(best, top)
    return best


def demo_part1() -> None:
    print("Part 1  The MSS engine: a non-variety source of the 2 sqrt(q) bound")
    print("-" * 70)
    for name, (edges, n) in [("K_{3,3}", k33_edges()), ("Q_3 cube", cube_edges())]:
        d = degree(edges, n)
        bound = 2.0 * np.sqrt(d - 1)
        mu = matching_polynomial(edges, n)
        exp = expected_char_poly(edges, n)
        gg_err = float(np.max(np.abs(mu - exp)))
        roots = np.roots(mu)
        max_imag = float(np.max(np.abs(roots.imag)))
        max_real_root = float(np.max(np.abs(roots.real)))
        best = min_max_root_over_signings(edges, n)

        print(f"\n  {name}  (d = {d}, Ramanujan bound 2 sqrt(d-1) = {bound:.3f})")
        print(f"    (i)   Godsil-Gutman: |avg char(A_s) - matching poly| = {gg_err:.2e}")
        print(f"    (ii)  Heilmann-Lieb: matching poly real-rooted? max|Im root| = {max_imag:.2e}"
              f"   max|root| = {max_real_root:.3f} <= {bound:.3f}? {max_real_root <= bound + 1e-9}")
        print(f"    (iii) best signing top |eigenvalue| = {best:.3f} <= {bound:.3f}? "
              f"{best <= bound + 1e-9}   (a Ramanujan 2-lift, sourced with NO variety)")
    print("\n  The 2 sqrt(q) bound is produced combinatorially. The engine is real-rootedness")
    print("  (Heilmann-Lieb), which holds because the signed adjacency A_s is SYMMETRIC.")


def demo_part2() -> None:
    print("\nPart 2  Why it does not transfer to Spec(Z): the L-polynomial is not real-rooted")
    print("-" * 70)
    print("  Arithmetic curve L-polynomials (char poly of Frobenius on H^1). Their roots are")
    print("  the Frobenius eigenvalues on the circle |u| = 1 (RH), genuinely COMPLEX:\n")
    for inst in POSITIVE_BATTERY:
        us = np.array(inst.eigenvalues_u, dtype=complex)
        max_imag = float(np.max(np.abs(us.imag)))
        print(f"    {inst.name:46}  max|Im root| = {max_imag:.3f}  (0 would be real-rooted)")
    print("\n  Every arithmetic instance has max|Im root| of order 1: the roots sit on the")
    print("  circle, not the real line. Heilmann-Lieb and the interlacing family both need")
    print("  real-rooted polynomials, so the MSS engine has no fuel here. Real-rootedness")
    print("  would require a self-adjoint operator behind Frobenius, which is Hilbert-Polya:")
    print("  the open problem. The non-variety source exists exactly where self-adjointness")
    print("  is free (the graph world) and fails exactly where it is missing (over Z).")


def demo() -> None:
    print("Interlacing families as a non-variety sqrt(q) source, and the transfer fault line\n")
    demo_part1()
    demo_part2()
    print("\n" + "=" * 70)
    print("Verdict: MSS crosses the R1 sourcing gap in the graph world by PAYING with")
    print("self-adjointness / real-rootedness. Spec(Z)'s Frobenius is not self-adjoint and")
    print("its L-polynomial is not real-rooted, so the engine cannot run. R1 (sourcing) and")
    print("M4 (polarization) are two faces of the one missing self-adjoint operator; #130 is")
    print("sharpened from 'variety-gated' to 'self-adjointness-gated'. A coordinate, not a")
    print("new route: the combinatorial method that beats R1 for graphs needs precisely the")
    print("ingredient zeta lacks.")


if __name__ == "__main__":
    demo()
