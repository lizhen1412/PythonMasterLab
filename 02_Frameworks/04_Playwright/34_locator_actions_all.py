#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 34：locator 常见动作全示例。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/34_locator_actions_all.py

本示例展示 locator 的常见操作方法：
1. fill(): 填写输入框
2. check()/uncheck(): 勾选/取消复选框
3. select_option(): 选择下拉选项
4. set_input_files(): 上传文件
5. hover(): 鼠标悬停
6. click(): 点击元素
7. focus(): 聚焦元素
8. press(): 按键

核心概念：
- locator 对象封装了元素定位和操作
- 所有操作都自动等待元素可交互
- 支持链式调用

常见操作方法：
- fill(value): 填写文本
- clear(): 清空输入
- check(): 勾选复选框/单选框
- uncheck(): 取消勾选
- select_option(value/label/index): 选择下拉选项
- set_input_files(files): 上传文件
- click(): 点击
- dblclick(): 双击
- hover(): 悬停
- focus(): 聚焦
- press(key): 按键（Enter、Tab 等）
- type(text): 逐字符输入

语义化定位器：
- get_by_label(): 按标签文本定位
- get_by_role(): 按 ARIA 角色定位
- get_by_placeholder(): 按占位符定位
- get_by_text(): 按文本内容定位
"""

from __future__ import annotations

from pathlib import Path


# 上传文件路径
UPLOAD_FILE = Path("/tmp/playwright_demo/locator_upload.txt")


# 模拟包含表单元素的 HTML
HTML = """
<form>
  <label for="name">Name</label>
  <input id="name" />

  <label>
    <input id="agree" type="checkbox" />
    Agree terms
  </label>

  <label for="level">Level</label>
  <select id="level">
    <option value="bronze">bronze</option>
    <option value="silver">silver</option>
    <option value="gold">gold</option>
  </select>

  <input id="file" type="file" />
  <button id="submit" type="button">Submit</button>

  <p id="hover-state"></p>
  <p id="key-state"></p>
  <p id="file-name"></p>
  <p id="status"></p>
</form>

<script>
  const submit = document.querySelector('#submit');
  const name = document.querySelector('#name');
  const agree = document.querySelector('#agree');
  const level = document.querySelector('#level');
  const file = document.querySelector('#file');

  submit.addEventListener('mouseenter', () => {
    document.querySelector('#hover-state').textContent = 'hovered';
  });

  name.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      document.querySelector('#key-state').textContent = 'enter-pressed';
    }
  });

  file.addEventListener('change', (e) => {
    const files = e.target.files;
    document.querySelector('#file-name').textContent = files.length ? files[0].name : '';
  });

  submit.addEventListener('click', () => {
    document.querySelector('#status').textContent = `${name.value}|agree=${agree.checked}|level=${level.value}`;
  });
</script>
"""


def main() -> None:
    try:
        from playwright.sync_api import expect, sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    # 创建测试文件
    UPLOAD_FILE.parent.mkdir(parents=True, exist_ok=True)
    UPLOAD_FILE.write_text("upload-demo", encoding="utf-8")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()
            page.set_content(HTML)

            # === 使用语义化定位器 ===
            name_input = page.get_by_label("Name")
            agree_checkbox = page.get_by_label("Agree terms")
            level_select = page.get_by_label("Level")
            file_input = page.locator("#file")
            submit_button = page.get_by_role("button", name="Submit")

            # === fill(): 填写输入框 ===
            name_input.fill("Lambert")
            name_input.focus()
            name_input.press("Enter")

            # === check()/uncheck(): 复选框操作 ===
            agree_checkbox.check()
            print("checked ->", page.evaluate("() => document.querySelector('#agree').checked"))
            agree_checkbox.uncheck()
            print("unchecked ->", not page.evaluate("() => document.querySelector('#agree').checked"))
            agree_checkbox.check()

            # === select_option(): 下拉选择 ===
            level_select.select_option("gold")

            # === set_input_files(): 文件上传 ===
            file_input.set_input_files(str(UPLOAD_FILE))

            # === hover(): 鼠标悬停 ===
            submit_button.hover()
            submit_button.click()

            # === 验证结果 ===
            expect(page.locator("#hover-state")).to_have_text("hovered")
            expect(page.locator("#key-state")).to_have_text("enter-pressed")
            expect(page.locator("#file-name")).to_have_text(UPLOAD_FILE.name)
            expect(page.locator("#status")).to_have_text("Lambert|agree=true|level=gold")

            print("[OK] locator 常见动作执行完成")
        finally:
            browser.close()


if __name__ == "__main__":
    main()

