"""E2AU-DEPTH3000: the depth-double residue of the turnaround ladder (P12).

WHY THIS EXISTS. The e2au ladder (LEARNINGS #189) certified the no-turnaround
collapse of the unconstrained hard-window Weil-form ground state through
a = 4 at zero cutoff T = 1500, with a = 4.5 recorded only (basis gate 0.134)
and a = 5.0 recorded only (mixing ~ 1: the above-cutoff zero tail could
still mix the two lowest eigenvectors). The e2au dossier's own tail
arithmetic predicted that one more depth doubling (T ~ 3000) cures the
a = 5 mixing certificate; this driver executes that doubling to strengthen
the P12 note's certified evidence range (the no-turnaround ladder and the
horizon claims).

WHY A THIN DRIVER AND NOT A FORK. The e2au machinery reads its zero cutoff
T2 and working precision DPS2 from module globals at call time (GS2._tail2
integrates the mixing tail from T2; solve() sets mp.mp.dps = DPS2), so the
retarget is two attribute assignments on the imported module and the
numerics stay bit-identical to the certified instrument by construction.
Only the zero supply is swapped: built by the #188 zero_polish engine,
exactly as the e2au hand-off (iv) prescribed for this doubling.

THE RUN ORDER. a = 4.0 first as the OVERLAP CONTROL: its ratios were
bit-stable across the T = 600 -> 1500 doubling, so reproducing the stored
T = 1500 values within the 0.05 gate tolerance is the internal check that
the retargeted pipeline is the same instrument. Then a = 4.5 and a = 5.0
as the two depth points. The npz is saved incrementally after every rung
so a partial night still lands rungs in certified order.

Run:
  python -m experiments.arithmetic_geometric.e2au_depth3000
  python -m experiments.arithmetic_geometric.e2au_depth3000 --smoke

Outputs: _cache/e2au_depth3000.npz (incremental; gitignored tonight, to be
promoted next to the dossier by the write-up round per the evidence rule).
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import numpy as np
import mpmath as mp

import experiments.arithmetic_geometric.e2au_turnaround_ladder as e2au
from experiments._shared.zero_polish import zeros_hp

HERE = Path(__file__).resolve().parent
CACHE_DIR = HERE / "_cache"
PRIOR_NPZ = HERE / "e2au_turnaround_ladder.npz"

CHECKS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}"
          + (f"  ({detail})" if detail else ""), flush=True)


def certified(r):
    """The e2au certificate conjunction, verbatim: basis gate + mixing +
    margin. Reused so CERTIFIED means the same thing across depths."""
    return (r["conv"] and r["ref"]["mix"] < 0.05
            and 10 ** r["ref"]["lg0"] > 10 * r["ref"]["tail"])


def prior_row(a):
    """The stored T = 1500 refined-solve ratios for rung a, if that rung
    exists in the tracked e2au npz (the like-for-like comparison target)."""
    if not PRIOR_NPZ.exists():
        return None
    d = np.load(PRIOR_NPZ)
    hits = np.where(np.abs(d["avals"] - a) < 1e-9)[0]
    if len(hits) == 0:
        return None
    i = int(hits[0])
    return {"ratios": d["ratios_ref"][i], "lg0": float(d["lg0_ref"][i]),
            "mix": float(d["mixes_ref"][i]), "shift": float(d["shifts"][i])}


def save_partial(out_path, rows, T3, dps, npass=0, ntot=0):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    priors = [prior_row(r["a"]) for r in rows]
    np.savez_compressed(
        out_path,
        T=T3, dps=dps,
        avals=np.array([r["a"] for r in rows]),
        shifts=np.array([r["shift"] for r in rows]),
        conv=np.array([r["conv"] for r in rows]),
        certified=np.array([certified(r) for r in rows]),
        ratios_ref=np.array([r["ref"]["ratios"] for r in rows]),
        ratios_base=np.array([r["base"]["ratios"] for r in rows]),
        lg0_ref=np.array([r["ref"]["lg0"] for r in rows]),
        gaps_ref=np.array([r["ref"]["gap"] for r in rows]),
        tails_ref=np.array([r["ref"]["tail"] for r in rows]),
        mixes_ref=np.array([r["ref"]["mix"] for r in rows]),
        Js=np.array([[r["base"]["J"], r["ref"]["J"]] for r in rows]),
        zpts=np.array(e2au.ZPTS),
        rung_seconds=np.array([r["secs"] for r in rows]),
        prior_ratios_ref=np.array(
            [p["ratios"] if p is not None else [np.nan] * len(e2au.ZPTS)
             for p in priors]),
        prior_lg0=np.array([p["lg0"] if p is not None else np.nan
                            for p in priors]),
        prior_mix=np.array([p["mix"] if p is not None else np.nan
                            for p in priors]),
        checks_passed=npass, checks_total=ntot,
    )


def run(smoke: bool):
    t0 = time.time()
    if smoke:
        # dps 60 / T = 200: the e2as a = 1 protocol regime. Lower dps starves
        # the degree-25 spline Gram (the documented e2av failure class) and
        # the smoke rung stops converging, which would test nothing.
        T3, dps, avals, workers = 200.0, 60, [1.0], 2
        out_path = CACHE_DIR / "e2au_depth3000_smoke.npz"
    else:
        T3, dps, avals, workers = 3000.0, 110, [4.0, 4.5, 5.0], 6
        out_path = CACHE_DIR / "e2au_depth3000.npz"
    print(f"== E2AU-DEPTH3000: the ladder depth-double "
          f"({'SMOKE' if smoke else 'FULL'}: T = {T3:g}, dps = {dps}, "
          f"a = {avals}) ==", flush=True)

    # retarget the imported instrument (module globals read at call time)
    e2au.T2 = T3
    e2au.DPS2 = dps

    # zero supply via the batch Newton polisher (count-checked against
    # mp.nzeros inside zeros_hp; cached in the shared cache dir in full mode)
    tz = time.time()
    gz = zeros_hp(T3, dps, workers=workers, cache=not smoke)
    print(f"  zeros: {len(gz)} to T = {T3:g} at {dps} digits "
          f"({time.time() - tz:.0f} s)", flush=True)
    check("zero cache sane: first zero is 14.134725..., last <= T",
          abs(float(gz[0]) - 14.134725) < 1e-5 and float(gz[-1]) <= T3,
          f"first = {float(gz[0]):.6f}, last = {float(gz[-1]):.3f}, "
          f"n = {len(gz)}")

    rows = []
    for a in avals:
        ta = time.time()
        base = e2au.solve(a, gz, int(round(56 * a)))
        ref = e2au.solve(a, gz, int(round(112 * a)))
        shift = float(max(abs(x - y)
                          for x, y in zip(base["ratios"], ref["ratios"])))
        conv = shift < 0.05
        rows.append({"a": a, "base": base, "ref": ref, "shift": shift,
                     "conv": conv, "secs": time.time() - ta})
        r = rows[-1]
        print(f"   a = {a} (J = {base['J']}/{ref['J']}, {r['secs']:.0f} s): "
              f"log10 lam0 = {ref['lg0']:.2f}, gap = {ref['gap']:.1f}, "
              f"mix = {ref['mix']:.0e}, gate {shift:.4f} -> "
              f"{'CONVERGED' if conv else 'NOT CONVERGED'}"
              f" -> {'CERTIFIED' if certified(r) else 'recorded'}", flush=True)
        print("      ratios = "
              + ", ".join(f"{v:+.4f}" for v in ref["ratios"]), flush=True)
        p = prior_row(a)
        if p is not None:
            dmax = float(max(abs(x - y)
                             for x, y in zip(ref["ratios"], p["ratios"])))
            print(f"      vs T = 1500: max |dr| = {dmax:.2e}, "
                  f"dlg lam0 = {ref['lg0'] - p['lg0']:+.3f}, "
                  f"mix {p['mix']:.0e} -> {ref['mix']:.0e}", flush=True)
        save_partial(out_path, rows, T3, dps)

    print("\n-- checks --", flush=True)
    # OVERLAP CONTROL: the first rung must reproduce its stored T = 1500
    # refined ratios within the gate tolerance (the prior doubling was
    # bit-stable, so this should land orders below 0.05)
    p0 = prior_row(rows[0]["a"])
    if p0 is None:
        check("overlap control: prior-rung lookup path exercised "
              "(no stored rung at this a: smoke mode)", smoke,
              f"a = {rows[0]['a']}")
    else:
        d0 = float(max(abs(x - y) for x, y in
                       zip(rows[0]["ref"]["ratios"], p0["ratios"])))
        check("OVERLAP CONTROL: a = 4.0 reproduces the stored T = 1500 "
              "ratios within the 0.05 gate tolerance",
              d0 < 0.05, f"max |dr| = {d0:.2e}")
    check("gates: every rung's base-vs-refined shift recorded; majority "
          "converged",
          sum(1 for r in rows if r["conv"]) * 2 >= len(rows),
          "shifts: " + ", ".join(f"{r['shift']:.3f}" for r in rows))
    conv_rungs = [r for r in rows if r["conv"]]
    if smoke:
        # at smoke depth the mixing certificate is honestly T-limited (the
        # e2as story: it cleans with depth); the smoke contract is that the
        # certificate quantities compute and the spectrum is sane
        check("smoke: certificate quantities computed and spectrum sane "
              "(lam0 finite, gap > 1, tail >= 0)",
              all(np.isfinite(r["ref"]["lg0"]) and -80 < r["ref"]["lg0"] < 0
                  and r["ref"]["gap"] > 1 and r["ref"]["tail"] >= 0
                  for r in rows),
              ", ".join(f"lg0 = {r['ref']['lg0']:.1f}, gap = "
                        f"{r['ref']['gap']:.1f}, mix = {r['ref']['mix']:.0e}"
                        for r in rows))
    else:
        check("certificates on converged rungs: mixing < 0.05 and "
              "margin > 10x tail",
              all(r["ref"]["mix"] < 0.05
                  and 10 ** r["ref"]["lg0"] > 10 * r["ref"]["tail"]
                  for r in conv_rungs),
              "mixes: "
              + ", ".join(f"{r['ref']['mix']:.0e}" for r in conv_rungs))
        r50 = next((r for r in rows if abs(r["a"] - 5.0) < 1e-9), None)
        check("THE DELIVERABLE: a = 5.0 fully certified at T = 3000 "
              "(the #189 tail-arithmetic prediction: mixing cured by the "
              "depth doubling)",
              r50 is not None and certified(r50),
              "" if r50 is None else
              f"gate {r50['shift']:.4f}, mix {r50['ref']['mix']:.0e}, "
              f"lg lam0 {r50['ref']['lg0']:.1f}")
        r45 = next((r for r in rows if abs(r["a"] - 4.5) < 1e-9), None)
        vals = [(r["a"], r["ref"]["ratios"][0]) for r in rows]
        mono = all(vals[i + 1][1] < vals[i][1] + 0.02
                   for i in range(len(vals) - 1))
        check("VERDICT READABLE: a = 4.5 typed (certified or recorded with "
              "named failing gate) and the r(z=2) collapse direction "
              "recorded",
              len(rows) == 3,
              (f"a=4.5 {'CERTIFIED' if r45 and certified(r45) else 'recorded'}"
               + (f" (gate {r45['shift']:.3f}, mix {r45['ref']['mix']:.0e})"
                  if r45 else "")
               + "; r(z=2): "
               + " -> ".join(f"{v:+.4f}" for _, v in vals)
               + (" (monotone collapse)" if mono else " (NOT monotone)")))

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print(f"\n{npass}/{len(CHECKS)} passed  ({time.time() - t0:.0f} s)",
          flush=True)
    save_partial(out_path, rows, T3, dps, npass, len(CHECKS))
    print(f"saved {out_path}", flush=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true",
                    help="tiny T / low dps end-to-end exercise of the path")
    run(ap.parse_args().smoke)
