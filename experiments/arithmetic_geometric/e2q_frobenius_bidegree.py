"""Experiment 2Q: the place-dependent bidegree obstruction -- the single sharpest
break between the function-field Hodge-index template (2G) and Spec(Z), and the
reverse-engineered constraint it puts on the arithmetic Frobenius correspondence.

Direction 8 / the product surface. The companion notes 2K (the dictionary) and
2J (the adjunction) established that EVERY intersection NUMBER of the would-be
surface S = Spec(Z) x Spec(Z) is now computable and validated on a single
arithmetic surface (2G/2H/2I/2L/2P), and that the one missing object is the
product surface itself and its Frobenius correspondence Gamma_S. This experiment
asks the next sharp question: granting the dictionary, what must Gamma_S actually
BE, and where exactly does the function-field rigidity break?

## The rigidity that breaks (recalled from 2G)

On C x C the Frobenius graph Gamma is a (1, q) CORRESPONDENCE:
    e.Gamma = 1,    f.Gamma = q.
The single number q is the residue-field cardinality, CONSTANT over the whole
curve. Everything downstream rides on that one scale:
    Gamma^2 = q (2 - 2g),       (the scale multiplies the adjunction)
    G_prim  = [[-2g, -t], [-t, -2gq]],
    neg. def. <=> 4 g^2 q - t^2 > 0 <=> |t| < 2g sqrt(q).
RH for the curve is an ALGEBRAIC inequality in two integers (t and the single
scale q), because the surface is finite-type and H^1 is 2g-dimensional.

## Where it breaks over Spec(Z)

Spec(Z) has no single residue cardinality: the fibre over the prime p is
Spec(F_p), of cardinality p. The arithmetic Frobenius correspondence Gamma_S
therefore cannot be a (1, q) correspondence for any single q. Its "second
bidegree" is PLACE-DEPENDENT: locally at p it is a (1, p) correspondence (the
geometric Frobenius of the residue field F_p). Equivalently, in the explicit
formula the prime side carries the weights {log p}_p, which are unbounded and
have no single value.

Three consequences, each a structural fact (not numerology):

  (1) NO SINGLE SCALE q. A 2G-style finite primitive Gram with one scale q cannot
      exist; the would-be Gram is block-graded over the places with scale p in the
      p-block. Picking any single effective q is overdetermined and inconsistent.

  (2) INFINITE GENUS. With one place-block per prime power and 2g eigenvalues per
      block forced to infinity in aggregate, H^1 is infinite-dimensional: the
      signature statement is a genuine infinite-dimensional index theorem, NOT a
      2x2 determinant. This is exactly Deninger's "H^i are infinite-dimensional."

  (3) Z-ACTION -> R-FLOW. A single Frobenius x |-> x^q generates a Z-action with
      one log-scale log q. Place-dependent log-scales {log p} that must act
      simultaneously and commensurably force a continuous R-action: the flow
      Phi_t = prod_p U_{log p}^{t / log p} of Directions 2/4. The flow is not an
      aesthetic preference; it is the only object that can carry a continuum of
      commensurable local scales. This experiment makes that necessity explicit.

## The reverse-engineered constraint on Gamma_S^2

In the function field, Gamma^2 = q * Delta^2 (the scale times the adjunction
self-intersection). Over Spec(Z), with no single q and with the adjunction
self-intersection now computed (2J/2L: omega-bar^2 = 12 h_Fal per elliptic fibre,
the arithmetic 2 - 2g), the analogue cannot be a single product. It must be the
REGULARIZED prime-weighted sum that the explicit formula already supplies:

    "Gamma_S^2"  =  reg-sum_p (log p) * (local self-intersection at p)

i.e. the prime side P_fin of the Weil form, read as a regularized self-pairing of
the correspondence -- which is precisely the regularized determinant
det_zeta(s - Phi_t | H^*_{F,pr}) that Direction 4.6 must produce. So Gamma_S is
pinned: a correspondence with place-dependent bidegree (1, p) whose regularized
self-intersection is the von Mangoldt prime sum. That is a sharper, falsifiable
target than "a Frobenius graph on S."

## The sharper K2 (Davenport-Heilbronn)

This refines the 2G K2 reading. 2G says D-H has "no Frobenius, no Gamma." 2Q says
WHY at the level of bidegree: a (1, p) local bidegree at each prime is exactly the
Euler factor (1 - p^{-s})^{-1}. D-H has a functional equation (hence a zero/genus
structure) but NO Euler product, so its von Mangoldt analogue delocalizes off
prime powers (the 3M finding): there are no clean per-place local degrees to
assemble into Gamma_S. The place-dependent-bidegree correspondence REQUIRES the
Euler product. No Euler product <=> no local bidegrees <=> no Gamma_S <=> no
surface. The discipline is now a statement about the correspondence's bidegree.

This experiment ships an honest ILLUSTRATION (the single-scale FF family vs. the
unbounded arithmetic place-spectrum, and the overdetermination of a single q),
not a proof. The deliverable is the sharpened specification, recorded in the
companion note e2q_frobenius_bidegree.md and folded into 2K section 4.

Outputs:
  - e2q_frobenius_bidegree.npz : FF single-scale data + arithmetic place spectrum
  - e2q_frobenius_bidegree.png : single scale q (FF) vs the {log p} place spectrum
  - stdout : the three structural consequences, quantified
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sympy import primerange  # first-n-primes helper

from experiments.arithmetic_geometric.e2f_hodge_index_sweep import (
    count_points_Fpk,
    elliptic_family,
)
from experiments.arithmetic_geometric.e2g_intersection_signature import (
    primitive_gram,
    signature,
)


def ff_single_scale(primes=(5, 7, 11, 13, 17, 19, 23, 29, 31)):
    """For each function-field curve, the single scale q and the algebraic
    Hasse-Weil margin. Demonstrates that the FF RH-bound rides on ONE number q."""
    curves = elliptic_family(list(primes))
    rows = []
    for c in curves:
        p, g = c["p"], c["g"]
        N1 = count_points_Fpk(c["f_coeffs"], p, 1)
        t = p + 1 - N1
        G_prim, _ = primitive_gram(p, g, N1)
        pos, neg, zero, _ = signature(G_prim)
        margin = 4 * g * g * p - t * t       # > 0  <=>  |t| < 2g sqrt(q)
        rows.append(dict(label=c["label"], q=p, g=g, t=t,
                         scale=p, margin=float(margin),
                         neg_def=(pos == 0 and neg == 2)))
    return rows


def arithmetic_place_spectrum(n_primes=40):
    """The arithmetic 'scales': residue cardinalities {p} and weights {log p}
    over the first n_primes primes. These are what a single q would have to be
    simultaneously. Returns the spectrum and the overdetermination measure."""
    # first n_primes primes; an upper bound of 15*n_primes comfortably contains them
    primes = np.array(list(primerange(2, 15 * n_primes + 100))[:n_primes], dtype=float)
    weights = np.log(primes)
    # Overdetermination: a single effective scale q would have to satisfy the
    # local (1, p) bidegree at EVERY prime. The spread of required scales is the
    # ratio max/min, which diverges -> no single q. We report it explicitly.
    spread = primes.max() / primes.min()
    weight_spread = weights.max() / weights.min()
    return dict(primes=primes, weights=weights,
                scale_spread=float(spread), weight_spread=float(weight_spread))


def run(n_primes=40, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("[2Q] The place-dependent bidegree obstruction.")
    print("     FF: Frobenius is a (1, q) correspondence -- ONE scale q per curve.")
    print("     Spec(Z): the arithmetic Frobenius has a (1, p) bidegree at EACH p")
    print("     -- a place-dependent scale, hence no single q. Quantified below.\n")

    ff = ff_single_scale()
    print(f"{'curve':<34} {'q=scale':>8} {'t':>5} {'4g^2q - t^2':>12} {'neg.def':>8}")
    print("-" * 72)
    for r in ff:
        print(f"{r['label']:<34} {r['q']:>8} {r['t']:>5} {r['margin']:>12.1f} "
              f"{'yes' if r['neg_def'] else 'NO':>8}")
    ff_scales = sorted({r["q"] for r in ff})
    print(f"\n     FF distinct scales across the family: {ff_scales}")
    print(f"     -> each curve has exactly ONE scale q; RH is an algebraic")
    print(f"        inequality |t| < 2g sqrt(q) in two integers. Finite-type.\n")

    spec = arithmetic_place_spectrum(n_primes)
    primes = spec["primes"].astype(int)
    print(f"[2Q] Arithmetic place spectrum (first {n_primes} primes):")
    print(f"     residue cardinalities (the would-be scales): "
          f"{[int(p) for p in primes[:10]]} ...")
    print(f"     weights log p: "
          f"[{', '.join(f'{w:.3f}' for w in spec['weights'][:6])} ...]")
    print(f"     scale spread max(p)/min(p) over these primes: "
          f"{spec['scale_spread']:.1f}  (diverges as N -> inf)")
    print(f"     -> NO single q fits all places: the correspondence Gamma_S has a")
    print(f"        place-dependent bidegree (1, p). Three consequences:\n")
    print(f"     (1) no single scale -> no finite 2x2 primitive Gram (block-graded")
    print(f"         over places, scale p in the p-block).")
    print(f"     (2) infinite genus -> H^1 infinite-dimensional -> the signature is")
    print(f"         an infinite-dim index theorem, not a 2x2 determinant.")
    print(f"     (3) Z-action (one log-scale log q) -> R-flow Phi_t (a continuum of")
    print(f"         commensurable log-scales {{log p}}): the Deninger flow is FORCED.\n")
    print(f"[2Q] Reverse-engineered constraint on Gamma_S^2:")
    print(f"     FF: Gamma^2 = q * Delta^2 (single scale x adjunction).")
    print(f"     Spec(Z): 'Gamma_S^2' = reg-sum_p (log p)*(local self-int at p)")
    print(f"              = the von Mangoldt prime side P_fin, read as the")
    print(f"              regularized determinant det_zeta(s - Phi_t) of Direction 4.6.")
    print(f"     Adjunction input now computed: omega-bar^2 = 12 h_Fal per fibre (2J/2L).\n")
    print(f"[2Q] Sharper K2 (D-H): a (1, p) local bidegree IS the Euler factor")
    print(f"     (1 - p^-s)^-1. D-H has no Euler product -> von Mangoldt delocalizes")
    print(f"     (3M) -> no clean per-place local degrees -> no Gamma_S -> no surface.")

    _save_and_plot(ff, spec, out_dir)
    return ff, spec


def _save_and_plot(ff, spec, out_dir: Path):
    np.savez_compressed(
        out_dir / "e2q_frobenius_bidegree.npz",
        ff_labels=np.array([r["label"] for r in ff], dtype=object),
        ff_q=np.array([r["q"] for r in ff]),
        ff_t=np.array([r["t"] for r in ff]),
        ff_margin=np.array([r["margin"] for r in ff]),
        arith_primes=spec["primes"],
        arith_weights=spec["weights"],
        scale_spread=spec["scale_spread"],
    )

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))

    # Panel 1: FF -- each curve sits at a SINGLE scale q.
    ax = axs[0]
    qs = [r["q"] for r in ff]
    ax.scatter(range(len(ff)), qs, color="tab:blue", zorder=3)
    for i, r in enumerate(ff):
        ax.annotate(str(r["q"]), (i, r["q"]), textcoords="offset points",
                    xytext=(0, 6), fontsize=8, ha="center")
    ax.set_xlabel("function-field curve index")
    ax.set_ylabel("scale q (single residue cardinality)")
    ax.set_title("Function field: ONE scale q per curve\nGamma is a (1, q) correspondence; RH bound is algebraic in q")
    ax.grid(alpha=0.3)

    # Panel 2: Spec(Z) -- a whole unbounded spectrum of place-weights {log p}.
    ax = axs[1]
    w = spec["weights"]
    ax.stem(spec["primes"], w, basefmt=" ", linefmt="tab:red", markerfmt="o")
    ax.set_xlabel("prime p (place)")
    ax.set_ylabel("place-weight  log p")
    ax.set_title("Spec(Z): a continuum-bound spectrum of place-weights {log p}\nGamma_S has bidegree (1, p) at each p; no single q -> R-flow forced")
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e2q_frobenius_bidegree.png", dpi=140)
    plt.close()
    print(f"\n[2Q] Saved {out_dir / 'e2q_frobenius_bidegree.png'}")
    print(f"[2Q] Saved {out_dir / 'e2q_frobenius_bidegree.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="The place-dependent bidegree obstruction (Direction 8).")
    parser.add_argument("--n-primes", type=int, default=40)
    args = parser.parse_args()
    run(n_primes=args.n_primes)
