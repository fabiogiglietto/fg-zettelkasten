"""Thin wrapper around the Anthropic SDK.

Centralises model selection, prompt caching of stable prefixes, and JSON
response parsing so the rest of the project never touches the SDK directly.
Claude does *all* LLM work in this project (see CLAUDE.md).
"""
from __future__ import annotations

import json
import os
from typing import Optional


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
        # TODO: build the system block (with cache_control when cache_system),
        #       call self._client.messages.create(...), return text content.
        raise NotImplementedError("claude_client.complete: implement SDK call")

    def complete_json(self, **kwargs) -> dict:
        """`complete` followed by a strict JSON parse of the response."""
        return json.loads(self.complete(**kwargs))
