#!/usr/bin/env python
"""

python3 core8/pwb.py typos/test

"""
from pathlib import Path

from newapi import printe
from typos.typos_text import typos_text_def  # typo_text = typos_text_def()
from typos.topy import fix_text  # fix_text(text)

Dir = Path(__file__).parent
# ---

typo_text = typos_text_def()


def handle_file(filename):
    """
    !
    """
    print(f"Reading {filename}")

    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    safe_name = filename

    newtext, sus = fix_text(text)

    if newtext == text:
        print(f"No changes in {safe_name}")
        return

    printe.showDiff(text, newtext)
    print(f"Writing {safe_name}")
    print(f"sus {sus}")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    handle_file(Dir / "texts/1.txt")
