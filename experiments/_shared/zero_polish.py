"""Bulk high-precision zeta-zero engine: batch Newton polish, not recompute.

WHY. Ladder experiments (e2as, e2au and successors) need every zero ordinate
to T ~ 350-600+ at 80-120 digits. Calling mp.zetazero(k) at high dps for each
k redoes root-finding from scratch at full precision. But a zero ordinate is
already known cheaply (the repo's prec-30 caches, or a fast sign-change scan
of Z at low dps), and Newton iteration on the real Riemann-Siegel function
Z(t) = exp(i*theta(t)) * zeta(1/2 + i*t) converges quadratically: from a
30-digit seed, ~3 iterations reach 110 digits, and only the last one or two
run at full working precision. The batch is embarrassingly parallel.

ALGORITHM (polish_zero):
  1. Seed t0 from a cheap source (caller supplies; zeros_hp harvests the
     existing caches, else scans siegelz for sign changes, else enumerates
     with mp.zetazero at dps 30).
  2. Staged Newton on Z: iterate t <- t - Z(t)/Z'(t) with working precision
     grown geometrically with the measured accuracy (each step roughly
     doubles correct digits), final steps at dps + guard.
  3. Validate: check that Z changes sign across [t - w, t + w] with
     w = 10^-(dps-5), evaluated at dps + guard.

HONESTY NOTE on validation. mpmath is not directed-rounding rigorous, so the
sign-change bracket is a strong consistency check, not a formal certificate.
The rigorous side (interval/ball certification) is handled elsewhere in the
repo by the certified_eig work; this module's contract is "same trust level
as mp.zetazero, much faster in bulk".

COUNT VALIDATION (zeros_hp). The number of zeros returned up to T_max is
required to equal mp.nzeros(T_max) (argument-principle count at dps 30), so
no zero is missed or duplicated regardless of seed source.

CACHE. zeros_hp writes experiments/_shared/_cache/zeros_polish_dps{D}_T{T}.json,
a JSON list of decimal ordinate strings, the same format as the hand-built
zeros_dps{D}_T{T}.json files that e2as/e2au consume:

    gz = [mp.mpf(s) for s in json.loads(path.read_text())]

The "zeros_polish_" prefix guarantees no collision with existing cache files;
existing files are never overwritten (an existing key is loaded, not rebuilt).

BENCHMARK (this box, 8 cores, 2026-08-20). Serial, 5 zeros near T ~ 517 at
dps 110 (indices 281..285), from 40-digit seeds:
    mp.zetazero at dps 110      : 2.92 s  (0.585 s/zero)
    polish, validate=True       : 1.92 s  (0.384 s/zero), 1.5x
    polish, validate=False      : 1.11 s  (0.221 s/zero), 2.6x
Batch: the full T=600 ladder cache (341 zeros at dps 110, validated):
    serial mp.zetazero loop     : 129.4 s
    zeros_hp(600, 110, workers=8): 18.4 s, 7.0x wall-clock
All polished values agreed bit-for-bit at 110 digits with mp.zetazero and
with the independently built zeros_dps110_T600.json ladder cache.

CLI:
    .venv/bin/python -m experiments._shared.zero_polish --tmax 100 --dps 60 --workers 4
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import pickle
import re
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import mpmath as mp

CACHE_DIR = Path(__file__).resolve().parent / "_cache"

# T values the repo's pickle caches were historically built at; used only to
# DISCOVER existing seed files (the pickle key is a hash, so (T, prec) cannot
# be read back from the filename).
_PICKLE_T_SWEEP = (30, 50, 60, 100, 120, 150, 200, 250, 300, 350, 400, 500,
                   600, 700, 800, 1000, 1500, 2000)
_PICKLE_PREC_SWEEP = (30, 50, 80)

_JSON_SEED_RE = re.compile(r"zeros(?:_polish)?_dps(\d+)_T(\d+(?:\.\d+)?)\.json$")


class ZeroPolishError(RuntimeError):
    """Raised when a polish fails to converge, drifts off its seed, or fails
    the sign-change bracket validation."""


# ---------------------------------------------------------------------------
# single-zero polish
# ---------------------------------------------------------------------------

def _bracket_ok(t, dps: int, guard: int) -> bool:
    """Sign change of Z across [t - w, t + w], w = 10^-(dps-5), at dps+guard.

    Consistency check, not a certificate (see module docstring)."""
    with mp.workdps(dps + guard):
        w = mp.mpf(10) ** (-(dps - 5))
        zl = mp.siegelz(mp.mpf(t) - w)
        zr = mp.siegelz(mp.mpf(t) + w)
        return mp.sign(zl) * mp.sign(zr) < 0


def polish_zero(t0, dps: int, guard: int = 15, max_iter: int = 30,
                validate: bool = True, max_drift: float = 2.0,
                seed_digits=None):
    """Newton-polish one zero ordinate t0 to dps digits. Returns mp.mpf at dps.

    t0: seed ordinate (float, mpf, or decimal string); a few correct digits
        suffice, the staged iteration measures its own accuracy.
    guard: extra working digits (all computation at dps + guard, result
        rounded to dps). Minimum 10 enforced.
    max_drift: a polished result more than this far from the seed is flagged
        (a bad seed that Newton carried to a distant zero). The first-step
        jump is also capped at 0.5 (below every zero gap in range).
    seed_digits: optional hint for the seed's correct digits. Purely a cost
        optimization (sizes the first Newton step); every later estimate is
        measured from the actual step lengths, so an optimistic hint costs an
        extra iteration rather than a wrong result.

    Cost model (WHY the loop looks like this): mpmath's siegelz cost is
    nearly flat in dps at fixed t (the Riemann-Siegel sum dominates), so the
    optimization target is the NUMBER of evaluations, not their precision.
    Z' is 1.5-2x the cost of Z and Newton only needs it to as many digits as
    the step still has to gain, so Z' is computed at reduced precision and
    REUSED across steps while its staleness (it was computed at a slightly
    different t) still covers the remaining digits.

    Raises ZeroPolishError on non-convergence, drift, or failed validation.
    """
    if dps < 15:
        raise ValueError("polish_zero targets dps >= 15; use mp.zetazero below that")
    guard = max(int(guard), 10)
    full = dps + guard
    with mp.workdps(50):
        # parse the seed at fixed precision: the ambient context may be dps 15
        # and would silently truncate a 40-digit seed string
        t = mp.mpf(str(t0)) if not isinstance(t0, mp.mpf) else t0
    t_seed = float(t)

    d = max(2.0, float(seed_digits) - 2.0) if seed_digits else 2.0
    dz = None
    d_dz = -1.0           # digits of relative accuracy the stored Z' still has
    t_dz = None           # where that Z' was computed
    converged = False
    for _ in range(max_iter):
        can_finish = 2.0 * d - 2.0 >= dps + 2
        # digits of Z' this step actually needs: enough to sustain doubling
        # mid-course, only the remaining gap on the finishing step
        req = (dps + 2 - d) if can_finish else d
        if dz is not None and t_dz is not None:
            drift_dz = abs(float(t) - t_dz)
            stale = 1e9 if drift_dz == 0 else -mp.log10(drift_dz) - 1
            d_dz = min(d_dz, float(stale))
        if dz is None or d_dz < req:
            dz_wp = min(full, max(35, int(req) + 16))
            with mp.workdps(dz_wp):
                dz = mp.siegelz(mp.mpf(t), derivative=1)
                if dz == 0:
                    raise ZeroPolishError(f"Z'(t) = 0 at t = {float(t)}")
            d_dz = dz_wp - 12.0
            t_dz = float(t)
        wp_z = min(full, max(40, int(min(2 * d, dps + 6)) + 10))
        with mp.workdps(wp_z + 8):
            tt = mp.mpf(t)
            z = mp.siegelz(tt)
            delta = z / dz
            t = tt - delta
        ad = abs(delta)
        if ad > 0.5:
            raise ZeroPolishError(
                f"Newton step {float(ad):.3g} from seed {t_seed:.6f}: seed too "
                "far from any zero")
        if abs(float(t) - t_seed) > max_drift:
            raise ZeroPolishError(
                f"drifted {abs(float(t) - t_seed):.3g} from seed {t_seed:.6f} "
                f"(max_drift = {max_drift})")
        # error after the update: quadratic term, the Z'-accuracy term, and
        # the working-precision floor, whichever is worst
        d_meas = float(wp_z) if ad == 0 else float(-mp.log10(ad))
        d = min(2.0 * d_meas - 2.0, d_meas + d_dz, wp_z + 3.0)
        if d >= dps + 2:
            converged = True
            break
    if not converged:
        raise ZeroPolishError(
            f"no convergence to {dps} digits in {max_iter} iterations from "
            f"seed {t_seed:.6f}")
    if validate and not _bracket_ok(t, dps, guard):
        raise ZeroPolishError(
            f"no sign change of Z across 1e-{dps - 5} bracket at "
            f"t = {float(t):.6f}")
    with mp.workdps(dps):
        return +t


# ---------------------------------------------------------------------------
# batch polish (multiprocessing)
# ---------------------------------------------------------------------------

def _polish_chunk(job):
    """One worker's chunk. Module-level so it survives pickling. Seeds and
    results travel as decimal strings (precision-safe across processes)."""
    idx, seeds, dps, guard, validate, max_drift, seed_digits = job
    out = []
    for s in seeds:
        try:
            t = polish_zero(s, dps, guard=guard, validate=validate,
                            max_drift=max_drift, seed_digits=seed_digits)
            out.append(("ok", mp.nstr(t, dps + 5)))
        except ZeroPolishError as e:
            out.append(("fail", str(e)))
    return idx, out


def polish_zeros(t_list, dps: int, workers: int = 1, guard: int = 15,
                 validate: bool = True, max_drift: float = 2.0,
                 seed_digits=None, progress=None):
    """Polish a list of seed ordinates to dps digits. Returns list of mp.mpf
    in input order. Raises ZeroPolishError listing every failed index (after
    attempting all of them), so one bad seed does not hide the others."""
    with mp.workdps(45):
        # normalize seeds to 40-digit strings at fixed precision (the ambient
        # context may be dps 15, which would truncate string seeds)
        seeds = [mp.nstr(t if isinstance(t, mp.mpf) else mp.mpf(str(t)), 40)
                 for t in t_list]
    n = len(seeds)
    if n == 0:
        return []
    workers = max(1, int(workers))
    results: list = [None] * n

    if workers == 1:
        for i, s in enumerate(seeds):
            _, out = _polish_chunk((0, [s], dps, guard, validate, max_drift,
                                    seed_digits))
            results[i] = out[0]
            if progress:
                progress(i + 1, n)
    else:
        # ~4 chunks per worker so a slow band does not straggle the pool
        csz = max(1, -(-n // (4 * workers)))
        jobs = [(i, seeds[i:i + csz], dps, guard, validate, max_drift,
                 seed_digits)
                for i in range(0, n, csz)]
        done = 0
        with ProcessPoolExecutor(max_workers=workers) as ex:
            futs = {ex.submit(_polish_chunk, j): j for j in jobs}
            for fut in as_completed(futs):
                idx, out = fut.result()
                results[idx:idx + len(out)] = out
                done += len(out)
                if progress:
                    progress(done, n)

    fails = [(i, msg) for i, (st, msg) in enumerate(results) if st != "ok"]
    if fails:
        detail = "; ".join(f"[{i}] {m}" for i, m in fails[:5])
        raise ZeroPolishError(
            f"{len(fails)}/{n} zeros failed to polish: {detail}"
            + ("; ..." if len(fails) > 5 else ""))
    with mp.workdps(dps):
        return [mp.mpf(msg) for _, msg in results]


# ---------------------------------------------------------------------------
# seed acquisition
# ---------------------------------------------------------------------------

def _nzeros(T_max: float) -> int:
    with mp.workdps(30):
        return int(mp.nzeros(T_max))


def _seeds_from_json(T_max: float, n_expect: int, seed_dir: Path):
    """Ordinate seeds from any existing zeros_dps*/zeros_polish_dps* JSON
    covering T_max. Read-only; a partially-written or short file (a builder
    may be running in the background) is skipped, never trusted."""
    cands = []
    for p in seed_dir.glob("zeros*json"):
        m = _JSON_SEED_RE.match(p.name)
        if m and float(m.group(2)) >= T_max:
            cands.append((float(m.group(2)), -int(m.group(1)), p))
    for _, neg_dps, p in sorted(cands):
        try:
            raw = json.loads(p.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        with mp.workdps(50):
            gz = [g for g in (mp.mpf(s) for s in raw) if g <= T_max]
        if len(gz) == n_expect:
            hint = min(-neg_dps, 40)
            return [mp.nstr(g, 40) for g in gz], p.name, hint
    return None, None, None


def _seeds_from_pickle(T_max: float, n_expect: int, seed_dir: Path):
    """Ordinate seeds from zeta.py's hashed pickle caches. The key is
    sha1("zeta|{T:.6f}|{prec}"), so we probe the historical (T, prec) grid
    plus the requested T_max itself."""
    for T in sorted({float(T_max), *map(float, _PICKLE_T_SWEEP)}):
        if T < T_max:
            continue
        for prec in _PICKLE_PREC_SWEEP:
            key = hashlib.sha1(f"zeta|{T:.6f}|{int(prec)}".encode()).hexdigest()[:16]
            p = seed_dir / f"zeta_zeros_{key}.pkl"
            if not p.exists():
                continue
            try:
                with open(p, "rb") as f:
                    rhos = pickle.load(f)
            except Exception:
                continue
            with mp.workdps(50):
                gz = [g for g in (mp.im(r) for r in rhos) if g <= T_max]
            if len(gz) == n_expect:
                return [mp.nstr(g, 40) for g in gz], p.name, min(prec, 40)
    return None, None, None


def _scan_band(job):
    """Sign-change scan of Z on a grid band, bisected to ~1e-8 seeds.
    Module-level for pickling. Grid points are integer-indexed globally so
    parallel bands share exact seams and no bracket is missed."""
    i0, i1, step, scan_dps = job
    seeds = []
    with mp.workdps(scan_dps):
        zprev = mp.siegelz(i0 * step)
        for i in range(i0 + 1, i1 + 1):
            z = mp.siegelz(i * step)
            if mp.sign(zprev) * mp.sign(z) < 0:
                a, b = (i - 1) * step, i * step
                fa = zprev
                for _ in range(28):
                    c = (a + b) / 2
                    fc = mp.siegelz(c)
                    if fc == 0:
                        a = b = c
                        break
                    if mp.sign(fa) * mp.sign(fc) < 0:
                        b = c
                    else:
                        a, fa = c, fc
                seeds.append(float((a + b) / 2))
            zprev = z
    return i0, seeds


def _seeds_from_scan(T_max: float, n_expect: int, workers: int,
                     say=lambda *_: None):
    """Grid scan of siegelz at low dps. Step starts at mean_gap/8 (min zero
    gap below T ~ 1000 is ~0.4, mean gap 2*pi/log(T/2*pi)); on a count
    mismatch the step halves and the scan reruns, because a miss means two
    zeros shared a grid cell."""
    mean_gap = 2 * 3.141592653589793 / max(1.0, float(mp.log(max(T_max, 20) / (2 * mp.pi))))
    step = float(min(0.05, mean_gap / 8))
    for attempt in range(3):
        n_grid = int(T_max / step) + 1
        nb = max(1, 4 * workers)
        bsz = max(64, -(-n_grid // nb))
        # dps escalates with the retry: a mismatch can also mean a grid value
        # of Z so small its sign was noise at the previous precision
        jobs = [(i, min(i + bsz, n_grid), step, 12 + 4 * attempt)
                for i in range(0, n_grid, bsz)]
        parts = {}
        if workers == 1:
            for j in jobs:
                i0, seeds = _scan_band(j)
                parts[i0] = seeds
        else:
            with ProcessPoolExecutor(max_workers=workers) as ex:
                for fut in as_completed({ex.submit(_scan_band, j) for j in jobs}):
                    i0, seeds = fut.result()
                    parts[i0] = seeds
        seeds = [s for i0 in sorted(parts) for s in parts[i0]
                 if s <= T_max]
        if len(seeds) == n_expect:
            return [f"{s:.10f}" for s in seeds]
        say(f"  scan step {step:.4f}: {len(seeds)} sign changes, expected "
            f"{n_expect}; refining")
        step /= 2
    return None


def _seeds_from_zetazero(T_max: float, say=lambda *_: None):
    """Authoritative fallback: enumerate mp.zetazero(k) at dps 30. Slowest
    path but correct by construction (zetazero is index-verified)."""
    seeds = []
    with mp.workdps(30):
        k = 1
        while True:
            g = mp.im(mp.zetazero(k))
            if g > T_max:
                break
            seeds.append(mp.nstr(g, 30))
            k += 1
            if k % 50 == 0:
                say(f"  zetazero enumeration: {k} zeros, t = {float(g):.1f}")
            if k > 1_000_000:
                raise ZeroPolishError("zetazero enumeration safety cap hit")
    return seeds


# ---------------------------------------------------------------------------
# end-to-end
# ---------------------------------------------------------------------------

def _cache_path(T_max: float, dps: int, cache_dir: Path) -> Path:
    return cache_dir / f"zeros_polish_dps{int(dps)}_T{T_max:g}.json"


def zeros_hp(T_max: float, dps: int, workers: int = 1, cache: bool = True,
             cache_dir=None, guard: int = 15, validate: bool = True,
             verbose: bool = True):
    """All zero ordinates 0 < gamma <= T_max at dps digits. Returns a sorted
    list of mp.mpf.

    Pipeline: seed (existing JSON/pickle caches, else siegelz scan, else
    mp.zetazero at dps 30) -> batch Newton polish at dps + guard -> per-zero
    sign-change validation -> count check against mp.nzeros(T_max) -> cache.

    Cache file: {cache_dir}/zeros_polish_dps{dps}_T{T}.json, a JSON list of
    decimal strings (the e2as/e2au format). An existing file is loaded as-is
    and NEVER overwritten. Seeds are always harvested from the shared cache
    dir; cache_dir only redirects where THIS module's result is written
    (tests use a temp dir).
    """
    say = (lambda *a: print(*a, flush=True)) if verbose else (lambda *a: None)
    cache_dir = Path(cache_dir) if cache_dir is not None else CACHE_DIR
    path = _cache_path(T_max, dps, cache_dir)
    if cache and path.exists():
        with mp.workdps(dps):
            gz = [mp.mpf(s) for s in json.loads(path.read_text())]
        say(f"loaded {len(gz)} zeros from cache {path.name}")
        return gz

    t0 = time.time()
    n_expect = _nzeros(T_max)
    say(f"zeros_hp: T_max = {T_max:g}, dps = {dps}, expecting {n_expect} "
        f"zeros (mp.nzeros)")

    seeds, src, hint = _seeds_from_json(T_max, n_expect, CACHE_DIR)
    if seeds is None:
        seeds, src, hint = _seeds_from_pickle(T_max, n_expect, CACHE_DIR)
    if seeds is None:
        say("  no cache seeds; scanning siegelz for sign changes")
        seeds, src, hint = _seeds_from_scan(T_max, n_expect, workers, say), \
            "siegelz scan", 8
    if seeds is None:
        say("  scan inconclusive; enumerating with mp.zetazero at dps 30")
        seeds, src, hint = _seeds_from_zetazero(T_max, say), \
            "mp.zetazero dps 30", 28
    say(f"  seeds: {len(seeds)} from {src}  ({time.time() - t0:.1f} s)")

    last = [0.0]

    def prog(done, n):
        if verbose and (done == n or time.time() - last[0] > 10):
            last[0] = time.time()
            say(f"  polished {done}/{n}  ({time.time() - t0:.1f} s)")

    gz = polish_zeros(seeds, dps, workers=workers, guard=guard,
                      validate=validate, seed_digits=hint, progress=prog)

    gz.sort()
    if len(gz) != n_expect:
        raise ZeroPolishError(
            f"count check failed: {len(gz)} polished vs {n_expect} expected")
    for a, b in zip(gz, gz[1:]):
        if b - a <= mp.mpf(10) ** (-(dps - 10)):
            raise ZeroPolishError(
                f"duplicate zeros after polish near t = {float(a):.6f} "
                "(two seeds converged to one root)")
    say(f"  count check: {len(gz)} == nzeros({T_max:g}); all "
        f"{'validated' if validate else 'polished (validation OFF)'}  "
        f"({time.time() - t0:.1f} s)")

    # normalize through the cache representation so a fresh computation and a
    # later cache load return bit-identical values
    strs = [mp.nstr(g, dps) for g in gz]
    with mp.workdps(dps):
        gz = [mp.mpf(s) for s in strs]

    if cache:
        cache_dir.mkdir(parents=True, exist_ok=True)
        if not path.exists():  # never overwrite an existing cache key
            tmp = path.with_suffix(".json.tmp%d" % os.getpid())
            tmp.write_text(json.dumps(strs))
            os.replace(tmp, path)
            say(f"  cached -> {path}")
    return gz


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="Bulk high-precision zeta zeros via batch Newton polish")
    ap.add_argument("--tmax", type=float, required=True)
    ap.add_argument("--dps", type=int, required=True)
    ap.add_argument("--workers", type=int, default=1)
    ap.add_argument("--no-cache", action="store_true",
                    help="compute only, do not read or write the cache")
    ap.add_argument("--no-validate", action="store_true",
                    help="skip the per-zero sign-change bracket check")
    args = ap.parse_args()
    t0 = time.time()
    gz = zeros_hp(args.tmax, args.dps, workers=args.workers,
                  cache=not args.no_cache, validate=not args.no_validate)
    print(f"{len(gz)} zeros to T = {args.tmax:g} at {args.dps} digits in "
          f"{time.time() - t0:.1f} s")
    print(f"first: {mp.nstr(gz[0], min(args.dps, 40))}")
    print(f"last : {mp.nstr(gz[-1], min(args.dps, 40))}")


if __name__ == "__main__":
    main()
