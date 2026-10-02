"""Announce a newly-added paper note on Mastodon, Threads and LinkedIn.

Each post carries the paper's APA-7 citation, the link to its note on the
published site and a hashtag. Where there is room — LinkedIn — it opens with
a brief description, the only LLM-written part (`social_description`, a cheap
classification-tier call). Mastodon and Threads get none: next to a full
citation their 500 characters leave a sentence too little room, and a model
cannot be held to a character count, so it kept arriving clipped.

Access tokens are secrets, read from the environment by the caller; a platform
with no token is simply inactive. Nothing here raises past `SocialError`: a
failed post must never break the vault build.
"""
from __future__ import annotations

import os
import re
import time
from dataclasses import dataclass
from typing import Callable, Optional

import requests

from .note_builder import build_apa_citation

_TIMEOUT = 30
_URL_RE = re.compile(r"https?://\S+")
_HASHTAG_RE = re.compile(r"(?<!\w)#\w+")

# The description's length: what the model is asked for, and the hard cap
# applied afterwards (on sentence boundaries).
DESCRIPTION_TARGET = 450
DESCRIPTION_MAX = 700

MASTODON_URL_LEN = 23       # Mastodon counts every URL as 23 characters
THREADS_API = "https://graph.threads.net/v1.0"
# "Invalid Link Attachment": Threads could not validate the URL given as
# `link_attachment`. Seen on every brand-new note — the page answers 200 to
# us, but Threads' own fetch of a minutes-old GitHub Pages URL fails.
THREADS_INVALID_LINK = 4279047
LINKEDIN_UGC = "https://api.linkedin.com/v2/ugcPosts"
LINKEDIN_USERINFO = "https://api.linkedin.com/v2/userinfo"


class SocialError(Exception):
    """A post could not be published. `first_url` is set when the first post
    of a two-post thread went out before the failure — the caller must then
    treat the paper as announced, or the retry would duplicate that post."""

    def __init__(self, message: str, first_url: Optional[str] = None,
                 subcode: Optional[int] = None):
        super().__init__(message)
        self.first_url = first_url
        self.subcode = subcode      # the platform's own error code, if any


class SocialAuthError(SocialError):
    """The platform rejected the access token (expired, revoked, wrong scope).
    Retrying is pointless until a human re-mints it."""


# --- text ------------------------------------------------------------------


def apa_plain(paper) -> str:
    """The note's APA-7 citation as plain text.

    `build_apa_citation` marks journal and volume with markdown `*italics*`;
    none of the three platforms renders markdown, so the asterisks would show
    up literally.
    """
    return build_apa_citation(paper).replace("*", "")


def plain_len(text: str) -> int:
    return len(text)


def mastodon_len(text: str) -> int:
    """Length as Mastodon counts it: every URL is 23 characters."""
    urls = _URL_RE.findall(text)
    return len(text) - sum(len(u) for u in urls) + MASTODON_URL_LEN * len(urls)


def threads_len(text: str) -> int:
    """Length as Threads counts it: emoji weigh their UTF-8 byte length."""
    return sum(len(ch.encode("utf-8")) if ord(ch) > 0xFFFF else 1 for ch in text)


def _trim(text: str, budget: int) -> str:
    """Cut `text` to `budget` characters at a word boundary, with an ellipsis."""
    text = text.strip()
    if len(text) <= budget:
        return text
    if budget < 2:
        return ""
    cut = text[: budget - 1]
    if " " in cut:
        cut = cut.rsplit(" ", 1)[0]
    return cut.rstrip(" ,;:—–-") + "…"


def whole_sentences(text: str, budget: int) -> str:
    """As many leading sentences of `text` as fit in `budget` — never a part
    of one. Empty when even the first sentence is too long: a description cut
    mid-sentence reads worse than no description."""
    kept = ""
    for sentence in re.split(r"(?<=[.!?])\s+", text.strip()):
        candidate = f"{kept} {sentence}".strip()
        if len(candidate) > budget:
            break
        kept = candidate
    return kept


def _clean_description(text) -> str:
    """Model-written text with anything that would break the layout removed:
    URLs (they would steal the link preview), hashtags (the post carries
    exactly one) and line breaks."""
    text = _URL_RE.sub("", str(text or ""))
    text = _HASHTAG_RE.sub(lambda m: m.group(0)[1:], text)
    return re.sub(r"\s+", " ", text).strip().strip('"')


def _fit_citation(citation: str, limit: int, measure: Callable[[str], int]) -> str:
    """The citation, shortened only when it alone exceeds a post.

    The DOI link is what makes a citation actionable, so the cut is taken from
    the text in front of it.
    """
    if measure(citation) <= limit:
        return citation
    match = re.search(r"\s(https?://\S+)$", citation)
    if not match:
        return _trim(citation, limit)
    doi = match.group(1)
    head = citation[: match.start()]
    budget = limit - measure(f" {doi}")
    return f"{_trim(head, budget)} {doi}"


def compose(
    description: str,
    citation: str,
    note_url: str,
    hashtag: str,
    limit: int,
    measure: Callable[[str], int] = plain_len,
) -> list[str]:
    """The post text(s) for one paper on one platform:

        <description>          (only where the platform has room for one)

        <APA-7 citation>

        Note: <note_url>
        #toread

    The citation is never shortened to make room. A description is kept only
    as whole sentences, and dropped when not even its first one fits. If the
    citation, note link and hashtag do not fit one post together, the note
    link and hashtag follow in a reply.
    """
    tail = f"Note: {note_url}\n{hashtag}"
    body = f"{citation}\n\n{tail}"
    if measure(body) > limit:
        return [_fit_citation(citation, limit, measure), tail]
    description = whole_sentences(
        _clean_description(description), limit - measure(f"\n\n{body}")
    )
    return [f"{description}\n\n{body}" if description else body]


# --- description (LLM) -------------------------------------------------------


_DESCRIPTION_SYSTEM = f"""\
You write the short description that accompanies an academic paper when a \
researcher shares it from his reading list on LinkedIn. The post already \
carries the full citation and a link, so do not repeat the title, the authors \
or the journal.

Say what the paper finds or argues and why it matters, in plain, precise \
English. Describe the paper in the third person ("The study shows…", "Finds \
that…"); never write as the paper's author and never address the reader. No \
hype, no questions, no emojis, no hashtags, no URLs. State only what the \
summary supports — never add a finding, a number or a claim that is not in it.

Write two or three complete sentences, about {DESCRIPTION_TARGET} characters \
in all. Return only those sentences — no preamble, no quotation marks."""


def fallback_description(summary: dict) -> str:
    """A description taken from the cached summary, for when Claude is
    unavailable."""
    abstract = re.sub(r"\s+", " ", str(summary.get("abstract") or "")).strip()
    return whole_sentences(abstract, DESCRIPTION_MAX)


def social_description(
    paper, summary: dict, claude, model: str, supersedes: bool = False
) -> str:
    """A two-or-three-sentence description of one paper, from its summary.

    Falls back to the summary's own abstract when the model is unavailable or
    returns something unusable — a post must never be held up by the one
    optional LLM call in this module.
    """
    fallback = fallback_description(summary)
    if claude is None:
        return fallback

    lines = [f"Title: {paper.title}"]
    if supersedes:
        lines.append(
            "Note: this is the newly published version of a working paper "
            "shared earlier — say that it is now published."
        )
    for label, key in (
        ("Overview", "abstract"),
        ("Findings", "findings"),
        ("Contributions", "contributions"),
    ):
        value = summary.get(key)
        if isinstance(value, list):
            value = "\n".join(f"- {v}" for v in value if v)
        if value:
            lines.append(f"{label}:\n{value}")
    try:
        reply = claude.complete(
            model=model,
            system=_DESCRIPTION_SYSTEM,
            prompt="\n\n".join(lines),
            max_tokens=600,
        )
    except Exception as exc:  # noqa: BLE001 - the fallback is always usable
        print(f"  social: description call failed for {paper.bibtex_key} ({exc})")
        return fallback
    # The model is not a reliable character counter, so the cap is applied
    # here — on sentence boundaries, never inside one.
    return whole_sentences(_clean_description(reply), DESCRIPTION_MAX) or fallback


# --- posters ---------------------------------------------------------------


def _check(resp, platform: str, first_url: Optional[str] = None) -> None:
    """Raise the right `SocialError` for a non-2xx response."""
    if resp.status_code // 100 == 2:
        return
    detail = resp.text[:300]
    auth = resp.status_code in (401, 403)
    # Threads (Graph API) reports an expired or revoked token as HTTP 400 with
    # OAuthException code 190, not as a 401. (Mastodon's `error` is a string.)
    try:
        error = resp.json().get("error")
    except (ValueError, AttributeError):
        error = None
    subcode = None
    if isinstance(error, dict):
        auth = auth or error.get("code") == 190
        subcode = error.get("error_subcode")
    cls = SocialAuthError if auth else SocialError
    raise cls(f"{platform} returned {resp.status_code}: {detail}", first_url,
              subcode)


def _request(method: str, url: str, platform: str,
             first_url: Optional[str] = None, **kwargs):
    try:
        resp = requests.request(method, url, timeout=_TIMEOUT, **kwargs)
    except requests.RequestException as exc:
        raise SocialError(f"{platform} request failed: {exc}", first_url) from exc
    _check(resp, platform, first_url)
    return resp


def mastodon_limit(instance: str, default: int = 500) -> int:
    """The instance's own status length limit (it is configurable per server)."""
    try:
        resp = requests.get(f"{instance.rstrip('/')}/api/v2/instance", timeout=15)
        return int(resp.json()["configuration"]["statuses"]["max_characters"])
    except (requests.RequestException, ValueError, KeyError, TypeError):
        return default


def post_mastodon(texts: list[str], *, token: str, instance: str,
                  key: str, **_) -> str:
    """Publish the post (and its reply, if any); return the first post's URL."""
    first_url = reply_to = None
    for i, text in enumerate(texts):
        data = {"status": text, "visibility": "public", "language": "en"}
        if reply_to:
            data["in_reply_to_id"] = reply_to
        resp = _request(
            "POST", f"{instance.rstrip('/')}/api/v1/statuses", "mastodon",
            first_url,
            headers={
                "Authorization": f"Bearer {token}",
                # Honoured for an hour: a retry after a lost response returns
                # the status already created instead of posting it twice.
                "Idempotency-Key": f"toread-{key}-{i}",
            },
            data=data,
        )
        status = resp.json()
        reply_to = status["id"]
        first_url = first_url or status.get("url") or status.get("uri")
    return first_url


def post_threads(texts: list[str], *, token: str, note_url: str,
                 user_id: str = "me", publish_wait: float = 5.0, **_) -> str:
    """Publish on Threads: each post is a container that is then published."""
    first_url = reply_to = None

    def publish(data: dict) -> str:
        container = _request(
            "POST", f"{THREADS_API}/{user_id}/threads", "threads", first_url,
            data=data,
        ).json()["id"]
        # A container is not publishable the instant it is created.
        time.sleep(publish_wait)
        return _request(
            "POST", f"{THREADS_API}/{user_id}/threads_publish", "threads",
            first_url, data={"creation_id": container, "access_token": token},
        ).json()["id"]

    for text in texts:
        data = {"media_type": "TEXT", "text": text, "access_token": token}
        if reply_to:
            data["reply_to_id"] = reply_to
        else:
            # Pin the link card to the note; otherwise Threads previews the
            # first URL in the text, which may be the DOI.
            data["link_attachment"] = note_url
        try:
            media_id = publish(data)
        except SocialError as exc:
            if exc.subcode != THREADS_INVALID_LINK or "link_attachment" not in data:
                raise
            # Threads cannot validate a brand-new note's URL yet. Post without
            # the pinned card rather than a day late: the text still carries
            # the note link.
            print("  social: threads rejected the note link card — "
                  "posting without it")
            media_id = publish(
                {k: v for k, v in data.items() if k != "link_attachment"}
            )
        if first_url is None:
            first_url = f"threads:{media_id}"
            try:
                first_url = _request(
                    "GET", f"{THREADS_API}/{media_id}", "threads",
                    params={"fields": "permalink", "access_token": token},
                ).json().get("permalink") or first_url
            except SocialError:
                pass  # published; only the permalink lookup failed
        reply_to = media_id
    return first_url


def linkedin_urn(value: str) -> str:
    """`urn:li:person:<id>` from either the full URN or the bare member id."""
    value = value.strip()
    return value if value.startswith("urn:li:") else f"urn:li:person:{value}"


def linkedin_author(token: str) -> str:
    """The member URN the token belongs to, from the OpenID userinfo endpoint.

    Saves a second secret: the token (scopes `openid profile`) already says
    whose it is, and a share must name that same member as its author.
    """
    resp = _request(
        "GET", LINKEDIN_USERINFO, "linkedin",
        headers={"Authorization": f"Bearer {token}"},
    )
    return linkedin_urn(resp.json()["sub"])


def post_linkedin(texts: list[str], *, token: str, note_url: str, title: str,
                  author: str = "", **_) -> str:
    """Publish one LinkedIn share with the note as its article card.

    LinkedIn's 3000-character limit always fits a whole post, so a two-part
    text is simply joined. `author` (LINKEDIN_PERSON_URN) is optional — left
    empty, it is resolved from the token.
    """
    body = {
        "author": linkedin_urn(author) if author else linkedin_author(token),
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": "\n\n".join(texts)},
                "shareMediaCategory": "ARTICLE",
                "media": [{
                    "status": "READY",
                    "originalUrl": note_url,
                    "title": {"text": title[:200]},
                }],
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
    }
    resp = _request(
        "POST", LINKEDIN_UGC, "linkedin",
        headers={
            "Authorization": f"Bearer {token}",
            "X-Restli-Protocol-Version": "2.0.0",
        },
        json=body,
    )
    urn = resp.headers.get("x-restli-id") or resp.json().get("id", "")
    return f"https://www.linkedin.com/feed/update/{urn}/"


# --- platform registry -------------------------------------------------------


@dataclass(frozen=True)
class Platform:
    name: str
    token_env: str
    limit: int
    measure: Callable[[str], int]
    describe: bool                  # room for the LLM-written description?
    post: Callable[..., str]
    expires_env: Optional[str] = None   # ISO date the token expires, if it does


PLATFORMS: dict[str, Platform] = {
    "mastodon": Platform(
        "mastodon", "MASTODON_ACCESS_TOKEN", 500, mastodon_len, False,
        post_mastodon,
    ),
    "threads": Platform(
        "threads", "THREADS_ACCESS_TOKEN", 500, threads_len, False,
        post_threads, "THREADS_TOKEN_EXPIRES",
    ),
    "linkedin": Platform(
        "linkedin", "LINKEDIN_ACCESS_TOKEN", 3000, plain_len, True,
        post_linkedin, "LINKEDIN_TOKEN_EXPIRES",
    ),
}


def enabled_platforms(cfg: dict) -> list[str]:
    """Platforms switched on in config, in registry order."""
    wanted = cfg.get("social", {}).get("platforms") or {}
    return [
        name for name in PLATFORMS
        if (wanted.get(name) or {}).get("enabled")
    ]


def active_platforms(cfg: dict, env=None) -> list[str]:
    """Enabled platforms that also have their access token in the environment.

    Both conditions, like the Slack digest: a fork that inherits the config
    block but holds no secrets can never post.
    """
    env = os.environ if env is None else env
    return [n for n in enabled_platforms(cfg) if env.get(PLATFORMS[n].token_env)]


def platform_texts(name: str, description: str, citation: str, note_url: str,
                   hashtag: str, limit: Optional[int] = None) -> list[str]:
    """The post text(s) for one platform."""
    platform = PLATFORMS[name]
    return compose(
        description if platform.describe else "", citation, note_url, hashtag,
        limit or platform.limit, platform.measure,
    )


def note_is_live(url: str, tries: int = 3, wait: float = 20.0) -> bool:
    """True once the note's page answers 200 on the published site.

    The post links to the note and the platforms cache its preview, so posting
    before GitHub Pages has the page would pin a 404 card to the post.
    """
    for attempt in range(tries):
        try:
            if requests.get(url, timeout=15).status_code == 200:
                return True
        except requests.RequestException:
            pass
        if attempt < tries - 1:
            time.sleep(wait)
    return False
