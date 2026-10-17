"""Figures for Chapter 5, International institutions.

Data, all downloaded at source into .data-cache/:

* World Bank Group country voting tables (IBRD, IDA, IFC, MIGA), PDFs linked from
  https://www.worldbank.org/en/about/leadership/votingpowers (data as of 30 June 2026).
* World Development Indicators API: GDP at market exchange rates (NY.GDP.MKTP.CD) and at PPP
  (NY.GDP.MKTP.PP.CD), https://api.worldbank.org/v2/.
* ICSID case database, https://icsid.worldbank.org/cases/case-database (its JSON feed).
* ForeignAssistance.gov Country Summary, us_foreign_aid_country.csv (fiscal years 1946-2026),
  https://foreignassistance.gov/data -> Country Summary. The site has been unstable since 2025; the
  download link checked in October 2026 is the S3 file below. If it fails, put the file in
  .data-cache/fa_us_foreign_aid_country.csv by hand (or use the frozen mirror at
  foreignassistance.andrewheiss.com, and say so).
* United Nations, Countries elected members of the Security Council,
  https://main.un.org/securitycouncil/en/content/countries-elected-members (HTML page).
"""

import json
import re
from collections import Counter

import numpy as np
import pandas as pd
from pypdf import PdfReader

from style import BLUE, GRID, INK, MUTED, OUT, PALE_BLUE, RED, TEAL, fetch, figure, save

WB_TABLES = {
    "IBRD": "https://thedocs.worldbank.org/en/doc/a16374a6cee037e274c5e932bf9f88c6-0330032021/original/IBRDCountryVotingTable.pdf",
    "IFC": "https://thedocs.worldbank.org/en/doc/c80cbb3c6ece4fa9d06109541cef7d34-0330032021/original/IFCCountryVotingTable.pdf",
    "MIGA": "https://thedocs.worldbank.org/en/doc/569dd95ea1da3949a1dbeb8dd431de39-0330032021/original/MIGACountryVotingTable.pdf",
    "IDA": "https://thedocs.worldbank.org/en/doc/c89cb290d3ddb1edf2accc9c1409e03f-0330032025/original/IDACountryVotingTable.pdf",
}
ICSID_URL = "https://icsid.worldbank.org/api/all/cases"
FA_URL = "https://s3.amazonaws.com/files.explorer.devtechlab.com/us_foreign_aid_country.csv"
UNSC_URL = "https://main.un.org/securitycouncil/en/content/countries-elected-members"
BROWSER = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/120 Safari/537.36"}

# The economies compared in the vote-versus-weight figure: voting-table name -> ISO3.
ECONOMIES = {
    "UNITED STATES": "USA", "CHINA": "CHN", "JAPAN": "JPN", "GERMANY": "DEU", "INDIA": "IND",
    "UNITED KINGDOM": "GBR", "FRANCE": "FRA", "ITALY": "ITA", "CANADA": "CAN", "BRAZIL": "BRA",
    "RUSSIAN FEDERATION": "RUS", "KOREA, REPUBLIC OF": "KOR", "INDONESIA": "IDN",
    "SAUDI ARABIA": "SAU", "MEXICO": "MEX",
}
SHORT = {"USA": "United States", "CHN": "China", "JPN": "Japan", "DEU": "Germany", "IND": "India",
         "GBR": "United Kingdom", "FRA": "France", "ITA": "Italy", "CAN": "Canada", "BRA": "Brazil",
         "RUS": "Russia", "KOR": "Korea", "IDN": "Indonesia", "SAU": "Saudi Arabia", "MEX": "Mexico"}


# --------------------------------------------------------------------------- World Bank votes
def voting_table(inst):
    """Member -> percent of total voting power, parsed from a World Bank Group country table."""
    path = fetch(WB_TABLES[inst], f"wbg_{inst.lower()}_country_voting_table.pdf", headers=BROWSER)
    text = "\n".join(p.extract_text() for p in PdfReader(path).pages)
    out = {}
    for line in text.splitlines():
        line = line.strip()
        if inst == "IDA":   # MEMBER  VOTES  PERCENT
            m = re.match(r"^([A-Z][A-Z ,.'()&-]+?)\s+([\d,]+)\s+([\d.]+)\s*\*?$", line)
            if m:
                out[m.group(1).strip()] = float(m.group(3))
        else:               # MEMBER  AMOUNT  PCT  VOTES  PCT
            m = re.match(r"^([A-Z][A-Z ,.'()&-]+?)\s+([\d,.]+)\s+([\d.]+)\s+([\d,]+)\s+([\d.]+)", line)
            if m:
                out[m.group(1).strip()] = float(m.group(5))
    return out


def wdi(indicator, year=2025):
    iso = ";".join(list(ECONOMIES.values()) + ["WLD"])
    url = (f"https://api.worldbank.org/v2/country/{iso}/indicator/{indicator}"
           f"?format=json&per_page=500&date={year}")
    rows = json.loads(fetch(url, f"wdi_api_{indicator}_{year}_ch05.json").read_text())[1]
    return {r["countryiso3code"]: r["value"] for r in rows if r["value"] is not None}


def fig_votes_vs_weight():
    ibrd = voting_table("IBRD")
    gdp, ppp = wdi("NY.GDP.MKTP.CD"), wdi("NY.GDP.MKTP.PP.CD")
    rows = []
    for name, iso in ECONOMIES.items():
        rows.append({"iso": iso, "votes": ibrd[name], "gdp": 100 * gdp[iso] / gdp["WLD"],
                     "ppp": 100 * ppp[iso] / ppp["WLD"]})
    df = pd.DataFrame(rows).sort_values("gdp")
    df["gap"] = df["votes"] - df["gdp"]
    print("\nIBRD votes (30 June 2026) vs share of world GDP, 2025 (%):")
    print(df.round(2).to_string(index=False))

    fig, ax = figure(7.2, 4.8)
    ax.grid(axis="x", color=GRID); ax.grid(axis="y", visible=False)
    y = np.arange(len(df))
    for i, r in enumerate(df.itertuples()):
        ax.plot([r.votes, r.gdp], [i, i], color=GRID, lw=2.4, zorder=1)
    ax.scatter(df["gdp"], y, color=RED, s=34, zorder=3)
    ax.scatter(df["ppp"], y, facecolor="none", edgecolor=RED, s=30, lw=1.1, zorder=3)
    ax.scatter(df["votes"], y, color=BLUE, s=34, zorder=3)
    ax.set_yticks(y, [SHORT[i] for i in df["iso"]])
    ax.set_xlabel("Per cent of total")
    top = len(df) - 1
    ax.annotate("IBRD voting power", (df["votes"].iloc[top], top), xytext=(4, 9),
                textcoords="offset points", color=BLUE, fontsize=9, ha="center")
    ax.annotate("Share of world GDP\n(market rates)", (df["gdp"].iloc[top], top), xytext=(0, -26),
                textcoords="offset points", color=RED, fontsize=9, ha="center")
    chn = list(df["iso"]).index("CHN")
    ax.annotate("at PPP", (df["ppp"].iloc[chn], chn), xytext=(0, 7), textcoords="offset points",
                color=RED, fontsize=8.5, ha="center")
    ax.set_xlim(0, 28)
    ax.set_title("Votes lag weight: China's IBRD vote is a third of its share of world output")
    return save(fig, "ch05-votes-vs-weight",
                "World Bank Group, IBRD country voting table (30 June 2026); World Bank, World "
                "Development Indicators, GDP in current US$ and PPP, 2025.")


def us_china_table():
    print("\nUS and China voting power by World Bank Group institution (30 June 2026, %):")
    for inst in ("IBRD", "IDA", "IFC", "MIGA"):
        t = voting_table(inst)
        print(f"  {inst:5s} members parsed {len(t):3d}  US {t['UNITED STATES']:5.2f}  "
              f"Japan {t['JAPAN']:5.2f}  China {t['CHINA']:5.2f}  India {t['INDIA']:5.2f}  "
              f"Russia {t['RUSSIAN FEDERATION']:5.2f}")


# --------------------------------------------------------------------------- ICSID
def icsid_cases():
    path = fetch(ICSID_URL, "icsid_case_database.json", headers=BROWSER)
    data = json.loads(path.read_text())["data"]["GetAllCasesResult"]
    rows = []
    for c in data:
        dates = [p.get("dateregistered") for p in c["caseproceedings"] if p.get("dateregistered")]
        year = int(re.search(r"/(\d{4})", dates[0]).group(1)) if dates else None
        rows.append({"caseno": c["caseno"], "year": year, "status": c["status"],
                     "respondent": re.sub(r"\s+", " ", c["respondent"]).strip()})
    df = pd.DataFrame(rows)
    df["kind"] = df["caseno"].str.extract(r"^([A-Z]+)")[0]
    # ICSID Convention and Additional Facility arbitration and conciliation; drop the UNCITRAL and
    # other cases that ICSID only administers.
    return df[df["kind"].isin(["ARB", "CON"])].dropna(subset=["year"])


def fig_icsid(df):
    by_year = df.groupby("year").size().reindex(range(1972, 2027), fill_value=0)
    print(f"\nICSID cases (ARB + CON) in the online database: {len(df)}; "
          f"pending {int((df['status'] == 'Pending').sum())}")
    for a, b in [(1972, 1996), (1997, 2006), (2007, 2016), (2017, 2025)]:
        s = by_year.loc[a:b]
        print(f"  {a}-{b}: total {s.sum()}, mean per year {s.mean():.1f}")
    print(f"  2026 to date: {by_year.loc[2026]}; peak year {by_year.idxmax()} ({by_year.max()})")
    share = by_year.loc[2012:2025].sum() / by_year.loc[:2025].sum()
    print(f"  share of all cases registered 1972-2025 that were registered 2012-2025: {share:.1%}")

    fig, ax = figure(7.2, 3.9)
    colors = [MUTED if y == 2026 else BLUE for y in by_year.index]
    ax.bar(by_year.index, by_year.values, color=colors, width=0.8)
    ax.set_ylabel("Cases registered per year")
    ax.set_xlim(1970.5, 2027)
    ax.annotate("Bilateral investment\ntreaties come of age", (1997, 10), xytext=(1984, 32),
                fontsize=8.5, color=INK, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    ax.annotate("Argentina's\ncrisis claims", (2003, 31), xytext=(1996, 50), fontsize=8.5,
                color=INK, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    ax.annotate("2026: to\nmid-October", (2026, by_year.loc[2026]), xytext=(2019.5, 76),
                fontsize=8.5, color=MUTED, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    ax.set_ylim(0, 85)
    ax.set_title("Investor–state arbitration at ICSID became a mass procedure after 1997")
    return save(fig, "ch05-icsid-cases",
                "ICSID case database (Convention and Additional Facility arbitration and "
                "conciliation, by year of registration), downloaded October 2026.")


def icsid_table(df):
    top = df["respondent"].value_counts().head(10)
    print("\nICSID respondent states, top 10 (ARB + CON):")
    for name, n in top.items():
        sub = df[df["respondent"] == name]
        print(f"  {name:40s} {n:3d}  first {int(sub['year'].min())}  last {int(sub['year'].max())}  "
              f"pending {int((sub['status'] == 'Pending').sum())}")
    print(f"  top-10 share of all cases: {top.sum() / len(df):.1%}")
    by = df.groupby(["respondent", "year"]).size()
    tot = df.groupby("year").size()
    for name, yrs in [("Argentine Republic", [2003]), ("Kingdom of Spain", [2015]),
                      ("Bolivarian Republic of Venezuela", [2011, 2012])]:
        n = sum(by.get((name, y), 0) for y in yrs)
        print(f"  {name} in {yrs}: {n} of {sum(tot[y] for y in yrs)} cases registered")


# --------------------------------------------------------------------------- UNSC and US aid
IDEAL_URL = "https://dataverse.harvard.edu/api/access/datafile/14098429"
GROUPS = [
    ("G7", ["USA", "CAN", "GBR", "FRA", "DEU", "ITA", "JPN"]),
    ("BRICS founders", ["BRA", "RUS", "IND", "CHN", "ZAF"]),
    ("BRICS members\nsince 2024–25", ["EGY", "ETH", "IRN", "ARE", "IDN"]),
    ("BRICS partner\ncountries", ["BLR", "BOL", "KAZ", "CUB", "MYS", "THA", "UGA", "UZB", "NGA",
                                  "VNM"]),
]


def fig_brics_alignment():
    """UNGA ideal points (Bailey, Strezhnev & Voeten), latest session, by club."""
    ip = pd.read_csv(fetch(IDEAL_URL, "unga_idealpoints_2026FP.csv"))
    year = int(ip["year"].max())
    y = ip[ip["year"] == year].set_index("iso3c")["IdealPointFP"]
    print(f"\nUNGA ideal points, {year}: {len(y)} members; median {y.median():.2f}")
    fig, ax = figure(7.2, 3.9)
    ax.grid(axis="x", color=GRID); ax.grid(axis="y", visible=False)
    rows = list(reversed(GROUPS))
    for i, (label, isos) in enumerate(rows):
        ax.scatter(y.values, np.full(len(y), i), color=GRID, s=14, zorder=1)
        v = y.reindex(isos)
        col = BLUE if label == "G7" else RED
        ax.scatter(v.values, np.full(len(v), i), color=col, s=34, zorder=3)
        print(f"  {label.replace(chr(10), ' ')}: median {v.median():.2f}, range {v.min():.2f} to "
              f"{v.max():.2f}; " + ", ".join(f"{k} {x:.2f}" for k, x in v.items()))
    brics = y.reindex(sum([g[1] for g in GROUPS[1:]], []))
    inside = ((y >= brics.min()) & (y <= brics.max())).mean()
    print(f"  share of all members within the BRICS-and-partners range: {inside:.0%}; "
          f"SAU (ambiguous status) {y['SAU']:.2f}")
    for iso_, dx, dy in [("USA", 0, 9), ("CUB", 0, 9), ("IRN", 0, 9), ("RUS", 0, 9),
                         ("IND", 0, -14), ("JPN", 0, -14)]:
        i = [k for k, (_, g) in enumerate(rows) if iso_ in g][0]
        ax.annotate(SHORT.get(iso_, {"CUB": "Cuba", "IRN": "Iran"}.get(iso_)), (y[iso_], i),
                    xytext=(dx, dy), textcoords="offset points", ha="center", fontsize=8.5)
    ax.set_yticks(range(len(rows)), [r[0] for r in rows])
    ax.set_ylim(-0.6, len(rows) - 0.4)
    ax.set_xlabel(f"UN General Assembly ideal point, {year} (grey: all {len(y)} members)")
    ax.set_title("BRICS and its partners sit in the Assembly's crowded middle, not at a pole")
    return save(fig, "ch05-brics-alignment",
                f"Bailey, Strezhnev & Voeten, UN General Assembly ideal points (Harvard Dataverse, "
                f"doi:10.7910/DVN/LEJUQZ), {year} session; BRICS membership as of 2026.")


UN_TO_ISO = {
    "Bolivia (Plurinational State of)": "BOL", "Cabo Verde": "CPV", "Côte d'Ivoire": "CIV",
    "Democratic Republic of the Congo": "COD", "Zaire": "COD", "Congo": "COG",
    "Iran (Islamic Republic of)": "IRN", "Libya": "LBY", "United Republic of Tanzania": "TZA",
    "Venezuela (Bolivarian Republic of)": "VEN", "Viet Nam": "VNM", "Syrian Arab Republic": "SYR",
    "Republic of Korea": "KOR", "Türkiye": "TUR", "Turkey": "TUR", "Egypt": "EGY",
    "Gambia": "GMB", "Guinea-Bissau": "GNB", "Lao People's Democratic Republic": "LAO",
    "North Macedonia": "MKD", "Russian Federation": "RUS", "Czechia": "CZE",
    "United Arab Emirates": "ARE", "Sri Lanka": "LKA", "Myanmar": "MMR", "Burma": "MMR",
    "Yemen": "YEM", "Somalia": "SOM", "Sudan": "SDN", "Eswatini": "SWZ",
    "Libyan Arab Jamahiriya": "LBY", "Czech Republic": "CZE", "Slovakia": "SVK",
    "Yugoslavia": "YUF", "Saint Vincent and the Grenadines": "VCT",
}


def unsc_terms():
    path = fetch(UNSC_URL, "un_unsc_elected_members.html", headers=BROWSER)
    html = path.read_text(errors="ignore")
    html = re.sub(r"<script.*?</script>|<style.*?</style>", "", html, flags=re.S)
    text = re.sub(r"<[^>]+>", "|", html).replace("&nbsp;", " ")
    text = re.sub(r"\s*\|[\s|]*", "|", text)
    start = text.find("at least once since 1946.")
    cells = text[start:].split("|")[1:]
    terms, name = [], None
    for cell in cells:
        cell = re.sub(r"\s+", " ", cell).strip()
        if not cell:
            continue
        if cell == "About":     # the list ends where the page's navigation menu begins
            break
        if re.match(r"^\d{4}", cell):
            # "1950-1951, 1956, 1972-1973": two-year terms (split one-year seats are skipped)
            terms += [(name, int(a), int(b)) for a, b in re.findall(r"(\d{4})-(\d{4})", cell)]
        else:
            name = cell
    return pd.DataFrame(terms, columns=["country", "start", "end"])


OECD_BY_1973 = {"AUT", "BEL", "CAN", "DNK", "FRA", "DEU", "GRC", "ISL", "IRL", "ITA", "JPN", "LUX",
                "NLD", "NOR", "PRT", "ESP", "SWE", "CHE", "TUR", "GBR", "USA", "FIN", "AUS", "NZL"}


def aid_panel():
    path = fetch(FA_URL, "fa_us_foreign_aid_country.csv")
    fa = pd.read_csv(path)
    fa = fa[(fa["Transaction Type Name"] == "Obligations") & (fa["Fiscal Year"] != "1976tq")]
    fa = fa[~fa["Country Name"].str.endswith("Region") & (fa["Country Name"] != "World")]
    fa["year"] = fa["Fiscal Year"].astype(int)
    names = dict(zip(fa["Country Name"], fa["Country Code"]))
    panel = fa.groupby(["Country Code", "year"])["constant_amount"].sum()
    return panel, names


def fig_unsc_aid():
    """Event-time re-estimate: log US aid around the first year of a Council term.

    Each country-year's log aid is first expressed relative to the mean log aid of all recipients
    that year (a year effect, which removes the rise and fall of the whole aid budget), then
    relative to the country's own average over event years -3..-1. Terms need positive
    obligations in all seven years -3..+3 so that logs exist.
    """
    terms = unsc_terms()
    panel, names = aid_panel()
    lower = {k.lower(): v for k, v in names.items() if isinstance(v, str)}

    def iso(c):
        c0 = c.split("(see")[0].strip()
        return UN_TO_ISO.get(c0) or lower.get(c0.lower())

    terms["iso"] = terms["country"].map(iso)
    print(f"\nUNSC: {len(terms)} elected two-year terms parsed for {terms['country'].nunique()} "
          f"names; unmatched: {sorted(terms.loc[terms['iso'].isna(), 'country'].unique())}")
    window = terms[(terms["start"] >= 1970) & (terms["start"] <= 2010)]
    print(f"  terms starting 1970-2010: {len(window)}")
    p = panel[panel > 0].rename("aid").reset_index()
    p.columns = ["iso", "year", "aid"]
    p = p[~p["iso"].isin(OECD_BY_1973)]
    p["log"] = np.log(p["aid"])
    p["adj"] = p["log"] - p.groupby("year")["log"].transform("mean")
    lookup = p.set_index(["iso", "year"])

    def event_matrix(sel, col):
        rows = []
        for r in sel.dropna(subset=["iso"]).itertuples():
            if r.iso in OECD_BY_1973:
                continue
            keys = [(r.iso, y) for y in range(r.start - 3, r.start + 4)]
            if not all(k in lookup.index for k in keys):
                continue
            v = lookup.loc[keys, col].to_numpy()
            rows.append(v - v[:3].mean())
        return pd.DataFrame(rows, columns=range(-3, 4))

    def pct(x):
        return 100 * (np.exp(x) - 1)

    results = {}
    for label, lo, hi, col in [("1970-2010, year-adjusted", 1970, 2010, "adj"),
                               ("1970-2010, raw logs", 1970, 2010, "log"),
                               ("1970-1989, year-adjusted", 1970, 1989, "adj"),
                               ("1990-2010, year-adjusted", 1990, 2010, "adj")]:
        d = event_matrix(terms[(terms["start"] >= lo) & (terms["start"] <= hi)], col)
        m, se = d.mean(), d.std() / np.sqrt(len(d))
        results[label] = (d, m, se)
        print(f"  {label}: {len(d)} terms; % difference from pre-term average (s.e. of log):")
        print("    " + "  ".join(f"{k:+d}: {pct(m[k]):+4.0f}% ({se[k]:.2f})" for k in m.index))
        term = d[[0, 1]].mean(axis=1)
        print(f"    term years (0, +1) vs baseline: {pct(term.mean()):+.1f}% "
              f"(95% CI {pct(term.mean() - 1.96 * term.std() / np.sqrt(len(d))):+.0f}% to "
              f"{pct(term.mean() + 1.96 * term.std() / np.sqrt(len(d))):+.0f}%); "
              f"share of terms above baseline {(term > 0).mean():.0%}")

    d, m, se = results["1970-2010, year-adjusted"]
    fig, ax = figure(7.2, 3.9)
    ax.axvspan(-0.5, 1.5, color=PALE_BLUE, zorder=0)
    ax.axhline(0, color=MUTED, lw=1, ls="--")
    x = list(m.index)
    ax.fill_between(x, pct(m - 1.96 * se), pct(m + 1.96 * se), color=RED, alpha=0.15, lw=0)
    ax.plot(x, pct(m), color=RED, marker="o", zorder=3)
    ax.axhline(59, color=TEAL, lw=1.2, ls=":")
    ax.text(-3.2, 61, "Kuziemko and Werker's headline estimate for elected members: +59%",
            color=TEAL, fontsize=8.5, va="bottom")
    ax.text(0.5, -44, "On the Council", ha="center", color=BLUE, fontsize=9, fontweight="bold")
    ax.text(3.1, pct(m.iloc[-1]) + 12, "Mean, with\n95% interval", color=RED, fontsize=8.5,
            va="center")
    ax.set_xticks(x, ["−3", "−2", "−1", "0", "+1", "+2", "+3"])
    ax.set_xlabel("Years relative to the first year of a Security Council term (−1 = election year)")
    ax.set_ylabel("US aid, % difference from the\ncountry's pre-term average")
    ax.set_xlim(-3.3, 4.0)
    ax.set_ylim(-50, 75)
    ax.set_title("On current data, a simple event-time comparison does not show the jump")
    save(fig, "ch05-unsc-aid",
         f"ForeignAssistance.gov Country Summary (US obligations, constant $, 2026 release); "
         f"UN, elected members\nof the Security Council. {len(d)} terms by developing countries "
         f"starting 1970–2010; log aid net of the year's mean across recipients.")
    return results


def main():
    made = [fig_votes_vs_weight()]
    us_china_table()
    cases = icsid_cases()
    made.append(fig_icsid(cases))
    icsid_table(cases)
    made.append(fig_brics_alignment())
    fig_unsc_aid()
    made.append(OUT / "ch05-unsc-aid.png")
    return made


if __name__ == "__main__":
    main()
