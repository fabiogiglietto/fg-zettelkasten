"""Tests for src.classics — ranking the works the vault cites but does not hold."""
from datetime import datetime, timedelta, timezone

from src import classics, openalex_client
from src.supersede import Record

NOW = datetime(2026, 9, 19, tzinfo=timezone.utc)


def _cache(**works) -> dict:
    return {
        "works": {
            key: {"doi": f"10.1/{key.lower()}", "openalex_id": oid,
                  "referenced_works": refs, "fetched": NOW.isoformat()}
            for key, (oid, refs) in works.items()
        }
    }


def _meta(title, authors=("Nir Grinberg",), **overrides) -> dict:
    base = {"doi": "", "title": title, "authors": list(authors), "year": 2019,
            "venue": "Science", "type": "article", "oa_status": "closed",
            "global_citations": 100}
    base.update(overrides)
    return base


def test_rank_counts_each_citing_note_once_and_skips_held_works():
    cache = _cache(A=("W1", ["W9", "W9", "W2"]), B=("W2", ["W9"]), C=("W3", ["W9", "W8"]))
    ranked = classics.rank(cache, {"A", "B", "C"}, {"A": ["t1"], "B": ["t1"], "C": ["t2"]})
    assert [(c["openalex_ids"], c["count"]) for c in ranked] == [(["W9"], 3), (["W8"], 1)]
    assert ranked[0]["cited_by"] == ["A", "B", "C"]
    assert ranked[0]["topics"] == {"t1": 2, "t2": 1}  # W2 is note B itself: not a candidate


def test_stale_keys_fetches_missing_changed_and_old_empty_entries():
    records = {
        "Fresh": Record(key="Fresh", doi="10.1/fresh"),
        "New": Record(key="New", doi="10.1/new"),
        "Upgraded": Record(key="Upgraded", doi="https://doi.org/10.1/PUBLISHED"),
        "EmptyOld": Record(key="EmptyOld", doi="10.1/emptyold"),
        "EmptyRecent": Record(key="EmptyRecent", doi="10.1/emptyrecent"),
        "NoDoi": Record(key="NoDoi"),
        "Stub": Record(key="Stub", doi="10.1/stub", superseded_by="bibtex:Fresh"),
    }
    cache = _cache(Fresh=("W1", ["W9"]), Upgraded=("W2", ["W9"]),
                   EmptyOld=(None, []), EmptyRecent=(None, []))
    cache["works"]["Upgraded"]["doi"] = "10.1/preprint"
    cache["works"]["EmptyOld"]["fetched"] = (NOW - timedelta(days=45)).isoformat()
    assert classics.stale_keys(records, cache, NOW, 30) == ["EmptyOld", "New", "Upgraded"]


def test_update_cache_keeps_an_unknown_doi_as_an_empty_entry():
    records = {"A": Record(key="A", doi="10.1/A"), "B": Record(key="B", doi="10.1/b")}
    cache = {"works": {}}
    fetched = {"10.1/a": {"openalex_id": "W1", "referenced_works": ["W9", "W9", "W3"]}}
    classics.update_cache(cache, records, ["A", "B"], fetched, NOW)
    assert cache["works"]["A"]["referenced_works"] == ["W3", "W9"]
    assert cache["works"]["B"] == {"doi": "10.1/b", "openalex_id": None,
                                  "referenced_works": [], "fetched": NOW.isoformat()}


def test_build_report_merges_editions_and_unions_their_citing_notes():
    ranked = [
        {"openalex_ids": ["W1"], "cited_by": ["A", "B"], "count": 2, "topics": {}},
        {"openalex_ids": ["W2"], "cited_by": ["B", "C"], "count": 2, "topics": {}},
        {"openalex_ids": ["W3"], "cited_by": ["A", "B"], "count": 2, "topics": {}},
    ]
    works = {
        "W1": _meta("The Hybrid Media System", ["Andrew Chadwick"], type="book", year=2013),
        "W2": _meta("The hybrid media system.", ["Andrew Chadwick"], type="book", year=2017),
        "W3": _meta("Fake news on Twitter"),
    }
    report = classics.build_report(ranked, works, {}, {"A": ["t"], "B": ["t"], "C": ["u"]})
    assert [(c["title"], c["count"]) for c in report] == [
        ("The Hybrid Media System", 3), ("Fake news on Twitter", 2)]
    assert report[0]["openalex_ids"] == ["W1", "W2"]
    assert report[0]["is_book"] and report[0]["topics"] == {"t": 2, "u": 1}


def test_build_report_drops_held_excluded_and_metadata_less_works():
    ranked = [{"openalex_ids": [w], "cited_by": ["A"], "count": 1, "topics": {}}
              for w in ("W1", "W2", "W3", "W4", "W5", "W6")]
    works = {
        "W1": _meta("Held by DOI", doi="10.1/HELD"),
        "W2": _meta("The Spread of True and False News Online!"),
        "W3": _meta("A dataset", type="dataset"),
        "W4": _meta("Louvain", doi="10.1/louvain"),
        "W5": _meta("Kept"),
        # W6 has no metadata at all
    }
    records = {
        "X": Record(key="X", title="Something else", doi="https://doi.org/10.1/held"),
        "Y": Record(key="Y", title="The spread of true and false news online"),
    }
    report = classics.build_report(ranked, works, records, {},
                                   exclude_types={"dataset"}, exclude_dois={"10.1/LOUVAIN"})
    assert [c["title"] for c in report] == ["Kept"]


def test_by_topic_ranks_within_the_topic_and_needs_two_citing_notes():
    report = [
        {"title": "Broad", "count": 9, "topics": {"t1": 2, "t2": 7}},
        {"title": "Niche", "count": 3, "topics": {"t1": 3}},
        {"title": "Once", "count": 5, "topics": {"t1": 1, "t2": 4}},
    ]
    view = classics.by_topic(report, per_topic=5)
    assert [c["title"] for c in view["t1"]] == ["Niche", "Broad"]
    assert [c["title"] for c in view["t2"]] == ["Broad", "Once"]


def test_cite_handles_particles_and_author_counts():
    assert classics.cite({"authors": ["José van Dijck", "Thomas Poell", "Martijn de Waal"],
                          "year": 2018}) == "van Dijck, Poell & de Waal (2018)"
    assert classics.cite({"authors": ["A One", "B Two", "C Three", "D Four"],
                          "year": 2019}) == "One et al. (2019)"
    assert classics.cite({"authors": [], "year": None}) == "Unknown (n.d.)"


def test_render_markdown_escapes_pipes_and_marks_books():
    cand = {**_meta("A | B", doi="10.1/x", type="book"), "is_book": True,
            "count": 4, "topics": {"t1": 3}}
    text = classics.render_markdown(
        [cand], {"t1": [cand]},
        {"sources": 10, "in_openalex": 9, "with_refs": 7, "distinct_works": 50}, "2026-09-19")
    assert "| 4 | 📕 Grinberg (2019). [A \\| B](https://doi.org/10.1/x) |" in text
    assert "### t1" in text and "7 of 10 notes" in text


def test_references_by_doi_batches_and_skips_unbatchable_dois(monkeypatch):
    calls = []

    def fake_batch(filter_value, select, mailto):
        calls.append(filter_value)
        return [{"id": "https://openalex.org/W1", "doi": "https://doi.org/10.1/A",
                 "referenced_works": ["https://openalex.org/W9"]}]

    monkeypatch.setattr(openalex_client, "_get_batch", fake_batch)
    dois = ["10.1/A", "10.1/a", "10.1/has,comma"] + [f"10.2/{i}" for i in range(45)]
    found = openalex_client.references_by_doi(dois, mailto="x@y.z")
    assert found == {"10.1/a": {"openalex_id": "W1", "referenced_works": ["W9"]}}
    assert len(calls) == 2 and "comma" not in "".join(calls)  # 46 DOIs -> 40 + 6


def test_openalex_batch_failure_is_not_fatal(monkeypatch):
    import requests

    def boom(*args, **kwargs):
        raise requests.ConnectionError("reset")

    monkeypatch.setattr("src.feed_client.get_with_retries", boom)
    assert openalex_client.references_by_doi(["10.1/a"]) == {}
    assert openalex_client.works_by_id(["W1"]) == {}
