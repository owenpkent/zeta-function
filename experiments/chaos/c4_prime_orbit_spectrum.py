"""C4: is {log p} the length spectrum of a genuine chaotic (Anosov) flow?

This points the chaos toolbox at the repo's 2R finding
(experiments/arithmetic_geometric/e2r_dynamical_zeta.py), which realized
Gamma_S^2 as the log-derivative of a Ruelle dynamical zeta whose primitive
orbit lengths are {log p}. 2R showed the object exists on the prime side and
does not exist for Davenport-Heilbronn. C4 deepens that with the
thermodynamic-formalism / transfer-operator lens and asks the sharper
question: can the primes actually BE the periodic orbits of a genuine chaotic
flow, the way closed geodesics are the orbits of the geodesic flow behind a
Selberg zeta?

The honest answer, in four computed parts:

  PART 1  The prime system has the counting law of an entropy-1 flow. A genuine
          Anosov flow satisfies N(L) = #{primitive orbits of length <= L}
          ~ e^{hL}/(hL); with orbit length log p this is pi(e^L), and the
          empirical entropy log N(L)/L -> 1 by the prime number theorem. This is
          a real consistency, which is why the analogy is seductive. It is NOT a
          kill.

  PART 2  The flow's Ruelle zeta (orbit lengths {log p}) is the Euler product
          = zeta(s). The prime orbits supply the PASSIVE half (Euler product
          = a nonnegative comb; the acoustic passive/lossless split, memory
          acoustic_passive_lossless_thread).

  PART 3  THE OBSTRUCTION. The archimedean Gamma-factor has no periodic-orbit
          source. The mean zero density N_smooth(T) ~ (T/2pi) log(T/2pi) - T/2pi
          is 100% archimedean (pure Gamma-factor, zero prime input). The prime
          orbits produce only the oscillation S(T) = O(log T); the MEAN is the
          archimedean place, and no orbit sum produces it. A compact-flow
          Selberg/Ruelle zeta gets its identity/area term from geometry; zeta's
          analogue is the archimedean place, which is not a flow. Same locus as
          the #34 stealth window and the lossless half of the acoustic split.

  PART 4  The thermodynamic lens separates zeta from D-H where GUE statistics
          cannot. Prime powers p^k are the repetitions of the primitive orbit
          gamma_p, so -zeta'/zeta = sum_n Lambda(n) n^{-s} is supported exactly
          on prime powers (localization 1.0). For D-H, Lambda_DH delocalizes off
          prime powers (2R), so there is no primitive-orbit-plus-repetition
          structure and no genuine flow. GUE pair correlation is blind to this;
          the orbit-repetition (Euler-product) structure is not. A genuine step
          past Level 3.

VERDICT: the prime orbits are a real entropy-1 dynamical skeleton (the passive
Euler-product half) and the thermodynamic lens is a genuine discriminator, but
the archimedean Gamma-factor (the mean density = the lossless / polarization
half) has no orbit source, so the dynamical route supplies the stage and
relocates to the archimedean place = M4. This deepens 2R; it is not a new route
to RH. A negative result is a coordinate that narrows the search.

Run:
    python -m experiments.chaos.c4_prime_orbit_spectrum
"""

from __future__ import annotations

import math
import os

import numpy as np
import mpmath as mp

from experiments._shared import DavenportHeilbronn
from experiments.positivity.e3m_place_type_balance import (
    von_mangoldt_zeta,
    lambda_coeffs_from_dirichlet,
)

_HERE = os.path.dirname(os.path.abspath(__file__))


def _prime_counts(x_max):
    """Sieve of Eratosthenes up to x_max; return a boolean prime mask (index = n)."""
    sieve = np.ones(x_max + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(math.isqrt(x_max)) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    return sieve


def is_prime_power(n):
    if n < 2:
        return False
    m, p = n, 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            return m == 1
        p += 1
    return True


def part1_entropy():
    print("PART 1  Topological entropy of the prime 'flow' (orbit length log p)")
    print("-" * 70)
    print("  A genuine Anosov flow has N(L) = #{orbits, length <= L} ~ e^{hL}/(hL).")
    print("  Orbit length l(gamma_p) = log p, so N(L) = pi(e^L). Empirical entropy")
    print("  h(L) = log N(L) / L should approach 1 (the prime number theorem).\n")

    x_max = 10 ** 7
    prime_mask = _prime_counts(x_max)
    cum = np.cumsum(prime_mask)  # cum[x] = pi(x)

    print("     x=e^L        L        pi(x)       h=logN/L    pi(x)logx/x")
    hs = []
    Ls = []
    for k in range(2, 8):
        x = 10 ** k
        L = math.log(x)
        pix = int(cum[x])
        h = math.log(pix) / L
        pnt_ratio = pix * math.log(x) / x
        hs.append(h)
        Ls.append(L)
        print("  %.3e   %7.3f   %9d     %.5f      %.5f" % (x, L, pix, h, pnt_ratio))
    print("\n  h(L) climbs toward 1: the primes have the counting law of an")
    print("  entropy-1 flow. Real consistency, and exactly why the analogy tempts.")
    print("  It is a consistency check, not a proof of a flow.\n")
    return np.array(Ls), np.array(hs)


def part2_euler_product():
    print("PART 2  The Ruelle zeta (orbit lengths {log p}) is the Euler product")
    print("-" * 70)
    mp.mp.dps = 25
    s = mp.mpc(2, 0)
    target = mp.zeta(s)
    print("  prod_{p<=P} (1 - p^{-s})^{-1}  vs  zeta(s) at s=2  (|zeta(2)|=%.6f):" % float(abs(target)))
    from sympy import primerange
    for P in [10, 100, 1000, 10000]:
        prod = mp.mpf(1)
        for p in primerange(2, P + 1):
            prod *= 1 / (1 - mp.mpf(p) ** (-s))
        print("      primes <= %6d:  |prod - zeta| = %.3e" % (P, float(abs(prod - target))))
    print("\n  The prime orbits give the PASSIVE half: the Euler product, a")
    print("  nonnegative comb (the acoustic passive/lossless split). This half")
    print("  is real and unconditional. It is not where RH lives.\n")


def part3_archimedean_obstruction():
    print("PART 3  THE OBSTRUCTION: the archimedean Gamma-factor has no orbit source")
    print("-" * 70)
    print("  The completed xi(s) = pi^{-s/2} Gamma(s/2) zeta(s) carries the")
    print("  functional equation and the critical line. The smooth zero count")
    print("  N_smooth(T) = theta(T)/pi + 1 comes ENTIRELY from the Gamma-factor.")
    print("  Riemann-von Mangoldt: (T/2pi) log(T/2pi) - T/2pi + 7/8.\n")
    mp.mp.dps = 30

    def theta(T):
        # Riemann-Siegel theta: Im log[ pi^{-(1/4 + iT/2)} Gamma(1/4 + iT/2) ].
        z = mp.mpf(1) / 4 + 1j * mp.mpf(T) / 2
        return mp.im(mp.loggamma(z)) - (mp.mpf(T) / 2) * mp.log(mp.pi)

    def rvm(T):
        T = mp.mpf(T)
        return (T / (2 * mp.pi)) * mp.log(T / (2 * mp.pi)) - T / (2 * mp.pi) + mp.mpf(7) / 8

    print("        T        N_smooth=theta/pi+1     RvM formula        difference")
    for T in [100, 1000, 10000, 100000]:
        ns = theta(T) / mp.pi + 1
        rv = rvm(T)
        print("  %9d      %16.6f    %16.6f    %.3e"
              % (T, float(ns), float(rv), float(abs(ns - rv))))
    print("\n  The two agree to O(1/T): the mean density is 100% archimedean, pure")
    print("  Gamma-factor, zero prime input. The prime orbits supply only the")
    print("  oscillation S(T) = O(log T); the MEAN is the archimedean place, and no")
    print("  periodic-orbit sum produces it. A Selberg/Ruelle zeta gets its")
    print("  identity term from geometry; zeta's analogue is the archimedean place,")
    print("  which is not a flow. This is the obstruction (the #34 stealth-window")
    print("  locus, the lossless half of the acoustic split).\n")


def part4_thermodynamic_discriminator():
    print("PART 4  The thermodynamic discriminator: zeta vs D-H beyond GUE")
    print("-" * 70)
    print("  Prime powers p^k are the REPETITIONS of the primitive orbit gamma_p")
    print("  (length k log p), so -zeta'/zeta = sum_n Lambda(n) n^{-s} is supported")
    print("  exactly on prime powers. A genuine flow needs this orbit + repetition")
    print("  structure. D-H's Lambda_DH delocalizes off prime powers (2R).\n")

    n_max = 36
    # zeta: von Mangoldt is supported on prime powers by definition -> localization 1.0.
    zeta_on = sum(abs(von_mangoldt_zeta(n)) for n in range(2, n_max + 1) if is_prime_power(n))
    zeta_off = sum(abs(von_mangoldt_zeta(n)) for n in range(2, n_max + 1) if not is_prime_power(n))
    zeta_loc = zeta_on / (zeta_on + zeta_off)

    dh = DavenportHeilbronn()
    lam_dh = lambda_coeffs_from_dirichlet(dh, n_max, prec=20)
    dh_on = sum(abs(lam_dh[n]) for n in range(2, n_max + 1) if is_prime_power(n))
    dh_off = sum(abs(lam_dh[n]) for n in range(2, n_max + 1) if not is_prime_power(n))
    dh_loc = dh_on / (dh_on + dh_off)

    print("        object     on prime powers   off prime powers   localization")
    print("        zeta       %13.4f    %14.4f    %.4f" % (zeta_on, zeta_off, zeta_loc))
    print("        D-H        %13.4f    %14.4f    %.4f" % (dh_on, dh_off, dh_loc))
    print("\n  zeta localizes perfectly (1.0000): clean primitive-orbit + repetition")
    print("  structure. D-H leaks mass off prime powers: no such structure, hence no")
    print("  genuine flow. GUE pair correlation is blind to this (D-H has GUE-like")
    print("  statistics too); the orbit-repetition (Euler-product) structure is not.")
    print("  A genuine step past Level 3.\n")
    return (zeta_on, zeta_off, zeta_loc), (dh_on, dh_off, dh_loc)


def _plot(Ls, hs, dh_stats, zeta_stats):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        print("  (matplotlib unavailable; skipping plot)")
        return
    fig, axs = plt.subplots(1, 2, figsize=(13, 5))

    ax = axs[0]
    ax.plot(Ls, hs, "o-", color="tab:blue")
    ax.axhline(1.0, color="crimson", ls="--", lw=1.5, label="entropy h = 1")
    ax.set_xlabel("L = log x")
    ax.set_ylabel("empirical entropy h(L) = log N(L) / L")
    ax.set_title("Part 1: the primes have the counting\nlaw of an entropy-1 flow (h -> 1)")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    ax = axs[1]
    zeta_on, zeta_off, _ = zeta_stats
    dh_on, dh_off, _ = dh_stats
    labels = ["zeta", "D-H"]
    on_vals = [zeta_on, dh_on]
    off_vals = [zeta_off, dh_off]
    xpos = np.arange(2)
    ax.bar(xpos - 0.18, on_vals, width=0.36, color="tab:blue", label="on prime powers")
    ax.bar(xpos + 0.18, off_vals, width=0.36, color="tab:red", label="off prime powers")
    ax.set_xticks(xpos)
    ax.set_xticklabels(labels)
    ax.set_ylabel("total |Lambda(n)| mass, n <= 36")
    ax.set_title("Part 4: orbit + repetition structure\n(zeta localizes; D-H delocalizes)")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis="y")

    fig.tight_layout()
    out = os.path.join(_HERE, "c4_prime_orbit_spectrum.png")
    fig.savefig(out, dpi=120)
    plt.close(fig)
    print("Saved plot: %s" % out)


def main():
    print("C4  Is {log p} the length spectrum of a genuine chaotic flow?")
    print("=" * 70)
    print()
    Ls, hs = part1_entropy()
    part2_euler_product()
    part3_archimedean_obstruction()
    zeta_stats, dh_stats = part4_thermodynamic_discriminator()
    _plot(Ls, hs, dh_stats, zeta_stats)

    print("=" * 70)
    print("VERDICT")
    print("-" * 70)
    print("  The prime orbits are a genuine entropy-1 dynamical skeleton (the")
    print("  passive Euler-product half), and the thermodynamic lens is a real")
    print("  discriminator: it separates zeta from Davenport-Heilbronn through the")
    print("  prime-power orbit-repetition structure, which GUE statistics cannot")
    print("  see. But the archimedean Gamma-factor (the mean zero density, the")
    print("  lossless / polarization half) has NO periodic-orbit source, so the")
    print("  dynamical route supplies the stage and relocates to the archimedean")
    print("  place = M4. This deepens 2R (e2r_dynamical_zeta.py) with the entropy")
    print("  framing, the archimedean-mean-has-no-orbit obstruction, and the")
    print("  thermodynamic D-H discriminator. It is not a new route to RH. The")
    print("  negative result is a coordinate: it says the flow is the fluctuation,")
    print("  the polarization is the mean, and the mean lives at the archimedean")
    print("  place.")


if __name__ == "__main__":
    main()
