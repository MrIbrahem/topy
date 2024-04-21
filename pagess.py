#!/usr/bin/python3
"""

python3 core8/pwb.py typos/pagess ask -newpages2:10

"""
from newapi.page import MainPage
from API import printe

from typos.topy import fix_text  # text, sum = fix_text(text)
import gent


def work_page(x):
    page = MainPage(x, "ar", family="wikipedia")

    if not page.exists():
        return

    text = page.get_text()

    page_edit = page.can_edit()
    if not page_edit:
        return
    # ---
    printe.output(f"fix_text, page:[[{x}]]")
    # ---
    new_text, sumn = fix_text(text)
    # ---
    if new_text == text:
        printe.output(f"No changes in {x}")
        return
    # ---
    page.save(newtext=new_text, summary=f"بوت: المستبدلات: {{{sumn}}}")


def main3():
    printe.output("<<lightred>> main3.")
    # ---
    generator = gent.get_gent()
    # ---
    for page in generator:
        title = page.title(as_link=False)
        work_page(title)


if __name__ == "__main__":
    main3()
