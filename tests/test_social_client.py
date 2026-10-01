"""Composing and publishing the social-media announcement of a new note."""
import pytest

from src import social_client as sc
from src.feed_client import _item_to_paper
from src.note_builder import build_apa_citation

NOTE = "https://fabiogiglietto.github.io/fg-zettelkasten/Papers/Vosoughi2018-ab"
PAPER = _item_to_paper({
    "id": "bibtex:Vosoughi2018-ab",
    "title": "The spread of true and false news online",
    "authors": [{"name": "Soroush Vosoughi"}, {"name": "Deb Roy"},
                {"name": "Sinan Aral"}],
    "date_published": "2018-03-09T00:00:00Z",
    "tags": ["Science", "Article"],
    "_academic": {"doi": "10.1126/science.aap9559", "volume": "359",
                  "pages": "1146--1151"},
})
CITATION = sc.apa_plain(PAPER)
BLURB = ("False news spreads farther, faster and more broadly than the truth "
         "on Twitter, and people rather than bots drive the difference.")


class FakeResponse:
    def __init__(self, status=200, payload=None, headers=None, text=""):
        self.status_code = status
        self._payload = payload
        self.headers = headers or {}
        self.text = text or str(payload)

    def json(self):
        if self._payload is None:
            raise ValueError("no json")
        return self._payload


@pytest.fixture
def calls(monkeypatch):
    """Record every outgoing request; answer from a queue of responses."""
    class Log(list):
        queue: list

    log = Log()
    log.queue = []

    def fake_request(method, url, timeout=None, **kwargs):
        log.append({"method": method, "url": url, **kwargs})
        return log.queue.pop(0)

    monkeypatch.setattr(sc.requests, "request", fake_request)
    return log


# --- text ------------------------------------------------------------------


def test_plain_citation_is_the_note_citation_without_markdown():
    assert "*" not in CITATION
    assert CITATION == build_apa_citation(PAPER).replace("*", "")
    assert CITATION.startswith("Vosoughi, S., Roy, D., & Aral, S. (2018).")
    assert CITATION.endswith("https://doi.org/10.1126/science.aap9559")


def test_mastodon_counts_every_url_as_23_characters():
    text = f"read {NOTE} and https://doi.org/10.1/x"
    assert sc.mastodon_len(text) == len("read  and ") + 2 * 23


def test_threads_weighs_emoji_by_their_bytes():
    assert sc.threads_len("abc") == 3
    assert sc.threads_len("é–") == 2          # ordinary non-ASCII is one each
    assert sc.threads_len("🎧") == 4


def test_a_post_that_fits_is_a_single_post_with_every_part():
    (post,) = sc.compose(BLURB, CITATION, NOTE, "#toread", 500, sc.threads_len)
    assert sc.threads_len(post) <= 500
    assert post.startswith(BLURB)
    assert CITATION in post
    assert f"Note: {NOTE}" in post
    assert post.endswith("#toread")


def test_the_blurb_gives_way_to_the_citation_at_a_word_boundary():
    long_blurb = " ".join(["polarization"] * 40)
    (post,) = sc.compose(long_blurb, CITATION, NOTE, "#toread", 500, sc.threads_len)
    assert sc.threads_len(post) <= 500
    assert CITATION in post                      # never shortened
    blurb = post.split("\n\n")[0]
    assert blurb.endswith("…")
    assert blurb[:-1].split()[-1] == "polarization"   # no word cut in half


def test_a_long_citation_moves_to_a_reply():
    citation = ("Author, A., " * 30) + "(2026). A title. https://doi.org/10.1/x"
    head, reply = sc.compose(BLURB, citation, NOTE, "#toread", 500, sc.threads_len)
    assert head.startswith(BLURB) and NOTE in head and head.endswith("#toread")
    assert reply == citation
    assert sc.threads_len(head) <= 500 and sc.threads_len(reply) <= 500


def test_a_citation_longer_than_a_post_keeps_its_doi():
    citation = ("Author, A., " * 60) + "(2026). A title. https://doi.org/10.1/x"
    _, reply = sc.compose(BLURB, citation, NOTE, "#toread", 500, sc.threads_len)
    assert sc.threads_len(reply) <= 500
    assert reply.endswith("… https://doi.org/10.1/x")


def test_mastodon_budget_uses_its_own_url_arithmetic():
    """The same content can need a reply on Threads and fit on Mastodon,
    where the two long URLs only cost 23 characters each."""
    citation = ("Author, A., " * 26) + "(2026). A title. https://doi.org/10.1126/science.aap9559"
    assert len(sc.compose(BLURB, citation, NOTE, "#toread", 500, sc.threads_len)) == 2
    (post,) = sc.compose(BLURB, citation, NOTE, "#toread", 500, sc.mastodon_len)
    assert sc.mastodon_len(post) <= 500


def test_model_text_cannot_smuggle_links_or_extra_hashtags():
    (post,) = sc.compose(
        "Great #misinformation study\nsee https://evil.example/x now",
        CITATION, NOTE, "#toread", 3000,
    )
    blurb = post.split("\n\n")[0]
    assert blurb == "Great misinformation study see now"
    assert post.count("#") == 1


def test_linkedin_gets_the_long_blurb_and_the_others_the_short_one():
    blurb = {"short": "Short one.", "long": "A longer one. With two sentences."}
    assert sc.platform_texts("linkedin", blurb, CITATION, NOTE, "#toread")[0] \
        .startswith("A longer one.")
    assert sc.platform_texts("mastodon", blurb, CITATION, NOTE, "#toread")[0] \
        .startswith("Short one.")


# --- blurb -------------------------------------------------------------------


SUMMARY = {
    "abstract": "False news spreads faster than true news. Humans, not bots, "
                "are responsible.",
    "findings": ["Falsehood diffused farther than the truth."],
}


class FakeClaude:
    assign_model = "haiku"

    def __init__(self, reply):
        self.reply, self.prompts = reply, []

    def complete_json(self, **kwargs):
        self.prompts.append(kwargs)
        if isinstance(self.reply, Exception):
            raise self.reply
        return self.reply


def test_blurb_comes_from_the_model_and_is_sanitised():
    claude = FakeClaude({"short": "Finds X. #wow", "long": "Finds X.\nIt matters."})
    blurb = sc.social_blurb(PAPER, SUMMARY, claude, "haiku")
    assert blurb == {"short": "Finds X. wow", "long": "Finds X. It matters."}
    assert claude.prompts[0]["model"] == "haiku"
    assert "Falsehood diffused farther" in claude.prompts[0]["prompt"]


def test_blurb_falls_back_to_the_abstract():
    expected = {
        "short": "False news spreads faster than true news.",
        "long": SUMMARY["abstract"],
    }
    assert sc.social_blurb(PAPER, SUMMARY, None, "") == expected
    assert sc.social_blurb(PAPER, SUMMARY, FakeClaude(RuntimeError("401")), "m") == expected
    assert sc.social_blurb(PAPER, SUMMARY, FakeClaude({"short": "", "long": ""}), "m") == expected


def test_the_short_blurb_is_sized_for_the_tightest_single_post():
    names = ["mastodon", "threads", "linkedin"]
    # A short citation leaves more room than the blurb ever takes.
    assert sc.short_budget(names, CITATION, NOTE, "#toread") == sc.SHORT_BLURB
    # A long one: Threads (URLs counted in full) is the tighter of the two.
    citation = ("Author, A., " * 22) + "(2026). A title. https://doi.org/10.1126/science.aap9559"
    frame = f"\n\n{citation}\n\nNote: {NOTE}\n#toread"
    assert sc.short_budget(names, citation, NOTE, "#toread") == 500 - sc.threads_len(frame)
    assert sc.short_budget(["mastodon"], citation, NOTE, "#toread") == 500 - sc.mastodon_len(frame)
    # Too long for one post: the citation goes to a reply, so no constraint.
    assert sc.short_budget(["threads"], "x" * 480, NOTE, "#toread") == sc.SHORT_BLURB


def test_the_model_is_told_the_limit_and_held_to_it():
    claude = FakeClaude({"short": "word " * 40, "long": "l"})
    blurb = sc.social_blurb(PAPER, SUMMARY, claude, "haiku", short_limit=90)
    assert 'Character limit for "short": 90' in claude.prompts[0]["prompt"]
    assert len(blurb["short"]) <= 90


def test_a_superseding_paper_is_introduced_as_now_published():
    claude = FakeClaude({"short": "s", "long": "l"})
    sc.social_blurb(PAPER, SUMMARY, claude, "haiku", supersedes=True)
    assert "now published" in claude.prompts[0]["prompt"]


# --- platforms -----------------------------------------------------------------


CFG = {"social": {"platforms": {
    "mastodon": {"enabled": True, "instance": "https://aoir.social"},
    "threads": {"enabled": True},
    "linkedin": {"enabled": False},
}}}


def test_a_platform_needs_both_the_config_switch_and_its_token():
    assert sc.enabled_platforms(CFG) == ["mastodon", "threads"]
    assert sc.active_platforms(CFG, {}) == []
    assert sc.active_platforms(CFG, {"MASTODON_ACCESS_TOKEN": "t"}) == ["mastodon"]
    # A token for a platform switched off in config changes nothing.
    assert sc.active_platforms(CFG, {"LINKEDIN_ACCESS_TOKEN": "t"}) == []


def test_linkedin_also_needs_its_author():
    cfg = {"social": {"platforms": {"linkedin": {"enabled": True}}}}
    assert sc.active_platforms(cfg, {"LINKEDIN_ACCESS_TOKEN": "t"}) == []
    assert sc.active_platforms(
        cfg, {"LINKEDIN_ACCESS_TOKEN": "t", "LINKEDIN_PERSON_URN": "abc"}
    ) == ["linkedin"]
    assert sc.linkedin_urn("abc") == "urn:li:person:abc"
    assert sc.linkedin_urn("urn:li:person:abc") == "urn:li:person:abc"


def test_mastodon_posts_a_thread_idempotently(calls):
    calls.queue += [
        FakeResponse(payload={"id": "1", "url": "https://aoir.social/@fg/1"}),
        FakeResponse(payload={"id": "2", "url": "https://aoir.social/@fg/2"}),
    ]
    url = sc.post_mastodon(["first", "second"], token="tok",
                           instance="https://aoir.social/", key="K1")
    assert url == "https://aoir.social/@fg/1"
    first, second = calls
    assert first["url"] == "https://aoir.social/api/v1/statuses"
    assert first["headers"] == {"Authorization": "Bearer tok",
                                "Idempotency-Key": "toread-K1-0"}
    assert first["data"]["status"] == "first"
    assert "in_reply_to_id" not in first["data"]
    assert second["data"]["in_reply_to_id"] == "1"
    assert second["headers"]["Idempotency-Key"] == "toread-K1-1"


def test_threads_creates_then_publishes_and_pins_the_note_card(calls):
    calls.queue += [
        FakeResponse(payload={"id": "c1"}),
        FakeResponse(payload={"id": "m1"}),
        FakeResponse(payload={"permalink": "https://www.threads.net/@fg/post/x"}),
        FakeResponse(payload={"id": "c2"}),
        FakeResponse(payload={"id": "m2"}),
    ]
    url = sc.post_threads(["first", "second"], token="tok", note_url=NOTE,
                          publish_wait=0)
    assert url == "https://www.threads.net/@fg/post/x"
    create, publish, _, reply, _ = calls
    assert create["url"] == f"{sc.THREADS_API}/me/threads"
    assert create["data"] == {"media_type": "TEXT", "text": "first",
                              "access_token": "tok", "link_attachment": NOTE}
    assert publish["url"] == f"{sc.THREADS_API}/me/threads_publish"
    assert publish["data"]["creation_id"] == "c1"
    assert reply["data"]["reply_to_id"] == "m1"
    assert "link_attachment" not in reply["data"]


def test_linkedin_shares_the_note_as_an_article(calls):
    calls.queue.append(FakeResponse(201, {}, {"x-restli-id": "urn:li:share:9"}))
    url = sc.post_linkedin(["the text"], token="tok", author="abc",
                           note_url=NOTE, title=PAPER.title)
    assert url == "https://www.linkedin.com/feed/update/urn:li:share:9/"
    (call,) = calls
    assert call["url"] == sc.LINKEDIN_UGC
    assert call["headers"]["X-Restli-Protocol-Version"] == "2.0.0"
    body = call["json"]
    assert body["author"] == "urn:li:person:abc"
    share = body["specificContent"]["com.linkedin.ugc.ShareContent"]
    assert share["shareCommentary"]["text"] == "the text"
    assert share["media"][0]["originalUrl"] == NOTE
    assert body["visibility"] == {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}


def test_a_rejected_token_is_an_auth_error(calls):
    calls.queue.append(FakeResponse(401, {"error": "invalid token"}))
    with pytest.raises(sc.SocialAuthError):
        sc.post_mastodon(["x"], token="t", instance="https://aoir.social", key="K")


def test_threads_reports_an_expired_token_as_code_190(calls):
    calls.queue.append(FakeResponse(400, {"error": {"code": 190, "message": "expired"}}))
    with pytest.raises(sc.SocialAuthError):
        sc.post_threads(["x"], token="t", note_url=NOTE, publish_wait=0)


def test_a_failed_reply_reports_the_post_already_published(calls):
    calls.queue += [
        FakeResponse(payload={"id": "1", "url": "https://aoir.social/@fg/1"}),
        FakeResponse(500, {"error": "boom"}),
    ]
    with pytest.raises(sc.SocialError) as err:
        sc.post_mastodon(["a", "b"], token="t", instance="https://aoir.social", key="K")
    assert not isinstance(err.value, sc.SocialAuthError)
    assert err.value.first_url == "https://aoir.social/@fg/1"
