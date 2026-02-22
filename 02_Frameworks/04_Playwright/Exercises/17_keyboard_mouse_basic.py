#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 17：keyboard / mouse 基础。
Author: Lambert
"""

from __future__ import annotations


HTML = """
<label for="in">Input</label><input id="in" />
<div id="pad" style="width:120px;height:60px;border:1px solid #555;margin-top:10px;"></div>
<p id="k"></p>
<p id="m"></p>
<script>
  const inp = document.querySelector('#in');
  const outK = document.querySelector('#k');
  inp.addEventListener('input', () => outK.textContent = inp.value);
  const outM = document.querySelector('#m');
  let c = 0;
  const pad = document.querySelector('#pad');
  pad.addEventListener('click', () => { c += 1; outM.textContent = `c=${c}`; });
  pad.addEventListener('dblclick', () => { outM.textContent += '|d'; });
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
        page.set_content(HTML)

        page.get_by_label("Input").click()
        page.keyboard.type("ab")
        page.keyboard.press("Backspace")
        page.keyboard.insert_text("!")
        print("k ->", page.locator("#k").inner_text())

        center = page.evaluate(
            "() => { const r = document.querySelector('#pad').getBoundingClientRect(); return [r.left+r.width/2, r.top+r.height/2]; }"
        )
        x, y = float(center[0]), float(center[1])
        page.mouse.move(x, y)
        page.mouse.click(x, y)
        page.mouse.dblclick(x, y)
        page.wait_for_timeout(100)
        print("m ->", page.locator("#m").inner_text())
        b.close()


if __name__ == "__main__":
    main()

