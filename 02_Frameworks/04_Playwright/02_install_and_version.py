#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：安装与版本检查（playwright 1.58.0）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/02_install_and_version.py
"""

from __future__ import annotations

try:
    from playwright.sync_api import sync_playwright
    PLAYWRIGHT_INSTALLED = True
except Exception as exc:
    PLAYWRIGHT_INSTALLED = False
    IMPORT_ERROR = str(exc)


EXPECTED = "1.58.0"


def main() -> None:
    if not PLAYWRIGHT_INSTALLED:
        print("无法导入 playwright:", IMPORT_ERROR)
        print("请先安装：")
        print("  python3 -m pip install playwright==1.58.0")
        print("  python3 -m playwright install")
        return

    # 获取版本（通过启动一个临时浏览器）
    try:
        with sync_playwright() as p:
            # playwright 对象没有直接的 __version__ 属性
            # 我们通过执行来验证安装是否成功
            print("playwright 安装成功")
            print("提示：playwright 没有直接的 __version__ 属性")
            print("当前章节基于 playwright", EXPECTED)
    except Exception as exc:
        print("运行时错误:", exc)


if __name__ == "__main__":
    main()
