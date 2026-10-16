# Session 10 — Data

Nothing in this folder is committed except this file — and for the GSDB, that is a **licence
obligation**, not only a course rule.

```text
10-economic-sanctions/data/
├── raw/
│   ├── GSDB_R5_…            ← as received by e-mail, never edited
│   ├── TIES_…xls            ← TIES v4.0 case file, as downloaded
│   └── (both codebooks / user manuals)
├── years.csv                 ← a scaffold you make: one column `Year`, 1945 to 2025
└── provenance-log.csv
```

## Source 1 — Global Sanctions Data Base, Release 5

| | |
|---|---|
| **Producer** | Felbermayr, Kirilakha, Syropoulos, Yalcin & Yotov — [globalsanctionsdatabase.com](https://globalsanctionsdatabase.com/) |
| **How** | **Request form** on the site; files sent by e-mail, usually within about 24 hours. Requested after Session 08. |
| **Coverage** | 1,794 cases, 1949–2025 (the site's own pages differ by a year on the start — note which you rely on) |
| **Versions** | A **case-level** file (one row per sanction case) and a **dyadic** file; also a separate financial-sanctions extension (GSDB-FS) |
| **Licence** | Free for academic use; **no redistribution, no commercial use** |

**The variables you need.** Read the codebook before opening Tableau. You need, for each case: the
sanctioning and sanctioned state(s), the **start** and **end** years (end empty if ongoing), the
**type** of sanction — the GSDB distinguishes trade, financial, travel, arms, military assistance
and other sanctions, typically as one indicator column per type — the **objective(s)**, and the
**outcome** (the GSDB codes success, partial success, negotiated settlement, failure and ongoing
cases). Exact column names and codes differ between releases: copy them from the codebook into your
provenance log, and do not trust this paragraph over the codebook.

## Source 2 — TIES, Threat and Imposition of Economic Sanctions, v4.0

| | |
|---|---|
| **Producer** | Morgan, Bapat & Kobayashi — [sanctions.web.unc.edu](https://sanctions.web.unc.edu/) |
| **File** | The case-level Excel file and the user manual |
| **Coverage** | 1945–2005 |
| **Access** | Free |
| **Citation** | Morgan, T. C., Bapat, N., & Kobayashi, Y. (2014). Threat and imposition of economic sanctions 1945–2005: Updating the TIES dataset. *Conflict Management and Peace Science*, 31(5), 541–558. [doi:10.1177/0738894213520379](https://doi.org/10.1177/0738894213520379) |

> **The trap.** TIES records **threats** as well as impositions: many of its cases were never
> imposed. Find in the manual the variable that tells them apart before you count anything.

## The year scaffold

Make `years.csv` in a spreadsheet: a header `Year` and one row per year, 1945 to 2025. It lets
Tableau turn an episode (start, end) into one row per year in which the case was active.
