"""Tests for scripts/build_skill_bundle.py — the zettel-paper upload bundle."""
import zipfile

import pytest

from scripts.build_skill_bundle import SOURCE, build

FG = {
    "name": "zettel-paper",
    "repo": "fabiogiglietto/fg-zettelkasten",
    "owner": "Fabio Giglietto's",
    "bundle": "bundle.zip",
}
MINE = {
    "name": "mine-zettel-paper",
    "repo": "fabiogiglietto/mine-zettelkasten",
    "owner": "the MINE team's",
    "bundle": "bundle.zip",
}


def _read(zip_path):
    with zipfile.ZipFile(zip_path) as zf:
        return {n: zf.read(n) for n in zf.namelist()}


def test_fg_config_bundles_the_source_verbatim(tmp_path):
    files = _read(build(FG, root=tmp_path))
    src = {
        f"zettel-paper/{p.relative_to(SOURCE).as_posix()}": p.read_bytes()
        for p in SOURCE.rglob("*")
        if p.is_file() and "__pycache__" not in p.parts
        and not any(part.startswith(".") for part in p.relative_to(SOURCE).parts)
    }
    assert files == src


def test_rebuild_is_byte_identical(tmp_path):
    a = build(FG, root=tmp_path).read_bytes()
    b = build(FG, root=tmp_path).read_bytes()
    assert a == b


def test_fork_config_retargets_the_skill(tmp_path):
    files = _read(build(MINE, root=tmp_path))
    assert all(n.startswith("mine-zettel-paper/") for n in files)
    skill_md = files["mine-zettel-paper/SKILL.md"].decode()
    assert "\nname: mine-zettel-paper\n" in skill_md
    assert "\n# mine-zettel-paper\n" in skill_md
    assert "FROM the MINE team's mine-zettelkasten" in skill_md
    assert "github.com/fabiogiglietto/mine-zettelkasten" in skill_md
    indexer = files["mine-zettel-paper/scripts/index_kasten.py"].decode()
    assert ('DEFAULT_REPO = "https://github.com/fabiogiglietto/'
            'mine-zettelkasten.git"') in indexer
    for name, data in files.items():
        text = data.decode()
        assert "fg-zettelkasten" not in text, name
        assert "Fabio Giglietto's" not in text, name


def test_invalid_skill_name_is_rejected(tmp_path):
    with pytest.raises(ValueError):
        build({**MINE, "name": "MINE Zettel"}, root=tmp_path)
