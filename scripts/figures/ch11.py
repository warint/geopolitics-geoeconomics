"""Chapter 11 — Space geopolitics. Figures from the public satellite catalogues.

Data, downloaded at source into .data-cache/:
- CelesTrak SATCAT (T. S. Kelso, from the US Space Force public catalogue), one row per
  catalogued object: https://celestrak.org/pub/satcat.csv (format: celestrak.org/satcat/satcat-format.php).
  CelesTrak asks for one download per update, which the cache respects.
- J. C. McDowell, General Catalog of Artificial Space Objects (GCAT), satellite catalogue:
  https://planet4589.org/space/gcat/tsv/cat/satcat.tsv (tab-separated, a "# Updated" line under the
  header). GCAT records for each fragment the date it separated from its parent (SDate), which
  SATCAT does not, and an operator code (Owner) as well as a state code (State).

Both catalogues are updated daily, so the numbers printed below (and quoted in the chapter) are
those of the vintage in the cache; delete the cache files to redraw from the current catalogues.
ESA's totals quoted in the chapter come from its Space Environment Report 2026, not from this script.
"""

import numpy as np
import pandas as pd

from style import (BLUE, GOLD, GRID, INK, MUTED, PALE_BLUE, PALE_RED, PALE_TEAL, RED, TEAL,
                   fetch, figure, plt, save)

SATCAT_URL = "https://celestrak.org/pub/satcat.csv"
GCAT_URL = "https://planet4589.org/space/gcat/tsv/cat/satcat.tsv"
SRC_SATCAT = "CelesTrak SATCAT (US Space Force public catalogue)"
SRC_GCAT = "J. C. McDowell, GCAT satellite catalogue"
ACTIVE = list("+PBSX")
LAST = 2025  # last complete year


def load_satcat():
    s = pd.read_csv(fetch(SATCAT_URL, "celestrak_satcat.csv"), keep_default_na=False,
                    na_values=[""])
    s["ly"] = pd.to_datetime(s["LAUNCH_DATE"], errors="coerce").dt.year
    s["dy"] = pd.to_datetime(s["DECAY_DATE"], errors="coerce").dt.year
    print(f"[satcat] vintage: last launch date {s['LAUNCH_DATE'].max()}, rows {len(s)}")
    return s


def load_gcat():
    g = pd.read_csv(fetch(GCAT_URL, "gcat_satcat.tsv"), sep="\t", skiprows=[1], dtype=str)
    g.columns = [c.lstrip("#") for c in g.columns]
    g = g.apply(lambda c: c.str.strip())
    g["ly"] = pd.to_numeric(g["LDate"].str[:4], errors="coerce")
    g["sy"] = pd.to_numeric(g["SDate"].str[:4], errors="coerce")
    g["dy"] = pd.to_numeric(g["DDate"].replace("-", np.nan).str[:4], errors="coerce")
    # Objects that left Earth orbit (deep space, escape, heliocentric) are dropped.
    g = g[~g["Status"].str.startswith(("DS", "E", "AO"))]
    g["cls"] = g["Type"].str[0].map({"P": "Payloads", "R": "Rocket bodies", "D": "Debris",
                                     "C": "Debris"})
    return g


def stock(start, end, years):
    return pd.Series([int(((start <= y) & (end.isna() | (end > y))).sum()) for y in years],
                     index=years)


def fig_stock(s, g):
    years = np.arange(1957, LAST + 1)
    gg = g.dropna(subset=["cls"])
    parts = {c: stock(gg.loc[gg["cls"] == c, "sy"], gg.loc[gg["cls"] == c, "dy"], years)
             for c in ["Payloads", "Rocket bodies", "Debris"]}
    e = s[s["ORBIT_CENTER"] == "EA"]
    deb_launch = stock(e.loc[e["OBJECT_TYPE"] == "DEB", "ly"], e.loc[e["OBJECT_TYPE"] == "DEB", "dy"],
                       years)
    fig, ax = figure(7.4, 4.0)
    ax.stackplot(years, parts["Payloads"], parts["Rocket bodies"], parts["Debris"],
                 colors=[BLUE, GOLD, PALE_RED], lw=0)
    ax.plot(years, parts["Payloads"] + parts["Rocket bodies"] + deb_launch, color=INK, lw=1.1,
            ls="--")
    ax.text(1962, 21500, "Total if debris is dated by its\nparent's launch (SATCAT)", fontsize=8,
            color=INK)
    tot = sum(parts.values())
    ax.text(1985, 6000, "Debris", fontsize=9, color=RED, fontweight="bold")
    ax.annotate("Rocket bodies", (2003, 3200), xytext=(1990, 9000), fontsize=8, color=INK,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    ax.text(1993, 800, "Payloads", fontsize=9, color="white", fontweight="bold")
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:,.0f}"))
    for yr, label, dy in [(2007, "2007 Chinese\nASAT test", 2500), (2009, "2009 Iridium–\nCosmos collision", 5200),
                          (2021, "2021 Russian\nASAT test", 4200)]:
        ax.annotate(label, (yr, tot[yr]), xytext=(yr - 13, tot[yr] + dy), fontsize=8,
                    arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    ax.set_xlim(1957, LAST + 1)
    ax.set_ylabel("Catalogued objects in Earth orbit, end of year")
    ax.set_title("Debris built the orbital population; payloads overtook it in 2024")
    for y in (1980, 2000, 2006, 2007, 2008, 2009, 2010, 2020, 2021, 2022, 2023, 2024, 2025):
        print(f"[stock] {y}: payloads {parts['Payloads'][y]}, R/B {parts['Rocket bodies'][y]}, "
              f"debris (event-dated) {parts['Debris'][y]}, total {tot[y]}; debris launch-dated "
              f"{deb_launch[y]}")
    y = LAST
    sc = e[(e["ly"] <= y) & (e["dy"].isna() | (e["dy"] > y))]
    print(f"[stock] SATCAT launch-dated stock end {y}: total {len(sc)}, "
          f"{sc['OBJECT_TYPE'].value_counts().to_dict()}")
    first = years[(parts["Debris"] > parts["Payloads"]).values]
    print(f"[stock] debris exceeds payloads first in {first.min()}")
    print(f"[stock] 2006->2007 change: event-dated debris {parts['Debris'][2007] - parts['Debris'][2006]}, "
          f"launch-dated {deb_launch[2007] - deb_launch[2006]}")
    cross = years[(parts["Payloads"] > parts["Debris"]).values & (years > 1970)]
    print(f"[stock] payloads exceed debris from {cross.min() if len(cross) else 'never'}")
    return save(fig, "ch11-objects-in-orbit", SRC_GCAT + " (objects dated by separation, "
                "debris includes mission-related objects); dashed line: " + SRC_SATCAT + ".")


def fig_launched(g):
    p = g[g["Type"].str[0] == "P"].copy()
    years = np.arange(1990, LAST + 1)
    grp = np.select([p["Owner"] == "SPXS", p["State"] == "US", p["State"] == "CN",
                     p["State"].isin(["RU", "SU"])],
                    ["SpaceX (Starlink)", "Other United States", "China", "Russia"], "Rest of world")
    p["grp"] = grp
    t = p[p["ly"].between(1990, LAST)].groupby(["ly", "grp"]).size().unstack(fill_value=0)
    t = t.reindex(years, fill_value=0)
    order = ["SpaceX (Starlink)", "Other United States", "China", "Russia", "Rest of world"]
    cols = [RED, PALE_RED, GOLD, BLUE, MUTED]
    fig, ax = figure(7.4, 3.9)
    bottom = np.zeros(len(years))
    for name, col in zip(order, cols):
        ax.bar(years, t[name], bottom=bottom, color=col, width=0.8)
        bottom += t[name].values
    ypos = {"SpaceX (Starlink)": 2600, "Other United States": 3500, "China": 3900,
            "Russia": 4200, "Rest of world": 4500}
    for name, col in zip(order, cols):
        ax.text(1991, ypos[name], name, color=col if col != PALE_RED else "#C9837E", fontsize=8.5,
                fontweight="bold")
    ax.set_xlim(1989, LAST + 1)
    ax.set_ylabel("Payloads launched in the year")
    ax.set_title("One company now launches most of the world's satellites")
    for y in (2000, 2018, 2019, 2020, 2022, 2024, 2025):
        row = t.loc[y]
        print(f"[launched] {y}: total {row.sum()}, " + ", ".join(f"{k} {v}" for k, v in row.items())
              + f"; SpaceX share {row['SpaceX (Starlink)'] / row.sum():.0%}")
    return save(fig, "ch11-payloads-launched", SRC_GCAT + "; payloads by launch year, grouped by "
                "operator (SpaceX) and owner state.")


def hhi(df, key):
    sh = df.groupby(["ly", key]).size()
    return sh.groupby(level=0).apply(lambda s: ((100 * s / s.sum()) ** 2).sum())


def fig_hhi(g):
    p = g[(g["Type"].str[0] == "P") & g["ly"].between(1957, LAST)].copy()
    p["state"] = p["State"].replace({"SU": "RU"})
    by_state = hhi(p, "state")
    by_owner = hhi(p, "Owner")
    fig, ax = figure(7.4, 3.9)
    ax.axhspan(1800, 10000, color=PALE_RED, alpha=0.35, lw=0, zorder=0)
    ax.text(1995, 9700, "Highly concentrated: above 1,800\n(2023 US merger guidelines)",
            fontsize=8, color=RED, va="top", ha="left")
    ax.plot(by_state.index, by_state.values, color=BLUE, lw=2)
    ax.plot(by_owner.index, by_owner.values, color=RED, lw=2)
    ax.text(1993, 5600, "By owner state", color=BLUE, fontsize=9,
            fontweight="bold")
    ax.text(2001, 900, "By operator", color=RED, fontsize=9, fontweight="bold")
    ax.annotate("Starlink's first\nlaunches, 2019", (2019, by_owner[2019]), xytext=(2005, 3600),
                fontsize=8, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    ax.set_ylim(0, 10000)
    ax.set_xlim(1957, LAST + 1)
    ax.set_ylabel("Herfindahl–Hirschman index")
    ax.set_title("Concentration of new satellites is back at Cold War levels, with a firm on top")
    for y in (1960, 1970, 1980, 1990, 2000, 2010, 2015, 2018, 2019, 2020, 2022, 2024, 2025):
        print(f"[hhi] {y}: state {by_state[y]:.0f}, operator {by_owner[y]:.0f}")
    low = by_state.loc[1990:2018]
    print(f"[hhi] state minimum 1990-2018: {low.min():.0f} in {low.idxmin()}; operator min "
          f"{by_owner.loc[1990:2018].min():.0f} in {by_owner.loc[1990:2018].idxmin()}")
    return save(fig, "ch11-concentration", SRC_GCAT + "; payloads launched each year; shares in "
                "percent; Soviet Union and Russia combined.")


def fig_altitude(s):
    e = s[(s["ORBIT_CENTER"] == "EA") & s["DECAY_DATE"].isna()].copy()
    e["alt"] = (e["APOGEE"] + e["PERIGEE"]) / 2
    leo = e[e["alt"].between(200, 2000)]
    bins = np.arange(200, 2001, 25)
    fig, ax = figure(7.4, 3.9)
    star = leo[leo["OBJECT_NAME"].str.startswith("STARLINK")]
    oth = leo[(leo["OBJECT_TYPE"] == "PAY") & ~leo["OBJECT_NAME"].str.startswith("STARLINK")]
    deb = leo[leo["OBJECT_TYPE"].isin(["DEB", "R/B", "UNK"])]
    h = [np.histogram(x["alt"], bins)[0] for x in (star, oth, deb)]
    mid = bins[:-1] + 12.5
    ax.bar(mid, h[0], width=24, color=RED)
    ax.bar(mid, h[1], width=24, bottom=h[0], color=BLUE)
    ax.bar(mid, h[2], width=24, bottom=h[0] + h[1], color=PALE_RED, edgecolor=GRID, lw=0.3)
    ax.text(1150, 3800, "Starlink", color=RED, fontsize=9, fontweight="bold")
    ax.text(1150, 3400, "Other payloads", color=BLUE, fontsize=9, fontweight="bold")
    ax.text(1150, 3000, "Debris and rocket bodies", color="#C9837E", fontsize=9, fontweight="bold")
    ax.set_xlabel("Mean altitude, km (average of apogee and perigee)")
    ax.set_ylabel("Objects in orbit, per 25 km band")
    ax.set_title("Satellites crowd below 600 km; debris lingers higher, where drag is weak")
    print(f"[altitude] objects in orbit {len(e)}, of which 200-2000 km {len(leo)}")
    for lo, hi in [(200, 600), (600, 700), (700, 900), (900, 2000)]:
        b = leo[leo["alt"].between(lo, hi, inclusive="left")]
        print(f"[altitude] {lo}-{hi} km: {len(b)} objects, payload share "
              f"{(b['OBJECT_TYPE'] == 'PAY').mean():.0%}, Starlink {b['OBJECT_NAME'].str.startswith('STARLINK').sum()}, "
              f"debris+R/B {b['OBJECT_TYPE'].isin(['DEB', 'R/B', 'UNK']).sum()}")
    return save(fig, "ch11-altitude", SRC_SATCAT + "; objects not decayed, orbiting the Earth, "
                "mean altitude 200–2,000 km.")


def events_table(s):
    events = {"FENGYUN 1C DEB": "Chinese ASAT test, Jan 2007",
              "COSMOS 2251 DEB": "Collision, Feb 2009 (Cosmos side)",
              "IRIDIUM 33 DEB": "Collision, Feb 2009 (Iridium side)",
              "USA 193 DEB": "US intercept, Feb 2008",
              "MICROSAT-R DEB": "Indian ASAT test, Mar 2019",
              "COSMOS 1408 DEB": "Russian ASAT test, Nov 2021",
              "NOAA 16 DEB": "Break-up, Nov 2015", "NOAA 17 DEB": "Break-up, Mar 2021",
              "DMSP 5D-2 F13 DEB": "Break-up, Feb 2015"}
    for name, label in events.items():
        d = s[s["OBJECT_NAME"] == name]
        left = int(d["DECAY_DATE"].isna().sum())
        alt = ((d["APOGEE"] + d["PERIGEE"]) / 2)[d["DECAY_DATE"].isna()].median()
        print(f"[events] {label}: catalogued {len(d)}, still in orbit {left} "
              f"({left / len(d):.0%}), median altitude of survivors {alt:.0f} km")


def main():
    s = load_satcat()
    g = load_gcat()
    e = s[(s["ORBIT_CENTER"] == "EA") & s["DECAY_DATE"].isna()]
    star = e[e["OBJECT_NAME"].str.startswith("STARLINK")]
    act = e["OPS_STATUS_CODE"].isin(ACTIVE)
    print(f"[now] SATCAT in Earth orbit {len(e)} ({e['OBJECT_TYPE'].value_counts().to_dict()}); "
          f"active {act.sum()}; Starlink in orbit {len(star)}, active "
          f"{star['OPS_STATUS_CODE'].isin(ACTIVE).sum()} = {star['OPS_STATUS_CODE'].isin(ACTIVE).sum() / act.sum():.0%} of active")
    events_table(s)
    return [fig_stock(s, g), fig_launched(g), fig_hhi(g), fig_altitude(s)]


if __name__ == "__main__":
    main()
