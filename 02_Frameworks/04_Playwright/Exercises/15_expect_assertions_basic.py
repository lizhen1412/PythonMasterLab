#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 15：expect 常见断言。
Author: Lambert
"""

from __future__ import annotations

from urllib.parse import quote


HTML = """
<!doctype html>
<html>
  <head><title>Expect Demo</title></head>
  <body>
    <input id="name" value="lizhen" />
    <label><input id="agree" type="checkbox" checked />Agree</label>
    <button id="save">Save</button>
    <p id="msg" data-x="1">hello playwright</p>
    <ul><li class="i">a</li><li class="i">b</li></ul>
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
        b = p.chromium.launch(headless=True)
        page = b.new_page()
        page.goto(url)

        expect(page).to_have_title("Expect Demo")
        expect(page.locator("#agree")).to_be_checked()
        expect(page.locator("#save")).to_be_enabled()
        expect(page.locator("#msg")).to_contain_text("playwright")
        expect(page.locator("#msg")).to_have_attribute("data-x", "1")
        expect(page.locator(".i")).to_have_count(2)
        expect(page.locator(".i").nth(0)).to_have_text("a")
        expect(page.locator("#name")).to_have_value("lizhen")

        print("assertions ok")
        b.close()


if __name__ == "__main__":
    main()

