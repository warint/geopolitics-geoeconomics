# Session 04 — Data

Nothing in this folder is committed except this file. Download at source, keep files as they
arrived in `raw/`, and record each in your provenance log.

```text
04-trade-conflict-and-fragmentation/data/
├── raw/
│   ├── IdealpointestimatesFP_2026FP.csv       ← UNGA ideal points, country-year
│   ├── Codebook_IdealPointEstimates1946-2025.txt
│   └── imf_imts_exports.csv                   ← your IMF extract (name it yourself)
└── provenance-log.csv
```

## Source 1 — UN General Assembly ideal points

| | |
|---|---|
| **Producer** | Erik Voeten (with Bailey & Strezhnev) |
| **Landing page** | Harvard Dataverse, [doi:10.7910/DVN/LEJUQZ](https://doi.org/10.7910/DVN/LEJUQZ) — "United Nations General Assembly Ideal Points" |
| **Files** | `IdealpointestimatesFP_2026FP.csv` (country-year ideal points) and the codebook `Codebook_IdealPointEstimates1946-2025.txt`. `AgreementScores.csv` and `IdealPointDyads1946-2025.tab` are useful for the *extend* step |
| **Version** | 39, released 30 July 2026. Estimates are **by calendar year** (since the July 2025 releases), where the legacy file `IdealpointestimatesAll_Jun2024.csv` used UNGA sessions. Log the version: the meaning of "year" changed. The file still carries a `session` column; `year` = `session` + 1945 |
| **Coverage** | 1946–2025 |
| **Access** | Free. Cite Bailey, Strezhnev & Voeten (2017), *Journal of Conflict Resolution*, 61(2), 430–456, [doi:10.1177/0022002715595700](https://doi.org/10.1177/0022002715595700), and the Dataverse record |

**Read the codebook.** Columns of `IdealpointestimatesFP_2026FP.csv` (checked October 2026): an
unnamed row-number column, `ccode` (COW numeric code), `session`, `NVotesFP`, `IdealPointFP` (the
ideal point, posterior mean), the quantiles `QO%FP`, `Q5%FP`, `Q10%FP`, `Q50%FP`, `Q90%FP`,
`Q95%FP`, `Q100%FP`, then `iso3c` (ISO 3-letter code), `Countryname` and `year`. One row per
country-year, 1946–2025 (193 countries in 2021). Sign convention: **higher = closer to the United
States** (USA 2.41, China −0.41 in 2021).

**What an ideal point is.** A one-dimensional position estimated from all UNGA roll-call votes,
designed to be **comparable over time**. It measures a state's alignment with the US-led liberal
order as revealed by its votes. It is not a measure of trade, alliance or friendship.

## Source 2 — IMF bilateral goods trade (IMTS)

| | |
|---|---|
| **Producer** | International Monetary Fund |
| **Landing page** | <https://data.imf.org/en/datasets/IMF.STA:IMTS> — "International Trade in Goods (by partner country)", formerly *Direction of Trade Statistics* (DOTS) |
| **What to select** | Indicator: **Exports of goods, Free on board (FOB), US dollar** (code `XG_FOB_USD`) · Frequency: **annual** · Countries: **all** · Counterpart countries: **all** · Years: **2015 to the latest** |
| **Format** | Download button → CSV (or Excel) |
| **Access** | Free |

The full matrix is large — about 240 reporters times 240 partners. Restrict the years before
downloading. What the dataset contains (checked October 2026 through the IMF SDMX API, which serves
the same dataset as the *Download* button):

- **Dimensions:** `COUNTRY` (the reporter — here the exporter), `INDICATOR`, `COUNTERPART_COUNTRY`
  (the partner), `FREQUENCY` (`A` = annual), `TIME_PERIOD` (the year), `OBS_VALUE` (the value).
- **Country codes are ISO 3-letter codes** (`USA`, `CHN`…), with IMF exceptions such as `KOS`
  (Kosovo) and `WBG` (West Bank and Gaza). Every country in the 2021 ideal-point file matches.
- **Aggregates are mixed in** with countries and must be removed: codes starting with `G` (`G001`
  World, `G110` Advanced Economies, `G998` European Union…) and `TX` (`TX126` Belgium-Luxembourg,
  `TX898` Countries & Areas not specified…).
- **Values are in US dollars** (USA → China, 2024: 143,545,739,507). The `SCALE` attribute (`6`)
  is a display hint for millions, not the unit of `OBS_VALUE`.

The column layout of the web *Download* CSV/Excel was not checked (it needs the browser): log what
you get, and map its columns onto the four dimensions above.

> **The mirror problem.** A's reported exports to B are not equal to B's reported imports from A
> (timing, valuation FOB/CIF, re-exports, confidentiality). Use **exporter-reported exports**
> throughout and say so. The *break* step compares with the mirror.

## Concordance

Both files carry ISO 3-letter codes (`iso3c` in the ideal points, `COUNTRY` / `COUNTERPART_COUNTRY`
in IMTS): relate on them. Only if your IMF download shows country names instead of codes, build a
two-column concordance sheet (name ↔ ISO3) and log where it came from — see
[`DATA-SOURCES.md`](../../DATA-SOURCES.md#country-codes).
