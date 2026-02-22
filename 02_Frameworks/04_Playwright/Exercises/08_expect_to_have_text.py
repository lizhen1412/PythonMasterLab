#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 08：使用 expect 断言文本。
Author: Lambert
"""

from __future__ import annotations


HTML = "<p id='msg'>hello</p>"


def main() -> None:
    try:
        from playwright.sync_api import expect, sync_playwright
    except Exception as exc:
        print(f"playwright import failed: {exc}")
        return

    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        page = b.new_page()
        page.set_content(HTML)
        expect(page.locator("#msg")).to_have_text("hello")
        print("assert ok")
        b.close()


if __name__ == "__main__":
    main()
