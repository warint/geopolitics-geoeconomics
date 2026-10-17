# Session 11 — Practice round 11 (second half, 90 min)

# Rebuild the debris record, measure the new space race

> **[Open the practice slides](https://warint.github.io/geopolitics-geoeconomics/session-11-practice.html)** — or read the source at [`INTE60019A-S11-Practice.qmd`](INTE60019A-S11-Practice.qmd).

> **The target.** ESA's *Space Environment Report 2026*, Figure 2.1: the **number of objects in
> geocentric orbit by object class**, from 1957 to the end of 2025, with the 2007 Chinese ASAT test,
> the 2009 Iridium–Cosmos collision and the 2021 Russian ASAT test annotated — rebuilt from the
> public catalogue. You add the **concentration** of who puts payloads into orbit, year by year, and
> who operates the active satellites today — and wire the views into **one dashboard with an
> action**.

**The last practice round of the term.** The last twenty minutes of Session 10 reviewed your team
dashboard's skeleton. Most skeletons still lack a space-infrastructure channel and any interaction
between views. Leave today with both: the dependence view you build is designed to be dropped into
your team dashboard, for the satellite services your own firm relies on.

Work in your project teams. Everyone builds the workbook; the team hands in one.

---

## 1 · Collect — 15 min

You arrive with `satcat.csv` (one download per team, pre-session). Use these fifteen minutes to
**check**, not to download again:

1. **The snapshot.** What is the latest `LAUNCH_DATE` in the file? Log it with your download date:
   the catalogue changes every day.
2. **The codes.** Open the [format documentation](https://celestrak.org/satcat/satcat-format.php)
   and the [status codes](https://celestrak.org/satcat/status.php). Which `OBJECT_TYPE` values are
   present? Which `OPS_STATUS_CODE` values count as **active**? What does a blank status mean?
3. **The trap you found before class.** Filter `OBJECT_NAME` = `FENGYUN 1C DEB`. How many rows?
   Which `LAUNCH_DATE`? Write the gap to 11 January 2007 in your log.

Provenance log — one line per file, as always:

| file | source | url | version / release | accessed | licence | notes |
|---|---|---|---|---|---|---|
| satcat.csv | CelesTrak / US Space Force public catalogue | celestrak.org/pub/satcat.csv | *last LAUNCH_DATE; Last-Modified* | *date* | free (usage policy) | *debris dated by parent launch* |
| ESA report | ESA Space Debris Office | sdo.esoc.esa.int/publications/… | *Issue 10.0, 1 May 2026* | *date* | public | *the original: Fig. 2.1, Table 3.1* |
| launch.tsv *(optional)* | J. C. McDowell, GCAT | planet4589.org/space/gcat | *"# Updated" line* | *date* | free | |

---

## 2 · Prepare — 15 min

You build **two data sources from the same file**: one reshaped into events (for the stock of
objects in orbit), one left as it is (for concentration).

### Data source A · "SATCAT events"

1. *Connect → Text file* → `satcat.csv`. Check the types: `LAUNCH_DATE` and `DECAY_DATE` must be
   **dates** (click the type icon above the column if they arrive as strings), `NORAD_CAT_ID` a number.
2. **Data source filter** (top right of the data source page → *Filters → Add*): `ORBIT_CENTER` =
   `EA`. Objects around the Sun or the Moon never decay and would stay "in orbit" for ever.
3. **Pivot the two dates.** Select `LAUNCH_DATE` and `DECAY_DATE` in the grid → right-click →
   **Pivot**. Rename `Pivot Field Names` → `Event` and `Pivot Field Values` → `Event date`. Each
   object now has two rows: its launch and its decay (empty if it is still in space).
4. Calculated fields:

   ```text
   Change  =  IF [Event] = "LAUNCH_DATE" THEN 1 ELSE -1 END
   Year    =  YEAR([Event date])
   ```

5. **Check the grain.** Note the row count before and after the pivot, then exclude the null
   `Event date` rows (decays that have not happened). What is one row now? Write it in the log.

### Data source B · "SATCAT objects"

6. *Data → New Data Source* → the same `satcat.csv`, **not** pivoted. Data source filter
   `OBJECT_TYPE` = `PAY` — a **data source** filter, not a sheet filter (step 3 explains why).
7. Calculated fields:

   ```text
   Launch year  =  YEAR([LAUNCH_DATE])
   Power        =  CASE [OWNER] WHEN "US" THEN "United States"
                                WHEN "PRC" THEN "China"
                                WHEN "CIS" THEN "USSR / Russia"
                                ELSE "Rest of the world" END
   Active       =  [OPS_STATUS_CODE] = "+" OR [OPS_STATUS_CODE] = "P" OR [OPS_STATUS_CODE] = "B"
                   OR [OPS_STATUS_CODE] = "S" OR [OPS_STATUS_CODE] = "X"
   Operator     =  IF STARTSWITH([OBJECT_NAME], "STARLINK") THEN "Starlink (SpaceX)"
                   ELSEIF STARTSWITH([OBJECT_NAME], "ONEWEB") THEN "OneWeb"
                   ELSEIF STARTSWITH([OBJECT_NAME], "KUIPER") THEN "Kuiper (Amazon)"
                   ELSEIF STARTSWITH([OBJECT_NAME], "QIANFAN") THEN "Qianfan"
                   ELSEIF STARTSWITH([OBJECT_NAME], "HULIANWANG") THEN "Guowang"
                   ELSE "Other: " + [OWNER] END
   ```

   `CIS` is CelesTrak's code for the USSR **and** Russia; `OWNER` is a registry-style code, not the
   operator — log both decisions.

---

## 3 · Replicate — 35 min

### Sheet 1 · "Objects in Earth orbit, by type" — the target figure (data source A)

1. `Year` → **Columns**: right-click → *Convert to Dimension*, keep it **continuous** (green).
2. `SUM([Change])` → **Rows**. You see net additions per year — a jagged line.
3. Right-click the pill → *Quick Table Calculation* → **Running Total**. Now you see the **stock**.
4. `OBJECT_TYPE` → **Colour**. *Edit Table Calculation → Compute using → Specific Dimensions* →
   tick `Year` only, so the running total restarts for each type. Mark type **Area** (stacked).
5. Filter `Year` ≤ 2025 to match ESA's end point. **Never filter out early years** with a normal
   filter: it runs before the table calculation and the running total would restart from zero.
   (To hide early years, use a table-calculation filter such as `LOOKUP(MIN([Year]), 0)`.)
6. **Annotate** 2007, 2009 and 2021 (*right-click → Annotate → Point*). Look at the debris band.
   Where are the steps?
7. Title stating the finding; caption with source, snapshot date and "objects dated by launch date".

### Sheet 2 · "Payloads launched per year, by power" (data source B)

8. `Launch year` → Columns (continuous dimension), `CNT([NORAD_CAT_ID])` → Rows, `Power` →
   Colour, mark type **Bar**. Where does the Cold War end, and where does the new race begin?

### Sheet 3 · "How concentrated is the new space race?" — the HHI (data source B)

9. Create:

   ```text
   Owner share  =  {FIXED [Launch year], [OWNER] : COUNT([NORAD_CAT_ID])}
                 / {FIXED [Launch year] : COUNT([NORAD_CAT_ID])}
   HHI piece    =  10000 * [Owner share] / {FIXED [Launch year] : COUNT([NORAD_CAT_ID])}
   ```

   Why the second line: each owner's squared share must be counted **once**, but the owner appears
   on as many rows as it has payloads. Spreading `share × 10,000` over the year's rows means that
   summing an owner's rows gives exactly `share² × 10,000`.
10. `Launch year` → Columns, `SUM([HHI piece])` → Rows, mark type **Line**. That sum **is** the
    HHI. Check: 1957 must give **10,000** (two Soviet payloads). Reference lines at **2,500** and
    **1,800**, labelled.
11. Why the data source filter in step 6: a `FIXED` expression is computed **before** ordinary
    filters. Had you filtered `OBJECT_TYPE` on the sheet, the shares would still include debris and
    rocket bodies. (Adding the filter to **context** also works.)

### Sheet 4 · "Who launched that year?" (data source B)

12. `OWNER` → Rows, `CNT([NORAD_CAT_ID])` → Columns, sorted descending, `Operator` → Colour; a
    *Top 10 by count* filter on `OWNER`. This is the **target** of the action.

### Sheet 5 · "Who operates the active satellites today?" (data source B)

13. Filter `Active` = True and `ORBIT_CENTER` = `EA`. `Operator` → Rows, `CNT([NORAD_CAT_ID])` →
    Columns, sorted; *Quick Table Calculation → Percent of Total*. Caption: "status as of the
    snapshot date; blank status excluded".

### Dashboard · "Space infrastructure exposure"

14. *New Dashboard*. Sheet 1 top left, Sheet 3 top right, Sheet 4 bottom left, Sheet 5 bottom right.
15. **Action 1.** *Dashboard → Actions → Add Action → Filter*. Source: Sheet 1. Target: Sheet 4.
    Run on: *Select*. Clearing the selection: *Show all values*. Filter: **Selected fields** →
    source field `Year` → target data source *SATCAT objects*, target field `Launch year`.
    Because the two sheets use different data sources, map the fields explicitly.
16. **Action 2.** The same, with Sheet 3 as source (same data source as Sheet 4: field
    `Launch year` → `Launch year`).
17. Click 1965 on Sheet 3, then 2025. Sheet 4 should show who launched that year. If it shows
    nothing, the field mapping is wrong: fix it, and log it.

---

## 4 · Compare and break — 15 min

1. **Differ.** Put Sheet 1 beside ESA's Figure 2.1 and Table 3.1 (end of 2025: 44,964 objects, of
   which 16,946 payloads). Give your totals by type and **one** reason for each gap — which
   catalogues ESA adds, what it calls "unidentified", what the public catalogue leaves out.
2. **Break: when does debris appear?** Your debris band does not step up in 2007, 2009 or 2021.
   Re-date the four big events' debris to the date the event happened. In data source A:

   ```text
   Appearance year  =  IF [Event] = "LAUNCH_DATE" AND CONTAINS([OBJECT_NAME], "FENGYUN 1C DEB") THEN 2007
                       ELSEIF [Event] = "LAUNCH_DATE" AND (CONTAINS([OBJECT_NAME], "COSMOS 2251 DEB")
                            OR CONTAINS([OBJECT_NAME], "IRIDIUM 33 DEB")) THEN 2009
                       ELSEIF [Event] = "LAUNCH_DATE" AND CONTAINS([OBJECT_NAME], "COSMOS 1408 DEB") THEN 2021
                       ELSE [Year] END
   ```

   Duplicate Sheet 1 and replace `Year` by `Appearance year`. How big is each step now? What about
   the thousands of other fragments whose event you did not re-date?
3. **Break: flag or firm?** On Sheet 5, replace `Operator` by `OWNER`, and compute the HHI of
   active satellites both ways. Which number describes your firm's **dependence** better?
4. **Extend.** For your **team's firm**, name the satellite services it relies on (GNSS timing,
   connectivity at sea or in remote sites, imagery). Find their operators in the file — `NAVSTAR`
   (GPS), `GSAT0…` (Galileo, coded `ESA`), `BEIDOU`, `[GLONASS-M]` — and add the one that matters
   to Sheet 5. Optional, with GCAT: orbital launch attempts per year (`LaunchCode` starting `O` or
   `D`) by launch-provider state.

---

## 5 · The catch — 10 min

**One slide**, three panels:

| Original | Ours | The catch |
|---|---|---|
| ESA's Figure 2.1 | Your dashboard | What it does **not** license your firm to conclude |

The model catch, if you need one to beat: *a count of objects is not a count of risk — the
fragments able to disable a satellite are mostly too small to catalogue, and the public catalogue
dates debris by its parent's launch, so the ASAT tests vanish from a chart built naively on it;
and concentration by flag hides dependence on one firm.* Beat it — say something specific to your
firm.

A member drawn at random presents in two minutes.

---

## Hand in

Upload to ZoneCours before leaving: the `.twbx`, the provenance log, and the slide. Formative:
commented, not marked; counts towards participation. (The SATCAT is freely available, so the
workbook may also go to Tableau Public — credit CelesTrak in the caption.)

**The one rule:** the log records at least one place where the data disagreed with the paper — a
total that does not reach ESA's, debris dated to the wrong year, an owner code that is not the
operator.

---

## Into the team dashboard

Before Session 12, re-point Sheet 5 at **your firm's** satellite services, keep the action, and
add the dependence view to your **channel views** with a threshold — for example *more than half of
a critical service from one operator → contract a second one*. A board member should be able to
click a year and see who controlled access to orbit then, and see in one screen who the firm
depends on now.

---

## What loses credit

- A running total that restarts because early years were filtered out
- Objects around the Sun or the Moon counted as "in orbit"
- An HHI that is not 10,000 in 1957 — shares computed after a sheet filter, or squared on every row
- `OWNER` presented as the operator, or blank status counted as inactive
- A dashboard action that silently filters to nothing
- A catch about ESA rather than about your firm
