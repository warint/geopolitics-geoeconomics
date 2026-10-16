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

1. **Connect → Text file / Excel** → the GSDB **case-level** file. From the codebook, note the exact
   names of: case identifier, sanctioned state, sanctioning state, begin year, end year, the **type**
   columns, the **objective** column(s), the **outcome** column(s).
2. **Pivot the types.** If the six types are separate indicator columns (trade, financial, travel,
   arms, military assistance, other), select them in the grid → right-click → **Pivot**. Rename
   `Pivot Field Names` → `Type`, `Pivot Field Values` → `Type flag`. Filter later on `Type flag = 1`.
3. **Build the years.** Add `years.csv` to the canvas and **join** it to the GSDB table with two
   clauses:
   - `Year` **>=** `begin`
   - `Year` **<=** *join calculation* `IFNULL([end], 2025)`
   (click the right-hand field of a clause → *Create Join Calculation*). Each case now has one row per
   active year — and, after the pivot, one per type.
4. **Check the grain.** Note the row count before and after. Write in the log what one row now is.
5. **Outcomes.** If outcomes are separate indicator columns, create one field `Outcome`:
   ```
   IF [success_total] = 1 THEN "Success"
   ELSEIF [success_part] = 1 THEN "Partial success"
   ELSEIF [nego_settlement] = 1 THEN "Negotiated settlement"
   ELSEIF [fail] = 1 THEN "Failure"
   ELSE "Ongoing / not coded" END
   ```
   **Replace the field names with the codebook's** — these are illustrative.

---

## 3 · Replicate — 25 min

### Sheet 1 · "Active sanctions cases per year, by type"

1. `Year` → **Columns** (continuous).
2. `COUNTD([case id])` → **Rows** — *count distinct*, never `SUM`, because the pivot and the
   scaffold multiply rows.
3. Filter `Type flag = 1`; `Type` → **Colour**; mark type **Area** or **Bar**.
4. Note in a caption: a case with several types is counted once **in each** type, so the stacked
   total exceeds the number of cases. Then build a version with no colour to show the true total.
5. Annotate 1990–91, 2014 and 2022. What explains the shape?

### Sheet 2 · "How do cases end, by objective?"

1. Use the **case-level** grain: duplicate the data source **without** the year scaffold, or use
   `{FIXED [case id] : MIN([Outcome])}`.
2. `Objective` → **Rows**, `COUNTD([case id])` → **Columns**, `Outcome` → **Colour**.
3. *Quick Table Calculation → Percent of Total*; *Edit Table Calculation → Compute using* `Outcome`
   so each objective sums to 100%.
4. Exclude ongoing cases from the denominator in a second version. How much does the success share
   move? (That is a coding decision too.)

### Sheet 3 · "One target's history" — a Gantt chart

1. Filter sanctioned state to **one** target (Iran, Russia, Cuba, North Korea…).
2. `begin` → **Columns** (continuous); case id (or sanctioning state + case id) → **Rows**.
3. Mark type **Gantt Bar**; calculated field `Duration` = `IFNULL([end], 2025) - [begin]` → **Size**.
4. `Type` → **Colour**. What does the target's history look like — layers added, never removed?

---

## 4 · Compare and break — 10 min

1. **Differ.** Put Sheet 1 beside the GSDB paper's figure. Release 5 runs years further and has
   added and recoded cases: write one difference.
2. **Threats vs impositions.** Open TIES. Using the manual, separate **threatened-only** cases from
   **imposed** cases and count each per start year (1945–2005). Put the counts beside GSDB
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
