"""Figures for Chapter 6, Private Authority, Standards and Global Regulation.

Data, downloaded at source into .data-cache/ by style.fetch():

* ISO Open Data (https://www.iso.org/open-data.html), published by ISO under the ODC
  Attribution licence: the technical-committee file (secretariat, creation date, participating
  members of every ISO committee and subcommittee) and the deliverables-metadata file (every ISO
  document with its type, edition and publication date).
  - iso_technical_committees.jsonl and iso_deliverables_metadata.jsonl, from
    https://isopublicstorageprod.blob.core.windows.net/opendata/_latest/...
* Science Based Targets initiative, Target Dashboard (https://sciencebasedtargets.org/target-dashboard):
  companies-excel.xlsx and targets-excel.xlsx (public downloads, no account).
* IMF, International Trade in Goods (IMTS), exports FOB in US dollars by partner, annual, from the
  IMF SDMX 3.0 API (https://api.imf.org/external/sdmx/3.0/...).
* World Bank, World Development Indicators: GDP (NY.GDP.MKTP.CD) and GDP per capita
  (NY.GDP.PCAP.CD), bulk CSV from the WDI API.

The ISO Survey of Management System Standard Certifications is not used: its data files sat on
ISO's Livelink content server, which has been decommissioned, and the survey is now compiled from
IAF CertSearch, whose statistics require an account. The chapter's certification evidence is
therefore illustrated with a different private standard whose register is public at the level of
the individual firm: the Science Based Targets initiative's validated corporate climate targets.

    .venv/bin/python scripts/figures/build_all.py 06
"""

import io
import json
import zipfile

import numpy as np
import pandas as pd

from style import (BLUE, GOLD, GRID, INK, MUTED, RED, TEAL, PALE_BLUE, figure, fetch, save)

ISO = "https://isopublicstorageprod.blob.core.windows.net/opendata/_latest"
TC_URL = f"{ISO}/iso_technical_committees/json/iso_technical_committees.jsonl"
DEL_URL = f"{ISO}/iso_deliverables_metadata/json/iso_deliverables_metadata.jsonl"
SBTI_CO = "https://files.sciencebasedtargets.org/production/files/companies-excel.xlsx"
SBTI_TG = "https://files.sciencebasedtargets.org/production/files/targets-excel.xlsx"
IMTS_URL = "https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/IMTS/+/*.XG_FOB_USD.*.A"
IMTS_HDR = {"Accept": "application/vnd.sdmx.data+csv;version=2.0.0",
            "User-Agent": "Mozilla/5.0 (book figures; research)"}
WDI = "https://api.worldbank.org/v2/en/indicator/{}?downloadformat=csv"

YEAR = 2024  # trade and GDP year for the export-market measure

# ISO member bodies that hold secretariats or appear in the tables, by country.
MEMBER = {
    "DIN": "Germany", "SAC": "China", "ANSI": "United States", "AFNOR": "France",
    "JISC": "Japan", "BSI": "United Kingdom", "SIS": "Sweden", "KATS": "Korea",
    "UNI": "Italy", "SA": "Australia", "SNV": "Switzerland", "SCC": "Canada", "BIS": "India",
    "SN": "Norway", "SABS": "South Africa", "NEN": "Netherlands", "GOST R": "Russia",
    "UNE": "Spain", "DS": "Denmark", "INSO": "Iran", "SII": "Israel", "ABNT": "Brazil",
    "ASI": "Austria", "IPQ": "Portugal", "SFS": "Finland", "DSM": "Malaysia", "PKN": "Poland",
    "NBN": "Belgium", "TSE": "Türkiye", "ICONTEC": "Colombia", "BSJ": "Jamaica",
    "IMANOR": "Morocco", "UNBS": "Uganda", "SE UkrNDNC": "Ukraine", "KEBS": "Kenya",
    "SASO": "Saudi Arabia",
}
EUROPE = {"Germany", "France", "United Kingdom", "Sweden", "Italy", "Switzerland", "Norway",
          "Netherlands", "Spain", "Denmark", "Austria", "Portugal", "Finland", "Poland", "Belgium"}

# SBTi uses UN M49 country names; map them to ISO 3166 alpha-3 codes (IMF and World Bank).
M49 = {
    "Afghanistan": "AFG", "Albania": "ALB", "Algeria": "DZA", "Argentina": "ARG",
    "Armenia": "ARM", "Australia": "AUS", "Austria": "AUT", "Azerbaijan": "AZE", "Bahrain": "BHR",
    "Bangladesh": "BGD", "Belgium": "BEL", "Bermuda": "BMU",
    "Bolivia (Plurinational State of)": "BOL", "Bosnia and Herzegovina": "BIH",
    "Botswana": "BWA", "Brazil": "BRA", "Bulgaria": "BGR", "Cambodia": "KHM", "Canada": "CAN",
    "Chile": "CHL", "China": "CHN", "China, Hong Kong Special Administrative Region": "HKG",
    "China, Macao Special Administrative Region": "MAC", "Colombia": "COL", "Costa Rica": "CRI",
    "Croatia": "HRV", "Cyprus": "CYP", "Czechia": "CZE", "Denmark": "DNK",
    "Dominican Republic": "DOM", "Ecuador": "ECU", "Egypt": "EGY", "El Salvador": "SLV",
    "Estonia": "EST", "Finland": "FIN", "France": "FRA", "Gabon": "GAB", "Georgia": "GEO",
    "Germany": "DEU", "Greece": "GRC", "Guatemala": "GTM", "Honduras": "HND", "Hungary": "HUN",
    "Iceland": "ISL", "India": "IND", "Indonesia": "IDN", "Iraq": "IRQ", "Ireland": "IRL",
    "Israel": "ISR", "Italy": "ITA", "Japan": "JPN", "Jersey": "JEY", "Jordan": "JOR",
    "Kazakhstan": "KAZ", "Kenya": "KEN", "Kuwait": "KWT", "Latvia": "LVA", "Lebanon": "LBN",
    "Liechtenstein": "LIE", "Lithuania": "LTU", "Luxembourg": "LUX", "Malaysia": "MYS",
    "Malta": "MLT", "Mauritius": "MUS", "Mexico": "MEX", "Monaco": "MCO", "Montenegro": "MNE",
    "Morocco": "MAR", "Myanmar": "MMR", "Netherlands (Kingdom of the)": "NLD",
    "New Zealand": "NZL", "Nigeria": "NGA", "Norway": "NOR", "Oman": "OMN", "Pakistan": "PAK",
    "Panama": "PAN", "Papua New Guinea": "PNG", "Paraguay": "PRY", "Peru": "PER",
    "Philippines": "PHL", "Poland": "POL", "Portugal": "PRT", "Qatar": "QAT",
    "Republic of Korea": "KOR", "Romania": "ROU", "Russian Federation": "RUS", "Samoa": "WSM",
    "Saudi Arabia": "SAU", "Serbia": "SRB", "Sierra Leone": "SLE", "Singapore": "SGP",
    "Slovakia": "SVK", "Slovenia": "SVN", "South Africa": "ZAF", "Spain": "ESP",
    "Sri Lanka": "LKA", "Sweden": "SWE", "Switzerland": "CHE",
    "Taiwan, Province of China": "TWN", "Thailand": "THA", "Trinidad and Tobago": "TTO",
    "Tunisia": "TUN", "Türkiye": "TUR", "Uganda": "UGA", "Ukraine": "UKR",
    "United Arab Emirates": "ARE", "United Kingdom of Great Britain and Northern Ireland": "GBR",
    "United Republic of Tanzania": "TZA", "United States of America": "USA", "Uruguay": "URY",
    "Viet Nam": "VNM", "Zambia": "ZMB", "Zimbabwe": "ZWE",
}


def load_committees():
    rows = [json.loads(line) for line in open(fetch(TC_URL, "iso_technical_committees.jsonl"),
                                              encoding="utf-8")]
    tc = pd.DataFrame({
        "ref": [r["reference"] for r in rows],
        "status": [r["status"] for r in rows],
        "sec": [(r.get("secretariat") or {}).get("acronym") for r in rows],
        "created": pd.to_datetime([r.get("creationDate") for r in rows], errors="coerce"),
        "sub": [r.get("parentId") is not None for r in rows],
        "p": [[m["acronym"] for m in (r.get("pMembers") or [])] for r in rows],
    })
    return tc[(tc.status == "Active") & tc.sec.notna()].copy()


def fig_output():
    d = pd.read_json(fetch(DEL_URL, "iso_deliverables_metadata.jsonl"), lines=True)
    d["year"] = pd.to_datetime(d.publicationDate, errors="coerce").dt.year
    s = d[(d.deliverableType == "IS") & d.supplementType.isna() & d.year.between(1970, 2025)]
    first = s[s.edition == 1].groupby("year").size()
    rev = s[s.edition > 1].groupby("year").size()
    total = s.groupby("year").size()
    in_force = d[(d.deliverableType == "IS") & d.supplementType.isna()
                 & d.currentStage.isin([6060, 9020, 9060, 9092, 9093])]
    print(f"[ch06] ISO International Standards published: 1970s mean "
          f"{total.loc[1970:1979].mean():.0f}/yr, 1990s {total.loc[1990:1999].mean():.0f}, "
          f"2000s {total.loc[2000:2009].mean():.0f}, 2010s {total.loc[2010:2019].mean():.0f}, "
          f"2020-25 {total.loc[2020:2025].mean():.0f}; peak {total.idxmax()} ({total.max()})")
    print(f"[ch06] share of revisions (edition>1): 1990s "
          f"{rev.loc[1990:1999].sum() / total.loc[1990:1999].sum():.0%}, 2020-25 "
          f"{rev.loc[2020:2025].sum() / total.loc[2020:2025].sum():.0%}")
    print(f"[ch06] International Standards currently published (in force): {len(in_force)}")
    fig, ax = figure()
    yrs = total.index
    ax.bar(yrs, first.reindex(yrs, fill_value=0), color=BLUE, width=0.8)
    ax.bar(yrs, rev.reindex(yrs, fill_value=0), bottom=first.reindex(yrs, fill_value=0),
           color=PALE_BLUE, width=0.8)
    ax.text(1972, 720, "First editions", color=BLUE, fontweight="bold")
    ax.text(1972, 1000, "Revisions of existing standards", color=MUTED, fontweight="bold")
    for y, lab in [(1987, "ISO 9000\nseries"), (1996, "ISO 14001"), (2015, "ISO 9001 and\n14001 revised")]:
        ax.annotate(lab, (y, total.loc[y]), xytext=(y, total.loc[y] + 250), ha="center",
                    fontsize=8, color=INK, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    ax.set_ylim(0, 1650)
    ax.set_xlim(1969, 2026)
    ax.set_ylabel("International Standards published per year")
    ax.set_title("ISO now publishes nearly three times as many standards a year as in the 1970s,\n"
                 "and most of them rewrite rules that already exist")
    return save(fig, "ch06-iso-output",
                "ISO Open Data, deliverables metadata (International Standards, excluding "
                "amendments and corrigenda), by year of publication.")


def fig_secretariats(tc):
    tc["country"] = tc.sec.map(MEMBER).fillna("Other")
    counts = tc.country.value_counts()
    total = len(tc)
    top = counts.head(12)[::-1]
    print(f"[ch06] active ISO TCs/SCs with a secretariat: {total} "
          f"({(~tc['sub']).sum()} TCs, {tc['sub'].sum()} SCs)")
    for c, n in counts.head(12).items():
        print(f"[ch06]   secretariats {c}: {n} ({n / total:.1%})")
    eu = tc.country.isin(EUROPE).sum()
    print(f"[ch06] European members (EU, EFTA, UK) hold {eu} ({eu / total:.0%}); "
          f"top six hold {counts.head(6).sum() / total:.0%}")
    fig, ax = figure(7.2, 4.2)
    colors = [RED if c == "China" else (BLUE if c in EUROPE else (GOLD if c == "United States"
              else MUTED)) for c in top.index]
    ax.barh(top.index, top.values, color=colors)
    for i, v in enumerate(top.values):
        ax.text(v + 1.5, i, f"{v}", va="center", fontsize=9)
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", color=GRID)
    ax.set_xlabel("Active ISO technical committees and subcommittees whose secretariat it holds")
    ax.set_title("Germany still runs more ISO committees than anyone,\nbut China is now second")
    ax.text(0.98, 0.08, f"European members hold {eu / total:.0%}\nof {total} secretariats",
            transform=ax.transAxes, ha="right", color=BLUE, fontsize=9)
    return save(fig, "ch06-iso-secretariats",
                "ISO Open Data, technical committees (current secretariats, October 2026).")


def fig_vintage(tc):
    tc = tc[tc.created.notna()].copy()
    tc["period"] = pd.cut(tc.created.dt.year, [1900, 1969, 1989, 2009, 2026],
                          labels=["before 1970", "1970–1989", "1990–2009", "2010–2026"])
    grp = np.where(tc.country == "China", "China",
                   np.where(tc.country == "United States", "United States",
                            np.where(tc.country == "Japan", "Japan",
                                     np.where(tc.country.isin(EUROPE), "Europe", "Rest of world"))))
    tab = pd.crosstab(tc.period, grp, normalize="index") * 100
    n = tc.period.value_counts().sort_index()
    print("[ch06] share of current secretariats by committee creation period (%):")
    print(tab.round(1).to_string())
    print(n.to_string())
    fig, ax = figure(7.2, 4.0)
    x = np.arange(len(tab))
    for g, col in [("Europe", BLUE), ("China", RED), ("United States", GOLD), ("Japan", TEAL),
                   ("Rest of world", MUTED)]:
        ax.plot(x, tab[g], color=col, marker="o")
        ax.text(x[-1] + 0.08, tab[g].iloc[-1], g, color=col, va="center", fontweight="bold")
    ax.set_xticks(x, [f"{p}\n({k} committees)" for p, k in zip(tab.index, n.values)])
    ax.set_xlim(-0.2, len(x) - 0.3)
    ax.set_ylabel("Share of secretariats held today (%)")
    ax.set_title("Of the committees created since 2010, China holds\nmore secretariats than "
                 "the United States and Japan together")
    return save(fig, "ch06-iso-vintage",
                "ISO Open Data, technical committees; active committees and subcommittees by "
                "creation date, current secretariat holder.")


ISO3 = {"Germany": "DEU", "China": "CHN", "United States": "USA", "France": "FRA", "Japan": "JPN",
        "United Kingdom": "GBR", "Korea": "KOR", "India": "IND", "Russia": "RUS", "Brazil": "BRA"}
EUROPE_ISO3 = ["AUT", "BEL", "BGR", "HRV", "CYP", "CZE", "DNK", "EST", "FIN", "FRA", "DEU", "GRC",
               "HUN", "IRL", "ITA", "LVA", "LTU", "LUX", "MLT", "NLD", "POL", "PRT", "ROU", "SVK",
               "SVN", "ESP", "SWE", "GBR", "CHE", "NOR", "ISL", "LIE"]


def participation_table(tc):
    """Table: secretariats, participating memberships and share of world GDP, by member."""
    gdp = wdi("NY.GDP.MKTP.CD", "wdi_gdp.zip")
    world = gdp.sum()
    p = pd.Series([m for lst in tc.p for m in lst]).value_counts()
    sec = tc.sec.value_counts()
    total = len(tc)
    print(f"[ch06] table: country | body | secretariats | % of {total} | P-memberships | "
          f"% world GDP {YEAR}")
    for acr in ["DIN", "SAC", "ANSI", "AFNOR", "JISC", "BSI", "KATS", "BIS", "GOST R", "ABNT"]:
        c = MEMBER[acr]
        print(f"[ch06]   {c} | {acr} | {sec.get(acr, 0)} | {100 * sec.get(acr, 0) / total:.1f} | "
              f"{p.get(acr, 0)} | {100 * gdp.get(ISO3[c], np.nan) / world:.1f}")
    eu = gdp.reindex(EUROPE_ISO3).sum() / world
    print(f"[ch06] EU + EFTA + UK share of world GDP {YEAR}: {eu:.1%} "
          f"({gdp.reindex(EUROPE_ISO3).notna().sum()} economies with data)")
    print(f"[ch06] most P-memberships: {p.head(5).to_dict()}")


def sbti_data():
    co = pd.read_excel(fetch(SBTI_CO, "sbti_companies-excel.xlsx"))
    tg = pd.read_excel(fetch(SBTI_TG, "sbti_targets-excel.xlsx"))
    return co, tg


def fig_sbti_diffusion(co, tg):
    nt = tg[(tg.target == "Near-term") & tg.date_published.notna()]
    first = nt.groupby("sbti_id").date_published.min().dt.year
    valid = co[co.near_term_status == "Validated Targets"].set_index("sbti_id")
    df = valid.join(first.rename("year"), how="inner")
    reg = df.region.map(lambda r: "Europe" if "Europe" in str(r) else
                        ("East Asia" if r == "Eastern Asia" else
                         ("North America" if r == "Northern America" else "Rest of world")))
    cum = pd.crosstab(df.year, reg).cumsum()
    cum = cum.loc[cum.index >= 2015]
    print(f"[ch06] SBTi: {len(valid)} companies with validated near-term targets; "
          f"{len(df)} with a publication date")
    print("[ch06] cumulative validated companies by region:")
    print(cum.to_string())
    loc = valid.location.value_counts()
    print("[ch06] top locations:", loc.head(12).to_dict())
    eu_share = (reg == "Europe").mean()
    print(f"[ch06] Europe share of validated companies: {eu_share:.0%}; East Asia "
          f"{(reg == 'East Asia').mean():.0%}; North America {(reg == 'North America').mean():.0%}")
    sme = (valid.organization_type == "SME").mean()
    print(f"[ch06] SME share of validated companies: {sme:.0%}")
    fig, ax = figure()
    last = cum.index.max()
    for g, col in [("Europe", BLUE), ("East Asia", RED), ("North America", GOLD),
                   ("Rest of world", MUTED)]:
        ax.plot(cum.index, cum[g], color=col, marker="o", markersize=3)
        dy = {"North America": 180, "Rest of world": -180}.get(g, 0)
        ax.text(last + 0.15, cum[g].iloc[-1] + dy, f"{g} {cum[g].iloc[-1]:,}", color=col,
                va="center", fontweight="bold", fontsize=9)
    ax.set_xlim(2015, last + 2.4)
    ax.set_xticks(range(2015, last + 1))
    ax.set_ylabel("Companies with a validated near-term target\n(cumulative, by year of earliest listed target)")
    ax.set_title("A private climate standard written in 2015 spread first through Europe,\n"
                 "then, from 2021, through Japan and the rest of East Asia")
    note = f"{last} to date" if last >= 2026 else ""
    if note:
        ax.text(last, -0.12, note, transform=ax.get_xaxis_transform(), ha="center",
                fontsize=8, color=MUTED)
    return save(fig, "ch06-sbti-diffusion",
                "Science Based Targets initiative, Target Dashboard (companies and targets files, "
                "downloaded October 2026); regions are UN M49.")


def wdi(indicator, name):
    z = zipfile.ZipFile(fetch(WDI.format(indicator), name))
    f = [n for n in z.namelist() if n.startswith("API_")][0]
    t = pd.read_csv(io.BytesIO(z.read(f)), skiprows=4)
    meta = [n for n in z.namelist() if n.startswith("Metadata_Country")][0]
    m = pd.read_csv(io.BytesIO(z.read(meta)))
    countries = set(m.loc[m.Region.notna(), "Country Code"])
    t = t[t["Country Code"].isin(countries)]
    return t.set_index("Country Code")[str(YEAR)].dropna()


def fig_export_pull(co):
    gdp = wdi("NY.GDP.MKTP.CD", "wdi_gdp.zip")
    gdppc = wdi("NY.GDP.PCAP.CD", "wdi_gdppc.zip")
    valid = co[co.near_term_status == "Validated Targets"]
    n = valid.location.map(M49).value_counts()
    adopt = (n.reindex(gdp.index, fill_value=0) / (gdp / 1e11))  # per US$100bn of GDP
    x = pd.read_csv(fetch(IMTS_URL, "imf_imts_exports_all.csv", headers=IMTS_HDR),
                    usecols=["COUNTRY", "COUNTERPART_COUNTRY", "TIME_PERIOD", "OBS_VALUE"])
    x = x[(x.TIME_PERIOD == YEAR) & x.COUNTRY.isin(gdp.index) & x.COUNTERPART_COUNTRY.isin(gdp.index)
          & (x.COUNTRY != x.COUNTERPART_COUNTRY)]
    x["w"] = x.OBS_VALUE / x.groupby("COUNTRY").OBS_VALUE.transform("sum")
    x["a"] = x.COUNTERPART_COUNTRY.map(adopt)
    emkt = x.groupby("COUNTRY").apply(lambda g: (g.w * g.a).sum(), include_groups=False)
    df = pd.DataFrame({"own": adopt, "emkt": emkt, "gdp": gdp, "pc": gdppc}).dropna()
    df = df[df.gdp >= 5e10]
    df["lown"] = np.log(df.own + 0.1)
    df["lemkt"] = np.log(df.emkt)
    df["lpc"] = np.log(df.pc)
    r = df[["lown", "lemkt"]].corr().iloc[0, 1]
    X = np.column_stack([np.ones(len(df)), df.lemkt, df.lpc])
    beta, *_ = np.linalg.lstsq(X, df.lown, rcond=None)
    resid = df.lown - X @ beta
    s2 = resid @ resid / (len(df) - 3)
    se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X)))
    X1 = np.column_stack([np.ones(len(df)), df.lemkt])
    b1, *_ = np.linalg.lstsq(X1, df.lown, rcond=None)
    res1 = df.lown - X1 @ b1
    se1 = np.sqrt(np.diag(res1 @ res1 / (len(df) - 2) * np.linalg.inv(X1.T @ X1)))
    r2_1 = 1 - res1 @ res1 / ((df.lown - df.lown.mean()) ** 2).sum()
    r2 = 1 - resid @ resid / ((df.lown - df.lown.mean()) ** 2).sum()
    Xp = np.column_stack([np.ones(len(df)), df.lpc])
    bp, *_ = np.linalg.lstsq(Xp, df.lown, rcond=None)
    resp = df.lown - Xp @ bp
    sep = np.sqrt(np.diag(resp @ resp / (len(df) - 2) * np.linalg.inv(Xp.T @ Xp)))
    r2_p = 1 - resp @ resp / ((df.lown - df.lown.mean()) ** 2).sum()
    print(f"[ch06] export-pull sample: {len(df)} economies with GDP >= $50bn in {YEAR}; "
          f"corr(log own, log export-market) = {r:.2f}")
    print(f"[ch06] OLS (1) export-market only: b={b1[1]:.2f} (se {se1[1]:.2f}), R2={r2_1:.2f}")
    print(f"[ch06] OLS (2) GDP pc only: b={bp[1]:.2f} (se {sep[1]:.2f}), R2={r2_p:.2f}")
    print(f"[ch06] OLS (3) both: b_emkt={beta[1]:.2f} (se {se[1]:.2f}), "
          f"b_pc={beta[2]:.2f} (se {se[2]:.2f}), R2={r2:.2f}")
    zero = (df.own == 0).sum()
    print(f"[ch06] economies with zero validated companies in sample: {zero}")
    for c in ["JPN", "GBR", "DEU", "USA", "CHN", "VNM", "MEX", "IND", "SAU", "RUS", "TUR",
              "DNK", "BGD", "CAN", "KOR"]:
        if c in df.index:
            print(f"[ch06]   {c}: own {df.loc[c, 'own']:.1f}, export-market {df.loc[c, 'emkt']:.1f}")
    fig, ax = figure(7.2, 4.6)
    ax.grid(axis="x", color=GRID)
    ax.scatter(df.emkt, df.own + 0.1, s=np.sqrt(df.gdp / 1e9) * 2.2, color=BLUE, alpha=0.55,
               edgecolor="white", linewidth=0.5)
    ax.set_xscale("log")
    ax.set_yscale("log")
    lab = {"JPN": "Japan", "GBR": "UK", "DEU": "Germany", "USA": "US", "CHN": "China",
           "MEX": "Mexico", "IND": "India", "SAU": "Saudi Arabia",
           "RUS": "Russia", "DNK": "Denmark", "CAN": "Canada", "BRA": "Brazil"}
    off = {"CHN": (-30, 8), "USA": (6, -12), "DEU": (-12, 10)}
    for c, name in lab.items():
        if c in df.index:
            ax.annotate(name, (df.loc[c, "emkt"], df.loc[c, "own"] + 0.1), xytext=off.get(c, (4, 3)),
                        textcoords="offset points", fontsize=8, color=INK)
    from matplotlib.ticker import FuncFormatter
    fmt = FuncFormatter(lambda v, _: f"{v:g}")
    for axis in (ax.xaxis, ax.yaxis):
        axis.set_major_formatter(fmt)
        axis.set_minor_formatter(FuncFormatter(lambda v, _: ""))
    ax.set_xticks([2, 5, 10, 20, 30])
    xs = np.linspace(df.lemkt.min(), df.lemkt.max(), 50)
    ax.plot(np.exp(xs), np.exp(b1[0] + b1[1] * xs), color=RED, lw=1.4)
    ax.set_xlabel("Export-market adoption: validated companies per US$100bn of GDP in the\n"
                  f"markets an economy sells to, weighted by {YEAR} export shares (log scale)")
    ax.set_ylabel("Own adoption: validated companies\nper US$100bn of GDP (log scale)")
    ax.set_title("Economies that sell to adopters adopt more —\n"
                 "the trading-up pattern, in a newer private standard")
    return save(fig, "ch06-sbti-export-pull",
                f"SBTi Target Dashboard (October 2026); IMF IMTS exports by partner, {YEAR}; "
                f"World Bank WDI GDP, {YEAR}.\nEconomies with GDP of US$50bn or more; bubble "
                "size proportional to GDP; zero adoption plotted at 0.1."), (b1, se1, r2_1, bp, sep,
                                                                               r2_p, beta, se, r2,
                                                                               len(df))


def main():
    tc = load_committees()
    made = [fig_output(), fig_secretariats(tc), fig_vintage(tc)]
    participation_table(tc)
    co, tg = sbti_data()
    made.append(fig_sbti_diffusion(co, tg))
    path, _ = fig_export_pull(co)
    made.append(path)
    return made


if __name__ == "__main__":
    main()
