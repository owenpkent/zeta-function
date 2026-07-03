# Literature survey (2021-2026)

Raw survey artifacts for the recent Riemann-Hypothesis literature, retrieved via the scholarly-literature connector and triaged 2026-07-03. Moved here from the repo root when the survey was integrated.

| File | What it is |
|------|-----------|
| [`rh_literature_map.md`](rh_literature_map.md) | Narrative field map of 303 arXiv papers by the generic six-thread taxonomy (spectral, RMT/moments, log-correlated, positivity criteria, zero-density, general-RH). The right frame for the field at large. |
| [`rh_full_corpus.csv`](rh_full_corpus.csv) | All 303 papers, with thread, category, publication status, and the `flagged_math_GM` filter column. |
| [`rh_selected_papers.csv`](rh_selected_papers.csv) | The 46 curated "notable" papers highlighted in the map. |
| [`rh_arch2_supplement.md`](rh_arch2_supplement.md) | Companion sweep of the arithmetic-geometry substrate the main map under-samples (prismatic/WCart/Sen, arithmetic Hodge-index/Arakelov positivity, Connes-Consani/F_1): 108 further math.AG papers, 17 curated. This is the M4/R1 critical-path half. |
| [`rh_arch2_supplement.csv`](rh_arch2_supplement.csv) | The 17 curated Architecture-2 papers. |

## What was done with it

These are the field's own framings (survey, not refereeing; no citation weighting, OpenAlex key not configured). The project-specific analysis, cross-referencing all 303 papers against this repo's five open coordinates (R1 / M4 / CCM / SP-C1 / LEVEL), lives in the reading note [`../reading_notes/rh_corpus_2021-2026_vs_frontier.md`](../reading_notes/rh_corpus_2021-2026_vs_frontier.md), synthesized in LEARNINGS #155.

Bottom line of that analysis: zero of the 303 papers supply a new load-bearing object for any open coordinate; the field builds machinery and converges on M4. Two durable outcomes followed: the Beurling firewall (`experiments/_shared/beurling.py`) gained four verified references, and Groskin (arXiv:2605.20224) was confirmed to contain no "two-meter law" (a project term) while independently corroborating LEARNINGS #154.
