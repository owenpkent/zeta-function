"""Shared experiment harness: the repo's scientific disciplines in one module.

Three things every arithmetic_geometric probe (e2aq, e2ar, e2at, and
neighbors) re-implements by hand:

  1. A named pass/fail check accumulator that prints "[PASS]"/"[FAIL]" rows
     as it goes and ends with the repo's "N/N passed" line, so
     experiments/run_all_tests.py's regex finds it. See Gates.
  2. A pre-registration ledger: a prediction and its kill condition are
     written down BEFORE the run and resolved (FIRED / SURVIVED / REFUTED)
     after, instead of being narrated after the fact once the answer is
     known. See PreRegistry.
  3. A uniform loader for the three controls (zeta, Davenport-Heilbronn,
     Beurling) so a probe runs the identical pipeline on the real object and
     on both wrong-approach detectors without re-importing three modules by
     hand each time. See controls() / run_on_controls().

This module encodes the D-H / Beurling control discipline (CLAUDE.md, "The
Davenport-Heilbronn discipline" and "the Beurling discipline") and the
pre-registration pattern used across the xi-ladder probes. It must not be
weakened: no control silently dropped from controls(), no quick mode that
turns a real gate into an automatic pass. Changing its printed contract (the
final "N/N passed" line run_all_tests.py greps for) requires updating
CLAUDE.md.

Usage sketch:
    from experiments._shared.harness import Gates, PreRegistry, quick_arg, save_npz

    quick = quick_arg()
    gates = Gates(quick=quick)
    pre = PreRegistry()
    pre.register("P1", "residual < 0.1 by a = 2", "residual stays > 1 at a = 2")
    resid = 0.03  # ... the actual computation ...
    gates.gate("residual small", resid < 0.1, f"resid={resid:.3f}")
    pre.resolve("P1", "FIRED" if resid < 0.1 else "REFUTED", f"resid={resid:.3f}")
    gates.gate("no unresolved predictions", pre.unresolved() == [])
    gates.summary()
    raise SystemExit(gates.exit_code())
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import OrderedDict
from pathlib import Path

import numpy as np

from experiments._shared.zeta import zeta as zeta_L
from experiments._shared.davenport_heilbronn import DavenportHeilbronn
from experiments._shared.beurling import BeurlingSystem

_OUTCOMES = ("FIRED", "SURVIVED", "REFUTED")
_PROV_KEY = "_harness_provenance"


class Gates:
    """Named boolean check accumulator with the repo's printed contract."""

    def __init__(self, quick: bool = False):
        self.quick = quick
        self._rows: list[tuple[str, str, str]] = []   # (name, status, detail)

    def gate(self, name: str, condition: bool, detail: str = "", verbose: bool = True) -> bool:
        ok = bool(condition)
        status = "PASS" if ok else "FAIL"
        self._rows.append((name, status, detail))
        if verbose:
            print(f"  [{status}] {name}" + (f"  ({detail})" if detail else ""))
        return ok

    def skip(self, name: str, detail: str = "skipped (quick mode)", verbose: bool = True) -> None:
        """Record a gate deliberately not evaluated (self.quick heavy-path).

        Skipped gates are excluded from n_total()/n_pass(): quick mode must
        never inflate the pass count for a check that was not actually run.
        """
        self._rows.append((name, "SKIP", detail))
        if verbose:
            print(f"  [SKIP] {name}" + (f"  ({detail})" if detail else ""))

    def n_pass(self) -> int:
        return sum(1 for _, status, _ in self._rows if status == "PASS")

    def n_total(self) -> int:
        return sum(1 for _, status, _ in self._rows if status in ("PASS", "FAIL"))

    def summary(self, elapsed: float | None = None) -> None:
        print("\n-- gate summary --")
        for name, status, detail in self._rows:
            print(f"  [{status}] {name}" + (f"  ({detail})" if detail else ""))
        npass, ntotal = self.n_pass(), self.n_total()
        suffix = f"  ({elapsed:.0f} s)" if elapsed is not None else ""
        print(f"\n{npass}/{ntotal} passed{suffix}")

    def exit_code(self) -> int:
        """0 iff every counted gate passed and at least one gate ran."""
        ntotal = self.n_total()
        return 0 if ntotal > 0 and self.n_pass() == ntotal else 1


class PreRegistry:
    """Pre-registered predictions, resolved after the run.

    register() runs BEFORE any computation touching the prediction; resolve()
    runs after, with outcome one of:
      FIRED     the kill condition did not happen; the prediction holds.
      SURVIVED  inconclusive at this resolution; not refuted, not confirmed.
      REFUTED   the kill condition happened.
    unresolved() lets a gate assert nothing was left dangling at the end of
    a run (the anti-narration discipline: no post-hoc "prediction").
    """

    def __init__(self):
        self._entries: "OrderedDict[str, dict]" = OrderedDict()

    def register(self, id: str, statement: str, kill_condition: str) -> None:
        if id in self._entries:
            raise ValueError(f"prediction id already registered: {id}")
        self._entries[id] = {
            "statement": statement,
            "kill_condition": kill_condition,
            "outcome": None,
            "note": "",
        }

    def resolve(self, id: str, outcome: str, note: str = "") -> None:
        if id not in self._entries:
            raise KeyError(f"unregistered prediction id: {id}")
        if outcome not in _OUTCOMES:
            raise ValueError(f"outcome must be one of {_OUTCOMES}, got {outcome!r}")
        self._entries[id]["outcome"] = outcome
        self._entries[id]["note"] = note

    def unresolved(self) -> list[str]:
        return [id for id, e in self._entries.items() if e["outcome"] is None]

    def table(self) -> None:
        print("\n-- pre-registration table --")
        for id, e in self._entries.items():
            outcome = e["outcome"] or "UNRESOLVED"
            print(f"  [{outcome:>9}] {id}: {e['statement']}")
            print(f"            kill: {e['kill_condition']}")
            if e["note"]:
                print(f"            note: {e['note']}")


def controls(names) -> "OrderedDict[str, object]":
    """Uniform loader for the three controls, by name.

    zeta:     experiments._shared.zeta.zeta, the shared LFunction singleton
              (evaluate, zeros).
    dh:       a fresh DavenportHeilbronn() (LFunction: evaluate, zeros). The
              functional equation without the Euler product; the form-side
              wrong-approach detector.
    beurling: a fresh BeurlingSystem() (theta, gen_integers, count_integers).
              The Euler product without the additive lattice; the
              counting-side wrong-approach detector. It is deliberately NOT
              an LFunction: no evaluate() or zeros(), because it has no
              analytic continuation to test on the critical line. A probe
              that needs "zeros" from beurling is asking the wrong question
              of this control; that mismatch is itself the discipline.
    """
    out: "OrderedDict[str, object]" = OrderedDict()
    for n in names:
        if n == "zeta":
            out[n] = zeta_L
        elif n == "dh":
            out[n] = DavenportHeilbronn()
        elif n == "beurling":
            out[n] = BeurlingSystem()
        else:
            raise ValueError(f"unknown control {n!r}; expected one of zeta, dh, beurling")
    return out


def run_on_controls(fn, names) -> "OrderedDict[str, object]":
    """Run fn(name, control_object) on each requested control.

    Returns an ordered dict name -> fn's return value, in request order, so
    a probe gets identical treatment of zeta/dh/beurling from one call site.
    """
    results: "OrderedDict[str, object]" = OrderedDict()
    for name, obj in controls(names).items():
        results[name] = fn(name, obj)
    return results


def save_npz(path, arrays_dict: dict, provenance_dict: dict) -> None:
    """np.savez_compressed with a provenance record embedded as JSON.

    provenance_dict should carry whatever a future reader needs to
    reproduce the run: parameters, dps, seed, wall time. No timestamps of
    authorship and no attribution; this is a reproducibility record, not a
    byline.
    """
    if _PROV_KEY in arrays_dict:
        raise ValueError(f"{_PROV_KEY!r} is reserved by harness.save_npz")
    payload = dict(arrays_dict)
    payload[_PROV_KEY] = np.array([json.dumps(provenance_dict)])
    np.savez_compressed(path, **payload)


def load_provenance(path) -> dict:
    with np.load(path, allow_pickle=False) as data:
        if _PROV_KEY not in data:
            raise KeyError(f"no provenance record in {path} (not saved via harness.save_npz)")
        return json.loads(str(data[_PROV_KEY][0]))


def quick_arg(argv: list[str] | None = None) -> bool:
    """Shared --quick flag convention. Returns True iff --quick was passed."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--quick", action="store_true")
    ns, _ = parser.parse_known_args(argv if argv is not None else sys.argv[1:])
    return ns.quick
