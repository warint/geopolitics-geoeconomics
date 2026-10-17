# Session 07 — Lecture notes (first half, 50 min after Quiz 2 and the Risk Briefs)

# Measuring risk: content analysis, coding, big data and composite indices

> **[Open the lecture slides](https://warint.github.io/geopolitics-geoeconomics/session-07-lecture.html)** — or read the source at [`INTE60019A-S07-Lecture.qmd`](INTE60019A-S07-Lecture.qmd).
> Read further: [Chapter 7 of the book](https://warint.github.io/geopolitics-geoeconomics/book/session-07.html) · Instructor plan:
> [`TEACHING-PLAN.md`](TEACHING-PLAN.md)

---

## 1. The measurement chain

Every number in this course — GPR, a capability share, an ideal point, a sanctions count — is the
end of a chain:

```
concept  →  indicator  →  source  →  coding rule  →  aggregation  →  presentation
"geopolitical    "share of      ten          the eight       monthly share,    a line with
 risk"           articles…"     newspapers   categories      base 1985–2019    spikes labelled
```

Two questions apply to every link:

- **Validity** — does the indicator measure the concept? (Is newspaper attention geopolitical risk?)
- **Reliability** — would someone else, following the same rules, get the same number? (Would a
  second coder put the same article in the same category?)

A measure can be perfectly reliable and invalid — a thermometer read identically by everyone that
measures the wrong room. Today is about seeing every link, so you can audit a score you are sold
and defend one you build.

---

## 2. Content analysis

Krippendorff (2018) defines content analysis as a research technique for making **replicable and
valid inferences** from texts to the contexts of their use. Its steps:

| Step | In the GPR index | In your coding today |
|---|---|---|
| **Unitising** — what is one unit? | an article | a headline |
| **Sampling** — which units? | all articles in ten newspapers | 40 headlines drawn at random from a GDELT query |
| **Recording / coding** — which category? | a dictionary of words | two human coders and a protocol |
| **Reducing** — how are codes summarised? | monthly share | counts and shares by category |
| **Inferring** — what do we conclude? | geopolitical risk is high | your firm's countries are in the news for … |

**Manifest vs latent content.** A dictionary sees **manifest** content — the words on the page. Human
coders can see **latent** content — what an article is *about*. Dictionaries are cheap, fast and
perfectly reliable; humans are slow and less reliable but can catch meaning. The best measures use
both: a dictionary, **audited by humans**.

---

## 3. Three dictionary methods

| | **GPR** — Caldara & Iacoviello | **EPU** — Baker, Bloom & Davis | **PRisk** — Hassan et al. |
|---|---|---|---|
| **Text** | newspaper articles | newspaper articles | earnings-call transcripts |
| **Unit counted** | article with GPR words | article with **E**conomy **and** **P**olicy **and** **U**ncertainty terms | political two-word combinations (bigrams) near synonyms of risk or uncertainty |
| **How the dictionary is chosen** | the authors' eight categories | the authors' term sets, audited by hand | **learned**: bigrams frequent in political texts and rare in non-political ones |
| **Scaled by** | all articles | all articles | length of the transcript |
| **Level** | world, 44 countries | country | **firm × quarter** |
| **Validation** | narrative, hand audit | large human audit of articles | correlation with EPU; firms with high PRisk lobby and donate more; cut investment and hiring |

**What Hassan et al. add.** Political risk becomes a **firm-level** variable — measured from what
managers and analysts actually discuss. Their striking finding is that most of the variation in
political risk is **across firms at a given time**, not common to all firms: aggregate indices like
EPU, however useful, miss most of the political risk an individual firm faces.

---

## 4. Reliability: how much do coders agree?

**Percent agreement** — the share of items both coders put in the same category — is intuitive and
misleading: two coders guessing at random will often agree, especially when one category dominates.

**Cohen's kappa** corrects for chance:

$$
\kappa = \frac{p_o - p_e}{1 - p_e}
\qquad
p_o = \frac{\text{agreements}}{N}
\qquad
p_e = \sum_k \frac{n_{A,k}}{N}\cdot\frac{n_{B,k}}{N}
$$

where $n_{A,k}$ is the number of items coder A put in category $k$.

**A worked example.** 40 headlines, three collapsed categories: not geopolitical (0), threat (1–5),
act (6–8).

| | **B: 0** | **B: threat** | **B: act** | **A total** |
|---|---:|---:|---:|---:|
| **A: 0** | **20** | 3 | 1 | 24 |
| **A: threat** | 2 | **8** | 0 | 10 |
| **A: act** | 0 | 1 | **5** | 6 |
| **B total** | 22 | 12 | 6 | 40 |

- $p_o = (20 + 8 + 5)/40 = 0.825$
- $p_e = (24\cdot22 + 10\cdot12 + 6\cdot6)/40^2 = 684/1600 = 0.4275$
- $\kappa = (0.825 - 0.4275)/(1 - 0.4275) \approx 0.69$

An 82.5% agreement becomes a kappa of about 0.69 once chance is removed. Conventions differ:
Landis and Koch's widely used labels call 0.61–0.80 "substantial"; Krippendorff, for his alpha (the
generalisation to more coders, missing data and other scales), asks for at least 0.800 for firm
conclusions and accepts 0.667 only for tentative ones.

**What to do with disagreement.** Never average it away. Read each disagreement, decide whether the
protocol was unclear or a coder erred, **revise the protocol**, and adjudicate. The disagreements are
where the concept is fuzzy — they are information.

---

## 5. Big data: what it adds, what it hides

GDELT monitors news in many languages worldwide and turns it into searchable records. Its promise is
**coverage and speed**: every country, every day, without a research assistant.

Its traps:

- **Selection.** Only what is reported, by sources GDELT monitors, in languages it processes. Coverage
  changes over time: a rising count may be more sources, not more events.
- **Duplication.** One wire story becomes hundreds of articles.
- **Machine coding.** Automated event coding misreads irony, quotation, and historical references.
- **"N = all" is never all.** A very large biased sample is still biased — and more confidently wrong.

**The rule for a risk analyst:** big data for **detection** (something is happening, here, now);
small, carefully coded data for **measurement** (how much, compared with what).

---

## 6. Composite indicators — the OECD/JRC discipline

A composite indicator combines several indicators into one number — country-risk ratings, governance
indices, your team's exposure index. The OECD/JRC *Handbook* (2008) sets out ten steps; the five
that decide most of the outcome are:

| Step | The choice | The risk |
|---|---|---|
| **Theoretical framework** | Which dimensions of risk, and why | An index of whatever data were available |
| **Missing data** | Drop, impute, or flag | Countries silently disappear — usually the risky ones |
| **Normalisation** | Min–max, z-score, rank, distance to a reference | Different methods, different rankings |
| **Weighting and aggregation** | Equal, statistical, expert; additive or geometric | Additive aggregation lets a strength **compensate** for a weakness |
| **Sensitivity analysis** | How much do results move when choices change? | A ranking presented as fact that one weight would overturn |

**Min–max normalisation** puts every indicator on 0–1, with the direction made consistent (higher =
more risk):

$$
x^{*} = \frac{x - \min x}{\max x - \min x}
\qquad\text{or, for an indicator where higher is safer,}\qquad
x^{*} = \frac{\max x - x}{\max x - \min x}
$$

**Weighted additive aggregation**: $\;CI = \dfrac{\sum_j w_j\, x^{*}_j}{\sum_j w_j}$.

**The point for the board.** Weights are value judgements. Show them; let the reader move them; and
report whether the ranking survives. A composite that hides its weights is an opinion dressed as a
measurement.

---

## 7. The Tableau skill of the day

- **Tableau Prep** (or the data source pane): parse a quarter string into a date; aggregate firm-
  quarters to quarters; union or join sources on a common key.
- A **highlight table** of coder A × coder B, with grand totals: the agreement matrix, read straight
  off the screen.
- **Normalisation with LOD**: `{ MIN([x]) }` and `{ MAX([x]) }` — a `FIXED` expression with no
  dimension computes over the whole table.
- **Parameters as weights**, and `RANK()` to show how the ranking moves when the weights do.

---

## References

Baker, S. R., Bloom, N., & Davis, S. J. (2016). Measuring economic policy uncertainty. *Quarterly
Journal of Economics*, 131(4), 1593–1636. https://doi.org/10.1093/qje/qjw024

Caldara, D., & Iacoviello, M. (2022). Measuring geopolitical risk. *American Economic Review*,
112(4), 1194–1225. https://doi.org/10.1257/aer.20191823

Hassan, T. A., Hollander, S., van Lent, L., & Tahoun, A. (2019). Firm-level political risk:
Measurement and effects. *Quarterly Journal of Economics*, 134(4), 2135–2202.
https://doi.org/10.1093/qje/qjz021

Krippendorff, K. (2018). *Content analysis: An introduction to its methodology* (4th ed.). SAGE.

Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data.
*Biometrics*, 33(1), 159–174.

OECD/JRC. (2008). *Handbook on constructing composite indicators: Methodology and user guide*. OECD
Publishing. https://doi.org/10.1787/9789264043466-en
