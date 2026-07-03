"""Tests for src.state duplicate detection (normalizers + indexes)."""
from src.state import (
    dedup_index,
    dedup_index_from_notes,
    find_duplicate,
    normalize_doi,
    normalize_title,
)


def test_normalize_doi_strips_prefix_and_case():
    assert normalize_doi("https://doi.org/10.1234/AbC.5") == "10.1234/abc.5"
    assert normalize_doi("dx.doi.org/10.1/x.") == "10.1/x"
    assert normalize_doi("10.1/x") == "10.1/x"
    assert normalize_doi(None) is None
    assert normalize_doi("") is None


def test_normalize_title_folds_accents_and_punctuation():
    a = normalize_title("Törnberg: “When do parties lie?”")
    b = normalize_title("Tornberg   when do parties lie")
    assert a == b


def test_normalize_title_rejects_too_short():
    assert normalize_title("short") is None
    assert normalize_title(None) is None


def test_dedup_index_and_find_duplicate():
    state = {
        "papers": {
            "bibtex:Boyd2026-pm": {
                "doi": "10.1/known", "title": "A Paper Already Archived",
            },
            "bibtex:NoMeta2020-aa": {},  # pre-dedup entry: contributes nothing
        }
    }
    idx = dedup_index(state)
    assert find_duplicate(idx, "https://doi.org/10.1/KNOWN", None) == "bibtex:Boyd2026-pm"
    assert find_duplicate(idx, None, "a paper already archived!") == "bibtex:Boyd2026-pm"
    assert find_duplicate(idx, "10.9/other", "something else entirely") is None


def test_doi_match_wins_over_title():
    state = {
        "papers": {
            "bibtex:A2026-aa": {"doi": "10.1/a", "title": "Shared Title Of Paper"},
            "bibtex:B2026-bb": {"doi": "10.1/b", "title": "Another Title Of Paper"},
        }
    }
    idx = dedup_index(state)
    # DOI says B even though the title matches A.
    assert find_duplicate(idx, "10.1/b", "Shared Title Of Paper") == "bibtex:B2026-bb"


def test_dedup_index_from_notes_reads_frontmatter(tmp_path):
    """Covers the seeded corpus whose state entries predate doi/title fields."""
    (tmp_path / "Seed2020-xx.md").write_text(
        "---\n"
        'title: "A Seeded Corpus Paper"\n'
        "doi: 10.5/seed\n"
        "bibtex_key: Seed2020-xx\n"
        "---\n\nBody.\n",
        encoding="utf-8",
    )
    (tmp_path / "broken.md").write_text("no frontmatter here", encoding="utf-8")
    idx = dedup_index_from_notes(tmp_path)
    assert find_duplicate(idx, "10.5/seed", None) == "bibtex:Seed2020-xx"
    assert find_duplicate(idx, None, "a seeded corpus paper") == "bibtex:Seed2020-xx"


def test_dedup_index_from_notes_missing_dir():
    assert dedup_index_from_notes("/nonexistent/nowhere") == {}
