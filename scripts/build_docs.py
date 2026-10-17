"""Assemble docs/ — the GitHub Pages site that serves the session decks.

Run after rendering the decks:

    scripts/render_slides.sh
    python3 scripts/build_docs.py

Then, once, in the repository on GitHub: Settings -> Pages -> Deploy from a branch -> main /docs.

Each deck is self-contained (`embed-resources: true`), so copying the file is the whole deployment.
"""

import html
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REPO_URL = "https://github.com/warint/geopolitics-geoeconomics"

KINDS = [("Pre-Session", "pre-session", "Before class"),
         ("Lecture", "lecture", "Lecture"),
         ("Practice", "practice", "Practice round")]


def session_title(folder: Path) -> str:
    """The first heading of the session README, without the 'Session NN — ' prefix."""
    readme = folder / "README.md"
    if readme.exists():
        for line in readme.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return re.sub(r"^#\s*Session\s*\d+\s*[—-]\s*", "", line).strip()
    return folder.name


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    for old in DOCS.glob("session-*.html"):
        old.unlink()

    rows = []
    for folder in sorted(p for p in ROOT.iterdir() if p.is_dir() and re.match(r"\d\d-", p.name)):
        num = folder.name[:2]
        links = []
        for suffix, slug, label in KINDS:
            src = next(folder.glob(f"*/INTE60019A-S{num}-{suffix}.html"), None)
            if src is None:
                continue
            dest = f"session-{num}-{slug}.html"
            shutil.copy2(src, DOCS / dest)
            links.append(f'<a href="{dest}">{label}</a>')
        # Session 12 has a single deck at the folder root.
        for src in sorted(folder.glob(f"INTE60019A-S{num}-*.html")):
            dest = f"session-{num}-{src.stem.split('-')[-1].lower()}.html"
            shutil.copy2(src, DOCS / dest)
            links.append(f'<a href="{dest}">{src.stem.split("-")[-1]}</a>')
        if (DOCS / "book" / f"session-{num}.html").exists():
            links.append(f'<a href="book/session-{num}.html">Book chapter</a>')
        if links:
            rows.append(
                f"<tr><td class='n'>{num}</td><td>{html.escape(session_title(folder))}</td>"
                f"<td>{' · '.join(links)}</td></tr>")

    (DOCS / ".nojekyll").write_text("")
    (DOCS / "index.html").write_text(PAGE.format(rows="\n".join(rows), repo=REPO_URL),
                                     encoding="utf-8")
    print(f"docs/: {len(rows)} sessions, {len(list(DOCS.glob('session-*.html')))} decks")


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Geopolitical Risks and International Business</title>
<style>
  :root {{ --paper:#F7F4ED; --ink:#222; --muted:#6B6B67; --red:#E3120B; --rule:#D8D3C8; --link:#356B8C; }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --paper:#1b1a18; --ink:#ecebe6; --muted:#a6a39b; --rule:#3a3833; --link:#8fbbd6; }}
  }}
  body {{ background:var(--paper); color:var(--ink); margin:0;
         font:17px/1.5 'Helvetica Neue', Inter, system-ui, -apple-system, 'Segoe UI', sans-serif; }}
  main {{ max-width:960px; margin:0 auto; padding:48px 16px; }}
  h1 {{ font-size:2rem; margin:0 0 .3em; }}
  h1::before {{ content:""; display:block; width:56px; height:6px; background:var(--red); margin-bottom:14px; }}
  .sub {{ color:var(--muted); margin:0 0 1.2em; }}
  .book {{ border-left:3px solid var(--red); padding:.2em 0 .2em .9em; margin:0 0 2em; }}
  table {{ width:100%; border-collapse:collapse; border-top:2px solid var(--ink); }}
  td {{ padding:10px 8px; border-bottom:1px solid var(--rule); vertical-align:top; }}
  td.n {{ font-weight:700; color:var(--red); width:2.5em; font-variant-numeric:tabular-nums; }}
  a {{ color:var(--link); }}
  footer {{ margin-top:2.5em; color:var(--muted); font-size:.9rem; }}
  @media (max-width:600px) {{ td {{ display:block; border:none; padding:2px 0; }} tr {{ display:block; border-bottom:1px solid var(--rule); padding:10px 0; }} }}
</style>
</head>
<body>
<main>
<h1>Geopolitical Risks and International Business</h1>
<p class="sub">INTE 60019A · HEC Montréal · Thierry Warin, PhD — every deck of the course, in your browser.
Press <b>F</b> for full screen, <b>S</b> for speaker notes, <b>Esc</b> for the overview.</p>
<p class="book"><a href="book/"><b>The book: <i>Geopolitical Risks and International Business</i></b></a> —
twelve chapters, one for each session, written to be read on their own. Searchable, with a
<a href="book/Geopolitical-Risks-and-International-Business.pdf">PDF</a>.</p>
<table>
{rows}
</table>
<footer>Sources, data instructions and assessment briefs: <a href="{repo}">the course repository</a>.
Teaching materials CC BY-NC 4.0.</footer>
</main>
</body>
</html>
"""

if __name__ == "__main__":
    main()
