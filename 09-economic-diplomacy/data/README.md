# Session 09 — Data

Nothing in this folder is committed except this file. Download at source, keep each file as it
arrived in `raw/`, and record it in your provenance log.

```text
09-economic-diplomacy/data/
├── raw/
│   ├── DataDownload.xlsx              ← Lowy Global Diplomacy Index, post level
│   ├── imts_exports_2023.csv          ← IMF bilateral goods exports (your own extraction)
│   └── wdi_gdp.csv                    ← World Bank GDP, current US$
└── provenance-log.csv
```

## Source 1 — Lowy Institute Global Diplomacy Index

| | |
|---|---|
| **Landing page** | [globaldiplomacyindex.lowyinstitute.org](https://globaldiplomacyindex.lowyinstitute.org/) |
| **File** | `https://globaldiplomacyindex.lowyinstitute.org/downloads/DataDownload.xlsx` |
| **Structure** | Sheets `2023`, `2021`, `2019`, `2017`, `2016`; **one row per diplomatic post**. Columns (checked October 2026): `COUNTRY` (sending country), `POPULATION (M)`, `GDP (B, USD)`, `G20 RANK`, `OECD RANK`, `ASIA RANK`, `OVERALL RANK`, `POST CITY`, `POST COUNTRY` (host), `TYPE OF POST` (four values: `Embassy / High Commission`, `Consulate / Consulate-General`, `Permanent Mission`, `Other`) and `POST TYPE TITLE` (the detailed label, e.g. `Mission to UN`) |
| **Coverage** | The networks of 66 countries or territories (2024 edition, data collected up to November 2023) — G20, OECD and Asian states. The 66 include `Taiwan*` and the `European External Action Service` (the EU), which has no ISO3 code. The `2023` sheet has 7,700 posts; the `2017` sheet covers 60 senders. **The `2019` sheet is incomplete** (40 rows, Venezuela only) — do not use it |
| **Access** | Free, no registration |

> **The trap.** The file lists posts that **exist**. A country with no post in a partner simply does
> not appear — the zero is missing, not zero. You will have to build it.

## Source 2 — IMF bilateral goods trade (IMTS, formerly DOTS)

| | |
|---|---|
| **Landing page** | [data.imf.org — IMF.STA:IMTS](https://data.imf.org/en/datasets/IMF.STA:IMTS) |
| **What to extract** | **Exports of goods, Free on board (FOB), US dollar** (`XG_FOB_USD`), annual, **2023**, for the sending countries you study (at least five of the Lowy 66, including Canada) × **all partners** |
| **Access** | Free; use the *Download* button (CSV or Excel) |

Read the indicator list carefully: it has four indicators — exports FOB (`XG_FOB_USD`), imports FOB
(`MG_FOB_USD`), imports CIF (`MG_CIF_USD`) and the trade balance (`TBG_USD`). The "mirror" of A's
exports to B is B's reported imports from A. Choose **exports reported by the exporter**
(`XG_FOB_USD`, `COUNTRY` = the exporter) and say so in your log. The columns are `COUNTRY`
(reporter), `COUNTERPART_COUNTRY` (partner), both in ISO3 codes, `TIME_PERIOD` and `OBS_VALUE`
(US dollars); aggregate partners have codes starting with `G` or `TX` (`G001` World). Details:
[Session 04 data](../../04-trade-conflict-and-fragmentation/data/README.md).

## Source 3 — World Bank WDI

| | |
|---|---|
| **Indicator** | `NY.GDP.MKTP.CD` — GDP, current US$ |
| **Download** | `https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=csv` (zip) |
| **Access** | Free, CC BY 4.0 |

## Country names

Lowy has **names only, no codes**; the IMF and the World Bank use ISO3 codes (with exceptions:
Kosovo is `KOS` at the IMF, `XKX` at the World Bank). Lowy's `POST COUNTRY` also has inconsistent
spellings and typos in the 2023 sheet (`Cote D'Ivoire` / `Cote d'Ivoire`, `Portual`, `Nigaragua`,
`Dominica Republic`, `Brussels` as a country, starred entries such as `Taiwan*`). Build a small
concordance sheet `name → ISO3` for every Lowy name you use and join on ISO3. List every manual fix in
your provenance log.
