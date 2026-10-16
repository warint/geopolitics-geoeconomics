# Data sources

Every dataset used in the course: who produces it, where to collect it, what it costs you to get it,
and the trap it holds. **Collect at source, every time**: the course repository contains no data.

Access status was last checked on **16 October 2026**. Sources move: if a link has changed, the
producer's landing page is canonical, and the change goes in your provenance log.

> **Lead times.** Two sources need action **days before** the session: the **Global Sanctions Data
> Base** (request form, data e-mailed within about 24 hours — request it after Session 08) and the
> **ISO Survey** (may require a free IAF CertSearch account — create it after Session 04).

---

## The registry

| # | Dataset | Producer | Landing page | File to collect | Coverage | Access | Session |
|---|---|---|---|---|---|---|---|
| 1 | **Geopolitical Risk (GPR) index** | Caldara & Iacoviello | [matteoiacoviello.com/gpr.htm](https://www.matteoiacoviello.com/gpr.htm) | `gpr_files/data_gpr_export.xls` (monthly; global, threats, acts, historical, 44 country indices) | 1900 / 1985 – last month | free | 01, 07, 12 |
| 2 | **World Development Indicators** | World Bank | [DataBank WDI](https://databank.worldbank.org/source/world-development-indicators) | `NY.GDP.MKTP.CD` (GDP, current US$), `NE.TRD.GNFS.ZS` (trade, % GDP), `NY.GDP.MKTP.PP.CD` (GDP, PPP) — per-indicator CSV: `api.worldbank.org/v2/en/indicator/{CODE}?downloadformat=csv` | 1960–2025 | free, CC BY 4.0 | 02, 03, 09 |
| 3 | **National Material Capabilities v7.0** | Correlates of War | [correlatesofwar.org/data-sets/national-material-capabilities](https://correlatesofwar.org/data-sets/national-material-capabilities/) | `wp-content/uploads/NMCv7.zip` (csv + codebook) | 1816–2022 | free; cite Singer, Bremer & Stuckey (1972) | 03 |
| 4 | **Military Expenditure Database** | SIPRI | [sipri.org/databases/milex](https://www.sipri.org/databases/milex) | `SIPRI-Milex-data-1949-2025_v1.2.xlsx` | 1949–2025 | free for non-commercial use | 03 |
| 5 | **UN General Assembly ideal points** | Bailey, Strezhnev & Voeten | [Harvard Dataverse doi:10.7910/DVN/LEJUQZ](https://doi.org/10.7910/DVN/LEJUQZ) | `IdealpointestimatesFP_2026FP.csv` (country-year), `AgreementScores.csv`, codebook | 1946–2025 | free | 04, 12 |
| 6 | **International Trade in Goods by partner (IMTS, formerly DOTS)** | IMF | [data.imf.org — IMF.STA:IMTS](https://data.imf.org/en/datasets/IMF.STA:IMTS) | exporter × partner × year, goods exports in US$ (Download button) | from 1948 for many countries | free | 04, 09 |
| 7 | **Kuziemko & Werker replication data** | AidData | [AidData replication page](https://www.aiddata.org/replication-datasets/how-much-is-a-seat-on-the-security-council-worth-foreign-aid-and-bribery-at-the-united-nations) | "Download Data" link (format to be checked on download) | 1946–2001 | free | 05 |
| 8 | **UN Security Council elected members** | United Nations | [main.un.org/securitycouncil — elected members](https://main.un.org/securitycouncil/en/content/countries-elected-members) | the table, copied into a sheet: country × term | 1946–today | free | 05 |
| 9 | **US foreign aid (Greenbook)** | US State Dept / ForeignAssistance.gov | [foreignassistance.gov/data](https://foreignassistance.gov/data) · frozen mirror: [foreignassistance.andrewheiss.com/greenbook.html](https://foreignassistance.andrewheiss.com/greenbook.html) | country summary, obligations, constant US$ | 1946–2023/24 | free; the official site has been unstable since 2025 — use the mirror if it fails, and log it | 05 |
| 10 | **ISO Survey of certifications** | ISO, via IAF CertSearch | [iso.org/the-iso-survey.html](https://www.iso.org/the-iso-survey.html) · [IAF CertSearch — ISO Survey](https://support.iafcertsearch.org/certification-bodies/overview/market-intelligence/iso-survey) | ISO 14001 and ISO 9001 certificates by country and year | 1993–2024 | free; may require an account | 06 |
| 11 | **Firm-level political risk** | Hassan, Hollander, van Lent & Tahoun | [firmlevelrisk.com/download](https://www.firmlevelrisk.com/download) | `firmquarter_2022q1.csv` (firm × quarter PRisk, NPRisk, sentiment, topic risks) | 2002–2021Q1 | free; no longer updated | 07 |
| 12 | **Economic Policy Uncertainty** | Baker, Bloom & Davis | [policyuncertainty.com](https://www.policyuncertainty.com/) | `media/Global_Policy_Uncertainty_Data.xlsx`, `media/All_Country_Data.xlsx` | 1997 – last month (US from 1900) | free, CC BY 4.0 | 07 |
| 13 | **GDELT** | The GDELT Project | [gdeltproject.org](https://www.gdeltproject.org/) | news articles, via the DOC 2.0 API or the web "Summary" tool | 2015–today | free | 07 |
| 14 | **Dyadic Cyber Incident and Campaign Data (DCID) v2.0** | Maness, Valeriano, Hedgecock, Macias & Jensen | [Harvard Dataverse doi:10.7910/DVN/CQOMYV](https://doi.org/10.7910/DVN/CQOMYV) | `Master_DCID_2.0_Release_public_Sep2022.tab` (export as csv) | 2000–2020, 429 incidents | free | 08 |
| 15 | **EuRepoC Global Dataset of Cyber Incidents v1.3** | European Repository of Cyber Incidents | [eurepoc.eu](https://eurepoc.eu/database/) · [Zenodo doi:10.5281/zenodo.14965395](https://doi.org/10.5281/zenodo.14965395) | `eurepoc_global_dataset_1_3.csv`, codebook | 2000–2024, 3,416 incidents | free | 08 |
| 16 | **CFR Cyber Operations Tracker** | Council on Foreign Relations | [cfr.org/cyber-operations](https://www.cfr.org/cyber-operations/) | no official download — browse and hand-code | 2005–2024 | free to read | 08 (reading only) |
| 17 | **Global Diplomacy Index** | Lowy Institute | [globaldiplomacyindex.lowyinstitute.org](https://globaldiplomacyindex.lowyinstitute.org/) | `downloads/DataDownload.xlsx` — one sheet per edition, one row per diplomatic post | 2016, 2017, 2019, 2021, 2023 (2024 edition) | free | 09 |
| 18 | **Global Sanctions Data Base, Release 5** | Felbermayr, Kirilakha, Syropoulos, Yalcin & Yotov | [globalsanctionsdatabase.com](https://globalsanctionsdatabase.com/) | **request form** → files by e-mail (case-level and dyadic) | 1949–2025, 1,794 cases | free on request; **no redistribution, no commercial use** — never publish raw data to Tableau Public | 10 |
| 19 | **TIES — Threat and Imposition of Economic Sanctions v4.0** | Morgan, Bapat & Kobayashi | [sanctions.web.unc.edu](https://sanctions.web.unc.edu/) | Excel case file + user manual | 1945–2005 | free | 10 |
| 20 | **OECD Inventory of Export Restrictions on Critical Raw Materials** | OECD | [OECD Data Explorer](https://data-explorer.oecd.org/) (search "export restrictions raw materials") · report: [doi:10.1787/d5ca8f62-en](https://doi.org/10.1787/d5ca8f62-en) | country × commodity × year × measure type | 2009–latest, 65 commodities, 82 countries | free | 11, take-home specimen |
| 21 | **Global Supply Chain Pressure Index** | Federal Reserve Bank of New York | [newyorkfed.org/research/policy/gscpi](https://www.newyorkfed.org/research/policy/gscpi) | `…/gscpi/gscpi_interactive_data.csv` (rows = months from 1997, columns = vintages; use the latest column) | 1997 – last month | free | 11 |
| 22 | **POLCON — Political Constraint Index** | Witold Henisz, Wharton | [POLCON dataset page](https://mgmt.wharton.upenn.edu/faculty/heniszpolcon/polcondataset/) | `POLCON_2025_FINALPOSTED.xlsx` (sheets *Data* and *Key*) | 1800–2025 | free | 12 |
| 23 | **Worldwide Governance Indicators** | World Bank | [worldbank.org — WGI](https://www.worldbank.org/en/publication/worldwide-governance-indicators) | six dimensions, country-year, 2025 edition (0–100 scale, history recalculated) | 1996–2024 | free | 07, 12 |

---

## Traps, source by source

| Dataset | The trap |
|---|---|
| **GPR** | Revised monthly; vintages exist (`data_gpr_export_YYYYMM.xls`). Country indices are the anglophone press's attention to a country, not that country's risk. |
| **WDI** | Aggregates ("World", "High income", "G7" is *not* provided — build it) sit in the same file as countries. Current-dollar shares move with exchange rates. |
| **NMC** | Uses COW country codes, not ISO; states enter and exit the system (Germany 1945–1990). Ends in 2022. |
| **SIPRI** | Several sheets (current US$, constant US$, % of GDP, per capita); "xxx" and "..." mean different things — read the notes. |
| **UNGA ideal points** | Uses COW codes and ISO; estimated by calendar year since 2026 (earlier versions by session) — the variable meaning changed between versions. |
| **IMF IMTS** | Exports reported by A ≠ imports reported by B ("mirror" asymmetry). Choose one side and say which. |
| **UNSC members** | Two-year terms starting 1 January; election happens the October before — the paper's "election year" matters. |
| **US aid** | Obligations vs disbursements; current vs constant dollars; the official site moved in 2025. |
| **ISO Survey** | Coverage of certification bodies changed over time: jumps in a country's count can be reporting, not adoption. |
| **Firm-level risk** | Listed firms holding earnings calls in English — mostly US. Stops in 2021. |
| **DCID** | State-to-state rivals only; 2000–2020; coded from open sources — attribution is by definition uncertain. |
| **EuRepoC** | Much wider than DCID (includes criminal and non-state); filter on initiator type before comparing. |
| **Lowy GDI** | 66 countries' networks only; counts posts, not staff or budget. |
| **GSDB** | Licence forbids redistribution: workbooks go to ZoneCours, never Tableau Public with the raw data. "Success" is the coders' judgement of objectives met. |
| **TIES** | Includes **threats** of sanctions — a case may never have been imposed. |
| **OECD export restrictions** | Counts measures, not their stringency; a licensing requirement and an outright ban each count once. |
| **GSCPI** | Every month the whole history is re-estimated: use one vintage and say which. |
| **POLCON / WGI** | WGI's 2025 edition changed scale and recalculated history: never mix editions. |

---

## Country codes

Join on **ISO 3166 alpha-3** codes, never on names. NMC, the UNGA ideal points and DCID use
**Correlates of War** codes: keep a concordance sheet (COW `ccode` ↔ ISO3) in your workbook. The
`countrycode` concordance tables published by Arel-Bundock et al. are the standard reference.
