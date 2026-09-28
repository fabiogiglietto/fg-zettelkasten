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


_SKILL = {
    "name": "mine-zettel-paper",
    "repo": "fabiogiglietto/mine-zettelkasten",
    "bundle": "zettel-paper-skill.zip",
    "homepage": True,
}


def _index_with(skill):
    return build_index(
        topics=[{"slug": "polarization", "name": "Polarization"}],
        state={"papers": {}},
        structure_slugs=set(),
        topics_dir="Topics",
        structures_dir="Structures",
        recent_papers=[],
        papers_dir="Papers",
        site_title="mine-zettelkasten",
        skill=skill,
    )


def test_no_skill_section_by_default():
    out = _index_with(None)
    assert "Write with an AI agent" not in out
    assert out.endswith("\n") and not out.endswith("\n\n")


def test_skill_section_names_the_configured_skill_and_download():
    out = _index_with(_SKILL)
    assert "[Write with an AI agent](#write-with-an-ai-agent)" in out
    assert "## Write with an AI agent" in out
    assert "**`mine-zettel-paper`**" in out
    assert "*from mine-zettelkasten*" in out
    assert (
        "[zettel-paper-skill.zip](https://github.com/fabiogiglietto/"
        "mine-zettelkasten/raw/main/zettel-paper-skill.zip)"
    ) in out
    for env in ("Claude.ai", "Team and Enterprise", "Claude Code",
                "OpenAI Codex CLI", "Other agents"):
        assert env in out
    assert out.index("## Structures") < out.index("## Write with an AI agent")


def test_skill_section_says_it_cannot_read_full_text():
    out = _index_with(_SKILL)
    assert "**from the notes, not the papers**" in out
    assert "cannot read them" in out
