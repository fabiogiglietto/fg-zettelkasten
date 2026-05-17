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


class ClaudeClient:
    def __init__(
        self,
        summary_model: str,
        reasoning_model: str,
        api_key: Optional[str] = None,
    ):
        import anthropic  # lazy import: keep the package importable pre-`pip install`

        self.summary_model = summary_model
        self.reasoning_model = reasoning_model
        key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            raise RuntimeError("ANTHROPIC_API_KEY is not set")
        self._client = anthropic.Anthropic(api_key=key)

    def complete(
        self,
        *,
        model: str,
        system: str,
        prompt: str,
        max_tokens: int = 4096,
        cache_system: bool = True,
    ) -> str:
        """Single-turn completion returning the text response.

        When `cache_system` is True the system prompt is marked as a
        prompt-cache breakpoint, so a stable instruction prefix reused across
        many papers is billed at the cache-read rate.
        """
        system_block = {"type": "text", "text": system}
        if cache_system:
            # Mark the (stable) instruction prefix as a prompt-cache breakpoint;
            # reused verbatim across many papers it bills at the cache-read rate.
            system_block["cache_control"] = {"type": "ephemeral"}

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
