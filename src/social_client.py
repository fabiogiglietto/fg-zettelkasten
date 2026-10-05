"""Announce a newly-added paper note on Mastodon, Threads, LinkedIn and Bluesky.

Each post opens with the column's masthead — the hashtag and a line saying the
post is auto-posted — so the series is recognisable in a feed and is not
taken for hand-written. Then the paper's APA-7 citation and the link to its
note on the published site. Where there is room —
LinkedIn — a brief description precedes the citation, the only LLM-written
part of the post (`social_description`, a cheap classification-tier call).
Mastodon, Threads and Bluesky get none: next to a full citation their 300-500
characters leave a sentence too little room, and a model cannot be held to a
character count, so it kept arriving clipped.

Every post shows the note as its link card. Threads, LinkedIn and Bluesky are
handed the card; Mastodon builds one from the first link in the text, so there
the note link goes above the citation and its DOI. On Bluesky the card *is*
the note link: repeating it in 300 characters would push most citations into
a reply.

Access tokens are secrets, read from the environment by the caller; a platform
with no token is simply inactive. Nothing here raises past `SocialError`: a
failed post must never break the vault build.
"""
from __future__ import annotations

import os
import re
import time
from dataclasses import dataclass
from datetime import datetime, timezone
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
BLUESKY_SERVICE = "https://bsky.social"
BLUESKY_LIMIT = 300
# Bluesky lets a link show any text, so a URL is displayed without its scheme
# and, when the post would not fit otherwise, cut to this many characters —
# the only way a citation, with its DOI, and the note link fit in 300.
BLUESKY_LINK_LEN = 32
BLUESKY_BLOB_MAX = 1_000_000    # largest image a link card may carry
NOTE_LABEL = "Note"
_OG_IMAGE_RE = re.compile(
    r"""<meta[^>]+property=["']og:image["'][^>]+content=["']([^"']+)["']""",
    re.IGNORECASE,
)
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


def plain_text(text: str) -> str:
    return text


def mastodon_len(text: str) -> int:
    """Length as Mastodon counts it: every URL is 23 characters."""
    urls = _URL_RE.findall(text)
    return len(text) - sum(len(u) for u in urls) + MASTODON_URL_LEN * len(urls)


def threads_len(text: str) -> int:
    """Length as Threads counts it: emoji weigh their UTF-8 byte length."""
    return sum(len(ch.encode("utf-8")) if ord(ch) > 0xFFFF else 1 for ch in text)


def bluesky_link_text(url: str, short: bool = True) -> str:
    """How a URL is shown in a Bluesky post: no scheme and, in the short form,
    at most `BLUESKY_LINK_LEN` characters. The link itself stays whole."""
    shown = re.sub(r"^https?://", "", url)
    if not short or len(shown) <= BLUESKY_LINK_LEN:
        return shown
    return shown[: BLUESKY_LINK_LEN - 1] + "…"


def _bluesky_short(text: str) -> bool:
    """Whether a post needs its links in the short form to fit."""
    full = _URL_RE.sub(lambda m: bluesky_link_text(m.group(0), short=False), text)
    return len(full) > BLUESKY_LIMIT


def bluesky_display(text: str) -> str:
    """A post's text as Bluesky shows it: links without their scheme, in full
    when the post has the room and in the short form when it does not."""
    short = _bluesky_short(text)
    return _URL_RE.sub(lambda m: bluesky_link_text(m.group(0), short), text)


def bluesky_len(text: str) -> int:
    """Length as Bluesky counts it — of the shortest form the post can take,
    which is what decides whether it fits."""
    return len(_URL_RE.sub(lambda m: bluesky_link_text(m.group(0)), text))


def bluesky_richtext(text: str) -> tuple[str, list[dict]]:
    """The displayed text of a post and its facets (links and hashtags).

    Bluesky does not auto-link: a URL or hashtag is clickable only through a
    facet naming its byte range (UTF-8, end exclusive) in the text.
    """
    shown, facets, last = "", [], 0
    short = _bluesky_short(text)

    def span(start_text: str, piece: str) -> dict:
        start = len(start_text.encode("utf-8"))
        return {"byteStart": start, "byteEnd": start + len(piece.encode("utf-8"))}

    for match in _URL_RE.finditer(text):
        shown += text[last:match.start()]
        piece = bluesky_link_text(match.group(0), short)
        facets.append({
            "index": span(shown, piece),
            "features": [{"$type": "app.bsky.richtext.facet#link",
                          "uri": match.group(0)}],
        })
        shown += piece
        last = match.end()
    shown += text[last:]
    for match in _HASHTAG_RE.finditer(shown):
        facets.append({
            "index": span(shown[:match.start()], match.group(0)),
            "features": [{"$type": "app.bsky.richtext.facet#tag",
                          "tag": match.group(0)[1:]}],
        })
    return shown, sorted(facets, key=lambda f: f["index"]["byteStart"])


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


def _chunks(text: str, limit: int, measure: Callable[[str], int],
            lead: str = "") -> list[str]:
    """`text` split at word boundaries into parts that each fit one post.

    A part that is continued ends in "…" and its continuation starts with one,
    so nothing is lost and the break is visible. A URL is a single word here
    and is never broken. `lead` opens the first part and counts against it.
    """
    parts, current = [], ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        opening = "" if parts else lead
        if not current or measure(f"{opening}{candidate}…") <= limit:
            current = candidate
            continue
        parts.append(f"{opening}{current}…")
        current = f"…{word}"
    parts.append(f"{'' if parts else lead}{current}")
    return parts


def compose(
    description: str,
    citation: str,
    note_url: str,
    header: str,
    limit: int,
    measure: Callable[[str], int] = plain_len,
    note_label: str = NOTE_LABEL,
    note_link: str = "last",
) -> list[str]:
    """The post text(s) for one paper on one platform:

        #toread <masthead>     (`header`: the column's first line, always)

        <description>          (only where the platform has room for one)

        <APA-7 citation>

        <note_label>: <note_url>

    `note_link` places the link to the note: "last" as above; "first", between
    the header and the rest — for a platform that builds its link card from
    the first link in the text, which would otherwise be the citation's DOI;
    "card", not in the text at all — for a platform whose posts always carry
    the note as an attached card and have no characters to spare.

    The citation is never shortened. A description is kept only as whole
    sentences, and dropped when not even its first one fits. If the header,
    citation and note link do not fit one post together, the note link
    follows in a reply; a citation longer than a post (common in Bluesky's
    300 characters) continues there too. The header always opens the first
    post.
    """
    lead = f"{header}\n\n" if header else ""
    link = f"{note_label}: {note_url}"
    tail = f"\n\n{link}" if note_link == "last" else ""
    if note_link == "first":
        lead = f"{lead}{link}\n\n"
    if measure(f"{lead}{citation}{tail}") > limit:
        parts = _chunks(citation, limit, measure, lead)
        if not tail:
            return parts
        closing = f"{parts[-1]}{tail}"
        if len(parts) > 1 and measure(closing) <= limit:
            return [*parts[:-1], closing]
        return [*parts, link]
    description = whole_sentences(
        _clean_description(description),
        limit - measure(f"{lead}\n\n{citation}{tail}"),
    )
    body = f"{description}\n\n{citation}" if description else citation
    return [f"{lead}{body}{tail}"]


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


def _bluesky_thumb(service: str, jwt: str, image_url: str) -> Optional[dict]:
    """The note's social image, uploaded as the blob a link card shows.

    Bluesky does not fetch a card's picture itself: the client uploads it.
    None when anything goes wrong — a card without a picture is still a post.
    """
    try:
        image = _request("GET", image_url, "bluesky")
        if not image.content or len(image.content) > BLUESKY_BLOB_MAX:
            return None
        return _request(
            "POST", f"{service}/xrpc/com.atproto.repo.uploadBlob", "bluesky",
            headers={
                "Authorization": f"Bearer {jwt}",
                "Content-Type": image.headers.get("Content-Type") or "image/webp",
            },
            data=image.content,
        ).json()["blob"]
    except (SocialError, KeyError, ValueError, TypeError):
        print("  social: bluesky link card goes out without its image")
        return None


def post_bluesky(texts: list[str], *, token: str, handle: str, note_url: str,
                 title: str, site: str = "", image: str = "",
                 service: str = BLUESKY_SERVICE, **_) -> str:
    """Publish on Bluesky with an app password; return the first post's URL.

    The first post carries the note as its link card — with `image` (the
    note's social image) as its picture and `site` as the line under the
    title; any further text goes out as replies in the same thread.
    """
    if not handle:
        raise SocialError("bluesky needs social.platforms.bluesky.handle in config")
    service = service.rstrip("/")
    session = _request(
        "POST", f"{service}/xrpc/com.atproto.server.createSession", "bluesky",
        json={"identifier": handle, "password": token},
    ).json()
    card = {"uri": note_url, "title": title[:300], "description": site}
    thumb = _bluesky_thumb(service, session["accessJwt"], image) if image else None
    if thumb:
        card["thumb"] = thumb
    first_url = root = parent = None
    for text in texts:
        shown, facets = bluesky_richtext(text)
        record = {
            "$type": "app.bsky.feed.post",
            "text": shown,
            "createdAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "langs": ["en"],
            "facets": facets,
        }
        if root is None:
            record["embed"] = {"$type": "app.bsky.embed.external",
                               "external": card}
        else:
            record["reply"] = {"root": root, "parent": parent}
        ref = _request(
            "POST", f"{service}/xrpc/com.atproto.repo.createRecord", "bluesky",
            first_url,
            headers={"Authorization": f"Bearer {session['accessJwt']}"},
            json={"repo": session["did"], "collection": "app.bsky.feed.post",
                  "record": record},
        ).json()
        parent = {"uri": ref["uri"], "cid": ref["cid"]}
        root = root or parent
        first_url = first_url or (
            f"https://bsky.app/profile/{handle}/post/{ref['uri'].rsplit('/', 1)[-1]}"
        )
    return first_url


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
    # The text as the platform shows it, where that differs from what is sent.
    display: Callable[[str], str] = plain_text
    # Where the link to the note goes (see `compose`). "first" where the link
    # card is built from the first link in the text, which must then not be
    # the citation's DOI; "card" where the attached card is the only link.
    note_link: str = "last"


PLATFORMS: dict[str, Platform] = {
    "mastodon": Platform(
        "mastodon", "MASTODON_ACCESS_TOKEN", 500, mastodon_len, False,
        post_mastodon, note_link="first",
    ),
    "threads": Platform(
        "threads", "THREADS_ACCESS_TOKEN", 500, threads_len, False,
        post_threads, "THREADS_TOKEN_EXPIRES",
    ),
    "linkedin": Platform(
        "linkedin", "LINKEDIN_ACCESS_TOKEN", 3000, plain_len, True,
        post_linkedin, "LINKEDIN_TOKEN_EXPIRES",
    ),
    # An app password, not an OAuth token: it does not expire.
    "bluesky": Platform(
        "bluesky", "BLUESKY_APP_PASSWORD", BLUESKY_LIMIT, bluesky_len, False,
        post_bluesky, display=bluesky_display, note_link="card",
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
                   header: str, limit: Optional[int] = None,
                   note_label: str = NOTE_LABEL) -> list[str]:
    """The post text(s) for one platform."""
    platform = PLATFORMS[name]
    return compose(
        description if platform.describe else "", citation, note_url, header,
        limit or platform.limit, platform.measure, note_label,
        platform.note_link,
    )


def post_header(hashtag: str, masthead: str = "") -> str:
    """The column's first line: the hashtag, then the masthead."""
    hashtag = "#" + str(hashtag or "toread").lstrip("#")
    return f"{hashtag} {str(masthead or '').strip()}".strip()


def note_image(url: str) -> str:
    """The note page's social image (`og:image`), or "" when it has none.

    For the platform that cannot fetch a card's picture itself (Bluesky).
    """
    try:
        match = _OG_IMAGE_RE.search(requests.get(url, timeout=15).text)
    except requests.RequestException:
        return ""
    return match.group(1) if match else ""


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
