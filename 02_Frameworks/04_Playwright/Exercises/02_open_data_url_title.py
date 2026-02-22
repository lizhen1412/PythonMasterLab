#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：打开 data URL 并读取标题文本。
Author: Lambert
"""

from __future__ import annotations


def run() -> str:
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:
        return f"playwright import failed: {exc}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("data:text/html,<h1 id='t'>hello</h1>")
        text = page.locator("#t").inner_text()
        browser.close()
        return text


def main() -> None:
    result = run()
    print("result ->", result)


if __name__ == "__main__":
    main()
