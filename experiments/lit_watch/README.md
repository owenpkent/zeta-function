# lit_watch: arXiv priority-claim watcher

Protects this project's priority claims on two fronts: (1) new versions of
the papers its live constructions cite as load-bearing (Suzuki
arXiv:2606.09096, CCM arXiv:2511.22755, and the rest of the live corpus in
`watchlist.json`), and (2) new entrants to the project's territory via a
fixed set of keyword queries against `cat:math.NT` on arXiv.

Standard library only (`urllib`, `xml.etree`, `json`). No new dependencies.

## How to run

From the repo root, with the repo's venv:

```
# First time only: seed state.json from a first fetch, no alerts.
.venv/bin/python -m experiments.lit_watch.arxiv_watch --init

# Every subsequent run: fetch, diff against stored state, print a report.
.venv/bin/python -m experiments.lit_watch.arxiv_watch --check
```

`--check` prints a markdown report to stdout (`NEW VERSION` / `NEW LISTING`
lines, or "No changes"), writes that same report to
`experiments/lit_watch/_cache/latest_report.md`, and updates
`experiments/lit_watch/_cache/state.json`. The first `--check` after
`--init` should report no changes; that is correct, since `--init` already
seeded the baseline.

Requests are politely spaced (a fixed delay between each arXiv API call,
watchlist IDs fetched in batches of ~20). A network failure fails soft: it
prints a clear error and leaves `state.json` untouched (the file is only
overwritten after every fetch in the run has already succeeded, via an
atomic write: temp file + rename).

## Where state lives

Everything under `experiments/lit_watch/_cache/` (gitignored, matches the
repo's existing `experiments/**/_cache/` convention):

- `state.json`: last-seen version/title/updated-date per watchlist paper,
  plus the last-seen id set per keyword query.
- `latest_report.md`: the most recent `--check` report.

## Adding a paper to the watchlist

Edit `watchlist.json`, add an object to `"papers"` with `"id"` (the arXiv
id, e.g. `"2606.09096"` or the old-style `"math/0511182"`) and `"note"`
(one line: what this paper guards or why it is load-bearing). Run
`--check` once; the new id has no prior baseline, so it is reported under
"Newly added to watchlist" rather than as a version alarm, and from then
on it is tracked normally. The two mandatory ids (`2606.09096`,
`2511.22755`) must stay in the list; `test_lit_watch.py` checks for both.

Adding or editing a keyword query works the same way, under
`"keyword_queries"`: `"query"` (the phrase, searched in `cat:math.NT`) and
`"note"` (what it guards).

## Automating it

This script does not install a cron job or a scheduled agent; it only
prints a suggestion at the end of `--check`. To actually automate, run
either of the printed suggestions yourself:

```
0 9 * * * cd /home/owen/dev/zeta-function && /home/owen/dev/zeta-function/.venv/bin/python -m experiments.lit_watch.arxiv_watch --check >> /home/owen/dev/zeta-function/experiments/lit_watch/_cache/cron.log 2>&1
```

or, in Claude Code, a `/schedule` request along the lines of: "daily at
9am, run `.venv/bin/python -m experiments.lit_watch.arxiv_watch --check`
from the repo root and report any NEW VERSION or NEW LISTING lines."

## Tests

`.venv/bin/python -m experiments.lit_watch.test_lit_watch` (fully offline,
embedded Atom XML fixture, no network calls; auto-discovered by
`experiments/run_all_tests.py`).
