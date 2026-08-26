# What

<!-- One paragraph: what this PR adds or changes. Name the LEARNINGS entry number if findings landed, and the experiment/dossier files if builds landed. -->

# Type

<!-- feat / fix / docs / refactor / chore, matching the conventional-commit prefix of the main commit. -->

# Checks

- [ ] `python -m experiments.run_all_tests` GREEN (the manual regression battery; there is no CI)
- [ ] New experiments follow the repo test pattern: `main()` under `__main__`, prints `N/N passed`, `--quick` mode never inflates the pass count
- [ ] Pre-registrations written before the run and all resolved (FIRED / SURVIVED / REFUTED); no post-hoc predictions
- [ ] D-H discipline applied to form-side methods, Beurling discipline to counting-side methods, where touched
- [ ] Coordinate claims labeled per the #201 derivability check (new coordinate vs re-measurement of the wall)
- [ ] Tracked `.npz` artifacts saved via `harness.save_npz` next to the scripts; load-bearing evidence tracked (`_evidence/` or `publications/`), never cited into `scratchpad/`
- [ ] `LEARNINGS.md` / `PHASE_STATE.md` updated if findings landed
- [ ] `cd lean; lake build` GREEN if `lean/` was touched
- [ ] Prose follows the style rules (no em dashes; negative results framed as coordinates, not verdicts)

# Frontier

<!-- Moved or UNMOVED, and why. UNMOVED is a normal, honest answer. -->
