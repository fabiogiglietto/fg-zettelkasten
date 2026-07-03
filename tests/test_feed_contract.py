"""Tests for src.feed_contract — the toread feed contract gate."""
import json
from pathlib import Path

import pytest

from src.feed_contract import (
    VENDORED_SCHEMA,
    FeedContractError,
    validate_toread_feed,
)


def _valid_feed() -> dict:
    return {
        "version": "https://jsonfeed.org/version/1.1",
        "title": "To Read - Research Papers",
        "items": [
            {
                "id": "bibtex:Boyd2026-pm",
                "title": "A paper",
                "date_published": "2026-01-01T00:00:00Z",
                "content_text": "Abstract.",
                "tags": ["Journal Article"],
                "_discovery_date": "2026-01-02T00:00:00Z",
                "_academic": {"doi": "10.1/xyz", "citation_count": 3},
            }
        ],
    }


def test_vendored_schema_is_valid_json_schema():
    schema = json.loads(Path(VENDORED_SCHEMA).read_text())
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert "item" in schema["$defs"]


def test_valid_feed_passes(monkeypatch):
    monkeypatch.setattr(
        "src.feed_contract._load_schema",
        lambda timeout=10: json.loads(Path(VENDORED_SCHEMA).read_text()),
    )
    validate_toread_feed(_valid_feed())  # must not raise


def test_nullable_fields_pass(monkeypatch):
    """date_published/content_text are null in practice for unenriched items."""
    monkeypatch.setattr(
        "src.feed_contract._load_schema",
        lambda timeout=10: json.loads(Path(VENDORED_SCHEMA).read_text()),
    )
    feed = _valid_feed()
    feed["items"][0]["date_published"] = None
    feed["items"][0]["content_text"] = None
    validate_toread_feed(feed)  # must not raise


def test_team_attribution_fields_pass(monkeypatch):
    """The MINE chain adds submitted_by/_id — optional in the shared schema."""
    monkeypatch.setattr(
        "src.feed_contract._load_schema",
        lambda timeout=10: json.loads(Path(VENDORED_SCHEMA).read_text()),
    )
    feed = _valid_feed()
    feed["items"][0]["_slack_suggestion"] = {
        "channel_id": "C123",
        "ts": "1782984077.356849",
        "submitted_by": "Teammate",
        "submitted_by_id": "U456",
    }
    validate_toread_feed(feed)  # must not raise


def test_broken_feed_raises(monkeypatch):
    monkeypatch.setattr(
        "src.feed_contract._load_schema",
        lambda timeout=10: json.loads(Path(VENDORED_SCHEMA).read_text()),
    )
    feed = _valid_feed()
    feed["items"][0].pop("id")
    feed["items"][0]["tags"] = "not-an-array"
    with pytest.raises(FeedContractError) as exc:
        validate_toread_feed(feed)
    assert "violates the published contract" in str(exc.value)


def test_bad_id_format_raises(monkeypatch):
    monkeypatch.setattr(
        "src.feed_contract._load_schema",
        lambda timeout=10: json.loads(Path(VENDORED_SCHEMA).read_text()),
    )
    feed = _valid_feed()
    feed["items"][0]["id"] = "doi:10.1/xyz"  # join key must be bibtex:<key>
    with pytest.raises(FeedContractError):
        validate_toread_feed(feed)
