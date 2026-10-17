# Session 07 — Pre-session preparation

> **Every geopolitical risk score a multinational buys or builds is a chain of choices: which texts,
> which words, which coder, which weights. Can you see the chain — and defend each link?**

> **[Open the pre-session slides](https://warint.github.io/geopolitics-geoeconomics/session-07-pre-session.html)** — or read the source at [`INTE60019A-S07-Pre-Session.qmd`](INTE60019A-S07-Pre-Session.qmd).

Four things to do before class. Budget **about two and a half hours**, and **revise Sessions 04–06**:
Quiz 2 opens the session.

| | Before class | Used in class for |
|---|---|---|
| **1** | Read the paper; skim two companions | the lecture and practice part (a) |
| **2** | Collect the data | practice parts (a) and (c) |
| **3** | Pull 40 headlines and **code them — two coders, independently** | practice part (b) |
| **4** | Self-check | the lecture |

---

## 1. The reading — 60–75 min

**The big work.** Hassan, T. A., Hollander, S., van Lent, L., & Tahoun, A. (2019). Firm-level
political risk: Measurement and effects. *Quarterly Journal of Economics*, 134(4), 2135–2202.
[doi:10.1093/qje/qjz021](https://doi.org/10.1093/qje/qjz021)

| | What to look for |
|---|---|
| **1** | The **question**: how much political risk does an individual firm face, and does it matter? |
| **2** | The **measurement**: what text, which word pairs, how are "political" bigrams identified, and how close to "risk" or "uncertainty" must they be? |
| **3** | The **validation**: what evidence shows that PRisk measures political risk and not something else? |
| **4** | The **finding** that surprised the authors most about where the variation lies — across time, sectors, or firms? |

Sections I–III closely; skim the rest.

**Skim, for the lecture:**

- Baker, S. R., Bloom, N., & Davis, S. J. (2016). Measuring economic policy uncertainty. *Quarterly
  Journal of Economics*, 131(4), 1593–1636. [doi:10.1093/qje/qjw024](https://doi.org/10.1093/qje/qjw024)
  — Section II: how the index is built, and how they audited it **by hand**.
- OECD/JRC (2008). *Handbook on Constructing Composite Indicators: Methodology and User Guide*. OECD
  Publishing. [doi:10.1787/9789264043466-en](https://doi.org/10.1787/9789264043466-en) — the
  ten-step checklist at the start of Part 1.

---

## 2. The data — 30 min

Details: [`../data/README.md`](../data/README.md). Split the work.

- `firmquarter_2022q1.csv` from firmlevelrisk.com
- `Global_Policy_Uncertainty_Data.xlsx` and `All_Country_Data.xlsx` from policyuncertainty.com
- `data_gpr_export.xls` again (revised since Session 01) and the **WGI** 2025 edition
- Your Session 04 ideal-point file

---

## 3. Your corpus, and coding it — 45 min

**One member** retrieves the headlines (GDELT query in [`../data/README.md`](../data/README.md)),
draws **40 at random**, and shares the coding sheet. **Two other members** code all 40 —
**independently, without talking to each other** — using the protocol below. The fourth member (or
the first, in a team of three) is the **adjudicator** in class.

### The coding protocol

Code the **headline only**. Assign **one** code: the category that best describes the headline's
main event. Categories follow Caldara and Iacoviello's eight, plus a zero.

| Code | Category | Assign when the headline reports… |
|---|---|---|
| **0** | Not geopolitical | anything else — domestic politics, markets, company news, disasters |
| **1** | War threats | a threat or risk of war between states |
| **2** | Peace threats | a threat to a peace process, ceasefire or agreement |
| **3** | Military build-ups | troop movements, exercises, arms build-ups, new deployments |
| **4** | Nuclear threats | nuclear tests, weapons programmes, nuclear threats |
| **5** | Terror threats | a threat or risk of a terrorist attack |
| **6** | Beginning of war | the start of a war or armed conflict between states |
| **7** | Escalation of war | an existing war intensifying |
| **8** | Terror acts | a terrorist attack that happened |

**Decision rules.**

1. **Acts beat threats**: if a headline reports both, code the act (6, 7 or 8).
2. **Sanctions, export controls and trade wars** are *not* in the eight categories: code **0**, and
   write `econ` in a comment column. (That gap is one of today's discussion points.)
3. **When in doubt, code 0** and write why in the comment column.
4. **Never revise** your code after seeing your partner's.

---

## 4. Self-check — 15 min

1. Name the three components of the EPU index's article filter.
2. Why do Hassan et al. look for political bigrams **near** words like "risk" and "uncertainty",
   rather than counting political words alone?
3. Two coders agree on 80% of items. Why might that still be poor agreement?
4. Name the steps in building a composite indicator. Which one do you think is most often skipped?

---

## Arrive with

- [ ] Sessions 04–06 revised — **Quiz 2**
- [ ] The paper read; the two companions skimmed
- [ ] All files in `data/raw/`, logged
- [ ] `coded/coding_sheet.xlsx` with **two independent codings** of 40 headlines
- [ ] Your self-check, on paper

---

[Session 07 overview](../README.md) · [The lecture](../01-lecture/README.md) ·
[The practice](../02-practice/README.md)
