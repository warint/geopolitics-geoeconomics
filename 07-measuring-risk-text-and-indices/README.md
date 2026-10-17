# Session 07 — Measuring risk: content analysis, coding, big data and composite indices

### How a political judgement becomes a number — and what is lost on the way

> **Every geopolitical risk score a multinational buys or builds is a chain of choices: which texts,
> which words, which coder, which weights. Can you see the chain — and defend each link?**

> **[Open the lecture slides](https://warint.github.io/geopolitics-geoeconomics/session-07-lecture.html)** — or read the source at
> [`01-lecture/INTE60019A-S07-Lecture.qmd`](01-lecture/INTE60019A-S07-Lecture.qmd).
> Also in your browser: [pre-session slides](https://warint.github.io/geopolitics-geoeconomics/session-07-pre-session.html) ·
> [practice slides](https://warint.github.io/geopolitics-geoeconomics/session-07-practice.html) · [the companion chapter in the book](https://warint.github.io/geopolitics-geoeconomics/book/session-07.html)

| | |
|---|---|
| **Big work** | Hassan, T. A., Hollander, S., van Lent, L., & Tahoun, A. (2019). Firm-level political risk: Measurement and effects. *Quarterly Journal of Economics*, 134(4), 2135–2202. [doi:10.1093/qje/qjz021](https://doi.org/10.1093/qje/qjz021) |
| **Companion works** | Baker, Bloom & Davis (2016), *Measuring Economic Policy Uncertainty*, QJE, [doi:10.1093/qje/qjw024](https://doi.org/10.1093/qje/qjw024) · OECD/JRC (2008), *Handbook on Constructing Composite Indicators*, [doi:10.1787/9789264043466-en](https://doi.org/10.1787/9789264043466-en) · Krippendorff (2018), *Content Analysis*, 4th ed. |
| **Target figures** | (a) **Average firm-level political risk over time**, against the Economic Policy Uncertainty index · (b) **your own coded index**, with its intercoder agreement · (c) **a composite exposure index** for your team's firm, with weights the reader can move |
| **Data you collect** | firmlevelrisk.com firm-quarter file; EPU (global); 40 news headlines from GDELT that **your team codes**; GPR country indices and Worldwide Governance Indicators for the composite |
| **Tableau skill** | **Tableau Prep** flows (or the data source pane) · unions · cleaning text-coded data · **normalisation** · **parameters as weights** |
| **Course themes** | Methodology: content analysis, coding, big data, statistical treatment — the Synthesis outcome |

**Quiz 2** (Sessions 04–06) opens the session: 20 minutes, on paper, closed book.

---

## What session 07 is for

| Geopolitics | Data & Tableau | International business |
|---|---|---|
| Explain how **dictionary methods** turn text into risk: GPR, EPU, and Hassan et al.'s political bigrams | Parse quarter strings into dates; aggregate firm-quarters to a series; relate two series at quarterly grain | Read a vendor's risk score as a chain of choices you can audit |
| Write a **coding protocol** and measure **intercoder reliability** — percent agreement and Cohen's kappa | Build a coder A × coder B **highlight table** and compute agreement | Know what "big data" adds — coverage, timeliness — and what it hides — language, source and selection bias |
| Build a **composite indicator** the OECD/JRC way: select, normalise, weight, aggregate, test sensitivity | Min–max normalisation with LOD; **parameters** as weights; ranks that move as weights move | Start the team's composite exposure index — the heart of the team dashboard |

---

## The session at a glance

| | Where | Time |
|---|---|---|
| **Before class** | [`00-pre-session/`](00-pre-session/README.md) — read; collect; **pull 40 headlines and code them, two coders independently** | 2 h 30 |
| **Opening** | **Quiz 2**, then four **Risk Briefs** | 20 + 20 min |
| **First half** | [`01-lecture/`](01-lecture/README.md) — content analysis; dictionaries; reliability; big data; composite indicators | 50 min |
| **Second half** | [`02-practice/`](02-practice/README.md) — **Practice round 07:** three short builds — firm-level risk vs EPU; your coded index; a composite with moving weights | 90 min |
| **Data** | [`data/`](data/README.md) | — |
| **Read further** | [Chapter 7 of the book *Geopolitical Risks and International Business*](https://warint.github.io/geopolitics-geoeconomics/book/session-07.html) — the argument at length, with its sources | — |

**Team project milestone.** The composite built in part (c) of today's practice is your **draft
composite index**, reviewed in class.

---

[← Previous session](../06-private-authority-and-standards/README.md) · [Syllabus](../SYLLABUS.md) ·
[Next session →](../08-cyber-geopolitics/README.md)
