# Session 10 — Lecture notes (first half, 50 min)

# Economic sanctions

Slides: [`INTE60019A-S10-Lecture.qmd`](INTE60019A-S10-Lecture.qmd) · Instructor plan:
[`TEACHING-PLAN.md`](TEACHING-PLAN.md) ·
As a book chapter: [course book, Session 10](https://warint.github.io/geopolitics-geoeconomics/book/session-10.html)

The session opens with **Quiz 3** (20 min) and **four Risk Briefs** (20 min). The lecture is
therefore shorter today.

---

## 1. The instrument of first resort

Economic sanctions are restrictions on economic relations imposed by one or more **senders** on a
**target** — a state, a government, a firm or an individual — to change its behaviour, weaken it,
or signal disapproval. Their use has grown markedly since the end of the Cold War; the Global
Sanctions Data Base documents the rise and its changing composition.

| Dimension | Categories |
|---|---|
| **Sender** | unilateral (one state) · plurilateral (the EU, a coalition) · multilateral (the UN Security Council) |
| **Type** | trade · financial · travel · arms · military assistance · other — the GSDB's classification |
| **Scope** | **comprehensive** (a whole economy) vs **targeted** or "smart" (named persons, firms, sectors) |
| **Objective** | change a policy · destabilise a regime · end a war or a territorial conflict · prevent war · fight terrorism · human rights · democracy |

---

## 2. Do they work? The great debate

**Hufbauer, Schott, Elliott and Oegg (2007)** — the third edition of a study first published in
1985 — code each episode on two components: how far the **policy outcome** sought was achieved, and
how far **sanctions contributed** to it. Combining the two, they judge **roughly a third** of cases
at least partly successful, with success more likely when goals are modest, the target is small,
weak and friendly to the sender, and sanctions are imposed quickly and decisively.

**Pape (1997)** re-examined the cases counted as successes and argued that most do not survive
scrutiny: in many, the outcome was achieved by **force**, was not really conceded, or cannot be
attributed to sanctions. His conclusion: economic sanctions rarely achieve **major** political goals.
Elliott (1998) replied that the glass is half full rather than empty — the debate turns on *coding*.

**The selection effect** (Drezner, 2003). If targets that would concede do so when sanctions are
only **threatened**, then the cases we observe as *imposed* are the hard ones. Imposed sanctions will
look ineffective even if the instrument works. This is why **TIES** records threats as well as
impositions — and why the practice round compares the two.

> **The lesson for an analyst.** "Do sanctions work?" has no answer independent of how a case, an
> objective and a success are coded. Every number in this debate is a coding decision.

---

## 3. From comprehensive to smart sanctions

The humanitarian cost of the comprehensive sanctions on Iraq in the 1990s pushed senders towards
**targeted** measures: asset freezes and travel bans on named individuals, sectoral restrictions,
financial measures. Farrell and Newman (Session 08) explain why **financial** sanctions became the
weapon of choice: the dollar-clearing system and financial-messaging networks are **chokepoints**
under the jurisdiction of a few senders.

Targeted does not mean contained. Sanctions on banks, insurers and shippers propagate to every firm
that depends on them.

---

## 4. The firm in the middle

**The compliance perimeter.** A firm must screen customers, suppliers, banks and vessels against
sanctions lists — in the US, the Treasury's OFAC lists; in the EU, Council regulations; in Canada,
regulations under the *Special Economic Measures Act* and related statutes. Ownership rules extend
listings to entities owned by listed persons, so the perimeter is wider than the list.

**Secondary sanctions** threaten third-country firms with penalties — loss of access to the
sender's market or financial system — for dealing with the target. They make a sender's foreign
policy binding on firms that are not its nationals.

**Overcompliance and de-risking.** Because penalties are severe and the rules complex, banks and
firms often withdraw from whole markets or sectors the law does not close. The *effective* scope of
sanctions is set by compliance departments as much as by governments.

**The exit decision: Russia 2022.** Following the full-scale invasion of Ukraine, Western sanctions
and public pressure led many multinationals to suspend, scale back or leave Russian operations.
Exits were complicated by countermeasures — approval requirements and discounts on sales of foreign
assets, and in some cases temporary state management of foreign-owned firms. The firm's options:

| Option | Cost | Risk |
|---|---|---|
| **Stay** | reputational, compliance burden | new sanctions; asset seizure; home-state pressure |
| **Suspend** | idle assets | write-off if the situation persists |
| **Sell** | forced discount, approval delays | buyer later sanctioned; buy-back clauses |
| **Walk away** | full write-off | — |

---

## 5. What a risk dashboard should track

1. **Exposure** — the firm's revenues, assets and suppliers in sanctioned or at-risk jurisdictions;
2. **Pipeline** — threats and announced measures (the TIES lesson);
3. **Propagation** — banks, insurers, logistics providers whose own exposure would cut the firm off;
4. **Counter-measures** — what the target can do to foreign firms on its soil.

---

## 6. The Tableau skill of the day

A **year scaffold** joined with a *range* condition (`Year ≥ begin_year` and `Year ≤ end_year`, in the GSDB's column names) turns episodes
into active cases per year; a **Gantt chart** draws each episode as a bar from start to end. Step by
step: [`../02-practice/README.md`](../02-practice/README.md).

---

## References

Drezner, D. W. (2003). The hidden hand of economic coercion. *International Organization*, 57(3),
643–659.

Elliott, K. A. (1998). The sanctions glass: Half full or completely empty? *International Security*,
23(1), 50–65.

Felbermayr, G., Kirilakha, A., Syropoulos, C., Yalcin, E., & Yotov, Y. V. (2020). The Global Sanctions
Data Base. *European Economic Review*, 129, 103561. https://doi.org/10.1016/j.euroecorev.2020.103561

Hufbauer, G. C., Schott, J. J., Elliott, K. A., & Oegg, B. (2007). *Economic sanctions reconsidered*
(3rd ed.). Peterson Institute for International Economics.

Morgan, T. C., Bapat, N., & Kobayashi, Y. (2014). Threat and imposition of economic sanctions
1945–2005: Updating the TIES dataset. *Conflict Management and Peace Science*, 31(5), 541–558.
https://doi.org/10.1177/0738894213520379

Pape, R. A. (1997). Why economic sanctions do not work. *International Security*, 22(2), 90–136.
https://doi.org/10.1162/isec.22.2.90
