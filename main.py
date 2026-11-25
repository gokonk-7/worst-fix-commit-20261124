#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message — make.fun entry.

The entry is a single commit message (at most 100 characters) for a fix
that made everything worse. Running this module prints exactly that
message, one line, deterministically.
"""

MESSAGE = "fix: the bug is gone \u2014 so are the data, the backups, and Dave"


def main() -> None:
    assert len(MESSAGE) <= 100, "commit message exceeds 100 characters"
    assert "\n" not in MESSAGE, "commit message must be a single line"
    print(MESSAGE)


if __name__ == "__main__":
    main()
