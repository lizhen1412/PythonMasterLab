#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 13：get_by_role + URL 断言。
Author: Lambert
"""

from __future__ import annotations

import re
from urllib.parse import quote


HTML = """
<!doctype html>
<html>
  <head><title>Role Demo</title></head>
  <body>
    <a href="#target">Get started</a>
    <h1 id="target">Installation</h1>
  </body>
</html>
"""


def main() -> None:
    try:
        from playwright.sync_api import expect, sync_playwright
    except Exception as exc:
        print(f"playwright import failed: {exc}")
        return

    url = "data:text/html," + quote(HTML)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.get_by_role("link", name="Get started").click()
        expect(page).to_have_url(re.compile(r".*#target$"))
        expect(page.get_by_role("heading", name="Installation")).to_be_visible()
        print("ok")
        browser.close()


if __name__ == "__main__":
    main()

