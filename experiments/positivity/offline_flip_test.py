"""The off-line-zero FLIP TEST: a reusable front-door filter for RH 'crazy ideas'.

Byproduct of the 2026-06-13 crazy-idea screener (LEARNINGS #96), which swept 7
fresh frames and found all 7 converge on the same gap. The single cheap probe that
would have killed every one of them in one evaluation, now packaged as a tool.

THE FILTER. The project's four-level framing says RH lives at LEVEL 4 (a property
RH-EQUIVALENT, i.e. one that flips exactly when a single zero leaves the critical
line), not LEVEL 3 (a statistical / robust property compatible with one off-line
zero). This module operationalizes that distinction as a one-call test:

    given a candidate functional Q of the zero configuration, move ONE zero off the
    line (beta: 1/2 -> 1/2 + delta, height gamma UNCHANGED) and check whether
    sign(Q) FLIPS.

WHY IT IS DECISIVE. Write each zero rho = beta + i*gamma. RH is a statement about
the REAL parts beta (all = 1/2); the heights gamma are what every spacing /
diffraction / pair-correlation / GUE statistic sees. Moving a zero off the line
changes beta but NOT gamma. Therefore:

  - ANY functional of the heights {gamma} alone (diffraction power, pair
    correlation, spectral gap, level density) is EXACTLY invariant under the move.
    It is Level 3 BY CONSTRUCTION and cannot detect RH. sign(Q) never flips.
  - A functional that sees the real parts beta (the Weil quadratic form, Li
    coefficients) CAN flip: on-line it is PSD (>=0), one off-line zero drives a
    negative eigenvalue. Level 4.

So the flip test sorts candidate detectors into "blind to the line" (no flip) vs
"RH-sensitive" (flip), locally and cheaply, before any deep dive.

USAGE:
    from experiments.positivity.offline_flip_test import flip_test, perturb_offline
    flip_test(my_Q, zeros_online, delta=0.05)
where my_Q(zeros) -> float and zeros is a list of upper-half-plane mp.mpc zeros.

Outputs (run as a module): a demonstration table contrasting a LEVEL-4 functional
(Weil-Gram min eigenvalue, FLIPS) with two LEVEL-3 functionals (diffraction power
at log 2, and pair-correlation variance, NO FLIP).
"""

from __future__ import annotations

import argparse
from pathlib import Path

import mpmath as mp
import numpy as np

from experiments._shared import zeta_L
from experiments.positivity.e3c_weil_form import phi_b


# --------------------------------------------------------------------------- #
# The perturbation: move one zero off the critical line (beta only, gamma kept).
# --------------------------------------------------------------------------- #
def perturb_offline(zeros, idx: int = 0, delta: float = 0.05):
    """Return a copy of `zeros` with the idx-th zero moved off the line:
    beta = 1/2 -> 1/2 + delta, height gamma unchanged. This is the minimal probe
    of detector sensitivity to the LINE (it deliberately ignores the
    functional-equation mirror; we are testing what Q can SEE, not building a
    valid L-function)."""
    out = list(zeros)
    z = mp.mpc(out[idx])
    out[idx] = mp.mpc(mp.re(z) + mp.mpf(delta), mp.im(z))
    return out


# --------------------------------------------------------------------------- #
# Candidate functionals Q(zeros) -> float.
# --------------------------------------------------------------------------- #
def Q_weil_min_eig(zeros, b_vals=None, prec: int = 30) -> float:
    """LEVEL 4: smallest eigenvalue of the Weil-form Gram
    M_jk = sum_rho 2 Re(Phi_{b_j}(rho) Phi_{b_k}(rho)).
    On-line (beta=1/2): Phi is real, M is a Gram of real vectors => PSD => min eig >= 0.
    Off-line: Phi is complex, M is the real part of a BILINEAR form => can go
    indefinite => min eig < 0. SEES beta."""
    if b_vals is None:
        b_vals = np.logspace(np.log10(1.1), np.log10(200.0), 6)
    mp.mp.dps = prec
    K = len(b_vals)
    phi = np.empty((K, len(zeros)), dtype=complex)
    for k, b in enumerate(b_vals):
        bm = mp.mpf(b)
        for r, rho in enumerate(zeros):
            phi[k, r] = complex(phi_b(bm, mp.mpc(rho), prec=prec))
    M = np.zeros((K, K))
    for j in range(K):
        for k in range(K):
            M[j, k] = 2.0 * float(np.real(np.sum(phi[j] * phi[k])))
    M = 0.5 * (M + M.T)
    return float(np.linalg.eigvalsh(M).min())


def Q_diffraction_power(zeros, u: float = None) -> float:
    """LEVEL 3: diffraction power |sum_gamma exp(i u gamma)|^2 of the HEIGHTS at a
    prime frequency u = log 2 (Dyson-quasicrystal Bragg-peak quantity). A squared
    modulus => manifestly >= 0, and a function of {gamma} ALONE => exactly
    invariant under the off-line move. Cannot see beta."""
    if u is None:
        u = float(mp.log(2))
    gammas = np.array([float(mp.im(mp.mpc(z))) for z in zeros])
    return float(abs(np.sum(np.exp(1j * u * gammas))) ** 2)


def Q_paircorr_var(zeros) -> float:
    """LEVEL 3: variance of nearest-neighbour spacings of the HEIGHTS (a GUE/
    pair-correlation-flavoured statistic). Function of {gamma} alone => invariant.
    Manifestly >= 0. Cannot see beta."""
    gammas = np.sort(np.array([float(mp.im(mp.mpc(z))) for z in zeros]))
    sp = np.diff(gammas)
    return float(np.var(sp)) if len(sp) else 0.0


# --------------------------------------------------------------------------- #
# The test.
# --------------------------------------------------------------------------- #
def _sign(x, tol=1e-12):
    return 0 if abs(x) < tol else (1 if x > 0 else -1)


def flip_test(Q, zeros_online, idx: int = 0, delta: float = 0.05, **qkw) -> dict:
    """Run the off-line-zero flip test on functional Q. Returns the on-line and
    off-line values, whether sign(Q) flips, and the LEVEL verdict."""
    q_on = Q(zeros_online, **qkw)
    q_off = Q(perturb_offline(zeros_online, idx=idx, delta=delta), **qkw)
    flips = _sign(q_on) != _sign(q_off)
    invariant = abs(q_on - q_off) < 1e-9 * max(1.0, abs(q_on))
    verdict = "LEVEL_4 (RH-sensitive: sign flips)" if flips else (
        "LEVEL_3 (blind: exactly invariant)" if invariant
        else "LEVEL_3 (blind: value moves, sign does not flip)")
    return dict(Q=getattr(Q, "__name__", str(Q)),
                q_online=q_on, q_offline=q_off,
                flips=flips, invariant=invariant, verdict=verdict)


def run(n_zeros: int = 15, delta: float = 0.3, prec: int = 30, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    mp.mp.dps = prec

    rhos = zeta_L.zeros(T_max=70.0, prec=prec)[:n_zeros]
    print(f"[flip-test] {len(rhos)} on-line zeta zeros; perturb zero #0 off the line")
    print(f"            beta: 0.5 -> {0.5 + delta} (height gamma UNCHANGED), delta={delta}\n")

    tests = [
        ("Q_weil_min_eig    (sees beta)", Q_weil_min_eig, {}),
        ("Q_diffraction_pow (heights only)", Q_diffraction_power, {}),
        ("Q_paircorr_var    (heights only)", Q_paircorr_var, {}),
    ]
    print(f"  {'functional':<34} {'Q(on-line)':>14} {'Q(off-line)':>14} {'verdict':>34}")
    print("  " + "-" * 96)
    results = []
    for label, Q, kw in tests:
        r = flip_test(Q, rhos, idx=0, delta=delta, **kw)
        results.append((label, r))
        print(f"  {label:<34} {r['q_online']:>14.6e} {r['q_offline']:>14.6e} {r['verdict']:>34}")
    print("  " + "-" * 96)

    print("\n[flip-test] Reading:")
    print("  The Weil form's min eigenvalue is >= 0 on the line and goes NEGATIVE when")
    print("  one zero leaves it: sign FLIPS => LEVEL 4 => RH-sensitive (a real detector).")
    print("  The diffraction power and pair-correlation variance depend on the heights")
    print("  {gamma} alone, which the off-line move does not touch: EXACTLY invariant")
    print("  => LEVEL 3 => blind to RH (compatible with a zero at Re=0.51).")
    print("  This is the one-call front-door screen for crazy ideas (LEARNINGS #96):")
    print("  a candidate functional that does not flip cannot, by itself, close RH.")
    print("  (Cushion note: a zero only BARELY off the line, beta~0.55 / delta~0.05,")
    print("   does NOT flip the Weil form at this scale - the on-line cushion dominates")
    print("   one mildly-off-line zero. That is the marginal-positivity wall (#3J) in")
    print("   miniature; a genuinely off-line zero, beta~0.8 like D-H, flips it cleanly.)")

    np.savez_compressed(
        out_dir / "offline_flip_test.npz",
        n_zeros=len(rhos), delta=delta,
        labels=np.array([t[0] for t in results], dtype=object),
        q_online=np.array([t[1]["q_online"] for t in results]),
        q_offline=np.array([t[1]["q_offline"] for t in results]),
        flips=np.array([t[1]["flips"] for t in results]),
    )
    print(f"\n[flip-test] Saved {out_dir / 'offline_flip_test.npz'}")
    return results


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Off-line-zero flip test (Level-4 vs Level-3 front-door filter).")
    ap.add_argument("--n-zeros", type=int, default=15)
    ap.add_argument("--delta", type=float, default=0.3)
    ap.add_argument("--prec", type=int, default=30)
    args = ap.parse_args()
    run(n_zeros=args.n_zeros, delta=args.delta, prec=args.prec)
