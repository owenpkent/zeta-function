"""The Ihara / graph proven world: a genuine Selberg-analogue where RH is a theorem.

This upgrades the abstract random-matrix spectral toy (selberg.py) into a real,
finite, fully computable dynamical zeta whose RH-analogue is a theorem. It is the
SECOND proven template alongside the function-field moment world (instances.py):
where that one is geometric (Rosati / Hodge index on a curve), this one is spectral
(self-adjointness plus a spectral gap).

The object. For a finite connected (q+1)-regular graph G with adjacency matrix A, the
Ihara zeta function is a product over the PRIMITIVE closed geodesics (primitive cycles)
of G:

    Z_G(u) = prod over primitive cycles C of  (1 - u^{length(C)})^{-1}.

The primitive cycles are LITERALLY the periodic orbits, and their lengths play the role
of log p: this is the "primes as periodic orbits" picture made finite and exact. The
Ihara-Bass determinant formula collapses the product to linear algebra on A:

    Z_G(u)^{-1} = (1 - u^2)^{r-1} det(I - A u + q u^2),     q = degree - 1,

so the poles of Z_G are governed by the adjacency spectrum. For each eigenvalue lambda,
the local factor 1 - lambda u + q u^2 = 0 gives u = (lambda +- sqrt(lambda^2 - 4q))/(2q),
a pair with product 1/q. When lambda^2 <= 4q the two poles are complex conjugates with
|u| = 1/sqrt(q); when lambda^2 > 4q they are real and split OFF the circle |u| = 1/sqrt(q).

The substitution u = q^{-s} maps |u| = 1/sqrt(q) to Re(s) = 1/2, so:

    graph RH  (all nontrivial poles on |u| = 1/sqrt(q))
      <=>  Ramanujan  (all nontrivial |lambda| <= 2 sqrt(q))
      <=>  the Weil bound |alpha| = sqrt(q) in the graph world.

This is a THEOREM (Ihara, Bass; the Ramanujan equivalence is standard, Terras, "Zeta
Functions of Graphs"). Self-adjointness of A (real spectrum) is FREE and gives the
imaginary axis for free; the load-bearing content is the spectral GAP, exactly the
2 sqrt(q) bound, exactly the polarization the project calls M4.

The native Davenport-Heilbronn. A non-Ramanujan (q+1)-regular graph has the SAME Ihara
functional equation yet some poles OFF |u| = 1/sqrt(q): a genuine off-line "zero" with
the functional equation intact. So the graph world carries its OWN wrong-approach
detector, native rather than imported (compare experiments/_shared/davenport_heilbronn.py).
The two_clique_bridge graphs below are guaranteed non-Ramanujan.

Reference: Terras, "Zeta Functions of Graphs: A Stroll through the Garden" (2011).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


# ---------------------------------------------------------------------------
# Graph builders (each returns an integer adjacency matrix, symmetric).
# ---------------------------------------------------------------------------
def complete_graph(n: int) -> np.ndarray:
    """K_n: (n-1)-regular. Only nontrivial adjacency eigenvalue is -1, so trivially
    Ramanujan (RH-analogue holds)."""
    A = np.ones((n, n), dtype=int) - np.eye(n, dtype=int)
    return A


def cycle_graph(n: int) -> np.ndarray:
    """C_n: 2-regular (q=1). Nontrivial eigenvalues 2 cos(2 pi k / n) all have |.| <= 2 =
    2 sqrt(1), so every cycle is Ramanujan."""
    A = np.zeros((n, n), dtype=int)
    for i in range(n):
        A[i, (i + 1) % n] = 1
        A[(i + 1) % n, i] = 1
    return A


def petersen_graph() -> np.ndarray:
    """The Petersen graph: 3-regular (q=2) on 10 vertices, spectrum {3, 1^5, (-2)^4}.
    Max nontrivial |lambda| = 2 <= 2 sqrt(2) = 2.828, so it is Ramanujan (RH holds) with a
    genuine gap (not the trivial K_n case)."""
    # outer 5-cycle 0..4, inner pentagram 5..9, spokes i <-> i+5.
    A = np.zeros((10, 10), dtype=int)
    for i in range(5):
        A[i, (i + 1) % 5] = A[(i + 1) % 5, i] = 1          # outer cycle
        A[5 + i, 5 + (i + 2) % 5] = A[5 + (i + 2) % 5, 5 + i] = 1  # inner pentagram
        A[i, 5 + i] = A[5 + i, i] = 1                       # spokes
    return A


def two_clique_bridge(d: int) -> np.ndarray:
    """Two copies of K_{d+1} joined by a regularity-preserving 2-swap. d-regular (q = d-1),
    connected, non-bipartite. Two barely-coupled communities are a poor expander, so the
    second eigenvalue stays near d. It exceeds the Ramanujan bound 2 sqrt(d-1) once the
    cliques are large enough that the 2-edge cut is a small fraction of the volume: this is
    non-Ramanujan for d >= 5 (for d = 3, 4 the fixed 2-edge cut is still a large relative
    coupling and the graph stays Ramanujan, verified numerically). For d >= 5 it is the
    native Davenport-Heilbronn of the graph world: the Ihara functional equation intact,
    poles off |u| = 1/sqrt(q)."""
    m = d + 1
    A = np.zeros((2 * m, 2 * m), dtype=int)
    # two disjoint complete graphs K_{d+1}
    for i in range(m):
        for j in range(m):
            if i != j:
                A[i, j] = 1
                A[m + i, m + j] = 1
    # remove edge (0,1) in copy A and (0,1) in copy B; add bridges (0, m+0) and (1, m+1)
    A[0, 1] = A[1, 0] = 0
    A[m, m + 1] = A[m + 1, m] = 0
    A[0, m] = A[m, 0] = 1
    A[1, m + 1] = A[m + 1, 1] = 1
    return A


def cycle_power(n: int, k: int) -> np.ndarray:
    """The k-th power of the n-cycle: vertex i joined to i +- 1, ..., i +- k (mod n).
    2k-regular (q = 2k - 1), connected, non-bipartite for n odd or k >= 2. For k >= 3 and n
    large the clustered connection set pushes the second eigenvalue toward 2k = degree, well
    above the Ramanujan bound 2 sqrt(2k-1), so it is non-Ramanujan: a second, structurally
    different native Davenport-Heilbronn (a poor expander by local clustering rather than by
    a community cut)."""
    A = np.zeros((n, n), dtype=int)
    for i in range(n):
        for s in range(1, k + 1):
            j = (i + s) % n
            A[i, j] = A[j, i] = 1
    return A


# ---------------------------------------------------------------------------
# The Ihara-Bass spectral analysis.
# ---------------------------------------------------------------------------
@dataclass
class GraphVerdict:
    q: int
    degree: int
    ramanujan_bound: float          # 2 sqrt(q)
    max_nontrivial_abs_lambda: float
    is_ramanujan: bool
    on_line: bool                   # all nontrivial poles on |u| = 1/sqrt(q)
    max_offline_defect: float       # max over nontrivial poles of | |u| - 1/sqrt(q) |
    nontrivial_eigs: np.ndarray


def _degree_and_q(A: np.ndarray) -> tuple:
    degs = A.sum(axis=1)
    d = int(round(float(degs[0])))
    if not np.allclose(degs, d):
        raise ValueError("Ihara world needs a regular graph; got non-constant degrees.")
    return d, d - 1


def ihara_poles(lam: float, q: int) -> tuple:
    """The two Ihara poles from an adjacency eigenvalue lambda: roots of q u^2 - lambda u + 1.
    Their product is 1/q, so complex-conjugate roots sit on |u| = 1/sqrt(q)."""
    disc = complex(lam * lam - 4 * q) ** 0.5
    return ((lam + disc) / (2 * q), (lam - disc) / (2 * q))


def graph_rh_verdict(A: np.ndarray, tol: float = 1e-9) -> GraphVerdict:
    """Compute the graph-RH verdict and confirm the equivalence Ramanujan <=> on-line."""
    d, q = _degree_and_q(A)
    eigs = np.linalg.eigvalsh(A.astype(float))     # A symmetric => real spectrum (free)
    # trivial eigenvalues: +d (Perron) and -d (only if bipartite).
    trivial = (np.abs(eigs - d) < 1e-6) | (np.abs(eigs + d) < 1e-6)
    nontrivial = eigs[~trivial]

    bound = 2.0 * np.sqrt(q)
    max_abs = float(np.max(np.abs(nontrivial))) if nontrivial.size else 0.0
    is_ram = max_abs <= bound + 1e-9

    inv_sqrt_q = 1.0 / np.sqrt(q)
    defect = 0.0
    for lam in nontrivial:
        for u in ihara_poles(float(lam), q):
            defect = max(defect, abs(abs(u) - inv_sqrt_q))
    on_line = defect <= 1e-9

    return GraphVerdict(
        q=q, degree=d, ramanujan_bound=bound, max_nontrivial_abs_lambda=max_abs,
        is_ramanujan=is_ram, on_line=on_line, max_offline_defect=defect,
        nontrivial_eigs=nontrivial,
    )


def closed_walk_counts(A: np.ndarray, K: int) -> np.ndarray:
    """N_k = trace(A^k) = sum of lambda^k, k = 0..K. The graph "point counts": the number
    of closed walks of length k. K1-clean data (a candidate may use these, never the
    spectrum itself), the exact analogue of the function-field point-count moments."""
    n = A.shape[0]
    P = np.eye(n)
    out = []
    Af = A.astype(float)
    for _ in range(K + 1):
        out.append(float(np.trace(P)))
        P = P @ Af
    return np.array(out)


def is_bipartite_regular(A: np.ndarray) -> bool:
    """A regular graph is bipartite iff -degree is an eigenvalue."""
    d, _ = _degree_and_q(A)
    eigs = np.linalg.eigvalsh(A.astype(float))
    return bool(np.any(np.abs(eigs + d) < 1e-6))


def demo() -> None:
    print("Ihara / graph proven world: graph-RH <=> Ramanujan <=> |lambda| <= 2 sqrt(q)\n")
    cases = [
        ("K_6 (complete, trivially Ramanujan)", complete_graph(6)),
        ("C_9 (cycle, Ramanujan)", cycle_graph(9)),
        ("Petersen (Ramanujan, genuine gap)", petersen_graph()),
        ("two-clique bridge d=5 (native D-H)", two_clique_bridge(5)),
        ("two-clique bridge d=7 (native D-H)", two_clique_bridge(7)),
        ("cycle power C_30^3 (native D-H)", cycle_power(30, 3)),
    ]
    for name, A in cases:
        v = graph_rh_verdict(A)
        tag = "RH HOLDS " if v.on_line else "RH FAILS "
        print(f"  {name}")
        print(f"    q={v.q}  bound 2sqrt(q)={v.ramanujan_bound:.3f}  "
              f"max|lambda_nontriv|={v.max_nontrivial_abs_lambda:.3f}  "
              f"Ramanujan={v.is_ramanujan}")
        print(f"    [{tag}] nontrivial poles on |u|=1/sqrt(q)? {v.on_line}   "
              f"max offline defect={v.max_offline_defect:.2e}")
        assert v.is_ramanujan == v.on_line, "theorem check: Ramanujan <=> on-line"
    print("\n  Theorem confirmed on every case: Ramanujan <=> all nontrivial poles on the")
    print("  line. Self-adjointness of A (real spectrum) is FREE; the spectral GAP (the")
    print("  2 sqrt(q) Weil bound) is the whole content, exactly the polarization = M4.")
    print("  The non-Ramanujan graphs are a NATIVE Davenport-Heilbronn: same functional")
    print("  equation, off-line poles.")


if __name__ == "__main__":
    demo()
