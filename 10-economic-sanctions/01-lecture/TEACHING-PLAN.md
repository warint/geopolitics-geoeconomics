# Session 10 — Teaching plan (first half, 90 min including Quiz 3 and Risk Briefs)

# Economic sanctions

> **Instructor page.** The student-facing companion is [`README.md`](README.md); the deck is
> [`INTE60019A-S10-Lecture.qmd`](INTE60019A-S10-Lecture.qmd).

*Sanctions have become the instrument of first resort. Are they an efficient mechanism for regulating
geopolitical risk — or a source of it?*

---

## Before the room fills

Check by e-mail the day before that every team has the GSDB files. Do **not** hand out copies: the
licence forbids redistribution. A student whose request is still pending works with a teammate's
screen for the GSDB steps and does the TIES steps on their own machine.

---

## Board plan

| Minutes | |
|---|---|
| **0–20** | **Quiz 3**, on paper. Collect at minute 20 sharp. |
| **20–40** | **Four Risk Briefs.** |
| **40–48** | **The instrument of first resort.** The four-dimension table. Ask the room to classify the 2022 measures on Russia along all four. |
| **48–63** | **Do they work?** Hufbauer et al.'s two components of success on the board. Then Pape: "most successes are not". Then Drezner's selection effect — draw two boxes, *threatened* and *imposed*, and show why the hard cases sink to the second. Punchline: every number in the debate is a coding decision. |
| **63–70** | **Smart sanctions** and financial chokepoints — the bridge back to Farrell & Newman. |
| **70–85** | **The firm in the middle.** Compliance perimeter; secondary sanctions; overcompliance. Russia 2022: the four-option table — make the room choose for a named consumer-goods firm, then for a named energy firm. Why do the answers differ? |
| **85–90** | **What a dashboard should track** — four lines, to carry into the team projects. Show the range join live. Hand over. |

---

## Run Tableau live

Show the range join: `years.csv` on the left, GSDB on the right, join clause `Year >= begin_year` and
`Year <= IFNULL(end_year, 2025)` (a **join calculation** on the right side). Show the row count before and
after: the jump is the point.

---

## Put this to the room

*"Your compliance team tells you the new measures do not legally require you to exit. Your bank tells
you it will no longer process your payments to that country. Who just set your sanctions policy?"*

---

## Misconception to pre-empt

That "sanctions work about a third of the time" is a fact about the world. It is a fact about one
coding of one set of cases. Say it during section 2, and again when the practice round computes its
own success shares.

---

## Last twenty minutes of the practice round

Team dashboard skeleton review (team-project milestone). Five minutes per cluster of teams: do they
have four datasets from three families? Is the composite index built? Is the watchlist written with
thresholds?
