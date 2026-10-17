# Session 01 — Lecture notes (first half, 90 min)

# What is geopolitical risk?

> **[Open the lecture slides](https://warint.github.io/geopolitics-geoeconomics/session-01-lecture.html)** — or read the source at [`INTE60019A-S01-Lecture.qmd`](INTE60019A-S01-Lecture.qmd).
> As a book chapter: [course book, Session 01](https://warint.github.io/geopolitics-geoeconomics/book/session-01.html) · Instructor plan:
> [`TEACHING-PLAN.md`](TEACHING-PLAN.md)

---

## 1. The course in fifteen minutes

The syllabus is [`SYLLABUS.md`](../../SYLLABUS.md). Three things matter today:

- **The big theme.** How does a multinational firm know how much geopolitical risk it faces — and
  what should it do about it?
- **The rhythm.** Every session: a big article or book read before class; a lecture; a practice round
  in which you collect its data at source and rebuild its central figure in Tableau.
- **The grade.** 80% individual. Three quizzes (Sessions 04, 07, 10), one Risk Brief (Sessions
  02–11), a team dashboard for one multinational (Session 12), a 48-hour take-home.

---

## 2. Risk, uncertainty, and three kinds of risk

**Risk versus uncertainty.** Knight (1921) separated *risk* — outcomes whose probabilities can be
estimated — from *uncertainty*, where they cannot. Most geopolitical events sit uncomfortably
between the two: wars and coups recur, but each is unlike the last. Everything in this course is an
attempt to move a question from the second category towards the first, and to be honest about how
far it moves.

| | Question it answers | Typical unit | Example |
|---|---|---|---|
| **Political risk** | Can the government of the host country change the rules on *me*? | firm × host country | expropriation, contract renegotiation, sudden tax, licence withdrawal |
| **Country risk** | Will this country pay, convert and transfer? | country | sovereign default, capital controls, currency inconvertibility |
| **Geopolitical risk** | Will relations *between* states and political actors move against me? | the international system, or a dyad | war, sanctions, export controls, bloc formation, state-sponsored cyber operations |

Kobrin (1979) made the classic distinction between **macro** risk, which hits every foreign firm in a
country, and **micro** risk, which hits one sector or one firm. Geopolitical risk adds a third layer:
risk that originates *outside* the host country — in Washington, Beijing, Brussels or Moscow — and
reaches the firm through its suppliers, customers, banks or networks.

---

## 3. Six families of indicators

| Family | What it counts | Examples you will use | Strength | Blind spot |
|---|---|---|---|---|
| **Event-based** | Things that happened, coded from reports | UCDP, cyber-incident data (S08), sanctions episodes (S10) | Concrete, datable | Only what was reported and coded |
| **Text-based** | How much the press or firms talk about a risk | **GPR (today)**, EPU, firm-level political risk (S07) | Timely, long, high frequency | Measures attention, not exposure |
| **Expert-based** | Scores assigned by analysts or surveys | World Governance Indicators, commercial country-risk ratings | Covers latent concepts | Opaque, sticky, perception-driven |
| **Structural** | Slow-moving features of the system | Material capabilities (S03), trade dependence (S04, S11) | Explains *why* | Rarely tells you *when* |
| **Market-based** | Prices that embed risk | sovereign CDS spreads, implied volatility | Forward-looking, daily | Mixes risk with risk appetite |
| **Firm-level** | Risk as perceived by firms themselves | earnings-call text (S07), disclosed exposures | Speaks to the decision | Self-reported, listed firms only |

A good risk assessment — the team project — **triangulates** across at least three families. The
quarrel between them is informative: when the text says calm and the market says danger, someone
knows something.

---

## 4. The GPR index: how it is built

Caldara and Iacoviello (2022) define geopolitical risk as *the threat, realisation and escalation of
adverse events associated with wars, terrorism and any tensions among states and political actors
that affect the peaceful course of international relations.*

**The construction**, in four steps:

1. **Corpus.** The electronic archives of ten leading newspapers (US, UK and Canadian) for the recent
   index from 1985; three US newspapers for the historical index from 1900.
2. **Dictionary.** Articles are counted if they contain words from eight categories — war threats,
   peace threats, military build-ups, nuclear threats, terror threats, beginning of war, escalation of
   war, terror acts — usually in combination with words that pin the article to geopolitics.
3. **Share.** For each month, the number of GPR articles divided by the total number of articles.
   Dividing by the total removes the effect of newspapers growing or shrinking.
4. **Normalisation.** The share is rescaled so that the 1985–2019 average equals 100.

**Threats versus acts.** The first five categories form **GPR Threats**, the last three **GPR Acts**.
The distinction matters to a firm: the paper finds that threats, not only realised acts, depress
investment.

**Validation.** The authors audit samples of articles by hand, compare the index with historical
narrative, and show it spikes at the events it should — the World Wars, Korea, the Cuban missile
crisis, the Gulf War, 9/11, the 2003 invasion of Iraq, the 2022 Russian invasion of Ukraine.

**Country-specific indices.** For several dozen countries, the same counts are restricted to articles
that also mention the country — a measure of how much the *anglophone press* associates that country
with geopolitical tension.

---

## 5. Why a firm should care

**The real-options channel.** When an investment is costly to reverse and the future is uncertain,
waiting has value (Bernanke, 1983; Bloom, 2009). A GPR spike raises the value of waiting: firms
postpone hiring, capital expenditure and entry. Caldara and Iacoviello find that higher GPR predicts
lower investment and employment, and that the effect is stronger in industries more exposed to
geopolitical risk.

**Five channels from the system to the P&L**, which return all term:

| Channel | Example | Session |
|---|---|---|
| Market access | tariffs, bloc-based trade diversion | 04 |
| Inputs | a critical service from one satellite operator | 11 |
| Finance and payments | sanctions on banks, asset freezes | 10 |
| Assets and people | conflict, expropriation, evacuation | 03, 05 |
| Data and operations | state-sponsored cyber operations | 08 |

---

## 6. What GPR does not tell you

- It measures **attention in the anglophone press**, not the risk faced by a subsidiary in Abidjan
  or a supplier in Shenzhen.
- It is **global**: one number for the world. The country indices help, but only for countries the
  newspapers write about.
- **Attention fades** even while risk persists: a frozen conflict may be a constant risk and a falling
  index.
- It is **not a forecast**. It rises with an event; it does not tell you the next one.

That list is the template for "the catch" — the last step of every practice round.

---

## 7. The Tableau skill of the day

Connect to `data_gpr_export.xls` → check that `month` is a **date** → drag `month` to Columns as a
**continuous month** → `GPR` to Rows → add a **constant reference line** at 100 → **annotate** the
spikes. The step-by-step version is the practice brief: [`../02-practice/README.md`](../02-practice/README.md).

---

## References

Bernanke, B. S. (1983). Irreversibility, uncertainty, and cyclical investment. *Quarterly Journal of
Economics*, 98(1), 85–106.

Bloom, N. (2009). The impact of uncertainty shocks. *Econometrica*, 77(3), 623–685.

Caldara, D., & Iacoviello, M. (2022). Measuring geopolitical risk. *American Economic Review*,
112(4), 1194–1225.

Knight, F. H. (1921). *Risk, uncertainty and profit*. Houghton Mifflin.

Kobrin, S. J. (1979). Political risk: A review and reconsideration. *Journal of International
Business Studies*, 10(1), 67–80.
