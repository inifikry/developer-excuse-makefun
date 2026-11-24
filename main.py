#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt. The line must be 1-200 UTF-8
characters, a single line, and not only whitespace.
"""

LINE = (
    "The bug only happens in production because that's the only place "
    "anyone actually uses my code."
)


def main() -> None:
    """Write the excuse as exactly one line to /output/entry.txt."""
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
