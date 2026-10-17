---
title: "Cyber Geopolitics: Restraint, Rivals and Weaponised Networks"
---

## The war that was supposed to happen

For most of the past three decades, the public conversation about cyberspace and international
politics has been conducted in the future tense. A "cyber Pearl Harbor" would switch off a country's
power grid; a handful of skilled operators would humble a great power; the next war would be won or
lost before a shot was fired. The scenarios were vivid, and they were not absurd: modern economies do
run on networked systems, and those systems can be broken. What the scenarios lacked was a record.
They were claims about what *could* happen, offered in the absence of systematic evidence about what
*had*.

The opposite caricature is just as easy to state. On this view cyber operations are simply crime and
espionage conducted with better tools — a nuisance for security departments, of no strategic
consequence, and no business of a course on geopolitics. It, too, is a claim about evidence, and it,
too, is usually made without any.

This chapter takes the question to the data. It does so through the work of Brandon Valeriano and
Ryan Maness, who built a dataset of cyber incidents between rival states and asked what the record
actually shows [@valeriano2015], and through the argument of Henry Farrell and Abraham Newman that
the networks globalisation built are not flat, and that states with jurisdiction over their hubs can
turn them into instruments of coercion [@farrell2019]. The two works answer different questions. The
first asks how states use offensive cyber operations against each other. The second asks how states
use the architecture of the global economy — including its digital architecture — to watch and to
deny. A multinational needs both answers, because it sits inside the architecture and in the path of
the operations.

The question for the firm is narrower and more practical than the question for the strategist. It is
not whether cyberspace is a new domain of war. It is *through which channels inter-state rivalry in
cyberspace reaches a firm's operations, and how its decision architecture should absorb it*. The
answer, this chapter argues, is that the firm is rarely the intended target of strategic cyber
operations, frequently their collateral, and increasingly a piece of the infrastructure over which
states compete.

## Three activities that look alike

Three kinds of activity are routinely run together under the heading "cyber attack", and the first
task is to separate them.

**Espionage** steals information: state secrets, negotiating positions, intellectual property, the
personal data of officials. Its typical actors are intelligence services and their contractors, and
its typical intrusion — into a ministry, a defence supplier or a law firm advising on a merger — is
designed never to be noticed. **Disruption and degradation** interrupt or damage systems: a
denial-of-service attack that floods a ministry's website, malware that wipes the disks of a
company's computers, an operation that manipulates an industrial control system. Its actors are
military and intelligence units and the proxies they sponsor. **Crime** extracts money: ransomware
that encrypts a hospital's records, fraud against a bank's payment systems. Its actors are criminal
groups.

::: {.definition}
[**Cyber operation**]{.term} — the use of computer code or network access by an organised actor to
obtain information from, disrupt, degrade or manipulate a target's information systems. Espionage,
disruption and crime are all cyber operations; they differ in purpose and actor, not in technique.
The same intrusion may serve any of the three.
:::

The boundaries blur, and the blurring is itself a geopolitical fact. States tolerate criminal groups
that operate from their territory against foreign targets, hire them, shelter them, and occasionally
use their tools. An intrusion that begins as espionage leaves access that can later be used for
disruption. A ransomware campaign run by a criminal group may serve a state's purposes by sowing
disorder in a rival's economy, without the state having ordered it. When a ransomware attack by a
criminal group believed to operate from Russia forced the shutdown of the Colonial Pipeline in the
United States in May 2021, it was crime in its motive and geopolitics in its consequences: the
question of what the Russian state knew, tolerated or could have prevented became a matter between
governments.

For a multinational the distinction matters because the three activities call for different
responses. Espionage is a threat to the firm's intellectual property and its negotiating position,
and the defence is largely technical and organisational. Disruption is a threat to its operations,
and the defence includes resilience — the ability to keep working when systems fail. Crime is a
threat to its cash and its reputation, and it is the one where law enforcement, insurers and the
firm's own willingness to pay become part of the calculation. A risk register that lists "cyber" as
a single line has not yet done the first piece of analysis.

::: {.archive}
[From the archive · Estonia, 2007]{.archive-label}

In April 2007 the Estonian government moved a Soviet-era war memorial, the Bronze Soldier, from the
centre of Tallinn to a military cemetery. The decision provoked protests by members of the country's
Russian-speaking minority and an angry response from Moscow. Over the following weeks a wave of
distributed denial-of-service attacks hit Estonian government websites, banks, newspapers and
political parties. Estonia, among the most digitised societies in Europe, found its online services
intermittently unreachable.

Estonian officials pointed to Russia. The Russian government denied involvement, and the public
record never established a chain of command; much of the traffic came from botnets and from
individuals mobilised on Russian-language forums. The episode thus contained, in compressed form,
nearly every feature that later analysts would identify in state cyber conflict: an existing
political rivalry, an operation of low technical sophistication and limited physical harm, high
political salience, and attribution that remained contested.

Its institutional legacy was substantial. NATO's Cooperative Cyber Defence Centre of Excellence was
established in Tallinn the following year, and under its auspices a group of international lawyers
produced the *Tallinn Manual*, an attempt to state how existing international law applies to cyber
operations [@schmitt2013]. The episode was widely described at the time as the first cyber war. With
hindsight it looks more like the first clear case of what Valeriano and Maness would call restraint: a
rival state's displeasure expressed through disruption that stopped well short of destruction.
:::

## The restraint thesis

Valeriano and Maness built their dataset around a simple design choice that shapes everything they
found. They did not try to catalogue every cyber operation in the world. They took pairs of states
with a history of enduring hostility — **rivals**, in the sense the international-conflict
literature has used for decades — and recorded the cyber incidents between them. The unit is the
incident, nested in campaigns; the population is rival dyads; the evidence is public. The dataset
has since been extended as the Dyadic Cyber Incident and Campaign Data, whose version 2.0 covers
incidents beginning between 2000 and 2020 and is the replication data for this session
[@maness2022].

::: {.definition}
[**Cyber incident**]{.term} (in DCID) — an individual cyber operation launched by one state against
another within a rival dyad, with a start date, a method, a target type, an objective and a severity
score. Incidents can be grouped into **campaigns**, sustained series of operations with a common
purpose. The unit is the incident between rivals, not the operation in general.
:::

The choice of rivals as the population is a theoretical commitment, not a convenience. The study of
international conflict has long found that a small number of pairs of states account for a large
share of militarised disputes, and that these enduring rivalries have their own dynamics: hostility
persists, crises recur, and each side interprets the other's moves in the light of a long history.
If cyber operations are a new instrument of old conflicts, rivalries are where they should appear;
if they are something genuinely new — an instrument that lets any state hurt any other cheaply —
they should appear outside rivalries too. Restricting the data to rivals makes the first hypothesis
testable and the second invisible — a limitation that the comparison dataset in the practice round
makes concrete.

From that record they drew four propositions.

The first is **restraint**. States use cyber operations far less often, and far less destructively,
than the "cyber war" narrative predicts. Most incidents in the data are of low severity: defacements
of websites, denial-of-service attacks, espionage. Operations that destroy physical property or take
lives are rare. The image of cyberspace as a domain of constant, escalating attack does not survive
contact with a systematic count.

::: {.definition}
[**Cyber restraint**]{.term} — the empirical pattern, and the theoretical argument, that states with
offensive cyber capabilities use them sparingly and at low severity against their rivals, holding back
the most destructive options. Restraint is a claim about *strategic* severity, not about frequency of
nuisance or about commercial cost.
:::

The second is that cyber conflict follows **regional rivalries**. The dyads that account for most of
the incidents are those that were already hostile before anyone had a network: the United States and
China, Russia and its neighbours and the West, Israel and Iran, India and Pakistan, the two Koreas.
Cyber operations do not create new conflicts; they are a tool in old ones. That finding matters for
anyone who expected the low cost of entry to cyber operations to flatten the international hierarchy.
The states that are most active in cyberspace are, by and large, the states that were already
contending.

The third proposition explains the first: **why** states hold back. The fourth is that cyber
operations have **limited coercive effect**. They rarely change the target's behaviour. They are
better at signalling displeasure and at gathering intelligence than at compelling a rival to do
something it would otherwise not do — a conclusion that the same authors developed at greater length
in later work on cyber strategy [@valeriano2018].

The restraint thesis did not arrive in an empty field. Thomas Rid had argued, provocatively, that
cyber war in the sense of an act of force that is violent, instrumental and political had never
occurred, and that what was called cyber war was better understood as sabotage, espionage and
subversion — old activities in a new medium [@rid2012; @rid2013]. Erik Gartzke made a related
argument from the logic of force: an attack that cannot be followed up by conventional power changes
nothing durable, so cyber operations are likely to be adjuncts to force rather than substitutes for
it [@gartzke2013]. Lucas Kello took the opposite position, arguing that the cyber revolution
genuinely strained the concepts of international relations because it blurred war and peace into a
condition of permanent, sub-threshold "unpeace" [@kello2013; @kello2017]. Valeriano and Maness's
contribution was to bring data to an argument that had been conducted largely through concepts and
anecdotes, and the data came down closer to Rid and Gartzke than to the prophets of catastrophe.

## Why states hold back

The reasons for restraint are worth taking one at a time, because each has an analogue in the firm's
own calculation.

**Escalation.** A destructive cyber operation against a rival invites a response, and the response
need not stay in cyberspace. A state that switches off a rival's grid has made a move whose
consequences it cannot control. In a relationship where both sides have conventional and sometimes
nuclear forces, the incentive to stay below the threshold that would provoke them is strong.

**Revelation.** A cyber capability depends on a vulnerability the target has not fixed. Using it
reveals it, and once revealed it can be patched — in the target's systems and everyone else's. The
most sophisticated capabilities are therefore wasting assets, worth more held in reserve than spent.

**Blowback.** Malicious code, once released, can be captured, analysed and reused. A weapon that can
be reverse-engineered and turned back on its maker, or on the maker's allies and firms, is a weapon
to be used with care.

**Access.** The value of being inside a rival's networks is often greater than the value of damaging
them. A state that can read a rival's communications has every reason not to do anything that would
alert the rival to its presence. Espionage, in this sense, restrains disruption.

These incentives are not the whole story. Ben Buchanan has argued that intrusions made for defensive
purposes — to understand a rival's capabilities, or to pre-position against a future threat — look
identical, from the target's side, to preparation for attack, and that this creates a security
dilemma in which each side's prudence alarms the other [@buchanan2017]. Restraint in the use of
destructive operations is compatible with constant, mutual intrusion, and the intrusions themselves
are a source of instability.

The war in Ukraine has tested the restraint thesis harder than anything in the dataset, which ends
in 2020. Russian cyber operations against Ukraine have been extensive since 2014, and they
intensified around the full-scale invasion of February 2022. The best systematic study of the
earlier period found that cyber operations had little discernible effect on events on the
battlefield [@kostyuk2019], which is consistent with the fourth proposition: cyber operations are
weak instruments of compulsion even in war. Whether the restraint thesis holds *as of today* is an
open question, and it is the right question to ask of the replication. A pattern measured to 2020 is
evidence about 2000–2020; extending it requires data the dataset does not contain.

The most famous exception proves the rule in an instructive way. The operation later known as
Stuxnet, discovered in 2010, sabotaged centrifuges at Iran's uranium-enrichment plant at Natanz by
manipulating the industrial control systems that ran them. It was widely attributed to the United
States and Israel, neither of which has formally acknowledged it. It is the clearest case in the
public record of code causing physical destruction to a rival's strategic asset, and it fits the
restraint thesis better than the catastrophe narrative: it was narrowly targeted, designed to look
like malfunction rather than attack, and aimed at delaying a programme rather than at provoking a
war. It also illustrates blowback. The code escaped the plant's isolated network, spread to
computers around the world, and was analysed in detail by security researchers, so that its
techniques became available to everyone. For firms, the lesson was that industrial control systems —
the machinery of plants, pipelines and utilities — were now a target class, and that the code
designed to attack one of them could end up on their own networks.

::: {.warn}
**Low strategic severity is not low commercial cost.** An operation that barely registers on a scale of
harm between states — a wiper that destroys no infrastructure and kills no one — can halt a company's
production for weeks. The restraint thesis is about what states do to each other. The firm's question
is what happens to the firms that happen to be in the way.
:::

## Weaponised interdependence

Valeriano and Maness study offensive operations. Farrell and Newman study something quieter and, for
a multinational, probably more consequential: the way in which the networks of the global economy
can be used by the states that sit at their centre [@farrell2019].

Their starting observation is that the networks globalisation built — for finance, for
communications, for the internet's physical and logical infrastructure — are not flat meshes in
which every node is equal. They are highly asymmetric, with a few hubs through which most traffic
passes. Network economics explains why: hubs are efficient, and efficiency attracts more traffic,
which makes the hub more central still. The internationalisation of the 1990s was conducted on the
assumption that this centralisation was a technical fact with no political content. Farrell and
Newman's argument is that the assumption was wrong. A state that has jurisdiction over a hub can use
it.

::: {.definition}
[**Panopticon effect**]{.term} — the use of jurisdiction over a network hub to *see* what flows through
it: to gather information about the activities of other states, firms and individuals whose traffic
passes through the hub.
:::

::: {.definition}
[**Chokepoint effect**]{.term} — the use of jurisdiction over a network hub to *deny* others access to
it: to cut a bank out of a payment system, a firm out of a software supply, a country out of a market
for critical components.
:::

The two effects need each other. The panopticon tells a state where to apply the chokepoint, and the
chokepoint gives the panopticon its teeth. Farrell and Newman's cases make both concrete. The
disclosures by Edward Snowden in 2013 showed the extent to which American intelligence agencies had
used the concentration of global internet traffic and data storage in American firms and on American
territory to collect information at scale — the panopticon. The disconnection of sanctioned Iranian
banks from the SWIFT financial-messaging network in 2012, after the European Union adopted the
necessary legal measures, showed how a hub located in one jurisdiction could be used to deny a whole
country's banking system its normal connection to the world — the chokepoint.

The implication for a multinational is uncomfortable in two ways. The first is that the firm's
exposure to geopolitical risk depends on where the hubs it uses are located and whose law applies to
them. A firm whose payments clear through one jurisdiction, whose data are stored with providers
subject to another, and whose software updates arrive from a third has three sets of exposure to the
coercive choices of three states, most of which have nothing to do with the firm.

The second is more uncomfortable still: **the firm itself can be the hub**. A cloud provider, a
payment network, a telecommunications operator, a maker of widely used software — each is
infrastructure that its home state can watch through or weaponise, and that rival states therefore
have reason to treat as a target, to exclude, or to replace with a domestic alternative. A firm in
that position is not a bystander to geopolitical competition. It is part of the terrain. This is the
bridge from this session to sanctions in Session 10, where the chokepoint becomes a legal
instrument, and to space in Session 11, where the hubs are in orbit.

## Attribution: evidence about evidence

Every dataset of state cyber operations rests on an act of attribution. Somebody has to say who did
it. And attribution in cyberspace has four properties that make it unlike the identification of the
attacker in almost any other kind of conflict event.

::: {.definition}
[**Attribution**]{.term} — the identification of the actor responsible for a cyber operation, at
three levels: the machines used, the individuals or groups who operated them, and the state, if any,
that directed or sponsored them. Public attribution is the decision to announce the third.
:::

It is **slow**. Forensic analysis takes weeks or months; public attribution by governments often
comes a year or more after the event. It is **probabilistic**. Technical indicators — the code, the
infrastructure, the working hours of the operators, the language settings left in a file — can be
faked, borrowed or reused, and a careful operator plants false ones. It is **political**.
Governments decide when to attribute publicly, to whom, and with how much of their evidence, and
they decide in the light of their relations with the accused state and their wish to protect their
own sources. And it is **selective**. What is attributed publicly is what someone wanted known.

Rid and Buchanan put the point sharply: attribution is what states make of it [@rid2015]. It is not
a technical fact waiting to be discovered but a judgement, assembled from technical, operational and
strategic evidence, and communicated for a purpose. Lindsay offered a partial corrective: for the
most consequential operations the set of capable actors is small, and the attribution problem is
therefore less severe than it is for routine intrusions — which is one reason deterrence of major
attacks remains possible [@lindsay2015]. Both views lead to the same conclusion about data.

**An event dataset of cyber operations is a record of public attributions, not a record of
operations.** That sentence is the most important caveat of the practice round. It has predictable
consequences for what the data show. States that attribute publicly — mostly Western democracies,
with active security services and a free press — appear more often as victims than states that do
not. Operations by allies against each other are rarely attributed in public and are therefore
nearly invisible. Operations that succeeded in remaining undetected are, by definition, absent. A
dyad with no incidents in the data may be a dyad with no operations, or a dyad in which neither side
chose to say anything.

## When the firm is collateral

The restraint thesis concerns the intentions of states. The cost to firms is driven by something
else: the technical reach of what states release.

::: {.archive}
[From the archive · NotPetya, June 2017]{.archive-label}

On 27 June 2017, the eve of a Ukrainian public holiday, malware spread through the update mechanism
of a Ukrainian accounting program widely used by businesses operating in the country. It looked like
ransomware, displaying a demand for payment, but its encryption could not be reversed: it was a
wiper dressed as a ransom note. Within hours it had spread beyond Ukraine through the internal
networks of any company that ran the software at a Ukrainian site. In February 2018 the governments
of the United States and the United Kingdom, among others, publicly attributed the operation to the
Russian military.

The apparent target was Ukraine. The victims included some of the largest firms in the world. The
shipping company Maersk lost the use of systems across its global operations. The pharmaceutical
company Merck and the food company Mondelez reported very large losses, as did logistics and
manufacturing firms in many countries. None of them had a quarrel with anyone; they had a subsidiary,
an office or a supplier in Ukraine, running a program everybody used [@greenberg2019].

The aftermath carried a second lesson. When the companies claimed under their property insurance,
insurers invoked the **war exclusions** that such policies had carried for generations, arguing that an
operation by a state's military was an act of war. The litigation lasted years and did not go
uniformly the insurers' way; in Merck's case, New Jersey courts held that the traditional exclusion,
written with armed conflict in mind, did not cover the attack. The market's response was to write
explicit exclusions for state-backed cyber operations into its contracts, which the Lloyd's market
required from 2023. The effect is that a firm's cyber cover may now end exactly where geopolitics
begins.
:::

Three lessons follow for the firm. The first is that **proximity in cyberspace is technical, not
political**. Firms were hit by NotPetya because they ran a piece of software in a country at war,
not because anyone chose them. A firm's exposure to a state's cyber operations depends on its
network architecture — what it connects to, what it updates from, what its subsidiaries can reach —
as much as on its political profile.

The second is that **insurance is not a backstop**. A risk transfer that excludes the scenario the
board is most worried about does not transfer that risk. The question to ask of a cyber policy is not
whether it covers "cyber attacks" but what it says about operations attributed to states — and who
decides the attribution.

The third is that **the board owns it**. Securities regulators increasingly require listed firms to
disclose material cyber incidents and to describe how their boards oversee cyber risk. In the United
States, rules adopted in 2023 require listed companies to report material incidents promptly and to
describe their risk management and governance of cybersecurity in their annual reports [@sec2023].
The geopolitical part of cyber risk — the part that arises from the rivalry of states — is thereby
made a matter of corporate governance, whatever the firm's own view of it.

## Digital sovereignty and the splintering network

Weaponised interdependence has a defensive mirror. States that fear the panopticon and the
chokepoint of others respond by asserting control over the networks within their own jurisdiction:
where data must be stored, who may access them, which foreign equipment may be installed, which
vendors may operate. The vocabulary varies — digital sovereignty, data localisation, trusted
vendors, technological self-reliance — and the effect is the same. The single global network on
which the internationalisation of the 1990s assumed firms could operate is splintering into
jurisdictions with different rules.

Three instruments matter most for a multinational. **Data-localisation and transfer rules** require
that certain data be stored within a country or restrict their movement abroad; the invalidation by
the Court of Justice of the European Union in 2020 of the framework that governed transfers of
personal data from the European Union to the United States showed how quickly a legal basis for a
firm's data architecture can disappear. **Security reviews and vendor bans** exclude foreign
suppliers from critical networks; the restrictions imposed on Huawei's telecommunications equipment
by the United States and a number of its allies from 2019 onward forced operators to redesign and in
some cases to strip out networks they had already built. **Access laws** give governments the power
to compel firms under their jurisdiction to hand over data, including data stored abroad; the United
States' CLOUD Act of 2018 is the best-known example, and it sits awkwardly beside European
data-protection law.

For the firm, these instruments generate three kinds of cost. **Duplication**: separate data centres
or cloud regions per jurisdiction, separate supply chains for network equipment, separate compliance
regimes. **Conflicting obligations**: one state's law requires a disclosure that another's forbids,
and the firm must choose which to break. **Vendor risk**: a supplier banned in one market may be
mandatory, or at least dominant, in another, so that a single global architecture becomes
impossible. None of these costs arises from a cyber operation. All of them arise from the
geopolitics of cyberspace.

## Where cyber risk sits in the firm

The five channels through which geopolitical risk reaches a multinational help locate cyber risk
precisely. It runs most obviously through **data and operations**: the operation that halts
production, the localisation rule that forces a redesign. It runs through **assets and people**,
when intellectual property is stolen or staff in a jurisdiction are compelled to provide access. It
runs through **finance**, when insurers exclude state-backed operations and when payment hubs become
chokepoints. It runs through **inputs**, when a vendor is banned or a software supply chain is
compromised — NotPetya travelled through a software update. And it runs through **market access**,
when a firm is excluded from a market as a security risk, or when its home state's use of the firm
as a hub makes it unwelcome abroad.

Inside the firm, the risk is distributed across several actors, and the distribution is part of the
problem. The **board** sets risk appetite and oversees disclosure; its distinctive question is
*which state actors would want our data or our downtime, and why?* The **chief information security
officer** turns threat intelligence into controls and owns incident response, but typically reports
through a technology function with limited geopolitical analysis. The **chief risk officer** is the
natural integrator of cyber risk with country, sanctions and supply-chain risk — the view the team
project takes. The **insurer** prices the risk and, increasingly, draws the line at state-backed
operations. And **regulators** impose disclosure, localisation and vendor rules from outside. A firm
in which each of these actors holds a piece of the picture and nobody holds the whole has a decision
architecture designed for crime and espionage, not for geopolitics.

What changes on Monday, for a firm with a plant in a country that sits in one of the densest cells
of the rivalry matrix? Not, in the first instance, its technology. The first change is to the map:
an inventory of which systems at that site connect to which systems elsewhere, which software is
updated from which vendors, and which data cross which borders — because it is along those
connections that an operation aimed at a government travels into a firm. The second is to
segmentation: a subsidiary in a contested jurisdiction whose network can reach the group's core
systems is a bridge for anyone who compromises it, and the cheapest geopolitical control a firm can
buy is often a wall between the two. The third is to contracts: what the insurance policy says about
operations attributed to states, what the cloud provider's terms say about government access in each
jurisdiction, and what suppliers have agreed about notifying the firm when they are compromised. The
fourth is to governance: who in the firm is responsible for asking, before an investment rather than
after an incident, which states would want the firm's data or its downtime. None of these is a
technical fix. All of them follow from treating cyber risk as a geopolitical exposure rather than an
IT problem.

## From concept to data

The replication target is the descriptive picture at the heart of Valeriano and Maness's book:
incidents by year, by method and by severity, and the matrix of who targets whom. Rebuilding it from
DCID version 2.0 is mostly a matter of reading the codebook carefully, and the codebook repays the
reading because it is where the concepts of this chapter become columns.

The unit is one incident between an initiating state and a target state within a rival dyad. The
dyad's two states are recorded as names, ordered by their Correlates of War codes, so that the first
state of the pair is not the initiator; the initiator is recorded separately, as a code, and the
target is whichever state of the dyad did not initiate. The method is coded on a scale that runs
from vandalism through denial of service and network intrusion to network infiltration, with
sub-codes for kinds of malicious software. Severity is coded on a scale the codebook defines from 0
to 10, of which the released file uses only the values 0 to 6 — a discrepancy worth logging and, if
the codebook's scale applies, consistent with restraint. The type of target distinguishes private
and non-state targets from governmental ones, civilian and military, and the objective distinguishes
disruption, short- and long-term espionage and degradation. The September 2022 release contains 433
incidents with start dates from September 2000 to January 2021.

Two properties of the data follow directly from the arguments above. The first is that the
population is rival dyads. A cell of the initiator × target matrix that is empty does not mean "no
cyber conflict"; it means "no rivalry in the data", because pairs of states that are not coded as
rivals never enter. The second is that the incidents are public attributions. The matrix is
therefore a picture of who has been publicly *accused* of operating against whom — itself a
geopolitical artefact, shaped by which governments attribute and when.

The comparison dataset, the European Repository of Cyber Incidents, makes both properties visible
[@zettlschabath2025]. It records incidents with state and non-state initiators, including criminal,
hacktivist and unattributed operations, and in its version 1.3 it contains 3,414 incidents with start
dates from 2000 to 2024 — several times the size of DCID. Restricting it to incidents attributed to
state or state-affiliated actors leaves 1,014; restricting it to states alone leaves 329. The gap
between those numbers, and between all of them and DCID's 433, is a measure of how much the answer to
"how much cyber conflict is there?" depends on the definition of the population and of attribution.

## A short review of the literature

::: {.lit}
The debate over whether cyberspace is a domain of war was framed in the early 2010s. @rid2012 and
@rid2013 argued that cyber war had not taken place and would not, reclassifying cyber operations as
sabotage, espionage and subversion; @gartzke2013 argued from the logic of force that cyber operations
would complement rather than replace conventional power; @kello2013 and @kello2017 argued, against
both, that the cyber revolution unsettled the conceptual foundations of international relations. The
legal question of how existing international law applies to cyber operations is set out in
@schmitt2013.

Systematic evidence arrived with @valeriano2015, whose dataset of incidents between rival states
supported a thesis of restraint and regional rivalry. The dataset has been extended through
successive releases, of which @maness2022 is the current public version; @maness2016 examine whether
cyber incidents shift the broader conflict and cooperation between rivals, and @valeriano2018
develop the argument that cyber operations are weak instruments of coercion. @kostyuk2019 tested
cyber operations in the war in eastern Ukraine against battlefield events and found little effect.
@buchanan2017 sets out the cybersecurity dilemma created by intrusions that are defensive in purpose
and threatening in appearance.

On attribution, @rid2015 treat it as a political judgement assembled from technical and strategic
evidence, and @lindsay2015 argues that its difficulty is overstated for consequential operations. On the
economic architecture of coercion, @farrell2019 is the foundational statement of weaponised
interdependence, with its panopticon and chokepoint effects. Wider datasets that include non-state
actors, such as @zettlschabath2025, now allow the rival-dyad picture to be set against the full record
of attributed incidents, and the firm's experience of state operations is documented most vividly in
@greenberg2019.
:::

## What the matrix will not tell the firm

The practice round rebuilds the incident picture and the initiator × target matrix, and then sets
them against a wider dataset. The dashboard that results is informative. It shows that cyber
conflict between rivals concentrates in a few dyads, that most incidents are of low severity, and
that the methods have shifted over two decades. It is tempting to read it as a map of where a
multinational's cyber risk lies. It is not, and the reasons are the arguments of this chapter.

The matrix does not license a firm to conclude that it is safe in a country whose cells are empty.
An empty cell means no publicly attributed incident between *rivals*; it says nothing about
operations that were never attributed, about operations between states that are not coded as rivals,
or about criminal groups, which account for much of the cyber harm firms actually suffer. Nor does a
dense cell tell a firm that it is a target. The incidents in that cell were aimed mostly at
governments, and the firm's exposure to them depends on whether it is technically in the path —
whether it runs software, holds data or provides infrastructure that an operation against the
government might traverse. NotPetya would have appeared in the data as one incident in one dyad; its
cost fell on firms in dozens of countries.

Nor does the evidence for restraint license complacency. It is a pattern in state behaviour to 2020,
measured on a scale of harm between states. It does not bound the commercial cost of a low-severity
operation, and it does not tell a firm what has happened since a large-scale war began in Europe.
The question to carry into the practice round is the one the dashboard cannot answer by itself:
given where interstate cyber conflict concentrates, which of the firm's networks, suppliers and hubs
lie in its path — and what has the firm agreed with its insurer about the operations that its
government will one day attribute to a state?