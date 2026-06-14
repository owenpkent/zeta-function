"""MC.3: the finite-prime modular structure is EULER-GATED (the K2 firewall at the
modular level) -- present for zeta, structurally absent for Davenport-Heilbronn
(modular-carrier milestone MC.3, -> LEARNINGS #102).

THE CLAIM
---------
The modular-carrier dictionary (#100/#101) splits into a finite-prime part (the
Frobenius / Euler factors) and an archimedean part (the Sen / Gamma-factor). The D-H
discipline requires the discriminator to live in the FINITE-prime part: D-H has a
functional equation (so it shares the archimedean Gamma-factor / Sen piece) but NO
Euler product, so the BC-type finite-prime modular structure cannot form for it (#44:
K2 lives on F, not on Theta_Sen). MC.3 checks this concretely.

The finite-prime modular structure is the Bost-Connes Gibbs/KMS structure: the BC
Hamiltonian H has eigenvalues {log n}, the partition function is
    Z(beta) = Tr(e^{-beta H}) = sum_n n^{-beta} = zeta(beta) = prod_p (1 - p^{-beta})^{-1},
positive weights n^{-beta} (a genuine Gibbs state), with a pole at beta = 1 (the type
III_1 phase transition, #81). The "interaction" is the von Mangoldt comb
    -f'/f(s) = sum_n Lambda_f(n) n^{-s},     Lambda_f(n) = a_n log n - sum_{d|n, d<n} a_{n/d} Lambda_f(d),
and the Euler product is exactly the statement that this comb is NON-NEGATIVE and
supported on prime powers (passivity, #90/#37). A function without an Euler product has
an indefinite comb, so no positive Gibbs state, so no BC modular structure.

WHAT THIS ESTABLISHES (each asserted)
-------------------------------------
1. zeta's comb is non-negative (von Mangoldt >= 0, supported on prime powers): the
   positive Gibbs weights exist, so the finite-prime modular structure forms.
2. D-H's comb goes NEGATIVE (first at n = 3, the first prime = 3 mod 5: Lambda_DH(3)
   = -kappa log 3 < 0): no positive Gibbs state, so the finite-prime modular structure
   does NOT form. (Reproduces #90 from the modular side.)
3. zeta's partition function is the Euler product with a pole at beta = 1 (type III_1);
   D-H has no Euler product. The archimedean Gamma-factor is SHARED (both have a
   functional equation), so it cannot discriminate; the discriminator is purely the
   finite-prime comb (#44).

So the finite-prime modular structure is euler-gated, and the modular polarization
carrier built on it passes the K2 firewall by construction. Running this file IS the test.
"""

from __future__ import annotations

import mpmath as mp

from experiments._shared import DavenportHeilbronn


def divisors_below(n: int) -> list:
    return [d for d in range(1, n) if n % d == 0]


def von_mangoldt_comb(coeff, N: int) -> dict:
    """Lambda_f(n) for a Dirichlet series f = sum a_n n^{-s} with a_1 = 1, via
    a_n log n = sum_{d|n} a_{n/d} Lambda_f(d)  =>
    Lambda_f(n) = a_n log n - sum_{d|n, d<n} a_{n/d} Lambda_f(d)."""
    Lam = {}
    for n in range(1, N + 1):
        s = coeff(n) * mp.log(n)
        for d in divisors_below(n):
            s -= coeff(n // d) * Lam[d]
        Lam[n] = s
    return Lam


def zeta_coeff(n: int):
    return mp.mpf(1)            # a_n = 1 for all n (the Euler product Z(beta) = zeta(beta))


def dh_coeff_factory():
    dh = DavenportHeilbronn()
    return lambda n: mp.re(dh.dirichlet_coefficient(n))   # real period-5 coefficients


def block1_zeta_comb_nonneg(N: int = 60) -> dict:
    Lam = von_mangoldt_comb(zeta_coeff, N)
    vals = [float(Lam[n]) for n in range(1, N + 1)]
    negatives = [n for n in range(1, N + 1) if float(Lam[n]) < -1e-12]
    # supported on prime powers: nonzero exactly at p^k
    prime_powers = {n for n in range(2, N + 1) if _is_prime_power(n)}
    nonzero = {n for n in range(2, N + 1) if abs(float(Lam[n])) > 1e-12}
    return {"min_value": min(vals), "n_negative": len(negatives),
            "supported_on_prime_powers": nonzero == prime_powers}


def block2_dh_comb_negative(N: int = 60) -> dict:
    mp.mp.dps = 40
    Lam = von_mangoldt_comb(dh_coeff_factory(), N)
    negatives = [n for n in range(1, N + 1) if float(Lam[n]) < -1e-9]
    kappa = mp.re(DavenportHeilbronn().dirichlet_coefficient(3))   # a_3 = -kappa
    lam3_closed = kappa * mp.log(3)                                # = -kappa log 3
    return {"Lambda_3": float(Lam[3]), "Lambda_3_closed_form": float(lam3_closed),
            "first_negative": negatives[0] if negatives else None,
            "n_negative": len(negatives)}


def block3_partition_function_euler_gating() -> dict:
    mp.mp.dps = 30
    # zeta(beta) = prod_{p<=P} (1 - p^{-beta})^{-1} (the BC partition function, Euler-factored)
    beta = mp.mpf("2.0")
    primes = [p for p in range(2, 5000) if _is_prime(p)]   # truncation tail -> 0 as P grows
    euler = mp.mpf(1)
    for p in primes:
        euler *= 1 / (1 - mp.power(p, -beta))
    euler_residual = abs(euler - mp.zeta(beta))
    # the pole at beta = 1 (the type III_1 phase transition): Z(beta) -> infinity
    z_near_pole = float(mp.zeta(mp.mpf("1.02")))
    dh = DavenportHeilbronn()
    return {
        "euler_product_residual_at_beta2": float(euler_residual),
        "Z_at_beta_1.02": z_near_pole,
        "zeta_has_euler_product": True,
        "dh_has_euler_product": bool(getattr(dh, "has_euler_product", False)),
        "dh_has_functional_equation": bool(getattr(dh, "has_functional_equation", False)),
    }


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def _is_prime_power(n: int) -> bool:
    for p in range(2, n + 1):
        if _is_prime(p):
            m, k = n, 0
            while m % p == 0:
                m //= p
                k += 1
            if m == 1 and k >= 1:
                return True
    return False


def demo() -> int:
    print("MC.3: the finite-prime modular structure is EULER-GATED (the K2 firewall)\n")

    b1 = block1_zeta_comb_nonneg()
    print("  [1] zeta's von Mangoldt comb is non-negative (the positive Gibbs weights exist):")
    print(f"      min Lambda(n) over n<=60 = {b1['min_value']:.4f}, negatives = {b1['n_negative']}, "
          f"supported on prime powers = {b1['supported_on_prime_powers']}")
    print(f"      => the BC Gibbs/KMS state forms; the finite-prime modular structure EXISTS for zeta.")

    b2 = block2_dh_comb_negative()
    print("\n  [2] D-H's comb goes NEGATIVE -> no positive Gibbs state -> no modular structure:")
    print(f"      Lambda_DH(3) = {b2['Lambda_3']:.4f} (closed form -kappa log 3 = {b2['Lambda_3_closed_form']:.4f}); "
          f"first negative at n = {b2['first_negative']}, total negatives <=60 = {b2['n_negative']}")
    print(f"      => no positive partition function over the primes; the finite-prime modular structure")
    print(f"         does NOT form for D-H (reproduces #90 from the modular side).")

    b3 = block3_partition_function_euler_gating()
    print("\n  [3] the partition function Z(beta) = zeta(beta) is Euler-factored with a pole at beta=1:")
    print(f"      prod_p (1-p^-2)^-1 = zeta(2) residual {b3['euler_product_residual_at_beta2']:.2e}; "
          f"Z(1.02) = {b3['Z_at_beta_1.02']:.2f} (the type III_1 pole)")
    print(f"      zeta euler-product = {b3['zeta_has_euler_product']}, D-H euler-product = "
          f"{b3['dh_has_euler_product']}, D-H functional-equation = {b3['dh_has_functional_equation']}")
    print(f"      => the archimedean Gamma-factor is SHARED (both have an FE), so the discriminator is")
    print(f"         purely the finite-prime comb (#44: K2 lives on F, not on Theta_Sen).")

    print("\n  VERDICT (MC.3 done): the finite-prime modular (Bost-Connes) structure is EULER-GATED.")
    print("  The positive von Mangoldt comb -> the Gibbs/KMS state -> the type III_1 factor exists for")
    print("  zeta and structurally FAILS for D-H (indefinite comb, no Euler product). So the modular")
    print("  polarization carrier, built on the finite-prime modular flow, passes the K2 firewall by")
    print("  construction. The archimedean half is shared and cannot discriminate; the arithmetic lives")
    print("  in the euler-gated finite-prime modular structure.")

    assert b1["n_negative"] == 0 and b1["supported_on_prime_powers"], \
        "[1] zeta's comb should be non-negative and supported on prime powers"
    assert b2["Lambda_3"] < -1e-6 and b2["first_negative"] == 3, \
        "[2] D-H's comb should go negative first at n=3"
    assert b3["euler_product_residual_at_beta2"] < 1e-4 and b3["Z_at_beta_1.02"] > 40 \
        and b3["zeta_has_euler_product"] and not b3["dh_has_euler_product"] \
        and b3["dh_has_functional_equation"], \
        "[3] zeta = Euler product with a pole; D-H has the FE (shared) but no Euler product"
    print("\n  (all three structural assertions hold)")
    return 0


if __name__ == "__main__":
    raise SystemExit(demo())
