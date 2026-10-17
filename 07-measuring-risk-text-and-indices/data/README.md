# Session 07 — Data

Nothing in this folder is committed except this file. Download at source, keep files as they
arrived in `raw/`, and record each in your provenance log.

```text
07-measuring-risk-text-and-indices/data/
├── raw/
│   ├── firmquarter_2022q1.csv              ← firm-level political risk
│   ├── Global_Policy_Uncertainty_Data.xlsx ← EPU, global
│   ├── gdelt_headlines.csv                 ← your team's 40 headlines, as retrieved
│   ├── data_gpr_export.xls                 ← from Session 01 (re-download: it has been revised)
│   └── wgidataset_with_sourcedata-2025.xlsx ← Worldwide Governance Indicators, 2025 edition
├── coded/
│   └── coding_sheet.xlsx                   ← your coding: one row per headline, two coders
└── provenance-log.csv
```

---

## (a) Firm-level political risk — Hassan, Hollander, van Lent & Tahoun

| | |
|---|---|
| **Landing page** | [firmlevelrisk.com/download](https://www.firmlevelrisk.com/download) |
| **File** | `firmquarter_2022q1.csv` (the latest vintage; older ones back to `firmquarter_2019q2.csv`) — hosted on Dropbox, "right-click, save as" |
| **Content** | One row per firm × quarter: overall political risk (**PRisk**), non-political risk, sentiment, and risk by political topic |
| **Coverage** | Earnings calls of listed firms, `2002q1` to `2022q1` (the page still says "through March 2021"; the file runs a year further). **No longer updated** — current data are with the authors' commercial partner |
| **Access** | Free, no registration |

The file is large (about 354,000 rows). Tableau handles it; Excel may not. Despite the `.csv`
extension it is **tab-separated**: if Tableau shows a single column, open *Text File Properties* on the
data source and set the field separator to *Tab*. Then **read the column names**. In the `2022q1`
vintage they are: `date` (the quarter, a string such as `2010q1`), firm identifiers `gvkey` (keep it
a string — it has leading zeros), `company_name`, `isin`, `cusip`, `ticker`, the headquarters country
`hqcountrycode` (**2-letter** ISO code: `US`, `CA`, `GB`…), and the risk measures `PRisk`, `NPRisk`,
`Risk`, `PSentiment`, `NPSentiment`, `Sentiment` and `PRiskT_economic` … `PRiskT_technology` (eight
topics). Write the exact names in your log — they have changed between vintages.

## (a) Economic Policy Uncertainty — Baker, Bloom & Davis

| | |
|---|---|
| **Landing page** | [policyuncertainty.com](https://www.policyuncertainty.com/) |
| **File** | `https://www.policyuncertainty.com/media/Global_Policy_Uncertainty_Data.xlsx` (global EPU, monthly, from 1997). Columns: `Year`, `Month`, `GEPU_current`, `GEPU_ppp` — two weightings of the same index (current-price or PPP-adjusted GDP); pick one and log it. The last rows hold a citation, not data |
| **Also** | `media/All_Country_Data.xlsx` — sheet `EPU`: `Year`, `Month`, the two global columns, then one column per country, named in English (`Canada`, `UK`, `US`, `Korea`…), useful for part (c) |
| **Access** | Free, CC BY 4.0 |

---

## (b) Your coded corpus — GDELT

| | |
|---|---|
| **Source** | The GDELT Project — [gdeltproject.org](https://www.gdeltproject.org/) — monitors news worldwide in many languages |
| **Tool** | The **DOC 2.0 API**, which returns a list of articles matching a query |
| **Access** | Free |

Build a query about your **team's firm's** key countries or sector and a geopolitical theme, for
example:

```text
https://api.gdeltproject.org/api/v2/doc/doc?query=(sanctions%20OR%20%22export%20controls%22)%20Vietnam%20sourcelang:english&mode=artlist&maxrecords=75&format=csv&timespan=12weeks
```

Open it in a browser; it downloads a CSV with four columns — `URL`, `MobileURL`, `Date`, `Title`.
Save it untouched as `gdelt_headlines.csv`. There is no source column: fill `source` in the coding
sheet with the domain of the `URL`. The API searches only the **last three months** (write it as
`timespan=12weeks`: `timespan=3months` returned an empty file when we tested it), and allows one
request every five seconds — if it answers "Please limit requests…", wait and retry. Then **draw 40
headlines at random** (sort by a random number in your spreadsheet) — not the first 40 — and paste
them into `coded/coding_sheet.xlsx`:

| id | date | source | url | title | coder_A | coder_B | final |
|---|---|---|---|---|---|---|---|

**If the API is down or changes**, collect 40 headlines by hand from a news search with the same
query and dates, and log the substitution. The point of today is the coding, not the API.

---

## (c) Composite index inputs

| Input | Source | Note |
|---|---|---|
| **Country GPR** (`GPRC_xxx`) | `data_gpr_export.xls`, Session 01 — re-download, it has been revised | 44 countries only — a missing-data decision for the others |
| **Country EPU** | `All_Country_Data.xlsx` | about twenty countries, columns named by country, not code |
| **Political stability and absence of violence** | [Worldwide Governance Indicators](https://www.worldbank.org/en/publication/worldwide-governance-indicators), 2025 edition — `wgidataset_with_sourcedata-2025.xlsx`, sheet `pv`; columns `Economy (code)`, `Year` (1996–2024), `Governance score (0-100)` | 0–100 scale since the 2025 edition (the old `Governance estimate (approx. -2.5 to +2.5)` is still there — do not mix them); **higher = more stable**, so it must be inverted. The landing page now serves the **2026** update (to 2025): use one edition only, and log which |
| **Ideal-point distance from the firm's home country** | UNGA ideal points, Session 04 | |

The 2025 WGI file is still online at
`https://www.worldbank.org/content/dam/sites/govindicators/doc/wgidataset_with_sourcedata-2025.xlsx`.

---

## Traps

- The firm-level file covers **listed firms that hold English-language earnings calls** — mostly US.
  An average across them is "the political risk US-listed firms talk about", not world risk.
- EPU is **monthly**, the firm file is **quarterly**: aggregate EPU to quarters before comparing.
- WGI changed scale and **recalculated its history** in 2025: never mix editions.
- GDELT's coverage of sources changes over time and is weighted towards online English-language
  media. Your 40 headlines are a sample of a sample — say so.
