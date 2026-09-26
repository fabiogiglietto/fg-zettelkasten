"""Drive PDF matching.

Focus: the bibkey-prefix match that makes PDF retrieval independent of upstream
metadata enrichment (toread issue #13). Before it, a Slack submission whose
enrichment failed was uploaded as `Unknown - untitled.pdf` and could never be
matched back — the title-token gate has nothing to work with — so the rebuilt
note fell back to `pdf_source=abstract_only` despite a valid full text sitting
in the inbox folder.
"""

from src.drive_client import DriveClient
from src.feed_client import Paper


def _client(files):
    """A DriveClient with no credentials and a canned folder listing."""
    client = DriveClient.__new__(DriveClient)
    client.folder_ids = ["folder"]
    client._file_cache = {}
    client._list_folder_files = lambda: list(files)
    return client


def _file(name):
    return {"id": f"id-{name}", "name": name, "size": "1024"}


PAPERPILE = _file("Esposito 2025 - Beyond Artificial Intelligence.pdf")
SLACK = _file("Slack1783075716-sl1c - Esposito 2025 - Beyond Artificial Intelligence.pdf")
UNTITLED = _file("Slack1783075716-sl1c - Unknown - untitled.pdf")


def test_titleless_paper_matches_on_bibkey():
    """The issue's case. With no title there are no tokens to gate on, so this
    is the only signal left — and it has to work."""
    client = _client([_file("Some Other Paper 2020 - Unrelated.pdf"), UNTITLED])
    paper = Paper(id="bibtex:Slack1783075716-sl1c", title="")

    assert client.find_pdf(paper) == UNTITLED


def test_titleless_paper_without_bibkey_file_still_returns_none():
    """Guard against over-matching: no bibkey file means no match, not a
    wrong one."""
    client = _client([PAPERPILE])
    paper = Paper(id="bibtex:Slack1783075716-sl1c", title="")

    assert client.find_pdf(paper) is None


def test_bibkey_match_is_case_insensitive():
    client = _client([_file("slack1783075716-SL1C - Whatever.pdf")])
    paper = Paper(id="bibtex:Slack1783075716-sl1c", title="")

    assert client.find_pdf(paper) is not None


def test_bibkey_prefix_does_not_match_a_longer_sibling_key():
    """`Foo2025-ab` must not claim `Foo2025-abc`'s file. The ' - ' separator is
    what makes the prefix unambiguous."""
    client = _client([_file("Foo2025-abc - Smith 2025 - Another Paper.pdf")])
    paper = Paper(id="bibtex:Foo2025-ab", title="")

    assert client.find_pdf(paper) is None


def test_paperpile_exact_match_still_works():
    """Backward compatibility: Paperpile uploads carry no bibkey prefix and are
    matched on the author/year/title name as before."""
    client = _client([PAPERPILE])
    paper = Paper(
        id="bibtex:Esposito2025-zz",
        title="Beyond Artificial Intelligence",
        authors=["Elena Esposito"],
        date_published="2025-07-10",
    )

    assert client.find_pdf(paper) == PAPERPILE


def test_token_matching_still_works():
    """The 0.6 title-overlap path is untouched for files that match neither the
    bibkey prefix nor the exact name."""
    client = _client([_file("Esposito 2025 - Beyond Artificial Intelligence and Beyond.pdf")])
    paper = Paper(
        id="bibtex:Esposito2025-zz",
        title="Beyond Artificial Intelligence",
        authors=["Elena Esposito"],
        date_published="2025-07-10",
    )

    assert client.find_pdf(paper) is not None


def test_bibkey_wins_over_a_token_match_on_another_file():
    """When both are present the bibkey is the stronger signal: it identifies
    the exact record, while token overlap only says the titles look alike."""
    sibling = _file("Esposito 2025 - Beyond Artificial Intelligence.pdf")
    client = _client([sibling, SLACK])
    paper = Paper(
        id="bibtex:Slack1783075716-sl1c",
        title="Beyond Artificial Intelligence",
        authors=["Elena Esposito"],
        date_published="2025-07-10",
    )

    assert client.find_pdf(paper) == SLACK


# --- title overlap needs author or year ------------------------------------
# Real failure (2026-09-26): the classics' PDFs sat in a folder the kasten did
# not search, and short generic titles cleared the 0.6 gate against unrelated
# papers already in Drive — Lazer 2018 "The science of fake news" was
# summarized from an Italian study of the "fake news" label.

ITALIAN = _file("Rossi et al. - 2025 - Fake news as a label in Italian political "
                "news science and strategy.pdf")
LAZER = Paper(
    id="bibtex:Lazer2018-mm",
    title="The science of fake news",
    authors=["David M. J. Lazer"],
    date_published="2018-03-09",
)


def test_a_generic_title_does_not_match_another_authors_paper():
    assert _client([ITALIAN]).find_pdf(LAZER) is None


def test_the_right_file_still_matches_on_title_plus_surname():
    right = _file("Lazer et al. - 2018 - The science of fake news.pdf")
    assert _client([ITALIAN, right]).find_pdf(LAZER) == right


def test_year_alone_is_enough_when_the_surname_differs():
    """Name-order slips ("Marino Giada") must not lose a correct match."""
    paper = Paper(id="bibtex:Marino2024-aa", title="Coordinated sharing behaviour",
                  authors=["Marino Giada"], date_published="2024-05-01")
    f = _file("Giada et al. - 2024 - Coordinated sharing behaviour on Facebook.pdf")
    assert _client([f]).find_pdf(paper) == f


def test_accented_surname_matches_a_folded_filename():
    paper = Paper(id="bibtex:Gonzalez-Bailon2023-uy",
                  title="Asymmetric ideological segregation in exposure to political news",
                  authors=["Sandra González-Bailón"], date_published="2023-07-27")
    f = _file("Gonzalez-Bailon et al. - 2023 - Asymmetric ideological segregation in "
              "exposure to political news on Facebook.pdf")
    assert _client([f]).find_pdf(paper) == f
