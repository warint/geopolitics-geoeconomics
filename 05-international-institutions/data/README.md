# Session 05 — Data

Nothing in this folder is committed except this file. Download at source, keep files as they
arrived in `raw/`, and record each in your provenance log.

```text
05-international-institutions/data/
├── raw/
│   ├── kw2006_replication.*          ← route A: the authors' file, as downloaded
│   ├── greenbook_country_summary.csv ← route B: US aid, country × year
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
| **Format** | Not verified at the time of writing — it is hosted on a file-sharing link. Open it, note the format and the variable list in your log |
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
| **Dataset** | *U.S. Overseas Loans and Grants* ("Greenbook"), country summary |
| **Official** | [foreignassistance.gov/data](https://foreignassistance.gov/data) — the Greenbook is under *Reports*. The site moved to the State Department in 2025 and has been unstable |
| **Mirror** | [foreignassistance.andrewheiss.com/greenbook.html](https://foreignassistance.andrewheiss.com/greenbook.html) — a frozen copy (December 2024) of the official CSVs |
| **What you need** | Country × fiscal year, **economic assistance**, obligations, in **constant** dollars if offered |
| **Coverage** | 1946 to the early 2020s |
| **Access** | Free |

If you use the mirror, write "mirror, frozen 2024-12-19" in the version column of your log. That is
your first disagreement-with-the-paper entry: the authors used an earlier release of the same series.

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
starting 1970–2010** — about two hundred rows. Then check for duplicates and for countries whose
name has changed (Zaire / Democratic Republic of the Congo, Yugoslavia, the two Yemens).

---

## Traps

- Terms run **1 January to 31 December of the following year**; the election is the October before.
  The paper's "year −1" is the election year.
- Before **1966** the Council had six elected members, not ten.
- Greenbook years are **US fiscal years** (October–September), not calendar years.
- Aid is lumpy: a single large programme can dominate a country's series. That is why the paper
  works with logs, and why the practice uses a **ratio to the country's own pre-term baseline**.
