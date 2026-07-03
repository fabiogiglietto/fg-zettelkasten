"""Validate the toread feed against its published JSON Schema.

The normative contract lives in the producer repo
(toread/schema/feed.schema.json); the vendored copy in schema/ is the
fallback so a raw.githubusercontent.com outage cannot block ingestion.
Validation is fail-fast: an invalid feed aborts the run *before* any vault
or state mutation, turning contract drift into a loud workflow failure
instead of silently malformed notes.

One schema serves both chains — team-only fields (`submitted_by`) are
optional in it — so the mine-zettelkasten fork inherits this unchanged.
The own-publications feed is *not* validated here (different producer).
"""
from __future__ import annotations

import json
import logging
from pathlib import Path

import jsonschema
import requests

logger = logging.getLogger(__name__)

SCHEMA_URL = (
    "https://raw.githubusercontent.com/fabiogiglietto/toread/main/"
    "schema/feed.schema.json"
)
VENDORED_SCHEMA = Path(__file__).resolve().parent.parent / "schema" / "feed.schema.json"


class FeedContractError(ValueError):
    """The fetched feed violates the published contract."""


def _load_schema(timeout: int = 10) -> dict:
    """Published schema first (always current), vendored copy as fallback."""
    try:
        resp = requests.get(SCHEMA_URL, timeout=timeout)
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        logger.warning(
            "Could not fetch published schema (%s); using vendored copy", exc
        )
        with open(VENDORED_SCHEMA) as f:
            return json.load(f)


def validate_toread_feed(feed_data: dict, max_errors: int = 10) -> None:
    """Raise FeedContractError if the feed violates the contract."""
    validator = jsonschema.Draft202012Validator(_load_schema())
    errors = sorted(validator.iter_errors(feed_data), key=lambda e: e.json_path)
    if errors:
        details = "; ".join(
            f"{e.json_path}: {e.message}" for e in errors[:max_errors]
        )
        raise FeedContractError(
            f"toread feed violates the published contract "
            f"({len(errors)} error(s)): {details}"
        )
