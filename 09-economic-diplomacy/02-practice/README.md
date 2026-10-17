# Session 09 — Practice round 09 (second half, 90 min)

# Do embassies follow, or lead, exports?

Slides: [`INTE60019A-S09-Practice.qmd`](INTE60019A-S09-Practice.qmd)

> **The target.** Rose (2007)'s central relationship: for each exporter–partner pair, **exports**
> against the **number of diplomatic posts** the exporter keeps in the partner — on log scales, with
> a trend line — rebuilt with the Lowy Global Diplomacy Index (2023 data) and IMF trade.

Work in your project teams. Everyone builds their own workbook; the team hands in one slide.

---

## 1 · Collect — 15 min

In `data/raw/` (see [`../data/README.md`](../data/README.md)):

- `DataDownload.xlsx` — Lowy Global Diplomacy Index;
- IMF IMTS — **exports of goods, FOB, US$, 2023**, for Canada and at least four other Lowy countries
  × all partners;
- WDI `NY.GDP.MKTP.CD` — GDP, current US$.

Provenance log — one line per file, including **which side** of the trade flow you used (exporter-
reported exports) and the IMF indicator name exactly as shown.

---

## 2 · Prepare — 25 min

This is the hard part today. Take your time.

1. **Lowy.** Connect to `DataDownload.xlsx`, sheet **2023**. The columns for sending country, host
   country and post type are `COUNTRY`, `POST COUNTRY` and `TYPE OF POST`. Filter out posts that are
   not bilateral: `TYPE OF POST` = `Permanent Mission` (missions to the UN, EU, OECD…). Look at what
   `Other` holds (representative and trade offices, e.g. in Taipei) and log your choice.
2. **IMF.** Add the IMF file as a **second table** on the canvas. Keep only the five exporters and
   the year 2023; drop aggregate partners ("World", regional totals — codes starting with `G` or
   `TX`). Rename `OBS_VALUE` → `Exports`.
3. **Concordance.** Lowy has country names only; the IMF file has ISO3 codes (`COUNTRY`,
   `COUNTERPART_COUNTRY`). Make a small sheet `name → ISO3` for the Lowy `COUNTRY` and
   `POST COUNTRY` names (watch the typos listed in the data README) and add ISO3 to Lowy.
4. **Relate, don't join.** Drag the IMF table first, then the Lowy table, and create a
   **relationship** on `exporter ISO3 = sending ISO3` **and** `partner ISO3 = host ISO3`.
   A relationship keeps the export totals at their own grain; a plain join would repeat each
   export value once per post and inflate it.
5. **Build the zeros.** Calculated field `Posts`:
   ```
   ZN(COUNT([POST CITY]))
   ```
   (`POST CITY` is never empty in the 2023 sheet). Partners with exports but no post now get 0.
6. **Make logging possible.** Calculated field `Posts + 1` = `[Posts] + 1`. Write this decision in the
   log: it is the same compromise most gravity papers make, and it has consequences.
7. **Exports per partner GDP.** Add WDI GDP (relationship on partner ISO3, year 2023) and create
   `Exports / partner GDP (‰)` = `SUM([Exports]) / SUM([GDP]) * 1000`.

---

## 3 · Replicate — 20 min

### Sheet 1 · "More posts, more exports"

1. `Posts + 1` → **Columns** (as a measure; aggregation `SUM` at the dyad level).
2. `Exports` → **Rows**.
3. Exporter ISO3 **and** partner ISO3 → **Detail** — one mark per pair.
4. Exporter → **Colour**.
5. Right-click each axis → *Edit Axis* → **Logarithmic**.
6. *Analytics* → **Trend Line** → *Linear*. Right-click the line → **Describe Trend Model**. Note the
   slope, R² and p-value (one line per exporter if colour splits them — try both ways).
7. Title states the finding; caption cites Lowy (2024 edition, 2023 data) and IMF IMTS, with access
   dates.

---

## 4 · Compare and break — 20 min

1. **Differ.** Rose used an earlier period and a different set of exporters. Is your slope steeper
   or flatter than the relationship he reports? Name one reason.
2. **Break: size.** Replace `Exports` by `Exports / partner GDP (‰)`. What happens to the slope and
   the R²? What did the raw chart owe to the sheer size of partners?
3. **Break: type of post.** Filter `TYPE OF POST` to **`Embassy / High Commission`** only, then to
   **`Consulate / Consulate-General`** only. Which
   carries the relationship? Does that match Rose?
4. **Break: the zeros.** Exclude partners with `Posts = 0`. How much does the trend line move? Why
   should a careful analyst never drop them silently?
5. **Extend — reverse causality** (fast teams). Add the Lowy **2017** sheet and IMF exports for
   2017. For each pair, compute the change in posts and the growth of exports 2017→2023. Do pairs
   that **gained** posts show faster export growth — or did posts open where exports had already
   grown? What would you need to tell the two apart?

---

## 5 · The catch — 10 min

| Original | Ours | The catch |
|---|---|---|
| Rose's posts–exports relationship | Your Sheet 1 | One sentence: what this trend line does **not** license a multinational — or a foreign ministry — to conclude |

A member drawn at random presents in two minutes.

---

## Hand in

On ZoneCours before leaving: `.twbx` and provenance log, including your concordance fixes.
Formative; counts towards participation.

**The one rule:** your log records at least one place where the data disagreed with the paper.

---

## What loses credit

- A **join** that inflated exports, unnoticed (check one pair's total against the IMF file)
- Zeros dropped without saying so
- "R² = 0.6, so embassies explain 60% of exports" — they explain nothing; they *co-vary*
- Unmatched countries silently missing from the chart
