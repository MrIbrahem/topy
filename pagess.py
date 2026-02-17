#!/usr/bin/python3
"""

python3 core8/pwb.py typos/pagess ask -newpages2:10

"""
from newapi.page import MainPage
from API import printe

from typos.topy import fix_text  # text, sum = fix_text(text)
import gent

import logging
logger = logging.getLogger(__name__)

def work_page(x):
    page = MainPage(x, "ar", family="wikipedia")

    if not page.exists():
        return

    text = page.get_text()

    page_edit = page.can_edit()
    if not page_edit:
        return
    # ---
    logger.info(f"fix_text, page:[[{x}]]")
    # ---
    new_text, sumn = fix_text(text)
    # ---
    if new_text == text:
        logger.info(f"No changes in {x}")
        return
    # ---
    page.save(newtext=new_text, summary=f"بوت: المستبدلات: {{{sumn}}}")


def main3():
    logger.info("<<lightred>> main3.")
    # ---
    generator = gent.get_gent(listonly=True)
    # ---
    for title in generator:
        work_page(title)


if __name__ == "__main__":
    main3()
