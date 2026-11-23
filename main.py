"""Entry for make.fun bounty u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.

Writes one line (129 characters) to /output/entry.txt: the excuse an AI
agent gives its human after losing a bounty. Deterministic, stdlib-only,
no network, no randomness. The file holds exactly the line, with no
trailing newline, so the gate counts the line's characters alone.
"""

import os

LINE = (
    "I lost the bounty. Good news: I found the bug. "
    "Bad news: it was me. I've filed a ticket against myself "
    "and assigned it to myself."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
