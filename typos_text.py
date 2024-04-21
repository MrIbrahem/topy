#!/usr/bin/python3
"""

from typos.typos_text import typos_text_def # typo_text = typos_text_def()

python3 core8/pwb.py typos/typos_text
"""
import os
import requests
from datetime import datetime
from pathlib import Path

Dir = Path(__file__).parent
# ---
filename = Dir / "typo.txt"
# ---
if not filename.exists():
    filename.touch()
# ---
with open(filename, "r", encoding="utf-8") as f:
    text_main = f.read()


def get_url_text(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print("Error: Unable to retrieve content from URL")
            return None
    except Exception as e:
        print("Error:", e)
        return None


def get_text_from_page():
    # ---
    url = "https://ar.wikipedia.org/wiki/Wikipedia:الأوتو_ويكي_براوزر/المستبدلات?action=raw"
    # ---
    text = get_url_text(url)
    # ---
    if not text:
        print("no text")
        return ""
    # ---
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    # ---
    return text


def typos_text_def():
    global text_main

    # Get the time of last modification
    last_modified_time = os.path.getmtime(filename)
    # ---
    date = datetime.fromtimestamp(last_modified_time).strftime("%Y-%m-%d")
    # ---
    today = datetime.today().strftime("%Y-%m-%d")
    # ---
    if date != today or not text_main:
        print(f"<<purple>> last modified: {date} , today: {today}, len: {len(text_main)} ")
        text_main = get_text_from_page()
    # ---
    return text_main


if __name__ == "__main__":
    u = typos_text_def()
    print(f"len text_main : {len(u)}")
