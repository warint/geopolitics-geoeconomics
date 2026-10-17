"""House style and helpers for the book's figures.

Every chapter's figures are drawn by scripts/figures/chNN.py, which import this module.
Raw data is downloaded at source into .data-cache/ (git-ignored, never committed); the figures
are written to assets/figures/ as PNG (and SVG), and those derived images are committed.

    .venv/bin/python scripts/figures/build_all.py          # every chapter
    .venv/bin/python scripts/figures/build_all.py 03 11    # some chapters
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import requests  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / ".data-cache"
OUT = ROOT / "assets" / "figures"

# The palette of slides/economist.scss and the book.
PAPER, INK, MUTED, GRID = "#F7F4ED", "#222222", "#6B6B67", "#D8D3C8"
RED, BLUE, TEAL, GOLD = "#E3120B", "#356B8C", "#2A8C82", "#D49A00"
PALE_RED, PALE_BLUE, PALE_TEAL = "#F7C9C6", "#C9DCE8", "#C6E2DE"
CYCLE = [RED, BLUE, TEAL, GOLD, MUTED, "#8C5A9E", "#5A8C3A"]

plt.rcParams.update({
    "figure.facecolor": PAPER, "axes.facecolor": PAPER, "savefig.facecolor": PAPER,
    "font.family": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 10, "axes.titlesize": 12, "axes.titleweight": "bold", "axes.titlelocation": "left",
    "axes.edgecolor": INK, "axes.labelcolor": INK, "text.color": INK,
    "xtick.color": INK, "ytick.color": INK,
    "axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False,
    "axes.grid": True, "axes.grid.axis": "y", "grid.color": GRID, "grid.linewidth": 0.8,
    "axes.prop_cycle": plt.cycler(color=CYCLE), "lines.linewidth": 1.8,
    "legend.frameon": False, "figure.dpi": 110, "savefig.dpi": 200, "savefig.bbox": "tight",
})


def fetch(url, name, headers=None):
    """Download url into .data-cache/name once; return the local path."""
    CACHE.mkdir(exist_ok=True)
    path = CACHE / name
    if not path.exists():
        r = requests.get(url, timeout=180,
                         headers=headers or {"User-Agent": "Mozilla/5.0 (book figures; research)"})
        r.raise_for_status()
        path.write_bytes(r.content)
    return path


def figure(width=7.2, height=3.9):
    """A new figure in the book's proportions, with the red rule above the title."""
    fig, ax = plt.subplots(figsize=(width, height))
    fig.add_artist(plt.Line2D([0.0, 0.07], [1.02, 1.02], transform=fig.transFigure,
                              color=RED, linewidth=4, solid_capstyle="butt"))
    return fig, ax


def save(fig, name, source):
    """Write assets/figures/<name>.png and .svg with a source line under the plot."""
    OUT.mkdir(parents=True, exist_ok=True)
    fig.text(0.0, -0.04, f"Source: {source}", fontsize=8, color=MUTED, ha="left", va="top",
             transform=fig.transFigure)
    for ext in ("png", "svg"):
        fig.savefig(OUT / f"{name}.{ext}")
    plt.close(fig)
    return OUT / f"{name}.png"
