# Session 05 — Lecture notes (first half, 70 min after the Risk Briefs)

# International institutions: arenas of power, or constraints on it?

Slides: [`INTE60019A-S05-Lecture.qmd`](INTE60019A-S05-Lecture.qmd) · Instructor plan:
[`TEACHING-PLAN.md`](TEACHING-PLAN.md) ·
As a book chapter: [course book, Session 05](https://warint.github.io/geopolitics-geoeconomics/book/session-05.html)

---

## 1. Why would states under anarchy build institutions at all?

Session 03 left us with a system without a government above states. Session 04 showed trade
reorganising itself along geopolitical lines. Yet the same system is dense with institutions — the
UN, the WTO, the IMF, the World Bank, investment treaties, export-control regimes. Why?

| | **Liberal institutionalism** | **Realism** |
|---|---|---|
| **Key text** | Keohane (1984), *After Hegemony* | Mearsheimer (1994/95), *The False Promise of International Institutions* |
| **Why institutions exist** | They lower the **transaction costs** of cooperation, provide **information**, and lengthen the **shadow of the future** so that states can make credible commitments | They reflect the **distribution of power**; the strong build them to serve their interests |
| **Do they constrain states?** | Yes, at the margin — states comply because the institution makes reneging costly and cooperation valuable | Rarely — when interests and rules collide, power wins |
| **What it predicts for a firm** | Rules are a reasonably stable floor: dispute settlement, treaties, sanctions regimes behave predictably | Rules are only as stable as the coalition behind them; read the coalition, not the treaty |

Neither is a strawman. The useful question for a firm is not which theory is "true" but **which
institution, on which issue, behaves like which**. That is an empirical question — and Kuziemko and
Werker give one of its sharpest answers.

---

## 2. The Security Council in five facts

1. **Fifteen members**: five permanent (China, France, Russia, the United Kingdom, the United States)
   and ten elected. Before 1966 there were six elected members.
2. **Elected members** serve **two-year terms**, five elected each year by the General Assembly, by
   regional group, with a two-thirds majority; they cannot be immediately re-elected.
3. **Decisions** on substantive matters need nine votes and **no veto** from a permanent member.
4. Under **Chapter VII** the Council can impose measures — sanctions, arms embargoes, the use of
   force — that **bind every UN member state**.
5. An elected member's vote **can be pivotal**: the P5 need nine votes, so they must court elected
   members.

---

## 3. The price of a seat — Kuziemko and Werker (2006)

**The question.** Do powerful states pay for the votes of elected Security Council members?

**The identification idea.** Countries do not choose *when* they rotate onto the Council in any way
that tracks their need for aid — rotation follows regional queues and norms. So the authors compare
a country **with itself** in the years before, during and after its term. If aid rises during the
term and falls back afterwards, the seat — not the country's poverty, alliances or politics — is the
likeliest explanation.

**The findings**, in the paper's own summary:

- US aid to a developing country rises substantially — by about 59% in the abstract's headline
  estimate — when it rotates onto the Council, and aid through the UN rises too, more modestly.
- The increase is concentrated in the **term years** and disappears after the term.
- The effect is **larger in years when the Council matters more** — measured by how much the press
  covered it.

**Why that last result matters.** It is the difference between a statistical curiosity and a
mechanism. If aid followed membership whatever the Council was doing, rotation might proxy for
something else. That aid tracks the **salience** of Council business is what makes "vote buying" the
most plausible reading.

**The follow-up literature.** Dreher, Sturm and Vreeland extended the question to the World Bank and
the IMF, and Vreeland and Dreher (2014), *The Political Economy of the United Nations Security
Council: Money and Influence* (Cambridge University Press), brings the evidence together. The common
thread: temporary members of the Council receive more favourable treatment in several channels.

---

## 4. What it means for multinational firms

Institutions enter a firm's risk in at least four places:

| Where | Institution | What the firm relies on | What Kuziemko and Werker warn |
|---|---|---|---|
| **Sanctions** | UN Security Council (Chapter VII); then national and EU regimes (Session 10) | A predictable list of who is sanctioned and why | Resolutions are bargained; votes have prices; a P5 veto blocks UN sanctions — and pushes them into unilateral national regimes that diverge |
| **Investment protection** | Bilateral investment treaties; ICSID arbitration | A neutral forum if a host state expropriates | Treaties are only as strong as the host state's willingness to pay awards |
| **Political risk insurance** | MIGA (World Bank Group), national export-credit agencies | Cover against expropriation, war, transfer restrictions | The insurer's own shareholders are states — cover is a political decision too |
| **Trade rules** | WTO dispute settlement | Tariff bindings, non-discrimination | The Appellate Body has been unable to function since 2019; "rules" now depend on the coalition |

**The lesson for the firm.** An international institution is a risk **mitigator** when the coalition
that sustains it is stable, and a risk **source** when it is not. A risk dashboard should therefore
track not only the rules but the coalition: who sits on the Council, how they vote, what they are
being offered — which is exactly what today's practice round builds.

---

## 5. The Tableau skill of the day — LOD expressions

The practice needs two numbers for every country-year that do not exist in either file:

**Years relative to a term.** Join the term table (one row per term) to the aid table (one row per
country-year) on the country code — a **join** in the physical layer, not a relationship, because a
row-level calculation cannot mix fields from two related tables. Each country-year now appears once
per term of that country, which is exactly what an event study needs:

```text
[Event time]   =  [Year] - [Term start]
```

**The country's own pre-term baseline**, a *Level of Detail* expression that fixes the computation at
the country × term level whatever is in the view:

```text
[Baseline aid] = { FIXED [Iso3], [Term start] :
                   AVG( IF [Event time] >= -3 AND [Event time] <= -1 THEN [Aid] END ) }

[Aid relative to baseline] = [Aid] / [Baseline aid]      // row level: one value per country-year-term
```

`FIXED` computes before the view's dimension filters (context filters apply first) and ignores what
is on Rows and Columns: every row of a term carries that term's baseline. The ratio is then computed
row by row, and averaging it at each event year gives the **average across terms** of a ratio
computed **within** each term.

---

## References

Keohane, R. O. (1984). *After hegemony: Cooperation and discord in the world political economy*.
Princeton University Press.

Kuziemko, I., & Werker, E. (2006). How much is a seat on the Security Council worth? Foreign aid and
bribery at the United Nations. *Journal of Political Economy*, 114(5), 905–930.
https://doi.org/10.1086/507155

Mearsheimer, J. J. (1994/95). The false promise of international institutions. *International
Security*, 19(3), 5–49.

Vreeland, J. R., & Dreher, A. (2014). *The political economy of the United Nations Security
Council: Money and influence*. Cambridge University Press.
