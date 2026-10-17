# Session 11 — Space geopolitics

### The orbital commons and the new space race

> **Satellites now carry the position, timing, connectivity and imagery a multinational runs on.
> When orbit is crowded, contested and dominated by one operator, who holds the risk — and what
> can the firm do about it?**

| | |
|---|---|
| **Big works** | ESA Space Debris Office. (2026). *ESA's annual space environment report* (Issue 10.0, 1 May 2026; GEN-DB-LOG-00288-OPS-SD). European Space Agency. [PDF](https://www.sdo.esoc.esa.int/publications/Space_Environment_Report_I10R0_20260501.pdf) · Samson, V., & Brett, K. (Eds.). (2026). *Global counterspace capabilities: An open source assessment*. Secure World Foundation. [swfound.org](https://www.swfound.org/publications-and-reports/2026-global-counterspace-capabilities-report) |
| **Companion readings** | Pekkanen, S. M. (2019). Governing the new space race. *AJIL Unbound*, 113, 92–97. [doi:10.1017/aju.2019.16](https://doi.org/10.1017/aju.2019.16) · The Outer Space Treaty (1967) · Farrell & Newman (2019), from Session 08 |
| **Target figure** | ESA's **evolution of the number of objects in geocentric orbit by object class**, 1957–2025 (Fig. 2.1), with the 2007 Chinese ASAT test, the 2009 Iridium–Cosmos collision and the 2021 Russian ASAT test annotated — and the **concentration** of who puts satellites up, then and now |
| **Data you collect** | CelesTrak **SATCAT** (`satcat.csv`, the public satellite catalogue); optionally Jonathan McDowell's **GCAT** launch log |
| **Tableau skill** | **Running sum** (table calculation) on a pivoted event table · **Herfindahl–Hirschman index with LOD expressions** · **dashboard actions** across data sources |
| **Course themes** | Inter-state anarchy and the balance of the major powers; cyber geopolitics and digital threats in the decision-making architecture of multinational firms |

---

## What session 11 is for

| Geopolitics | Data & Tableau | International business |
|---|---|---|
| Explain why Earth orbit is a **commons** — the Outer Space Treaty, ITU coordination, and the Kessler logic of debris | Rebuild a **stock from flows**: objects in orbit = running sum of launches minus running sum of decays | Map the satellite services a firm depends on — **GNSS timing, connectivity, Earth observation** — to the operators and states behind them |
| Distinguish **destructive** from **non-destructive** counterspace capabilities, and say which ones are used in today's wars | Compute an **HHI with LOD expressions** and read the U-shape of concentration from 1957 to today | Read **dependence on one operator** (Starlink in Ukraine) as a risk with a sovereign behind it — weaponised interdependence, Session 08, moved to orbit |
| Place the **new space race** — democratisation, commercialisation, militarisation (Pekkanen) — in the balance of power | Wire a **dashboard action** that filters across two data sources | Choose between redundancy, multi-orbit contracts, terrestrial back-ups and insurance — and set the thresholds a dashboard should watch |

---

## The session at a glance

| | Where | Time |
|---|---|---|
| **Before class** | [`00-pre-session/`](00-pre-session/README.md) — read the ESA report and the SWF executive summary; Pekkanen; the Outer Space Treaty; **one** SATCAT download per team | 2 h |
| **Opening** | Four Risk Briefs (4 min + one question each) | 20 min |
| **First half** | [`01-lecture/`](01-lecture/README.md) — infrastructure in orbit; the commons; astropolitics; counterspace; the debris record; one operator; what the firm can do | 70 min |
| **Second half** | [`02-practice/`](02-practice/README.md) — **Practice round 11:** rebuild the debris record, measure the new space race, one dashboard | 90 min |
| **Data** | [`data/`](data/README.md) — what to download, where to put it | — |
| **Lecture notes** | [Chapter 11 of the course book](https://warint.github.io/geopolitics-geoeconomics/book/session-11.html) — pre-session, lecture and practice as one readable, searchable page | — |

> **The last practice round before the presentations.** Session 11 is the final practice round of
> the term. The last twenty minutes of Session 10 reviewed each team's dashboard skeleton; today's
> round adds the **space-infrastructure channel** — and the dashboard actions — that most team
> dashboards still lack. Session 12 is the presentations.

---

[← Previous session](../10-economic-sanctions/README.md) · [Syllabus](../SYLLABUS.md) ·
[Next session →](../12-team-presentations/README.md)
