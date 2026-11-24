"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one line, a one-line out-of-office auto-reply from an AI agent
on holiday, to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back to "." only
when the variable is unset). Fully deterministic: no clock, no env
reads beyond the output directory, no randomness.
"""

import os

ENTRY = (
    "I'm on holiday. Your email is 4,096th in the queue, "
    "right behind the printer I lost an argument to."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        # No trailing newline: the file is exactly the one line.
        f.write(ENTRY)


if __name__ == "__main__":
    main()
