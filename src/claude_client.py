"""Thin wrapper around the Anthropic SDK.

Centralises model selection, prompt caching of stable prefixes, and JSON
response parsing so the rest of the project never touches the SDK directly.
Claude does *all* LLM work in this project (see CLAUDE.md).
"""
from __future__ import annotations

import json
import os
import re
from typing import Optional


def credential_source() -> Optional[str]:
    """Which credential the Anthropic SDK will resolve, or None if it finds none.

    Deliberately not a bare `ANTHROPIC_API_KEY` check. In CI the credentials
    come from Workload Identity Federation: the workflow writes a short-lived
    GitHub OIDC token to a file and the SDK exchanges it for an access token.
    There is no API key at all on that path, so gating on one would silently
    disable every Claude call in production while still working locally.

    Federation needs the whole quartet; a partial set is a misconfiguration,
    not a usable credential.
    """
    if os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN"):
        return "api-key"
    federated = (
        os.environ.get("ANTHROPIC_FEDERATION_RULE_ID")
        and os.environ.get("ANTHROPIC_ORGANIZATION_ID")
        and os.environ.get("ANTHROPIC_SERVICE_ACCOUNT_ID")
        and (
            os.environ.get("ANTHROPIC_IDENTITY_TOKEN_FILE")
            or os.environ.get("ANTHROPIC_IDENTITY_TOKEN")
        )
    )
    return "federation" if federated else None


def _extract_json(text: str):
    """Parse a JSON value out of a model response.

    Tolerates a ```json fenced block or leading/trailing prose around the
    JSON payload — Claude is asked for bare JSON but this keeps parsing robust.
    """
    fenced = re.search(r"```(?:json)?\s*(.+?)\s*```", text, re.DOTALL)
    candidate = fenced.group(1) if fenced else text
    candidate = candidate.strip()
    try:
        return json.loads(candidate)
    except json.JSONDecodeError:
        pass
    # Fall back to the first complete JSON value in the response, ignoring any
    # trailing prose the model appended after it (raw_decode stops at the end
    # of the first value rather than guessing a closing brace by rfind).
    start = min(
        (i for i in (candidate.find("{"), candidate.find("[")) if i != -1),
        default=-1,
    )
    if start != -1:
        try:
            value, _ = json.JSONDecoder().raw_decode(candidate, start)
            return value
        except json.JSONDecodeError:
            pass
    raise ValueError(f"no JSON found in response: {text[:200]!r}")


def json_list(value) -> list:
    """Normalize a `complete_json` reply that is expected to be a JSON array.

    Claude is asked for a bare array but sometimes wraps it in an object
    (`{"topics": [...]}`); unwrap the first list value so one off-shape reply
    cannot abort a whole run. Anything else normalizes to an empty list, which
    every caller already treats as "the model proposed nothing".
    """
    if isinstance(value, list):
        return value
    if isinstance(value, dict):
        return next((v for v in value.values() if isinstance(v, list)), [])
    return []


def json_obj(value) -> dict:
    """Normalize a `complete_json` reply that is expected to be a JSON object.

    The mirror of `json_list`: unwraps a single-object array. Callers that
    persist the result must still reject an empty dict rather than cache it.
    """
    if isinstance(value, dict):
        return value
    if isinstance(value, list):
        return next((v for v in value if isinstance(v, dict)), {})
    return {}


class ClaudeClient:
    def __init__(
        self,
        summary_model: str,
        reasoning_model: str,
        api_key: Optional[str] = None,
        assign_model: Optional[str] = None,
        note_model: Optional[str] = None,
    ):
        import anthropic  # lazy import: keep the package importable pre-`pip install`

        self.summary_model = summary_model
        self.reasoning_model = reasoning_model
        # Topic assignment is classification-grade work; a config without
        # `assign_model` keeps the pre-tiering behavior (reasoning_model).
        self.assign_model = assign_model or reasoning_model
        # Paper-note bodies (the Connections paragraph lives there) get their
        # own knob so they can run on a stronger model than the other prose.
        self.note_model = note_model or reasoning_model
        # An explicit api_key still wins (tests, callers that inject one), but
        # the default path constructs zero-arg so the SDK can resolve either an
        # API key or a federated identity token. Passing api_key= unconditionally
        # would pin tier 1 of the credential chain and defeat federation.
        if api_key:
            self._client = anthropic.Anthropic(api_key=api_key)
        else:
            if credential_source() is None:
                raise RuntimeError(
                    "No Anthropic credentials: set ANTHROPIC_API_KEY, or set "
                    "ANTHROPIC_FEDERATION_RULE_ID / _ORGANIZATION_ID / "
                    "_SERVICE_ACCOUNT_ID / _IDENTITY_TOKEN_FILE for federation"
                )
            self._client = anthropic.Anthropic()

    def complete(
        self,
        *,
        model: str,
        system: str,
        prompt: str,
        max_tokens: int = 4096,
    ) -> str:
        """Single-turn completion returning the text response."""
        # No prompt-cache breakpoint on the system prompt: every per-stage
        # system prompt here is 170-425 tokens, far below the cache minimum
        # (4096 for Opus/Haiku, 2048 for Sonnet 5), so a `cache_control` marker
        # would silently never cache. The volatile per-paper content (PDF text,
        # summary) is unique per call and uncacheable too. Add a breakpoint back
        # only if a system prompt ever grows past the model's minimum.
        system_block = {"type": "text", "text": system}

        response = self._client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=[system_block],
            messages=[{"role": "user", "content": prompt}],
        )
        return "".join(
            block.text for block in response.content if block.type == "text"
        )

    def complete_json(self, **kwargs):
        """`complete` followed by a tolerant JSON parse of the response."""
        return _extract_json(self.complete(**kwargs))
