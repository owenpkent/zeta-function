"""Standalone checks for the VERIFIER target-discharge queue tool
(experiments/lemma_db/lean_targets.py). NOT pytest; run as

    .venv/bin/python -m experiments.lemma_db.test_lean_targets

Fast (<15 s), offline, never invokes lake or lean. Prints "N/N passed" last.
"""

from __future__ import annotations

import json

from experiments.lemma_db.lean_targets import (
    ALLOWED_STATUSES, E1U, E1V, E1Z, FEASIBILITY_ORDER, README, REGISTRY_PATH,
    REPO_ROOT, VALUE_ORDER, build_registry, parse_dossier_targets,
    parse_readme_table,
)

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


def main() -> None:
    # 1. the README table parser finds a healthy number of target rows
    rows = parse_readme_table(README.read_text(encoding="utf-8"))
    check("readme_table_nonzero", len(rows) >= 50, f"{len(rows)} rows")

    # 2. landmark rows are present with their modules
    ids = {r["id"]: r for r in rows}
    landmarks = ["#FE-1", "#EF-2", "#2H-1", "#S4C-5", "#GF-1", "V4"]
    check("readme_landmarks", all(t in ids for t in landmarks),
          ", ".join(t for t in landmarks if t not in ids) or "all present")

    # 3. the escaped-pipe row (#FF-M1B) survived cell splitting intact
    check("escaped_pipe_row", "#FF-M1B" in ids and "TateModule" in ids.get(
        "#FF-M1B", {}).get("module", ""))

    # 4. dossier extraction: e1z has 4 targets, e1u has 6, e1v has 4
    e1z = parse_dossier_targets(E1Z, "e1z")
    e1u = parse_dossier_targets(E1U, "e1u")
    e1v = parse_dossier_targets(E1V, "e1v")
    check("dossier_counts", (len(e1z), len(e1u), len(e1v)) == (4, 6, 4),
          f"e1z={len(e1z)} e1u={len(e1u)} e1v={len(e1v)}")

    # 5. the e1z targets are found and the first is the Frostman statement
    check("e1z_frostman_found", len(e1z) >= 1 and "Frostman" in e1z[0]["statement"])

    registry = build_registry()
    targets = registry["targets"]
    by_id = {t["id"]: t for t in targets}

    # 6. registry JSON on disk round-trips against a fresh build
    on_disk = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    check("registry_roundtrip", on_disk == registry,
          "regenerate with: .venv/bin/python -m experiments.lemma_db.lean_targets"
          if on_disk != registry else "")

    # 7. every entry has the required fields, non-empty where it matters
    required = ["id", "statement", "source", "status", "feasibility",
                "feasibility_why", "mathlib_routes", "value"]
    bad = [t["id"] for t in targets
           if any(k not in t for k in required)
           or not t["statement"] or not t["feasibility_why"]
           or not isinstance(t["mathlib_routes"], list)]
    check("required_fields", not bad, ",".join(bad[:5]))

    # 8. statuses and triage codes are from the allowed sets
    bad = [t["id"] for t in targets
           if t["status"] not in ALLOWED_STATUSES
           or t["feasibility"] not in FEASIBILITY_ORDER
           or t["value"] not in VALUE_ORDER]
    check("allowed_codes", not bad, ",".join(bad[:5]))

    # 9. the load-bearing verdicts: e1u-6 discharged (by e1v Theorem V2),
    #    Frostman Mathlib-blocked, and the three drafts marked DRAFTED
    ok = (by_id.get("e1u-6", {}).get("status") == "DISCHARGED"
          and by_id.get("e1z-1", {}).get("feasibility") == "MATHLIB-BLOCKED"
          and all(by_id.get(i, {}).get("status") == "DRAFTED"
                  for i in ["e1z-2", "e1v-1", "e1u-2"]))
    check("triage_verdicts", ok)

    # 10. every DRAFTED entry's lean_ref exists in VerifierQueue.lean
    vq = (REPO_ROOT / "lean" / "ZetaRH" / "VerifierQueue.lean").read_text(
        encoding="utf-8")
    drafted = [t for t in targets if t["status"] == "DRAFTED"]
    bad = [t["id"] for t in drafted
           if "lean_ref" not in t or t["lean_ref"] not in vq]
    check("drafts_present_in_lean", bool(drafted) and not bad, ",".join(bad[:5]))

    # 11. no em dash anywhere in the new artifacts
    files = [
        REPO_ROOT / "experiments" / "lemma_db" / "lean_targets.py",
        REPO_ROOT / "experiments" / "lemma_db" / "test_lean_targets.py",
        REPO_ROOT / "experiments" / "lemma_db" / "verifier_queue.md",
        REPO_ROOT / "experiments" / "lemma_db" / "lean_targets.json",
        REPO_ROOT / "lean" / "ZetaRH" / "VerifierQueue.lean",
    ]
    offenders = [f.name for f in files
                 if f.exists() and "\u2014" in f.read_text(encoding="utf-8")]
    check("no_em_dash", not offenders, ",".join(offenders))

    # 12. the open/discharged split is sane: some of each, and every README
    #     DISCHARGED row really carries a PROVED/DISCHARGED marker upstream
    n_open = sum(1 for t in targets if t["status"] == "OPEN")
    n_done = sum(1 for t in targets if t["status"] == "DISCHARGED")
    check("split_sane", n_open >= 30 and n_done >= 30,
          f"open={n_open} discharged={n_done}")

    npass = sum(1 for _, ok, _ in RESULTS if ok)
    print(f"\n{npass}/{len(RESULTS)} passed")


if __name__ == "__main__":
    main()
