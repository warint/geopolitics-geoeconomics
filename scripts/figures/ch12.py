"""Chapter 12 — From indicators to decisions. Figures that set the book's series side by side.

Data, downloaded at source into .data-cache/:
- Caldara and Iacoviello, Geopolitical Risk index (global and country indices)
  https://www.matteoiacoviello.com/gpr_files/data_gpr_export.xls
- Baker, Bloom and Davis, Global Economic Policy Uncertainty index
  https://www.policyuncertainty.com/media/Global_Policy_Uncertainty_Data.xlsx
- Hassan, Hollander, van Lent and Tahoun, firm-level political risk, vintage 2022q1 (tab-separated)
  https://www.dropbox.com/s/96xo9f1twlu3525/firmquarter_2022q1.csv?raw=1 (linked from
  https://www.firmlevelrisk.com/download). The file is 76 MB; if the Dropbox link fails, download it
  from the landing page into .data-cache/flr_firmquarter_2022q1.csv.
- Cboe, VIX index daily history, https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv
- Federal Reserve Bank of New York, Global Supply Chain Pressure Index
  https://www.newyorkfed.org/medialibrary/research/interactives/gscpi/downloads/gscpi_data.xlsx
- World Bank, Worldwide Governance Indicators, 2025 edition (sheet `pv`, Governance score 0-100)
  https://www.worldbank.org/content/dam/sites/govindicators/doc/wgidataset_with_sourcedata-2025.xlsx
- Henisz, POLCON 2025 (POLCONIII_2025), sheet `Data`
  https://mgmt.wharton.upenn.edu/wp-content/uploads/2026/03/POLCON_2025_FINALPOSTED.xlsx

The text-based and market series are revised or extended monthly, so the numbers printed below are
those of the vintages in the cache; delete the cache files to redraw from the current data.
"""

import numpy as np
import pandas as pd

from style import (BLUE, GOLD, GRID, INK, MUTED, PALE_BLUE, PALE_RED, RED, TEAL, fetch, figure,
                   plt, save)

UA = {"User-Agent": "Mozilla/5.0"}
GPR_URL = "https://www.matteoiacoviello.com/gpr_files/data_gpr_export.xls"
EPU_URL = "https://www.policyuncertainty.com/media/Global_Policy_Uncertainty_Data.xlsx"
FLR_URL = "https://www.dropbox.com/s/96xo9f1twlu3525/firmquarter_2022q1.csv?raw=1"
VIX_URL = "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv"
GSCPI_URL = ("https://www.newyorkfed.org/medialibrary/research/interactives/gscpi/downloads/"
             "gscpi_data.xlsx")
WGI_URL = ("https://www.worldbank.org/content/dam/sites/govindicators/doc/"
           "wgidataset_with_sourcedata-2025.xlsx")
POLCON_URL = "https://mgmt.wharton.upenn.edu/wp-content/uploads/2026/03/POLCON_2025_FINALPOSTED.xlsx"

COW = {"ARG": 160, "AUS": 900, "BEL": 211, "BRA": 140, "CAN": 20, "CHE": 225, "CHL": 155,
       "CHN": 710, "COL": 100, "DEU": 255, "DNK": 390, "EGY": 651, "ESP": 230, "FIN": 375,
       "FRA": 220, "GBR": 200, "HUN": 310, "IDN": 850, "IND": 750, "ISR": 666, "ITA": 325,
       "JPN": 740, "KOR": 732, "MEX": 70, "MYS": 820, "NLD": 210, "NOR": 385, "PER": 135,
       "PHL": 840, "POL": 290, "PRT": 235, "RUS": 365, "SAU": 670, "SWE": 380, "THA": 800,
       "TUN": 616, "TUR": 640, "TWN": 713, "UKR": 369, "USA": 2, "VEN": 101, "VNM": 816,
       "ZAF": 560}
NAMES = {"ARG": "Argentina", "AUS": "Australia", "BEL": "Belgium", "BRA": "Brazil",
         "CAN": "Canada", "CHE": "Switzerland", "CHL": "Chile", "CHN": "China", "COL": "Colombia",
         "DEU": "Germany", "DNK": "Denmark", "EGY": "Egypt", "ESP": "Spain", "FIN": "Finland",
         "FRA": "France", "GBR": "United Kingdom", "HUN": "Hungary", "IDN": "Indonesia",
         "IND": "India", "ISR": "Israel", "ITA": "Italy", "JPN": "Japan", "KOR": "South Korea",
         "MEX": "Mexico", "MYS": "Malaysia", "NLD": "Netherlands", "NOR": "Norway", "PER": "Peru",
         "PHL": "Philippines", "POL": "Poland", "PRT": "Portugal", "RUS": "Russia",
         "SAU": "Saudi Arabia", "SWE": "Sweden", "THA": "Thailand", "TUN": "Tunisia",
         "TUR": "Türkiye", "TWN": "Taiwan", "UKR": "Ukraine", "USA": "United States",
         "VEN": "Venezuela", "VNM": "Vietnam", "ZAF": "South Africa"}


def quarterly(s):
    return s.resample("QE").mean()


def load_series():
    g = pd.read_excel(fetch(GPR_URL, "gpr_export.xls"))
    g = g.dropna(subset=["month"]).set_index("month")
    g.index = pd.to_datetime(g.index)
    e = pd.read_excel(fetch(EPU_URL, "epu_global.xlsx"))
    e = e[pd.to_numeric(e["Year"], errors="coerce").notna() & e["Month"].notna()]
    e.index = pd.to_datetime(dict(year=e["Year"].astype(int), month=e["Month"].astype(int), day=1))
    f = pd.read_csv(fetch(FLR_URL, "flr_firmquarter_2022q1.csv"), sep="\t",
                    usecols=["date", "PRisk"])
    f["q"] = pd.PeriodIndex(f["date"].str.upper(), freq="Q").to_timestamp(how="end").normalize()
    prisk = f.groupby("q")["PRisk"].mean()
    prisk.index = prisk.index + pd.offsets.QuarterEnd(0)
    v = pd.read_csv(fetch(VIX_URL, "cboe_VIX_History.csv", headers=UA))
    v.index = pd.to_datetime(v["DATE"], format="%m/%d/%Y")
    x = pd.read_excel(fetch(GSCPI_URL, "nyfed_gscpi_data.xlsx", headers=UA),
                      sheet_name="GSCPI Monthly Data").dropna(subset=["GSCPI"])
    x.index = pd.to_datetime(x["Date"], format="%d-%b-%Y")
    q = pd.DataFrame({
        "Geopolitical risk (newspapers)": quarterly(g["GPR"]),
        "Policy uncertainty (newspapers)": quarterly(e["GEPU_current"].astype(float)),
        "Political risk (earnings calls)": prisk,
        "Market volatility (VIX)": quarterly(v["CLOSE"]),
        "Supply-chain pressure (GSCPI)": quarterly(x["GSCPI"]),
    })
    return g, q.loc["2002":"2026-06"]


def fig_families(q):
    common = q.loc[:"2022-03"].dropna()
    z = (q - common.mean()) / common.std()
    events = [("2003-03", "Iraq"), ("2008-10", "Lehman"), ("2016-09", "Brexit,\nTrump"),
              ("2020-03", "Covid"), ("2022-03", "Ukraine")]
    cols = [RED, GOLD, BLUE, TEAL, MUTED]
    fig, axes = plt.subplots(len(q.columns), 1, figsize=(7.4, 7.2), sharex=True)
    fig.add_artist(plt.Line2D([0.0, 0.07], [1.0, 1.0], transform=fig.transFigure, color=RED,
                              linewidth=4, solid_capstyle="butt"))
    for ax, name, col in zip(axes, q.columns, cols):
        s = z[name].dropna()
        ax.fill_between(s.index, 0, s.values, where=s.values > 0, color=col, alpha=0.25, lw=0)
        ax.plot(s.index, s.values, color=col, lw=1.4)
        ax.axhline(0, color=MUTED, lw=0.6)
        ax.set_ylim(-2.5, 6.5)
        ax.set_yticks([0, 3, 6])
        ax.text(pd.Timestamp("2009-09-01"), 6.2, name, fontsize=9, fontweight="bold", color=col,
                va="top")
        peak = s.idxmax()
        ax.plot([peak], [s.max()], "o", ms=4, color=INK)
        ax.annotate(f"peak {peak.year}Q{peak.quarter}", (peak, s.max()), xytext=(4, -2),
                    textcoords="offset points", fontsize=7.5, color=INK, va="top")
        for m, _ in events:
            ax.axvline(pd.Timestamp(m), color=GRID, lw=0.8, zorder=0)
    for m, label in events:
        axes[0].text(pd.Timestamp(m), 7.0, label, fontsize=7.5, color=MUTED, ha="center",
                     va="bottom")
    axes[2].set_ylabel("Standard deviations from the 2002–2022Q1 mean")
    fig.suptitle("Five measures of risk, five different crises at the top", x=0.0, ha="left",
                 fontweight="bold", fontsize=12, y=1.04)
    fig.subplots_adjust(hspace=0.12)
    print(f"[families] common sample {common.index[0]:%Y-%m} to {common.index[-1]:%Y-%m}, "
          f"{len(common)} quarters")
    for name in q.columns:
        s = z[name].dropna()
        top = s.sort_values(ascending=False).head(3)
        print(f"[families] {name}: peak {s.idxmax():%Y-%m} z={s.max():.1f}; top three "
              + ", ".join(f"{d.year}Q{d.quarter}" for d in top.index)
              + f"; last {s.index[-1]:%Y-%m} z={s.iloc[-1]:.1f}")
    print("[families] correlations over the common sample (quarterly levels):")
    print(common.corr().round(2).to_string())
    ch = common.diff().dropna()
    print("[families] correlations of quarterly changes:")
    print(ch.corr().round(2).to_string())
    ranks = common.rank(ascending=False)
    for d in ["2003-03-31", "2008-12-31", "2020-03-31", "2020-06-30", "2021-12-31", "2022-03-31"]:
        print(f"[families] rank of {d} among {len(common)} quarters: "
              + ", ".join(f"{k.split(' (')[0]} {int(r)}" for k, r in ranks.loc[d].items()))
    return save(fig, "ch12-families", "Caldara and Iacoviello (GPR); Baker, Bloom and Davis "
                "(global EPU); Hassan et al. (mean firm PRisk, to 2022Q1); Cboe (VIX); New York Fed "
                "(GSCPI). Quarterly means, standardised on 2002–2022Q1.")


def load_country(g):
    w = pd.read_excel(fetch(WGI_URL, "wgi_2025.xlsx", headers=UA), sheet_name="pv",
                      usecols=["Economy (code)", "Year", "Governance score (0-100)"])
    w.columns = ["code", "year", "score"]
    pc = pd.read_excel(fetch(POLCON_URL, "polcon_2025.xlsx", headers=UA), sheet_name="Data",
                       usecols=["ccode", "year", "POLCONIII_2025"])
    gpr_c = g[[c for c in g.columns if c.startswith("GPRC_")]].resample("YE").mean()
    gpr_c.index = gpr_c.index.year
    gpr_c.columns = [c[5:] for c in gpr_c.columns]
    return w, pc, gpr_c


def fig_country(w, pc, gpr_c):
    countries = [("RUS", "Russia"), ("UKR", "Ukraine"), ("ISR", "Israel")]
    rows = [("Geopolitical risk in the press\n(share of articles, %)", BLUE),
            ("Political stability, expert view\n(WGI score, 0–100; lower = less stable)", GOLD),
            ("Political constraint\n(POLCON III, 0–1)", TEAL)]
    fig, axes = plt.subplots(3, 3, figsize=(7.6, 6.0), sharex=True)
    fig.add_artist(plt.Line2D([0.0, 0.07], [1.0, 1.0], transform=fig.transFigure, color=RED,
                              linewidth=4, solid_capstyle="butt"))
    yrs = range(2002, 2026)
    for j, (code, name) in enumerate(countries):
        series = [gpr_c[code].reindex(yrs),
                  w[w["code"] == code].set_index("year")["score"].reindex(yrs),
                  pc[pc["ccode"] == COW[code]].set_index("year")["POLCONIII_2025"].reindex(yrs)]
        for i, (s, (label, col)) in enumerate(zip(series, rows)):
            ax = axes[i, j]
            ax.plot(s.index, s.values, color=col, lw=1.8)
            for yr in (2014, 2022):
                ax.axvline(yr, color=GRID, lw=0.8, zorder=0)
            if i == 0:
                ax.set_title(name, fontsize=10)
            if j == 0:
                ax.set_ylabel(label, fontsize=7.5)
            ax.tick_params(labelsize=7.5)
        g, wg, p = series
        print(f"[country] {name}: GPR share 2013 {g[2013]:.2f}, 2014 {g[2014]:.2f}, 2021 "
              f"{g[2021]:.2f}, 2022 {g[2022]:.2f}, 2023 {g[2023]:.2f}, 2025 {g[2025]:.2f}; WGI 2013 "
              f"{wg[2013]:.1f}, 2014 {wg[2014]:.1f}, 2021 {wg[2021]:.1f}, 2022 {wg[2022]:.1f}, "
              f"2023 {wg[2023]:.1f}, 2024 {wg[2024]:.1f}; POLCON 2013 {p[2013]:.2f}, 2021 "
              f"{p[2021]:.2f}, 2022 {p[2022]:.2f}, 2025 {p[2025]:.2f}")
    for i in range(3):
        lo = min(axes[i, j].get_ylim()[0] for j in range(3))
        hi = max(axes[i, j].get_ylim()[1] for j in range(3))
        for j in range(3):
            axes[i, j].set_ylim(lo, hi)
    axes[2, 0].set_xticks([2005, 2014, 2022])
    fig.suptitle("Three families, three verdicts on the same wars", x=0.0, ha="left",
                 fontweight="bold", fontsize=12, y=1.04)
    fig.subplots_adjust(hspace=0.15, wspace=0.25)
    return save(fig, "ch12-countries", "Caldara and Iacoviello, country GPR (annual mean of "
                "monthly shares); World Bank, WGI 2025 edition, political stability score; "
                "Henisz, POLCON 2025. Vertical lines: 2014 and 2022.")


def fig_composite(w, pc, gpr_c):
    year = 2024
    d = pd.DataFrame({"gpr": gpr_c.loc[year]})
    d["wgi"] = w[w["year"] == year].set_index("code")["score"]
    p = pc[pc["year"] == year].set_index("ccode")["POLCONIII_2025"]
    d["polcon"] = [p.get(COW.get(c, -1), np.nan) for c in d.index]
    d = d.dropna()
    # Normalise each to 0-1 with 1 = most risk: more press attention, less stability, less constraint.
    r = pd.DataFrame({
        "text": (d["gpr"] - d["gpr"].min()) / (d["gpr"].max() - d["gpr"].min()),
        "expert": (d["wgi"].max() - d["wgi"]) / (d["wgi"].max() - d["wgi"].min()),
        "structure": (d["polcon"].max() - d["polcon"]) / (d["polcon"].max() - d["polcon"].min()),
    })
    schemes = {"Equal weights": (1 / 3, 1 / 3, 1 / 3), "Press-heavy": (0.6, 0.2, 0.2),
               "Expert-heavy": (0.2, 0.6, 0.2), "Constraint-heavy": (0.2, 0.2, 0.6)}
    ranks = pd.DataFrame({k: (r @ np.array(wt)).rank(ascending=False).astype(int)
                          for k, wt in schemes.items()})
    ranks["lo"], ranks["hi"] = ranks.min(axis=1), ranks.max(axis=1)
    ranks = ranks.sort_values("Equal weights")
    print(f"[composite] {len(d)} countries with all three indicators in {year}")
    print(ranks.assign(name=[NAMES[c] for c in ranks.index]).to_string())
    print(f"[composite] median rank range {(ranks['hi'] - ranks['lo']).median():.0f}; countries "
          f"moving 10+ places {(ranks['hi'] - ranks['lo'] >= 10).sum()}")
    top10 = {k: set(ranks.index[ranks[k] <= 10]) for k in schemes}
    always = set.intersection(*top10.values())
    print(f"[composite] in the top ten under all four schemes: {sorted(NAMES[c] for c in always)}")
    print("[composite] raw values:", d.round(2).loc[ranks.index[:12]].to_dict("index"))
    fig, ax = figure(7.4, 6.4)
    ax.grid(False)
    ax.grid(axis="x", color=GRID, lw=0.8)
    yy = np.arange(len(ranks))[::-1]
    marks = {"Press-heavy": (BLUE, "o"), "Expert-heavy": (GOLD, "s"),
             "Constraint-heavy": (TEAL, "D"), "Equal weights": (RED, "|")}
    for y, (code, row) in zip(yy, ranks.iterrows()):
        ax.plot([row["lo"], row["hi"]], [y, y], color=GRID, lw=3, solid_capstyle="round",
                zorder=1)
    for k, (col, m) in marks.items():
        ax.scatter(ranks[k], yy, color=col, marker=m, s=60 if m == "|" else 18, zorder=3,
                   lw=2 if m == "|" else 0)
    ax.set_yticks(yy)
    ax.set_yticklabels([NAMES[c] for c in ranks.index], fontsize=7.5)
    ax.set_xlim(0.5, len(ranks) + 0.5)
    ax.invert_xaxis()
    ax.set_xlabel("Rank, 1 = riskiest (countries ordered by the equal-weight rank)")
    ax.set_ylim(-1, len(ranks) + 2.2)
    lx = len(ranks) - 1
    for i, (k, (col, m)) in enumerate(marks.items()):
        ax.scatter([lx - i * 9.5], [len(ranks) + 1.1], color=col, marker=m,
                   s=60 if m == "|" else 18, lw=2 if m == "|" else 0)
        ax.text(lx - i * 9.5 - 0.6, len(ranks) + 1.1, k, fontsize=7.5, va="center", color=col)
    ax.set_title("Who is riskiest depends on whose weights: one composite, four rankings")
    return save(fig, "ch12-composite", f"Composite of country GPR (press), WGI political "
                f"stability (expert) and POLCON III (constraint), {year}, each rescaled 0–1 "
                "across the countries shown; weights as labelled.")


def main():
    g, q = load_series()
    w, pc, gpr_c = load_country(g)
    return [fig_families(q), fig_country(w, pc, gpr_c), fig_composite(w, pc, gpr_c)]


if __name__ == "__main__":
    main()
