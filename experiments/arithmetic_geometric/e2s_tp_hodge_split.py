"""Experiment 2S: the TP odd/even split IS the Weil Hodge-index split, and RH is
the signature on TP_odd. Pivot to the signature (Direction 8 / form 10A.iii),
informed by the THH/Hesselholt lens from the 2026-05-30 survey (LEARNINGS #29).

CONTEXT. The session's cross-direction synthesis (docs/03_research/
all_roads_to_the_signature.md) found that every framework supplies the
REALIZATION of zeta (a determinant/trace) but RH is the SIGNATURE/positivity,
the same object everywhere. Hesselholt's theorem over F_q gives
    zeta(C,s) = det_inf(s - Theta | TP_odd) / det_inf(s - Theta | TP_even),
with Theta the Frobenius-flow generator on the S^1-Tate periodic TP and
q^Theta = Fr^*. This experiment shows that Hesselholt's odd/even TP split is
EXACTLY the primitive/hyperbolic split of Weil's Hodge index (2G), and that the
three faces of RH for a curve coincide:

    (Hodge index, 2G)   primitive intersection form on H^1 negative definite
      <=>  (eigenvalues) |alpha_i| = sqrt(q) for Frobenius on H^1
      <=>  (Hesselholt)  the zeros of det_inf(s - Theta | TP_odd), at
                         s = log_q(alpha_i), have Re(s) = 1/2.

TP DICTIONARY (function-field case, g = genus):
    TP_even(C) ~ H^0 + H^2 : Frobenius eigenvalues 1 and q. The hyperbolic plane
                 {e, f} of 2G. Signature (1,1). This is the DENOMINATOR of
                 Hesselholt's ratio (poles of zeta at s=0,1).
    TP_odd(C)  ~ H^1       : Frobenius eigenvalues {alpha_i}, 2g of them. The
                 primitive part {Delta_0, Gamma_0, ...} of 2G. Signature (0,2g),
                 negative definite <=> RH. The NUMERATOR (the zeros).

So "RH = a definite cup-product signature on TP_odd" is, in the function-field
case, literally 2G's negative-definite primitive Gram. This experiment verifies
the triple equivalence across the curve family (the K3 / Weil-specialization
check for the TP lens) and states precisely the Spec(Z) target.

THE Spec(Z) TARGET (open). Over Z, TP_odd is infinite-dimensional (the H^1 of
LEARNINGS #25, one place-block per prime, forced by the (1,p) bidegree), and RH
is the negative-definiteness of the cup-product pairing on its primitive part.
That is Direction 8's Hodge index and form 10A.iii, now seen as one object. No
realization theorem (Connes, Deninger, Hesselholt, Morin) produces this
signature; it is the irreducible content.

Outputs:
  - e2s_tp_hodge_split.npz
  - e2s_tp_hodge_split.png
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from experiments.arithmetic_geometric.e2g_intersection_signature import (
    full_gram, primitive_gram, signature,
)
from experiments.arithmetic_geometric.e2f_hodge_index_sweep import (
    count_points_Fpk, elliptic_family, genus2_family,
)


def frobenius_h1_eigenvalues(q: int, g: int, N1: int, curve=None):
    """Frobenius eigenvalues on H^1 (the TP_odd eigenvalues).

    For g=1: characteristic poly X^2 - t X + q, t = q+1-N1, roots
    (t +/- sqrt(t^2-4q))/2. For g>=2 we need N_1..N_g; if `curve` is given we
    compute them and form the zeta numerator polynomial, else we return None.
    """
    if g == 1:
        t = q + 1 - N1
        disc = complex(t * t - 4 * q)
        r = np.sqrt(disc)
        return np.array([(t + r) / 2, (t - r) / 2])
    if curve is not None:
        # L-poly from N_1..N_g via Newton's identities on power sums of alpha_i.
        # P(T) = prod (1 - alpha_i T), with sum alpha_i^k = q^k + 1 - N_k.
        f_coeffs, p = curve["f_coeffs"], curve["p"]
        power_sums = []
        for k in range(1, g + 1):
            Nk = count_points_Fpk(f_coeffs, p, k)
            power_sums.append(q ** k + 1 - Nk)  # sum_i (alpha_i^k + conj) = trace on H^1
        # Newton: e_k from p_k. We have 2g eigenvalues; build the full L-poly of
        # degree 2g using the functional equation alpha <-> q/alpha.
        # Coeffs c_0..c_g of P(T) = sum c_j T^j, c_0=1; c_k = -(1/k) sum_{j=1}^k p_j c_{k-j}.
        c = [1.0]
        for k in range(1, g + 1):
            ck = -sum(power_sums[j - 1] * c[k - j] for j in range(1, k + 1)) / k
            c.append(ck)
        # full degree-2g poly by functional equation: c_{2g-j} = q^{g-j} c_j
        full = [0.0] * (2 * g + 1)
        for j in range(g + 1):
            full[j] = c[j]
        for j in range(g):
            full[2 * g - j] = (q ** (g - j)) * c[j]
        # roots of sum full[j] T^j (these are 1/alpha_i); invert
        coeffs_desc = np.array(full[::-1], dtype=complex)
        roots = np.roots(coeffs_desc)  # = 1/alpha_i
        alphas = 1.0 / roots
        return alphas
    return None


def theta_eigenvalues(alphas, q):
    """Hesselholt Theta on the alpha-eigenspace: q^Theta = Fr^* => Theta = log_q(alpha).

    The zeros of det_inf(s - Theta | TP_odd) sit at s = log_q(alpha_i).
    RH for C <=> all have Re(s) = 1/2 <=> |alpha_i| = sqrt(q).
    """
    return np.log(alphas) / np.log(q)


def analyze(curve):
    p, g, f_coeffs = curve["p"], curve["g"], curve["f_coeffs"]
    N1 = count_points_Fpk(f_coeffs, p, 1)
    t = p + 1 - N1

    G_prim, _ = primitive_gram(p, g, N1)
    sig_prim = signature(G_prim)
    prim_neg_def = (sig_prim[0] == 0 and sig_prim[1] == G_prim.shape[0])

    alphas = frobenius_h1_eigenvalues(p, g, N1, curve=curve)
    abs_alpha = np.abs(alphas)
    rh_eig = bool(np.all(np.abs(abs_alpha - np.sqrt(p)) < 1e-6 * np.sqrt(p)))

    thetas = theta_eigenvalues(alphas, p)
    re_theta = thetas.real
    rh_zeros = bool(np.all(np.abs(re_theta - 0.5) < 1e-6))

    return dict(label=curve["label"], p=p, g=g, N1=N1, t=t,
                sig_prim=sig_prim[:3], prim_neg_def=prim_neg_def,
                abs_alpha=abs_alpha, sqrt_q=float(np.sqrt(p)), rh_eig=rh_eig,
                re_theta=re_theta, rh_zeros=rh_zeros,
                triple_agree=(prim_neg_def == rh_eig == rh_zeros))


def run(full=False, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    primes_e = (5, 7, 11, 13, 17, 19, 23, 29, 31) if full else (5, 7, 11, 13)
    primes_g2 = (5, 7, 11, 13) if full else (5, 7, 11)
    curves = elliptic_family(list(primes_e)) + genus2_family(list(primes_g2))

    print("[2S] TP odd/even split = Weil Hodge-index split; RH = signature on TP_odd.")
    print("     Triple equivalence per curve:")
    print("       primitive cup-form on H^1 (=TP_odd) negative definite")
    print("        <=> |Frobenius eigenvalues on H^1| = sqrt(q)")
    print("        <=> zeros of det_inf(s-Theta|TP_odd) at s=log_q(alpha) have Re=1/2.\n")
    header = (f"{'curve':<34} {'g':>2} {'q':>3} {'t':>5} {'sig(TP_odd)':>12} "
              f"{'|a|=sqrt q':>10} {'Re(zeros)=1/2':>13} {'agree':>6}")
    print(header); print("-" * len(header))

    results = []
    all_agree = True
    for curve in curves:
        r = analyze(curve)
        results.append(r)
        all_agree = all_agree and r["triple_agree"]
        sp = f"(0,{r['sig_prim'][1]})" if r["prim_neg_def"] else f"({r['sig_prim'][0]},{r['sig_prim'][1]})"
        print(f"{r['label']:<34} {r['g']:>2} {r['p']:>3} {r['t']:>5} {sp:>12} "
              f"{'yes' if r['rh_eig'] else 'NO':>10} {'yes' if r['rh_zeros'] else 'NO':>13} "
              f"{'OK' if r['triple_agree'] else 'X':>6}")

    print("-" * len(header))
    print(f"\n[2S] TP_odd (= primitive H^1) negative definite for all curves: "
          f"{all(r['prim_neg_def'] for r in results)}")
    print(f"     |alpha_i| = sqrt(q) on H^1 for all curves: {all(r['rh_eig'] for r in results)}")
    print(f"     Hesselholt zeros Re(s)=1/2 for all curves: {all(r['rh_zeros'] for r in results)}")
    print(f"     TRIPLE EQUIVALENCE holds across the family (K3 / Weil-spec for the TP lens): {all_agree}")
    print("     (Note: for g>=2 the sig(TP_odd) column is the 2-dim 2G primitive slice")
    print("      {Delta_0,Gamma_0}; the full TP_odd=H^1 is 2g-dim with signature (0,2g). The")
    print("      |alpha|=sqrt(q) and Re=1/2 checks use the FULL 2g-dim H^1, so they are the")
    print("      honest full-dimensional witnesses; the slice is a negative-definite witness.)")
    print("\n[2S] CONCLUSION. Hesselholt's TP_odd/TP_even split is the Weil Hodge-index")
    print("     primitive/hyperbolic split, and RH for the curve is the negative-definite")
    print("     SIGNATURE on TP_odd, identically the 2G primitive Gram. The Spec(Z) target")
    print("     (form 10A.iii = Direction 8): TP_odd over Z is infinite-dimensional (#25),")
    print("     and RH = its cup-product pairing negative definite on the primitive part.")
    print("     No realization theorem produces this; it is the irreducible content.")

    np.savez_compressed(
        out_dir / "e2s_tp_hodge_split.npz",
        labels=np.array([r["label"] for r in results], dtype=object),
        all_agree=all_agree,
        **{f"abs_alpha_{i}": r["abs_alpha"] for i, r in enumerate(results)},
        **{f"re_theta_{i}": r["re_theta"] for i, r in enumerate(results)},
        **{f"sqrtq_{i}": r["sqrt_q"] for i, r in enumerate(results)},
    )

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))

    ax = axs[0]
    for i, r in enumerate(results):
        ax.scatter([i] * len(r["abs_alpha"]), r["abs_alpha"], color="tab:blue", zorder=3)
        ax.scatter([i], [r["sqrt_q"]], color="tab:red", marker="_", s=200, zorder=2)
    ax.set_xlabel("curve index")
    ax.set_ylabel(r"$|\alpha_i|$ on $H^1$ = TP$_{\rm odd}$  (red = $\sqrt{q}$)")
    ax.set_title("Frobenius eigenvalues on TP_odd lie on |a|=sqrt(q)\n(= primitive cup-form negative definite = RH)")
    ax.grid(alpha=0.3)

    ax = axs[1]
    for i, r in enumerate(results):
        ax.scatter(r["re_theta"], [i] * len(r["re_theta"]), color="tab:green", zorder=3)
    ax.axvline(0.5, color="r", ls="--", lw=1, label="Re(s) = 1/2")
    ax.set_xlabel(r"Re$(s)$ of zeros of $\det_\infty(s-\Theta\,|\,$TP$_{\rm odd})$")
    ax.set_ylabel("curve index")
    ax.set_title("Hesselholt zeros at s = log_q(alpha) sit on Re=1/2\n(the critical line, via the TP lens)")
    ax.legend(); ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e2s_tp_hodge_split.png", dpi=140)
    plt.close()
    print(f"\n[2S] Saved {out_dir / 'e2s_tp_hodge_split.png'}")
    print(f"[2S] Saved {out_dir / 'e2s_tp_hodge_split.npz'}")
    return results, all_agree


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--full", action="store_true")
    args = parser.parse_args()
    run(full=args.full)
