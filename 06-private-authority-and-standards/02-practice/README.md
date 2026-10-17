# Session 06 — Practice round 06 (second half, 90 min)

# The diffusion of ISO 14001 — and the pull of export markets

Slides: [`INTE60019A-S06-Practice.qmd`](INTE60019A-S06-Practice.qmd)

> **The target.** Prakash & Potoski (2006): ISO 14001 spreads across countries, and a country adopts
> more when its **export markets** have adopted more. Two views: the diffusion (a map and small
> multiples over time), and the trade channel (own adoption against export-market adoption).

In your teams. One workbook per team; everyone builds at least one sheet.

---

## 1 · Collect — 10 min

Your three files should already be in `data/raw/` ([`../data/README.md`](../data/README.md)). Finish
the provenance log:

| file | source | url | version / release | accessed | licence | notes |
|---|---|---|---|---|---|---|
| iso_survey_14001.xlsx *or* iso_survey_transcribed.xlsx | ISO / IAF CertSearch | … | *survey edition* | *date* | *free / account* | *full tables or transcription; coverage changes?* |
| imf_imts_exports.csv | IMF | data.imf.org — IMTS | *download date* | *date* | free | *exports FOB, US$; partner codes used* |
| wdi_gdp.csv | World Bank | api.worldbank.org/… | *last updated* | *date* | CC BY 4.0 | |

---

## 2 · Prepare — 20 min

1. **ISO table.** If years are columns, **pivot** them (select the year columns → right-click →
   *Pivot*), rename to `Year` and `Certificates`. Add or check `iso3`. Keep 14001 and 9001 as two
   columns, or as a `Standard` dimension — your choice, logged.
2. **WDI GDP.** Pivot the year columns too. Keep `Country Code` (it is ISO3) and the value. From the
   `Metadata_Country_…` file in the same zip, bring in **Region**, and drop the aggregates (World,
   regions, income groups): they are the rows with an empty `Region`.
3. **Join** ISO to GDP on `iso3` **and** `Year` (both join clauses). Check the row count.
4. Calculated field:

   ```text
   [ISO 14001 per $bn GDP] = [Certificates 14001] / ([GDP current US$] / 1e9)
   ```

5. Log: which countries did not match, and why.

---

## 3 · Replicate — 30 min

### Sheet 1 · "ISO 14001 spread" — a map

1. `iso3` → *Geographic Role → Country/Region*; double-click it. Check the **unknown** indicator,
   bottom right; fix with *Map → Edit Locations*.
2. Mark type **Map**; `[ISO 14001 per $bn GDP]` → Colour, **sequential** palette. Consider a log-like
   scale: the distribution is very skewed (try *Edit Colors → Stepped* with 5 steps).
3. `Year` → **Pages**. Press play. Title it with what you see.

### Sheet 2 · "Diffusion by region" — small multiples

`Year` → Columns (continuous), `Region` → Rows, `MEDIAN([ISO 14001 per $bn GDP])` → Rows. One small
line per region. Which region adopted first? Which caught up?

### Sheet 3 · "The pull of export markets" — the trade channel

This is the core of Prakash and Potoski: does a country's adoption track its **export markets'**
adoption?

1. New data source. Start from `imf_imts_exports.csv` (reporter × partner × year × exports). In the
   IMF layout reporter and partner are `COUNTRY` and `COUNTERPART_COUNTRY`, in ISO3 codes (rename
   them `Reporter iso3` and `Partner iso3`; `TIME_PERIOD` → `Year`, `OBS_VALUE` → `Exports`). Drop
   aggregate partners (codes starting with `G` or `TX`). If your download shows names instead, build
   a concordance. Kosovo is `KOS` at the IMF but `XKX` at the World Bank.
2. **Join** the ISO + GDP table to it **twice** (Tableau lets you add the same table again; rename
   the copies):
   - as **Partner**: `Partner iso3 = iso3` and `Year = Year`
   - as **Reporter**: `Reporter iso3 = iso3` and `Year = Year`
3. Calculated fields:

   ```text
   [Weighted partner adoption]  = [Exports] * [Partner ISO 14001 per $bn GDP]

   [Export-market adoption]     = SUM([Weighted partner adoption]) / SUM([Exports])

   [Own adoption]               = { FIXED [Reporter iso3], [Year] :
                                    AVG([Reporter ISO 14001 per $bn GDP]) }
   ```

   The `FIXED` matters: the reporter's own value is repeated on every partner row, so it must not be
   summed.
4. Scatter: `[Export-market adoption]` → Columns, `AVG([Own adoption])` → Rows, `Reporter iso3` →
   Detail, `Year` → Colour (or filter to one year). **Log scales** on both axes (right-click axis →
   *Edit Axis → Logarithmic*). Add a trend line (*Analytics → Trend Line → Linear*) — read it as a
   description, not a test: Session 09 returns to what its R² means.

---

## 4 · Compare and break — 20 min

1. **Differ.** Your scatter versus the paper's argument. The paper estimates a panel with controls;
   you have drawn a cloud. What can your cloud show, and what can it not?
2. **The placebo.** Rebuild Sheet 3 with **ISO 9001** — the quality standard, demanded by buyers
   everywhere, with no environmental content. If the export-market pull is just as strong, what does
   that say about *why* firms certify to 14001?
3. **Break the weighting.** Replace the export-weighted average with an **unweighted** average of
   partners (`AVG` instead of the weighted ratio). Does the relationship survive? Why should weighting
   matter for the California-effect argument?
4. **Break the normalisation.** Raw counts instead of per $bn GDP on Sheet 1. Which countries jump to
   the top — and why is that misleading?

---

## 5 · The catch — 10 min

| Original | Ours | The catch |
|---|---|---|
| Prakash and Potoski's finding | Your Sheet 3 (and Sheet 1) | What it does **not** license a multinational to conclude — for instance that a certified supplier is environmentally better, or that adoption *caused* export success |

A member drawn at random presents in two minutes.

---

## Hand in

`.twbx` + provenance log on ZoneCours. Formative; counts towards participation.

**The one rule:** your log records at least one place where the data disagreed with the paper.

**Team project.** Which private standards do your firm's buyers or home market require? Which of its
key countries are below the median adoption of its export markets? Note it for the dashboard.
