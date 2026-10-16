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
| **Version** | 39, released July 2026 — **now estimated by calendar year**, where earlier versions used UNGA sessions. Log the version: the meaning of "year" changed |
| **Coverage** | 1946–2025 |
| **Access** | Free. Cite Bailey, Strezhnev & Voeten (2017), *Journal of Conflict Resolution*, 61(2), 430–456, [doi:10.1177/0022002715595700](https://doi.org/10.1177/0022002715595700), and the Dataverse record |

**Read the codebook** for the column holding the ideal point, the country identifiers (COW code and
ISO 3-letter code, if present), and the sign convention: which end of the scale the United States
sits on.

**What an ideal point is.** A one-dimensional position estimated from all UNGA roll-call votes,
designed to be **comparable over time**. It measures a state's alignment with the US-led liberal
order as revealed by its votes. It is not a measure of trade, alliance or friendship.

## Source 2 — IMF bilateral goods trade (IMTS)

| | |
|---|---|
| **Producer** | International Monetary Fund |
| **Landing page** | <https://data.imf.org/en/datasets/IMF.STA:IMTS> — "International Trade in Goods (by partner country)", formerly *Direction of Trade Statistics* (DOTS) |
| **What to select** | Indicator: **exports of goods, FOB, US dollars** · Frequency: **annual** · Countries: **all** · Counterpart countries: **all** · Years: **2015 to the latest** |
| **Format** | Download button → CSV (or Excel) |
| **Access** | Free |

The full matrix is large — roughly two hundred reporters times two hundred partners. Restrict the
years before downloading. Check how the extract identifies countries (ISO 3-letter codes, IMF
numeric codes or names) and whether aggregate partners ("World", "Advanced economies") are mixed in
with countries: you will need to remove them.

> **The mirror problem.** A's reported exports to B are not equal to B's reported imports from A
> (timing, valuation FOB/CIF, re-exports, confidentiality). Use **exporter-reported exports**
> throughout and say so. The *break* step compares with the mirror.

## Concordance

If the ideal-point file and the IMF extract do not share a code system, build a two-column
concordance sheet (COW code ↔ ISO3) and log where it came from — see
[`DATA-SOURCES.md`](../../DATA-SOURCES.md#country-codes).
