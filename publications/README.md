# Publications workflow (usage guide)

How to use the publication-tracking system: what the pieces are, how to evaluate a finding, and how to
drive a candidate from "logged in LEARNINGS" to "submitted". The registry itself lives one level up in
[`../PUBLICATIONS.md`](../PUBLICATIONS.md); this file is the how-to.

## The two surfaces

| File | Role |
|------|------|
| [`../PUBLICATIONS.md`](../PUBLICATIONS.md) | The **registry**: the candidate table, the evaluation gate, the scoring rubric, the Portfolio read, and the per-candidate dossiers. The single source of truth for status. |
| `publications/` (this directory) | The **work products**: outlines, draft skeletons, scoping docs, and the adversary review. One file per active candidate. |

`experiments/LEARNINGS.md` is the firehose of every finding. `PUBLICATIONS.md` is the small subset that
could leave the repo. This directory is where those get drafted.

## The core idea

A *discovery* and a *paper* are not the same thing. Each `P#` in the registry is a discovery; a paper may
bundle several. The job of this system is to decide, honestly, which discoveries are worth publishing,
where, and in what form, and to keep that decision current as the work and the literature move.

## The workflow (for any new candidate)

1. **Trigger.** A finding in `LEARNINGS.md` (or a Lean result, or a doc) looks like it might be
   publishable. It becomes a candidate.
2. **Run the evaluation gate** (top of `PUBLICATIONS.md`): six questions covering completeness,
   verification status, novelty, D-H soundness, honest framing for negatives, and venue/effort. The
   gate outputs a tier, a venue, and the one next action.
3. **Lit-check BEFORE drafting.** This is the load-bearing discipline (see below). Do not write prose
   for a research candidate until its literature has been checked for pre-emption.
4. **Record it.** Add a registry row + a dossier with the six gate fields. If it is pre-empted or a
   reformulation trap, put it in *Parked / pre-empted* with the pre-empting reference, not in the
   registry.
5. **Draft or scope** in this directory (`P#_*.md`). Keep the registry's "Next" field pointing at the
   single next action so the system stays operational, not archival.
6. **Advance the pipeline:** `candidate -> evaluated -> drafting -> ready -> submitted -> published`.

## The lit-check discipline (the most important rule)

**Every research candidate gets a literature pre-emption check before it is drafted.** This is the
publication-side analogue of the project's Davenport-Heilbronn discipline: a structural sanity check that
catches things that *feel* publishable but are already known.

The track record is the argument for it. Of the three research-tier candidates checked so far:
- **P3** (the D-H wrong-approach discipline): thesis turned out to be canonical Selberg-class folklore
  (Bombieri, Conrey). Demoted; folded into the survey.
- **P5** (the zero-free LP/SDP/SOS ceiling): the 1D headline is the established Mossinghoff-Trudgian
  program. Demoted and reframed to the narrow negative residue.
- **P6** (the function-field RH Lean chain): confirmed genuinely absent from every proof assistant.
  Survived intact.

Two of three over-claims were caught before any drafting effort was spent. Treat "this research finding
is novel" as a hypothesis to be falsified, not an assumption.

## Tiers (set by the gate; full definitions in the registry)

- **READY** (green): verified, novel, submittable now. Only mechanical/human steps remain.
- **STRONG** (blue): genuinely novel and rigorous; needs drafting, not new mathematics.
- **DEVELOPING** (yellow): a real contribution that needs more work, a lit-check, or a bundle decision.
- **PARKED**: not currently publishable as new (pre-empted, or a reformulation that detects the wrong
  thing). Kept so it is not re-proposed.

## Current work products in this directory

| File | What it is |
|------|------------|
| `P4_survey_outline.md` | Outline + positioning for the flagship survey (the convergence thesis). |
| `P4_survey_draft.md` | First prose pass, gate-free sections; §4 (the scorecard) is a stub pending an expert reader. |
| `P5_zero_free_ceiling.md` | Draft skeleton for the zero-free negative-closure note (reframed after lit-check). |
| `P6_hasse_bound_scope.md` | Scoping + Mathlib-source probe for the unconditional Hasse bound. |
| `ADVERSARY_REVIEW.md` | Adversarial review of the system and its claims (severity-ranked findings). |

## How to drive it forward

The standalone-publishable set is `{P1, P2, P6}`; the flagship is the `P4` survey; `P3, P5, P7, P8` fold
into `P4`. The remaining moves are human-gated:

- **P1, P2 (Mathlib PRs):** the math is done and the PR bodies are staged in
  [`../lean/upstream/`](../lean/upstream/). What remains is the GitHub fork / CLA / rebase / submit
  workflow, which a human account must do (this repo cannot open PRs). Submit digamma first.
- **P6:** decide whether to ship the conditional reduction now or budget the multi-month unconditional
  build (see its scoping doc for the route and the M-b1.3 gate).
- **P4:** line up an expert reader for the scorecard's polarization column, then write §4 and revise.

## Maintenance

- Keep the registry table, the dossiers, and the changelog in `PUBLICATIONS.md` current; the changelog is
  the audit trail.
- When a candidate's status changes, update its registry row, its dossier "Next" field, and the
  `TODO.md` Publications section together.
- The memory pointer is `publications_registry.md` in the project memory; update it on major status
  shifts so future sessions inherit the map.
