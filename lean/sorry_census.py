#!/usr/bin/env python3
"""Count REAL `sorry` invocations in the ZetaRH library, from source.

Why this exists: this codebase discusses sorries constantly in prose
("sorry-free", "`sorry`", "sorryAx", "the former sorry-bodied lemma"), so a
naive `grep -c sorry lean/ZetaRH/*.lean` reports roughly 140 hits across 33
files when the true figure is 33 across 11. And the VERIFIER target registry in
lean/README.md is parsed from README prose rather than from the Lean source, so
it drifts whenever a status line is not updated.

This strips Lean comments (line `--`, nested block `/- -/`, and doc `/-- -/`)
and counts `sorry` / `admit` as whole tokens in the remaining code.

    python3 lean/sorry_census.py                # summary
    python3 lean/sorry_census.py --list         # every occurrence with its VERIFIER id
    python3 lean/sorry_census.py --check 33     # exit 1 if the count moved

Wire the --check form into smoke_test.sh to make a silent regression loud.
"""
from __future__ import annotations
import argparse
import pathlib
import re
import sys

LIB = pathlib.Path(__file__).resolve().parent / "ZetaRH"
TOKEN = re.compile(r"\b(sorry|admit)\b")
# Trailing `-- #LI-1` style VERIFIER target id, captured before comments are cut.
TARGET_ID = re.compile(r"#([A-Za-z0-9]+-[A-Za-z0-9]+)")


def strip_comments(src: str) -> str:
    """Blank out Lean comments, preserving line count and column offsets."""
    out = list(src)
    i, n, depth = 0, len(src), 0
    while i < n:
        if depth == 0 and src.startswith("--", i):
            j = src.find("\n", i)
            j = n if j == -1 else j
            for k in range(i, j):
                out[k] = " "
            i = j
        elif src.startswith("/-", i):
            depth += 1
            out[i] = out[i + 1] = " "
            i += 2
        elif depth and src.startswith("-/", i):
            depth -= 1
            out[i] = out[i + 1] = " "
            i += 2
        else:
            if depth and src[i] != "\n":
                out[i] = " "
            i += 1
    return "".join(out)


def scan() -> list[tuple[str, int, str, str]]:
    """Return (file, lineno, token, verifier_id) for every real occurrence."""
    hits = []
    for path in sorted(LIB.glob("*.lean")):
        raw = path.read_text(encoding="utf-8", errors="replace")
        raw_lines = raw.splitlines()
        for lineno, line in enumerate(strip_comments(raw).splitlines(), 1):
            for m in TOKEN.finditer(line):
                original = raw_lines[lineno - 1] if lineno <= len(raw_lines) else ""
                tid = TARGET_ID.search(original)
                hits.append((path.name, lineno, m.group(1), tid.group(0) if tid else "-"))
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true", help="print every occurrence")
    ap.add_argument("--check", type=int, metavar="N",
                    help="exit 1 unless the count is exactly N")
    args = ap.parse_args()

    hits = scan()
    per_file: dict[str, int] = {}
    for name, _, _, _ in hits:
        per_file[name] = per_file.get(name, 0) + 1

    if args.list:
        for name, lineno, token, tid in hits:
            print(f"{name}:{lineno}  {token:6s} {tid}")
        print()

    for name, count in sorted(per_file.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"{count:4d}  {name}")
    untagged = sum(1 for h in hits if h[3] == "-")
    print(f"\n{len(hits)} sorry/admit in {len(per_file)} of "
          f"{len(list(LIB.glob('*.lean')))} files ({untagged} without a VERIFIER id)")

    if args.check is not None and len(hits) != args.check:
        print(f"\nFAIL: expected {args.check}, found {len(hits)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
