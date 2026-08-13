"""Tests for src.supersede — same-work detection and the tombstone merge.

Fixtures are the real duplicate pairs that were sitting in the vault when this
was written, with their real titles, author strings, DOIs and citation counts.
They are the reason the feature exists, so they are what it is tested against.
Everything here is offline: no network, no Claude.
"""
import json

import pytest

from src import note_builder, site_export, supersede
from src.supersede import (
    RANK_PREPRINT,
    RANK_PUBLISHED,
    RANK_UNKNOWN,
    Candidate,
    Record,
    abstract_jaccard,
    author_tokens,
    authors_compatible,
    direction,
    doi_base,
    pub_rank,
    resolve_head,
    title_sim,
)

# --- fixtures --------------------------------------------------------------

CIB = Record(
    key="noauthor_undated-bm",
    title="cib.pdf",
    authors=[],
    url="https://scholar.google.com/scholar?q=cib.pdf",
    discovery_date="2026-03-27T17:13:56.619953Z",
    abstract=(
        "Meta identified 49 deceptive networks engaged in coordinated "
        "inauthentic behavior. These networks reached 37 million Facebook "
        "users, about 15 percent of US adults, and 3 million Instagram users "
        "during the 2020 elections, measured against FIES survey panel data."
    ),
)
APPEL = Record(
    key="Appel2026-qr",
    title="How deceptive online networks reached millions in the US 2020 elections",
    authors=["Ruth E. Appel", "Young Mie Kim", "Jennifer Pan", "Yiqing Xu"],
    doi="10.1038/s41562-026-02435-2",
    url="https://doi.org/10.1038/s41562-026-02435-2",
    journal="Nature Human Behaviour",
    year="2026",
    discovery_date="2026-04-11T07:41:51.831048Z",
    abstract=(
        "We study 49 deceptive networks removed by Meta for coordinated "
        "inauthentic behavior, estimating that they reached 37 million "
        "Facebook users, roughly 15 percent of US adults, and 3 million "
        "Instagram users, linking exposure to FIES survey panel data."
    ),
)

_BLUNT = ('"A Pretty Blunt Approach": Meta\'s Political Content Reduction '
          "Policy and Italian Parliamentarians' Facebook Visibility")
BLUNT_V1 = Record(key="Giglietto2025-1e9a0917", title=_BLUNT,
                  authors=["Fabio Giglietto"], doi="10.31235/osf.io/8dqag_v1",
                  year="2025", citation_count=0)
BLUNT_V2 = Record(key="Giglietto2025-1765bb4f", title=_BLUNT,
                  authors=["Fabio Giglietto"], doi="10.31235/osf.io/8dqag_v2",
                  year="2025", citation_count=2)

_BIGDATA = ("Three Consequences of Big Data on the Practices and Scholarships "
            "of Political Communication")
BIGDATA_F = Record(key="F2020-6278a4aa", title=_BIGDATA,
                   authors=["Giglietto F."], doi="10.3270/96423",
                   year="2020", citation_count=0)
BIGDATA_FULL = Record(key="Giglietto2020-6278a4aa", title=_BIGDATA,
                      authors=["Fabio Giglietto"], doi="10.3270/96423",
                      year="2020", citation_count=2)

_APIS = "The State of Social Media Research APIs &amp; Tools in the Digital Service Act Era"
APIS_UNKNOWN = Record(key="Unknown2025-ed60bc90", title=_APIS, authors=[],
                      doi="10.5281/zenodo.16269197", year="2025", citation_count=0)
APIS_NAMED = Record(key="Giglietto2025-ed60bc90", title=_APIS,
                    authors=["M Terenzi F Giglietto"],
                    doi="10.5281/zenodo.16269197", year="2025", citation_count=1)

_AIN = ("The power of Alternative Influence Networks (AIN) for spreading "
        "Covid-19 problematic information on Facebook during a year of pandemic")
AIN_UNKNOWN = Record(key="Unknown2023-9137f448", title=_AIN, authors=[],
                     doi="10.1445/106772", year="2023", citation_count=0)
AIN_NAMED = Record(key="Marino2023-9137f448", title=_AIN,
                   authors=["F Giglietto G Marino"], doi="10.1445/106772",
                   year="2023", citation_count=2)

# Same four authors, adjacent topic, both arXiv — and genuinely different papers
# (a Perspective essay vs an empirical audit). The pair that must NOT merge.
BAKC_A = Record(
    key="Bak-Coleman2025-pm",
    title="The risks of industry influence in tech research",
    authors=["Joseph Bak-Coleman", "Cailin O'Connor", "Carl Bergstrom", "Jevin West"],
    url="http://arxiv.org/abs/2510.19894v2",
    year="2025",
    abstract=(
        "Industry funding shapes what questions technology researchers ask. We "
        "argue that the field needs disclosure norms and independent replication "
        "to preserve credibility, and outline a set of governance proposals."
    ),
)
BAKC_B = Record(
    key="Bak-Coleman2026-mk",
    title="Industry influence in high-profile social media research",
    authors=["Joseph Bak-Coleman", "Jevin West", "Cailin O'Connor", "Carl T. Bergstrom"],
    url="http://arxiv.org/abs/2601.11507v1",
    year="2026",
    abstract=(
        "We audit papers published in Science, Nature and PNAS that relied on "
        "platform-provided data, coding each for author affiliation, data access "
        "conditions and stated conflicts, and report how often terms were disclosed."
    ),
)

REAL_PAIRS = [
    pytest.param(CIB, APPEL, id="cib-pdf-to-nature"),
    pytest.param(BLUNT_V1, BLUNT_V2, id="socarxiv-v1-to-v2"),
    pytest.param(BIGDATA_F, BIGDATA_FULL, id="initial-only-author"),
    pytest.param(APIS_UNKNOWN, APIS_NAMED, id="unknown-author-zenodo"),
    pytest.param(AIN_UNKNOWN, AIN_NAMED, id="unknown-author-journal"),
]


class StubClaude:
    """A Claude client that returns a canned verdict and counts its calls."""

    def __init__(self, payload, reasoning_model="stub-model"):
        self.payload = payload
        self.reasoning_model = reasoning_model
        self.calls = 0

    def complete_json(self, **kwargs):
        self.calls += 1
        if isinstance(self.payload, Exception):
            raise self.payload
        return self.payload


# --- publication rank ------------------------------------------------------


@pytest.mark.parametrize(
    "doi,url,expected",
    [
        ("10.31235/osf.io/bf459", None, RANK_PREPRINT),      # SocArXiv
        ("10.31234/osf.io/xcwdn", None, RANK_PREPRINT),      # PsyArXiv
        ("10.31219/osf.io/ch8gj", None, RANK_PREPRINT),      # OSF
        ("10.2139/ssrn.5259653", None, RANK_PREPRINT),       # SSRN
        ("10.5281/zenodo.16269197", None, RANK_PREPRINT),    # Zenodo
        ("10.3386/w33818", None, RANK_PREPRINT),             # NBER working paper
        ("10.6084/m9.figshare.33103437", None, RANK_PREPRINT),  # figshare deposit
        (None, "http://arxiv.org/abs/2510.19894v2", RANK_PREPRINT),
        ("10.1126/science.aaa1160", None, RANK_PUBLISHED),
        ("10.1038/s41562-026-02435-2", None, RANK_PUBLISHED),
        (None, "https://scholar.google.com/scholar?q=cib.pdf", RANK_UNKNOWN),
        (None, None, RANK_UNKNOWN),
    ],
)
def test_pub_rank(doi, url, expected):
    assert pub_rank(doi, url)[0] == expected


def test_arxiv_records_carry_no_doi_so_the_url_is_the_only_signal():
    assert BAKC_A.doi is None
    assert BAKC_A.rank == RANK_PREPRINT


def test_venue_conflict_flags_preprint_doi_with_a_journal_venue():
    # Arminio2025-tw: an OSF deposit whose citation names a real journal.
    rank, conflict = pub_rank("10.31235/osf.io/bf459", None, "Soc. Sci. Comput. Rev.")
    assert (rank, conflict) == (RANK_PREPRINT, True)


def test_no_venue_conflict_for_a_preprint_servers_own_name():
    # Crossref reports the publisher for OSF deposits; it is not a journal.
    assert pub_rank("10.31235/osf.io/8dqag", None, "Center for Open Science") == (
        RANK_PREPRINT, False
    )


def test_doi_base_ignores_the_version_suffix():
    assert doi_base("10.31235/osf.io/8dqag_v1") == doi_base("10.31235/osf.io/8dqag_v2")
    assert doi_base("https://doi.org/10.1445/106772") == "10.1445/106772"
    assert doi_base(None) is None


# --- names and similarity --------------------------------------------------


@pytest.mark.parametrize(
    "authors,expected",
    [
        (["Fabio Giglietto"], {"fabio", "giglietto"}),
        (["Giglietto F."], {"giglietto"}),
        (["M Terenzi F Giglietto"], {"terenzi", "giglietto"}),
        (["Righetti, Nicola"], {"righetti", "nicola"}),
        (["Claes H. de Vreese"], {"claes", "vreese"}),
        ([], set()),
    ],
)
def test_author_tokens_handles_every_real_format(authors, expected):
    assert author_tokens(authors) == expected


def test_authors_compatible_is_subset_tolerant():
    assert authors_compatible({"giglietto"}, {"fabio", "giglietto"})
    # An added co-author on the published version must not break the match.
    assert authors_compatible({"appel", "kim"}, {"appel", "kim", "pan"})


def test_authors_compatible_defers_when_authorship_is_unknown():
    assert authors_compatible(set(), {"appel", "kim"})


def test_authors_compatible_rejects_disjoint_authorship():
    assert not authors_compatible({"appel"}, {"bakshy"})


def test_title_sim_normalizes_before_comparing():
    assert title_sim("The State of APIs", "the state of apis") == 1.0
    assert title_sim("cib.pdf", APPEL.title) < 0.3


# --- the prefilter ---------------------------------------------------------


@pytest.mark.parametrize("loser,winner", REAL_PAIRS)
def test_prefilter_finds_every_real_duplicate(loser, winner):
    assert supersede._score_pair(loser, winner) is not None


@pytest.mark.parametrize("loser,winner", REAL_PAIRS)
def test_direction_picks_the_published_side(loser, winner):
    got_winner, got_loser = direction(loser, winner)
    assert (got_winner.key, got_loser.key) == (winner.key, loser.key)
    # Order of arguments must not matter.
    assert direction(winner, loser)[0].key == winner.key


def test_direction_is_decided_by_status_not_arrival_order():
    """A preprint added after the journal version must not displace it."""
    late_preprint = Record(
        key="Late2026-zz", title=APPEL.title, authors=APPEL.authors,
        doi="10.31235/osf.io/late", year="2026",
        discovery_date="2027-01-01T00:00:00Z",   # newer than the journal note
    )
    winner, loser = direction(late_preprint, APPEL)
    assert winner.key == APPEL.key
    assert loser.key == late_preprint.key


def test_metadata_quality_breaks_the_identical_doi_ties():
    """The three author-parsing collisions tie on rank, version and title."""
    for loser, winner in ((BIGDATA_F, BIGDATA_FULL),
                          (APIS_UNKNOWN, APIS_NAMED),
                          (AIN_UNKNOWN, AIN_NAMED)):
        assert doi_base(loser.doi) == doi_base(winner.doi)
        assert loser.rank == winner.rank
        assert supersede.metadata_quality(winner) > supersede.metadata_quality(loser)


def test_doi_pairs_take_the_llm_free_fast_path():
    for loser, winner in ((BIGDATA_F, BIGDATA_FULL), (BLUNT_V1, BLUNT_V2)):
        assert supersede._score_pair(loser, winner).auto is True


def test_the_junk_title_pair_is_reachable_only_through_the_abstract():
    """Title and author matching both fail on `cib.pdf`; jaccard is all there is."""
    assert title_sim(CIB.title, APPEL.title) < supersede.TITLE_WEAK
    assert CIB.tokens == set()
    cand = supersede._score_pair(CIB, APPEL)
    assert cand.rule == "abstract"
    assert cand.abstract_score >= supersede.ABSTRACT_ALONE


def test_distinct_papers_by_the_same_authors_are_not_candidates():
    """The nearest real near-miss in the corpus must stay below the threshold."""
    assert authors_compatible(BAKC_A.tokens, BAKC_B.tokens)  # same four people
    assert abstract_jaccard(BAKC_A.abstract, BAKC_B.abstract) < supersede.ABSTRACT_ALONE
    assert supersede._score_pair(BAKC_A, BAKC_B) is None


def test_find_candidates_skips_notes_already_tombstoned():
    records = {
        CIB.key: CIB,
        APPEL.key: Record(**{**APPEL.__dict__, "superseded_by": "Other2026-aa"}),
    }
    index = supersede.build_candidate_index(records)
    assert find_candidates_keys(CIB, records, index) == []


def find_candidates_keys(record, records, index):
    return [c.key for c in supersede.find_candidates(record, records, index)]


def test_records_without_authors_still_reach_the_whole_corpus():
    records = {CIB.key: CIB, APPEL.key: APPEL}
    index = supersede.build_candidate_index(records)
    # CIB contributes no tokens, so the name index cannot narrow anything.
    assert find_candidates_keys(CIB, records, index) == [APPEL.key]


def test_an_authorless_note_is_reachable_from_an_incoming_paper():
    """The live `update` direction: incoming has authors, the vault note has none.

    The name index can only connect records through a shared token, so without
    an explicit no-authors bucket a note like `cib.pdf` is invisible to every
    arriving paper — which is the one case this whole feature exists to catch.
    """
    records = {CIB.key: CIB, APPEL.key: APPEL}
    index = supersede.build_candidate_index(records)
    assert find_candidates_keys(APPEL, records, index) == [CIB.key]


# --- adjudication ----------------------------------------------------------


def test_adjudication_applies_only_an_unhedged_yes():
    for payload, expected in [
        ({"same_work": True, "confidence": "high", "reason": "x"}, True),
        ({"same_work": True, "confidence": "medium", "reason": "x"}, False),
        ({"same_work": True, "confidence": "low", "reason": "x"}, False),
        ({"same_work": False, "confidence": "high", "reason": "x"}, False),
    ]:
        claude = StubClaude(payload)
        cand = Candidate(APPEL.key, "abstract", 0.0, 0.34, True, False)
        verdict = supersede.adjudicate(CIB, APPEL, cand, claude, "m", {})
        assert verdict.applies is expected


@pytest.mark.parametrize(
    "payload",
    [
        {"same_work": "yes", "confidence": "high"},   # wrong type
        {"confidence": "high"},                       # missing verdict
        {"same_work": True, "confidence": "certain"}, # unknown confidence
        RuntimeError("API exploded"),
    ],
)
def test_adjudication_fails_closed(payload):
    claude = StubClaude(payload)
    cand = Candidate(APPEL.key, "abstract", 0.0, 0.34, True, False)
    verdict = supersede.adjudicate(CIB, APPEL, cand, claude, "m", {})
    assert verdict.applies is False


def test_doi_fast_path_needs_no_model_call():
    claude = StubClaude({"same_work": False, "confidence": "high", "reason": "no"})
    cand = Candidate(BIGDATA_FULL.key, "doi", 1.0, 0.0, True, auto=True)
    verdict = supersede.adjudicate(BIGDATA_F, BIGDATA_FULL, cand, claude, "m", {})
    assert verdict.applies and verdict.source == "doi"
    assert claude.calls == 0


def test_decision_cache_prevents_re_adjudication():
    """A rejected pair must not be re-billed on every subsequent run."""
    claude = StubClaude({"same_work": False, "confidence": "high", "reason": "distinct"})
    cand = Candidate(BAKC_B.key, "abstract", 0.6, 0.3, True, False)
    cache = {}
    for _ in range(3):
        verdict = supersede.adjudicate(BAKC_A, BAKC_B, cand, claude, "m", cache)
        assert verdict.applies is False
    assert claude.calls == 1
    assert len(cache) == 1


def test_decision_cache_key_is_order_independent():
    assert supersede.pair_key("bibtex:a", "bibtex:b") == supersede.pair_key(
        "bibtex:b", "bibtex:a"
    )


# --- chains ----------------------------------------------------------------


def test_resolve_head_collapses_a_chain():
    records = {
        "v1": Record(key="v1", superseded_by="v2"),
        "v2": Record(key="v2", superseded_by="journal"),
        "journal": Record(key="journal"),
    }
    assert resolve_head("v1", records) == "journal"


def test_resolve_head_survives_a_cycle():
    records = {
        "a": Record(key="a", superseded_by="b"),
        "b": Record(key="b", superseded_by="a"),
    }
    assert resolve_head("a", records) in {"a", "b"}


# --- tombstones ------------------------------------------------------------


def _write_note(papers_dir, record, body="## Summary\n\nA real note body.\n"):
    fm = note_builder.render_frontmatter({
        "title": note_builder._yaml_quote(record.title),
        "aliases": [note_builder._yaml_quote(record.title)],
        "authors": [note_builder._yaml_quote(a) for a in record.authors],
        "year": record.year,
        "doi": record.doi or "",
        "bibtex_key": record.key,
        "topics": ["coordinated-inauthentic-behavior"],
        "citation_count": record.citation_count,
        "source_url": record.url or "",
        "podcast_url": "https://example.org/ep.mp3",
        "discovery_date": record.discovery_date,
    })
    path = papers_dir / f"{record.key}.md"
    path.write_text(f"{fm}\n\n# {record.title}\n\n> A citation.\n\n{body}",
                    encoding="utf-8")
    return path


def test_tombstone_keeps_its_own_identity_and_drops_its_topics(tmp_path):
    papers = tmp_path / "Papers"
    papers.mkdir()
    _write_note(papers, CIB)

    supersede.write_tombstone(papers, CIB.key, APPEL)
    text = (papers / f"{CIB.key}.md").read_text(encoding="utf-8")
    fm = supersede.read_frontmatter(text)

    # Its own title, not the winner's — site_export shows aliases[0].
    assert fm["title"] == CIB.title
    assert fm["aliases"] == [CIB.title]
    assert fm["superseded_by"] == APPEL.key
    assert fm["topics"] == []
    # Rendered as a bare `podcast_url:`, matching the vault's existing
    # convention for an absent episode; YAML reads that back as None.
    assert not fm["podcast_url"]
    # The original discovery date is preserved verbatim, not re-serialised.
    assert CIB.discovery_date in text
    assert f"[[{APPEL.key}]]" in text


def test_tombstone_wikilink_survives_link_sanitisation(tmp_path):
    papers = tmp_path / "Papers"
    papers.mkdir()
    _write_note(papers, CIB)
    supersede.write_tombstone(papers, CIB.key, APPEL)
    text = (papers / f"{CIB.key}.md").read_text(encoding="utf-8")

    _, changes = note_builder.sanitize_links(text, {CIB.key, APPEL.key})
    assert changes == []


def test_tombstone_never_takes_a_latest_papers_slot(tmp_path):
    papers = tmp_path / "Papers"
    papers.mkdir()
    _write_note(papers, CIB)
    live = (papers / f"{CIB.key}.md").read_text(encoding="utf-8")
    assert site_export._read_paper_meta(live) is not None

    supersede.write_tombstone(papers, CIB.key, APPEL)
    stub = (papers / f"{CIB.key}.md").read_text(encoding="utf-8")
    assert site_export._read_paper_meta(stub) is None


def test_tombstone_is_idempotent(tmp_path):
    papers = tmp_path / "Papers"
    papers.mkdir()
    _write_note(papers, CIB)
    supersede.write_tombstone(papers, CIB.key, APPEL)
    first = (papers / f"{CIB.key}.md").read_text(encoding="utf-8")
    supersede.write_tombstone(papers, CIB.key, APPEL)
    assert (papers / f"{CIB.key}.md").read_text(encoding="utf-8") == first


def test_podcast_url_is_inherited_from_the_note_being_replaced(tmp_path):
    papers = tmp_path / "Papers"
    papers.mkdir()
    _write_note(papers, CIB)
    assert supersede.podcast_url_of(papers, CIB.key) == "https://example.org/ep.mp3"


def test_tombstone_for_a_record_with_no_note(tmp_path):
    """The incumbent-wins path: an incoming preprint that never had a note."""
    papers = tmp_path / "Papers"
    papers.mkdir()
    preprint = Record(key="Late2026-zz", title=APPEL.title, authors=APPEL.authors,
                      doi="10.31235/osf.io/late", year="2026")
    supersede.tombstone_from_record(papers, preprint, APPEL)
    fm = supersede.read_frontmatter(
        (papers / "Late2026-zz.md").read_text(encoding="utf-8")
    )
    assert fm["superseded_by"] == APPEL.key
    assert fm["topics"] == []


def test_mark_supersedes_touches_only_the_frontmatter(tmp_path):
    papers = tmp_path / "Papers"
    papers.mkdir()
    _write_note(papers, APPEL, body="## Summary\n\nIrreplaceable LLM prose.\n")
    before = (papers / f"{APPEL.key}.md").read_text(encoding="utf-8")

    assert supersede.mark_supersedes(papers, APPEL.key, CIB.key) is True
    after = (papers / f"{APPEL.key}.md").read_text(encoding="utf-8")
    assert supersede.read_frontmatter(after)["supersedes"] == CIB.key
    assert "Irreplaceable LLM prose." in after
    assert before.split("---\n", 2)[2] == after.split("---\n", 2)[2]


# --- state and re-entrancy -------------------------------------------------


def test_tombstoned_state_entry_is_kept_not_deleted():
    state = {"papers": {"bibtex:old": {"topics": ["t"], "slack_pending": True}}}
    supersede.tombstone_state(state, "bibtex:old", "bibtex:new", "Papers/old.md", "now")
    entry = state["papers"]["bibtex:old"]
    assert entry["superseded_by"] == "bibtex:new"
    assert entry["topics"] == []
    assert entry["slack_posted"] is True
    assert "slack_pending" not in entry


def test_a_tombstone_is_never_re_rendered_by_a_later_update():
    """The `changed_papers` path would otherwise overwrite the stub.

    A tombstoned paper is still in the feed — it was merged here, not withdrawn
    upstream — so its content hash keeps moving as episodes appear. It must land
    in neither bucket of the new/changed diff. Asserted through the same helper
    `cmd_update` calls, so deleting the guard fails this test.
    """
    from src.main import classify_feed_paper

    state = {"papers": {}}
    supersede.tombstone_state(state, "bibtex:old", "bibtex:new", "Papers/old.md", "now")
    entry = state["papers"]["bibtex:old"]

    assert classify_feed_paper(entry, "a-brand-new-hash") == "tombstoned"
    # ...and it stays tombstoned however far the content drifts.
    entry["content_hash"] = "a-brand-new-hash"
    assert classify_feed_paper(entry, "another-hash-entirely") == "tombstoned"


def test_classify_feed_paper_still_routes_ordinary_papers():
    from src.main import classify_feed_paper

    assert classify_feed_paper(None, "h") == "new"
    assert classify_feed_paper({"content_hash": "h"}, "h") == "unchanged"
    assert classify_feed_paper({"content_hash": "old"}, "h") == "changed"


# --- chain collapse --------------------------------------------------------


def test_retarget_chain_keeps_every_stub_pointing_at_a_live_note(tmp_path):
    """v1 -> v2 -> journal: tombstoning v2 must drag v1 along with it.

    Otherwise a reader following v1's redirect lands on another redirect. This
    is the ordinary progression for a preprint that is revised and then
    published, not an edge case.
    """
    papers = tmp_path / "Papers"
    papers.mkdir()
    _write_note(papers, BLUNT_V1)
    _write_note(papers, BLUNT_V2)
    state = {"papers": {BLUNT_V1.paper_id: {}, BLUNT_V2.paper_id: {}}}

    # First merge: v1 -> v2.
    supersede.write_tombstone(papers, BLUNT_V1.key, BLUNT_V2)
    supersede.tombstone_state(state, BLUNT_V1.paper_id, BLUNT_V2.paper_id, "p", "t0")
    records = supersede.load_vault_records(papers)
    assert records[BLUNT_V1.key].superseded_by == BLUNT_V2.key

    # Later the journal version arrives and v2 is tombstoned in turn.
    journal = Record(key="Giglietto2026-jj", title=_BLUNT,
                     authors=["Fabio Giglietto"], doi="10.1177/14614448261234567",
                     journal="New Media & Society", year="2026")
    supersede.write_tombstone(papers, BLUNT_V2.key, journal)
    records[BLUNT_V2.key] = supersede.dataclass_replace(
        records[BLUNT_V2.key], superseded_by=journal.key
    )
    moved = supersede.retarget_chain(
        papers, records, state, BLUNT_V2.key, journal.key, "t1"
    )

    assert moved == [BLUNT_V1.key]
    v1_text = (papers / f"{BLUNT_V1.key}.md").read_text(encoding="utf-8")
    assert supersede.read_frontmatter(v1_text)["superseded_by"] == journal.key
    assert f"[[{journal.key}]]" in v1_text
    assert f"[[{BLUNT_V2.key}]]" not in v1_text
    assert state["papers"][BLUNT_V1.paper_id]["superseded_by"] == journal.paper_id
    # No stub points at a stub.
    for key in (BLUNT_V1.key, BLUNT_V2.key):
        head = supersede.read_frontmatter(
            (papers / f"{key}.md").read_text(encoding="utf-8")
        )["superseded_by"]
        assert head == journal.key


def test_retarget_chain_never_points_a_note_at_itself(tmp_path):
    papers = tmp_path / "Papers"
    papers.mkdir()
    _write_note(papers, BLUNT_V2)
    records = {
        BLUNT_V2.key: supersede.dataclass_replace(BLUNT_V2, superseded_by="old"),
    }
    moved = supersede.retarget_chain(
        papers, records, {"papers": {}}, "old", BLUNT_V2.key, "t"
    )
    assert moved == []


# --- in-place upgrade ------------------------------------------------------


def test_inplace_upgrade_rewrites_identity_and_citation(tmp_path):
    papers = tmp_path / "Papers"
    papers.mkdir()
    preprint = Record(
        key="Arminio2025-tw",
        title="Leveraging VLLMs for visual clustering",
        authors=["Luigi Arminio", "Matteo Magnani"],
        doi="10.31235/osf.io/bf459",
        url="https://doi.org/10.31235/osf.io/bf459",
        year="2025",
    )
    _write_note(papers, preprint)

    assert supersede.apply_inplace_upgrade(
        papers, preprint.key, "10.1177/08944393251376703",
        "Social Science Computer Review", "2025",
    ) is True

    text = (papers / f"{preprint.key}.md").read_text(encoding="utf-8")
    fm = supersede.read_frontmatter(text)
    assert fm["doi"] == "10.1177/08944393251376703"
    assert fm["preprint_doi"] == "10.31235/osf.io/bf459"
    assert fm["published_venue"] == "Social Science Computer Review"
    assert fm["bibtex_key"] == preprint.key          # the key never moves
    assert "Social Science Computer Review" in text  # citation re-rendered
    # Re-running is a no-op.
    assert supersede.apply_inplace_upgrade(
        papers, preprint.key, "10.1177/08944393251376703",
        "Social Science Computer Review", "2025",
    ) is False


# --- Slack "now published" framing -----------------------------------------


def _slack_paper(record):
    from src.feed_client import Paper

    return Paper(id=record.paper_id, title=record.title, authors=list(record.authors),
                 abstract=record.abstract, doi=record.doi, url=record.url,
                 journal=record.journal, date_published=record.year)


def test_slack_digest_marks_a_now_published_paper():
    from src import slack_client

    blocks = slack_client.build_blocks(
        _slack_paper(APPEL), {"abstract": "x"}, ["topic-a"], None,
        superseded_note={"key": CIB.key, "venue": "Nature Human Behaviour",
                         "discovery_date": "2026-03-27T17:13:56Z"},
    )
    contexts = [
        element["text"]
        for block in blocks if block["type"] == "context"
        for element in block["elements"]
    ]
    banner = [t for t in contexts if "Now published" in t]
    assert len(banner) == 1
    assert "Nature Human Behaviour" in banner[0]
    assert "2026-03-27" in banner[0]
    # Block Kit shape: every block must be renderable.
    assert all("type" in b for b in blocks)


def test_slack_digest_is_unchanged_for_an_ordinary_paper():
    from src import slack_client

    paper = _slack_paper(APPEL)
    plain = slack_client.build_blocks(paper, {"abstract": "x"}, ["topic-a"], None)
    assert not any(
        "Now published" in element.get("text", "")
        for block in plain if block["type"] == "context"
        for element in block["elements"]
    )


def test_slack_banner_survives_a_missing_venue_or_date():
    from src import slack_client

    blocks = slack_client.build_blocks(
        _slack_paper(APPEL), {"abstract": "x"}, [], None,
        superseded_note={"key": CIB.key},
    )
    banner = [
        element["text"]
        for block in blocks if block["type"] == "context"
        for element in block["elements"]
        if "Now published" in element.get("text", "")
    ]
    assert len(banner) == 1


# --- OpenAlex parsing (offline fixture) ------------------------------------

_OPENALEX_RESULTS = json.loads("""
{"results": [
  {"id": "W1", "doi": "https://doi.org/10.31235/osf.io/bf459",
   "title": "Leveraging VLLMs for Visual Clustering", "type": "preprint",
   "publication_year": 2024,
   "primary_location": {"source": null},
   "authorships": [{"author": {"display_name": "Luigi Arminio"}}]},
  {"id": "W2", "doi": "https://doi.org/10.6084/m9.figshare.33103437",
   "title": "Leveraging VLLMs for Visual Clustering", "type": "article",
   "publication_year": 2025,
   "primary_location": {"source": {"display_name": "Figshare", "type": "repository"}},
   "authorships": [{"author": {"display_name": "Luigi Arminio"}}]},
  {"id": "W3", "doi": "https://doi.org/10.1177/08944393251376703",
   "title": "Leveraging VLLMs for Visual Clustering", "type": "article",
   "publication_year": 2025,
   "primary_location": {"source": {"display_name": "Social Science Computer Review",
                                   "type": "journal"}},
   "authorships": [{"author": {"display_name": "Luigi Arminio"}}]}
]}
""")["results"]


def test_openalex_prefers_the_journal_over_a_repository_copy(monkeypatch):
    from src import openalex_client

    monkeypatch.setattr(
        openalex_client, "search_by_title", lambda *a, **k: _OPENALEX_RESULTS
    )
    preprint = Record(
        key="Arminio2025-tw", title="Leveraging VLLMs for Visual Clustering",
        authors=["Luigi Arminio"], doi="10.31235/osf.io/bf459",
    )
    work = openalex_client.find_published_version(preprint)
    assert openalex_client.describe(work) == {
        "doi": "10.1177/08944393251376703",
        "title": "Leveraging VLLMs for Visual Clustering",
        "venue": "Social Science Computer Review",
        "year": "2025",
    }


def test_openalex_returns_nothing_when_only_repositories_match(monkeypatch):
    from src import openalex_client

    monkeypatch.setattr(
        openalex_client, "search_by_title",
        lambda *a, **k: [w for w in _OPENALEX_RESULTS if w["id"] != "W3"],
    )
    preprint = Record(
        key="Arminio2025-tw", title="Leveraging VLLMs for Visual Clustering",
        authors=["Luigi Arminio"], doi="10.31235/osf.io/bf459",
    )
    assert openalex_client.find_published_version(preprint) is None


# --- the update wiring -----------------------------------------------------


def _write_summary(summaries_dir, record):
    """The abstract a vault note contributes comes from its structured summary."""
    summaries_dir.mkdir(parents=True, exist_ok=True)
    (summaries_dir / f"{record.key}.json").write_text(
        json.dumps({"abstract": record.abstract or "", "pdf_source": "abstract_only"}),
        encoding="utf-8",
    )


def _cfg(tmp_path):
    return {
        "vault": {"path": str(tmp_path), "papers_dir": "Papers"},
        "supersede": {"enabled": True, "max_adjudications_per_run": 5},
    }


def _paper(record):
    from src.feed_client import Paper

    return Paper(
        id=record.paper_id, title=record.title, authors=list(record.authors),
        abstract=record.abstract, doi=record.doi, url=record.url,
        journal=record.journal, date_published=record.year,
        discovery_date=record.discovery_date,
    )


def test_update_merges_an_arriving_published_version(tmp_path):
    """The published version arrives: incumbent becomes a stub, paper survives."""
    from src.main import _resolve_supersedes

    papers = tmp_path / "Papers"
    papers.mkdir()
    _write_note(papers, CIB)
    _write_summary(tmp_path / "summaries", CIB)
    state = {"papers": {CIB.paper_id: {"topics": ["t"], "note_path": "x"}}}
    claude = StubClaude({"same_work": True, "confidence": "high", "reason": "same study"})

    kept, supersedes_map, inherit_podcast, merged = _resolve_supersedes(
        _cfg(tmp_path), state, [_paper(APPEL)], claude,
        str(tmp_path), "Papers", str(tmp_path / "summaries"),
    )

    assert [p.bibtex_key for p in kept] == [APPEL.key]      # still processed
    assert supersedes_map == {APPEL.key: CIB.key}
    assert merged == [(CIB.key, APPEL.key)]
    # The episode on the note being replaced is carried over.
    assert inherit_podcast == {APPEL.key: "https://example.org/ep.mp3"}
    assert state["papers"][CIB.paper_id]["superseded_by"] == APPEL.paper_id
    assert state["papers"][CIB.paper_id]["topics"] == []
    stub = supersede.read_frontmatter((papers / f"{CIB.key}.md").read_text())
    assert stub["superseded_by"] == APPEL.key


def test_update_tombstones_a_late_arriving_preprint(tmp_path):
    """Decision 10: publication status decides, so the incumbent keeps its note."""
    from src.main import _resolve_supersedes

    papers = tmp_path / "Papers"
    papers.mkdir()
    _write_note(papers, APPEL, body="## Summary\n\nExpensive LLM prose.\n")
    before = (papers / f"{APPEL.key}.md").read_text(encoding="utf-8")

    late = Record(key="Late2026-zz", title=APPEL.title, authors=APPEL.authors,
                  doi="10.31235/osf.io/late", year="2026",
                  abstract=APPEL.abstract, discovery_date="2027-01-01T00:00:00Z")
    state = {"papers": {APPEL.paper_id: {"topics": ["t"]}}}
    claude = StubClaude({"same_work": True, "confidence": "high", "reason": "same"})

    kept, supersedes_map, _, merged = _resolve_supersedes(
        _cfg(tmp_path), state, [_paper(late)], claude,
        str(tmp_path), "Papers", str(tmp_path / "summaries"),
    )

    assert kept == []                       # never summarized, never posted
    assert merged == [(late.key, APPEL.key)]
    assert supersedes_map == {}             # the incumbent is not re-rendered
    assert state["papers"][late.paper_id]["superseded_by"] == APPEL.paper_id
    assert state["papers"][late.paper_id]["slack_posted"] is True
    after = (papers / f"{APPEL.key}.md").read_text(encoding="utf-8")
    assert "Expensive LLM prose." in after
    assert supersede.read_frontmatter(after)["supersedes"] == late.key
    assert before.split("---\n", 2)[2] == after.split("---\n", 2)[2]


def test_update_keeps_an_unrelated_paper(tmp_path):
    from src.main import _resolve_supersedes

    papers = tmp_path / "Papers"
    papers.mkdir()
    _write_note(papers, BAKC_A)
    _write_summary(tmp_path / "summaries", BAKC_A)
    state = {"papers": {}}
    claude = StubClaude({"same_work": False, "confidence": "high", "reason": "distinct"})

    kept, supersedes_map, _, merged = _resolve_supersedes(
        _cfg(tmp_path), state, [_paper(BAKC_B)], claude,
        str(tmp_path), "Papers", str(tmp_path / "summaries"),
    )
    assert [p.bibtex_key for p in kept] == [BAKC_B.key]
    assert (supersedes_map, merged) == ({}, [])


def test_update_respects_the_adjudication_budget(tmp_path):
    """A run must not be able to spend unbounded Claude calls on matching."""
    from src.main import _resolve_supersedes

    papers = tmp_path / "Papers"
    papers.mkdir()
    _write_note(papers, CIB)
    _write_summary(tmp_path / "summaries", CIB)
    cfg = _cfg(tmp_path)
    cfg["supersede"]["max_adjudications_per_run"] = 0
    claude = StubClaude({"same_work": True, "confidence": "high", "reason": "same"})

    kept, _, _, merged = _resolve_supersedes(
        cfg, {"papers": {}}, [_paper(APPEL)], claude,
        str(tmp_path), "Papers", str(tmp_path / "summaries"),
    )
    assert claude.calls == 0
    assert merged == [] and [p.bibtex_key for p in kept] == [APPEL.key]


def test_update_can_be_disabled(tmp_path):
    from src.main import _resolve_supersedes

    cfg = _cfg(tmp_path)
    cfg["supersede"]["enabled"] = False
    papers = [_paper(APPEL)]
    kept, sm, ip, merged = _resolve_supersedes(
        cfg, {"papers": {}}, papers, StubClaude({}),
        str(tmp_path), "Papers", str(tmp_path / "summaries"),
    )
    assert kept == papers and (sm, ip, merged) == ({}, {}, [])


def test_openalex_network_failure_is_not_fatal(monkeypatch):
    import requests

    from src import openalex_client

    def boom(*a, **k):
        raise requests.RequestException("no network")

    monkeypatch.setattr(openalex_client.requests, "get", boom)
    assert openalex_client.search_by_title("some long enough title here") == []
