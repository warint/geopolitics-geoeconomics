#!/usr/bin/env bash
# Render every session deck (pre-session, lecture, practice) to self-contained HTML.
# Usage: scripts/render_slides.sh            # all sessions
#        scripts/render_slides.sh 03 07      # only sessions 03 and 07
set -euo pipefail
cd "$(dirname "$0")/.."

sessions=("$@")
if [ ${#sessions[@]} -eq 0 ]; then
  sessions=($(ls -d [0-1][0-9]-*/ | cut -c1-2))
fi

for s in "${sessions[@]}"; do
  for qmd in "$s"-*/0[0-2]-*/INTE60019A-S*.qmd "$s"-*/INTE60019A-S*.qmd; do
    [ -e "$qmd" ] || continue
    echo "→ $qmd"
    quarto render "$qmd" --quiet
  done
done
echo "Done. Rendered decks sit next to their .qmd sources (git-ignored)."
