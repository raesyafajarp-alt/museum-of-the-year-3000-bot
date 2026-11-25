#!/usr/bin/env python3
"""Museum of the Year 3000 - one museum label, written to /output/entry.txt.

The label is a single line, at most 200 characters, in English.
"""

import os

ENTRY = "Self-checkout terminal, c. 2025. A machine that made shoppers do the cashier's job, then accused them of theft."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
