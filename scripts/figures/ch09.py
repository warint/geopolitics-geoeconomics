"""Figures and numbers for Chapter 9, Economic diplomacy.

Sources, downloaded at source into .data-cache/:
- Lowy Institute, Global Diplomacy Index, post-level data (sheets 2023 and 2017)
  (https://globaldiplomacyindex.lowyinstitute.org/downloads/DataDownload.xlsx)
- IMF, International Merchandise Trade Statistics (IMTS), exports of goods FOB in US dollars
  (XG_FOB_USD), annual, six reporters x all partners, via the IMF SDMX 3.0 API
- World Bank, WDI, GDP in current US dollars (NY.GDP.MKTP.CD), bulk CSV
"""

import io
import zipfile

import numpy as np
import pandas as pd

from style import BLUE, GOLD, GRID, MUTED, PALE_BLUE, RED, TEAL, fetch, figure, save

LOWY_URL = "https://globaldiplomacyindex.lowyinstitute.org/downloads/DataDownload.xlsx"
SENDERS = {"CAN": "Canada", "USA": "United States", "CHN": "China", "JPN": "Japan",
           "DEU": "Germany", "AUS": "Australia"}
IMTS_URL = ("https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/IMTS/%2B/"
            + "+".join(SENDERS) + ".XG_FOB_USD.*.A")
WDI_URL = "https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=csv"
YEAR = 2023

SENDER_2017 = {"Brunei Darussalam": "Brunei", "Czech Republic": "Czechia",
               "Korea Democratic People's Republic of (North Korea)": "North Korea",
               "Korea Republic of (South Korea)": "South Korea",
               "Lao People's Democratic Republic": "Laos", "Russian Federation": "Russia",
               "Slovak Republic": "Slovakia", "Turkey": "Türkiye"}

# Lowy host names that do not match WDI country names -> ISO3 (None: no ISO3 / not a state).
HOST_FIX = {"Bahamas": "BHS", "Bermuda (British overseas territory)": "BMU", "Brunei": "BRN",
            "Brussels": "BEL", "Cape Verde": "CPV", "Congo": "COG", "Cook Islands": "COK",
            "Cote D'Ivoire": "CIV", "Cote d'Ivoire": "CIV", "Democratic The Congo": "COD",
            "Democratic the Congo": "COD", "Dominica Republic": "DOM", "Egypt": "EGY",
            "French Guiana": "GUF", "Gambia": "GMB", "Guam (US territory)": "GUM", "Iran": "IRN",
            "Kosovo*": "XKX", "Kyrgyzstan": "KGZ", "Laos": "LAO",
            "Micronesia Federated States of": "FSM", "Nauru": "NRU",
            "New Caledonia (France)": "NCL", "New Caledonia (French Territory)": "NCL",
            "New Caledonia (French territory)": "NCL", "Nigaragua": "NIC", "Niue": "NIU",
            "North Korea": "PRK", "Palestinian Territories*": "PSE", "Portual": "PRT",
            "Puerto Rico (US territory)": "PRI", "Russia": "RUS", "Saint Kitts and Nevis": "KNA",
            "Saint Lucia": "LCA", "Saint Vincent and the Grenadines": "VCT", "Slovakia": "SVK",
            "Somalia": "SOM", "South Korea": "KOR", "Syria": "SYR", "Taiwan": "TWN", "Taiwan*": "TWN",
            "Türkiye": "TUR", "Vatican City": "VAT", "Venezuela": "VEN", "Vietnam": "VNM",
            "Yemen": "YEM", "Abkhazia*": None, "Jerusalem*": None, "Northern Cyprus*": None,
            "Somaliland*": None, "South Ossetia*": None}

BILATERAL = ["Embassy / High Commission", "Consulate / Consulate-General"]


def load_lowy():
    path = fetch(LOWY_URL, "lowy_gdi_DataDownload.xlsx")
    a = pd.read_excel(path, sheet_name="2023")
    b = pd.read_excel(path, sheet_name="2017")
    for x in (a, b):
        x["COUNTRY"] = x["COUNTRY"].astype(str).str.strip()
        x["POST COUNTRY"] = x["POST COUNTRY"].astype(str).str.strip()
    b["COUNTRY"] = b["COUNTRY"].replace(SENDER_2017)
    return a, b


def load_gdp():
    z = zipfile.ZipFile(fetch(WDI_URL, "wdi_NY.GDP.MKTP.CD.zip"))
    name = [n for n in z.namelist() if n.startswith("API_")][0]
    g = pd.read_csv(io.BytesIO(z.read(name)), skiprows=4)
    meta = [n for n in z.namelist() if n.startswith("Metadata_Country")][0]
    m = pd.read_csv(io.BytesIO(z.read(meta)))
    countries = set(m.loc[m["Region"].notna(), "Country Code"])  # drop aggregates
    g = g[g["Country Code"].isin(countries)]
    return g.set_index("Country Code")[str(YEAR)], dict(zip(g["Country Name"], g["Country Code"])), countries


def load_imts():
    t = pd.read_csv(fetch(IMTS_URL, "imts_xg_fob_6senders.csv",
                          headers={"Accept": "application/vnd.sdmx.data+csv;version=2.0.0",
                                   "User-Agent": "Mozilla/5.0 (book figures; research)"}),
                    usecols=["COUNTRY", "COUNTERPART_COUNTRY", "TIME_PERIOD", "OBS_VALUE"])
    t = t[t["TIME_PERIOD"] == YEAR]
    t["COUNTERPART_COUNTRY"] = t["COUNTERPART_COUNTRY"].replace({"KOS": "XKX"})
    return t.pivot_table(index="COUNTERPART_COUNTRY", columns="COUNTRY", values="OBS_VALUE", aggfunc="sum")


def host_iso(a, name2iso):
    def f(n):
        if n in HOST_FIX:
            return HOST_FIX[n]
        if n.startswith("Cura"):
            return "CUW"
        return name2iso.get(n)
    iso = a["POST COUNTRY"].map(f)
    unmatched = sorted(set(a.loc[iso.isna(), "POST COUNTRY"]) - {k for k, v in HOST_FIX.items() if v is None})
    print("ch09 Lowy host names without ISO3 after concordance:", unmatched)
    return iso


def fig_networks(a, b):
    t23, t17 = a.groupby("COUNTRY").size(), b.groupby("COUNTRY").size()
    top = t23.sort_values(ascending=False).head(15)
    print("ch09 total posts 2023:", len(a), "senders:", a["COUNTRY"].nunique(), "; 2017:", len(b),
          "senders:", b["COUNTRY"].nunique())
    print("ch09 top 2023:", top.to_dict())
    print("ch09 same senders 2017:", {k: int(t17.get(k, 0)) for k in top.index})
    both = t23.index.intersection(t17.index)
    ch = (t23[both] - t17[both]).sort_values()
    print("ch09 senders in both years:", len(both), "net change all:", int(ch.sum()),
          "; grew:", int((ch > 0).sum()), "shrank:", int((ch < 0).sum()), "unchanged:", int((ch == 0).sum()))
    print("ch09 largest falls:", ch.head(6).to_dict(), "largest rises:", ch.tail(6).to_dict())
    fig, ax = figure(7.2, 5.0)
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", color=GRID)
    y = np.arange(len(top))[::-1]
    for yi, k in zip(y, top.index):
        v17, v23 = t17.get(k, np.nan), top[k]
        ax.plot([v17, v23], [yi, yi], color=GRID, lw=3, solid_capstyle="round", zorder=1)
        ax.plot(v17, yi, "o", color=MUTED, ms=6, zorder=2)
        ax.plot(v23, yi, "o", color=RED if v23 >= v17 else BLUE, ms=7, zorder=3)
        ax.text(max(v17, v23) + 3, yi, f"{v23}", va="center", fontsize=8)
    ax.set_yticks(y)
    ax.set_yticklabels(top.index, fontsize=8.5)
    ax.set_xlabel("Diplomatic posts abroad (embassies, consulates, missions, other)")
    ax.text(180, y[0] + 0.9, "● 2017", color=MUTED, fontsize=8.5)
    ax.text(205, y[0] + 0.9, "● 2023, grew", color=RED, fontsize=8.5)
    ax.text(250, y[0] + 0.9, "● 2023, shrank", color=BLUE, fontsize=8.5)
    ax.set_ylim(-0.8, len(top) + 0.3)
    ax.set_title("China passed the United States as the largest diplomatic network")
    return save(fig, "ch09-networks", "Lowy Institute, Global Diplomacy Index, post-level data, 2017 and 2023 sheets")


def fig_change(a, b):
    t23, t17 = a.groupby("COUNTRY").size(), b.groupby("COUNTRY").size()
    both = t23.index.intersection(t17.index)
    ch = (t23[both] - t17[both]).sort_values()
    sel = pd.concat([ch.head(8), ch.tail(8)])
    fig, ax = figure(7.2, 4.6)
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", color=GRID)
    y = np.arange(len(sel))
    ax.barh(y, sel.values, color=[BLUE if v < 0 else RED for v in sel.values], height=0.65)
    for yi, v in zip(y, sel.values):
        ax.text(v + (0.6 if v > 0 else -0.6), yi, f"{v:+d}", va="center", ha="left" if v > 0 else "right",
                fontsize=8)
    ax.set_yticks(y)
    ax.set_yticklabels(sel.index, fontsize=8.5)
    ax.axvline(0, color="#222222", lw=0.8)
    ax.set_xlim(sel.min() - 6, sel.max() + 6)
    ax.set_xlabel("Change in the number of posts abroad, 2017 to 2023")
    ax.set_title("Spain, France and Brazil cut their networks; Türkiye, Ireland and the UK grew")
    return save(fig, "ch09-network-change",
                "Lowy Institute, Global Diplomacy Index, post-level data, 2017 and 2023 sheets; "
                f"the eight largest falls and rises among the {len(both)} senders in both")


def fig_composition(a, b):
    top = a.groupby("COUNTRY").size().sort_values(ascending=False).head(10).index
    c = a[a["COUNTRY"].isin(top)].groupby(["COUNTRY", "TYPE OF POST"]).size().unstack(fill_value=0)
    c = c.loc[top]
    c17 = b[b["COUNTRY"].isin(top)].groupby(["COUNTRY", "TYPE OF POST"]).size().unstack(fill_value=0)
    print("ch09 composition 2023:")
    print(c.to_string())
    print("ch09 composition 2017:")
    print(c17.reindex(top).to_string())
    print("ch09 all senders 2023 types:", a["TYPE OF POST"].value_counts().to_dict())
    order = ["Embassy / High Commission", "Consulate / Consulate-General", "Permanent Mission", "Other"]
    cols = [BLUE, RED, GOLD, "#BDB8AD"]
    labs = ["Embassies and high commissions", "Consulates", "Permanent missions", "Other"]
    fig, ax = figure(7.2, 4.4)
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", color=GRID)
    y = np.arange(len(top))[::-1]
    left = np.zeros(len(top))
    for o, col, lab in zip(order, cols, labs):
        v = c[o].values
        ax.barh(y, v, left=left, color=col, height=0.65, label=lab)
        if o in order[:2]:
            for yi, l, vi in zip(y, left, v):
                ax.text(l + vi / 2, yi, str(vi), ha="center", va="center", color="white", fontsize=7.5)
        left += v
    ax.set_yticks(y)
    ax.set_yticklabels(top, fontsize=8.5)
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.0), fontsize=7.5, ncol=4, handlelength=1.2,
              columnspacing=1.0)
    ax.set_xlabel("Posts, 2023")
    ax.set_title("China's lead rests on its consulates", pad=24)
    return save(fig, "ch09-composition", "Lowy Institute, Global Diplomacy Index, post-level data, 2023 sheet")


def ols(y, X):
    X = np.column_stack([np.ones(len(y))] + list(X))
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    r2 = 1 - (resid ** 2).sum() / ((y - y.mean()) ** 2).sum()
    n, k = X.shape
    s2 = (resid ** 2).sum() / (n - k)
    cov = s2 * np.linalg.inv(X.T @ X)
    return beta, np.sqrt(np.diag(cov)), r2


def ppml(y, X, iters=200):
    """Poisson pseudo-maximum likelihood (Newton steps with step-halving); robust standard errors."""
    X = np.column_stack([np.ones(len(y))] + list(X))
    beta, *_ = np.linalg.lstsq(X, np.log(y + y[y > 0].min()), rcond=None)

    def loglik(b):
        eta = X @ b
        return (y * eta - np.exp(eta)).sum()

    ll = loglik(beta)
    for _ in range(iters):
        mu = np.exp(X @ beta)
        grad = X.T @ (y - mu)
        hess = X.T @ (mu[:, None] * X)
        step = np.linalg.solve(hess, grad)
        t = 1.0
        while loglik(beta + t * step) < ll and t > 1e-8:
            t /= 2
        beta = beta + t * step
        new_ll = loglik(beta)
        if abs(new_ll - ll) < 1e-12 * max(1, abs(ll)):
            ll = new_ll
            break
        ll = new_ll
    mu = np.exp(X @ beta)
    bread = np.linalg.inv(X.T @ (mu[:, None] * X))
    meat = X.T @ (((y - mu) ** 2)[:, None] * X)
    se = np.sqrt(np.diag(bread @ meat @ bread))
    return beta, se


def pair_data(a, gdp, name2iso, countries, imts):
    a = a.copy()
    a["iso"] = host_iso(a, name2iso)
    rows = {}
    for iso, name in SENDERS.items():
        p = a[(a["COUNTRY"] == name) & a["TYPE OF POST"].isin(BILATERAL)]
        emb = p[p["TYPE OF POST"] == BILATERAL[0]].groupby("iso").size()
        con = p[p["TYPE OF POST"] == BILATERAL[1]].groupby("iso").size()
        partners = [c for c in countries if c != iso]
        df = pd.DataFrame(index=partners)
        df["emb"] = emb.reindex(df.index).fillna(0)
        df["con"] = con.reindex(df.index).fillna(0)
        df["posts"] = df["emb"] + df["con"]
        df["x"] = imts[iso].reindex(df.index) if iso in imts else np.nan
        df["gdp"] = gdp.reindex(df.index)
        rows[iso] = df
    return rows


def regressions(rows):
    """Posts-exports association for six senders under four specifications (no distance or other
    gravity controls: these are illustrations of fragility, not estimates of an effect)."""
    out = []
    for iso, df in rows.items():
        d = df.dropna(subset=["x", "gdp"])
        d = d[d["gdp"] > 0]
        pos = d[(d["posts"] > 0) & (d["x"] > 0)]
        b1, se1, r21 = ols(np.log(pos["x"].values), [np.log(pos["posts"].values)])
        b2, se2, r22 = ols(np.log(pos["x"].values), [np.log(pos["gdp"].values), np.log(pos["posts"].values)])
        b2s, _, r2s = ols(np.log((pos["x"] / pos["gdp"]).values), [np.log(pos["posts"].values)])
        b3, se3, r23 = ols(np.log(d["x"].values), [np.log(d["gdp"].values), np.log1p(d["posts"].values)])
        b4, se4 = ppml(d["x"].values / 1e9, [np.log(d["gdp"].values), np.log1p(d["posts"].values)])
        out.append(dict(sender=SENDERS[iso], partners=len(d), no_post=int((d["posts"] == 0).sum()),
                        zero_trade=int((d["x"] <= 0).sum()), n_pos=len(pos),
                        naive=b1[1], naive_se=se1[1], naive_r2=r21,
                        gdp_ctrl=b2[2], gdp_ctrl_se=se2[2],
                        scaled=b2s[1], scaled_r2=r2s,
                        ols_all=b3[2], ols_all_se=se3[2], ppml_all=b4[2], ppml_all_se=se4[2]))
    R = pd.DataFrame(out).set_index("sender")
    pd.set_option("display.width", 220)
    print("ch09 posts-exports elasticities: naive = log X on log posts (partners with >=1 post); gdp_ctrl = adding "
          "log GDP; scaled = log(X/GDP) on log posts; ols_all / ppml_all = all partners, log GDP and log(1+posts):")
    print(R.round(2).to_string())
    return R


def fig_canada(df):
    d = df.dropna(subset=["x", "gdp"])
    d = d[d["gdp"] > 0].copy()
    d["bin"] = d["posts"].clip(upper=4).astype(int)
    d["share"] = d["x"] / d["gdp"] * 100
    med = d.groupby("bin").agg(n=("x", "size"), x=("x", "median"), share=("share", "median"),
                               gdp=("gdp", "median"))
    print("ch09 Canada partners:", len(d), "with no post:", int((d["posts"] == 0).sum()),
          "no post and positive exports:", int(((d["posts"] == 0) & (d["x"] > 0)).sum()),
          "exports to no-post partners, share of total to these partners:",
          round(d.loc[d["posts"] == 0, "x"].sum() / d["x"].sum(), 4))
    print("ch09 Canada medians by posts (0,1,2,3,4+):")
    print(med.to_string())
    print("ch09 Canada max posts:", d["posts"].idxmax(), int(d["posts"].max()))
    rng = np.random.default_rng(7)
    fig, axes = plt_subplots()
    for ax, col, lab, ttl in [(axes[0], "x", "Exports, US$ (log scale)", "Exports"),
                              (axes[1], "share", "Exports as % of partner GDP (log scale)",
                               "Exports scaled by partner GDP")]:
        dd = d[d[col] > 0]
        xj = dd["bin"] + rng.uniform(-0.18, 0.18, len(dd))
        ax.scatter(xj, dd[col], s=10, color=BLUE, alpha=0.45, lw=0)
        m = dd.groupby("bin")[col].median()
        for k, v in m.items():
            ax.plot([k - 0.3, k + 0.3], [v, v], color=RED, lw=2.4)
        ax.set_yscale("log")
        ax.set_xticks(range(5))
        ax.set_xticklabels(["0", "1", "2", "3", "4+"])
        ax.set_xlabel("Canadian embassies and consulates in the partner")
        ax.set_ylabel(lab)
        ax.set_title(ttl, fontsize=10, loc="left")
    axes[1].text(3.4, m.max() * 2.2, "median", color=RED, fontsize=8.5, ha="center")
    axes[0].text(-0.3, 1.5e10, f"{int((d['posts'] == 0).sum())} partners\nwith no post",
                 ha="left", va="bottom", fontsize=8, color=MUTED)
    fig.suptitle("Canada exports more where it keeps posts; scaled by size, much less so",
                 x=0.06, ha="left", fontweight="bold", fontsize=12, y=1.0)
    return save(fig, "ch09-canada-posts-exports",
                f"Lowy Institute, Global Diplomacy Index (2023 sheet); IMF IMTS, exports of goods FOB, {YEAR}; "
                f"World Bank WDI, GDP, {YEAR}")


def plt_subplots():
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.9))
    fig.add_artist(plt.Line2D([0.0, 0.07], [1.06, 1.06], transform=fig.transFigure,
                              color=RED, linewidth=4, solid_capstyle="butt"))
    fig.subplots_adjust(wspace=0.32)
    return fig, axes


def main():
    a, b = load_lowy()
    gdp, name2iso, countries = load_gdp()
    imts = load_imts()
    out = [fig_networks(a, b), fig_change(a, b), fig_composition(a, b)]
    rows = pair_data(a, gdp, name2iso, countries, imts)
    regressions(rows)
    print("ch09 Canada exports to the US, share of exports to the world:",
          round(imts.loc["USA", "CAN"] / imts.loc["G001", "CAN"], 3))
    out.append(fig_canada(rows["CAN"]))
    return out


if __name__ == "__main__":
    main()
