# Geopolitical Risks and International Business

### How does a multinational firm know how much geopolitical risk it faces — and what should it do about it?

**INTE 60019A · HEC Montréal · M. Sc. in International Business · 3 credits · in English**
Thierry Warin, PhD

> **The lecture notes are a book.** [*Geopolitical Risks and International Business*](https://warint.github.io/geopolitics-geoeconomics/book/) — every
> session as one chapter (before the session, the lecture, the practice round), searchable, with a
> [PDF](https://warint.github.io/geopolitics-geoeconomics/book/Geopolitical-Risks-and-International-Business.pdf). The slides are on the
> [course site](https://warint.github.io/geopolitics-geoeconomics/).

A twelve-session graduate course in which every big idea about geopolitical risk is **read**, then
**rebuilt from its data**. Each session pairs a landmark article or book — Caldara and Iacoviello's
geopolitical risk index, Baldwin's *Great Convergence*, Kuziemko and Werker on the price of a
Security Council seat, the Global Sanctions Data Base — with a **practice round** in which you collect
the data at source and replicate its central figure in **Tableau**. Then you ask the question every
practice round ends on: *what does this figure not license a multinational to conclude?*

| | |
|---|---|
| **Read the argument, rebuild the evidence** | Eleven practice rounds, eleven replications. A famous chart is a set of decisions — countries, years, deflators, coding rules. You only see them when you make them yourself. |
| **Collect the data, do not receive it** | Nothing is pre-cleaned. You find the source, read the codebook, log the version, and notice that it was revised since the paper. That is half of professional risk analysis. |
| **The data will disagree with the paper** | Every practice deliverable documents at least one place where it did. You are never penalised for a replication that does not match — only for not noticing. |
| **Write for a decision-maker** | Every deliverable has a reader: a country manager, a chief risk officer, a board. The term ends with a risk dashboard for one real multinational, defended in front of the room. |

---

## The twelve sessions

| # | Session | Big work replicated | Tableau skill |
|---|---|---|---|
| [01](01-what-is-geopolitical-risk/README.md) | What is geopolitical risk? | Caldara & Iacoviello (2022) — the GPR index | dates, line charts, annotations |
| [02](02-the-international-economic-order/README.md) | The international economic order | Baldwin (2016) — the G7 share of world GDP | pivot, percent of total |
| [03](03-anarchy-and-the-balance-of-power/README.md) | Anarchy and the balance of the major powers | Mearsheimer (2001), Allison (2017) — shares of world capabilities | calculated fields, parameters |
| [04](04-trade-conflict-and-fragmentation/README.md) | Trade, conflict and geoeconomic fragmentation · *Quiz 1* | Gopinath et al. (2025) — trade within and between blocs | dyadic joins, groups and sets |
| [05](05-international-institutions/README.md) | International institutions | Kuziemko & Werker (2006) — aid and the Security Council | LOD expressions, event time |
| [06](06-private-authority-and-standards/README.md) | Private authority, standards and global regulation | Prakash & Potoski (2006) — the diffusion of ISO 14001 | maps, pages |
| [07](07-measuring-risk-text-and-indices/README.md) | Measuring risk: content analysis, coding, big data, indices · *Quiz 2* | Hassan et al. (2019) — firm-level political risk; your own coded index | Tableau Prep, normalisation, weights |
| [08](08-cyber-geopolitics/README.md) | Cyber geopolitics and digital threats | Valeriano & Maness (2015) — cyber incidents between rivals | highlight tables, actions |
| [09](09-economic-diplomacy/README.md) | The redefinition of economic diplomacy | Rose (2007) — embassies as export promotion | log scales, trend lines |
| [10](10-economic-sanctions/README.md) | Economic sanctions · *Quiz 3* | Hufbauer et al. (2007); the Global Sanctions Data Base | Gantt charts, stacked shares |
| [11](11-space-geopolitics/README.md) | Space geopolitics: the orbital commons and the new space race | ESA (2026), *Space Environment Report*; SWF (2026), *Global Counterspace Capabilities* — objects in orbit, and who launches | running sum, HHI with LOD, dashboard actions |
| [12](12-team-presentations/README.md) | Team presentations | your dashboard for one multinational | dashboards, stories, Tableau Public |

**The arc.** The system (01–04) → who governs it (05–06) → how risk becomes a number (07) → the four
channels through which it reaches the firm (08–11) → the firm's own assessment (12).

---

## How every session works

```
Before class                First half (~70–90 min)         Second half (~90 min) · practice round
─────────────────────────   ─────────────────────────────   ──────────────────────────────────────
00-pre-session/             01-lecture/                     02-practice/
  · the big work              · four Risk Briefs (02–11)      1 COLLECT    the data at source
  · its target figure         · the concept and its theory    2 PREPARE    it in Tableau
  · data source located       · the evidence, and its limits  3 REPLICATE  the target figure
  · written self-check        · what it means for the firm    4 COMPARE    break · extend
                              · the Tableau skill of the day  5 THE CATCH  one slide, two minutes
```

Each session folder holds the student pages (`README.md`), the decks (`INTE60019A-SNN-*.qmd`,
Quarto reveal.js), the instructor's `TEACHING-PLAN.md`, and a `data/README.md` saying exactly what to
collect and where to put it.

---

## Assessment

| Component | Weight | When |
|---|---|---|
| Participation | 10% | every session |
| Three quizzes, in class | 15% | Sessions 04, 07, 10 |
| Risk Brief — individual presentation | 15% | one of Sessions 02–11 |
| Team work — risk dashboard and memo for one multinational | 20% | Session 12, memo a week later |
| Take-home examination — 3 h in a 48 h window | 40% | final examination period |

Full detail: [`SYLLABUS.md`](SYLLABUS.md) · [`assessments/`](assessments/README.md)

---

## Getting started

1. **Tableau.** Request the academic licence, install Tableau Desktop (and Prep, where the licence
   includes it), open a Tableau Public account: [`TABLEAU-TOOLKIT.md`](TABLEAU-TOOLKIT.md).
2. **This repository.** Download or clone it to your Desktop. Each session's `data/` folder is where
   your downloads go; it is git-ignored, so nothing you collect is ever committed.
3. **Session 01.** Do the [pre-session](01-what-is-geopolitical-risk/00-pre-session/README.md).

```bash
cd ~/Desktop
git clone <this repository> geopolitical-risks-international-business
```

**Rendering the decks and the book** (instructors): `scripts/render_slides.sh` renders every `.qmd`
to a self-contained HTML deck with Quarto (press **F** for full screen, **S** for speaker view);
`scripts/render_book.sh` assembles the lecture notes into `book/` and renders them to `docs/book/`;
`python3 scripts/build_docs.py` publishes the decks to `docs/`.

---

## Repository map

```
├── README.md                     this page
├── SYLLABUS.md                   the course: outcomes, sessions, assessment, policies
├── REPLICATIONS.md               the big work, data and target figure of every practice round
├── DATA-SOURCES.md               every dataset: producer, URL, access, traps
├── READINGS.md                   required and further reading, session by session
├── TABLEAU-TOOLKIT.md            installation, skills ladder, conventions, traps, provenance log
├── assessments/                  quizzes · Risk Brief · team project · take-home
├── templates/                    provenance-log.csv
├── slides/                       deck theme (economist.scss), book theme (book.scss), filter
├── scripts/                      render_slides.sh · render_book.sh · build_book.py · build_docs.py
├── book/                         the course book, assembled from the sessions (generated — do not edit)
├── docs/                         the GitHub Pages site: decks and docs/book/
├── NN-session-slug/              sessions 01–11
│   ├── README.md                 the session at a glance
│   ├── data/README.md            what to collect, where, and its traps
│   ├── 00-pre-session/           reading, data, self-check · README + deck
│   ├── 01-lecture/               notes · TEACHING-PLAN · deck
│   └── 02-practice/              the practice round brief · deck
└── 12-team-presentations/        run of show, rubric, closing
```

---

## Licence

Teaching materials CC BY-NC 4.0; code MIT; **no data is redistributed** — see
[`LICENSING.md`](LICENSING.md). Cite as in [`CITATION.cff`](CITATION.cff).
