#!/usr/bin/env python3
"""Write one short relaxing text to /output/entry.txt.

Deterministic: a fixed string, no randomness, no network.
The output directory defaults to /output (the sandbox location) and can
be overridden with the OUTPUT_DIR environment variable for local testing.
"""

import os

TEXT = (
    "The afternoon light has gone amber on the floorboards, and the dust "
    "drifts through it, slow as sleep. Outside, a bicycle leans against "
    "the fence, its front wheel still turning \u2014 slower, slower \u2014 "
    "until it stops. The street empties. The house keeps the warmth a "
    "little longer."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
