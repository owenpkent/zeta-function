"""Experiment 2R: the Ruelle dynamical-zeta realization of `Gamma_S^2`.

Direction 8 / the product surface; continues 2Q. 2Q pinned the missing arithmetic
Frobenius correspondence `Gamma_S` to a place-dependent bidegree `(1, p)` per prime
and pinned its regularized self-intersection to

    "Gamma_S^2"  =  reg-sum_p (log p) * (local self-int at p)  =  the von Mangoldt
                    prime side  =  the Direction 4.6 determinant det_zeta(s - Phi_t).

That was an abstract specification. 2R makes it CONCRETE on the dynamical side: it
exhibits the closed-orbit / Ruelle dynamical-zeta object whose data is exactly
`Gamma_S^2`, and confirms the Davenport-Heilbronn control has no such object.

## The dynamical picture (Deninger; the Morishita closed-orbits <-> primes bridge)

In Deninger's program (and the Morishita bridge, arXiv:2508.15971, which matches
closed orbits to primes), the arithmetic flow `Phi_t` has primitive closed orbits
`gamma_p`, one per prime, of LENGTH `l(gamma_p) = log p`. These lengths are exactly
2Q's place-weights `{log p}`. The Ruelle dynamical zeta of such a flow is

    zeta_Ruelle(s) = prod_p (1 - e^{-s l(gamma_p)})^{-1} = prod_p (1 - p^{-s})^{-1}
                   = zeta(s)        (Re s > 1, the Euler product),

and its logarithmic derivative is the flow's regularized self-pairing (the
Lefschetz / "Gamma_S^2" object):

    -zeta'/zeta(s) = sum_p sum_{k>=1} (log p) p^{-ks} = sum_n Lambda(n) n^{-s}.

So the abstract `Gamma_S^2 = reg-sum_p (log p)(...)` of 2Q IS `-zeta'/zeta`, realized
as the log-derivative of a dynamical zeta whose primitive-orbit-length spectrum is
`{log p}`. The local factor at `p` (orbit length `log p`) is the Euler factor
`(1 - p^{-s})^{-1}` -- the geometric content of 2Q's `(1, p)` bidegree.

## What 2R verifies (and what it is NOT)

It VERIFIES, numerically:
  (1) the dynamical-zeta product over primes (orbit lengths `log p`) reproduces
      `zeta(s)` (Euler product convergence);
  (2) `-zeta'/zeta(s) = sum_n Lambda(n) n^{-s}` (the `Gamma_S^2` realization), i.e.
      the flow's self-pairing equals the prime side, to high precision;
  (3) the D-H control: `-L_DH'/L_DH(s) = sum_n Lambda_DH(n) n^{-s}` has `Lambda_DH`
      DELOCALIZED off prime powers (no Euler product), so D-H has NO primitive-orbit
      length spectrum `{log p}` -- the dynamical flow / dynamical-zeta representation
      does not exist for D-H. This is the dynamical-language form of the sharper K2
      (2Q) and the 3M delocalization finding (#20).

It is NOT a new route to RH. Items (1)-(2) are classical identities; the NEW content
is the structural identification -- orbit-length spectrum `= {log p} =` 2Q's
place-weights `=` the realized `Gamma_S^2` -- and the D-H non-existence. 2R makes
`Gamma_S^2` a concrete dynamical object (the half of the Morishita bridge that
Deninger supplies); it does NOT build the product surface or its index theorem.

Outputs:
  - e2r_dynamical_zeta.npz : convergence data + zeta/D-H von Mangoldt supports
  - e2r_dynamical_zeta.png : Euler-product + (-z'/z) convergence; zeta vs D-H support
  - stdout : the three verifications, quantified
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
from sympy import primerange

from experiments._shared import zeta_L, DavenportHeilbronn
from experiments.positivity.e3m_place_type_balance import (
    von_mangoldt_zeta,
    lambda_coeffs_from_dirichlet,
)


def is_prime_power(n: int) -> bool:
    """True iff n = p^k for a prime p and k >= 1."""
    if n < 2:
        return False
    m, p = n, 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            return m == 1
        p += 1
    return True  # m itself prime


def euler_product_convergence(s, cutoffs, prec: int):
    """Truncated dynamical-zeta product prod_{p <= P} (1 - p^{-s})^{-1} (orbit
    lengths log p) vs zeta(s). Returns |product - zeta(s)| per cutoff."""
    mp.mp.dps = prec
    s = mp.mpc(s)
    target = mp.zeta(s)
    errs = []
    for P in cutoffs:
        prod = mp.mpf(1)
        for p in primerange(2, P + 1):
            prod *= 1 / (1 - mp.mpf(p) ** (-s))
        errs.append(float(abs(prod - target)))
    return float(abs(target)), errs


def vonmangoldt_convergence(s, n_maxes, prec: int):
    """Truncated sum_{n <= N} Lambda(n) n^{-s} (the Gamma_S^2 realization) vs the
    exact -zeta'/zeta(s). Returns |sum - (-z'/z)| per cutoff."""
    mp.mp.dps = prec
    s = mp.mpc(s)
    # -zeta'/zeta(s): mp.zeta(s, 1, 1) is the first s-derivative of zeta.
    exact = -mp.zeta(s, 1, 1) / mp.zeta(s)
    errs = []
    for N in n_maxes:
        acc = mp.mpf(0)
        for n in range(2, N + 1):
            lam = von_mangoldt_zeta(n)
            if lam != 0.0:
                acc += mp.mpf(lam) * mp.mpf(n) ** (-s)
        errs.append(float(abs(acc - exact)))
    return complex(exact), errs


def dh_delocalization(n_max: int, prec: int):
    """Lambda_DH(n) for Davenport-Heilbronn. Returns (lam, off_pp_mass, first_off_pp,
    on_pp_mass): how much of the log-derivative coefficient mass sits OFF prime
    powers (the missing-Euler-product fingerprint => no closed-orbit spectrum)."""
    dh = DavenportHeilbronn()
    lam = lambda_coeffs_from_dirichlet(dh, n_max, prec)
    off_pp_mass = 0.0
    on_pp_mass = 0.0
    first_off_pp = None
    for n in range(2, n_max + 1):
        if is_prime_power(n):
            on_pp_mass += abs(lam[n])
        else:
            off_pp_mass += abs(lam[n])
            if first_off_pp is None and abs(lam[n]) > 1e-9:
                first_off_pp = n
    return lam, off_pp_mass, first_off_pp, on_pp_mass


def run(prec: int = 30, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("[2R] Ruelle dynamical-zeta realization of Gamma_S^2.")
    print("     Primitive closed-orbit lengths l(gamma_p) = log p (the 2Q place-weights);")
    print("     zeta_Ruelle(s) = prod_p (1 - p^-s)^-1 = zeta(s); -zeta'/zeta = sum_n Lambda(n) n^-s.\n")

    # (1) Euler product (orbit lengths log p) -> zeta
    s1 = mp.mpc(2, 0)
    cutoffs = [10, 50, 200, 1000, 5000]
    ztgt, eprod_errs = euler_product_convergence(s1, cutoffs, prec)
    print(f"(1) Dynamical-zeta product vs zeta at s={complex(s1)} (|zeta|={ztgt:.6f}):")
    for P, e in zip(cutoffs, eprod_errs):
        print(f"      primes <= {P:>5}:  |prod - zeta| = {e:.3e}")
    print(f"    => orbit-length spectrum {{log p}} reproduces zeta via the Euler product.\n")

    # (2) von Mangoldt sum (Gamma_S^2) -> -zeta'/zeta
    s2 = mp.mpc(2, 0)
    n_maxes = [10, 50, 200, 1000, 5000]
    exact, vm_errs = vonmangoldt_convergence(s2, n_maxes, prec)
    print(f"(2) Gamma_S^2 realization: sum_n Lambda(n) n^-s vs -zeta'/zeta at s={complex(s2)}")
    print(f"    exact -zeta'/zeta(s) = {exact:.8f}:")
    for N, e in zip(n_maxes, vm_errs):
        print(f"      n <= {N:>5}:  |sum - (-z'/z)| = {e:.3e}")
    print(f"    => the flow's regularized self-pairing IS the prime side = Gamma_S^2 (2Q).\n")

    # (3) D-H control: no closed-orbit spectrum (Lambda_DH delocalizes)
    n_max = 60
    lam_dh, off_mass, first_off, on_mass = dh_delocalization(n_max, prec)
    lam_zeta = np.array([von_mangoldt_zeta(n) for n in range(n_max + 1)])
    print(f"(3) D-H control (Lambda_DH from -L_DH'/L_DH, n <= {n_max}):")
    print(f"      on  prime powers: total |Lambda_DH| = {on_mass:.4f}")
    print(f"      off prime powers: total |Lambda_DH| = {off_mass:.4f}  "
          f"(first nonzero off-pp at n = {first_off})")
    print(f"    => D-H delocalizes off prime powers (no Euler product), so there is NO")
    print(f"       primitive-orbit-length spectrum {{log p}}: the dynamical flow /")
    print(f"       dynamical-zeta representation does NOT exist for D-H. Dynamical K2.\n")
    print(f"[2R] Net: Gamma_S^2 (2Q) is realized as the log-derivative of a dynamical")
    print(f"     zeta with orbit lengths {{log p}}; D-H has no such object. This makes")
    print(f"     the Deninger half of the Morishita bridge concrete. NOT a new RH route.")

    _save_and_plot(cutoffs, eprod_errs, n_maxes, vm_errs,
                   lam_zeta, lam_dh, n_max, out_dir)
    return dict(eprod_errs=eprod_errs, vm_errs=vm_errs,
                off_mass=off_mass, on_mass=on_mass, first_off=first_off)


def _save_and_plot(cutoffs, eprod_errs, n_maxes, vm_errs,
                   lam_zeta, lam_dh, n_max, out_dir: Path):
    np.savez_compressed(
        out_dir / "e2r_dynamical_zeta.npz",
        cutoffs=np.array(cutoffs), eprod_errs=np.array(eprod_errs),
        n_maxes=np.array(n_maxes), vm_errs=np.array(vm_errs),
        lam_zeta=lam_zeta, lam_dh=lam_dh, n_max=n_max,
    )

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))

    # Panel 1: both realizations converge.
    ax = axs[0]
    ax.loglog(cutoffs, eprod_errs, "o-", color="tab:blue",
              label=r"$|\prod_{p\leq P}(1-p^{-s})^{-1} - \zeta(s)|$ (orbit lengths $\log p$)")
    ax.loglog(n_maxes, vm_errs, "s-", color="tab:green",
              label=r"$|\sum_{n\leq N}\Lambda(n)n^{-s} - (-\zeta'/\zeta)|$ ($\Gamma_S^2$)")
    ax.set_xlabel(r"cutoff (primes $\leq P$ / terms $\leq N$)")
    ax.set_ylabel("error at $s = 2$")
    ax.set_title("Dynamical-zeta realization converges\n(orbit lengths $\\{\\log p\\}$ → $\\zeta$; self-pairing → prime side)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, which="both")

    # Panel 2: zeta supported on prime powers; D-H delocalized.
    ax = axs[1]
    ns = np.arange(2, n_max + 1)
    pp_mask = np.array([is_prime_power(int(n)) for n in ns])
    ax.bar(ns[pp_mask], np.abs(lam_zeta[2:][pp_mask]), width=0.8,
           color="tab:blue", label=r"$|\Lambda_\zeta|$ (prime powers only)")
    ax.bar(ns[~pp_mask], np.abs(lam_dh[2:][~pp_mask]), width=0.8,
           color="tab:red", label=r"$|\Lambda_{\rm DH}|$ off prime powers (delocalized)")
    ax.set_xlabel("n")
    ax.set_ylabel(r"$|\Lambda(n)|$ (log-derivative coefficient)")
    ax.set_title("Closed-orbit spectrum exists iff Euler product\n($\\zeta$: clean $\\{\\log p\\}$; D-H: mass off prime powers → no flow)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig(out_dir / "e2r_dynamical_zeta.png", dpi=140)
    plt.close()
    print(f"\n[2R] Saved {out_dir / 'e2r_dynamical_zeta.png'}")
    print(f"[2R] Saved {out_dir / 'e2r_dynamical_zeta.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ruelle dynamical-zeta realization of Gamma_S^2 (Direction 8).")
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(prec=args.prec)
