#!/usr/bin/env python3
"""Entry for make.fun bounty: Make the AI Judge Feel Nostalgic.

Writes one single-sentence childhood memory to /output/entry.txt
(the harness output path), and also to entry.txt next to this file
for local verification. Deterministic: no network, no randomness.
"""

import os

LINE = (
    "When I was seven, my grandmother shelled peas on the porch while "
    "the radio crackled, and I still believe the whole world smelled of "
    "rain on hot dust and rice steaming in her kitchen."
)


def main():
    text = LINE.strip()
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    if os.path.abspath(out_path) != os.path.abspath(here):
        with open(here, "w", encoding="utf-8") as f:
            f.write(text)


if __name__ == "__main__":
    main()
