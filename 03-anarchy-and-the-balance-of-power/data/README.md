# Session 03 — Data

Nothing in this folder is committed except this file. Download at source, keep files as they
arrived in `raw/`, and record each in your provenance log.

```text
03-anarchy-and-the-balance-of-power/data/
├── raw/
│   ├── NMCv7.zip                              ← as downloaded
│   ├── NMCv7/NMCv7/                           ← unzipped: codebook PDF + two inner zips
│   ├── NMC-70-abridged.csv                    ← from NMC-v7-abridged.zip: the file you use
│   └── SIPRI-Milex-data-1949-2025_v1.2.xlsx   ← as downloaded
└── provenance-log.csv
```

## Source 1 — National Material Capabilities (NMC) v7.0

| | |
|---|---|
| **Producer** | Correlates of War Project |
| **Landing page** | <https://correlatesofwar.org/data-sets/national-material-capabilities/> |
| **File** | `NMCv7.zip` — contains a folder `NMCv7/` with the **codebook** `NMC_Documentation_v7.pdf` (dated 20 February 2026 — read it) and two more zips: `NMC-v7-abridged.zip` (`NMC-70-abridged.csv`, `.txt`, `.dta` — the one you use) and `NMC-v7-supplemental.zip` (the same plus source, note and quality-code columns) |
| **Coverage** | 1816–2022, every member of the state system, one row per state-year |
| **Access** | Free. Required citation: Singer, J. D., Bremer, S., & Stuckey, J. (1972). Capability distribution, uncertainty, and major power war, 1820–1965. In B. Russett (Ed.), *Peace, war, and numbers* (pp. 19–48). Sage |

**The six components** of the Composite Index of National Capability (CINC):

| Dimension | Components |
|---|---|
| Demographic | total population · urban population |
| Industrial | iron and steel production · primary energy consumption |
| Military | military personnel · military expenditure |

The v7.0 csv (`NMC-70-abridged.csv`, 17,121 state-years, checked October 2026) has the same 11
columns as v6.0, in this order: `stateabb`, `ccode`, `year`, `milex`, `milper`, `irst`, `pec`,
`tpop`, `upop`, `cinc`, `version` (`version` = `2025`). Units, from the codebook: `milex` in
thousands of current British pounds for 1816–1913 and thousands of current US dollars from 1914;
`milper` thousands of personnel; `irst` thousands of tons; `pec` thousands of coal-ton equivalents;
`tpop` and `upop` thousands. **Missing values are coded `-9`**, not left blank — `cinc` has none, but
the six components do. Read the codebook anyway, for the definitions.

CINC averages a state's shares over the components it **has**, so the yearly sum of `cinc` over all
states is not exactly 1: in v7.0 it runs from 1.000 to about 1.075, highest in the nineteenth
century.

**Codes.** NMC uses **Correlates of War** country codes (`ccode`, numeric; `stateabb`, three letters
that look like ISO but are not: Germany is `GMY`, China `CHN`, Russia `RUS`, the UK `UKG`, Japan
`JPN`, the US `USA`, France `FRN`, Italy `ITA`). The codebook has no state list: it is a separate
file, [`COW-country-codes.csv`](https://correlatesofwar.org/wp-content/uploads/COW-country-codes.csv)
(columns `StateAbb`, `CCode`, `StateNme`). Watch the series breaks: `GMY` stops in 1945 and returns
in 1991, with West and East Germany as `GFR` (260) and `GDR` (265) in between; the USSR is coded
`RUS` (365), continuous 1816–2022; `JPN` and `CHN` enter in 1860, and `JPN` is absent 1946–1951.

```bash
mkdir -p 03-anarchy-and-the-balance-of-power/data/raw && cd 03-anarchy-and-the-balance-of-power/data/raw
curl -L -o NMCv7.zip "https://correlatesofwar.org/wp-content/uploads/NMCv7.zip"
unzip -q NMCv7.zip -d NMCv7                         # → NMCv7/NMCv7/ (ignore __MACOSX/)
unzip -q NMCv7/NMCv7/NMC-v7-abridged.zip -d .        # → NMC-70-abridged.csv (.txt, .dta)
cd -
```

## Source 2 — SIPRI Military Expenditure Database

| | |
|---|---|
| **Producer** | Stockholm International Peace Research Institute |
| **Landing page** | <https://www.sipri.org/databases/milex> |
| **File** | `SIPRI-Milex-data-1949-2025_v1.2.xlsx` (revised 27 April 2026) — the name changes with each release; take the latest |
| **Coverage** | 1949–2025; the world total from 1988 |
| **Access** | Free for non-commercial use |

The workbook has **several sheets** — `Regional totals`, two local-currency sheets, `Constant (2024)
US$`, `Current US$`, `Share of GDP`, `Per capita`, `Share of Govt. spending`, and `Footnotes`
(the special-note symbols such as † and §). Use the **`Constant (2024) US$`** sheet for the
practice: US$ millions at constant 2024 prices and exchange rates. Its first five rows are notes;
the header is row 6 — `Country`, an unnamed column, `Notes`, then one column per year `1949` …
`2025`. Region and sub-region headings (`Africa`, `North Africa`, …) sit between the countries as
rows with no values. Missing values are text: `...` (data unavailable) and `xxx` (country did not
exist or was not independent); blue figures are SIPRI estimates and red ones highly uncertain — colour
that Tableau will not see. Countries are named, not coded: in v1.2 they are `China`, `United States
of America` and `Russia`, with the Soviet Union on a separate `USSR` row (in the constant-dollar sheet: values for 1988–1990
only; `Russia` starts in 1992).

## Source 3 — GDP

Reuse your Session 02 WDI extract (`NY.GDP.MKTP.CD` and `NY.GDP.MKTP.PP.CD`) for `USA`, `CHN`,
`RUS`, `DEU`, `JPN`, `GBR`, `IND`, `FRA`, and `WLD`. Log it again: same file, new use.
