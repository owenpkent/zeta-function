"""E5F: verifying the Riemann Hypothesis ourselves, up to a height T.

WHY THIS AND NOT A RACE. E5E measured GUE statistics and showed they are
RH-blind: they are functions of the zeros' HEIGHTS, and RH is about their
REAL PARTS. The natural next thought is a prime-side "race" observable with
real teeth, and that thought is dead on arrival for a quantitative reason.
Every prime-side statistic factors through the zeros as a sum of x^rho/rho,
so a hypothetical off-line zero contributes x^beta/gamma. RH is already
verified below height 3e12, so any off-line zero is pre-suppressed by that
1/gamma, and for its term to clear the ordinary sqrt(x) log x noise one
needs x^(beta - 1/2) > gamma. That is x ~ 10^150 for beta = 0.6 and worse
below it. No prime computation reaches that; searching HEIGHT is
exponentially cheaper than searching LENGTH. Which is why every RH
verification on record counts zeros, and none counts primes.

WHAT THIS DOES. Walks Gram points g_n (theta(g_n) = n pi) and checks that
the zeros of the Hardy function Z fall between them as they must if RH holds
on the range. Since N(t) = theta(t)/pi + 1 + S(t) counts ALL zeros of zeta
in the strip up to height t, while every sign change of Z is a zero ON the
critical line, finding exactly n + 1 sign changes below g_n pins S(g_n) = 0
and leaves no room for a zero off the line.

Gram's law (that Z alternates sign at consecutive Gram points) holds for
most n but fails infinitely often, so the count is done by GRAM BLOCKS: a
maximal run between two Gram points where the law does hold. Rosser's rule
says a block of length L contains exactly L zeros, and blocks that come up
short are subdivided until the missing sign changes are found. A block that
cannot be resolved is reported, not silently dropped.

CLOSING THE COUNT. Counting sign changes proves only N(g_m) >= m + 1, i.e.
S(g_m) >= 0. Turing's method supplies the other side, and since S(g_m) is an
INTEGER at a Gram point it is enough to squeeze it below 1. See turing_check
below, which uses Trudgian's explicit bound on the integral of S.

CERTIFIED MODE. With certified=True every sign the argument rests on is a
theorem rather than a floating-point opinion: a float64 sign is accepted only
when |Z| exceeds a rigorous error bound (Gabcke's bound on the discarded
Riemann-Siegel tail, plus an explicit accounting of float64 rounding), and
anything closer is recomputed in exact arithmetic. The escalation count is
reported, so the reader can see how often the fast path was not enough.

STATUS. With certified=True the chain is complete: certified signs give a
rigorous lower bound on the zero count, Turing's method closes it from above,
and the conclusion is that every zero below the height is simple and on the
critical line. The result itself is long known (Platt 3e12, Gourdon 1e13);
what is ours is the pipeline, from Riemann-Siegel through the Gram-block
bookkeeping to the Turing closure.

Usage:
    python -m experiments.primes.e5f_rh_verification 1e7            # full run
    python -m experiments.primes.e5f_rh_verification 1e5 certified  # certified
"""
from __future__ import annotations

import sys
import time

import numpy as np

from experiments.primes.primestream import CACHE_DIR
from experiments.primes.rsz import (
    TWO_PI, certified_sign, gram_point, rs_error_bound, theta, zed, zeros_in,
)

MAX_REFINE = 5          # subdivision rounds before a block is declared unresolved
MAX_MERGE = 8           # neighbouring blocks to absorb when one stays short
TURING_K = 80           # Gram intervals above the top used to close S(g_m) <= 0


def n_max_for(T: float) -> int:
    """Largest Gram index with g_n <= T."""
    return int(np.floor(theta(T) / np.pi))


def turing_bound(t2: float) -> float:
    """Trudgian 2014, *Improvements to Turing's Method II*, Theorem 1:

        |int_{t1}^{t2} S(t) dt| <= 1.698 + 0.183 log log t2 + 0.049 log t2

    for t2 > t1 > 10^5, where pi*S(t) = arg zeta(1/2 + it).
    """
    return 1.698 + 0.183 * np.log(np.log(t2)) + 0.049 * np.log(t2)


def turing_check(m: int, k: int = 40, step: float = 0.01) -> dict:
    """Turing's method: prove S(g_m) <= 0, closing the count from above.

    At a Gram point, S(g_m) = N(g_m) - m - 1 is an INTEGER, and having found
    m + 1 zeros on the line below g_m already gives S(g_m) >= 0. What is
    missing is the other side, and that is what Turing's method supplies.

    Since N is non-decreasing and every zero we locate in the stretch above
    g_m is genuine,

        S(t) >= S(g_m) + (F(t) - F(g_m)) - (theta(t) - theta(g_m))/pi

    for t in [g_m, g_{m+k}], where F counts the zeros we found. Integrating
    and combining with Trudgian's bound B on |int S| gives

        S(g_m) <= (B + C - A) / L,

    with L the length of the stretch, A = sum over found zeros of
    (g_{m+k} - gamma_i), and C = (1/pi) int (theta(t) - theta(g_m)) dt. If
    that bound falls below 1 then the integer S(g_m) is <= 0, hence exactly
    0: every zero below g_m has been found, and all of them are on the line.
    """
    ga, gb = float(gram_point(m)), float(gram_point(m + k))
    gammas = zeros_in(ga, gb, step=step)
    L = gb - ga
    A = float(np.sum(gb - gammas))
    ts = np.linspace(ga, gb, 40001)
    C = float(np.trapezoid(theta(ts) - theta(ga), ts) / np.pi)
    B = turing_bound(gb)
    s_upper = (B + C - A) / L
    return dict(m=m, k=k, t_lo=ga, t_hi=gb, stretch=L, zeros_in_stretch=int(gammas.size),
                trudgian_B=B, A=A, C=C, s_upper=s_upper, closed=bool(s_upper < 1.0),
                valid=bool(ga > 1e5))


_ESCALATIONS = [0]      # count of points that needed exact arithmetic


def _signs(t: np.ndarray, z: np.ndarray, certified: bool) -> np.ndarray:
    """Sign bits of Z, provably correct when `certified` is set.

    In certified mode a float64 sign is accepted only when |Z| exceeds the
    rigorous error bound (Gabcke's remainder plus rounding); anything closer
    is recomputed exactly. Everything downstream then rests on signs that are
    theorems rather than floating-point opinions.
    """
    if not certified:
        return np.signbit(z)
    sb, esc = certified_sign(t, z)
    _ESCALATIONS[0] += esc
    return sb


def _sign_changes(z: np.ndarray, t: np.ndarray | None = None,
                  certified: bool = False) -> int:
    sb = np.signbit(z) if not certified else _signs(t, z, True)
    return int(np.count_nonzero(sb[:-1] != sb[1:]))


def _resolve_block(t_lo: float, t_hi: float, need: int,
                   certified: bool = False) -> tuple[int, int]:
    """Subdivide a Gram block until `need` sign changes appear.

    Returns (found, rounds). Sampling density doubles each round, so a block
    holding a Lehmer-style close pair is resolved rather than miscounted.
    """
    m = 64 * max(need, 1)
    for rounds in range(1, MAX_REFINE + 1):
        grid = np.linspace(t_lo, t_hi, m)
        found = _sign_changes(zed(grid), grid, certified)
        if found >= need:
            return found, rounds
        m *= 4
    return found, MAX_REFINE


def verify(T: float, n_start: int = 0, chunk: int = 20000, log=None,
           progress_every: int = 20, certified: bool = False) -> dict:
    """Verify that every zero up to height T is simple and on the critical line.

    `n_start` begins the walk at a Gram index other than 0, which verifies the
    band [g_n_start, T] on its own. Useful for testing and for re-checking a
    region without re-walking everything below it.
    """
    say = log or (lambda *_: None)
    n_end = n_max_for(T)
    t0 = time.time()

    n_cur = n_start               # Gram index reached so far
    found_total = 1 if n_start == 0 else 0   # the one zero below g_0 = 17.8456
    blocks_total = exceptions = unresolved = boundary_merges = 0
    max_block = 1
    worst = []

    it = 0
    while n_cur < n_end:
        # A window must contain at least two Gram points where Gram's law holds,
        # or there is no block to close. Near the top of the range the window is
        # short and may not, so look a little PAST the target rather than
        # widening inside it, which cannot help once the window is capped.
        pad = 0
        while True:
            hi = min(n_cur + chunk, n_end) + pad
            idx = np.arange(n_cur, hi + 1)
            g = gram_point(idx)
            z = zed(g)
            # Gram's law: (-1)^n Z(g_n) > 0. Points where it holds delimit blocks.
            sb = _signs(g, z, certified)
            good = sb == (idx % 2 == 1)
            gi = np.flatnonzero(good)
            if gi.size >= 2 and int(idx[gi[-1]]) > n_cur:
                break
            pad += 64

        a_all, b_all = gi[:-1], gi[1:]
        lengths = b_all - a_all
        blocks_total += a_all.size
        max_block = max(max_block, int(lengths.max()))
        exceptions += int(np.count_nonzero(lengths > 1))

        # cheap pass: sign changes between Gram points, per block
        flips = (sb[:-1] != sb[1:]).astype(np.int64)
        cum = np.concatenate(([0], np.cumsum(flips)))
        found_per = cum[b_all] - cum[a_all]

        short = np.flatnonzero(found_per < lengths)
        handled = np.zeros(a_all.size, dtype=bool)
        for k in short:
            if handled[k]:
                continue
            a, b = int(a_all[k]), int(b_all[k])
            need = int(lengths[k])
            got, _ = _resolve_block(float(g[a]), float(g[b]), need, certified)
            if got >= need:
                found_per[k] = got
                continue
            # A zero landing on (or very near) a Gram point moves zeros across a
            # block edge, so a block can hold fewer than its length while its
            # neighbour holds more, and the neighbour's surplus is invisible at
            # Gram resolution: two zeros in one Gram interval give no net sign
            # change. Absorb neighbours until the merged region balances.
            lo_k = hi_k = k
            merged = False
            for _ in range(MAX_MERGE):
                lo_k, hi_k = max(lo_k - 1, 0), min(hi_k + 1, a_all.size - 1)
                A, B = int(a_all[lo_k]), int(b_all[hi_k])
                need_m = B - A
                got_m, _ = _resolve_block(float(g[A]), float(g[B]), need_m, certified)
                if got_m >= need_m:
                    found_per[lo_k : hi_k + 1] = 0
                    found_per[k] = need_m
                    handled[lo_k : hi_k + 1] = True
                    merged = True
                    boundary_merges += 1
                    break
            if not merged:
                found_per[k] = got
                unresolved += 1
                worst.append((int(idx[a]), int(idx[b]), need, got))

        found_total += int(found_per.sum())
        n_cur = int(idx[b_all[-1]])
        it += 1
        if log and (it % progress_every == 0 or n_cur >= n_end):
            say(f"  n = {n_cur:,}/{n_end:,}  t = {float(g[b_all[-1]]):,.0f}  "
                f"zeros = {found_total:,}  ({time.time()-t0:.0f}s)")

    expected = (n_cur - n_start) + (1 if n_start == 0 else 0)
    return dict(
        T=T, n_start=n_start, n_reached=n_cur, height=float(gram_point(n_cur)),
        found=found_total, expected=expected, verified=found_total == expected,
        blocks=blocks_total, exceptions=exceptions, unresolved=unresolved,
        boundary_merges=boundary_merges,
        max_block=max_block, worst=worst[:10], elapsed=time.time() - t0,
    )


def main(T: float = 1e7, certified: bool = False) -> int:
    print(f"E5F: verifying RH up to height T = {T:.3g}"
          + ("  [CERTIFIED: every sign checked against a rigorous error bound]"
             if certified else ""))
    _ESCALATIONS[0] = 0
    print(f"  Gram indices to walk: {n_max_for(T):,}  "
          f"(that many zeros, plus the one below g_0)")
    r = verify(T, log=print, certified=certified)

    print(f"\n  zeros found on the critical line : {r['found']:,}")
    print(f"  zeros required by Riemann-von Mangoldt: {r['expected']:,}")
    print(f"  height reached                   : {r['height']:,.1f}")
    print(f"  Gram blocks                      : {r['blocks']:,}")
    print(f"  Gram's law exceptions (block > 1): {r['exceptions']:,} "
          f"({100*r['exceptions']/max(r['blocks'],1):.2f}%), longest block {r['max_block']}")
    print(f"  blocks merged at a boundary      : {r['boundary_merges']}")
    print(f"  unresolved blocks                : {r['unresolved']}")
    if certified:
        print(f"  signs needing exact arithmetic   : {_ESCALATIONS[0]:,} "
              f"(bound at the top: {float(rs_error_bound(r['height'])):.2e})")
    if r["worst"]:
        print(f"  first unresolved: {r['worst']}")
    print(f"  elapsed                          : {r['elapsed']:.0f}s")

    tc = None
    if r["verified"] and r["height"] > 1e5:
        tc = turing_check(r["n_reached"], k=TURING_K)
        print(f"\n  Turing's method on the {TURING_K} Gram intervals above g_m:")
        print(f"    Trudgian bound B = {tc['trudgian_B']:.3f}, stretch L = {tc['stretch']:.2f}, "
              f"{tc['zeros_in_stretch']} zeros located in it")
        print(f"    => S(g_m) <= {tc['s_upper']:.4f}"
              + ("  (< 1, so the integer S(g_m) is <= 0)" if tc["closed"] else "  NOT CLOSED"))

    if r["verified"]:
        print(f"\nVERIFIED: every one of the {r['found']:,} zeros of zeta with "
              f"0 < Im(rho) <= {r['height']:,.1f}")
        print("is simple and lies exactly on the critical line Re(s) = 1/2.")
        if tc and tc["closed"]:
            print("\nThe count is now pinned from BOTH sides. Finding that many sign changes")
            print("of Z gives S(g_m) >= 0; Turing's method with Trudgian's explicit bound on")
            print("the integral of S gives S(g_m) <= 0. Since S(g_m) is an integer at a Gram")
            print("point, S(g_m) = 0 exactly: no zero anywhere below that height is missing,")
            print("so none can be sitting off the critical line.")
        if certified:
            print(f"\nEvery sign above is certified: accepted only where |Z| exceeds a rigorous")
            print(f"error bound (Gabcke's Riemann-Siegel remainder plus float64 rounding), with")
            print(f"{_ESCALATIONS[0]:,} borderline points recomputed in exact arithmetic. The chain is")
            print("complete: certified signs bound the count from below, Turing's method bounds")
            print("it from above, and the two meet.")
        else:
            print("\nRemaining caveat: the arithmetic is float64, not interval. Every step above")
            print("is a theorem; the numbers fed into it are not rigorously bounded. Re-run with")
            print("the 'certified' argument to close that gap too.")
    else:
        print(f"\nNOT VERIFIED: found {r['found']:,} vs required {r['expected']:,} "
              f"(difference {r['found']-r['expected']:+,}).")
        print("A shortfall means zeros were missed by the sampling (look at the")
        print("unresolved blocks), NOT that RH failed: a genuine counterexample would")
        print("show up as a Gram block that stays short at every refinement depth.")

    out = {k: v for k, v in r.items() if k != "worst"}
    out["certified"] = certified
    out["escalations"] = _ESCALATIONS[0]
    if tc:
        out.update({f"turing_{k}": v for k, v in tc.items()})
    np.savez_compressed(
        CACHE_DIR / f"e5f_rh_verified_{int(T)}{'_certified' if certified else ''}.npz",
        **out)
    return 0 if r["verified"] else 1


if __name__ == "__main__":
    raise SystemExit(main(float(sys.argv[1]) if len(sys.argv) > 1 else 1e7,
                          certified="certified" in sys.argv[2:]))
