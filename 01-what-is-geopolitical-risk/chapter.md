---
title: "What Is Geopolitical Risk? Counting the Threat Before the War"
---

## A question about counting

Every risk function in every multinational firm already has a view about geopolitics. It sits in
the annual report, in the paragraph on principal risks; it sits in the treasury's hedging policy, in
the procurement team's list of single-source suppliers, in the country manager's sense of which
visas will be hard to renew next year. What it rarely has is a *number* — and when it does, the
number usually comes from somewhere else, built by someone else, for a purpose the firm never
examined.

This course begins with a deliberately narrow question: before a firm can manage geopolitical risk,
what exactly is it counting? The question sounds pedantic. It is not. A board that is told
"geopolitical risk is at its highest level in forty years" has been told something precise about a
particular index, constructed from particular newspapers, normalised to a particular base period.
Whether that statement should change a capital-expenditure plan in Monterrey or a supplier
contract in Penang depends entirely on what was counted, and the person presenting the slide often
does not know.

The answer this chapter builds towards is that geopolitical risk is not one thing to be measured
but a family of things, each visible to some instruments and invisible to others. We start with the
oldest distinction in the subject, between risk and uncertainty; separate three kinds of risk that
are routinely confused; sort the instruments that try to measure them into six families; and then
take one instrument apart in detail — the Geopolitical Risk index of @caldara2022, the big work of
this session and the target of its replication. The chapter closes on what that index cannot tell a
firm, because a measure whose limits you cannot state is a measure you should not use.

## Risk, uncertainty, and the ground in between

The modern vocabulary starts in 1921, with an economist trying to explain where profit comes
from.

::: {.archive}
[From the archive · Knight, 1921]{.archive-label}

Frank Knight's *Risk, Uncertainty and Profit* began as a doctoral dissertation at Cornell and was
published in 1921. Its problem was a theoretical embarrassment: in a perfectly competitive economy
with full information, competition should drive profit to zero, yet profit plainly exists. Knight's
answer was that some of what businessmen face can be reduced to known odds and therefore insured,
pooled or priced into costs — and some cannot.

The first he called *risk*: a situation in which the distribution of outcomes is known, either a
priori, as with dice, or statistically, from the experience of many similar cases, as with fire
insurance. The second he called *uncertainty*: a situation that is unique enough that no such
distribution can be formed, and in which the decision-maker must act on judgement. Risk, being
insurable, becomes a cost like any other. Uncertainty cannot be shifted to an insurer, and it is
the bearing of uncertainty — the entrepreneur's willingness to commit resources on a judgement no
one can verify in advance — that profit rewards [@knight1921].

A century later, the distinction is quoted more often than it is read, and usually as a
binary. Knight's own treatment was more graded: what matters is whether instances can be grouped
into classes homogeneous enough to support an estimate. That is precisely the question a
geopolitical risk analyst faces every morning.
:::

::: {.definition}
[**Risk**]{.term} (in Knight's sense) — a situation in which the probabilities of outcomes can be
estimated, from theory or from the experience of sufficiently similar cases, so that the exposure
can be priced, pooled or insured.
:::

::: {.definition}
[**Uncertainty**]{.term} (Knightian uncertainty) — a situation in which no reliable probability
distribution over outcomes can be formed, because the case is too unlike any class of past cases.
It cannot be insured away; it can only be judged.
:::

Geopolitics lives in the ground between the two. A shipping insurer pricing piracy off the Horn of
Africa is close to Knightian risk: there are thousands of transits, hundreds of incidents, and a
market for war-risk premiums that updates as the incidents accumulate. A board asking whether a
particular strait will be blockaded within five years is close to Knightian uncertainty: there have
been blockades, but never this one, by this state, against this coalition, with these weapons.
Wars recur, coups recur, sanctions recur — the categories are populated — but each instance is
unlike the last in ways that matter for the estimate.

The honest description of this course is that it is an attempt to move questions from the second
category towards the first, and to be candid about how far they move. Every index you will
replicate is a device for grouping unlike events into classes so that something can be counted.
Grouping is never neutral. When the Geopolitical Risk index counts an article about a nuclear test
and an article about a terrorist bombing as two instances of the same thing, it has made a
modelling choice about what is homogeneous. When the Correlates of War project averages steel
output and population into one number for "power" (Session 03), it has made another. The skill
the course tries to teach is not to avoid these choices — no measurement is possible without them
— but to see them, state them, and ask what they do to the conclusion.

There is a practical corollary for the firm. Knightian risk can be transferred: political-risk
insurance, war-risk cover on cargo, credit insurance on export receivables are all markets for it.
Knightian uncertainty cannot be transferred, only managed — by flexibility, by diversification, by
keeping options open, by being willing to pay for the ability to change one's mind. Much of the
strategic response to geopolitical change that firms now describe as "resilience" is, in Knight's
terms, an admission that the relevant exposures are uncertain rather than risky, and that the
premium has to be paid in redundancy because there is no one to pay it to.

## Three kinds of risk, and the layer that comes from outside

The second distinction is between three phrases that firms, consultancies and journalists use
almost interchangeably: political risk, country risk and geopolitical risk. They answer different
questions, attach to different units of analysis, and call for different instruments.

::: {.definition}
[**Political risk**]{.term} — the possibility that the government of a host country changes the
rules applying to a foreign firm in a way that reduces the value of its investment: expropriation,
forced renegotiation, discriminatory taxation, licence withdrawal, restrictions on repatriation.
Its natural unit is the firm in a host country.
:::

::: {.definition}
[**Country risk**]{.term} — the possibility that a country as a whole fails to pay, convert or
transfer: sovereign default, capital controls, currency inconvertibility, a banking crisis. Its
natural unit is the country, and its natural user is the lender.
:::

::: {.definition}
[**Geopolitical risk**]{.term} — the possibility that relations *between* states and other
political actors move against the firm: war, terrorism, sanctions, export controls, the formation
of blocs, state-sponsored cyber operations. Its natural unit is the international system or a pair
of states, and it frequently originates outside any country in which the firm operates.
:::

Political risk is the oldest of the three in the international business literature, and its
archetypes are dramatic. When Mexico nationalised the assets of foreign oil companies in 1938, or
Iran nationalised the Anglo-Iranian Oil Company in 1951, the threat came from the host government
and fell on identifiable foreign firms. The scholarly literature that grew up in the 1960s and
1970s, as decolonisation multiplied the number of host governments and expropriations became
frequent, was preoccupied with this kind of event. Its classic synthesis is @kobrin1979, who
reviewed a decade and a half of work and complained that "political risk" was used to mean too many
things — sometimes the political event itself, sometimes the instability of a regime, sometimes the
consequences for a firm's operations — and that the literature rarely connected the first to the
last.

Kobrin's lasting contribution was to insist that risk is a property of the relationship between an
environment and a particular firm, not of the environment alone. Political instability in a
country matters to a foreign investor only through specific *contingencies* that affect specific
operations; a coup that changes nothing about the mining code may be irrelevant to the mining
company, while a quiet amendment to a tax treaty may be decisive. From this followed the
distinction between **macro** risk, which affects all foreign firms in a country, and **micro**
risk, which falls on a sector, an industry or a single firm. Expropriation of every foreign asset
after a revolution is macro; a windfall tax on telecommunications operators is micro.

Country risk grew from a different root — the bank lending of the 1970s to developing-country
governments, and the debt crisis that followed in the 1980s. Its question is whether a country, as
an economic and financial unit, will service its obligations and let money move. Its instruments are
sovereign ratings, debt-sustainability analysis and the spreads on sovereign bonds and credit
default swaps. It cares less about what the government will do to a particular investor than about
whether the treasury will have the dollars.

Geopolitical risk adds a third layer that neither of the earlier traditions was designed to see:
risk that originates *outside* the host country. A Canadian firm operating in Vietnam can be hurt by
a decision taken in Washington about Chinese inputs, by a decision in Beijing about rare-earth
exports, by a decision in Brussels about which payment systems may be used for which counterparties,
or by a naval incident in a sea lane neither Canada nor Vietnam controls. The host government may
be perfectly stable and perfectly friendly; the threat travels through the firm's suppliers,
customers, banks and networks.

The three are not mutually exclusive, and the clearest way to see that is a single case. Take a
Canadian bank with a subsidiary in Moscow in February 2022. It faces *political* risk when the host
state restricts the ability of foreign firms to sell their assets and leave. It faces *country*
risk when capital controls trap the subsidiary's earnings and the rouble's convertibility is
suspended for foreigners. And it faces *geopolitical* risk in its purest form when its own
government, acting with its allies, forbids transactions on which the subsidiary depends. All
three arrive in the same quarter; they arrive through different channels; and they call for
different responses — a write-down, a liquidity plan, a compliance review. A risk function that has
only one of the three words in its vocabulary will see one-third of the problem.

## Six ways of counting

If geopolitical risk is a family of phenomena, it is measured by a family of instruments, and the
instruments disagree. It helps to sort them by *what they count*, because what an indicator counts
determines what it cannot see.

| Family | What it counts | Examples in this course | Strength | Blind spot |
|---|---|---|---|---|
| **Event-based** | things that happened, coded from reports | cyber incidents (S08), sanctions episodes (S10) | concrete, datable | only what was reported and coded |
| **Text-based** | how much the press or firms talk about a risk | GPR (today), EPU, firm-level risk (S07) | timely, long, high-frequency | measures attention, not exposure |
| **Expert-based** | scores assigned by analysts or surveys | governance indicators, commercial ratings | reaches latent concepts | opaque, sticky, perception-driven |
| **Structural** | slow-moving features of the system | material capabilities (S03), trade dependence (S04, S11) | explains *why* | rarely says *when* |
| **Market-based** | prices that embed risk | sovereign CDS spreads, implied volatility | forward-looking, daily | mixes risk with risk appetite |
| **Firm-level** | risk as perceived by firms themselves | earnings-call text (S07), disclosed exposures | speaks to the decision | self-reported, listed firms only |

*Event-based* indicators record occurrences — a war began, a sanction was imposed, an intrusion
was attributed — coded by researchers from reports. They are concrete, but they see only what was
reported and coded, and they are backward-looking: a threat never carried out leaves no event.
*Text-based* indicators count words. The Geopolitical Risk index is one; the Economic Policy
Uncertainty index of @baker2016 is its older sibling; the firm-level political-risk measure of
@hassan2019 applies the idea to earnings calls. Text is abundant, long and timely, but it measures
*attention*: how much the writers thought a subject worth discussing, which is related to, but not
the same as, how much risk any particular reader faces.

*Expert-based* indicators ask people to score what cannot be observed directly — the rule of law,
the likelihood of political violence. The Worldwide Governance Indicators aggregate many such
sources [@kaufmann2011]. They reach latent concepts, at the price of opacity, stickiness and shared
perceptions. *Structural* indicators — the distribution of capabilities, the concentration of a
country's imports — explain *why* a situation is fragile but rarely *when* the fragility will
matter, which is the question a firm is usually paid to answer. *Market-based* indicators are
prices, bets placed by people with money at stake; but a price combines the quantity of risk with
the appetite for bearing it, and a spread can widen because danger rose or because investors grew
more fearful of the same danger. *Firm-level* indicators record what the people who allocate
capital say worries them; they are also self-reported, shaped by liability and investor relations,
and available almost only for listed firms.

No family is enough on its own. The team project in this course requires a risk assessment that
**triangulates** across at least three, and the reason is not that more is better. It is that the
families fail in different ways, so their disagreements carry information. When the text is calm
and the market is not, someone may be pricing something the press has not yet seen. When the
structure is fragile and the events are quiet, risk is accumulating rather than absent. When the
experts are alarmed and the firms are not, either the exposure is concentrated in a few firms or
the experts are behind. A single index can only tell you its own story; three indices that quarrel
force you to say which one you believe, and why.

## How a newspaper archive becomes an index

The rest of the chapter takes one text-based instrument apart. Dario Caldara and Matteo Iacoviello,
economists at the Federal Reserve Board, published the Geopolitical Risk index in the *American
Economic Review* in 2022, after circulating it for several years as a working paper. It has become
the default series for anyone — central bank, investment bank, consultancy or doctoral student —
who needs a number for geopolitical risk. That ubiquity is the reason to understand its
construction exactly.

### The definition

The authors begin with a definition, and it is worth copying word for word, as the pre-session
asked you to do. Geopolitical risk is "the threat, realization, and escalation of adverse events
associated with wars, terrorism, and any tensions among states and political actors that affect
the peaceful course of international relations" [@caldara2022].

Read it for what is in and what is out. *In* are threats as well as realisations — the index is
meant to rise when war becomes more likely, not only when it starts. *In* are non-state actors:
"political actors", not only states, which is how terrorism enters. *In* are tensions short of war.
*Out* are domestic politics, elections, regulation and economic policy, which belong to other
indices. The definition is therefore closer to the third row of the typology above than to the
first two: it is about relations between actors, not about what a host government does to a firm.

::: {.definition}
[**Geopolitical Risk (GPR) index**]{.term} — a monthly text-based index, constructed by
@caldara2022, equal to the share of articles in a fixed set of major newspapers that discuss
adverse geopolitical events and threats, rescaled so that its average over a base period equals
100.
:::

### Four steps

The construction has four steps, and each is a decision that could have been taken differently.

**The corpus.** The recent index, from 1985, is built from the electronic archives of ten leading
newspapers published in the United States, the United Kingdom and Canada. The historical index,
from 1900, uses three American newspapers whose archives reach that far back. Already the scope is
clear: this is the anglophone press of three allied countries, and the historical series is the
American press alone.

**The dictionary.** An article counts as a GPR article if it contains words from one of eight
categories: war threats, peace threats, military build-ups, nuclear threats, terror threats, the
beginning of war, the escalation of war, and terror acts. In most categories, the search requires
a combination — a word for the threat and a word that anchors the article to geopolitics — so that
an article about a "price war" or a "threat" to a football team's league position does not
qualify. Designing such a dictionary is a trade-off between precision (only relevant articles) and
recall (all relevant articles), and it is the step on which most of the paper's validation effort
is spent.

**The share.** For each month, the number of GPR articles is divided by the total number of
articles published. The division matters more than it looks. Newspapers grow and shrink; their
archives are digitised unevenly; the number of articles a newspaper publishes in a month changes
for reasons that have nothing to do with geopolitics. A raw count would rise whenever the archive
grew. The share does not care how large the newspaper is, only what fraction of its attention went
to war and terror.

**The normalisation.** Finally the share is rescaled so that its average over 1985–2019 equals 100.
The historical index is normalised to its own average over 1900–2019. A reading of 300 therefore
means that, in that month, the share of articles discussing geopolitical threats and acts was three
times its average over the base period. It does not mean that risk was three times higher in any
sense a probability could express; it means that attention was.

::: {.warn}
**The misconception to drop now.** A high GPR reading does not mean that risk is high *for your
firm*. It means that the anglophone press was writing a great deal about geopolitical tension that
month. The second statement is what the index measures; the first is an inference that requires
everything else in this course.
:::

### Threats and acts

The eight categories are split into two groups. The first five — war threats, peace threats,
military build-ups, nuclear threats, terror threats — form the **GPR Threats** sub-index. The last
three — the beginning of war, the escalation of war, terror acts — form **GPR Acts**. The split is
the most useful thing in the paper for a firm, because the two need not move together. Threats can
build for months before anything happens, and they can subside without anything happening at all.
Acts can arrive with almost no prior threat, as a terrorist attack usually does.

The authors report that threats, and not only realised acts, depress economic activity. For a firm,
that finding has a blunt implication: you do not need the war to pay its cost. If what moves
investment is the threat, then the cost is borne in the months of tension, by firms that delay,
hedge and wait, whether or not the feared event ever occurs.

::: {.archive}
[From the archive · The Cuban missile crisis, 1962]{.archive-label}

In mid-October 1962, photographs taken by American U-2 reconnaissance aircraft showed Soviet
medium-range ballistic missile sites under construction in Cuba. On 22 October President Kennedy
announced the discovery in a televised address and a naval "quarantine" of the island. For the
next six days the two nuclear powers negotiated in public and in private while ships approached the
quarantine line. On 28 October Khrushchev announced that the missiles would be dismantled and
returned to the Soviet Union; the United States pledged not to invade Cuba and, privately, agreed to
withdraw its own Jupiter missiles from Turkey.

No war began. No shot was exchanged between the principal forces. In the categories of the GPR
dictionary, the crisis is almost entirely *threats*: nuclear threats, military build-ups, war
threats. It is also one of the episodes at which the historical index spikes, which is why the
practice round asks you to annotate it alongside the two World Wars and Korea.

The episode makes two points at once. First, it is a case in which the index is doing exactly what
its definition promises — registering the threat of adverse events, not only their realisation.
Second, it is a case in which the risk was arguably greatest at a moment, not over a month: the
crisis lasted thirteen days. A monthly index records it as one high observation. A firm deciding
whether to load a ship that week needed a finer clock.
:::

### Country-specific indices

For several dozen countries, the authors also publish country-specific series: the same search,
restricted to articles that also mention the country. In the monthly file these are the `GPRC_`
columns, one per country identified by its three-letter ISO code. They are not normalised to 100;
they are the percentage of articles that both discuss geopolitical risk and mention the country.
They measure, in other words, how much the anglophone press associates a given country with
geopolitical tension. That is useful, and it is also a very particular thing: a country can be the
*source* of tension, its *victim*, its *mediator* or merely its *location*, and the count does not
distinguish them.

## Does it measure something real?

A text-based index is a hypothesis about the world: that the frequency of certain words in certain
newspapers tracks a phenomenon of interest. The paper tests the hypothesis in three ways, and
reading them is the best training this course offers in how to evaluate an index you did not build.

The first is **narrative**. The index should spike when, on any reasonable reading of history, the
world's geopolitical tension spiked: at the outbreak of the two World Wars, the Korean War, the
Cuban missile crisis, the Gulf War, the attacks of 11 September 2001, the invasion of Iraq in 2003,
the Russian invasion of Ukraine in 2022. It does. This is a necessary test and a weak one: any index
that failed it would be discarded, but many indices would pass it, including some that measure
something other than what is claimed.

The second is **audit**. The authors drew samples of articles flagged by the dictionary and had them
read by people, to estimate how often the algorithm counted an article that a human would not
consider to be about geopolitical risk, and how often it missed one that a human would. A text
measure whose false-positive rate is unknown is a measure whose movements cannot be interpreted;
the audit is what licenses the claim that the counted articles are, for the most part, about what
they are supposed to be about.

The third is **economic content**. If the index measures something real, it should be related to
economic outcomes in the ways theory predicts. The paper finds that higher geopolitical risk
predicts lower investment and employment, and that the effect is stronger in industries more
exposed to geopolitical risk. That is the bridge to the firm, and the subject of the next section.

None of the three tests establishes that the index measures *risk* in Knight's sense — a probability
of adverse outcomes. What they establish is that it measures *attention to geopolitical adversity*,
that this attention is concentrated in the right months, that the counted articles are mostly about
the right things, and that the attention is associated with economic decisions. That is a
considerable achievement. It is also a narrower one than the word "risk" in the name suggests, and
the gap between the two is where the misuse of the index lives.

## Why waiting has value

Why should a firm's investment fall when the newspapers write about war, if the war has not yet
begun and may never begin? The answer comes from the theory of irreversible investment under
uncertainty, and it is one of the few results in economics that every manager already knows
intuitively.

::: {.definition}
[**The real-options channel**]{.term} — when an investment is costly to reverse and its payoff
depends on information that will arrive later, the opportunity to wait has value; an increase in
uncertainty raises that value and so leads firms to postpone investment, hiring and entry, even if
expected returns are unchanged.
:::

@bernanke1983 made the argument for cyclical investment: a firm choosing between investing now
and waiting for news gives up some return by waiting, but avoids the possibility of having sunk
capital into a project that the news would have shown to be a mistake. Because the investment is
irreversible — a plant cannot be un-built at its cost — the bad outcomes weigh more heavily in the
decision than the good ones, and more uncertainty about the bad outcomes makes waiting more
attractive. @dixit1994 gave the idea its general treatment, borrowing the mathematics of financial
options: an unexercised investment opportunity is like a call option, and exercising it early
destroys the option's time value.

@bloom2009 turned the theory into a macroeconomic prediction and tested it: a spike in uncertainty
should produce a rapid drop in hiring and investment as firms pause, followed by a rebound as the
uncertainty resolves and pent-up decisions are taken. The pause-and-rebound pattern is the
fingerprint of the real-options channel, and it is what distinguishes uncertainty effects from a
simple loss of confidence about the level of future demand. Political uncertainty has been shown to
work the same way: @julio2012 find that corporate investment falls in the period before national
elections, when the identity of the next government is unknown, and recovers after it.

Geopolitical risk is a natural candidate for the same mechanism, and it fits the threat-versus-act
distinction exactly. A threat raises uncertainty about future states of the world without yet
changing the present one; it is the purest form of the shock the real-options model describes.
Caldara and Iacoviello's finding that threats depress investment is, read this way, an application
of Bernanke's 1983 argument to a new source of uncertainty.

The firm-level implication is concrete. The decisions most exposed to geopolitical threats are
those that are large, lumpy and hard to reverse: a greenfield plant, an acquisition, a long-term
supply contract with take-or-pay terms, a decision to localise production for one market. The
decisions least exposed are those that can be scaled up and down: inventory, temporary staff,
contract manufacturing. A firm that wants to keep investing through a period of geopolitical
tension is, in effect, paying to convert the first kind of decision into the second — leasing
rather than building, dual-sourcing rather than committing, staging an investment in tranches with
exit points. That conversion has a cost, and the measure of what the firm is willing to pay for it
is a measure of how much it believes the tension is uncertainty rather than noise.

The classroom question that closes the lecture is this: in March 2022, with the GPR index several
times its long-run average, you run a Canadian fertiliser exporter. What do you do differently this
month? "Monitor the situation" is not an answer. A real answer names a decision — hedge the
currency, delay the warehouse in Europe, reroute shipments, sign longer contracts with customers who
have lost a Russian or Belarusian supplier — and names the threshold that would trigger it. The
index can be an input to that threshold. It cannot be the threshold, because it says nothing about
the exporter in particular.

## From the system to the profit and loss account

The real-options channel explains why aggregate investment responds to geopolitical risk. A firm
needs something more specific: the routes by which a change in relations between states reaches
*its* costs, revenues and assets. This course uses five, and they return in every session.

| Channel | How it reaches the firm | An example | Where it returns |
|---|---|---|---|
| **Market access** | tariffs, quotas, bloc-based trade diversion, procurement bans | a market closes to firms from a rival bloc | Session 04 |
| **Inputs** | a critical input or service controlled by a foreign state or a single provider | a critical service from one satellite operator | Session 11 |
| **Finance and payments** | sanctions on banks, asset freezes, exclusion from payment networks | a correspondent bank exits a jurisdiction | Session 10 |
| **Assets and people** | conflict, expropriation, evacuation, detention | staff evacuated, a plant abandoned | Sessions 03, 05 |
| **Data and operations** | state-sponsored cyber operations, data-localisation demands | operations halted by an intrusion | Session 08 |

The channels matter because the same geopolitical event reaches different firms through different
channels, and therefore with different magnitudes and different timing. A war in a grain-exporting
region reaches a food processor through *inputs*, a shipping line through *assets and people* and
the insurance market, a bank through *finance and payments*, and a software firm through *data and
operations* when the conflict spills into cyberspace. A global index records one event. A firm's
exposure is a vector, and the index is a scalar.

The channels also tell you which data to look for. Market-access exposure is visible in the
geographic breakdown of revenue that most listed firms publish. Input exposure is visible, if at
all, in the supply-chain maps that firms are increasingly asked to produce by regulators and
customers. Financial exposure sits in the treasury: which banks, which currencies, which payment
routes. Asset exposure sits in the fixed-asset register and the list of staff posted abroad. Data
exposure sits with the chief information security officer. A geopolitical risk assessment that
does not ask each of these offices a question is a geopolitical risk assessment written from the
newspaper.

## What the index cannot see

The practice round ends every week with "the catch": one sentence saying what the figure you have
just rebuilt does *not* license a multinational to conclude. This session supplies the template,
and the GPR index supplies at least four limits.

The first is that it measures **attention in the anglophone press**. The newspapers are American,
British and Canadian. Their editors decide what is news for their readers, and their readers are
not in Abidjan or Shenzhen. A violent dispute that dominates the regional press of West Africa can
leave the index untouched; a crisis involving the United States can dominate it. The index is
therefore partly a measure of what is geopolitically salient *from the perspective of three allied
countries* — which is a legitimate thing to measure, and which is not the same as the risk faced by
a subsidiary elsewhere.

The second is that it is **global**. One number per month for the whole world cannot distinguish a
risk that falls on the Baltic from one that falls on the Taiwan Strait, and for most firms that
distinction is the whole question. The country indices help, but only for the countries the
newspapers write about often enough to produce a stable series, and only in the sense of
"mentioned together with tension".

The third is that **attention fades while risk persists**. Newspapers cover change. A frozen
conflict — an unresolved territorial dispute, a ceasefire line, a sanctions regime in its tenth year
— can be a constant and material risk for firms operating near it while generating ever fewer
articles. On the index, a persistent risk looks like a declining one. This is the most important
limit for a firm, because firms often hold assets for longer than editors hold attention.

The fourth is that the index is **not a forecast**. It rises with events and with threats as they
are reported. It does not tell you what the next event will be, or when. Its predictive content for
investment arises because firms *respond* to the same reported threats; that is a statement about
behaviour, not about the probability of war.

A fifth, which the lecture invites you to supply, can be drawn from the construction itself. The
denominator is all articles: if newspapers devote their space to an election or a pandemic, the
geopolitical share can fall with no change in geopolitics. Each such limit is a reason to
triangulate.

## How a concept becomes data

The practice round follows a sequence that recurs in every session. A concept — geopolitical
risk, defined in words — becomes an *operational definition*: the eight
categories of the dictionary, the ten newspapers, the share, the base period. The operational
definition becomes a *dataset*: a spreadsheet, published by the authors, with one row per month and
columns for the recent index, its threats and acts components, the historical index and the country
series. The dataset becomes a *figure*. And the figure becomes an *argument*, the moment someone
puts it on a slide in front of a board.

Every link in that chain is a place where meaning can be lost. Between concept and operational
definition, everything the dictionary does not capture is dropped. Between operational definition
and dataset, the series is revised — the index is updated monthly and the authors refine it, so
the values you download need not equal the values printed in the paper. Between dataset and figure,
choices of frequency, smoothing and axis change what the eye sees: the same series averaged by
year loses most of its spikes, because a geopolitical shock is a monthly phenomenon and a yearly
average buries it. And between figure and argument, the slide's title replaces the paper's caveats.

That is why every practice round in this course has the same rule: the deliverable documents at
least one place where the data disagreed with the paper. The disagreement is not a failure of the
replication. It is evidence that you looked.

## A short review of the literature

::: {.lit}
The distinction between measurable risk and unmeasurable uncertainty is due to @knight1921, and it
remains the vocabulary of the field even where the measurement it describes has moved on. In
international business, political risk became a subject in its own right in the 1960s and 1970s,
when expropriations were frequent; @kobrin1979 is the synthesis that defined it as a property of the
firm–environment relationship rather than of the environment alone, and that distinguished macro
from micro risk. Later work moved from case-based assessment to measurement: @henisz2000 built an
index of political constraints on policy change from the structure of political institutions, and
@jensen2003 showed that democratic regimes attract more foreign direct investment, consistent with
their greater credibility towards investors. The expert-based tradition is summarised in the
methodology of the Worldwide Governance Indicators [@kaufmann2011]. @bremmer2009 wrote the
practitioner's case for treating political knowledge as an investment input.

The economics of why uncertainty matters for investment runs from @bernanke1983 through the
real-options synthesis of @dixit1994 to the empirical work of @bloom2009, who showed that
uncertainty shocks produce a sharp fall and rebound in activity. @julio2012 documented the same
mechanism for political uncertainty around elections.

The measurement of uncertainty from text is the most recent strand. @baker2016 built the Economic
Policy Uncertainty index by counting newspaper articles that combine terms for the economy, policy
and uncertainty, and validated it by human audit — the template @caldara2022 followed for
geopolitical risk, adding the split between threats and acts, a historical series to 1900, and
country-specific indices. @hassan2019 moved the method from newspapers to the firm, measuring each
company's political risk from the transcripts of its own earnings calls — the measure Session 07
replicates.

The through-line is a shift of the unit of analysis: from the host country, to the system, and
back to the firm. The indices have become better at counting what is said. Whether what is said
is what a firm is exposed to remains the open question.
:::

## Into the practice round

The practice round rebuilds the paper's central figure: the monthly GPR index since 1985 with its
spikes labelled, then its historical counterpart since 1900, then the threats and acts sub-indices
on one axis. The steps are in the brief that follows. What this chapter adds is the question to
hold while you build.

When you place a reference line at 100, remember that it is the base-period average of a share of
newspaper articles, and that the two series you plot are normalised to different base periods. When
you annotate the spikes, check the months yourself rather than trusting any list, and ask which
episodes were mainly threats and which mainly acts. When you compare your figure with the paper's,
expect differences — the series is revised — and record one. And when you change the monthly view
to a yearly average, watch which spikes disappear, because that is a demonstration, on your own
screen, that a measurement choice can erase the phenomenon the index was built to see.

Then write the catch. Not a criticism of Caldara and Iacoviello, whose index does what it says,
but a sentence about a firm: what this figure does not license a multinational to conclude. The
strongest answers will name a channel and a place — a supplier, a subsidiary, a payment route —
that a global count of anglophone newspaper articles cannot see. That sentence is the first entry
in the risk register your team will build for its multinational over the term, and the next eleven
sessions are, in a sense, a sequence of instruments designed to see what this one misses.
