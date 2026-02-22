#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 14：locator 常见动作。
Author: Lambert
"""

from __future__ import annotations

from pathlib import Path


UPLOAD = Path("/tmp/playwright_demo/ex14.txt")

HTML = """
<label for="name">Name</label>
<input id="name" />
<label><input id="agree" type="checkbox" />Agree</label>
<label for="lv">Level</label>
<select id="lv">
  <option value="a">a</option>
  <option value="b">b</option>
</select>
<input id="file" type="file" />
<button id="ok" type="button">OK</button>
<p id="out"></p>
<script>
  const ok = document.querySelector('#ok');
  ok.addEventListener('click', () => {
    const n = document.querySelector('#name').value;
    const a = document.querySelector('#agree').checked;
    const lv = document.querySelector('#lv').value;
    document.querySelector('#out').textContent = `${n}|${a}|${lv}`;
  });
</script>
"""


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:
        print(f"playwright import failed: {exc}")
        return

    UPLOAD.parent.mkdir(parents=True, exist_ok=True)
    UPLOAD.write_text("hello", encoding="utf-8")

    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        page = b.new_page()
        page.set_content(HTML)

        page.get_by_label("Name").fill("lz")
        page.get_by_label("Name").focus()
        page.get_by_label("Name").press("Enter")

        box = page.get_by_label("Agree")
        box.check()
        box.uncheck()
        box.check()

        page.get_by_label("Level").select_option("b")
        page.locator("#file").set_input_files(str(UPLOAD))

        button = page.get_by_role("button", name="OK")
        button.hover()
        button.click()

        print(page.locator("#out").inner_text())
        b.close()


if __name__ == "__main__":
    main()

