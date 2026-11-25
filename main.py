#!/usr/bin/env python3
"""Print the one-line Lights Out entry from entry.txt."""

from pathlib import Path

# The entry lives next to this script, so it runs from any directory.
line = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8").strip()
print(line)
