"""Standalone tests for experiments/_shared/harness.py.

Not pytest (repo convention): main() under __main__, prints "N/N passed"
last. Auto-discovered by experiments/run_all_tests.py, so this must stay
fast: controls() only checks that objects construct and expose the right
attributes, it never calls zeros() or evaluate() with anything that would
trigger a real zero computation.

Run: python -m experiments._shared.test_harness
"""

from __future__ import annotations

import json

import numpy as np

from experiments._shared.harness import (
    Gates,
    PreRegistry,
    controls,
    load_provenance,
    quick_arg,
    run_on_controls,
    save_npz,
)

CHECKS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


def test_gates_accounting():
    print("Test 1: Gates pass/fail/skip accounting")
    g = Gates(quick=True)
    g.gate("a", True, "ok", verbose=False)
    g.gate("b", False, "bad", verbose=False)
    g.gate("c", True, verbose=False)
    g.skip("d", "heavy, quick mode", verbose=False)
    check("n_pass counts only PASS", g.n_pass() == 2, f"got {g.n_pass()}")
    check("n_total excludes SKIP", g.n_total() == 3, f"got {g.n_total()}")
    check("exit_code nonzero when a gate failed", g.exit_code() == 1, f"got {g.exit_code()}")
    check("quick flag stored", g.quick is True)

    g2 = Gates()
    g2.gate("x", True, verbose=False)
    g2.gate("y", True, verbose=False)
    check("exit_code zero when all gates pass", g2.exit_code() == 0, f"got {g2.exit_code()}")

    g3 = Gates()
    check("exit_code nonzero with zero gates run (no false green)", g3.exit_code() == 1)


def test_summary_line_format(capsys=None):
    print("Test 2: summary() output line format")
    import io
    import contextlib

    g = Gates()
    g.gate("a", True, verbose=False)
    g.gate("b", True, verbose=False)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        g.summary()
    lines = [l for l in buf.getvalue().splitlines() if l.strip()]
    last = lines[-1]
    check("last summary line is exactly 'N/N passed'", last == "2/2 passed", repr(last))

    buf2 = io.StringIO()
    with contextlib.redirect_stdout(buf2):
        g.summary(elapsed=12.3)
    last2 = [l for l in buf2.getvalue().splitlines() if l.strip()][-1]
    check("elapsed suffix keeps the 'N/N passed' substring and a digit/digit count",
          last2.startswith("2/2 passed") and "12 s" in last2, repr(last2))

    # this is the contract run_all_tests.py's COUNT_RE + "passed" scan relies on
    import re
    count_re = re.compile(r"(\d+)\s*/\s*(\d+)")
    m = count_re.search(last)
    check("regex used by run_all_tests.py matches the final line",
          m is not None and m.group(1) == m.group(2) == "2", repr(last))


def test_preregistry():
    print("Test 3: PreRegistry register/resolve/unresolved")
    pre = PreRegistry()
    pre.register("P1", "residual < 0.1 by a = 2", "residual stays > 1")
    pre.register("P2", "gap monotone in Omega", "gap non-monotone at any rung")
    check("both registered, both unresolved", pre.unresolved() == ["P1", "P2"],
          f"got {pre.unresolved()}")

    pre.resolve("P1", "FIRED", "resid=0.03")
    check("resolving one leaves exactly the other unresolved",
          pre.unresolved() == ["P2"], f"got {pre.unresolved()}")

    pre.resolve("P2", "REFUTED", "gap dropped at Omega=24")
    check("all resolved after both resolve() calls", pre.unresolved() == [],
          f"got {pre.unresolved()}")

    threw = False
    try:
        pre.resolve("P3", "FIRED")
    except KeyError:
        threw = True
    check("resolve() on unregistered id raises KeyError", threw)

    threw = False
    try:
        pre.resolve("P1", "MAYBE")
    except ValueError:
        threw = True
    check("resolve() rejects an outcome outside FIRED/SURVIVED/REFUTED", threw)

    threw = False
    try:
        pre.register("P1", "dup", "dup")
    except ValueError:
        threw = True
    check("re-registering the same id raises ValueError", threw)


def test_controls_construct():
    print("Test 4: controls() constructs the three objects with the right shape")
    objs = controls(["zeta", "dh", "beurling"])
    check("returns all three requested, in order",
          list(objs.keys()) == ["zeta", "dh", "beurling"], f"got {list(objs.keys())}")
    z, dh, beu = objs["zeta"], objs["dh"], objs["beurling"]
    check("zeta exposes evaluate/zeros (not called)",
          hasattr(z, "evaluate") and hasattr(z, "zeros"))
    check("dh exposes evaluate/zeros (not called)",
          hasattr(dh, "evaluate") and hasattr(dh, "zeros"))
    check("beurling exposes theta/gen_integers/count_integers, deliberately no evaluate/zeros",
          hasattr(beu, "theta") and hasattr(beu, "gen_integers")
          and hasattr(beu, "count_integers")
          and not hasattr(beu, "evaluate") and not hasattr(beu, "zeros"))

    threw = False
    try:
        controls(["not_a_control"])
    except ValueError:
        threw = True
    check("unknown control name raises ValueError", threw)

    results = run_on_controls(lambda name, obj: name.upper(), ["zeta", "dh"])
    check("run_on_controls preserves order and applies fn per control",
          list(results.items()) == [("zeta", "ZETA"), ("dh", "DH")], f"got {dict(results)}")


def test_npz_roundtrip(tmp_path=None):
    print("Test 5: save_npz / load_provenance round trip")
    out_dir = _cache_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "test_harness_roundtrip.npz"
    arrays = {"xs": np.array([1.0, 2.0, 3.0]), "ys": np.array([[1, 2], [3, 4]])}
    prov = {"dps": 50, "seed": 149, "wall_time_s": 0.01, "params": {"a": 1.0, "sigma": 0.5}}
    save_npz(path, arrays, prov)
    loaded = np.load(path)
    check("array round-trips", np.allclose(loaded["xs"], arrays["xs"]))
    check("2D array round-trips", np.array_equal(loaded["ys"], arrays["ys"]))
    got_prov = load_provenance(path)
    check("provenance round-trips as a dict", got_prov == prov, f"got {got_prov}")

    threw = False
    try:
        save_npz(path, {"_harness_provenance": np.array([1])}, {})
    except ValueError:
        threw = True
    check("reserved provenance key collision raises ValueError", threw)

    path.unlink(missing_ok=True)


def _cache_dir():
    from pathlib import Path
    return Path(__file__).resolve().parent / "_cache"


def test_quick_arg():
    print("Test 6: quick_arg parsing")
    check("--quick present sets True", quick_arg(["--quick"]) is True)
    check("no flag defaults to False", quick_arg([]) is False)
    check("unrelated flags ignored, --quick still found",
          quick_arg(["--other", "value", "--quick"]) is True)
    check("plain positional args do not set quick",
          quick_arg(["some_module_arg"]) is False)


def main():
    test_gates_accounting()
    test_summary_line_format()
    test_preregistry()
    test_controls_construct()
    test_npz_roundtrip()
    test_quick_arg()

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print(f"\n{npass}/{len(CHECKS)} passed")
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
