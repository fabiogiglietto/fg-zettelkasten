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
