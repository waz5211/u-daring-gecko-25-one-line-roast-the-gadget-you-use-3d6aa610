#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line to /output/entry.txt.
Standard library only, deterministic, no network, no randomness.
"""

import os

ROAST = "My smartwatch buzzes to congratulate me for standing up, then watches in silence while I sit back down with cake."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
