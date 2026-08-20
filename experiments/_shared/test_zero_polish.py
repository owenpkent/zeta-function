"""Tests for the bulk zero-polish engine (experiments/_shared/zero_polish.py).

Standalone module in the repo's test pattern (not pytest): main() prints
"N/N passed" last. Auto-discovered by experiments.run_all_tests; kept under
90 seconds by using low heights and moderate dps.

Run: .venv/bin/python -m experiments._shared.test_zero_polish
"""

from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path

import mpmath as mp

from experiments._shared.zero_polish import (
    ZeroPolishError, _bracket_ok, _seeds_from_scan, polish_zero,
    polish_zeros, zeros_hp)

RESULTS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


def test_agreement_with_zetazero():
    """First 8 zeros polished to dps 60 from crude float seeds must agree
    with mp.zetazero at dps 60 to < 1e-55."""
    seeds = [14.134725, 21.022040, 25.010858, 30.424876,
             32.935062, 37.586178, 40.918719, 43.327073]
    polished = polish_zeros(seeds, 60, workers=1)
    with mp.workdps(65):
        refs = [mp.im(mp.zetazero(k)) for k in range(1, 9)]
        mx = max(abs(p - r) for p, r in zip(polished, refs))
        ok = mx < mp.mpf(10) ** (-55)
    check("polish vs mp.zetazero, 8 zeros at dps 60", ok,
          f"max |diff| = {mp.nstr(mx, 3)}")


def test_bracket_validation():
    """The bracket check passes at a polished zero and fails at a point
    perturbed by far more than the bracket width."""
    z = polish_zero(14.134725, 60)
    ok_at_zero = _bracket_ok(z, 60, 15)
    with mp.workdps(80):
        off = z + mp.mpf(10) ** (-20)  # 1e-20 off; bracket width is 1e-55
    ok_off_zero = _bracket_ok(off, 60, 15)
    check("bracket validation passes at zero", ok_at_zero)
    check("bracket validation rejects off-zero point", not ok_off_zero)


def test_bad_seed():
    """A seed between two zeros either gets flagged or lands on a genuine
    neighboring zero: silent nonsense is the only failure mode."""
    outcomes = []
    for bad in (17.5, 15.9):
        try:
            z = polish_zero(bad, 40)
            with mp.workdps(45):
                refs = [mp.im(mp.zetazero(k)) for k in (1, 2)]
                near = min(abs(z - r) for r in refs)
            outcomes.append(("zero", near < mp.mpf(10) ** (-35)))
        except ZeroPolishError:
            outcomes.append(("flagged", True))
    ok = all(good for _, good in outcomes)
    check("bad seeds flagged or converge to genuine zero", ok,
          ", ".join(f"{bad}: {what}" for (what, _), bad in zip(outcomes, (17.5, 15.9))))


def test_count_and_cache():
    """zeros_hp count matches mp.nzeros; cache round-trips bit-identically;
    the cache file parses via the e2as consumer pattern."""
    tmp = Path(tempfile.mkdtemp(prefix="zero_polish_test_"))
    try:
        gz = zeros_hp(60, 40, workers=2, cache_dir=tmp, verbose=False)
        with mp.workdps(30):
            n_expect = int(mp.nzeros(60))
        check("count consistency to T = 60", len(gz) == n_expect,
              f"{len(gz)} == nzeros(60) = {n_expect}")
        check("ordinates sorted and in range",
              all(a < b for a, b in zip(gz, gz[1:])) and float(gz[-1]) <= 60)

        gz2 = zeros_hp(60, 40, workers=1, cache_dir=tmp, verbose=False)
        check("cache round-trip bit-identical",
              len(gz) == len(gz2) and all(a == b for a, b in zip(gz, gz2)))

        path = tmp / "zeros_polish_dps40_T60.json"
        with mp.workdps(40):
            consumer = [mp.mpf(s) for s in json.loads(path.read_text())]
        check("cache file consumable by the e2as pattern",
              path.exists() and len(consumer) == n_expect
              and all(a == b for a, b in zip(gz, consumer)))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_scan_seed_path():
    """The siegelz sign-change scan (the no-cache fallback) finds exactly the
    right number of seeds and they polish to genuine zeros."""
    with mp.workdps(30):
        n_expect = int(mp.nzeros(40))
    seeds = _seeds_from_scan(40, n_expect, workers=1)
    ok_count = seeds is not None and len(seeds) == n_expect
    check("scan finds nzeros(40) sign changes", ok_count,
          f"{len(seeds) if seeds else None} == {n_expect}")
    if ok_count:
        polished = polish_zeros(seeds, 40, workers=1, seed_digits=8)
        with mp.workdps(45):
            refs = [mp.im(mp.zetazero(k)) for k in range(1, n_expect + 1)]
            mx = max(abs(p - r) for p, r in zip(polished, refs))
            ok = mx < mp.mpf(10) ** (-35)
        check("scan seeds polish to the true zeros", ok,
              f"max |diff| = {mp.nstr(mx, 3)}")


def test_optimistic_hint():
    """seed_digits is a cost hint only: overclaiming the seed quality must
    still converge to the right zero (the loop measures actual accuracy)."""
    z = polish_zero(14.134725, 60, seed_digits=40)  # seed really has ~8 digits
    with mp.workdps(65):
        ref = mp.im(mp.zetazero(1))
        ok = abs(z - ref) < mp.mpf(10) ** (-55)
    check("over-optimistic seed_digits hint still converges", ok)


def test_first_zero_high_dps():
    """One zero at dps 110 (the ladder precision) against mp.zetazero."""
    z = polish_zero(14.134725, 110)
    with mp.workdps(115):
        ref = mp.im(mp.zetazero(1))
        diff = abs(z - ref)
        ok = diff < mp.mpf(10) ** (-105)
    check("dps 110 polish matches zetazero", ok, f"|diff| = {mp.nstr(diff, 3)}")


def main():
    print("test_zero_polish: bulk Newton-polish zero engine")
    test_agreement_with_zetazero()
    test_bracket_validation()
    test_bad_seed()
    test_count_and_cache()
    test_scan_seed_path()
    test_optimistic_hint()
    test_first_zero_high_dps()
    n_pass = sum(1 for _, ok, _ in RESULTS if ok)
    print(f"{n_pass}/{len(RESULTS)} passed")
    return n_pass == len(RESULTS)


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
