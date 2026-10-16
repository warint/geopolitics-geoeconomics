# Session 11 — Practice round 11 (second half, 80 min)

# Restrictions, concentration, and one dashboard

Slides: [`INTE60019A-S11-Practice.qmd`](INTE60019A-S11-Practice.qmd)

> **The targets.** Kowalski & Legendre (2023): (1) the growth of export restrictions on critical
> raw materials since 2009, by commodity and by restricting country; (2) the concentration of world
> production by country. You add a third view — the GSCPI — and wire the three into **one dashboard
> with an action**.

**The last practice round of the term.** The last twenty minutes of Session 10 reviewed your team
dashboard's skeleton. Most skeletons still lack a supply-chain channel and any interaction between
views. Leave today with both: the workbook you build is designed to be dropped into your team
dashboard, for your own firm's minerals.

Work in your project teams. Everyone builds the workbook; the team hands in one.

---

## 1 · Collect — 15 min

You arrive with the three files and your transcription (pre-session). Use these fifteen minutes to
**check**, not to download:

1. **The transcription.** One teammate who did not transcribe a mineral checks its rows against the
   USGS PDF. Does the sum of your country rows (with *Other countries*) match the *World total
   (rounded)* within rounding? Log the gap.
2. **The OECD export.** Open the CSV. Which measure types are present? Which years? Which
   commodity names will you need to match to *cobalt, graphite, lithium, rare earths*? (The
   inventory may split them — e.g. ores, concentrates, oxides, waste and scrap.)
3. **The GSCPI.** Which column is the latest vintage? Log its name.

Provenance log — one line per file, as always:

| file | source | url | version / release | accessed | licence | notes |
|---|---|---|---|---|---|---|
| oecd_export_restrictions.csv | OECD | data-explorer.oecd.org (dataflow id) | *edition* | *date* | free | *measure types kept* |
| usgs_world_production.csv | your transcription of USGS MCS | usgs.gov/…/mineral-commodity-summaries | *MCS edition, year column* | *date* | public domain | *gap to world total* |
| gscpi_interactive_data.csv | NY Fed | newyorkfed.org/research/policy/gscpi | *vintage column used* | *date* | free | |

---

## 2 · Prepare — 15 min

### The OECD inventory

1. Connect to the CSV. If years arrive as columns, **pivot** them (select the year columns →
   right-click → *Pivot*), rename `Pivot Field Names` → `Year` and `Pivot Field Values` → `Value`.
2. Make sure `Year` is a number or a date, not a string.
3. Create a calculated field **`Mineral`** that groups the inventory's commodity labels into your
   four minerals (and `Other` for the rest):

   ```text
   IF CONTAINS(LOWER([Commodity]), "cobalt") THEN "Cobalt"
   ELSEIF CONTAINS(LOWER([Commodity]), "graphite") THEN "Graphite"
   ELSEIF CONTAINS(LOWER([Commodity]), "lithium") THEN "Lithium"
   ELSEIF CONTAINS(LOWER([Commodity]), "rare earth") THEN "Rare earths"
   ELSE "Other" END
   ```

   Then **look at what landed in each group**: `CONTAINS` is blunt. Log every label you moved by hand.
4. Keep only rows where a measure **applies** (value 1, or a non-zero tax rate — whichever your export
   uses).

### The USGS transcription

5. Add `usgs_world_production.csv` as a **second data source** (not a join — the two tables do not
   share a grain).

### The GSCPI

6. Add the GSCPI CSV as a third data source. Keep `Date` and the **one** latest-vintage column;
   hide the rest.

---

## 3 · Replicate — 25 min

### Sheet 1 · "Export restrictions since 2009"

1. `Year` → Columns (continuous). `CNT` of measures (or `SUM([Value])` if one row = one measure)
   → Rows.
2. `Mineral` → Colour. Filter out `Other`, or keep it in grey — decide, and say why.
3. Compare the shape with the paper's figure: does the count multiply after 2009?

### Sheet 2 · "Who restricts?"

4. Restricting country → Rows, count of measures → Columns, sorted descending. `Mineral` → Colour.
   Top 15 countries.

### Sheet 3 · "Concentration of mine production" — the HHI

5. In the USGS source, create:

   ```text
   Share   =  [Production] / {FIXED [Mineral] : SUM([Production])}
   Share²  =  POWER([Share] * 100, 2)
   ```

6. Bar chart: `Mineral` → Rows, `SUM([Share²])` → Columns. That sum **is** the HHI. Add a reference
   line at **2,500**, labelled "highly concentrated".
7. Label each bar with the **numbers equivalent**: `10000 / SUM([Share²])`, formatted to one decimal.

### Sheet 4 · "Who produces?" — the treemap

8. `Country` → Detail and Label, `SUM([Production])` → Size, `SUM([Share])` → Colour, `Mineral` →
   Filter (single value, shown).

### Sheet 5 · "System-wide pressure"

9. GSCPI: `Date` (continuous month) → Columns, the vintage column → Rows. Reference line at 0.
   Caption names the vintage.

### Dashboard · "Critical-mineral exposure"

10. *New Dashboard*. Treemap top left, HHI bars top right, restrictions over time bottom left,
    GSCPI bottom right.
11. **Action.** *Dashboard → Actions → Add Action → Filter*. Source: Sheet 4 (treemap) and Sheet 3
    (HHI). Target: Sheet 1. Run on: *Select*. Fields: **Selected fields → Mineral → Mineral**. Because
    the sources are different data sources, map the fields explicitly — and check the mineral
    labels are spelt identically in both.
12. Click *Graphite* in the HHI bars. The restrictions chart should show only graphite. If it shows
    nothing, the labels do not match: fix them, and log it.

---

## 4 · Compare and break — 15 min

1. **Differ.** Put Sheet 1 beside the paper's figure. Your series runs further and your edition is
   newer; the inventory has been revised and renamed. Give one concrete difference and its cause.
2. **Break: "Other countries".** Exclude the `OTH` rows and recompute the HHI. Then treat `OTH` as
   one country. Report both numbers for each mineral. Which mineral's verdict ("highly
   concentrated" or not) changes?
3. **Break: count vs coverage.** Weight each restriction by the restricting country's share of world
   production of that mineral (blend Sheet 1 with the USGS shares on `Mineral` + country ISO code).
   Does the ranking of minerals by "restrictions" change when a restriction by a 70% producer counts
   more than one by a 1% producer?
4. **Extend.** Replace one of the four minerals by one that your **team's firm** depends on (nickel,
   copper, gallium, tungsten…). Transcribe its table and add it to the dashboard.

---

## 5 · The catch — 10 min

**One slide**, three panels:

| Original | Ours | The catch |
|---|---|---|
| The paper's restrictions figure, or its concentration table | Your dashboard | What it does **not** license your firm to conclude |

The model catch, if you need one to beat: *mine-production HHI understates the chokepoint, which is
at the refinery; and a count of restrictions says nothing about how much supply is actually
withheld.* Beat it — say something specific to your firm.

A member drawn at random presents in two minutes.

---

## Hand in

Upload to ZoneCours before leaving: the `.twbx`, your transcription CSV, and the provenance log.
Formative: commented, not marked; counts towards participation.

**The one rule:** the log records at least one place where the data disagreed with the paper — an
edition renamed, a commodity split differently, a world total your rows do not reach.

---

## Into the team dashboard

Before Session 12, re-point Sheets 3–4 at **your firm's** two or three most critical inputs, keep
the action, and add the treemap to your **channel views**. A board member should be able to click a
mineral and see, in one screen, who produces it, who restricts it, and whether the system as a whole
is under pressure.

---

## What loses credit

- An HHI computed with shares that do not sum to 100% within each mineral
- Minerals pooled across different units
- A GSCPI line that mixes vintages, or whose vintage is not named
- A dashboard action that silently filters to nothing
- A catch about the OECD paper rather than about your firm
