#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 38：keyboard / mouse 设备操作。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/38_keyboard_mouse_actions.py

本示例展示如何模拟键盘和鼠标操作：
1. page.keyboard: 键盘操作
2. page.mouse: 鼠标操作

核心概念：
- Playwright 可以精确模拟键盘和鼠标输入
- 支持所有标准按键和鼠标操作
- 适合测试需要复杂交互的场景

Keyboard 方法：
- type(text): 逐字符输入
- press(key): 按下按键（Enter、Tab 等）
- down(key): 按下按键不释放
- up(key): 释放按键
- insert_text(text): 直接插入文本

Mouse 方法：
- click(x, y): 点击指定坐标
- dblclick(x, y): 双击
- move(x, y): 移动鼠标
- down(button): 按下鼠标键
- up(button): 释放鼠标键
- wheel(delta_x, delta_y): 滚轮

常用按键：
- Enter、Tab、Backspace、Delete
- ArrowUp、ArrowDown、ArrowLeft、ArrowRight
- Shift、Control、Alt、Meta
- F1-F12

鼠标按钮：
- left: 左键
- right: 右键
- middle: 中键
"""

from __future__ import annotations


HTML = """
<label for="txt">Text</label>
<input id="txt" />

<div id="pad" style="margin-top:12px;width:180px;height:80px;background:#e6f4ff;border:1px solid #6aa7d9;">
  PAD
</div>

<p id="keyboard"></p>
<p id="mouse"></p>

<script>
  const txt = document.querySelector('#txt');
  const keyboardOut = document.querySelector('#keyboard');
  txt.addEventListener('input', () => {
    keyboardOut.textContent = txt.value;
  });

  const pad = document.querySelector('#pad');
  const mouseOut = document.querySelector('#mouse');
  let clickCount = 0;
  pad.addEventListener('click', () => {
    clickCount += 1;
    mouseOut.textContent = `click=${clickCount}`;
  });
  pad.addEventListener('dblclick', () => {
    mouseOut.textContent += '|dbl';
  });
  pad.addEventListener('wheel', () => {
    mouseOut.textContent += '|wheel';
  });
</script>
"""


def main() -> None:
    try:
        from playwright.sync_api import expect, sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        text_input = page.get_by_label("Text")
        text_input.click()

        # === 键盘操作 ===
        page.keyboard.type("ab")
        page.keyboard.press("Backspace")
        page.keyboard.down("Shift")
        page.keyboard.type("z")
        page.keyboard.up("Shift")
        page.keyboard.insert_text("!")

        expect(page.locator("#keyboard")).to_have_text("aZ!")

        # === 鼠标操作 ===
        center = page.evaluate(
            """
            () => {
              const r = document.querySelector('#pad').getBoundingClientRect();
              return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
            }
            """
        )
        x = float(center["x"])
        y = float(center["y"])

        page.mouse.move(x, y)
        page.mouse.click(x, y)
        page.mouse.dblclick(x, y)
        page.mouse.wheel(0, 100)

        page.wait_for_timeout(120)
        expect(page.locator("#mouse")).to_contain_text("click=")
        expect(page.locator("#mouse")).to_contain_text("dbl")

        print("keyboard ->", page.locator("#keyboard").inner_text())
        print("mouse ->", page.locator("#mouse").inner_text())

        browser.close()


if __name__ == "__main__":
    main()

