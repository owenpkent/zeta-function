"""The spectral grader: score a candidate against the Ihara / graph proven world.

This is the Architecture-1 (spectral) counterpart of grader.py. Where that grader tests
a candidate polarization against function-field curves (RH <=> Weil / Hodge index), this
one tests a candidate against finite regular graphs (graph-RH <=> Ramanujan <=> the poles
of the Ihara zeta lie on |u| = 1/sqrt(q)). Both are worlds where the RH-analogue is a
THEOREM, so a proposed move is graded right or wrong on contact.

A CANDIDATE is a function

    candidate(data: GraphData) -> numpy.ndarray | None

that, from the K1-clean data alone (q, degree, the closed-walk counts N_0..N_K, and the
public structural flags), builds a real symmetric matrix it claims is PSD <=> graph-RH.

The K1-clean data is the graph analogue of point counts. N_k = trace(A^k) is the number
of closed walks of length k; a candidate may use these and the PUBLIC facts (the degree d,
hence the Perron eigenvalue d, and whether the graph is bipartite, hence whether -d is an
eigenvalue). It may NOT use the adjacency spectrum or the eigenvalue moduli: that is the
answer key, exactly as |u| is hidden in the function-field grader.

The four scores mirror grader.py, with the D-H axis specialized to this world:

  reproduces_ramanujan  : M is PSD on every Ramanujan (RH-true) graph.
  rejects_nonramanujan  : M is indefinite on every non-Ramanujan graph. In this world the
                          non-Ramanujan regular graphs (two_clique_bridge, cycle_power) ARE
                          the native Davenport-Heilbronn: same Ihara functional equation,
                          off-line poles. So this axis IS the D-H discipline, native.
  k1_clean              : structural. The candidate only ever saw closed-walk counts and
                          public structure, never the spectrum, so it cannot read the answer.
  gap_is_the_content    : structural. Self-adjointness of A (real spectrum) is FREE here, so
                          the Hamburger/real-spectrum half of any honest form is unconditional;
                          the discriminating half is the localizing form for the 2 sqrt(q) gap.
                          A candidate that certifies only self-adjointness passes reproduce and
                          FAILS reject. This is the exact lesson for zeta: the operator (real
                          ordinates) is not the hard part, the polarization (the gap) is = M4.

The REFERENCE candidate (`moment_localizing_candidate`) is the [-1,1] moment form. Writing
the normalized nontrivial spectrum as nu = lambda / (2 sqrt(q)), Ramanujan means every
nu in [-1,1]. By the Hausdorff moment theorem on [-1,1] this holds iff BOTH
  H0 = [m_{i+j}]                    (Hamburger: the m are moments of a real measure)  and
  H1 = [m_{i+j} - m_{i+j+2}]        (localizing on 1 - nu^2 >= 0: support inside [-1,1])
are PSD, where m_k = sum nu_i^k. H0 is always PSD (A is symmetric), so H1 carries all the
RH content. It scores all green; it is the known-correct spectral M4 move in this world.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional

import numpy as np

from experiments.toy.ihara import (
    closed_walk_counts,
    graph_rh_verdict,
    is_bipartite_regular,
    complete_graph,
    cycle_graph,
    petersen_graph,
    two_clique_bridge,
    cycle_power,
)

PSD_TOL = 1e-9


@dataclass(frozen=True)
class GraphData:
    """The candidate's K1-clean view of a graph. Excludes the adjacency spectrum and the
    eigenvalue moduli; carries only closed-walk counts and public structure."""
    q: int
    degree: int
    walk_counts: tuple      # (N_0, ..., N_K)
    bipartite: bool
    n_vertices: int

    def nontrivial_moments(self) -> np.ndarray:
        """m_k = (N_k - d^k - [bipartite] (-d)^k) / (2 sqrt(q))^k, the normalized moments of
        the NONtrivial spectrum. Uses only public data (d is the Perron eigenvalue of a
        connected d-regular graph; -d is an eigenvalue iff bipartite), so it is K1-clean."""
        d = self.degree
        N = np.asarray(self.walk_counts, dtype=float)
        K = len(N) - 1
        scale = 2.0 * np.sqrt(self.q)
        m = np.empty(K + 1)
        for k in range(K + 1):
            trivial = d ** k + ((-d) ** k if self.bipartite else 0.0)
            m[k] = (N[k] - trivial) / (scale ** k)
        return m


@dataclass(frozen=True)
class GraphInstance:
    name: str
    adjacency: np.ndarray
    kind: str = "graph"     # 'graph' (all instances here are buildable and self-adjoint)

    @property
    def rh_true(self) -> bool:
        return graph_rh_verdict(self.adjacency).is_ramanujan

    def to_data(self, K: int) -> GraphData:
        A = self.adjacency
        v = graph_rh_verdict(A)
        return GraphData(
            q=v.q,
            degree=v.degree,
            walk_counts=tuple(closed_walk_counts(A, K)),
            bipartite=is_bipartite_regular(A),
            n_vertices=A.shape[0],
        )


# ---------------------------------------------------------------------------
# The battery.
# ---------------------------------------------------------------------------
POSITIVE_GRAPHS = [
    GraphInstance("K_6 (complete, Ramanujan)", complete_graph(6)),
    GraphInstance("C_9 (cycle, Ramanujan)", cycle_graph(9)),
    GraphInstance("Petersen (Ramanujan, genuine gap)", petersen_graph()),
]

# The native Davenport-Heilbronn: non-Ramanujan regular graphs (functional equation
# intact, poles off |u| = 1/sqrt(q)).
NEGATIVE_GRAPHS = [
    GraphInstance("two-clique bridge d=5 (native D-H)", two_clique_bridge(5)),
    GraphInstance("two-clique bridge d=7 (native D-H)", two_clique_bridge(7)),
    GraphInstance("cycle power C_30^3 (native D-H)", cycle_power(30, 3)),
]

FULL_GRAPH_BATTERY = POSITIVE_GRAPHS + NEGATIVE_GRAPHS


def is_psd(M: Optional[np.ndarray], tol: float = PSD_TOL) -> bool:
    if M is None:
        return False
    w = np.linalg.eigvalsh((M + M.T) / 2.0)
    return float(w.min()) >= -tol


def min_eig(M: Optional[np.ndarray]) -> float:
    if M is None:
        return float("nan")
    return float(np.linalg.eigvalsh((M + M.T) / 2.0).min())


# ---------------------------------------------------------------------------
# Candidates.
# ---------------------------------------------------------------------------
def _hankel(m: np.ndarray, size: int, shift: int = 0) -> np.ndarray:
    return np.array([[m[i + j + shift] for j in range(size)] for i in range(size)], dtype=float)


def moment_localizing_candidate(data: GraphData) -> Optional[np.ndarray]:
    """The reference: block_diag(H0, H1) with H0 = [m_{i+j}] (Hamburger, real spectrum) and
    H1 = [m_{i+j} - m_{i+j+2}] (localizing on [-1,1]). PSD <=> every normalized nontrivial
    eigenvalue in [-1,1] <=> Ramanujan <=> graph-RH."""
    m = data.nontrivial_moments()
    K = len(m) - 1
    if K < 6:
        return None
    H0 = _hankel(m, 4)                          # uses m_0..m_6
    H1 = _hankel(m, 3) - _hankel(m, 3, shift=2)  # uses m_0..m_6
    out = np.zeros((7, 7))
    out[:4, :4] = H0
    out[4:, 4:] = H1
    return out


def hamburger_only_candidate(data: GraphData) -> Optional[np.ndarray]:
    """Certifies ONLY self-adjointness (real spectrum): returns just the Hamburger H0, which
    is PSD for every graph because A is symmetric. Passes reproduce, FAILS reject. The lesson:
    the operator / real ordinates are free; the spectral gap is the content (= M4 for zeta)."""
    m = data.nontrivial_moments()
    if len(m) - 1 < 6:
        return None
    return _hankel(m, 4)


def identity_candidate(data: GraphData) -> Optional[np.ndarray]:
    """A soft positivity with no RH content: always PSD. Fails reject."""
    return np.eye(4)


# ---------------------------------------------------------------------------
# The scorecard.
# ---------------------------------------------------------------------------
@dataclass
class GraphResult:
    name: str
    rh_true: bool
    psd: Optional[bool]
    min_eig: float
    correct: bool


@dataclass
class GraphScorecard:
    candidate_name: str
    K: int
    results: list
    reproduces_ramanujan: bool
    rejects_nonramanujan: bool
    k1_clean: bool = True
    gap_is_the_content: bool = True

    @property
    def all_green(self) -> bool:
        return self.reproduces_ramanujan and self.rejects_nonramanujan and self.k1_clean

    def report(self) -> str:
        lines = [f"  candidate: {self.candidate_name}   (K = {self.K} walk-counts exposed)"]
        for r in self.results:
            verdict = (f"{'PSD  ' if r.psd else 'INDEF'}  min_eig={r.min_eig:+.3e}"
                       if r.psd is not None else "unbuildable")
            tag = "Ramanujan " if r.rh_true else "non-Raman."
            mark = "OK " if r.correct else "BAD"
            lines.append(f"    [{mark}] {tag}  {r.name:38}  {verdict}")
        lines.append(
            f"  => reproduces_ramanujan={self.reproduces_ramanujan}  "
            f"rejects_nonramanujan={self.rejects_nonramanujan}  k1_clean={self.k1_clean}  "
            f"{'<<< ALL GREEN' if self.all_green else '<<< FAILS'}"
        )
        return "\n".join(lines)


def grade(candidate: Callable[[GraphData], Optional[np.ndarray]],
          name: str = "candidate", battery: Optional[list] = None, K: int = 6) -> GraphScorecard:
    if battery is None:
        battery = FULL_GRAPH_BATTERY
    results = []
    reproduces = True
    rejects = True
    for inst in battery:
        data = inst.to_data(K)
        try:
            M = candidate(data)
        except Exception:
            M = None
        if M is None:
            correct = False
            if inst.rh_true:
                reproduces = False
            else:
                rejects = False
            results.append(GraphResult(inst.name, inst.rh_true, None, float("nan"), correct))
            continue
        psd = is_psd(M)
        correct = (psd == inst.rh_true)
        if inst.rh_true and not psd:
            reproduces = False
        if (not inst.rh_true) and psd:
            rejects = False
        results.append(GraphResult(inst.name, inst.rh_true, psd, min_eig(M), correct))
    return GraphScorecard(name, K, results, reproduces, rejects)


def demo() -> None:
    print("Spectral grader (Ihara / graph world): grade a candidate against graph-RH\n")
    print(grade(moment_localizing_candidate, "moment localizing [-1,1] form (reference)").report())
    print()
    print(grade(hamburger_only_candidate, "Hamburger only (self-adjointness certificate)").report())
    print()
    print(grade(identity_candidate, "identity (soft positivity)").report())
    print("\n  The reference is all green: a SECOND proven-world M4 move (spectral, alongside")
    print("  the function-field geometric one). The Hamburger-only candidate reproduces but")
    print("  fails to reject: real spectrum (self-adjointness) is free, so it certifies the")
    print("  native Davenport-Heilbronn too. The localizing block (the 2 sqrt(q) gap) is the")
    print("  content, and it is exactly the polarization that is open for zeta = M4.")


if __name__ == "__main__":
    demo()
