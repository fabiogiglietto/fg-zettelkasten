"""Build the zettel-paper upload bundle from `.claude/skills/zettel-paper/`.

The skill source is written for this repo. A fork (mine-zettelkasten) needs a
skill that clones *its* kasten and can be installed next to this one, so the
bundle is rendered from the `skill:` block of config.yml:

- the skill folder and frontmatter `name` become `skill.name`
- `github.com/fabiogiglietto/fg-zettelkasten` becomes `github.com/<skill.repo>`
- "Fabio Giglietto's" in front of the repo name becomes `skill.owner`
- every other `fg-zettelkasten` becomes the repo name (e.g. the indexer's
  DEFAULT_REPO and clone directory)
- the Drive folders of the full-text path (`references/fulltext-access.md`,
  between the `fulltext-folders` markers) become `skill.fulltext_folders`

With this repo's own values every rewrite is the identity, so the bundle holds
the source verbatim. Entries carry a fixed timestamp and a sorted order, so an
unchanged skill rebuilds to identical bytes and CI commits nothing.

Run from the repo root:  python -m scripts.build_skill_bundle
"""
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / ".claude" / "skills" / "zettel-paper"

SOURCE_NAME = "zettel-paper"
SOURCE_REPO = "fabiogiglietto/fg-zettelkasten"
SOURCE_OWNER = "Fabio Giglietto's"

# Agent Skills spec: lowercase letters, digits and hyphens, at most 64 chars;
# the description is capped at 1024.
_NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
_DESCRIPTION_MAX = 1024
_TEXT_SUFFIXES = {".md", ".py", ".txt", ".json", ".csv", ".yml", ".yaml"}
_ZIP_DATE = (1980, 1, 1, 0, 0, 0)

FULLTEXT_DOC = "references/fulltext-access.md"
_FOLDERS_BLOCK = re.compile(
    r"(<!-- fulltext-folders:start -->\n).*?(\n<!-- fulltext-folders:end -->)",
    re.DOTALL,
)
_FILENAMES = {
    "paperpile": "Paperpile (`Author [et al.] Year - Title.pdf`)",
    "bibkey": "Slack inbox (`bibtex_key - Author [et al.] Year - Title.pdf`)",
}


def render_folders(folders: list[dict]) -> str:
    """The folder table the full-text path searches, from `skill.fulltext_folders`."""
    if not folders:
        return ("No Drive folders are configured for this kasten, so there is no "
                "full-text path: say so and stay on the summaries.")
    lines = ["| folder | id | filenames |", "|---|---|---|"]
    for f in folders:
        kind = f.get("filenames", "paperpile")
        if kind not in _FILENAMES:
            raise ValueError(f"fulltext folder {f.get('label')!r}: filenames "
                             f"must be one of {sorted(_FILENAMES)}")
        lines.append(f"| {f['label']} | `{f['id']}` | {_FILENAMES[kind]} |")
    return "\n".join(lines)


def set_folders(text: str, folders: list[dict]) -> str:
    """Replace the generated folder block in fulltext-access.md."""
    if not _FOLDERS_BLOCK.search(text):
        raise ValueError(f"{FULLTEXT_DOC}: fulltext-folders markers missing")
    return _FOLDERS_BLOCK.sub(
        lambda m: m.group(1) + render_folders(folders) + m.group(2), text)


def rewrite(text: str, name: str, repo: str, owner: str) -> str:
    """Retarget one skill file from this repo to `repo` under skill `name`."""
    repo_name = repo.rsplit("/", 1)[-1]
    source_repo_name = SOURCE_REPO.rsplit("/", 1)[-1]
    text = text.replace(f"github.com/{SOURCE_REPO}", f"github.com/{repo}")
    text = text.replace(f"{SOURCE_OWNER} {source_repo_name}",
                        f"{owner} {repo_name}")
    text = text.replace(source_repo_name, repo_name)
    text = re.sub(rf"^name: {SOURCE_NAME}$", f"name: {name}", text,
                  count=1, flags=re.MULTILINE)
    text = re.sub(rf"^# {SOURCE_NAME}$", f"# {name}", text,
                  count=1, flags=re.MULTILINE)
    return text


def _description(skill_md: str) -> str:
    front = skill_md.split("---", 2)[1]
    return str(yaml.safe_load(front).get("description", ""))


def build(skill_cfg: dict, source: Path = SOURCE, root: Path = ROOT) -> Path:
    """Write the bundle named by `skill_cfg["bundle"]` under `root`; return its path."""
    name = skill_cfg.get("name", SOURCE_NAME)
    repo = skill_cfg.get("repo", SOURCE_REPO)
    owner = skill_cfg.get("owner", SOURCE_OWNER)
    if not _NAME_RE.match(name) or len(name) > 64:
        raise ValueError(f"skill.name {name!r}: use lowercase letters, digits, hyphens")

    files: dict[str, bytes] = {}
    for path in sorted(source.rglob("*")):
        rel = path.relative_to(source)
        if not path.is_file() or any(p.startswith(".") or p == "__pycache__"
                                     for p in rel.parts):
            continue
        data = path.read_bytes()
        if path.suffix in _TEXT_SUFFIXES:
            text = rewrite(data.decode("utf-8"), name, repo, owner)
            if rel.as_posix() == FULLTEXT_DOC and "fulltext_folders" in skill_cfg:
                text = set_folders(text, skill_cfg["fulltext_folders"] or [])
            data = text.encode("utf-8")
        files[f"{name}/{rel.as_posix()}"] = data

    description = _description(files[f"{name}/SKILL.md"].decode("utf-8"))
    if len(description) > _DESCRIPTION_MAX:
        raise ValueError(f"SKILL.md description is {len(description)} chars "
                         f"(max {_DESCRIPTION_MAX})")

    out = root / skill_cfg.get("bundle", "zettel-paper-skill.zip")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for arcname, data in files.items():
            info = zipfile.ZipInfo(arcname, date_time=_ZIP_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, data)
    return out


def main() -> int:
    cfg = yaml.safe_load((ROOT / "config.yml").read_text(encoding="utf-8"))
    out = build(cfg.get("skill") or {})
    print(f"build_skill_bundle: wrote {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
