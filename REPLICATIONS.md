# Practice rounds — the big work and the data behind each

Each of Sessions 01–11 pairs one **big article or book** with the **data it is built on**. Before
class you read the work and locate its source. In the 90-minute practice round your team:

1. **Collects** the data from the original producer and logs its provenance;
2. **Prepares** it in Tableau — pivot, join, recode — recording each decision;
3. **Replicates** the target figure as closely as the data allow;
4. **Compares** yours with the original, **breaks** one decision, and **extends** it in one direction;
5. Presents **one slide — original · ours · the catch** — in two minutes, by a member drawn at random.

Every source, its access conditions and its traps: [`DATA-SOURCES.md`](DATA-SOURCES.md).

---

## Article–data map

| Session | Big work | Data you collect | Target figure | Compare · break · extend |
|---|---|---|---|---|
| **01** · What is geopolitical risk? | Caldara & Iacoviello (2022), *Measuring Geopolitical Risk*, AER · [doi:10.1257/aer.20191823](https://doi.org/10.1257/aer.20191823) | GPR index | The monthly GPR index since 1985, spikes annotated; the historical index since 1900 | Threats vs acts · monthly vs yearly averages · one country index against the global |
| **02** · The international economic order | Baldwin (2016), *The Great Convergence*, Belknap/Harvard UP | World Bank WDI: GDP (current US$ and PPP), trade % GDP | The **G7 share of world GDP**, 1970–today — the "great convergence" after 1990 | Current dollars vs PPP · Baldwin's "Industrialising Six" · world trade/GDP and the "slowbalisation" after 2008 |
| **03** · Anarchy and the balance of power | Mearsheimer (2001), *The Tragedy of Great Power Politics*; Allison (2017), *Destined for War* | COW National Material Capabilities v7.0 (CINC); SIPRI military expenditure | **Shares of world capabilities** of the major powers, 1816–2022, and the US–China crossover | CINC vs military spending vs GDP — three measures, three different power transitions · a parameter to choose the challenger |
| **04** · Trade, conflict and fragmentation | Gopinath, Gourinchas, Presbitero & Topalova (2025), *Changing Global Linkages: A New Cold War?*, JIE · [doi:10.1016/j.jinteco.2024.104042](https://doi.org/10.1016/j.jinteco.2024.104042); Mansfield (2021) | UNGA ideal points (Voeten); IMF bilateral goods trade (IMTS) | **Trade within vs between geopolitical blocs**, indexed to before the 2022 invasion of Ukraine | Bloc definitions: thresholds on ideal-point distance · mirror trade (exports vs imports) · one "connector" country |
| **05** · International institutions | Kuziemko & Werker (2006), *How Much Is a Seat on the Security Council Worth?*, JPE · [doi:10.1086/507155](https://doi.org/10.1086/507155) | UNSC elected members; US foreign aid (Greenbook) or the AidData replication file | **US aid to elected members in event time**, years −3 to +3 around a Security Council term | Current vs constant dollars · mean vs median · years with and without salient Council business |
| **06** · Private authority and standards | Prakash & Potoski (2006), *Racing to the Bottom? Trade, Environmental Governance, and ISO 14001*, AJPS · [doi:10.1111/j.1540-5907.2006.00188.x](https://doi.org/10.1111/j.1540-5907.2006.00188.x); Abbott & Snidal (2009); Mattli & Büthe (2003) | ISO Survey (ISO 14001, ISO 9001); IMF bilateral exports; WDI GDP | **The diffusion of ISO 14001** across countries (map and small multiples), and adoption against the adoption level of each country's export markets | Counts vs per-$ of GDP · ISO 9001 as the placebo · trade-weighted vs unweighted export markets |
| **07** · Measuring risk: text, coding, big data, indices | Hassan, Hollander, van Lent & Tahoun (2019), *Firm-Level Political Risk*, QJE · [doi:10.1093/qje/qjz021](https://doi.org/10.1093/qje/qjz021); Baker, Bloom & Davis (2016), QJE; OECD/JRC (2008) *Handbook on Constructing Composite Indicators* | firmlevelrisk.com firm-quarter file; EPU; a corpus of news items from GDELT that **you code yourselves** | **Average firm-level political risk over time** against EPU — then **your own coded index** | Intercoder agreement on your corpus · normalisation choices · weights as parameters: how much does the ranking move? |
| **08** · Cyber geopolitics | Valeriano & Maness (2015), *Cyber War versus Cyber Realities*, OUP · [doi:10.1093/acprof:oso/9780190204792.001.0001](https://doi.org/10.1093/acprof:oso/9780190204792.001.0001); Farrell & Newman (2019) | DCID v2.0; EuRepoC v1.3 | **Incidents by year, method and severity**, and the **initiator × target matrix** of rival dyads | DCID (state rivals) vs EuRepoC (all incidents) · severity distribution — evidence of "cyber restraint"? · incidents hitting the private sector |
| **09** · Economic diplomacy | Rose (2007), *The Foreign Service and Foreign Trade: Embassies as Export Promotion*, World Economy · [doi:10.1111/j.1467-9701.2007.00870.x](https://doi.org/10.1111/j.1467-9701.2007.00870.x); Bjola & Manor (2018); Putnam (1988) | Lowy Global Diplomacy Index; IMF bilateral exports; WDI GDP | **Exports against the number of diplomatic posts** in the partner, log scale, with trend line | Raw vs GDP-adjusted · embassies vs consulates · reverse causality: posts follow trade? |
| **10** · Economic sanctions | Hufbauer, Schott, Elliott & Oegg (2007), *Economic Sanctions Reconsidered*, PIIE; Felbermayr et al. (2020), *The Global Sanctions Data Base*, EER · [doi:10.1016/j.euroecorev.2020.103561](https://doi.org/10.1016/j.euroecorev.2020.103561); Pape (1997) | GSDB Release 5 (by request); TIES v4.0 | **Active sanctions cases per year by type**, 1950–today, and the **share judged successful** by objective | Threats (TIES) vs impositions · success by objective · a Gantt chart of one target's sanctions history |
| **11** · Supply chains and critical minerals | Kowalski & Legendre (2023), *Raw Materials Critical for the Green Transition*, OECD Trade Policy Papers 269 · [doi:10.1787/c6bb598b-en](https://doi.org/10.1787/c6bb598b-en); Le Billon & Shykora (2020); Farrell & Newman (2019) | OECD Inventory of Export Restrictions on Critical Raw Materials; USGS world production tables; NY Fed GSCPI | **Export restrictions on critical raw materials since 2009**, by commodity and country, and the **concentration (HHI) of world production** | Count vs coverage-weighted restrictions · HHI on production vs on exports · GSCPI as the system-wide signal |
| **12** · Team presentations | Kobrin (1979); Henisz (2000) | All of the above; POLCON; WGI | **Your team's dashboard** for one multinational | Defended live, in front of the room |

---

## Why replicate figures, not regressions

This is not an econometrics course. The figure at the heart of a big work is where its argument
meets the reader — the image that ends up in board presentations and ministerial speeches. Rebuilding
it forces every decision the authors made into the open: which countries, which years, which
deflator, which coding rule, which normalisation. A multinational's risk team makes the same
decisions every time it builds a dashboard. Learning to see them is the point.

## Citing

Cite the work **and** the dataset, with version and access date. They are distinct contributions,
often by different people, and the dataset has usually been revised since the work was published.
