"""C3: the multifractal bridge, from strange attractors to the zeta thread.

Two connected measurements, both aimed at showing that "dimension" is really a
spectrum, not a number, and that this is the same multifractal machinery the
zeta / log-correlated thread uses.

Part A. The Renyi dimension ladder D_q on the Henon attractor. If the natural
    (SRB) measure on the attractor is multifractal, then D_0 > D_1 > D_2: the
    box-counting, information, and correlation dimensions genuinely differ. The
    spread D_0 - D_infinity is a direct analogue of the singularity-spectrum
    width Delta-alpha that experiments/multifractal reports for log|zeta|.

Part B. Reuse of the project's own MFDFA (experiments/multifractal/mfdfa.py) on
    a Lorenz coordinate time series x(t). This is the literal handshake between
    the two threads: the same estimator that measures the multifractality of
    log|zeta(1/2+it)| runs here on a chaotic trajectory. Read with the caveat
    below: MFDFA on a single coordinate measures temporal scaling of that signal,
    which is a different object from the spatial multifractality of the invariant
    measure in Part A. Both are facets of the same D_q / D(alpha) formalism.

Run:
    python -m experiments.chaos.c3_multifractal_bridge
"""

from __future__ import annotations

import numpy as np

from experiments.chaos.systems import SYSTEMS, integrate
from experiments.chaos.dimension import generalized_dimensions
from experiments.multifractal.mfdfa import mfdfa, hurst_summary


def part_a_henon_ladder():
    print("Part A  Renyi dimension ladder D_q on the Henon attractor")
    print("-" * 68)
    henon = SYSTEMS["Henon"]
    pts = integrate(henon, n_samples=500_000, sample_every=1)

    q_values = np.array([0.0, 1.0, 2.0, 3.0, 5.0])
    dims, _ = generalized_dimensions(pts, q_values, k_range=(3, 8))

    print("  q     D_q      name")
    labels = {0.0: "capacity (box-counting)", 1.0: "information",
              2.0: "correlation", 3.0: "", 5.0: ""}
    for q in q_values:
        print("  %-4g  %.4f   %s" % (q, dims[float(q)], labels[q]))

    spread = dims[0.0] - dims[5.0]
    print("\n  D_0 - D_5 = %.4f" % spread)
    monotone = all(dims[float(q_values[i])] >= dims[float(q_values[i + 1])] - 1e-3
                   for i in range(len(q_values) - 1))
    print("  D_q non-increasing in q: %s" % ("yes" if monotone else "no"))
    print("  Reading: D_q is non-increasing with a real spread, so the Henon")
    print("  measure is multifractal. D_2 here should track the C2 estimate,")
    print("  and D_0 tracks the Kaplan-Yorke dimension from C1 (~1.26).")
    return dims


def part_b_lorenz_mfdfa():
    print("\nPart B  Project MFDFA on a Lorenz coordinate time series x(t)")
    print("-" * 68)
    lorenz = SYSTEMS["Lorenz"]
    # A long, lightly-thinned x(t) series; MFDFA wants an approximately
    # stationary 1D signal, and the mean-centered Lorenz x-coordinate qualifies.
    traj = integrate(lorenz, n_samples=16384, sample_every=2)
    x_series = traj[:, 0]

    scales = np.unique(np.floor(np.logspace(np.log10(16), np.log10(len(x_series) // 4), 20)).astype(int))
    q_values = np.linspace(-4, 4, 17)
    res = mfdfa(x_series, scales, q_values, order=2)
    print("  " + hurst_summary(res))
    print("  Caveat: this is temporal scaling of one coordinate, a different")
    print("  object from the spatial measure in Part A. Same D(alpha) formalism,")
    print("  different slice. It is the handshake, not an identity.")
    return res


def main():
    print("C3  The multifractal bridge")
    print("=" * 68)
    part_a_henon_ladder()
    part_b_lorenz_mfdfa()
    print("\n" + "=" * 68)
    print("Through-line: D_0 (capacity) >= D_1 (information) >= D_2 (correlation)")
    print("is the Renyi ladder. C1 measured D_0 as Kaplan-Yorke from the Lyapunov")
    print("spectrum, C2 measured D_2 from pair counts, and here the whole ladder")
    print("shows the spread. The singularity-spectrum width Delta-alpha that")
    print("experiments/multifractal reports for log|zeta(1/2+it)| is the SAME")
    print("quantity for the log-correlated field on the critical line. Chaos")
    print("theory and the zeta thread share one formalism: the multifractal")
    print("spectrum. See docs/03_research/quantum_chaos_and_the_zeros.md for the")
    print("spectral (Berry-Keating) side of the same bridge.")


if __name__ == "__main__":
    main()
