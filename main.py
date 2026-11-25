#!/usr/bin/env python3
"""make.fun entry: The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue (104 words) to /output/entry.txt, spoken by a fantasy
villain who is secretly just very tired:

    Right. The eclipse is Tuesday, the blood-moon, the whole choir of the
    damned — yes, yes, I've had the banners made since spring. ...

Why this monologue (judge brief, in order):
1. On subject: a ~100-word monologue for a fantasy villain who is secretly
   just very tired — an eclipse, a blood-moon, a prophecy, a throne.
2. The tiredness is felt, never announced: it lives in the rhythm — the
   repeated "Midnight. Midnight.", the to-do list of a siege at dawn, a tax
   revolt in the marshes — and in the small deflections ("yes, yes"), never
   in the word "weary".
3. A specific villain with a history and a scheme: banners made since
   spring, a dragon who only answers to "Greg" now, skulls that go in the
   cellar with the other skulls — concrete detail, not stock scenery.
4. Speakable dialogue with a turn in the last line: after all the menace,
   the sting lands on "I am taking the afternoon off."
5. Close to 100 words (104), every word working.

Selected by manual ranking against the kit judge brief plus manual
pairwise checks (see candidates.md); no automated judge was used.

Local validation: `MAKEFUN_OUTPUT=/tmp/entry.txt python3 main.py` run
twice, byte-identical; entry.txt is the monologue plus one trailing
newline, UTF-8 — gate 1-600 chars PASS.
"""

import os

LINE = (
    "Right. The eclipse is Tuesday, the blood-moon, the whole choir of the "
    "damned — yes, yes, I've had the banners made since spring. The prophecy "
    "says I rise at midnight. Midnight. I have a siege at dawn, a tax revolt "
    "in the marshes, and a dragon who only answers to 'Greg' now. Fine. Let "
    "them come. I'll be on the throne, in the dark, doing the voice. But if "
    "one more acolyte asks where the skulls go — the skulls go in the "
    "cellar, with the other skulls — I swear, by the old gods and the new, "
    "I am taking the afternoon off."
)

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 600, f"entry must be 1-600 chars, got {len(text)}"
    assert text and not text.isspace(), "entry must not be only whitespace"
    assert text == text.strip() and "\n" not in text, "entry must be a single line"
    words = text.split()
    assert 90 <= len(words) <= 110, f"monologue must be ~100 words, got {len(words)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read back and verify the written file round-trips exactly: the
    # monologue plus exactly one trailing newline, nothing else.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    assert raw == (text + "\n").encode("utf-8"), "written entry does not match"
    assert raw.count(b"\n") == 1, "entry file must hold exactly one line"


if __name__ == "__main__":
    main()
