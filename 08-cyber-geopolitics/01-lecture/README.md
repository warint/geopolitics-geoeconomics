# Session 08 — Lecture notes (first half, 70 min)

# Cyber geopolitics and digital threats

Slides: [`INTE60019A-S08-Lecture.qmd`](INTE60019A-S08-Lecture.qmd) · Instructor plan:
[`TEACHING-PLAN.md`](TEACHING-PLAN.md) ·
As a book chapter: [course book, Session 08](https://warint.github.io/geopolitics-geoeconomics/book/session-08.html)

The session opens with **four Risk Briefs** (20 min). The lecture follows.

---

## 1. Is cyberspace a domain of geopolitics?

Two caricatures dominate public debate. In the first, cyberspace is a revolutionary battlefield: a
"cyber Pearl Harbor" can switch off a country's grid, and small states or non-state actors can
humble great powers. In the second, cyber operations are simply crime and espionage with better
tools, of no strategic consequence.

Both are claims about **evidence**, and this session puts them to data. The question for a
multinational is narrower and more practical: *through which channels does inter-state rivalry in
cyberspace reach my operations, and how should my decision architecture absorb it?*

Three kinds of activity are easily confused:

| | Purpose | Typical actor | Example of the type |
|---|---|---|---|
| **Espionage** | Steal information — state secrets or intellectual property | intelligence services, contractors | intrusion into a defence supplier's network |
| **Disruption and degradation** | Interrupt or damage systems | military and intelligence units, proxies | denial of service against a ministry; wiper malware |
| **Crime** | Extract money | criminal groups, sometimes tolerated or used by states | ransomware against a hospital or a pipeline operator |

The boundaries blur — states tolerate, hire or shelter criminal groups — and that blurring is itself
a geopolitical fact.

---

## 2. Valeriano and Maness: cyber war versus cyber realities

Valeriano and Maness (2015) built a dataset of cyber incidents and campaigns between **rival
states** — pairs of states with a history of enduring hostility — and asked what the record actually
shows. Their argument, in four propositions:

1. **Restraint.** States use cyber operations far less, and far less destructively, than the
   "cyber war" narrative predicts. The severity of most incidents is low: defacements, denial of
   service, espionage — rarely physical destruction.
2. **Regional rivals.** Cyber conflict mostly follows existing rivalries — the United States and
   China, Russia and its neighbours, Israel and Iran, India and Pakistan, the two Koreas. Cyber
   does not create new conflicts; it is a tool in old ones.
3. **Why restraint?** Fear of escalation and blowback, the risk of revealing and losing a capability
   once used, the possibility that a weapon is reverse-engineered and turned back, and the value of
   keeping networks intact to spy on them.
4. **Limited coercive effect.** Cyber operations rarely change the target's behaviour. They are
   better at signalling and spying than at compelling.

The **Dyadic Cyber Incident and Campaign Data (DCID)** extends that work; version 2.0 covers
2000–2020. It is today's replication data.

**What restraint does not mean for the firm.** Low *strategic* severity is perfectly compatible with
high *commercial* cost. An operation that barely registers on a scale of interstate harm can still
halt a company's production for weeks.

---

## 3. Farrell and Newman: weaponised interdependence

Farrell and Newman (2019) look at the networks that globalisation built — finance, communications,
the internet's infrastructure — and observe that they are **not flat**. They have hubs. States that
have jurisdiction over a hub can use it:

| Effect | Mechanism | Example of the type |
|---|---|---|
| **Panopticon** | Use access to the hub to **see** what flows through it | intelligence access to data transiting cables, data centres or cloud providers under a state's jurisdiction |
| **Chokepoint** | Use control of the hub to **deny** access to others | cutting banks out of a financial-messaging network; denying firms access to software, chips or cloud services |

For a multinational, the implication is uncomfortable: **the firm itself can be the hub**. Its
cloud, its payment rails, its software updates are infrastructure that its home state can watch or
weaponise — and that rival states therefore treat as a target. This is the bridge from cyber
(today) to sanctions (Session 10) and space (Session 11).

---

## 4. The attribution problem

Every cyber dataset rests on **attribution**: someone has to say who did it. Attribution is

- **slow** — months or years after the event;
- **probabilistic** — technical indicators can be faked or reused;
- **political** — governments choose when to attribute publicly, and to whom;
- **selective** — what is attributed is what someone wanted known.

So event data on cyber operations is *a record of public attributions*, not a record of operations.
That is the most important caveat of today's practice round — and the heart of its "catch".

---

## 5. When the firm is collateral: NotPetya and its lessons

In June 2017 the **NotPetya** malware, spread through a Ukrainian accounting-software update and
widely attributed by Western governments to Russian military intelligence, spread far beyond its
apparent target. Shipping, pharmaceutical, food and logistics multinationals reported very large
losses — Maersk, Merck and Mondelez among them.

Three lessons for the firm:

1. **Proximity is technical, not political.** Firms were hit because they ran a piece of software
   in Ukraine, not because anyone chose them.
2. **Insurance is not a backstop.** Insurers invoked **war exclusions** to contest claims; the
   litigation that followed pushed the market to write explicit exclusions for state-backed cyber
   operations (Lloyd's required them from 2023). A firm's cyber cover may end exactly where
   geopolitics begins.
3. **The board owns it.** Securities regulators increasingly require disclosure of material cyber
   incidents and of board oversight of cyber risk.

---

## 6. Digital sovereignty and the splintering of the network

States increasingly regulate **where data sits and who may access it**: data-localisation rules,
restrictions on cross-border data transfers, security reviews of foreign cloud and telecoms
equipment, bans on particular vendors. For a multinational this is geopolitical risk in its
architecture:

- **Duplication costs** — separate data centres or cloud regions per jurisdiction;
- **Conflicting obligations** — one state's law requires disclosure that another's forbids;
- **Vendor risk** — a supplier banned in one market may be mandatory in another.

---

## 7. Cyber risk in the decision architecture of the firm

| Who | Role in geopolitical cyber risk |
|---|---|
| **Board** | Sets risk appetite; oversees disclosure; asks *which state actors would want our data or our downtime?* |
| **CISO** | Turns threat intelligence into controls; owns incident response |
| **Chief risk officer** | Integrates cyber with country, sanctions and supply-chain risk — the team-project view |
| **Insurer** | Prices the risk — and draws the line at state-backed operations |
| **Regulators** | Impose disclosure, localisation and vendor rules |

The question to bring to the practice round: *if the dataset shows where interstate cyber conflict
concentrates, how should a firm with operations in those dyads change its architecture?*

---

## 8. The Tableau skill of the day

A **highlight table** (rows × columns, colour = count) turns the incident list into an
**initiator × target matrix**. A **filter action** on a dashboard lets a click on one cell filter the
time series and the method breakdown on the other sheets. Step by step:
[`../02-practice/README.md`](../02-practice/README.md).

---

## References

Farrell, H., & Newman, A. L. (2019). Weaponized interdependence: How global economic networks shape
state coercion. *International Security*, 44(1), 42–79. https://doi.org/10.1162/isec_a_00351

Maness, R. C., Valeriano, B., Hedgecock, K., Macias, J. M., & Jensen, B. (2022). *Dyadic Cyber Incident
and Campaign Data (DCID)*, version 2.0. Harvard Dataverse. https://doi.org/10.7910/DVN/CQOMYV

Valeriano, B., & Maness, R. C. (2015). *Cyber war versus cyber realities: Cyber conflict in the
international system*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780190204792.001.0001
