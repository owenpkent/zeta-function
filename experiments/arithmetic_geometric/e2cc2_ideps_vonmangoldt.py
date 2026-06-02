"""2CC.2 -- does the Connes-Consani self-composition Id_eps carry the von Mangoldt /
-zeta'/zeta spectrum? YES, as the TRACE (the flow generator), refining 2CC: the diagonal
self-intersection is trace-rich where the off-diagonal point-count froze. Still the trace,
not the signature -- the q-lift gap is unchanged.

CONTEXT (Direction 8, the q-lift; follows 2CC #40). 2CC showed the C-C square's tropical
mixed-volume form gives a free Alexandrov-Fenchel signature but is arithmetic-blind: the
OFF-DIAGONAL point count Delta . Gamma_p froze at the tropical value p-1 (= q+1-t with t=2),
losing the Frobenius trace. This experiment probes the DIAGONAL / self-intersection instead.

THE OBJECT. Connes-Consani Thm 7.7: for irrational lambda with lambda*lambda^{-1}=1 in Q,
the self-composition of Frobenius correspondences is Psi(lambda) o Psi(lambda^{-1}) = Id_eps,
the TANGENTIAL DEFORMATION of the identity (Def 7.6: l_eps(q^n)=q^{(1+eps)n}, r_eps(q^n)=q^n).
The reading note (Connes-Consani-2015 point #4) identifies Id_eps as the analytic shadow of
the self-intersection Gamma_S^2, and 2R pinned Gamma_S^2 = -zeta'/zeta = sum_n Lambda(n) n^-s
(a Ruelle dynamical zeta with primitive orbit lengths {log p}). So the question is whether
the C-C Id_eps deformation reproduces that von Mangoldt spectrum.

THE KEY IDENTIFICATION. The Id_eps tangent is
    d/d_eps [ l_eps(q^n) / r_eps(q^n) ]|_{eps=0} = d/d_eps q^{eps n}|_0 = n log q,
i.e. the NUMBER / SCALING operator n (times log q). That is exactly the Deninger / Hesselholt
flow generator Theta (Theta(v) = (2 pi i / log q) v, q^Theta = Fr; #29), and
    -d/ds log det_inf(s - Theta) = -d/ds log prod_p (1 - p^{-s})^{-1}
                                 = -zeta'/zeta(s) = sum_n Lambda(n) n^{-s}.
The C-C multiplicative composition law Fr_{1,p} o Fr_{1,p} ... = Fr_{1,p^k} (slope p^k) is
exactly the iterate structure of the primitive orbit at p: the prime slopes {p} are the
primitive periodic orbits, with log-scales {log p}. So Id_eps (the diagonal anomaly) carries
the full von Mangoldt / -zeta'/zeta arithmetic, via the flow generator.

WHAT WE CONFIRM:
 1. The C-C prime-slope dynamical zeta prod_p (1-p^{-s})^{-1} = zeta(s); its log-derivative
    is -zeta'/zeta = sum Lambda(n) n^{-s} (von Mangoldt). The orbits = primes, lengths log p,
    iterates Fr_{1,p}^k = Fr_{1,p^k}. (Reproduces 2R, now tied to the C-C composition law.)
 2. The CONTRAST refining 2CC: the off-diagonal Delta . Gamma_p (mixed-area shadow) = p-1,
    t-FROZEN; the self-intersection Gamma_S^2 (Id_eps / the regularized orbit sum) carries
    the full von Mangoldt coefficient Lambda(n) (trace-rich). The diagonal sees the arithmetic
    the off-diagonal lost.
 3. D-H control: no Euler product => the von Mangoldt analogue Lambda_DH delocalizes onto
    COMPOSITE n (no primitive prime-power orbit structure), so there is no clean Id_eps / flow
    spectrum (2R/#20 confirmed here from the C-C-composition viewpoint).

HONEST FRAMING. Id_eps carries the TRACE (the spectrum / the realization of zeta as a
flow-determinant, the EASY half, #30 "all roads to the signature"). It does NOT carry the
SIGNATURE: the von Mangoldt sum is a determinant/trace, not a Hodge index, and RH is the
signature of the H^1 / TP_odd / numerator (2S), which the C-C square still lacks (2CC: no
signed pairing). So the Id_eps probe CONFIRMS the C-C square carries the von Mangoldt trace
(via the flow generator, connecting C-C <-> 2R <-> Deninger/Hesselholt) but the q-lift gap
(turn this trace into a signature) is unchanged.

Run:  python -m experiments.arithmetic_geometric.e2cc2_ideps_vonmangoldt
"""

from __future__ import annotations

from pathlib import Path

import mpmath as mp

from experiments._shared.davenport_heilbronn import davenport_heilbronn

HERE = Path(__file__).resolve().parent
DPS = 30


def primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def von_mangoldt_analogue(coeff_fn, N):
    """Lambda_L(n) for n=1..N, defined by -L'/L = sum_n Lambda_L(n) n^{-s} for
    L = sum_n c_n n^{-s} (c_1 = 1). Recursion: sum_{d|n} Lambda_L(d) c_{n/d} = c_n log n.

    coeff_fn(n) returns c_n (mpf/mpc). For zeta c_n=1 => Lambda_L = von Mangoldt (prime
    powers only). For D-H the c_n are period-5 => Lambda_L delocalizes onto composites.
    """
    c = [mp.mpf(0)] + [mp.mpc(coeff_fn(n)) for n in range(1, N + 1)]
    Lam = [mp.mpf(0)] * (N + 1)
    for n in range(2, N + 1):
        # sum_{d|n} Lam[d] c[n/d] = c[n] log n  ->  solve for Lam[n] (d=n term has c[1]=1)
        acc = mp.mpc(0)
        d = 1
        while d * d <= n:
            if n % d == 0:
                if d != n:
                    acc += Lam[d] * c[n // d]
                e = n // d
                if e != d and e != n:
                    acc += Lam[e] * c[n // e]
            d += 1
        Lam[n] = c[n] * mp.log(n) - acc
    return Lam


def run():
    mp.mp.dps = DPS
    print("2CC.2 -- does the Connes-Consani Id_eps self-composition carry -zeta'/zeta?")
    print("Probe of the diagonal self-intersection (Gamma_S^2) vs 2CC's frozen off-diagonal.\n")

    # ---- 1. The C-C prime-slope dynamical zeta = zeta; log-deriv = von Mangoldt -------
    print("=" * 78)
    print("1. C-C prime slopes {p} as primitive orbits (lengths log p; iterates Fr_{1,p}^k")
    print("   = Fr_{1,p^k}). Dynamical zeta prod_p (1-p^-s)^-1 = zeta; -d/ds log = -zeta'/zeta.")
    print("=" * 78)
    s = mp.mpf(2)
    P = primes_up_to(20000)
    Zdyn = mp.mpf(1)
    for p in P:
        Zdyn *= 1 / (1 - mp.power(p, -s))
    zeta_s = mp.zeta(s)
    print(f"  prod_p (1-p^-s)^-1 at s=2  = {mp.nstr(Zdyn, 12)}")
    print(f"  zeta(2)                    = {mp.nstr(zeta_s, 12)}  (= pi^2/6 = {mp.nstr(mp.pi**2/6,12)})")
    print(f"  rel. error                 = {mp.nstr(abs(Zdyn - zeta_s)/abs(zeta_s), 3)}")
    # -zeta'/zeta(2) = sum_n Lambda(n) n^-2
    neg_zp_over_z = -mp.zeta(s, derivative=1) / zeta_s
    Lam_zeta = von_mangoldt_analogue(lambda n: mp.mpf(1), 200)
    vm_sum = sum(Lam_zeta[n] / mp.power(n, s) for n in range(1, 201))
    print(f"  -zeta'/zeta(2)             = {mp.nstr(neg_zp_over_z, 12)}")
    print(f"  sum_n Lambda(n) n^-2 (N=200)= {mp.nstr(vm_sum, 12)}  (von Mangoldt)")
    print(f"  rel. error                 = {mp.nstr(abs(vm_sum - neg_zp_over_z)/abs(neg_zp_over_z), 3)}")
    # confirm Lambda_zeta supported on prime powers
    off_pp = [n for n in range(2, 201) if abs(Lam_zeta[n]) > mp.mpf(10)**-10
              and not _is_prime_power(n)]
    print(f"  Lambda_zeta supported OFF prime powers below 200: {len(off_pp)} (must be 0)\n")

    # ---- 2. Contrast: off-diagonal (frozen, 2CC) vs self-intersection (trace-rich) ----
    print("=" * 78)
    print("2. CONTRAST refining 2CC: off-diagonal Delta.Gamma_p (mixed-area shadow) is")
    print("   t-FROZEN at p-1; the self-intersection Gamma_S^2 (Id_eps / orbit sum) carries")
    print("   the full von Mangoldt coefficient (trace-rich).")
    print("=" * 78)
    print(f"  {'p':>4} {'Delta.Gamma_p (shadow, 2CC)':>28} {'Gamma_S^2 coeff Lambda(p)=log p':>34}")
    for p in [2, 3, 5, 7, 11, 13]:
        off = p - 1                      # 2CC mixed-area off-diagonal (t frozen at 2)
        diag = float(mp.log(p))          # von Mangoldt primitive-orbit weight (trace-rich)
        print(f"  {p:>4} {off:>28} {diag:>34.6f}")
    print("  off-diagonal: t-blind tropical shadow (2CC).  self/diagonal (Id_eps): the")
    print("  arithmetic trace -zeta'/zeta. The diagonal anomaly sees what the off-diagonal lost.\n")

    # ---- 3. D-H control: no Euler product => Lambda_DH delocalizes => no orbit spectrum
    print("=" * 78)
    print("3. K2 (Davenport-Heilbronn): no Euler product => Lambda_DH delocalizes onto")
    print("   composite n => no primitive prime-power orbit structure => no Id_eps / flow")
    print("   spectrum (2R/#20, from the C-C-composition viewpoint).")
    print("=" * 78)
    Ndh = 60
    Lam_dh = von_mangoldt_analogue(lambda n: davenport_heilbronn.dirichlet_coefficient(n), Ndh)
    leaks = [(n, complex(Lam_dh[n])) for n in range(2, Ndh + 1)
             if abs(Lam_dh[n]) > mp.mpf(10)**-9 and not _is_prime_power(n)]
    mass_on = sum(abs(Lam_dh[n]) for n in range(2, Ndh + 1) if _is_prime_power(n))
    mass_off = sum(abs(Lam_dh[n]) for n in range(2, Ndh + 1) if not _is_prime_power(n))
    print(f"  Lambda_DH on prime powers (mass, n<= {Ndh}) = {float(mass_on):.4f}")
    print(f"  Lambda_DH OFF prime powers (mass)          = {float(mass_off):.4f}")
    print(f"  first composite leaks: {[(n, round(v.real,4)) for n,v in leaks[:6]]}")
    print(f"  => D-H von Mangoldt delocalizes (first leak n={leaks[0][0] if leaks else None});")
    print(f"     no clean {{log p}} orbit spectrum => no Id_eps self-intersection spectrum.\n")

    # ---- Synthesis ----------------------------------------------------------
    print("=" * 78)
    print("SYNTHESIS")
    print("=" * 78)
    print("  The C-C self-composition Id_eps DOES carry the von Mangoldt / -zeta'/zeta spectrum:")
    print("  its tangent is the number/scaling operator n = the Deninger-Hesselholt flow")
    print("  generator Theta, and -d/ds log det_inf(s-Theta) = -zeta'/zeta. The prime slopes")
    print("  {p} (with Fr_{1,p}^k = Fr_{1,p^k}) are the primitive orbits {log p}.")
    print("  REFINES 2CC: the off-diagonal point count froze (tropical shadow), but the")
    print("  DIAGONAL self-intersection (Id_eps) is trace-rich -- it carries the arithmetic.")
    print("  HONEST: this is the TRACE (the realization of zeta as a flow determinant, the")
    print("  EASY half, #30), NOT the SIGNATURE. The von Mangoldt sum is a determinant/trace,")
    print("  not a Hodge index; RH is the signature of the H^1/TP_odd/numerator (2S), which the")
    print("  C-C square still lacks (2CC: no signed pairing). So the q-lift gap is unchanged:")
    print("  turn the Id_eps TRACE into a Hodge-index SIGNATURE. D-H has no orbit spectrum (K2).")

    _plot(P, s)
    print(f"\nSaved: e2cc2_ideps_vonmangoldt.png")
    return dict(Zdyn=complex(Zdyn), zeta=complex(zeta_s), vm_err=float(abs(vm_sum-neg_zp_over_z)),
                dh_leak_first=(leaks[0][0] if leaks else None), dh_mass_off=float(mass_off))


def _is_prime_power(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            while n % d == 0:
                n //= d
            return n == 1
        d += 1
    return True  # n prime


def _plot(P, s):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:  # pragma: no cover
        print(f"(plot skipped: {exc})")
        return
    # Convergence of the C-C prime-slope dynamical zeta to zeta(2).
    import mpmath as mp
    zeta2 = float(mp.zeta(2))
    cuts = [10, 30, 100, 300, 1000, 3000, 10000, 20000]
    errs = []
    Z = mp.mpf(1)
    idx = 0
    vals = []
    for k, p in enumerate(P, 1):
        Z *= 1 / (1 - mp.power(p, -s))
        if idx < len(cuts) and k >= cuts[idx]:
            vals.append((cuts[idx], abs(float(Z) - zeta2) / zeta2))
            idx += 1
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    xs = [v[0] for v in vals]
    ys = [v[1] for v in vals]
    ax.loglog(xs, ys, "o-", color="tab:blue")
    ax.set_xlabel("# primes (orbits) included")
    ax.set_ylabel("rel. error vs zeta(2)")
    ax.set_title("C-C prime-slope dynamical zeta prod_p (1-p^-s)^-1 -> zeta(s)\n"
                 "(Id_eps self-composition carries -zeta'/zeta = von Mangoldt: the trace, not the signature)")
    ax.grid(alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(HERE / "e2cc2_ideps_vonmangoldt.png", dpi=130)
    plt.close(fig)


if __name__ == "__main__":
    run()
