"""Recognize that a working paper and a published paper are the same work.

A paper often enters the kasten as a preprint (SocArXiv, arXiv, SSRN, OSF) and
is later re-added in its published form under a different `bibtex:` id. The vault
then holds two notes for one work, both assigned to topics and both listed in the
registers. This module decides when two records are the same work and which of
them is the more published one; `main` applies the result.

The `state` dedup index (exact normalized DOI/title) is the cheap ancestor of
this: it catches a byte-identical re-submission but not a preprint whose DOI and
title both moved. Matching here is a three-signal prefilter — normalized title
similarity, author-token overlap, summary-abstract jaccard — narrowing to a
handful of candidates that Claude then adjudicates. The prefilter is deliberately
loose: it is a recall device, and the LLM is the gate.
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Optional

from . import state as state_mod

# --- publication status ----------------------------------------------------
# Ordinal so the direction rule is a comparison: the more-published record always
# wins, regardless of which one arrived first.

RANK_UNKNOWN = 0
RANK_PREPRINT = 1
RANK_PUBLISHED = 2

# DOI prefixes owned by preprint servers. arXiv items in this vault carry no DOI
# at all (they are recorded by arxiv.org URL), so 10.48550 is listed for
# completeness but the URL check below is what actually covers them.
PREPRINT_DOI_PREFIXES = {
    "10.31235": "SocArXiv",
    "10.31234": "PsyArXiv",
    "10.31219": "OSF Preprints",
    "10.2139": "SSRN",
    "10.5281": "Zenodo",
    "10.48550": "arXiv",
    "10.1101": "bioRxiv/medRxiv",
    "10.21203": "Research Square",
    "10.20944": "Preprints.org",
    # Working-paper series and generic repositories. A DOI here is a deposit,
    # not a version of record — NBER and Figshare both turned up as spurious
    # "published versions" of vault preprints before they were listed.
    "10.3386": "NBER working papers",
    "10.6084": "figshare",
    "10.17605": "OSF",
}

_PREPRINT_VENUE_RE = re.compile(
    r"\b(?:arxiv|socarxiv|psyarxiv|biorxiv|medrxiv|edarxiv|metaarxiv|eartharxiv"
    r"|ssrn|zenodo|osf\s+preprints|research\s+square|preprints\.org"
    # Crossref reports the *publisher* rather than a venue for preprint
    # deposits, so these institution names appear where a journal title would.
    # Without them "Center for Open Science" reads as a journal and every OSF
    # deposit raises a spurious venue conflict.
    r"|center\s+for\s+open\s+science|cold\s+spring\s+harbor"
    r"|figshare|national\s+bureau\s+of\s+economic\s+research"
    r"|preprint|working\s+paper)\b",
    re.IGNORECASE,
)

_PREPRINT_URL_RE = re.compile(
    r"(?:arxiv\.org|biorxiv\.org|medrxiv\.org|osf\.io/preprints|ssrn\.com)",
    re.IGNORECASE,
)


def pub_rank(
    doi: Optional[str],
    url: Optional[str] = None,
    journal: Optional[str] = None,
    tags: Optional[list[str]] = None,
) -> tuple[int, bool]:
    """`(rank, venue_conflict)` — how published this record is.

    `RANK_PUBLISHED` for a DOI outside the known preprint registries,
    `RANK_PREPRINT` for a preprint DOI prefix / preprint host URL / preprint
    venue name, `RANK_UNKNOWN` when there is no DOI and no venue signal at all
    (the `scholar.google.com` fallback records).

    `venue_conflict` marks the awkward real case — an OSF/SocArXiv DOI whose
    venue names an actual journal, e.g. `Arminio2025-tw`
    (`10.31235/osf.io/bf459`, *Soc. Sci. Comput. Rev.*). The DOI wins the rank,
    because it is the record's canonical identifier and it points at the
    preprint deposit: scoring such a record as published would block the journal
    version from ever superseding it. The flag routes the pair through the LLM
    even on the DOI fast-path, so the ambiguity is adjudicated rather than
    assumed.
    """
    nd = state_mod.normalize_doi(doi) or ""
    venue_text = " ".join([journal or "", *(tags or [])]).strip()

    doi_preprint = any(nd.startswith(f"{p}/") for p in PREPRINT_DOI_PREFIXES)
    url_preprint = bool(_PREPRINT_URL_RE.search(url or ""))
    venue_preprint = bool(_PREPRINT_VENUE_RE.search(venue_text))

    if doi_preprint or url_preprint or venue_preprint:
        # A named venue that is not itself a preprint server contradicts the
        # preprint identifier — record it rather than silently picking a side.
        conflict = bool(venue_text) and not venue_preprint
        return RANK_PREPRINT, conflict
    if nd:
        return RANK_PUBLISHED, False
    return RANK_UNKNOWN, False


_DOI_VERSION_RE = re.compile(r"[._-]v\d+$")


def doi_base(doi: Optional[str]) -> Optional[str]:
    """Normalized DOI with any trailing version suffix removed.

    `10.31235/osf.io/8dqag_v1` and `..._v2` are the *same* deposit at two
    revisions; `state.normalize_doi` keeps them distinct, which is why the v1/v2
    pair sat in the vault undetected.
    """
    nd = state_mod.normalize_doi(doi)
    if not nd:
        return None
    return _DOI_VERSION_RE.sub("", nd) or None


# --- name and text similarity ----------------------------------------------

# Nobiliary particles carry no discriminating power and attach inconsistently.
_PARTICLES = {
    "de", "del", "della", "di", "da", "dos", "du", "la", "le", "van", "von",
    "der", "den", "ten", "ter", "al", "bin", "ibn", "st", "mc", "mac",
}


def _fold(text: str) -> str:
    """Lowercased, accent-folded ASCII."""
    folded = unicodedata.normalize("NFKD", text)
    return folded.encode("ascii", "ignore").decode("ascii").lower()


def author_tokens(authors: Optional[list[str]]) -> set[str]:
    """Discriminating name tokens from an author list, order-insensitive.

    Deliberately *not* "the surnames". The vault's author strings do not
    reliably separate given from family names — the four real formats are
    `["Fabio Giglietto"]`, `["Giglietto F."]`, `["M Terenzi F Giglietto"]`
    (a whole author list mashed into one string) and `[]` — so any rule that
    picks one token per entry as the surname is wrong on at least one of them.
    Keeping every token of length >= 2 and matching with subset tolerance
    (`authors_compatible`) is correct on all four: `{giglietto}` is a subset of
    `{fabio, giglietto}`.

    Initials, punctuation and nobiliary particles are dropped.
    """
    out: set[str] = set()
    for entry in authors or []:
        if not entry:
            continue
        for raw in re.split(r"[\s,;&]+", str(entry)):
            token = re.sub(r"[^a-z'-]", "", _fold(raw)).strip("'-")
            if len(token) < 2 or token in _PARTICLES:
                continue
            out.add(token)
    return out


def authors_compatible(a: set[str], b: set[str]) -> bool:
    """Whether two author-token sets could describe the same paper's authorship.

    An empty set means "authorship unknown" — the `cib.pdf` record has none —
    and defers to the title/abstract signals rather than blocking the match.
    Otherwise one set must contain the other (published versions add and drop
    co-authors) or the two must overlap heavily.
    """
    if not a or not b:
        return True
    if a <= b or b <= a:
        return True
    inter = a & b
    if not inter:
        return False
    return len(inter) / len(a | b) >= 0.6


def title_sim(a: Optional[str], b: Optional[str]) -> float:
    """Similarity of two titles after `state.normalize_title`, in [0, 1]."""
    na, nb = state_mod.normalize_title(a), state_mod.normalize_title(b)
    if not na or not nb:
        return 0.0
    if na == nb:
        return 1.0
    return SequenceMatcher(None, na, nb).ratio()


_STOPWORDS = {
    "the", "and", "for", "with", "that", "this", "from", "are", "was", "were",
    "have", "has", "had", "but", "not", "their", "them", "they", "these",
    "those", "which", "when", "what", "than", "then", "into", "over", "such",
    "also", "more", "most", "been", "being", "who", "whom", "its", "our",
    "can", "may", "using", "used", "use", "based", "study", "paper", "we",
}


def _content_tokens(text: Optional[str]) -> set[str]:
    if not text:
        return set()
    words = re.findall(r"[a-z]{4,}", _fold(str(text)))
    return {w for w in words if w not in _STOPWORDS}


def abstract_jaccard(a: Optional[str], b: Optional[str]) -> float:
    """Jaccard overlap of two abstracts' content words, in [0, 1].

    The only signal that finds a pair whose title and authors are both junk —
    `cib.pdf` vs its published form scores ~0.33 here while sharing no title
    words and no authors at all.
    """
    ta, tb = _content_tokens(a), _content_tokens(b)
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


# --- records ---------------------------------------------------------------


@dataclass
class Record:
    """One paper as this module sees it, from either the feed or a vault note."""

    key: str                      # bibtex key (no "bibtex:" prefix)
    title: str = ""
    authors: list[str] = field(default_factory=list)
    doi: Optional[str] = None
    url: Optional[str] = None
    journal: Optional[str] = None
    tags: list[str] = field(default_factory=list)
    year: str = ""
    abstract: Optional[str] = None
    discovery_date: str = ""
    citation_count: int = 0
    superseded_by: Optional[str] = None
    supersedes: Optional[str] = None

    @property
    def paper_id(self) -> str:
        return f"bibtex:{self.key}"

    @property
    def tokens(self) -> set[str]:
        return author_tokens(self.authors)

    @property
    def rank(self) -> int:
        return pub_rank(self.doi, self.url, self.journal, self.tags)[0]

    @property
    def venue_conflict(self) -> bool:
        return pub_rank(self.doi, self.url, self.journal, self.tags)[1]


_FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
# The APA citation block renders the venue as the first italic run after the
# title (`note_builder.build_apa_citation`); a volume, when present, follows as a
# second italic run. Frontmatter carries no venue key, so this is the only place
# a note records where it was published.
_CITATION_VENUE_RE = re.compile(r"^>\s.*?\*([^*]+)\*", re.MULTILINE)


def _loader():
    """A SafeLoader that leaves ISO timestamps as strings.

    `yaml.safe_load` turns `discovery_date: 2026-03-27T17:13:56.619953Z` into a
    `datetime`, which renders back as `2026-03-27 17:13:56.619953+00:00` — a
    different string in the same field. Since these values are read from a note
    and written straight back to it, that round-trip would rewrite dates
    gratuitously on every note this module touches.
    """
    import yaml

    class _NoTimestamps(yaml.SafeLoader):
        pass

    _NoTimestamps.add_constructor(
        "tag:yaml.org,2002:timestamp", yaml.SafeLoader.construct_yaml_str
    )
    return _NoTimestamps


def read_frontmatter(text: str) -> dict[str, Any]:
    """Parse a note's YAML frontmatter, or `{}` when it has none / is malformed."""
    import yaml  # local import: PyYAML is already a dependency (site_export)

    match = _FRONTMATTER_RE.match(text)
    if not match:
        return {}
    try:
        data = yaml.load(match.group(1), Loader=_loader())
    except Exception:  # noqa: BLE001 - a broken note must not abort a whole scan
        return {}
    return data if isinstance(data, dict) else {}


def _venue_of_note(text: str) -> Optional[str]:
    match = _CITATION_VENUE_RE.search(text)
    return match.group(1).strip() if match else None


def record_from_note(path: Path, summaries_dir: Optional[Path] = None) -> Optional[Record]:
    """Build a `Record` from a vault paper note, or None when unparseable.

    The abstract comes from the note's structured summary
    (`data/summaries/<key>.json`) — the note body is LLM prose, not a corpus
    signal, and the summary abstract is what the jaccard rule is tuned on.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    fm = read_frontmatter(text)
    if not fm:
        return None

    key = str(fm.get("bibtex_key") or path.stem)
    abstract = None
    if summaries_dir is not None:
        from . import summarizer

        summary = summarizer.load_summary(str(summaries_dir), key)
        if summary:
            abstract = summary.get("abstract")

    authors = fm.get("authors") or []
    return Record(
        key=key,
        title=str(fm.get("title") or ""),
        authors=[str(a) for a in authors if a],
        doi=str(fm.get("doi") or "") or None,
        url=str(fm.get("source_url") or "") or None,
        journal=_venue_of_note(text),
        year=str(fm.get("year") or ""),
        abstract=abstract,
        discovery_date=str(fm.get("discovery_date") or ""),
        citation_count=int(fm.get("citation_count") or 0),
        superseded_by=str(fm.get("superseded_by") or "") or None,
        supersedes=str(fm.get("supersedes") or "") or None,
    )


def load_vault_records(
    papers_dir: Path, summaries_dir: Optional[Path] = None
) -> dict[str, Record]:
    """Every paper note in the vault as `{bibtex_key: Record}`."""
    records: dict[str, Record] = {}
    if not papers_dir.is_dir():
        return records
    for note in sorted(papers_dir.glob("*.md")):
        record = record_from_note(note, summaries_dir)
        if record is not None:
            records[record.key] = record
    return records


def record_from_paper(paper, summary: Optional[dict] = None) -> Record:
    """Build a `Record` from a feed `Paper` (plus its summary when available)."""
    academic = getattr(paper, "academic", None) or {}
    return Record(
        key=paper.bibtex_key,
        title=paper.title or "",
        authors=list(paper.authors or []),
        doi=paper.doi,
        url=paper.url,
        journal=paper.journal,
        tags=list(getattr(paper, "tags", None) or []),
        year=_year_of_paper(paper),
        abstract=(summary or {}).get("abstract") or paper.abstract,
        discovery_date=paper.discovery_date or "",
        citation_count=int(academic.get("citation_count") or 0),
    )


def _year_of_paper(paper) -> str:
    for source in (paper.date_published, paper.id):
        if source:
            match = re.search(r"(19|20)\d{2}", str(source))
            if match:
                return match.group(0)
    return ""


_JUNK_KEY_RE = re.compile(
    r"^(?:unknown|noauthor|[a-z])(?:\d{4}|_undated|unknown)", re.IGNORECASE
)


def metadata_quality(record: Record) -> int:
    """How trustworthy this record's *identity* metadata looks.

    Breaks the direction tie for the three author-parsing collisions in the
    vault (`Unknown2025-ed60bc90` vs `Giglietto2025-ed60bc90` and friends),
    which share an identical DOI *and* title and so tie on every other signal.
    Without it the direction falls to discovery date, which says nothing about
    which note actually has usable authors.
    """
    score = 0
    if record.tokens:
        score += 4
    if not _JUNK_KEY_RE.match(record.key):
        score += 2
    if record.year:
        score += 1
    if record.discovery_date:
        score += 1
    return score


def direction(a: Record, b: Record) -> tuple[Record, Record]:
    """`(winner, loser)` — which record supersedes the other.

    Publication status decides, never arrival order: a preprint added after the
    journal version must not displace it. Ties fall through to the DOI version
    suffix (`_v2` beats `_v1`), then metadata quality, citations, and finally
    recency.
    """
    def sort_key(r: Record) -> tuple:
        version = _DOI_VERSION_RE.search(state_mod.normalize_doi(r.doi) or "")
        return (
            r.rank,
            int(version.group(0)[2:]) if version else 0,
            metadata_quality(r),
            r.citation_count or 0,
            r.discovery_date or "",
        )

    return (a, b) if sort_key(a) >= sort_key(b) else (b, a)


# --- candidate search ------------------------------------------------------

# Prefilter thresholds, measured against the five duplicate pairs actually
# present in the vault. Rules A-C catch the identical-title ones; rule D exists
# solely to reach the pair whose title is a filename and whose author list is
# empty (jaccard 0.34 with no other signal at all).
#
# Over all 33,670 note pairs the abstract scores separate cleanly: the five real
# duplicates score 0.30-0.60, and the highest-scoring pair of genuinely distinct
# papers is 0.246. ABSTRACT_ALONE sits in that gap, closer to the noise floor
# than to the duplicates so a real pair with a rewritten abstract still lands
# above it. Widening it further is cheap — every hit is adjudicated, not applied.
TITLE_STRONG = 0.90
TITLE_WEAK = 0.60
ABSTRACT_WITH_TITLE = 0.25
ABSTRACT_ALONE = 0.27
DOI_FASTPATH_TITLE = 0.85


@dataclass
class Candidate:
    """A possible same-work pairing, with the evidence that surfaced it."""

    key: str
    rule: str
    title_score: float
    abstract_score: float
    authors_ok: bool
    auto: bool          # DOI fast-path — identity is asserted, no LLM needed

    @property
    def strength(self) -> float:
        return max(self.title_score, self.abstract_score)


# Bucket holding records with no usable author tokens. "" can never collide with
# a real token, which is always at least two characters.
NO_AUTHORS = ""


def build_candidate_index(records: dict[str, Record]) -> dict[str, list[str]]:
    """Map each author token to the keys carrying it.

    Scopes the pairwise comparison: a new paper is only compared against records
    sharing at least one name token. Records with no usable authors go in the
    `NO_AUTHORS` bucket and are compared against *everything* — they are
    unreachable through name tokens in either direction, and they are precisely
    the records this feature exists for (the vault's worst duplicate had the
    title `cib.pdf` and an empty author list).
    """
    index: dict[str, list[str]] = {}
    for key, record in records.items():
        tokens = record.tokens
        if not tokens:
            index.setdefault(NO_AUTHORS, []).append(key)
            continue
        for token in tokens:
            index.setdefault(token, []).append(key)
    return index


def find_candidates(
    record: Record,
    records: dict[str, Record],
    index: dict[str, list[str]],
) -> list[Candidate]:
    """Possible same-work matches for `record`, strongest first.

    Skips records already tombstoned — a stub is not a merge target; callers
    resolve chains with `resolve_head` before applying anything.
    """
    tokens = record.tokens
    if tokens:
        scope: set[str] = set()
        for token in tokens:
            scope.update(index.get(token, ()))
        # Records with no authorship of their own share no token with anything,
        # so they would never be proposed as a match however well their text
        # lines up. Always consider them.
        scope.update(index.get(NO_AUTHORS, ()))
    else:
        # No usable authorship on this side either: the index cannot narrow
        # anything, so the only honest option is to compare against everything.
        scope = set(records)
    scope.discard(record.key)

    out: list[Candidate] = []
    for key in scope:
        other = records[key]
        if other.superseded_by:
            continue
        cand = _score_pair(record, other)
        if cand is not None:
            out.append(cand)
    out.sort(key=lambda c: (c.auto, c.strength), reverse=True)
    return out


def _score_pair(a: Record, b: Record) -> Optional[Candidate]:
    ok = authors_compatible(a.tokens, b.tokens)
    base_a, base_b = doi_base(a.doi), doi_base(b.doi)
    ts = title_sim(a.title, b.title)

    if base_a and base_a == base_b and (ts >= DOI_FASTPATH_TITLE or ok):
        # Same deposit. Identity is asserted by the DOI itself, so this needs no
        # LLM call — unless a venue conflict means one side may already be the
        # journal version, in which case the pair is adjudicated like any other.
        auto = not (a.venue_conflict or b.venue_conflict)
        return Candidate(b.key, "doi", ts, 0.0, ok, auto)

    abs_score = abstract_jaccard(a.abstract, b.abstract)

    if ok and ts >= TITLE_STRONG:
        return Candidate(b.key, "title", ts, abs_score, ok, False)
    if ok and ts >= TITLE_WEAK and abs_score >= ABSTRACT_WITH_TITLE:
        return Candidate(b.key, "title+abstract", ts, abs_score, ok, False)
    if abs_score >= ABSTRACT_ALONE and (ok or not a.tokens or not b.tokens):
        return Candidate(b.key, "abstract", ts, abs_score, ok, False)
    return None


# --- chains ----------------------------------------------------------------

_MAX_CHAIN_HOPS = 5


def resolve_head(key: str, records: dict[str, Record]) -> str:
    """Follow `superseded_by` to the live note at the head of a chain.

    v1 -> v2 -> journal is a real progression, and every stub must point at a
    note that still has content. Cycles and runaway chains stop at the last key
    reached rather than looping.
    """
    seen = {key}
    current = key
    for _ in range(_MAX_CHAIN_HOPS):
        record = records.get(current)
        nxt = record.superseded_by if record else None
        if not nxt or nxt in seen:
            break
        seen.add(nxt)
        current = nxt
    return current


def retarget_chain(
    papers_dir: Path,
    records: dict[str, Record],
    state: dict[str, Any],
    old_head: str,
    new_head: str,
    now: str,
) -> list[str]:
    """Point every stub that referenced `old_head` at `new_head` instead.

    Tombstoning a note that other tombstones already point at would otherwise
    leave a stub pointing at a stub — a reader following the redirect lands on
    another redirect, and the chain deepens every time the work is republished.
    v1 -> v2 -> journal is the ordinary progression, not an edge case: the vault
    holds a SocArXiv `_v2` note that two other notes already defer to, and it is
    itself a live candidate for the journal version.

    Returns the keys retargeted.
    """
    from . import note_builder

    moved: list[str] = []
    for key, record in list(records.items()):
        if key == new_head or record.superseded_by != old_head:
            continue
        path = note_path(papers_dir, key)
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            updated = note_builder.set_frontmatter_field(
                text, "superseded_by", new_head
            )
            body = updated.replace(f"[[{old_head}]]", f"[[{new_head}]]")
            if body != text:
                path.write_text(body, encoding="utf-8")
        entry = state["papers"].get(f"bibtex:{key}")
        if entry is not None:
            entry["superseded_by"] = f"bibtex:{new_head}"
            entry["last_processed"] = now
        records[key] = dataclass_replace(record, superseded_by=new_head)
        moved.append(key)
    return moved


def dataclass_replace(record: Record, **changes) -> Record:
    """`dataclasses.replace` for a Record, kept here so callers need not import it."""
    from dataclasses import replace

    return replace(record, **changes)


def pair_key(id_a: str, id_b: str) -> str:
    """Order-independent key for the adjudication decision cache."""
    return "|".join(sorted((id_a, id_b)))


# --- adjudication ----------------------------------------------------------

_ADJUDICATE_SYSTEM = """\
You decide whether two bibliographic records describe the SAME scholarly work.

The same work includes: a preprint and its published journal version; two \
versions of one preprint deposit; the same paper indexed twice with different \
metadata quality. Titles are often revised between preprint and publication, \
author lists gain or lose co-authors, and venue and DOI normally both change — \
none of that makes them different works.

Different works include: two papers by the same authors on a related question; \
a short commentary and the full study it discusses; successive studies in one \
research programme; a conference paper and a substantially different journal \
article. Shared authorship and shared topic are NOT evidence of sameness.

Judge on what the records actually claim: the research question, the data, the \
methods and the findings. If the evidence is thin or the two could plausibly be \
distinct studies, say so — a wrong merge destroys a note, so uncertainty must \
resolve to false.

Return ONLY a JSON object, no prose or fences:
  {"same_work": true|false, "confidence": "high"|"medium"|"low", \
"reason": "one sentence citing the decisive evidence"}"""


@dataclass
class Verdict:
    """The outcome of a same-work decision, whatever produced it."""

    same_work: bool
    confidence: str
    reason: str
    source: str = "claude"      # "claude" | "doi" | "cache"

    @property
    def applies(self) -> bool:
        """Whether this verdict is strong enough to rewrite the vault.

        Deliberately strict: only an unhedged yes. Everything else — a no, a
        hedge, a malformed reply, a transport error — leaves both notes alone.
        """
        return bool(self.same_work) and self.confidence == "high"


def _describe(record: Record) -> str:
    bits = [
        f"bibtex_key: {record.key}",
        f"title: {record.title}",
        f"authors: {', '.join(record.authors) if record.authors else '(none recorded)'}",
        f"year: {record.year or '(unknown)'}",
        f"doi: {record.doi or '(none)'}",
        f"venue: {record.journal or '(unknown)'}",
        f"url: {record.url or '(none)'}",
    ]
    if record.abstract:
        bits.append(f"abstract: {record.abstract}")
    return "\n".join(bits)


def adjudicate(
    a: Record,
    b: Record,
    candidate: Candidate,
    claude,
    model: str,
    cache: dict[str, Any],
) -> Verdict:
    """Decide whether `a` and `b` are the same work, consulting `cache` first.

    `cache` is `state["supersede_decisions"]`, keyed by the unordered pair. It
    holds negative verdicts as well as positive ones: without that, a pair of
    genuinely distinct papers that trips the prefilter is re-sent to Claude on
    every single run, forever.

    A DOI fast-path candidate is an identity assertion by the registrar and
    needs no model call.
    """
    key = pair_key(a.paper_id, b.paper_id)
    cached = cache.get(key)
    if isinstance(cached, dict) and "same_work" in cached:
        return Verdict(
            bool(cached.get("same_work")),
            str(cached.get("confidence") or "low"),
            str(cached.get("reason") or ""),
            source="cache",
        )

    if candidate.auto:
        verdict = Verdict(
            True, "high",
            f"same DOI deposit ({doi_base(a.doi)})",
            source="doi",
        )
    else:
        verdict = _ask_claude(a, b, claude, model)

    cache[key] = {
        "same_work": verdict.same_work,
        "confidence": verdict.confidence,
        "reason": verdict.reason,
        "source": verdict.source,
        "model": model if verdict.source == "claude" else "",
    }
    return verdict


def _ask_claude(a: Record, b: Record, claude, model: str) -> Verdict:
    from .claude_client import json_obj

    prompt = (
        f"Record A:\n{_describe(a)}\n\n"
        f"Record B:\n{_describe(b)}\n\n"
        "Are A and B the same scholarly work?"
    )
    try:
        result = json_obj(
            claude.complete_json(
                model=model,
                system=_ADJUDICATE_SYSTEM,
                prompt=prompt,
                max_tokens=1024,
            )
        )
    except Exception as exc:  # noqa: BLE001 - never abort a run over one pair
        return Verdict(False, "low", f"adjudication failed ({exc})")

    same = result.get("same_work")
    confidence = str(result.get("confidence") or "").lower()
    reason = str(result.get("reason") or "").strip()
    if not isinstance(same, bool) or confidence not in ("high", "medium", "low"):
        # An off-shape reply is not a "no" we can trust either — record it as a
        # low-confidence negative so it is neither applied nor re-billed.
        return Verdict(False, "low", f"unparseable verdict: {str(result)[:120]}")
    return Verdict(same, confidence, reason)


# --- applying a decision ---------------------------------------------------
# These are the file- and state-level primitives. Sequencing them (and running
# the summarize/assign pipeline the winning note needs) stays in `main`, which
# already owns the Claude client, the Drive client and the episode index.


def note_path(papers_dir: Path, key: str) -> Path:
    return Path(papers_dir) / f"{key}.md"


def podcast_url_of(papers_dir: Path, key: str) -> str:
    """The `podcast_url` recorded on a note, or "" — for podcast inheritance.

    A research-radio episode is produced per paper id, so the published version
    of a work usually has none while the working paper it replaced does. Losing
    the episode link on merge would be a regression for the reader.
    """
    path = note_path(papers_dir, key)
    if not path.is_file():
        return ""
    fm = read_frontmatter(path.read_text(encoding="utf-8"))
    return str(fm.get("podcast_url") or "")


def write_tombstone(
    papers_dir: Path, loser_key: str, winner: Record
) -> Optional[Path]:
    """Replace the loser's note with a stub pointing at `winner`.

    Returns the path written, or None when the loser has no note on disk (the
    incumbent-wins path writes a tombstone for a paper that never had one).
    """
    from . import note_builder

    path = note_path(papers_dir, loser_key)
    frontmatter = (
        read_frontmatter(path.read_text(encoding="utf-8")) if path.is_file() else {}
    )
    frontmatter.setdefault("bibtex_key", loser_key)
    stub = note_builder.build_tombstone_note(
        frontmatter,
        winner_key=winner.key,
        winner_title=winner.title,
        winner_venue=winner.journal or "",
        winner_year=winner.year,
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(stub, encoding="utf-8")
    return path


def tombstone_from_record(papers_dir: Path, loser: Record, winner: Record) -> Path:
    """Write a tombstone for a record that has no note yet (incumbent wins).

    An incoming preprint of a paper already held in published form gets a stub
    rather than a full note: no summary, no topics, no Slack. Writing *something*
    matters — the previous behaviour dropped such a paper with no trace, so the
    same decision was re-made on every subsequent run.
    """
    from . import note_builder

    frontmatter = {
        "title": loser.title,
        "aliases": [loser.title] if loser.title else [],
        "authors": loser.authors,
        "year": loser.year,
        "doi": loser.doi or "",
        "bibtex_key": loser.key,
        "source_url": loser.url or "",
        "discovery_date": loser.discovery_date or "",
    }
    stub = note_builder.build_tombstone_note(
        frontmatter,
        winner_key=winner.key,
        winner_title=winner.title,
        winner_venue=winner.journal or "",
        winner_year=winner.year,
    )
    path = note_path(papers_dir, loser.key)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(stub, encoding="utf-8")
    return path


def mark_supersedes(papers_dir: Path, winner_key: str, loser_key: str) -> bool:
    """Add `supersedes:` to an existing note's frontmatter. Body untouched.

    Used wherever the winner's note is already correct — the incumbent-wins path
    and the backfill — so a one-line metadata change never costs an LLM call.
    """
    from . import note_builder

    path = note_path(papers_dir, winner_key)
    if not path.is_file():
        return False
    text = path.read_text(encoding="utf-8")
    updated = note_builder.set_frontmatter_field(text, "supersedes", loser_key)
    if updated == text:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def tombstone_state(
    state: dict[str, Any],
    loser_id: str,
    winner_id: str,
    note_path_rel: str,
    now: str,
) -> dict[str, Any]:
    """Mark a state entry as superseded, keeping it in place.

    The entry is never deleted. `update` diffs the feed against state by id, so
    a deleted entry would make the paper look brand new on the next run and the
    whole decision would be re-made. `topics` is emptied so the paper leaves the
    registers and `_related_keys`; `slack_posted` is set so it can never enter a
    digest.
    """
    entry = state["papers"].get(loser_id) or {}
    entry.update(
        {
            "note_path": note_path_rel,
            "topics": [],
            "superseded_by": winner_id,
            "slack_posted": True,
            "last_processed": now,
        }
    )
    entry.pop("slack_pending", None)
    state["papers"][loser_id] = entry
    return entry


@dataclass
class _CitationView:
    """The subset of `Paper` that `note_builder.build_apa_citation` reads."""

    title: str
    authors: list[str]
    doi: Optional[str]
    url: Optional[str]
    journal: Optional[str]
    date_published: str
    volume: Optional[str] = None
    pages: Optional[str] = None
    id: str = ""


def apply_inplace_upgrade(
    papers_dir: Path,
    key: str,
    published_doi: str,
    venue: Optional[str] = None,
    year: Optional[str] = None,
) -> bool:
    """Upgrade a preprint note to its published record, keeping its bibtex key.

    Used when we learn a preprint has been published but no published record has
    entered the feed — there is no upstream bibtex key to build a new note under,
    and minting one locally would collide with whatever `toread` assigns later.
    So the existing note is amended in place: new DOI, the old one preserved as
    `preprint_doi`, the venue recorded, and the visible citation re-rendered. The
    LLM-written body is left alone.
    """
    from . import note_builder

    path = note_path(papers_dir, key)
    if not path.is_file():
        return False
    text = path.read_text(encoding="utf-8")
    fm = read_frontmatter(text)
    old_doi = str(fm.get("doi") or "")
    if state_mod.normalize_doi(old_doi) == state_mod.normalize_doi(published_doi):
        return False

    updated = text
    if old_doi:
        updated = note_builder.set_frontmatter_field(updated, "preprint_doi", old_doi)
    updated = note_builder.set_frontmatter_field(updated, "doi", published_doi)
    # Point the reader at the version of record; the preprint stays reachable
    # through `preprint_doi`.
    updated = note_builder.set_frontmatter_field(
        updated, "source_url", f"https://doi.org/{published_doi}"
    )
    if venue:
        updated = note_builder.set_frontmatter_field(
            updated, "published_venue", note_builder._yaml_quote(venue)
        )
    new_year = str(year or fm.get("year") or "")
    if year and str(year) > str(fm.get("year") or ""):
        updated = note_builder.set_frontmatter_field(updated, "year", year)

    citation = note_builder.render_citation_block(
        _CitationView(
            title=str(fm.get("title") or ""),
            authors=[str(a) for a in (fm.get("authors") or [])],
            doi=published_doi,
            url=f"https://doi.org/{published_doi}",
            journal=venue,
            date_published=new_year,
            id=key,
        )
    )
    updated = note_builder.replace_citation_block(updated, citation)
    if updated == text:
        return False
    path.write_text(updated, encoding="utf-8")
    return True
