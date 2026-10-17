# Session 10 — Data

Nothing in this folder is committed except this file — and for the GSDB, that is a **licence
obligation**, not only a course rule.

```text
10-economic-sanctions/data/
├── raw/
│   ├── GSDB_R5_…            ← as received by e-mail, never edited
│   ├── TIESv4-1.xls         ← TIES v4.0 case file, as downloaded (sheet `TIESv4.1.raw`)
│   └── (both codebooks / user manuals)
├── years.csv                 ← a scaffold you make: one column `Year`, 1945 to 2025
└── provenance-log.csv
```

## Source 1 — Global Sanctions Data Base, Release 5

| | |
|---|---|
| **Producer** | Felbermayr, Kirilakha, Syropoulos, Yalcin & Yotov — [globalsanctionsdatabase.com](https://globalsanctionsdatabase.com/) |
| **How** | **Request form** on the site; files sent by e-mail, usually within about 24 hours. Requested after Session 08. |
| **Coverage** | 1,794 cases; earliest `begin_year` 1949, latest 2025 (the site's home page says 1950–2025, its *Data* page 1949–2025 — note which you rely on) |
| **Versions** | A **case-level** file (one row per sanction case) and a **dyadic** file; also a separate financial-sanctions extension (GSDB-FS) |
| **Licence** | Free for academic use; **no redistribution, no commercial use** |

**The variables you need.** Read the codebook before opening Tableau. The Release 5 case-level file
(`GSDB-R5.csv`, 1,794 rows × 18 columns) has these columns:

| Concept | Column(s) | Format |
|---|---|---|
| Case identifier | `case_id` | integer, one row per case |
| Sanctioned / sanctioning state(s) | `sanctioned_state`, `sanctioning_state` | country **names**; several parties in one comma-separated string (e.g. `EU, Canada, …`) |
| Start, end | `begin_year`, `end_year` (also `begin_month`, `end_month`, new in R5) | years |
| Type | `trade`, `arms`, `military`, `financial`, `travel`, `other` | one 0/1 column per type; `descr_trade` details trade measures (export/import, partial/complete) |
| Objective(s) | `objective` | text codes, comma-separated if several: `policy_change`, `destab_regime`, `territorial_conflict`, `prevent_war`, `end_war`, `terrorism`, `human_rights`, `democracy`, `other` |
| Outcome | `success` | text codes, **one per objective, in the same order**: `success_total`, `success_part`, `nego_settlement`, `failed`, `ongoing` |
| Multilateral flags | `target_mult`, `sender_mult` | 0/1 |

Two traps. **(1)** The codebook says `end_year` is empty for ongoing cases, but in the distributed
file it is filled with **2025**: identify ongoing cases by `success` containing `ongoing`, not by an
empty end. **(2)** A case can name several targets, so filter a country with `CONTAINS`, not `=`.
These names were checked against the distributed R5 file as reported in a public analysis of it, not
against the codebook itself: confirm them in your codebook and copy them into your provenance log.

## Source 2 — TIES, Threat and Imposition of Economic Sanctions, v4.0

| | |
|---|---|
| **Producer** | Morgan, Bapat & Kobayashi — [sanctions.web.unc.edu](https://sanctions.web.unc.edu/) |
| **File** | `TIESv4-1.xls` (case-level, 1,412 cases × 66 columns) and `tiesusersmanualv4.pdf`, both linked from the home page |
| **Coverage** | 1945–2005 |
| **Access** | Free |
| **Citation** | Morgan, T. C., Bapat, N., & Kobayashi, Y. (2014). Threat and imposition of economic sanctions 1945–2005: Updating the TIES dataset. *Conflict Management and Peace Science*, 31(5), 541–558. [doi:10.1177/0738894213520379](https://doi.org/10.1177/0738894213520379) |

> **The trap.** TIES records **threats** as well as impositions: many of its cases were never
> imposed. The variable that tells them apart is `imposition` (1 = sanctions imposed, 0 = not
> imposed): 845 imposed, 567 threat-only. Other columns you need: `caseid`, `startyear`, `endyear`
> (empty for 451 cases), `sancimpositionstartyear`, `targetstate`, `sender1`…`sender5`,
> `primarysender`, `issue1`–`issue3`, `threat`, `finaloutcome` (codes 1–10, defined in the manual).
> States are **Correlates of War numeric codes** (2 = United States), not names: you need a COW
> country-code list to label them.

## The year scaffold

Make `years.csv` in a spreadsheet: a header `Year` and one row per year, 1945 to 2025. It lets
Tableau turn an episode (start, end) into one row per year in which the case was active.
