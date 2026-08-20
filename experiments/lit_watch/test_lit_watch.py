"""Standalone (non-pytest) test module for experiments/lit_watch.

Fully offline: uses an embedded Atom XML fixture in the real arXiv API
shape instead of any network call, so this runs in well under a second.
Run as: .venv/bin/python -m experiments.lit_watch.test_lit_watch
"""

from __future__ import annotations

import tempfile
from datetime import datetime, timezone
from pathlib import Path

from experiments.lit_watch import arxiv_watch as lw

# Three entries, real arXiv Atom API shape: 2606.09096 at v2 (the "new version"
# case relative to a v1 baseline), 2511.22755 at v1 (the "no change" case
# relative to a v1 baseline), and 2609.00001 (the "new listing" case, an
# id that never appears in any stored baseline below).
FIXTURE_ATOM_XML = """<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
  <title>arXiv Query</title>
  <opensearch:totalResults>3</opensearch:totalResults>
  <opensearch:startIndex>0</opensearch:startIndex>
  <opensearch:itemsPerPage>3</opensearch:itemsPerPage>
  <entry>
    <id>http://arxiv.org/abs/2606.09096v2</id>
    <updated>2026-08-17T13:42:46Z</updated>
    <published>2026-06-10T00:00:00Z</published>
    <title>Weil's quadratic form via the screw function</title>
    <summary>   We establish a unified operator-theoretic framework for understanding the
   results on the Weil quadratic form obtained by Yoshida, Bombieri, and
   Connes-Consani-Moscovici from the perspective of the screw function.   </summary>
    <author><name>Masatoshi Suzuki</name></author>
    <arxiv:primary_category term="math.NT" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2511.22755v1</id>
    <updated>2025-11-27T09:00:00Z</updated>
    <published>2025-11-27T09:00:00Z</published>
    <title>Zeta Spectral Triples</title>
    <summary>  We study spectral triples associated with the Riemann zeta function
  and prove a uniform-convergence lemma for the constrained kernel.  </summary>
    <author><name>Alain Connes</name></author>
    <author><name>Caterina Consani</name></author>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2609.00001v1</id>
    <updated>2026-09-01T00:00:00Z</updated>
    <published>2026-09-01T00:00:00Z</published>
    <title>A brand new result about Weil positivity in the critical strip</title>
    <summary>  We prove a new positivity statement for the Weil explicit formula
  restricted to a family of localized windows.  </summary>
    <author><name>Jane Doe</name></author>
  </entry>
</feed>
"""


def check(label: str, ok: bool, info: str = "") -> bool:
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}{(' - ' + info) if info else ''}")
    return ok


def test_fixture_parsing() -> bool:
    print("Test 1: fixture Atom XML parsing")
    entries = lw.parse_atom_feed(FIXTURE_ATOM_XML)
    ok = check("three entries parsed", len(entries) == 3, f"got {len(entries)}")
    by_id = {e["id"]: e for e in entries}
    ok &= check("2606.09096 present at version 2", by_id.get("2606.09096", {}).get("version") == 2)
    ok &= check("2511.22755 present at version 1", by_id.get("2511.22755", {}).get("version") == 1)
    ok &= check(
        "title parsed and whitespace-collapsed",
        by_id["2606.09096"]["title"] == "Weil's quadratic form via the screw function",
    )
    ok &= check(
        "authors parsed",
        by_id["2511.22755"]["authors"] == ["Alain Connes", "Caterina Consani"],
        str(by_id["2511.22755"]["authors"]),
    )
    ok &= check("summary has no embedded newlines", "\n" not in by_id["2606.09096"]["summary"])
    return ok


def test_version_diff_detection() -> bool:
    print("Test 2: version-diff detection (v1 stored vs v2 fetched -> NEW VERSION)")
    entries = lw.parse_atom_feed(FIXTURE_ATOM_XML)
    old_papers = {
        "2606.09096": {"version": 1, "updated": "2026-06-10T00:00:00Z", "title": "old title"},
        "2511.22755": {"version": 1, "updated": "2025-11-27T09:00:00Z", "title": "Zeta Spectral Triples"},
    }
    new_versions, newly_tracked = lw.compute_version_changes(old_papers, entries)
    ok = check("exactly one version bump detected", len(new_versions) == 1, str(new_versions))
    ok &= check("the bump is 2606.09096", new_versions[0]["id"] == "2606.09096" if new_versions else False)
    ok &= check("old_version=1, new_version=2", new_versions[0]["old_version"] == 1 and new_versions[0]["new_version"] == 2 if new_versions else False)
    ok &= check("2609.00001 flagged newly-tracked, not a version bump", any(e["id"] == "2609.00001" for e in newly_tracked))
    return ok


def test_no_change_detection() -> bool:
    print("Test 3: no-change detection")
    entries = lw.parse_atom_feed(FIXTURE_ATOM_XML)
    # Baseline already at the fetched versions for all three ids: nothing should fire.
    old_papers = {
        "2606.09096": {"version": 2, "updated": "2026-08-17T13:42:46Z", "title": "x"},
        "2511.22755": {"version": 1, "updated": "2025-11-27T09:00:00Z", "title": "x"},
        "2609.00001": {"version": 1, "updated": "2026-09-01T00:00:00Z", "title": "x"},
    }
    new_versions, newly_tracked = lw.compute_version_changes(old_papers, entries)
    ok = check("no version bumps", new_versions == [], str(new_versions))
    ok &= check("no newly-tracked entries", newly_tracked == [], str(newly_tracked))

    # Keyword-listing side: same three ids already in the seen-list -> no new listings.
    new_listings, updated_seen = lw.compute_new_listings(
        ["2606.09096", "2511.22755", "2609.00001"], entries
    )
    ok &= check("no new listings when all ids already seen", new_listings == [], str(new_listings))
    ok &= check("seen-list unchanged in content", set(updated_seen) == {"2606.09096", "2511.22755", "2609.00001"})

    # And the positive case: an empty prior seen-list flags all three as new.
    new_listings2, updated_seen2 = lw.compute_new_listings([], entries)
    ok &= check("empty baseline flags all three as new listings", len(new_listings2) == 3, str(len(new_listings2)))
    ok &= check("updated seen-list absorbs all three ids", set(updated_seen2) == {"2606.09096", "2511.22755", "2609.00001"})
    return ok


def test_state_roundtrip() -> bool:
    print("Test 4: state round-trip via temp dir (atomic write)")
    with tempfile.TemporaryDirectory() as tmp:
        state_path = Path(tmp) / "state.json"
        payload = {
            "papers": {"2606.09096": {"version": 2, "updated": "x", "title": "y"}},
            "keyword_seen": {"Weil positivity": ["2606.09096"]},
            "last_run": datetime.now(timezone.utc).isoformat(),
            "last_mode": "check",
        }
        lw.atomic_write_json(state_path, payload)
        ok = check("state file exists after atomic write", state_path.exists())
        ok &= check("no leftover .tmp files in the directory", not any(p.suffix == ".tmp" for p in Path(tmp).iterdir()))
        loaded = lw.load_json(state_path)
        ok &= check("round-tripped content matches", loaded == payload, str(loaded))

        # Overwrite (second atomic write must also succeed and replace cleanly).
        payload2 = dict(payload)
        payload2["last_mode"] = "init"
        lw.atomic_write_json(state_path, payload2)
        loaded2 = lw.load_json(state_path)
        ok &= check("second atomic write replaces content", loaded2["last_mode"] == "init")

        # load_json on a missing path returns the given default rather than raising.
        missing = lw.load_json(Path(tmp) / "does_not_exist.json", default=None)
        ok &= check("load_json returns default for missing file", missing is None)
    return ok


def test_keyword_query_url_construction() -> bool:
    print("Test 5: keyword-query URL construction")
    fixed_now = datetime(2026, 8, 20, 12, 0, 0, tzinfo=timezone.utc)
    url = lw.build_keyword_query_url("Weil positivity", days=30, max_results=30, now=fixed_now)
    ok = check("targets the arXiv export API", url.startswith(lw.ARXIV_API_BASE))
    ok &= check("restricted to cat:math.NT", "cat%3Amath.NT" in url or "cat:math.NT" in url)
    ok &= check("phrase is present (percent-encoded)", "Weil" in url and ("positivity" in url or urllib_unquote_has(url, "positivity")))
    ok &= check("submittedDate range present", "submittedDate" in url)
    ok &= check("window start is 30 days before now", "20260721" in url, url)
    ok &= check("window end is now", "20260820" in url, url)
    ok &= check("sorted by submission date, descending", "sortBy=submittedDate" in url and "sortOrder=descending" in url)

    ids_url = lw.build_id_list_url(["2606.09096", "2511.22755", "math/0511182"])
    ok &= check("id_list url contains all three ids", all(i in ids_url for i in ["2606.09096", "2511.22755", "math/0511182"]))

    chunks = lw.chunked(list(range(45)), 20)
    ok &= check("chunking splits 45 items into 20/20/5", [len(c) for c in chunks] == [20, 20, 5], str([len(c) for c in chunks]))
    return ok


def urllib_unquote_has(url: str, needle: str) -> bool:
    import urllib.parse as up
    return needle in up.unquote_plus(url)


def test_watchlist_contents() -> bool:
    print("Test 6: watchlist.json loads and contains the two mandatory IDs")
    watchlist = lw.load_watchlist()
    ok = check("watchlist.json has a 'papers' key", "papers" in watchlist)
    ok &= check("watchlist.json has a 'keyword_queries' key", "keyword_queries" in watchlist)
    ids = [p["id"] for p in watchlist.get("papers", [])]
    ok &= check("Suzuki 2606.09096 is present", "2606.09096" in ids)
    ok &= check("CCM 2511.22755 is present", "2511.22755" in ids)
    ok &= check("watchlist size is in the 10-25 range", 10 <= len(ids) <= 25, str(len(ids)))
    ok &= check("no duplicate ids", len(ids) == len(set(ids)), str(len(ids) - len(set(ids))))
    ok &= check("every paper entry has a note", all(p.get("note") for p in watchlist["papers"]))
    ok &= check(
        "every keyword query has a note",
        all(q.get("note") for q in watchlist["keyword_queries"]),
    )
    ok &= check(
        "keyword queries include the seven specified phrases",
        {q["query"] for q in watchlist["keyword_queries"]}
        == {
            "Weil positivity",
            "Weil explicit formula",
            "Li coefficients",
            "Nyman-Beurling",
            "de Branges space",
            "determinant class zeta",
            "Riemann hypothesis positivity",
        },
    )
    return ok


def main() -> int:
    tests = [
        test_fixture_parsing,
        test_version_diff_detection,
        test_no_change_detection,
        test_state_roundtrip,
        test_keyword_query_url_construction,
        test_watchlist_contents,
    ]
    results = []
    for t in tests:
        results.append(t())
        print()
    passed = sum(1 for r in results if r)
    total = len(results)
    print(f"{passed}/{total} passed")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
