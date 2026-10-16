# Session 06 — Data

Nothing in this folder is committed except this file. Download at source, keep files as they
arrived in `raw/`, and record each in your provenance log.

```text
06-private-authority-and-standards/data/
├── raw/
│   ├── iso_survey_14001.xlsx        ← or iso_survey_transcribed.xlsx (fallback)
│   ├── iso_survey_9001.xlsx         ← the placebo standard
│   ├── imf_imts_exports.csv         ← exporter × partner × year
│   └── wdi_gdp.csv                  ← NY.GDP.MKTP.CD
└── provenance-log.csv
```

---

## 1. The ISO Survey of certifications

| | |
|---|---|
| **Dataset** | The ISO Survey of Management System Standard Certifications |
| **Producer** | ISO; since recent editions produced and hosted with **IAF CertSearch** |
| **Landing pages** | [iso.org/the-iso-survey.html](https://www.iso.org/the-iso-survey.html) · [IAF CertSearch — ISO Survey](https://support.iafcertsearch.org/certification-bodies/overview/market-intelligence/iso-survey) |
| **What you need** | Number of **ISO 14001** certificates by country and year; the same for **ISO 9001** |
| **Coverage** | 1993 onwards (ISO 14001 from its first certificates in the late 1990s) to 2024 |
| **Access** | Free. Access through IAF CertSearch **may require a free account** — create it at least two days before class. The exact file format was not verified when this page was written: log what you get |

### Fallback if you cannot download the full tables

Transcribe a subset by hand from the survey's published tables (any edition you can open), one row
per country-year, into `iso_survey_transcribed.xlsx`:

| iso3 | country | year | iso14001 | iso9001 |
|---|---|---|---|---|

- **Countries:** your team's firm's home country and five key countries, plus — split across the
  team — the G20 and ten other countries of your choice (about **35 countries**).
- **Years:** 2000, 2005, 2010, 2015, 2020, 2024 (or the nearest available).

That is about two hundred rows: forty minutes for a team of four. Write "transcribed from …, edition
…" in the version column.

---

## 2. Bilateral exports — IMF IMTS

| | |
|---|---|
| **Dataset** | International Trade in Goods by partner country (IMTS, formerly DOTS) |
| **Landing page** | [data.imf.org — IMF.STA:IMTS](https://data.imf.org/en/datasets/IMF.STA:IMTS) |
| **What you need** | **Goods exports, FOB, US dollars**, annual, for your ~35 reporting countries to **all partner countries**, for the same years as the ISO data |
| **Access** | Free (Download button) |

If you collected IMTS data in Session 04, reuse that download and add the missing years.

---

## 3. GDP — World Bank WDI

`NY.GDP.MKTP.CD` (GDP, current US$), all countries, 1995–latest:
`https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=csv` (a zip; the data file
is the one starting `API_`). You already used it in Session 02.

---

## Traps

- **Counts are not adoption rates.** A large economy has more certificates because it has more
  firms. Normalise: certificates per **billion US$ of GDP** — and check how Prakash and Potoski scale
  their own dependent variable; if it differs, that is a logged disagreement.
- **Certification-body coverage changed** across survey editions. A jump in one country in one year
  may be reporting, not adoption. Look for it and log it.
- ISO 14001 was **revised in 2015**; transition years can show dips as certificates expire and are
  reissued.
- **Country names** in the ISO tables are not ISO codes: Hong Kong, Taiwan, Korea, Türkiye, Czechia,
  Viet Nam will not match by name. Add `iso3` yourself.
