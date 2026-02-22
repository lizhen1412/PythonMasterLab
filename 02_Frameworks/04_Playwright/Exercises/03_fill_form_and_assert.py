#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：填写表单并断言输出。
Author: Lambert
"""

from __future__ import annotations


HTML = """
<input id="name" />
<button id="ok">OK</button>
<p id="out"></p>
<script>
  document.querySelector('#ok').addEventListener('click', () => {
    const n = document.querySelector('#name').value;
    document.querySelector('#out').textContent = `user=${n}`;
  });
</script>
"""


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:
        print(f"playwright import failed: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)
        page.fill("#name", "lizhen")
        page.click("#ok")
        out = page.locator("#out").inner_text()
        print("out ->", out)
        assert out == "user=lizhen"
        browser.close()


if __name__ == "__main__":
    main()
