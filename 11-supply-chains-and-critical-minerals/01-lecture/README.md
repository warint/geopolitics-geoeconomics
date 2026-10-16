# Session 11 — Lecture notes (first half, 70 min after the Risk Briefs)

# Weaponised interdependence: supply chains and critical minerals

Slides: [`INTE60019A-S11-Lecture.qmd`](INTE60019A-S11-Lecture.qmd) · Instructor plan:
[`TEACHING-PLAN.md`](TEACHING-PLAN.md)

The session opens with **four Risk Briefs** (30 min). The lecture follows.

---

## 1. From efficiency to exposure

For three decades, supply chains were designed for **cost and speed**: single sourcing,
just-in-time inventories, production where it was cheapest. The design rested on an unstated
premise of the liberal economic order (Session 02): that trade would stay apolitical. Sessions 04
and 10 showed the premise eroding through blocs and sanctions. Today we look at the input side of
the firm — the materials without which it cannot produce at all.

The **green and digital transitions** make this acute. Batteries, permanent magnets, solar panels,
wind turbines and semiconductors depend on a short list of minerals — lithium, cobalt, nickel,
graphite, rare earths, gallium, germanium — whose mining and, above all, **refining** are
geographically concentrated.

---

## 2. Three ways commodities become geopolitical

| | What drives it | Classic example | Who acts |
|---|---|---|---|
| **Conflict commodities** | Resources finance or motivate armed conflict; the supply chain carries the conflict to the consumer | tin, tantalum, tungsten and gold from eastern DRC | armed groups, traders, smelters, end buyers |
| **Resource nationalism** | A producing state captures more of the value — taxes, local processing, state ownership | Indonesia's bans on unprocessed nickel ore exports (first in 2014, reinstated from 2020), built to force smelting at home | the producing state |
| **Strategic export controls** | A state restricts a material to coerce, signal, or protect its own industry | China's export licensing on gallium and germanium (2023), on graphite (late 2023), and on several rare-earth elements (2025) | the dominant producer or refiner |

**Le Billon and Shykora (2020)** argue that the first category is a lens on all three: supply
chains are not neutral conduits but **sites** where conflict, environmental damage and political
power are produced and transferred. Due diligence regimes — the OECD *Due Diligence Guidance for
Responsible Supply Chains of Minerals from Conflict-Affected and High-Risk Areas*, section 1502 of
the US Dodd–Frank Act, the EU Conflict Minerals Regulation — shift responsibility onto the
importing firm, but they cover a few minerals, rely on audits of the smelter rather than the mine,
and can lead firms to **avoid** a region rather than improve it.

> **For the firm:** the same mineral can carry all three risks at once. Cobalt from the DRC is a
> conflict-and-labour risk at the mine, a resource-nationalism risk at the border (export bans and
> quotas), and a strategic risk at the refinery, most of which is in China.

---

## 3. Weaponised interdependence

**Farrell and Newman (2019)** turn the liberal argument on its head. Global networks — finance,
communications, supply chains — are not flat; they are **hub-and-spoke**. A state with jurisdiction
over a hub can:

- exploit a **panopticon effect**: see what passes through the hub (who pays whom, who ships what);
- exploit a **chokepoint effect**: deny others access to the hub.

The concept was built on SWIFT and the US dollar (Session 10). Minerals are the physical analogue:
**the refinery is the hub**. Mining is somewhat dispersed; refining and processing are much more
concentrated. A country that refines most of the world's graphite or rare earths holds a chokepoint
even over ore mined elsewhere.

**Two conditions** make a chokepoint usable: (1) the network must be **concentrated**, and (2) the
state must have **domestic institutions** able to direct the firms that run the hub. Both are
measurable — the first with today's HHI, the second with the governance indicators of Session 12.

---

## 4. Export restrictions: the evidence

**Kowalski and Legendre (2023)** use the OECD *Inventory of Export Restrictions on Industrial Raw
Materials* — now the *Inventory of Export Restrictions on Critical Raw Materials* — which records,
country by country and commodity by commodity since 2009, export taxes, quotas, prohibitions,
licensing requirements and minimum export prices.

Their headline: **export restrictions on critical raw materials multiplied several-fold between
2009 and the early 2020s** (roughly fivefold in the 2023 paper — check the exact factor and end year
in your edition), and they are concentrated among a few large producers — China, India, Argentina,
Russia, Viet Nam, Kazakhstan among them — and in exactly the minerals whose production is most
concentrated.

**What the count does not measure.** A licensing requirement and an outright ban each count as one
measure. A tax of 5% and one of 40% each count as one. The inventory is a **map of where to look**,
not a measure of how much supply is withheld.

---

## 5. Concentration, measured: the Herfindahl–Hirschman index

For a mineral with producers $i = 1, \dots, N$ and shares of world production $s_i$ expressed in
percent:

$$
\text{HHI} = \sum_{i=1}^{N} s_i^2, \qquad 0 < \text{HHI} \le 10\,000.
$$

- One producer with 100%: HHI = 10,000. Ten equal producers: HHI = 1,000.
- Antitrust convention: above **2,500** is "highly concentrated" (the 2023 US Merger Guidelines
  lowered the threshold to **1,800**).
- HHI weights large shares heavily: one country at 70% contributes 4,900 on its own.

**Three decisions change the number**, and each must be named:

1. **Stage.** Mine production, refining, or exports? Refining is usually far more concentrated than
   mining.
2. **The "Other countries" row.** Treating it as one country inflates the HHI; dropping it deflates
   the denominator. Report both.
3. **Units.** Shares are computed within one mineral, in that mineral's unit. Never pool minerals.

The **numbers equivalent**, $1 / \sum s_i^2$ with shares as fractions, converts the HHI into "the
number of equal-sized producers that would give this concentration" — a figure a board understands.

---

## 6. The system-wide signal: GSCPI

The New York Fed's **Global Supply Chain Pressure Index** combines transport costs (shipping and air
freight) with supply-chain components of manufacturing surveys across major economies into one
monthly series, measured in standard deviations from its average. It spiked during the pandemic and
eased in 2023. It is **system-wide**: it says nothing about one mineral. Its use in a dashboard is as
the background against which mineral-specific restrictions are read. Every release re-estimates the
history; use one vintage.

---

## 7. What can the firm do?

| Strategy | Example | Cost | Limit |
|---|---|---|---|
| **Stockpile** | months of cobalt or rare-earth magnets in inventory | working capital, obsolescence | buys time, not supply |
| **Diversify** | second sources outside the dominant producer | higher unit price, qualification time | the refinery may still be in the same country |
| **Friend-shore** | source from allies (the "friend-shoring" agenda of 2022) | price premium; fewer suppliers | allies' output may not exist yet |
| **Substitute** | LFP batteries without cobalt; magnet designs with fewer heavy rare earths | R&D, performance trade-offs | substitutes have their own chokepoints |
| **Integrate vertically** | equity stakes in mines or offtake contracts | capital, host-country political risk | swaps a geopolitical risk for a political one |
| **Recycle** | closed-loop battery and magnet recycling | scale, collection | small share of supply for a decade |

Governments are moving in the same direction: the European Commission's language of **de-risking**
rather than decoupling (2023); the **EU Critical Raw Materials Act** (2024), with 2030 benchmarks for
strategic raw materials — 10% of EU consumption extracted in the EU, 40% processed, 25% recycled,
and no more than 65% from any single third country at any stage; the critical-mineral sourcing
conditions attached to US electric-vehicle tax credits. Each changes the firm's calculation, and each
is itself a source of regulatory risk.

---

## 8. The Tableau skill of the day

- **Share** of world production, row-level, using a FIXED LOD for the mineral total:
  `[Production] / {FIXED [Mineral]: SUM([Production])}`
- **HHI** as the sum of squared shares: `SUM(POWER([Share] * 100, 2))` with `Mineral` on the view.
- **Treemap**: Country on Detail and Label, Production on Size, Share on Colour, one per mineral.
- **Dashboard action**: *Dashboard → Actions → Add Action → Filter*, source = treemap, target =
  restrictions chart, field = mineral.

The step-by-step version is the practice brief: [`../02-practice/README.md`](../02-practice/README.md).

---

## References

Farrell, H., & Newman, A. L. (2019). Weaponized interdependence: How global economic networks shape
state coercion. *International Security*, 44(1), 42–79. https://doi.org/10.1162/isec_a_00351

Kowalski, P., & Legendre, C. (2023). Raw materials critical for the green transition: Production,
international trade and export restrictions. *OECD Trade Policy Papers*, No. 269. OECD Publishing.
https://doi.org/10.1787/c6bb598b-en

Le Billon, P., & Shykora, L. (2020). Conflicts, commodities and the environmental geopolitics of
supply chains. In S. O'Lear (Ed.), *A research agenda for environmental geopolitics* (pp. 59–73).
Edward Elgar. https://doi.org/10.4337/9781788971249.00012

OECD (2026). *OECD inventory of export restrictions on critical raw materials 2026*. OECD
Publishing. https://doi.org/10.1787/d5ca8f62-en
