# Session 08 — Practice round 08 (second half, 90 min)

# Rebuild the cyber-conflict picture

Slides: [`INTE60019A-S08-Practice.qmd`](INTE60019A-S08-Practice.qmd)

> **The target.** Valeriano & Maness's descriptive picture of interstate cyber conflict: incidents
> **by year and method**, the **distribution of severity**, and the **initiator × target matrix** of
> rival dyads — rebuilt from DCID v2.0, then confronted with the wider EuRepoC record.

Work in your project teams. Everyone builds their own workbook; the team hands in one slide.

---

## 1 · Collect — 15 min

If you did the pre-session, both files are in `data/raw/`. If not:

- **DCID v2.0** — [doi:10.7910/DVN/CQOMYV](https://doi.org/10.7910/DVN/CQOMYV) → file
  `Master_DCID_2.0_Release_public_Sep2022.tab` → *Access File → Comma Separated Values (Original File
  Format)*. The codebook is not on Dataverse: *Codebook 2.0* is on
  [ryanmaness.com/cyber-conflict-dataset](https://www.ryanmaness.com/cyber-conflict-dataset).
- **EuRepoC v1.3** — [doi:10.5281/zenodo.14965395](https://doi.org/10.5281/zenodo.14965395) →
  `eurepoc_global_dataset_1_3.csv` and `eurepoc_codebook_1_2.pdf`.

Provenance log — one line per file:

| file | source | url | version / release | accessed | licence | notes |
|---|---|---|---|---|---|---|
| Master_DCID_2.0_…csv | Maness, Valeriano et al. | doi:10.7910/DVN/CQOMYV | v2.0, Sep 2022 | *today* | CC0, cite | *original CSV behind the .tab; 433 rows* |
| eurepoc_global_dataset_1_3.csv | EuRepoC | doi:10.5281/zenodo.14965395 | v1.3 (1.3.2), Mar 2025 | *today* | CC BY-NC 4.0 | *3,414 rows* |

---

## 2 · Prepare — 15 min

1. **Connect → Text file** → the DCID CSV. Look at the grid.
2. Find the columns (checked in the September 2022 file — see [`../data/README.md`](../data/README.md)):
   `initiator`, `StateA`, `StateB`, `Dyadpair`, `interactionstartdate`, `method`, `severity`,
   `targettype`. **There is no target column**, and `StateA`/`StateB` are the dyad, not initiator
   and target. Write the exact names in your log.
3. `initiator` is a **COW code** (16 values: 2 US, 365 Russia, 710 China, 630 Iran, 731 North Korea,
   770 Pakistan, 666 Israel, 750 India, 732 South Korea…). `Dyadpair` joins the COW codes of
   `StateA` and `StateB` (`2365` = 2 + 365; State B's code is always the last three digits). Build
   names for both sides:
   ```text
   [Initiator] = IF STR([initiator]) = RIGHT(STR([Dyadpair]), 3)
                 THEN TRIM([StateB]) ELSE TRIM([StateA]) END
   [Target]    = IF STR([initiator]) = RIGHT(STR([Dyadpair]), 3)
                 THEN TRIM([StateA]) ELSE TRIM([StateB]) END
   ```
   Two incidents (313 and 335) name an initiator outside the dyad — check them by hand.
4. `method` and `targettype` are **codes**. Alias them from the codebook: `method` 1 vandalism,
   2 denial of service, 3 network intrusion, 4 network infiltration (4.1–4.4 are infiltration
   sub-types — group them, or round down with `FLOOR([method])`); `targettype` 1 private / non-state,
   2 government non-military, 3 government military.
5. `interactionstartdate` is month/day/year text (`2/1/2008`). If Tableau has not read it as a date,
   create `Start Year` = `YEAR(DATEPARSE("M/d/yyyy", [interactionstartdate]))`.
6. Record every recode in the log.

---

## 3 · Replicate — 25 min

### Sheet 1 · "Incidents per year, by method"

1. `Start Year` → **Columns** (discrete is fine: one bar per year).
2. `COUNTD([Cyberincidentnum])` (or the table's record count) → **Rows**.
3. Method → **Colour**. Stacked bars.
4. Title states the finding. Caption: *Source: DCID v2.0 (Maness, Valeriano et al., 2022), accessed …*

### Sheet 2 · "How severe?"

1. Severity → **Columns** (discrete), count → **Rows**. A bar chart of the distribution.
2. Add a **reference line** at the median severity (*Analytics → Median with Quartiles* or a
   constant you computed).
3. Annotate the highest-severity incidents: what were they?

### Sheet 3 · "Who targets whom" — the dyad matrix

1. `[Initiator]` → **Rows**, `[Target]` → **Columns** (the calculated fields from step 2.3).
2. Count → **Colour**, then *Show Me → highlight table*. Add count to **Label**.
3. Sort initiators by total count (right-click the pill → *Sort → Field → Count → Descending*).
4. Which five cells hold most incidents? Do they match the book's regional rivals?

### Dashboard · link them

1. *New Dashboard* → drag Sheet 3 on the left, Sheets 1 and 2 on the right.
2. *Dashboard → Actions → Add Action → Filter…* — source sheet: Sheet 3; target sheets: 1 and 2;
   run on **Select**; clearing the selection **shows all values**.
3. Click the US–China cell, then the Russia–Ukraine cell. Write down how their histories differ.

---

## 4 · Compare and break — 20 min

1. **Differ.** Put your Sheets 1–2 beside the book's descriptive figures. DCID v2.0 runs to 2020 (one
   incident starts in January 2021) and has been revised since 2015. Write one difference, and its likely cause.
2. **Break the population.** Load EuRepoC as a second data source. Rebuild Sheet 1 on it — first
   with **all** incidents, then filtered to incidents attributed to **state** actors (field
   `initiator_category`; read the codebook to decide which values — `State` only, or also
   `State affiliated actor`). EuRepoC's `start_date` is day.month.year text:
   `DATEPARSE("dd.MM.yyyy", [start_date])`. How many times larger is EuRepoC? What does
   the difference tell you about what DCID leaves out?
3. **Restraint, tested.** In DCID, what share of incidents sits in the lowest severity levels?
   (*Quick Table Calculation → Percent of Total* on Sheet 2.) Does the evidence support restraint
   *as of 2020*? What would you need to know about 2022 onward?
4. **Extend — the firm.** Using `targettype` = 1 (*private / non-state*), isolate incidents that hit
   non-government targets. Which dyads hit firms most? Name a sector you would worry about.

---

## 5 · The catch — 15 min

One slide (a dashboard exported as an image):

| Original | Ours | The catch |
|---|---|---|
| The book's incident picture | Your dashboard | One sentence: what this matrix does **not** license a multinational to conclude |

A hint: it is a matrix of *publicly attributed* incidents between *rivals*. A member drawn at random
presents in two minutes.

---

## Hand in

On ZoneCours before leaving: your `.twbx` and provenance log. Formative; counts towards participation.

**The one rule:** your log records at least one place where the data disagreed with the book — a
dyad that is missing, a method with a different label, a severity that shifted between versions.

---

## What loses credit

- Comparing DCID with *all* of EuRepoC without saying so
- Empty cells read as "no cyber conflict" rather than "no rivalry in the data"
- Codes (1, 2, 3) left on the chart instead of aliased labels
- A catch about the book rather than about what the firm may conclude
