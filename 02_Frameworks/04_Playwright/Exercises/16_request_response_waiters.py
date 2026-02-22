#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 16：expect_request / expect_response。
Author: Lambert
"""

from __future__ import annotations


HTML = """
<button id="load">load</button>
<p id="out"></p>
<script>
  document.querySelector('#load').addEventListener('click', async () => {
    const r = await fetch('https://api.example.local/x');
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
        page.route(
            "**/x",
            lambda route: route.fulfill(
                status=200,
                content_type="application/json",
                body='{"msg":"ok-x"}',
            ),
        )
        page.set_content(HTML)

        with page.expect_request("**/x") as req_info:
            with page.expect_response("**/x") as resp_info:
                page.click("#load")

        print(req_info.value.method, resp_info.value.status)
        print(page.locator("#out").inner_text())
        b.close()


if __name__ == "__main__":
    main()

