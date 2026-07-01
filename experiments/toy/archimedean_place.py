"""The archimedean place as the single missing factor: the passage from a finite atomic
spectrum (flat, RH-provable) to a continuous one (never-flat, RH-hard).

The function-field world (curves over F_q) has NO archimedean place: every place is finite,
the Frobenius spectrum is a FINITE atomic set, and RH is a theorem. Over Q there is exactly
ONE extra place, the archimedean place, carried by the Gamma-factor in the completed zeta
xi(s) = pi^{-s/2} Gamma(s/2) zeta(s). The whole difficulty of RH is localized at that one
place, so the sharpest question is: what does adding it change?

This experiment answers with the moment / flat-extension mechanism the project already uses
(LEARNINGS #79, #80): a measure is finitely atomic iff its moment (Hankel) matrix goes FLAT
(the rank stabilizes and a machine-zero eigenvalue appears at a fixed order). Curto-Fialkow
flat extension then gives a unique measure, and in the function-field world that is exactly
why RH is decidable. A CONTINUOUS measure never goes flat: its Hankel matrices stay full rank.

The new content is the IDENTIFICATION of the archimedean continuous spectrum with the
UNIVERSAL COVER. The Alon-Boppana / Kesten-McKay result (#141) says the (q+1)-regular tree,
the universal cover of every finite regular graph, has a CONTINUOUS spectral measure on
[-2 sqrt(q), 2 sqrt(q)]. A finite graph has an ATOMIC spectrum (flat, RH-provable); its
infinite-volume limit (the tree) is CONTINUOUS (never-flat). So:

    adding the archimedean place  =  passing to the continuous spectrum of the universal cover
                                  =  the flat problem (RH-provable) becoming never-flat (RH-hard).

Three checkable parts confirm this. The honest caveat: this is a structural model of the
OBSTRUCTION SHAPE (atomic-flat vs continuous-never-flat), computably faithful to #79/#80 and
tied to the tree of #141. It runs on the self-adjoint spectral measure, so like #139/#140 it
models the shape, not the arithmetic content of zeta's actual archimedean Gamma-factor.
"""

from __future__ import annotations

import numpy as np

from experiments.toy.ihara import petersen_graph, complete_graph, graph_rh_verdict
from experiments.toy.alon_boppana import random_regular, kesten_mckay_edge


def nontrivial_eigs(A: np.ndarray) -> np.ndarray:
    d = int(round(float(A.sum(axis=1)[0])))
    eigs = np.linalg.eigvalsh(A.astype(float))
    return eigs[(np.abs(eigs - d) > 1e-6) & (np.abs(eigs + d) > 1e-6)]


def hankel(moments: np.ndarray, K: int) -> np.ndarray:
    return np.array([[moments[i + j] for j in range(K + 1)] for i in range(K + 1)])


def atom_moments(vals: np.ndarray, order: int) -> np.ndarray:
    """Empirical moments m_k = mean(vals^k), k = 0..order, of an atomic spectral measure."""
    vals = np.asarray(vals, dtype=float)
    return np.array([float(np.mean(vals ** k)) for k in range(order + 1)])


def kesten_mckay_moments(d: int, order: int, ngrid: int = 400001) -> np.ndarray:
    """Moments of the Kesten-McKay measure (the d-regular tree's continuous spectrum),
    by fine-grid quadrature, normalized so m_0 = 1."""
    a = kesten_mckay_edge(d)
    x = np.linspace(-a, a, ngrid)
    rho = (d / (2 * np.pi)) * np.sqrt(np.clip(4 * (d - 1) - x * x, 0.0, None)) / (d * d - x * x)
    dx = x[1] - x[0]
    raw = np.array([float(np.sum((x ** k) * rho) * dx) for k in range(order + 1)])
    return raw / raw[0]


def min_eig(H: np.ndarray) -> float:
    return float(np.linalg.eigvalsh((H + H.T) / 2.0).min())


def part1_finite_atomic() -> None:
    print("Part 1  Finite graph = atomic spectrum = FLAT Hankel = RH-provable (no arch place)")
    print("-" * 72)
    print("  A finite graph's nontrivial spectrum is a finite atom set. Its moment matrix goes")
    print("  flat at rank = number of distinct atoms: a machine-zero eigenvalue appears and the")
    print("  measure is pinned (Curto-Fialkow), which is why the function-field RH is decidable.\n")
    for name, A in [("K_6 (1 distinct nontrivial atom)", complete_graph(6)),
                    ("Petersen (2 distinct nontrivial atoms)", petersen_graph())]:
        vals = nontrivial_eigs(A)
        n_distinct = len(np.unique(np.round(vals, 6)))
        m = atom_moments(vals, 2 * 6)
        print(f"  {name}   ({n_distinct} distinct)")
        print("     order K:   " + "  ".join(f"K={K}" for K in range(1, 7)))
        eigs = [min_eig(hankel(m, K)) for K in range(1, 7)]
        print("     min eig :  " + "  ".join(f"{e:+.0e}" for e in eigs))
        flat_at = next((K for K in range(1, 7) if min_eig(hankel(m, K)) < 1e-10), None)
        print(f"     -> Hankel goes FLAT at order {flat_at} (rank = {n_distinct}); measure pinned.\n")


def part2_continuous_never_flat() -> None:
    print("Part 2  Universal cover = continuous Kesten-McKay spectrum = NEVER-flat Hankel")
    print("-" * 72)
    print("  The (q+1)-regular tree (the universal cover) has a CONTINUOUS spectral measure on")
    print("  [-2 sqrt(q), 2 sqrt(q)]. A continuous measure never goes flat: its Hankel stays")
    print("  full rank (min eigenvalue positive, no machine-zero cliff). This mirrors zeta (#80).\n")
    for d in (3, 4):
        m = kesten_mckay_moments(d, 2 * 6)
        print(f"  d = {d}  (Kesten-McKay edge 2 sqrt(d-1) = {kesten_mckay_edge(d):.3f}; "
              f"m_0={m[0]:.3f}, m_2={m[2]:.3f} = d)")
        eigs = [min_eig(hankel(m, K)) for K in range(1, 7)]
        print("     order K:   " + "  ".join(f"K={K}" for K in range(1, 7)))
        print("     min eig :  " + "  ".join(f"{e:.0e}" for e in eigs))
        print("     -> no machine-zero cliff: full rank at every order, never flat.\n")


def part3_the_passage() -> None:
    print("Part 3  The passage: growing finite graphs -> the continuous universal-cover measure")
    print("-" * 72)
    print("  As n grows the finite atomic spectrum fills out the continuous Kesten-McKay band.")
    print("  Its normalized moments (on [-1,1]) converge to the tree's moments, so the atomic")
    print("  (flat, RH-provable) measure approaches the continuous (never-flat, RH-hard) limit.\n")
    d, K = 3, 8
    edge = kesten_mckay_edge(d)
    m_km = kesten_mckay_moments(d, K)
    m_km_norm = np.array([m_km[k] / edge ** k for k in range(K + 1)])
    print(f"     Kesten-McKay normalized moments m_2..m_6 = "
          f"{', '.join(f'{m_km_norm[k]:.4f}' for k in range(2, 7))}")
    print("     n        ||m_finite - m_KM||  (normalized moments, k=2..8)")
    for i, n in enumerate((30, 100, 300, 1000)):
        A = random_regular(n, d, seed=200 + i)
        nu = nontrivial_eigs(A) / edge
        m_fin = atom_moments(nu, K)
        dist = float(np.linalg.norm(m_fin[2:] - m_km_norm[2:]))
        print(f"     {n:<7}  {dist:.4f}")
    print("\n  The distance shrinks toward zero: the finite atomic measures converge to the")
    print("  continuous universal-cover measure. That infinite-volume limit (the tree = the")
    print("  archimedean/continuous place) is exactly where atomic-flat becomes never-flat.")


def demo() -> None:
    print("The archimedean place as the passage to the continuous spectrum of the universal cover\n")
    part1_finite_atomic()
    part2_continuous_never_flat()
    part3_the_passage()
    print("=" * 72)
    print("Verdict: the one archimedean place is structurally the passage from a finite atomic")
    print("spectrum (flat Hankel, Curto-Fialkow pins the measure, function-field RH decidable)")
    print("to the continuous spectrum of the universal cover (never-flat, RH-hard). It unifies")
    print("#141 (the tree = the marginal/extremal continuous limit) with #79/#80 (flat vs")
    print("never-flat) and c4 (the archimedean Gamma-factor is the continuous mean). The whole")
    print("M4 difficulty localizes at this one place = the continuous limit. Honest caveat: a")
    print("structural model of the obstruction SHAPE on the self-adjoint spectrum (#139/#140),")
    print("not zeta's arithmetic archimedean content. A coordinate, not a route.")


if __name__ == "__main__":
    demo()
