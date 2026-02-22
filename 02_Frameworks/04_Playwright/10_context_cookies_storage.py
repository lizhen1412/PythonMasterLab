#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：context、cookie 与 storage_state。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/10_context_cookies_storage.py

本示例展示 BrowserContext 的状态管理功能：
1. add_cookies(): 添加 cookies
2. cookies(): 获取所有 cookies
3. storage_state(): 保存状态到文件

核心概念：
- BrowserContext 类似于浏览器的隐身模式
- 每个 context 有独立的 cookie、localStorage、sessionStorage 等
- storage_state() 可以保存和恢复整个上下文的状态
- 保存的状态文件包含：cookies、localStorage、sessionStorage 等

常见用途：
- 保持登录状态：保存登录后的 cookies，下次直接恢复
- 测试隔离：不同测试用独立的 context，互不干扰
- 状态复用：在不同脚本间共享浏览器状态

storage_state 文件格式：
{
  "cookies": [...],
  "origins": [
    {
      "origin": "https://example.com",
      "localStorage": [...]
    }
  ]
}
"""

from __future__ import annotations

from pathlib import Path


# 状态文件保存路径
# cookies、localStorage 等将保存在这个文件中
STATE_PATH = Path("/tmp/playwright_demo/storage_state.json")


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    # 确保输出目录存在
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = None
        try:
            context = browser.new_context()

            # === 添加 cookies ===
            # add_cookies() 接受一个 cookie 对象列表
            # 每个 cookie 包含：name、value、domain、path 等属性
            context.add_cookies([
                {
                    "name": "session_id",
                    "value": "abc123",
                    "domain": "example.local",
                    "path": "/",
                    "httpOnly": True,  # 只能通过 HTTP 访问
                    "secure": False,   # 不需要 HTTPS
                }
            ])

            # === 获取所有 cookies ===
            # cookies() 返回上下文中的所有 cookies
            cookies = context.cookies()
            print("cookies count ->", len(cookies))
            print("cookies ->", cookies)

            # === 保存状态到文件 ===
            # storage_state() 将整个上下文状态保存到文件
            # 包括：cookies、localStorage、sessionStorage 等
            context.storage_state(path=str(STATE_PATH))
            print("\nstorage_state ->", STATE_PATH)
            print("提示: 可以使用 storage_state() 加载保存的状态")

            # 显示保存的文件内容摘要
            if STATE_PATH.exists():
                import json
                state = json.loads(STATE_PATH.read_text())
                print(f"\n保存的状态包含:")
                print(f"  - cookies: {len(state.get('cookies', []))} 个")
                print(f"  - origins: {len(state.get('origins', []))} 个")
        finally:
            if context:
                context.close()
            browser.close()


if __name__ == "__main__":
    main()
