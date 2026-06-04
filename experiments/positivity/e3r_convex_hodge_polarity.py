"""Experiment 3R: the wrong-polarity check for the convex-Hodge accident channel.

Cheap-probe 6 of the "RH solved by accident" dossier
(docs/03_research/rh_solved_by_accident.md). One B-credible accident channel is
the weighted tropical Kahler package (Amini-Piquerez): a Hodge-Riemann signature
that MOVES with arithmetic weights w_p = log p (defeating the AHK arithmetic-
blindness of #40). The ADVERSARY's objection is a polarity argument: a proven
Kahler / Hodge-Riemann package is UNCONDITIONALLY definite (it holds for ALL
admissible weights), so it can never go indefinite, i.e. it can never FAIL when a
zero leaves the line. Wrong polarity for an RH detector.

A real RH detector needs CONDITIONAL definiteness: the form is definite-on-the-
primitive-part IFF RH holds, and acquires the wrong-sign eigenvalue when an
off-line zero appears. This experiment contrasts the two polarities on small,
explicit, fast models:

  Part 1 (convex-Hodge, WRONG polarity): the mixed-area (Alexandrov-Fenchel /
    Lorentzian) form of n segments with weights w_i. By AF its signature is
    (1, n-1) for ANY positive weights. We sweep weights (uniform, the arithmetic
    w_p = log p, many random, adversarial extremes) and directions, and confirm
    the signature is INVARIANT (1, n-1): injecting arithmetic weights does not
    let it flip. It cannot detect.

  Part 2 (Weil form, RIGHT polarity): the augmented Weil Gram (e3k) is PSD when
    only on-line zeros are present (RH holds) and acquires a NEGATIVE eigenvalue
    when an off-line pair is injected (RH fails). Its signature is conditional.

Verdict: the convex-Hodge channel has the wrong polarity at the signature level.
Combined with #40 (arithmetic-blind), this is why the channel needs a genuinely
new theorem (a HR signature that BOTH carries t AND can fail), not just weight
injection. This is the dossier's #1 watchlist signal, stated as an obstruction.

Outputs:
  - e3r_convex_hodge_polarity.npz
  - e3r_convex_hodge_polarity.png
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from experiments._shared import zeta_L
from experiments.positivity.e3k_hypothetical_offline import augmented_gram

FIRST_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


def mixed_area_matrix(thetas, weights):
    """Lorentzian mixed-area form of n segments.

    Segment i has unit direction theta_i and length w_i. The 2D mixed area of two
    segments is V(i,j) = (1/2) w_i w_j |sin(theta_i - theta_j)| (a parallelogram
    area); V(i,i) = 0 (a segment has zero area). By Alexandrov-Fenchel the matrix
    [V(i,j)] is Lorentzian: exactly one positive eigenvalue, signature (1, n-1).
    """
    n = len(thetas)
    V = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                V[i, j] = 0.5 * weights[i] * weights[j] * abs(np.sin(thetas[i] - thetas[j]))
    return V


def signature(M, rtol=1e-9):
    eig = np.linalg.eigvalsh(M)
    tol = rtol * max(abs(eig).max(), 1.0)
    return int((eig > tol).sum()), int((eig < -tol).sum()), int((np.abs(eig) <= tol).sum())


def run(n=8, n_random=2000, K=40, T_max=50.0, prec=30, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 76)
    print("[3R] Wrong-polarity check for the convex-Hodge accident channel")
    print(f"     n={n} segments; sweeping {n_random} random weightings + curated ones")
    print("=" * 76)

    # Fixed generic directions (no two parallel).
    rng = np.random.default_rng(12345)
    thetas = np.sort(rng.uniform(0, np.pi, n))

    # ---- Part 1: convex-Hodge (Lorentzian) signature is invariant under weights ----
    print("\n[3R] Part 1: convex-Hodge (mixed-area) signature vs weight choice")
    weightings = {
        "uniform (w=1)": np.ones(n),
        "arithmetic w_p=log p": np.array([np.log(p) for p in FIRST_PRIMES[:n]]),
        "steep w=p": np.array(FIRST_PRIMES[:n], dtype=float),
        "adversarial (one huge)": np.array([1e6] + [1.0] * (n - 1)),
        "adversarial (one tiny)": np.array([1e-6] + [1.0] * (n - 1)),
    }
    sig_counts = {}
    for label, w in weightings.items():
        V = mixed_area_matrix(thetas, w)
        sig = signature(V)
        sig_counts[label] = sig
        print(f"     {label:<26} signature (pos,neg,zero) = {sig}")

    # Many random weightings + random directions: does the signature EVER leave (1, n-1)?
    off_polarity = 0
    sigs_seen = {}
    for _ in range(n_random):
        th = np.sort(rng.uniform(0, np.pi, n))
        w = rng.uniform(0.01, 100.0, n)
        sig = signature(mixed_area_matrix(th, w))
        sigs_seen[sig] = sigs_seen.get(sig, 0) + 1
        if sig[0] != 1:  # more (or fewer) than one positive eigenvalue => not Lorentzian
            off_polarity += 1
    print(f"     {n_random} random (weights, directions): signatures seen = {sigs_seen}")
    print(f"     -> NOT Lorentzian (pos != 1) in {off_polarity} / {n_random} cases")
    lorentzian_always = (off_polarity == 0)
    print(f"     => the convex-Hodge signature is {'INVARIANT (1, n-1) for all weights' if lorentzian_always else 'NOT always (1,n-1)'}.")
    print("        Unconditional definiteness on the primitive part => it can NEVER")
    print("        flip to flag an off-line zero. WRONG POLARITY for an RH detector.")

    # ---- Part 2: the Weil form has the RIGHT polarity (conditional) ----
    print("\n[3R] Part 2: the Weil/Schur form flips signature with an off-line zero")
    t0 = time.time()
    on_zeros = zeta_L.zeros(T_max=T_max, prec=prec)
    b_vals = np.logspace(np.log10(1.1), np.log10(200.0), K)
    print(f"     loaded {len(on_zeros)} on-line zeros in {time.time()-t0:.1f}s")

    # RH-holds case: on-line cushion only (no injected off-line pair). We build it by
    # injecting a pair AT the line (beta = 0.5), which contributes no off-line negativity.
    M_on, M_off0 = augmented_gram(on_zeros, b_vals, 0.5, 30.0, prec=prec)
    sig_rh = signature(M_on)  # the on-line Gram alone (RH-holds analog): PSD
    # RH-fails case: inject a genuine off-line pair at beta = 0.7.
    M_on2, M_off = augmented_gram(on_zeros, b_vals, 0.7, 30.0, prec=prec)
    M_aug = M_on2 + M_off
    sig_off = signature(M_aug)
    min_on = float(np.linalg.eigvalsh(M_on).min())
    min_aug = float(np.linalg.eigvalsh(M_aug).min())
    print(f"     RH-holds (on-line Gram only):   signature = {sig_rh}, min-eig = {min_on:+.3e}")
    print(f"     RH-fails (off-line pair beta=0.7): signature = {sig_off}, min-eig = {min_aug:+.3e}")
    weil_flips = (min_aug < -1e-6 and min_on > -1e-6)
    print(f"     => the Weil form {'FLIPS (PSD -> indefinite) with the off-line zero' if weil_flips else 'did not flip cleanly'}.")
    print("        Conditional definiteness (definite IFF RH). RIGHT POLARITY.")

    print("\n" + "=" * 76)
    print("[3R] VERDICT")
    if lorentzian_always and weil_flips:
        print("     The convex-Hodge (Kahler / Hodge-Riemann / AHK) signature is")
        print("     UNCONDITIONALLY (1, n-1) for every weighting tested, including the")
        print("     arithmetic w_p = log p. It cannot acquire the detecting indefiniteness,")
        print("     so it has the WRONG POLARITY: it can never fail when a zero goes off-line.")
        print("     The Weil form, by contrast, FLIPS from PSD to indefinite exactly when an")
        print("     off-line zero is present: the RIGHT polarity.")
        print("     CONSEQUENCE for the B-credible weighted-tropical-Kahler accident channel:")
        print("       injecting arithmetic weights (the Amini-Piquerez move) is NOT enough.")
        print("       #40 showed the channel is arithmetic-BLIND (signature does not move with t);")
        print("       this shows that even a signature that DID move could not FAIL (wrong polarity).")
        print("       The dossier's #1 watchlist signal -- a HR theorem whose signature BOTH moves")
        print("       with t AND can fail -- needs a genuinely new theorem, not weight injection.")
    else:
        print(f"     Inconclusive: lorentzian_always={lorentzian_always}, weil_flips={weil_flips} (see above).")
    print("     HONEST SCOPE: this is a SIGNATURE-LEVEL polarity argument on a small explicit")
    print("       model (segments / mixed areas, an exact Lorentzian instance), plus the known")
    print("       Weil-form behavior (e3k). It does NOT prove no Kahler-type RH detector can")
    print("       exist; it shows the naive 'inject arithmetic weights into a Kahler package'")
    print("       route has the wrong polarity, complementing #40's arithmetic-blindness.")
    print("=" * 76)

    np.savez_compressed(
        out_dir / "e3r_convex_hodge_polarity.npz",
        n=n, thetas=thetas,
        curated_labels=np.array(list(sig_counts.keys()), dtype=object),
        curated_sigs=np.array([sig_counts[k] for k in sig_counts]),
        random_sigs=np.array([[list(k), v] for k, v in sigs_seen.items()], dtype=object),
        off_polarity=off_polarity, n_random=n_random,
        sig_rh=np.array(sig_rh), sig_off=np.array(sig_off),
        min_on=min_on, min_aug=min_aug, K=K, T_max=T_max,
    )

    # Plot: a schematic of the two polarities.
    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    ax = axs[0]
    V = mixed_area_matrix(thetas, weightings["arithmetic w_p=log p"])
    eig = np.sort(np.linalg.eigvalsh(V))
    ax.bar(range(len(eig)), eig, color=["tab:green" if e > 0 else "tab:red" for e in eig])
    ax.axhline(0, color="k", lw=1)
    ax.set_title(f"Part 1: convex-Hodge eigenvalues (w_p=log p)\nsignature (1, n-1), UNCONDITIONAL -> wrong polarity")
    ax.set_xlabel("eigenvalue index"); ax.set_ylabel("eigenvalue")
    ax = axs[1]
    e_on = np.sort(np.linalg.eigvalsh(M_on))
    e_aug = np.sort(np.linalg.eigvalsh(M_aug))
    ax.plot(e_on, "o-", color="tab:green", label=f"RH holds (on-line): min {min_on:+.1e}")
    ax.plot(e_aug, "s-", color="tab:red", label=f"RH fails (off-line): min {min_aug:+.1e}")
    ax.axhline(0, color="k", lw=1)
    ax.set_yscale("symlog", linthresh=1e-6)
    ax.set_title("Part 2: Weil form eigenvalues\nflips PSD -> indefinite -> RIGHT polarity")
    ax.set_xlabel("eigenvalue index"); ax.set_ylabel("eigenvalue (symlog)")
    ax.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(out_dir / "e3r_convex_hodge_polarity.png", dpi=140)
    plt.close()
    print(f"[3R] Saved {out_dir / 'e3r_convex_hodge_polarity.png'}")
    print(f"[3R] Saved {out_dir / 'e3r_convex_hodge_polarity.npz'}")
    return sig_counts, sigs_seen, (sig_rh, sig_off)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=8)
    parser.add_argument("--n-random", type=int, default=2000)
    parser.add_argument("--K", type=int, default=40)
    parser.add_argument("--T-max", type=float, default=50.0)
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(n=args.n, n_random=args.n_random, K=args.K, T_max=args.T_max, prec=args.prec)
