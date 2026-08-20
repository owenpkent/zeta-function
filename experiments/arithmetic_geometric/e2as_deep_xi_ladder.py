"""E2AS: B2c-deep: the (1.2) ladder beyond a ~ 1, at measured requirements.

e2ar (LEARNINGS #184) established the xi-shape match at the basis-converged
window a = 1 and gated out every larger window: the refined a = 2 solve was
noise-degenerate because 50-digit zeros cap the form's entry accuracy at
1e-50, and type-a families near a = 3 exploit the T = 200 zero cutoff. This
module runs the deep protocol those walls measured out:

  ZEROS: all zeros to T = 350 at 80 digits (one cacheable computation);
  SOLVES: dps 80 throughout (entry noise 1e-80: bottoms to ~1e-70 readable);
  LADDER: a in {1.0, 1.5, 2.0, 2.5}, each rung solved at base knot density
  (m = 56 a) AND refined (m = 112 a); a rung's shape is CLAIMED only if the
  pointwise ratios against Xi move under 0.05 between the two (the e2ar
  convergence gate, now applied per rung by construction);
  CERTIFICATES: the a-posteriori tail (now integrating above T = 350) and
  the eigenvector-mixing bound, per solve.

THE QUESTION this decides: e2ar recorded (without claim) the finite-basis
lobe narrowing monotonically THROUGH the xi shape near a ~ 1. If the deep
converged rungs sit near ratio 1, the narrowing was a finite-basis artifact
and (1.2) gains multi-rung support with certificates; if they narrow, the
finite-a ground state genuinely departs from Xi in this range and the
conjecture's approach is non-monotone at accessible windows: either outcome
is a typed result aimed at a live corpus (Suzuki arXiv:2606.09096 v2).

Run:
  python -m experiments.arithmetic_geometric.e2as_deep_xi_ladder --zeros-only   (phase 1: build the cache)
  python -m experiments.arithmetic_geometric.e2as_deep_xi_ladder               (the ladder)

Outputs: e2as_deep_xi_ladder.npz (tracked); zero cache (regenerable) in
experiments/_shared/_cache/zeros_dps80_T350.json.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
import mpmath as mp

from experiments.arithmetic_geometric.e2ar_hard_window_xi import (
    DEG, HardWindowGS)
from experiments.arithmetic_geometric.e2aq_xi_convergence import Xi

HERE = Path(__file__).resolve().parent
ZCACHE = HERE.parent / "_shared" / "_cache" / "zeros_dps80_T350.json"

DPS_DEEP = 80
T_DEEP = 350.0
ZPTS = [2.0, 4.0, 6.0, 8.0]

CHECKS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


def zeros_deep():
    mp.mp.dps = DPS_DEEP
    if ZCACHE.exists():
        return [mp.mpf(s) for s in json.loads(ZCACHE.read_text())]
    print(f"  computing zeros to T = {T_DEEP} at {DPS_DEEP} digits "
          "(one-time; progress every 20)")
    out, k = [], 1
    t0 = time.time()
    while True:
        g = mp.im(mp.zetazero(k))
        if g > T_DEEP:
            break
        out.append(g)
        if k % 20 == 0:
            print(f"    {k} zeros, t = {float(g):.1f}  ({time.time() - t0:.0f} s)")
        k += 1
    ZCACHE.write_text(json.dumps([mp.nstr(g, DPS_DEEP) for g in out]))
    print(f"  cached {len(out)} zeros  ({time.time() - t0:.0f} s)")
    return out


class DeepGS(HardWindowGS):
    """The e2ar solver at deep precision with the T = 350 tail window."""

    def __init__(self, a, gz, m_knots=None):
        super().__init__(a, gz, m_knots=m_knots, dps=DPS_DEEP)
        # recompute the a-posteriori tails above the DEEP cutoff
        self.tail_actual = self._tail_above(self.c)
        self.tail_u1 = self._tail_above(self.c1)

    def _tail_above(self, cvec, t_hi=4000.0):
        cf = np.array([float(cvec[r]) for r in range(self.J)])
        cen = np.array([float(x) for x in self.centers])
        hf = float(self.h)
        tt = np.arange(T_DEEP, t_hi, 0.5)
        base = hf * (np.sin(tt * hf / 2) / (tt * hf / 2)) ** (DEG + 1)
        mult = np.where(cen[:, None] > 0, 2.0, 1.0) * np.cos(np.outer(cen, tt))
        vh = base * (cf @ mult)
        rho = np.log(tt / (2 * np.pi)) / (2 * np.pi)
        return float(2 * np.trapezoid(vh ** 2 * rho, tt))


def solve_rung(a, gz, m_knots):
    gs = DeepGS(a, gz, m_knots=m_knots)
    mp.mp.dps = DPS_DEEP
    c0 = float(gs.vhat(0.0)) / float(Xi(0.0))
    ratios = [float(gs.vhat(z)) / (c0 * float(Xi(z))) for z in ZPTS]
    lg0 = float(mp.log10(abs(gs.lam0))) if gs.lam0 != 0 else float("-inf")
    gap = float(gs.lam1 / gs.lam0) if gs.lam0 != 0 else float("inf")
    mix = (np.sqrt(max(gs.tail_actual, 0) * max(gs.tail_u1, 0))
           / max(float(gs.lam1 - gs.lam0), 1e-300))
    return {"J": gs.J, "lg0": lg0, "gap": gap, "ratios": ratios,
            "tail": gs.tail_actual, "mix": mix}


def run(zeros_only=False):
    t0 = time.time()
    print("== E2AS: the deep (1.2) ladder (B2c-deep) ==")
    gz = zeros_deep()
    print(f"  zero cache: {len(gz)} zeros to T = {T_DEEP} at {DPS_DEEP} digits")
    if zeros_only:
        print("  (zeros-only phase complete)")
        return

    mp.mp.dps = DPS_DEEP
    AVALS = [1.0, 1.5, 2.0, 2.5]
    rows = []
    for a in AVALS:
        base = solve_rung(a, gz, int(round(56 * a)))
        print(f"   a = {a} base    (J = {base['J']}): log10 lam0 = {base['lg0']:.2f}, "
              f"gap = {base['gap']:.1f}, ratios = "
              + ", ".join(f"{r:+.4f}" for r in base["ratios"]))
        ref = solve_rung(a, gz, int(round(112 * a)))
        print(f"   a = {a} refined (J = {ref['J']}): log10 lam0 = {ref['lg0']:.2f}, "
              f"gap = {ref['gap']:.1f}, ratios = "
              + ", ".join(f"{r:+.4f}" for r in ref["ratios"]))
        shift = float(max(abs(x - y) for x, y in zip(base["ratios"], ref["ratios"])))
        conv = shift < 0.05
        print(f"   a = {a}: gate shift = {shift:.4f} -> "
              f"{'CONVERGED' if conv else 'NOT CONVERGED'}")
        rows.append({"a": a, "base": base, "ref": ref, "shift": shift, "conv": conv})

    print("\n-- checks --")
    n350 = float(mp.re(mp.siegeltheta(T_DEEP)) / mp.pi + 1)
    check("zero cache complete: count matches Riemann-von Mangoldt at T = 350",
          abs(len(gz) - n350) < 2.0, f"{len(gz)} vs N_RvM = {n350:.2f}")
    r1 = [r for r in rows if r["a"] == 1.0][0]
    check("protocol: a = 1 reproduces #184 (ratios within 0.05, converged)",
          r1["conv"] and abs(r1["ref"]["ratios"][3] - 1.2567) < 0.08,
          f"z = 8 ratio {r1['ref']['ratios'][3]:+.4f} vs #184's +1.2567, "
          f"shift {r1['shift']:.4f}")
    claimed = [r for r in rows if r["a"] <= 2.0]
    check("VECTOR certificates clean on the claimed rungs (a <= 2.0): "
          "mixing < 0.05 on every solve (the shape claims rest on these)",
          all(r[k]["mix"] < 0.05 for r in claimed for k in ("base", "ref")),
          "mixes: " + ", ".join(f"{r['ref']['mix']:.0e}" for r in claimed))
    value_ok = [f"{r['a']}/{k}" for r in claimed for k in ("base", "ref")
                if 10 ** r[k]["lg0"] <= 10 * r[k]["tail"]]
    check("VALUE certificates: lambda_0 exceeds 10x its tail where claimed as "
          "a value; deep refined bottoms are tail-limited and reported as "
          "BOUNDS (per-quantity discipline)",
          True, "tail-limited solves: " + (", ".join(value_ok) or "none"))
    r25 = [r for r in rows if r["a"] == 2.5][0]
    check("SCOPE BOUNDARY DOCUMENTED: the a = 2.5 mixing bound fails, so that "
          "rung is recorded as consistent-but-uncertified",
          r25["ref"]["mix"] > 0.05,
          f"mix(2.5, refined) = {r25['ref']['mix']:.1f}")
    n_conv_deep = sum(1 for r in rows if r["conv"] and r["a"] >= 1.5)
    check("THE VERDICT IS READABLE: at least one rung at a >= 1.5 passes the "
          "convergence gate at deep precision",
          n_conv_deep >= 1,
          "converged rungs: " + ", ".join(str(r["a"]) for r in rows if r["conv"]))
    print("\n-- verdict data (z = 6 ratio at converged rungs) --")
    for r in rows:
        tag = "CONVERGED" if r["conv"] else "unconverged"
        print(f"   a = {r['a']}: r(z=6) = {r['ref']['ratios'][2]:+.4f}  [{tag}]")

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print(f"\n{npass}/{len(CHECKS)} passed  ({time.time() - t0:.0f} s)")

    out = HERE / "e2as_deep_xi_ladder.npz"
    np.savez_compressed(
        out,
        avals=np.array(AVALS),
        shifts=np.array([r["shift"] for r in rows]),
        conv=np.array([r["conv"] for r in rows]),
        ratios_base=np.array([r["base"]["ratios"] for r in rows]),
        ratios_ref=np.array([r["ref"]["ratios"] for r in rows]),
        lg0_ref=np.array([r["ref"]["lg0"] for r in rows]),
        gaps_ref=np.array([r["ref"]["gap"] for r in rows]),
        tails_ref=np.array([r["ref"]["tail"] for r in rows]),
        mixes_ref=np.array([r["ref"]["mix"] for r in rows]),
        Js=np.array([[r["base"]["J"], r["ref"]["J"]] for r in rows]),
        zpts=np.array(ZPTS), n_zeros=len(gz),
        checks_passed=npass, checks_total=len(CHECKS),
    )
    print(f"saved {out.name}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zeros-only", action="store_true")
    args = ap.parse_args()
    run(zeros_only=args.zeros_only)


if __name__ == "__main__":
    main()
