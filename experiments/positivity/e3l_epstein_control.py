"""Experiment 3L: a SECOND, independent off-line-zero control for the
Weil-form Gram-matrix / Schur-complement wrong-approach detector.

## Why

Every prior firing of the project's positivity detectors against a "wrong"
L-function used the SAME counterexample: Davenport-Heilbronn (3B, 3C, 3D, 3J,
3K). The detector's central claim is that it responds to off-line zeros per se
(one negative eigenvalue of the Schur complement per off-line zero pair), not
to a quirk of the D-H construction. That claim has never been tested against a
second, structurally independent construction. This experiment supplies one.

## The control

The Epstein zeta function Z_Q(s) of a positive-definite binary quadratic form
Q has a functional equation but, for class number > 1 non-principal forms, no
single Euler product, and it then has zeros off the critical line. It is a
genuinely different object from D-H (lattice sums vs a period-5 Dirichlet
series). Reconnaissance for this project found:

  - d = 47, NON-principal form 2x^2 + xy + 6y^2 (class number 5):
    one off-line zero pair at rho ~ 0.634 + 32.05 i (and FE partner
    0.366 + 32.05 i) up to T = 120.
  - d = 47, PRINCIPAL form x^2 + xy + 12y^2: NO off-line zeros up to T = 120
    (Selberg-like: it factors through Selberg-class L-functions).

So within a single discriminant we get both a D-H-like control (off-line zeros
present) and a Selberg-like control (none), in addition to zeta and chi_3.

## The test

For each target L we build the Weil-form Gram matrix M = M_on + M_off and its
Schur complement S against the on-line subspace, EXACTLY as in 3J (we import
that machinery). The detector predicts:

    schur_neg(L) = number of off-line zero pairs of L in the upper half plane.

Predictions:
    zeta,  chi_3                       : 0 off-line pairs -> schur_neg = 0
    Epstein d=47 principal             : 0 off-line pairs -> schur_neg = 0
    Epstein d=47 non-principal (T<=60) : 1 off-line pair  -> schur_neg = 1
    Davenport-Heilbronn (T<=200)       : 4 off-line pairs -> schur_neg = 4

If the Epstein non-principal form gives schur_neg = 1 (and PSD-with-redundancy
structure on the on-line part, like D-H), while the principal form looks
Selberg-like, the detector GENERALISES beyond D-H and the wrong-approach
discipline is hardened. If it does not, the detector was D-H-specific, which is
equally important to know.

Note on matched heights: different L-functions have their first off-line zero
at different heights (D-H at 85.7, Epstein d=47 at 32.05), so we do NOT force a
common T_max. We run each L at a T_max that comfortably contains its known
off-line structure and check the relation schur_neg = n_off_pairs per L, which
is T_max-independent in content.

Outputs:
  - e3l_epstein_control.npz : per-(L, K) eigen statistics
  - e3l_epstein_control.png : detector summary across the five targets
  - stdout : per-target verdict table
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np

from experiments._shared import (
    zeta_L, chi3_L, DavenportHeilbronn,
    epstein_d47, epstein_d47_principal,
)
from experiments.positivity.e3c_weil_form import phi_b
from experiments.positivity.e3j_schur_complement import split_gram, schur_complement


def build_targets():
    """(label, L, T_max) for each control.

    T_max is chosen per L to contain its known off-line structure. The
    detector counting law is NOT hardcoded: it is the relation established
    for D-H in 3D.4, namely

        schur_neg == n_off      (one negative eigenvalue per off-line zero)
        schur_dim == 2 * n_off  (rank of M_off)

    where n_off is the number of off-line zeros that zeros() returns in the
    upper half plane (each off-line height contributes the pair beta+i gamma
    and its functional-equation partner (1-beta)+i gamma, both in the UHP, so
    a single off-line height shows up as n_off = 2). The experiment tests
    whether this same law holds for the Epstein controls.
    """
    dh = DavenportHeilbronn()
    return [
        ("zeta",            zeta_L,                  60.0),
        ("chi3",            chi3_L,                  60.0),
        ("epstein_d47_prin", epstein_d47_principal,  60.0),
        ("epstein_d47_np",  epstein_d47,             60.0),
        ("DH",              dh,                     200.0),
    ]


def run(
    K_vals=(50, 100, 200, 300),
    b_min: float = 1.1,
    b_max: float = 1000.0,
    prec: int = 30,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    targets = build_targets()

    print(f"[3L] Epstein second-control detector test (prec = {prec})")
    print(f"[3L] Loading zeros per target...")
    zeros_cache = {}
    for label, L, T_max in targets:
        t0 = time.time()
        rhos = L.zeros(T_max=T_max, prec=prec)
        is_on = np.array([abs(float(rho.real) - 0.5) < 1e-6 for rho in rhos])
        n_off = int((~is_on).sum())
        # Detector counting law (established for D-H in 3J / 3D.4): off-line
        # zeros come in functional-equation pairs sharing a HEIGHT gamma
        # (beta + i gamma and (1-beta) + i gamma). Each off-line HEIGHT
        # contributes a rank-2 indefinite block (signature (+1,-1)), so
        #     schur_dim == 2 * (# distinct off-line heights)
        #     schur_neg ==      (# distinct off-line heights).
        # The prediction is the number of distinct off-line heights.
        off_heights = sorted({round(float(r.imag), 3)
                              for r, on in zip(rhos, is_on) if not on})
        pred = len(off_heights)
        zeros_cache[label] = (rhos, is_on, T_max, pred)
        print(f"  {label:16s}: {len(rhos):3d} zeros "
              f"({int(is_on.sum())} on-line, {n_off} off-line at "
              f"{pred} distinct height(s)) T_max={T_max:.0f}, "
              f"predicted Schur neg = {pred}, dim = {2*pred} "
              f"[{time.time() - t0:.1f}s]")

    results = {label: {} for label, *_ in targets}

    for K in K_vals:
        b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)
        print(f"\n[3L] K = {K}")
        for label, L, T_max in targets:
            rhos, is_on, _, pred = zeros_cache[label]
            t0 = time.time()
            phi_table = np.empty((K, len(rhos)), dtype=np.complex128)
            for k, b in enumerate(b_vals):
                b_mp = mp.mpf(b)
                for r_idx, rho in enumerate(rhos):
                    phi_table[k, r_idx] = complex(phi_b(b_mp, rho, prec=prec))

            M_on, M_off = split_gram(phi_table, is_on)
            M = M_on + M_off
            S, d_off, M_on_Q, M_QC, r_dim = schur_complement(M_on, M_off)

            eig_M = np.linalg.eigvalsh(M)
            scale_M = max(abs(eig_M).max(), 1.0)
            if S.size > 0:
                eig_S = np.linalg.eigvalsh(S)
                scale_S = max(abs(eig_S).max(), 1.0)
                schur_neg = int((eig_S < -1e-10 * scale_S).sum())
                schur_pos = int((eig_S > 1e-10 * scale_S).sum())
                schur_min = float(eig_S.min())
                schur_rel_min = schur_min / scale_S
            else:
                schur_neg = schur_pos = 0
                schur_min = schur_rel_min = 0.0

            n_off = int((~is_on).sum())
            results[label][K] = {
                "n_on": int(is_on.sum()),
                "n_off": n_off,
                "predicted_schur_neg": pred,
                "schur_dim": r_dim,
                "schur_neg": schur_neg,
                "schur_pos": schur_pos,
                "schur_min": schur_min,
                "schur_rel_min": schur_rel_min,
                "eig_M_min": float(eig_M.min()),
                "eig_M_rel_min": float(eig_M.min() / scale_M),
                "eig_M_neg": int((eig_M < -1e-10 * scale_M).sum()),
                "T_max": T_max,
            }
            r = results[label][K]
            law_neg = (schur_neg == pred)
            law_dim = (r_dim == 2 * pred)
            verdict = "PASS" if (law_neg and law_dim) else "MISMATCH"
            print(f"  {label:16s}: Schur dim={r_dim} (pred {2*pred}), "
                  f"neg={schur_neg} (pred {pred}), pos={schur_pos}, "
                  f"rel_min={schur_rel_min:+.4%} -> {verdict} "
                  f"[{time.time() - t0:.1f}s]")

    # Save
    save = {"K_vals": np.asarray(K_vals), "prec": int(prec)}
    for label, res in results.items():
        for K, r in res.items():
            for key, val in r.items():
                save[f"{label}_K{K}_{key}"] = val
    np.savez_compressed(out_dir / "e3l_epstein_control.npz", **save)

    # Plot: schur_neg vs predicted, and schur_rel_min, across targets at max K.
    Kmax = max(K_vals)
    labels = [t[0] for t in targets]
    colors = {"zeta": "tab:blue", "chi3": "tab:green",
              "epstein_d47_prin": "tab:purple", "epstein_d47_np": "tab:orange",
              "DH": "tab:red"}

    fig, axs = plt.subplots(2, 2, figsize=(13, 9))

    ax = axs[0, 0]
    preds = [results[l][Kmax]["predicted_schur_neg"] for l in labels]
    obs = [results[l][Kmax]["schur_neg"] for l in labels]
    xpos = np.arange(len(labels))
    ax.bar(xpos - 0.2, preds, 0.4, label="predicted = #off-line heights", color="lightgray", edgecolor="k")
    ax.bar(xpos + 0.2, obs, 0.4, label="observed Schur neg", color="tab:red", alpha=0.8)
    ax.set_xticks(xpos); ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=8)
    ax.set_ylabel("count")
    ax.set_title(f"Detector counting law at K={Kmax}\n(observed neg should equal predicted off pairs)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis="y")

    ax = axs[0, 1]
    for l in labels:
        Ks = list(results[l].keys())
        vals = [results[l][k]["schur_neg"] for k in Ks]
        ax.plot(Ks, vals, "o-", label=l, color=colors.get(l))
    ax.set_xlabel("K (basis size)"); ax.set_ylabel("# negative eigenvalues of S")
    ax.set_title("Schur negative count vs K\n(should be flat = off-line pair count)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axs[1, 0]
    for l in labels:
        Ks = list(results[l].keys())
        vals = [results[l][k]["schur_rel_min"] for k in Ks]
        ax.plot(Ks, vals, "o-", label=l, color=colors.get(l))
    ax.axhline(0, color="k", lw=0.5)
    ax.set_yscale("symlog", linthresh=1e-6)
    ax.set_xlabel("K (basis size)"); ax.set_ylabel(r"rel. $\lambda_{\min}(S)$")
    ax.set_title("Schur relative min eigenvalue\n(negative = off-line obstruction)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axs[1, 1]
    for l in labels:
        Ks = list(results[l].keys())
        vals = [results[l][k]["schur_dim"] for k in Ks]
        ax.plot(Ks, vals, "o-", label=l, color=colors.get(l))
    ax.set_xlabel("K (basis size)"); ax.set_ylabel("dim(Schur subspace) = rank $M_{off}$")
    ax.set_title("Off-line subspace dimension\n(= 2 x off-line pair count)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e3l_epstein_control.png", dpi=140)
    plt.close()
    print(f"\n[3L] Saved {out_dir / 'e3l_epstein_control.png'}")
    print(f"[3L] Saved {out_dir / 'e3l_epstein_control.npz'}")

    # Verdict summary
    print("\n" + "=" * 78)
    print("[3L] Verdict (at K = %d)" % Kmax)
    print("=" * 78)
    all_pass = True
    for label, *_ in targets:
        r = results[label][Kmax]
        pred = r["predicted_schur_neg"]
        ok = (r["schur_neg"] == pred and r["schur_dim"] == 2 * pred)
        all_pass = all_pass and ok
        print(f"  {label:16s}: off-line heights = {pred:2d}, "
              f"Schur dim = {r['schur_dim']:2d} (law 2*heights = {2*pred:2d}), "
              f"Schur neg = {r['schur_neg']:2d} (law heights = {pred:2d})  "
              f"-> {'PASS' if ok else 'MISMATCH'}")
    print()
    if all_pass:
        print("  RESULT: the Weil-form Schur detector obeys the same counting law")
        print("  on the Epstein controls as on D-H: schur_neg = n_off and")
        print("  schur_dim = 2 * n_off. The Epstein NON-principal form (off-line")
        print("  zeros present) fires the detector; the Epstein PRINCIPAL form and")
        print("  the Selberg-class L-functions (zeta, chi_3) are PSD with no")
        print("  obstruction. The wrong-approach detector GENERALISES beyond")
        print("  Davenport-Heilbronn to a second, independent construction.")
    else:
        print("  RESULT: at least one target broke the counting law. The detector")
        print("  may be construction-specific; see the mismatched rows above.")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--K", type=int, nargs="+", default=[50, 100, 200, 300])
    parser.add_argument("--prec", type=int, default=30)
    parser.add_argument("--b-min", type=float, default=1.1)
    parser.add_argument("--b-max", type=float, default=1000.0)
    args = parser.parse_args()
    run(K_vals=tuple(args.K), b_min=args.b_min, b_max=args.b_max, prec=args.prec)
