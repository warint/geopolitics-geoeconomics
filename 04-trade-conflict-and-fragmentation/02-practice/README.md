# Session 04 — Practice round 04 (second half, 90 min)

# Rebuild trade within and between blocs

Slides: [`INTE60019A-S04-Practice.qmd`](INTE60019A-S04-Practice.qmd)

> **The target.** Gopinath, Gourinchas, Presbitero & Topalova (2025): trade **between** geopolitical
> blocs against trade **within** them, before and after Russia's invasion of Ukraine. You define the
> blocs yourself from UN General Assembly ideal points, then watch what happens to the finding when
> you move the line.

Work in your team. One extract per team; everyone builds their own workbook.

---

## 1 · Collect — 10 min

Ideal points and codebook from Dataverse; your IMF IMTS extract of bilateral goods exports, annual,
2015–latest. If not done: [`../data/README.md`](../data/README.md).

Provenance log: one line per file. For the ideal points, log **version 39** and the change to
calendar-year estimation. For IMF, log the date of the extract and the exact indicator you chose.

---

## 2 · Prepare — 25 min

### A · Classify countries into blocs (ideal points)

1. **Connect → Text file** → `IdealpointestimatesFP_2026FP.csv`. The **ISO 3-letter code**, the
   **year** and the **ideal point** are `iso3c`, `year` and `IdealPointFP` (see the codebook).
   Rename `iso3c` → `iso3` and `IdealPointFP` → `IdealPoint` (right-click → *Rename*): the steps
   below use those names.
2. New sheet. Filter `year` = **2021** — the last full year before the invasion. (Gopinath et al. may
   use a different reference: check, and log the difference.)
3. Read the ideal points of the US (`USA`) and China (`CHN`) off the data. Create two parameters,
   `US ref` and `CHN ref` (*Float*), and type those two values in.
4. Create a third parameter `Margin` (*Float*, start at **0.5**) and the calculated field:

   ```text
   Bloc =
   IF ABS([IdealPoint] - [CHN ref]) - ABS([IdealPoint] - [US ref]) > [Margin] THEN "US-leaning"
   ELSEIF ABS([IdealPoint] - [US ref]) - ABS([IdealPoint] - [CHN ref]) > [Margin] THEN "China-leaning"
   ELSE "Non-aligned"
   END
   ```

5. `iso3` → Rows, `Bloc` → Rows, `IdealPoint` → Text. Sort by ideal point. Does the classification
   look right for countries you know? Adjust `Margin` until you can defend it — and write down the
   value and why.
6. **Export the classification** as a derived file: *Worksheet → Export → Crosstab to Excel* (or
   *View Data → Export All* to CSV). Save it as `data/derived/blocs_2021.csv` — **not** in `raw/`.
   Add a provenance line: derived from the ideal points, `Margin` = …, base year 2021.

### B · Relate trade to blocs — the dyad model

1. New data source: **Connect → Text file** (or Excel) → your IMF extract. Identify the exporter,
   partner, year and value columns — in the IMF's SDMX layout `COUNTRY`, `COUNTERPART_COUNTRY`,
   `TIME_PERIOD`, `OBS_VALUE` — and rename them `exporter`, `partner`, `year`, `value`. Keep only
   `INDICATOR` = `XG_FOB_USD`.
2. Remove aggregate partners ("World", "Advanced Economies", regions — codes starting with `G` or
   `TX`, e.g. `G001` World): filter them out, and log which.
3. In the data source pane, drag `blocs_2021.csv` onto the canvas: Tableau creates a
   **relationship**. Click the noodle → relate `exporter` = `iso3`.
4. Drag `blocs_2021.csv` onto the canvas **a second time**. Relate `partner` = `iso3`. Rename this
   copy **Partner blocs** and its `Bloc` field **Partner bloc**; rename the first copy's field
   **Exporter bloc**.
5. IMTS uses ISO3 codes, so the relationship works directly. If your download shows names instead,
   you need a concordance table — log it.

---

## 3 · Replicate — 25 min

### Sheet 1 · "Trade within and between blocs"

1. The pair type:

   ```text
   Pair type =
   IF [Exporter bloc] = "Non-aligned" OR [Partner bloc] = "Non-aligned" THEN "Involves non-aligned"
   ELSEIF [Exporter bloc] = [Partner bloc] THEN "Within bloc"
   ELSE "Between US- and China-leaning"
   END
   ```

2. The index, 2021 = 100:

   ```text
   Trade index = SUM([value]) / WINDOW_SUM(SUM(IF [year] = 2021 THEN [value] END)) * 100
   ```

3. `year` → Columns as a **discrete** dimension (blue); `Trade index` → Rows; `Pair type` → Colour.
   Right-click `Trade index` → **Edit Table Calculation → Compute Using → year**, so each pair type is
   indexed to its own 2021.
4. Reference line at 100. Annotate 2022.
5. Title with the finding. Caption: both sources with versions, and *"Blocs: ideal-point distance to
   US vs China, 2021, margin = …"*.

### Sheet 2 · "Who sits where?" — the classification on a map

`iso3` (geographic role *Country/Region*, ISO 3166-1 alpha-3) on the map, coloured by `Bloc`. Mark
your team firm's five main countries with a **group** (*Create → Group*, "Our markets").

---

## 4 · Compare and break — 20 min

1. **Compare.** Put Sheet 1 beside the paper's figure. Their data are quarterly and their estimate
   controls for other determinants of trade; ours is annual and raw. Does the direction match? Is the
   gap between "within" and "between" of a similar order? Write one difference and its likely cause.
2. **Break the bloc definition.** Move `Margin` (0.25, 1.0), re-export, refresh. Which countries
   change bloc? Does the gap between the lines survive? This is the most important answer of the round.
3. **Break the side of the trade.** If your extract has the mirror series (imports reported by the
   partner), rebuild the index with it. Same picture?
4. **Extend — connectors.** Create a **set** of non-aligned countries (*Create → Set*, *Top* tab: top
   10 by growth in exports to *both* blocs, 2021 → latest — or pick by hand from a table). Which are
   they? Is any of them among your firm's markets?

---

## 5 · The catch — 10 min

One slide:

| Original | Ours | The catch |
|---|---|---|
| Gopinath et al.'s within/between figure | Sheet 1, and the same chart with another `Margin` | One sentence: what this figure does **not** license your team's multinational to conclude |

A member drawn at random presents in two minutes.

---

## Hand in

On ZoneCours before leaving, one per team: `.twbx` (including the derived `blocs_2021.csv`),
provenance log, slide. Formative.

**The one rule:** your log records at least one place where the data disagreed with the paper — and
your slide says how your blocs differ from theirs.

---

## What loses credit

- Joining on country names (Türkiye, Côte d'Ivoire, Korea…)
- Leaving "World" or regional aggregates among the partners
- An index computed across pair types instead of within each one
- A bloc threshold that is not reported on the slide
