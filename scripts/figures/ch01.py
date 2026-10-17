"""Chapter 1 — What is geopolitical risk? Figures from the Geopolitical Risk index.

Data, downloaded at source into .data-cache/:
- Caldara and Iacoviello, Geopolitical Risk index, monthly export file
  https://www.matteoiacoviello.com/gpr_files/data_gpr_export.xls
- Baker, Bloom and Davis, Global Economic Policy Uncertainty index (Davis 2016)
  https://www.policyuncertainty.com/media/Global_Policy_Uncertainty_Data.xlsx

Both files are revised monthly, so the numbers printed below (and quoted in the chapter) are those
of the vintage in the cache; delete .data-cache/ to redraw from the current files.
"""

import numpy as np
import pandas as pd

from style import BLUE, GOLD, GRID, INK, MUTED, PALE_BLUE, RED, fetch, figure, plt, save

GPR_URL = "https://www.matteoiacoviello.com/gpr_files/data_gpr_export.xls"
EPU_URL = "https://www.policyuncertainty.com/media/Global_Policy_Uncertainty_Data.xlsx"
SRC_GPR = "Caldara and Iacoviello, Geopolitical Risk index (data_gpr_export.xls)"

CATEGORIES = ["War threats", "Peace threats", "Military build-ups", "Nuclear threats",
              "Terror threats", "Beginning of war", "Escalation of war", "Terror acts"]

COUNTRY = {
    "USA": "United States", "ISR": "Israel", "GBR": "United Kingdom", "RUS": "Russia",
    "UKR": "Ukraine", "CHN": "China", "FRA": "France", "DEU": "Germany", "SAU": "Saudi Arabia",
    "VEN": "Venezuela", "CAN": "Canada", "IND": "India", "TUR": "Turkey", "JPN": "Japan",
    "KOR": "South Korea", "EGY": "Egypt", "ITA": "Italy", "TWN": "Taiwan", "ESP": "Spain",
    "AUS": "Australia", "MEX": "Mexico", "POL": "Poland", "BRA": "Brazil", "VNM": "Vietnam",
    "ZAF": "South Africa", "IDN": "Indonesia", "MYS": "Malaysia", "TUN": "Tunisia",
}


def load_gpr():
    d = pd.read_excel(fetch(GPR_URL, "gpr_export.xls"))
    d = d.dropna(subset=["month"]).set_index("month")
    d.index = pd.to_datetime(d.index)
    return d


def load_epu():
    e = pd.read_excel(fetch(EPU_URL, "epu_global.xlsx"))
    e = e[pd.to_numeric(e["Year"], errors="coerce").notna() & e["Month"].notna()]
    e.index = pd.to_datetime(dict(year=e["Year"].astype(int), month=e["Month"].astype(int), day=1))
    return e["GEPU_current"].astype(float)


def fig_recent(d):
    r = d.loc["1985":, "GPR"]
    last = r.index[-1]
    fig, ax = figure(7.4, 3.9)
    ax.fill_between(r.index, 100, r.values, where=r.values > 100, color=PALE_BLUE, lw=0)
    ax.plot(r.index, r.values, color=BLUE, lw=1.1)
    ax.axhline(100, color=MUTED, lw=0.8, ls="--")
    ax.text(pd.Timestamp("2007-01"), 30, "dashed line: 1985–2019 average = 100", color=MUTED,
            fontsize=8)
    events = [("1991-01", "Gulf War"), ("2001-10", "11 September and\nAfghanistan"),
              ("2003-03", "Iraq"), ("2022-03", "Russia invades\nUkraine"),
              ("2026-03", "War with Iran")]
    for m, label in events:
        t = pd.Timestamp(m)
        v = r.loc[t]
        dx, ha = {"2022-03": (-6, "right"), "2026-03": (4, "center")}.get(m, (0, "center"))
        ax.annotate(label, (t, v), xytext=(dx, 8), textcoords="offset points", ha=ha,
                    fontsize=8, color=INK)
        ax.plot([t], [v], "o", ms=3, color=RED)
    ax.set_ylim(0, 600)
    ax.set_ylabel("Index, 1985–2019 = 100")
    ax.set_title("Geopolitical risk is measured in spikes: five episodes tower over forty years")
    ax.set_xlim(r.index[0], last + pd.DateOffset(months=6))
    print(f"[recent] last month {last:%Y-%m}: {r.iloc[-1]:.0f}; share of months above 200: "
          f"{(r > 200).mean():.1%}; months above 300: {(r > 300).sum()}")
    ann = r.resample("YE").mean()
    print("[recent] annual means:", {y.year: round(v) for y, v in ann.items()})
    print(f"[recent] 2001 annual mean {ann.loc['2001'].iloc[0]:.0f}; "
          f"median month 1985-2026 {r.median():.0f}")
    return save(fig, "ch01-gpr-recent", SRC_GPR + "; recent index, ten newspapers, monthly.")


def fig_threats_acts(d):
    windows = [("2001-06", "2002-03", "2001: the act came first"),
               ("2021-10", "2022-07", "2022: the threat came first"),
               ("2025-11", "2026-08", "2026: both at once")]
    fig, axes = plt.subplots(1, 3, figsize=(8.2, 3.3), sharey=True)
    fig.add_artist(plt.Line2D([0.0, 0.07], [1.08, 1.08], transform=fig.transFigure,
                              color=RED, linewidth=4, solid_capstyle="butt"))
    for ax, (a, b, title) in zip(axes, windows):
        w = d.loc[a:b, ["GPRT", "GPRA"]]
        x = np.arange(len(w))
        ax.plot(x, w["GPRT"], color=BLUE, lw=2)
        ax.plot(x, w["GPRA"], color=RED, lw=2)
        ax.axhline(100, color=MUTED, lw=0.7, ls="--")
        ax.set_xticks(x[::3])
        ax.set_xticklabels([f"{t:%b}\n{t:%Y}" for t in w.index[::3]], fontsize=8)
        ax.set_title(title, fontsize=10)
        for col, name, c in [("GPRT", "Threats", BLUE), ("GPRA", "Acts", RED)]:
            i = int(np.argmax(w[col].values))
            ax.text(i + 0.4, w[col].iloc[i] + 15, name, color=c, fontsize=8.5, va="bottom",
                    fontweight="bold")
        ax.set_xlim(-0.5, len(w) - 0.5)
        print(f"[threats-acts] {title}: max threats {w['GPRT'].max():.0f} "
              f"({w['GPRT'].idxmax():%Y-%m}), max acts {w['GPRA'].max():.0f} ({w['GPRA'].idxmax():%Y-%m})")
    axes[0].set_ylabel("Index, 1985–2019 = 100")
    fig.suptitle("Threats and acts: three spikes, three different shocks", x=0.0, ha="left",
                 fontweight="bold", fontsize=12, y=1.04)
    r = d.loc["1985":]
    print("[threats-acts] highest acts months:",
          {f"{t:%Y-%m}": round(v) for t, v in r["GPRA"].nlargest(7).items()})
    print(f"[threats-acts] correlation threats/acts 1985-: {r['GPRT'].corr(r['GPRA']):.2f}")
    return save(fig, "ch01-threats-acts", SRC_GPR + "; GPR Threats and GPR Acts sub-indices.")


def fig_historical(d):
    h = d["GPRH"]
    smooth = h.rolling(12, center=True).mean()
    fig, ax = figure(7.4, 3.9)
    ax.plot(h.index, h.values, color=PALE_BLUE, lw=0.7)
    ax.plot(smooth.index, smooth.values, color=BLUE, lw=1.8)
    ax.axhline(100, color=MUTED, lw=0.8, ls="--")
    events = [("1914-08", "1914"), ("1939-09", "1939"), ("1944-06", "  D-Day"),
              ("1950-07", "Korea"), ("1962-10", "Cuba"), ("1991-01", "Gulf War"),
              ("2001-10", "2001"), ("2022-03", "Ukraine"), ("2026-03", "Iran")]
    for m, label in events:
        t = pd.Timestamp(m)
        dx, ha = (3, "left") if m == "1944-06" else ((-2, "right") if m == "1939-09" else (0, "center"))
        ax.annotate(label.strip(), (t, h.loc[t]), xytext=(dx, 5), textcoords="offset points",
                    ha=ha, fontsize=7.5, color=INK)
    ax.text(pd.Timestamp("1975-01"), 360, "monthly", color=MUTED, fontsize=8)
    ax.text(pd.Timestamp("1975-01"), 335, "12-month average", color=BLUE, fontsize=8)
    ax.set_ylim(0, 540)
    ax.set_ylabel("Index, 1900–2019 = 100")
    ax.set_title("A century of attention: the world wars still dwarf everything since")
    for m in ["1914-08", "1939-09", "1944-06", "1962-10", "2001-10", "2022-03", "2026-03"]:
        print(f"[historical] {m}: {h.loc[m].iloc[0]:.0f}")
    print(f"[historical] 1962 annual mean {h.loc['1962'].mean():.0f}; "
          f"1940s mean {h.loc['1940':'1949'].mean():.0f}; 2000s mean {h.loc['2000':'2009'].mean():.0f}; "
          f"2020-latest mean {h.loc['2020':].mean():.0f}")
    return save(fig, "ch01-gpr-historical", SRC_GPR + "; historical index, three US newspapers.")


def fig_countries(d):
    cols = [c for c in d.columns if c.startswith("GPRC_")]
    end = d["GPR"].last_valid_index()
    window = d.loc[end - pd.DateOffset(months=11):end, cols].mean()
    base = d.loc["1985":"2019", cols].mean()
    s = window.sort_values(ascending=True).tail(20)
    fig, ax = figure(7.2, 4.8)
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", color=GRID)
    names = [COUNTRY.get(c[5:], c[5:]) for c in s.index]
    ax.barh(names, s.values, color=BLUE, height=0.7)
    ax.plot(base[s.index].values, names, "|", color=INK, ms=9, mew=1.6)
    ax.text(2.4, 2, "bars: last twelve months\n| : 1985–2019 average", fontsize=8.5, color=INK)
    ax.set_xlabel("Share of all articles that discuss geopolitical risk and mention the country, %")
    start = end - pd.DateOffset(months=11)
    ax.set_title(f"Country series: the press's own country and its wars lead the ranking")
    ax.tick_params(axis="y", labelsize=8.5)
    print(f"[countries] window {start:%Y-%m} to {end:%Y-%m}; top 10:",
          {COUNTRY.get(c[5:], c[5:]): round(v, 2) for c, v in window.sort_values(ascending=False).head(10).items()})
    print("[countries] Denmark rank:", list(window.sort_values(ascending=False).index).index("GPRC_DNK") + 1)
    print(f"[countries] bottom 5:", {c[5:]: round(v, 2) for c, v in window.sort_values().head(5).items()})
    print(f"[countries] ratio window/base, top:",
          {c[5:]: round(v, 1) for c, v in (window / base).sort_values(ascending=False).head(6).items()})
    m = d.loc["2026-03", cols].iloc[0].sort_values(ascending=False).head(5)
    print("[countries] March 2026 top 5:", {c[5:]: round(v, 2) for c, v in m.items()})
    m = d.loc["2022-03", cols].iloc[0].sort_values(ascending=False).head(4)
    print("[countries] March 2022 top 4:", {c[5:]: round(v, 2) for c, v in m.items()})
    return save(fig, "ch01-gpr-countries",
                SRC_GPR + f"; country series GPRC_, mean of {start:%B %Y}–{end:%B %Y}; 20 of 44 countries.")


def fig_epu(d):
    e = load_epu()
    j = pd.concat([d["GPR"], e.rename("EPU")], axis=1).dropna()
    fig, ax = figure(7.4, 3.9)
    ax.plot(j.index, j["EPU"], color=GOLD, lw=1.3)
    ax.plot(j.index, j["GPR"], color=BLUE, lw=1.3)
    ax.axhline(100, color=MUTED, lw=0.8, ls="--")
    ax.text(pd.Timestamp("2008-06"), 330, "Global economic policy\nuncertainty (EPU)", color=GOLD,
            fontsize=8.5)
    ax.text(pd.Timestamp("2004-03"), 250, "Geopolitical risk (GPR)", color=BLUE, fontsize=8.5)
    for m, label, col in [("2001-10", "2001", BLUE), ("2020-05", "Pandemic", GOLD),
                          ("2025-04", "Tariffs", GOLD), ("2022-03", "Ukraine", BLUE)]:
        t = pd.Timestamp(m)
        v = j.loc[t, "GPR" if col == BLUE else "EPU"]
        ax.annotate(label, (t, v), xytext=(0, 6), textcoords="offset points", ha="center",
                    fontsize=8, color=INK)
    ax.set_ylim(0, 680)
    ax.set_ylabel("Index (each = 100 in its own base period)")
    ax.set_title("Two text indices, two different worlds: policy uncertainty is not war risk")
    corr = j["GPR"].corr(j["EPU"])
    yr = j.resample("YE").mean()
    print(f"[epu] months {j.index[0]:%Y-%m}..{j.index[-1]:%Y-%m}, n={len(j)}, corr={corr:.2f}, "
          f"annual corr={yr['GPR'].corr(yr['EPU']):.2f}")
    for m in ["2001-10", "2020-05", "2022-03", "2025-04", "2026-03"]:
        print(f"[epu] {m}: GPR {j.loc[m, 'GPR'].iloc[0]:.0f}, EPU {j.loc[m, 'EPU'].iloc[0]:.0f}")
    print(f"[epu] EPU peak {j['EPU'].idxmax():%Y-%m} {j['EPU'].max():.0f}")
    return save(fig, "ch01-gpr-epu",
                SRC_GPR + "; Davis (2016), Global Economic Policy Uncertainty index (current-price GDP weights).")


def tables(d):
    r = d.loc["1985":]
    print("\n[table peaks] top 10 months, recent index")
    for t, row in r.nlargest(10, "GPR")[["GPR", "GPRT", "GPRA"]].iterrows():
        print(f"  {t:%B %Y}: GPR {row.GPR:.0f}, threats {row.GPRT:.0f}, acts {row.GPRA:.0f}")
    print("\n[table variants]")
    for c, label in [("GPR", "headline"), ("GPR_BASIC", "basic (narrow)"),
                     ("GPR_NOEW", "no excluded words"), ("GPR_AND", "broad (AND)")]:
        s = r[c]
        print(f"  {label}: corr {s.corr(r['GPR']):.2f}, peak {s.idxmax():%B %Y} {s.max():.0f}, "
              f"Mar 2022 {s.loc['2022-03'].iloc[0]:.0f}, Mar 2026 {s.loc['2026-03'].iloc[0]:.0f}")
    print("\n[table categories] historical share of articles, % of all articles, decade means")
    cats = [f"SHAREH_CAT_{i}" for i in range(1, 9)]
    h = d[cats + ["SHARE_GPRH"]].copy()
    h["decade"] = (h.index.year // 10) * 10
    t = h.groupby("decade").mean()
    t.columns = CATEGORIES + ["Any category"]
    with pd.option_context("display.width", 200):
        print(t.loc[[1910, 1940, 1960, 1980, 2000, 2020]].round(2).to_string())


def main():
    d = load_gpr()
    print(f"GPR file: {d['GPR'].last_valid_index():%Y-%m} latest month")
    made = [fig_recent(d), fig_threats_acts(d), fig_historical(d), fig_countries(d), fig_epu(d)]
    tables(d)
    return made


if __name__ == "__main__":
    main()
