"""Assemble the book *Geopolitical Risks and International Business* from the session chapters.

    python3 scripts/build_book.py
    scripts/render_book.sh            # assemble, then render (HTML + PDF) into docs/book/

The book is a *derived* artefact: nothing in book/ is authored. Each chapter is written in its
session folder, as NN-slug/chapter.md (front matter `title:`, narrative `##` sections, and the
book's fenced divs: .definition, .archive, .lit, .step, .check, .warn), with its sources in
NN-slug/chapter.bib. Figures are drawn from public data by scripts/figures/chNN.py into
assets/figures/, and a chapter embeds them as `![caption](figures/name.png)`. This script copies the
chapters and figures in, merges the bibliographies, writes the preface and the reference list, and
arranges the chapters into parts.

The book stands on its own. It carries no course scaffolding — no slide links, no session facts,
no practice briefs — so a chapter reads the same whether or not the reader is taking the course.
"""

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "book"
REPO = "warint/geopolitics-geoeconomics"
TITLE = "Geopolitical Risks and International Business"
SUBTITLE = "Measuring the politics of the world economy, and acting on it"
AUTHOR = "Thierry Warin"

# Chapter 1 opens the book and chapter 12 closes it; the rest fall into four parts.
PARTS = [
    (None, ["01"]),
    ("The system", ["02", "03", "04"]),
    ("Who governs", ["05", "06"]),
    ("From judgement to number", ["07"]),
    ("The channels", ["08", "09", "10", "11"]),
    (None, ["12"]),
]


def sessions():
    return {p.name[:2]: p for p in sorted(ROOT.iterdir())
            if p.is_dir() and re.match(r"\d\d-", p.name) and (p / "chapter.md").exists()}


def front_matter(text):
    """(declared fields, body) of a chapter.md."""
    declared = {}
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return declared, text
    for line in m.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep:
            declared[key.strip()] = value.strip().strip("\"'")
    return declared, text[m.end():]


def chapter_title(folder):
    declared, _ = front_matter((folder / "chapter.md").read_text(encoding="utf-8"))
    return declared.get("title", folder.name)


def chapter(folder):
    declared, body = front_matter((folder / "chapter.md").read_text(encoding="utf-8"))
    title = declared.get("title", folder.name).replace('"', '\\"')
    return f'---\ntitle: "{title}"\n---\n\n{body.strip()}\n'


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


def preface(chapters):
    contents = []
    for part, nums in PARTS:
        if part:
            contents.append(f"\n**Part — {part}**\n")
        for n in nums:
            if n in chapters:
                contents.append(f"- [Chapter {int(n)} · {chapter_title(chapters[n])}](session-{n}.qmd)")
    contents = "\n".join(contents).strip()
    return f"""# Preface {{.unnumbered}}

Every multinational now says that geopolitics matters to it. Far fewer can say *how much*, *through
which channel*, or *what they would do differently if the number changed*. The gap is not one of
attention — boards discuss sanctions, export controls, wars and elections every quarter — but of
measurement. Geopolitical risk reaches a firm through its market access, its inputs, its finance, its
people and assets, and its data and operations, and each of those channels can be observed and
counted. Most firms do not count them, and the numbers they buy are rarely examined.

This book is about that gap. It treats geopolitical risk as something to be argued about with
evidence: what a concept means, how it has been turned into data, what the data show, and what they
cannot show. Each chapter takes one idea that has shaped how scholars and practitioners think about
the political environment of international business — the balance of power, the commercial peace,
the authority of institutions and standards, the measurement of risk from text, the weaponisation of
networks, sanctions, the new contest in orbit — and follows it from its origins to the numbers built
on it, and from the numbers to the decisions a multinational actually takes.

::: {{.step}}
**The numbers disagree with the stories told about them.** Indices are revised, codebooks change,
countries are renamed and recoded, and the same concept measured two ways gives two answers. The
chapters dwell on those disagreements, because they are where an analyst earns their keep.
:::

The argument runs in five movements. Chapter 1 asks what is being counted when we speak of
geopolitical risk. Part I describes the system a firm operates in: an economic order written by a
few powers, an anarchic distribution of power, and a trading system fragmenting along geopolitical
lines. Part II asks who governs that system — public institutions, old and new, and the private
authority of standards. Part III shows how political judgement becomes a number, and what is lost on
the way. Part IV follows the four channels through which geopolitical risk now reaches the firm most
directly: cyberspace, economic diplomacy, sanctions and outer space. Chapter 12 returns to the firm,
and to the step that no indicator takes for it — the decision.

## Contents {{.unnumbered}}

{contents}

## How to read it {{.unnumbered}}

The chapters can be read in order or on their own; cross-references point back where an argument
depends on an earlier one. Definitions are set apart, so that a reader looking for what a term means
can find it; boxes headed *From the archive* recount an episode that made an argument concrete; each
chapter closes with a short review of the literature for readers who want to go further. Every source
is listed in the [references](references.qmd), and every data source is public.

::: {{.muted}}
{AUTHOR} · HEC Montréal · Source: [github.com/{REPO}](https://github.com/{REPO}) ·
{{{{< meta date >}}}}
:::
"""


REFERENCES = """# References {.unnumbered}

::: {#refs}
:::
"""


def quarto_yml(chapters):
    lines = ["    - index.qmd"]
    for part, nums in PARTS:
        files = [f"session-{n}.qmd" for n in nums if n in chapters]
        if not files:
            continue
        if part:
            lines.append(f'    - part: "{part}"\n      chapters:')
            lines += [f"        - {f}" for f in files]
        else:
            lines += [f"    - {f}" for f in files]
    lines.append("    - references.qmd")
    chapter_list = "\n".join(lines)
    return f"""# Generated by scripts/build_book.py — edit that, not this.
project:
  type: book
  output-dir: ../docs/book

book:
  title: "{TITLE}"
  subtitle: "{SUBTITLE}"
  author: "{AUTHOR}"
  date: last-modified
  date-format: "D MMMM YYYY"
  search: true
  repo-url: https://github.com/{REPO}
  repo-branch: main
  downloads: [pdf]
  page-navigation: true
  sidebar:
    style: docked
    collapse-level: 1
  page-footer:
    left: "{AUTHOR} · {TITLE}"
    right: "HEC Montréal"
  chapters:
{chapter_list}

bibliography: references.bib
link-citations: true

format:
  html:
    theme: [cosmo, book.scss]
    toc: true
    toc-depth: 3
    link-external-newwindow: true
    fig-cap-location: bottom
    tbl-cap-location: top
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
    toc-depth: 1
    number-sections: true
    geometry: [margin=2.2cm]
"""


GENERATED = ("*.qmd", "*.scss", "_quarto.yml", "references.bib")


def clean():
    """Remove what this script generated, and nothing else (book/.quarto belongs to Quarto)."""
    BOOK.mkdir(exist_ok=True)
    for pattern in GENERATED:
        for stale in BOOK.glob(pattern):
            stale.unlink()
    if (BOOK / "figures").exists():
        shutil.rmtree(BOOK / "figures")


def copy_figures():
    src = ROOT / "assets" / "figures"
    if not src.exists():
        return 0
    dst = BOOK / "figures"
    dst.mkdir(exist_ok=True)
    pngs = sorted(src.glob("*.png"))
    for png in pngs:
        shutil.copy2(png, dst / png.name)
    return len(pngs)


def main():
    clean()
    chapters = sessions()
    (BOOK / "_quarto.yml").write_text(quarto_yml(chapters), encoding="utf-8")
    shutil.copy2(ROOT / "slides/book.scss", BOOK / "book.scss")
    (BOOK / "index.qmd").write_text(preface(chapters), encoding="utf-8")
    for n, folder in chapters.items():
        (BOOK / f"session-{n}.qmd").write_text(chapter(folder), encoding="utf-8")
    (BOOK / "references.qmd").write_text(REFERENCES, encoding="utf-8")
    refs = merge_bibliographies(list(chapters.values()))
    figs = copy_figures()
    print(f"book/: {len(chapters)} chapters in {sum(1 for p, _ in PARTS if p)} parts, "
          f"{refs} references, {figs} figures")


if __name__ == "__main__":
    main()
