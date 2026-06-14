"""The proven-case shadow battery: a graded positive value function (Generative Engine, 6f).

Spec / motivation: `docs/03_research/optimizing_rh_for_ai.md` (lever A). This generalizes
the function-field shadow (6d, `fq_shadow.py`) from ONE mirror to a BATTERY.

WHY THIS EXISTS (the blind spot, restated as a design problem)
-------------------------------------------------------------
Marginal positivity means there is NO cheap value signal at the goal M4: nothing returns a
partial score for "almost proved the arithmetic Hodge index." That removes the gradient an
AI (or any search) needs. The function-field shadow supplied ONE positive gradient bit: does
a candidate, specialized to F_q, reproduce Weil's proven theorem (eigenvalues on the sqrt(q)
circle)? This module turns that one bit into a GRADED battery of proven cases, each a
checkpoint a genuine M4 construction must reproduce:

  CP-fq     function field        Weil/Hasse: |alpha| = sqrt(q)              (tests: carries t)
  CP-hodge  algebraic surface     Hodge index: signature (1, rho-1) on NS    (tests: indefinite)
  CP-ahk    matroid Chow ring     AHK: Whitney numbers log-concave           (tests: HR, no variety)
  CP-fh     arithmetic surface    Faltings-Hriljac: Neron-Tate height PD     (tests: a real polarization)
  CP-af     convex bodies         Alexandrov-Fenchel: Lorentzian (1, n-1)    (tests: the convex signature)

A candidate's score is how many applicable checkpoints it reproduces, with the Davenport-
Heilbronn firewall (euler-gated) as a hard side condition. "No gradient" becomes "k of N
checkpoints + firewall holds," which is a signal a generate-evaluate loop can climb.

WHAT THIS IS AND IS NOT (the same asymmetry as the oracle)
----------------------------------------------------------
This is the POSITIVE mirror of `oracle.py` (which KILLS/PARKS on the D-H side). The battery
SCORES; reproducing every checkpoint is NECESSARY, never SUFFICIENT. FULL means "consistent
with every proven case and the firewall," never "proves M4." The single source of positive
truth remains the Lean floor. Each checkpoint encodes a proven theorem's signature as a
checkable property; a candidate supplies the structural object it specializes to in that
domain, and the checkpoint asks whether that object HAS the proven property.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Optional

import numpy as np

from experiments.lemma_db.fq_shadow import elliptic_eigenvalues, circle_defect


# Per-checkpoint verdicts (mirroring fq_shadow's SHADOW_* trio).
CP_PASS = "PASS"   # reproduces the proven signature: consistent
CP_KILL = "KILL"   # supplies an object that BREAKS the proven theorem (wrong signature)
CP_NA = "NA"       # no specialization to this domain


# Aggregate verdicts.
FULL = "FULL"        # passes every applicable checkpoint AND the firewall holds
PARTIAL = "PARTIAL"  # passes some; none broken; the graded middle (the gradient lives here)
BROKEN = "BROKEN"    # breaks at least one proven case (a KILL) -> not a reformulation, a contradiction


# ---------------------------------------------------------------------------
# Signature helpers (the proven signatures are linear-algebra facts; compute them).
# ---------------------------------------------------------------------------

def signature(matrix, tol: float = 1e-9) -> tuple:
    """(n_pos, n_neg, n_zero) of a real symmetric matrix."""
    w = np.linalg.eigvalsh(np.asarray(matrix, dtype=float))
    pos = int((w > tol).sum())
    neg = int((w < -tol).sum())
    return pos, neg, len(w) - pos - neg


def is_lorentzian(matrix, tol: float = 1e-9) -> bool:
    """Signature (1, n-1): exactly one positive eigenvalue, the rest negative.
    The Hodge-index / Castelnuovo-Severi / Alexandrov-Fenchel shape M4 needs."""
    pos, neg, zero = signature(matrix, tol)
    return pos == 1 and zero == 0 and neg == len(np.asarray(matrix)) - 1


def is_pos_def(matrix, tol: float = 1e-9) -> bool:
    w = np.linalg.eigvalsh(np.asarray(matrix, dtype=float))
    return bool((w > tol).all())


def is_log_concave(seq, tol: float = 1e-9) -> bool:
    a = [abs(float(x)) for x in seq]
    return all(a[k] * a[k] >= a[k - 1] * a[k + 1] - tol for k in range(1, len(a) - 1))


# ---------------------------------------------------------------------------
# The checkpoints. Each verifier takes the candidate's specialization data for
# that domain (or None = NA) and returns (verdict, detail). The proven property
# is checked directly, so the checkpoint is self-contained and non-vacuous (it
# passes its own canonical witness; see the test module).
# ---------------------------------------------------------------------------

def _verify_fq(data) -> tuple:
    """data = (q, eigenvalues). PASS iff the eigenvalues sit on the sqrt(q)
    circle (Weil/Hasse). A t-blind candidate supplies a modulus that ignores the
    trace, lands off the circle, and is KILLED (the #40 failure: same signature
    for all t)."""
    if data is None:
        return CP_NA, "no function-field specialization"
    q, eigs = data
    d = circle_defect(eigs, q)
    if d < 1e-9:
        return CP_PASS, f"on the sqrt({q}) circle (defect {d:.2e})"
    return CP_KILL, f"off-circle (defect {d:.2e}): breaks Weil/Hasse (t-blind?)"


def _verify_hodge(data) -> tuple:
    """data = NS intersection matrix. PASS iff signature (1, rho-1) (Hodge index).
    A too-strong candidate that forces a positive-DEFINITE form overshoots (the
    de Branges failure) and is KILLED for the wrong signature."""
    if data is None:
        return CP_NA, "no algebraic-surface specialization"
    pos, neg, zero = signature(data)
    if is_lorentzian(data):
        return CP_PASS, f"signature (1, {neg}) = Hodge index"
    return CP_KILL, f"signature ({pos}, {neg}, {zero}) is not (1, n-1): wrong polarization"


def _verify_ahk(data) -> tuple:
    """data = Whitney-number / characteristic-polynomial coefficient sequence.
    PASS iff log-concave (AHK Hodge-Riemann in degree 1). This is the K1-clean,
    no-variety signature; the arithmetic-blind candidate passes it (it is the one
    thing AHK does supply)."""
    if data is None:
        return CP_NA, "no matroid/combinatorial specialization"
    if len(data) < 3:
        return CP_NA, "sequence too short to test log-concavity"
    if is_log_concave(data):
        return CP_PASS, f"log-concave Whitney sequence {list(data)}"
    return CP_KILL, f"not log-concave: {list(data)} breaks AHK"


def _verify_fh(data) -> tuple:
    """data = Neron-Tate height Gram matrix. PASS iff positive-definite (Faltings-
    Hriljac: the height pairing is PD on the Mordell-Weil lattice; equivalently
    the primitive intersection form is negative-definite on one surface)."""
    if data is None:
        return CP_NA, "no arithmetic-surface (height) specialization"
    if is_pos_def(data):
        return CP_PASS, "Neron-Tate height pairing positive-definite"
    return CP_KILL, "height Gram not positive-definite: breaks Faltings-Hriljac"


def _verify_af(data) -> tuple:
    """data = mixed-volume matrix. PASS iff Lorentzian (1, n-1) (Alexandrov-
    Fenchel). The convex signature is free; reproducing it is necessary but
    arithmetic-blind on its own."""
    if data is None:
        return CP_NA, "no convex-geometry specialization"
    pos, neg, zero = signature(data)
    if is_lorentzian(data):
        return CP_PASS, f"Lorentzian (1, {neg}) mixed-volume form"
    return CP_KILL, f"signature ({pos}, {neg}, {zero}) is not Lorentzian: breaks Alexandrov-Fenchel"


@dataclass
class Checkpoint:
    cid: str
    domain: str
    proven: str        # the proven theorem this checkpoint anchors
    facet: str         # which M4 facet it tests
    verify: Callable[[object], tuple]
    witness: object    # a canonical object known to PASS (non-vacuity self-test)


CHECKPOINTS = [
    Checkpoint("CP-fq", "function field", "Weil/Hasse: |alpha| = sqrt(q)",
               "carries the Frobenius trace t", _verify_fq,
               witness=(13, elliptic_eigenvalues(13, 4))),
    Checkpoint("CP-hodge", "algebraic surface", "Hodge index: signature (1, rho-1) on NS",
               "indefinite (1, n-1) signature", _verify_hodge,
               witness=np.diag([1.0, -1.0, -1.0, -1.0])),
    Checkpoint("CP-ahk", "matroid Chow ring", "AHK: Whitney numbers log-concave",
               "Hodge-Riemann with no variety (K1-clean)", _verify_ahk,
               witness=(1, 6, 11, 6)),  # the rank-3 braid matroid / cycle matroid of K_4
    Checkpoint("CP-fh", "arithmetic surface", "Faltings-Hriljac: Neron-Tate height PD",
               "a real proven polarization", _verify_fh,
               witness=np.array([[2.0, 1.0], [1.0, 2.0]])),
    Checkpoint("CP-af", "convex bodies", "Alexandrov-Fenchel: Lorentzian (1, n-1)",
               "the convex signature (free, arithmetic-blind)", _verify_af,
               witness=np.diag([1.0, -1.0, -1.0])),
]

_BY_ID = {cp.cid: cp for cp in CHECKPOINTS}


# ---------------------------------------------------------------------------
# Candidates and scoring.
# ---------------------------------------------------------------------------

@dataclass
class BatteryCandidate:
    """A candidate's specialization to each proven domain. `spec` maps a
    checkpoint id to the structural object the candidate produces there (or omit
    a key = NA). `euler_gated` is the D-H firewall side condition (a genuine M4
    object exists only with an Euler product)."""
    node_id: str
    spec: dict = field(default_factory=dict)
    euler_gated: bool = False
    notes: str = ""


@dataclass
class BatteryScore:
    node_id: str
    per_cp: dict          # cid -> (verdict, detail)
    passed: int
    applicable: int
    killed: list
    firewall: str         # 'HOLDS' | 'FAILS'
    verdict: str          # FULL | PARTIAL | BROKEN
    purity: float         # passed / applicable (0 if none applicable)
    coverage: float       # passed / total checkpoints: THE gradient the loop climbs


def score(candidate: BatteryCandidate) -> BatteryScore:
    per_cp: dict = {}
    passed = applicable = 0
    killed = []
    for cp in CHECKPOINTS:
        v, detail = cp.verify(candidate.spec.get(cp.cid))
        per_cp[cp.cid] = (v, detail)
        if v == CP_NA:
            continue
        applicable += 1
        if v == CP_PASS:
            passed += 1
        elif v == CP_KILL:
            killed.append(cp.cid)
    firewall = "HOLDS" if candidate.euler_gated else "FAILS"
    purity = passed / applicable if applicable else 0.0
    coverage = passed / len(CHECKPOINTS)
    if killed:
        verdict = BROKEN
    elif applicable and passed == applicable and firewall == "HOLDS":
        verdict = FULL
    else:
        verdict = PARTIAL
    return BatteryScore(candidate.node_id, per_cp, passed, applicable, killed,
                        firewall, verdict, purity, coverage)


# ---------------------------------------------------------------------------
# Example candidates: the graded gradient made visible. A genuine M4-shape object
# reproduces every proven case and is euler-gated; the known failure modes
# (#40 arithmetic-blind, the off-line forgery, de Branges too-strong) each score
# strictly lower, along the project's three real axes (carries-t / indefinite /
# euler-gated).
# ---------------------------------------------------------------------------

EXAMPLE_CANDIDATES = {
    # Reproduces all five proven signatures, euler-gated -> FULL (necessary, not
    # sufficient: PASS-all is "consistent with every proven case," never a proof).
    "genuine-m4": BatteryCandidate(
        node_id="EX-genuine-m4",
        spec={
            "CP-fq": (13, elliptic_eigenvalues(13, 4)),
            "CP-hodge": np.diag([1.0, -1.0, -1.0, -1.0]),
            "CP-ahk": (1, 6, 11, 6),
            "CP-fh": np.array([[2.0, 1.0], [1.0, 2.0]]),
            "CP-af": np.diag([1.0, -1.0, -1.0]),
        },
        euler_gated=True,
        notes="reproduces every proven case; the honest M4 shape"),

    # The #40 failure: gets the convex / combinatorial signatures free (hodge, ahk,
    # af) but is t-BLIND (its F_q modulus ignores the trace -> off-circle) and has
    # no Euler product -> the firewall FAILS. The trap AHK fell into.
    "arithmetic-blind": BatteryCandidate(
        node_id="EX-arithmetic-blind",
        spec={
            "CP-fq": (13, (3.0, 3.0)),  # t-blind: a fixed modulus, not sqrt(13)=3.606
            "CP-hodge": np.diag([1.0, -1.0, -1.0, -1.0]),
            "CP-ahk": (1, 6, 11, 6),
            "CP-af": np.diag([1.0, -1.0, -1.0]),
        },
        euler_gated=False,
        notes="convex/combinatorial signatures free, but t-blind and non-Euler (#40)"),

    # The function-field analogue of D-H: an off-line forgery breaks CP-fq.
    "off-line-forgery": BatteryCandidate(
        node_id="EX-off-line-forgery",
        spec={"CP-fq": (7, (elliptic_eigenvalues(7, 2)[0] * 1.3, elliptic_eigenvalues(7, 2)[1]))},
        euler_gated=True,
        notes="off-circle eigenvalue: breaks Weil where RH is a theorem"),

    # de Branges / too-strong: forces a positive-DEFINITE form where the Hodge
    # index must be indefinite -> overshoots, KILLED at CP-hodge for wrong signature.
    "too-strong": BatteryCandidate(
        node_id="EX-too-strong",
        spec={
            "CP-fq": (13, elliptic_eigenvalues(13, 4)),
            "CP-hodge": np.diag([1.0, 1.0, 1.0, 1.0]),  # definite, not (1,3)
            "CP-fh": np.array([[2.0, 1.0], [1.0, 2.0]]),
        },
        euler_gated=True,
        notes="positivity strictly stronger than RH (de Branges); wrong (definite) signature"),

    # The honest convex/combinatorial candidate: it does NOT fake a function-field
    # modulus (NA on CP-fq, CP-fh), passes the convex/combinatorial cases cleanly,
    # but has no Euler product -> firewall FAILS. The clean PARTIAL: it breaks
    # nothing, yet reproduces only 3 of 5 proven cases. The gradient's middle.
    "convex-only": BatteryCandidate(
        node_id="EX-convex-only",
        spec={
            "CP-hodge": np.diag([1.0, -1.0, -1.0, -1.0]),
            "CP-ahk": (1, 6, 11, 6),
            "CP-af": np.diag([1.0, -1.0, -1.0]),
        },
        euler_gated=False,
        notes="reproduces the convex/combinatorial signatures only; no Euler product"),
}


def demo() -> int:
    print("Proven-case shadow battery (6f): a graded positive value function\n")
    print("  Checkpoints (each a proven case a genuine M4 construction must reproduce):")
    for cp in CHECKPOINTS:
        print(f"    {cp.cid:9} [{cp.facet}]  {cp.proven}")
    print()
    for key in ("genuine-m4", "convex-only", "arithmetic-blind", "too-strong", "off-line-forgery"):
        s = score(EXAMPLE_CANDIDATES[key])
        print(f"  {key:18} {s.verdict:8} coverage={s.coverage:.2f} ({s.passed}/{len(CHECKPOINTS)})  "
              f"firewall={s.firewall}" + (f"  killed={s.killed}" if s.killed else ""))
        for cid, (v, detail) in s.per_cp.items():
            if v != CP_NA:
                print(f"      {cid:9} {v:4}  {detail}")
    print("\n  The gradient: genuine-m4 (FULL) > arithmetic-blind (t-blind, firewall fails) "
          "> too-strong /\n  off-line-forgery (BROKEN). 'No gradient at M4' becomes 'k of N "
          "proven cases + the firewall'.\n  FULL is necessary, never sufficient: only Lean validates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(demo())
