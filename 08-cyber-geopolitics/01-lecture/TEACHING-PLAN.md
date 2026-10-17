# Session 08 — Teaching plan (first half, 90 min including Risk Briefs)

# Cyber geopolitics and digital threats

> **Instructor page.** The student-facing companion is [`README.md`](README.md); the deck is
> [`INTE60019A-S08-Lecture.qmd`](INTE60019A-S08-Lecture.qmd).

*Is cyberspace a new battlefield for great powers — or a new way for old rivals to hurt each other,
with multinationals as collateral?*

---

## Opening

Before the briefs: *"Hands up if you think a cyber attack will one day switch off a G7 country's
power grid for a week."* Count. Leave the number on the board — it returns at minute 45.

Then check, by show of hands, who submitted the **GSDB request**. Anyone who has not does it during
the break.

---

## Board plan

| Minutes | |
|---|---|
| **0–20** | **Four Risk Briefs**, five-minute slots (four minutes + one question). Keep time strictly. |
| **20–30** | **A domain of geopolitics?** The two caricatures. Espionage / disruption / crime table — ask for one example of each from the briefs or the news. Insist on the blur: states and criminal groups. |
| **30–45** | **Valeriano and Maness.** Four propositions. Return to the opening vote: what would the book say? Ask why a state would hold back a weapon it has — get *escalation*, *revealing the capability*, *blowback*, *keeping access to spy*. Then: restraint is low *strategic* severity, not low *commercial* cost. |
| **45–58** | **Weaponised interdependence.** Draw a hub-and-spoke network on the board. Panopticon: circle the hub, draw the eye. Chokepoint: cut a spoke. Ask: *which firms in this room's future employers are hubs?* (cloud, payments, telecoms, software). Bridge to Sessions 10 and 11. |
| **58–66** | **Attribution.** Four properties. Then the punchline: event data are a record of public attributions. Ask what bias that creates in a dataset of rival dyads (democracies attribute more publicly; some victims never do). |
| **66–78** | **NotPetya** and insurance war exclusions. Digital sovereignty in three bullet points. |
| **78–90** | **The firm's decision architecture** table. Close with the question for the practice round. Open Tableau: show a highlight table being built from DCID in two drags. Hand over. |

---

## Run Tableau live

Import the DCID CSV and show that a dyad file needs **two** country fields — and that DCID's are
`StateA`/`StateB` (the dyad) plus `initiator` (a COW code), with no target column. Build `[Initiator]`
and `[Target]` (formula in the practice README, step 2.3), then the highlight table (`[Initiator]` on
Rows, `[Target]` on Columns, the record count on Colour, then *Show Me → highlight table*). Ask what the empty cells mean: no incidents, or no rivalry in the data? (The second — DCID
only covers rivals.)

---

## Put this to the room

*"Your firm runs a plant in a country that sits in one of the densest cells of this matrix. What do
you change on Monday — and what do you tell the insurer?"*

---

## Misconception to pre-empt

That a dataset of cyber incidents is a dataset of cyber operations. It is a dataset of **publicly
attributed** incidents between **rivals**, coded from open sources. Say it at section 4 and again
before the practice round.
