# Tableau toolkit

Everything you need to install, the one new skill each session adds, the conventions every chart
follows, and the traps that cost most marks.

---

## 1. Installation — before Session 01

| Tool | How | Used for |
|---|---|---|
| **Tableau Desktop** | Free academic licence through **Tableau for Students** (Tableau Academic Programs). Request it with your HEC e-mail; the key arrives by e-mail. | every practice round |
| **Tableau Prep Builder** | Same licence, same key, where the academic programme includes it — optional | cleaning, reshaping and unioning files (from Session 02; essential in Session 07) |
| **Tableau Public** | Free account at public.tableau.com | publishing the team dashboard and Risk Briefs |
| A spreadsheet | Excel, LibreOffice Calc or Numbers | opening files at source, reading codebooks |

**Test.** Open Tableau Desktop → *Sample – Superstore* → `Order Date` to Columns, `Sales` to Rows.
A line appears: you are ready.

**If the key has not arrived** install the 14-day trial and switch to the key when it comes. The
academic licence is renewable each year while you are enrolled.

> **If the academic programme no longer covers your case.** Tableau's academic terms have changed
> more than once (reports in 2025 indicated that free student licences for Desktop and Prep were
> being withdrawn in some programmes; check [tableau.com/academic/students](https://www.tableau.com/academic/students)
> and HEC's own software page at the start of term). The fallback is the free **Tableau Public**
> desktop edition. Everything in the course works in it — pivots, joins, relationships, LOD,
> parameters, maps, dashboards — with two differences you must manage:
>
> 1. **It saves only to Tableau Public**, where workbooks are public. For data whose licence forbids
>    redistribution (the Global Sanctions Data Base, possibly the ISO Survey), publish only
>    aggregated views, keep "allow download" off, and hand in screenshots plus your calculated-field
>    definitions instead of a `.twbx`.
> 2. **No Tableau Prep.** Do the Session 07 cleaning in the data source pane (pivot, split, union,
>    calculated fields) — the practice brief gives both routes.

**Mac and Windows** behave identically for everything in this course, with one exception: on a Mac,
right-drag is *Option*-drag.

---

## 2. The skills ladder

One new skill per session, always applied to the session's replication. Nothing is taught twice;
everything is assumed afterwards.

| Session | Replication | The new skill |
|---|---|---|
| **01** | GPR index | Connect to Excel · fix data types · continuous dates · reference lines · annotations · captions |
| **02** | G7 share of world GDP | **Pivot** wide years to long · filter on ISO codes, not names · area chart · **percent of total** (table calculation) |
| **03** | Distribution of power | **Calculated fields** · ratios · **parameters** to choose a country · dual axis |
| **04** | Trade between blocs | **Joins and relationships** on dyads (exporter × importer × year) · **groups** and **sets** for blocs · indexing to a base year |
| **05** | Aid and the Security Council | **LOD expressions** (`FIXED`) to compute "years relative to a term" · event-time charts · reference bands |
| **06** | ISO 14001 diffusion | **Maps** · geocoding by ISO code · fixing unmatched countries · the **Pages** shelf for animation · small multiples |
| **07** | Firm-level risk and your coded corpus | **Tableau Prep** flows · unions · cleaning text-coded data · **normalisation** (min–max, z-score) · **parameters as weights** in a composite index |
| **08** | Cyber incidents | **Highlight tables** · dyad matrices (initiator × target) · **filter and highlight actions** |
| **09** | Embassies and exports | **Log scales** · **trend lines** and what their R² and p-value do and do not say · clusters |
| **10** | Sanctions episodes | **Gantt charts** for episode durations · stacked bars of shares · **quick table calculations** |
| **11** | Critical-mineral concentration | **Herfindahl–Hirschman index** with LOD · treemaps · **dashboard actions** across sheets |
| **12** | Your team dashboard | **Dashboards** · **stories** · publishing to Tableau Public · writing captions a board can read |

---

## 3. Conventions every chart follows

1. **A title that states the finding**, not the variable. *"The G7's share of world GDP fell by a
   third after 1990"*, not *"GDP share"*.
2. **A source caption**: dataset, producer, version, access date. No caption, no credit.
3. **Units on every axis.** Current US dollars or constant? Index base year? Share or count?
4. **Direct labels** in place of legends wherever there are fewer than six series.
5. **One accent colour** for the series the argument is about; greys for the rest.
6. **Annotate the events** that explain the shape of the line.
7. **Name your decisions** in a footnote: countries dropped, years rebased, codes changed.

---

## 4. The traps that cost marks

| Trap | Symptom | Fix |
|---|---|---|
| **Joining on country names** | Côte d'Ivoire, Türkiye, Korea, Rep. silently drop out | Always join on **ISO 3166 alpha-3** codes. Keep a concordance sheet for datasets that use COW or UN codes |
| **Wide years** | 60 columns called `1960` … `2023` | **Pivot** them in the data source pane (select columns → right-click → *Pivot*) |
| **SUM of an index** | A line ten times too high | An index is averaged, not summed. Check the aggregation on every pill |
| **Discrete vs continuous dates** | A bar for "May" across all years | Use the *continuous* date (green pill) for time series |
| **Duplicated rows after a join** | Totals inflate | Check the row count before and after; use a **relationship** instead of a join when the grain differs |
| **Revised data** | Your numbers do not match last year's paper | That is a finding, not an error: log the release you used |
| **Aggregates in country lists** | "World", "High income" and "Euro area" counted as countries | Filter on a country list, not on "everything that is not blank" |
| **Percent of total computed the wrong way** | Shares that sum to 100% across years instead of within each year | *Edit Table Calculation → Compute using* the country dimension, restart every year |

---

## 5. The provenance log

One CSV per practice round, in the session's `data/` folder. Template:
[`templates/provenance-log.csv`](templates/provenance-log.csv).

| Column | What goes in it |
|---|---|
| `file` | The file name exactly as saved in `raw/` |
| `source` | The producer: author, agency, organisation |
| `url` | The landing page you downloaded from — not a mirror |
| `version_or_release` | Release number, "last updated" date, or edition |
| `accessed` | Today's date, ISO format: `2026-09-02` |
| `licence` | Free / registration / request / restricted redistribution |
| `notes` | Anything odd — and **at least one place where the data disagreed with the paper** |

---

## 6. Handing in

- *File → Export Packaged Workbook* (`.twbx`) — it contains the data extract, so the workbook opens
  on any machine. Do not upload a `.twb`: it does not contain the data.
- For data whose licence forbids redistribution (several of them — see
  [`DATA-SOURCES.md`](DATA-SOURCES.md)), upload to **ZoneCours only**, never to Tableau Public.
