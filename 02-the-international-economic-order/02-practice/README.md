# Session 02 — Practice round 02 (second half, 90 min)

# Rebuild the Great Convergence

Slides: [`INTE60019A-S02-Practice.qmd`](INTE60019A-S02-Practice.qmd)

> **The target.** Baldwin (2016): the **G7 share of world GDP**, rising for a century and falling
> sharply after about 1990. You rebuild it from 1970 with World Bank data, then ask what changes
> when the dollars change.

---

## 0 · Form your team — 10 min

Teams of three or four, for the rest of the term. Agree on **one multinational** from your shortlists
and register it on ZoneCours (first come, first served). Write the team name and firm at the top
of your provenance log.

---

## 1 · Collect — 10 min

If you did the pre-session, your DataBank extract is in `data/raw/`. If not, build it now —
[`../data/README.md`](../data/README.md). One extract per team is enough; everyone builds their own
workbook from it.

Copy [`templates/provenance-log.csv`](../../templates/provenance-log.csv) into `data/` and fill one line
per file. For WDI, the **version** is the "Last Updated" date DataBank shows for the database.

---

## 2 · Prepare — 20 min

1. **Connect → Microsoft Excel** → your extract. Drag the data sheet to the canvas.
2. If there are notes rows at the bottom ("Data from database…", "Last Updated…"), tick **Use Data
   Interpreter**, or filter them out later. Write which you did.
3. **Pivot the years.** Click the first year column, shift-click the last → right-click →
   **Pivot**. Two new columns appear.
4. Rename `Pivot Field Names` → `Year`, `Pivot Field Values` → `Value`.
5. `Year` is text like `1990 [YR1990]`. Create a calculated field from the data source pane:
   `Year (n)` = `INT(LEFT([Year], 4))`. (If your extract has plain `1990`, just change the type to
   *Number (whole)*.)
6. `Value` is text — DataBank writes missing data as `..`. Change its type to **Number (decimal)**;
   the dots become nulls. Check the null count: is it plausible?
7. Look at `Country Code` and `Series Code` (in the Route B CSV the second is `Indicator Code`, the
   years are plain `1990`, and missing values are blank). **From now on you filter on codes, never
   on names.**

---

## 3 · Replicate — 25 min

### Sheet 1 · "The G7 share of world GDP"

1. Filters: `Series Code` = `NY.GDP.MKTP.CD` only.
2. Create two calculated fields:

   ```text
   G7 GDP     = IF [Country Code] IN ("CAN","FRA","DEU","ITA","JPN","GBR","USA") THEN [Value] END
   World GDP  = IF [Country Code] = "WLD" THEN [Value] END
   ```

3. And the share:

   ```text
   G7 share   = SUM([G7 GDP]) / SUM([World GDP])
   ```

   Format it as a percentage (right-click → *Default Properties → Number Format*).
4. `Year (n)` → Columns as a **continuous dimension** (green); `G7 share` → Rows.
5. Annotate the peak year and the latest year with their values. Title the sheet with the finding,
   not the variable. Caption: *World Bank, WDI, NY.GDP.MKTP.CD, last updated …, accessed …*.

### Sheet 2 · "Who gained?" — a stacked area of world shares

1. Two more calculated fields:

   ```text
   I6 GDP              = IF [Country Code] IN ("CHN","KOR","IND","POL","IDN","THA") THEN [Value] END
   Rest of world GDP   = SUM([World GDP]) - SUM([G7 GDP]) - SUM([I6 GDP])
   ```

2. `Year (n)` → Columns. Drag `G7 GDP`, `I6 GDP` and `Rest of world GDP` onto Rows as **Measure
   Values** (drop the second and third onto the first axis).
3. **Marks → Area**. `Measure Names` → Colour.
4. Right-click `Measure Values` → **Quick Table Calculation → Percent of Total**. Then **Edit Table
   Calculation → Compute Using → Measure Names**, so that the three shares sum to 100% **within each
   year** — not across years. Check one year by hand against Sheet 1.

---

## 4 · Compare and break — 15 min

1. **Compare.** Put Sheet 1 beside Baldwin's figure. Where does the curve peak in yours? How far
   has it fallen by Baldwin's last year, and by the latest year? Write down one difference and its
   most likely cause (dollars, years, data revision).
2. **Missing data.** Which I6 members have no GDP value in the 1970s or 1980s? What does that do to
   the I6 and "rest of world" areas in those years? This is your "the data disagreed" entry.
3. **Break — change the dollars.** Duplicate Sheet 1 and switch the filter to `NY.GDP.MKTP.PP.CD`.
   The PPP series starts in 1990. How much smaller is the G7 at PPP? Which board decision would you
   use each line for?
4. **Extend — slowbalisation.** New sheet: `NE.TRD.GNFS.ZS` for `WLD` — world trade in % of GDP
   (an index, so check the aggregation: there is one value per year; `AVG` or `SUM` give the same
   only because you filtered to one country — say so). Annotate 2008. Is the line after 2008 a retreat?

---

## 5 · The catch — 10 min

One slide (a dashboard exported as an image):

| Original | Ours | The catch |
|---|---|---|
| Baldwin's G7 share figure | Your Sheet 1, plus the PPP line | One sentence: what this figure does **not** license your team's multinational to conclude |

A member drawn at random presents in two minutes.

---

## Hand in

On ZoneCours before leaving, one per team: the `.twbx` (*File → Export Packaged Workbook*), the
provenance log, and the slide. Formative: commented, not marked; counts towards participation.

**The one rule:** your log records at least one place where the data disagreed with the book.

---

## What loses credit

- Filtering on country *names* ("Korea, Rep." will bite you in Session 04)
- A percent of total that sums to 100% across years instead of within each year
- A share chart in current dollars with no mention of exchange rates
- A catch about Baldwin's book rather than about what your firm may conclude
