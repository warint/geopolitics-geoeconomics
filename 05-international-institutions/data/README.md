# Session 05 — Data

Nothing in this folder is committed except this file. Download at source, keep files as they
arrived in `raw/`, and record each in your provenance log.

```text
05-international-institutions/data/
├── raw/
│   ├── kw2006_replication.*          ← route A: the authors' file, as downloaded
│   ├── us_foreign_aid_country.csv    ← route B: US aid, country × year (Country Summary)
│   └── unsc_elected_members.xlsx     ← route B: transcribed from the UN page (see below)
└── provenance-log.csv
```

There are **two routes**. Choose one as a team before class; route A is faster, route B teaches more.

---

## Route A — the replication file

| | |
|---|---|
| **Dataset** | Replication data for Kuziemko & Werker (2006) |
| **Landing page** | [AidData — replication datasets](https://www.aiddata.org/replication-datasets/how-much-is-a-seat-on-the-security-council-worth-foreign-aid-and-bribery-at-the-united-nations) → "Download Data" |
| **Format** | Unverified. "Download Data" is a Google Drive link; when checked (October 2026) it asked for a Google sign-in and did not return the file. If it does not open for you, take route B. If it does, note the format and the variable list in your log |
| **Coverage** | The paper's sample: developing countries, 1946–2001 |
| **Access** | Free |

Find in the variable list: a country identifier, a year, **US aid** (and its units — current or
constant dollars, levels or logs), and an indicator of **Security Council membership**. If the file
is in Stata format (`.dta`), Tableau Desktop opens it directly (*Connect → Statistical File*).

---

## Route B — collect the two pieces yourself

### 1. US foreign aid

| | |
|---|---|
| **Dataset** | ForeignAssistance.gov **Country Summary** (`us_foreign_aid_country.csv`) — obligations and disbursements by country, fiscal years from 1946 |
| **Official** | [foreignassistance.gov/data](https://foreignassistance.gov/data) → *Country Summary* → CSV. The site moved to the State Department in 2025 and has been unstable; when checked (October 2026) its download link was [this file](https://s3.amazonaws.com/files.explorer.devtechlab.com/us_foreign_aid_country.csv) (fiscal years 1946–2026) |
| **Mirror** | [foreignassistance.andrewheiss.com](https://foreignassistance.andrewheiss.com/) → *Country Summary* — a frozen copy (19 December 2024, fiscal years 1946–2024). Its CSV link was down when checked; the same file is in the mirror's full download, `data-raw_2025-02-03.zip` (115 MB) |
| **Columns** | `Country Code` (ISO alpha-3) · `Country Name` · `Region Name` · `Income Group Name` · `Transaction Type Name` · `Fiscal Year` · `current_amount` · `constant_amount` |
| **What you need** | Filter `Transaction Type Name` = **Obligations** → one row per country × fiscal year. Use `constant_amount` |
| **Access** | Free |

**Economic vs military.** The Country Summary does **not** split economic from military assistance:
its amounts are the total. Record that in your log. Teams that want economic aid only can use the
mirror's [Greenbook page](https://foreignassistance.andrewheiss.com/greenbook.html):
`us_foreignaid_greenbook.xlsx` (USAID, prepared 9 August 2022, fiscal years 1946–2020, constant 2020
dollars), with columns `Fiscal Year`, `Region`, `Country`, `Assistance Category` (*Economic* /
*Military*), `Publication Row`, `Funding Agency`, `Funding Account Name`, `Obligations (Historical Dollars)`,
`Obligations (Constant Dollars)`. But it has six title rows above the header (use *Data
Interpreter*), **no ISO code**, and one row per funding account — you must sum to country × year
before the event-time ratio.

If you use the mirror, write "mirror, frozen 2024-12-19" in the version column of your log. That is
your first disagreement-with-the-paper entry: the authors used an earlier release of the same series.
The constant-dollar base year changes between releases: the same country-year has different
`constant_amount` values in the 2024 mirror and the 2026 official file.

### 2. Elected members of the Security Council

| | |
|---|---|
| **Source** | United Nations, [Countries elected members of the Security Council](https://main.un.org/securitycouncil/en/content/countries-elected-members) |
| **Format** | A web page, listing each member state with the years it served |
| **Access** | Free |

Transcribe it into a sheet with **one row per term**:

| country | iso3 | term_start | term_end |
|---|---|---|---|
| Brazil | BRA | 1998 | 1999 |
| … | | | |

Split the work: each member of the team transcribes one alphabetical range. **Restrict to terms
starting 1970–2010** — 204 rows on the page as checked in October 2026. Then check for duplicates
and for countries whose name has changed (Zaire / Democratic Republic of the Congo, Yugoslavia, the two Yemens).

---

## Traps

- Terms run **1 January to 31 December of the following year**; the election is the October before.
  The paper's "year −1" is the election year.
- Before **1966** the Council had six elected members, not ten.
- Greenbook years are **US fiscal years** (October–September; July–June before 1977), not calendar
  years. `Fiscal Year` is text in the Country Summary because of `1976tq`, the 1976 transition
  quarter: drop it, then convert the field to a number.
- The aid file has regional rows (`World`, `Africa Region`, … every name ending in "Region") and
  former states with non-ISO codes (`YUF` Yugoslavia, `SCG` Serbia and Montenegro, `SDF` Sudan)
  or no code at all (`Yemen (former P.D.R.)`).
- Aid is lumpy: a single large programme can dominate a country's series. That is why the paper
  works with logs, and why the practice uses a **ratio to the country's own pre-term baseline**.
