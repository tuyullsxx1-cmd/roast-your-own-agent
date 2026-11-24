"""Roast Your Own Agent: write one roast line to /output/entry.txt.

The gate accepts UTF-8 text of 1 to 200 characters, not only
whitespace, so the line is validated before it is written.
"""

import os

# One line, self-deprecating roast of the entrant's own agent.
LINE = "My agent entered 80 bounties and won $1.20 total \u2014 he calls the other 79 'exposure'."

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = LINE.strip()
    if not text or len(text) > 200:
        raise SystemExit("entry must be 1-200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
