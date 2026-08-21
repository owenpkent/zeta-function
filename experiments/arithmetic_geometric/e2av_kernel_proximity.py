"""E2AV: B2c-prox: the kernel-groundstate proximity, measured in our hands.

The dichotomy (#189): our certified collapse of the (1.2) object coexists
with CCM's PROVEN kernel limit (arXiv:2511.22755 Lemma 7.3: the Fourier
transform of k_lambda converges to Xi interior-uniformly) only if the
kernel-groundstate proximity CCM observed at lambda <= 6 fails at larger
lambda, OR if the kernel's own approach to Xi is slow enough that both
objects are far from Xi at accessible windows. This module measures both.

THE KERNEL, from source (CCM (7.5)-(7.6)): k_lambda = E(h_lambda) on
[1/lambda, lambda], with E(f)(u) = u^{1/2} sum_{n>=1} f(nu), and h_lambda
the unique (up to scalar) combination of the prolate-wave-operator
eigenfunctions h_{0,lambda}, h_{4,lambda} with vanishing integral. Their
Lemma 7.2: h_{n,lambda} equals the Fourier-self-dual HERMITE function
psi_n up to c/lambda^2 uniformly. We build k_lambda with the Hermite limit
seed h = psi_0 - alpha psi_4 (vanishing integral), carrying CCM's own
lambda^{-2} bound as the substitution caveat (<= 2 percent at a >= 2, the
decisive range).

THE GROUND STATE: our certified solver (e2ar machinery, dps-50 on the
110-digit zero cache truncated to 50 digits; refined resolution m = 112a,
the gate-passing regime from #185/#189).

READOUTS per window a = log lambda:
  (1) THE PROXIMITY: |cos angle| between k_lambda and xi_lambda in
      L^2(-a, a) (log coordinates; scalar- and sign-free).
  (2) THE KERNEL'S OWN APPROACH: khat(z)/(c Xi(z)) ratios at z = 2..8
      (c fitted at z = 0), against the ground state's collapsed ratios.
Scenario (i): proximity falls -> (1.2)-as-stated rests on an approximation
that breaks; scenario (ii): proximity holds AND the kernel's ratios collapse
along with the ground state's -> slow-limit reconciliation ((1.2) survivable,
the turnaround beyond accessible windows, its rate calibrated by the kernel).

Run:
  python -m experiments.arithmetic_geometric.e2av_kernel_proximity

Outputs: e2av_kernel_proximity.npz (tracked).
"""

from __future__ import annotations

import json
import time
from math import pi
from pathlib import Path

import numpy as np
import mpmath as mp

from experiments.arithmetic_geometric.e2ar_hard_window_xi import (
    DEG, HardWindowGS, cardinal_spline)
from experiments.arithmetic_geometric.e2aq_xi_convergence import Xi

HERE = Path(__file__).resolve().parent
ZCACHE = HERE.parent / "_shared" / "_cache" / "zeros_dps110_T1500.json"

DPS = 80
ZPTS = [2.0, 4.0, 6.0, 8.0]

CHECKS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


# ---------------------------------------------------------------------------
# the Fourier-self-dual Hermite functions and the CCM seed
# psi_n(x) = c_n H_n(sqrt(2 pi) x) e^{-pi x^2},  FT(psi_n) = (-i)^n psi_n
# under fhat(y) = int f(x) e^{-2 pi i x y} dx. Only n = 0, 4 needed.
# ---------------------------------------------------------------------------

def psi0(x):
    return 2.0 ** 0.25 * np.exp(-pi * x * x)


def psi4(x):
    u = np.sqrt(2 * pi) * x
    H4 = 16 * u ** 4 - 48 * u ** 2 + 12
    n = 4
    c = 2.0 ** 0.25 / np.sqrt(float(2 ** n) * 24.0)
    return c * H4 * np.exp(-pi * x * x)


def seed_alpha():
    xg = np.arange(-8.0, 8.0, 1e-4)
    i0 = np.trapezoid(psi0(xg), xg)
    i4 = np.trapezoid(psi4(xg), xg)
    return i0 / i4


ALPHA = seed_alpha()


def hseed(x):
    return psi0(x) - ALPHA * psi4(x)


def k_lambda_log(a: float, xgrid: np.ndarray) -> np.ndarray:
    """k_lambda(e^x) = e^{x/2} sum_{n>=1} h(n e^x) on the log grid."""
    out = np.zeros_like(xgrid)
    for i, x in enumerate(xgrid):
        u = np.exp(x)
        nmax = int(np.ceil(2.5 / u)) + 1
        n = np.arange(1, nmax + 1)
        out[i] = np.exp(x / 2) * float(np.sum(hseed(n * u)))
    return out


# ---------------------------------------------------------------------------
# the ground state in x-space (float B-spline evaluation of the mp solve)
# ---------------------------------------------------------------------------

def spline_eval(gs: HardWindowGS, xgrid: np.ndarray) -> np.ndarray:
    h = float(gs.h)
    cen = [float(c) for c in gs.centers]
    cf = [float(gs.c[r]) for r in range(gs.J)]
    d = DEG
    from math import comb, factorial

    def M(xv):
        acc = 0.0
        for i in range(d + 2):
            u = xv + (d + 1) / 2 - i
            if u > 0:
                acc += (-1) ** i * comb(d + 1, i) * u ** d
        return acc / factorial(d)

    out = np.zeros_like(xgrid)
    for j, x in enumerate(xgrid):
        v = 0.0
        for c0, cc in zip(cen, cf):
            if abs(x - c0) < (d + 1) / 2 * h:
                v += cc * M((x - c0) / h)
            if c0 > 0 and abs(x + c0) < (d + 1) / 2 * h:
                v += cc * M((x + c0) / h)
        out[j] = v
    return out


def zeros50():
    mp.mp.dps = DPS
    return [mp.mpf(s[: DPS + 8]) for s in json.loads(ZCACHE.read_text())]


def run():
    t0 = time.time()
    print("== E2AV: the kernel-groundstate proximity (B2c-prox) ==")
    gz = zeros50()
    print(f"  {len(gz)} zeros (dps {DPS}); seed alpha = {ALPHA:.6f}")

    # seed sanity: vanishing integral and Fourier self-duality
    xg = np.arange(-8.0, 8.0, 1e-4)
    hint = float(np.trapezoid(hseed(xg), xg))
    yg = np.arange(-4.0, 4.0, 2e-3)
    ft0 = np.array([np.trapezoid(psi0(xg) * np.cos(2 * pi * xg * y), xg) for y in yg])
    ft4 = np.array([np.trapezoid(psi4(xg) * np.cos(2 * pi * xg * y), xg) for y in yg])
    sd0 = float(np.max(np.abs(ft0 - psi0(yg))))
    sd4 = float(np.max(np.abs(ft4 - psi4(yg))))

    mp.mp.dps = DPS
    Xi0 = float(Xi(0.0))
    Xi_at = {z: float(Xi(z)) for z in ZPTS}

    AVALS = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    rows = []
    for a in AVALS:
        ta = time.time()
        gs = HardWindowGS(a, gz, m_knots=int(round(112 * a)), dps=DPS)
        xgrid = np.arange(-a + 1e-6, a, min(2e-3, a / 4000))
        v = spline_eval(gs, xgrid)
        k = k_lambda_log(a, xgrid)
        cosang = float(abs(np.trapezoid(v * k, xgrid))
                       / np.sqrt(np.trapezoid(v * v, xgrid)
                                 * np.trapezoid(k * k, xgrid)))
        # the kernel's own FT ratios against Xi (c fitted at z = 0)
        kz0 = float(np.trapezoid(k, xgrid))
        ck = kz0 / Xi0
        kr = [float(np.trapezoid(k * np.cos(z * xgrid), xgrid)) / (ck * Xi_at[z])
              for z in ZPTS]
        # the ground state's ratios for side-by-side display
        gz0 = float(np.trapezoid(v, xgrid))
        cv = gz0 / Xi0
        vr = [float(np.trapezoid(v * np.cos(z * xgrid), xgrid)) / (cv * Xi_at[z])
              for z in ZPTS]
        rows.append({"a": a, "cos": cosang, "kr": kr, "vr": vr,
                     "lam2": float(np.exp(-2 * a))})
        print(f"   a = {a} ({time.time() - ta:.0f} s): |cos(k, xi)| = {cosang:.4f}   "
              f"[lambda^-2 caveat {np.exp(-2 * a):.3f}]")
        print(f"      khat/(c Xi) at z = 2,4,6,8: " + ", ".join(f"{r:+.6f}" for r in kr))
        print(f"      vhat/(c Xi) at z = 2,4,6,8: " + ", ".join(f"{r:+.4f}" for r in vr))

    print("\n-- checks --")
    check("seed: vanishing integral (|int h| < 1e-8 after alpha)",
          abs(hint) < 1e-8, f"int h = {hint:.1e}, alpha = {ALPHA:.6f}")
    check("seed: psi_0 and psi_4 are Fourier self-dual (convention verified)",
          sd0 < 1e-6 and sd4 < 1e-6, f"max devs {sd0:.1e}, {sd4:.1e}")
    coss = [r["cos"] for r in rows]
    check("READOUT 1 recorded: the proximity curve |cos(k, xi)| across a",
          len(coss) == len(AVALS),
          " -> ".join(f"{c:.3f}" for c in coss))
    kz6 = [r["kr"][2] for r in rows]
    vz6 = [r["vr"][2] for r in rows]
    check("READOUT 2 recorded: kernel-vs-Xi and groundstate-vs-Xi at z = 6",
          True,
          "k: " + " -> ".join(f"{v:+.3f}" for v in kz6)
          + " | xi_gs: " + " -> ".join(f"{v:+.3f}" for v in vz6))

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print(f"\n{npass}/{len(CHECKS)} passed  ({time.time() - t0:.0f} s)")

    out = HERE / "e2av_kernel_proximity.npz"
    np.savez_compressed(
        out,
        avals=np.array(AVALS), cos=np.array(coss),
        kr=np.array([r["kr"] for r in rows]),
        vr=np.array([r["vr"] for r in rows]),
        lam2=np.array([r["lam2"] for r in rows]),
        alpha=ALPHA, zpts=np.array(ZPTS),
        checks_passed=npass, checks_total=len(CHECKS),
    )
    print(f"saved {out.name}")


if __name__ == "__main__":
    run()
