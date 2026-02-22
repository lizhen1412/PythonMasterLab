#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 29：pytest 插件用法（含 fixture/hook）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/29_pytest_plugin_basics.py

本示例展示如何使用 Playwright 的 pytest 插件：
1. pytest-playwright: Playwright 官方 pytest 集成
2. Page fixture: 自动创建和清理浏览器页面
3. conftest.py: pytest 配置文件，支持自定义 fixtures

核心概念：
- pytest-playwright 提供了 pytest 集成
- 自动处理浏览器启动和清理
- 支持多种浏览器和配置选项
- 可以使用 pytest 的断言和 fixture 机制

内置 Fixtures：
- browser: 浏览器实例
- browser_context: 浏览器上下文
- page: 页面实例（最常用）
- browser_type_launch_args: 浏览器启动参数
- browser_context_args: 上下文参数

pytest 命令行参数：
- --headed: 显示浏览器窗口
- --browser: 选择浏览器（chromium/firefox/webkit）
- --slowmo: 减慢操作速度（毫秒）
- --tracing: 开启/关闭 trace 记录
- --video: 视频录制选项

conftest.py 用途：
- 定义自定义 fixtures
- 配置测试钩子（setup/teardown）
- 设置测试参数和选项

常见用法：
- 使用 autouse fixture 自动执行设置
- 使用@pytest.mark.parametrize 参数化测试
- 使用 --browser 跨浏览器测试
"""

from __future__ import annotations


SAMPLE_TEST = """
from playwright.sync_api import Page, expect


def test_official_style(page: Page) -> None:
    page.goto(\"data:text/html,<title>Demo</title><a href='#x'>Get started</a><h1 id='x'>Installation</h1>\")
    expect(page).to_have_title(\"Demo\")
    page.get_by_role(\"link\", name=\"Get started\").click()
    expect(page).to_have_url(\"**#x\")
    expect(page.get_by_role(\"heading\", name=\"Installation\")).to_be_visible()
""".strip()


SAMPLE_CONFTEST = """
import pytest
from playwright.sync_api import Page


@pytest.fixture(autouse=True)
def goto_data_home(page: Page) -> None:
    page.goto(\"data:text/html,<title>Home</title><h1>home</h1>\")
""".strip()


def main() -> None:
    print("== pytest + playwright 最小工程骨架 ==\n")

    print("1) tests/test_demo.py：\n")
    print(SAMPLE_TEST)

    print("\n2) tests/conftest.py（可选，演示 autouse fixture）：\n")
    print(SAMPLE_CONFTEST)

    print("\n3) 安装与运行命令：")
    print("python3 -m pip install pytest pytest-playwright playwright==1.58.0")
    print("python3 -m playwright install")
    print("pytest -q tests/test_demo.py")

    print("\n4) 常用调试参数：")
    print("pytest --headed --browser webkit -q tests/test_demo.py")
    print("pytest --slowmo 300 -q tests/test_demo.py")
    print("pytest --tracing on -q tests/test_demo.py")


if __name__ == "__main__":
    main()
