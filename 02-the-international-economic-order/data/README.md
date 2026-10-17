# Session 02 — Data

Nothing in this folder is committed except this file. Download at source, keep the file as it
arrived in `raw/`, and record it in your provenance log.

```text
02-the-international-economic-order/data/
├── raw/
│   └── wdi_extract.xlsx           ← your DataBank extract, never edited (or the CSV route below)
└── provenance-log.csv              ← one line per file (template: templates/provenance-log.csv)
```

## The source

| | |
|---|---|
| **Dataset** | World Development Indicators (WDI) — World Bank |
| **Landing page** | <https://databank.worldbank.org/source/world-development-indicators> |
| **Catalogue entry** | <https://datacatalog.worldbank.org/search/dataset/0037712/world-development-indicators> |
| **Coverage** | 1960–2025 for most series; PPP series from 1990 |
| **Access** | Free, CC BY 4.0. Cite the World Bank and the release date shown in DataBank |

## The series you need

| Code | Series | Used for |
|---|---|---|
| `NY.GDP.MKTP.CD` | GDP (current US$) | the target figure |
| `NY.GDP.MKTP.PP.CD` | GDP, PPP (current international $) | *break*: the same figure at purchasing-power parity |
| `NE.TRD.GNFS.ZS` | Trade (% of GDP) | *extend*: world trade openness and "slowbalisation" |

## The countries you need — by ISO code, never by name

| Group | ISO 3166 alpha-3 codes |
|---|---|
| **G7** | `CAN` `FRA` `DEU` `ITA` `JPN` `GBR` `USA` |
| **World** | `WLD` (a World Bank aggregate, not a country) |
| **Baldwin's "Industrialising Six" (I6)** | `CHN` `KOR` `IND` `POL` `IDN` `THA` |

> **The G7 is not in WDI.** The World Bank publishes "World", "High income", "Euro area" and many
> other aggregates — but no G7. You build it. That is the first decision of the round, and the
> first line in your notes.

## Route A — a DataBank extract (recommended)

1. Open DataBank WDI. **Country:** tick the 13 countries above plus *World*.
2. **Series:** search and tick the three codes.
3. **Time:** 1970 to the latest year.
4. **Layout:** Time in **columns**, Country and Series in rows (the default) — you will pivot in Tableau.
5. **Download options → Excel**. Save to `raw/` without opening and re-saving it.

DataBank writes missing values as `..` — two dots. Remember that when Tableau calls your numbers text.

## Route B — the per-indicator CSV (if DataBank is slow)

```bash
mkdir -p 02-the-international-economic-order/data/raw
curl -L -o 02-the-international-economic-order/data/raw/gdp_current_usd.zip \
  "https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=csv"
```

Repeat for `NY.GDP.MKTP.PP.CD` and `NE.TRD.GNFS.ZS` (one zip per series). Each zip holds three
files (checked October 2026; the number at the end of the name changes between releases):

| File | What it holds |
|---|---|
| `API_NY.GDP.MKTP.CD_DS2_en_csv_v2_….csv` | the data: one row per country or aggregate, 1960 to the latest year |
| `Metadata_Country_API_….csv` | `Country Code`, `Region`, `IncomeGroup`, `SpecialNotes`, `TableName` — aggregates such as `WLD` have an empty `Region` |
| `Metadata_Indicator_API_….csv` | `INDICATOR_CODE`, `INDICATOR_NAME`, `SOURCE_NOTE`, `SOURCE_ORGANIZATION` — the definition to cite |

The data file has **four lines above the header** (`"Data Source"`, a blank line, `"Last Updated
Date"` — your version — and another blank line): in Tableau's text connector use **Data
Interpreter**, or skip four rows elsewhere. The header is `Country Name`, `Country Code`,
`Indicator Name`, `Indicator Code`, then `1960` … `2025` as plain years, plus an empty last column.
Two differences from Route A: the code column is **`Indicator Code`**, not `Series Code`, and
missing values are **empty cells**, not `..`.
