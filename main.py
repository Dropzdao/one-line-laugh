#!/usr/bin/env python3
"""The One-Line Laugh: a smartwatch joke, one line, written to /output/entry.txt."""

import os

SETUP = "My smartwatch keeps telling me to move more,"
PUNCHLINE = "so I moved it to a drawer where it can't judge me."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate_line(line):
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError("entry line is %d chars, max %d" % (len(line), MAX_CHARS))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def compose_line(setup, punchline):
    return setup + " " + punchline


def main():
    line = validate_line(compose_line(SETUP, PUNCHLINE))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
