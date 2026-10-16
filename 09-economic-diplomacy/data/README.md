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
| **Structure** | One sheet per data year (2023, 2021, 2019, 2017, 2016); **one row per diplomatic post**: the sending country, the city and country of the post, the type of post (embassy, consulate, permanent mission…) |
| **Coverage** | The networks of 66 countries (2024 edition, data collected in 2023) — G20, OECD and Asian states |
| **Access** | Free, no registration |

> **The trap.** The file lists posts that **exist**. A country with no post in a partner simply does
> not appear — the zero is missing, not zero. You will have to build it.

## Source 2 — IMF bilateral goods trade (IMTS, formerly DOTS)

| | |
|---|---|
| **Landing page** | [data.imf.org — IMF.STA:IMTS](https://data.imf.org/en/datasets/IMF.STA:IMTS) |
| **What to extract** | **Exports of goods, FOB, in US dollars**, annual, **2023**, for the sending countries you study (at least five of the Lowy 66, including Canada) × **all partners** |
| **Access** | Free; use the *Download* button (CSV or Excel) |

Read the indicator list carefully: the dataset reports both exports and imports, and partner-reported
("mirror") values. Choose **exports reported by the exporter** and say so in your log.

## Source 3 — World Bank WDI

| | |
|---|---|
| **Indicator** | `NY.GDP.MKTP.CD` — GDP, current US$ |
| **Download** | `https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=csv` (zip) |
| **Access** | Free, CC BY 4.0 |

## Country names

Lowy, the IMF and the World Bank do **not** spell countries the same way (Türkiye, Korea, Côte
d'Ivoire, Viet Nam, Hong Kong SAR…). Build a small concordance sheet `name → ISO3` for every
unmatched name and join on ISO3. List every manual fix in your provenance log.
