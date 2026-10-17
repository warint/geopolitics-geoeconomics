# Session 02 — Lecture notes (first half, 70 min)

# The international economic order

Slides: [`INTE60019A-S02-Lecture.qmd`](INTE60019A-S02-Lecture.qmd) · Instructor plan:
[`TEACHING-PLAN.md`](TEACHING-PLAN.md) ·
As a book chapter: [course book, Session 02](https://warint.github.io/geopolitics-geoeconomics/book/session-02.html)

The session opens with four Risk Briefs (20 minutes); the lecture takes the next seventy.

---

## 1. What an "economic order" is

An **international order** is a set of rules, institutions and expectations that governs relations
between states, backed by some distribution of power. An **economic order** is the part of it that
governs trade, money and investment — the part a multinational lives inside without noticing, until
it changes.

Three questions describe any economic order:

| Question | What to look at |
|---|---|
| **Who wrote the rules?** | Which states designed the institutions, and in whose interest |
| **What do the rules say?** | Openness to trade, to capital, to investment; how disputes are settled |
| **What holds them in place?** | Hegemonic power, shared interest, institutions with their own momentum |

---

## 2. The post-1945 order, in four layers

**Bretton Woods (1944).** Forty-four allied states create the **International Monetary Fund**
(stable exchange rates, balance-of-payments support) and the **International Bank for
Reconstruction and Development**, the core of the World Bank. Fixed but adjustable exchange rates
anchored on the dollar, the dollar on gold.

**The GATT (1947).** A provisional agreement — the planned International Trade Organization never
came into being — that cuts tariffs in successive rounds on the principle of
**most-favoured-nation** treatment and **national treatment**.

**Embedded liberalism.** Ruggie (1982) named the bargain: openness abroad, made politically
sustainable by social protection and macroeconomic autonomy at home. Capital controls were normal;
free trade was managed.

**The neoliberal turn and the WTO (1995).** The dollar's link to gold ends in 1971; capital controls
are dismantled through the 1980s and 1990s; the Uruguay Round creates the **World Trade
Organization**, with a binding dispute-settlement mechanism and rules reaching into services,
intellectual property (TRIPS) and investment measures (TRIMs). China joins in 2001.

**The liberal order as a political project.** Ikenberry (2011, *Liberal Leviathan*) argues the
order was American-led but **easy to join and hard to overturn**: open, rule-based, institutional
enough that rising states gain more by joining than by challenging it. Session 03 sets the realist
reply beside it.

---

## 3. Baldwin's three unbundlings

Baldwin organises globalisation around **three costs**: of moving **goods**, moving **ideas**, and
moving **people**.

| Phase | What became cheap | What it unbundled | Consequence |
|---|---|---|---|
| **First unbundling** (steam, from the 19th century) | moving **goods** | production from consumption: you could make things far from where they were bought | Industry **clustered** in the North, where ideas stayed cheap to move locally. **Great divergence** between North and South |
| **Second unbundling** (ICT, from about 1990) | moving **ideas** | the factory itself: stages of production could be offshored while coordinated from headquarters | Northern know-how moved South **inside the multinational's value chain**. **Great convergence** |
| **Third unbundling** (prospective) | moving **people** — virtually: telepresence, telerobotics | the worker from the workplace | Services trade in tasks; competition reaches occupations, not only sectors |

**The key point for this course.** In the second unbundling, *the multinational is the vehicle of
convergence*. Know-how is transferred through supply chains the firm controls. That is why
geopolitics now reaches firms so directly: the supply chain is where technology, jobs and security
dependence travel together.

**Baldwin's evidence** is a picture: the G7's share of world income, rising for over a century, then
falling sharply after about 1990 — while a handful of developing economies (his "Industrialising
Six": China, Korea, India, Poland, Indonesia, Thailand) gain almost all of it. That is today's
target figure.

---

## 4. From convergence to backlash

**Rodrik's trilemma** (Rodrik, 2011, *The Globalization Paradox*): a country can have at most two of
**deep economic integration**, **national sovereignty** and **democratic politics**.

| Choose | Give up | Looks like |
|---|---|---|
| integration + sovereignty | democracy | the "golden straitjacket": policies dictated by markets |
| integration + democracy | sovereignty | global federalism: rules made above the state |
| sovereignty + democracy | deep integration | Bretton Woods compromise: shallow, managed openness |

The trilemma reads the 2010s and 2020s: Brexit, tariff wars, industrial policy, export controls, and
"de-risking" are choices of sovereignty and democracy over integration.

**Slowbalisation.** World trade in percent of GDP rose steeply from the 1990s to 2008 and has broadly
flattened since. Whether that is a retreat from globalisation or a shift in its form — from goods to
services and data — is contested. The *extend* step of the practice round lets you see the flattening
and judge it.

**When the writers' share shrinks.** If the G7 produced around two-thirds of world GDP when it wrote
the rules, and much less today, two questions follow — and they open Sessions 03 and 04: will the
rules be rewritten by the new powers (power transition), and will the world split into blocs with
rules of their own (fragmentation)?

---

## 5. What it means for the multinational

| Implication | Example |
|---|---|
| **Your market is no longer where the rules are written.** | A European firm earns a growing share of revenue in markets whose governments did not design the WTO and do not feel bound by its spirit |
| **Your supply chain is a geopolitical object.** | The know-how the second unbundling moved is what export controls now try to stop |
| **Multilateral protection is weaker.** | The WTO's Appellate Body has been unable to hear appeals since December 2019; disputes are settled by power more often than by panels |
| **Measurement choices are strategy choices.** | At market exchange rates, the G7 still looks large; at PPP, it looks much smaller. Which one a board sees shapes where it builds |

---

## 6. What the figure does not license

- A falling G7 share is **relative**: G7 economies kept growing. It does not mean the G7 market
  shrank.
- At **current US dollars**, the share moves with the dollar: part of any year-to-year change is the
  exchange rate, not production.
- **Convergence is concentrated.** Most of the gain goes to a handful of countries — above all
  China. "The South" did not converge.
- It shows **income**, not **rule-making power**. Whether shrinking share means shrinking influence is
  the question of Session 03, not a reading of this chart.

---

## 7. The Tableau skill of the day

DataBank gives you **years as columns**. Tableau wants **one row per country-year**. Select the year
columns in the data source pane → right-click → **Pivot**. Rename `Pivot Field Names` to `Year`
and `Pivot Field Values` to `Value`. Change `Year` to a number or date and `Value` to a number —
DataBank's `..` become nulls. Then build the G7 share with a calculated field, and check it with a
**percent of total** table calculation. Full click-path: [`../02-practice/README.md`](../02-practice/README.md).

---

## References

Baldwin, R. (2016). *The great convergence: Information technology and the new globalization*.
Belknap Press of Harvard University Press.

Ikenberry, G. J. (2011). *Liberal Leviathan: The origins, crisis, and transformation of the American
world order*. Princeton University Press.

Rodrik, D. (2011). *The globalization paradox: Democracy and the future of the world economy*.
W. W. Norton.

Ruggie, J. G. (1982). International regimes, transactions, and change: Embedded liberalism in the
postwar economic order. *International Organization*, 36(2), 379–415.
