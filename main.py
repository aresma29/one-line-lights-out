#!/usr/bin/env python3
"""One Line, Lights Out — print the entry line exactly as stored.

The entry lives in entry.txt next to this script. This program reads it
and writes it to standard output byte-for-byte, with no stripping,
no added newline, and no decoration, then exits successfully.
"""

import sys
from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    sys.stdout.write(entry_path.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
