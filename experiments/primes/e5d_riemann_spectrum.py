"""E5D: the primes know the zeros. Recovering gamma from prime data alone.

QUESTION. E5C ran the explicit formula forwards: zeros rebuild the prime
staircase. Does it run BACKWARDS? Can the primes, with no zeta evaluation
anywhere in the pipeline, tell us where the nontrivial zeros are?

METHOD. The Dirichlet series of the logarithmic derivative,
-zeta'/zeta(s) = sum_n Lambda(n) n^{-s}, has a simple pole at every
nontrivial zero rho, with residue -1 (zeta VANISHES at rho, so zeta'/zeta
~ +1/(s-rho)). Approaching the critical line from the right,
Re[-zeta'/zeta(sigma+it)] near rho = 1/2 + i*gamma is an inverted
Lorentzian in t, a trough at t = gamma of depth 1/(sigma-1/2). Truncating
the series at n <= X with a Fejer weight (1 - log n/log X) acts like an
effective sigma - 1/2 ~ 1/log X, so

    Phi_X(t) = -sum_{n <= X} Lambda(n) n^{-1/2} cos(t log n)(1 - log n/log X)

(note the leading minus, which turns those troughs into peaks) should show
a peak at every gamma. The input is ONLY prime powers and their logs. No
zeta values, no zeros, nothing analytic: just the primes.

RELATION TO PRIOR WORK IN THIS REPO. Two neighbours, neither duplicated.
(i) experiments/positivity/e3s_connes_eta.py recovers zeros from prime data
by a different route (Connes' Weil quadratic form, roots of the minimal
eigenvector's Fourier transform) and already found that the recovery is not
zeta-specific: it reproduces Davenport-Heilbronn's ON-LINE zeros just as
well. (ii) The overnight stream2 CCM probe evaluated the RAW sum
sum_{p^k<=x} (log p) cos(t log p^k) p^{-k/2} at fixed t = gamma_1 and found
it does NOT converge as x grows: it oscillates without a limit. That is
consistent with what is measured below and worth stating precisely, because
it is the sharpest thing here: the raw sum at a FIXED t has no limit, but
the Fejer-regularized transform's PEAK LOCATION is still a good estimator
of gamma. The zero is encoded in where the resonance sits, not in the value
of any one sum. Section [A] measures how good: every zero in the window is
found at every cutoff, with the error falling from ~5e-3 at X = 10^3 to
~1e-3 at X = 10^5 and then flattening rather than continuing down, which is
the pointwise non-convergence showing through. This is an accurate
estimator, not a convergent one.

THE CONTROL (the point, for this repo). This construction uses exactly one
structural fact: that Lambda is supported on prime powers, i.e. the Euler
product. It does not use the functional equation or the additive lattice.
So it must work identically for a Beurling generalized-prime system, which
has an Euler product and no lattice, and it does. The Beurling spectrum has
peaks of its own, at its own zeros, which lie wherever they lie. Recovering
a spectrum from an Euler product is therefore NOT evidence for a critical
line: the transform is blind to the very question RH asks. That is the
Beurling discipline (experiments/_shared/beurling.py) applied to the
prettiest positive result on this page.
"""
from __future__ import annotations

import sys

import numpy as np
import mpmath as mp

from experiments._shared.beurling import BeurlingSystem
from experiments.primes.primestream import CACHE_DIR, flat_primes

T_LO, T_HI, DT = 5.0, 100.0, 0.002


def prime_power_terms(X: int) -> tuple[np.ndarray, np.ndarray]:
    """(log n, Lambda(n)) over prime powers n = p^k <= X."""
    logs, lam = [], []
    for p in flat_primes(int(X)):
        lp, pk = np.log(float(p)), int(p)
        while pk <= X:
            logs.append(np.log(float(pk)))
            lam.append(lp)
            pk *= int(p)
    return np.asarray(logs), np.asarray(lam)


def beurling_terms(X: float, prime_bound: int | None = None) -> tuple[np.ndarray, np.ndarray]:
    """Same, for the density-matched Beurling fake: generalized prime powers."""
    logX = np.log(X)
    prime_bound = int(X) if prime_bound is None else prime_bound
    logs, lam = [], []
    for lb in BeurlingSystem(prime_bound=prime_bound).logs:
        u = lb
        while u <= logX:
            logs.append(u)
            lam.append(lb)
            u += lb
    return np.asarray(logs), np.asarray(lam)


def spectrum(t: np.ndarray, logn: np.ndarray, lam: np.ndarray, logX: float,
             chunk: int = 256) -> np.ndarray:
    """Phi_X(t): Fejer-weighted, half-line-normalized cosine transform.

    The leading minus makes the zeros peaks rather than troughs: the residue
    of -zeta'/zeta at a zero is -1.
    """
    w = lam * np.exp(-0.5 * logn) * (1.0 - logn / logX)
    out = np.empty(t.size)
    for i in range(0, t.size, chunk):
        tc = t[i : i + chunk]
        out[i : i + chunk] = np.cos(np.outer(tc, logn)) @ w
    return -out


def peaks(t: np.ndarray, y: np.ndarray, min_height: float) -> np.ndarray:
    """Local maxima above a height floor, refined by parabolic interpolation."""
    i = np.flatnonzero((y[1:-1] > y[:-2]) & (y[1:-1] >= y[2:]) & (y[1:-1] > min_height)) + 1
    a, b, c = y[i - 1], y[i], y[i + 1]
    denom = a - 2 * b + c
    shift = np.where(denom != 0, 0.5 * (a - c) / np.where(denom != 0, denom, 1), 0.0)
    return t[i] + shift * (t[1] - t[0])


def true_gammas(t_hi: float) -> np.ndarray:
    """Nontrivial zero ordinates up to t_hi, straight from mpmath (the answer key)."""
    mp.mp.dps = 20
    out, k = [], 1
    while True:
        g = float(mp.zetazero(k).imag)
        if g > t_hi:
            return np.asarray(out)
        out.append(g)
        k += 1


def match(found: np.ndarray, truth: np.ndarray) -> np.ndarray:
    """Distance from each true gamma to the nearest recovered peak."""
    if found.size == 0:
        return np.full(truth.shape, np.inf)
    return np.abs(truth[:, None] - found[None, :]).min(axis=1)


def main(x_max: int = 10**6) -> None:
    print("E5D: recovering the zeta zeros from prime data alone")
    t = np.arange(T_LO, T_HI, DT)
    truth = true_gammas(T_HI)
    print(f"  answer key: {truth.size} true zeros in ({T_LO}, {T_HI}), "
          f"first {truth[0]:.6f}, last {truth[-1]:.6f}")

    print("\n[A] Peaks of Phi_X(t) vs the true gamma, as the prime cutoff X grows")
    print("      X        peaks found   matched   median |t_peak - gamma|   worst")
    best = None
    for X in (10**3, 10**4, 10**5, x_max):
        logn, lam = prime_power_terms(X)
        y = spectrum(t, logn, lam, np.log(X))
        pk = peaks(t, y, 0.35 * y.max())
        d = match(pk, truth)
        hit = d < 0.5
        med = np.median(d[hit]) if hit.any() else float("nan")
        wor = d[hit].max() if hit.any() else float("nan")
        print(f"    10^{int(round(np.log10(X)))}  {pk.size:>10}   {int(hit.sum()):>3}/{truth.size}"
              f"      {med:.5f}            {wor:.5f}")
        if X == x_max:
            best = (y, pk, d, hit)

    y, pk, d, hit = best
    print(f"\n[B] The first ten zeros, read off the primes below {x_max:.0e}")
    print("      true gamma      recovered peak     error")
    for i in range(min(10, truth.size)):
        j = int(np.argmin(np.abs(pk - truth[i])))
        print(f"    {truth[i]:12.6f}   {pk[j]:14.6f}   {pk[j]-truth[i]:+9.6f}")

    print("\n[C] Control: the same transform on a Beurling generalized-prime")
    print("    system (Euler product, no additive lattice, no functional equation)")
    blogn, blam = beurling_terms(x_max)
    by = spectrum(t, blogn, blam, np.log(x_max))
    bpk = peaks(t, by, 0.35 * by.max())
    bd = match(bpk, truth)
    print(f"    Beurling peaks found: {bpk.size}   (zeta peaks: {pk.size})")
    print(f"    true zeta gammas matched by a Beurling peak (within 0.5): "
          f"{int((bd < 0.5).sum())}/{truth.size}")
    print(f"    median distance from a zeta gamma to the nearest Beurling peak: "
          f"{np.median(bd):.4f}  (zeta's own: {np.median(d[hit]):.5f})")

    print("\nVERDICT: the primes alone locate every zero in the window to ~1e-3,")
    print("the error falling with the cutoff X and then flattening (the sum does")
    print("not converge pointwise; the peak POSITION is still a good estimator):")
    print("the explicit formula runs backwards. The control shows what that does")
    print("NOT buy. A Beurling")
    print("system, with an Euler product but no lattice, yields the same kind of")
    print("spectrum at its own zeros, so 'the primes have a spectrum' is a")
    print("consequence of the Euler product alone and is blind to where the")
    print("zeros sit. Recovering the spectrum is not evidence for RH.")

    np.savez_compressed(CACHE_DIR / "e5d_results.npz", t=t, phi=y, peaks=pk,
                        truth=truth, beurling_phi=by, beurling_peaks=bpk, X=x_max)
    print(f"\nsaved curves to {CACHE_DIR / 'e5d_results.npz'}")


if __name__ == "__main__":
    main(int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**6)
