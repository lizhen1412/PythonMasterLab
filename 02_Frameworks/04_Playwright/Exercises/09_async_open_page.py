#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 09：Async API 打开页面。
Author: Lambert
"""

from __future__ import annotations

import asyncio


async def run_async() -> None:
    try:
        from playwright.async_api import async_playwright
    except Exception as exc:
        print(f"playwright import failed: {exc}")
        return

    async with async_playwright() as p:
        b = await p.chromium.launch(headless=True)
        page = await b.new_page()
        await page.set_content("<h1 id='t'>async</h1>")
        print(await page.locator("#t").inner_text())
        await b.close()


def main() -> None:
    asyncio.run(run_async())


if __name__ == "__main__":
    main()
