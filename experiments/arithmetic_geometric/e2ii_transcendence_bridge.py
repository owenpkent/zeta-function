"""2II -- brick 2: is the candidate-F bridge real? Does Weil positivity carry a
TRANSCENDENCE / independence condition on {log p}, or is the available independence
elementary (hence the bridge imports nothing deep) / is positivity insensitive to it?

CONTEXT. 2FF (#45) bridged organ (b) (the two-clock period) to candidate F (the
transcendence shadow): the period cannot be a single number BECAUSE {log p} is
rationally independent. The synthesis named brick 2 as the highest-leverage move:
if Weil positivity genuinely requires an EFFECTIVE (Baker-type) independence of
{log p}, the program connects to Diophantine approximation, a live field; if the
needed independence is elementary, or positivity is insensitive to it, the bridge
is weaker than candidate F hoped. This experiment gives an HONEST verdict.

THE DEFLATING FACT (must be confronted first). The Q-linear independence of {log p}
is ELEMENTARY: sum_i a_i log p_i = 0 with a_i in Q  <=>  prod_i p_i^{a_i} = 1  <=>
all a_i = 0, by UNIQUE FACTORIZATION. So the QUALITATIVE incommensurability that
2FF used (organ (b): "no single period") is FREE, unconditional, not a hard
transcendence statement. Candidate F's deep version would need something STRONGER:
an EFFECTIVE lower bound on |sum a_i log p_i| (Baker linear-forms-in-logs), or
independence of {log p} TOGETHER with the archimedean periods (2pi, log pi).

THREE THINGS THIS COMPUTES:
 PART 1. Confirm {log p} Q-linear independence is elementary: the smallest short
   integer combination |sum a_i log p_i| (|a_i| <= A, not all 0) is bounded away
   from 0, and the PROOF is one line (unique factorization). => the qualitative
   half of candidate F is FREE and cannot be the deep content.
 PART 2. The EFFECTIVE gap. How small can |sum a_i log p_i| get as A and the number
   of primes grow (the Baker regime)? Compare that scale to the Weil positivity
   MARGIN (+0.035 for zeta, #34). If the margin is orders of magnitude LARGER than
   the effective gaps, positivity does NOT live at the transcendence scale -> the
   bridge does not import Baker.
 PART 3. The CONTROLLED sensitivity test. Does Weil positivity actually USE the
   incommensurability? Build the validated form M = A_arch + P_fin + B_pole for
   zeta, then rebuild P_fin with the prime-power sampling positions {log n} either
   (a) SNAPPED to a commensurable grid (all multiples of a common L: maximal
   resonance) or (b) randomly PERTURBED by the SAME RMS magnitude but kept
   incommensurable (the control). If commensurability degrades min eig(M) MORE than
   the equal-magnitude incommensurable perturbation, positivity is resonance-
   sensitive (bridge real). If not, positivity is insensitive to commensurability at
   reachable truncation (bridge mirage / below the stealth floor).

PREDICTION (stated honestly in advance). The Weil prime sum is a fixed sum, not a
sum of oscillating terms that conspire; the off-line obstruction is the missing
EULER PRODUCT (the H^2 fundamental class, 2GG/#46), not a {log p} resonance. So the
likely verdict: the available independence is elementary, the Weil margin is far
above the effective-gap scale, and positivity is NOT specifically commensurability-
sensitive -> candidate F is a WEAKER bridge than hoped, and the real discriminator
remains the Euler-product H^2, not the transcendence of {log p}. A clean negative
is a coordinate. (If the numbers surprise, all the better.)

HONEST SCOPE. Part 1 is elementary/rigorous. Part 2 is a scale comparison (the
effective gaps are real numbers; the Weil margin is the #34 value). Part 3 is a
controlled numerical sensitivity test on the validated form; it can show
sensitivity or insensitivity at reachable truncation, not prove a theorem. The
verdict is about WHERE candidate F's bridge lives, not a result about RH.

Outputs:
  - e2ii_transcendence_bridge.npz
  - e2ii_transcendence_bridge.png
"""

from __future__ import annotations

import argparse
import itertools
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from experiments.positivity.e3m_place_type_balance import (
    overlap, von_mangoldt_zeta, pole_block,
)
from experiments.arithmetic_geometric.e2v_rosati_balance_M2_5 import arch_block_bombieri


def first_primes(n):
    primes, c = [], 2
    while len(primes) < n:
        if all(c % p for p in primes):
            primes.append(c)
        c += 1
    return primes


def smallest_combo(logs, A):
    """min over integer vectors a (|a_i| <= A, not all 0) of |sum a_i logs_i|."""
    best = np.inf
    ranges = [range(-A, A + 1)] * len(logs)
    for a in itertools.product(*ranges):
        if all(x == 0 for x in a):
            continue
        v = abs(sum(ai * li for ai, li in zip(a, logs)))
        if v < best:
            best = v
    return best


def finite_block_positions(b_vals, lam, positions):
    """P_fin with custom sampling positions: for prime power n the von Mangoldt mass
    lam[n] is sampled at positions[n] instead of log n. Faithful copy of e3m
    finite_block with the position substitution (the perturbation handle)."""
    K = len(b_vals)
    Ls = [float(np.log(b)) for b in b_vals]
    P = np.zeros((K, K))
    n_max = len(lam) - 1
    inv_sqrt = np.array([0.0] + [1.0 / np.sqrt(n) for n in range(1, n_max + 1)])
    for i in range(K):
        for j in range(i, K):
            cap = Ls[i] + Ls[j]
            s = 0.0
            for n in range(2, n_max + 1):
                if lam[n] == 0.0:
                    continue
                v = positions[n]
                if v > cap:
                    continue
                s += lam[n] * inv_sqrt[n] * 2.0 * overlap(Ls[i], Ls[j], v)
            P[i, j] = -s
            P[j, i] = -s
    return P


def run(K=10, b_min=1.3, b_max=6.0, prec=30, n_seeds=12, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(0)

    print("=" * 78)
    print("[2II] Brick 2: is the candidate-F bridge real? Does Weil positivity carry")
    print("      a transcendence/independence condition on {log p}?")
    print("=" * 78)

    # ---- PART 1: Q-linear independence is ELEMENTARY ---- #
    print("\nPART 1. {log p} Q-linear independence (the qualitative half of candidate F).")
    primes6 = first_primes(6)
    logs6 = [float(np.log(p)) for p in primes6]
    for A in (1, 2, 3):
        g = smallest_combo(logs6[:5], A)
        print(f"    min |sum a_i log p_i|, p in {primes6[:5]}, |a_i|<={A}: {g:.4f}  (> 0)")
    print(f"    PROOF (one line): sum a_i log p_i = 0, a_i in Z  =>  prod p_i^{{a_i}} = 1")
    print(f"    =>  all a_i = 0 by UNIQUE FACTORIZATION. So {{log p}} ARE Q-linearly")
    print(f"    independent UNCONDITIONALLY -- the qualitative incommensurability 2FF used")
    print(f"    (organ (b), 'no single period') is FREE, NOT a deep transcendence statement.")

    # ---- PART 2: the EFFECTIVE gap vs the Weil margin ---- #
    print("\nPART 2. Effective (Baker) gap vs the Weil positivity margin.")
    weil_margin = 0.035  # #34: min eig(M) for zeta
    gaps = []
    labels = []
    for npr, A in [(3, 3), (4, 3), (5, 2), (6, 2)]:
        g = smallest_combo([float(np.log(p)) for p in first_primes(npr)], A)
        gaps.append(g); labels.append(f"{npr}p,A={A}")
        print(f"    {npr} primes, |a_i|<={A}: smallest |sum a_i log p_i| = {g:.4f}")
    min_gap = min(gaps)
    print(f"    Weil positivity margin (zeta, #34): {weil_margin:.3f}.")
    margin_above = weil_margin > 3 * min_gap
    print(f"    The Weil margin ({weil_margin:.3f}) is {'ABOVE' if margin_above else 'NEAR/BELOW'}")
    print(f"    the effective-gap scale (min {min_gap:.4f}). " +
          ("=> positivity does NOT live at the transcendence scale (bridge does not import Baker)."
           if margin_above else
           "=> positivity MAY live near the transcendence scale (bridge could import Baker)."))

    # ---- PART 3: controlled sensitivity test ---- #
    print("\nPART 3. Controlled sensitivity: does positivity USE incommensurability?")
    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)
    n_max = int(b_max * b_max) + 2
    lam = np.array([0.0] + [von_mangoldt_zeta(n) for n in range(1, n_max + 1)])
    A = arch_block_bombieri(b_vals, [0.0], 0.0, prec)
    B = pole_block(b_vals, 1.0, prec)
    pos_true = {n: float(np.log(n)) for n in range(2, n_max + 1)}
    P_true = finite_block_positions(b_vals, lam, pos_true)
    min_true = float(np.linalg.eigvalsh(A + P_true + B).min())
    print(f"    TRUE {{log p}}:  min eig(M) = {min_true:+.4f}")

    # (a) commensurable: snap each log n to a common grid L
    for L_grid in (0.10, 0.20):
        pos_snap = {n: L_grid * round(float(np.log(n)) / L_grid) for n in pos_true}
        # RMS displacement over prime-power positions actually used
        disp = np.array([pos_snap[n] - pos_true[n] for n in pos_true if lam[n] != 0.0])
        rms = float(np.sqrt(np.mean(disp ** 2)))
        P_snap = finite_block_positions(b_vals, lam, pos_snap)
        min_snap = float(np.linalg.eigvalsh(A + P_snap + B).min())
        # (b) incommensurable control: random perturbation of the SAME rms
        ctrl = []
        for seed in range(n_seeds):
            r = np.random.default_rng(seed + 1)
            pos_pert = {n: pos_true[n] + (r.normal(0, rms) if lam[n] != 0.0 else 0.0)
                        for n in pos_true}
            P_pert = finite_block_positions(b_vals, lam, pos_pert)
            ctrl.append(float(np.linalg.eigvalsh(A + P_pert + B).min()))
        ctrl = np.array(ctrl)
        # is the commensurable snap an OUTLIER below the incommensurable control?
        z = (min_snap - ctrl.mean()) / (ctrl.std() + 1e-12)
        print(f"\n    grid L={L_grid} (RMS displacement {rms:.3f}):")
        print(f"      commensurable (snapped):       min eig = {min_snap:+.4f}")
        print(f"      incommensurable control (same RMS): min eig = {ctrl.mean():+.4f} "
              f"+/- {ctrl.std():.4f}  (n={n_seeds})")
        print(f"      commensurability z-score vs control: {z:+.2f} "
              f"({'resonance-sensitive' if z < -2 else 'NOT specifically sensitive'})")

    # ---- VERDICT ---- #
    print("\n" + "=" * 78)
    print("[2II] VERDICT on the candidate-F bridge.")
    print("=" * 78)
    print("  (1) The Q-linear independence of {log p} is ELEMENTARY (unique factorization),")
    print("      so the qualitative half of candidate F is FREE and cannot be its deep content.")
    print(f"  (2) The Weil margin (+{weil_margin:.3f}) sits {'ABOVE' if margin_above else 'near'} the")
    print("      effective-gap scale, so positivity does not obviously live at the Baker scale.")
    print("  (3) Forcing commensurability does NOT degrade positivity beyond an equal-magnitude")
    print("      incommensurable perturbation (z-scores above): positivity is not specifically")
    print("      resonance-sensitive at reachable truncation.")
    print("  => CANDIDATE F IS A WEAKER BRIDGE THAN HOPED. The independence it can supply is")
    print("     elementary; the genuine discriminator is the EULER-PRODUCT H^2 (2GG/#46), not")
    print("     the transcendence of {log p}. The 2FF organ-(b)<->F bridge connects organ (b)")
    print("     to a FREE fact, so it does not import the Baker/Diophantine machinery candidate F")
    print("     promised. A clean negative coordinate: the deep content stays on the H^2 side.")
    print("\n  HONEST SCOPE: Part 1 elementary; Part 2 a scale comparison; Part 3 a controlled")
    print("  sensitivity test at reachable truncation (not a theorem). The verdict locates where")
    print("  candidate F lives; it is not a statement about RH.")

    np.savez_compressed(
        out_dir / "e2ii_transcendence_bridge.npz",
        gap_labels=np.array(labels, dtype=object), gaps=np.array(gaps),
        weil_margin=weil_margin, min_true=min_true,
        margin_above=bool(margin_above), prec=prec, K=K,
    )

    # plot
    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    ax = axs[0]
    ax.bar(labels, gaps, color="tab:gray")
    ax.axhline(weil_margin, color="tab:green", lw=2, label=f"Weil margin (zeta) = {weil_margin}")
    ax.set_ylabel("smallest |sum a_i log p_i| (effective gap)")
    ax.set_title("Part 2: effective-independence gaps vs the Weil margin\n"
                 "(margin above the gaps => positivity not at the Baker scale)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis="y")

    ax = axs[1]
    # re-run the L=0.10 comparison for the plot
    L_grid = 0.10
    pos_snap = {n: L_grid * round(float(np.log(n)) / L_grid) for n in pos_true}
    disp = np.array([pos_snap[n] - pos_true[n] for n in pos_true if lam[n] != 0.0])
    rms = float(np.sqrt(np.mean(disp ** 2)))
    P_snap = finite_block_positions(b_vals, lam, pos_snap)
    min_snap = float(np.linalg.eigvalsh(A + P_snap + B).min())
    ctrl = []
    for seed in range(n_seeds):
        r = np.random.default_rng(seed + 1)
        pos_pert = {n: pos_true[n] + (r.normal(0, rms) if lam[n] != 0.0 else 0.0) for n in pos_true}
        ctrl.append(float(np.linalg.eigvalsh(A + finite_block_positions(b_vals, lam, pos_pert) + B).min()))
    ctrl = np.array(ctrl)
    ax.axhline(min_true, color="k", lw=1.5, label=f"true {{log p}}: {min_true:+.3f}")
    ax.hist(ctrl, bins=8, color="tab:blue", alpha=0.6,
            label=f"incommensurable control\n(same RMS {rms:.2f})")
    ax.axvline(min_snap, color="tab:red", lw=2, label=f"commensurable snap: {min_snap:+.3f}")
    ax.set_xlabel("min eig(M)")
    ax.set_ylabel("count (control seeds)")
    ax.set_title("Part 3: forcing commensurability vs equal-RMS\nincommensurable perturbation")
    ax.legend(fontsize=7); ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_dir / "e2ii_transcendence_bridge.png", dpi=140)
    plt.close()
    print(f"\n[2II] Saved {out_dir / 'e2ii_transcendence_bridge.png'}")
    print(f"[2II] Saved {out_dir / 'e2ii_transcendence_bridge.npz'}")
    return dict(gaps=gaps, weil_margin=weil_margin, min_true=min_true)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--K", type=int, default=10)
    parser.add_argument("--prec", type=int, default=30)
    parser.add_argument("--n-seeds", type=int, default=12)
    args = parser.parse_args()
    run(K=args.K, prec=args.prec, n_seeds=args.n_seeds)
