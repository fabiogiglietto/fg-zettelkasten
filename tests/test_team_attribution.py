"""Characterization tests for the team-submission (attribution) path.

On the fg chain the feed never carries `_slack_suggestion.submitted_by*`, so
every team behavior below must be inert; on the mine chain the same code
renders attribution. Both positions are pinned here.
"""
from src.feed_client import _item_to_paper
from src.site_export import inject_contributor, inject_title


def _item(**overrides) -> dict:
    base = {
        "id": "bibtex:Doe2026-sla1",
        "title": "A Suggested Paper",
        "content_text": "Abstract.",
        "tags": [],
        "_academic": {"doi": "10.2/x"},
    }
    base.update(overrides)
    return base


def test_fg_item_is_not_team_submission():
    p = _item_to_paper(_item())
    assert p.is_team_submission is False
    assert p.submitted_by is None
    assert p.submitted_by_id is None


def test_fg_slack_suggestion_without_identity_is_not_team():
    """fg feeds carry _slack_suggestion (channel/ts/permalink) but no
    identity — that must NOT count as a team submission."""
    p = _item_to_paper(_item(_slack_suggestion={
        "channel_id": "C1", "ts": "1.0", "permalink": "https://slack/p",
    }))
    assert p.is_team_submission is False
    assert p.slack_permalink == "https://slack/p"


def test_team_item_carries_attribution():
    p = _item_to_paper(_item(_slack_suggestion={
        "channel_id": "C1", "ts": "1.0", "permalink": "https://slack/p",
        "submitted_by": "GiadaM.", "submitted_by_id": "UR389",
    }))
    assert p.is_team_submission is True
    assert p.submitted_by == "GiadaM."
    assert p.submitted_by_id == "UR389"


def test_user_id_alone_counts_as_team():
    p = _item_to_paper(_item(_slack_suggestion={
        "channel_id": "C1", "ts": "1.0", "submitted_by_id": "UR389",
    }))
    assert p.is_team_submission is True


# ---- site export helpers -------------------------------------------------


def test_inject_contributor_adds_footer():
    note = (
        "---\n"
        'title: "X"\n'
        'submitted_by: "GiadaM."\n'
        "---\n\nBody.\n"
    )
    out = inject_contributor(note)
    assert "Suggested by GiadaM." in out


def test_inject_contributor_noop_without_frontmatter_field():
    note = "---\ntitle: \"X\"\n---\n\nBody.\n"
    assert "Suggested by" not in inject_contributor(note)


def test_inject_title_promotes_h1_with_suffix():
    note = "---\ndate: 2026-01-01\n---\n# My Topic\n\nBody.\n"
    out = inject_title(note, " (Structure)")
    assert 'title: "My Topic (Structure)"' in out
    assert "# My Topic\n" not in out


def test_inject_title_noop_when_title_present():
    note = '---\ntitle: "Already"\n---\n# H1\n\nBody.\n'
    assert inject_title(note) == note
