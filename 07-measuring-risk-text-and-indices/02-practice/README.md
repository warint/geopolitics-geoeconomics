# Session 07 — Practice round 07 (second half, 90 min)

# Three measures: firm-level risk, your coded index, and a composite with moving weights

Slides: [`INTE60019A-S07-Practice.qmd`](INTE60019A-S07-Practice.qmd)

> **The targets.** (a) Hassan et al. (2019): **average firm-level political risk over time**, against
> the EPU index. (b) **Your own coded index** — 40 headlines, two coders, a kappa. (c) A **composite
> exposure index** for your team's firm, with weights the board can move — your team's draft.

Today has three short builds instead of one long one. Keep to the clock.

| Part | Minutes | The five steps, compressed |
|---|---|---|
| **(a) Firm-level risk vs EPU** | 30 | collect · prepare · replicate · compare |
| **(b) Your coded index** | 20 | agreement · adjudicate · count |
| **(c) A composite with moving weights** | 30 | select · normalise · weight · test |
| **The catch** | 10 | one slide, three panels |

Data: [`../data/README.md`](../data/README.md). Provenance log as always — one line per file, including
your own `coding_sheet.xlsx` ("produced by the team, protocol of Session 07").

---

## (a) Firm-level political risk against EPU — 30 min

### Prepare — choose a route

The firm file is **firm × quarter**; EPU is **monthly**. Both must reach a common **quarter** grain.

The quarter identifier in the firm file is a string such as `2010q1` in the vintages we have seen —
**check yours**. Convert it to a date:

```text
[Quarter date] = MAKEDATE( INT(LEFT([date], 4)),
                           (INT(RIGHT([date], 1)) - 1) * 3 + 1,
                           1 )
```

And for EPU (check the names of its year and month columns):

```text
[Quarter date] = DATETRUNC('quarter', MAKEDATE([Year], [Month], 1))
```

**Route 1 · Tableau Prep** (if your licence includes it)

1. *Input* `firmquarter_2022q1.csv` → *Clean* step: add `[Quarter date]` → *Aggregate* step: group by
   `[Quarter date]`; `AVG(PRisk)`, `COUNTD` of the firm identifier.
2. *Input* the EPU workbook → *Clean*: add `[Quarter date]`, drop rows with no value →
   *Aggregate*: group by `[Quarter date]`; `AVG` of the global EPU column.
3. *Join* the two on `[Quarter date]` (inner) → *Output* as `.hyper`. Open it in Tableau Desktop.
4. Every step is a visible, saved decision: export the flow (`.tfl`) with your hand-in.

**Route 2 · the data source pane** (Tableau Desktop or Tableau Public edition)

1. Connect to both files. Drag the firm file to the canvas, then the EPU sheet next to it.
2. In the relationship dialog, choose **Create Relationship Calculation** on each side and enter the
   two `[Quarter date]` formulas above.
3. Relationships aggregate each table at its own level: `AVG(PRisk)` is averaged over firms,
   `AVG(GEPU)` over the months of the quarter — exactly what you want.

### Replicate — Sheet "Firm-level political risk and EPU"

1. `[Quarter date]` → Columns as continuous **Quarter**.
2. `AVG(PRisk)` → Rows; the EPU measure → Rows; **dual axis**, *not* synchronised (different units).
3. Annotate three peaks; check what happened in those quarters.
4. Title with the finding; caption with both sources, vintages and access dates.

### Compare

- Do the two series move together? Where do they part company — and which one would you trust for a
  firm, and which for a country?
- Add `COUNTD` of firms as a third view. Does the number of firms change over the period? Why does
  that matter for an average?
- If the file has a headquarters-country column, filter to non-US firms. How many are left?

---

## (b) Your coded index — 20 min

Connect to `coded/coding_sheet.xlsx`.

1. **The agreement matrix.** `coder_A` → Rows, `coder_B` → Columns, `CNT(id)` → Text and Colour:
   a **highlight table**. *Analysis → Totals → Show Row and Column Grand Totals.*
2. **Percent agreement** in Tableau:

   ```text
   [Agree] = IF [coder_A] = [coder_B] THEN 1 ELSE 0 END      →   AVG([Agree]) = p_o
   ```

3. **Kappa, by hand.** From the grand totals, compute $p_e = \sum_k (n_{A,k}/N)(n_{B,k}/N)$ and
   $\kappa = (p_o - p_e)/(1 - p_e)$. Write both on your slide. If categories are sparse, also compute
   kappa on three collapsed categories (0 / threat / act) — and say which you report.
4. **Adjudicate.** The adjudicator reads every disagreement and fills `final`, with a one-line reason.
   List the **protocol changes** you would make.
5. **The index.** From `final`: the share of headlines in each category, and the share coded
   geopolitical (≠ 0) by month. Mark `econ` comments separately: how many headlines about sanctions
   or export controls did the GPR categories force into 0?

---

## (c) A composite exposure index with moving weights — 30 min

### Select

Start from a **spine**: a sheet listing your firm's key countries plus comparators — **8 to 12
countries**, with `iso3`. Every input is **left-joined** to it, so missing values are visible rather
than silently dropped.

| Indicator | Source | Direction | Preparation |
|---|---|---|---|
| Country GPR | `GPRC_xxx` columns | higher = riskier | pivot the `GPRC_` columns; extract the code with `RIGHT([Pivot Field Names], 3)`; average the last 12 months |
| Country EPU | `All_Country_Data.xlsx` | higher = riskier | pivot country columns; add `iso3` (the columns are country names — check); average the last 12 months |
| Political stability | WGI 2025 | **higher = safer** | latest year |
| Distance in UN voting from the firm's home country | Session 04 ideal points | higher = riskier | `ABS([Ideal point] - [Home ideal point])`, latest year |

**Each input must be one row per country before it is joined to the spine** — otherwise the min and
max below are taken over months, not countries. Reduce each input first: an *Aggregate* step in
Tableau Prep, or — in Desktop — a small sheet (country × the averaged value) exported with
*Worksheet → Export → Crosstab* into a derived file in `data/derived/`, logged as such. Raw files are
never edited.

### Normalise

Min–max across the spine countries, with a `FIXED` expression over the whole table:

```text
[GPR n]   = ([GPR]   - {MIN([GPR])})   / ({MAX([GPR])}   - {MIN([GPR])})
[WGI n]   = ({MAX([WGI])} - [WGI])     / ({MAX([WGI])}   - {MIN([WGI])})      // inverted
```

…and the same for EPU and voting distance.

### Weight

Create four **parameters**, `w GPR`, `w EPU`, `w WGI`, `w Vote` — integers 0 to 5, default 1 — and
show their controls. Missing values must not count as zero risk, so reweight over the indicators
that exist:

```text
[Composite] =
  ( IF NOT ISNULL([GPR n])  THEN [w GPR]  * [GPR n]  ELSE 0 END
  + IF NOT ISNULL([EPU n])  THEN [w EPU]  * [EPU n]  ELSE 0 END
  + IF NOT ISNULL([WGI n])  THEN [w WGI]  * [WGI n]  ELSE 0 END
  + IF NOT ISNULL([Vote n]) THEN [w Vote] * [Vote n] ELSE 0 END )
  /
  ( IF NOT ISNULL([GPR n])  THEN [w GPR]  ELSE 0 END
  + IF NOT ISNULL([EPU n])  THEN [w EPU]  ELSE 0 END
  + IF NOT ISNULL([WGI n])  THEN [w WGI]  ELSE 0 END
  + IF NOT ISNULL([Vote n]) THEN [w Vote] ELSE 0 END )
```

That is a **decision**, not a fix: write it in your log ("composite renormalised over available
indicators").

Sheet: countries on Rows, sorted by `SUM([Composite])`, bars, with `RANK(SUM([Composite]))` as a
label.

### Test

Record each country's rank under **equal weights**, then under each indicator **alone** (weight 1,
others 0). In a small table: how many countries change rank by more than two places? Which country
is most sensitive to the weights — and why?

---

## The catch — 10 min

One slide, three panels:

| (a) | (b) | (c) |
|---|---|---|
| PRisk vs EPU: what an average of US-listed firms does **not** tell your firm | Your kappa and the protocol change you would make | Your composite's ranking — and the weight that would overturn it |

A member drawn at random presents in two minutes.

---

## Hand in

`.twbx` (+ `.tfl` if you used Prep), `coding_sheet.xlsx` with `final` filled, and the provenance log,
on ZoneCours. Formative; counts towards participation.

**The one rule:** your log records at least one place where the data disagreed with the paper — for
(a), or for the GPR categories meeting your headlines in (b).

**Team project milestone.** Part (c) is your **draft composite index**. Bring it, revised, to the
dashboard review in Session 10.
