#!/usr/bin/env bash
# Rebuild the book: assemble book/ from the session chapters, then render it
# (HTML and PDF) into docs/book/, where GitHub Pages serves it.
# Usage: scripts/render_book.sh [--html-only]
#
# Nothing in book/ is authored — scripts/build_book.py regenerates it from each
# session's chapter.md and chapter.bib, so edit those and run this.

set -euo pipefail
cd "$(dirname "$0")/.."

command -v quarto >/dev/null 2>&1 || { echo "quarto not found — https://quarto.org/docs/download/" >&2; exit 1; }

echo "=== assembling book/ from the sessions"
python3 scripts/build_book.py

echo "=== rendering to docs/book/"
rm -rf docs/book   # a removed page must not linger on the site
if [ "${1:-}" = "--html-only" ]; then
    (cd book && quarto render --to html)
else
    (cd book && quarto render)
fi

echo "Book written to docs/book/ — then: python3 scripts/build_docs.py, commit and push."
