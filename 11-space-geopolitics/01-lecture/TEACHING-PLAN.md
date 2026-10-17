# Session 11 — Teaching plan (Risk Briefs 20 min + lecture 70 min)

# Space geopolitics: the orbital commons and the new space race

> **Instructor page.** The student-facing companion is [`README.md`](README.md); the deck is
> [`INTE60019A-S11-Lecture.qmd`](INTE60019A-S11-Lecture.qmd).

*Satellites now carry the position, timing, connectivity and imagery a multinational runs on. When
orbit is crowded, contested and dominated by one operator, who holds the risk?*

---

## Before the room fills

Check by e-mail the day before that **one person per team** has downloaded `satcat.csv`. CelesTrak's
usage policy asks for one download per update and warns that addresses ignoring error responses go
to its firewall: thirty students on the campus network fetching the same 6.8 MB file in the same
minute is exactly what it guards against. Bring your own copy on a USB key as a fallback — a copy
for in-class use only, not posted anywhere.

---

## Opening — the Risk Briefs (0–20)

Four briefs, four minutes each plus one question. Keep time strictly: stop at five minutes. After
the last brief, ask the room which of the four depended on a **satellite** somewhere — shipping,
aviation, payments, connectivity. Usually more than one did, without saying so. Use it as the bridge.

---

## Board plan

| Minutes | |
|---|---|
| **20–28** | **Infrastructure in orbit.** Ask: *"What did your firm use this morning that came from space?"* Collect: GPS on the trucks, the time stamp on a trade, the ship's connectivity, the crop forecast. Put the three services on the board with the four GNSS systems and their four states. |
| **28–40** | **The commons.** The five Treaty articles. Make the room find the gap in Article IV: conventional weapons and ASAT tests are not banned. Then Article VI: every private satellite has a state behind it — hold on to that for section 6. ITU first-come priority in one sentence. Kessler on the board: density → collisions → fragments → collisions. |
| **40–48** | **Astropolitics.** Three columns: Dolman (territory), Pekkanen (market; 95% dual-use), Bowen (infrastructure for war on Earth; the "cosmic coastline"). Ask which reading a satellite-service buyer should use. Answer: all three, at different horizons. |
| **48–58** | **Counterspace.** The five SWF categories; the four states that have destroyed a satellite from the ground. Then the punchline: only non-destructive means are used in today's wars — and they hit **customers**. KA-SAT, 24 February 2022; GNSS jamming and Tartu. |
| **58–70** | **The debris record.** ESA's method first (catalogued + asserted; three catalogues; DISCOS). Then Table 3.1: 44,964 objects, 16,946 payloads. Then the three events, with dates and altitudes. Ask: *"Where will Fengyun's debris show on a chart built from the public catalogue?"* Do not answer — the practice round does. |
| **70–82** | **One operator.** Starlink in Ukraine. Draw Farrell and Newman's hub: panopticon, chokepoint, the two conditions — and Article VI as the bridge from firm to state. IRIS², Qianfan, Guowang. Export controls: ITAR Category XV and EAR 9x515 in one minute. |
| **82–90** | **What the firm can do.** The five channels; the four watchlist lines with thresholds; the strategy table. Ask each team which line its firm would put on its dashboard. Hand over — the last practice round before Session 12. |

---

## Run Tableau live

Open `satcat.csv`, show the pivot of `LAUNCH_DATE` and `DECAY_DATE`, build `Change`, and put
`SUM([Change])` by `Year` on the screen **without** the running total: a jagged line of net
additions. Then *Quick Table Calculation → Running Total*: the stock appears. Then show the wrong
version — filter years from 1990 with a normal dimension filter — and watch the curve restart from
zero. That is the trap in step 3 of the practice round.

---

## What the students should find (SATCAT downloaded 16 October 2026; last launch 2026-10-14)

Instructor-only. Their numbers will differ by a few units with a later download.

**Objects in Earth orbit (`ORBIT_CENTER` = `EA`), end of year, by `LAUNCH_DATE`:**

| End of | PAY | R/B | DEB | UNK | Total |
|---|---|---|---|---|---|
| 1970 | 432 | 254 | 3,078 | 0 | 3,764 |
| 1990 | 1,884 | 1,235 | 9,088 | 0 | 12,207 |
| 2000 | 3,145 | 1,602 | 16,843 | 1 | 21,591 |
| 2006 | 3,455 | 1,670 | 17,320 | 1 | 22,446 |
| 2007 | 3,533 | 1,703 | 17,359 | 1 | 22,596 |
| 2009 | 3,710 | 1,772 | 16,858 | 1 | 22,341 |
| 2020 | 6,528 | 2,134 | 16,039 | 35 | 24,736 |
| 2021 | 8,123 | 2,164 | 15,834 | 69 | 26,190 |
| 2025 | **17,414** | **2,275** | **12,718** | **53** | **32,460** |
| on download | 20,149 | 2,297 | 12,543 | 55 | 35,044 |

Pivot check: 71,073 rows → 70,647 after the `EA` filter → 141,294 after the pivot → **106,250**
after removing null event dates (70,647 launches + 35,603 decays).

**The catch they should find.** Built on `LAUNCH_DATE`, the debris line shows **no step in 2007,
2009 or 2021** — 17,320 → 17,359 in 2007 — and instead jumps in 1999 (12,857 → 16,608), the year
Fengyun-1C was launched. Its 3,531 `FENGYUN 1C DEB` pieces (2,311 still in orbit) carry
`LAUNCH_DATE` 1999-05-10; Cosmos 2251 debris (1,714) is dated 1993, Iridium 33 debris (656) 1997,
Cosmos 1408 debris (1,806, of which 4 still in orbit) 1982. The debris line even **falls** after 2007
in this construction, which ESA's figure does not show.

**Re-dated to the event** (the `Appearance year` field of step 4), the steps appear:

| End of | DEB by launch date | DEB re-dated |
|---|---|---|
| 2006 | 17,320 | 9,613 |
| 2007 | 17,359 | **13,183** (+3,570) |
| 2008 | 16,913 | 12,737 |
| 2009 | 16,858 | **15,052** (+2,315) |
| 2020 | 16,039 | 14,234 |
| 2021 | 15,834 | **15,834** (+1,600) |

One `COSMOS 1408 DEB` piece decayed in 2017 — a fragment of an earlier event — and becomes a −1
before its re-dated +1; ignore it, or let a student find it.

A third method, for the strongest teams: `NORAD_CAT_ID` is assigned in cataloguing order, so the
running maximum of launch year in catalogue-number order approximates the year an object was
**catalogued**. It gives debris counts of 4,824 (2005), 7,594 (2007), 10,169 (2009), 13,158 (2020),
14,427 (2021), 12,672 (2025) — lower before 2007 than either other method, because much old debris
was only catalogued later.

**Against ESA (end of 2025, Table 3.1):** ESA 44,964 objects vs SATCAT 32,460; payloads 16,946 vs
17,414; rocket bodies 2,080 vs 2,275; ESA's debris classes (PF+PD+PM+RF+RD+RM) 14,851 vs SATCAT
`DEB` 12,718; ESA's **unidentified** 11,087 vs SATCAT `UNK` 53. The gap is ESA's extra catalogues
(Vimpel), asserted objects and objects it cannot trace to a source.

**Payloads launched per year and HHI by `OWNER`** (all payloads, all orbits):

| Year | US | CIS | PRC | Rest | Payloads | HHI |
|---|---|---|---|---|---|---|
| 1957 | 0 | 2 | 0 | 0 | 2 | 10,000 |
| 1965 | 90 | 64 | 0 | 4 | 158 | 4,888 |
| 1980 | 16 | 110 | 0 | 4 | 130 | 7,315 |
| 1990 | 39 | 96 | 5 | 26 | 166 | 3,937 |
| 2000 | 45 | 24 | 6 | 44 | 119 | 1,954 |
| **2008** | 18 | 21 | 15 | 49 | 103 | **1,111** (the minimum) |
| 2015 | 49 | 27 | 38 | 60 | 174 | 1,611 |
| 2019 | 256 | 31 | 70 | 96 | 453 | 3,503 |
| 2020 | 959 | 22 | 73 | 181 | 1,235 | 6,142 |
| 2025 | 3,703 | 59 | 369 | 361 | 4,492 | **6,870** |

The U-shape is the story: bipolar concentration, diffusion to a minimum in 2008, and a return
above Cold War levels — driven by one firm. Starlink's share of payloads launched: 26.5% (2019),
67.4% (2020), 70.5% (2025).

**Active satellites today** (`OPS_STATUS_CODE` in `+ P B S X`, `OBJECT_TYPE` = `PAY`, `ORBIT_CENTER`
= `EA`): **17,246**. By `OWNER`: US 75.5%, PRC 9.0%, UK 4.1%, CIS 2.2%; 99 owner codes; **HHI 5,803**
(numbers equivalent 1.7). By operator (Starlink, OneWeb, Kuiper, Qianfan, Guowang split out of their
owner codes): Starlink **11,152 = 64.7%**; HHI 4,325 — lower than by country, because splitting
Starlink from "US" spreads the shares. The point for the catch: a board's dependence is on the
**firm**, not on the flag.

**GNSS, active, for the extension:** GPS (`NAVSTAR`) 40, Galileo 33 (coded `ESA`), BeiDou 56,
GLONASS 29 (names `COSMOS … [GLONASS-M]`).

**GCAT extension:** orbital launch attempts (`LaunchCode` starting `O` or `D`) — 114 (2018), 186
(2022), 262 (2024), **330 (2025)**; by launch-provider state in 2025: US 181, China 93, Russia 17,
New Zealand 17 (Rocket Lab), France 7.

---

## Put this to the room

*"Your shipping subsidiary's only broadband at sea is one low-orbit constellation. Its operator's
government has just been asked by an ally to switch the service off over a strait your ships use.
What do you do this quarter?"*

Push for the distinction between **dependence on a service** and **dependence on a state**: a
second operator licensed by the same state is not diversification.

---

## Misconception to pre-empt

That the debris problem is the ASAT tests. They are the spectacular part; ESA's report says the
dominant source of debris is **fragmentations other than collisions** — old rocket stages and
batteries exploding — and that the long-term trend is driven by **traffic**. Say it in section 5,
and make the dating of debris the model catch of the practice.

---

## Last minutes of the practice round

There is no skeleton review today (that was Session 10). Walk the room during step 5 and check
that each team has decided **which** Session 11 view goes into its dashboard, and with which
threshold.
