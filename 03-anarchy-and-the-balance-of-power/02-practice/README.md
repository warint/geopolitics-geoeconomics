# Session 03 — Practice round 03 (second half, 90 min)

# Rebuild the distribution of power

Slides: [`INTE60019A-S03-Practice.qmd`](INTE60019A-S03-Practice.qmd)

> **The target.** The shares of world material capabilities (CINC) of the major powers, 1816–2022 —
> the picture behind Mearsheimer's and Allison's argument — and the year China passes the United
> States. Then: the same transition measured two other ways, dated two other years.

Work in your team. Everyone builds their own workbook; the team hands in one.

---

## 1 · Collect — 15 min

NMC v7.0 and the SIPRI workbook should already be in `data/raw/`; your Session 02 WDI extract
too. If not: [`../data/README.md`](../data/README.md).

Provenance log: three lines — NMC (version 7.0, and the codebook's date), SIPRI (the file name gives
the release), WDI (reused; same version as Session 02).

---

## 2 · Prepare — 20 min

### NMC

1. **Connect → Text file** → `NMC-70-abridged.csv` (from `NMC-v7-abridged.zip`, inside
   `NMCv7.zip`). Drag it to the canvas.
2. Check the columns against the **codebook**. In v7.0 they are unchanged from v6.0: `stateabb`
   (three letters), `ccode` (number), `year`, the six components `milex`, `milper`, `irst`, `pec`,
   `tpop`, `upop`, then `cinc` and `version`. Missing component values are coded **`-9`**: before you
   use any component, exclude them (a filter `>= 0`), or every sum is wrong.
3. `year` should be a **number (whole)**, not a date: keep it that way for now.
4. Sanity check before you build anything: new sheet, `year` → Columns (continuous), `SUM(cinc)` →
   Rows, no filter. Every year should sum to **about 1** — in v7.0, between 1.000 and about 1.075.
   Which years are furthest from 1, and why? (The codebook's CINC section explains it: the average
   is taken over the components a state *has*.)

### SIPRI

1. **Connect → Microsoft Excel** → the SIPRI workbook. Use the **`Constant (2024) US$`** sheet
   (US$ millions, constant 2024 prices).
2. Tick **Use Data Interpreter**: the sheet has five rows of notes above the header (`Country`, an
   unnamed column, `Notes`, `1949` … `2025`). Region headings (`Africa`, `North Africa`, …) remain
   as rows with no values: filter them out.
3. **Pivot** the year columns (as in Session 02). Rename to `Year` and `Milex`. Make `Year` a whole
   number with the same name as NMC's year field — it will be the link.
4. `Milex` arrives as text: SIPRI writes `...` for unavailable data and `xxx` for a country that
   did not exist (the notes at the top of the sheet; the `Footnotes` sheet explains the † § ¶
   marks in `Notes`). Change to **Number (decimal)** and check what became null.
5. SIPRI identifies countries by **name**, not code. Write down the exact strings for China, the
   United States and Russia. This is a provenance-log entry.

---

## 3 · Replicate — 25 min

### Sheet 1 · "Shares of world capabilities, 1816–2022"

1. `year` → Columns (continuous); `SUM(cinc)` → Rows.
2. `stateabb` → Colour. Filter to the major powers: `USA`, `UKG`, `FRN`, `GMY`, `RUS`, `JPN`,
   `CHN`, `ITA` — **check each code in the COW state list** (`COW-country-codes.csv`; see
   [`../data/README.md`](../data/README.md)). Russia/USSR is one continuous series (`RUS`).
   Germany is not: `GMY` stops in 1945 and returns in 1991, with `GFR` and `GDR` in between.
   `JPN` also has a gap (1946–1951). Look for them, and decide what your line does there.
3. Highlight the US and China (strong colours), grey the rest.
4. Annotate 1945, 1991, and the year China passes the US.
5. Title with the finding; caption: *Correlates of War, NMC v7.0 (Singer, Bremer & Stuckey 1972),
   accessed …*.

### Sheet 2 · "How close is the challenger?"

1. **Create → Parameter** `Challenger`: data type *String*, *List*, **Add values from** `stateabb`.
   Default `CHN`.
2. Calculated fields:

   ```text
   Challenger CINC = IF [stateabb] = [Challenger] THEN [cinc] END
   US CINC         = IF [stateabb] = "USA" THEN [cinc] END
   Power ratio     = SUM([Challenger CINC]) / SUM([US CINC])
   ```

3. `year` → Columns; `Power ratio` → Rows. Right-click the parameter → **Show Parameter**.
4. **Analytics → Reference Line**: constant **1** ("parity") and constant **0.8** ("power transition
   zone", Organski & Kugler).
5. Switch the parameter to `GMY`, `JPN` and `RUS`. When did each enter the transition zone against
   the US — or against the UK, if you also make the leader a parameter?

---

## 4 · Compare and break — 20 min

1. **Compare.** Put Sheet 1 beside the readings' claims. In which year does China's CINC first exceed
   the US's in your data? Does that date surprise you, given what you read?
2. **Break — change the measure of power.** Build two more ratios, China ÷ US:
   - **military expenditure** from SIPRI (constant dollars), and
   - **GDP** from your WDI extract (current US$ and PPP).

   Put them on one sheet with the CINC ratio by **blending** on the year: on a sheet that uses NMC,
   drag a SIPRI field onto the view; check that the link icon is active on the year field (*Data →
   Edit Blend Relationships* if Tableau did not find it). **Blending links fields only by name and
   type**: if the year is `year` in NMC, `Year` in SIPRI and `Year (n)` in your Session 02 WDI
   extract, rename them to the same name (right-click → *Rename*) and make all three whole numbers
   before you blend, or use *Edit Blend Relationships → Custom* to pair them by hand. Use a **dual axis** (right-click the
   second axis → *Dual Axis* → *Synchronize Axis*) so both ratios share one scale, with the parity
   line at 1.
3. **Read it.** Three measures, three transition dates (or no transition yet). Which date belongs in a
   board presentation, and for which decision?
4. **Extend.** Use the NMC components: which of the six drives China's CINC? Build one component's
   share (e.g. iron and steel) with a percent-of-total table calculation computed across states,
   restarting every year.

---

## 5 · The catch — 10 min

One slide:

| Original | Ours | The catch |
|---|---|---|
| The distribution of power as the readings describe it | Sheet 1, and the three-measure ratio sheet | One sentence: what this figure does **not** license your team's multinational to conclude |

A member drawn at random presents in two minutes.

---

## Hand in

On ZoneCours before leaving, one per team: `.twbx`, provenance log, slide. Formative.

**The one rule:** your log records at least one place where the data disagreed with the readings — or
with each other.

**Team project milestone (Session 04):** a one-paragraph footprint of your firm — its five most
important countries, with sources.

---

## What loses credit

- Joining NMC to WDI or SIPRI on names or on COW codes treated as ISO
- `SUM` of a ratio across years or states
- "China overtook the US in …" without saying on what measure
- A catch about the theory rather than about what the firm may conclude
