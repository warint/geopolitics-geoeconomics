"""Chapter 10 — Economic sanctions. Figures from TIES and from IMF trade statistics.

Data, downloaded at source into .data-cache/:
- Morgan, Bapat and Kobayashi, Threat and Imposition of Economic Sanctions (TIES) v4.0, case file
  https://sanctions.web.unc.edu/wp-content/uploads/sites/18834/2021/04/TIESv4-1.xls
  (user manual: .../2021/04/tiesusersmanualv4.pdf). The UNC server refuses scripted requests from
  Python (HTTP 403) while serving browsers and curl: if fetch() fails, download the file by hand
  (or `curl -A "Mozilla/5.0" -o .data-cache/ties_TIESv4-1.xls <url>`) and rerun. Outcome codes 1-5 end a case at the threat
  stage, 6-10 after imposition (manual, variable 39).
- Correlates of War state codes, https://correlatesofwar.org/wp-content/uploads/COW-country-codes.csv
  (TIES codes the European Community / Union as 1000, which is not in the COW list).
- IMF, International Trade in Goods by partner country (IMTS), exports f.o.b. in US dollars, annual,
  SDMX 3.0 API at https://api.imf.org/external/sdmx/3.0/ (dataflow IMF.STA:IMTS).

The Global Sanctions Data Base is not used: it is distributed on request and may not be
redistributed. IMTS is revised as countries report, so the figures printed below are those of the
vintage in the cache; delete the cache files to redraw from the current data.
"""

import io

import numpy as np
import pandas as pd

from style import (BLUE, GOLD, GRID, INK, MUTED, PALE_BLUE, PALE_RED, PALE_TEAL, RED, TEAL,
                   fetch, figure, plt, save)

TIES_URL = "https://sanctions.web.unc.edu/wp-content/uploads/sites/18834/2021/04/TIESv4-1.xls"
COW_URL = "https://correlatesofwar.org/wp-content/uploads/COW-country-codes.csv"
EU27 = ("AUT BEL BGR HRV CYP CZE DNK EST FIN FRA DEU GRC HUN IRL ITA LVA LTU LUX MLT NLD POL PRT "
        "ROU SVK SVN ESP SWE").split()
OTHERS = ["CHN", "TUR", "USA", "JPN", "KOR", "IND", "GBR"]
PARTNERS = ["RUS", "KGZ", "ARM", "KAZ", "GEO", "UZB", "TJK"]
IMTS_URL = ("https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/IMTS/+/"
            + "+".join(EU27 + OTHERS) + ".XG_FOB_USD." + "+".join(PARTNERS) + ".A")
UA = {"User-Agent": "Mozilla/5.0"}
IMTS_HDR = {"Accept": "application/vnd.sdmx.data+csv;version=2.0.0", "User-Agent": "Mozilla/5.0"}
SRC_TIES = "Morgan, Bapat and Kobayashi, TIES v4.0 case file (1,412 cases, 1945–2005)"
SRC_IMTS = "IMF, International Trade in Goods by partner country (IMTS), exports f.o.b., US dollars"

OUTCOME = {1: "Partial acquiescence", 2: "Complete acquiescence", 3: "Sender backs down",
           4: "Stalemate", 5: "Negotiated settlement"}
ORDER = ["Complete acquiescence", "Partial acquiescence", "Negotiated settlement", "Stalemate",
         "Sender backs down"]


def load_ties():
    t = pd.read_excel(fetch(TIES_URL, "ties_TIESv4-1.xls", headers=UA))
    issues = t[["issue1", "issue2", "issue3"]]
    # Economic disputes: every coded issue is trade practices (13) or economic reform (14).
    t["economic"] = issues.apply(lambda r: set(r.dropna().astype(int)) <= {13, 14}, axis=1)
    code = t["finaloutcome"]
    t["stage"] = np.select([code.between(1, 5), code.between(6, 10)],
                           ["Threat stage", "After imposition"], "No outcome coded")
    t["outcome"] = ((code - 1) % 5 + 1).map(OUTCOME)
    return t


def cow_names():
    raw = fetch(COW_URL, "cow_country_codes.csv", headers=UA).read_bytes().decode("latin-1")
    c = pd.read_csv(io.StringIO(raw.replace("\r", "\n"))).drop_duplicates("CCode")
    names = dict(zip(c["CCode"], c["StateNme"]))
    names.update({1000: "EC / EU", 2: "United States", 260: "West Germany", 730: "Korea"})
    return names


def fig_cases(t):
    years = np.arange(1945, 2006)
    imp = t[t["imposition"] == 1].groupby("startyear").size().reindex(years, fill_value=0)
    thr = t[t["imposition"] == 0].groupby("startyear").size().reindex(years, fill_value=0)
    fig, ax = figure(7.4, 3.8)
    ax.bar(years, imp, color=BLUE, width=0.8, label="Sanctions imposed")
    ax.bar(years, thr, bottom=imp, color=PALE_BLUE, width=0.8, label="Threat only")
    ax.text(1950, 75, "Sanctions imposed", color=BLUE, fontsize=9, fontweight="bold")
    ax.text(1950, 67, "Threatened, never imposed", color=MUTED, fontsize=9)
    ax.annotate("1993: 87 cases begin,\nthe peak of the record", (1993, 87), xytext=(1966, 52),
                fontsize=8, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    ax.set_ylabel("Cases beginning in the year")
    ax.set_xlim(1944, 2006)
    ax.set_title("Sanctions cases multiplied after the Cold War, and many never got past a threat")
    dec = t.groupby(t["startyear"] // 10 * 10)["imposition"].agg(["size", "sum"])
    dec["threat_only_share"] = 1 - dec["sum"] / dec["size"]
    print("[cases] by decade:\n", dec.round(3))
    print(f"[cases] total {len(t)}, imposed {int(t['imposition'].sum())}, threat-only "
          f"{int((t['imposition'] == 0).sum())}; peak year {(imp + thr).idxmax()} "
          f"with {(imp + thr).max()} cases")
    us = (t["primarysender"] == 2).mean()
    print(f"[cases] US primary sender share: {us:.1%}")
    return save(fig, "ch10-ties-cases", SRC_TIES + "; cases by start year.")


def fig_active(t):
    """Active imposed cases per year under three rules for cases without an end year."""
    imp = t[t["imposition"] == 1].copy()
    # Three imposition years carry a coder's note after the year ("1949, sometime before ..."):
    # keep the leading four digits.
    yr = imp["sancimpositionstartyear"].astype(str).str.extract(r"^(\d{4})")[0].astype(float)
    imp["start"] = yr.fillna(imp["startyear"])
    years = np.arange(1945, 2006)
    rules = {
        "No end year = still in force in 2005": imp["endyear"].fillna(2005),
        "No end year = ended at last news report": imp["endyear"].fillna(
            imp["ongoingasofyear"]).fillna(imp["start"]),
        "No end year = ended the year it began": imp["endyear"].fillna(imp["start"]),
    }
    fig, ax = figure(7.4, 3.9)
    colours = [RED, GOLD, BLUE]
    out = {}
    for (label, end), col in zip(rules.items(), colours):
        s = pd.Series([((imp["start"] <= y) & (end.clip(upper=2005) >= y)).sum() for y in years],
                      index=years)
        out[label] = s
        ax.plot(years, s, color=col, lw=2)
        ax.text(2005.6, s.iloc[-1], label.replace("No end year = ", ""), color=col, fontsize=8,
                va="center")
    ax.set_xlim(1945, 2019)
    ax.set_ylabel("Imposed cases in force")
    ax.set_title("How many sanctions were in force? It depends on how open cases are closed")
    n_missing = int(imp["endyear"].isna().sum())
    print(f"[active] imposed cases {len(imp)}, without end year {n_missing}")
    for label, s in out.items():
        print(f"[active] {label}: 1990 {s[1990]}, 2000 {s[2000]}, 2005 {s[2005]}, peak {s.max()} "
              f"in {s.idxmax()}")
    return save(fig, "ch10-ties-active", SRC_TIES + "; imposed cases only, active from the year "
                "of imposition to the end year.")


def fig_outcomes(t):
    coded = t[t["stage"] != "No outcome coded"]
    groups = [("Economic disputes", True), ("Political and security disputes", False)]
    rows, labels = [], []
    for gname, flag in groups:
        for stage in ["Threat stage", "After imposition"]:
            g = coded[(coded["economic"] == flag) & (coded["stage"] == stage)]
            share = g["outcome"].value_counts(normalize=True).reindex(ORDER, fill_value=0)
            rows.append(share.values)
            labels.append(f"{gname}\n{stage.lower()} (n = {len(g)})")
            print(f"[outcomes] {gname} / {stage}: n={len(g)} "
                  + ", ".join(f"{k} {v:.0%}" for k, v in share.items()))
    for stage in ["Threat stage", "After imposition"]:
        g = coded[coded["stage"] == stage]
        share = g["outcome"].value_counts(normalize=True).reindex(ORDER, fill_value=0)
        print(f"[outcomes] all / {stage}: n={len(g)} "
              + ", ".join(f"{k} {v:.0%}" for k, v in share.items()))
    rows = np.array(rows)
    colours = [TEAL, PALE_TEAL, GOLD, GRID, MUTED]
    fig, ax = figure(7.6, 3.7)
    ax.grid(False)
    y = np.array([3.2, 2.4, 1.0, 0.2])
    left = np.zeros(len(rows))
    for k, (name, col) in enumerate(zip(ORDER, colours)):
        ax.barh(y, rows[:, k], left=left, color=col, height=0.62)
        for yi, l, w in zip(y, left, rows[:, k]):
            if w >= 0.07:
                ax.text(l + w / 2, yi, f"{w:.0%}", ha="center", va="center", fontsize=8,
                        color="white" if col in (TEAL, MUTED) else INK)
        ax.text(left[0] + rows[0, k] / 2, 3.75, name.replace(" ", "\n", 1), ha="center",
                va="bottom", fontsize=7.5, color=INK)
        left += rows[:, k]
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=8)
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.3, 4.35)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0%}"))
    ax.set_xlabel("Share of cases with a coded outcome")
    ax.set_title("Targets give in fully at the threat stage far more often in economic disputes",
                 pad=6)
    return save(fig, "ch10-ties-outcomes", SRC_TIES + "; final outcome (codes 1–5 at the "
                "threat stage, 6–10 after imposition). Economic disputes: every coded issue is "
                "trade practices or economic reform.")


def senders_table(t, names):
    top = t["primarysender"].value_counts().head(6)
    print("[senders] primary senders:")
    for code, n in top.items():
        g = t[t["primarysender"] == code]
        print(f"  {names.get(int(code), code)}: {n} cases ({n / len(t):.1%}), imposed "
              f"{g['imposition'].mean():.0%}")
    tg = t["targetstate"].value_counts().head(8)
    print("[senders] targets:", {names.get(int(k), k): int(v) for k, v in tg.items()})
    us = t[t["primarysender"] == 2]
    print(f"[senders] US cases economic-only share {us['economic'].mean():.0%}; all cases "
          f"{t['economic'].mean():.0%}; institution-involved {t['institution'].eq(1).mean():.0%}")
    usdec = t.groupby(t["startyear"] // 10 * 10).apply(lambda g: (g["primarysender"] == 2).mean())
    print("[senders] US share by decade:", usdec.round(2).to_dict())


def load_imts():
    d = pd.read_csv(fetch(IMTS_URL, "imts_exports_russia_neighbours.csv", headers=IMTS_HDR))
    d = d[["COUNTRY", "COUNTERPART_COUNTRY", "TIME_PERIOD", "OBS_VALUE"]]
    d = d.drop_duplicates(["COUNTRY", "COUNTERPART_COUNTRY", "TIME_PERIOD"])
    d["value"] = d["OBS_VALUE"].astype(float) / 1e9
    return d.pivot_table(index="TIME_PERIOD", columns=["COUNTRY", "COUNTERPART_COUNTRY"],
                         values="value")


def fig_russia(x):
    yrs = range(2012, 2026)
    eu = x.xs("RUS", axis=1, level=1)[EU27].sum(axis=1, min_count=20).reindex(yrs)
    series = {"European Union (27)": (eu, BLUE), "China": (x[("CHN", "RUS")].reindex(yrs), RED),
              "Türkiye": (x[("TUR", "RUS")].reindex(yrs), GOLD),
              "United States": (x[("USA", "RUS")].reindex(yrs), MUTED)}
    fig, ax = figure(7.4, 3.9)
    for label, (s, col) in series.items():
        ax.plot(s.index, s.values, color=col, lw=2.2 if col in (BLUE, RED) else 1.6)
        ax.text(2025.3, s.iloc[-1], label, color=col, fontsize=8.5, va="center")
    for yr, label in [(2014, "Crimea"), (2022, "Full-scale\ninvasion")]:
        ax.axvline(yr, color=GRID, lw=1, zorder=0)
        ax.text(yr + 0.15, 168, label, fontsize=8, color=MUTED, va="top")
    ax.set_xlim(2012, 2027.6)
    ax.set_ylim(0, 170)
    ax.set_ylabel("Exports to Russia, US$ billion")
    ax.set_title("After 2022, China replaced Europe as Russia's supplier")
    for y in (2013, 2021, 2022, 2023, 2024, 2025):
        print(f"[russia] {y}: EU {eu[y]:.1f}, China {x[('CHN', 'RUS')][y]:.1f}, Türkiye "
              f"{x[('TUR', 'RUS')][y]:.1f}, US {x[('USA', 'RUS')][y]:.2f}, Germany "
              f"{x[('DEU', 'RUS')][y]:.1f}")
    return save(fig, "ch10-russia-suppliers", SRC_IMTS + "; as reported by the exporter. EU = "
                "sum of the 27 current member states.")


def spread(values, gap):
    """Label positions at least gap apart, in the order of the values."""
    order = np.argsort(values)
    pos = np.array(values, dtype=float)
    for k in range(1, len(order)):
        if pos[order[k]] - pos[order[k - 1]] < gap:
            pos[order[k]] = pos[order[k - 1]] + gap
    return pos


def fig_diversion(x):
    yrs = range(2015, 2026)
    neighbours = {"KGZ": "Kyrgyzstan", "ARM": "Armenia", "KAZ": "Kazakhstan", "GEO": "Georgia",
                  "UZB": "Uzbekistan"}
    fig, ax = figure(7.4, 3.9)
    cols = [RED, GOLD, BLUE, TEAL, MUTED]
    table, ends = {}, []
    for (code, name), col in zip(neighbours.items(), cols):
        eu = x.xs(code, axis=1, level=1)[EU27].sum(axis=1, min_count=20).reindex(yrs)
        idx = 100 * eu / eu[2021]
        table[name] = eu
        ax.plot(idx.index, idx.values, color=col, lw=2)
        ends.append(idx.iloc[-1])
    for (code, name), col, y in zip(neighbours.items(), cols, spread(ends, 40)):
        ax.text(2025.3, y, name, color=col, fontsize=8.5, va="center")
    ru = x.xs("RUS", axis=1, level=1)[EU27].sum(axis=1, min_count=20).reindex(yrs)
    ridx = 100 * ru / ru[2021]
    ax.plot(ridx.index, ridx.values, color=INK, lw=1.4, ls="--")
    ax.text(2025.3, ridx.iloc[-1], "Russia", color=INK, fontsize=8.5, va="center")
    ax.axhline(100, color=MUTED, lw=0.7)
    ax.axvline(2022, color=GRID, lw=1, zorder=0)
    ax.set_xlim(2015, 2026.9)
    ax.set_ylabel("EU exports, index 2021 = 100")
    ax.set_title("EU exports to Russia's neighbours jumped as exports to Russia collapsed")
    print("[diversion] EU exports, US$ bn:")
    for name, s in table.items():
        print(f"  {name}: 2021 {s[2021]:.2f}, 2022 {s[2022]:.2f}, 2023 {s[2023]:.2f}, 2024 "
              f"{s[2024]:.2f}, 2025 {s[2025]:.2f}; 2023/2021 x{s[2023] / s[2021]:.1f}")
    print(f"  Russia: 2021 {ru[2021]:.1f}, 2023 {ru[2023]:.1f}, 2025 {ru[2025]:.1f}")
    five = sum(table.values())
    print(f"  five neighbours together: 2021 {five[2021]:.1f}, 2023 {five[2023]:.1f}, 2025 "
          f"{five[2025]:.1f}; gain 2021-23 {five[2023] - five[2021]:.1f} vs loss to Russia "
          f"{ru[2021] - ru[2023]:.1f} ({(five[2023] - five[2021]) / (ru[2021] - ru[2023]):.0%})")
    for code in ["KGZ", "ARM", "KAZ"]:
        print(f"  Germany->{code}: 2021 {x[('DEU', code)][2021]:.3f}, 2023 "
              f"{x[('DEU', code)][2023]:.3f}, 2025 {x[('DEU', code)][2025]:.3f}")
    for code in ["KGZ", "ARM", "KAZ"]:
        print(f"  China->{code}: 2021 {x[('CHN', code)][2021]:.2f}, 2023 "
              f"{x[('CHN', code)][2023]:.2f}")
    return save(fig, "ch10-diversion", SRC_IMTS + "; EU = sum of the 27 current member states, "
                "as reported by each exporter.")


def main():
    t = load_ties()
    names = cow_names()
    senders_table(t, names)
    x = load_imts()
    return [fig_cases(t), fig_active(t), fig_outcomes(t), fig_russia(x), fig_diversion(x)]


if __name__ == "__main__":
    main()
