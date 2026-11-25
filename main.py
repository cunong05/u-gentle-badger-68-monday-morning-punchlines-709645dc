#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun bounty entry.

Writes one original joke about Monday mornings to /output/entry.txt.
"""

import os

ENTRY = (
    "Monday morning, I told my boss I was working from home. "
    "Technically true \u2014 I spent the whole morning working very hard on staying home."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
