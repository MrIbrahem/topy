#!/usr/bin/env python
"""

from typos.topy import fix_text  # text, sum = fix_text(text)

"""
# import wikitextparser as wtp
import regex
from bs4 import BeautifulSoup
from newapi import printe
from typos.typos_text import typos_text_def  # typo_text = typos_text_def()

from typos.chaa import change_text, un_change_text

# ca, text2 = change_text(text)
# newtext = un_change_text(ca, text)

from pathlib import Path

Dir = Path(__file__).parent

typo_text = typos_text_def()


def load_rules():
    """Load and parse rules from `filename`, returns list of 3-tuples [(name, regexp, replacement), ...]"""
    soup = BeautifulSoup(typo_text, "html.parser")
    regs = []

    n_disabled = 0
    n_errors = 0
    n_loaded = 0

    for typo in soup.findAll("typo"):
        if "word" not in typo.attrs:
            n_disabled += 1
            continue

        word = typo.attrs["word"]
        find = typo.attrs["find"]
        replace = typo.attrs["replace"]

        try:
            r = regex.compile(find)
            replace = regex.sub(r"\$(\d)", r"\\\1", replace)

            regs.append((word, r, replace))
            n_loaded += 1
        except regex.error as err:
            print(f"cannot compile {word} {find} {err}")
            n_errors += 1

    print(f"Loaded {n_loaded} rules (except {n_errors} errors, {n_disabled} disabled)")

    return regs


regs = load_rules()


def fix_text(old_text):
    """
    !
    """
    # print(f"fix_text, len regs: {len(regs)}")
    # ---
    ca, text = change_text(old_text)
    # ---
    replaced = 0
    # ---
    repsa = {}
    # ---
    for word, r, replace in regs:
        try:
            newtext, count = r.subn(replace, text)
            if count > 0 and newtext != text:
                replaced += count
                print(f"replaced {word} x {count}")
                repsa[word] = count
            text = newtext
        except regex.error as err:
            print(f"error replacing {word} ({r}=>{replace}): {err}")
    # ---
    newtext = un_change_text(ca, text)
    # ---
    errs = [
        "(@@@@",
        "(&&&&",
        "(####",
        "(!!__!!",
        "(?_?_?",
    ]
    # ---
    for key in errs:
        if key in newtext:
            printe.output(f"<<red>> found key: {key} in newtext")
            err_file = Dir / "err.txt"
            err_file.write_text(newtext, encoding="utf-8")
            return old_text, ""
    # ---
    sum = "، ".join([f"{w} ({v})" for w, v in repsa.items()])
    # ---
    return newtext, sum
