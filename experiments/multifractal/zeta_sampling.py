"""Sampling log|zeta(1/2 + it)| via mpmath, with disk caching.

mpmath evaluation of zeta on the critical line is the bottleneck for E1 and
E2. We cache each (T_center, window, num_points, prec) call to .npz files
under experiments/multifractal/_cache/.

A laptop-friendly run: a single window of width 1 with 2048 points at
T = 10^6 takes roughly 20 seconds; at T = 10^8 it climbs to a few minutes.
"""

from __future__ import annotations

import hashlib
import os
from pathlib import Path

import numpy as np


CACHE_DIR = Path(__file__).resolve().parent / "_cache"


def _cache_key(T_center, window, num_points, prec):
    raw = f"{float(T_center):.6f}|{float(window):.6f}|{int(num_points)}|{int(prec)}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:16]


def sample_log_zeta_window(T_center, window=1.0, num_points=2048, prec=30, use_cache=True):
    """Sample log|zeta(1/2 + it)| at num_points uniform t in [T_center - w/2, T_center + w/2].

    Returns (ts, log_abs_zeta).
    """
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    key = _cache_key(T_center, window, num_points, prec)
    path = CACHE_DIR / f"zeta_window_{key}.npz"
    if use_cache and path.exists():
        data = np.load(path)
        return data["ts"], data["log_abs"]

    try:
        import mpmath as mp
    except ImportError as exc:
        raise SystemExit(
            "mpmath is required for zeta sampling. Install via `pip install mpmath`."
        ) from exc

    mp.mp.dps = int(prec)
    half = window / 2.0
    ts = np.linspace(T_center - half, T_center + half, int(num_points))
    log_abs = np.empty(ts.size, dtype=float)
    half_mp = mp.mpf("0.5")
    for k, t in enumerate(ts):
        z = mp.zeta(mp.mpc(half_mp, mp.mpf(float(t))))
        log_abs[k] = float(mp.log(abs(z)))

    np.savez_compressed(path, ts=ts, log_abs=log_abs)
    return ts, log_abs


def window_max(T_center, window=1.0, num_points=4096, prec=30):
    """max_{|h|<=window/2} log|zeta(1/2 + i(T_center + h))|.

    Discrete maximum over a fine sampling; not a true continuous maximum but
    accurate to within typical local derivative * sample spacing.
    """
    _, log_abs = sample_log_zeta_window(
        T_center=T_center,
        window=window,
        num_points=num_points,
        prec=prec,
    )
    return float(np.max(log_abs))
