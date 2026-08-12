r"""The wrong-approach detector, expressed as an ASSAY experiment.

This is the second domain ported onto ASSAY, and it exists to test the claim the
library makes about itself: that the invariants are domain-agnostic, and that a
program about $L$-functions and one about unit-distance graphs need the same
refusal machinery. Nothing in `assay` knows what a zero is.

THE QUESTION, per unit: does this $L$-function have a zero off the critical line
below height $T$? YES for Davenport-Heilbronn (Davenport-Heilbronn 1936; the
first off-line zero sits near $0.8085 + 85.699i$), NO for $\zeta$ in the same
window (RH is verified numerically far past it).

WHY THIS IS THE RIGHT SHAPE. The repo's central discipline is that D-H is the
wrong-approach detector: it has a functional equation but no Euler product and
genuine off-line zeros, so any method that cannot tell it apart from $\zeta$ is
structurally wrong. Stated as an existence question, that discipline IS the
ASSAY control: the tool must return YES on D-H. A tool that says D-H has no
off-line zeros has disqualified itself, and the runner refuses to let it produce
anything else.

THE FOUR GUARDS, in this domain:

  control     D-H must yield an off-line zero. This is the detector.
  ladder      Both directions against external answers: YES on D-H (a theorem),
              NO on $\zeta$ below height 100 (verified numerics).
  probe       NON-VACUITY, and it is not decorative here. "No off-line zero in
              the window" is worthless if the search found no zeros AT ALL: a
              broken evaluator returns exactly that. So the probe demands the
              window contain zeros, on or off the line, before a NO is counted.
  verify      A claimed off-line zero is re-checked by code disjoint from the
              search: $|L(\rho)|$ must be small, $|\mathrm{Re}\,\rho - 1/2|$ must
              exceed a margin so numerical drift on the critical line cannot
              masquerade as a violation, and the functional-equation partner
              $1 - \bar\rho$ must also be a zero.

Run:  .venv/bin/python experiments/assay_offline_zeros.py
"""
from __future__ import annotations

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))      # the repo root, so experiments/ is a package

import mpmath as mp                                            # noqa: E402
from assay.core import Experiment, Verdict, run, YES, NO, UNKNOWN  # noqa: E402
from experiments._shared.davenport_heilbronn import (           # noqa: E402
    DavenportHeilbronn)

T_MAX = 100.0            # search height; the first D-H off-line zero is at ~85.7
OFF_LINE_MARGIN = 1e-3   # how far from Re = 1/2 counts as genuinely off-line
ZERO_TOL = 1e-8


class Zeta:
    """The control's counterpart: an Euler product where RH is believed."""
    name = "zeta"

    def evaluate(self, s):
        return mp.zeta(s)

    def zeros(self, T_max, **kw):
        """Zeros of zeta below T_max, from mpmath's zetazero (on the line)."""
        out, k = [], 1
        while True:
            z = mp.zetazero(k)
            if mp.im(z) > T_max:
                break
            out.append(z)
            k += 1
        return out


class DH:
    name = "davenport_heilbronn"

    def __init__(self):
        self._f = DavenportHeilbronn()

    def evaluate(self, s):
        return self._f.evaluate(s)

    def zeros(self, T_max, **kw):
        return list(self._f.zeros(T_max, **kw))


def off_line(rho):
    return abs(mp.re(rho) - mp.mpf("0.5")) > OFF_LINE_MARGIN


def search(L):
    """The tool: is there an off-line zero below T_MAX? Returns (verdict, detail)."""
    zs = L.zeros(T_MAX)
    off = [z for z in zs if off_line(z)]
    return zs, off


def build() -> Experiment:
    zeta, dh = Zeta(), DH()

    exp = Experiment(
        name="offline-zeros",
        question=(f"Does this L-function have a zero off the critical line with "
                  f"0 < Im(s) <= {T_MAX:g}?"),
        scope=("Establishes the presence or absence of off-line zeros in a FINITE "
               "window by numerics. It is not a proof of RH for any L-function, "
               "and a NO here is a statement about the window, not the half-plane."),
    )

    # INVARIANT 4, and it is this repo's founding discipline. Davenport-Heilbronn
    # has a functional equation but no Euler product, and provably has off-line
    # zeros. A method that reports otherwise is not weak, it is wrong, and nothing
    # it says about zeta can be trusted.
    @exp.control(name="DH_has_offline_zeros",
                 note="the wrong-approach detector: D-H must betray a broken tool")
    def dh_control():
        _, off = search(dh)
        return YES if off else NO

    # INVARIANT 1, the YES direction, against a theorem.
    @exp.calibration(expect=YES, external=True, name="DH_offline_zero_near_85.7",
                     note="Davenport-Heilbronn 1936; first off-line zero ~0.8085+85.699i")
    def dh_rung():
        _, off = search(dh)
        near = [z for z in off if abs(mp.im(z) - mp.mpf("85.699")) < 1.0]
        return YES if near else NO

    # INVARIANT 1/3, the NO direction. Without this a tool that shouted YES at
    # everything would pass, and every "off-line zero found" would be unfounded.
    @exp.calibration(expect=NO, external=True, name="zeta_has_none_below_100",
                     note="RH verified numerically far beyond height 100")
    def zeta_rung():
        _, off = search(zeta)
        return YES if off else NO

    @exp.units
    def units():
        return ["zeta", "davenport_heilbronn"]

    OBJ = {"zeta": zeta, "davenport_heilbronn": dh}

    @exp.work
    def work(name):
        zs, off = search(OBJ[name])
        return Verdict(YES if off else NO, name,
                       detail={"zeros_found": len(zs),
                               "offline": [str(z) for z in off[:4]]})

    @exp.probe
    def nonvacuous(name):
        """A NO means nothing if the search found no zeros at all: that is what a
        broken evaluator produces, and it is indistinguishable from a genuine
        absence unless you ask."""
        zs, _ = search(OBJ[name])
        return len(zs) > 0

    @exp.verify
    def reverify(name, detail):
        """Independent re-check of a claimed off-line zero, deliberately not
        reusing the search: evaluate directly, demand the margin, and demand the
        functional-equation partner."""
        L = OBJ[name]
        for zs in detail.get("offline", []):
            rho = mp.mpc(zs)
            if abs(L.evaluate(rho)) > ZERO_TOL:
                return False
            if not off_line(rho):
                return False
            partner = mp.mpc(1 - mp.re(rho), mp.im(rho))
            if abs(L.evaluate(partner)) > 1e-4:
                return False
            return True
        return False

    return exp


def main():
    mp.mp.dps = 25
    exp = build()
    out = run(exp, ledger_path=HERE / "_cache" / "assay_offline_zeros.json")
    print()
    if out["halt"]:
        kind, msg = out["halt"]
        print(f"HALT [{kind}]: {msg}")
        return 2 if kind == "HIT" else 1
    print(f"{out['decided']} unit(s) decided")
    return 0


if __name__ == "__main__":
    sys.exit(main())
