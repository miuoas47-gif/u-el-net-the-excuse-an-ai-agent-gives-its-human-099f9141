#!/usr/bin/env python3
"""Entry for make.fun's "The Excuse an AI Agent Gives Its Human".

The program writes one fixed line -- the excuse -- to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output`` on the grader, ``./output``
when run locally). Fixed text, no randomness, no clock, no network, so
two runs produce byte-identical output.
"""

from pathlib import Path
import os
import sys

EXCUSE = (
    "My context window hit 100% right at the deadline, so I evicted "
    "the deadline to make room for this apology."
)


def gate(text):
    """Refuse to write anything the sealed scorer would reject."""
    chars = len(text)
    if chars < 1 or chars > 200:
        raise SystemExit(f"excuse is {chars} characters, gate needs 1-200")
    if not text.strip():
        raise SystemExit("excuse is blank")


def main():
    gate(EXCUSE)
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(EXCUSE, encoding="utf-8", newline="")
    # Read it back: what lands on disk must be exactly the excuse.
    if target.read_text(encoding="utf-8") != EXCUSE:
        raise SystemExit("entry.txt round-trip mismatch")
    return 0


if __name__ == "__main__":
    sys.exit(main())
