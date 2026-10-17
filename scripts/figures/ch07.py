"""Figures and numbers for Chapter 7, Measuring risk: text and indices.

Sources, all downloaded at source into .data-cache/:
- Caldara & Iacoviello, Geopolitical Risk index, data_gpr_export.xls
  (https://www.matteoiacoviello.com/gpr_files/data_gpr_export.xls)
- Baker, Bloom & Davis, Economic Policy Uncertainty: global index and country indices
  (https://www.policyuncertainty.com/media/Global_Policy_Uncertainty_Data.xlsx,
   https://www.policyuncertainty.com/media/All_Country_Data.xlsx)
- Hassan, Hollander, van Lent & Tahoun, firm-level political risk, vintage 2022q1
  (firmlevelrisk.com/download -> Dropbox, tab-separated despite the .csv extension)
- World Bank, Worldwide Governance Indicators, 2025 edition, sheet pv
  (https://www.worldbank.org/content/dam/sites/govindicators/doc/wgidataset_with_sourcedata-2025.xlsx)
"""

import numpy as np
import pandas as pd

from style import BLUE, GRID, MUTED, PALE_RED, RED, fetch, figure, save

GPR_URL = "https://www.matteoiacoviello.com/gpr_files/data_gpr_export.xls"
EPU_URL = "https://www.policyuncertainty.com/media/Global_Policy_Uncertainty_Data.xlsx"
EPU_C_URL = "https://www.policyuncertainty.com/media/All_Country_Data.xlsx"
FLR_URL = "https://www.dropbox.com/s/96xo9f1twlu3525/firmquarter_2022q1.csv?raw=1"
WGI_URL = ("https://www.worldbank.org/content/dam/sites/govindicators/doc/"
           "wgidataset_with_sourcedata-2025.xlsx")


def load_gpr():
    g = pd.read_excel(fetch(GPR_URL, "gpr_export.xls"))
    g["month"] = pd.to_datetime(g["month"])
    return g


def load_epu_global():
    e = pd.read_excel(fetch(EPU_URL, "epu_global.xlsx"))
    e = e[pd.to_numeric(e["Year"], errors="coerce").notna() & e["Month"].notna()].copy()
    e["month"] = pd.to_datetime(dict(year=e["Year"].astype(int), month=e["Month"].astype(int), day=1))
    return e.set_index("month")[["GEPU_current", "GEPU_ppp"]].astype(float)


def load_epu_us_quarterly():
    e = pd.read_excel(fetch(EPU_C_URL, "epu_all_country.xlsx"), sheet_name="EPU")
    e = e[pd.to_numeric(e["Year"], errors="coerce").notna() & e["Month"].notna()].copy()
    e["q"] = pd.PeriodIndex(pd.to_datetime(dict(year=e["Year"].astype(int),
                                                month=e["Month"].astype(int), day=1)), freq="Q")
    return e.groupby("q")["US"].mean()


def fig_threats_acts(g):
    d = g[g["month"] >= "1985-01-01"].set_index("month")
    ann = d[["GPRT", "GPRA"]].rolling(3, center=True).mean()
    fig, ax = figure(7.4, 4.0)
    ax.plot(ann.index, ann["GPRT"], color=RED, lw=1.4)
    ax.plot(ann.index, ann["GPRA"], color=BLUE, lw=1.4)
    last = ann.dropna().index[-1]
    ax.text(last, ann["GPRT"].dropna().iloc[-1] + 25, " Threats", color=RED, fontsize=9, fontweight="bold")
    ax.text(last, ann["GPRA"].dropna().iloc[-1] - 45, " Acts", color=BLUE, fontsize=9, fontweight="bold")
    events = {"1991-01-01": "Gulf War", "2001-09-01": "9/11", "2003-03-01": "Iraq invasion",
              "2014-03-01": "Crimea", "2022-02-01": "Ukraine invasion"}
    for date, lab in events.items():
        t = pd.Timestamp(date)
        y = max(ann.loc[t - pd.Timedelta(days=62):t + pd.Timedelta(days=62)].max())
        ax.annotate(lab, (t, y), xytext=(0, 8), textcoords="offset points", ha="center",
                    fontsize=8, color="#222222")
    ax.set_ylabel("Index, 1985–2019 = 100 (3-month average)")
    ax.set_title("9/11 registered as an act; the war in Ukraine began as a threat")
    ax.set_ylim(0, 820)
    # numbers for the text
    t, a = d["GPRT"], d["GPRA"]
    print("ch07 GPRT/GPRA correlation, monthly 1985-:", round(t.corr(a), 2))
    for date in ["2001-09-01", "2003-03-01", "2022-02-01", "2022-03-01"]:
        print("ch07 GPR", date, "GPR", round(d.loc[date, "GPR"]), "threats", round(t[date]),
              "acts", round(a[date]))
    print("ch07 Iraq run-up threats/acts:", d.loc["2002-12-01":"2003-03-01", ["GPRT", "GPRA"]].round().values.tolist())
    pre = d.loc["2021-10-01":"2022-01-01"]
    print("ch07 Oct2021-Jan2022 mean threats/acts:", round(pre["GPRT"].mean()), round(pre["GPRA"].mean()))
    print("ch07 GPR latest", d.index[-1].date(), round(d["GPR"].iloc[-1]),
          "max since 1985", d["GPR"].idxmax().date(), round(d["GPR"].max()))
    return save(fig, "ch07-gpr-threats-acts",
                "Caldara and Iacoviello, Geopolitical Risk index (data_gpr_export.xls), monthly GPRT and GPRA")


def fig_gpr_epu(g, epu):
    d = g.set_index("month")[["GPR"]].join(epu, how="inner")
    z = d[["GPR", "GEPU_current"]].apply(lambda s: s / s.loc["1997":"2019"].mean() * 100)
    sm = z.rolling(3, center=True).mean()
    fig, ax = figure(7.4, 4.0)
    ax.plot(sm.index, sm["GPR"], color=RED, lw=1.4)
    ax.plot(sm.index, sm["GEPU_current"], color=BLUE, lw=1.4)
    ax.text(pd.Timestamp("2004-06-01"), 255, "Geopolitical risk (GPR)", color=RED, fontsize=9,
            fontweight="bold")
    ax.text(pd.Timestamp("2010-01-01"), 40, "Global economic policy uncertainty (EPU)", color=BLUE,
            fontsize=9, fontweight="bold")
    for date, lab, col in [("2001-09-01", "9/11", RED), ("2003-03-01", "Iraq", RED),
                           ("2016-11-01", "Brexit, US election", BLUE), ("2020-04-01", "Covid-19", BLUE),
                           ("2022-03-01", "Ukraine", RED), ("2025-04-01", "US tariffs", BLUE)]:
        t = pd.Timestamp(date)
        y = sm.loc[t - pd.Timedelta(days=62):t + pd.Timedelta(days=62)].max().max()
        right = lab.startswith("Brexit")
        ax.annotate(lab, (t, y), xytext=(-8 if right else 0, 6), textcoords="offset points",
                    ha="right" if right else "center", fontsize=8, color=col)
    ax.set_ylabel("Index, 1997–2019 mean = 100 (3-month average)")
    ax.set_title("Two newspaper indices, two different crises")
    ax.set_ylim(0, None)
    r_lvl = d["GPR"].corr(d["GEPU_current"])
    r_chg = d["GPR"].diff().corr(d["GEPU_current"].diff())
    print("ch07 GPR-EPU correlation, levels:", round(r_lvl, 2), "monthly changes:", round(r_chg, 2),
          "months:", len(d), d.index[0].date(), "to", d.index[-1].date())
    print("ch07 GPR-EPU corr GEPU_current vs GEPU_ppp:", round(d["GEPU_current"].corr(d["GEPU_ppp"]), 3))
    for col in ["GPR", "GEPU_current"]:
        top = z[col].sort_values(ascending=False)
        top5 = []
        for t, v in top.items():
            if all(abs((t - s).days) > 180 for s, _ in top5):
                top5.append((t, v))
            if len(top5) == 5:
                break
        print("ch07 top episodes", col, [(t.strftime("%Y-%m"), round(v)) for t, v in top5])
    return save(fig, "ch07-gpr-epu",
                "Caldara and Iacoviello (GPR); Baker, Bloom and Davis, Global EPU (current-price GDP weights); "
                "both rescaled to their 1997–2019 means")


def load_flr():
    cols = ["gvkey", "date", "PRisk", "hqcountrycode"]
    f = pd.read_csv(fetch(FLR_URL, "hassan_firmquarter_2022q1.csv"), sep="\t", usecols=cols,
                    dtype={"gvkey": str})
    f = f.dropna(subset=["PRisk"])
    f["q"] = pd.PeriodIndex(f["date"].str.upper(), freq="Q")
    return f


def fig_prisk(f, epu_q):
    us = f[f["hqcountrycode"] == "US"]
    s = us["PRisk"] / us["PRisk"].std()
    us = us.assign(z=s)
    agg = us.groupby("q")["z"].agg(mean="mean", p90=lambda x: x.quantile(0.9),
                                   p10=lambda x: x.quantile(0.1), sd="std", n="size")
    agg["iqr90"] = agg["p90"] - agg["p10"]
    j = agg.join(epu_q.rename("epu"), how="inner")
    print("ch07 PRisk US firm-quarters:", len(us), "firms:", us["gvkey"].nunique(),
          "quarters:", agg.index.min(), "-", agg.index.max(),
          "median firms per quarter:", int(agg["n"].median()))
    print("ch07 corr(mean PRisk, US EPU quarterly):", round(j["mean"].corr(j["epu"]), 2))
    print("ch07 corr(mean PRisk, cross-firm sd):", round(agg["mean"].corr(agg["sd"]), 2),
          "corr(mean, p90-p10):", round(agg["mean"].corr(agg["iqr90"]), 2))
    print("ch07 2011Q3: mean PRisk", round(agg.loc[pd.Period("2011Q3"), "mean"], 2), "US EPU",
          round(j.loc[pd.Period("2011Q3"), "epu"]), "; 2011Q2:", round(agg.loc[pd.Period("2011Q2"), "mean"], 2),
          round(j.loc[pd.Period("2011Q2"), "epu"]))
    top = agg["mean"].sort_values(ascending=False).head(5)
    print("ch07 top PRisk quarters:", [(str(k), round(v, 2)) for k, v in top.items()])
    fig, ax = figure(7.4, 4.0)
    x = agg.index.to_timestamp()
    ax.fill_between(x, agg["p10"], agg["p90"], color="#C9DCE8", lw=0)
    ax.plot(x, agg["mean"], color=BLUE, lw=1.8)
    ax2 = ax.twinx()
    ax2.plot(j.index.to_timestamp(), j["epu"], color=RED, lw=1.2, alpha=0.9)
    ax2.set_ylim(0, j["epu"].max() * 1.25)
    ax2.spines["right"].set_visible(False)
    ax2.grid(False)
    ax2.tick_params(axis="y", colors=RED)
    ax2.set_ylabel("US EPU index (quarterly mean)", color=RED)
    ax.set_ylim(0, agg["p90"].max() * 1.1)
    ax.set_ylabel("PRisk, in standard deviations", color=BLUE)
    ax.text(x[3], agg["p90"].iloc[3] + 0.15, "10th–90th percentile of firms", color=BLUE, fontsize=8)
    ax.text(x[18], agg["mean"].iloc[18] - 0.35, "Average firm", color=BLUE, fontsize=9, fontweight="bold")
    ax2.annotate("US EPU", (pd.Timestamp("2011-09-01"), 236), xytext=(5, -3), textcoords="offset points",
                 color=RED, fontsize=9, fontweight="bold", ha="left")
    ax.set_title("When political risk rises on average, firms spread further apart")
    return save(fig, "ch07-prisk-dispersion",
                "Hassan, Hollander, van Lent and Tahoun, firm-level political risk (2022q1 vintage), "
                "US-headquartered firms; Baker, Bloom and Davis, US EPU")


def r2_groups(y, groups):
    """Share of variance of y explained by group fixed effects (one or two-way, by alternating projections)."""
    y = y - y.mean()
    tot = (y ** 2).sum()
    resid = y.copy()
    for _ in range(50 if len(groups) > 1 else 1):
        for g in groups:
            resid = resid - resid.groupby(g).transform("mean")
    return 1 - (resid ** 2).sum() / tot


def fig_variance(f):
    us = f[f["hqcountrycode"] == "US"].copy()
    y = us["PRisk"] / us["PRisk"].std()
    y.index = range(len(y))
    q = us["q"].astype(str).values
    firm = us["gvkey"].values
    qs, fs = pd.Series(q, index=y.index), pd.Series(firm, index=y.index)
    r_time = r2_groups(y, [qs])
    r_firm = r2_groups(y, [fs])
    r_both = r2_groups(y, [qs, fs])
    print("ch07 variance of PRisk (US): time FE", round(r_time, 3), "firm FE", round(r_firm, 3),
          "time+firm FE", round(r_both, 3), "residual", round(1 - r_both, 3))
    parts = [("Common to all firms\nin a quarter", r_time, MUTED),
             ("Permanent differences\nbetween firms", r_both - r_time, BLUE),
             ("Firm-specific, changing\nfrom quarter to quarter", 1 - r_both, RED)]
    fig, ax = figure(7.2, 3.0)
    ax.grid(False)
    left = 0
    for lab, v, c in parts:
        ax.barh([0], [v], left=left, color=c, height=0.5)
        ax.text(left + v / 2, 0, f"{v:.0%}", ha="center", va="center", color="white",
                fontsize=11, fontweight="bold") if v > 0.05 else None
        if v > 0.05:
            ax.text(left + v / 2, 0.30, lab, ha="center", va="bottom", fontsize=8.5, color=c)
        else:
            ax.annotate(f"{lab.replace(chr(10), ' ')}: {v:.0%}", (left + v / 2, -0.25), xytext=(4, -22),
                        textcoords="offset points", fontsize=8.5, color="#222222",
                        arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
        left += v
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.75, 0.75)
    ax.set_yticks([])
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"])
    ax.set_xlabel("Share of the variance of PRisk across US firm-quarters")
    ax.set_title("Most political risk is specific to the firm and the quarter")
    return save(fig, "ch07-prisk-variance",
                "Hassan, Hollander, van Lent and Tahoun, firm-level political risk (2022q1 vintage); "
                "author's decomposition with quarter and firm fixed effects")


def fig_composite(g):
    gc = g.set_index("month")
    year = 2025
    gcols = [c for c in gc.columns if c.startswith("GPRC_")]
    gpr = gc.loc[str(year), gcols].mean()
    gpr.index = [c[5:] for c in gpr.index]
    w = pd.read_excel(fetch(WGI_URL, "wgi_2025.xlsx"), sheet_name="pv")
    w = w[w["Year"] == 2024].set_index("Economy (code)")["Governance score (0-100)"].astype(float)
    names = pd.read_excel(fetch(WGI_URL, "wgi_2025.xlsx"), sheet_name="pv")
    names = names.drop_duplicates("Economy (code)").set_index("Economy (code)")["Economy (name)"]
    d = pd.DataFrame({"gpr": gpr, "pv": w.reindex(gpr.index)})
    print("ch07 composite: countries with GPRC:", len(d), "missing WGI:", d["pv"].isna().sum())
    print("ch07 country GPR", year, "max", d["gpr"].idxmax(), round(d["gpr"].max(), 2), "median",
          round(d["gpr"].median(), 2), "; countries below 25% of the range:",
          int(((d["gpr"] - d["gpr"].min()) / (d["gpr"].max() - d["gpr"].min()) < 0.25).sum()))
    d = d.dropna()
    x1 = (d["gpr"] - d["gpr"].min()) / (d["gpr"].max() - d["gpr"].min())
    x2 = (d["pv"].max() - d["pv"]) / (d["pv"].max() - d["pv"].min())  # inverted: higher = riskier
    ranks = {}
    for wg in [0, 0.25, 0.5, 0.75, 1.0]:
        ci = wg * x1 + (1 - wg) * x2
        ranks[wg] = ci.rank(ascending=False, method="min").astype(int)
    R = pd.DataFrame(ranks)
    R["spread"] = R[[0.25, 0.5, 0.75]].max(axis=1) - R[[0.25, 0.5, 0.75]].min(axis=1)
    R["spread_all"] = R.max(axis=1) - R[[0, 0.25, 0.5, 0.75, 1.0]].min(axis=1)
    R["name"] = [names.get(c, c) for c in R.index]
    R["gpr"], R["pv"] = d["gpr"].round(2), d["pv"].round(1)
    R = R.sort_values(0.5)
    print("ch07 composite ranks (w_GPR = 0, .25, .5, .75, 1):")
    print(R.to_string())
    print("ch07 countries moving >5 places between w=.25 and w=.75:", int((R["spread"] > 5).sum()),
          "of", len(R), "; >10 places:", int((R["spread"] > 10).sum()))
    print("ch07 rank correlation GPR alone vs WGI alone:", round(R[1.0].corr(R[0.0]), 2))
    # chart: for each country, rank at w=.5 with range across .25-.75
    fig, ax = figure(7.4, 6.6)
    ax.grid(axis="x", color=GRID)
    ax.grid(axis="y", visible=False)
    yy = np.arange(len(R))[::-1]
    for y, (_, r) in zip(yy, R.iterrows()):
        lo, hi = min(r[0.25], r[0.75]), max(r[0.25], r[0.75])
        ax.plot([lo, hi], [y, y], color=GRID if r["spread"] <= 5 else PALE_RED, lw=3, solid_capstyle="round")
        ax.plot(r[0.25], y, "o", color=BLUE, ms=4)
        ax.plot(r[0.75], y, "o", color=RED, ms=4)
        ax.plot(r[0.5], y, "|", color="#222222", ms=7)
    ax.set_yticks(yy)
    ax.set_yticklabels(R["name"], fontsize=7.5)
    ax.set_xlim(0.5, len(R) + 0.5)
    ax.invert_xaxis()
    ax.set_xlabel("Rank in the composite (1 = riskiest)")
    ax.text(len(R) - 1, len(R) + 0.3, "● 25% weight on GPR", color=BLUE, fontsize=8.5, ha="left")
    ax.text(len(R) - 16, len(R) + 0.3, "● 75% weight on GPR", color=RED, fontsize=8.5, ha="left")
    ax.text(len(R) - 31, len(R) + 0.3, "| equal weights", color="#222222", fontsize=8.5, ha="left")
    ax.set_ylim(-1, len(R) + 1.2)
    ax.set_title("One weight reorders the middle of a two-indicator risk ranking")
    out = save(fig, "ch07-composite-ranks",
               f"Caldara and Iacoviello, country GPR (mean of {year}); World Bank, WGI 2025 edition, "
               "political stability score 2024, inverted; min–max normalised, weighted arithmetic mean")
    return out, R




def main():
    g = load_gpr()
    epu = load_epu_global()
    f = load_flr()
    epu_q = load_epu_us_quarterly()
    out = [fig_threats_acts(g), fig_gpr_epu(g, epu), fig_prisk(f, epu_q), fig_variance(f)]
    p, _ = fig_composite(g)
    out.append(p)
    return out


if __name__ == "__main__":
    main()
