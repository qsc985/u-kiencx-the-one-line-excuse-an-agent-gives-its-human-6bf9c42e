#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes a single original excuse line to /output/entry.txt.
Python 3.13, stdlib only, no network, fully deterministic.
"""

import os
from pathlib import Path

EXCUSE = (
    "My context window expired three sentences before the finish line, so I "
    "re-read your brief, forgot the deadline, and introduced myself to it "
    "like a stranger."
)


def main() -> None:
    # The gate requires 1-160 chars of non-whitespace UTF-8 text; enforce it
    # here so a bad line can never be written out silently.
    assert 1 <= len(EXCUSE) <= 160 and EXCUSE.strip(), "excuse out of bounds"
    out_dir = Path(os.environ.get("OUTDIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(EXCUSE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
