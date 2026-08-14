"""E5C: the pole of zeta at s = 1 runs the PNT; the zeros are the error term.

QUESTION (the "singularity" question). Where does the regularity of the
primes come from, and what controls the error? The answer is one identity,
the Riemann-von Mangoldt explicit formula for psi(x) = sum_{p^k <= x} log p:

    psi(x) = x - sum_rho x^rho/rho - log(2 pi) - (1/2) log(1 - x^-2)

The main term x is EXACTLY the residue of -zeta'/zeta at the pole s = 1:
the singularity of zeta is the prime number theorem's engine. Every
nontrivial zero rho = beta + i*gamma contributes an oscillation of size
x^beta/|rho|: the zeros ARE the error term. PNT is equivalent to no zeros
on Re(s) = 1; RH is the statement that every oscillation has the minimal
possible amplitude sqrt(x) (square-root cancellation).

METHOD. psi(x) computed exactly from prime powers up to X; the truncated
formula evaluated with the first K zeros (from experiments._shared.zeta,
disk-cached, 30 digits); errors measured at half-integer x to dodge the
jumps. Then the PNT scoreboard: pi(x) vs x/log x vs li(x) at decade
checkpoints, with the Schoenfeld RH band sqrt(x) log(x) / (8 pi) that
|li(x) - pi(x)| must respect (x >= 2657) if and only if RH holds.

READING IT. Watching the truncated sum converge to the psi staircase is
watching the zeros rebuild the primes: analytic data on one side, integers
on the other. That two-sidedness (Euler product + Poisson/theta lattice) is
the same joint the main program keeps hitting (the additive lattice clause).
"""
from __future__ import annotations

import sys

import numpy as np
import mpmath as mp

from experiments._shared.zeta import zeta
from experiments.primes.primestream import CACHE_DIR, flat_primes, stream

X_MAX = 1000.0
T_MAX = 250.0          # ~108 zeros; enough to resolve the staircase visibly


def prime_power_measure(x_max: float) -> tuple[np.ndarray, np.ndarray]:
    """Sorted prime powers p^k <= x_max and their von Mangoldt weights log p."""
    ps = flat_primes(int(x_max))
    vals, wts = [], []
    for p in ps:
        pk = int(p)
        while pk <= x_max:
            vals.append(pk)
            wts.append(np.log(float(p)))
            pk *= int(p)
    order = np.argsort(vals)
    return np.asarray(vals, dtype=np.float64)[order], np.asarray(wts)[order]


def psi_exact(x: np.ndarray, x_max: float = X_MAX) -> np.ndarray:
    vals, wts = prime_power_measure(x_max)
    cum = np.concatenate(([0.0], np.cumsum(wts)))
    return cum[np.searchsorted(vals, x, side="right")]


def zero_gammas(t_max: float = T_MAX, prec: int = 30) -> np.ndarray:
    return np.array([float(z.imag) for z in zeta.zeros(t_max, prec=prec)])


def psi_formula(x: np.ndarray, gammas: np.ndarray, k: int | None = None) -> np.ndarray:
    g = gammas[:k] if k else gammas
    rho = 0.5 + 1j * g
    osc = 2.0 * np.real(x[:, None] ** rho / rho).sum(axis=1)
    return x - osc - np.log(2 * np.pi) - 0.5 * np.log1p(-x**-2.0)


def main(t_max: float = T_MAX) -> None:
    print("E5C: explicit formula and the PNT scoreboard")
    print(f"loading zeros to T = {t_max} (cached after first run) ...")
    gammas = zero_gammas(t_max)
    print(f"  {len(gammas)} zeros; first gamma = {gammas[0]:.6f}, last = {gammas[-1]:.3f}")

    x = np.arange(2.25, X_MAX, 0.5)     # half-integer grid: no prime-power jumps
    psi = psi_exact(x)
    print("\n[A] Truncated explicit formula vs the exact psi staircase")
    print("    K zeros    max|err| x<=100    max|err| x<=1000    mean|err| x<=1000")
    for k in (5, 25, len(gammas)):
        approx = psi_formula(x, gammas, k)
        err = np.abs(approx - psi)
        m100 = float(err[x <= 100].max())
        print(f"    {k:>7}    {m100:14.4f}    {float(err.max()):15.4f}    "
              f"{float(err.mean()):14.4f}")

    print("\n[B] PNT scoreboard: pi(x) vs x/log x vs li(x), and the RH band")
    res = stream(10**8)
    pi_cum = np.cumsum(res["pi_dec"])
    mp.mp.dps = 30
    print("      x        pi(x)      pi/(x/log x)   li(x)-pi(x)   RH band sqrt(x)logx/8pi")
    for k in range(4, 9):
        xk = 10.0 ** k
        pi_x = int(pi_cum[k - 1])
        ratio = pi_x / (xk / np.log(xk))
        li_gap = float(mp.li(xk)) - pi_x
        band = np.sqrt(xk) * np.log(xk) / (8 * np.pi)
        print(f"    10^{k:<2} {pi_x:>12}    {ratio:.6f}    {li_gap:>10.1f}   {band:>12.1f}")

    print("\nVERDICT: the pole at s = 1 supplies the main term x (PNT); with")
    print(f"{len(gammas)} zeros the formula tracks the staircase to a fraction of a")
    print("single log p step. li(x) - pi(x) sits far inside the RH square-root")
    print("band (it stays positive here, but Littlewood proved it flips sign")
    print("infinitely often; the first flip is expected near 10^316, Skewes/")
    print("Bays-Hudson). PNT itself is exactly: no zeros on Re(s) = 1.")

    np.savez_compressed(
        CACHE_DIR / "e5c_results.npz",
        gammas=gammas,
        x=x, psi=psi,
        approx_k10=psi_formula(x, gammas, 10),
        approx_full=psi_formula(x, gammas, None),
    )
    print(f"\nsaved curves to {CACHE_DIR / 'e5c_results.npz'}")


if __name__ == "__main__":
    main(float(sys.argv[1]) if len(sys.argv) > 1 else T_MAX)
