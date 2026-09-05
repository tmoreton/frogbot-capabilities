from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "site"
OUTPUT = ROOT / "dist"


def main() -> None:
    catalog = json.loads((ROOT / "catalog.json").read_text())
    if catalog.get("repository") != "tmoreton/frogbot-skills":
        raise ValueError("catalog repository must match the renamed GitHub repository")

    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    shutil.copytree(SOURCE, OUTPUT)
    shutil.copy2(ROOT / "catalog.json", OUTPUT / "catalog.json")
    (OUTPUT / ".nojekyll").touch()
    print(f"Built GitHub Pages site in {OUTPUT}")


if __name__ == "__main__":
    main()
