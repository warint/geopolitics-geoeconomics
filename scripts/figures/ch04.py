"""Figures and tables for Chapter 4: Trade, conflict and geoeconomic fragmentation.

Sources, all downloaded at source into .data-cache/:

- World Bank, World Development Indicators, NE.TRD.GNFS.ZS (trade in goods and services, % of
  GDP), bulk CSV from the World Bank API.
- Bailey, Strezhnev & Voeten, UN General Assembly ideal points, Harvard Dataverse
  doi:10.7910/DVN/LEJUQZ, version 39 (file IdealpointestimatesFP_2026FP.csv, by calendar year).
- IMF, International Trade in Goods by partner country (IMTS, formerly DOTS), SDMX 3.0 API:
  exporter-reported goods exports FOB in US dollars (XG_FOB_USD) for every reporter and partner,
  and US-reported imports CIF (MG_CIF_USD).

The full IMTS export matrix is about 120 MB and the IMF API can be slow to serve it. If the
download times out, seed .data-cache/imts_xg_fob_all.csv with the same query saved from
https://data.imf.org/en/datasets/IMF.STA:IMTS (indicator "Exports of goods, FOB, US dollar",
annual, all countries, all counterparts) in the SDMX-CSV layout (columns COUNTRY,
COUNTERPART_COUNTRY, TIME_PERIOD, OBS_VALUE).

Every number quoted in the chapter about these figures and tables is printed when this runs.
"""

import io
import zipfile

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from style import BLUE, GOLD, GRID, INK, MUTED, RED, TEAL, fetch, figure, save

WDI_TRADE = "https://api.worldbank.org/v2/en/indicator/NE.TRD.GNFS.ZS?downloadformat=csv"
IDEAL = "https://dataverse.harvard.edu/api/access/datafile/14098429"
IMTS = "https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/IMTS/+/"
SDMX_CSV = {"Accept": "application/vnd.sdmx.data+csv;version=2.0.0",
            "User-Agent": "Mozilla/5.0 (book figures; research)"}

REF_YEAR = 2021          # blocs fixed at the last full year before the invasion of Ukraine
MAIN_RULE = (0.5, -0.2)  # US-leaning if ideal point >= 0.5, China-leaning if <= -0.2
LAST = 2024              # last year with near-complete reporting in IMTS


# --------------------------------------------------------------------------- data

def wdi_series(url, name, code="WLD"):
    raw = fetch(url, name)
    with zipfile.ZipFile(raw) as z:
        member = next(n for n in z.namelist() if n.startswith("API_"))
        df = pd.read_csv(io.BytesIO(z.read(member)), skiprows=4)
    row = df[df["Country Code"] == code].iloc[0]
    years = [c for c in df.columns if c.isdigit()]
    return pd.Series(row[years].values.astype(float), index=[int(y) for y in years]).dropna()


def ideal_points():
    ip = pd.read_csv(fetch(IDEAL, "unga_idealpoints_2026FP.csv"))
    return ip[["iso3c", "year", "IdealPointFP"]].rename(columns={"IdealPointFP": "ip"})


def imts_exports():
    path = fetch(IMTS + "*.XG_FOB_USD.*.A", "imts_xg_fob_all.csv", headers=SDMX_CSV)
    t = pd.read_csv(path, usecols=["COUNTRY", "COUNTERPART_COUNTRY", "TIME_PERIOD", "OBS_VALUE"])
    t.columns = ["o", "d", "yr", "v"]
    return t.dropna()


def us_imports():
    path = fetch(IMTS + "USA.MG_CIF_USD.*.A", "imts_usa_mg_cif.csv", headers=SDMX_CSV)
    t = pd.read_csv(path, usecols=["COUNTERPART_COUNTRY", "TIME_PERIOD", "OBS_VALUE"])
    return t.pivot_table(index="TIME_PERIOD", columns="COUNTERPART_COUNTRY", values="OBS_VALUE")


# --------------------------------------------------------------------------- blocs

def blocs_cut(ip_year, hi, lo, overrides=None):
    b = pd.Series(np.where(ip_year >= hi, "US", np.where(ip_year <= lo, "CN", "NA")),
                  index=ip_year.index)
    for k, v in (overrides or {}).items():
        b[k] = v
    return b


def blocs_mid(ip_year, margin):
    """The 'closer to Washington or to Beijing' rule: |x - CHN| - |x - USA| against a margin."""
    d = (ip_year - ip_year["CHN"]).abs() - (ip_year - ip_year["USA"]).abs()
    return pd.Series(np.where(d > margin, "US", np.where(d < -margin, "CN", "NA")), index=d.index)


def bloc_flows(t, b):
    o, d = t.o.map(b), t.d.map(b)
    cat = np.select([(o == "US") & (d == "US"), (o == "CN") & (d == "CN"),
                     ((o == "US") & (d == "CN")) | ((o == "CN") & (d == "US"))],
                    ["within US-leaning", "within China-leaning", "between blocs"],
                    "involving non-aligned")
    return t.assign(c=cat).pivot_table(index="yr", columns="c", values="v", aggfunc="sum")


def gap(f, base=REF_YEAR, end=LAST):
    """Growth of between-bloc trade minus growth of within-bloc trade (both blocs pooled), pp."""
    within = f["within US-leaning"] + f["within China-leaning"]
    g_w = (within[end] / within[base] - 1) * 100
    g_b = (f["between blocs"][end] / f["between blocs"][base] - 1) * 100
    return g_b, g_w, g_b - g_w


# --------------------------------------------------------------------------- figures

def spread(values, gap):
    """Nudge label positions apart so that neighbours are at least `gap` apart."""
    order = sorted(values, key=values.get)
    out, last = {}, -np.inf
    for k in order:
        out[k] = max(values[k], last + gap)
        last = out[k]
    return out

def fig_world_trade():
    s = wdi_series(WDI_TRADE, "wdi_NE.TRD.GNFS.ZS.zip")
    print(f"[F1] latest WDI value {s.index[-1]} {s.iloc[-1]:.1f} (partial aggregate, dropped)")
    s = s.loc[:LAST]
    peak = s.loc[:2010].idxmax()
    print(f"[F1] world trade/GDP: 1970 {s[1970]:.1f}, 1990 {s[1990]:.1f}, peak {peak} "
          f"{s[peak]:.1f}, 2009 {s[2009]:.1f}, 2019 {s[2019]:.1f}, 2020 {s[2020]:.1f}, "
          f"2022 {s[2022]:.1f}, last {s.index[-1]} {s.iloc[-1]:.1f}; max {s.idxmax()} {s.max():.1f}")
    fig, ax = figure()
    ax.plot(s.index, s.values, color=BLUE)
    ax.set_title("World trade rose for four decades and has moved sideways since 2008")
    ax.set_ylabel("Exports plus imports, % of world GDP")
    for yr, label, dy in [(1991, "End of the\nCold War", 6), (2001, "China joins\nthe WTO", 7),
                          (2009, "Global financial\ncrisis", -10), (2020, "Pandemic", -9),
                          (2022, "Invasion of\nUkraine", 5)]:
        ax.annotate(label, (yr, s[yr]), (yr, s[yr] + dy), ha="center", fontsize=8, color=MUTED,
                    arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    ax.set_xlim(s.index[0] - 1, s.index[-1] + 1)
    ax.set_ylim(20, 70)
    return save(fig, "ch04-world-trade-gdp", "World Bank, World Development Indicators "
                "(NE.TRD.GNFS.ZS, world aggregate).")


def fig_ideal_points(ip):
    show = {"USA": ("United States", BLUE), "CHN": ("China", RED), "RUS": ("Russia / USSR", INK),
            "IND": ("India", GOLD), "DEU": ("Germany (FRG)", TEAL)}
    fig, ax = figure(7.2, 4.2)
    ends = {}
    for iso, (label, col) in show.items():
        s = ip[ip.iso3c == iso].set_index("year").ip.sort_index()
        s = s[s.index >= 1950]
        ax.plot(s.index, s.values, color=col, lw=1.6)
        ends[iso] = s.iloc[-1]
        print(f"[F2] {iso}: 1985 {s.get(1985, np.nan):.2f}, 1995 {s.get(1995, np.nan):.2f}, "
              f"2021 {s[2021]:.2f}, 2025 {s.get(2025, np.nan):.2f}")
    for iso, yv in spread(ends, 0.3).items():
        ax.text(2026, yv, show[iso][0], color=show[iso][1], fontsize=8.5, va="center")
    ax.axvline(1991, color=GRID, lw=1)
    ax.text(1991.5, ax.get_ylim()[1] * 0.95, "1991", fontsize=8, color=MUTED)
    ax.set_title("On the UN General Assembly scale, the United States sits at one end, alone")
    ax.set_ylabel("Ideal point (higher = closer to the US)")
    ax.set_xlim(1950, 2034)
    return save(fig, "ch04-ideal-points", "Bailey, Strezhnev & Voeten, UN General Assembly ideal "
                "points, Harvard Dataverse doi:10.7910/DVN/LEJUQZ, v39 (2026).")


def fig_bloc_trade(t, b):
    f = bloc_flows(t[t.yr.between(2015, LAST)], b)
    cols = {"within US-leaning": BLUE, "within China-leaning": RED,
            "involving non-aligned": GOLD, "between blocs": INK}
    fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.9), sharey=True)
    fig.add_artist(plt.Line2D([0.0, 0.07], [1.02, 1.02], transform=fig.transFigure, color=RED,
                              linewidth=4, solid_capstyle="butt"))
    for ax, base in zip(axes, (2019, 2021)):
        ix = f / f.loc[base] * 100
        for c, col in cols.items():
            ax.plot(ix.index, ix[c], color=col, lw=2.2 if c == "between blocs" else 1.6)
        ax.axhline(100, color=MUTED, lw=0.7)
        ax.axvline(2022, color=GRID, lw=1)
        ax.set_title(f"Index, {base} = 100", fontsize=10.5)
        ax.set_xticks(range(2015, LAST + 1, 3))
        print(f"[F3] base {base}: " + ", ".join(f"{c} {ix.loc[LAST, c]:.0f}" for c in cols))
    ix = f / f.loc[2021] * 100
    for c, yv in spread({c: ix.loc[LAST, c] for c in cols}, 3.5).items():
        axes[1].text(LAST + 0.2, yv, c, color=cols[c], fontsize=8, va="center")
    axes[0].set_ylabel("Goods exports in current US$")
    fig.suptitle("Since 2022, trade between the blocs has grown more slowly than trade within them",
                 x=0.0, ha="left", fontsize=12, fontweight="bold", y=1.0)
    fig.subplots_adjust(top=0.84, wspace=0.08)
    return save(fig, "ch04-bloc-trade", "IMF IMTS (exporter-reported exports, FOB, US$); blocs "
                "from UNGA ideal points in 2021 (US-leaning >= 0.5, China-leaning <= -0.2); "
                "author's calculations.")


def rule_table(t, ipy):
    tt = t[t.yr.between(2015, LAST)]
    variants = [
        ("Closer to Washington or Beijing, margin 0", blocs_mid(ipy, 0)),
        ("Closer to Washington or Beijing, margin 0.5", blocs_mid(ipy, 0.5)),
        ("Cut-offs +0.3 / -0.3", blocs_cut(ipy, 0.3, -0.3)),
        ("Cut-offs +0.5 / -0.2 (main)", blocs_cut(ipy, *MAIN_RULE)),
        ("Cut-offs +0.5 / -0.4", blocs_cut(ipy, 0.5, -0.4)),
        ("Cut-offs +0.7 / -0.1", blocs_cut(ipy, 0.7, -0.1)),
        ("Main, Russia moved to China-leaning", blocs_cut(ipy, *MAIN_RULE, {"RUS": "CN"})),
    ]
    rows = []
    for name, b in variants:
        f = bloc_flows(tt, b)
        g_b, g_w, g = gap(f)
        g19 = gap(f, base=2019)[2]
        n = b.value_counts()
        share = f.loc[REF_YEAR, "between blocs"] / f.loc[REF_YEAR].sum() * 100
        rows.append((name, n.get("US", 0), n.get("CN", 0), n.get("NA", 0), share, g_b, g_w, g, g19))
    tab = pd.DataFrame(rows, columns=["rule", "US", "CN", "NA", "between_share_2021",
                                      "between_growth", "within_growth", "gap_2021", "gap_2019"])
    print("[T1] bloc-rule sensitivity (growth 2021->%d, %%; gap in pp):" % LAST)
    print(tab.round(1).to_string(index=False))
    fig, ax = figure(7.2, 3.6)
    y = np.arange(len(tab))[::-1]
    colors = [RED if "main" in r else (MUTED if "Washington" in r else BLUE) for r in tab.rule]
    ax.barh(y, tab.gap_2021, color=colors, height=0.6)
    for yi, v in zip(y, tab.gap_2021):
        ax.text(v - 0.4 if v < 0 else v + 0.4, yi, f"{v:+.0f}", va="center",
                ha="right" if v < 0 else "left", fontsize=8.5)
    ax.set_yticks(y, tab.rule, fontsize=8.5)
    ax.axvline(0, color=INK, lw=0.8)
    ax.set_xlim(tab.gap_2021.min() - 2.5, 0.5)
    ax.set_xticks(range(-16, 1, 2))
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", color=GRID)
    ax.set_xlabel(f"Between-bloc growth minus within-bloc growth, {REF_YEAR}-{LAST}, "
                  "percentage points")
    ax.set_title("The size of the break depends on where the bloc lines are drawn")
    save(fig, "ch04-rule-sensitivity", "IMF IMTS; UNGA ideal points (Bailey, Strezhnev & "
         "Voeten, v39); author's calculations.")
    return tab


def connectors(t, b):
    """Non-aligned countries: change in total goods trade with each bloc, 2019 -> LAST."""
    tt = t[t.yr.isin([2019, REF_YEAR, LAST])]
    na = b[b == "NA"].index
    out = []
    for c in na:
        row = {"iso": c}
        for yr in (2019, LAST):
            s = tt[tt.yr == yr]
            for bloc in ("US", "CN"):
                members = b[b == bloc].index
                x = s[(s.o == c) & s.d.isin(members)].v.sum()     # c's exports to bloc
                m = s[s.o.isin(members) & (s.d == c)].v.sum()     # bloc's exports to c
                row[f"{bloc}{yr}"] = x + m
        out.append(row)
    df = pd.DataFrame(out).set_index("iso")
    df["gUS"] = (df[f"US{LAST}"] / df["US2019"] - 1) * 100
    df["gCN"] = (df[f"CN{LAST}"] / df["CN2019"] - 1) * 100
    df["size"] = (df[f"US{LAST}"] + df[f"CN{LAST}"]) / 1e9
    top = df.sort_values("size", ascending=False).head(10)
    print(f"[T2] largest non-aligned traders, growth of trade with each bloc 2019->{LAST} (%), "
          f"size = trade with both blocs {LAST}, US$ bn:")
    print(top[["size", "gUS", "gCN"]].round(0).to_string())
    return top


def hirschman(t):
    """Hirschman's index of partner concentration of exports: 100 * sqrt(sum of squared shares)."""
    rows = []
    for c in ["MNG", "RUS", "MEX", "CAN", "VNM", "KOR", "DEU", "CHN", "USA", "IND"]:
        r = {"iso": c}
        for yr in (REF_YEAR, LAST):
            s = t[(t.o == c) & (t.yr == yr) & ~t.d.str.match(r"^(G\d|GX|TX)")]
            s = s.groupby("d").v.sum()
            sh = s / s.sum()
            r[f"H{yr}"] = 100 * np.sqrt((sh ** 2).sum())
            r[f"top{yr}"] = sh.idxmax()
            r[f"topshare{yr}"] = sh.max() * 100
        rows.append(r)
    df = pd.DataFrame(rows).set_index("iso")
    print(f"[T3] Hirschman export-concentration index and largest partner, {REF_YEAR} and {LAST}:")
    print(df.round(1).to_string())
    return df


def fig_us_imports():
    m = us_imports()
    world = m["G001"]
    sh = m[["CHN", "MEX", "VNM", "CAN"]].div(world, axis=0) * 100
    sh = sh.loc[1990:]
    for yr in (2000, 2017, 2022, 2024, sh.index[-1]):
        print(f"[F5] US import shares {yr}: " + ", ".join(f"{c} {sh.loc[yr, c]:.1f}"
                                                         for c in sh.columns))
    fig, ax = figure()
    names = {"CHN": ("China", RED), "MEX": ("Mexico", TEAL), "CAN": ("Canada", MUTED),
             "VNM": ("Vietnam", GOLD)}
    for c, (label, col) in names.items():
        ax.plot(sh.index, sh[c], color=col)
        ax.text(sh.index[-1] + 0.4, sh[c].iloc[-1], label, color=col, fontsize=8.5, va="center")
    ax.axvline(2018, color=GRID, lw=1)
    ax.text(2017.7, 24.5, "Section 301\ntariffs, 2018", fontsize=8, color=MUTED, ha="right")
    ax.axvline(2001, color=GRID, lw=1)
    ax.text(2001.3, 24.5, "China joins\nthe WTO", fontsize=8, color=MUTED)
    ax.set_title("China's share of US goods imports has fallen by more than half since 2017")
    ax.set_ylabel("% of US goods imports (CIF)")
    ax.set_xlim(1990, sh.index[-1] + 4)
    ax.set_ylim(0, 27)
    return save(fig, "ch04-us-import-shares", "IMF IMTS, US-reported imports CIF by partner "
                f"(MG_CIF_USD); {sh.index[-1]} provisional.")


def main():
    ip = ideal_points()
    ipy = ip[ip.year == REF_YEAR].set_index("iso3c").ip
    print(f"ideal points {REF_YEAR}: {len(ipy)} countries; USA {ipy['USA']:.2f}, CHN "
          f"{ipy['CHN']:.2f}, midpoint {(ipy['USA'] + ipy['CHN']) / 2:.2f}; RUS {ipy['RUS']:.2f}, "
          f"IND {ipy['IND']:.2f}, BRA {ipy['BRA']:.2f}, MEX {ipy['MEX']:.2f}, VNM "
          f"{ipy['VNM']:.2f}, JPN {ipy['JPN']:.2f}, KOR {ipy['KOR']:.2f}, TUR {ipy['TUR']:.2f}")
    print("  countries above the US-China midpoint:", (ipy > (ipy["USA"] + ipy["CHN"]) / 2).sum())
    t_all = imts_exports()
    t = t_all[t_all.o.isin(ipy.index) & t_all.d.isin(ipy.index)]
    b = blocs_cut(ipy, *MAIN_RULE)
    for bloc in ("US", "CN", "NA"):
        print(f"  main rule {bloc}: {sorted(b[b == bloc].index)}")
    paths = [fig_world_trade(), fig_ideal_points(ip), fig_bloc_trade(t, b)]
    rule_table(t, ipy)
    paths.append(paths[-1].with_name("ch04-rule-sensitivity.png"))
    connectors(t, b)
    hirschman(t_all)
    paths.append(fig_us_imports())
    world = t_all[(t_all.yr == LAST) & (t_all.d == "G001") & t_all.o.isin(ipy.index)]
    covered = t[t.yr == LAST].v.sum() / world.v.sum()
    print(f"share of world exports ({LAST}) covered by ideal-point countries: {covered * 100:.1f}%")
    return paths


if __name__ == "__main__":
    main()
