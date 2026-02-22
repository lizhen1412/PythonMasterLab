#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 10：通过 frame_locator 读取 iframe 文本。
Author: Lambert
"""

from __future__ import annotations


HTML = "<iframe id='f' srcdoc=\"<span id='x'>inside</span>\"></iframe>"


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
        print(page.frame_locator("#f").locator("#x").inner_text())
        b.close()


if __name__ == "__main__":
    main()
