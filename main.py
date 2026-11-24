#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one line (1-200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt:
a sick-day excuse that is half believable, fresh, and lands its
twist on the last word.
"""

import os
import sys


def main() -> int:
    excuse = (
        "Sorry, can't come in today \u2014 I tried to fix a leaking tap, "
        "flooded the bathroom, and my goldfish has started charging me rent."
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(excuse + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
