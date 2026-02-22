#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：持久化上下文（launch_persistent_context）与 CDP 连接入门。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/03_persistent_context_and_cdp_intro.py

本示例展示 Playwright 的两个独立的高级特性：
1. launch_persistent_context(): 启动新浏览器，数据持久化到本地
2. connect_over_cdp(): 连接并接管一个已运行的浏览器

===========================================
第 1 部分：launch_persistent_context
===========================================

## 功能说明
- 启动一个新的浏览器实例
- 将浏览器数据持久化到本地目录
- 包括：cookies、localStorage、sessionStorage、缓存、IndexedDB 等
- 下次运行时会恢复之前的会话状态

## 常见用途
- 爬虫需要保持登录状态（多次运行无需重新登录）
- 跨脚本共享浏览器数据
- 模拟真实用户长期使用浏览器的行为

## 与普通 launch 的区别
- launch(): 每次都是全新浏览器，关闭后数据丢失
- launch_persistent_context(): 数据持久化到本地，可恢复

===========================================
第 2 部分：connect_over_cdp
===========================================

## 功能说明
- CDP (Chrome DevTools Protocol) 是 Chrome 的调试协议
- 连接并接管一个**已经在运行**的浏览器
- 该浏览器必须以调试模式启动（带 --remote-debugging-port 参数）

## 常见用途
- 调试：连接到手动打开的浏览器进行自动化操作
- 开发：在真实浏览器环境中测试脚本
- 混合操作：手动登录 + 自动化后续操作

## 如何启动带 CDP 的浏览器

# macOS / Linux:
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

# Windows:
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222

# 或使用 Chromium:
chromium --remote-debugging-port=9222
"""

from __future__ import annotations

import datetime
import time
from pathlib import Path

# 持久化数据保存目录
# 浏览器的 cookies、缓存等会保存在这里（脚本所在目录下）
USER_DATA_DIR = Path(__file__).parent / "persistent_profile"

# CDP 连接地址（默认 Chrome 调试端口）
CDP_ENDPOINT = "http://127.0.0.1:9222"

# 用于演示持久化的标记文件
# 通过检查这个文件是否存在，判断是否是第一次运行
FIRST_RUN_MARKER = USER_DATA_DIR / ".first_run_completed"


def demo_persistent_context() -> bool:
    """演示持久化上下文：启动新浏览器，数据保存到本地

    Returns:
        bool: 是否执行成功
    """
    print("=" * 60)
    print("第 1 部分：持久化上下文 (launch_persistent_context)")
    print("=" * 60)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"\n✗ 无法导入 playwright: {exc}")
        print("请先安装：python3 -m pip install playwright==1.58.0")
        print("并执行：python3 -m playwright install")
        return False

    # 确保持久化目录存在
    USER_DATA_DIR.mkdir(parents=True, exist_ok=True)

    # 检查是否是第一次运行
    is_first_run = not FIRST_RUN_MARKER.exists()

    print(f"\n用户数据目录: {USER_DATA_DIR}")
    if is_first_run:
        print("状态: 首次运行，将创建数据并保存")
    else:
        print("状态: 非首次运行，将恢复之前保存的数据")

    try:
        with sync_playwright() as p:
            # 启动持久化上下文
            context = p.chromium.launch_persistent_context(
                user_data_dir=str(USER_DATA_DIR),
                headless=True,
            )

            print("\n1. 浏览器已启动")
            print(f"   - 当前上下文页面数: {len(context.pages)}")

            # 创建新页面
            if not context.pages:
                page = context.new_page()
            else:
                page = context.pages[0]

            # 使用真实网站演示数据持久化
            # httpbin.org 是一个用于测试 HTTP 请求的公共网站
            print("\n2. 访问真实网站演示数据持久化")
            print("   - 访问: https://httpbin.org/cookies/set?demo_user=visit_001")

            try:
                page.goto("https://httpbin.org/cookies/set?demo_user=visit_001")
                # 等待页面加载完成（使用 load 而非 networkidle，更稳定）
                page.wait_for_load_state("load", timeout=10000)
            except Exception as exc:
                print(f"   ✗ 访问网站失败: {exc}")
                print("   提示: 请检查网络连接或稍后重试")
                context.close()
                return False

            # 验证 cookies 是否被设置
            cookies = context.cookies()
            demo_cookie = next((c for c in cookies if c["name"] == "demo_user"), None)

            print(f"\n3. Cookies 验证:")
            print(f"   - 总 cookies 数: {len(cookies)}")
            if demo_cookie:
                print(f"   - demo_user 值: {demo_cookie['value']}")
            else:
                print(f"   - demo_user: (未设置)")

            # 如果是第一次运行，创建标记文件
            if is_first_run:
                FIRST_RUN_MARKER.touch()
                print(f"\n4. [首次运行] 标记文件已创建，下次运行将恢复数据")
            else:
                print(f"\n4. [非首次运行] 数据已从本地恢复")

            context.close()
            print(f"\n5. 浏览器已关闭，数据已保存到本地目录")
            print(f"   - 再次运行脚本将看到数据被恢复")
            print(f"   - 如需重置，删除目录: {USER_DATA_DIR}\n")

    except Exception as exc:
        print(f"\n✗ 发生错误: {exc}")
        return False

    return True


def demo_connect_over_cdp() -> bool:
    """演示 CDP 连接：接管已运行的浏览器

    Returns:
        bool: 是否连接成功
    """
    print("=" * 60)
    print("第 2 部分：CDP 连接 (connect_over_cdp)")
    print("=" * 60)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"\n✗ 无法导入 playwright: {exc}")
        print("请先安装：python3 -m pip install playwright==1.58.0")
        print("并执行：python3 -m playwright install")
        return False

    print(f"\nCDP 端点: {CDP_ENDPOINT}")
    print("\n使用前需要先启动带调试端口的浏览器：")
    print("  macOS:")
    print("    /Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome \\")
    print("    --remote-debugging-port=9222")
    print("  Windows:")
    print("    chrome.exe --remote-debugging-port=9222")
    print("  Linux:")
    print("    chromium --remote-debugging-port=9222\n")

    try:
        with sync_playwright() as p:
            # 多次尝试连接，给用户时间启动浏览器
            max_retries = 3
            connected = False

            for attempt in range(1, max_retries + 1):
                if attempt > 1:
                    print(f"\n等待 3 秒后重试 ({attempt}/{max_retries})...")
                    time.sleep(3)

                try:
                    print(f"尝试连接到已有浏览器 (第 {attempt} 次)...")
                    browser = p.chromium.connect_over_cdp(CDP_ENDPOINT)
                    connected = True
                    break
                except Exception as exc:
                    if attempt < max_retries:
                        print(f"  ✗ 连接失败: {exc}")
                        print("  提示: 请在另一个终端启动带调试端口的浏览器")
                    else:
                        print(f"  ✗ 连接失败: {exc}")
                        print("\n可能的原因:")
                        print("    1. 没有启动带 --remote-debugging-port=9222 的浏览器")
                        print("    2. 端口 9222 被其他程序占用")
                        print("    3. 防火墙阻止了连接")
                        return False

            if not connected:
                return False

            print("\n✓ 连接成功!")

            # 多次确认连接信息
            print("\n" + "-" * 40)
            print("确认 1: 浏览器基本信息")
            print("-" * 40)
            print(f"  浏览器版本: {browser.version}")
            print(f"  是否已连接: {browser.is_connected()}")

            # 获取当前上下文
            contexts = browser.contexts
            print(f"\n确认 2: 上下文信息")
            print(f"  上下文数量: {len(contexts)}")

            if contexts:
                first_context = contexts[0]
                pages = first_context.pages
                print(f"\n确认 3: 页面信息")
                print(f"  页面数量: {len(pages)}")

                if pages:
                    for i, pg in enumerate(pages, 1):
                        print(f"\n  页面 {i}:")
                        print(f"    URL: {pg.url}")
                        try:
                            title = pg.title()
                            print(f"    标题: {title}")
                        except Exception:
                            print(f"    标题: (无法获取)")

            # 尝试截图（如果浏览器有页面）
            if contexts and contexts[0].pages:
                try:
                    # 使用时间戳避免文件名冲突
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    screenshot_path = Path(__file__).parent / f"cdp_screenshot_{timestamp}.png"
                    contexts[0].pages[0].screenshot(path=str(screenshot_path))
                    print(f"\n确认 4: 截图已保存")
                    print(f"  路径: {screenshot_path}")
                except Exception as exc:
                    print(f"\n确认 4: 截图失败 ({exc})")

            print("\n" + "-" * 40)
            print("提示: 浏览器将继续运行，连接即将关闭...")
            browser.close()
            print("\n连接已关闭，浏览器仍保持运行")

    except Exception as exc:
        print(f"\n✗ 发生错误: {exc}")
        return False

    return True


def main() -> None:
    # 检查 playwright 是否已安装
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"✗ 无法导入 playwright: {exc}")
        print("\n请先安装 Playwright:")
        print("  1. python3 -m pip install playwright==1.58.0")
        print("  2. python3 -m playwright install")
        return

    # 执行结果记录
    results = {
        "persistent_context": False,
        "cdp_connection": False,
    }

    # 演示 1：持久化上下文
    results["persistent_context"] = demo_persistent_context()

    # 演示 2：CDP 连接
    results["cdp_connection"] = demo_connect_over_cdp()

    # 总结
    print("\n" + "=" * 60)
    print("演示完成！")
    print("=" * 60)

    # 根据执行结果输出不同的总结
    print("\n执行结果:")
    print(f"  1. 持久化上下文: {'✓ 成功' if results['persistent_context'] else '✗ 失败'}")
    print(f"  2. CDP 连接:     {'✓ 成功' if results['cdp_connection'] else '✗ 失败'}")

    if results["persistent_context"] or results["cdp_connection"]:
        print("\n核心知识点:")
        if results["persistent_context"]:
            print("  1. launch_persistent_context")
            print("     -> 启动新浏览器")
            print("     -> 数据保存到本地目录")
            print("     -> 下次运行时自动恢复")
        if results["cdp_connection"]:
            print("  2. connect_over_cdp")
            print("     -> 连接并接管已运行的浏览器")
            print("     -> 浏览器需以 --remote-debugging-port=9222 启动")
            print("     -> 适用于调试和混合操作场景")


if __name__ == "__main__":
    main()
