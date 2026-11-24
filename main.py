#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original line to /output/entry.txt: a fortune-cookie
prophecy aimed at a software developer who inherits legacy code.
The fortune is a true dev-day moment — meeting a TODO from 2019
whose author is long gone — turned with a fresh twist: the comment
lies, and the code still runs production anyway. The dated TODO
(2019) is the concrete anchor: every tired senior engineer has
met exactly this one. The line is cut to three sharp fragments
after the colon — a stab, not a status report.
"""

import os
import sys

TEXT = (
    # One concrete date (2019) anchors the fortune; three short
    # fragments after the colon deliver the punch in one breath.
    "You will meet a 2019 TODO: author gone, comment lying, "
    "code still in production."
)


def main() -> int:
    # Gate: 1 to 120 characters, counted as Unicode code points,
    # and not only white space. The line runs 80 — well inside.
    if not (1 <= len(TEXT) <= 120) or not TEXT.strip():
        print("entry text fails the 1-120 gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read back and re-check: the file on disk must be exactly the text
    # the program claims to have written.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote entry.txt ({len(TEXT)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
