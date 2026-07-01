"""Fractal-dimension estimators for point sets sampled from an attractor.

Two estimators, each of a different flavor of "dimension":

correlation_dimension  D_2 via Grassberger-Procaccia. The correlation sum
    C(r) = fraction of point pairs closer than r scales as C(r) ~ r^{D_2}
    in the fractal regime, so D_2 is the slope of log C vs log r. A Theiler
    window excludes temporally close pairs, which would otherwise bias the
    estimate downward through trajectory autocorrelation.

generalized_dimensions  the Renyi dimension ladder D_q via box counting.
    Partition space into boxes of side eps, let p_i be the fraction of points
    in box i, and define the partition function Z_q(eps) = sum_i p_i^q. Then
    D_q = lim (1/(q-1)) log Z_q / log eps  (with the q=1 information-dimension
    limit handled separately). D_0 is the box-counting (capacity) dimension,
    D_1 the information dimension, D_2 the correlation dimension. A strict
    ordering D_0 >= D_1 >= D_2 with real spread is the signature of a
    multifractal measure; equality across q means monofractal.

Reference: Grassberger & Procaccia, Phys. Rev. Lett. 50 (1983) 346;
Hentschel & Procaccia, Physica D 8 (1983) 435.
"""

from __future__ import annotations

import numpy as np


def correlation_dimension(points, n_pairs=3_000_000, theiler=20,
                          n_r=48, c_lo=1e-3, c_hi=1e-1, seed=0):
    """Estimate D_2 from a trajectory via Grassberger-Procaccia.

    points : (N, dim) array, ordered along the trajectory (index = time).
    Returns (D2, info) where info holds the log-log curve and the fit window,
    for plotting. The slope is fit over the scaling region where the
    correlation sum C(r) lies in [c_lo, c_hi], the standard clean band.
    """
    pts = np.asarray(points, dtype=float)
    N = len(pts)
    rng = np.random.default_rng(seed)

    i = rng.integers(0, N, size=n_pairs)
    j = rng.integers(0, N, size=n_pairs)
    keep = np.abs(i - j) > theiler
    i, j = i[keep], j[keep]
    d = np.linalg.norm(pts[i] - pts[j], axis=1)
    d = d[d > 0]

    r_lo = np.percentile(d, 0.5)
    r_hi = np.percentile(d, 60.0)
    rs = np.logspace(np.log10(r_lo), np.log10(r_hi), n_r)
    d_sorted = np.sort(d)
    counts = np.searchsorted(d_sorted, rs, side="right")
    C = counts / d.size

    log_r = np.log(rs)
    log_C = np.log(np.clip(C, 1e-300, None))
    sel = (C >= c_lo) & (C <= c_hi)
    if sel.sum() < 3:
        # widen the band if the default one caught too few points
        sel = (C >= C[C > 0].min()) & (C <= 0.3)
    slope, intercept = np.polyfit(log_r[sel], log_C[sel], 1)

    info = {
        "log_r": log_r,
        "log_C": log_C,
        "sel": sel,
        "fit": (slope, intercept),
    }
    return float(slope), info


def generalized_dimensions(points, q_values, k_range=(3, 9), seed=0):
    """Estimate the Renyi dimension ladder D_q by box counting.

    points : (N, dim) array. k_range gives the range of dyadic refinements:
    box side eps = 1 / 2^k over the normalized bounding cube, for k in
    [k_range[0], k_range[1]]. Returns a dict {q: D_q} plus per-scale detail.
    """
    pts = np.asarray(points, dtype=float)
    mins = pts.min(axis=0)
    span = (pts.max(axis=0) - mins).max()
    norm = (pts - mins) / span                  # into [0,1]^dim, aspect kept
    dim = pts.shape[1]

    ks = list(range(k_range[0], k_range[1] + 1))
    log_eps = np.array([-k * np.log(2.0) for k in ks])   # log(eps), eps = 2^-k

    q_values = np.asarray(q_values, dtype=float)
    # log Z_q(eps) for q != 1, and sum p_i log p_i for q == 1.
    logZ = {float(q): [] for q in q_values}
    entropy = []          # sum p_i log p_i, for D_1
    box_counts = []

    for k in ks:
        nb = 2 ** k
        idx = np.minimum((norm * nb).astype(np.int64), nb - 1)
        # unique box id via mixed-radix encoding
        key = np.zeros(len(idx), dtype=np.int64)
        for d in range(dim):
            key = key * nb + idx[:, d]
        _, counts = np.unique(key, return_counts=True)
        p = counts / counts.sum()
        box_counts.append(len(counts))
        entropy.append(np.sum(p * np.log(p)))
        for q in q_values:
            qf = float(q)
            if abs(qf - 1.0) < 1e-9:
                continue
            logZ[qf].append(np.log(np.sum(p ** qf)))

    dims = {}
    detail = {"ks": ks, "log_eps": log_eps, "box_counts": box_counts}
    for q in q_values:
        qf = float(q)
        if abs(qf - 1.0) < 1e-9:
            slope, _ = np.polyfit(log_eps, np.array(entropy), 1)
            dims[qf] = float(slope)           # D_1 = d(sum p log p)/d(log eps)
        else:
            slope, _ = np.polyfit(log_eps, np.array(logZ[qf]), 1)
            dims[qf] = float(slope / (qf - 1.0))
    return dims, detail
