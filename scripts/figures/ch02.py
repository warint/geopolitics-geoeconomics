"""Chapter 2 — The international economic order: figures from the World Development Indicators.

Every series is downloaded at source from the World Bank's bulk-download API
(https://api.worldbank.org/v2/en/indicator/<code>?downloadformat=csv) into .data-cache/ and read
from the zip. The G7 and the "Industrialising Six" are not World Bank aggregates; they are built
here by summing members. The world total is the World Bank's own aggregate (WLD).

    .venv/bin/python scripts/figures/build_all.py 02
"""

import zipfile

import pandas as pd

from style import BLUE, GOLD, GRID, INK, MUTED, PALE_BLUE, RED, TEAL, fetch, figure, save
import matplotlib.pyplot as plt

API = "https://api.worldbank.org/v2/en/indicator/{}?downloadformat=csv"
WDI = "World Bank, World Development Indicators ({})"

G7 = ["CAN", "FRA", "DEU", "ITA", "JPN", "GBR", "USA"]
I6 = ["CHN", "KOR", "IND", "POL", "IDN", "THA"]
NAMES = {"CAN": "Canada", "FRA": "France", "DEU": "Germany", "ITA": "Italy", "JPN": "Japan",
         "GBR": "United Kingdom", "USA": "United States"}


def wdi(code):
    """(values by economy x year, list of economy codes that are countries, not aggregates)."""
    path = fetch(API.format(code), f"wdi_{code}.zip")
    z = zipfile.ZipFile(path)
    data = [n for n in z.namelist() if n.startswith("API_")][0]
    meta = [n for n in z.namelist() if n.startswith("Metadata_Country")][0]
    d = pd.read_csv(z.open(data), skiprows=4).set_index("Country Code")
    years = [c for c in d.columns if c.isdigit()]
    d = d[years].astype(float)
    d.columns = d.columns.astype(int)
    m = pd.read_csv(z.open(meta))
    countries = list(m.loc[m["Region"].notna(), "Country Code"])
    return d, countries


def shares(d):
    w = d.loc["WLD"]
    return pd.DataFrame({
        "G7": d.loc[G7].sum(min_count=7) / w * 100,
        "I6": d.loc[I6].sum(min_count=1) / w * 100,
        "CHN": d.loc["CHN"] / w * 100,
        "USA": d.loc["USA"] / w * 100,
        "CHN/USA": d.loc["CHN"] / d.loc["USA"] * 100,
    }).dropna(subset=["G7"])


def label_end(ax, x, y, text, color, dy=0, **kw):
    ax.annotate(text, (x, y), xytext=(6, dy), textcoords="offset points", color=color,
                va="center", fontsize=9, fontweight="bold", **kw)


def fig_g7_share(mkt):
    s = mkt.loc[1970:]
    peak = s["G7"].idxmax()
    last = s.index.max()
    print(f"[g7-share] G7 1970 {s.loc[1970, 'G7']:.1f}  peak {peak} {s.loc[peak, 'G7']:.1f}  "
          f"1990 {s.loc[1990, 'G7']:.1f}  2005 {s.loc[2005, 'G7']:.1f}  2010 {s.loc[2010, 'G7']:.1f}  "
          f"{last} {s.loc[last, 'G7']:.1f}")
    print(f"[g7-share] I6 1970 {s.loc[1970, 'I6']:.1f}  1990 {s.loc[1990, 'I6']:.1f}  "
          f"2010 {s.loc[2010, 'I6']:.1f}  max {s['I6'].idxmax()} {s['I6'].max():.1f}  "
          f"{last} {s.loc[last, 'I6']:.1f}")
    print(f"[g7-share] China 1990 {s.loc[1990, 'CHN']:.1f}  {last} {s.loc[last, 'CHN']:.1f}; "
          f"China's share of the I6 in {last}: {s.loc[last, 'CHN'] / s.loc[last, 'I6'] * 100:.0f}%")
    fig, ax = figure(7.2, 4.0)
    ax.plot(s.index, s["G7"], color=RED, lw=2.2)
    ax.plot(s.index, s["I6"], color=BLUE, lw=2.2)
    ax.plot(s.index, s["CHN"], color=BLUE, lw=1.2, ls="--")
    label_end(ax, last, s.loc[last, "G7"], "G7", RED)
    label_end(ax, last, s.loc[last, "I6"], "Industrialising Six", BLUE, dy=4)
    label_end(ax, last, s.loc[last, "CHN"], "of which China", BLUE, dy=-4)
    ax.axvline(1990, color=MUTED, lw=0.8, ls=":")
    ax.annotate(f"Peak {peak}: {s.loc[peak, 'G7']:.1f}%", (peak, s.loc[peak, "G7"]),
                xytext=(peak + 3, 72), color=INK, fontsize=8.5,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    ax.text(1990.5, 33, "ICT revolution:\nthe second unbundling", color=MUTED, fontsize=8)
    ax.annotate("China joins\nthe WTO, 2001", (2001, s.loc[2001, "CHN"]), xytext=(1994, 16),
                color=MUTED, fontsize=8, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    ax.set_xlim(1970, last + 14)
    ax.set_xticks(range(1970, 2021, 10))
    ax.spines["bottom"].set_bounds(1970, last)
    ax.set_ylim(0, 75)
    ax.set_ylabel("Share of world GDP, current US$ (%)")
    ax.set_title("The economies that wrote the rules went from two-thirds of world output to under half")
    return save(fig, "ch02-g7-share", WDI.format("NY.GDP.MKTP.CD, GDP in current US$") +
                "; G7 and Industrialising Six (China, Korea, India, Poland, Indonesia, Thailand) "
                "summed by the author; Poland from 1990.")


def fig_ppp(mkt, ppp):
    last = ppp.index.max()
    cross = int(ppp.index[ppp["CHN/USA"] >= 100].min())
    print(f"[ppp] G7 at PPP 1990 {ppp.loc[1990, 'G7']:.1f}  {last} {ppp.loc[last, 'G7']:.1f}; "
          f"at market 1990 {mkt.loc[1990, 'G7']:.1f}  {last} {mkt.loc[last, 'G7']:.1f}")
    print(f"[ppp] I6 at PPP 1990 {ppp.loc[1990, 'I6']:.1f}  {last} {ppp.loc[last, 'I6']:.1f}; "
          f"I6 passes G7 at PPP in {int(ppp.index[ppp['I6'] >= ppp['G7']].min())}")
    print(f"[ppp] China/US at PPP: passes 100 in {cross}; {last} {ppp.loc[last, 'CHN/USA']:.0f}; "
          f"at market 1990 {mkt.loc[1990, 'CHN/USA']:.0f}  2010 {mkt.loc[2010, 'CHN/USA']:.0f}  "
          f"max {mkt['CHN/USA'].idxmax()} {mkt['CHN/USA'].max():.0f}  {last} {mkt.loc[last, 'CHN/USA']:.0f}")
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.8))
    fig.add_artist(plt.Line2D([0.0, 0.07], [1.02, 1.02], transform=fig.transFigure, color=RED,
                              linewidth=4, solid_capstyle="butt"))
    m = mkt.loc[1990:]
    for ax, col, ttl, unit in [(a1, "G7", "G7 share of world GDP", "%"),
                               (a2, "CHN/USA", "China's GDP as % of the United States'", "%")]:
        ax.plot(m.index, m[col], color=RED, lw=2)
        ax.plot(ppp.index, ppp[col], color=BLUE, lw=2)
        ax.set_title(ttl, fontsize=10, fontweight="bold")
        ax.set_xlim(1990, last + 1)
    a1.set_ylim(0, 75)
    a1.fill_between(ppp.index, ppp["G7"], m["G7"].reindex(ppp.index), color=PALE_BLUE, alpha=0.6, lw=0)
    a1.text(1991, m.loc[1991, "G7"] + 3, "market exchange rates", color=RED, fontsize=8.5)
    a1.text(1991, 22, "purchasing-power parity", color=BLUE, fontsize=8.5)
    a2.set_ylim(0, 145)
    a2.axhline(100, color=INK, lw=0.8)
    a2.text(1991, 103, "parity with the US", fontsize=8, color=INK)
    a2.annotate(f"passes the US\nat PPP, {cross}", (cross, 100), xytext=(cross - 13, 118),
                fontsize=8, color=BLUE, arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.8))
    peak = m["CHN/USA"].idxmax()
    a2.annotate(f"{peak}: {m.loc[peak, 'CHN/USA']:.0f}%", (peak, m.loc[peak, "CHN/USA"]),
                xytext=(peak - 4, 30), fontsize=8, color=RED,
                arrowprops=dict(arrowstyle="-", color=RED, lw=0.8))
    fig.suptitle("Measured at purchasing-power parity, the convergence is larger and earlier",
                 x=0.0, ha="left", y=1.0, fontsize=12, fontweight="bold")
    fig.tight_layout()
    return save(fig, "ch02-ppp-vs-market",
                WDI.format("NY.GDP.MKTP.CD and NY.GDP.MKTP.PP.CD") + "; PPP series begins in 1990.")


def fig_members(gdp):
    w = gdp.loc["WLD"]
    sh = (gdp.loc[G7].div(w) * 100).T.loc[1970:]
    last = sh.index.max()
    for c in G7:
        print(f"[members] {c}: 1970 {sh.loc[1970, c]:.1f}  1990 {sh.loc[1990, c]:.1f}  "
              f"max {sh[c].idxmax()} {sh[c].max():.1f}  {last} {sh.loc[last, c]:.1f}")
    eu4 = sh[["FRA", "DEU", "ITA", "GBR"]].sum(axis=1)
    print(f"[members] Europe-4: 1990 {eu4.loc[1990]:.1f}  {last} {eu4.loc[last]:.1f}; "
          f"G7 ex-US 1990 {sh.loc[1990].sum() - sh.loc[1990, 'USA']:.1f}  "
          f"{last} {sh.loc[last].sum() - sh.loc[last, 'USA']:.1f}")
    fig, axes = plt.subplots(2, 4, figsize=(7.6, 4.0), sharex=True)
    fig.add_artist(plt.Line2D([0.0, 0.07], [1.02, 1.02], transform=fig.transFigure, color=RED,
                              linewidth=4, solid_capstyle="butt"))
    order = ["USA", "JPN", "DEU", "FRA", "GBR", "ITA", "CAN"]
    for ax, c in zip(axes.flat, order):
        ax.plot(sh.index, sh[c], color=RED if c in ("USA",) else BLUE, lw=1.8)
        ax.set_title(NAMES[c], fontsize=9, fontweight="bold")
        top = 40 if c == "USA" else 20
        ax.set_ylim(0, top)
        ax.set_yticks([0, top / 2, top])
        ax.tick_params(labelsize=7.5)
        ax.text(last, sh.loc[last, c] + top * (0.12 if c == "JPN" else 0.06), f"{sh.loc[last, c]:.1f}", fontsize=7.5,
                ha="right", color=INK)
    ax = axes.flat[-1]
    ax.plot(eu4.index, eu4, color=TEAL, lw=1.8)
    ax.set_ylim(0, 40)
    ax.set_yticks([0, 20, 40])
    ax.tick_params(labelsize=7.5)
    ax.set_title("FR+DE+GB+IT", fontsize=9, fontweight="bold")
    ax.text(last, eu4.loc[last] + 2.4, f"{eu4.loc[last]:.1f}", fontsize=7.5, ha="right")
    for a in axes.flat:
        a.set_xticks([1970, 2000, 2025])
        a.set_xticklabels(["1970", "2000", "'25"])
    fig.suptitle("The G7's decline is Japan's and Europe's; the US share is where it was in 1990",
                 x=0.0, ha="left", y=1.0, fontsize=11.5, fontweight="bold")
    fig.supylabel("Share of world GDP, current US$ (%)", fontsize=8.5)
    fig.tight_layout()
    return save(fig, "ch02-g7-members", WDI.format("NY.GDP.MKTP.CD") +
                "; note the different vertical scales for the United States and Europe-4.")


def fig_trade_fdi(trade, trade_c, fdi):
    t = trade.loc["WLD"].dropna()
    n = trade.loc[trade.index.isin(trade_c)].notna().sum()
    f = fdi.loc["WLD"].dropna().loc[1970:]
    last = int(t.index.max())
    print(f"[trade] world trade/GDP 1970 {t.loc[1970]:.1f} 1990 {t.loc[1990]:.1f} "
          f"2008 {t.loc[2008]:.1f} 2009 {t.loc[2009]:.1f} 2020 {t.loc[2020]:.1f} "
          f"2022 {t.loc[2022]:.1f} 2023 {t.loc[2023]:.1f} 2024 {t.loc[2024]:.1f} {last} {t.loc[last]:.1f}")
    print(f"[trade] reporting economies 2022 {n.loc[2022]}  2024 {n.loc[2024]}  {last} {n.loc[last]}")
    pk = f.loc[:2010].idxmax()
    print(f"[fdi] world FDI inflows/GDP 1990 {f.loc[1990]:.1f}  2000 {f.loc[2000]:.1f}  "
          f"peak {pk} {f.loc[pk]:.1f}  2015 {f.loc[2015]:.1f}  2023 {f.loc[2023]:.1f}  "
          f"{int(f.index.max())} {f.iloc[-1]:.1f}; mean 2000-07 {f.loc[2000:2007].mean():.1f}  "
          f"mean 2018-{int(f.index.max())} {f.loc[2018:].mean():.1f}")
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.8))
    fig.add_artist(plt.Line2D([0.0, 0.07], [1.02, 1.02], transform=fig.transFigure, color=RED,
                              linewidth=4, solid_capstyle="butt"))
    tt = t.loc[:last - 1]
    a1.plot(tt.index, tt, color=BLUE, lw=2)
    a1.plot([last - 1, last], [t.loc[last - 1], t.loc[last]], color=BLUE, lw=1.2, ls=":")
    a1.scatter([last], [t.loc[last]], s=22, facecolor="white", edgecolor=BLUE, zorder=3)
    a1.annotate(f"{last}: {n.loc[last]} of\n{n.loc[2022]} reporters", (last, t.loc[last]),
                xytext=(last - 17, 70), fontsize=7.5, color=MUTED,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    a1.annotate(f"2008: {t.loc[2008]:.0f}%", (2008, t.loc[2008]), xytext=(1990, 60),
                fontsize=8, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    a1.set_ylim(0, 75)
    a1.set_title("World trade, % of world GDP", fontsize=10, fontweight="bold")
    a2.fill_between(f.index, f, color=PALE_BLUE, lw=0)
    a2.plot(f.index, f, color=BLUE, lw=1.6)
    a2.annotate(f"{pk}: {f.loc[pk]:.1f}%", (pk, f.loc[pk]), xytext=(pk - 22, 5.0), fontsize=8,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    a2.set_ylim(0, 6)
    a2.set_title("FDI net inflows, % of world GDP", fontsize=10, fontweight="bold")
    for a in (a1, a2):
        a.set_xlim(1970, last + 1)
    fig.suptitle("Trade plateaued after 2008; foreign direct investment fell back to 1990s levels",
                 x=0.0, ha="left", y=1.0, fontsize=12, fontweight="bold")
    fig.tight_layout()
    return save(fig, "ch02-trade-fdi",
                WDI.format("NE.TRD.GNFS.ZS and BX.KLT.DINV.WD.GD.ZS, world aggregates") +
                f"; {last} trade value provisional.")


def table(mkt, ppp):
    last = mkt.index.max()
    rows = []
    for y in (1970, 1990, 2010, 2024):
        r = {"year": y}
        for k in ("G7", "I6", "USA", "CHN"):
            r[f"{k} mkt"] = round(mkt.loc[y, k], 1)
            r[f"{k} ppp"] = round(ppp.loc[y, k], 1) if y in ppp.index else None
        rows.append(r)
    print("[table]\n" + pd.DataFrame(rows).to_string(index=False))
    print(f"[table] last year in release: {last}")


def main():
    gdp, _ = wdi("NY.GDP.MKTP.CD")
    gdpp, _ = wdi("NY.GDP.MKTP.PP.CD")
    trade, trade_c = wdi("NE.TRD.GNFS.ZS")
    fdi, _ = wdi("BX.KLT.DINV.WD.GD.ZS")
    mkt, ppp = shares(gdp), shares(gdpp)
    table(mkt, ppp)
    return [fig_g7_share(mkt), fig_ppp(mkt, ppp), fig_members(gdp),
            fig_trade_fdi(trade, trade_c, fdi)]


if __name__ == "__main__":
    main()
