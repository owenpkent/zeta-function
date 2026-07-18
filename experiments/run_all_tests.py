"""Aggregate runner for the repo's standalone test modules.

The repo convention (CLAUDE.md) is standalone test modules, not pytest: each
test_*.py / smoke_test.py has a main() under __main__ and prints "N/N passed".
This runner discovers them, runs each as `python -m <module>` from the repo
root, parses the final count, and prints one summary table. Exit code 0 iff
every module exits 0 AND reports a full count.

Usage:
    python -m experiments.run_all_tests             # run everything
    python -m experiments.run_all_tests lemma_db    # substring filter
    python -m experiments.run_all_tests --list      # discovery only, no runs

Run this after every merge (Housekeeping item in TODO.md). There is no CI;
this is the whole regression net.
"""
from __future__ import annotations

import re
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
# Matches "9/9 passed" and variants like "14/14 toy sandbox tests passed."
COUNT_RE = re.compile(r"(\d+)\s*/\s*(\d+)")
# Zero caches make warm reruns fast; a cold first run of the D-H scan is not.
PER_MODULE_TIMEOUT = 900


def discover() -> list[str]:
    mods = set()
    for pat in ("experiments/**/test_*.py", "experiments/**/smoke_test.py"):
        for p in REPO_ROOT.glob(pat):
            if "_cache" in p.parts:
                continue
            rel = p.relative_to(REPO_ROOT).with_suffix("")
            mods.add(".".join(rel.parts))
    return sorted(mods)


def run_module(mod: str) -> tuple[str, str | None, float]:
    t0 = time.time()
    try:
        proc = subprocess.run(
            [sys.executable, "-m", mod],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=PER_MODULE_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        return "TIMEOUT", None, time.time() - t0
    dt = time.time() - t0
    m = None
    for line in reversed((proc.stdout or "").splitlines()):
        if "passed" in line.lower():
            m = COUNT_RE.search(line)
            if m:
                break
    count = m.group(0) if m else None
    if proc.returncode != 0:
        return "ERROR", count, dt
    if m is None:
        return "NO-COUNT", None, dt
    return ("OK" if m.group(1) == m.group(2) else "FAIL"), count, dt


def main(argv: list[str]) -> int:
    filters = [a for a in argv if not a.startswith("--")]
    mods = discover()
    if filters:
        mods = [m for m in mods if any(f in m for f in filters)]
    if "--list" in argv:
        print("\n".join(mods))
        return 0
    if not mods:
        print("no test modules matched")
        return 1
    results = []
    for mod in mods:
        print(f"[run ] {mod} ...", flush=True)
        status, count, dt = run_module(mod)
        results.append((mod, status, count, dt))
        print(f"[{status:>4}] {mod}  {count or '-'}  ({dt:.1f}s)", flush=True)
    width = max(len(m) for m, *_ in results)
    print("\n" + "=" * (width + 30))
    ok = 0
    for mod, status, count, dt in results:
        print(f"{mod:<{width}}  {status:<8} {count or '-':>14} {dt:7.1f}s")
        ok += status == "OK"
    print("=" * (width + 30))
    print(f"run_all_tests: {ok}/{len(results)} modules fully passed")
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
