#!/usr/bin/env python3
"""
index_kasten.py — build a machine-readable map of the fg-zettelkasten.

Pure standard library: runs the instant the repo is cloned, no pip installs.

It reads the vault (Papers / Topics / Structures markdown + frontmatter) and the
structured data/summaries/*.json, builds the [[wikilink]] citation graph, scores
each paper for "register-crossing" (the Luhmann serendipity signal), and writes:

  index.json      one bundled object the assistant reads to plan an outline
  papers.csv      node table  -> igraph vertices
  edges.csv       link table  -> igraph edges  (cross_topic flag included)
  topics.csv      topic registers + paper counts
  structures.csv  the pre-written argument threads (slug, topic, path)
  bridges.csv     ranked register-crossing papers  (fuel for "cross the registers")
  crossings.csv   the actual cross-topic linked PAIRS (the "box surprised me" list)

The CSVs are deliberately flat so the analysis layer can be done in R:
    library(igraph); library(readr)
    nodes <- read_csv("kasten_index/papers.csv")
    edges <- read_csv("kasten_index/edges.csv")
    g <- graph_from_data_frame(edges, vertices = nodes, directed = TRUE)

Usage:
    python3 index_kasten.py                       # clone fresh, index, write ./kasten_index
    python3 index_kasten.py --out-dir /path/out
    python3 index_kasten.py --vault-path /path/to/repo --skip-clone   # index a local clone
    python3 index_kasten.py --repo-url <url> --clone-dir /tmp
"""

import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import sys
from collections import defaultdict, Counter

DEFAULT_REPO = "https://github.com/fabiogiglietto/fg-zettelkasten.git"
WIKILINK = re.compile(r"\[\[([^\]|#]+)")  # [[id]], [[id|alias]], [[id#section]]


# --------------------------------------------------------------------------- #
# clone / locate
# --------------------------------------------------------------------------- #
def clone_or_update(repo_url, clone_dir):
    """Fresh shallow clone each run (pull if it already exists)."""
    dest = os.path.join(clone_dir, "fg-zettelkasten")
    if os.path.isdir(os.path.join(dest, ".git")):
        subprocess.run(["git", "-C", dest, "pull", "--ff-only", "--depth", "1"],
                       check=False, capture_output=True)
    else:
        shutil.rmtree(dest, ignore_errors=True)
        r = subprocess.run(["git", "clone", "--depth", "1", repo_url, dest],
                           capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit("git clone failed:\n" + r.stderr)
    return dest


def find_vault(root):
    """Accept either a repo root (containing vault/) or the vault/ dir itself."""
    for cand in (os.path.join(root, "vault"), root):
        if all(os.path.isdir(os.path.join(cand, d))
               for d in ("Papers", "Topics", "Structures")):
            return cand
    sys.exit(f"Could not find vault/{{Papers,Topics,Structures}} under {root}")


# --------------------------------------------------------------------------- #
# minimal, dependency-free frontmatter parser
# handles: scalars, "quoted" scalars, inline arrays [a, "b c"], ints, bools
# --------------------------------------------------------------------------- #
def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block, body = text[3:end], text[end + 4:]
    meta = {}
    for line in block.splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, _, val = line.partition(":")
        meta[key.strip()] = _coerce(val.strip())
    return meta, body


def _coerce(val):
    if val == "":
        return None
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        if not inner:
            return []
        return [_unquote(x.strip()) for x in _split_top_commas(inner)]
    if val.lower() in ("true", "false"):
        return val.lower() == "true"
    if re.fullmatch(r"-?\d+", val):
        return int(val)
    return _unquote(val)


def _unquote(s):
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


def _split_top_commas(s):
    out, depth, buf, q = [], 0, [], None
    for ch in s:
        if q:
            buf.append(ch)
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch
            buf.append(ch)
        elif ch in "[(":
            depth += 1; buf.append(ch)
        elif ch in "])":
            depth -= 1; buf.append(ch)
        elif ch == "," and depth == 0:
            out.append("".join(buf)); buf = []
        else:
            buf.append(ch)
    if buf:
        out.append("".join(buf))
    return out


# --------------------------------------------------------------------------- #
# build the index
# --------------------------------------------------------------------------- #
def build(vault, data_dir):
    papers = {}            # id -> record
    edges = []             # (src, dst)
    summaries_dir = os.path.join(data_dir, "summaries") if data_dir else None

    for fn in sorted(os.listdir(os.path.join(vault, "Papers"))):
        if not fn.endswith(".md"):
            continue
        pid = fn[:-3]
        text = _read(os.path.join(vault, "Papers", fn))
        meta, body = parse_frontmatter(text)
        key = meta.get("bibtex_key") or pid
        links = [m.strip() for m in WIKILINK.findall(body)]
        summary = _load_summary(summaries_dir, key, pid)
        papers[key] = {
            "id": key,
            "file": fn,
            "title": meta.get("title") or pid,
            "authors": meta.get("authors") or [],
            "year": meta.get("year"),
            "doi": meta.get("doi"),
            "topics": meta.get("topics") or [],
            "citation_count": meta.get("citation_count"),
            "source_url": meta.get("source_url"),
            "links_out": links,
            "has_summary": summary is not None,
            "key_claims": (summary or {}).get("key_claims", [])[:5],
        }
        for tgt in links:
            edges.append((key, tgt))

    # topics
    topics = {}
    tj = os.path.join(data_dir, "topics.json") if data_dir else None
    if tj and os.path.isfile(tj):
        for t in json.loads(_read(tj)):
            topics[t["slug"]] = {"slug": t["slug"], "name": t.get("name", t["slug"]),
                                 "description": t.get("description", ""), "n_papers": 0}
    topic_members = defaultdict(set)
    for p in papers.values():
        for slug in p["topics"]:
            topic_members[slug].add(p["id"])
            topics.setdefault(slug, {"slug": slug, "name": slug, "description": "", "n_papers": 0})
    for slug, members in topic_members.items():
        topics[slug]["n_papers"] = len(members)

    # structures
    structures = []
    for fn in sorted(os.listdir(os.path.join(vault, "Structures"))):
        if not fn.endswith(".md"):
            continue
        meta, _ = parse_frontmatter(_read(os.path.join(vault, "Structures", fn)))
        structures.append({"slug": meta.get("slug", fn[:-3]),
                            "topic": meta.get("topic", ""),
                            "path": os.path.join("vault", "Structures", fn)})

    _annotate_graph(papers, edges, topic_members)
    build.name_warnings = _resolve_first_authors(papers)
    crossings = _crossings(papers, edges)
    return papers, edges, topics, structures, crossings


def _resolve_first_authors(papers):
    """Robustly determine each paper's first-author SURNAME and flag uncertain
    orderings. Targets the failure modes seen in this corpus:
      (a) surname-first storage without a comma ("Marino Giada") -> caught by
          comparing against the MAJORITY ordering of that same person across all
          notes (she is "Giada Marino" in ~40 notes, "Marino Giada" in 1);
      (b) surname-first with a comma ("Vincent, Emmanuel") -> comma is explicit;
      (c) the auto-generated bibtex_key encoding a GIVEN name ("Philipp2026" for
          "Philipp Darius") -> caught when key == folded(first token) != surname.
    Diacritics and lowercase name particles (van, de, di ...) are folded/absorbed
    so accented and particle surnames (Toernberg, van Erkel) are NOT false-flagged.
    Returns [(id, stored_first_author, resolved_surname, reason), ...].
    """
    import unicodedata
    def fold(t):
        t = unicodedata.normalize("NFKD", t or "")
        t = "".join(c for c in t if not unicodedata.combining(c))
        return t.lower().strip(".,")
    def toks(name):
        return [t for t in re.split(r"\s+", (name or "").strip()) if t]
    PARTICLES = {"van","von","de","del","della","der","di","da","dos","das",
                 "la","le","du","den","ten","ter","al","bin","ibn","san","st"}

    registry = defaultdict(Counter)
    for p in papers.values():
        for a in p.get("authors") or []:
            if "," in a:            # comma names are unambiguous; skip registry
                continue
            ts = toks(a)
            if len(ts) >= 2:
                registry[frozenset(fold(t) for t in ts)][tuple(ts)] += 1

    def surname_from_order(ordering):
        ts = list(ordering)
        s = ts[-1]
        if len(ts) >= 2 and fold(ts[-2]) in PARTICLES:
            s = ts[-2] + " " + s
        return s

    warnings = []
    for pid, p in papers.items():
        p["first_author_surname"] = None
        p["citation_label"] = None
        p["name_order_uncertain"] = False
        authors = p.get("authors") or []
        if not authors:
            continue
        a0 = authors[0]
        reason = []
        if "," in a0:                       # "Surname, Given" -> surname-first
            surname = a0.split(",")[0].strip()
            if not fold(pid).startswith(fold(surname.split()[-1])):
                reason.append("first author stored surname-first (comma form)")
        else:
            ts = toks(a0)
            if len(ts) == 1:
                surname = ts[0]
            else:
                canon = registry[frozenset(fold(t) for t in ts)].most_common(1)[0][0]
                surname = surname_from_order(canon)
                if tuple(fold(t) for t in ts) != tuple(fold(t) for t in canon):
                    reason.append("first author stored in minority order vs. rest of corpus")
                m = re.match(r"([A-Za-z]+)", pid)
                keytok = m.group(1).lower() if m else ""
                if keytok and keytok == fold(ts[0]) and keytok != fold(surname.split()[-1]) \
                        and fold(ts[0]) not in PARTICLES:
                    reason.append('bibtex-key token "%s" is the given name, not the surname "%s"' % (keytok, surname))
        p["first_author_surname"] = surname
        label = surname if len(authors) == 1 else surname + " et al."
        p["citation_label"] = (label + ", " + str(p["year"])) if p.get("year") else label
        if reason:
            p["name_order_uncertain"] = True
            warnings.append((pid, a0, surname, "; ".join(reason)))
    return warnings


def _annotate_graph(papers, edges, topic_members):
    indeg, outdeg = defaultdict(int), defaultdict(int)
    for s, t in edges:
        outdeg[s] += 1
        indeg[t] += 1
    topic_of = {pid: set(p["topics"]) for pid, p in papers.items()}
    for pid, p in papers.items():
        my_topics = topic_of.get(pid, set())
        foreign = set()
        for tgt in p["links_out"]:
            if tgt in topic_of:
                foreign |= (topic_of[tgt] - my_topics)
        # bridge_score: how far this note reaches across the register system
        p["n_topics"] = len(my_topics)
        p["links_in"] = indeg[pid]
        p["links_out_n"] = outdeg[pid]
        p["foreign_topics_reached"] = len(foreign)
        p["bridge_score"] = (max(0, len(my_topics) - 1)) + len(foreign)


def _crossings(papers, edges):
    topic_of = {pid: set(p["topics"]) for pid, p in papers.items()}
    seen, out = set(), []
    for s, t in edges:
        if t not in papers:           # dangling link (e.g. own-pub not in vault)
            continue
        st, tt = topic_of.get(s, set()), topic_of.get(t, set())
        if st and tt and not (st & tt):   # linked but share NO topic = surprising
            keypair = tuple(sorted((s, t)))
            if keypair in seen:
                continue
            seen.add(keypair)
            out.append({"source": s, "target": t,
                        "source_topics": "|".join(sorted(st)),
                        "target_topics": "|".join(sorted(tt))})
    return out


def _load_summary(sdir, key, pid):
    if not sdir:
        return None
    for cand in (key, pid):
        path = os.path.join(sdir, cand + ".json")
        if os.path.isfile(path):
            try:
                return json.loads(_read(path))
            except Exception:
                return None
    return None


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


# --------------------------------------------------------------------------- #
# emit
# --------------------------------------------------------------------------- #
def write_outputs(out_dir, papers, edges, topics, structures, crossings):
    os.makedirs(out_dir, exist_ok=True)
    topic_of = {pid: set(p["topics"]) for pid, p in papers.items()}

    with open(os.path.join(out_dir, "papers.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "title", "authors", "year", "doi", "topics",
                    "n_topics", "citation_count", "links_out", "links_in",
                    "foreign_topics_reached", "bridge_score", "has_summary",
                    "citation_label", "first_author_surname", "name_order_uncertain"])
        for p in sorted(papers.values(), key=lambda x: -x["bridge_score"]):
            w.writerow([p["id"], p["title"], "; ".join(p["authors"]), p["year"],
                        p["doi"], "|".join(p["topics"]), p["n_topics"],
                        p["citation_count"], p["links_out_n"], p["links_in"],
                        p["foreign_topics_reached"], p["bridge_score"],
                        int(p["has_summary"]), p.get("citation_label"),
                        p.get("first_author_surname"),
                        int(bool(p.get("name_order_uncertain")))])

    with open(os.path.join(out_dir, "edges.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["source", "target", "target_in_vault", "cross_topic"])
        for s, t in edges:
            st, tt = topic_of.get(s, set()), topic_of.get(t, set())
            cross = bool(st and tt and not (st & tt))
            w.writerow([s, t, int(t in papers), int(cross)])

    with open(os.path.join(out_dir, "topics.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["slug", "name", "n_papers", "description"])
        for t in sorted(topics.values(), key=lambda x: -x["n_papers"]):
            w.writerow([t["slug"], t["name"], t["n_papers"], t["description"]])

    with open(os.path.join(out_dir, "structures.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["slug", "topic", "path"])
        for s in structures:
            w.writerow([s["slug"], s["topic"], s["path"]])

    with open(os.path.join(out_dir, "bridges.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "title", "topics", "bridge_score", "foreign_topics_reached"])
        ranked = sorted((p for p in papers.values() if p["bridge_score"] > 0),
                        key=lambda x: -x["bridge_score"])
        for p in ranked:
            w.writerow([p["id"], p["title"], "|".join(p["topics"]),
                        p["bridge_score"], p["foreign_topics_reached"]])

    with open(os.path.join(out_dir, "crossings.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["source", "target", "source_topics", "target_topics"])
        for c in crossings:
            w.writerow([c["source"], c["target"], c["source_topics"], c["target_topics"]])

    # lean bundle for the assistant (no heavy abstract/findings text)
    index = {
        "n_papers": len(papers),
        "n_topics": len(topics),
        "n_structures": len(structures),
        "n_edges": len(edges),
        "n_crossings": len(crossings),
        "topics": sorted(topics.values(), key=lambda x: -x["n_papers"]),
        "structures": structures,
        "papers": {pid: {k: p[k] for k in
                         ("title", "authors", "year", "doi", "topics",
                          "bridge_score", "links_in", "key_claims",
                          "citation_label", "first_author_surname",
                          "name_order_uncertain")}
                   for pid, p in papers.items()},
    }
    with open(os.path.join(out_dir, "index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=1)
    return index


# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo-url", default=DEFAULT_REPO)
    ap.add_argument("--clone-dir", default="/tmp")
    ap.add_argument("--vault-path", help="repo root or vault dir of an existing clone")
    ap.add_argument("--skip-clone", action="store_true")
    ap.add_argument("--out-dir", default="kasten_index")
    args = ap.parse_args()

    if args.skip_clone or args.vault_path:
        root = args.vault_path or os.path.join(args.clone_dir, "fg-zettelkasten")
    else:
        root = clone_or_update(args.repo_url, args.clone_dir)

    vault = find_vault(root)
    repo_root = os.path.dirname(vault) if os.path.basename(vault) == "vault" else vault
    data_dir = os.path.join(repo_root, "data")
    data_dir = data_dir if os.path.isdir(data_dir) else None

    papers, edges, topics, structures, crossings = build(vault, data_dir)
    index = write_outputs(args.out_dir, papers, edges, topics, structures, crossings)

    dangling = sum(1 for _, t in edges if t not in papers)
    print(f"indexed: {index['n_papers']} papers · {index['n_topics']} topics · "
          f"{index['n_structures']} structures")
    print(f"graph:   {index['n_edges']} links ({dangling} dangling) · "
          f"{index['n_crossings']} cross-topic pairs")
    warns = getattr(build, "name_warnings", [])
    if warns:
        print(f"name checks: {len(warns)} first-author name(s) flagged for review:")
        for pid, stored, surname, why in warns:
            print(f"   ⚠ {pid}: stored \"{stored}\" -> cite as \"{surname}\" ({why})")
    else:
        print("name checks: 0 flagged")
    print(f"written: {os.path.abspath(args.out_dir)}/  "
          f"(index.json, papers.csv, edges.csv, topics.csv, structures.csv, "
          f"bridges.csv, crossings.csv)")


if __name__ == "__main__":
    main()
