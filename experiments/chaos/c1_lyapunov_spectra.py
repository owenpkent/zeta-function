"""C1: Lyapunov spectra and Kaplan-Yorke dimension for the three systems.

Computes the full ordered Lyapunov spectrum of Lorenz, Rossler, and Henon via
the Benettin tangent-space QR method, then the Kaplan-Yorke dimension from each
spectrum, and checks both against the literature values stored in systems.py.

The point of this script is calibration: it confirms the estimator reproduces
published exponents, so the dimension work in C2 and C3 rests on a trusted base.

Run:
    python -m experiments.chaos.c1_lyapunov_spectra
"""

from __future__ import annotations

import numpy as np

from experiments.chaos.systems import SYSTEMS
from experiments.chaos.lyapunov import lyapunov_spectrum, kaplan_yorke


def _fmt(vals):
    return "[" + ", ".join("%+.4f" % v for v in vals) + "]"


def main():
    print("C1  Lyapunov spectra (Benettin QR) and Kaplan-Yorke dimension")
    print("=" * 68)
    for name in ("Lorenz", "Rossler", "Henon"):
        sys = SYSTEMS[name]
        if sys.is_map:
            lam = lyapunov_spectrum(sys, n_steps=400_000)
            unit = "per iterate"
        else:
            lam = lyapunov_spectrum(sys, total_time=800.0)
            unit = "per unit time"
        d_ky = kaplan_yorke(lam)
        ref_lam = sys.known["lyapunov"]
        ref_dky = sys.known["kaplan_yorke"]

        print("\n%s  (%s)" % (name, unit))
        print("  lambda measured : %s" % _fmt(lam))
        print("  lambda reference: %s" % _fmt(ref_lam))
        print("  sum(lambda)     : %+.4f   (= average phase-space contraction)"
              % float(np.sum(lam)))
        print("  largest exponent: %+.4f   -> %s"
              % (lam[0], "CHAOS (positive)" if lam[0] > 1e-3 else "not chaotic"))
        print("  Kaplan-Yorke dim: %.4f   (reference %.4f)" % (d_ky, ref_dky))

    print("\n" + "=" * 68)
    print("Reading: a positive largest exponent with a fractal (non-integer)")
    print("Kaplan-Yorke dimension is the joint signature of a strange attractor.")
    print("The exponents sum to the mean contraction rate, so the attractor")
    print("lives on zero volume yet stretches along the unstable direction.")


if __name__ == "__main__":
    main()
