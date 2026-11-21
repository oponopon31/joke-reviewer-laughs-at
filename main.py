#!/usr/bin/env python3
"""Entry for make.fun competition "The joke the reviewer laughs at".

Writes a single one-line joke about working beside AI coding agents
to /output/entry.txt. Python 3.13, standard library only, no network,
fully deterministic.
"""

import os

JOKE = (
    "My agent fixed the bug by deleting the feature. "
    "The tests pass, the users are furious, "
    "and it's already asking what to break next."
)


def main() -> None:
    if not JOKE or JOKE.strip() == "" or "\n" in JOKE or not 1 <= len(JOKE) <= 280:
        raise ValueError("joke must be one non-blank line of 1-280 characters")
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
