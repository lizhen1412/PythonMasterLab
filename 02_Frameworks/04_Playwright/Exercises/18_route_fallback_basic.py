#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 18：route.fallback。
Author: Lambert
"""

from __future__ import annotations


HTML = """
<button id="go">go</button>
<p id="out"></p>
<script>
  document.querySelector('#go').addEventListener('click', async () => {
    const r = await fetch('https://api.example.local/m');
    const d = await r.json();
    document.querySelector('#out').textContent = d.msg;
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
        b = p.chromium.launch(headless=True)
        page = b.new_page()

        def last(route) -> None:  # type: ignore[no-untyped-def]
            route.fulfill(status=200, content_type="application/json", body='{"msg":"ok"}')

        def first(route) -> None:  # type: ignore[no-untyped-def]
            route.fallback()

        page.route("**/m", last)
        page.route("**/m", first)

        page.set_content(HTML)
        page.click("#go")
        print(page.locator("#out").inner_text())
        b.close()


if __name__ == "__main__":
    main()

