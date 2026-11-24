"""Alien Field Notes: The Two Day Earth Review — make.fun entry.

Writes one line to entry.txt: an alien tourist's review of Earth after a
two-day stay. The laugh comes from the visitor's angle on ordinary human
habits — glowing rectangles, bitter bean water, apologising to robots —
and it closes like a real review: a verdict, five stars, and a punch.
"""

import os

REVIEW = (
    "Two-day stay: the hosts worship glowing rectangles, queue for bitter "
    "bean water, and apologise to robots. Sunsets unreal, though. "
    "Five stars — would abduct again."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The gate allows 1 to 200 characters; keep the review inside it.
    assert 1 <= len(REVIEW) <= 200, f"review is {len(REVIEW)} chars"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
