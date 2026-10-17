# Session 08 — Data

Nothing in this folder is committed except this file. Download at source, keep each file as it
arrived in `raw/`, and record it in your provenance log.

```text
08-cyber-geopolitics/data/
├── raw/
│   ├── Master_DCID_2.0_Release_public_Sep2022.csv   ← DCID v2.0, original CSV from Dataverse
│   ├── eurepoc_global_dataset_1_3.csv                ← EuRepoC v1.3
│   └── (codebooks of both, as PDF)
└── provenance-log.csv
```

## Source 1 — DCID v2.0 (the replication)

| | |
|---|---|
| **Dataset** | Dyadic Cyber Incident and Campaign Data (DCID), version 2.0 — Maness, Valeriano, Hedgecock, Macias & Jensen |
| **Landing page** | Harvard Dataverse, [doi:10.7910/DVN/CQOMYV](https://doi.org/10.7910/DVN/CQOMYV) |
| **File** | `Master_DCID_2.0_Release_public_Sep2022.tab` — on Dataverse choose *Access File → Comma Separated Values (Original File Format)*; you get `Master_DCID_2.0_Release_public_Sep2022.csv` |
| **Codebook** | Not on Dataverse. *Codebook 2.0* (PDF, July 2022) is on the authors' site, [ryanmaness.com/cyber-conflict-dataset](https://www.ryanmaness.com/cyber-conflict-dataset) |
| **Coverage** | 433 rows (one per incident) between **rival states** · start dates September 2000 – January 2021 · released September 2022 (the authors' site also has a 429-row "June" sheet and a February 2023 update — use the Dataverse file) |
| **Access** | Free, no registration · CC0 |

**The unit.** One row is one cyber **incident** between an initiating state and a target state,
nested in **campaigns**. Only pairs of states that are rivals enter the data.

**The columns you need** (checked against the September 2022 file and *Codebook 2.0*; write the
exact names you used in your provenance log — they differ between releases):

| Column | What it holds |
|---|---|
| `StateA`, `StateB` | The two states of the dyad, **as names** (`US`, `China`, `N Korea`, `S Korea`…), State A having the lower COW code. They are **not** initiator and target. A few names carry a trailing space (`Russia `) — wrap them in `TRIM()` |
| `Dyadpair` | The two COW codes run together: `2365` = US (2) + Russia (365) |
| `initiator` | The initiating state, as a **COW code** (2 US, 365 Russia, 710 China, 630 Iran, 731 North Korea…). There is **no target column**: the target is the other state of the dyad |
| `interactionstartdate`, `interactionenddate` | Dates as text, month/day/year (`2/1/2008`) |
| `method` | 1 vandalism · 2 denial of service · 3 network intrusion · 4 network infiltration — with decimals for infiltrations (4.1 logic bomb, 4.2 virus, 4.3 worm, 4.4 keystroke logging); the file also holds 3.1 |
| `severity` | 0–10 scale in the codebook; the file uses 0–6 |
| `targettype` | 1 private / non-state · 2 government non-military · 3 government military |
| `cyber_objective` | 1 disruption · 2 short-term espionage · 3 long-term espionage · 4 degrade |

Also in the file: `Cyberincidentnum` (incident ID), `Name`, `damage type`, `Crit Inf`, `Supply Ch`,
`Ransomware`, `Political Objective`, and source URLs.

## Source 2 — EuRepoC v1.3 (the comparison)

| | |
|---|---|
| **Dataset** | European Repository of Cyber Incidents — Global Dataset of Cyber Incidents, v1.3 |
| **Landing page** | [eurepoc.eu/database](https://eurepoc.eu/database/) · Zenodo [doi:10.5281/zenodo.14965395](https://doi.org/10.5281/zenodo.14965395) |
| **File** | `eurepoc_global_dataset_1_3.csv` and the codebook `eurepoc_codebook_1_2.pdf`, from the Zenodo record (scroll down: Zenodo previews only the attribution dataset) |
| **Coverage** | Start dates 2000–2024 · 3,414 rows, one per incident (the record's text says 3,416) · state **and non-state** initiators · release 1.3.2, extracted 4 March 2025 |
| **Access** | Free · CC BY-NC 4.0 |

**Columns you will use:** `incident_id`, `start_date` (text, day.month.year: `01.01.2023` — use
`DATEPARSE("dd.MM.yyyy", [start_date])`; "Not available" for 92 rows), `incident_type`,
`initiator_country`, `initiator_category`, `receiver_country`, `receiver_category`. Cells with
several values are separated by semicolons (`State;State`).

> **The trap.** EuRepoC is much wider than DCID: it includes criminal, hacktivist and unattributed
> incidents. Before you compare the two, filter EuRepoC to incidents attributed to **state**
> actors — and say in your log how you defined that. The field is `initiator_category`; its values
> include `State`, `State affiliated actor`, `Non-state-group`, `Individual hacker(s)`, `Unknown`
> and `Not attributed`. Do not test `CONTAINS([initiator_category], "State")`: Tableau may ignore case
> and catch `Non-state-group`. State or state-affiliated —
> `CONTAINS([initiator_category], "State affiliated") OR CONTAINS(";" + [initiator_category] + ";", ";State;")`
> — keeps 1,014 incidents; `State` alone, 329.

## Not a download — CFR Cyber Operations Tracker

[cfr.org/cyber-operations](https://www.cfr.org/cyber-operations/) catalogues state-sponsored operations
since 2005 but offers no official file. Use it to **read** about the incidents you see in the
matrix, not as a dataset.
