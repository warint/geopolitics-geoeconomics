# Session 01 — Pre-session preparation

> **Before we can manage geopolitical risk, what exactly are we counting?**

Slides: [`INTE60019A-S01-Pre-Session.qmd`](INTE60019A-S01-Pre-Session.qmd)

Three things to do before class. Budget **about two hours** — most of it is the reading. Start the
Tableau licence request **today**: approval can take several days.

| | Before class | Used in class for |
|---|---|---|
| **1** | Install Tableau Desktop and Tableau Prep Builder | every practice round, starting today |
| **2** | Read the paper | the lecture discussion and the replication |
| **3** | Download the GPR index | Practice round 01 |

---

## 1. Install Tableau — 20 min, plus waiting for the licence

1. Request the free academic licence through the **Tableau for Students** programme (Tableau
   Academic Programs) with your HEC e-mail address. You receive a product key by e-mail.
2. Install **Tableau Desktop** and, if your licence includes it, **Tableau Prep Builder**; activate with the key.
3. Create a free **Tableau Public** account — the team dashboard is published there.
   If the academic programme no longer offers you a licence, install the free **Tableau Public**
   desktop edition instead — see the fallback note in the toolkit.
4. Open Tableau Desktop, connect to *Sample – Superstore*, drag `Order Date` to Columns and `Sales`
   to Rows. If a line appears, you are ready.

Full instructions and troubleshooting: [`TABLEAU-TOOLKIT.md`](../../TABLEAU-TOOLKIT.md).

> If the key has not arrived by class, install the 14-day trial of Tableau Desktop. Do not arrive
> without a working installation: the practice round starts at minute 90.

---

## 2. The reading — 60–75 min

**Caldara, D., & Iacoviello, M. (2022). Measuring geopolitical risk. *American Economic Review*,
112(4), 1194–1225.** [doi:10.1257/aer.20191823](https://doi.org/10.1257/aer.20191823) · a free
working-paper version (Federal Reserve Board, *International Finance Discussion Papers* 1222) is
linked from the authors' page.

Read for the **argument**, not for coverage. Annotate four things:

| | What to look for |
|---|---|
| **1** | Their **definition** of geopolitical risk — copy it word for word |
| **2** | How the index is **built**: which newspapers, which words, which normalisation |
| **3** | The **strongest single piece of evidence** that the index measures something real |
| **4** | One **limitation** you would raise if you were the multinational's chief risk officer |

Skim Sections IV–V (the macroeconomic and firm-level effects). Read Sections I–III and Figure 1
closely: **Figure 1 is today's target figure**.

---

## 3. The data — 10 min

Download the monthly export from the authors' page and save it, untouched, in
`01-what-is-geopolitical-risk/data/raw/`. Details: [`../data/README.md`](../data/README.md).

Open it once in a spreadsheet and find: the first month of the recent index, the first month of the
historical index, and the column for **one country you care about**.

---

## 4. Self-check — 15 min

Answer on paper. If you cannot, that is what the lecture is for.

1. In one sentence: what is the difference between **risk** and **uncertainty**?
2. The GPR index is "text-based". Name one other kind of geopolitical risk indicator and one
   advantage it has over text.
3. GPR is normalised so that 1985–2019 averages 100. What does a reading of 300 in March 2022 mean,
   in words a manager would understand?
4. Name one geopolitical event that **mattered to a multinational firm** but that you suspect barely
   moved the GPR index. Why might it not have?

---

## Arrive with

- [ ] Tableau Desktop installed and activated (academic key, trial, or Tableau Public edition)
- [ ] A Tableau Public account
- [ ] The paper read and annotated, Figure 1 understood
- [ ] `data_gpr_export.xls` in `data/raw/`
- [ ] Your self-check answers, on paper

---

[Session 01 overview](../README.md) · [The lecture](../01-lecture/README.md) ·
[The practice](../02-practice/README.md)
