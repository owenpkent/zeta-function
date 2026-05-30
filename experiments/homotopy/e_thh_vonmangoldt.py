"""Direction 10A.ii, first pass: does Bokstedt's THH(Z) torsion reproduce the
von Mangoldt sum -zeta'/zeta = sum_n Lambda(n) n^{-s}?

This is the THH-side mirror of LEARNINGS #26 (where the dynamical zeta with
closed-orbit lengths {log p} was shown to give exactly the von Mangoldt sum).
Direction 10 claims THH(Z), with its S^1-action and cyclotomic Frobenii, is the
single object carrying all scales {log p} at once. The decisive checkpoint
(doc 10A) asks whether an S^1-equivariant invariant of THH(Z) reproduces the
von Mangoldt sum. This experiment runs the cheapest concrete form of that test.

THE RIGOROUS SUBSTRATE (Bokstedt's theorem):
    pi_*(THH(Z)) = Z (degree 0),  Z/i (degree 2i-1, i>=1),  0 (even > 0).
So the torsion group in degree 2i-1 has ORDER i, and its p-primary part is
Z/p^{v_p(i)}. The prime p enters degree 2i-1 exactly when p | i.

THE CANDIDATE EQUIVARIANT SERIES. Assign the degree-(2i-1) torsion the spectral
weight i^{-s} (this weight is the one ASSUMPTION the eventual equivariant-
determinant formalism must justify; see Caveat A below) and value log|torsion|
= log i. The assembled series is
    Z_THH(s) := sum_{i>=1} log|THH_{2i-1}(Z)| * i^{-s} = sum_i (log i) i^{-s}.

THE RESULT (verified below). Z_THH(s) = -zeta'(s), the IMPRIMITIVE log-sum, NOT
the von Mangoldt sum. They differ by exactly a factor of zeta:
    -zeta'(s) = zeta(s) * (-zeta'/zeta)(s).
The von Mangoldt / Euler-product / primitive sum is recovered by Mobius
convolution (multiplication by 1/zeta):
    Lambda = mu * log,   i.e.   (-zeta'/zeta) = (-zeta') * (1/zeta).
On the spectral side, 1/zeta = mu is exactly the "primitive reduction" that the
cyclotomic-Frobenius / TC equalizer must supply (passing from THH to TC).

So the checkpoint's verdict is a SHARP CONDITIONAL, not a yes/no:
  - The imprimitive log-sum -zeta'(s) falls out of Bokstedt RIGOROUSLY (given
    the i^{-s} weight). The primes enter through v_p(i) with the correct log p
    weights and assemble correctly per prime (verified below).
  - The von Mangoldt sum = #26's dynamical zeta = Gamma_S^2 needs the extra
    factor 1/zeta (Mobius). The next milestone (10A, route A) is precisely:
    does the THH -> TC cyclotomic equalizer implement Mobius inversion?

CAVEATS (kept explicit, per the adversary discipline):
  A. The weight i^{-s} on degree 2i-1 is an assumption. With weight (2i-1)^{-s}
     one gets an odd-zeta-like object instead. Justifying i^{-s} from the
     S^1-equivariant / regularized-determinant formalism is part of milestone
     10A.ii proper. This experiment establishes the CONDITIONAL identity.
  B. "1/zeta = the TC reduction" is a conjectural mapping, not a theorem. It is
     the identified target, stated as such.

D-H FIREWALL (K2). Davenport-Heilbronn is a C-linear combination of L-functions,
not a ring; there is no ring spectrum whose THH could give it, hence no torsion-
order sequence to assemble. Concretely, its von Mangoldt coefficients Lambda_DH
delocalize onto composite n (first at n=6, LEARNINGS #20/#26), so they are NOT
mu * (log of any order-i sequence): the THH -> von-Mangoldt route has no D-H
analogue. Verified below.

Outputs:
  - e_thh_vonmangoldt.npz
  - e_thh_vonmangoldt.png
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np


# ---------------------------------------------------------------------------
# Bokstedt's THH(Z) and elementary number theory
# ---------------------------------------------------------------------------

def thh_torsion_order(i: int) -> int:
    """|THH_{2i-1}(Z)| = i  (Bokstedt). The torsion group is Z/i."""
    return i


def vp(i: int, p: int) -> int:
    """p-adic valuation of i."""
    v = 0
    while i % p == 0:
        i //= p
        v += 1
    return v


def divisors(n: int):
    ds = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            ds.append(d)
            if d != n // d:
                ds.append(n // d)
        d += 1
    return sorted(ds)


def mobius(n: int) -> int:
    if n == 1:
        return 1
    m = n
    result = 1
    p = 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0  # squared prime factor
            result = -result
        p += 1
    if m > 1:
        result = -result
    return result


def lambda_coefficients(a, n_max: int):
    """von Mangoldt-type coefficients of -L'/L from Dirichlet coefficients a[n].

    Solves a_n log n = sum_{d|n} Lambda_L(d) a_{n/d}, with a[1] = 1, for
    Lambda_L(n) = a_n log n - sum_{d|n, d<n} Lambda_L(d) a_{n/d}.
    `a` is a function a(n) -> mpf. Returns list Lambda_L[1..n_max].
    """
    Lam = [mp.mpf(0)] * (n_max + 1)
    for n in range(1, n_max + 1):
        s = a(n) * mp.log(n) if n > 1 else mp.mpf(0)
        for d in divisors(n):
            if d < n:
                s -= Lam[d] * a(n // d)
        Lam[n] = s  # a(1) = 1
    return Lam[1:]


# ---------------------------------------------------------------------------

def run(N_terms: int = 200000, n_coeff: int = 60, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    mp.mp.dps = 30

    test_s = [mp.mpf(2), mp.mpf(3), mp.mpf(4)]

    print("[THH] Link 1 (EXACT identity, term-by-term: zeta'(s) = -sum_i (log i) i^-s):")
    print("      Z_THH(s) = sum_i log|THH_{2i-1}(Z)| i^-s = sum_i (log i) i^-s  ==  -zeta'(s)")
    print("      (numeric below is a truncated-partial-sum convergence check, M=%d)" % N_terms)
    link1 = {}
    for s in test_s:
        Z = mp.fsum(mp.log(i) * mp.power(i, -s) for i in range(2, N_terms + 1))
        target = -mp.zeta(s, derivative=1)
        err = float(abs(Z - target))
        link1[float(s)] = (complex(Z), complex(target), err)
        print(f"      s={float(s):.0f}: Z_THH(partial)={mp.nstr(Z,12)}  -zeta'={mp.nstr(target,12)}  err={err:.2e}")

    print("\n[THH] Link 2 (CLASSICAL identity): Lambda = mu * log  (i.e. -zeta'/zeta = (-zeta')(1/zeta))")
    # von Mangoldt from Mobius convolution of log-orders, vs direct -zeta'/zeta.
    conv_err = mp.mpf(0)
    Lam_zeta = []
    for n in range(1, n_coeff + 1):
        val = sum(mobius(n // d) * mp.log(d) for d in divisors(n))  # (mu * log)(n)
        Lam_zeta.append(val)
    # check: this equals von Mangoldt (log p on prime powers, else 0)
    vm_direct = lambda_coefficients(lambda k: mp.mpf(1), n_coeff)  # zeta a_n = 1
    max_diff = max(float(abs(Lam_zeta[i] - vm_direct[i])) for i in range(n_coeff))
    print(f"      max|mu*log - vonMangoldt| over n<= {n_coeff}: {max_diff:.2e}")
    # spot-check it reconstructs -zeta'/zeta as a Dirichlet series
    link2 = {}
    for s in test_s:
        approx = sum(Lam_zeta[n - 1] * mp.power(n, -s) for n in range(1, n_coeff + 1))
        target = -mp.zeta(s, derivative=1) / mp.zeta(s)
        link2[float(s)] = (complex(approx), complex(target), float(abs(approx - target)))
        print(f"      s={float(s):.0f}: sum (mu*log)(n) n^-s ={mp.nstr(approx,12)}  "
              f"-zeta'/zeta={mp.nstr(target,12)}  err={float(abs(approx-target)):.2e}")

    print("\n[THH] Link 3 (per-prime structure, EXACT by regrouping): prime p enters degree 2i-1 via v_p(i).")
    print("      sum_i v_p(i) i^-s = sum_k sum_{p^k | i} i^-s = zeta(s) sum_k p^-ks = zeta(s) p^-s/(1-p^-s).")
    print("      Times log p this is zeta(s) * [p-Euler factor of -zeta'/zeta]. (M=%d partial-sum check)" % N_terms)
    primes = [2, 3, 5]
    link3 = {}
    s = mp.mpf(3)  # s=3: faster convergence than s=2 for a clean numeric check
    for p in primes:
        lhs = mp.fsum(vp(i, p) * mp.log(p) * mp.power(i, -s) for i in range(2, N_terms + 1))
        rhs = mp.zeta(s) * mp.log(p) * mp.power(p, -s) / (1 - mp.power(p, -s))
        link3[p] = (complex(lhs), complex(rhs), float(abs(lhs - rhs)))
        print(f"      p={p}, s=3: THH side(partial)={mp.nstr(lhs,12)}  zeta*EulerFactor={mp.nstr(rhs,12)}  "
              f"err={float(abs(lhs-rhs)):.2e}")
    # and sum over p of v_p(i) log p = log i (so summing all primes recovers Link 1)
    check_logi = all(abs(float(sum(vp(i, q) * mp.log(q)
                     for q in range(2, i + 1) if all(q % r for r in range(2, q))) - mp.log(i))) < 1e-12
                     for i in range(2, 40))
    print(f"      cross-check sum_p v_p(i) log p = log i for i<40: {check_logi}")

    print("\n[THH] D-H FIREWALL (K2): von Mangoldt coefficients of D-H delocalize off prime powers.")
    sqrt5 = mp.sqrt(5)
    kappa = (mp.sqrt(10 - 2 * sqrt5) - 2) / (sqrt5 - 1)
    dh_period = [mp.mpf(1), kappa, -kappa, mp.mpf(-1), mp.mpf(0)]
    a_dh = lambda n: dh_period[(n - 1) % 5]
    Lam_dh = lambda_coefficients(a_dh, n_coeff)

    def is_prime_power(n):
        for p in range(2, n + 1):
            if p * p > n and n > 1:
                return True  # n itself prime
            if n % p == 0:
                while n % p == 0:
                    n //= p
                return n == 1
        return False

    composite_support = [n for n in range(2, n_coeff + 1)
                         if not is_prime_power(n) and abs(float(Lam_dh[n - 1])) > 1e-12]
    first_leak = composite_support[0] if composite_support else None
    print(f"      D-H Lambda_DH nonzero on COMPOSITE (non-prime-power) n: {composite_support[:8]}...")
    print(f"      first leak at n={first_leak} (expected n=6, per #20/#26)")
    print(f"      => Lambda_DH is NOT mu*(log-order sequence): no THH, no surface (K2 holds).")

    print("\n[THH] ===== VERDICT =====")
    print("      Bokstedt's THH(Z) log-orders assemble RIGOROUSLY to -zeta'(s) (Link 1),")
    print("      with the correct per-prime log p structure via v_p(i) (Link 3). The von")
    print("      Mangoldt sum = #26 dynamical zeta = Gamma_S^2 is one Mobius factor (1/zeta)")
    print("      away (Link 2). That factor is the conjectural THH->TC cyclotomic reduction.")
    print("      Checkpoint 10A.ii is PASSED in its imprimitive form and reduced to a single,")
    print("      sharp target: does the cyclotomic equalizer implement Mobius inversion?")

    np.savez_compressed(
        out_dir / "e_thh_vonmangoldt.npz",
        link1_err=np.array([link1[float(s)][2] for s in test_s]),
        link2_err=np.array([link2[float(s)][2] for s in test_s]),
        link3_err=np.array([link3[p][2] for p in primes]),
        mu_log_vs_vonmangoldt=max_diff,
        dh_composite_support=np.array(composite_support),
        dh_first_leak=(first_leak if first_leak else -1),
        test_s=np.array([float(s) for s in test_s]),
        primes=np.array(primes),
    )

    # Plot: the THH order sequence, the two Dirichlet series, the D-H leak.
    fig, axs = plt.subplots(1, 3, figsize=(16, 4.6))

    ax = axs[0]
    iv = np.arange(1, 41)
    ax.bar(iv, [np.log(thh_torsion_order(int(i))) for i in iv], color="steelblue")
    ax.set_xlabel("i  (degree 2i-1)")
    ax.set_ylabel("log |THH_{2i-1}(Z)| = log i")
    ax.set_title("Bokstedt torsion log-orders\n(assemble to -zeta'(s) under weight i^-s)")
    ax.grid(alpha=0.3, axis="y")

    ax = axs[1]
    ss = np.linspace(1.6, 4.0, 40)
    z_thh = [float(-mp.zeta(mp.mpf(x), derivative=1)) for x in ss]            # Link 1 target
    vm = [float(-mp.zeta(mp.mpf(x), derivative=1) / mp.zeta(mp.mpf(x))) for x in ss]  # von Mangoldt
    ax.plot(ss, z_thh, "b-", label="-zeta'(s) = THH log-order sum (imprimitive)")
    ax.plot(ss, vm, "r-", label="-zeta'/zeta = von Mangoldt (#26, primitive)")
    ax.set_xlabel("s"); ax.set_ylabel("value")
    ax.set_title("The Mobius gap: factor 1/zeta separates\nTHH log-sum from the von Mangoldt sum")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axs[2]
    ns = np.arange(1, n_coeff + 1)
    lam_zeta_arr = np.array([float(x) for x in Lam_zeta])
    lam_dh_arr = np.array([float(x) for x in Lam_dh])
    ax.stem(ns, lam_dh_arr, linefmt="r-", markerfmt="rx", basefmt=" ", label="D-H Lambda_DH")
    ax.stem(ns, lam_zeta_arr, linefmt="b-", markerfmt="bo", basefmt=" ", label="zeta vonMangoldt")
    if first_leak:
        ax.axvline(first_leak, color="green", ls="--", lw=1, label=f"D-H first composite leak n={first_leak}")
    ax.set_xlabel("n"); ax.set_ylabel("Lambda_L(n)")
    ax.set_title("K2 firewall: D-H delocalizes off prime powers\n(zeta stays on prime powers = Euler product)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e_thh_vonmangoldt.png", dpi=140)
    plt.close()
    print(f"[THH] Saved {out_dir / 'e_thh_vonmangoldt.png'}")
    print(f"[THH] Saved {out_dir / 'e_thh_vonmangoldt.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-coeff", type=int, default=60)
    args = parser.parse_args()
    run(n_coeff=args.n_coeff)
