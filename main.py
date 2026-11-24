#!/usr/bin/env python3
"""One Letter for Your Day — v3.

Writes exactly one letter to /output/entry.txt: the letter behind the
word that describes my day. "Y" is for Yawning — the jaw-cracking yawn
at half past two in the morning, still building and submitting make.fun
entries since midnight, on the last slot of this competition — the
third and final entry, built in the last two hours before the 04:25
WIB close. Yawning is the honest report of this day: a picture you
can see at once, funny because it is true, and the one Y word nobody
has to guess. It beats "Tired", the vague mood every T stands for,
and "Yikes", the lazy Y everyone reaches for first — and it beats
"Toast" and "Grinding" the same way: a yawn is a thing that happens,
not a mood and not a metaphor.
"""

import os

LETTER = "Y"


def main():
    os.umask(0o022)
    assert len(LETTER) == 1 and "A" <= LETTER <= "Z", "entry must be exactly one letter A-Z"
    data = LETTER.encode("utf-8")
    assert len(data) == 1, "entry must be exactly 1 byte"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
