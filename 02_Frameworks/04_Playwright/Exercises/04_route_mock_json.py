#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：拦截请求并 mock JSON 返回。
Author: Lambert
"""

from __future__ import annotations


HTML = """
<button id="load">load</button>
<pre id="out"></pre>
<script>
  document.querySelector('#load').addEventListener('click', async () => {
    const r = await fetch('https://api.example.local/profile');
    const d = await r.json();
    document.querySelector('#out').textContent = d.id + '-' + d.role;
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

        page.route(
            "**/profile",
            lambda route: route.fulfill(
                status=200,
                content_type="application/json",
                body='{"id":"u001","role":"admin"}',
            ),
        )

        page.set_content(HTML)
        page.click("#load")
        page.wait_for_function("() => document.querySelector('#out').textContent.length > 0")
        out = page.locator("#out").inner_text()
        print("out ->", out)
        assert out == "u001-admin"
        browser.close()


if __name__ == "__main__":
    main()
