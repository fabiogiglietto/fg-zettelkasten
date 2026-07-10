"""Tests for src.feed_client item parsing (characterization) and retries."""
import pytest
import requests

from src.feed_client import Paper, _item_to_paper, get_with_retries


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


class _Resp:
    def __init__(self, status_code: int):
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"{self.status_code} Server Error")


def _serve(monkeypatch, responses):
    """Stub requests.get to pop from `responses` (a _Resp or an exception);
    disable backoff sleeps. Returns the list of attempts made."""
    attempts = []

    def fake_get(url, headers=None, timeout=None):
        attempts.append(url)
        item = responses.pop(0)
        if isinstance(item, Exception):
            raise item
        return item

    monkeypatch.setattr("src.feed_client.requests.get", fake_get)
    monkeypatch.setattr("src.feed_client.time.sleep", lambda s: None)
    return attempts


def test_get_with_retries_recovers_from_transient_502(monkeypatch):
    attempts = _serve(monkeypatch, [_Resp(502), _Resp(200)])
    resp = get_with_retries("https://api.example/feed.json")
    assert resp.status_code == 200
    assert len(attempts) == 2


def test_get_with_retries_recovers_from_connection_error(monkeypatch):
    attempts = _serve(
        monkeypatch, [requests.ConnectionError("reset"), _Resp(200)]
    )
    resp = get_with_retries("https://api.example/feed.json")
    assert resp.status_code == 200
    assert len(attempts) == 2


def test_get_with_retries_gives_up_after_max_attempts(monkeypatch):
    attempts = _serve(monkeypatch, [_Resp(502), _Resp(502), _Resp(502)])
    with pytest.raises(requests.HTTPError):
        get_with_retries("https://api.example/feed.json")
    assert len(attempts) == 3


def test_get_with_retries_does_not_retry_client_errors(monkeypatch):
    attempts = _serve(monkeypatch, [_Resp(404)])
    with pytest.raises(requests.HTTPError):
        get_with_retries("https://api.example/feed.json")
    assert len(attempts) == 1
