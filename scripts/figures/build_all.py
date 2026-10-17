"""Draw the book's figures: run scripts/figures/chNN.py for every (or the given) chapter."""

import importlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

wanted = sys.argv[1:] or sorted(p.stem[2:] for p in HERE.glob("ch[0-9][0-9].py"))
for num in wanted:
    module = importlib.import_module(f"ch{num}")
    made = module.main()
    print(f"ch{num}: {len(made or [])} figures")
