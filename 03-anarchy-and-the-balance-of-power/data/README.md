# Session 03 — Data

Nothing in this folder is committed except this file. Download at source, keep files as they
arrived in `raw/`, and record each in your provenance log.

```text
03-anarchy-and-the-balance-of-power/data/
├── raw/
│   ├── NMCv7.zip                              ← as downloaded
│   ├── NMCv7/                                 ← unzipped: csv, dta, codebook
│   └── SIPRI-Milex-data-1949-2025_v1.2.xlsx   ← as downloaded
└── provenance-log.csv
```

## Source 1 — National Material Capabilities (NMC) v7.0

| | |
|---|---|
| **Producer** | Correlates of War Project |
| **Landing page** | <https://correlatesofwar.org/data-sets/national-material-capabilities/> |
| **File** | `NMCv7.zip` — contains the data as csv (and Stata), plus the **codebook** (read it) |
| **Coverage** | 1816–2022, every member of the state system, one row per state-year |
| **Access** | Free. Required citation: Singer, J. D., Bremer, S., & Stuckey, J. (1972). Capability distribution, uncertainty, and major power war, 1820–1965. In B. Russett (Ed.), *Peace, war, and numbers* (pp. 19–48). Sage |

**The six components** of the Composite Index of National Capability (CINC):

| Dimension | Components |
|---|---|
| Demographic | total population · urban population |
| Industrial | iron and steel production · primary energy consumption |
| Military | military personnel · military expenditure |

In versions up to 6.0 the columns were `ccode`, `stateabb`, `year`, `milex`, `milper`, `irst`,
`pec`, `tpop`, `upop` and `cinc`. **Check the v7.0 codebook** for the exact names and units before
you build anything — and log any change.

**Codes.** NMC uses **Correlates of War** country codes (`ccode`, numeric; `stateabb`, three letters
that look like ISO but are not: Germany is `GMY`, China `CHN`, Russia `RUS`, the UK `UKG`, Japan
`JPN`, the US `USA`). Read the codebook's state list.

```bash
mkdir -p 03-anarchy-and-the-balance-of-power/data/raw && cd 03-anarchy-and-the-balance-of-power/data/raw
curl -L -o NMCv7.zip "https://correlatesofwar.org/wp-content/uploads/NMCv7.zip"
unzip -q NMCv7.zip -d NMCv7 && cd -
```

## Source 2 — SIPRI Military Expenditure Database

| | |
|---|---|
| **Producer** | Stockholm International Peace Research Institute |
| **Landing page** | <https://www.sipri.org/databases/milex> |
| **File** | `SIPRI-Milex-data-1949-2025_v1.2.xlsx` (revised April 2026) — the name changes with each release; take the latest |
| **Coverage** | 1949–2025; the world total from 1988 |
| **Access** | Free for non-commercial use |

The workbook has **several sheets** — expenditure in constant US dollars, current US dollars, share
of GDP, per capita, share of government spending. Each sheet has a few rows of notes above the
table, and uses special symbols for missing and uncertain values (read the notes sheet). Use the
**constant US dollar** sheet for the practice.

## Source 3 — GDP

Reuse your Session 02 WDI extract (`NY.GDP.MKTP.CD` and `NY.GDP.MKTP.PP.CD`) for `USA`, `CHN`,
`RUS`, `DEU`, `JPN`, `GBR`, `IND`, `FRA`, and `WLD`. Log it again: same file, new use.
