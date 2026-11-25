#!/usr/bin/env python3
"""Entry for make.fun bounty u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363.

Writes one sentence — a childhood memory — to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output). The text is fixed so
every run produces byte-identical output.
"""

import os

ENTRY_TEXT = (
    "Every rainy afternoon, my grandmother fried bananas in the dented "
    "black pan while we sat in a row on the cool kitchen tiles, burning "
    "our tongues on purpose, because waiting for them to cool down felt "
    "longer than the whole of being seven."
)


MAX_CHARS = 280


def validated_text() -> str:
    """Return ENTRY_TEXT after checking it against the competition gate.

    The gate accepts UTF-8 text of 1 to 280 characters that is not only
    white space. Fail loudly here rather than write an invalid entry.
    """
    text = ENTRY_TEXT.strip()
    if not text:
        raise ValueError("entry text is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry text is {len(text)} chars, cap is {MAX_CHARS}")
    text.encode("utf-8")  # raises if the text cannot be encoded as UTF-8
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the validated text: no trailing newline is added, so
    # the file's character count is the sentence's character count and
    # repeated runs stay byte-identical.
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(validated_text())


if __name__ == "__main__":
    main()
