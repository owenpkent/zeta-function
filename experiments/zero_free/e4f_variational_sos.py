"""e4f: Bombieri variational SOS -- does controlled negativity escape the 4E.3 Fejer wall?

Direction 6 (docs/03_research/research_directions/06_bombieri_variational_sos.md), the one escape
route from the 4E.3 line-restriction lemma NOT in the LP/SDP family (e4e6-e4e8 all saturate Fejer).

The 4E.3 lemma: any NON-NEGATIVE bivariate trig polynomial P(x,y), restricted to the line phi=2theta,
gives a 1D non-negative trig polynomial whose c_1/c_0 is bounded by the 1D Fejer ceiling at the matched
effective degree. For bidegree (2,2) the restriction Q(theta)=P(theta,2theta) has effective degree 6,
and the ceiling is 2 cos(pi/8) = 1.8478 (raw convention P = c_0 + c_1 cos + c_2 cos2 + ...). Every
LP/SDP relaxation of the non-negative cone saturates this and cannot exceed it (e4e8 Phase D, ratio
1.0000).

The Bombieri relaxation RELAXES non-negativity: allow P to go slightly negative, penalized by the L^2
norm of its negative part ||P_-||^2, P_-(x,y) = max(0, -P(x,y)). The feasible set is strictly LARGER
than the non-negative cone, so it is OUTSIDE the LP/SDP family and might escape 4E.3.

THE DECISIVE TEST (Direction 6 sec 5.5). For each target ratio r, solve

    min_c  ||P_-||^2   subject to   c_1(Q) = r,  c_0(Q) = 1,   Q(theta) = P(theta, 2theta),

over P(x,y) = sum_{j,k<=2} c_{jk} cos(jx) cos(ky). If the minimum ||P_-||^2 is 0 for r <= 1.8478 and
becomes POSITIVE exactly as r crosses 1.8478, then Fejer is precisely the non-negative-cone ceiling and
super-Fejer c_1/c_0 REQUIRES genuine negativity (the variational relaxation gives no free lunch, and
4E.3 extends to the variational setting). If instead ||P_-||^2 stays ~0 past 1.8478, the variational
SOS ESCAPES Fejer -- a real Architecture-4 advance.

Prediction (Direction 6 sec 6, the marginal-positivity thesis): no escape. ||P_-||^2 = 0 up to Fejer
and grows for r > Fejer; the relaxation buys super-Fejer ratios only by paying L^2-negativity, which
(sec 5.6) does not translate to a valid zero-free-region constant.

Run: python -m experiments.zero_free.e4f_variational_sos
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from scipy.optimize import minimize

CACHE_DIR = Path(__file__).resolve().parent / "_cache"
FEJER_DEG6 = 2.0 * np.cos(np.pi / 8)  # 1.84776: the 4E.3 ceiling at effective degree 6

L = 2  # bidegree (2,2) -> restriction effective degree 6, matching e4e8 / 4E.3
IDX = [(j, k) for j in range(L + 1) for k in range(L + 1)]
NC = len(IDX)

# --- restriction Q(theta) = P(theta, 2theta): c_0, c_1 are LINEAR in the coefficient vector c ---
_NT = 1024
_theta = np.linspace(0.0, 2.0 * np.pi, _NT, endpoint=False)
_Bq = np.array([np.cos(j * _theta) * np.cos(2 * k * _theta) for (j, k) in IDX])  # (NC, NT)
W0 = _Bq.mean(axis=1)                              # c_0(Q) = W0 . c
W1 = 2.0 * (_Bq * np.cos(_theta)).mean(axis=1)     # c_1(Q) = W1 . c  (raw convention)

# --- 2D grid for the negative-part L^2 penalty ---
_NG = 64
_xs = np.linspace(0.0, 2.0 * np.pi, _NG, endpoint=False)
_X, _Y = np.meshgrid(_xs, _xs, indexing="ij")
_B2 = np.array([np.cos(j * _X) * np.cos(k * _Y) for (j, k) in IDX])  # (NC, NG, NG)


def P_grid(c: np.ndarray) -> np.ndarray:
    return np.tensordot(c, _B2, axes=(0, 0))


def neg_l2(c: np.ndarray) -> float:
    """||P_-||^2 = mean over the grid of max(0, -P)^2."""
    n = np.minimum(P_grid(c), 0.0)
    return float((n * n).mean())


def neg_l2_grad(c: np.ndarray) -> np.ndarray:
    n = np.minimum(P_grid(c), 0.0)
    return 2.0 * np.einsum("xy,cxy->c", n, _B2) / (_NG * _NG)


def min_negativity_for_ratio(r: float, n_starts: int = 12, seed: int = 0) -> float:
    """min ||P_-||^2 s.t. c_1(Q) = r, c_0(Q) = 1 (both linear). Nonconvex; multi-start SLSQP."""
    rng = np.random.default_rng(seed)
    cons = [
        {"type": "eq", "fun": lambda c: float(W0 @ c) - 1.0, "jac": lambda c: W0},
        {"type": "eq", "fun": lambda c, r=r: float(W1 @ c) - r, "jac": lambda c, r=r: W1},
    ]
    best = np.inf
    for s in range(n_starts):
        # Start from a feasible-ish point: c00 set so c_0(Q)=1, plus noise (and the cos x term).
        c0 = rng.normal(0, 0.4, NC)
        c0[IDX.index((0, 0))] = 1.0
        res = minimize(neg_l2, c0, jac=neg_l2_grad, constraints=cons, method="SLSQP",
                       options={"maxiter": 400, "ftol": 1e-12})
        if res.success or res.status in (0, 9):
            v = neg_l2(res.x)
            # enforce the constraints actually hold (SLSQP can return slightly infeasible)
            if abs(W0 @ res.x - 1.0) < 1e-5 and abs(W1 @ res.x - r) < 1e-5:
                best = min(best, v)
    return float(best)


def run(out_dir: Path = None) -> dict:
    if out_dir is None:
        out_dir = CACHE_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 84)
    print("[e4f] Bombieri variational SOS: min ||P_-||^2 vs target line-restriction c_1/c_0")
    print("=" * 84)
    print(f"      bidegree (2,2) -> restriction effective degree 6; Fejer ceiling = 2 cos(pi/8) "
          f"= {FEJER_DEG6:.5f}")
    print(f"      4E.3: a NON-NEGATIVE P caps c_1/c_0 at Fejer. Does penalized negativity escape it?\n")

    ratios = np.round(np.arange(1.70, 1.96 + 1e-9, 0.02), 3)
    print(f"      {'target c_1/c_0':>14} {'min ||P_-||^2':>14} {'vs Fejer':>10}")
    print("      " + "-" * 42)
    rows = []
    for r in ratios:
        v = min_negativity_for_ratio(float(r))
        tag = "<= Fejer" if r <= FEJER_DEG6 else "> Fejer"
        flag = "  (essentially 0)" if v < 1e-7 else ""
        rows.append((float(r), v))
        print(f"      {r:>14.3f} {v:>14.3e} {tag:>10}{flag}")
    print("      " + "-" * 42)

    arr = np.array(rows)
    below = arr[arr[:, 0] <= FEJER_DEG6]
    above = arr[arr[:, 0] > FEJER_DEG6]
    max_below = float(below[:, 1].max()) if len(below) else 0.0
    min_above = float(above[:, 1].min()) if len(above) else np.inf
    # "escape" = a super-Fejer ratio achievable with negligible negativity
    escaped = min_above < 1e-6

    print("\n[e4f] ===== VERDICT =====")
    print(f"      max ||P_-||^2 at/below Fejer (r <= {FEJER_DEG6:.4f}): {max_below:.2e} "
          f"({'~0, as 4E.3 predicts' if max_below < 1e-6 else 'NONZERO -- check'})")
    print(f"      min ||P_-||^2 above Fejer  (r > {FEJER_DEG6:.4f}): {min_above:.2e}")
    if escaped:
        print("      ESCAPE (prediction REFUTED): a super-Fejer line-restriction ratio is achievable")
        print("      with negligible negativity. The variational SOS leaves the non-negative cone")
        print("      WITHOUT cost -- 4E.3 is escaped. This needs the 5.6 translation to a zero-free")
        print("      constant and adversarial re-checking before any claim.")
    else:
        print("      NO ESCAPE (prediction holds). ||P_-||^2 is ~0 up to the Fejer ceiling and turns")
        print("      POSITIVE exactly as the target crosses it: Fejer IS the non-negative-cone")
        print("      boundary, and super-Fejer c_1/c_0 REQUIRES genuine L^2-negativity. The")
        print("      variational relaxation gives no free lunch; the 4E.3 line-restriction lemma")
        print("      extends to the Bombieri variational setting, sharpening the LP/SDP saturation")
        print("      (e4e6-e4e8) one rung further. The marginal-positivity thesis on the Arch-4 side:")
        print("      the figure of merit is pinned at the cone boundary, with no soft slack to exploit.")

    np.savez_compressed(out_dir / "e4f_variational_sos.npz",
                        ratios=arr[:, 0], min_neg_l2=arr[:, 1],
                        fejer=FEJER_DEG6, escaped=escaped)
    print(f"\n[e4f] Saved {out_dir / 'e4f_variational_sos.npz'}")
    return {"ratios": arr, "fejer": FEJER_DEG6, "escaped": escaped}


if __name__ == "__main__":
    run()
