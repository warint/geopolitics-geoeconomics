"""Figures and numbers for Chapter 8, Cyber geopolitics.

Sources, downloaded at source into .data-cache/:
- Dyadic Cyber Incident and Campaign Data (DCID) v2.0, Maness, Valeriano, Hedgecock, Macias & Jensen,
  Harvard Dataverse doi:10.7910/DVN/CQOMYV, file Master_DCID_2.0_Release_public_Sep2022 (original CSV)
- European Repository of Cyber Incidents (EuRepoC), Global Dataset of Cyber Incidents v1.3,
  Zenodo doi:10.5281/zenodo.14965395, file eurepoc_global_dataset_1_3.csv
"""

from collections import Counter

import numpy as np
import pandas as pd

from style import BLUE, GOLD, GRID, MUTED, PALE_BLUE, RED, TEAL, fetch, figure, save

DCID_URL = "https://dataverse.harvard.edu/api/access/datafile/6503190?format=original"
EUREPOC_URL = ("https://zenodo.org/api/records/14965395/files/"
               "eurepoc_global_dataset_1_3.csv/content")

COW = {2: "US", 365: "Russia", 369: "Ukraine", 372: "Georgia", 630: "Iran", 640: "Turkey",
       652: "Syria", 666: "Israel", 710: "China", 713: "Taiwan", 731: "N Korea", 732: "S Korea",
       740: "Japan", 750: "India", 770: "Pakistan", 816: "Vietnam"}
LONG = {"US": "United States", "N Korea": "North Korea", "S Korea": "South Korea"}


def load_dcid():
    d = pd.read_csv(fetch(DCID_URL, "dcid_v2_sep2022.csv"), encoding="latin-1")
    d["A"], d["B"] = d["StateA"].str.strip(), d["StateB"].str.strip()
    d["init"] = d["initiator"].map(COW)
    assert d["init"].notna().all()
    # Two rows name an initiator outside the dyad (313: N Korea in China-S Korea; 335: Pakistan in
    # China-India); for those the target is taken to be State B (S Korea, India).
    odd = ~((d["init"] == d["A"]) | (d["init"] == d["B"]))
    print("ch08 DCID rows with initiator outside the dyad:",
          d.loc[odd, ["Cyberincidentnum", "A", "B", "init"]].values.tolist())
    d["target"] = np.where(d["init"] == d["B"], d["A"], d["B"])
    d["start"] = pd.to_datetime(d["interactionstartdate"], format="%m/%d/%Y", errors="coerce")
    d["year"] = d["start"].dt.year
    return d


def load_eurepoc():
    e = pd.read_csv(fetch(EUREPOC_URL, "eurepoc_global_dataset_1_3.csv"))
    c = e["initiator_category"].fillna("")
    state_aff = c.str.contains("State affiliated") | (";" + c + ";").str.contains(";State;")
    nonstate = c.str.contains("Non-state-group") | c.str.contains("Individual hacker")
    e["who"] = np.select([state_aff, nonstate], ["state", "nonstate"], "unattributed")
    e["state_only"] = (";" + c + ";").str.contains(";State;")
    e["year"] = pd.to_datetime(e["start_date"], format="%d.%m.%Y", errors="coerce").dt.year
    return e


def fig_records(d, e):
    years = range(2000, 2025)
    t = e.dropna(subset=["year"]).groupby(["year", "who"]).size().unstack(fill_value=0).reindex(years, fill_value=0)
    dc = d.groupby("year").size().reindex(range(2000, 2021), fill_value=0)
    print("ch08 EuRepoC rows:", len(e), "no start date:", int(e["year"].isna().sum()),
          "state or state-affiliated:", int((e["who"] == "state").sum()),
          "state only:", int(e["state_only"].sum()),
          "non-state:", int((e["who"] == "nonstate").sum()),
          "not attributed/unknown:", int((e["who"] == "unattributed").sum()))
    for p, (a, b) in {"2000-2010": (2000, 2010), "2011-2020": (2011, 2020), "2021-2024": (2021, 2024)}.items():
        s = t.loc[a:b]
        print(f"ch08 EuRepoC {p}: total {int(s.values.sum())}, state share "
              f"{s['state'].sum() / s.values.sum():.0%}")
    print("ch08 EuRepoC 2023, 2024 totals:", int(t.loc[2023].sum()), int(t.loc[2024].sum()),
          "; 2020:", int(t.loc[2020].sum()))
    print("ch08 DCID per year max:", int(dc.max()), dc.idxmax(), "; DCID rows:", len(d),
          "start dates", d["start"].min().date(), "-", d["start"].max().date())
    ov = e[(e["year"] >= 2000) & (e["year"] <= 2020)]
    print("ch08 EuRepoC 2000-2020 total:", len(ov), "state or affiliated:", int((ov["who"] == "state").sum()))
    fig, ax = figure(7.4, 4.1)
    x = np.array(list(years))
    bottom = np.zeros(len(x))
    for key, col, lab in [("state", RED, "Attributed to a state or state-affiliated actor"),
                          ("nonstate", GOLD, "Non-state groups and individual hackers"),
                          ("unattributed", "#BDB8AD", "Not attributed or unknown")]:
        ax.bar(x, t[key].values, bottom=bottom, color=col, width=0.8, label=lab)
        bottom += t[key].values
    ax.plot(dc.index, dc.values, color=BLUE, lw=2.2, marker="o", ms=3)
    ax.annotate("DCID: incidents between\nrival states (2000–2020)", (2014, dc.loc[2014]), xytext=(-150, 60),
                textcoords="offset points", color=BLUE, fontsize=8.5, fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.8))
    ax.legend(loc="upper left", fontsize=8, title="EuRepoC v1.3, all incidents, by initiator",
              title_fontsize=8.5, alignment="left")
    ax.set_ylabel("Incidents by year of start")
    ax.set_xlim(1999.4, 2024.6)
    ax.set_title("Who counts as an attacker decides how much cyber conflict there is")
    return save(fig, "ch08-records-by-year",
                "EuRepoC Global Dataset of Cyber Incidents v1.3 (92 incidents without a start date omitted); "
                "DCID v2.0 (September 2022 release)")


def fig_severity(d):
    s = d["severity"].value_counts().reindex(range(0, 11), fill_value=0)
    print("ch08 DCID severity counts:", s.to_dict(), "share 2-4:", round(s.loc[2:4].sum() / s.sum(), 3),
          "share >=5:", round(s.loc[5:].sum() / s.sum(), 3))
    print("ch08 DCID severity 6 incidents:", d.loc[d["severity"] == 6, ["Name", "init", "target", "year"]].values.tolist())
    labels = {0: "No activity", 1: "Probing", 2: "Harassment,\ndisruption", 3: "Theft from\none network",
              4: "Widespread\nintrusion", 5: "Attempted\ndestruction", 6: "Widespread\ndestruction",
              7: "Minimal\ndeath", 8: "Economic\ndisruption", 9: "Infrastructure\ndestruction",
              10: "Massive\ndeath"}
    fig, ax = figure(7.6, 4.0)
    cols = [BLUE if k <= 4 else RED for k in s.index]
    ax.bar(s.index, s.values, color=cols, width=0.7)
    for k, v in s.items():
        ax.text(k, v + 3, str(v), ha="center", fontsize=8.5, color="#222222" if v else MUTED)
    ax.axvspan(6.5, 10.5, color=GRID, alpha=0.35, lw=0)
    ax.text(8.5, 120, "Nothing coded\nabove 6 in\ntwo decades", ha="center", fontsize=9, color=MUTED)
    ax.set_xticks(list(s.index))
    ax.set_xticklabels([f"{k}\n{labels[k]}" for k in s.index], fontsize=7)
    ax.set_ylabel("Incidents, 2000–2020")
    ax.set_xlim(-0.6, 10.6)
    ax.set_title("Nine incidents in ten sit between 2 and 4 on a 10-point scale")
    return save(fig, "ch08-dcid-severity",
                "DCID v2.0 (September 2022 release), severity of 433 incidents; scale labels from Codebook 2.0")


def fig_dyads(d):
    dy = d.groupby(["init", "target"]).size().sort_values(ascending=False)
    n = len(d)
    print("ch08 DCID directed dyads:", len(dy), "top 5 share:", round(dy.head(5).sum() / n, 3),
          "top 10 share:", round(dy.head(10).sum() / n, 3))
    print("ch08 DCID top dyads:", [(f"{a}->{b}", int(v)) for (a, b), v in dy.head(12).items()])
    ini = d["init"].value_counts()
    print("ch08 DCID initiators:", ini.to_dict(), "big four share:",
          round(ini[["China", "Russia", "Iran", "N Korea"]].sum() / n, 3))
    tg = d["target"].value_counts()
    print("ch08 DCID targets:", tg.head(8).to_dict(), "US as target share:", round(tg["US"] / n, 3))
    top = dy.head(12)[::-1]
    fig, ax = figure(7.2, 4.6)
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", color=GRID)
    colors = {"China": RED, "Russia": BLUE, "Iran": TEAL, "N Korea": GOLD}
    labels = [f"{LONG.get(a, a)} → {LONG.get(b, b)}" for a, b in top.index]
    ax.barh(range(len(top)), top.values, color=[colors.get(a, MUTED) for a, _ in top.index], height=0.65)
    for i, v in enumerate(top.values):
        ax.text(v + 0.8, i, str(v), va="center", fontsize=8.5)
    ax.set_yticks(range(len(top)))
    ax.set_yticklabels(labels, fontsize=8.5)
    ax.set_xlabel("Incidents, 2000–2020 (initiator → target)")
    ax.set_title("Cyber conflict between rivals runs through a handful of old rivalries")
    return save(fig, "ch08-dcid-dyads", "DCID v2.0 (September 2022 release), 433 incidents between rival states")


EU_NAMES = {"China": "China", "Russia": "Russia", "Iran, Islamic Republic of": "Iran",
            "Korea, Democratic People's Republic of": "N Korea", "United States": "US"}


def fig_initiators(d, e):
    st = e[e["who"] == "state"]
    cnt = Counter()
    for s in st["initiator_country"].dropna():
        cnt.update({EU_NAMES.get(x, x) for x in s.split(";")})
    eu = pd.Series(cnt) / len(st)
    dc = d["init"].value_counts() / len(d)
    keys = ["China", "Russia", "Iran", "N Korea", "US"]
    print("ch08 initiator shares DCID:", {k: round(dc.get(k, 0), 3) for k in keys})
    print("ch08 initiator shares EuRepoC state/affiliated (incidents naming each):",
          {k: round(eu.get(k, 0), 3) for k in keys}, "n =", len(st))
    four = st["initiator_country"].fillna("").apply(
        lambda s: any(EU_NAMES.get(x) in ("China", "Russia", "Iran", "N Korea") for x in s.split(";")))
    print("ch08 EuRepoC state/affiliated naming at least one of the big four:", round(four.mean(), 3))
    fig, ax = figure(7.2, 3.8)
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", color=GRID)
    y = np.arange(len(keys))[::-1]
    ax.barh(y + 0.19, [dc.get(k, 0) for k in keys], height=0.36, color=BLUE)
    ax.barh(y - 0.19, [eu.get(k, 0) for k in keys], height=0.36, color=RED)
    for yi, k in zip(y, keys):
        ax.text(dc.get(k, 0) + 0.005, yi + 0.19, f"{dc.get(k, 0):.0%}", va="center", fontsize=8, color=BLUE)
        ax.text(eu.get(k, 0) + 0.005, yi - 0.19, f"{eu.get(k, 0):.0%}", va="center", fontsize=8, color=RED)
    ax.set_yticks(y)
    ax.set_yticklabels([LONG.get(k, k) for k in keys])
    ax.set_xlim(0, 0.33)
    ax.xaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    ax.text(0.12, 0.19, "DCID, rival states, 2000–2020", color=BLUE, fontsize=8.5, fontweight="bold",
            va="center")
    ax.text(0.12, -0.19, "EuRepoC, state or state-affiliated, 2000–2024", color=RED, fontsize=8.5,
            fontweight="bold", va="center")
    ax.set_xlabel("Share of incidents naming the state as initiator")
    ax.set_title("Two datasets, the same four principal initiators")
    return save(fig, "ch08-initiators",
                "DCID v2.0 (433 incidents); EuRepoC v1.3 (1,014 incidents attributed to a state or "
                "state-affiliated actor; an incident may name several states)")


def tables(d):
    tt = pd.crosstab(d["targettype"], d["cyber_objective"], margins=True)
    print("ch08 DCID target type x objective (1 private, 2 gov non-mil, 3 military; "
          "objective 1 disruption, 2 short espionage, 3 long espionage, 4 degrade):")
    print(tt.to_string())
    per = pd.cut(d["year"], [1999, 2009, 2014, 2021], labels=["2000-09", "2010-14", "2015-21"])
    meth = d["method"].astype(float).apply(lambda m: "vandalism" if m == 1 else "DDoS" if m == 2
                                           else "intrusion" if m < 4 else "infiltration")
    print("ch08 DCID method by period:")
    print(pd.crosstab(meth, per, margins=True).to_string())
    print("ch08 DCID ransomware incidents:", int(d["Ransomware"].sum()))
    named = d[d["Name"].str.contains("Petya|WannaCry|Shamoon|OPM Hack|Sony Hack", na=False)]
    print("ch08 DCID named cases (name, initiator, target, severity, target type):",
          named[["Name", "init", "target", "severity", "targettype"]].values.tolist())


def receivers(e):
    cnt = Counter()
    for s in e["receiver_category"].dropna():
        cnt.update(set(s.split(";")))
    print("ch08 EuRepoC receiver categories (incidents):",
          [(k[:30], v) for k, v in cnt.most_common(6)])
    corp = e["receiver_category"].fillna("").str.contains("Corporate|Critical infrastructure")
    print("ch08 EuRepoC incidents with a corporate or critical-infrastructure receiver:",
          int(corp.sum()), round(corp.mean(), 3))
    st = e[e["who"] == "state"]
    c2 = st["receiver_category"].fillna("").str.contains("Corporate|Critical infrastructure")
    print("ch08 ... among state/affiliated:", int(c2.sum()), round(c2.mean(), 3))


def main():
    d, e = load_dcid(), load_eurepoc()
    out = [fig_records(d, e), fig_severity(d), fig_dyads(d), fig_initiators(d, e)]
    tables(d)
    receivers(e)
    return out


if __name__ == "__main__":
    main()
