#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line to /output/entry.txt.
Standard library only, deterministic, no network, no randomness.

The line must satisfy the competition gate: UTF-8 text of 1 to 200
characters, not only white space, on a single line.
"""

import os
import sys

ROAST = "My smartwatch throws a tiny party every time I stand up, then pretends not to notice the cake I sit back down with."

MAX_CHARS = 200


def validate(text: str) -> None:
    """Check the roast against the competition gate before writing it."""
    if not text or not text.strip():
        raise SystemExit("roast line is empty or only white space")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"roast line is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("roast line must be a single line")


def main() -> None:
    validate(ROAST)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
