# Session 04 — Lecture notes (first half, 50 min)

# Trade, conflict and geoeconomic fragmentation

> **[Open the lecture slides](https://warint.github.io/geopolitics-geoeconomics/session-04-lecture.html)** — or read the source at [`INTE60019A-S04-Lecture.qmd`](INTE60019A-S04-Lecture.qmd).
> As a book chapter: [course book, Session 04](https://warint.github.io/geopolitics-geoeconomics/book/session-04.html) · Instructor plan:
> [`TEACHING-PLAN.md`](TEACHING-PLAN.md)

The session opens with Quiz 1 (20 minutes) and four Risk Briefs (20 minutes); the lecture takes the
remaining fifty.

---

## 1. Does trade keep the peace? The liberal answer

The **commercial peace** is one of the oldest ideas in international political economy. From
Montesquieu ("peace is the natural effect of trade") to Norman Angell's *The Great Illusion* (1910),
the argument is that trade raises the **opportunity cost of war**: states that gain from exchange
lose those gains if they fight.

Modern versions add mechanisms:

- **Opportunity cost.** Conflict disrupts trade; the more a dyad trades, the more it loses.
- **Signalling.** Interdependent states can send costly signals — threatening economic ties — short
  of force, which reduces miscalculation.
- **Domestic coalitions.** Trade creates exporters and importers with a stake in peaceful relations
  who lobby their governments.
- **Institutions.** Trade agreements create forums and dispute-settlement procedures.

Statistical studies of dyads from the 1990s onwards (notably Russett & Oneal's *Triangulating
Peace*, 2001) found that dyads with more trade relative to GDP experience fewer militarised disputes.

---

## 2. The realist critique

Realists reply that interdependence can **cause** conflict:

- **Vulnerability.** Dependence on a rival for essential goods is a security risk. States therefore
  limit it — or fight to secure supplies (Waltz, 1979).
- **Relative gains** (Session 03). If trade makes the rival stronger faster, it is a threat.
- **Security externalities** (Gowa, 1994). Trade raises the economic capacity of the partner; states
  therefore trade more with **allies** than with adversaries.
- **Expectations of future trade** (Copeland, 2015). What matters is not today's trade but whether
  leaders expect it to continue. When they expect to be cut off, interdependence becomes a reason to
  act before the window closes.

The history the realists point to: Britain and Germany were heavily interdependent in 1914.

---

## 3. What the evidence says: Mansfield (2021)

Mansfield's review in the *Oxford Handbook of International Political Economy* sets out the
debate and the main empirical findings. Four points to retain:

1. **The relationship runs both ways.** Conflict reduces trade, so a negative correlation between
   trade and conflict does not by itself show that trade causes peace.
2. **Institutions matter.** Preferential trading arrangements are associated with fewer disputes
   among members (Mansfield & Pevehouse, 2000).
3. **Context matters.** The effect differs with regime type, the level of development, and the
   distribution of power between the partners.
4. **The question has changed.** As geopolitical competition returned, research has turned from
   "does trade pacify?" to "how do states use trade as an instrument of conflict?" — the questions
   of Sessions 08, 10 and 11.

---

## 4. Bilateral versus multilateral openness

**Martin, Mayer & Thoenig (2008), *Make Trade Not War?*, *Review of Economic Studies*, 75(3),
865–900** ([doi:10.1111/j.1467-937X.2008.00492.x](https://doi.org/10.1111/j.1467-937X.2008.00492.x)).

Their argument separates two effects:

| | Effect on the risk of a bilateral conflict |
|---|---|
| **Bilateral trade** between A and B | **lowers** it: A and B have more to lose from fighting each other |
| **Multilateral trade openness** of A and B with the rest of the world | **raises** it: if A can trade with everyone else, losing B costs less |

The implication is uncomfortable for the liberal view: **globalisation lowers the cost of
bilateral conflict** because it provides substitutes. A world of many alternative suppliers makes
it cheaper to break with any one of them. Their empirical work finds support for both effects.

---

## 5. Fragmentation: the new question

**Friend-shoring** (a term popularised in US policy debate in 2022) proposes to move supply chains
towards trusted partners. **De-risking** (the European Commission's term, 2023) proposes to reduce
dependence on rivals in critical goods without breaking trade overall. **De-coupling** is the end
point: separate economic blocs.

**Gopinath, Gourinchas, Presbitero & Topalova (2025)** ask whether the data show this happening.
Their design:

1. **Define blocs.** Countries are grouped into a **US-leaning** bloc, a **China-leaning** bloc and a
   **non-aligned** group on the basis of their **foreign-policy alignment as revealed by UN General
   Assembly voting**. Read Section 2 of the paper for exactly which vote or measure, and which year,
   they use — ours will be a simplification, and you must say how it differs.
2. **Compare trade within and between blocs** before and after Russia's invasion of Ukraine in
   February 2022, controlling for the usual determinants of bilateral trade.
3. **Look for connectors** — non-aligned countries whose trade with both blocs grew, through which
   some between-bloc trade may be rerouted.

**Their main finding**: after the invasion, trade **between** the two blocs fell relative to trade
**within** them, by a margin of the order of ten percent or more (find the exact estimate in the
paper and write it in your notes), and foreign direct investment shows a similar pattern. They are
careful to say this is a fragmentation still small compared with the Cold War — but it is
happening, and it is concentrated in strategic sectors.

---

## 6. What it means for the multinational

| | |
|---|---|
| **Classify your markets by alignment** | Which of your five most important countries (the team milestone) sit in which bloc — and which are drifting? |
| **Connectors are opportunities and risks** | Mexico, Vietnam and others gain between-bloc trade — and attract scrutiny for transshipment and rules-of-origin enforcement |
| **The cost of switching is falling for states, not for you** | Martin, Mayer & Thoenig: multilateral openness makes it cheaper for *states* to break with a partner. Your supply contracts do not get cheaper to break |
| **De-risking is sectoral** | Fragmentation is concentrated in strategic goods; a firm in consumer goods and one in semiconductors face different worlds |

---

## 7. What the figure does not license

- A fall in between-bloc trade is a **correlation with a date**, not proof that geopolitics caused it:
  sanctions on Russia, the post-COVID rebound and price changes all move trade values in the same
  years.
- **Bloc membership is a modelling choice.** Change the threshold or the base year and countries
  move between blocs — and the figure moves with them.
- **Values, not volumes.** Trade in US dollars rises with commodity prices; 2022 was a year of
  very high energy and food prices.
- It shows **aggregate** trade. Your firm's products may be in a sector where fragmentation is far
  stronger — or absent.

---

## 8. The Tableau skill of the day

A dyadic table (exporter × partner × year) needs **two** copies of the country table: one for the
exporter's bloc, one for the partner's. In Tableau's data model, add the bloc table, relate it on
`exporter = country`, then add it again and relate the second copy on `partner = country`. Blocs
are **sets** defined by a condition on the ideal point, with **parameters** as thresholds. The trade
series is indexed to a base year with a table calculation. Click-path:
[`../02-practice/README.md`](../02-practice/README.md).

---

## References

Angell, N. (1910). *The great illusion*. Heinemann.

Bailey, M. A., Strezhnev, A., & Voeten, E. (2017). Estimating dynamic state preferences from United
Nations voting data. *Journal of Conflict Resolution*, 61(2), 430–456.

Copeland, D. C. (2015). *Economic interdependence and war*. Princeton University Press.

Gopinath, G., Gourinchas, P.-O., Presbitero, A. F., & Topalova, P. (2025). Changing global linkages:
A new Cold War? *Journal of International Economics*, 153, 104042.

Gowa, J. (1994). *Allies, adversaries, and international trade*. Princeton University Press.

Mansfield, E. D. (2021). International trade and conflict. In J. C. W. Pevehouse & L. Seabrooke
(Eds.), *The Oxford handbook of international political economy* (pp. 660–671). Oxford University
Press.

Mansfield, E. D., & Pevehouse, J. C. (2000). Trade blocs, trade flows, and international conflict.
*International Organization*, 54(4), 775–808.

Martin, P., Mayer, T., & Thoenig, M. (2008). Make trade not war? *Review of Economic Studies*, 75(3),
865–900.

Russett, B., & Oneal, J. R. (2001). *Triangulating peace: Democracy, interdependence, and
international organizations*. W. W. Norton.
