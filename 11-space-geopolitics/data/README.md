# Session 11 — Data

Nothing in this folder is committed except this file. Download at source, keep each file as it
arrived in `raw/`, and record it in your provenance log.

```text
11-space-geopolitics/data/
├── raw/
│   ├── satcat.csv          ← CelesTrak SATCAT, as downloaded — ONE download per team, never edited
│   ├── launch.tsv          ← optional: GCAT launch log (McDowell), as downloaded
│   └── orgs.tsv            ← optional: GCAT organisations table, to give each launch a state
└── provenance-log.csv      ← one line per file (template: templates/provenance-log.csv)
```

The report you replicate is not data: download *ESA's Annual Space Environment Report* (PDF) to
read, not to load into Tableau.

---

## 1 · CelesTrak SATCAT — the satellite catalogue

| | |
|---|---|
| **Producer** | CelesTrak (Dr T. S. Kelso), from the public catalogue of the US Space Force |
| **Landing page** | [celestrak.org/satcat](https://celestrak.org/satcat/) · format: [SATCAT Format Documentation](https://celestrak.org/satcat/satcat-format.php) · status codes: [SATCAT Operational Status](https://celestrak.org/satcat/status.php) · owner codes: [SATCAT Sources](https://celestrak.org/satcat/sources.php) |
| **File** | `satcat.csv` — one row per **catalogued object** ever (payloads, rocket bodies, debris), launched or decayed, from Sputnik's rocket body (catalogue number 1) onwards |
| **Size** | about 71,000 rows × 17 columns, 6.8 MB (71,073 rows when checked on 16 October 2026; last launch 2026-10-14) |
| **Updates** | by hand, "once or twice a day" (CelesTrak usage policy) — the file is a **snapshot**: log the `Last-Modified` date or your download date |
| **Access** | Free. **Usage policy:** download only once per update, only what you need. Thirty students fetching the same file from one campus address can be firewalled: **one person per team downloads it and shares it.** Any answer other than HTTP 200 (403, 404, 50x): stop and tell the instructor |

```bash
mkdir -p 11-space-geopolitics/data/raw
curl -L -o 11-space-geopolitics/data/raw/satcat.csv https://celestrak.org/pub/satcat.csv
```

**The columns.** Comma-separated (RFC 4180), header in the first row, dates in ISO format
(`1957-10-04`).

| Column | What it holds | Values you will meet |
|---|---|---|
| `OBJECT_NAME` | name; debris carries the parent's name + `DEB` | `FENGYUN 1C DEB`, `COSMOS 2251 DEB`, `IRIDIUM 33 DEB`, `COSMOS 1408 DEB`, `STARLINK-1007` |
| `OBJECT_ID` | international designator `YYYY-NNNAAA` (launch year, launch of the year, piece) | `1999-025A` — every piece of a launch shares `1999-025` |
| `NORAD_CAT_ID` | catalogue number, assigned in **order of cataloguing** | 1 … 101074 (six digits since July 2026) |
| `OBJECT_TYPE` | object type | `PAY` payload · `R/B` rocket body · `DEB` other debris · `UNK` unknown |
| `OPS_STATUS_CODE` | operational status | `+` operational · `-` nonoperational · `P` partially operational · `B` backup/standby · `S` spare · `X` extended mission · `D` decayed · `?` unknown · **blank** = no status (all debris and rocket bodies, and some payloads). CelesTrak counts as **active** any satellite coded `+`, `P`, `B`, `S` or `X` |
| `OWNER` | "source or ownership" — a **country, organisation or company code**, not the operator's nationality | `US`, `PRC` (China), `CIS` (former USSR **and** Russia, before and after 1991), `UK`, `JPN`, `IND`, `FR`, `ESA`, `TBD`… |
| `LAUNCH_DATE` | launch date | `YYYY-MM-DD`, never empty |
| `LAUNCH_SITE` | launch-site code | `AFETR` (Cape Canaveral), `AFWTR` (Vandenberg), `TYMSC` (Baikonur)… |
| `DECAY_DATE` | date of re-entry, if any | `YYYY-MM-DD`; **empty = still in space** (every row with a date has status `D`) |
| `PERIOD`, `INCLINATION`, `APOGEE`, `PERIGEE` | orbit, in minutes, degrees and kilometres | empty if no data |
| `RCS` | radar cross-section, m² | often empty |
| `DATA_STATUS_CODE` | element status | `NCE` no current elements · `NIE` no initial elements · `NEA` no elements available · blank |
| `ORBIT_CENTER` | what the object orbits | `EA` Earth · `MO` Moon · `SU` Sun · `MA` Mars · `EL1`, `EL2` Earth Lagrange points · … · a catalogue number = docked to that object (`25544` = the ISS) |
| `ORBIT_TYPE` | | `ORB` orbit · `LAN` landing · `IMP` impact (incl. re-entry) · `DOC` docked · `R/T` round trip |

> **The grain.** One row = one catalogued object, for its whole life. There is no "year" in the file:
> an object is **in orbit in year Y** if it was launched by Y and has not decayed by Y. Hence the
> practice round's construction: running sum of launches **minus** running sum of decays.

### Five traps

1. **Debris carries its parent's launch date.** The 3,531 `FENGYUN 1C DEB` pieces created by
   China's anti-satellite test of **11 January 2007** all have `LAUNCH_DATE` = `1999-05-10`, the
   date Fengyun-1C was launched; the debris of the 2009 Iridium 33 – Cosmos 2251 collision is dated
   1997 and 1993; the `COSMOS 1408 DEB` of Russia's 2021 test is dated 1982. Built on
   `LAUNCH_DATE`, the debris line moves in the wrong year. The file has no "date catalogued"
   column; `NORAD_CAT_ID` gives the **order** of cataloguing, not a date.
2. **"Not decayed" is not "in Earth orbit".** Some 300 objects that never decay orbit the Sun, the
   Moon, Mars or a Lagrange point. Filter `ORBIT_CENTER` = `EA` before you count objects around
   Earth.
3. **`OWNER` is not the operator.** Every Starlink is `US`; OneWeb (since 2023 part of the French
   Eutelsat group) is `UK`; Galileo, an EU programme, is `ESA`; Russia is still `CIS`. To see
   operators you must build them from `OBJECT_NAME`.
4. **Blank status is not "inactive".** Among payloads still in Earth orbit, about 1,400 have no
   status at all. Active = `+`, `P`, `B`, `S`, `X` — say so in your caption. Status describes
   **today** only: the file cannot tell you how many satellites were active in 2010.
5. **The public catalogue is not the environment.** It holds only what the US Space Force
   publishes: no classified objects, none of its "analyst" objects, nothing too small to track
   (roughly below 10 cm in low orbit). ESA adds the Russian Vimpel catalogue and objects asserted
   by design, so its totals are higher.

---

## 2 · GCAT launch log — optional, for the extension

| | |
|---|---|
| **Producer** | Jonathan C. McDowell, *General Catalog of Artificial Space Objects* (GCAT) |
| **Landing page** | [planet4589.org/space/gcat](https://planet4589.org/space/gcat/) · column definitions: [Launch List columns](https://planet4589.org/space/gcat/web/launch/lcols.html) |
| **Files** | `launch.tsv` (every launch since 1942, about 76,000 rows, 33 columns, 14 MB) and `orgs.tsv` (organisations, with a `StateCode`) |
| **Access** | Free; please cite McDowell and the GCAT release date |

```bash
curl -L -o 11-space-geopolitics/data/raw/launch.tsv https://planet4589.org/space/gcat/tsv/launch/launch.tsv
curl -L -o 11-space-geopolitics/data/raw/orgs.tsv   https://planet4589.org/space/gcat/tsv/tables/orgs.tsv
```

| Column | What it holds |
|---|---|
| `Launch_Tag` | launch identifier, e.g. `2007-001` (the header line starts with `#`: `#Launch_Tag`) |
| `Launch_Date` | **text** in McDowell's "vague date" format: `1957 Oct  4 1928`, sometimes with `?` — take the year with `LEFT([Launch_Date], 4)` |
| `LaunchCode` | first letter = launch category: `O` orbital, `D` deep space, `M` military missile, `S` suborbital, `T` test, `A` atmospheric… (plus `L` and `N`, added in 2026); second letter = outcome: `S` success, `F` failure, `U` unknown, `E` pad explosion |
| `Agency` | code of the **launch-service** organisation (several separated by `/`) → join to `orgs.tsv` on `Code` to get `StateCode` (`US`, `CN`, `RU`, `SU`, `F`, `J`, `IN`, `NZ`…) |

Traps: the **second line of each file** is a comment (`# Updated 2026 Oct 15 …`) that Tableau reads
as a data row — do not edit the file; filter out the row whose `#Launch_Tag` starts with `#`, and
copy the date into your log; values are padded with spaces (use `TRIM`); orbital launches are `O` **and** `D`, not only `O`; the state is the **launch provider's**,
not the customer's — Rocket Lab's Electron launches count as New Zealand's.

---

## 3 · Two sources you will be tempted by

- **UCS Satellite Database** (Union of Concerned Scientists) — the classic list of operational
  satellites with operator, users and purpose. **Frozen**: its page says it "has paused updates",
  data current through **1 May 2023**. Use it only for questions about 2023, and say so.
- **UNOOSA Online Index of Objects Launched into Outer Space** — what states have *registered*
  under the 1975 Registration Convention. It measures legal registration, not what is in orbit;
  registrations lag and some objects are never registered. A reading, not a dataset, today.

---

## Provenance-log lines to start from

```text
file,source,url,version_or_release,accessed,licence,notes
satcat.csv,CelesTrak (T.S. Kelso) / US Space Force public catalogue,https://celestrak.org/pub/satcat.csv,"snapshot; Last-Modified …; last LAUNCH_DATE …",2026-…,free (CelesTrak usage policy),"debris dated by parent launch; ORBIT_CENTER = EA kept"
launch.tsv,J.C. McDowell GCAT,https://planet4589.org/space/gcat/tsv/launch/launch.tsv,"# Updated … (line 2 of the file)",2026-…,free,"orbital = LaunchCode starting O or D"
orgs.tsv,J.C. McDowell GCAT,https://planet4589.org/space/gcat/tsv/tables/orgs.tsv,"# Updated …",2026-…,free,"StateCode = launch provider's state"
ESA Space Environment Report 2026,ESA Space Debris Office,https://www.sdo.esoc.esa.int/publications/Space_Environment_Report_I10R0_20260501.pdf,"Issue 10.0, 1 May 2026",2026-…,public,"the original: Fig. 2.1 / Table 3.1"
```
