#!/usr/bin/env python
"""

from typos.chaa import change_text, un_change_text
# change_text(text)
# un_change_text(ca, text)

python3 core8/pwb.py typos/chaa


"""
import wikitextparser as wtp
from newapi import printe
from pathlib import Path

Dir = Path(__file__).parent


def change_text(text):
    ca = {}
    ca["temps"] = {}
    # ---
    prased = wtp.parse(text)
    # ---
    for n, t in enumerate(reversed(prased.templates)):
        k = f"(@@@@{n}@@@@)"
        ca["temps"][k] = t.string
        t.string = k
    # ---
    ca["links"] = {}
    # ---
    for n, lo in enumerate(reversed(prased.wikilinks)):
        k = f"(&&&&{n}&&&&)"
        ca["links"][k] = lo.string
        lo.string = k
    # ---
    ca["tags"] = {}
    # ---
    for n, t in enumerate(reversed(prased.get_tags())):
        k = f"(####{n}####)"
        ca["tags"][k] = t.string
        t.string = k
    # ---
    ca["ext"] = {}
    # ---
    for n, t in enumerate(reversed(prased.external_links)):
        k = f"(!!__!!{n}!!__!!)"
        ca["ext"][k] = t.string
        t.string = k
    # ---
    ca["pf"] = {}
    # ---
    for n, t in enumerate(reversed(prased.parser_functions)):
        k = f"(?_?_?{n}?_?_?)"
        ca["pf"][k] = t.string
        t.string = k
    # ---
    return ca, prased.string


def un_change_text(ca, text):
    # ---
    text2 = text
    # ---
    for i in [1, 2]:
        for key, tag in ca["pf"].items():
            text2 = text2.replace(key, tag)
        # ---
        for key, tag in ca["ext"].items():
            text2 = text2.replace(key, tag)
        # ---
        for key, tag in ca["tags"].items():
            text2 = text2.replace(key, tag)
        # ---
        for key, link in ca["links"].items():
            text2 = text2.replace(key, link)
        # ---
        for key, text in ca["temps"].items():
            text2 = text2.replace(key, text)
    # ---
    return text2


if __name__ == "__main__":
    file = Dir / "texts/1.txt"
    text = file.read_text(encoding="utf-8")
    ca, text2 = change_text(text)

    printe.showDiff(text, text2)

    file2 = Dir / "texts/1_2.txt"

    file2.write_text(text2, encoding="utf-8")
