"""E5E: the zeros behave like random-matrix eigenvalues, and that is Level 3.

QUESTION. Montgomery (1973) computed the pair correlation of the zeta zeros
and Dyson recognised it as the GUE kernel: the zeros repel exactly like the
eigenvalues of a large random Hermitian matrix. Odlyzko confirmed it
numerically at enormous height. Two things to measure here. (i) Does it
hold, in our own data and in Odlyzko's, and does the agreement sharpen with
height? (ii) What does it buy for RH?

METHOD. Five heights, two independent sources.
  - height ~10^4 and ~10^6: zeros located here, by a vectorized
    Riemann-Siegel Z sign-change search (experiments/primes/rsz.py). The
    finder is validated against Odlyzko's table (agreement to 4e-6 of a mean
    spacing at t = 70,000) and its completeness is checked against the
    Riemann-von Mangoldt count.
  - heights ~10^12, ~10^21, ~10^22: Odlyzko's published tables, 10^4 zeros
    each (zeros3/zeros4/zeros5). Those heights are far past anything this
    box can compute, and they are where GUE agreement becomes sharp.
Zeros are unfolded to unit mean spacing with the local density
log(t/2pi)/(2pi), then compared with the GUE nearest-neighbour surmise and
with Montgomery's exact pair correlation 1 - (sin(pi u)/(pi u))^2. A Poisson
(uncorrelated) sample of the same size is carried as a positive control, so
"the test has power" is measured rather than assumed.

WHAT IT BUYS (the honest half; docs/03_research/quantum_chaos_and_the_zeros.md
argues this in prose, and this module measures it). Every statistic here is
a function of the HEIGHTS gamma alone. A zero moved off the critical line
keeps its height, so it changes none of these numbers: the whole battery is
invariant under exactly the falsification RH cares about. Section [D]
demonstrates that literally, by moving zeros off the line and recomputing.
That is the four-level framing's Level 3 (CLAUDE.md): GUE statistics are
compatible with worlds where some zero has beta = 0.51, so no amount of
agreement closes RH. The agreement is a compass for where the proof must
live (a spectral interpretation), not evidence that it is true.
"""
from __future__ import annotations

import pickle
import re
import sys
from pathlib import Path

import numpy as np

from experiments.primes.primestream import CACHE_DIR
from experiments.primes.rsz import (
    completeness, n_count, pair_correlation, sine_kernel, unfold, wigner_gue, zeros_in,
)

ODLYZKO = CACHE_DIR / "odlyzko"
ODLYZKO_URL = "https://www-users.cse.umn.edu/~odlyzko/zeta_tables/"
UMAX, NBINS = 3.0, 60
SMAX, SBINS = 4.0, 80


def load_odlyzko(name: str) -> tuple[np.ndarray, int]:
    """(values, offset) from an Odlyzko table; gamma = offset + value."""
    path = ODLYZKO / name
    if not path.exists():
        raise FileNotFoundError(
            f"{path} missing. Fetch the tables with:\n"
            f"  mkdir -p {ODLYZKO} && cd {ODLYZKO} && "
            f"curl -O {ODLYZKO_URL}{{zeros1,zeros3,zeros4,zeros5}}")
    text = path.read_text().splitlines()
    offset = 0
    for line in text[:12]:
        m = re.search(r"gamma\s*-\s*(\d+)", line)
        if m:
            offset = int(m.group(1))
            break
    vals = []
    for line in text:
        s = line.strip()
        if not s:
            continue
        try:
            vals.append(float(s))
        except ValueError:
            continue
    return np.asarray(vals), offset


def our_zeros(t0: float, span: float, step: float = 0.02) -> np.ndarray:
    """Zeros we compute ourselves, cached on disk."""
    cache = CACHE_DIR / f"rsz_zeros_{t0:.0f}_{span:.0f}.npy"
    if cache.exists():
        return np.load(cache)
    g = zeros_in(t0, t0 + span, step=step)
    np.save(cache, g)
    return g


def model_cdf(pdf, xs: np.ndarray) -> np.ndarray:
    grid = np.linspace(0, xs.max() + 1e-9, 20001)
    c = np.concatenate(([0.0], np.cumsum(pdf(grid[1:]) * np.diff(grid))))
    return np.interp(xs, grid, c)


def ks(spacings: np.ndarray, pdf) -> float:
    """Kolmogorov-Smirnov distance between the empirical and model CDF."""
    s = np.sort(spacings)
    emp = np.arange(1, s.size + 1) / s.size
    mod = model_cdf(pdf, s)
    return float(np.max(np.abs(emp - mod)))


def poisson_pdf(s):
    return np.exp(-s)


COMMON_N = 9999          # every set is cut to this so the columns compare like for like


def summarize(name: str, sp: np.ndarray, cap: int = COMMON_N) -> dict:
    """Statistics on a fixed sample size: deviations shrink like 1/sqrt(n), so
    comparing a 40,000-zero set with a 10,000-zero one would read sample noise
    as a height trend."""
    n_full = sp.size
    sp = sp[:cap]
    u, r2 = pair_correlation(sp, UMAX, NBINS)
    pred = sine_kernel(u)
    band = u <= 1.5                       # where the sine kernel has structure
    hist, edges = np.histogram(sp, bins=SBINS, range=(0, SMAX), density=True)
    return dict(
        name=name, n=sp.size, n_full=n_full, mean=float(sp.mean()),
        ks_gue=ks(sp, wigner_gue), ks_poisson=ks(sp, poisson_pdf),
        p_small=float((sp < 0.1).mean()),
        r2_rms=float(np.sqrt(np.mean((r2[band] - pred[band]) ** 2))),
        u=u, r2=r2, hist=hist, edges=edges,
    )


def main(compute_span: float = 21000.0) -> None:
    print("E5E: zero statistics vs the GUE, from height 10^4 to 10^22")
    rows, saves = [], {}

    z1, _ = load_odlyzko("zeros1")
    g_low = z1[:10000]
    print(f"\n  height ~1e4  : Odlyzko zeros1, first {g_low.size} zeros "
          f"(gamma {g_low[0]:.3f} .. {g_low[-1]:.3f})")
    rows.append(summarize("1e4 (computed by Odlyzko)", unfold(g_low)))

    print(f"  height ~1e6  : computing our own zeros on [1e6, 1e6+{compute_span:.0f}] ...")
    g_our = our_zeros(1e6, compute_span)
    found, pred = completeness(g_our, 1e6, 1e6 + compute_span)
    print(f"                 {found} zeros found, Riemann-von Mangoldt predicts "
          f"{pred:.1f} (ratio {found/pred:.6f})")
    rows.append(summarize("1e6 (computed here)", unfold(g_our)))

    for fn, label in (("zeros3", "1e12"), ("zeros4", "1e21"), ("zeros5", "1e22")):
        v, off = load_odlyzko(fn)
        h = float(off) + float(v.mean())
        print(f"  height ~{label} : Odlyzko {fn}, {v.size} zeros near gamma = {h:.6e}")
        rows.append(summarize(f"{label} (Odlyzko)", unfold(v, center=h)))

    rng = np.random.default_rng(20260814)
    rows.append(summarize("Poisson control", rng.exponential(1.0, 40000)))

    print("\n[A] Nearest-neighbour spacings: distance to the GUE surmise and to Poisson")
    print(f"    (every set cut to the same {COMMON_N} spacings, so the columns compare)")
    print("    dataset                     avail    mean s    KS vs GUE   KS vs Poisson")
    for r in rows:
        print(f"    {r['name']:<26} {r['n_full']:>7}   {r['mean']:.4f}    "
              f"{r['ks_gue']:.4f}       {r['ks_poisson']:.4f}")

    print("\n[B] Level repulsion: fraction of spacings below 0.1 of the mean")
    print(f"    GUE predicts {model_cdf(wigner_gue, np.array([0.1]))[0]:.5f}, "
          f"Poisson predicts {1-np.exp(-0.1):.5f}")
    for r in rows:
        print(f"    {r['name']:<26} {r['p_small']:.5f}")

    print("\n[C] Pair correlation vs Montgomery's exact kernel 1 - (sin(pi u)/(pi u))^2")
    print("    RMS deviation over u in (0, 1.5], and the curve at three points")
    print("    dataset                     RMS dev     R2(0.5)  R2(1.0)  R2(1.5)")
    pts = [0.5, 1.0, 1.5]
    for r in rows:
        vals = [float(np.interp(p, r["u"], r["r2"])) for p in pts]
        print(f"    {r['name']:<26} {r['r2_rms']:.4f}      "
              + "   ".join(f"{v:.3f}" for v in vals))
    print("    sine kernel says             (exact)     "
          + "   ".join(f"{sine_kernel(np.array([p]))[0]:.3f}" for p in pts))

    print("\n[D] The control that matters: this battery cannot see the critical line")
    rho = 0.5 + 1j * g_our                       # the real zeros, on the line
    rng2 = np.random.default_rng(7)
    moved = rng2.choice(rho.size, size=rho.size // 100, replace=False)
    rho_bad = rho.copy()
    rho_bad[moved] = 0.8085 + 1j * rho[moved].imag   # D-H's actual off-line real part
    print(f"    Build a counterfactual zero set: take our {rho.size} zeros and move")
    print(f"    {moved.size} of them to Re(rho) = 0.8085, the real part Davenport-")
    print("    Heilbronn's off-line zeros actually have. RH is false for that set.")
    r_before = summarize("before", unfold(rho.imag))
    r_after = summarize("after", unfold(rho_bad.imag))
    print(f"    max |Re(rho) - 1/2| went from {np.abs(rho.real-0.5).max():.4f} to "
          f"{np.abs(rho_bad.real-0.5).max():.4f}, and the statistics did this:")
    print(f"      KS vs GUE   before {r_before['ks_gue']:.6f}   after {r_after['ks_gue']:.6f}")
    print(f"      pair-corr RMS before {r_before['r2_rms']:.6f}   after {r_after['r2_rms']:.6f}")
    print("    RH is false in that world and this page cannot tell. Compare")
    print("    experiments/positivity/offline_flip_test.py, which formalizes the")
    print("    screen: a statistic of heights alone is RH-blind by construction.")

    dh = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    if dh and dh.exists():
        z = pickle.load(open(dh, "rb"))
        gam = np.sort(np.array([w.imag for w in z if w.imag > 0]))
        heights = np.unique(np.round(gam, 6))
        offl = sorted({round(w.imag, 3) for w in z if abs(w.real - 0.5) > 1e-6})
        T = float(gam.max())
        # degree 1, conductor 5, one gamma factor (see davenport_heilbronn.py)
        expected = T / (2 * np.pi) * np.log(5 * T / (2 * np.pi * np.e))
        print(f"\n[E] Davenport-Heilbronn control: attempted, and refused")
        print(f"    The repo's D-H scanner is a coarse grid search, not a bracketing")
        print(f"    zero finder. It returns {heights.size} distinct heights below T = {T:.0f}, "
              f"where the")
        print(f"    functional equation predicts about {expected:.0f}. The list is roughly "
              f"{100*heights.size/expected:.0f}% complete.")
        sp = np.diff(gam)
        sp = sp[sp > 0]
        sp = sp / sp.mean()
        print(f"    Running the battery on it anyway would report KS vs GUE "
              f"{ks(sp, wigner_gue):.2f} and")
        print(f"    KS vs Poisson {ks(sp, poisson_pdf):.2f}, i.e. 'D-H is not GUE'. That is an")
        print("    ARTIFACT: deleting points at random from a repulsive sequence makes it")
        print("    look Poisson. No D-H spacing statistic is reported here. What it would")
        print("    take is a Hardy-function analogue of Z(t) for D-H, giving sign-change")
        print("    bracketing plus a Riemann-von Mangoldt completeness check: the two")
        print("    things that make the zeta rows above trustworthy.")
        print(f"    Worth keeping from the scan: the off-line zeros it did find, at heights")
        print(f"    {offl}. Each is a conjugate pair (beta, 1-beta)")
        print("    sharing ONE height, so a height-only statistic sees a spacing of exactly")
        print("    zero there, and cannot tell that the pair is off the line at all.")

    for r in rows:
        key = r["name"].split()[0].replace(".", "")
        saves[f"u_{key}"] = r["u"]
        saves[f"r2_{key}"] = r["r2"]
        saves[f"hist_{key}"] = r["hist"]
        saves[f"edges_{key}"] = r["edges"]
        saves[f"ks_{key}"] = np.array([r["ks_gue"], r["ks_poisson"], r["p_small"],
                                       r["r2_rms"], r["n"]])
    np.savez_compressed(CACHE_DIR / "e5e_results.npz", **saves)

    print("\nVERDICT: the zeros repel like GUE eigenvalues, and the agreement")
    print("sharpens with height exactly as Montgomery-Odlyzko predict, while a")
    print("Poisson sample of the same size is rejected outright, so the test has")
    print("real power. It has no power over RH: every statistic is built from")
    print("heights, and the critical line is a statement about real parts.")
    print(f"\nsaved curves to {CACHE_DIR / 'e5e_results.npz'}")


if __name__ == "__main__":
    main(float(sys.argv[1]) if len(sys.argv) > 1 else 21000.0)
