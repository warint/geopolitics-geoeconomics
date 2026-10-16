# Session 05 — Practice round 05 (second half, 90 min)

# The price of a seat, in event time

Slides: [`INTE60019A-S05-Practice.qmd`](INTE60019A-S05-Practice.qmd)

> **The target.** Kuziemko & Werker (2006): US aid to developing countries **in the years around a
> Security Council term** — flat before, higher during the two term years, back down after.

In your teams. One workbook per team; everyone builds at least one sheet.

---

## 1 · Collect — 15 min

You should arrive with route A or route B files in `data/raw/` ([`../data/README.md`](../data/README.md)).
Finish what is missing, and fill the provenance log — one line per file.

| file | source | url | version / release | accessed | licence | notes |
|---|---|---|---|---|---|---|
| greenbook_country_summary.csv | US State Dept (Greenbook) | foreignassistance.gov/data *or the mirror* | *release / "frozen 2024-12-19"* | *today* | free | *fiscal years; obligations; constant $?* |
| unsc_elected_members.xlsx | United Nations | main.un.org/securitycouncil/… | *page date* | *today* | free | *your transcription; name changes handled* |

**Route A teams** also need a **term table**. Open the replication file, filter on Security Council
membership = 1, show country × year as a text table, export it (*Worksheet → Export → Crosstab to
Excel*), and mark the first year of each two-year run as `term_start`. Ten minutes; it gives you the
same term table as route B.

---

## 2 · Prepare — 20 min

1. **Connect** to the aid file and to `unsc_elected_members.xlsx`.
2. Drag the aid table to the canvas, then **double-click it** to open the physical layer, and drag the
   term table next to it: **inner join** on `Iso3` (or on country name only if you have checked every
   match — see the trap list in [`TABLEAU-TOOLKIT.md`](../../TABLEAU-TOOLKIT.md)).
   > Why a join, not a relationship? The next step is a row-level calculation that uses `Year` from
   > one table and `Term start` from the other. Relationships do not allow that.
3. Check the row count before and after the join and write both in your log. The join should
   multiply rows: each country-year now appears once per term of that country.
4. Keep only aid **recipients** (drop donors and regional aggregates such as "World", "Africa
   Regional"), and check that aid is in **constant** dollars. If it is not, say so in the log — the
   ratio to baseline below limits the damage, but does not remove it.

---

## 3 · Replicate — 25 min

### Calculated fields

```text
[Event time]               = [Year] - [Term start]

[Baseline aid]             = { FIXED [Iso3], [Term start] :
                               AVG( IF [Event time] >= -3 AND [Event time] <= -1
                                    THEN [Aid] END ) }

[Aid relative to baseline] = [Aid] / [Baseline aid]      // row level: one value per country-year-term
```

Route A teams: if aid is in logs in the file, use `[Log aid] - [Baseline log aid]` instead of a ratio.

### Sheet 1 · "Aid in event time"

1. Filter `[Event time]` to **−3 … +3** (make it a dimension, discrete).
2. `[Event time]` → Columns; `[Aid relative to baseline]` → Rows, then change its aggregation to
   **AVG** (right-click the pill → *Measure → Average*). Because the ratio is computed row by row —
   one row per country-year-term — the average at each event year is the average **across terms**.
3. Mark type **Line**, then add **Circle** marks on a dual axis so each year is visible.
4. **Analytics → Reference Band** from 0 to 1 on `[Event time]`, shaded, labelled "On the Council".
5. Constant **reference line at 1.0**, labelled "Pre-term baseline".
6. Title it with the finding; caption with both sources, versions and access dates.

### Sheet 2 · "How many terms?"

`[Event time]` → Columns, `COUNTD([Iso3])` → Rows. The number of terms behind each point. Is the
sample balanced across event years? If not, why?

---

## 4 · Compare and break — 20 min

1. **Differ.** Put your Sheet 1 beside the paper's event-time evidence. Same shape? Same size? Write
   one difference and its most likely cause (release of the aid data, years covered, the sample of
   countries, constant vs current dollars, levels vs logs).
2. **Break one decision.** Replace the **mean** across terms by the **median** (a quick change of
   aggregation). Does the term-year bump survive? What does that tell you about whether a few large
   cases drive it?
3. **Break another.** Restrict to terms starting **after 1990**. Does the pattern survive the end of the
   Cold War?
4. **Extend — salience.** The paper finds the effect is larger when the Council matters more. Build a
   crude proxy: tag the years 1990–91 (Gulf War), 2002–03 (Iraq) as *high salience* with a calculated
   field, and colour Sheet 1 by it. What do you see — and why is two episodes far too few to conclude?

---

## 5 · The catch — 10 min

| Original | Ours | The catch |
|---|---|---|
| The paper's event-time evidence | Your Sheet 1 | What it does **not** license a multinational to conclude — for instance about how durable a UN sanctions resolution is, or what a host government on the Council will do |

A member drawn at random presents in two minutes.

---

## Hand in

Upload to ZoneCours before leaving: the `.twbx` and the provenance log. Formative: commented, not
marked; counts towards participation.

**The one rule:** your log records at least one place where the data disagreed with the paper.

**Team project.** Is any of your firm's five key countries — or its home country — on the Council
now, or about to be? Add it to your footprint notes.
