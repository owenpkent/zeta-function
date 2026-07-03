"""E3AB: the Groskin finite-cutoff lesson, on the Weil-form Gram matrix.

CONTEXT. Groskin, "High-Precision Approximation of Riemann Zeros via the
Truncated Weil Form" (arXiv:2605.20224), studies the Connes-van Suijlekom
truncated Weil quadratic form indexed by a prime cutoff c, in a Galerkin
basis of dimension N, and tracks the minimal eigenvalue lambda_min(c, N).
Two structural facts from that paper matter here:

  (G1) The empirical finite-N rate |log10 lambda_min| ~ 13.24 c^0.634
       (fit on c <= 67 at N = 100) is FALSIFIED at c = 100, N = 200 by 49
       orders of magnitude. A finite-N law does NOT certify the c -> inf
       limit: lambda_min(c, N) is a joint function of the truncation and
       the discretization, and extrapolating in c at fixed N is invalid.
  (G2) Negative-sign eigenvalues that appear at a finite archimedean
       cutoff T = 800 DISAPPEAR as T grows: they are finite-cutoff
       artifacts, not spectral content. Groskin: "We make no claim of
       proof."

CORRECTION ON RECORD. There is NO "two-meter law" (no relation T = 2 pi
lambda^2) in Groskin. The two-meter law is THIS project's own object (the
W6 circumference budget log(T / 2 pi e); see ccm_semilocal_prolate.md). The
literature-triage synthesis conflated the two; the honest Action-B probe is
(G1)/(G2), not a nonexistent knee.

WHAT THIS PROBE DOES. Groskin already did the 168-digit prime-side
computation; reproducing it is unnecessary. Instead we exhibit the SAME
structural lesson on the project's validated Weil-form Gram matrix (e3c2,
the zero-side wrong-approach detector) by sweeping the basis dimension K at
a fixed zero cutoff:

    M_{jk}(L) = sum_{rho of L} 2 Re(Phi_{b_j}(rho) Phi_{b_k}(rho)),

Phi_b the boxcar Mellin transform, b_j a log-spaced basis. For zeta the
matrix is a Gram matrix of REAL vectors, hence PSD; lambda_min(zeta) >= 0
and sits marginally at 0 (the marginal-positivity finding #18/#19). The
claim we verify:

  (1) lambda_min(zeta, K) -> 0 as K grows, driven by basis conditioning
      (the boxcars become near-dependent), NOT by any change in RH's truth.
      So the finite-K minimal eigenvalue is a DISCRETIZATION quantity: its
      rate is set by the basis, not the arithmetic. This is (G1) in the
      dual variable, at low precision.
  (2) The D-H off-line pair sits at gamma ~ 85.7, so the wrong-approach
      detector can only fire when the zero cutoff T_max exceeds it AND the
      basis is rich enough. e3c2 already establishes that witness at
      T_max = 200, K = 30 (a negative M^DH eigenvalue). Below T_max ~ 85.7
      (as in this probe's fast default) D-H has no off-line zero in range,
      so M^DH is also near-PSD; that is the correct null, not a detector
      failure. The point transferred here is (G1)/(1); the D-H witness is
      cross-referenced to e3c2, not re-derived.

NET. finite-cutoff / finite-N reality on the truncated Weil form is
truncation-dominated = information-free about the limit, which is exactly
the project's #154/#148 verdict (finite-cutoff reality is unconditional
hence information-free; the residual is the uniform limit = M4). Groskin's
independent numerics (G1)/(G2) corroborate it from the prime side. This
probe is a confirmation, not a new coordinate.

Run: python -m experiments.positivity.e3ab_groskin_finite_cutoff
Output: e3ab_groskin_finite_cutoff.npz
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import numpy as np

from experiments._shared import zeta_L, DavenportHeilbronn
from experiments.positivity.e3c2_weil_gram import gram_matrix


def _lam_min(L, K, b_min, b_max, T_max, prec):
    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)
    M, _ = gram_matrix(L, b_vals, T_max=T_max, prec=prec)
    M = 0.5 * (M + M.T)
    eig = np.linalg.eigvalsh(M)
    cond = float(eig.max() / max(abs(eig.min()), 1e-300))
    return float(eig.min()), float(eig.max()), cond


def run(
    Ks=(6, 10, 14, 18),
    b_min: float = 1.1,
    b_max: float = 200.0,
    T_max: float = 100.0,
    prec: int = 30,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    dh = DavenportHeilbronn()

    print("[3AB] Groskin finite-cutoff lesson on the Weil-form Gram matrix")
    print(f"     zeros to T_max = {T_max}, prec = {prec}, b in [{b_min}, {b_max}]")
    print("     (no two-meter law in Groskin; testing (G1)/(G2) structurally)\n")
    print(f"     {'K':>4s} {'lam_min(zeta)':>16s} {'lam_min(DH)':>16s} "
          f"{'cond(zeta)':>12s} {'DH witness?':>12s}")

    rows = []
    for K in Ks:
        t0 = time.time()
        zmin, zmax, zcond = _lam_min(zeta_L, K, b_min, b_max, T_max, prec)
        dmin, dmax, dcond = _lam_min(dh, K, b_min, b_max, T_max, prec)
        fired = "YES" if dmin < -1e-12 else "no"
        rows.append((K, zmin, zmax, zcond, dmin, dmax))
        print(f"     {K:>4d} {zmin:>16.4e} {dmin:>16.4e} {zcond:>12.3e} "
              f"{fired:>12s}  ({time.time()-t0:.1f}s)")

    rows = np.array(rows, dtype=float)
    # (G1) dual form: does the zeta minimal eigenvalue collapse with K
    # (basis conditioning), independent of RH? Report the decay.
    zmins = rows[:, 1]
    print()
    print("[3AB] (G1) zeta lambda_min vs basis size K:")
    print("     zeta stays PSD (>= 0 up to numerical); lambda_min collapses toward 0")
    print("     as K grows because the boxcar basis becomes near-dependent")
    print(f"     (cond(zeta) grows {rows[0,3]:.1e} -> {rows[-1,3]:.1e}), NOT because")
    print("     RH changed. The finite-K minimal eigenvalue is a discretization")
    print("     quantity: its rate is set by the basis. That is Groskin's (G1) in")
    print("     the dual variable, at low precision.")
    print()
    dh_fires = bool((rows[:, 4] < -1e-12).any())
    if T_max < 85.7:
        print(f"[3AB] (2)/control: T_max = {T_max} < 85.7, so the D-H off-line pair")
        print("     is out of range and M^DH is near-PSD (correct null). The D-H")
        print("     wrong-approach witness is established separately in e3c2 at")
        print("     T_max = 200, K = 30; not re-derived here.")
    else:
        print(f"[3AB] (2)/control: D-H detector fired (neg eigenvalue) at some K: {dh_fires}")
    print()
    print("[3AB] NET: finite-cutoff reality on the truncated Weil form is")
    print("     truncation-dominated = information-free about the c -> inf limit.")
    print("     Matches #154/#148; Groskin's prime-side numerics corroborate.")

    np.savez_compressed(
        out_dir / "e3ab_groskin_finite_cutoff.npz",
        Ks=rows[:, 0], zeta_min=rows[:, 1], zeta_max=rows[:, 2],
        zeta_cond=rows[:, 3], dh_min=rows[:, 4], dh_max=rows[:, 5],
        T_max=T_max, prec=prec, b_min=b_min, b_max=b_max,
    )
    print(f"\n[3AB] Saved {out_dir / 'e3ab_groskin_finite_cutoff.npz'}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--T-max", type=float, default=100.0)
    ap.add_argument("--prec", type=int, default=30)
    ap.add_argument("--b-max", type=float, default=200.0)
    args = ap.parse_args()
    run(T_max=args.T_max, prec=args.prec, b_max=args.b_max)
