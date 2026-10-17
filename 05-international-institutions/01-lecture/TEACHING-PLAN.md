# Session 05 — Teaching plan (first half, 90 min)

# International institutions: the economic institutions that build business — old and new

> **Instructor page.** The student-facing companion is [`README.md`](README.md); the deck is
> [`INTE60019A-S05-Lecture.qmd`](INTE60019A-S05-Lecture.qmd).

*When a multinational relies on an international institution to finance, insure or protect its
business, is it relying on a rule — or on the states that buy and sell influence inside it?*

---

## Opening

Before any slide, ask: *"Your firm is bidding to build a power plant in Kenya. Name every
international institution that could be involved — as lender, insurer, co-investor, referee or
competitor."* Write the list on the board as it comes. Expect the World Bank and the IMF; push for
IFC, MIGA, ICSID, the AfDB, the AIIB, China's Exim Bank. Return to the list in section 8 and sort
it into the four channels.

---

## Board plan

| Minutes | |
|---|---|
| **0–20** | **Four Risk Briefs**, five-minute slots (four minutes + one question). Keep strict time; one question from the room per brief. |
| **20–26** | **Why institutions — and why a firm should care.** Keohane and Mearsheimer side by side; the four-row table. Introduce *contested multilateralism* (Morse & Keohane): regime shifting vs competitive regime creation. |
| **26–34** | **The Bretton Woods core.** The IMF in one table: 191 members, the 85% rule, US 16.49% vs China 6.08%. Write "votes lag economic weight" on the board — it is the hinge of the session. WTO: the empty Appellate Body and the MPIA. OECD: export credits, the MNE Guidelines, Pillar Two — one line each. |
| **34–44** | **The World Bank Group as a business toolkit.** Draw five boxes: IBRD/IDA (contracts), IFC (co-investment), MIGA (insurance), ICSID (arbitration), procurement and debarment. For each, ask *what would your firm use it for?* Land the two non-obvious points: procurement is the biggest channel; cross-debarment makes a sanction at one bank a sanction at five. |
| **44–54** | **Does influence have a price?** The Council in five facts (draw fifteen seats, shade the P5, "9 votes, no veto"). Kuziemko & Werker: the question, the identification idea — *a country compared with itself* — then draw the expected event-time shape before showing the result. The salience result. Then the bridge: the same pattern at the World Bank and the IMF (Dreher, Sturm & Vreeland). |
| **54–60** | **The regional development banks.** The six-row table; ask the room which banks a Canadian firm may bid at and which a Chinese firm may. Point to the EBRD's 2022 suspension of Russia and Belarus. |
| **60–70** | **The new institutions.** AIIB (China 26.37% of votes, ¾ supermajority), NDB (equal shares), CRA (30% delinked), CMIM (40% delinked) and AMRO, China's policy banks and the Silk Road Fund, BRICS expansion. Ask: *why did the UK join the AIIB and the US not?* |
| **70–77** | **Complement or counter-hegemony?** Four rows — votes, standards, currency, sanctions. The 2022 test: the AIIB and NDB froze Russia. Vote with hands, then ask what evidence would change their mind. |
| **77–84** | **What it means for the firm.** Return to the opening list; sort it into procurement, finance, insurance, dispute settlement. Then the five risks. Land the lesson: track the coalition, not just the rule. |
| **84–90** | **The Tableau skill.** Open Tableau on the projector; write the `[Event time]` and `[Baseline aid]` calculations live; explain why `FIXED` and not a table calculation. Hand over. |

The timing is tight. If the room is slow, compress section 5 to the procurement-eligibility column
and the EBRD suspension; the table is in the notes.

---

## Run Tableau live

Join the term table to the aid table on the ISO code (double-click into the logical table to reach
the join layer) and show the row count before and after. Then filter `[Event time]` to −3…+3 and
show that a country with two terms close together appears twice in some years. Ask whether that is
a problem. (It is a feature of event studies — overlapping windows — and it goes in the log.)

---

## Put this to the room

*"Your project in a BRICS partner country is co-financed by the AIIB and insured by MIGA. The host
state is sanctioned by the United States next year. Which of the two institutions do you expect to
keep its commitments — and why?"*

Push for the mechanism: both fund themselves in dollar markets and both froze Russia in 2022; MIGA's
largest shareholder is the sender, the AIIB's is not; the answer depends on the coalition inside
each, not on its charter.

And the Council version: *"If a seat on the Security Council can be bought, should a firm treat a UN
sanctions resolution as more or less durable than a unilateral US one?"* UN resolutions need a broad
coalition and survive changes of government in any one capital; unilateral measures can be reversed
by one executive — but also extended by one.

---

## Misconceptions to pre-empt

- **That the paper proves "corruption at the UN".** It shows that aid moves with membership and with
  the Council's salience; *bribery* is the authors' interpretation of a well-identified pattern.
  Make the room separate the finding from the reading of it — it is the same discipline as "the
  catch".
- **That the new institutions are simply "China's banks".** The NDB gives its five founders equal
  votes; the AIIB has more than a hundred members, including most of Europe; both froze Russia in
  2022. Make the room distinguish the AIIB and the NDB (multilateral, rule-based, dollar-funded)
  from China's bilateral policy banks (state-owned, confidential terms).
- **That BRICS is an institution.** It is a summit club; its institutions are the NDB and the CRA.
  Membership counts change, and Saudi Arabia's status is ambiguous — students must cite a date.
