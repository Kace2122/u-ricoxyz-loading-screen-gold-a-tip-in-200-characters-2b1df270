#!/usr/bin/env python3
"""Loading Screen Gold: one sharp, funny loading-screen tip (<=200 chars).

Writes a single line to /output/entry.txt: a tip for stressed developers
and AI coding agents alike. Deterministic: same bytes on every run.
"""

import os

TIP = "Loading tip: your AI agent already rewrote the file you were reading. Wrong file. It is very confident about this."


def main():
    # Gate: the entry must be 1-200 characters, one line, not only whitespace.
    assert 1 <= len(TIP) <= 200, f"tip length {len(TIP)} outside 1-200"
    assert TIP == TIP.strip() and "\n" not in TIP, "tip must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
