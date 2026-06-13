# Increment 1: the executable falsifier oracle (build-ready spec)

> Build-ready specification for `experiments/lemma_db/oracle.py`, the first component of the Reduction Engine ([`docs/03_research/reduction_engine.md`](../../docs/03_research/reduction_engine.md), section 2). This is the increment that survived the increment-2 pressure-test clean, because the oracle only ever runs in the **negative** direction (kill / park), checked against an external counterexample (Davenport-Heilbronn) and an external floor (Lean). Falsification launders nothing.
>
> The oracle turns the project's disciplines from **audited flags** (a human sets `dh_buildable`, `dh_audit` checks it) into **computed verdicts** (the oracle evaluates the object on D-H and sets `dh_buildable` from what comes out). It catches not just a human who mislabels a node, but a candidate the human never thought to label.

Status: 2026-06-13. Spec only; no code yet. Effort estimate: ~150-250 lines, reuses `experiments/_shared/` entirely.

---

## 0. The one boundary that defines the whole module

> **The oracle KILLS or PARKS. It never VALIDATES.** A candidate that survives every disqualifier returns `PASS`, and `PASS` means exactly "not yet killed," never "correct." The sole source of positive truth is the Lean floor. Every signature, docstring, and return value in this module must preserve that asymmetry.

This is the soundness invariant from the engine spec, expressed in code. It is also why increment 1 is safe to build before increment 2: nothing here asserts a reduction, so nothing here can launder a prior.

---

## 1. The candidate schema (the interface contract)

The oracle cannot run on free text. A candidate must arrive in a structured form. Defining this schema is part of increment 1, because it is the contract the BUILDER (and later the loop driver, increment 4) must emit against.

```python
@dataclass
class Candidate:
    node_id: str                     # matches a node id in seed_lemmas.json, or a new one
    claim_type: str                  # 'positivity' | 'spectral' | 'statistical' | 'trace' | 'other'
    claims_rh_equivalent: bool       # does the author assert this implies RH?
    inputs: frozenset[str]           # declared inputs, e.g. {'euler_product', 'gamma_factor'}
                                     #   or {'zero_locations'} -- the K1 tripwire
    construction: Callable[[LFunction], object] | None
                                     # parameterized by an L-function; None if abstract
    detector: Callable[[LFunction], float] | None
                                     # the quantity the author claims is >= 0 iff RH; None if none
    notes: str = ""
```

`construction` and `detector` are what make a candidate *evaluable*. An abstract candidate (a described-but-not-yet-instantiable construction) supplies `None` for both, and the oracle runs only the static disqualifiers (D0, D3), returning `UNTESTABLE` for the dynamic ones (D1, D2). That is honest: the oracle reports what it could not test rather than passing it silently.

---

## 2. The disqualifiers, cheapest first

Each returns a `Verdict(result, reason, evidence)` with `result in {KILL, PARK, PASS, UNTESTABLE}`. The oracle runs them in order and short-circuits on the first `KILL`.

### D0. Level classifier (cheapest)

Kills a Level-3-only edge into `TGT-rh`. Statistical / spectral-without-positivity claims are compatible with a world where some zero has $\beta = 0.51$, so they cannot reduce RH.

```python
def level_classifier(c: Candidate) -> Verdict:
    if c.claim_type in ('statistical', 'spectral') and not c.claims_rh_equivalent:
        return Verdict(KILL, "Level-3: statistics/spectrum without a positivity claim",
                       evidence=c.claim_type)
    if c.claim_type == 'trace' and not c.claims_rh_equivalent:
        return Verdict(PARK, "realization-only (trace/explicit-formula); D-H has this too")
    return Verdict(PASS, "claims Level-4 positivity or RH-equivalence")
```

Partly a required structured input (the author declares `claim_type` and `claims_rh_equivalent`); the classifier enforces the consequence. This is the cheapest kill and removes the largest class of wrong candidates.

### D1. Compute `dh_buildable` (replaces the hand-set flag)

Instantiate the *same* construction on Davenport-Heilbronn and on zeta. If a finite, well-defined object comes out for D-H, the construction is realization-half and `dh_buildable='true'`.

```python
from experiments._shared.davenport_heilbronn import DavenportHeilbronn
from experiments._shared.zeta import RiemannZeta

def dh_buildable_compute(c: Candidate) -> Verdict:
    if c.construction is None:
        return Verdict(UNTESTABLE, "abstract candidate; no construction callable")
    try:
        val_dh = c.construction(DavenportHeilbronn())
    except (NoEulerProduct, NotImplementedError) as e:
        return Verdict(PASS, f"construction is uninstantiable on D-H: {e}",
                       evidence="dh_buildable=false (structural)")
    if _is_finite(val_dh):
        return Verdict(PARK, "construction returns a finite value on D-H (realization-half)",
                       evidence=f"dh_buildable=true; D-H value={val_dh!r}")
    return Verdict(PASS, "construction does not produce a finite D-H object")
```

The result feeds the node's `dh_buildable` column. The `dh_audit` view then runs against a **computed** flag rather than a trusted one. A `dh_buildable='true'` content node (layer in realization/signature/bridge) on a load-bearing path to `TGT-rh` fails the build, exactly as today, but now the flag cannot be wishful.

`NoEulerProduct` is the structural firewall: a construction that requires a Frobenius element raises it on D-H (which has `has_euler_product=False`). That raise is a `PASS`, the desired outcome: the object genuinely does not exist for the counterexample.

### D2. The flip test (the project's reusable filter)

Run the candidate's own detector (the quantity it claims is $\geq 0$ iff RH) on D-H, whose off-line zeros are known. If the detector does *not* go negative, it is blind to exactly the failure RH forbids, so it cannot be detecting RH.

```python
DH_OFFLINE_ZERO = complex(0.8085, 85.699)   # the landmark pair partner: 0.1915 + 85.699i

def flip_test(c: Candidate) -> Verdict:
    if c.detector is None:
        return Verdict(UNTESTABLE, "no detector to flip")
    sign_zeta = c.detector(RiemannZeta())
    sign_dh   = c.detector(DavenportHeilbronn())
    if sign_dh >= 0 and sign_zeta >= 0:
        return Verdict(KILL, "detector non-negative on D-H too: cannot separate zeta from "
                       "a known off-line-zero L-function", evidence=f"zeta={sign_zeta}, dh={sign_dh}")
    return Verdict(PASS, "detector distinguishes D-H (goes negative)",
                   evidence=f"zeta={sign_zeta}, dh={sign_dh}")
```

**Empirical result (implemented, 2026-06-13), and it is sharper than this spec first guessed.** The first draft assumed the Li functional would be the reference *separating* detector. It is the opposite. Computed over zeros to $T = 100$: $\min_n \lambda_n = +0.017$ for zeta and $+0.080$ for D-H, both non-negative through $n = 12$. The canonical soft positivity functional is **blind** to D-H's off-line zeros in any reachable range, so the flip test KILLS it. The only detector that separates D-H is one that reads the zero locations directly (`offline_zero_detector`), and that one is K1-circular, so `k1_noncircular` (D3) KILLS it first. So the oracle reproduces the marginal-positivity wall as a two-move trap: every detector dies, by blindness (Li) or by circularity (zero-reading). A general candidate supplies its own `detector(L) -> float`; the two reference detectors live in `oracle.py` and encode the wall.

### D3. K1 non-circularity (static)

Positivity must come from a polarization, never be read off the zeros. Inspect the candidate's declared inputs.

```python
ZERO_INPUTS = {'zero_locations', 'zeros', 'rho', 'critical_zeros'}

def k1_noncircular(c: Candidate) -> Verdict:
    if c.claim_type == 'positivity' and (c.inputs & ZERO_INPUTS):
        return Verdict(KILL, "circular: positivity claim consumes zero locations as input",
                       evidence=sorted(c.inputs & ZERO_INPUTS))
    return Verdict(PASS, "positivity does not depend on zero locations")
```

### D4+ (hooks only, out of scope for increment 1)

K2-K4 are heavier structural attacks. Leave named no-op hooks so the loop driver can register them later.

---

## 3. Aggregation and output

```python
@dataclass
class OracleVerdict:
    node_id: str
    overall: str                 # KILL | PARK | PASS
    killed_by: str | None        # the disqualifier id that fired, if any
    verdicts: dict[str, Verdict] # per-disqualifier detail
    dh_buildable: str            # 'true' | 'false' | 'N/A', COMPUTED
```

`overall = KILL` if any disqualifier killed; else `PARK` if any parked; else `PASS`. `PASS` means "not yet killed" (section 0). Persist `OracleVerdict` to a sidecar table `oracle_verdict` and to a monotone log line so kills are permanent coordinates (the monotone-memory invariant).

---

## 4. Integration with `build_db.py`

1. On ingest, if a node has a `construction`/`detector` available, run the oracle and **set `dh_buildable` from D1** rather than reading the seed's hand-set value (the seed value becomes a fallback for abstract nodes).
2. Re-run `dh_audit` against the computed flags. Exit non-zero on any violation, exactly as today; the gate is unchanged, the flag is now earned.
3. Emit the **anti-theater metric**: count candidates killed this build, broken down by disqualifier. This is the engine's kill-count, the number that justifies the oracle's existence per the anti-theater guard.

---

## 5. Acceptance tests (the oracle's own smoke test)

Implemented as `experiments/lemma_db/test_oracle.py` (6/6 passing), mirroring the smoke-test style.

| id | candidate | expected | what it proves |
|----|-----------|----------|----------------|
| 1 | level classifier on statistical / positivity / trace | KILL / PASS / PARK | Level-3 removal works |
| 2 | K1 on `inputs={'zero_locations'}` vs `{'polarization'}` | KILL / PASS | the circularity tripwire works |
| 3 | `dh_buildable_compute` on realization / signature / abstract construction | `true`(PARK) / `false`(PASS) / `N/A`(UNTESTABLE) | the flag is computed, not trusted |
| 4 | `offline_zero_detector` (separating) | `flip_test` PASS | the oracle does not kill a real separator |
| 5 | `li_min_detector` (blind) | `li_min(zeta) >= 0`, `li_min(D-H) >= 0`, `flip_test` KILL | **the load-bearing test**: the soft detector is blind to D-H |
| 6 | full pipeline on the 4 example candidates | soft-li KILL@flip, zero-reader KILL@k1, abstract PASS, realization PARK | the two-move wall, end to end |

Test 5 is load-bearing. The oracle is only trustworthy if it kills the known counterexample's natural detector, and if it ever stops being a KILL then either the oracle broke or someone found a soft detector that separates D-H (which would be major). It is wired into `python -m experiments._shared.smoke_test` as Test 9 (the Li blindness + off-line-zero detectability regression), so a change that blinds the flip test or loses the off-line zero fails CI. Verified: smoke test 9/9.

---

## 6. Why this is safe to build first

The oracle never asserts a reduction. It only removes candidates that fail a necessary condition, and every necessary condition is checked against something external: D-H for D1/D2, the declared-input set for D3, the claim type for D0. Three of the four PROP conjuncts the engine cares about are checkable only as necessary tests, and `PROP-rh-equivalent` is checkable only in the falsifying direction, which is precisely D1 and D2. So the oracle is the honest, soundness-respecting half of the engine. Increment 2 (the residual/collision engine) is the half that needed rescoping; this half did not.

---

## 7. Status: built (2026-06-13)

Landed as `experiments/lemma_db/oracle.py` (+ `test_oracle.py`), with the regression in `experiments/_shared/smoke_test.py` (Test 9). What is real:

- The `Candidate` / `Verdict` / `OracleVerdict` dataclasses and the `PASS`-is-not-`VALID` boundary in the module docstring.
- The four disqualifiers, run cheapest-first: `level_classifier` (static) -> `k1_noncircular` (static) -> `dh_buildable_compute` (one D-H evaluation) -> `flip_test` (zeros / Li sums). `run_oracle` short-circuits on the first KILL.
- The two reference detectors (`li_min_detector` blind, `offline_zero_detector` separating-but-circular) and the two reference constructions (`realization_construction` finite on D-H, `signature_construction` raising `NoEulerProduct`).
- `python -m experiments.lemma_db.oracle` runs `demo()`: the two-move wall printed.
- Acceptance: `test_oracle.py` 6/6; `smoke_test.py` 9/9.

Not yet built (deferred, honestly): the `build_db.py` gate that recomputes a seed node's `dh_buildable` from a registered construction. No seed node carries a construction callable yet, so this is the increment-1-to-4 handoff (the loop driver attaches constructions on ingest). The computation exists (`dh_buildable_compute`); only the registry that feeds it real seed nodes is pending. Until then `build_db.py`'s `dh_audit` runs against the hand-set flags, unchanged.
