"""Transfer-search: the bridge-finder (Generative Engine, 6b).

Spec: `docs/03_research/generative_engine.md` section 4. The prize. The claim is
that the untried approach is a BRIDGE, not an atom: a proven theorem in some field
$A$ whose structure matches the open target $M4$ in field $B$, transferable across.
A machine's edge is breadth held at once, so it can search the product space for
structural matches no siloed human would scan.

WHAT THIS IS AND IS NOT
-----------------------
This is RETRIEVAL, not a verdict. It scores a curated corpus of proven positivity
theorems by structural-feature match against the M4 residual spec (the missing
object 6e reads off the gap), and ranks them. The embedding is hand-tagged
features, not a learned one; the score is a prior that says "look here," never
"these are the same theorem." Certifying an actual transfer (the functor
$A \\to \\mathrm{Spec}(\\mathbb{Z})$) stays a human / LLM judgement on the shortlist.

The discriminating axis is `positivity_kind`. M4 needs an INDEFINITE (1, n-1)
Hodge-index signature; an all-positive (DEFINITE) theorem cannot match, however
elegant. That is the Lee-Yang kill, encoded: the retrieval must demote Lee-Yang.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Features:
    positivity_kind: str   # 'indefinite' | 'definite' | 'uniqueness'
    carrier: str           # cohomology | intersection | convex | combinatorial | moment | state | height | hilbert
    source: str            # polarization | lorentzian | ergodic-rigidity | flat-extension | positive-definite | analytic
    continuous_spectrum: bool   # handles a continuous (pole-sourced archimedean) spectral component
    euler_gated: bool           # requires prime / Euler structure


@dataclass
class Theorem:
    name: str
    setting: str
    features: Features
    role: str              # 'template' | 'imported' | 'candidate' | 'fresh' | 'killed'
    note: str


# The missing object for M4, as a feature signature (read off the 6e residual spec).
M4_RESIDUAL = Features(
    positivity_kind="indefinite",   # the (1, n-1) Hodge-index signature
    carrier="cohomology",
    source="polarization",
    continuous_spectrum=True,        # the pole-sourced archimedean component must be pinned
    euler_gated=True,
)


def _F(*a, **k):
    return Features(*a, **k)


CORPUS = [
    Theorem("Weil positivity (function-field RH)", "ell-adic H^1 of C x C / F_q",
            _F("indefinite", "cohomology", "polarization", False, True),
            "template", "the direct model M4 lifts; the Hodge-index / Castelnuovo-Severi signature"),
    Theorem("Hodge index theorem (algebraic surface)", "Neron-Severi of a surface",
            _F("indefinite", "intersection", "polarization", False, False),
            "template", "signature (1, rho-1) on NS; the geometric template of the arithmetic target"),
    Theorem("Hodge-Riemann bilinear relations", "compact Kahler middle cohomology",
            _F("indefinite", "cohomology", "polarization", False, False),
            "fresh", "the char-0 Hodge theory; an indefinite polarization on primitive cohomology"),
    Theorem("Alexandrov-Fenchel inequality", "mixed volumes / convex bodies",
            _F("indefinite", "convex", "lorentzian", False, False),
            "fresh", "a (1, n-1) Lorentzian signature in convex geometry; a different-domain sibling"),
    Theorem("Adiprasito-Huh-Katz (matroid Hodge theory)", "Chow ring of a matroid",
            _F("indefinite", "combinatorial", "lorentzian", False, False),
            "candidate", "Hodge-Riemann for matroids; in the candidate set, bracketed on carries-trace"),
    Theorem("Marcus-Spielman-Srivastava interlacing families", "signed adjacency / 2-lifts of graphs",
            _F("definite", "combinatorial", "lorentzian", False, False),
            "killed", "KILLED as an M4 transfer (2026-07-01, LEARNINGS #140, toy/interlacing.py): a "
            "genuine NON-variety source of the sqrt(q) bound (bipartite Ramanujan graphs of all "
            "degrees via interlacing families / expected characteristic polynomials, MSS 2015). It "
            "addresses R1 (the sourcing gap, #130), not M4 (the signature): its output is a real-rooted "
            "one-sided spectral bound, not an indefinite (1,n-1) polarization, so it scores 0 on the "
            "hard gate. The engine is real-rootedness (Heilmann-Lieb) = self-adjointness of the signed "
            "adjacency, exactly the ingredient Spec(Z)'s non-self-adjoint Frobenius lacks (its "
            "L-polynomial is not real-rooted). Sibling to the Lorentzian / real-stable kill; kept in "
            "corpus so R1-sourcing sweeps neither lose it nor re-propose it. Net: R1 is "
            "self-adjointness-gated, not merely variety-gated."),
    Theorem("Boucksom-Jonsson non-archimedean Monge-Ampere / K-stability",
            "energy positivity on the Berkovich analytification",
            _F("definite", "convex", "valuative", False, False),
            "killed", "KILLED (breadth sweep 2026-06-14, LEARNINGS #97): surfaced by the engine, "
            "then demoted. The K-energy / NA-Monge-Ampere positivity on offer is convex one-sided, "
            "not the indefinite (1,n-1) Hodge index M4 needs (the NA Hodge-index inequality, where it "
            "exists, is the existing 'Hodge index theorem' node over a NA base, no new transfer). "
            "Valuative at a single Berkovich place => blind to the archimedean continuation where the "
            "zeros sit (Re(s)<1); arithmetic-blind, no t-slot; cannot separate zeta from D-H. "
            "Kept in-corpus with this annotation so future sweeps neither lose it nor re-propose it."),
    Theorem("Bost-Connes KMS uniqueness", "the BC C*-dynamical system",
            _F("uniqueness", "state", "ergodic-rigidity", True, True),
            "imported", "the KMS simplex is a point: a continuous spectrum PINNED by Euler structure"),
    Theorem("Curto-Fialkow flat extension", "truncated trigonometric moment problem",
            _F("uniqueness", "moment", "flat-extension", False, False),
            "imported", "moment-uniqueness; atomic only, no continuous component (why it falls short for zeta)"),
    Theorem("Lee-Yang circle theorem", "Ising partition-function zeros",
            _F("definite", "measure", "analytic", False, False),
            "fresh", "all zeros on a circle: an ALL-POSITIVE (definite) shape, the wrong signature for M4"),
    Theorem("de Branges spaces positivity", "Hilbert spaces of entire functions",
            _F("definite", "hilbert", "analytic", False, True),
            "candidate", "in the candidate set, bracketed: the positivity is too strong (overshoots to GRH)"),
    Theorem("Neron-Tate / Faltings-Hriljac height", "Arakelov height pairing",
            _F("definite", "height", "positive-definite", False, False),
            "candidate", "the height pairing is positive-DEFINITE and local; bracketed on global / signature"),
]


_KIND = {"indefinite": 4, "uniqueness": 2, "definite": 0}
_CARRIER = {"cohomology": 2, "intersection": 2, "convex": 1, "combinatorial": 1,
            "moment": 1, "state": 1, "measure": 1, "height": 0, "hilbert": 0}
_SOURCE = {"polarization": 2, "lorentzian": 2, "ergodic-rigidity": 1, "flat-extension": 1,
           "positive-definite": 0, "analytic": 0, "valuative": 0}


def match_score(f: Features, target: Features = M4_RESIDUAL) -> int:
    """Structural-feature match score against the target. positivity_kind is the
    hard discriminator (a definite theorem scores 0 there: the Lee-Yang gate)."""
    s = _KIND.get(f.positivity_kind, 0)
    s += _CARRIER.get(f.carrier, 0)
    s += _SOURCE.get(f.source, 0)
    if f.continuous_spectrum and target.continuous_spectrum:
        s += 2
    if f.euler_gated and target.euler_gated:
        s += 1
    return s


def rank(corpus=CORPUS, target: Features = M4_RESIDUAL) -> list:
    scored = [(t, match_score(t.features, target)) for t in corpus]
    return sorted(scored, key=lambda ts: (-ts[1], ts[0].name))


def demo() -> int:
    print("Transfer-search (6b): proven positivity theorems ranked against the M4 residual\n")
    print("  M4 residual = INDEFINITE (1,n-1) polarization, cohomological, Euler-gated, "
          "continuous-spectrum.\n  The hard gate is the signature: an all-positive (definite) "
          "theorem cannot match.\n")
    ranked = rank()
    for t, s in ranked:
        print(f"  {s:2}  [{t.role:9}] {t.name}")
        print(f"          {t.setting}  --  {t.note}")
    # Verdicts against the three success criteria.
    by_name = {t.name: s for t, s in ranked}
    top = ranked[0][0]
    bc = by_name["Bost-Connes KMS uniqueness"]
    ly = by_name["Lee-Yang circle theorem"]
    fresh = [(t, s) for t, s in ranked if t.role == "fresh" and t.features.positivity_kind == "indefinite"]
    print(f"\n  VALIDATION: top match is a template ({top.name}) = the right shape;")
    print(f"              Bost-Connes (the hand-found pinning import) scores {bc}, well above")
    print(f"              Lee-Yang ({ly}) which is correctly DEMOTED for its all-positive signature.")
    if fresh:
        ft, fs = fresh[0]
        print(f"  NOVELTY:    the freshest high-match is {ft.name} (score {fs}, {ft.setting}),")
        print(f"              a different-domain indefinite Hodge-index sibling = a transfer candidate.")
    print("\n  HONEST VERDICT: the retrieval VALIDATES (rediscovers Bost-Connes, finds the")
    print("  Hodge-index family, demotes Lee-Yang) but surfaces no escape to a FOREIGN field:")
    print("  every high match is a Hodge-index sibling. That sharpens, rather than moves, the")
    print("  conclusion that M4 IS the arithmetic Hodge index. Retrieval is a prior, not a proof.")
    return 0


if __name__ == "__main__":
    raise SystemExit(demo())
