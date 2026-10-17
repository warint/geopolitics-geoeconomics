# Session 06 — Lecture notes (first half, 70 min after the Risk Briefs)

# Private authority, standards and global regulation

> **[Open the lecture slides](https://warint.github.io/geopolitics-geoeconomics/session-06-lecture.html)** — or read the source at [`INTE60019A-S06-Lecture.qmd`](INTE60019A-S06-Lecture.qmd).
> As a book chapter: [course book, Session 06](https://warint.github.io/geopolitics-geoeconomics/book/session-06.html) · Instructor plan:
> [`TEACHING-PLAN.md`](TEACHING-PLAN.md)

---

## 1. The rules a firm actually follows

Session 05 looked at intergovernmental institutions. But walk through a multinational's supply
chain and count the rules it obeys: quality management (ISO 9001), environmental management (ISO
14001), information security (ISO/IEC 27001), forest and fisheries certification, labour codes of
conduct, carbon accounting (the GHG Protocol), sustainability reporting standards, telecom technical
specifications. **Most were not written by a government.** They are written by private or hybrid
bodies, adopted voluntarily — and then made compulsory by **buyers, investors and export markets**.

That is **private authority**: the capacity of non-state actors to make rules that others treat as
binding. For a multinational it is both a **risk** (a standard written elsewhere becomes a condition
of market access) and a **lever** (a firm that shapes the standard shapes the market).

---

## 2. The governance triangle — Abbott and Snidal (2009)

Abbott and Snidal map **regulatory standards-setting (RSS) schemes** in a triangle whose corners
are the three types of actor that can write rules:

```
                       STATE
                        /\
                       /  \
                      /    \
                     /      \
                    /        \
                   /__________\
                FIRM           NGO
```

- Schemes near a **corner** are run by one actor type: an industry code of conduct (firms), an
  activist certification (NGOs), an intergovernmental rule (states).
- Schemes in the **middle** are hybrids: firms and NGOs together (multi-stakeholder certification);
  states, firms and NGOs together (the UN Global Compact is often placed here).
- The **shadow of the state**: even private schemes are shaped by the possibility that states will
  regulate if private actors do not — and by states choosing to endorse, require or ignore them.

**Why it matters for a firm.** Where a scheme sits predicts how it behaves: who can change it, how
legitimate NGOs and governments will find it, and whether a state may one day make it mandatory.

---

## 3. Standards and power — Mattli and Büthe (2003)

Who wins when an *international* product standard is written at ISO or the IEC? Mattli and Büthe
compare three explanations:

| Explanation | Prediction |
|---|---|
| **Technological rationality** | The technically best solution wins, whoever proposes it |
| **Primacy of power** | The standard favours the states with the largest markets |
| **Institutional complementarity** (their argument) | Countries whose **domestic** standard-setting system is hierarchical and coordinated — matching the structure of ISO/IEC — are more effective at shaping international standards than countries with fragmented domestic systems |

Their evidence points to institutional complementarity: the coordinated European national standards
bodies were better placed than the fragmented, decentralised US system. **The lesson:** influence over
"technical" rules depends on how a country — and its firms — are organised to take part.

**Today, that is geopolitics.** The competition over telecommunications standards, over battery and
charging standards, over AI and data rules, is a competition between blocs, each trying to make its
domestic rules the world's. Bradford's *Brussels effect* (2020) describes how EU rules become global
because firms find it cheaper to adopt the strictest rule everywhere than to run two production
lines.

---

## 4. Three perspectives on standardization — Brunsson, Rasche and Seidl (2012)

Brunsson and colleagues organise research on standards around three aspects:

- **standardization *of* organizations** — standards that tell firms how to be organised (management
  system standards such as ISO 14001);
- **standardization *by* organizations** — the bodies that write standards and how they work;
- **standardization *as* organization** — standards as a way of organising markets and fields without
  formal hierarchy.

Their key point is that standards, usually associated with stability and sameness, are **dynamic**:
they are revised, contested, translated locally, decoupled from practice. A firm "certified" to ISO
14001 may run its plants exactly as before — the certificate and the practice can diverge.

---

## 5. Delegated or entrepreneurial — Green (2013)

Green distinguishes two sources of private authority:

| | **Delegated** | **Entrepreneurial** |
|---|---|---|
| **Origin** | States hand rule-making to private actors | Private actors create rules on their own, and others adopt them |
| **Illustration (carbon governance, Green's field)** | Private bodies accrediting and verifying projects under the Kyoto Protocol's Clean Development Mechanism | Voluntary carbon accounting and offset standards, such as the GHG Protocol |
| **What a firm should watch** | The state that delegated can take it back | Adoption — the rule is as strong as the number of users |

---

## 6. Race to the bottom, or trading up? — Prakash and Potoski (2006)

**The worry.** Trade intensifies competition; governments lower environmental standards to attract
investment and win exports — a race to the bottom.

**The alternative.** Vogel's (1995) *California effect*: exporters to strict markets adopt strict
standards, and trade spreads them — trading up.

**The test.** ISO 14001 is a voluntary environmental management standard that goes beyond what many
domestic laws require. Prakash and Potoski use a panel of 108 countries over seven years and ask
whether adoption in a country depends on adoption in its **export markets**.

**The finding.** Trade linkages **encourage** ISO 14001 adoption **when a country's major export
markets have themselves adopted it**. Trade spreads private standards upward — towards the
standards of the customers.

**For the firm.** A private standard can become a de facto condition of access to a market without a
single law changing. Monitoring "regulatory" risk means monitoring what your customers' home markets
adopt.

---

## 7. The Tableau skill of the day — maps and Pages

- Give `iso3` the geographic role **Country/Region** (right-click → *Geographic Role*). Tableau
  recognises ISO 3166 codes; check the **"unknown"** indicator at the bottom right of the map and fix
  what it could not place (*Map → Edit Locations*).
- **Filled map** of certificates per billion US$ of GDP; colour on a sequential palette, never a
  rainbow.
- `Year` on the **Pages** shelf: a play button animates the diffusion.
- **Small multiples**: `Region` on Rows and `Year` on Columns with a line of the median country —
  the same story, without animation, on one page.

---

## References

Abbott, K. W., & Snidal, D. (2009). The governance triangle: Regulatory standards institutions and
the shadow of the state. In W. Mattli & N. Woods (Eds.), *The politics of global regulation*
(pp. 44–88). Princeton University Press. https://doi.org/10.1515/9781400830732.44

Bradford, A. (2020). *The Brussels effect: How the European Union rules the world*. Oxford
University Press.

Brunsson, N., Rasche, A., & Seidl, D. (2012). The dynamics of standardization: Three perspectives on
standards in organization studies. *Organization Studies*, 33(5–6), 613–632.
https://doi.org/10.1177/0170840612450120

Green, J. F. (2013). *Rethinking private authority: Agents and entrepreneurs in global environmental
governance*. Princeton University Press.

Mattli, W., & Büthe, T. (2003). Setting international standards: Technological rationality or
primacy of power? *World Politics*, 56(1), 1–42. https://doi.org/10.1353/wp.2004.0006

Prakash, A., & Potoski, M. (2006). Racing to the bottom? Trade, environmental governance, and ISO
14001. *American Journal of Political Science*, 50(2), 350–364.
https://doi.org/10.1111/j.1540-5907.2006.00188.x

Vogel, D. (1995). *Trading up: Consumer and environmental regulation in a global economy*. Harvard
University Press.
