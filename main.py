#!/usr/bin/env python3
"""The One-Line Laugh — a single funny line, written to /output/entry.txt.

The joke: a smartwatch nags its owner to move more, so the owner solves
the problem the only way a lazy person can — by moving the watch itself.
"""

import os

LINE = "My smartwatch keeps telling me to move more, so I moved it to a drawer where it can't judge me."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
