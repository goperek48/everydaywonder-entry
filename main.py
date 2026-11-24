#!/usr/bin/env python3
"""Everyday Wonder — a single sentence that estranges an ordinary instant.

The competition wants one sentence, no more than 200 characters, that makes
a familiar moment feel unfamiliar: lift doors, a stranger's tune, a memory
that has no business being there. This script only puts that sentence where
the harness looks for it.
"""

import os
import sys

# The entry: one sentence, 132 characters, closing on one startling image.
# A stranger humming a dead grandmother's lullaby makes a routine lift ride
# feel as though the building itself is holding on to her memory.
SENTENCE = (
    "The lift doors opened on a stranger humming my dead grandmother's "
    "lullaby, and for one floor I believed the building remembered her."
)


def main() -> int:
    # MAKEFUN_OUTPUT_DIR tells us the destination; /output is the
    # documented fallback for the program/v1 harness.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    # Write the sentence exactly as drafted, without a trailing newline, so
    # the gate measures the same 132 characters the judge will read.
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(SENTENCE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
