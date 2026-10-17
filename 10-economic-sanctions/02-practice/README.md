# Session 10 — Practice round 10 (second half, 90 min)

# Rebuild the sanctions record

Slides: [`INTE60019A-S10-Practice.qmd`](INTE60019A-S10-Practice.qmd)

> **The target.** The Global Sanctions Data Base's descriptive picture (Felbermayr et al., 2020):
> **active sanctions cases per year, by type**, from 1950 to today, and the **distribution of
> outcomes by objective** — rebuilt from Release 5, then confronted with the **threats** in TIES.

Work in your project teams. The last **20 minutes** are the team dashboard skeleton review.

> **Licence.** GSDB data may not be redistributed. Hand in on **ZoneCours only**. Do not publish this
> workbook to Tableau Public.

---

## 1 · Collect — 5 min

Everything should already be in `data/raw/`: the GSDB files as e-mailed, TIES v4.0, both codebooks,
and `years.csv` (see [`../data/README.md`](../data/README.md)). Fill the provenance log — for the
GSDB, the **release number** and the **date of the e-mail**.

---

## 2 · Prepare — 20 min

1. **Connect → Text file / Excel** → the GSDB **case-level** file. Confirm in the codebook, and log,
   the names used below: `case_id`, `sanctioned_state`, `sanctioning_state`, `begin_year`,
   `end_year`, the six **type** columns, `objective`, `success`.
2. **Pivot the types.** The six types are separate 0/1 columns (`trade`, `financial`, `travel`,
   `arms`, `military`, `other`): select them in the grid → right-click → **Pivot**. Rename
   `Pivot Field Names` → `Type`, `Pivot Field Values` → `Type flag`. Filter later on `Type flag = 1`.
3. **Build the years.** Add `years.csv` to the canvas and **join** it to the GSDB table with two
   clauses:
   - `Year` **>=** `begin_year`
   - `Year` **<=** *join calculation* `IFNULL([end_year], 2025)`
   (click the right-hand field of a clause → *Create Join Calculation*). Each case now has one row per
   active year — and, after the pivot, one per type. (In the R5 file ongoing cases already carry
   `end_year` = 2025; the `IFNULL` is a guard for releases that leave it empty.)
4. **Check the grain.** Note the row count before and after. Write in the log what one row now is.
5. **Outcomes.** Outcomes are **not** indicator columns: `success` is one text field holding one code
   per objective, in the order of `objective` (e.g. `objective` = `human_rights,democracy`,
   `success` = `failed,ongoing`). Take the first objective and its outcome:
   ```
   Objective  =  TRIM(SPLIT([objective], ",", 1))
   Outcome    =  CASE TRIM(SPLIT([success], ",", 1))
                 WHEN "success_total"   THEN "Success"
                 WHEN "success_part"    THEN "Partial success"
                 WHEN "nego_settlement" THEN "Negotiated settlement"
                 WHEN "failed"          THEN "Failure"
                 WHEN "ongoing"         THEN "Ongoing"
                 ELSE "Not coded" END
   ```
   Log the decision: cases with several objectives count here under their **first** one only.

---

## 3 · Replicate — 25 min

### Sheet 1 · "Active sanctions cases per year, by type"

1. `Year` → **Columns** (continuous).
2. `COUNTD([case_id])` → **Rows** — *count distinct*, never `SUM`, because the pivot and the
   scaffold multiply rows.
3. Filter `Type flag = 1`; `Type` → **Colour**; mark type **Area** or **Bar**.
4. Note in a caption: a case with several types is counted once **in each** type, so the stacked
   total exceeds the number of cases. Then build a version with no colour to show the true total.
5. Annotate 1990–91, 2014 and 2022. What explains the shape?

### Sheet 2 · "How do cases end, by objective?"

1. Use the **case-level** grain: duplicate the data source **without** the year scaffold, or use
   `{FIXED [case_id] : MIN([Outcome])}`.
2. `Objective` → **Rows**, `COUNTD([case_id])` → **Columns**, `Outcome` → **Colour**.
3. *Quick Table Calculation → Percent of Total*; *Edit Table Calculation → Compute using* `Outcome`
   so each objective sums to 100%.
4. Exclude ongoing cases from the denominator in a second version. How much does the success share
   move? (That is a coding decision too.)

### Sheet 3 · "One target's history" — a Gantt chart

1. Filter `sanctioned_state` to **one** target (Iran, Russia, Cuba, North Korea…) — with a
   calculated filter `CONTAINS([sanctioned_state], "Iran")`, because some cases list several targets.
2. `begin_year` → **Columns** (continuous); `case_id` (or `sanctioning_state` + `case_id`) → **Rows**.
3. Mark type **Gantt Bar**; calculated field `Duration` = `IFNULL([end_year], 2025) - [begin_year]` → **Size**.
4. `Type` → **Colour**. What does the target's history look like — layers added, never removed?

---

## 4 · Compare and break — 10 min

1. **Differ.** Put Sheet 1 beside the GSDB paper's figure. Release 5 runs years further and has
   added and recoded cases: write one difference.
2. **Threats vs impositions.** Open TIES. Using the manual, separate **threatened-only** cases
   (`imposition` = 0) from **imposed** cases (`imposition` = 1) and count each per `startyear`
   (1945–2005). Put the counts beside GSDB
   impositions for the same years. What does the gap say about Drezner's selection effect?
3. **Extend — the firm.** For your team's firm, list its top five countries. How many active GSDB
   cases name each as the sanctioned state in the latest year?

---

## 5 · The catch — 10 min

| Original | Ours | The catch |
|---|---|---|
| The GSDB paper's figure | Your Sheet 1 (and Sheet 2) | One sentence: what these charts do **not** license a multinational to conclude about *its* sanctions exposure |

A member drawn at random presents in two minutes.

---

## 6 · Team dashboard skeleton review — 20 min

Have your team-project workbook open. The instructor checks: four datasets from three indicator
families; the composite index; at least one channel view; the watchlist with thresholds. You leave
with three written comments.

---

## Hand in

On **ZoneCours only**: `.twbx` and provenance log. Formative; counts towards participation.

**The one rule:** your log records at least one place where the data disagreed with the paper.

---

## What loses credit

- `SUM` of anything after the scaffold join
- Stacked type totals presented as the number of cases
- Success shares without saying whether ongoing cases are in the denominator
- The GSDB workbook published on Tableau Public
