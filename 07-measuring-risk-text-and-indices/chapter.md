---
title: "Measuring Risk: How a Political Judgement Becomes a Number"
---

## The thermometer in the wrong room

Every geopolitical risk score that reaches a board has a pedigree, and the pedigree is usually
hidden. A consultancy reports that a country's risk has "risen to 71"; a bank's dashboard turns a
cell from amber to red; an index published by a central bank spikes in the week an invasion begins.
Each of these numbers is the last link of a chain that started with a concept nobody can observe
directly — the probability that politics will damage a firm's business — and passed through a
sequence of choices about texts, words, coders, units, weights and scales. The choices were made by
someone, for reasons, and most of them could have been made differently.

This chapter is about seeing that chain, so that a score one is sold can be audited and a score one
builds can be defended. Two words carry most of the weight, and they are worth fixing at the start.

::: {.definition}
[**Validity**]{.term} — the degree to which an indicator measures the concept it claims to measure.
Is the share of newspaper articles mentioning war threats a measure of geopolitical *risk*, or of
editors' attention to geopolitics, or of the number of journalists posted to a war zone?
:::

::: {.definition}
[**Reliability**]{.term} — the degree to which the same procedure, applied by someone else to the
same material, yields the same number. Would a second coder, following the same rules, put the same
article in the same category? Would the same dictionary, run next year on the same archive, return
the same count?
:::

The two are independent in one direction only. A measure can be perfectly reliable and entirely
invalid: a thermometer that everyone reads identically, hanging in the wrong room. It cannot be
valid without being reasonably reliable, because a measure that returns different numbers for the
same object is measuring, in part, the person who applied it. The history of measurement in the
social sciences is largely a history of trading one against the other — cheap, mechanical procedures
that are perfectly reliable and of uncertain validity, against slow human judgement that captures
meaning and disagrees with itself.

## The chain, link by link

Write the chain out once, so that its parts have names. A measure of geopolitical risk passes from
a **concept** ("geopolitical risk") to an **indicator** (the share of articles that discuss
geopolitical tensions), drawn from a **source** (a fixed set of newspapers), processed by a **coding
rule** (a list of words grouped into categories), summarised by an **aggregation** (a monthly share,
rescaled so that a base period averages 100) and delivered in a **presentation** (a line with spikes
labelled "9/11" and "Iraq invasion"). Every one of the risk measures in this course can be written
in that form, and every link is a place where the number can part company with the concept.

At the concept link, the danger is that nobody has said what is being measured. "Political risk" in
the business literature has meant expropriation, contract repudiation, currency inconvertibility,
civil unrest, regulatory change and, more recently, sanctions and export controls — things with
different causes, different probabilities and different remedies. An indicator that pools them may
be a reasonable summary of the newspapers and a poor guide to any one of the decisions it is meant
to inform.

At the indicator and source links, the danger is selection. Newspapers report what is new and
dramatic, in the countries their readers care about, in the language they print in. The ten
newspapers behind the Caldara–Iacoviello index are American, British and Canadian; a war in a
country with no correspondents may barely register. That is a property of the index, not a flaw, but
a user must carry it into every inference.

At the coding link, the danger is the gap between words and meaning: a rule that counts "war"
cannot tell a war from a price war or a trade war.

At the aggregation link, the danger is that choices about scaling and weighting, innocuous one at a
time, decide the result. A share of articles behaves differently from a count when the number of
articles changes; an average across countries weighted by GDP tells a different story from an
unweighted one. And at the presentation link — the one most often forgotten — the labels on the
spikes tell the reader what to see, and the absence of labels on the troughs tells them what not to.

::: {.archive}
[From the archive · Inferences from enemy propaganda, 1941–1945]{.archive-label}

The systematic analysis of text as evidence about political intentions did not begin with computers.
During the Second World War, analysts in the United States — among them a group at the Federal
Communications Commission's foreign broadcast monitoring service — read German radio propaganda not
for what it said but for what its saying implied. If the propaganda ministry began preparing the
public for a particular kind of news, what did the regime expect to happen? If a theme disappeared
from broadcasts, what had changed in the regime's own calculation?

Alexander George later reconstructed this work and asked how well the analysts' inferences had held
up once the German archives could be checked [@george1959]. His account made two points that every
risk analyst should know. The first is that the useful inferences were rarely about the *manifest*
content — the frequency of a word — and usually about what the content revealed of the speaker's
situation and purposes, which required a model of the speaker. The second is that the analysts were
most often wrong when they forgot that the text had been produced *for* an audience, by an actor with
reasons to mislead it. A newspaper is not a propaganda ministry, and an earnings call is not a
broadcast to a wartime public. But both are texts written by people with purposes, and an index built
from them inherits those purposes.
:::

## Content analysis: from reading to inference

The discipline that formalised these practices is content analysis. Its early textbook definition
called it a technique "for the objective, systematic, and quantitative description of the manifest
content of communication" [@berelson1952]. The modern definition, Krippendorff's, is broader and
more demanding.

::: {.definition}
[**Content analysis**]{.term} — a research technique for making replicable and valid inferences from
texts (or other meaningful matter) to the contexts of their use [@krippendorff2018]. Replicable: a
second analyst following the same procedure should reach the same result. Valid: the inference must
hold about the context, not merely about the texts.
:::

The shift from "description" to "inference" matters. Nobody builds a geopolitical risk index because
they want to know how often the word "missile" appears in newspapers. They want to infer something
about the world the newspapers describe — and, in the case of a multinational, about the likelihood
that the world will change in ways that touch the firm. The texts are evidence; the context is the
object.

Krippendorff breaks the procedure into steps, and they map cleanly onto both the published indices
and the coding exercise in this session. **Unitising** decides what a single unit is: an article in
the GPR and EPU indices, a transcript in Hassan and colleagues' measure, a headline in this session's
own coding. **Sampling** decides which units enter: every article in ten newspapers, every earnings
call of listed firms that hold one, forty headlines drawn at random from a news query. **Recording**
or coding assigns each unit to a category, by a dictionary or by human coders following a protocol.
**Reducing** summarises the codes — counts, shares, monthly averages. **Inferring** draws the
conclusion about the context: geopolitical risk is high this month; this firm faces unusual political
risk this quarter; the countries in which a firm operates are in the news for military build-ups
rather than for elections.

### Manifest and latent content

The distinction that does most of the work in practice is between what a text *says* and what it is
*about*. Manifest content is on the surface: the words, their frequency, their co-occurrence. Latent
content requires interpretation: whether a headline reports a threat or an act, whether a statement
is ironic, whether a reference to war is literal. Dictionaries read manifest content; human coders
can read latent content. The trade-off between them is the trade-off between reliability and
validity seen from another angle. A dictionary is perfectly reliable — run it twice and it returns the
same count — and blind. A human coder sees meaning, and two human coders see slightly different
meanings.

The best measures use both. They encode the analyst's judgement in a dictionary that a machine can
apply to millions of documents, and then audit the machine with humans who read a sample and check
whether the dictionary's classifications match what the texts are about. That design — a dictionary
audited by people — is common to all three of the indices this session examines, and the quality of
the audit is the best single guide to the quality of the index.

## Three dictionaries, three theories of risk

The three measures on the table share a family resemblance and differ in ways that matter.

| | **GPR** | **EPU** | **PRisk** |
|---|---|---|---|
| Text | newspaper articles | newspaper articles | earnings-call transcripts |
| Unit counted | articles containing geopolitical terms | articles containing economy *and* policy *and* uncertainty terms | political bigrams near synonyms of risk or uncertainty |
| Dictionary | authors' eight categories | authors' term sets, audited by hand | learned from political vs non-political texts |
| Scaled by | all articles | all articles | transcript length |
| Level | world; 44 countries | country; global aggregate | firm × quarter |

### Geopolitical risk as newspaper attention

Caldara and Iacoviello define geopolitical risk as the threat, realisation and escalation of adverse
events associated with wars, terrorism and tensions between states that affect the normal and
peaceful course of international relations [@caldara2022]. Their index counts, each month, the share
of articles in a fixed set of newspapers that contain words from eight categories: war threats,
peace threats, military build-ups, nuclear threats, terror threats, beginning of war, escalation of
war and terror acts. The first five form a sub-index of *threats*, the last three a sub-index of
*acts*. The series is rescaled so that its average over a base period equals 100, and national
indices are built by requiring that the article also mention the country.

The theory of risk embedded in this procedure is explicit: geopolitical risk is what informed
newspaper readers in a few large democracies are being told to worry about. The split between threats
and acts is not a technical detail. It distinguishes the risk that something will happen from the
fact that it has, and the two behave differently — threats can rise for months before an act, and an
act can resolve uncertainty as well as create it. The coding protocol of this session borrows the eight
categories, with a rule that acts beat threats.

### Policy uncertainty as a three-way conjunction

Baker, Bloom and Davis built the Economic Policy Uncertainty index on a different logic
[@baker2016]. An article counts only if it contains a term from each of three sets: one about the
economy, one about policy and one about uncertainty. The conjunction is the clever part. A filter on
"uncertainty" alone would capture weather and sport; a filter on "policy" alone would capture every
legislative report. Requiring all three narrows the count to articles that discuss uncertainty about
economic policy, at the cost of missing articles that discuss it without using any of the listed
words.

What distinguishes the EPU work methodologically is the audit. The authors had human readers code a
large sample of articles and compared the human judgements with the dictionary's, tuning the policy
term set to reduce errors in both directions — articles the dictionary flagged that humans judged
irrelevant, and articles humans judged relevant that the dictionary missed. The audit does not make
the index perfect. It makes its error rates *known*, which is the more useful property. The global
index used in this session is a GDP-weighted average of national indices; the data file offers two
weightings, current-price and purchasing-power-parity GDP, and the choice between them is a small
instance of the aggregation decisions discussed below.

### Political risk as what managers discuss

Hassan, Hollander, van Lent and Tahoun asked a question the newspaper indices cannot answer: how much
political risk does an *individual firm* face, and does it matter for what the firm does
[@hassan2019]? Their text is not newspapers but the transcripts of quarterly earnings conference
calls, in which senior managers present results and answer questions from analysts. The choice is
deliberate. An earnings call is the place where a firm's own leadership, under questioning from people
paid to find weaknesses, talks about what worries it.

Their dictionary is not written by hand. It is *learned*. The authors took a body of political texts
and a body of non-political texts and identified two-word combinations — bigrams — that are frequent
in the first and rare in the second. A bigram such as a reference to a particular kind of legislation
is political; a bigram such as a reference to a production process is not. They then counted, in each
transcript, the political bigrams that appear close to a synonym of "risk" or "uncertainty",
weighted them by how distinctively political they are, and divided by the length of the transcript.
The result, PRisk, is a firm-quarter measure of the share of the conversation devoted to political
risk.

::: {.definition}
[**Dictionary method**]{.term} — a measurement procedure that assigns texts to categories by
counting words or phrases from a pre-specified list. The list may be written by the analyst (GPR,
EPU) or learned from labelled texts (PRisk). Either way it is a theory of what the concept looks like
in language, and its validity depends on whether that theory holds in the texts to which it is
applied.
:::

The proximity requirement deserves a moment. Counting political bigrams alone would measure how much
a firm talks about politics — which may reflect opportunity as much as risk, or simply a chief
executive's interests. Requiring that the political language appear near the language of risk and
uncertainty turns a measure of political *attention* into a measure of political *risk*. It is the
same logic as EPU's three-way conjunction, applied at the level of a sentence rather than an article.
The authors also construct the companion measures in the data file — non-political risk, sentiment
and risk by political topic — so that a user can ask whether a firm's political risk moves
independently of its overall risk and its overall mood.

The dependence of a dictionary on its domain is not a hypothetical worry. Loughran and McDonald
showed that the general-purpose word lists then in common use classified much of the ordinary
vocabulary of corporate filings as negative — words such as "liability", "tax" or "cost" that in a
financial report are neutral descriptions — and built a finance-specific list in response
[@loughran2011]. Tetlock's earlier work on newspaper pessimism and stock prices had shown that a
dictionary measure of tone could carry real information about markets [@tetlock2007]. The two papers
together make the point that runs through this chapter: a dictionary can work, but only for the texts
it was built for, and its transfer to a new domain is an empirical question, not an assumption.

## What the firm-level measure found

Hassan and colleagues validated PRisk in three ways, and the structure of the validation is as
instructive as the result. First, the aggregate of PRisk across firms moves over time with the
newspaper-based EPU index, which is what one would expect if both capture the same underlying
variation in political uncertainty. Second, the measure picks out the topics one would expect at the
times one would expect — firms talk about political risk in a given domain when policy in that domain
is in motion. Third, and most persuasively, firms with high PRisk *behave* as theory predicts firms
facing political risk should behave: they cut investment and hiring, and they become more active
politically, lobbying more and donating more to politicians. A measure that predicted nothing about
behaviour would be a curiosity. A measure that predicts the behaviour the concept implies has passed a
test of validity that no amount of reliability could substitute for.

The finding that surprised the authors, and that matters most for a multinational, concerns where
the variation lies. Most of the variation in political risk is not common to all firms at a given
time, nor common to all firms in a sector; it is *specific to the firm*. Two companies in the same
industry, in the same quarter, can face very different political risk, because they sell to different
governments, depend on different regulations, source from different countries or hold different
licences.

The implication is uncomfortable for anyone who buys a country-risk score. An aggregate index —
however carefully built, however well audited — measures what is common. The political risk that
actually reaches a particular firm is mostly what is *not* common. A board that tracks a national
index and believes it is tracking its own exposure is watching the weather report for a region while
the risk is in the plumbing of its own building.

This is where the five channels used throughout the course earn their place. Political risk reaches a
multinational through **market access** (who may sell what to whom), **inputs** (what can be bought,
and from where), **finance** (who will lend, insure, settle), **assets and people** (what can be
seized, damaged or detained) and **data and operations** (what can be stored, transferred or shut
down). An index built from newspapers measures, at best, the climate in which these channels operate.
A firm-level measure such as PRisk measures how much a firm's own managers are worried, which
integrates the channels from the inside. Neither tells the firm which channel is exposed. That is the
job of the team composite index, built at the end of this chapter, which is assembled channel by
channel for a named firm.

## Two coders and a protocol

The obvious measure of reliability is **percent agreement**: the share of items on which two coders
chose the same category. It is intuitive and misleading. Two coders who never read the headlines and
simply assigned codes at random, in proportion to how often each category occurs, would agree often —
and very often if one category dominates. In a sample where four headlines in five are not about
geopolitics at all, two coders who both write "not geopolitical" for every item will agree on most of
them, while having measured nothing.

Cohen's coefficient corrects for this by comparing observed agreement with the agreement that chance
alone would produce, given each coder's own distribution of codes [@cohen1960].

::: {.definition}
[**Cohen's kappa**]{.term} — a measure of agreement between two coders on a nominal scale, corrected
for chance: $\kappa = (p_o - p_e)/(1 - p_e)$, where $p_o$ is the observed share of agreements and
$p_e$ the agreement expected if the two coders assigned categories independently at their own
marginal rates. A kappa of 1 is perfect agreement; 0 is agreement no better than chance; negative
values are worse than chance.
:::

The expected agreement is computed from the margins of the agreement table. If coder A puts
$n_{A,k}$ of $N$ items in category $k$ and coder B puts $n_{B,k}$ there, the chance that both pick
$k$ for the same item, if they choose independently, is the product of their shares; summing over
categories gives

$$
p_e = \sum_k \frac{n_{A,k}}{N}\cdot\frac{n_{B,k}}{N}.
$$

Take forty headlines, collapsed into three categories — not geopolitical, threat, act — with coder
A's codes in the rows and coder B's in the columns:

| | **B: 0** | **B: threat** | **B: act** | **A total** |
|---|---:|---:|---:|---:|
| **A: 0** | **20** | 3 | 1 | 24 |
| **A: threat** | 2 | **8** | 0 | 10 |
| **A: act** | 0 | 1 | **5** | 6 |
| **B total** | 22 | 12 | 6 | 40 |

The coders agree on the diagonal, $20 + 8 + 5 = 33$ items, so $p_o = 33/40 = 0.825$. Chance agreement
is $(24 \cdot 22 + 10 \cdot 12 + 6 \cdot 6)/40^2 = 684/1600 = 0.4275$. Kappa is therefore
$(0.825 - 0.4275)/(1 - 0.4275) \approx 0.69$. An agreement rate that sounds excellent — better than
four in five — shrinks by almost a fifth once the agreement the coders would have reached without
reading is removed. The shrinkage is driven by the dominant category: because both coders put more
than half the headlines in "not geopolitical", much of their agreement there was to be expected.

What counts as good enough is a convention, and the conventions differ. Landis and Koch proposed a
set of labels that have become widely used, under which values between 0.61 and 0.80 are
"substantial" [@landis1977]. Krippendorff, for his alpha — a generalisation that handles more than
two coders, missing data and ordinal or interval scales — asks for at least 0.800 before data are
relied on, and accepts values from 0.667 only for tentative conclusions [@krippendorff2018;
@hayes2007]. By the first convention the worked example is respectable; by the second it would
support only a tentative claim.

### What disagreement is for

The worst thing to do with disagreement is to average it away — to take the mean of two codes, or to
pick one coder's version at random. Disagreements are where the concept is fuzzy, and they are
information. Read each one. Some will be errors: a coder misread a headline, or forgot a decision
rule. Others will reveal that the protocol did not anticipate a case — a headline about sanctions, a
cyber operation, a military exercise that might be a build-up or might be routine. Those are the
valuable ones. The right response is to **revise the protocol**, write down the new rule, and then
adjudicate.

The protocol used in this session contains a deliberate gap of exactly this kind. Sanctions, export
controls and trade wars are not among Caldara and Iacoviello's eight categories, so the protocol
tells coders to assign them to "not geopolitical" and flag them. For a multinational in the 2020s,
that is a strange place for them to be. A headline about export controls on semiconductors may
matter more to a firm's inputs channel than a headline about a distant military exercise. The gap is
not a mistake in the GPR index, which measures what it says it measures; it is a reminder that an
index built for one purpose — tracking the risk of war and terrorism as perceived by newspaper readers
— may not be the index a firm needs.

## Big data: detection, not measurement

The coding exercise draws its headlines from the GDELT Project, which monitors news media worldwide in
many languages and turns them into searchable records. It is the most visible example of what is
usually called big data in political risk: a source that promises *coverage* — every country, every
day — and *speed*, without a research assistant reading anything.

The promise is real, and the traps are four. The first is **selection**. GDELT records what is
reported, by the sources it monitors, in the languages it processes. Its coverage of sources has
changed over time, so a rising count of articles about a country may mean more sources rather than
more events. The second is **duplication**: a single wire-service story is republished by hundreds of
outlets, and a naive count treats each republication as evidence. The third is **machine coding**:
automated classification of events misreads irony, quotation and historical reference, and errs in
ways that are not random — it is worse in some languages than in others, and worse for some kinds of
event. The fourth is the most seductive. "N = all" is never all. A very large sample drawn by a biased
process is still biased, and the large number only makes the estimate more confidently wrong.

The fourth trap has been formalised. Meng showed that the error of an estimate from a large
non-random sample depends on the correlation between being in the sample and the quantity being
measured, and that even a tiny such correlation can make a sample of millions worth less than a
small random sample [@meng2018]. The parable everyone cites is the story of a search-based model of
influenza that, after an initial success, substantially overestimated flu prevalence for long
stretches, because the behaviour generating the data changed while the model did not [@lazer2014].
Neither example is about geopolitics; both describe exactly what can happen to an event count built
from online news.

::: {.warn}
**More data is not better measurement.** A dataset of millions of machine-coded news records is a
sample drawn by a process nobody controls, measured with error nobody has fully characterised. Forty
headlines drawn at random from a well-defined query and coded by two people with a written protocol
can be more *valid* for a specific question — not because forty is more than millions, but because
you know what the forty are.
:::

The working rule for a risk analyst follows. Use big data for **detection**: something is happening,
here, now, and it is worth a closer look. Use small, carefully coded data for **measurement**: how
much is happening, compared with what, and whether it has changed. The two jobs are complementary. A
monitoring system that flags a spike in news about a firm's supplier country is doing detection well.
A board paper that reports that "risk in the supplier country has doubled" on the strength of the same
spike is doing measurement badly.

## Composite indicators and the arithmetic of judgement

The third measurement task of the session is the one that a multinational is most likely to perform
itself: combining several indicators into one number. Country-risk ratings, governance indices,
supplier-risk scores and the team's own exposure index are all composite indicators. They are
attractive for the same reason they are dangerous: they compress several dimensions into one figure
that a board can read at a glance, and they hide, in the compression, a series of decisions that
determine the ranking.

The standard guide is the handbook produced by the OECD and the European Commission's Joint Research
Centre [@oecd2008]. It sets out ten steps, from the theoretical framework to the presentation of
results. Five of them decide most of the outcome.

The **theoretical framework** says which dimensions of risk the index captures and why. Without one,
the index becomes a collection of whatever data were available — which is to say, an index whose
content was chosen by the data suppliers rather than by the analyst. For the team composite, the
framework is the five channels: each indicator must be defended as a measure of exposure through a
named channel, or it does not belong.

**Missing data** is where indices quietly lie. The country GPR indices cover 44 countries; the
country EPU indices about twenty. A composite that drops every country missing an indicator will
cover only large, well-documented economies — and the countries it silently drops are, very often, the
risky ones, about which fewer people write. Imputing a value is a claim about a country nobody
measured; flagging the gap is honest and less tidy. Whatever is chosen should be visible in the
output.

**Normalisation** puts indicators measured in different units on a common scale. The simplest method,
min–max, maps each indicator to the interval from 0 to 1:

$$
x^{*} = \frac{x - \min x}{\max x - \min x}
\qquad\text{or, where higher is safer,}\qquad
x^{*} = \frac{\max x - x}{\max x - \min x}.
$$

The second form matters more than it looks. The Worldwide Governance Indicators' measure of
political stability is scored so that higher means *more* stable; in a risk index it must be
inverted, or a stable country will score as risky. The indicators also changed scale in their 2025
edition, moving to a 0–100 score and recalculating their history, so that values from different
editions cannot be mixed; the methodology behind the indicators is set out in @kaufmann2011. Other
normalisations — z-scores, ranks, distance to a reference country — produce different rankings from
the same data, because they treat outliers and gaps differently. Min–max is sensitive to the
extremes: a single country with an extraordinary value compresses everyone else into a narrow band.

**Weighting and aggregation** combine the normalised indicators. The usual form is a weighted
average,

$$
CI = \frac{\sum_j w_j \, x^{*}_j}{\sum_j w_j},
$$

and the weights can be equal, derived statistically (from principal components, say), or set by
experts. Each choice is defensible and none is neutral. Equal weights are a judgement that every
dimension matters equally, which is rarely what anyone believes. Statistical weights reward the
indicators that move together, which may simply be the redundant ones. Expert weights encode the
expert.

The aggregation rule carries a further assumption that is easy to miss.

::: {.definition}
[**Compensability**]{.term} — the property of an aggregation rule under which a high score on one
dimension can offset a low score on another. Additive aggregation is fully compensatory: a country
with excellent governance and an active war can average to "medium". Geometric aggregation is
partially compensatory, penalising unbalanced profiles; non-compensatory rules rank countries without
allowing any trade-off at all.
:::

For a risk index, full compensability is often the wrong assumption. A firm does not experience the
average of a country's risks; it experiences the worst of them that touches its operations. Excellent
contract enforcement does not compensate for a plant inside a war zone. Additive aggregation is still
the default, because it is simple and transparent, but an analyst who uses it should be able to say
why the dimensions can trade off — or at least show the profile behind each score so that the reader
can see when they cannot.

::: {.archive}
[From the archive · The Human Development Index, 1990 and 2010]{.archive-label}

The most influential composite indicator of the past half-century was designed to argue with a single
number. The first *Human Development Report*, published by the United Nations Development Programme
in 1990 under the direction of Mahbub ul Haq, proposed the Human Development Index as an alternative
to ranking countries by income per head [@undp1990]. It combined three dimensions — a long and healthy
life, knowledge and a decent standard of living — each normalised against minimum and maximum values,
and averaged them with equal weights. Its authors were explicit that the index was a simplification
built to change a conversation, and it did.

Twenty years later the 2010 report changed the aggregation from an arithmetic to a geometric mean of
the three dimension indices and revised the indicators of education and income [@undp2010]. The
reason given was compensability: under the arithmetic mean, a country could make up for poor health
with high income, one for one; under the geometric mean, poor performance in one dimension weighs more
heavily. The change re-ranked countries. Ravallion then showed that the new formula implied
trade-offs between longevity and income that few would accept if they were stated openly — in effect,
valuations of an extra year of life that varied enormously with a country's income, and were very low
in the poorest countries [@ravallion2012].

The episode is a compact lesson in everything this section argues. The weights and the aggregation
rule were value judgements; changing them changed the ranking; and the implicit prices they carried
became visible only when someone did the algebra. A firm's exposure index embeds trade-offs of the
same kind — between, say, sanctions exposure and political instability — and the board deserves to
see them stated.
:::

## Sensitivity: the ranking that one weight overturns

The last of the decisive steps is the one most often skipped. **Sensitivity analysis** asks how much
the results move when the choices change: a different normalisation, different weights, a different
treatment of missing data, a different aggregation rule. Saisana, Saltelli and Tarantola set out how
to do this systematically, by treating each methodological choice as an uncertain input and examining
the distribution of ranks it produces [@saisana2005]. The simplest version needs no special software.
Record the ranking under equal weights; then under each indicator alone; then count how many
countries move by more than a few places. A country that stays near the top under every reasonable
choice is robustly high-risk. A country whose rank swings from fifth to twenty-fifth depending on one
weight is not "fifth"; it is a country about which the index has no firm opinion.

This is why the practice round builds the team composite with weights a reader can move. The point is
not interactivity for its own sake. It is that a composite which hides its weights is an opinion
dressed as a measurement, and a composite whose weights are visible and adjustable is an argument the
reader can test.

::: {.step}
**A minimal sensitivity report** for any composite: the ranking under the chosen weights; the
ranking under equal weights; the ranking under each indicator alone; the number of units whose rank
changes by more than a stated threshold; and a sentence on the unit most sensitive to the weights and
why.
:::

## A short review of the literature

::: {.lit}
Content analysis as a social-science method was codified in the mid-twentieth century. @berelson1952
gave the classic definition centred on manifest content, and @george1959 reconstructed the wartime
analysis of enemy propaganda that showed both the power and the dangers of inference from text.
@krippendorff2018 is the standard modern treatment, recasting the method around replicable and valid
inference and setting out the reliability apparatus; @hayes2007 make the case for Krippendorff's alpha
as a general standard. The chance-corrected agreement coefficient is @cohen1960, and the labels most
often attached to its values are @landis1977.

Automated text analysis in political science and economics has grown into a large literature.
@grimmer2013 is the essential warning and guide for political texts — their principle that automated
methods amplify rather than replace human reading, and must be validated for every application, is the
spine of this chapter. @gentzkow2019 survey text as data in economics. In finance, @tetlock2007 showed
that dictionary measures of media tone carry information about markets, and @loughran2011 showed how
badly general-purpose dictionaries misread specialised documents.

The three indices at the centre of the session are @caldara2022 for geopolitical risk, @baker2016 for
economic policy uncertainty and @hassan2019 for firm-level political risk; the last is notable both for
its learned dictionary and for its demonstration that most political risk is firm-specific. On big data,
@lazer2014 is the cautionary tale and @meng2018 the formal account of why sample size does not rescue a
biased selection process.

Composite indicators have their own methodological literature. @oecd2008 is the practitioner's
handbook and @saisana2005 the statement of sensitivity and uncertainty analysis as a quality test.
@kaufmann2011 document the Worldwide Governance Indicators, a composite of composites. The Human
Development Index [@undp1990; @undp2010] and the critique of its implicit trade-offs in @ravallion2012
are the clearest case study of how aggregation rules carry value judgements.
:::

## What the figure will not tell the firm

The practice round produces three figures — the firm-level measure against the newspaper-based one,
the team's own coded index and the draft composite for the team's firm — and each comes with a
sentence it does not license. The first comparison is two indicators of a similar concept built from
different texts, dictionaries and levels of aggregation; where they part company, the question is which
link of which chain explains the gap.

The line of average firm-level political risk set against policy uncertainty does not tell a
particular multinational how much political risk *it* faces. It is an average over listed firms that
hold earnings calls in English, which is mostly to say American listed firms, over a period that ends
in early 2022. The most important finding of the paper it replicates is that most of the variation in
political risk is specific to the firm — and that is precisely the variation an average removes. A
board can use the line to see when political uncertainty was high for corporate America as a whole; it
cannot use it to see its own exposure, which would require scoring its own calls, or at least those of
its closest peers.

The team's coded index, with its kappa, does not license a claim about how geopolitical the news about
a country is. It is forty headlines from a three-month window of an online news monitor whose sources
are weighted towards English-language media, coded against a protocol that by design places sanctions
and export controls outside geopolitics. What it licenses is a statement about how reliably two
trained readers can apply that protocol — and a list of the places where the protocol needs to change
before anyone relies on it.

The composite exposure index does not license a ranking presented as fact. It licenses a ranking
*under stated weights*, together with the weight that would overturn it. The question to carry into
the practice round, and into every risk score a multinational is sold, is the five-part audit this
chapter has built: what concept, from which sources, coded by whom or by what, normalised and weighted
how, and how sensitive to each of those choices. A score that can answer all five is a measurement. A
score that cannot is somebody's opinion, with decimals.
