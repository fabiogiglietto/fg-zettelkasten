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


def test_credential_source_detects_federation_without_api_key(monkeypatch):
    """Federation must be recognised when no API key is present.

    Guards the migration's sharpest edge: a bare ANTHROPIC_API_KEY check here
    would make every CI run a silent no-op while local runs kept working.
    """
    from src.claude_client import credential_source

    for var in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN"):
        monkeypatch.delenv(var, raising=False)
    for var in ("ANTHROPIC_FEDERATION_RULE_ID", "ANTHROPIC_ORGANIZATION_ID",
                "ANTHROPIC_SERVICE_ACCOUNT_ID", "ANTHROPIC_IDENTITY_TOKEN_FILE"):
        monkeypatch.setenv(var, "x")
    assert credential_source() == "federation"

    # A partial quartet is a misconfiguration, not a credential.
    monkeypatch.delenv("ANTHROPIC_SERVICE_ACCOUNT_ID")
    assert credential_source() is None

    # An API key still outranks federation, matching SDK precedence.
    monkeypatch.setenv("ANTHROPIC_SERVICE_ACCOUNT_ID", "x")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "k")
    assert credential_source() == "api-key"
