"""Assemble the course book — the lecture notes as one searchable Quarto book.

    python3 scripts/build_book.py
    scripts/render_book.sh            # assemble, then render into docs/book/

The book is a *derived* artefact. Nothing in book/ is authored: every chapter is
assembled from files that already exist, so the book cannot drift from the
repository the way a hand-maintained second copy would. Edit the session
README, the lecture notes or the practice brief, and rebuild.

The shape of a chapter
----------------------
One session is one chapter, and it holds the whole session:

    the session at a glance    question, big work, target figure, data, Tableau skill
    the chapter                long-form prose, authored in NN-slug/chapter.md
    ## In the practice         the practice-round brief (02-practice/README.md)

chapter.md is the session's lecture notes written as a book chapter, as in the
quantitative-methods course: front matter (`title:`), narrative `##` sections,
and the book's fenced divs (.definition, .archive, .lit, .step, .check, .warn).
Its citations ([@key]) resolve against NN-slug/chapter.bib; every session's bib
is merged into book/references.bib. A session without chapter.md falls back to
its structured notes: Before the session, The lecture, In the practice.

A student who searches "Herfindahl" should land once, on Session 11, and find
the concept, the reading and the exercise that uses it, in that order.
"""

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "book"
REPO = "warint/geopolitics-geoeconomics"
GH = f"https://github.com/{REPO}/blob/main/"
PAGES = f"https://warint.github.io/{REPO.split('/')[1]}/"
TITLE = "Geopolitical Risks and International Business"

# Top-level documents that become appendices, and the chapter each maps to.
APPENDICES = [
    ("replications.qmd", "The replications", "REPLICATIONS.md"),
    ("data-sources.qmd", "Data sources", "DATA-SOURCES.md"),
    ("tableau-toolkit.qmd", "The Tableau toolkit", "TABLEAU-TOOLKIT.md"),
    ("readings.qmd", "Readings", "READINGS.md"),
    ("assessment.qmd", "Assessment", "assessments/README.md"),
]
ASSESSMENT_BRIEFS = [
    ("Quizzes", "assessments/quizzes/README.md"),
    ("The Risk Brief", "assessments/risk-brief/README.md"),
    ("Team work", "assessments/team-project/README.md"),
    ("Take-home examination", "assessments/take-home/README.md"),
]
CHAPTER_LINKS = {f"{src}": qmd for qmd, _, src in APPENDICES}
for _, src in ASSESSMENT_BRIEFS:
    CHAPTER_LINKS[src] = "assessment.qmd"


def sessions():
    return sorted(p for p in ROOT.iterdir() if p.is_dir() and re.match(r"\d\d-", p.name))


# ---------------------------------------------------------------------------
# Fence-aware line walking: a `# comment` inside a code block is not a heading.
# ---------------------------------------------------------------------------
def walk(text):
    fence = None
    for line in text.split("\n"):
        m = re.match(r"^\s*(`{3,}|~{3,})", line)
        if m:
            if fence is None:
                fence = m.group(1)[0] * 3
            elif m.group(1).startswith(fence):
                fence = None
            yield line, True
            continue
        yield line, fence is not None


def shift_headings(text, by=1):
    out = []
    for line, code in walk(text):
        if not code and re.match(r"^#{1,5} ", line):
            line = "#" * by + line
        out.append(line)
    return "\n".join(out)


def drop_titles(text):
    """Remove the brief's own H1 lines (and a leading 'Slides:' pointer); the chapter supplies them."""
    out, started = [], False
    for line, code in walk(text):
        if not started and not code and (line.startswith("# ") or line.startswith("Slides:")):
            continue
        if line.strip():
            started = True
        out.append(line)
    return "\n".join(out).strip("\n")


# ---------------------------------------------------------------------------
# Links. Every source links relative to its own directory; flattened into
# book/, those paths point at nothing. Known targets become chapters or
# anchors; anything else goes to the file on GitHub, so a link degrades to
# "the file on GitHub" rather than to a 404.
# ---------------------------------------------------------------------------
def rewrite_links(text, source):
    src_dir = source.parent
    session_dir = next((p for p in [source.parent, *source.parents]
                        if p.parent == ROOT and re.match(r"\d\d-", p.name)), None)

    def repl(m):
        bang, label, target = m.group(1), m.group(2), m.group(3).strip()
        if bang or target.startswith(("http://", "https://", "#", "mailto:")):
            return m.group(0)
        base, _, frag = target.partition("#")
        try:
            rel = (src_dir / base).resolve().relative_to(ROOT.resolve())
        except ValueError:
            return m.group(0)
        rel_s = rel.as_posix()

        # The three parts of a session live in one chapter: links become anchors.
        parts = rel.parts
        if session_dir is not None and parts and parts[0] == session_dir.name:
            sub = "/".join(parts[1:])
            anchors = {"00-pre-session/README.md": "#before-the-session",
                       "01-lecture/README.md": "#the-lecture",
                       "02-practice/README.md": "#in-the-practice",
                       "README.md": "#"}
            if sub in anchors:
                a = anchors[sub]
                return f"[{label}]({a})" if a != "#" else f"[{label}](session-{session_dir.name[:2]}.qmd)"
            deck = re.match(r"(?:0[0-2]-[a-z-]+/)?INTE60019A-S(\d\d)-([A-Za-z-]+)\.qmd$", sub)
            if deck:
                return f"[{label}]({PAGES}session-{deck.group(1)}-{deck.group(2).lower()}.html)"
        # Another session's folder.
        if parts and re.match(r"\d\d-", parts[0]):
            num = parts[0][:2]
            if len(parts) == 1 or parts[1:] == ("README.md",):
                return f"[{label}](session-{num}.qmd)"
            sub = "/".join(parts[1:])
            anchors = {"00-pre-session/README.md": "before-the-session",
                       "01-lecture/README.md": "the-lecture",
                       "02-practice/README.md": "in-the-practice"}
            if sub in anchors:
                return f"[{label}](session-{num}.qmd#{anchors[sub]})"
        if rel_s in CHAPTER_LINKS:
            return f"[{label}]({CHAPTER_LINKS[rel_s]}{'#' + frag if frag else ''})"
        kind = "tree" if (ROOT / rel).is_dir() else "blob"
        return f"[{label}]({GH.replace('/blob/', f'/{kind}/')}{rel_s}{'#' + frag if frag else ''})"

    return re.sub(r"(!?)\[([^\]]*)\]\(([^)\s]+)\)", repl, text)


# The "> **[Open the … slides](…)**" block at the top of every README: the chapter
# header already links the decks, so it is dropped from the book.
SLIDE_LINKS = re.compile(r"^> \*\*\[Open the .*(?:\n>.*)*\n\n?", re.M)


def brief(path, by=1, question=""):
    text = path.read_text(encoding="utf-8")
    if question:
        text = text.replace(question + "\n", "", 1)
    # The "Slides: … · Instructor plan: …" paragraph points at files; the chapter header links the decks.
    text = re.sub(r"^Slides: .*(?:\n.+)*\n", "", text, count=1, flags=re.M)
    text = SLIDE_LINKS.sub("", text, count=1)
    return rewrite_links(shift_headings(drop_titles(text), by), path)


# ---------------------------------------------------------------------------
# The session README supplies the chapter's title, question and fact table.
# ---------------------------------------------------------------------------
def session_facts(folder):
    lines = (folder / "README.md").read_text(encoding="utf-8").splitlines()
    title = re.sub(r"^#\s*Session\s*\d+\s*[—-]\s*", "", lines[0]).strip()
    subtitle = next((l[4:].strip() for l in lines[:6] if l.startswith("### ")), "")
    start = next((i for i, l in enumerate(lines) if l.startswith("> **")), None)
    question = ""
    if start is not None:
        block = []
        for l in lines[start:]:
            if not l.startswith(">"):
                break
            block.append(l)
        question = "\n".join(block)
    table, inside = [], False
    for l in lines:
        if l.startswith("|"):
            inside = True
            table.append(l)
        elif inside:
            break
    return title, subtitle, question, rewrite_links("\n".join(table), folder / "README.md")


def deck_links(num, folder):
    kinds = [("Pre-Session", "Pre-session slides"), ("Lecture", "Lecture slides"),
             ("Practice", "Practice slides")]
    links = [f"[{label}]({PAGES}session-{num}-{kind.lower()}.html)" for kind, label in kinds
             if list(folder.glob(f"*/INTE60019A-S{num}-{kind}.qmd"))]
    if num == "12":
        links = [f"[Presentation-day slides]({PAGES}session-12-presentations.html)"]
    if (folder / "00-pre-session/README.md").exists():
        links.append(f"[Pre-session page]({GH}{folder.name}/00-pre-session/README.md)")
    links.append(f"[Session folder]({GH.replace('/blob/', '/tree/')}{folder.name})")
    links.append(f"[Data instructions]({GH}{folder.name}/data/README.md)"
                 if (folder / "data/README.md").exists() else "")
    return " · ".join(l for l in links if l)


def chapter_prose(folder):
    """(declared front matter, body) of NN-slug/chapter.md, or ({}, None)."""
    path = folder / "chapter.md"
    if not path.exists():
        return {}, None
    raw = path.read_text(encoding="utf-8")
    declared = {}
    m = re.match(r"^---\n(.*?)\n---\n", raw, re.S)
    if m:
        for line in m.group(1).splitlines():
            key, sep, value = line.partition(":")
            if sep:
                declared[key.strip()] = value.strip().strip("\"'")
        raw = raw[m.end():]
    return declared, rewrite_links(raw.strip(), path)


def chapter(folder):
    num = folder.name[:2]
    title, subtitle, question, table = session_facts(folder)
    declared, prose = chapter_prose(folder)
    title = declared.get("title") or title
    parts = [f'---\ntitle: "{title}"\n---\n',
             f"::: {{.chapter-meta}}\nSession {int(num)}"
             + (f" · {subtitle}" if subtitle else "") + f"<br>\n{deck_links(num, folder)}\n:::\n"]
    if question:
        parts.append(question + "\n")

    if prose:
        if table and num != "12":
            parts.append(table + "\n")
        parts.append(prose + "\n")
        if num == "12":
            body = (folder / "README.md").read_text(encoding="utf-8")
            body = re.sub(r"^#\s.*\n", "", body, count=1)
            body = re.sub(r"^###\s.*\n", "", body, count=1)
            body = re.sub(r"^>.*\n(?:>.*\n)*", "", body.strip() + "\n", count=1, flags=re.M)
            body = SLIDE_LINKS.sub("", body.lstrip("\n"), count=1)
            parts.append("## On the day\n\n" + shift_headings(rewrite_links(body.strip(), folder / "README.md")))
        else:
            p = folder / "02-practice/README.md"
            if p.exists():
                parts.append(f"## In the practice\n\n{brief(p, question=question)}\n")
        return "\n".join(parts) + "\n"

    if num == "12":
        body = (folder / "README.md").read_text(encoding="utf-8")
        body = re.sub(r"^#\s.*\n", "", body, count=1)
        body = re.sub(r"^###\s.*\n", "", body, count=1)
        parts.append(rewrite_links(body.strip(), folder / "README.md"))
        return "\n".join(parts) + "\n"

    if table:
        parts.append(table + "\n")
    for heading, sub in (("Before the session", "00-pre-session/README.md"),
                         ("The lecture", "01-lecture/README.md"),
                         ("In the practice", "02-practice/README.md")):
        p = folder / sub
        if p.exists():
            parts.append(f"## {heading}\n\n{brief(p, question=question)}\n")
    return "\n".join(parts) + "\n"


def flat_page(title, source, extra=""):
    path = ROOT / source
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"^#\s+.*\n", "", text, count=1)
    # Pages whose own sections start at ### keep their shape under ##.
    return f'---\ntitle: "{title}"\n---\n\n{extra}{rewrite_links(text.strip(), path)}\n'


def assessment_page():
    page = flat_page("Assessment", "assessments/README.md")
    for title, src in ASSESSMENT_BRIEFS:
        page += f"\n## {title}\n\n{brief(ROOT / src)}\n"
    return page


def preface(folders):
    rows = []
    for f in folders:
        num = f.name[:2]
        title, _, question, _ = session_facts(f)
        q = re.sub(r"\s*\n>\s*", " ", question)
        q = re.sub(r"^>\s*\*\*(.*)\*\*\s*$", r"\1", q)
        rows.append(f"| [{int(num)}](session-{num}.qmd) | {title} | {q} |")
    table = "\n".join(rows)
    return f"""# Foreword {{.unnumbered}}

Every multinational now says that geopolitics matters to it. Far fewer can say *how much*, *through
which channel*, or *what they would do differently if the number changed*. The gap is not one of
attention — boards discuss sanctions, export controls, wars and elections every quarter — but of
measurement. Geopolitical risk reaches a firm through its market access, its inputs, its finance,
its people and its data, and each of those channels can be counted. Most firms do not count them.

This book is the lecture notes of a twelve-session graduate course that tries to close that gap. Its
method is simple and a little stubborn: **every big idea is read, then rebuilt from its data.** A
landmark article or book — Caldara and Iacoviello's geopolitical risk index, Baldwin's *Great
Convergence*, Kuziemko and Werker on the price of a Security Council seat, the Global Sanctions Data
Base — is paired with a practice round in which the data are collected at source and its central
figure is replicated in Tableau. A famous chart is a set of decisions: which countries, which years,
which deflator, which coding rule. You only see the decisions when you make them yourself.

::: {{.step}}
**The data will disagree with the paper.** Sources are revised, codebooks change, countries are
renamed and recoded. Every practice round records at least one place where the replication did not
match — and asks what that disagreement means for a firm that would have relied on the original.
:::

Each chapter ends on the same question: *what does this figure not license a multinational to
conclude?* That is the habit the course is built to leave behind.

## How to use it {{.unnumbered}}

| If you want to | Go to |
|---|---|
| Prepare for next week | the session's pre-session page, linked at the top of each chapter |
| Re-read the argument after class | the chapter itself |
| Know exactly what the practice round asks | the chapter's last section, **In the practice** |
| Find where something was covered | the **search box**, top of the sidebar |
| Find a dataset, its URL and its traps | [Data sources](data-sources.qmd) |
| Know how you are graded | [Assessment](assessment.qmd) |

::: {{.check}}
**The search box is the reason this book exists.** Slides are good for a room and bad for finding
something three weeks later. Search covers every session at once, so a term you half-remember —
*weaponised interdependence*, *ideal points*, *Herfindahl* — takes you to the session that introduced
it, with its reading and its exercise.
:::

## The slides {{.unnumbered}}

Each chapter links to the decks it was built from. The slides remain the version delivered in class;
the book sets the same argument out at length, as continuous prose — about six thousand words a
session, with the definitions, the history and the literature the slides only point to.
All decks are also listed on the [course site]({PAGES}).

## The twelve chapters {{.unnumbered}}

| | Chapter | Question |
|---|---|---|
{table}

::: {{.muted}}
INTE 60019A · HEC Montréal · Thierry Warin, PhD · Source:
[github.com/{REPO}](https://github.com/{REPO}) · {{{{< meta date >}}}}
:::
"""


def quarto_yml(folders):
    chapters = "\n".join(f"    - session-{f.name[:2]}.qmd" for f in folders)
    appendices = "\n".join(f"    - {q}" for q, _, _ in APPENDICES)
    return f"""# Generated by scripts/build_book.py — edit that, not this.
project:
  type: book
  output-dir: ../docs/book

book:
  title: "{TITLE}"
  subtitle: "INTE 60019A · HEC Montréal"
  author: "Thierry Warin, PhD"
  date: last-modified
  date-format: "D MMMM YYYY"
  search: true
  repo-url: https://github.com/{REPO}
  repo-branch: main
  repo-actions: [source, issue]
  downloads: [pdf]
  page-navigation: true
  sidebar:
    style: docked
    collapse-level: 1
  page-footer:
    left: "INTE 60019A · HEC Montréal"
    right: "Built from the course repository"
  chapters:
    - index.qmd
{chapters}
  appendices:
{appendices}

bibliography: references.bib
link-citations: true

format:
  html:
    theme: [cosmo, book.scss]
    toc: true
    toc-depth: 3
    link-external-newwindow: true
  pdf:
    documentclass: scrbook
    classoption: [10pt, twoside, openright, numbers=noenddot, chapterprefix=true]
    pdf-engine: xelatex
    mainfont: "Times New Roman"
    sansfont: "Helvetica Neue"
    monofont: "Menlo"
    monofontoptions: [Scale=0.82]
    colorlinks: true
    toc: true
    toc-depth: 2
    number-sections: true
    geometry: [margin=2.2cm]
"""


GENERATED = ("*.qmd", "*.scss", "_quarto.yml", "references.bib")


def merge_bibliographies(folders):
    """Concatenate every NN-slug/chapter.bib, keeping the first entry for each key."""
    seen, out = set(), []
    for f in folders:
        bib = f / "chapter.bib"
        if not bib.exists():
            continue
        for entry in re.split(r"\n(?=@)", "\n" + bib.read_text(encoding="utf-8")):
            m = re.match(r"\s*@\w+\s*\{\s*([^,\s]+)\s*,", entry)
            if m and m.group(1) not in seen:
                seen.add(m.group(1))
                out.append(entry.strip())
    (BOOK / "references.bib").write_text("\n\n".join(out) + "\n", encoding="utf-8")
    return len(out)


def clean():
    """Remove what this script generated, and nothing else (book/.quarto belongs to Quarto)."""
    BOOK.mkdir(exist_ok=True)
    for pattern in GENERATED:
        for stale in BOOK.glob(pattern):
            stale.unlink()


def main():
    clean()
    folders = sessions()
    (BOOK / "_quarto.yml").write_text(quarto_yml(folders), encoding="utf-8")
    shutil.copy2(ROOT / "slides/book.scss", BOOK / "book.scss")
    (BOOK / "index.qmd").write_text(preface(folders), encoding="utf-8")
    refs = merge_bibliographies(folders)
    for f in folders:
        (BOOK / f"session-{f.name[:2]}.qmd").write_text(chapter(f), encoding="utf-8")
    for qmd, title, src in APPENDICES:
        text = assessment_page() if qmd == "assessment.qmd" else flat_page(title, src)
        (BOOK / qmd).write_text(text, encoding="utf-8")
    print(f"book/: {len(folders)} chapters ({sum((f / 'chapter.md').exists() for f in folders)} "
          f"written), {len(APPENDICES)} appendices, {refs} references")


if __name__ == "__main__":
    main()
