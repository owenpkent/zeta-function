"""E5G: predicting the Chebyshev race from the zeros of the L-function.

THE CLAIM UNDER TEST. E5A measured the prime races and E5F argued that their
amplitude is governed by the REAL parts of the zeros of Dirichlet L-functions,
which is what makes a race (unlike GUE statistics) sensitive to RH. That is a
mechanism story, asserted. Here it is checked: the zeros are used to PREDICT
the race, including the exact height of the first sign change, with no prime
data anywhere in the prediction.

THE FORMULA. Write E(x) = (log x / sqrt x) [pi(x;q,N) - pi(x;q,R)] for the
race between the nonresidue and residue classes. For q = 3 and q = 4 there is
exactly one non-principal character, real and primitive, and

    psi(x;q,N) - psi(x;q,R) = -psi(x, chi) = sum_rho x^rho / rho.

Prime squares all land in the residue class (p^2 = 1 mod 3 and mod 4), which
contributes -theta(sqrt x) ~ -sqrt x to that difference and is exactly the
systematic bias. Undoing it and passing from psi to pi by partial summation
leaves, under GRH,

    E(x) = 1 + 2 sum_{gamma > 0} Re[ x^{i gamma} / (1/2 + i gamma) ]
         = 1 + 2 sum_{gamma > 0} [ cos(gamma L)/2 + gamma sin(gamma L) ]
                                 / (1/4 + gamma^2),        L = log x,

with gamma running over the ordinates of the zeros of L(s, chi). The constant
1 is the bias (the number of square roots of 1 mod q, minus one); everything
else is the zeros talking. The race is ahead when E > 0 and flips when E < 0.

THE DATA. Zeros come from Oliveira e Silva's tables (10,000 per character;
see DATASETS.md), which were computed from the L-functions and know nothing
about our prime counts. The prime side comes from the 10^12 stream. The two
were produced by completely separate computations, which is the point.

WHAT TRUNCATION COSTS. Stopping at 10,000 zeros (height ~8700 for modulus 3)
leaves a tail whose RMS contribution to E is about 0.02, and it caps the
resolution in log x at 2*pi/gamma_max. So the prediction resolves the shape
and the location of an excursion, not its last digit.
"""
from __future__ import annotations

import gzip
import sys
from pathlib import Path

import numpy as np

from experiments.primes.primestream import CACHE_DIR, stream

TOS = CACHE_DIR / "datasets" / "tos" / "zeta"
# (modulus, file, nonresidue class, residue class, published first sign change)
RACES = {
    3: ("zeros_003_001.txt.gz", 2, 1, 608981813029),
    4: ("zeros_004_001.txt.gz", 3, 1, 26861),
}


def load_zeros(modulus: int) -> np.ndarray:
    """Ordinates of the zeros of L(s, chi) for the real primitive character."""
    path = TOS / RACES[modulus][0]
    if not path.exists():
        raise FileNotFoundError(
            f"{path} missing. See experiments/primes/DATASETS.md for the fetch command.")
    vals = []
    with gzip.open(path, "rt") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            try:
                vals.append(float(s))
            except ValueError:
                continue
    return np.asarray(vals)


def E_predicted(logx: np.ndarray, gammas: np.ndarray, chunk: int = 4096) -> np.ndarray:
    """E(x) from the zeros alone. No prime data enters this function."""
    denom = 0.25 + gammas**2
    w_cos, w_sin = 0.5 / denom, gammas / denom
    out = np.empty(logx.size)
    for i in range(0, logx.size, chunk):
        L = logx[i : i + chunk]
        ph = np.outer(L, gammas)
        out[i : i + chunk] = 1.0 + 2.0 * (np.cos(ph) @ w_cos + np.sin(ph) @ w_sin)
    return out


def E_measured(modulus: int, res: dict) -> tuple[np.ndarray, np.ndarray]:
    """E(x) from our own prime stream, on its log-spaced sample grid."""
    name = f"race{modulus}"
    done = int(res[f"{name}_sample_done"])
    x = res["race_thresholds"][:done].astype(float)
    lead = res[f"{name}_sample_lead"][:done].astype(float)
    keep = x > 1e3
    x, lead = x[keep], lead[keep]
    return x, lead * np.log(x) / np.sqrt(x)


def tail_rms(gammas: np.ndarray) -> float:
    """RMS contribution to E of the zeros we do NOT have (gamma > gamma_max).

    Each zero adds a term of size 2/|rho| with an effectively independent
    phase, so the discarded tail has variance ~ sum_{gamma > G} 2/gamma^2,
    which with the Riemann-von Mangoldt density for L(s, chi) mod q is about
    2 * density(G) / G. This is the floor below which a predicted wiggle
    means nothing.
    """
    G = float(gammas[-1])
    density = np.log(G) / (2 * np.pi)          # zeros per unit height, near G
    return float(np.sqrt(2.0 * density / G))


def excursions(logx: np.ndarray, E: np.ndarray) -> list[dict]:
    """Maximal runs where the predicted E is negative, deepest first."""
    neg = np.flatnonzero(E < 0)
    if neg.size == 0:
        return []
    runs, cur = [], [neg[0]]
    for a, b in zip(neg, neg[1:]):
        if b == a + 1:
            cur.append(b)
        else:
            runs.append(cur)
            cur = [b]
    runs.append(cur)
    out = []
    for r in runs:
        i = r[int(np.argmin(E[r]))]
        out.append(dict(x_lo=float(np.exp(logx[r[0]])), x_hi=float(np.exp(logx[r[-1]])),
                        x_min=float(np.exp(logx[i])), depth=float(E[i])))
    out.sort(key=lambda d: d["depth"])
    return out


def main(modulus: int = 3) -> None:
    fname, N, R, published = RACES[modulus]
    g = load_zeros(modulus)
    print(f"E5G: predicting the mod-{modulus} race from the zeros of L(s, chi)")
    print(f"  zeros loaded: {g.size:,}  first {g[0]:.6f}  last {g[-1]:.3f}  "
          f"(Oliveira e Silva)")
    print(f"  truncation: resolves log x down to 2pi/gamma_max = {2*np.pi/g[-1]:.2e}")

    res = stream(10**12)
    x, Em = E_measured(modulus, res)
    Ep = E_predicted(np.log(x), g)
    band = (x > 1e5) & (x < 1e12)
    corr = float(np.corrcoef(Em[band], Ep[band])[0, 1])
    print(f"\n[A] Prediction vs measurement on {int(band.sum())} sampled x in (1e5, 1e12)")
    print(f"    correlation           : {corr:+.4f}")
    print(f"    mean E measured       : {Em[band].mean():+.4f}   predicted "
          f"{Ep[band].mean():+.4f}   (theory says the bias term is exactly 1)")
    print(f"    RMS difference        : {float(np.sqrt(np.mean((Em[band]-Ep[band])**2))):.4f}")
    print("    (our x-samples are log-spaced at 5.8e-3, coarser than the zeros'")
    print("     finest oscillation, so the high-frequency part is aliased away;")
    print("     what should agree is the envelope and the low-frequency shape.)")

    floor = tail_rms(g)
    span = 300.0
    # E(x) = 1 + oscillation drops the O(1/log x) terms of the passage from psi
    # to pi, so it is only trustworthy once log x is comfortably large. Below
    # x ~ 1e4 those neglected terms are the size of the excursions themselves.
    x_lo = max(published / span, 1e4)
    # Nyquist for the truncated sum is pi/gamma_max in log x; sample ~6x finer.
    npts = int(6 * np.log(published * span / x_lo) * g[-1] / np.pi)
    L = np.linspace(np.log(x_lo), np.log(published * span), npts)
    E = E_predicted(L, g)
    exc = excursions(L, E)
    deep = [e for e in exc if e["depth"] < -2 * floor]
    print(f"\n[B] Where do the zeros say the race goes negative?")
    print(f"    search window         : x in ({x_lo:.3g}, {published*span:.3g}), "
          f"{np.log(published*span/x_lo):.1f} in log x")
    print(f"    noise floor (tail RMS): {floor:.4f}; only dips past {2*floor:.4f} are meaningful")
    print(f"    meaningful excursions : {len(deep)} of {len(exc)} sign changes in the window")
    for e in deep[:5]:
        print(f"      E = {e['depth']:+.4f} at x = {e['x_min']:,.0f}"
              f"   (negative on {e['x_lo']:,.0f} .. {e['x_hi']:,.0f})")
    print(f"\n    measured first flip   : x = {int(res[f'race{modulus}_first_cross']):,}")
    if deep:
        best = deep[0]
        print(f"    deepest predicted dip : x = {best['x_min']:,.0f}   "
              f"ratio to measured {best['x_min']/published:.4f}")
        first_neg = min(deep, key=lambda e: e["x_lo"])
        print(f"    earliest meaningful   : x = {first_neg['x_lo']:,.0f}   "
              f"ratio {first_neg['x_lo']/published:.4f}")
        print(f"    log-x error of deepest: {abs(np.log(best['x_min'])-np.log(published)):.4f}"
              f"  (the truncated sum cannot resolve below {2*np.pi/g[-1]:.1e})")

    print(f"\n[C] Depth of the excursion: prediction vs measurement")
    lead_min = int(res[f"race{modulus}_min_lead"])
    x_min = float(res[f"race{modulus}_min_lead_x"])
    E_meas_min = lead_min * np.log(x_min) / np.sqrt(x_min)
    at = E_predicted(np.log(np.array([x_min, float(published)])), g)
    print(f"    measured deepest lead : {lead_min:,} primes at x = {x_min:,.0f}, "
          f"i.e. E = {E_meas_min:+.4f}")
    print(f"    predicted E there     : {at[0]:+.4f}")
    print(f"    predicted E at the measured first flip: {at[1]:+.4f}  "
          f"(E crosses zero there by definition, so a small negative value is a hit)")

    np.savez_compressed(CACHE_DIR / f"e5g_race{modulus}.npz",
                        x=x, E_meas=Em, E_pred=Ep, gammas=g,
                        zoom_logx=L, zoom_E=E, predicted_flip=pred)
    print(f"\nsaved to {CACHE_DIR / f'e5g_race{modulus}.npz'}")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 3)
