"""arXiv literature watcher for the RH proof program's priority claims.

Protects two things: (1) new versions of the live corpus this project's
constructions cite as load-bearing (Suzuki arXiv:2606.09096, CCM
arXiv:2511.22755, and the rest of watchlist.json's papers), and (2) new
entrants to the project's territory via a fixed set of keyword queries
against cat:math.NT.

Usage (run as a module from the repo root, with the repo's venv):
    .venv/bin/python -m experiments.lit_watch.arxiv_watch --init
    .venv/bin/python -m experiments.lit_watch.arxiv_watch --check

--init seeds experiments/lit_watch/_cache/state.json from a first fetch
without printing any alerts (that fetch establishes the baseline versions
and the baseline "already seen" set for every keyword query).

--check re-fetches everything, diffs against the stored state, prints a
markdown report (NEW VERSION / NEW LISTING / no changes), writes that
report to _cache/latest_report.md, and updates _cache/state.json.

Only the standard library is used (urllib, xml.etree, json). Network calls
are politely spaced (a fixed delay between HTTP requests) and the whole
run fails soft on any network error: state.json is only overwritten after
every fetch in the run has already succeeded, so a failed --check never
leaves a half-written or corrupted state file.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

LIT_WATCH_DIR = Path(__file__).resolve().parent
WATCHLIST_PATH = LIT_WATCH_DIR / "watchlist.json"
CACHE_DIR = LIT_WATCH_DIR / "_cache"
STATE_PATH = CACHE_DIR / "state.json"
REPORT_PATH = CACHE_DIR / "latest_report.md"

ARXIV_API_BASE = "https://export.arxiv.org/api/query"
USER_AGENT = "zeta-function-repo-lit-watch/1 (research literature watcher; single low-rate requests)"
REQUEST_DELAY_SECONDS = 3.0
ID_CHUNK_SIZE = 20
DEFAULT_WINDOW_DAYS = 30
DEFAULT_MAX_RESULTS = 30

ATOM_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
    "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
}

_ID_VERSION_RE = re.compile(r"/abs/(?P<id>.+?)v(?P<version>\d+)$")


class LitWatchNetworkError(RuntimeError):
    """Raised when a fetch from the arXiv API fails. Never leaves state.json touched."""


# ---------------------------------------------------------------------------
# Watchlist / state I/O
# ---------------------------------------------------------------------------

def load_watchlist(path: Path = WATCHLIST_PATH) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_json(path: Path, default=None):
    if not path.exists():
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def atomic_write_json(path: Path, obj) -> None:
    """Write JSON atomically: write to a temp file in the same directory, then rename.

    A rename within the same filesystem is atomic, so a crash or interrupt
    mid-write never leaves a truncated or partially-written state.json.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(prefix=".state_", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(obj, f, indent=2, sort_keys=True)
            f.write("\n")
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(prefix=".report_", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


# ---------------------------------------------------------------------------
# arXiv Atom API: URL construction and parsing (pure functions, no I/O)
# ---------------------------------------------------------------------------

def chunked(items: list, size: int) -> list:
    return [items[i:i + size] for i in range(0, len(items), size)]


def build_id_list_url(ids: list[str], base: str = ARXIV_API_BASE) -> str:
    """Batched id_list query for a chunk of arXiv IDs (old- and new-style both work)."""
    params = {"id_list": ",".join(ids), "max_results": str(max(len(ids), 1))}
    return f"{base}?{urllib.parse.urlencode(params, safe=',/')}"


def build_keyword_query_url(
    keyword: str,
    days: int = DEFAULT_WINDOW_DAYS,
    max_results: int = DEFAULT_MAX_RESULTS,
    now: datetime | None = None,
    base: str = ARXIV_API_BASE,
) -> str:
    """New-listing query: cat:math.NT AND abs:"<keyword>", submittedDate within a trailing window."""
    now = now or datetime.now(timezone.utc)
    start = now - timedelta(days=days)
    date_fmt = "%Y%m%d%H%M%S"
    search_query = (
        f'cat:math.NT AND abs:"{keyword}" '
        f"AND submittedDate:[{start.strftime(date_fmt)} TO {now.strftime(date_fmt)}]"
    )
    params = {
        "search_query": search_query,
        "start": "0",
        "max_results": str(max_results),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    return f"{base}?{urllib.parse.urlencode(params)}"


def _first_text(elem, path: str, ns=ATOM_NS) -> str:
    node = elem.find(path, ns)
    return (node.text or "").strip() if node is not None else ""


def parse_atom_feed(xml_text: str | bytes) -> list[dict]:
    """Parse an arXiv Atom feed into a list of entry dicts.

    Each dict: id (short arXiv id, no version), version (int), updated (str,
    ISO8601 as returned by arXiv), title (str, whitespace-collapsed),
    authors (list[str]), summary (str, whitespace-collapsed).

    Entries whose <id> does not match the expected .../abs/<id>v<n> shape
    are skipped rather than raising, so a feed format quirk degrades to
    "fewer entries parsed" rather than a crash.
    """
    root = ET.fromstring(xml_text)
    out = []
    for entry in root.findall("atom:entry", ATOM_NS):
        raw_id = _first_text(entry, "atom:id")
        m = _ID_VERSION_RE.search(raw_id)
        if not m:
            continue
        title = " ".join(_first_text(entry, "atom:title").split())
        summary = " ".join(_first_text(entry, "atom:summary").split())
        authors = [
            " ".join((_first_text(a, "atom:name") or "").split())
            for a in entry.findall("atom:author", ATOM_NS)
        ]
        out.append(
            {
                "id": m.group("id"),
                "version": int(m.group("version")),
                "updated": _first_text(entry, "atom:updated"),
                "title": title,
                "authors": [a for a in authors if a],
                "summary": summary,
            }
        )
    return out


# ---------------------------------------------------------------------------
# Diffing (pure functions, no I/O)
# ---------------------------------------------------------------------------

def compute_version_changes(old_papers: dict, new_entries: list[dict]) -> tuple[list[dict], list[dict]]:
    """Compare freshly-fetched watchlist entries against the stored state.

    Returns (new_versions, newly_tracked):
    - new_versions: entries whose fetched version is strictly greater than
      the stored version, each carrying old_version/new_version/updated/title.
    - newly_tracked: entries with no prior state (first time seen; not an
      alarm, just informational, e.g. after the watchlist itself grows).
    """
    new_versions = []
    newly_tracked = []
    for entry in new_entries:
        pid = entry["id"]
        old = old_papers.get(pid)
        if old is None:
            newly_tracked.append(entry)
        elif entry["version"] > int(old.get("version", 0)):
            new_versions.append(
                {
                    "id": pid,
                    "old_version": int(old.get("version", 0)),
                    "new_version": entry["version"],
                    "updated": entry["updated"],
                    "title": entry["title"],
                }
            )
    return new_versions, newly_tracked


def compute_new_listings(old_seen_ids: list[str], entries: list[dict]) -> tuple[list[dict], list[str]]:
    """Compare one keyword query's fresh results against its stored 'seen' id list.

    Returns (new_listings, updated_seen_ids). updated_seen_ids is the union
    of old and newly-seen ids (the new persisted baseline for this query).
    """
    seen_set = set(old_seen_ids)
    new_listings = [e for e in entries if e["id"] not in seen_set]
    updated_seen_ids = sorted(seen_set | {e["id"] for e in entries})
    return new_listings, updated_seen_ids


def snippet(summary: str, max_chars: int = 220) -> str:
    summary = summary.strip()
    if len(summary) <= max_chars:
        return summary
    cut = summary[:max_chars].rsplit(" ", 1)[0]
    return cut + "..."


# ---------------------------------------------------------------------------
# Network (impure; isolated so tests never touch it)
# ---------------------------------------------------------------------------

def _http_get(url: str, timeout: float = 20.0, sleep_after: bool = True) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise LitWatchNetworkError(f"request failed for {url}: {exc}") from exc
    finally:
        if sleep_after:
            time.sleep(REQUEST_DELAY_SECONDS)
    return data


def fetch_watchlist_entries(ids: list[str]) -> list[dict]:
    """Batched id_list fetch, chunked to ID_CHUNK_SIZE, one polite request per chunk."""
    entries = []
    for chunk in chunked(ids, ID_CHUNK_SIZE):
        xml_text = _http_get(build_id_list_url(chunk))
        entries.extend(parse_atom_feed(xml_text))
    return entries


def fetch_keyword_entries(keyword: str, days: int, max_results: int) -> list[dict]:
    xml_text = _http_get(build_keyword_query_url(keyword, days=days, max_results=max_results))
    return parse_atom_feed(xml_text)


# ---------------------------------------------------------------------------
# Report formatting
# ---------------------------------------------------------------------------

def format_report(
    mode: str,
    new_versions: list[dict],
    new_listings: list[dict],
    newly_tracked: list[dict],
    n_papers: int,
    n_queries: int,
) -> str:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [f"# Literature watch report ({mode}) - {ts}", ""]

    if mode == "init":
        lines.append(f"Seeded state from {n_papers} watchlist papers and {n_queries} keyword queries.")
        lines.append("No alerts on init; this run establishes the baseline for the next --check.")
        return "\n".join(lines) + "\n"

    if not new_versions and not new_listings and not newly_tracked:
        lines.append(f"No changes. {n_papers} tracked papers unchanged; {n_queries} keyword queries: no new listings in the trailing window.")
        return "\n".join(lines) + "\n"

    if new_versions:
        lines.append("## NEW VERSION")
        lines.append("")
        for c in sorted(new_versions, key=lambda x: x["id"]):
            lines.append(
                f"- **{c['id']}**: v{c['old_version']} -> v{c['new_version']} "
                f"(updated {c['updated']}) - \"{c['title']}\""
            )
        lines.append("")

    if new_listings:
        lines.append("## NEW LISTING")
        lines.append("")
        for e in sorted(new_listings, key=lambda x: x["id"]):
            authors = ", ".join(e["authors"]) if e["authors"] else "(authors unknown)"
            lines.append(
                f"- **{e['id']}**: \"{e['title']}\" - {authors} - {snippet(e['summary'])} "
                f"(caught by query: \"{e['query']}\")"
            )
        lines.append("")

    if newly_tracked:
        lines.append("## Newly added to watchlist (no prior baseline; now tracked)")
        lines.append("")
        for e in sorted(newly_tracked, key=lambda x: x["id"]):
            lines.append(f"- **{e['id']}**: v{e['version']} - \"{e['title']}\"")
        lines.append("")

    return "\n".join(lines) + "\n"


CRONTAB_SUGGESTION = (
    "0 9 * * * cd /home/owen/dev/zeta-function && "
    "/home/owen/dev/zeta-function/.venv/bin/python -m experiments.lit_watch.arxiv_watch --check "
    ">> /home/owen/dev/zeta-function/experiments/lit_watch/_cache/cron.log 2>&1"
)

SCHEDULE_SUGGESTION = (
    '/schedule daily at 9am: run ".venv/bin/python -m experiments.lit_watch.arxiv_watch --check" '
    "from /home/owen/dev/zeta-function and report any NEW VERSION or NEW LISTING lines "
    "from the printed output (or experiments/lit_watch/_cache/latest_report.md)."
)


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def _papers_dict_from_entries(entries: list[dict]) -> dict:
    return {
        e["id"]: {"version": e["version"], "updated": e["updated"], "title": e["title"]}
        for e in entries
    }


def cmd_init(watchlist: dict) -> int:
    ids = [p["id"] for p in watchlist["papers"]]
    queries = [q["query"] for q in watchlist["keyword_queries"]]

    try:
        print(f"Fetching {len(ids)} watchlist papers (chunks of {ID_CHUNK_SIZE})...")
        entries = fetch_watchlist_entries(ids)
        keyword_seen = {}
        for q in queries:
            print(f"Fetching keyword baseline: \"{q}\"...")
            hits = fetch_keyword_entries(q, DEFAULT_WINDOW_DAYS, DEFAULT_MAX_RESULTS)
            keyword_seen[q] = sorted({h["id"] for h in hits})
    except LitWatchNetworkError as exc:
        print(f"NETWORK ERROR during --init: {exc}")
        print("state.json was NOT written (fail-soft: nothing is overwritten on a failed fetch).")
        return 1

    state = {
        "papers": _papers_dict_from_entries(entries),
        "keyword_seen": keyword_seen,
        "last_run": datetime.now(timezone.utc).isoformat(),
        "last_mode": "init",
    }
    atomic_write_json(STATE_PATH, state)

    fetched_ids = {e["id"] for e in entries}
    missing = [i for i in ids if i not in fetched_ids]
    if missing:
        print(f"WARNING: {len(missing)} watchlist id(s) returned no metadata from arXiv: {missing}")

    report = format_report("init", [], [], [], len(state["papers"]), len(keyword_seen))
    print(report)
    print(f"State written to {STATE_PATH}")
    return 0


def cmd_check(watchlist: dict) -> int:
    old_state = load_json(STATE_PATH)
    if old_state is None:
        print(f"No state found at {STATE_PATH}.")
        print("Run --init first: .venv/bin/python -m experiments.lit_watch.arxiv_watch --init")
        return 1

    ids = [p["id"] for p in watchlist["papers"]]
    queries = [q["query"] for q in watchlist["keyword_queries"]]

    try:
        print(f"Fetching {len(ids)} watchlist papers (chunks of {ID_CHUNK_SIZE})...")
        fresh_entries = fetch_watchlist_entries(ids)

        new_listings = []
        updated_keyword_seen = dict(old_state.get("keyword_seen", {}))
        for q in queries:
            print(f"Fetching keyword window: \"{q}\"...")
            hits = fetch_keyword_entries(q, DEFAULT_WINDOW_DAYS, DEFAULT_MAX_RESULTS)
            old_seen = old_state.get("keyword_seen", {}).get(q, [])
            listings, updated_seen = compute_new_listings(old_seen, hits)
            for e in listings:
                e = dict(e)
                e["query"] = q
                new_listings.append(e)
            updated_keyword_seen[q] = updated_seen
    except LitWatchNetworkError as exc:
        print(f"NETWORK ERROR during --check: {exc}")
        print("state.json was NOT modified (fail-soft: the prior state file is untouched).")
        return 1

    old_papers = old_state.get("papers", {})
    new_versions, newly_tracked = compute_version_changes(old_papers, fresh_entries)

    report = format_report(
        "check", new_versions, new_listings, newly_tracked, len(ids), len(queries)
    )
    print(report)

    new_state = {
        "papers": _papers_dict_from_entries(fresh_entries),
        "keyword_seen": updated_keyword_seen,
        "last_run": datetime.now(timezone.utc).isoformat(),
        "last_mode": "check",
    }
    atomic_write_json(STATE_PATH, new_state)
    atomic_write_text(REPORT_PATH, report)
    print(f"Report written to {REPORT_PATH}")
    print(f"State written to {STATE_PATH}")

    print()
    print("Suggested crontab line (not installed; add with `crontab -e` if desired):")
    print(f"  {CRONTAB_SUGGESTION}")
    print()
    print("Suggested Claude Code /schedule phrasing (not scheduled; run manually if desired):")
    print(f"  {SCHEDULE_SUGGESTION}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--init", action="store_true", help="seed state.json without alerting")
    group.add_argument("--check", action="store_true", help="fetch, diff against state, report, update state")
    args = parser.parse_args(argv)

    watchlist = load_watchlist()

    if args.init:
        return cmd_init(watchlist)
    return cmd_check(watchlist)


if __name__ == "__main__":
    sys.exit(main())
