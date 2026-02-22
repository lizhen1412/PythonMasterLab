#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 07：验证两个 context 的 cookie 隔离。
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
        browser = p.chromium.launch(headless=True)
        c1 = browser.new_context()
        c2 = browser.new_context()
        c1.add_cookies([{"name": "a", "value": "1", "domain": "x.local", "path": "/"}])
        c2.add_cookies([{"name": "a", "value": "2", "domain": "x.local", "path": "/"}])
        print(c1.cookies()[0]["value"], c2.cookies()[0]["value"])
        c1.close()
        c2.close()
        browser.close()


if __name__ == "__main__":
    main()
