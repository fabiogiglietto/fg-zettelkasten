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


def test_a_post_without_description_is_citation_note_and_hashtag():
    (post,) = sc.compose("", CITATION, NOTE, "#toread", 500, sc.threads_len)
    assert post == f"{CITATION}\n\nNote: {NOTE}\n#toread"


def test_mastodon_and_threads_never_carry_a_description():
    """Decided after two live previews: next to a full citation, 500
    characters leave a sentence too little room and it kept arriving clipped."""
    for name in ("mastodon", "threads"):
        (post,) = sc.platform_texts(name, BLURB, CITATION, NOTE, "#toread")
        assert post.startswith(CITATION)
        assert BLURB not in post
    (post,) = sc.platform_texts("linkedin", BLURB, CITATION, NOTE, "#toread")
    assert post == f"{BLURB}\n\n{CITATION}\n\nNote: {NOTE}\n#toread"


def test_a_description_is_only_ever_whole_sentences():
    text = "First finding here. Second finding follows. Third one is long."
    assert sc.whole_sentences(text, 200) == text
    assert sc.whole_sentences(text, 45) == "First finding here. Second finding follows."
    assert sc.whole_sentences(text, 30) == "First finding here."
    assert sc.whole_sentences(text, 10) == ""        # never a clipped sentence

    room = len(CITATION) + len(NOTE) + 60
    (post,) = sc.compose(text, CITATION, NOTE, "#toread", room)
    assert post.startswith("First finding here.\n\n")
    assert "…" not in post


def test_a_citation_too_long_for_one_post_sends_the_link_in_a_reply():
    citation = ("Author, A., " * 38) + "(2026). A title. https://doi.org/10.1/x"
    head, reply = sc.compose("", citation, NOTE, "#toread", 500, sc.threads_len)
    assert head == citation
    assert reply == f"Note: {NOTE}\n#toread"
    assert sc.threads_len(head) <= 500


def test_a_citation_longer_than_a_post_keeps_its_doi():
    citation = ("Author, A., " * 60) + "(2026). A title. https://doi.org/10.1/x"
    head, _ = sc.compose("", citation, NOTE, "#toread", 500, sc.threads_len)
    assert sc.threads_len(head) <= 500
    assert head.endswith("… https://doi.org/10.1/x")


def test_mastodon_budget_uses_its_own_url_arithmetic():
    """The same citation can need a reply on Threads and fit on Mastodon,
    where the two long URLs only cost 23 characters each."""
    citation = ("Author, A., " * 31) + "(2026). A title. https://doi.org/10.1126/science.aap9559"
    assert len(sc.compose("", citation, NOTE, "#toread", 500, sc.threads_len)) == 2
    (post,) = sc.compose("", citation, NOTE, "#toread", 500, sc.mastodon_len)
    assert sc.mastodon_len(post) <= 500


def test_model_text_cannot_smuggle_links_or_extra_hashtags():
    (post,) = sc.compose(
        "Great #misinformation study\nsee https://evil.example/x now.",
        CITATION, NOTE, "#toread", 3000,
    )
    assert post.split("\n\n")[0] == "Great misinformation study see now."
    assert post.count("#") == 1


# --- description -----------------------------------------------------------


SUMMARY = {
    "abstract": "False news spreads faster than true news. Humans, not bots, "
                "are responsible.",
    "findings": ["Falsehood diffused farther than the truth."],
}


class FakeClaude:
    assign_model = "haiku"

    def __init__(self, reply):
        self.reply, self.prompts = reply, []

    def complete(self, **kwargs):
        self.prompts.append(kwargs)
        if isinstance(self.reply, Exception):
            raise self.reply
        return self.reply


def test_description_comes_from_the_model_and_is_sanitised():
    claude = FakeClaude('"Finds X. #wow\nIt matters."')
    assert sc.social_description(PAPER, SUMMARY, claude, "haiku") \
        == "Finds X. wow It matters."
    assert claude.prompts[0]["model"] == "haiku"
    assert "Falsehood diffused farther" in claude.prompts[0]["prompt"]


def test_an_overlong_description_loses_its_last_sentence_not_half_of_it():
    """The second live preview: the model ran past the cap and the LinkedIn
    description ended in "…resonates…"."""
    sentence = "This sentence is exactly as long as it needs to be for the test. "
    claude = FakeClaude(sentence * 20)
    text = sc.social_description(PAPER, SUMMARY, claude, "haiku")
    assert len(text) <= sc.DESCRIPTION_MAX
    assert text.endswith("for the test.") and "…" not in text


def test_description_falls_back_to_the_abstract():
    assert sc.social_description(PAPER, SUMMARY, None, "") == SUMMARY["abstract"]
    assert sc.social_description(PAPER, SUMMARY, FakeClaude(RuntimeError("401")), "m") \
        == SUMMARY["abstract"]
    assert sc.social_description(PAPER, SUMMARY, FakeClaude("  "), "m") == SUMMARY["abstract"]


def test_a_superseding_paper_is_introduced_as_now_published():
    claude = FakeClaude("s.")
    sc.social_description(PAPER, SUMMARY, claude, "haiku", supersedes=True)
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


def test_linkedin_author_is_resolved_from_the_token_when_not_given(calls):
    calls.queue += [
        FakeResponse(payload={"sub": "abc"}),
        FakeResponse(201, {}, {"x-restli-id": "urn:li:share:9"}),
    ]
    sc.post_linkedin(["the text"], token="tok", note_url=NOTE, title="T")
    userinfo, share = calls
    assert userinfo["url"] == sc.LINKEDIN_USERINFO
    assert userinfo["headers"] == {"Authorization": "Bearer tok"}
    assert share["json"]["author"] == "urn:li:person:abc"
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


INVALID_LINK = {"error": {"message": "Fatal", "type": "OAuthException",
                          "code": -1, "error_subcode": 4279047,
                          "error_user_title": "Invalid Link Attachment"}}


@pytest.mark.parametrize("rejected_at", ["create", "publish"])
def test_threads_posts_without_the_card_when_the_note_link_is_rejected(calls, rejected_at):
    """Every brand-new note hit this on 2026-10-01/02: Threads could not
    validate the minutes-old page as a link attachment, so the post waited a
    day for the next run."""
    if rejected_at == "publish":
        calls.queue.append(FakeResponse(payload={"id": "c0"}))
    calls.queue += [
        FakeResponse(400, INVALID_LINK),
        FakeResponse(payload={"id": "c1"}),
        FakeResponse(payload={"id": "m1"}),
        FakeResponse(payload={"permalink": "https://www.threads.com/@fg/post/x"}),
    ]
    url = sc.post_threads(["the text"], token="tok", note_url=NOTE, publish_wait=0)
    assert url == "https://www.threads.com/@fg/post/x"
    creates = [c for c in calls if c["url"].endswith("/me/threads")]
    assert creates[0]["data"]["link_attachment"] == NOTE
    assert "link_attachment" not in creates[-1]["data"]
    assert creates[-1]["data"]["text"] == "the text"


def test_another_threads_error_is_not_retried(calls):
    calls.queue.append(FakeResponse(400, {"error": {"code": -1, "error_subcode": 123}}))
    with pytest.raises(sc.SocialError) as err:
        sc.post_threads(["x"], token="t", note_url=NOTE, publish_wait=0)
    assert err.value.subcode == 123 and len(calls) == 1


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
