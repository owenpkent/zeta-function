"""The executable falsifier oracle (Reduction Engine, increment 1).

Spec: `experiments/lemma_db/oracle_spec.md`. Design: `docs/03_research/reduction_engine.md` section 2.

The oracle takes a structured Candidate and runs four cheap-first disqualifiers
against the Davenport-Heilbronn control and the candidate's own declarations. It
turns the project's disciplines from audited flags into computed verdicts.

THE ONE BOUNDARY THAT DEFINES THIS MODULE
-----------------------------------------
The oracle KILLS or PARKS. It never VALIDATES. A candidate that survives every
disqualifier returns PASS, and PASS means exactly "not yet killed," never
"correct." The single source of positive truth is the Lean floor. Every return
value here preserves that asymmetry.

WHAT THE FLIP TEST ACTUALLY FOUND
---------------------------------
The spec first guessed the Li-coefficient functional would be the reference
SEPARATING detector. The numbers say the opposite (and it is a sharper result):
over zeros to T=100, min_n lambda_n is +0.017 for zeta and +0.080 for D-H, both
non-negative. The canonical soft positivity functional is BLIND to D-H's off-line
zeros in any reachable range, so the flip test KILLS it. The only detector that
separates D-H is one that reads the zero locations directly, which the K1
disqualifier KILLS as circular. So the oracle reproduces the marginal-positivity
wall as a two-move trap: every detector dies, by blindness or by circularity.
That is `demo()`.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Callable, Optional

import mpmath as mp

from experiments._shared import DavenportHeilbronn, zeta_L
from experiments._shared.lfunction import LFunction, li_coefficients

# Verdict results.
KILL = "KILL"
PARK = "PARK"
PASS = "PASS"
UNTESTABLE = "UNTESTABLE"


class NoEulerProduct(Exception):
    """Raised by a construction that cannot be instantiated without an Euler
    product. The structural D-H firewall: no Euler product => no Frobenius
    element => the polarized algebra is uninhabited (AX-FORM)."""


@dataclass
class Verdict:
    result: str                       # KILL | PARK | PASS | UNTESTABLE
    reason: str
    evidence: object = None


@dataclass
class Candidate:
    """The interface contract. The oracle cannot run on prose; a candidate must
    arrive in this structured form (the BUILDER / loop driver emits against it)."""
    node_id: str
    claim_type: str                   # positivity | spectral | statistical | trace | other
    claims_rh_equivalent: bool
    inputs: frozenset                 # declared inputs; {'zero_locations'} is the K1 tripwire
    construction: Optional[Callable[[LFunction], object]] = None
    detector: Optional[Callable[[LFunction], float]] = None
    notes: str = ""


@dataclass
class OracleVerdict:
    node_id: str
    overall: str                      # KILL | PARK | PASS  (PASS == "not yet killed", never "valid")
    killed_by: Optional[str]
    verdicts: dict                    # disqualifier name -> Verdict
    dh_buildable: str                 # 'true' | 'false' | 'N/A', COMPUTED where possible


# ---------------------------------------------------------------------------
# Reference detectors and constructions. A real candidate supplies its own;
# these are the canonical examples that encode the two-move wall.
# ---------------------------------------------------------------------------

DETECTOR_T_MAX = 100.0   # aligned with smoke_test test 5's D-H zero cache (key dh|100|30|0.5)


def li_min_detector(L: LFunction) -> float:
    """min_n lambda_n, the canonical soft positivity functional (Li's criterion).
    EMPIRICALLY BLIND to D-H: +0.080 on D-H, +0.017 on zeta (zeros to T=100).
    A candidate relying on this is killed by the flip test."""
    mp.mp.dps = 30
    coeffs, _ = li_coefficients(L, 12, T_max=DETECTOR_T_MAX, prec=30)
    return float(min(coeffs))


def offline_zero_detector(L: LFunction) -> float:
    """-1 if any zero off the critical line below T_max, else +1. SEPARATES D-H
    (it reads the off-line zero at 0.8085+85.699i), but it is K1-circular: it
    consumes the zero locations, which is the conclusion. Killed by k1_noncircular
    when the candidate honestly declares 'zero_locations' as an input."""
    mp.mp.dps = 30
    zs = L.zeros(DETECTOR_T_MAX, prec=30)
    return -1.0 if any(abs(float(z.real) - 0.5) > 0.01 for z in zs) else 1.0


def realization_construction(L: LFunction) -> complex:
    """A realization-half object: a value comes out for ANY L-function, D-H
    included (here, L(2)). Computes dh_buildable='true'."""
    mp.mp.dps = 30
    return complex(L.evaluate(mp.mpc(2)))


def signature_construction(L: LFunction) -> float:
    """A signature-half object that exists only with an Euler product. On D-H it
    raises NoEulerProduct, so dh_buildable='false' by formation (AX-FORM)."""
    if not getattr(L, "has_euler_product", False):
        raise NoEulerProduct(f"{L.name} has no Euler product; the Frobenius algebra is uninhabited")
    return 1.0


# ---------------------------------------------------------------------------
# The disqualifiers, cheapest first. Each returns a Verdict.
# Run order: level (static) -> k1 (static) -> dh_buildable (one eval) -> flip (zeros).
# ---------------------------------------------------------------------------

def level_classifier(c: Candidate) -> Verdict:
    """D0. Kill a Level-3-only edge into RH (statistics/spectrum without a
    positivity claim are compatible with a zero at beta=0.51)."""
    if c.claim_type in ("statistical", "spectral") and not c.claims_rh_equivalent:
        return Verdict(KILL, f"Level-3: {c.claim_type} without a positivity / RH-equivalence claim",
                       evidence=c.claim_type)
    if c.claim_type == "trace" and not c.claims_rh_equivalent:
        return Verdict(PARK, "realization-only (trace / explicit-formula); D-H has this too")
    return Verdict(PASS, "claims Level-4 positivity or RH-equivalence")


ZERO_INPUTS = frozenset({"zero_locations", "zeros", "rho", "critical_zeros"})


def k1_noncircular(c: Candidate) -> Verdict:
    """D3 (run early; it is static). Positivity must come from a polarization,
    never be read off the zeros."""
    bad = c.inputs & ZERO_INPUTS
    if c.claim_type == "positivity" and bad:
        return Verdict(KILL, "circular: positivity claim consumes zero locations as input",
                       evidence=sorted(bad))
    return Verdict(PASS, "positivity does not depend on zero locations")


def _is_finite(v) -> bool:
    try:
        z = complex(v)
        return math.isfinite(z.real) and math.isfinite(z.imag)
    except (TypeError, ValueError):
        try:
            return bool(mp.isfinite(v))
        except Exception:
            return False


def dh_buildable_compute(c: Candidate) -> Verdict:
    """D1. Replace the hand-set dh_buildable flag with a computation: instantiate
    the construction on D-H. A finite object out => realization-half (PARK,
    dh_buildable='true'). A NoEulerProduct raise => structurally absent (PASS,
    dh_buildable='false'). The graph-level dh_audit turns a 'true' content node on
    a load-bearing path into a build failure; the oracle only computes the flag."""
    if c.construction is None:
        return Verdict(UNTESTABLE, "abstract candidate; no construction callable",
                       evidence={"dh_buildable": "N/A"})
    try:
        val = c.construction(DavenportHeilbronn())
    except (NoEulerProduct, NotImplementedError) as e:
        return Verdict(PASS, f"construction is uninstantiable on D-H: {e}",
                       evidence={"dh_buildable": "false"})
    if _is_finite(val):
        return Verdict(PARK, "construction returns a finite value on D-H (realization-half)",
                       evidence={"dh_buildable": "true", "dh_value": repr(val)})
    return Verdict(PASS, "construction does not produce a finite D-H object",
                   evidence={"dh_buildable": "false"})


def flip_test(c: Candidate) -> Verdict:
    """D2 (most expensive: computes zeros / Li sums). Run the candidate's own
    detector on zeta and on D-H. A detector that stays non-negative on D-H is
    blind to exactly the off-line zeros RH forbids, so it cannot be detecting RH."""
    if c.detector is None:
        return Verdict(UNTESTABLE, "no detector to flip")
    d_zeta = c.detector(zeta_L)
    d_dh = c.detector(DavenportHeilbronn())
    ev = {"zeta": d_zeta, "dh": d_dh}
    if d_dh >= 0 and d_zeta >= 0:
        return Verdict(KILL, "detector non-negative on D-H too: blind to its off-line zeros", evidence=ev)
    if d_zeta < 0:
        return Verdict(PARK, "detector negative on zeta too: mis-specified / too strong", evidence=ev)
    return Verdict(PASS, "detector separates D-H (negative there, non-negative on zeta)", evidence=ev)


DISQUALIFIERS = [
    ("level", level_classifier),
    ("k1_noncircular", k1_noncircular),
    ("dh_buildable", dh_buildable_compute),
    ("flip_test", flip_test),
]


def run_oracle(c: Candidate) -> OracleVerdict:
    """Run the disqualifiers cheap-first, short-circuiting on the first KILL.
    overall = KILL if any killed; else PARK if any parked; else PASS.
    PASS means "not yet killed," never "valid"."""
    verdicts: dict = {}
    dh_flag = "N/A"
    saw_park = False
    for name, fn in DISQUALIFIERS:
        v = fn(c)
        verdicts[name] = v
        if name == "dh_buildable" and isinstance(v.evidence, dict):
            dh_flag = v.evidence.get("dh_buildable", dh_flag)
        if v.result == KILL:
            return OracleVerdict(c.node_id, KILL, name, verdicts, dh_flag)
        if v.result == PARK:
            saw_park = True
    return OracleVerdict(c.node_id, PARK if saw_park else PASS, None, verdicts, dh_flag)


# ---------------------------------------------------------------------------
# Canonical example candidates: the two-move wall and the honest target shape.
# ---------------------------------------------------------------------------

EXAMPLE_CANDIDATES = {
    # The natural soft positivity detector. Survives level/k1/dh, dies at the
    # flip test because Li is blind to D-H.
    "soft-li": Candidate(
        node_id="EX-soft-li", claim_type="positivity", claims_rh_equivalent=True,
        inputs=frozenset({"polarization"}), construction=signature_construction,
        detector=li_min_detector, notes="canonical soft detector; flip test kills it (Li is blind)"),
    # The only detector that separates D-H reads the zeros: K1-circular.
    "zero-reader": Candidate(
        node_id="EX-zero-reader", claim_type="positivity", claims_rh_equivalent=True,
        inputs=frozenset({"zero_locations"}), construction=None,
        detector=offline_zero_detector, notes="separates D-H but circular; dies at K1 before the flip test"),
    # Level-3.
    "level3": Candidate(
        node_id="EX-level3", claim_type="statistical", claims_rh_equivalent=False,
        inputs=frozenset(), notes="GUE-style statistics, no positivity claim"),
    # A realization-half object: dh_buildable computes to 'true'.
    "realization": Candidate(
        node_id="EX-realization", claim_type="trace", claims_rh_equivalent=False,
        inputs=frozenset(), construction=realization_construction,
        notes="trace/realization; D-H instantiates it (dh_buildable=true)"),
    # The idealized honest target (M4 shape): abstract, clean, survives the cheap
    # oracle. overall PASS == not yet killed, NOT valid.
    "abstract-honest": Candidate(
        node_id="EX-abstract-honest", claim_type="positivity", claims_rh_equivalent=True,
        inputs=frozenset({"polarization", "euler_product"}), construction=None, detector=None,
        notes="abstract signature construction; oracle cannot dynamically test it"),
}


def demo() -> None:
    print("Reduction Engine oracle: the marginal-positivity wall as a two-move trap\n")
    for key in ("soft-li", "zero-reader", "level3", "realization", "abstract-honest"):
        ov = run_oracle(EXAMPLE_CANDIDATES[key])
        head = f"{key:>16}  ->  {ov.overall:4}"
        tail = f"killed_by={ov.killed_by}" if ov.killed_by else f"dh_buildable={ov.dh_buildable}"
        print(f"{head}   {tail}")
        if ov.killed_by:
            print(f"{'':18}    {ov.verdicts[ov.killed_by].reason}")
    print("\nsoft-li dies by BLINDNESS (Li >= 0 on D-H); zero-reader dies by CIRCULARITY "
          "(reads zeros).\nEvery detector dies. That is why the problem is open. "
          "PASS = not yet killed, never valid.")


if __name__ == "__main__":
    demo()
