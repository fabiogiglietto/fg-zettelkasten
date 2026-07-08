"""Tests for src.state incremental-work fingerprints (and the ClaudeClient
assign_model fallback they key on)."""
import pytest

from src.state import (
    assign_fingerprint,
    emergent_fingerprint,
    register_fingerprint,
    signals_hash,
    structure_fingerprint,
)
from src.themes import summary_digest

TOPIC_A = {"slug": "a", "name": "A", "description": "alpha"}
TOPIC_B = {"slug": "b", "name": "B", "description": "beta"}


def test_signals_hash_deterministic_and_order_independent():
    one = signals_hash({"x.yml": "foo", "y.yml": "bar"})
    two = signals_hash({"y.yml": "bar", "x.yml": "foo"})
    assert one == two
    assert one != signals_hash({"x.yml": "foo", "y.yml": "baz"})


def test_signals_hash_keys_and_values_do_not_collide():
    # path/text boundaries are delimited, so shifting a char across them differs
    assert signals_hash({"ab": "c"}) != signals_hash({"a": "bc"})


def test_register_fingerprint_order_independent():
    assert register_fingerprint([TOPIC_A, TOPIC_B]) == register_fingerprint(
        [TOPIC_B, TOPIC_A]
    )


def test_register_fingerprint_sensitive_to_description():
    changed = dict(TOPIC_A, description="alpha, reworded")
    assert register_fingerprint([TOPIC_A]) != register_fingerprint([changed])


def test_assign_fingerprint_changes_with_each_input():
    base = assign_fingerprint("regfp", "digest", "claude-haiku-4-5")
    assert base == assign_fingerprint("regfp", "digest", "claude-haiku-4-5")
    assert base != assign_fingerprint("other", "digest", "claude-haiku-4-5")
    assert base != assign_fingerprint("regfp", "other", "claude-haiku-4-5")
    assert base != assign_fingerprint("regfp", "digest", "claude-sonnet-5")


def test_emergent_fingerprint_order_independent_members():
    one = emergent_fingerprint("fp", ["k1", "k2"], "m")
    two = emergent_fingerprint("fp", ["k2", "k1"], "m")
    assert one == two
    assert one != emergent_fingerprint("fp", ["k1"], "m")


def test_structure_fingerprint_sensitive_to_membership_stable_otherwise():
    base = structure_fingerprint(TOPIC_A, ["k1", "k2"], "digests", "m")
    same = structure_fingerprint(dict(TOPIC_A), ["k2", "k1"], "digests", "m")
    assert base == same
    assert base != structure_fingerprint(TOPIC_A, ["k1"], "digests", "m")
    assert base != structure_fingerprint(TOPIC_A, ["k1", "k2"], "other", "m")
    renamed = dict(TOPIC_A, name="A renamed")
    assert base != structure_fingerprint(renamed, ["k1", "k2"], "digests", "m")


def test_summary_digest_shape():
    digest = summary_digest(
        {"abstract": "text", "key_claims": ["c1", "c2"], "pdf_source": "drive"}
    )
    assert "abstract: text" in digest
    assert "key_claims: c1; c2" in digest
    assert "pdf_source" not in digest


def test_claude_client_assign_model_falls_back_to_reasoning(monkeypatch):
    pytest.importorskip("anthropic")  # ClaudeClient lazily imports the SDK
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    from src.claude_client import ClaudeClient

    client = ClaudeClient(summary_model="s", reasoning_model="r")
    assert client.assign_model == "r"
    assert client.note_model == "r"
    client = ClaudeClient(summary_model="s", reasoning_model="r",
                          assign_model="a", note_model="n")
    assert client.assign_model == "a"
    assert client.note_model == "n"
