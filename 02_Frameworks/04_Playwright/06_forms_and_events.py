#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：表单输入、点击、事件监听。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/06_forms_and_events.py

本示例展示如何与表单元素交互和执行 JavaScript：
1. fill(): 填写输入框
2. click(): 点击按钮
3. evaluate(): 在浏览器中执行 JavaScript 代码
4. locator(): 定位元素获取结果

核心概念：
- fill() 会自动清空输入框的现有内容，然后输入新文本
- click() 会等待元素可点击（可见、启用、不在动画中）
- evaluate() 可以执行任意 JavaScript，访问浏览器环境
- 可以通过 window 对象在 JS 和 Python 之间传递数据
"""

from __future__ import annotations


# 模拟一个包含表单和 JavaScript 事件的 HTML 页面
HTML = """
<form>
  <label>Name <input id="name" /></label>
  <button id="btn" type="button">Submit</button>
  <p id="out"></p>
</form>
<script>
  // 使用 window 对象存储点击计数（方便从 Playwright 访问）
  window.__clicked = 0;

  // 为按钮添加点击事件监听器
  document.querySelector('#btn').addEventListener('click', () => {
    window.__clicked += 1;                      // 增加点击计数
    const name = document.querySelector('#name').value;  // 获取输入框的值
    document.querySelector('#out').textContent = `hello, ${name}`;  // 输出问候语
  });
</script>
"""


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()

            # 设置页面内容
            page.set_content(HTML)

            # === 表单交互 ===
            # fill() 用于填写输入框
            # 会自动：清空现有内容、聚焦元素、输入文本、触发 change 事件
            page.fill("#name", "Lambert")

            # click() 用于点击按钮
            # Playwright 会自动等待元素可点击（可见、启用）
            page.click("#btn")

            # === 获取结果 ===
            # 使用 locator 定位输出元素，获取其文本内容
            out = page.locator("#out").inner_text()
            print("output ->", out)

            # === 执行 JavaScript ===
            # evaluate() 在浏览器上下文中执行 JavaScript
            # 可以访问页面的 window、document 等对象
            # 这里我们读取 window.__clicked 的值
            clicked = page.evaluate("() => window.__clicked")
            print("clicked ->", clicked)

            # === 断言验证 ===
            assert out == "hello, Lambert", f"输出应该是 'hello, Lambert'，实际是 '{out}'"
            assert clicked == 1, f"点击次数应该是 1，实际是 {clicked}"

            print("测试通过！")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
