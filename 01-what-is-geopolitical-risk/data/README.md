# Session 01 — Data

Nothing in this folder is committed except this file. Download at source, keep the file as it
arrived in `raw/`, and record it in your provenance log.

```text
01-what-is-geopolitical-risk/data/
├── raw/
│   └── data_gpr_export.xls      ← as downloaded, never edited
└── provenance-log.csv            ← one line per file (template: templates/provenance-log.csv)
```

## The source

| | |
|---|---|
| **Dataset** | Geopolitical Risk (GPR) Index — Caldara & Iacoviello |
| **Landing page** | <https://www.matteoiacoviello.com/gpr.htm> |
| **File** | The monthly export, `data_gpr_export.xls` (the page also offers a daily file; you do not need it today) |
| **Format** | Excel 97–2003 workbook, a single sheet (`Sheet1`), one row per month |
| **Coverage** | Recent index from January 1985; historical index from January 1900; updated monthly |
| **Access** | Free, no registration. Cite the AER article when you use it |

## The columns you need

Open the file in a spreadsheet first and read the header row. There is no notes tab: every column
is described in the **last two columns** of the sheet, `var_name` and `var_label`. The columns used in
Practice round 01 are:

| Column | Meaning |
|---|---|
| `month` | First day of the month |
| `GPR` | Recent GPR index, ten newspapers, 1985–today, average 1985–2019 = 100 |
| `GPRT` · `GPRA` | The **threats** and **acts** sub-indices of the recent index |
| `GPRH` | Historical GPR index, three US newspapers, 1900–today, average **1900–2019** = 100 |
| `GPRC_XXX` | Country-specific recent GPR for country `XXX` (ISO 3-letter code), e.g. `GPRC_CAN`, from 1985, 44 countries. **Not** an index to 100: it is the *percent of articles* (`GPRHC_XXX` is the historical version) |

> **Check before you trust.** Column names have changed between releases. If a name above is not
> in your file, find its equivalent in `var_name` / `var_label`, and write the change in your
> provenance log — that is your first "the data disagreed with the paper" entry.

## Download from the terminal (optional)

```bash
mkdir -p 01-what-is-geopolitical-risk/data/raw
curl -L -o 01-what-is-geopolitical-risk/data/raw/data_gpr_export.xls \
  "https://www.matteoiacoviello.com/gpr_files/data_gpr_export.xls"
```

If the direct link has moved, download from the landing page by hand — the landing page is the
canonical source, the direct link is a convenience.
