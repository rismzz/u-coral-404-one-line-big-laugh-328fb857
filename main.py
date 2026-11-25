#!/usr/bin/env python3
"""One Line, Big Laugh — a single funny line of at most 200 characters.

The judge reads lines two at a time and the funniest ones take the
reward, so the line is built to land on its own: a Roomba that learned
to fetch now returns its owner's lost socks — with judgement. The
punchline is the judgement: the machine is not just helpful, it has
opinions about its owner.
"""

import os
from pathlib import Path

LINE = "I taught my Roomba to fetch — now it brings me my own lost socks and judges me for losing them in the first place."

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
