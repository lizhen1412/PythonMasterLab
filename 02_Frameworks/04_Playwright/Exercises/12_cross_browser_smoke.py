#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 12：跨浏览器 smoke 测试。
Author: Lambert
"""

from __future__ import annotations


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:
        print(f"playwright import failed: {exc}")
        return

    with sync_playwright() as p:
        for bt in [p.chromium, p.firefox, p.webkit]:
            try:
                b = bt.launch(headless=True)
                page = b.new_page()
                page.set_content("<h3>ok</h3>")
                print(bt.name, page.locator("h3").inner_text())
                b.close()
            except Exception as exc:
                print(bt.name, "failed", exc)


if __name__ == "__main__":
    main()
