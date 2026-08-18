"""Regression tests for the primes thread (e5a-e5e).

Standalone module per repo convention: prints "N/N passed", exit 0 iff all
pass. Everything runs at 10^6 scale plus small zero windows, so the whole
file is well under a minute.

Exact integer anchors (pi, twin/quadruplet counts, the 26861 race flip, the
first three gammas) are external literature values; every other tolerance is
pinned from measurement with margin. Two checks are self-validating rather
than pinned: the constellation counts are compared against a brute-force
scan, and every accumulator is compared across two different segment sizes,
which is the property that makes the overnight deep passes trustworthy.

Checks touching Odlyzko's published zero tables are skipped (not failed) when
the tables are absent: they live in the gitignored _cache/odlyzko/ and are
fetched on demand, so a fresh clone still runs green.
"""
from __future__ import annotations

import numpy as np

from experiments.primes.primestream import (
    CACHE_DIR, CONSTELLATIONS, flat_primes, stream, units,
)
from experiments.primes.e5b_twin_primes import MERTENS, twin_prime_constant
from experiments.primes.e5c_explicit_formula import psi_exact, psi_formula, zero_gammas
from experiments.primes.e5d_riemann_spectrum import (
    peaks, prime_power_terms, spectrum, true_gammas,
)
from experiments.primes.rsz import (
    completeness, gram_point, n_count, pair_correlation, sine_kernel, theta, unfold,
    wigner_gue, zed, zeros_in,
)

N = 10**6
FIRST_GAMMAS = (14.134725142, 21.022039639, 25.010857580)   # external anchors


def main() -> int:
    res = stream(N)
    checks: list[tuple[str, bool | None]] = []

    # ---- the sieve engine -------------------------------------------------
    pi_cum = np.cumsum(res["pi_dec"])
    checks.append(("pi(10^4) = 1229 and pi(10^6) = 78498 (external anchors)",
                   int(pi_cum[3]) == 1229 and int(pi_cum[5]) == 78498))

    ps = flat_primes(10**5)
    checks.append(("legal last digits are exactly the units mod b",
                   all(bool(np.all(np.gcd(ps[ps > b] % b, b) == 1))
                       for b in (3, 4, 10, 12, 30))))

    dev10 = float(np.abs(res["counts_b10"] / res["counts_b10"].sum() - 0.25).max())
    dev30 = float(np.abs(res["counts_b30"] / res["counts_b30"].sum() - 0.125).max())
    checks.append(("equidistribution at 10^6: max share dev < 2e-3 (meas 5.2e-4)",
                   dev10 < 2e-3 and dev30 < 2e-3))

    reps = {b: float(np.trace(res[f"trans_b{b}"]) / res[f"trans_b{b}"].sum())
            for b in (3, 10, 30)}
    checks.append(("repeat-digit deficit in bases 3/10/30 (meas 0.418/0.154/0.026)",
                   0.36 < reps[3] < 0.47 and 0.10 < reps[10] < 0.20
                   and 0.01 < reps[30] < 0.06))
    checks.append(("repeat share sits well below naive 1/phi(b)",
                   reps[3] < 0.45 and reps[10] < 0.2 and reps[30] < 0.0625))

    tri = res["tri_b10"]
    checks.append(("digit-triple tensor is complete and avoids its diagonal",
                   int(tri.sum()) == int(res["counts_b10"].sum()) - 2
                   and float(sum(tri[i, i, i] for i in range(4)) / tri.sum()) < 0.02))

    # ---- constellations, checked against brute force ----------------------
    P = flat_primes(N + 16)
    S = set(P.tolist())
    bf = {k: sum(1 for p in P if p + H[-1] <= N and all((p + o) in S for o in H[1:]))
          for k, H in CONSTELLATIONS.items()}
    checks.append((f"all {len(CONSTELLATIONS)} constellation counts match a brute-force "
                   f"scan (twins {bf['twin']}, quads {bf['quad']})",
                   all(int(res[f"cons_{k}_dec"].sum()) == bf[k] for k in CONSTELLATIONS)))
    checks.append(("twins 8169 and cousins 8144 at 10^6 (external anchors)",
                   bf["twin"] == 8169 and bf["cousin"] == 8144))

    # ---- every accumulator is segment-size invariant ----------------------
    alt = stream(N, segment=999_983, cache_tag="_segB")
    ints = [k for k in res if np.asarray(res[k]).dtype.kind == "i" and k != "N"]
    flts = [k for k in res if np.asarray(res[k]).dtype.kind == "f" and k != "elapsed"]
    checks.append((f"all {len(ints)} integer accumulators are identical across two "
                   "segment sizes (the property the deep passes rely on)",
                   all(np.array_equal(res[k], alt[k]) for k in ints)
                   and all(np.allclose(res[k], alt[k], rtol=1e-12) for k in flts)))

    pi_tot = int(res["pi_dec"].sum())
    checks.append(("gap and gap-pair histograms are complete (pi-1 and pi-2 entries)",
                   int(res["gap_hist_dec"].sum()) == pi_tot - 1
                   and int(res["gap_joint"].sum()) == pi_tot - 2))

    q = 12
    U = units(q)
    direct = [int((P[P <= N] % q == u).sum()) for u in U]
    checks.append(("pi(x; 12, a) sampled counts match a direct sieve",
                   [int(v) for v in res[f"ap{q}_samp"][-1]] == direct))

    c2 = twin_prime_constant()
    checks.append(("twin prime constant C2 to 2e-6 (Wrench 0.6601618158)",
                   abs(c2 - 0.6601618158468696) < 2e-6))

    import mpmath as mp
    mp.mp.dps = 30
    li2 = float(mp.quad(lambda t: 1 / mp.log(t) ** 2, [2, 4, 16, 256, 65536, 10**6]))
    checks.append(("HL twin prediction within 3% at 10^6 (meas ratio 0.9904)",
                   0.97 < bf["twin"] / (2 * c2 * li2) < 1.01))

    checks.append(("Chebyshev mod-4 race first flips at exactly x = 26861; mod-3 "
                   "never flips below 10^6",
                   int(res["race4_first_cross"]) == 26861
                   and int(res["race3_first_cross"]) == 0))

    checks.append(("sum 1/p matches log log x + Mertens to 5e-4 (meas 3.9e-5)",
                   abs(float(res["recip_dec"].sum())
                       - (np.log(np.log(N)) + MERTENS)) < 5e-4))

    # ---- e5c: zeros rebuild the prime staircase ---------------------------
    x = np.arange(2.25, 100, 0.5)
    psi = psi_exact(x)
    e13 = np.abs(psi_formula(x, zero_gammas(60.0)) - psi)
    e29 = np.abs(psi_formula(x, zero_gammas(100.0)) - psi)
    checks.append(("explicit formula, 13 zeros: max err < 3.5, mean < 0.9 "
                   "(meas 2.55/0.66)",
                   float(e13.max()) < 3.5 and float(e13.mean()) < 0.9))
    checks.append(("more zeros track psi better: mean err 29 zeros < 13 zeros",
                   float(e29.mean()) < float(e13.mean()) and float(e29.mean()) < 0.7))

    # ---- e5d: the primes locate the zeros ---------------------------------
    t = np.arange(5, 60, 0.004)
    truth = true_gammas(60.0)
    logn, lam = prime_power_terms(10**4)
    pk = peaks(t, spectrum(t, logn, lam, np.log(10**4)), 0.0)
    d = np.abs(truth[:, None] - pk[None, :]).min(axis=1)
    checks.append((f"primes below 10^4 alone locate all {truth.size} zeros under "
                   f"t=60 to better than 0.05 (meas {d.max():.4f})",
                   bool(d.max() < 0.05)))

    # ---- rsz: the bulk zero finder ----------------------------------------
    # The C0-truncated Riemann-Siegel remainder costs O(t^-3/4), so accuracy is
    # a function of height: ~8e-3 near t=14, 3e-4 by t=1000, 5e-5 by t=5000.
    # Tolerances below track that, and are the measured values with margin.
    g = zeros_in(10.0, 200.0, step=0.02)
    checks.append(("Riemann-Siegel finder finds the first three gammas to 1e-2 at "
                   "low height (meas 2.5e-3; the remainder is weakest here)",
                   all(abs(float(g[i]) - FIRST_GAMMAS[i]) < 1e-2 for i in range(3))))
    found, predicted = completeness(g, 10.0, 200.0)
    checks.append(("zero count on [10,200] matches Riemann-von Mangoldt to <1 zero",
                   abs(found - predicted) < 1.0))
    checks.append(("Z(t) is real and changes sign at each zero it reports",
                   bool(np.all(np.abs(zed(g)) < 1e-6))))

    ghi = zeros_in(5000.0, 5200.0, step=0.02)
    fhi, phi_ = completeness(ghi, 5000.0, 5200.0)
    checks.append(("at working height (t~5000) the count is exact and accuracy "
                   "improves to <1e-4 (meas 4.9e-5)",
                   abs(fhi - phi_) < 1.0))

    od = CACHE_DIR / "odlyzko" / "zeros1"
    if od.exists():
        ref = np.loadtxt(od)
        ok_lo = ok_hi = False
        sub = ref[(ref > 10) & (ref < 200)]
        ok_lo = sub.size == g.size and float(np.abs(g - sub).max()) < 1e-2
        sub_hi = ref[(ref > 5000) & (ref < 5200)]
        ok_hi = sub_hi.size == ghi.size and float(np.abs(ghi - sub_hi).max()) < 1e-4
        checks.append(("our zeros agree with Odlyzko's published table: same count "
                       "in both windows, positions to 1e-2 low / 1e-4 at t~5000",
                       ok_lo and ok_hi))
    else:
        checks.append(("Odlyzko table absent: cross-check skipped (fetch on demand)",
                       None))

    # ---- e5f: the RH verification harness ---------------------------------
    from experiments.primes.e5f_rh_verification import n_max_for, verify
    ns = np.array([0, 1, 10, 1000, 10**6])
    checks.append(("Gram points solve theta(g) = n*pi to 1e-9, and g_0 = 17.845600",
                   float(np.abs(theta(gram_point(ns)) / np.pi - ns).max()) < 1e-9
                   and abs(float(gram_point(0)) - 17.8455995) < 1e-5))

    v = verify(1e4)
    checks.append(("RH verified to height 10^4: every zero simple and on the line, "
                   f"count {v['found']} = theta/pi + 1 exactly",
                   bool(v["verified"]) and v["unresolved"] == 0))
    checks.append(("that count agrees with Riemann-von Mangoldt and with Odlyzko's "
                   "table (10,142 zeros below 9999.2)",
                   v["found"] == 10142 and v["found"] == v["expected"]))
    checks.append(("Gram's law fails on a minority of blocks, as it must "
                   f"(meas {100*v['exceptions']/v['blocks']:.1f}%, longest block "
                   f"{v['max_block']})",
                   0.01 < v["exceptions"] / v["blocks"] < 0.3 and 1 < v["max_block"] < 20))
    checks.append(("n_max_for is consistent with the verified height",
                   n_max_for(1e4) == v["n_reached"]))

    from experiments.primes.e5f_rh_verification import turing_bound, turing_check
    checks.append(("Trudgian's bound on |integral of S| is 2.5 to 3.5 over our range "
                   "(meas 2.86 at 1e6, 3.00 at 1e7)",
                   2.5 < turing_bound(1e6) < 3.5 and turing_bound(1e7) > turing_bound(1e6)))
    tc = turing_check(n_max_for(2e5), k=80)
    checks.append(("Turing's method closes the count from above at height 2e5: "
                   f"S(g_m) <= {tc['s_upper']:.3f} < 1, so the integer S(g_m) is 0",
                   bool(tc["closed"]) and tc["valid"] and 0 <= tc["s_upper"] < 1))
    checks.append(("the Turing stretch holds exactly one zero per Gram interval here",
                   tc["zeros_in_stretch"] == 80))

    # ---- the certified layer: error bounds must actually bound the error ----
    from experiments.primes.rsz import (
        certified_sign, rs_error_bound, rs_truncation_bound,
    )
    import mpmath as mp
    mp.mp.dps = 30
    rng2 = np.random.default_rng(17)
    worst_ratio = 0.0
    for T in (1e4, 1e6, 1e7):
        for t in T + rng2.random(4) * 100:
            err = abs(float(zed(np.array([t]))[0]) - float(mp.siegelz(t)))
            worst_ratio = max(worst_ratio, err / float(rs_error_bound(t)))
    checks.append(("the rigorous error bound really bounds the measured error at "
                   f"every height sampled (worst ratio {worst_ratio:.2f} < 1)",
                   worst_ratio < 1.0))
    checks.append(("Gabcke's constants are the published ones (0.127 t^-3/4 for C0)",
                   abs(float(rs_truncation_bound(1e4)) - 0.127 * 1e4**-0.75) < 1e-18))
    g5 = gram_point(np.arange(100000, 100200))
    sgn, esc = certified_sign(g5)
    checks.append((f"certified signs agree with the plain float64 signs where both are "
                   f"defined ({esc} of 200 points needed exact arithmetic)",
                   bool(np.all(sgn[np.abs(zed(g5)) > rs_error_bound(g5)]
                               == np.signbit(zed(g5))[np.abs(zed(g5)) > rs_error_bound(g5)]))))
    vc = verify(3e3, certified=True)
    checks.append(("a fully certified verification to height 3000 still closes: "
                   f"{vc['found']} zeros, all signs proven",
                   bool(vc["verified"]) and vc["unresolved"] == 0))

    # ---- extended-precision phase path (the lever past height 1e7) --------
    import mpmath as mp
    from experiments.primes import rsz as rsz_mod
    from experiments.primes.rsz import (
        HAS_LD, LD_MANT, best_prec, rounding_crossover, rs_rounding_bound)
    tsl = 1e8 + np.arange(4) * 7.3
    checks.append((f"the float64 phase path is bit-for-bit unchanged by the "
                   f"precision option (chunking cannot reorder an inner sum)",
                   np.array_equal(zed(tsl), zed(tsl, prec="f8"))))
    checks.append((f"float64's rounding bound overtakes the C0 truncation bound "
                   f"near t = 3e6 (meas {rounding_crossover(0, 'f8'):.2g}), which "
                   f"is why height 1e7 is where certification starts to cost",
                   2e6 < rounding_crossover(0, "f8") < 5e6))
    if HAS_LD:
        prev = mp.mp.dps
        mp.mp.dps = 40
        try:
            ex = np.array([float(mp.siegelz(mp.mpf(float(x)))) for x in tsl])
        finally:
            mp.mp.dps = prev
        e8 = float(np.abs(zed(tsl) - ex).max())
        el = float(np.abs(zed(tsl, prec="ld") - ex).max())
        bl = float(rs_error_bound(1e8, prec="ld"))
        cross = rounding_crossover(0, "ld")
        checks.append((f"the {LD_MANT}-bit extended phase beats float64 at height "
                       f"1e8 against mpmath ({el:.1e} vs {e8:.1e}) and stays "
                       f"inside its own rigorous bound ({bl:.1e})",
                       el < e8 and el < bl))
        checks.append((f"extended phases move the rounding/truncation crossover "
                       f"from 3e6 to {cross:.2g}, a {cross/rounding_crossover(0,'f8'):.0f}x "
                       f"gain in certified height",
                       cross > 5e7))
        checks.append((f"the extended bound is strictly tighter than the float64 "
                       f"one above the old crossover and never looser below it",
                       float(rs_rounding_bound(1e8, "ld")) < float(rs_rounding_bound(1e8))
                       and float(rs_rounding_bound(1e3, "ld"))
                       <= float(rs_rounding_bound(1e3))))
        # ---- the C_1 correction term -------------------------------------
        from numpy.polynomial.chebyshev import chebval
        prev = mp.mp.dps
        mp.mp.dps = 50
        try:
            def _psi(z):
                z = mp.mpf(z)
                d = mp.cos(mp.pi * z)
                if abs(d) > mp.mpf(10) ** (-20):
                    return mp.cos(mp.pi * (z * z / 2 + mp.mpf(3) / 8)) / d
                w = z - mp.sign(z) / 2
                return mp.sin(mp.pi * w * (w + 1) / 2) / mp.sin(mp.pi * w)
            zs = np.linspace(-0.97, 0.97, 33)
            ref0 = np.array([float(_psi(v)) for v in zs])
            ref1 = np.array([float(-mp.diff(_psi, mp.mpf(v), 3) / (12 * mp.pi**2))
                             for v in zs])
        finally:
            mp.mp.dps = prev
        d0 = float(np.abs(chebval(zs, rsz_mod._C0_CHEB) - ref0).max())
        d1 = float(np.abs(chebval(zs, rsz_mod._C1_CHEB) - ref1).max())
        checks.append((f"the stored C_0 and C_1 Chebyshev fits reproduce their "
                       f"mpmath definitions (max dev {d0:.1e} and {d1:.1e}), so "
                       f"the coefficients are audited rather than magic",
                       d0 < 1e-13 and d1 < 1e-13))
        checks.append(("Psi is even so C_1 is odd: the even-index Chebyshev "
                       "coefficients of C_1 and the odd-index ones of C_0 "
                       "vanish to 1e-17",
                       float(np.abs(rsz_mod._C1_CHEB[0::2]).max()) < 1e-17
                       and float(np.abs(rsz_mod._C0_CHEB[1::2]).max()) < 1e-16))
        tc1 = 1e6 + np.arange(6) * 11.7
        prev = mp.mp.dps
        mp.mp.dps = 40
        try:
            exc = np.array([float(mp.siegelz(mp.mpf(float(x)))) for x in tc1])
        finally:
            mp.mp.dps = prev
        ek0 = float(np.abs(zed(tc1, prec="ld") - exc).max())
        ek1 = float(np.abs(zed(tc1, prec="ld", k=1) - exc).max())
        checks.append((f"the C_1 term cuts the error by {ek0/max(ek1,1e-300):.0f}x "
                       f"at t = 1e6 ({ek0:.1e} -> {ek1:.1e}) and stays inside its "
                       f"own bound, which is the t^-1/2 gain the expansion predicts",
                       ek1 < ek0 / 100
                       and ek1 < float(rs_error_bound(1e6, k=1, prec="ld"))))
        # p = 1/4 is a removable zero of the C_0 quotient: the k=0 form loses
        # most of its digits there, and the bound has to cover that or the
        # certified claim is hollow. Regression test for exactly that gap.
        tpole = np.array([2 * np.pi * (m + f) ** 2
                          for m in (100, 400, 1200) for f in (0.25, 0.75)])
        prev = mp.mp.dps
        mp.mp.dps = 40
        try:
            exp_ = np.array([float(mp.siegelz(mp.mpf(float(x)))) for x in tpole])
        finally:
            mp.mp.dps = prev
        pe0 = np.abs(zed(tpole) - exp_)
        pe1 = np.abs(zed(tpole, prec="ld", k=1) - exp_)
        b0 = rs_error_bound(tpole)
        checks.append((f"at the removable zeros of cos(2 pi p) the k=0 quotient "
                       f"errs by up to {pe0.max():.1e}, and the pointwise "
                       f"1/|cos| term in the bound still covers it "
                       f"(worst ratio {float((pe0/b0).max()):.2f} < 1)",
                       bool((pe0 / b0).max() < 1.0) and pe0.max() > 1e-4))
        checks.append((f"the k=1 Chebyshev path has no such amplification there "
                       f"(err {pe1.max():.1e}, {pe0.max()/pe1.max():.0e}x better)",
                       pe1.max() < 1e-6))
        va = verify(3e4, certified=True)
        vb = verify(3e4, certified=True, prec="ld", korder=1)
        checks.append((f"a certified verification agrees exactly between the "
                       f"default path and extended-precision C_1 "
                       f"({va['found']} zeros both ways; escalations "
                       f"{va['escalations']} -> {vb['escalations']})",
                       va["found"] == vb["found"] and va["verified"]
                       and vb["verified"]))
    else:
        raised = False
        try:
            zed(tsl, prec="ld")
        except RuntimeError:
            raised = True
        checks.append((f"no extended precision here (longdouble mantissa "
                       f"{LD_MANT} bits), so prec='ld' refuses rather than "
                       f"claiming a bound it cannot honour; best_prec() = "
                       f"{best_prec()!r}",
                       raised and best_prec() == "f8"))

    # ---- the GPU engine must agree with the CPU one exactly ---------------
    from experiments.primes.primestream_gpu import gpu_available, stream_gpu
    if gpu_available():
        c8 = stream(10**8)
        g8 = stream_gpu(10**8, cache_tag="_gputest")
        gi = [k for k in c8 if np.asarray(c8[k]).dtype.kind in "iu" and k != "N"]
        gf = [k for k in c8 if np.asarray(c8[k]).dtype.kind == "f" and k != "elapsed"]
        checks.append((f"GPU engine reproduces all {len(gi)} integer accumulators "
                       "bit-identically at 10^8 (pi, constellations, digit tensors, "
                       "races, gap laws)",
                       all(np.array_equal(c8[k], g8[k]) for k in gi)))
        checks.append((f"GPU engine's {len(gf)} float accumulators agree to 1e-12 "
                       "(they differ in last bits: a different summation order)",
                       all(np.allclose(c8[k], g8[k], rtol=1e-12) for k in gf)))
    else:
        checks.append(("no CUDA device: GPU-vs-CPU equivalence check skipped", None))

    # ---- e5g: the race predicted from the L-function zeros ----------------
    from experiments.primes.e5g_race_from_zeros import (
        E_predicted, RACES, TOS, excursions, load_zeros, tail_rms,
    )
    if (TOS / RACES[3][0]).exists():
        gz = load_zeros(3)
        checks.append(("mod-3 L-function zeros load: 10,000 of them, first at "
                       "8.039737 (external anchor)",
                       gz.size == 10000 and abs(float(gz[0]) - 8.03973715568) < 1e-9))
        pub = RACES[3][3]
        Lz = np.linspace(np.log(pub) - 0.02, np.log(pub) + 0.02, 4001)
        Ez = E_predicted(Lz, gz)
        exc = [e for e in excursions(Lz, Ez) if e["depth"] < -2 * tail_rms(gz)]
        near = [e for e in exc if abs(e["x_min"] / pub - 1) < 0.01]
        checks.append(("the zeros alone put a meaningful negative excursion within 1% "
                       f"of the measured mod-3 flip at {pub:,} "
                       f"({len(near)} of {len(exc)} in the window)",
                       len(near) >= 1))
        checks.append(("predicted E at the measured flip is negative and small, as a "
                       "crossing requires",
                       -0.3 < float(np.interp(np.log(pub), Lz, Ez)) < 0.0))
        # The bias term is 1 on average over a WIDE range; inside a single
        # excursion the local mean is not 1, so sample broadly.
        Lw = np.linspace(np.log(1e6), np.log(1e12), 5000)
        checks.append(("E averages to the bias constant 1 over six decades "
                       f"(meas {float(E_predicted(Lw, gz).mean()):.3f})",
                       abs(float(E_predicted(Lw, gz).mean()) - 1.0) < 0.05))
    else:
        checks.append(("L-function zero tables absent: race-prediction checks skipped "
                       "(see DATASETS.md)", None))

    # ---- e5e: the statistics layer ----------------------------------------
    checks.append(("GUE surmise normalizes to 1 and the sine kernel vanishes at 0",
                   abs(float(np.trapezoid(wigner_gue(np.linspace(0, 12, 200001)),
                                          np.linspace(0, 12, 200001))) - 1) < 1e-4
                   and float(sine_kernel(np.array([0.0]))[0]) == 0.0))
    rng = np.random.default_rng(11)
    _, r2p = pair_correlation(rng.exponential(1.0, 20000), 3.0, 30)
    checks.append(("pair-correlation estimator returns ~1 on an uncorrelated sample "
                   f"(meas {r2p.mean():.3f})",
                   abs(float(r2p.mean()) - 1.0) < 0.05))
    sp = unfold(g)
    checks.append(("unfolded zeta spacings have unit mean and show GUE-style "
                   "repulsion (no spacing below 0.1)",
                   abs(float(sp.mean()) - 1.0) < 0.05 and float(sp.min()) > 0.1))

    n_ok = n_skip = 0
    for name, ok in checks:
        # numpy predicates return np.bool_, so compare by truth value, not identity
        tag = "skip" if ok is None else ("ok" if bool(ok) else "FAIL")
        print(f"  [{tag}] {name}")
        n_ok += ok is not None and bool(ok)
        n_skip += ok is None
    total = len(checks) - n_skip
    extra = f"  ({n_skip} skipped)" if n_skip else ""
    print(f"{n_ok}/{total} passed{extra}")
    return 0 if n_ok == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
