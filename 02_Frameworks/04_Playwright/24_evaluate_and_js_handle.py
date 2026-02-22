#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 24：evaluate 与 JSHandle。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/24_evaluate_and_js_handle.py

本示例展示如何在 Playwright 中执行 JavaScript 代码：
1. page.evaluate(): 执行 JavaScript 并返回结果
2. page.evaluate_handle(): 执行 JavaScript 并返回 JSHandle
3. handle.json_value(): 将 JSHandle 转换为 Python 对象

核心概念：
- evaluate() 用于在浏览器中执行 JavaScript 代码
- 可以访问页面的 DOM、window、document 等
- 返回的值会自动转换为 Python 类型
- evaluate_handle() 用于处理无法序列化的 JavaScript 对象

evaluate() 的用法：
- page.evaluate("javascript code"): 执行 JS 表达式
- page.evaluate("() => document.title"): 获取页面标题
- page.evaluate("(x, y) => x + y", a, b): 传递参数
- 返回值会被自动序列化（JSON）

evaluate_handle() 的用法：
- 返回 JSHandle 对象，代表页面中的 JavaScript 对象
- 适合处理 DOM 元素、复杂对象等
- handle.json_value(): 转换为 Python 对象
- handle.dispose(): 释放资源

JSHandle vs ElementHandle：
- JSHandle: 任意 JavaScript 对象的引用
- ElementHandle: DOM 元素的引用（JSHandle 的子类）
- ElementHandle 有额外的 DOM 操作方法

常见用途：
- 访问页面变量和函数
- 执行自定义 JavaScript 逻辑
- 获取计算后的样式或属性
- 与页面 JavaScript 代码交互
"""

from __future__ import annotations


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
            page.set_content("<h2>eval demo</h2>")

            # === evaluate(): 执行 JavaScript 并返回结果 ===
            # evaluate() 在浏览器上下文中执行 JavaScript
            # 返回值会自动转换为 Python 类型
            # 适合简单表达式和可序列化的值
            value = page.evaluate("() => 1 + 2 + 3")
            print("evaluate result ->", value)

            # === evaluate_handle(): 执行 JavaScript 并返回 JSHandle ===
            # evaluate_handle() 返回 JSHandle 对象
            # 适合处理复杂对象、DOM 元素等无法直接序列化的值
            handle = page.evaluate_handle("() => ({name: 'pw', version: '1.58.0'})")
            # json_value() 将 JSHandle 转换为 Python 字典
            data = handle.json_value()
            print("handle json ->", data)
            # 使用完 JSHandle 后需要手动释放
            handle.dispose()
        finally:
            browser.close()


if __name__ == "__main__":
    main()
