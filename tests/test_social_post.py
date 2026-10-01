"""`social-post`: which papers are announced, and that each is announced once."""
import dataclasses
import json
from argparse import Namespace
from datetime import datetime, timedelta, timezone

import pytest

from src import main, social_client as sc
from src.feed_client import _item_to_paper
from src.main import social_queue, social_queued


def _paper(key: str, **extra):
    return _item_to_paper({
        "id": f"bibtex:{key}",
        "title": f"Paper {key}",
        "authors": [{"name": "Ada Lovelace"}],
        "date_published": "2026-01-01T00:00:00Z",
        "_academic": {"doi": f"10.1/{key}"},
        **extra,
    })


def _ago(days: float) -> str:
    return (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()


def _entry(days: float = 0, **extra) -> dict:
    return {"social_pending": True, "last_processed": _ago(days), **extra}


# --- queueing --------------------------------------------------------------


def test_a_classic_is_never_queued():
    assert social_queued(_paper("A2026-aa")) is True
    assert social_queued(_paper("B1990-bb", _classic=True)) is False


def test_cmd_update_queues_new_papers():
    """Asserted on the source, like test_classics_digest: the flag must be set
    where a new entry is built, or nothing is ever announced."""
    import inspect
    assert '"social_pending": social_queued(paper)' in inspect.getsource(main.cmd_update)


def test_only_pending_live_recent_papers_are_announced():
    papers = [_paper(k) for k in ("New", "Backlog", "Retracted", "Stub", "Old")]
    papers.append(_paper("Classic", _classic=True))
    state = {"papers": {
        "bibtex:New": _entry(),
        "bibtex:Backlog": {"last_processed": _ago(1)},        # predates the flag
        "bibtex:Retracted": _entry(retracted=True),
        "bibtex:Stub": _entry(superseded_by="New"),
        "bibtex:Old": _entry(days=30),
        "bibtex:Classic": _entry(),                            # moved to Classics later
    }}
    queue = social_queue(papers, state, max_age_days=14, limit=10)
    assert [p.bibtex_key for p, _ in queue] == ["New"]
    # The paper that waited too long leaves the queue for good.
    assert "social_pending" not in state["papers"]["bibtex:Old"]


def test_the_queue_is_oldest_first_and_capped():
    papers = [_paper(k) for k in ("A", "B", "C", "D")]
    state = {"papers": {
        "bibtex:A": _entry(1), "bibtex:B": _entry(4),
        "bibtex:C": _entry(2), "bibtex:D": _entry(3),
    }}
    queue = social_queue(papers, state, max_age_days=14, limit=3)
    assert [p.bibtex_key for p, _ in queue] == ["B", "D", "C"]


def test_a_key_selects_one_paper_even_from_the_backlog():
    papers = [_paper("A"), _paper("B")]
    state = {"papers": {"bibtex:A": _entry(), "bibtex:B": {"last_processed": _ago(90)}}}
    queue = social_queue(papers, state, max_age_days=14, limit=3, key="B")
    assert [p.bibtex_key for p, _ in queue] == ["B"]


def test_a_dry_run_previews_each_paper_once_and_expires_nothing():
    papers = [_paper("A"), _paper("B"), _paper("Old")]
    state = {"papers": {
        "bibtex:A": _entry(social_previewed=True),
        "bibtex:B": _entry(),
        "bibtex:Old": _entry(days=30),
    }}
    queue = social_queue(papers, state, max_age_days=14, limit=3, dry_run=True)
    assert [p.bibtex_key for p, _ in queue] == ["B"]
    assert state["papers"]["bibtex:Old"]["social_pending"] is True


# --- the command -------------------------------------------------------------


class Harness:
    """A throwaway project (state + summaries on disk) with stubbed platforms."""

    def __init__(self, tmp_path, monkeypatch, papers, entries, dry_run=False,
                 tokens=("MASTODON_ACCESS_TOKEN", "THREADS_ACCESS_TOKEN")):
        self.state_file = tmp_path / "state.json"
        self.state_file.write_text(json.dumps({"papers": entries}))
        summaries = tmp_path / "summaries"
        summaries.mkdir()
        for paper in papers:
            (summaries / f"{paper.bibtex_key}.json").write_text(
                json.dumps({"abstract": f"About {paper.bibtex_key}. More."})
            )
        self.cfg = {
            "paths": {"state_file": str(self.state_file),
                      "summaries_dir": str(summaries)},
            "slack": {"note_base_url": "https://example.org/Papers"},
            "social": {
                "enabled": True, "dry_run": dry_run, "hashtag": "#toread",
                "max_per_run": 3, "max_age_days": 14,
                "platforms": {"mastodon": {"enabled": True,
                                           "instance": "https://m.example"},
                              "threads": {"enabled": True},
                              "linkedin": {"enabled": True}},
            },
        }
        self.posts: list[tuple[str, str, list[str]]] = []
        self.fail: dict[str, Exception] = {}
        self.ops: list[str] = []

        for var in ("MASTODON_ACCESS_TOKEN", "THREADS_ACCESS_TOKEN",
                    "LINKEDIN_ACCESS_TOKEN", "LINKEDIN_PERSON_URN",
                    "THREADS_TOKEN_EXPIRES", "LINKEDIN_TOKEN_EXPIRES"):
            monkeypatch.delenv(var, raising=False)
        for var in tokens:
            monkeypatch.setenv(var, "tok")
        monkeypatch.setenv("SLACK_BOT_TOKEN", "xoxb")
        monkeypatch.setenv("OPS_SLACK_CHANNEL", "C-OPS")

        def poster(name):
            def post(texts, *, key, **_):
                if name in self.fail:
                    raise self.fail[name]
                self.posts.append((name, key, texts))
                return f"https://{name}.example/{key}"
            return post

        monkeypatch.setattr(sc, "PLATFORMS", {
            name: dataclasses.replace(p, post=poster(name))
            for name, p in sc.PLATFORMS.items()
        })
        monkeypatch.setattr(sc, "mastodon_limit", lambda instance: 500)
        monkeypatch.setattr(sc, "note_is_live", lambda url: True)
        monkeypatch.setattr(main, "_fetch_feed", lambda cfg: papers)
        monkeypatch.setattr(main, "_claude", self._no_claude)
        from src import slack_client
        monkeypatch.setattr(
            slack_client, "post_ops",
            lambda token, channel, text: self.ops.append(text) or True,
        )

    @staticmethod
    def _no_claude(cfg):
        raise RuntimeError("no credentials in tests")

    def run(self, **args) -> int:
        return main.cmd_social_post(
            self.cfg, Namespace(dry_run=False, key=None, **args)
        )

    @property
    def papers(self) -> dict:
        return json.loads(self.state_file.read_text())["papers"]


@pytest.fixture
def harness(tmp_path, monkeypatch):
    def build(papers, entries, **kwargs):
        return Harness(tmp_path, monkeypatch, papers, entries, **kwargs)
    return build


def test_a_new_paper_is_posted_to_every_platform_with_a_token(harness):
    h = harness([_paper("A")], {"bibtex:A": _entry()})
    assert h.run() == 0

    assert [(name, key) for name, key, _ in h.posts] == [
        ("mastodon", "A"), ("threads", "A"),      # linkedin has no token
    ]
    assert h.posts[0][2] == [
        "Lovelace, A. (2026). Paper A. https://doi.org/10.1/A\n\n"
        "Note: https://example.org/Papers/A\n#toread"
    ]

    entry = h.papers["bibtex:A"]
    assert entry["social"]["mastodon"]["url"] == "https://mastodon.example/A"
    assert entry["social"]["threads"]["url"] == "https://threads.example/A"
    assert "social_pending" not in entry and "social_blurb" not in entry


def test_only_linkedin_opens_with_a_description(harness):
    h = harness([_paper("A")], {"bibtex:A": _entry()},
                tokens=("MASTODON_ACCESS_TOKEN", "LINKEDIN_ACCESS_TOKEN"))
    h.run()
    texts = {name: parts[0] for name, _, parts in h.posts}
    assert texts["linkedin"].startswith("About A. More.\n\nLovelace, A. (2026).")
    assert texts["mastodon"].startswith("Lovelace, A. (2026).")


def test_no_description_is_written_when_no_platform_shows_one(harness, monkeypatch):
    h = harness([_paper("A")], {"bibtex:A": _entry()})    # mastodon + threads
    monkeypatch.setattr(sc, "social_description",
                        lambda *a, **k: pytest.fail("no platform uses it"))
    h.run()
    assert len(h.posts) == 2
    assert "social_blurb" not in h.papers["bibtex:A"]


def test_a_paper_without_a_summary_is_still_announced(harness):
    h = harness([_paper("A")], {"bibtex:A": _entry()},
                tokens=("LINKEDIN_ACCESS_TOKEN",))
    for f in (h.state_file.parent / "summaries").iterdir():
        f.unlink()
    h.run()
    (post,) = h.posts
    assert post[2][0].startswith("Lovelace, A. (2026).")


def test_a_second_run_posts_nothing(harness):
    h = harness([_paper("A")], {"bibtex:A": _entry()})
    h.run()
    h.posts.clear()
    h.run()
    assert h.posts == []


def test_backlog_is_never_posted(harness):
    h = harness([_paper("A")], {"bibtex:A": {"last_processed": _ago(1)}})
    h.run()
    assert h.posts == []


def test_a_rejected_token_leaves_the_paper_pending_for_that_platform_only(harness):
    papers = [_paper("A"), _paper("B")]
    h = harness(papers, {"bibtex:A": _entry(2), "bibtex:B": _entry(1)})
    h.fail["threads"] = sc.SocialAuthError("threads returned 400: expired")
    assert h.run() == 0

    assert [(n, k) for n, k, _ in h.posts] == [("mastodon", "A"), ("mastodon", "B")]
    entry = h.papers["bibtex:A"]
    assert "mastodon" in entry["social"] and "threads" not in entry["social"]
    assert entry["social_pending"] is True
    # One alert for the platform, not one per paper.
    assert len(h.ops) == 1 and "THREADS_ACCESS_TOKEN" in h.ops[0]

    # Token re-minted: only the missing platform is posted, in the same words.
    del h.fail["threads"]
    h.posts.clear()
    h.run()
    assert [(n, k) for n, k, _ in h.posts] == [("threads", "A"), ("threads", "B")]
    assert "social_pending" not in h.papers["bibtex:A"]


def test_a_half_published_thread_is_recorded_not_repeated(harness):
    h = harness([_paper("A")], {"bibtex:A": _entry()},
                tokens=("MASTODON_ACCESS_TOKEN",))
    h.fail["mastodon"] = sc.SocialError("reply failed", "https://m.example/1")
    h.run()
    assert h.papers["bibtex:A"]["social"]["mastodon"] == {
        "url": "https://m.example/1",
        "at": h.papers["bibtex:A"]["social"]["mastodon"]["at"],
        "incomplete": True,
    }
    del h.fail["mastodon"]
    h.run()
    assert h.posts == []


def test_a_note_that_is_not_live_waits_for_the_next_run(harness, monkeypatch):
    h = harness([_paper("A")], {"bibtex:A": _entry()})
    monkeypatch.setattr(sc, "note_is_live", lambda url: False)
    h.run()
    assert h.posts == []
    assert h.papers["bibtex:A"]["social_pending"] is True


def test_the_per_run_cap_holds(harness):
    keys = ["A", "B", "C", "D", "E"]
    h = harness([_paper(k) for k in keys],
                {f"bibtex:{k}": _entry(i) for i, k in enumerate(keys)},
                tokens=("MASTODON_ACCESS_TOKEN",))
    h.run()
    assert [k for _, k, _ in h.posts] == ["E", "D", "C"]


def test_a_dry_run_publishes_nothing_and_previews_once(harness):
    h = harness([_paper("A")], {"bibtex:A": _entry()}, dry_run=True)
    h.run()
    assert h.posts == []
    (preview,) = h.ops
    # Every platform switched on in config is previewed, token or not.
    assert all(name in preview for name in ("mastodon", "threads", "linkedin"))
    assert "Note: https://example.org/Papers/A" in preview
    entry = h.papers["bibtex:A"]
    assert entry["social_pending"] is True and entry["social_previewed"] is True

    h.run()
    assert len(h.ops) == 1

    # Going live posts the previewed paper, in the previewed words.
    h.cfg["social"]["dry_run"] = False
    h.run()
    assert [(n, k) for n, k, _ in h.posts] == [("mastodon", "A"), ("threads", "A")]
    assert "social_previewed" not in h.papers["bibtex:A"]


def test_a_config_dry_run_stays_silent_without_any_token(harness):
    """A fork that inherits the config block but holds no secrets."""
    h = harness([_paper("A")], {"bibtex:A": _entry()}, dry_run=True, tokens=())
    h.run()
    assert h.posts == [] and h.ops == []
    # ... while an explicit --dry-run always previews.
    main.cmd_social_post(h.cfg, Namespace(dry_run=True, key=None))
    assert len(h.ops) == 1


def test_disabled_in_config_does_nothing(harness):
    h = harness([_paper("A")], {"bibtex:A": _entry()})
    h.cfg["social"]["enabled"] = False
    h.run()
    assert h.posts == []
    del h.cfg["social"]
    h.run()
    assert h.posts == []


def test_an_expiring_token_is_announced_once_a_day(harness, monkeypatch):
    h = harness([], {})
    soon = (datetime.now(timezone.utc) + timedelta(days=3)).date().isoformat()
    monkeypatch.setenv("THREADS_TOKEN_EXPIRES", soon)
    h.run()
    h.run()
    assert len(h.ops) == 1
    assert "threads" in h.ops[0] and soon in h.ops[0]


def test_a_hand_picked_dry_run_leaves_no_trace_on_an_unqueued_paper(harness):
    h = harness([_paper("A")], {"bibtex:A": {"last_processed": _ago(40)}}, dry_run=True)
    main.cmd_social_post(h.cfg, Namespace(dry_run=False, key="A"))
    assert len(h.ops) == 1 and h.posts == []
    assert h.papers["bibtex:A"] == {"last_processed": h.papers["bibtex:A"]["last_processed"]}
