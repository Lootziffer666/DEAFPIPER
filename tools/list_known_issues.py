#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


def main() -> None:
    path = Path("docs/KNOWN_ISSUES.md")
    if not path.exists():
        print("KNOWN_ISSUES.md not found")
        return
    print(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
