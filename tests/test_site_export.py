"""Tests for the homepage rendered by src.site_export.build_index."""
from src.site_export import build_index


def _index(title: str) -> str:
    return build_index(
        topics=[{"slug": "polarization", "name": "Polarization"}],
        state={"papers": {"bibtex:Holland_Levin2026-qx": {"topics": ["polarization"]}}},
        structure_slugs=set(),
        topics_dir="Topics",
        structures_dir="Structures",
        recent_papers=[
            (
                "Holland_Levin2026-qx",
                {"title": title, "discovery_date": "2026-09-05", "topics": ["polarization"]},
            )
        ],
        papers_dir="Papers",
    )


def test_latest_paper_with_hashtag_title_is_a_markdown_link():
    """Quartz's wikilink regex rejects `#` in an alias, so a hashtag title in a
    `[[path|alias]]` link is left on the page as raw text. Markdown links have
    no such restriction."""
    out = _index("From #StayWoke to “culture wars”")
    assert (
        "- [From #StayWoke to “culture wars”](Papers/Holland_Levin2026-qx) — 2026-09-05"
        " · Polarization"
    ) in out
    assert "[[Papers/" not in out


def test_latest_paper_title_brackets_are_escaped():
    out = _index("Trust [and distrust] online")
    assert "- [Trust \\[and distrust\\] online](Papers/Holland_Levin2026-qx)" in out
