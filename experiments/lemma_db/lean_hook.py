"""Lean closability hook (Reduction Engine, increment 5).

Spec: `docs/03_research/reduction_engine.md` sections 5 and 6. The soundness floor
of the engine: a frontier node's discharge is real only when it type-checks in
the Lean substrate (`lean/`).

THE SOUNDNESS BOUNDARY
----------------------
This hook PROMOTES NOTHING. It reports closability; promotion to `proven_lean`
stays a deliberate human edit informed by an authoritative build. Two reasons it
must not auto-mutate:

  1. The authoritative check is `lake build` + a scan for "declaration uses
     'sorry'" warnings. The cheap textual file-level sorry scan does NOT localize
     to a declaration: `RHEquivalences.lean` has 15 sorry/admit tokens yet
     contains the sorry-free anchor `FND-rh-pi01`. File-level sorry presence is
     therefore an ADVISORY signal, never a verdict.
  2. A script flipping a node to `proven_lean` from a textual heuristic would be
     exactly the laundering the engine exists to prevent.

So: textual mode (default, fast) gives advisory consistency flags; build mode
(`run_build=True`, needs the lean toolchain) gives the authoritative verdict.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from dataclasses import dataclass

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LEAN_DIR = os.path.join(REPO_ROOT, "lean")
SEED_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "seed_lemmas.json")

# Verdicts.
DANGLING = "DANGLING"          # lean_ref file does not exist (broken reference)
OVERCLAIM = "OVERCLAIM"        # claims proven_lean but the build is not clean
CLOSABLE = "CLOSABLE"          # proven_lean confirmed by a clean, sorry-free build
CONSISTENT = "CONSISTENT"      # proven_lean; file sorry-free (textual); build to confirm
REVIEW = "REVIEW"              # proven_lean but the file carries sorry tokens; confirm the decl
SCAFFOLD = "SCAFFOLD"          # open/target node whose lean_ref is a work-in-progress file
PROMOTABLE = "PROMOTABLE"      # open node whose file builds clean + sorry-free; review for promotion

# Statuses that ASSERT a Lean proof exists (the ones a clean build must back).
PROVEN_LEAN = ("proven_lean",)

_SORRY_RE = re.compile(r"\b(sorry|admit)\b")


def lake_available() -> bool:
    return shutil.which("lake") is not None


def _strip_comments(text: str) -> str:
    text = re.sub(r"/-.*?-/", "", text, flags=re.S)   # block comments
    text = re.sub(r"--[^\n]*", "", text)              # line comments
    return text


def _textual_sorry_count(path: str) -> int:
    with open(path, encoding="utf-8") as f:
        return len(_SORRY_RE.findall(_strip_comments(f.read())))


def _ref_to_path(lean_ref: str) -> str:
    return os.path.join(REPO_ROOT, lean_ref.replace("/", os.sep))


def _ref_to_module(lean_ref: str) -> str:
    p = lean_ref
    if p.startswith("lean/"):
        p = p[len("lean/"):]
    if p.endswith(".lean"):
        p = p[:-5]
    return p.replace("/", ".")


@dataclass
class LeanCheck:
    node_id: str
    status: str
    lean_ref: str
    file_exists: bool
    textual_sorry: int          # -1 if file missing
    build_status: str           # clean | sorry_warnings | failed | skipped | no_toolchain
    verdict: str
    severity: str               # ERROR | WARN | INFO | OK
    reason: str


def check_node_lean(node: dict, run_build: bool = False, build_timeout: int = 600) -> "LeanCheck | None":
    """Check one node's lean_ref. Returns None if the node has no lean_ref."""
    ref = node.get("lean_ref") or ""
    if not ref:
        return None
    nid, status = node["id"], node["status"]
    path = _ref_to_path(ref)

    if not os.path.exists(path):
        return LeanCheck(nid, status, ref, False, -1, "skipped", DANGLING, "ERROR",
                         f"lean_ref file missing: {ref}")

    ts = _textual_sorry_count(path)

    build_status = "skipped"
    if run_build and lake_available():
        try:
            r = subprocess.run(
                ["lake", "build", _ref_to_module(ref)],
                cwd=LEAN_DIR, capture_output=True, text=True, timeout=build_timeout,
            )
            out = (r.stdout or "") + (r.stderr or "")
            if r.returncode != 0:
                build_status = "failed"
            elif "declaration uses 'sorry'" in out:
                build_status = "sorry_warnings"
            else:
                build_status = "clean"
        except subprocess.TimeoutExpired:
            build_status = "failed"
    elif run_build:
        build_status = "no_toolchain"

    if status in PROVEN_LEAN:
        if build_status == "clean":
            return LeanCheck(nid, status, ref, True, ts, build_status, CLOSABLE, "OK",
                             "proven_lean confirmed by a clean, sorry-free build")
        if build_status in ("failed", "sorry_warnings"):
            return LeanCheck(nid, status, ref, True, ts, build_status, OVERCLAIM, "ERROR",
                             f"claims proven_lean but the build is {build_status}")
        if ts == 0:
            return LeanCheck(nid, status, ref, True, ts, build_status, CONSISTENT, "OK",
                             "proven_lean; file sorry-free (textual); run a build to confirm the decl")
        return LeanCheck(nid, status, ref, True, ts, build_status, REVIEW, "WARN",
                         f"proven_lean but file carries {ts} sorry/admit token(s); confirm the "
                         "declaration is one of the file's sorry-free anchors")

    # open / conjectured / proven_ff / proven_char0 / numerical_only with a lean_ref.
    if build_status == "clean" and ts == 0:
        return LeanCheck(nid, status, ref, True, ts, build_status, PROMOTABLE, "INFO",
                         f"status {status}; file builds clean and is sorry-free - review for promotion "
                         "(declaration-level confirmation needed)")
    return LeanCheck(nid, status, ref, True, ts, build_status, SCAFFOLD, "INFO",
                     f"status {status}; lean_ref is a target/scaffold ({ts} sorry token(s))")


def audit_lean_refs(seed: dict, run_build: bool = False) -> list:
    return [c for n in seed["nodes"]
            if (c := check_node_lean(n, run_build=run_build)) is not None]


def _load_seed(path: str = SEED_PATH) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    seed = _load_seed()
    rb = lake_available()
    print("Lean closability hook (increment 5)")
    print(f"  lake toolchain available: {rb}  |  mode: TEXTUAL (advisory); "
          "pass run_build=True for the authoritative check\n")
    checks = audit_lean_refs(seed, run_build=False)
    width = max(len(c.node_id) for c in checks)
    by_sev = {"ERROR": [], "WARN": [], "INFO": [], "OK": []}
    for c in sorted(checks, key=lambda c: (("ERROR", "WARN", "INFO", "OK").index(c.severity), c.node_id)):
        print(f"  [{c.severity:5}] {c.node_id:<{width}}  {c.verdict:<10} {c.reason}")
        by_sev[c.severity].append(c.node_id)
    print()
    print(f"{len(checks)} lean_ref node(s): "
          f"{len(by_sev['ERROR'])} ERROR, {len(by_sev['WARN'])} WARN (review), "
          f"{len(by_sev['INFO'])} INFO, {len(by_sev['OK'])} OK.")
    if by_sev["ERROR"]:
        print("ERROR rows are dangling refs or proven_lean overclaims; fix or run the build.")
    return 1 if by_sev["ERROR"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
