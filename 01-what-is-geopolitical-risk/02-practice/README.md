# Session 01 — Practice round 01 (second half, 90 min)

# Rebuild the Geopolitical Risk index

> **[Open the practice slides](https://warint.github.io/geopolitics-geoeconomics/session-01-practice.html)** — or read the source at [`INTE60019A-S01-Practice.qmd`](INTE60019A-S01-Practice.qmd).

> **The target.** Caldara & Iacoviello (2022), Figure 1: the monthly GPR index since 1985, its
> spikes labelled with the events behind them. Then its historical counterpart since 1900.

Teams are not yet formed: today you work **in pairs**. Everyone builds their own workbook.

---

## 1 · Collect — 15 min

If you did the pre-session, `data_gpr_export.xls` is already in `data/raw/`. If not, download it now
from [matteoiacoviello.com/gpr.htm](https://www.matteoiacoviello.com/gpr.htm). Details:
[`../data/README.md`](../data/README.md).

Start your **provenance log** — copy [`templates/provenance-log.csv`](../../templates/provenance-log.csv)
into `data/` and fill one line:

| file | source | url | version / release | accessed | licence | notes |
|---|---|---|---|---|---|---|
| data_gpr_export.xls | Caldara & Iacoviello | matteoiacoviello.com/gpr.htm | *the "last updated" date on the page* | *today* | free, cite AER 2022 | *anything odd* |

---

## 2 · Prepare — 15 min

1. Tableau Desktop → **Connect → Microsoft Excel** → `data_gpr_export.xls`.
2. Drag the data sheet (`Sheet1`) to the canvas. Look at the grid at the bottom. The last two
   columns, `var_name` and `var_label`, are the authors' notes, not data.
3. Check the type icon of `month`. It must be a **date** (calendar). If it is text (`Abc`) or a
   date-time, click the icon and change it to *Date*.
4. Check `GPR`, `GPRT`, `GPRA`, `GPRH` are **numbers** (`#`). Empty cells in early years of the
   recent index are expected: it starts in 1985.
5. Write in your log what Tableau got wrong on its own, if anything.

---

## 3 · Replicate — 30 min

### Sheet 1 · "GPR since 1985"

1. `month` → **Columns**. Right-click the pill → choose the *continuous* **Month** (green pill,
   the second "Month" in the menu — the one showing *May 2015*, not *May*).
2. `GPR` → **Rows**. Keep the aggregation `SUM` — there is one row per month, so the sum is the value.
3. Filter `month` to January 1985 onward.
4. **Analytics** pane → drag **Reference Line** onto the view → *Table* → **Constant 100**, label
   "1985–2019 average = 100".
5. Find the five highest peaks. Right-click each → **Annotate → Point** and write the event:
   Gulf War (1991), 9/11 (2001), Iraq invasion (2003), Paris attacks (2015), Russia invades Ukraine
   (2022) — but **check the months yourself**; do not trust this list.
6. Title the sheet the way the paper would, and put the source in a caption:
   *Source: Caldara & Iacoviello (2022), matteoiacoviello.com, accessed …*

### Sheet 2 · "GPR since 1900"

Duplicate Sheet 1, replace `GPR` with `GPRH`, remove the 1985 filter. Relabel the reference line:
`GPRH` is normalised to its **1900–2019** average = 100, not 1985–2019. Annotate the two World Wars,
Korea and the Cuban missile crisis.

### Sheet 3 · "Threats and acts"

Put `GPRT` and `GPRA` on the same axis: drag `GPRA` onto the `GPRT` axis until the double-ruler
icon appears (**Measure Values**). Colour by **Measure Names**.

---

## 4 · Compare and break — 20 min

Put your Sheet 1 beside Figure 1 of the paper.

1. **Where do they differ?** Your series runs further: the index is updated monthly, and the
   authors also revise it. Are past values exactly the paper's? Write down one difference.
2. **Threats versus acts.** Find one episode where threats rose long before acts did. What would a
   firm watching only *acts* have missed?
3. **Break one decision.** Replace the monthly view by a **yearly average** (change the pill to
   continuous *Year*, aggregation `AVG`). Which spikes disappear? What does that tell you about the
   frequency at which a risk dashboard should run?
4. **Extend.** Add a `GPRC_` country index for a country of your choice (Sheet 4). It is a *percent
   of articles*, not an index to 100: use a dual axis. Is the country index correlated with the
   global one? When does it diverge?

---

## 5 · The catch — 10 min

Build **one slide** (a Tableau dashboard exported as an image is fine) with three panels:

| Original | Ours | The catch |
|---|---|---|
| Figure 1 of the paper | Your Sheet 1 | One sentence: what this figure does **not** license a multinational to conclude |

A pair drawn at random presents in two minutes.

---

## Hand in

Upload to ZoneCours before leaving: your `.twbx` (packaged workbook, *File → Export Packaged*)
and your provenance log. Today's round is **formative**: it is commented on, not marked, and it
counts towards participation.

**The one rule:** your log records at least one place where the data disagreed with the paper.

---

## What loses credit, from Session 02 onwards

- A chart with no source caption
- A provenance log with no version or access date
- "The data matched exactly" — it rarely does; look harder
- A catch that is a limitation of the *paper* rather than of what the *firm* may conclude
