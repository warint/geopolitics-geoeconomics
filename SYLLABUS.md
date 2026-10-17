# Geopolitical Risks and International Business

**INTE 60019A · HEC Montréal · Department of International Business**
M. Sc. in International Business (thesis and project streams) · elective · 3 credits · in person · taught in English

**Instructor:** Thierry Warin, PhD · `thierry.warin@hec.ca`
**Course coordinator (professeur responsable):** Philippe Bourbeau

---

## Contents

1. [What this course is](#1-what-this-course-is)
2. [Learning outcomes](#2-learning-outcomes)
3. [How a session works](#3-how-a-session-works)
4. [The twelve sessions](#4-the-twelve-sessions)
5. [Assessment](#5-assessment)
6. [The five evaluations, and why each exists](#6-the-five-evaluations-and-why-each-exists)
7. [Tools](#7-tools)
8. [Standing rules on data](#8-standing-rules-on-data)
9. [Policies](#9-policies)
10. [Core references](#10-core-references)

---

## 1. What this course is

Multinational firms do not operate in a market. They operate in an **international system** — one
without a government, shaped by the balance between great powers, partly governed by institutions,
standards and private authority, and increasingly contested through trade, sanctions, cyberspace
and outer space. Geopolitical risk is the name we give to the part of that system that can move a
firm's costs, revenues and assets without asking.

This course teaches you to **think about that risk as a political scientist, measure it as an
empirical researcher, and present it as an adviser to a board**.

Its distinctive feature is that every claim is put to data. Each of Sessions 01–11 is built around a
**big article or book** in the field — Caldara and Iacoviello's geopolitical risk index, Baldwin's
*Great Convergence*, Kuziemko and Werker on the price of a Security Council seat, the Global
Sanctions Data Base, and others. In the second half of each session you **collect the data the work
is built on yourself, from the original source, and rebuild its central figure in Tableau**. Then
you ask what the figure does — and does not — let a multinational conclude.

> ### Why the course is built this way
>
> **Read the argument, then rebuild the evidence.** A chart in a famous paper is a set of decisions —
> which countries, which years, which deflator, which coding rule. You only see the decisions when
> you have to make them yourself. That is what a replication round is for.
>
> **Collect the data, do not receive it.** In professional life nobody hands you a clean file. Finding
> the series, reading its codebook, noticing that it was revised last year, recording where it came
> from — that is half of geopolitical risk analysis, and the half most often done badly.
>
> **Write for a decision-maker.** Every deliverable has a reader: a country manager, a chief risk
> officer, a board. A chart that cannot be acted on is not finished.

---

## 2. Learning outcomes

By the end of the course you will be able to:

| Level | Outcome |
|---|---|
| **Knowledge** | **Define** international geopolitical risk analysis and **identify** its principal indicators — event-based, text-based, structural, institutional and firm-level. |
| **Comprehension** | **Explain and interpret** the international geopolitical context in which multinational firms operate: the economic order, inter-state anarchy and the balance of the major powers. |
| **Application** | **Apply** the concepts of economic diplomacy to new, multidimensional forms of geopolitical risk — sanctions, cyber operations, export restrictions, standards. |
| **Analysis** | **Analyse critically** the interactions between different types of geopolitical risk and their implications for the decisions of multinational firms. |
| **Synthesis** | **Integrate** different methodological approaches — content analysis, coding, big data, statistical treatment and visualisation — into interdisciplinary analytical thinking. |
| **Evaluation** | **Design** geopolitical risk assessment strategies for multinational firms on a rigorous methodological footing, and defend them. |

The Synthesis and Evaluation outcomes are carried mainly by the eleven practice rounds, the team
dashboard and the take-home examination.

---

## 3. How a session works

Sessions 01–11 share one rhythm. Session 12 is the team presentations.

```
Before class                First half (~90 min)            Second half (~90 min)
─────────────────────────   ─────────────────────────────   ─────────────────────────────
00-pre-session/             01-lecture/                     02-practice/  · practice round
  · the big article/book      · the concept and its theory    · COLLECT the data at source
  · its target figure         · the evidence, and its limits  · PREPARE it in Tableau
  · data source located       · what it means for the firm    · REPLICATE the target figure
  · written self-check        · the Tableau skill of the day  · COMPARE, break, extend
                                                              · one slide · two minutes
```

**Risk Briefs.** Sessions 02–11 open with four individual Risk Briefs in five-minute slots (20 minutes in all) — one
current geopolitical development, one Tableau view, one named multinational. See
[`assessments/risk-brief/`](assessments/risk-brief/README.md).

**The practice round.** Teams of three or four work through five steps, always the same:

| Step | Minutes | What you do |
|---|---|---|
| **1 · Collect** | 20 | Download the data from the original source. Fill in the provenance log: source, URL, version, date accessed, licence. |
| **2 · Prepare** | 20 | Pivot, join, clean and recode in Tableau's data source page or Tableau Prep. Record every decision. |
| **3 · Replicate** | 25 | Rebuild the target figure of the article or book, as close to the original as the data allow. |
| **4 · Compare and break** | 15 | Put yours beside the original. Where do they differ, and why? Change one defensible decision and show what moves. |
| **5 · The catch** | 10 | One slide: **original · ours · the catch** — what the figure does *not* license a multinational to conclude. A member drawn at random presents it. |

> ### The one rule of every practice round
>
> **Every deliverable documents at least one place where the data disagreed with the paper** — a
> revised series, a missing country, a changed coding rule, a country name that would not match.
> You are never penalised for a replication that does not match. You are penalised for not noticing.

---

## 4. The twelve sessions

**The big theme.** *How does a multinational firm know how much geopolitical risk it faces — and
what should it do about it?* The twelve sessions move from the system (01–04), to the institutions
that govern it (05–06), to how risk is measured (07), to the four instruments through which it now
reaches the firm (08–11), and end with the firm's own assessment (12).

| # | Session | The big work replicated | Data you collect | Tableau skill |
|---|---|---|---|---|
| [01](01-what-is-geopolitical-risk/README.md) | **What is geopolitical risk?** Concepts, indicators, and the syllabus | Caldara & Iacoviello (2022), *Measuring Geopolitical Risk* — the GPR index, 1900–today | GPR index (Iacoviello) | Connect, dates, line chart, annotations |
| [02](02-the-international-economic-order/README.md) | **The international economic order** in which multinationals operate | Baldwin (2016), *The Great Convergence* — the G7 share of world GDP | World Bank WDI | Pivot wide-to-long, area chart, percent of total |
| [03](03-anarchy-and-the-balance-of-power/README.md) | **Anarchy and the balance of the major powers** | Mearsheimer (2001) and Allison (2017) — the shifting distribution of power | Correlates of War, National Material Capabilities; SIPRI | Calculated fields, shares, parameters |
| [04](04-trade-conflict-and-fragmentation/README.md) | **Trade, conflict and geoeconomic fragmentation** · *Quiz 1* | Gopinath et al., *Changing Global Linkages: A New Cold War?* — trade between blocs | UNGA ideal points (Voeten); IMF bilateral trade | Joins on dyads, groups and sets |
| [05](05-international-institutions/README.md) | **International institutions** as arenas of power | Kuziemko & Werker (2006), *How Much Is a Seat on the Security Council Worth?* | UNSC membership; US foreign aid | Event-time with LOD expressions |
| [06](06-private-authority-and-standards/README.md) | **Private authority, standards and global regulation** | Prakash & Potoski (2006), *Racing to the Bottom?* — the diffusion of ISO 14001 | ISO Survey of certifications | Maps, geocoding, pages |
| [07](07-measuring-risk-text-and-indices/README.md) | **Measuring risk: content analysis, coding, big data and composite indices** · *Quiz 2* | Hassan et al. (2019), *Firm-Level Political Risk*; Baker, Bloom & Davis (2016) | Firm-level risk data; EPU; your own coded corpus | Tableau Prep, normalisation, weight parameters |
| [08](08-cyber-geopolitics/README.md) | **Cyber geopolitics and digital threats** | Valeriano & Maness (2015), *Cyber War versus Cyber Realities* | Dyadic Cyber Incident data; EuRepoC | Highlight tables, dyad matrices, filter actions |
| [09](09-economic-diplomacy/README.md) | **The redefinition of economic diplomacy** | Rose (2007), *Embassies as Export Promotion*; Bjola & Manor (2018) | Lowy Global Diplomacy Index; bilateral exports | Log scales, trend lines, what R² means |
| [10](10-economic-sanctions/README.md) | **Economic sanctions** as instruments for regulating geopolitical risk · *Quiz 3* | Hufbauer et al. (2007), *Economic Sanctions Reconsidered*; the Global Sanctions Data Base | GSDB; TIES | Gantt charts, stacked shares |
| [11](11-space-geopolitics/README.md) | **Space geopolitics:** the orbital commons and the new space race | ESA Space Debris Office (2026), *ESA's Annual Space Environment Report*; Samson & Brett (Eds., 2026), *Global Counterspace Capabilities* (SWF) | CelesTrak SATCAT; GCAT (optional) | Running sum, HHI with LOD, dashboard actions |
| [12](12-team-presentations/README.md) | **Team presentations:** a geopolitical risk assessment for one multinational | *Your own dashboard* | Everything above | Dashboards, stories, Tableau Public |

**The arc.** Session 01 asks what geopolitical risk *is* and shows the most cited attempt to count
it. Sessions 02–04 build the system a multinational operates in: an economic order (02), resting on
a distribution of power under anarchy (03), now fragmenting along geopolitical lines (04). Sessions
05–06 ask whether institutions — public (05) and private (06) — tame that system or are instruments
within it. Session 07 is the methodological hinge: how text, coding, big data and composite indices
turn a political judgement into a number, and what is lost on the way. Sessions 08–11 take the four
channels through which geopolitical risk now reaches the firm most directly — cyberspace (08),
economic diplomacy (09), sanctions (10) and space (11). Session 12 is where each team stakes
its own assessment, for one named multinational, in front of the room.

**The course themes**, as set out in the course description, are carried as follows:

| Theme | Sessions |
|---|---|
| The system of international economic order in which multinational firms operate | 02, 04 |
| Inter-state anarchy and the geostrategic balance of the major powers that dictate international trade relations | 03, 04, 11 |
| The impact and role of international institutions in analysing the geopolitical risks on which multinationals base their decisions | 05, 06 |
| The evolution of cyber geopolitics and digital threats in the decision-making architecture of multinational firms | 08, 11 |
| The redefinition of economic diplomacy and the implications for multinational firms | 09 |
| The efficiency of economic sanctions as mechanisms for regulating geopolitical risks | 10 |
| Methodology: content analysis, coding, big data, statistical treatment | 01, 07, and every practice round |

---

## 5. Assessment

| Component | Weight | Form | When |
|---|---|---|---|
| **Participation** | **10%** | individual, continuous | every session |
| **Quizzes** | **15%** | three in-class quizzes, 5% each, 20 minutes, individual | Sessions 04, 07, 10 |
| **Risk Brief** | **15%** | individual presentation in class, 4 min + one question | one of Sessions 02–11, by sign-up |
| **Team work** | **20%** | team geopolitical risk dashboard for one multinational (Tableau Public) + 2,500-word memo + presentation | presented Session 12 · memo due one week later |
| **Take-home examination** | **40%** | individual, 3 hours, within a 48-hour window during the final examination period | final examination period |

80% of the grade is individual. Everything about the grade, on one page:
[`assessments/README.md`](assessments/README.md).

---

## 6. The five evaluations, and why each exists

### Participation — 10%

Attendance is assumed. Participation means **active engagement**: contributing to the discussion of
the reading, engaging in the practice round, and asking a real question after a Risk Brief. What is
marked is sustained engagement across the term against a published bar, not a count of interventions
and never a ranking.

> **Why it exists.** Geopolitical analysis is argued, not computed. The room is where you learn to
> defend a judgement against someone who reads the same evidence differently.

### Quizzes — 15% (3 × 5%)

Twenty minutes at the start of Sessions 04, 07 and 10, on paper, closed book. Each covers the
three sessions before it: the concepts, the big work and its target figure, and the reading of one
unseen Tableau chart. Specimen questions: [`assessments/quizzes/`](assessments/quizzes/README.md).

> **Why it exists.** The take-home examination assumes you have the concepts cold. Three small
> checkpoints tell you — and me — early whether you do.

### Risk Brief — 15%

One individual presentation in one of Sessions 02–11: **four minutes, one current geopolitical
development, one Tableau view built from data you collected, one named multinational, one
recommendation.** One question follows, from the room or the instructor. Brief and rubric:
[`assessments/risk-brief/`](assessments/risk-brief/README.md).

> **Why it exists.** The practice rounds are done in teams; this is where you show you can do alone,
> and against the clock, what a risk analyst does every week.

### Team work — 20%

Teams of three or four, formed in Session 02, each adopt **one named multinational** for the whole
term. The team builds a **geopolitical risk dashboard** for it on Tableau Public, drawing on at least
four of the datasets collected in the practice rounds, and writes a 2,500-word memo to its board.
Presented in Session 12 (5 of the 20 points); the memo and dashboard are due one week later
(15 points). Brief: [`assessments/team-project/`](assessments/team-project/README.md).

> **Why it exists.** It is the Evaluation outcome made concrete: design a risk assessment strategy
> for a real firm and defend the method behind it.

### Take-home examination — 40%

Individual. **Three hours of work, released in a 48-hour window** during the final examination
period. You receive an unseen scenario, a data source to collect from, and a firm. You produce one
Tableau workbook and a written assessment answering conceptual and applied questions across the
whole course. Open book, open notes; no collaboration of any kind. Brief and specimen:
[`assessments/take-home/`](assessments/take-home/README.md).

> **Why it exists.** It tests the whole course the way the work is actually done: with your sources
> open, under time pressure, alone, and answerable for every number.

### From a mark to a letter

The five components give a mark out of 100, converted to a letter grade according to the HEC
Montréal M. Sc. grading scale. Nothing within a component is curved.

---

## 7. Tools

| Tool | Why this one |
|---|---|
| **Tableau Desktop** (free academic licence, *Tableau for Students*; fallback: the free *Tableau Public* desktop edition) | The industry standard for analytical dashboards in risk and strategy teams. You will be hired into it. |
| **Tableau Prep Builder** (academic licence, where available) | Cleaning and reshaping you can show and audit, step by step. Optional: every practice round can be prepared in Desktop's data source pane instead. |
| **Tableau Public** | Where the team dashboard is published, and where you can study how others built theirs. |
| **A spreadsheet** (Excel, LibreOffice or Numbers) | For opening files at source and reading codebooks. Not for analysis you cannot reproduce. |
| **A provenance log** | One table per practice round: what you downloaded, from where, when, which version, under which licence. Template in [`TABLEAU-TOOLKIT.md`](TABLEAU-TOOLKIT.md). |

Installation and the skills ladder, session by session: [`TABLEAU-TOOLKIT.md`](TABLEAU-TOOLKIT.md).
Every dataset, its access conditions and its traps: [`DATA-SOURCES.md`](DATA-SOURCES.md).

> **On language models.** You may use one — to read a codebook faster, to draft a calculated field,
> to argue against your recommendation. You may not use one to write the slide, the memo or the
> take-home for you. Every factual claim a model gives you about a dataset is unverified until you
> have checked it against the codebook. Say where you used it.

---

## 8. Standing rules on data

**Collect at source.** Download from the producer of the data — the author's page, the agency, the
repository — never from a mirror, a blog or a classmate.

**Log provenance.** Every file you use has a line in the provenance log: source, URL, version,
date accessed, licence, and a note of anything odd.

**Never edit raw files.** Keep the download as it arrived in `raw/`. All changes happen in Tableau
or Tableau Prep, where they are visible and repeatable.

**Respect the licence.** Several sources (ACLED, GSDB, some ISO tables) restrict redistribution.
Publish derived views on Tableau Public; do not publish the raw extract.

**Name your decisions.** If you dropped a country, rebased a year or chose a deflator, it goes on
the slide.

---

## 9. Policies

**Academic integrity.** HEC Montréal's regulations on plagiarism and cheating apply in full. In the
take-home examination any collaboration, including with a language model producing the text, is a
violation.

**Late work.** The team memo loses 5% of its mark per day late. A Risk Brief missed without a
documented reason scores zero; with one, it is rescheduled.

**Accommodations.** Students with accommodation letters from the Service aux étudiants should contact
the instructor in the first two weeks.

**Language.** The course is taught in English. Written work may be submitted in French or English.

---

## 10. Core references

Full article–data map: [`REPLICATIONS.md`](REPLICATIONS.md). Complete bibliography:
[`READINGS.md`](READINGS.md).

Abbott, K. W., & Snidal, D. (2009). The governance triangle: Regulatory standards institutions and
the shadow of the state. In W. Mattli & N. Woods (Eds.), *The politics of global regulation*.
Princeton University Press. https://doi.org/10.1515/9781400830732.44

Bjola, C., & Manor, I. (2018). Revisiting Putnam's two-level game theory in the digital age:
Domestic digital diplomacy and the Iran nuclear deal. *Cambridge Review of International Affairs*,
31(1), 3–32. https://doi.org/10.1080/09557571.2018.1476836

Brunsson, N., Rasche, A., & Seidl, D. (2012). The dynamics of standardization: Three perspectives on
standards in organization studies. *Organization Studies*, 33(5–6), 613–632. https://doi.org/10.1177/0170840612450120

Green, J. F. (2013). *Rethinking private authority: Agents and entrepreneurs in global environmental
governance*. Princeton University Press.

Kuziemko, I., & Werker, E. (2006). How much is a seat on the Security Council worth? Foreign aid and
bribery at the United Nations. *Journal of Political Economy*, 114(5), 905–930. https://doi.org/10.1086/507155

Le Billon, P., & Shykora, L. (2020). Conflicts, commodities and the environmental geopolitics of
supply chains. In S. O'Lear (Ed.), *A research agenda for environmental geopolitics* (pp. 59–73).
Edward Elgar. https://doi.org/10.4337/9781788971249.00012

Mansfield, E. D. (2021). International trade and conflict. In J. C. W. Pevehouse & L. Seabrooke
(Eds.), *The Oxford handbook of international political economy* (pp. 660–671). Oxford University
Press. https://doi.org/10.1093/oxfordhb/9780198793519.013.27

Mattli, W., & Büthe, T. (2003). Setting international standards: Technological rationality or
primacy of power? *World Politics*, 56(1), 1–42. https://doi.org/10.1353/wp.2004.0006
