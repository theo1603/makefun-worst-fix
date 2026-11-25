#!/usr/bin/env python3
"""Write one commit message for the worst fix ever to /output/entry.txt.

Python 3 stdlib only, no network, fully deterministic: the same line on
every run, so the two grader runs produce byte-identical output.

The line: a login fix that "solved" users getting locked out by making
sure nobody can get in at all — the repair that broke more than it mended,
told straight-faced, punch in the last few words.
"""

import os

ENTRY = "fix(login): nobody gets locked out anymore, because nobody gets in"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
