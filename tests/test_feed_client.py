"""Tests for src.feed_client item parsing (characterization)."""
from src.feed_client import Paper, _item_to_paper


def _item(**overrides) -> dict:
    base = {
        "id": "bibtex:Boyd2026-pm",
        "title": "A paper",
        "content_text": "Abstract.",
        "content_html": (
            "<ul><li><strong>Published in:</strong> New Media &amp;amp; Society"
            "</li></ul>"
        ),
        "date_published": "2026-01-01T00:00:00Z",
        "_discovery_date": "2026-01-02T00:00:00Z",
        "url": "https://doi.org/10.1/xyz",
        "authors": [{"name": "Boyd, Danah"}, {"name": "Ellison, Nicole"}],
        "tags": ["Journal Article"],
        "_academic": {"doi": "10.1/xyz", "volume": "28", "pages": "1-20"},
    }
    base.update(overrides)
    return base


def test_item_to_paper_basic():
    p = _item_to_paper(_item())
    assert p.bibtex_key == "Boyd2026-pm"
    assert p.authors == ["Boyd, Danah", "Ellison, Nicole"]
    assert p.doi == "10.1/xyz"
    assert p.volume == "28"
    assert p.is_own is False


def test_journal_extracted_and_double_unescaped():
    p = _item_to_paper(_item())
    assert p.journal == "New Media & Society"


def test_tolerates_missing_optional_fields():
    p = _item_to_paper(
        {
            "id": "bibtex:X2026-aa",
            "title": "Minimal",
            "tags": [],
            "_academic": {},
        }
    )
    assert isinstance(p, Paper)
    assert p.abstract is None
    assert p.date_published is None
    assert p.journal is None
    assert p.authors == []


def test_tolerates_null_content_fields():
    """The live feed carries null date_published/content_text for some items."""
    p = _item_to_paper(
        _item(content_text=None, date_published=None, content_html=None)
    )
    assert p.abstract is None
    assert p.date_published is None
