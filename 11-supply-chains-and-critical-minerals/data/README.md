# Session 11 — Data

Nothing in this folder is committed except this file. Download at source, keep each file as it
arrived in `raw/`, and record it in your provenance log.

```text
11-supply-chains-and-critical-minerals/data/
├── raw/
│   ├── oecd_export_restrictions.csv     ← exported from OECD Data Explorer, never edited
│   ├── usgs_mcs_<year>_<mineral>.pdf    ← the four USGS commodity summaries, as downloaded
│   └── gscpi_interactive_data.csv       ← NY Fed, as downloaded
├── usgs_world_production.csv           ← YOUR transcription of the four production tables
└── provenance-log.csv                   ← one line per file (template: templates/provenance-log.csv)
```

---

## 1 · OECD Inventory of Export Restrictions on Critical Raw Materials

| | |
|---|---|
| **Producer** | OECD, Trade and Agriculture Directorate |
| **Landing page** | [OECD Data Explorer](https://data-explorer.oecd.org/) — search *"export restrictions"* and *"raw materials"*. Report of the latest edition: *OECD Inventory of Export Restrictions on Critical Raw Materials 2026*, [doi:10.1787/d5ca8f62-en](https://doi.org/10.1787/d5ca8f62-en) |
| **What to export** | Every year, every country, every commodity, every measure type → **Download → Filtered data in tabular text (CSV)** |
| **Coverage** | 2009 onward, about 65 commodities, about 82 producing countries |
| **Access** | Free |

> **The name has changed.** Earlier editions were called *Inventory of Export Restrictions on
> Industrial Raw Materials* (2024, 2025). The dataflow's exact name and code in the Data Explorer
> can change between editions: find it by search, and write the name, the dataflow identifier shown
> in the URL, and the edition in your provenance log.

**The columns you need** (names vary by export; map them in your log):

| Concept | Typical label |
|---|---|
| Exporting country | `Reference area` / `REF_AREA` |
| Commodity | `Commodity` / a commodity code with an HS reference |
| Measure type | export tax, export quota, export prohibition, licensing requirement, minimum export price, … |
| Year | `TIME_PERIOD` |
| Value | 1 if the measure applies (some exports show a count, some the tax rate) |

> **Check before you trust.** The inventory counts *measures*, not their stringency. A licensing
> requirement and an outright ban each count once. Write down which measure types your figure
> includes.

---

## 2 · USGS *Mineral Commodity Summaries* — world mine production

| | |
|---|---|
| **Producer** | US Geological Survey, National Minerals Information Center |
| **Landing page** | [usgs.gov — Mineral Commodity Summaries](https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries) |
| **What to collect** | The most recent edition's two-page summaries for **cobalt, graphite (natural), lithium and rare earths** |
| **The table** | *World Mine Production and Reserves*: one row per producing country, two columns of production (previous year, current-year estimate), and reserves |
| **Access** | Free, public domain |

There is no ready-made file for these four tables in the shape you need. **You transcribe them**,
one row per country × mineral, into `usgs_world_production.csv`:

```text
mineral,country,iso3,year,production,unit,source_page
cobalt,Congo (Kinshasa),COD,2025,...,metric tons cobalt content,MCS 2026 p. ...
cobalt,Indonesia,IDN,2025,...,metric tons cobalt content,MCS 2026 p. ...
...
```

Rules of transcription — each one is a decision you log:

1. Use the **estimated latest year** column, and say so.
2. **Exclude** the rows *"World total (rounded)"* and keep it aside as a check.
3. Keep *"Other countries"* as its own row, flagged `iso3 = OTH`. You will decide in the practice
   whether it enters the HHI.
4. Withheld figures ("W") and the United States' confidential values: leave blank and note them.
5. Write the **unit** exactly: cobalt and lithium are reported in metal content, graphite in tons of
   natural graphite, rare earths in rare-earth-oxide equivalent. Never add across minerals.

---

## 3 · Global Supply Chain Pressure Index (GSCPI)

| | |
|---|---|
| **Producer** | Federal Reserve Bank of New York |
| **Landing page** | [newyorkfed.org/research/policy/gscpi](https://www.newyorkfed.org/research/policy/gscpi) |
| **File** | `gscpi_interactive_data.csv` (the *interactive data* download on the page) |
| **Format** | Rows are months from 1997; **columns are vintages** — each monthly release re-estimates the whole history |
| **Access** | Free |

> **The vintage trap.** Use **one column only — the latest vintage** — and write its name in your
> log. An older Excel file is also linked from the page; check its last-saved date before using it.
> Mixing vintages produces a series no one ever published.

Download from the terminal (optional; if the link has moved, use the landing page):

```bash
mkdir -p 11-supply-chains-and-critical-minerals/data/raw
curl -L -o 11-supply-chains-and-critical-minerals/data/raw/gscpi_interactive_data.csv \
  "https://www.newyorkfed.org/medialibrary/research/interactives/data/gscpi/gscpi_interactive_data.csv"
```
