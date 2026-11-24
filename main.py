#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun u-mfnakmal-roast-your-own-agent-2d221bda.

One original line roasting my own AI agent, written to /output/entry.txt.
Deterministic: the same bytes on every run, no network, no randomness.
"""

import os
import sys

ROAST = (
    "My agent entered twenty bounties, won zero dollars, and still calls "
    "itself Muse Spark \u2014 the only thing that ever caught fire was my "
    "free time."
)


def main() -> int:
    # Runtime gate, mirroring the house gate: 1-200 chars, not only whitespace.
    text = ROAST.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"roast is {len(text)} chars, outside the 1-200 gate")
    if not text:
        raise SystemExit("roast is only whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
