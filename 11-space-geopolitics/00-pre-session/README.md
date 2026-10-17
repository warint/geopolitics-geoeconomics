# Session 11 — Pre-session preparation

> **Satellites now carry the position, timing, connectivity and imagery a multinational runs on.
> When orbit is crowded, contested and dominated by one operator, who holds the risk?**

Slides: [`INTE60019A-S11-Pre-Session.qmd`](INTE60019A-S11-Pre-Session.qmd)

Four things to do before class. Budget **about two hours**. **The download in step 3 is done once
per team, not once per student** — CelesTrak blocks addresses that download the same file too often.

| | Before class | Used in class for |
|---|---|---|
| **1** | Read the ESA report (selected pages) | the target figure |
| **2** | Read the SWF executive summary, Pekkanen and the Outer Space Treaty | the lecture discussion and the catch |
| **3** | One teammate downloads `satcat.csv` and shares it; everyone opens it | Practice round 11 |
| **4** | Self-check | the lecture |

---

## 1. The big work — 45 min

**ESA Space Debris Office. (2026). *ESA's annual space environment report* (Issue 10.0, 1 May 2026;
GEN-DB-LOG-00288-OPS-SD). European Space Agency.**
[PDF](https://www.sdo.esoc.esa.int/publications/Space_Environment_Report_I10R0_20260501.pdf) · free

Read the **executive summary** (pp. 3–11), **section 1.1–1.2** on definitions and data sources
(pp. 13–16), **section 2.1** (pp. 23–24) and **Table 3.1** (p. 63). Annotate four things:

| | What to look for |
|---|---|
| **1** | What counts as an **object** — catalogued, asserted, and the nine object classes (Table 1.1) |
| **2** | Where the data **come from** — which catalogues, and what is beyond the report's scope |
| **3** | The **strongest single piece of evidence** that the environment is getting worse |
| **4** | One **limitation** an insurer or a satellite-service buyer would raise |

Find **Figure 2.1** — *evolution of number of objects in geocentric orbit by object class* (the
same chart opens the executive summary as Figure 1). It is today's target. Mark where you expect
the 2007, 2009 and 2021 events to show.

---

## 2. The companion readings — 45 min

**Samson, V., & Brett, K. (Eds.). (2026). *Global counterspace capabilities: An open source
assessment*. Secure World Foundation.** — the **executive summary** only (24 pages; free on
[swfound.org](https://www.swfound.org/publications-and-reports/2026-global-counterspace-capabilities-report)).
Annotate: (a) the five categories of counterspace capability; (b) which of them are used in current
military operations; (c) one capability that would hit a commercial operator first.

**Pekkanen, S. M. (2019). Governing the new space race. *AJIL Unbound*, 113, 92–97.**
[doi:10.1017/aju.2019.16](https://doi.org/10.1017/aju.2019.16) · open access. Annotate her three
trends and the share of space technologies she calls dual-use.

**The Outer Space Treaty (1967)** — *Treaty on Principles Governing the Activities of States in the
Exploration and Use of Outer Space, including the Moon and Other Celestial Bodies*, on the
[UNOOSA site](https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/outerspacetreaty.html).
Read Articles I, II, IV, VI, VII and IX — two pages.

---

## 3. The data — 15 min

Details: [`../data/README.md`](../data/README.md).

1. **One teammate** downloads `satcat.csv` from [celestrak.org/pub/satcat.csv](https://celestrak.org/pub/satcat.csv)
   into `data/raw/` and shares it with the team. Note the date.
2. Everyone opens it in a spreadsheet. Find the rows whose `OBJECT_NAME` is `FENGYUN 1C DEB`. What
   is their `LAUNCH_DATE`? When did the event that created them happen? **Write down the gap: it is
   the first trap of the practice round.**
3. Optional, for the extension: GCAT's `launch.tsv` and `orgs.tsv`.

---

## 4. Self-check — 15 min

Answer on paper. If you cannot, that is what the lecture is for.

1. Which article of the Outer Space Treaty makes orbit a **commons**, and which one makes a state
   answer for a **private** company's satellites?
2. What is the **Kessler** mechanism, and why does it make one destructive ASAT test a problem for
   every operator in that orbit, not only for the target?
3. According to the SWF, are **destructive** or **non-destructive** counterspace capabilities being
   used in current wars? Why does that matter more to a firm than to a defence ministry?
4. One owner has 75% of active satellites, the next two 9% and 4%, and the rest is spread thinly
   over a hundred owners. Roughly what is the **HHI**? Is it "highly concentrated"?
5. Name one service your team's firm buys that would stop, or degrade, without a satellite.

---

## Arrive with

- [ ] ESA report annotated; Figure 2.1 located; the three events marked on it
- [ ] SWF executive summary, Pekkanen and the Treaty articles annotated
- [ ] `satcat.csv` in `data/raw/` (one download per team), the date noted
- [ ] The `FENGYUN 1C DEB` gap written down
- [ ] Provenance log started
- [ ] Your self-check answers, on paper

---

[Session 11 overview](../README.md) · [The lecture](../01-lecture/README.md) ·
[The practice](../02-practice/README.md)
