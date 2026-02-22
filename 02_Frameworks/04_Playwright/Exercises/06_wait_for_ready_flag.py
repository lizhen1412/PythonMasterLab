#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 06：等待按钮变为可点击。
Author: Lambert
"""

from __future__ import annotations


HTML = """
<button id="ok" disabled>wait</button>
<script>setTimeout(() => document.querySelector('#ok').disabled = false, 150);</script>
"""


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:
        print(f"playwright import failed: {exc}")
        return

    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        page = b.new_page()
        page.set_content(HTML)
        page.click("#ok")
        print("clicked")
        b.close()


if __name__ == "__main__":
    main()
