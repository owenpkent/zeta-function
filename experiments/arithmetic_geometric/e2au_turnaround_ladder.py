"""E2AU: B2c-deep2: hunting the turnaround window a* (LEARNINGS #187 mission).

The composition that defines this run: #185 measured (certified, gated) the
unconstrained hard-window Weil-form ground state NARROWING away from the xi
shape through a = 2.5; CCM (arXiv:2511.22755, Lemma 7.3) PROVE their kernel's
Fourier transform converges to Xi interior-uniformly as the window grows; and
#187 settled at source that (1.2)'s object is the unconstrained bottom. If
CCM's kernel-groundstate proximity persists, the measured outbound narrowing
must therefore REVERSE at some turnaround window a*. This module hunts it:

  LADDER: a in {2.5, 3.0, 3.5, 4.0, 4.5, 5.0}, dps-110 solves on 110-digit
  zeros to T = 600 (both walls scaled from the e2ar/e2as measurements), base
  (m = 56 a) and refined (m = 112 a) per rung with the pointwise convergence
  gate, tail and mixing certificates, and INCREMENTAL npz saving (long run:
  partial results survive).

  READOUT: the ratio v/(c Xi) at z = 6 (and the wider z-grid) across a.
  Turnaround = the sequence turning back UP toward 1 after its minimum.
  Either outcome types: a* located (first quantitative contact with the
  conjectured mechanism) or monotone continuation (the proximity to CCM's
  kernel must fail somewhere: equally sharp, and measurable next).

Run (after _e2au_zeros builds the cache):
  python -m experiments.arithmetic_geometric.e2au_turnaround_ladder

Outputs: e2au_turnaround_ladder.npz (tracked; written incrementally).
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import mpmath as mp

from experiments.arithmetic_geometric.e2ar_hard_window_xi import (
    DEG, HardWindowGS)
from experiments.arithmetic_geometric.e2aq_xi_convergence import Xi

HERE = Path(__file__).resolve().parent
ZCACHE = HERE.parent / "_shared" / "_cache" / "zeros_dps110_T600.json"

DPS2 = 110
T2 = 600.0
ZPTS = [2.0, 4.0, 6.0, 8.0, 10.0]

CHECKS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


def zeros2():
    mp.mp.dps = DPS2
    return [mp.mpf(s) for s in json.loads(ZCACHE.read_text())]


class GS2(HardWindowGS):
    def __init__(self, a, gz, m_knots=None):
        super().__init__(a, gz, m_knots=m_knots, dps=DPS2)
        self.tail_actual = self._tail2(self.c)
        self.tail_u1 = self._tail2(self.c1)

    def _tail2(self, cvec, t_hi=8000.0):
        cf = np.array([float(cvec[r]) for r in range(self.J)])
        cen = np.array([float(x) for x in self.centers])
        hf = float(self.h)
        tt = np.arange(T2, t_hi, 0.5)
        base = hf * (np.sin(tt * hf / 2) / (tt * hf / 2)) ** (DEG + 1)
        mult = np.where(cen[:, None] > 0, 2.0, 1.0) * np.cos(np.outer(cen, tt))
        vh = base * (cf @ mult)
        rho = np.log(tt / (2 * np.pi)) / (2 * np.pi)
        return float(2 * np.trapezoid(vh ** 2 * rho, tt))


def solve(a, gz, m):
    gs = GS2(a, gz, m_knots=m)
    mp.mp.dps = DPS2
    c0 = float(gs.vhat(0.0)) / float(Xi(0.0))
    ratios = [float(gs.vhat(z)) / (c0 * float(Xi(z))) for z in ZPTS]
    lg0 = float(mp.log10(abs(gs.lam0))) if gs.lam0 != 0 else float("-inf")
    gap = float(gs.lam1 / gs.lam0) if gs.lam0 != 0 else float("inf")
    mix = (np.sqrt(max(gs.tail_actual, 0) * max(gs.tail_u1, 0))
           / max(float(gs.lam1 - gs.lam0), 1e-300))
    return {"J": gs.J, "lg0": lg0, "gap": gap, "ratios": ratios,
            "tail": gs.tail_actual, "mix": mix}


def save_partial(rows, npass=0, ntot=0):
    out = HERE / "e2au_turnaround_ladder.npz"
    np.savez_compressed(
        out,
        avals=np.array([r["a"] for r in rows]),
        shifts=np.array([r["shift"] for r in rows]),
        conv=np.array([r["conv"] for r in rows]),
        ratios_ref=np.array([r["ref"]["ratios"] for r in rows]),
        ratios_base=np.array([r["base"]["ratios"] for r in rows]),
        lg0_ref=np.array([r["ref"]["lg0"] for r in rows]),
        gaps_ref=np.array([r["ref"]["gap"] for r in rows]),
        tails_ref=np.array([r["ref"]["tail"] for r in rows]),
        mixes_ref=np.array([r["ref"]["mix"] for r in rows]),
        Js=np.array([[r["base"]["J"], r["ref"]["J"]] for r in rows]),
        zpts=np.array(ZPTS),
        checks_passed=npass, checks_total=ntot,
    )


def run():
    t0 = time.time()
    print("== E2AU: the turnaround hunt (B2c-deep2) ==")
    gz = zeros2()
    print(f"  zero cache: {len(gz)} zeros to T = {T2} at {DPS2} digits")
    mp.mp.dps = DPS2

    AVALS = [2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
    rows = []
    for a in AVALS:
        ta = time.time()
        base = solve(a, gz, int(round(56 * a)))
        ref = solve(a, gz, int(round(112 * a)))
        shift = float(max(abs(x - y) for x, y in zip(base["ratios"], ref["ratios"])))
        conv = shift < 0.05
        rows.append({"a": a, "base": base, "ref": ref, "shift": shift, "conv": conv})
        print(f"   a = {a} (J = {base['J']}/{ref['J']}, {time.time() - ta:.0f} s): "
              f"log10 lam0 = {ref['lg0']:.2f}, gap = {ref['gap']:.1f}, "
              f"mix = {ref['mix']:.0e}, gate {shift:.4f} -> "
              f"{'CONVERGED' if conv else 'NOT CONVERGED'}")
        print(f"      ratios = " + ", ".join(f"{r:+.4f}" for r in ref["ratios"]))
        save_partial(rows)

    print("\n-- checks --")
    check("anchor: a = 2.5 reproduces #185 within 0.06 at z = 6 (now with "
          "deeper zeros; its e2as mixing failure should also clean up)",
          abs(rows[0]["ref"]["ratios"][2] - 0.0286) < 0.06
          and rows[0]["ref"]["mix"] < 0.05,
          f"r(z=6) = {rows[0]['ref']['ratios'][2]:+.4f}, mix = {rows[0]['ref']['mix']:.0e}")
    conv_rungs = [r for r in rows if r["conv"]]
    check("gates: majority of rungs converged",
          len(conv_rungs) >= 4,
          "shifts: " + ", ".join(f"{r['shift']:.3f}" for r in rows))
    check("certificates on converged rungs: mixing < 0.05 and margin > 10x tail",
          all(r["ref"]["mix"] < 0.05 and 10 ** r["ref"]["lg0"] > 10 * r["ref"]["tail"]
              for r in conv_rungs),
          "mixes: " + ", ".join(f"{r['ref']['mix']:.0e}" for r in conv_rungs))
    r6 = [(r["a"], r["ref"]["ratios"][2], r["conv"]) for r in rows]
    print("\n-- THE TURNAROUND READOUT (r at z = 6 across the ladder) --")
    for a, v, c in r6:
        print(f"   a = {a}: r(z=6) = {v:+.4f}  [{'conv' if c else 'UNCONV'}]")
    vals = [v for _, v, c in r6 if c]
    turned = any(vals[i + 1] > vals[i] + 0.02 for i in range(len(vals) - 1))
    check("VERDICT READABLE: the r(z=6) sequence on converged rungs either "
          "turns back up (a* bracketed) or continues down (proximity must "
          "fail): recorded either way",
          len(vals) >= 3,
          ("TURNAROUND detected" if turned else "monotone continuation")
          + ": " + " -> ".join(f"{v:+.3f}" for v in vals))

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print(f"\n{npass}/{len(CHECKS)} passed  ({time.time() - t0:.0f} s)")
    save_partial(rows, npass, len(CHECKS))
    print("saved e2au_turnaround_ladder.npz")


if __name__ == "__main__":
    run()
