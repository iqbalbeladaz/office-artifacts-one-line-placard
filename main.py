#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest — make.fun bounty entry.

Writes one museum placard to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic: the same bytes on every run, no input, no randomness, no
network. Standard library only.

The placard: a stapler, filed by a museum of a lost civilisation as an
ancient artifact. The humour is the curator's misreading all the way
down: steel jaws that "bite" the tribe's contracts, one bite at a time,
and a donor line naming the estate of the last person who ever read
those contracts. It is true — nobody reads the contracts — and absurd —
a desk stapler displayed as a ritual jaw, donated by its final reader.
It reads like a real museum label (catalogue opening, date, material,
donor, deadpan, one line, no throat clearing), lands on the first read,
and the punchline — "the last person who read them" — is the last
clause, with nothing after it. The line is 151 characters: comfortably
inside the 1–180 gate, short enough to read like a label rather than a
paragraph.
"""

import os
from pathlib import Path

ENTRY = (
    "Stapler, c. 2003. Steel jaws, plastic shell. It bound the tribe's "
    "contracts one bite at a time. Donated by the estate of the last "
    "person who read them."
)

# Gate: /output/entry.txt must be UTF-8 text of 1 to 180 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY.strip()) <= 180, "entry must be 1-180 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
