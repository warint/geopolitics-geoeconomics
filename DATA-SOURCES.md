# Data sources

Every dataset used in the course: who produces it, where to collect it, what it costs you to get it,
and the trap it holds. **Collect at source, every time**: the course repository contains no data.

Access status was last checked on **16 October 2026**. Sources move: if a link has changed, the
producer's landing page is canonical, and the change goes in your provenance log.

> **Lead times.** Two sources need action **days before** the session: the **Global Sanctions Data
> Base** (request form, data e-mailed within about 24 hours — request it after Session 08) and the
> **ISO Survey** (requires a free IAF CertSearch account — log in at [iafcertsearch.org/services/iso-survey](https://www.iafcertsearch.org/services/iso-survey); create it after Session 04).

---

## The registry

| # | Dataset | Producer | Landing page | File to collect | Coverage | Access | Session |
|---|---|---|---|---|---|---|---|
| 1 | **Geopolitical Risk (GPR) index** | Caldara & Iacoviello | [matteoiacoviello.com/gpr.htm](https://www.matteoiacoviello.com/gpr.htm) | `gpr_files/data_gpr_export.xls` (one sheet, `Sheet1`; monthly `GPR`, `GPRT`, `GPRA`, historical `GPRH`; 44 country series `GPRC_XXX` — percent of articles, from 1985 — and historical `GPRHC_XXX`; variable notes in the `var_name`/`var_label` columns) | 1900 / 1985 – last month | free | 01, 07, 12 |
| 2 | **World Development Indicators** | World Bank | [DataBank WDI](https://databank.worldbank.org/source/world-development-indicators) | `NY.GDP.MKTP.CD` (GDP, current US$), `NE.TRD.GNFS.ZS` (trade, % GDP), `NY.GDP.MKTP.PP.CD` (GDP, PPP) — per-indicator CSV: `api.worldbank.org/v2/en/indicator/{CODE}?downloadformat=csv` (4 lines above the header; `Indicator Code`, not `Series Code`; missing = blank) | 1960–2025 | free, CC BY 4.0 | 02, 03, 09 |
| 3 | **National Material Capabilities v7.0** | Correlates of War | [correlatesofwar.org/data-sets/national-material-capabilities](https://correlatesofwar.org/data-sets/national-material-capabilities/) | `wp-content/uploads/NMCv7.zip` (codebook `NMC_Documentation_v7.pdf` + nested `NMC-v7-abridged.zip` → `NMC-70-abridged.csv`) | 1816–2022 | free; cite Singer, Bremer & Stuckey (1972) | 03 |
| 4 | **Military Expenditure Database** | SIPRI | [sipri.org/databases/milex](https://www.sipri.org/databases/milex) | `SIPRI-Milex-data-1949-2025_v1.2.xlsx` (revised 27 April 2026) | 1949–2025 | free for non-commercial use | 03 |
| 5 | **UN General Assembly ideal points** | Bailey, Strezhnev & Voeten | [Harvard Dataverse doi:10.7910/DVN/LEJUQZ](https://doi.org/10.7910/DVN/LEJUQZ) | `IdealpointestimatesFP_2026FP.csv` (country-year: `iso3c`, `ccode`, `year`, `IdealPointFP`; `session` = `year` − 1945), `AgreementScores.csv`, codebook | 1946–2025 | free | 04, 12 |
| 6 | **International Trade in Goods by partner (IMTS, formerly DOTS)** | IMF | [data.imf.org — IMF.STA:IMTS](https://data.imf.org/en/datasets/IMF.STA:IMTS) | exporter × partner × year: indicator `XG_FOB_USD`; columns `COUNTRY`, `COUNTERPART_COUNTRY`, `TIME_PERIOD`, `OBS_VALUE` (US dollars); ISO3 codes except `KOS`, `WBG`; aggregates coded `G…`/`TX…` (Download button) | from 1948 for many countries | free | 04, 06, 09 |
| 7 | **Kuziemko & Werker replication data** | AidData | [AidData replication page](https://www.aiddata.org/replication-datasets/how-much-is-a-seat-on-the-security-council-worth-foreign-aid-and-bribery-at-the-united-nations) | "Download Data" link (a Google Drive file; required a Google sign-in when checked in October 2026 — contents unverified) | 1946–2001 | free | 05 |
| 8 | **UN Security Council elected members** | United Nations | [main.un.org/securitycouncil — elected members](https://main.un.org/securitycouncil/en/content/countries-elected-members) | the table, copied into a sheet: country × term | 1946–today | free | 05 |
| 9 | **US foreign aid (Greenbook)** | US State Dept / ForeignAssistance.gov | [foreignassistance.gov/data](https://foreignassistance.gov/data) · frozen mirror (December 2024; use its Dropbox zip): [foreignassistance.andrewheiss.com](https://foreignassistance.andrewheiss.com/) | Country Summary `us_foreign_aid_country.csv`: ISO3 in `Country Code`; filter `Transaction Type Name` = Obligations; use `constant_amount`. Economic and military **combined** — the split is only in the Greenbook xlsx on the mirror (`greenbook.html`, FY 1946–2020) | official 1946–2026 · mirror 1946–2024 | free; the official site has been unstable since 2025 — use the mirror if it fails, and log it | 05 |
| 10 | **ISO Survey of certifications** | ISO, via IAF CertSearch | [iso.org/the-iso-survey.html](https://www.iso.org/the-iso-survey.html) · [IAF CertSearch — ISO Survey](https://support.iafcertsearch.org/certification-bodies/overview/market-intelligence/iso-survey) | ISO 14001 and ISO 9001 certificates by country and year; from 2025 compiled from IAF CertSearch data (file format unverified) | 1993–2024 | free; IAF CertSearch account required | 06 |
| 11 | **Firm-level political risk** | Hassan, Hollander, van Lent & Tahoun | [firmlevelrisk.com/download](https://www.firmlevelrisk.com/download) | `firmquarter_2022q1.csv` (firm × quarter `PRisk`, `NPRisk`, sentiment, topic risks; **tab-separated despite `.csv`**; `hqcountrycode` is ISO **2**-letter) | 2002Q1–2022Q1 | free; no longer updated | 07 |
| 12 | **Economic Policy Uncertainty** | Baker, Bloom & Davis | [policyuncertainty.com](https://www.policyuncertainty.com/) | `media/Global_Policy_Uncertainty_Data.xlsx` (`Year`, `Month`, `GEPU_current`, `GEPU_ppp` — no `GEPU` column), `media/All_Country_Data.xlsx` (sheet `EPU`, one column per country, named in English) | 1997 – last month (some countries from 1985; the US from 1900 in a separate file) | free, CC BY 4.0 | 07 |
| 13 | **GDELT** | The GDELT Project | [gdeltproject.org](https://www.gdeltproject.org/) | news articles, via the DOC 2.0 API (CSV columns `URL`, `MobileURL`, `Date`, `Title`; one request every 5 seconds) or the web "Summary" tool | the DOC API searches a rolling last 3 months — use `timespan=12weeks` | free | 07 |
| 14 | **Dyadic Cyber Incident and Campaign Data (DCID) v2.0** | Maness, Valeriano, Hedgecock, Macias & Jensen | [Harvard Dataverse doi:10.7910/DVN/CQOMYV](https://doi.org/10.7910/DVN/CQOMYV) | `Master_DCID_2.0_Release_public_Sep2022.tab` (Access File → original CSV); codebook at [ryanmaness.com/cyber-conflict-dataset](https://www.ryanmaness.com/cyber-conflict-dataset), not on Dataverse | Sep 2000 – Jan 2021, 433 incidents | free, CC0 | 08 |
| 15 | **EuRepoC Global Dataset of Cyber Incidents v1.3** | European Repository of Cyber Incidents | [eurepoc.eu](https://eurepoc.eu/database/) · [Zenodo doi:10.5281/zenodo.14965395](https://doi.org/10.5281/zenodo.14965395) | `eurepoc_global_dataset_1_3.csv`, `eurepoc_codebook_1_2.pdf` | 2000–2024, 3,414 rows in the CSV (the record says 3,416) | free, CC BY-NC 4.0 | 08 |
| 16 | **CFR Cyber Operations Tracker** | Council on Foreign Relations | [cfr.org/cyber-operations](https://www.cfr.org/cyber-operations/) | no official download — browse and hand-code | 2005–2024 | free to read | 08 (reading only) |
| 17 | **Global Diplomacy Index** | Lowy Institute | [globaldiplomacyindex.lowyinstitute.org](https://globaldiplomacyindex.lowyinstitute.org/) | `downloads/DataDownload.xlsx` — one sheet per data year (`2023`, `2021`, `2019`, `2017`, `2016`), one row per diplomatic post: `COUNTRY`, `POST CITY`, `POST COUNTRY`, `TYPE OF POST`; **the 2019 sheet is incomplete** (Venezuela only, 40 rows) | 2016, 2017, 2019, 2021, 2023 (2024 edition) | free | 09 |
| 18 | **Global Sanctions Data Base, Release 5** | Felbermayr, Kirilakha, Syropoulos, Yalcin & Yotov | [globalsanctionsdatabase.com](https://globalsanctionsdatabase.com/) | **request form** → files by e-mail (case-level and dyadic). Case file columns (from a public notebook, not yet checked against the codebook): `case_id`, `sanctioned_state`, `sanctioning_state`, `begin_year`, `end_year`, six 0/1 type columns, `objective`, `success` | 1,794 cases; begin years 1949–2025 (the home page says 1950) | free on request; **no redistribution, no commercial use** — never publish raw data to Tableau Public | 10 |
| 19 | **TIES — Threat and Imposition of Economic Sanctions v4.0** | Morgan, Bapat & Kobayashi | [sanctions.web.unc.edu](https://sanctions.web.unc.edu/) | `TIESv4-1.xls` + `tiesusersmanualv4.pdf`; states as COW codes; threat-only cases have `imposition` = 0 | 1945–2005 | free | 10 |
| 20 | **POLCON — Political Constraint Index** | Witold Henisz, Wharton | [POLCON dataset page](https://mgmt.wharton.upenn.edu/faculty/heniszpolcon/polcondataset/) | `POLCON_2025_FINALPOSTED.xlsx` (sheets *Data* and *Key*) | 1800–2025 | free | 12 |
| 21 | **Worldwide Governance Indicators** | World Bank | [worldbank.org — WGI](https://www.worldbank.org/en/publication/worldwide-governance-indicators) | `wgidataset_with_sourcedata-2025.xlsx`: one sheet per dimension (`pv` = political stability), `Economy (code)`, `Year`, `Governance score (0-100)` — not to be mixed with the estimate column. The 2026 update (1996–2025) is now the landing-page default and recalculates history again: use one edition and log it | 1996–2024 (2025 ed.) | free | 07, 12 |
| 22 | **SATCAT — satellite catalogue** | CelesTrak (T. S. Kelso), from the US Space Force public catalogue | [celestrak.org/satcat](https://celestrak.org/satcat/) · [format](https://celestrak.org/satcat/satcat-format.php) | `pub/satcat.csv` (one row per catalogued object, 17 columns: `OBJECT_TYPE` PAY/R/B/DEB/UNK, `OPS_STATUS_CODE` — active = `+ P B S X`, `OWNER`, `LAUNCH_DATE`, `DECAY_DATE` empty = in space, `ORBIT_CENTER`) | 1957 – day of download | free; usage policy: one download per update | 11 |
| 23 | **GCAT — General Catalog of Artificial Space Objects** | Jonathan C. McDowell | [planet4589.org/space/gcat](https://planet4589.org/space/gcat/) | `tsv/launch/launch.tsv` + `tsv/tables/orgs.tsv` (tab-separated; line 2 a "# Updated" comment; orbital = `LaunchCode` starting `O` or `D`; state via `Agency` → `orgs.Code` → `StateCode`) | 1942 – last week | free | 11 (optional) |

---

## Traps, source by source

| Dataset | The trap |
|---|---|
| **GPR** | Revised monthly; vintages exist (`data_gpr_export_YYYYMM.xls`). Country indices are the anglophone press's attention to a country, not that country's risk. |
| **WDI** | Aggregates ("World", "High income", "G7" is *not* provided — build it) sit in the same file as countries. Current-dollar shares move with exchange rates. |
| **NMC** | Uses COW country codes, not ISO; states enter and exit the system (`GMY` absent 1946–1990, when `GFR`/`GDR` cover 1955/1954–1990). Missing components are coded `-9`. Yearly CINC sums run 1.000–1.075, not exactly 1. Ends in 2022. |
| **SIPRI** | Several sheets (`Constant (2024) US$`, `Current US$`, `Share of GDP`, `Per capita`, `Share of Govt. spending`, local-currency and `Regional totals`); `...` = data unavailable, `xxx` = the state did not exist — notes atop each sheet, plus a `Footnotes` sheet. Country strings: `United States of America`; `Russia` from 1992, `USSR` before. |
| **UNGA ideal points** | Carries both COW `ccode` and ISO `iso3c`; estimated by calendar year since the July 2025 releases (v36/37; current v39, 30 July 2026) — earlier versions by session, so the variable meaning changed between versions. Higher = closer to the US. |
| **IMF IMTS** | Exports reported by A ≠ imports reported by B ("mirror" asymmetry). Choose one side and say which. |
| **UNSC members** | Two-year terms starting 1 January; election happens the October before — the paper's "election year" matters. |
| **US aid** | Obligations vs disbursements; current vs constant dollars; the official site moved in 2025. |
| **ISO Survey** | Coverage of certification bodies changed over time: jumps in a country's count can be reporting, not adoption. |
| **Firm-level risk** | Listed firms holding earnings calls in English — mostly US. Stops in 2021. |
| **DCID** | State-to-state rivals only; `StateA`/`StateB` are the dyad as **names**, not initiator and target — derive the target from `initiator` (COW code) and `Dyadpair`; coded from open sources — attribution is by definition uncertain. |
| **EuRepoC** | Much wider than DCID (includes criminal and non-state); filter on `initiator_category` (`State` / `State affiliated actor`) before comparing. |
| **Lowy GDI** | 66 countries or territories only (including Taiwan and the EU's EEAS); names, not codes, with typos (`Portual`, `Nigaragua`); counts posts, not staff or budget. |
| **GSDB** | Licence forbids redistribution: workbooks go to ZoneCours, never Tableau Public with the raw data. "Success" is the coders' judgement of objectives met. |
| **TIES** | Includes **threats** of sanctions — a case may never have been imposed. |
| **POLCON / WGI** | WGI's 2025 edition changed scale and recalculated history: never mix editions. |
| **SATCAT** | Debris carries its parent's `LAUNCH_DATE` (Fengyun-1C debris is dated 1999, not 2007); `OWNER` is not the operator (Starlink `US`, Galileo `ESA`, Russia `CIS`); filter `ORBIT_CENTER` = `EA`; a blank status is not "inactive"; one download per team. |
| **GCAT** | The state is the launch provider's, not the customer's (Rocket Lab = New Zealand); vague-date text, padded values. |
| **UCS Satellite Database** | Frozen: data current through 1 May 2023. Use SATCAT for anything later. |

---

## Country codes

Join on **ISO 3166 alpha-3** codes, never on names. NMC and DCID (in `initiator` and `Dyadpair`) use
**Correlates of War** codes ([official list](https://correlatesofwar.org/wp-content/uploads/COW-country-codes.csv)): keep a concordance sheet (COW `ccode` ↔ ISO3) in your workbook. The
`countrycode` concordance tables published by Arel-Bundock et al. are the standard reference. The UNGA
ideal points carry `iso3c` too. Kosovo is `KOS` at the IMF and `XKX` at the World Bank; the West Bank and Gaza is `WBG` at the IMF.
