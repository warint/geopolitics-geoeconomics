# Session 08 — Data

Nothing in this folder is committed except this file. Download at source, keep each file as it
arrived in `raw/`, and record it in your provenance log.

```text
08-cyber-geopolitics/data/
├── raw/
│   ├── Master_DCID_2.0_Release_public_Sep2022.csv   ← DCID v2.0, exported as CSV from Dataverse
│   ├── eurepoc_global_dataset_1_3.csv                ← EuRepoC v1.3
│   └── (codebooks of both, as PDF/TXT)
└── provenance-log.csv
```

## Source 1 — DCID v2.0 (the replication)

| | |
|---|---|
| **Dataset** | Dyadic Cyber Incident and Campaign Data (DCID), version 2.0 — Maness, Valeriano, Hedgecock, Macias & Jensen |
| **Landing page** | Harvard Dataverse, [doi:10.7910/DVN/CQOMYV](https://doi.org/10.7910/DVN/CQOMYV) |
| **File** | `Master_DCID_2.0_Release_public_Sep2022.tab` — on Dataverse choose *Access File → Comma Separated Values* to download it as CSV |
| **Coverage** | 2000–2020 · 429 incidents between **rival states** · released September 2022 |
| **Access** | Free, no registration |

**The unit.** One row is one cyber **incident** between an initiating state and a target state,
nested in **campaigns**. Only pairs of states that are rivals enter the data.

**The columns you need.** Open the codebook first. You need the columns for: the initiating state,
the target state, the start date (or year), the **method** of the incident (the codebook
distinguishes vandalism, denial of service, network intrusion and network infiltration), the
**severity** score, and the **type of target** (government, private, military…). Column names
differ between releases — write the exact names you used in your provenance log.

## Source 2 — EuRepoC v1.3 (the comparison)

| | |
|---|---|
| **Dataset** | European Repository of Cyber Incidents — Global Dataset of Cyber Incidents, v1.3 |
| **Landing page** | [eurepoc.eu/database](https://eurepoc.eu/database/) · Zenodo [doi:10.5281/zenodo.14965395](https://doi.org/10.5281/zenodo.14965395) |
| **File** | `eurepoc_global_dataset_1_3.csv` and the codebook, from the Zenodo record |
| **Coverage** | 2000–2024 · 3,416 incidents · state **and non-state** initiators |
| **Access** | Free |

> **The trap.** EuRepoC is much wider than DCID: it includes criminal, hacktivist and unattributed
> incidents. Before you compare the two, filter EuRepoC to incidents attributed to **state**
> actors — and say in your log how you defined that.

## Not a download — CFR Cyber Operations Tracker

[cfr.org/cyber-operations](https://www.cfr.org/cyber-operations/) catalogues state-sponsored operations
since 2005 but offers no official file. Use it to **read** about the incidents you see in the
matrix, not as a dataset.
