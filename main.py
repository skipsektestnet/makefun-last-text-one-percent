"""Last Text at One Percent: writes the entry text to /output/entry.txt.

Why this line: The phone speaks in its own voice, with a stake in dying: a specific, funny last confession (47 tabs, 3am search history). No low-battery pun.
"""

import os

ENTRY = 'okay this is it. tell my owner i died doing what i loved: 47 tabs open, brightness at 100%, judging him for that 3am search history'

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
