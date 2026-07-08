"""Tests for the APA author formatter (comma-format names included)."""
from src.note_builder import _format_author, _format_authors


def test_natural_order_name():
    assert _format_author("Eytan Bakshy") == "Bakshy, E."
    assert _format_author("Lada A. Adamic") == "Adamic, L. A."


def test_nobiliary_particles():
    assert _format_author("Claes H. de Vreese") == "de Vreese, C. H."


def test_comma_format_name():
    # Some feed sources deliver "Family, Given" (e.g. OpenAlex author
    # entities seeded from repository deposits).
    assert _format_author("Righetti, Nicola") == "Righetti, N."
    assert _format_author("Adamic, Lada A.") == "Adamic, L. A."


def test_single_token_and_degenerate():
    assert _format_author("Cher") == "Cher"
    assert _format_author("") == ""


def test_author_list_joining():
    out = _format_authors(["Righetti, Nicola", "Fabio Giglietto"])
    assert out == "Righetti, N., & Giglietto, F."
