#!/usr/bin/env python3
"""Write one short relaxing text to /output/entry.txt.

Deterministic: a fixed string, no randomness, no network.
The output directory defaults to /output (the sandbox location) and can
be overridden with the OUTPUT_DIR environment variable for local testing.
"""

import os
import sys
import tempfile

TEXT = (
    "The afternoon light has gone amber on the floorboards, and the dust "
    "drifts through it, slow as sleep. Outside, a bicycle leans against "
    "the fence, its front wheel still turning \u2014 slower, slower \u2014 "
    "until it stops. The street empties. The house keeps the warmth a "
    "little longer."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write(TEXT)
            os.replace(tmp_path, os.path.join(out_dir, "entry.txt"))
        except BaseException:
            try:
                os.unlink(tmp_path)
            except OSError:
                pass
            raise
    except OSError as exc:
        print(f"error: cannot write entry.txt in {out_dir}: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
