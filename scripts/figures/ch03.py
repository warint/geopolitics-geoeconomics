"""Chapter 3 — Anarchy and the balance of power: figures and table numbers.

Data, downloaded at source into .data-cache/:
- Correlates of War, National Material Capabilities v7.0 (1816-2022):
  https://correlatesofwar.org/wp-content/uploads/NMCv7.zip  (abridged csv inside an inner zip)
- SIPRI Military Expenditure Database, 1949-2025, v1.2 (constant 2024 US$):
  https://www.sipri.org/sites/default/files/SIPRI-Milex-data-1949-2025_v1.2.xlsx
- World Bank WDI, GDP in current US$ (NY.GDP.MKTP.CD) and at PPP (NY.GDP.MKTP.PP.CD):
  https://api.worldbank.org/v2/en/indicator/<code>?downloadformat=csv

    .venv/bin/python scripts/figures/build_all.py 03
"""

import io
import zipfile

import numpy as np
import pandas as pd

from style import BLUE, GOLD, GRID, INK, MUTED, PALE_BLUE, PALE_RED, RED, TEAL, fetch, figure, save

NMC_URL = "https://correlatesofwar.org/wp-content/uploads/NMCv7.zip"
SIPRI_URL = "https://www.sipri.org/sites/default/files/SIPRI-Milex-data-1949-2025_v1.2.xlsx"
WDI_URL = "https://api.worldbank.org/v2/en/indicator/{}?downloadformat=csv"

COMPONENTS = {"tpop": "Total population", "upop": "Urban population",
              "irst": "Iron and steel production", "pec": "Primary energy consumption",
              "milper": "Military personnel", "milex": "Military expenditure"}


def nmc():
    z = zipfile.ZipFile(fetch(NMC_URL, "cow_NMCv7.zip"))
    inner = zipfile.ZipFile(io.BytesIO(z.read("NMCv7/NMC-v7-abridged.zip")))
    d = pd.read_csv(inner.open("NMC-70-abridged.csv"))
    return d.replace(-9, np.nan)


def sipri():
    path = fetch(SIPRI_URL, "sipri_milex_1949-2025_v1.2.xlsx")
    c = pd.read_excel(path, sheet_name="Constant (2024) US$", header=5)
    c = c.dropna(subset=["Country"]).set_index("Country")
    c = c[[y for y in c.columns if isinstance(y, int)]].apply(pd.to_numeric, errors="coerce")
    c.columns = c.columns.astype(int)
    r = pd.read_excel(path, sheet_name="Regional totals", header=13).set_index("Region")
    world = pd.to_numeric(r.loc["World", [y for y in r.columns if isinstance(y, (int, float))
                                          and not isinstance(y, bool)]], errors="coerce") * 1000
    world.index = world.index.astype(int)
    return c, world.dropna()


def wdi(code):
    z = zipfile.ZipFile(fetch(WDI_URL.format(code), f"wdi_{code}.zip"))
    name = [n for n in z.namelist() if n.startswith("API_")][0]
    d = pd.read_csv(z.open(name), skiprows=4).set_index("Country Code")
    years = [c for c in d.columns if c.isdigit()]
    out = d[years].T
    out.index = out.index.astype(int)
    return out


def first_year(series, level):
    hit = series[series >= level]
    return int(hit.index[0]) if len(hit) else None


def label_end(ax, x, y, text, color, dy=0.0):
    ax.text(x + 1, y + dy, text, color=color, fontsize=9, va="center", fontweight="bold")


def fig_cinc_shares(d):
    w = d.pivot(index="year", columns="stateabb", values="cinc")
    germany = w["GMY"].combine_first(w["GFR"])  # West Germany stands in for 1949-1990
    series = [("United States", w["USA"], BLUE), ("China", w["CHN"], RED),
              ("Britain", w["UKG"], GOLD), ("Russia / USSR", w["RUS"], TEAL),
              ("Germany", germany, MUTED), ("Japan", w["JPN"], "#8C5A9E")]
    fig, ax = figure(7.4, 4.3)
    for name, s, col in series:
        ax.plot(s.index, s * 100, color=col, lw=2.0 if name in ("United States", "China") else 1.3)
    ends = {"United States": w["USA"].iloc[-1] * 100, "China": w["CHN"].iloc[-1] * 100,
            "Russia / USSR": 5.6, "Japan": 3.8, "Germany": 2.0, "Britain": 0.4}
    for name, s, col in series:
        label_end(ax, 2022, ends[name], name, col)
    usa_peak = w["USA"].idxmax()
    ax.annotate(f"US peak, {usa_peak}:\n{w['USA'].max()*100:.0f}% of the system",
                xy=(usa_peak, w["USA"].max() * 100), xytext=(1953, 37.5), fontsize=8.5,
                color=INK, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    ax.annotate("China passes the\nUnited States, 1995", xy=(1995, w.loc[1995, "CHN"] * 100),
                xytext=(1958, 27), fontsize=8.5, color=INK,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    ax.annotate("Soviet lead, 1971-1988", xy=(1980, w.loc[1980, "RUS"] * 100), xytext=(1957, 7.6),
                fontsize=8.5, color=INK, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    ax.set_xlim(1816, 2040)
    ax.set_xticks(range(1825, 2030, 25))
    ax.set_ylim(-0.5, 42)
    ax.set_ylabel("Share of system capabilities (CINC, %)")
    ax.set_title("Britain, then America, then China: two centuries of capability shares")
    return save(fig, "ch03-cinc-shares",
                "Correlates of War, National Material Capabilities v7.0 (CINC); "
                "Germany 1949-1990 is the Federal Republic.")


def fig_four_measures(d, gdp, ppp, milex):
    w = d.pivot(index="year", columns="stateabb", values="cinc")
    ratios = {
        "Capability index (CINC)": ((w["CHN"] / w["USA"] * 100).loc[1950:], RED),
        "GDP at PPP": (((ppp["CHN"] / ppp["USA"]) * 100).dropna(), GOLD),
        "GDP at market exchange rates": (((gdp["CHN"] / gdp["USA"]) * 100).dropna(), BLUE),
        "Military expenditure (SIPRI)": (((milex.loc["China"] / milex.loc["United States of America"])
                                         * 100).dropna(), TEAL),
    }
    fig, ax = figure(7.4, 4.3)
    ax.axhline(100, color=INK, lw=0.9)
    ax.axhline(80, color=MUTED, lw=0.8, ls="--")
    ax.text(1951, 101.5, "parity", fontsize=8.5, color=INK)
    ax.text(1951, 78, "80%: 'approaching parity'", fontsize=8.5, va="top",
            color=MUTED)
    offsets = {"Capability index (CINC)": 0, "GDP at PPP": 0, "GDP at market exchange rates": -3,
               "Military expenditure (SIPRI)": 0}
    for name, (s, col) in ratios.items():
        ax.plot(s.index, s, color=col, lw=2)
        label_end(ax, s.index[-1], s.iloc[-1] + offsets[name], f"{name}\n{s.iloc[-1]:.0f}% "
                  f"({s.index[-1]})", col)
    ax.set_xlim(1950, 2048)
    ax.set_xticks(range(1950, 2030, 10))
    ax.set_ylim(0, 200)
    ax.set_ylabel("China as % of the United States")
    ax.set_title("One transition, four dates: China relative to the United States")
    path = save(fig, "ch03-four-measures",
                "Correlates of War NMC v7.0; World Bank WDI (NY.GDP.MKTP.PP.CD, NY.GDP.MKTP.CD); "
                "SIPRI Military Expenditure Database 2026 (constant 2024 US$).")
    return path, {k: v for k, (v, _) in ratios.items()}


def fig_components(d, year=2022):
    y = d[d.year == year]
    tot = y[list(COMPONENTS)].sum()
    rows = []
    for k, lab in COMPONENTS.items():
        s = y.set_index("stateabb")[k] / tot[k] * 100
        rows.append((lab, s["USA"], s["CHN"]))
    rows = rows[::-1]
    fig, ax = figure(7.2, 3.9)
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", color=GRID)
    pos = np.arange(len(rows))
    ax.barh(pos + 0.19, [r[2] for r in rows], height=0.36, color=RED)
    ax.barh(pos - 0.19, [r[1] for r in rows], height=0.36, color=BLUE)
    for i, (lab, us, cn) in enumerate(rows):
        ax.text(cn + 0.6, i + 0.19, f"{cn:.0f}%", va="center", fontsize=8.5, color=RED)
        ax.text(us + 0.6, i - 0.19, f"{us:.0f}%", va="center", fontsize=8.5, color=BLUE)
    ax.set_yticks(pos, [r[0] for r in rows])
    ax.text(55, 5.3, "China", color=RED, fontweight="bold")
    ax.text(55, 4.8, "United States", color=BLUE, fontweight="bold")
    ax.set_xlim(0, 70)
    ax.set_xlabel(f"Share of the state-system total, {year} (%)")
    ax.set_title("China's lead is made of steel, energy and people; America's of money")
    return save(fig, "ch03-cinc-components",
                f"Correlates of War, National Material Capabilities v7.0, {year}."), rows[::-1]


def fig_concentration(d):
    ranks = (d.sort_values(["year", "cinc"], ascending=[True, False]).groupby("year")["cinc"]
             .apply(lambda s: s.head(3).reset_index(drop=True)).unstack())
    ranks = ranks * 100
    fig, ax = figure(7.4, 4.0)
    ax.fill_between(ranks.index, ranks[2], ranks[1], color=PALE_BLUE, lw=0)
    for k, lab, col in [(0, "Largest state", RED), (1, "Second", BLUE), (2, "Third", MUTED)]:
        ax.plot(ranks.index, ranks[k], color=col, lw=1.8 if k < 2 else 1.3)
        label_end(ax, 2022, ranks[k].iloc[-1], lab, col)
    ax.annotate("Cold War: a wide gap\nbetween second and third", xy=(1965, 14), xytext=(1983, 29),
                fontsize=8.5, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    ax.set_xlim(1816, 2045)
    ax.set_xticks(range(1825, 2030, 25))
    ax.set_ylabel("Share of system capabilities (CINC, %)")
    ax.set_title("Polarity on the capability index: the gap below the top two")
    return save(fig, "ch03-concentration",
                "Correlates of War, National Material Capabilities v7.0. Shaded: gap between "
                "the second- and third-largest states."), ranks


def fig_milex_shares(milex, world):
    names = {"United States of America": ("United States", BLUE), "China": ("China", RED),
             "Russia": ("Russia (USSR to 1991)", TEAL)}
    fig, ax = figure(7.4, 3.9)
    shares = {}
    for c, (lab, col) in names.items():
        s = milex.loc[c].copy()
        if c == "Russia":
            s = s.combine_first(milex.loc["USSR"])
        s = (s / world * 100).dropna().loc[1988:]
        shares[lab] = s
        ax.plot(s.index, s, color=col, lw=2)
        label_end(ax, s.index[-1], s.iloc[-1], f"{lab.split(' (')[0]} {s.iloc[-1]:.0f}%", col)
    ax.set_xlim(1988, 2033)
    ax.set_ylim(0, 60)
    ax.set_ylabel("Share of world military spending (%)")
    ax.set_title("On military money, America still spends almost three times what China does")
    return save(fig, "ch03-milex-shares",
                "SIPRI Military Expenditure Database 2026, constant 2024 US$; world total from the "
                "regional-totals sheet."), shares


def main():
    d = nmc()
    milex, world = sipri()
    gdp, ppp = wdi("NY.GDP.MKTP.CD"), wdi("NY.GDP.MKTP.PP.CD")

    paths = [fig_cinc_shares(d)]
    p, ratios = fig_four_measures(d, gdp, ppp, milex)
    paths.append(p)
    p, rows = fig_components(d)
    paths.append(p)
    p, ranks = fig_concentration(d)
    paths.append(p)
    p, shares = fig_milex_shares(milex, world)
    paths.append(p)

    # Numbers the text states.
    w = d.pivot(index="year", columns="stateabb", values="cinc")
    print("CINC sum range", d.groupby("year").cinc.sum().agg(["min", "max", "idxmax"]).round(3).tolist())
    print("leader by year changes:")
    lead = w.idxmax(axis=1)
    print(lead[lead != lead.shift()].to_dict())
    print("USA peak", w.USA.idxmax(), round(w.USA.max(), 3), "CHN 2022", round(w.CHN[2022], 3),
          "USA 2022", round(w.USA[2022], 3), "IND 2022", round(w.IND[2022], 3))
    print("USA 1945,1950,1990,2000", w.USA[[1945, 1950, 1990, 2000]].round(3).tolist())
    print("RUS 1985", round(w.RUS[1985], 3), "RUS 1992", round(w.RUS[1992], 3))
    for name, s in ratios.items():
        print(f"{name}: first>=80 {first_year(s, 80)}, first>=100 {first_year(s, 100)}, "
              f"max {s.max():.1f} in {s.idxmax()}, last {s.iloc[-1]:.1f} in {s.index[-1]}, "
              f"1990 {s.get(1990, np.nan):.1f}, 2000 {s.get(2000, np.nan):.1f}")
    print("components 2022 (US, CN shares %):", [(r[0], round(r[1], 1), round(r[2], 1)) for r in rows])
    r = ranks.copy()
    r["gap23"] = r[1] - r[2]
    r["ratio32"] = r[2] / r[1]
    print("rank shares:", r.loc[[1850, 1900, 1913, 1938, 1950, 1970, 1985, 1995, 2010, 2022]].round(1))
    for lab, s in shares.items():
        print(lab, "share", {y: round(s.get(y, np.nan), 1) for y in (1988, 1990, 2000, 2010, 2015, 2025)})
    print("world milex 2025 bn", round(world[2025] / 1000, 1), "2015", round(world[2015] / 1000, 1))

    # Top ten spenders, 2025.
    c = milex.drop(index=[i for i in milex.index if i in ("USSR",)], errors="ignore")
    top = c[2025].dropna().sort_values(ascending=False).head(10)
    for k, v in top.items():
        print(f"TOP | {k} | {v/1000:.1f} | {v/world[2025]*100:.1f} | "
              f"{(v/c.loc[k, 2015]-1)*100 if pd.notna(c.loc[k, 2015]) else np.nan:.0f}")
    print("top10 share", round(top.sum() / world[2025] * 100, 1))

    # US urban population break.
    us = d[d.stateabb == "USA"].set_index("year")
    cn = d[d.stateabb == "CHN"].set_index("year")
    print("US upop 2016/17", us.upop[2016], us.upop[2017], "CHN upop 2016/17", cn.upop[2016], cn.upop[2017])
    print("US cinc 2016/17", round(us.cinc[2016], 3), round(us.cinc[2017], 3))
    print("N states 1816, 1900, 1950, 2022", d.groupby("year").size()[[1816, 1900, 1950, 2022]].tolist())
    print("CHN vs USA 1870 cinc", round(w.CHN[1870], 3), round(w.USA[1870], 3))
    yrs = w.index[(w.CHN > w.USA)]
    print("CHN>USA years pre-1900", [y for y in yrs if y < 1900])
    print("CHN steel share 1995/2022, pec share",
          {k: [round((d[(d.year == y) & (d.stateabb == 'CHN')][k].iloc[0] /
                      d[d.year == y][k].sum()) * 100, 1) for y in (1995, 2022)] for k in COMPONENTS})
    print("USA shares 1995/2022",
          {k: [round((d[(d.year == y) & (d.stateabb == 'USA')][k].iloc[0] /
                      d[d.year == y][k].sum()) * 100, 1) for y in (1995, 2022)] for k in COMPONENTS})
    print("IND/USA cinc first >=80", first_year((w.IND / w.USA * 100).dropna(), 80),
          "IND/USA 2022", round(w.IND[2022] / w.USA[2022] * 100, 1))
    print("UKG share 1816, 1860, 1897; USA 1897", round(w.UKG[1816], 3), round(w.UKG[1860], 3),
          round(w.UKG[1897], 3), round(w.USA[1897], 3))
    print("GMY 1913, 1938, RUS 1913, USA 1913, UKG 1913, JPN 1938",
          [round(w.loc[y, k], 3) for y, k in [(1913, "GMY"), (1938, "GMY"), (1913, "RUS"),
                                               (1913, "USA"), (1913, "UKG"), (1938, "JPN")]])
    print("USA 1919", round(w.USA[1919], 3), "UKG 1919", round(w.UKG[1919], 3))
    sh = {k: (d[(d.year == 2022) & (d.stateabb == "CHN")][k].iloc[0] / d[d.year == 2022][k].sum(),
              d[(d.year == 2022) & (d.stateabb == "USA")][k].iloc[0] / d[d.year == 2022][k].sum())
          for k in COMPONENTS}
    for lab, keys in [("without steel", [k for k in COMPONENTS if k != "irst"]),
                      ("military only", ["milper", "milex"]),
                      ("demographic only", ["tpop", "upop"]), ("industrial only", ["irst", "pec"])]:
        cn = np.mean([sh[k][0] for k in keys]) * 100
        us = np.mean([sh[k][1] for k in keys]) * 100
        print(f"2022 {lab}: CHN {cn:.1f} USA {us:.1f} ratio {cn/us*100:.0f}%")
    print("steel contribution to CHN cinc pts", round(sh["irst"][0] / 6 * 100, 1))
    print("COW milex CHN/USA 2022", round(sh["milex"][0] / sh["milex"][1] * 100, 1))
    usm = milex.loc["United States of America"]
    print("US milex 2024, 2025 bn", round(usm[2024] / 1000, 1), round(usm[2025] / 1000, 1),
          "China 2015, 2025", round(milex.loc["China", 2015] / 1000, 1), round(milex.loc["China", 2025] / 1000, 1))
    print("US/CHN milex 2025 multiple", round(usm[2025] / milex.loc["China", 2025], 2))
    print("ppp ratio 2014, market 2024", round(ratios["GDP at PPP"][2014], 1),
          round(ratios["GDP at market exchange rates"][2024], 1))
    return paths


if __name__ == "__main__":
    import sys
    sys.path.insert(0, ".")
    main()
