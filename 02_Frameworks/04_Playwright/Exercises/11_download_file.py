#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 11：点击下载并保存文件。
Author: Lambert
"""

from __future__ import annotations

from pathlib import Path


OUT = Path("/tmp/playwright_demo/ex11.txt")
HTML = "<a id='dl' download='x.txt' href='data:text/plain,hello-ex11'>download</a>"


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:
        print(f"playwright import failed: {exc}")
        return

    OUT.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        page = b.new_page()
        page.set_content(HTML)
        with page.expect_download() as info:
            page.click("#dl")
        info.value.save_as(str(OUT))
        print("saved ->", OUT)
        b.close()


if __name__ == "__main__":
    main()
