"""Tests for retraction handling — the state marker, the guard, the note banner.

The fixture is the real case that prompted the feature: Smith2025-kc, retracted
by PNAS Nexus on 2026-05-07 (notice 10.1093/pnasnexus/pgag137). Offline only.
"""
from src import note_builder
from src.main import classify_feed_paper
from src.state import is_inactive

NOTICE = "10.1093/pnasnexus/pgag137"
DATE = "2026-05-07"

NOTE = """---
title: "Emergent structures of attention on social media are driven by amplification and triad transitivity"
bibtex_key: Smith2025-kc
topics: [computational-network-structure-analysis, platform-engagement-algorithmic-visibility]
---

# Emergent structures of attention on social media are driven by amplification and triad transitivity

> Smith, A. H., Green, J., Welles, B. F., & Lazer, D. (2025). Emergent structures of attention. *PNAS Nexus*.
>
> [View paper](https://doi.org/10.1093/pnasnexus/pgaf106)

## Summary

This paper introduces the concept of the attention broker.
"""


def _retracted_entry() -> dict:
    return {
        "topics": [],
        "content_hash": "h",
        "retracted": {"notice_doi": NOTICE, "date": DATE, "source": "manual"},
    }


def test_is_inactive_covers_tombstones_and_retractions():
    assert is_inactive({"superseded_by": "bibtex:new"})
    assert is_inactive(_retracted_entry())
    assert not is_inactive({"topics": ["t"]})
    assert not is_inactive(None)


def test_a_retracted_paper_is_never_re_rendered_by_a_later_update():
    """Its content hash keeps moving upstream; a re-render would wipe the banner."""
    entry = _retracted_entry()
    assert classify_feed_paper(entry, "h") == "tombstoned"
    assert classify_feed_paper(entry, "a-brand-new-hash") == "tombstoned"


def test_apply_retraction_banners_the_note_and_empties_topics():
    out = note_builder.apply_retraction(NOTE, NOTICE, DATE)
    fm = out.split("\n---\n", 1)[0]
    assert "topics: []" in fm
    assert f"retracted: {DATE}" in fm
    assert f"retraction_notice: {NOTICE}" in fm
    # The banner sits directly under the H1, ahead of the citation...
    h1_end = out.index("\n", out.index("\n# ")+1)
    assert out[h1_end:].lstrip("\n").startswith(note_builder.RETRACTION_MARKER)
    assert f"https://doi.org/{NOTICE}" in out
    # ...and the summary is kept.
    assert "This paper introduces the concept of the attention broker." in out


def test_apply_retraction_is_idempotent():
    once = note_builder.apply_retraction(NOTE, NOTICE, DATE)
    assert note_builder.apply_retraction(once, NOTICE, DATE) == once
    assert once.count(note_builder.RETRACTION_MARKER) == 1


def test_citation_refresh_skips_the_retraction_banner():
    out = note_builder.replace_citation_block(
        note_builder.apply_retraction(NOTE, NOTICE, DATE), "> NEW CITATION"
    )
    assert note_builder.RETRACTION_MARKER in out
    assert "> NEW CITATION" in out
    assert "Smith, A. H., Green" not in out


# --- Crossref notices ------------------------------------------------------

from src import retractions  # noqa: E402

# Real `updated-by` payloads: Smith2025-kc's retraction, and a lung-cancer
# paper whose expression of concern Crossref lists twice with two dates.
SMITH_UPDATED_BY = [{
    "DOI": "10.1093/pnasnexus/pgag137", "type": "retraction", "label": "Retraction",
    "source": "retraction-watch", "record-id": "71976",
    "updated": {"date-parts": [[2026, 5, 7]]},
}]
EOC_UPDATED_BY = [
    {"DOI": "10.1016/j.lungcan.2026.109332", "type": "expression_of_concern",
     "source": "publisher", "updated": {"date-parts": [[2026, 5, 1]]}},
    {"DOI": "10.1016/j.lungcan.2026.109332", "type": "expression_of_concern",
     "source": "publisher", "updated": {"date-parts": [[2026, 2, 13]]}},
    {"DOI": "10.1016/x.new", "type": "new_version", "updated": {"date-parts": [[2026]]}},
]


def test_parse_updates_reads_a_retraction():
    notices = retractions.parse_updates(SMITH_UPDATED_BY)
    assert notices == [{"type": "retraction", "doi": NOTICE, "date": DATE,
                        "source": "retraction-watch"}]
    assert retractions.retraction_of(notices)["doi"] == NOTICE
    assert retractions.flags_of(notices) == []


def test_parse_updates_dedupes_keeps_earliest_and_drops_non_notices():
    notices = retractions.parse_updates(EOC_UPDATED_BY)
    assert len(notices) == 1
    assert notices[0]["type"] == "expression_of_concern"
    assert notices[0]["date"] == "2026-02-13"
    assert retractions.retraction_of(notices) is None
    assert retractions.flags_of(notices) == notices


def test_parse_updates_pads_a_year_only_date():
    [n] = retractions.parse_updates(
        [{"DOI": "10.1/c", "type": "correction", "updated": {"date-parts": [[2020]]}}]
    )
    assert n["date"] == "2020-01-01"


# --- flag callout ----------------------------------------------------------

EOC = {"type": "expression_of_concern", "doi": "10.1/eoc", "date": "2026-02-13",
       "source": "publisher"}
CORRECTION = {"type": "correction", "doi": "10.1/cor", "date": "2026-03-01",
              "source": "publisher"}


def test_apply_notices_flags_without_leaving_the_registers():
    out = note_builder.apply_notices(NOTE, [EOC])
    fm = out.split("\n---\n", 1)[0]
    assert "editorial_notices: [expression_of_concern]" in fm
    assert "topics: [computational-network-structure-analysis" in fm
    assert "Expression of concern (2026-02-13)" in out
    assert note_builder.apply_notices(out, [EOC]) == out


def test_concerns_get_a_caution_callout_and_corrections_a_note():
    out = note_builder.apply_notices(NOTE, [EOC, CORRECTION])
    concern = out.index(note_builder.CONCERN_MARKER)
    corrected = out.index(note_builder.CORRECTION_MARKER)
    assert concern < corrected  # the warning reads first
    assert "Expression of concern (2026-02-13)" in out[concern:corrected]
    assert "Correction (2026-03-01)" in out[corrected:]
    only_correction = note_builder.apply_notices(NOTE, [CORRECTION])
    assert note_builder.CONCERN_MARKER not in only_correction
    assert "[!caution]" not in only_correction


def test_apply_notices_rebuilds_the_blocks_when_a_notice_joins():
    once = note_builder.apply_notices(NOTE, [CORRECTION])
    twice = note_builder.apply_notices(once, [EOC, CORRECTION])
    assert twice.count(note_builder.CONCERN_MARKER) == 1
    assert twice.count(note_builder.CORRECTION_MARKER) == 1
    assert "editorial_notices: [expression_of_concern, correction]" in twice
    assert twice == note_builder.apply_notices(NOTE, [EOC, CORRECTION])


LEGACY_CALLOUT = (
    "> [!caution] Editorial notices\n"
    "> - Correction (2026-03-01): [10.1/cor](https://doi.org/10.1/cor)"
)


def _legacy_note() -> str:
    """A note flagged by the first release: one [!caution] block for everything."""
    h1_end = NOTE.index("\n", NOTE.index("\n# ") + 1)
    return f"{NOTE[:h1_end]}\n\n{LEGACY_CALLOUT}{NOTE[h1_end:]}"


def test_a_single_callout_note_is_migrated_to_the_split_layout():
    migrated = note_builder.apply_notices(_legacy_note(), [CORRECTION])
    assert "Editorial notices" not in migrated
    assert migrated == note_builder.apply_notices(NOTE, [CORRECTION])


def test_notices_sit_below_the_retraction_banner():
    out = note_builder.apply_notices(
        note_builder.apply_retraction(NOTE, NOTICE, DATE), [CORRECTION]
    )
    assert out.index(note_builder.RETRACTION_MARKER) < out.index(note_builder.CORRECTION_MARKER)
    # The citation refresh skips both callouts.
    refreshed = note_builder.replace_citation_block(out, "> NEW CITATION")
    assert note_builder.CORRECTION_MARKER in refreshed
    assert "Smith, A. H., Green" not in refreshed


# --- the other inactive guards --------------------------------------------


def test_a_retracted_note_is_an_inactive_record(tmp_path):
    from src import supersede

    path = tmp_path / "Smith2025-kc.md"
    path.write_text(note_builder.apply_retraction(NOTE, NOTICE, DATE), encoding="utf-8")
    record = supersede.record_from_note(path)
    assert record.retracted == DATE
    assert record.inactive


def test_a_retracted_note_never_takes_a_latest_papers_slot():
    from src import site_export

    text = note_builder.apply_retraction(
        NOTE.replace("topics:", "discovery_date: 2026-09-01T00:00:00Z\ntopics:"),
        NOTICE, DATE,
    )
    assert site_export._read_paper_meta(text) is None


def test_retraction_slack_blocks_link_the_notice_and_the_note():
    from src import slack_client

    [block] = slack_client.build_retraction_blocks(
        "Smith2025-kc", "Emergent structures of attention", "10.1093/pnasnexus/pgaf106",
        NOTICE, DATE, "https://example.org/Papers/Smith2025-kc",
    )
    text = block["text"]["text"]
    assert "Retracted" in text and f"https://doi.org/{NOTICE}" in text
    assert "https://example.org/Papers/Smith2025-kc" in text


# --- check-retractions end to end (Crossref stubbed) ------------------------


def _mini_vault(tmp_path):
    import json

    from src import state as state_mod

    vault = tmp_path / "vault"
    (vault / "Papers").mkdir(parents=True)
    (vault / "Topics").mkdir()
    (vault / "Structures").mkdir()
    notes = {
        "Smith2025-kc": ("10.1093/pnasnexus/pgaf106", NOTE),
        "Tai2026-qk": ("10.1080/10584609.2026.2613661", NOTE.replace(
            "Smith2025-kc", "Tai2026-qk")),
    }
    papers = {}
    for key, (doi, text) in notes.items():
        text = text.replace("bibtex_key:", f"doi: {doi}\nbibtex_key:")
        (vault / "Papers" / f"{key}.md").write_text(text, encoding="utf-8")
        papers[f"bibtex:{key}"] = {
            "note_path": f"Papers/{key}.md",
            "topics": ["computational-network-structure-analysis"],
            "slack_posted": True,
        }
    topics = [{"slug": "computational-network-structure-analysis",
               "name": "Networks", "description": "d"}]
    (tmp_path / "topics.json").write_text(json.dumps(topics), encoding="utf-8")
    state_file = tmp_path / "state.json"
    state_mod.save_state({"papers": papers}, str(state_file))
    cfg = {
        "vault": {"path": str(vault), "papers_dir": "Papers",
                  "topics_dir": "Topics", "structures_dir": "Structures"},
        "paths": {"state_file": str(state_file), "topics_file": str(tmp_path / "topics.json"),
                  "summaries_dir": str(tmp_path / "summaries")},
        "retractions": {"enabled": True, "slack_notice": True},
        "slack": {"enabled": True, "note_base_url": "https://example.org/Papers"},
    }
    return cfg, vault, state_file


def test_check_retractions_applies_both_kinds(tmp_path, monkeypatch):
    import argparse

    from src import main, slack_client, state as state_mod

    cfg, vault, state_file = _mini_vault(tmp_path)
    monkeypatch.setattr(retractions, "fetch_updates", lambda dois, mailto=None: {
        "10.1093/pnasnexus/pgaf106": retractions.parse_updates(SMITH_UPDATED_BY),
        "10.1080/10584609.2026.2613661": [CORRECTION],
    })
    posted = []
    monkeypatch.setattr(slack_client, "post_retraction",
                        lambda *a, **k: posted.append(a[1]) or True)
    monkeypatch.setenv("SLACK_WEBHOOK_URL", "https://hooks.example/x")

    args = argparse.Namespace(apply=True, no_structures=True)
    assert main.cmd_check_retractions(cfg, args) == 0

    state = state_mod.load_state(str(state_file))
    smith, tai = state["papers"]["bibtex:Smith2025-kc"], state["papers"]["bibtex:Tai2026-qk"]
    assert smith["retracted"]["notice_doi"] == NOTICE
    assert smith["retracted"]["source"] == "retraction-watch"
    assert smith["topics"] == []
    assert tai["notices"] == [CORRECTION]
    assert tai["topics"] == ["computational-network-structure-analysis"]
    assert posted == ["Smith2025-kc"]
    register = (vault / "Topics" / "computational-network-structure-analysis.md").read_text()
    assert "[[Tai2026-qk]]" in register and "[[Smith2025-kc]]" not in register

    # A second run finds nothing new: Smith is inactive, Tai's notice is known.
    posted.clear()
    assert main.cmd_check_retractions(cfg, args) == 0
    assert posted == []


def test_check_retractions_reports_without_apply(tmp_path, monkeypatch):
    import argparse

    from src import main, state as state_mod

    cfg, vault, state_file = _mini_vault(tmp_path)
    before = state_file.read_text()
    monkeypatch.setattr(retractions, "fetch_updates", lambda dois, mailto=None: {
        "10.1093/pnasnexus/pgaf106": retractions.parse_updates(SMITH_UPDATED_BY),
    })
    args = argparse.Namespace(apply=False, no_structures=True)
    assert main.cmd_check_retractions(cfg, args) == 0
    assert state_file.read_text() == before
    assert note_builder.RETRACTION_MARKER not in (vault / "Papers" / "Smith2025-kc.md").read_text()


def test_check_retractions_restores_a_flag_a_re_render_dropped(tmp_path, monkeypatch):
    """State knows the notice, but the note lost its callout: re-flag it."""
    import argparse

    from src import main, state as state_mod

    cfg, vault, state_file = _mini_vault(tmp_path)
    state = state_mod.load_state(str(state_file))
    state["papers"]["bibtex:Tai2026-qk"]["notices"] = [CORRECTION]
    state_mod.save_state(state, str(state_file))
    monkeypatch.setattr(retractions, "fetch_updates", lambda dois, mailto=None: {
        "10.1080/10584609.2026.2613661": [CORRECTION],
    })
    note = vault / "Papers" / "Tai2026-qk.md"
    assert note_builder.CORRECTION_MARKER not in note.read_text()

    assert main.cmd_check_retractions(
        cfg, argparse.Namespace(apply=True, no_structures=True)) == 0
    assert note_builder.CORRECTION_MARKER in note.read_text()


def test_structures_pass_can_be_limited_to_the_topics_a_retraction_left(
    tmp_path, monkeypatch
):
    """Between reclusters most fingerprints are stale (update adds papers but
    never rewrites Structures). A retraction must re-bill only its own topics,
    and must neither prune nor forget the others."""
    from types import SimpleNamespace

    from src import main

    structures = tmp_path / "vault" / "Structures"
    structures.mkdir(parents=True)
    (structures / "b.md").write_text("old b", encoding="utf-8")
    register = [{"slug": "a", "name": "A", "description": ""},
                {"slug": "b", "name": "B", "description": ""}]
    state = {
        "papers": {"bibtex:P1": {"topics": ["a"]}, "bibtex:P2": {"topics": ["b"]}},
        "structure_fps": {"a": "stale", "b": "stale"},
    }
    papers_by_key = {k: SimpleNamespace(bibtex_key=k) for k in ("P1", "P2")}
    built = []
    monkeypatch.setattr(note_builder, "build_structure_note",
                        lambda topic, *a, **k: built.append(topic["slug"]) or "new")
    cfg = {"vault": {"path": str(tmp_path / "vault"), "structures_dir": "Structures"},
           "processing": {"incremental_recluster": True}}

    main._generate_structure_notes(
        cfg, register, state, papers_by_key, {}, SimpleNamespace(reasoning_model="m"),
        only={"a"},
    )
    assert built == ["a"]
    assert state["structure_fps"]["b"] == "stale"
    assert (structures / "b.md").read_text() == "old b"


def test_check_retractions_migrates_a_single_callout_note(tmp_path, monkeypatch):
    """State already knows the correction; only the callout layout is stale."""
    import argparse

    from src import main, state as state_mod

    cfg, vault, state_file = _mini_vault(tmp_path)
    state = state_mod.load_state(str(state_file))
    state["papers"]["bibtex:Tai2026-qk"]["notices"] = [CORRECTION]
    state_mod.save_state(state, str(state_file))
    note = vault / "Papers" / "Tai2026-qk.md"
    note.write_text(_legacy_note().replace("Smith2025-kc", "Tai2026-qk").replace(
        "bibtex_key:", "doi: 10.1080/10584609.2026.2613661\nbibtex_key:"), encoding="utf-8")
    monkeypatch.setattr(retractions, "fetch_updates", lambda dois, mailto=None: {
        "10.1080/10584609.2026.2613661": [CORRECTION],
    })

    assert main.cmd_check_retractions(
        cfg, argparse.Namespace(apply=True, no_structures=True)) == 0
    text = note.read_text()
    assert "Editorial notices" not in text
    assert note_builder.CORRECTION_MARKER in text
