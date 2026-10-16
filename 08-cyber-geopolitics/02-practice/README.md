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
  `Master_DCID_2.0_Release_public_Sep2022.tab` → *Access File → Comma Separated Values*; download the
  codebook too.
- **EuRepoC v1.3** — [doi:10.5281/zenodo.14965395](https://doi.org/10.5281/zenodo.14965395) →
  `eurepoc_global_dataset_1_3.csv` and the codebook.

Provenance log — one line per file:

| file | source | url | version / release | accessed | licence | notes |
|---|---|---|---|---|---|---|
| Master_DCID_2.0_…csv | Maness, Valeriano et al. | doi:10.7910/DVN/CQOMYV | v2.0, Sep 2022 | *today* | free, cite | *exported from .tab* |
| eurepoc_global_dataset_1_3.csv | EuRepoC | doi:10.5281/zenodo.14965395 | v1.3, Mar 2025 | *today* | free, cite | |

---

## 2 · Prepare — 15 min

1. **Connect → Text file** → the DCID CSV. Look at the grid.
2. In the codebook, identify the columns for **initiator**, **target**, **start date or year**,
   **method**, **severity**, and **target type**. Write the exact names in your log.
3. Countries may be stored as **COW codes** (numbers). If so, create **aliases** (right-click the
   field → *Aliases…*) for the dozen or so states that appear, or join a small COW ↔ name sheet.
4. Methods and target types may be stored as **codes** (1, 2, 3, 4). Use the codebook to alias them
   — e.g. vandalism, denial of service, network intrusion, network infiltration. Check the list
   against the codebook; do not trust this sentence.
5. If the start date is a string, create a calculated field `Start Year`:
   `YEAR(DATE([start date field]))` — or use the year column if one exists.
6. Record every recode in the log.

---

## 3 · Replicate — 25 min

### Sheet 1 · "Incidents per year, by method"

1. `Start Year` → **Columns** (discrete is fine: one bar per year).
2. `Number of Records` (or `COUNT` of an incident ID) → **Rows**.
3. Method → **Colour**. Stacked bars.
4. Title states the finding. Caption: *Source: DCID v2.0 (Maness, Valeriano et al., 2022), accessed …*

### Sheet 2 · "How severe?"

1. Severity → **Columns** (discrete), count → **Rows**. A bar chart of the distribution.
2. Add a **reference line** at the median severity (*Analytics → Median with Quartiles* or a
   constant you computed).
3. Annotate the highest-severity incidents: what were they?

### Sheet 3 · "Who targets whom" — the dyad matrix

1. Initiator → **Rows**, target → **Columns**.
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

1. **Differ.** Put your Sheets 1–2 beside the book's descriptive figures. DCID v2.0 runs to 2020 and
   has been revised since 2015. Write one difference, and its likely cause.
2. **Break the population.** Load EuRepoC as a second data source. Rebuild Sheet 1 on it — first
   with **all** incidents, then filtered to incidents attributed to **state** actors (read the
   codebook to decide which field and which values). How many times larger is EuRepoC? What does
   the difference tell you about what DCID leaves out?
3. **Restraint, tested.** In DCID, what share of incidents sits in the lowest severity levels?
   (*Quick Table Calculation → Percent of Total* on Sheet 2.) Does the evidence support restraint
   *as of 2020*? What would you need to know about 2022 onward?
4. **Extend — the firm.** Using target type, isolate incidents whose target is **private** or
   **commercial**. Which dyads hit firms most? Name a sector you would worry about.

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
