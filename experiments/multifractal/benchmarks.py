"""Synthetic benchmark series with known multifractal properties.

These exist to calibrate the MFDFA pipeline. If the pipeline reports the
expected h(q) for white noise (0.5) and fractional Gaussian noise (H), and
the expected curvature for a binomial multiplicative cascade, then results
on zeta and prime data can be trusted.

Generators:
    white_noise(N, rng)          : iid N(0,1). MFDFA expects h(q) = 0.5 const.
    fgn_spectral(N, H, rng)      : fractional Gaussian noise, Hurst H, by
                                   spectral synthesis. MFDFA expects
                                   h(q) = H const (monofractal).
    binomial_cascade(p, levels, rng):
                                   p-binomial multiplicative cascade on
                                   [0, 1], N = 2**levels samples. Multifractal;
                                   alpha runs from -log2(max(p,1-p)) to
                                   -log2(min(p,1-p)) and D(alpha) is the
                                   binomial entropy formula.
"""

from __future__ import annotations

import numpy as np


def white_noise(N, rng=None):
    rng = np.random.default_rng() if rng is None else rng
    return rng.standard_normal(int(N))


def fgn_spectral(N, H, rng=None):
    """Fractional Gaussian noise with Hurst exponent H, via spectral synthesis.

    Not as exact as Davies-Harte circulant embedding but adequate for
    calibration. The expected MFDFA generalized Hurst is h(q) = H for all q.
    """
    rng = np.random.default_rng() if rng is None else rng
    N = int(N)
    # Build a real signal of length N from positive frequencies.
    n_freq = N // 2 + 1
    freqs = np.arange(n_freq) / N
    freqs[0] = 1.0 / N  # avoid divide-by-zero; DC will be zeroed out later
    # fGn power spectrum: S(f) ~ |f|^(1 - 2H)  (for f != 0)
    amplitudes = freqs ** (0.5 - H)
    amplitudes[0] = 0.0  # zero-mean
    phases = rng.uniform(0.0, 2.0 * np.pi, size=n_freq)
    # build a Hermitian-symmetric spectrum and ifft
    spectrum = amplitudes * np.exp(1j * phases)
    if N % 2 == 0:
        spectrum[-1] = spectrum[-1].real  # Nyquist real
    sig = np.fft.irfft(spectrum, n=N)
    sig = (sig - sig.mean()) / sig.std()
    return sig


def binomial_cascade(p, levels, rng=None):
    """Deterministic p-binomial multiplicative cascade.

    Splits the interval [0, 1] in half repeatedly; left half scales by p,
    right by (1 - p). After `levels` iterations the measure has
    2**levels cells. Multifractal for p != 1/2.

    Returns a 1D numpy array of cell masses (sums to 1).
    """
    if not (0.0 < p < 1.0):
        raise ValueError("p must be in (0, 1)")
    measure = np.array([1.0])
    q = 1.0 - p
    for _ in range(int(levels)):
        new = np.empty(2 * measure.size, dtype=float)
        new[0::2] = measure * p
        new[1::2] = measure * q
        measure = new
    return measure


def binomial_cascade_theory(p, q_values):
    """Closed-form MFDFA-equivalent generalized Hurst h(q) for binomial cascade.

    For a p-binomial cascade, tau(q) = -log2(p**q + (1-p)**q). With the MFDFA
    convention h(q) = (tau(q) + 1) / q, this is the prediction to compare
    against.
    """
    q_values = np.asarray(q_values, dtype=float)
    tau = -np.log2(p ** q_values + (1.0 - p) ** q_values)
    h = np.where(np.abs(q_values) > 1e-12, (tau + 1.0) / q_values, np.nan)
    return tau, h
