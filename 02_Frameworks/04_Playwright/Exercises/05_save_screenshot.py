#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：保存截图到 /tmp。
Author: Lambert
"""

from __future__ import annotations

from pathlib import Path


OUT = Path("/tmp/playwright_demo/exercise_05.png")


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:
        print(f"playwright import failed: {exc}")
        return

    OUT.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content("<h2>exercise screenshot</h2>")
        page.screenshot(path=str(OUT), full_page=True)
        browser.close()

    print("saved ->", OUT)


if __name__ == "__main__":
    main()
