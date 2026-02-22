#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 52：Accessibility、Coverage 和其他高级 API（完整覆盖）。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/52_accessibility_other_advanced.py

本示例演示 Playwright 的以下高级 API：

## Accessibility（无障碍）
1. page.accessibility.snapshot(): 获取无障碍树
2. AXNode 属性：role, name, value, checked, expanded 等

## ARIA Snapshot
1. locator.aria_snapshot(): 生成 ARIA 快照
2. expect(locator).to_match_aria_snapshot(): 匹配 ARIA 快照

## Code Coverage（代码覆盖率）
1. page.start_js_coverage() / stop_js_coverage(): JavaScript 覆盖率
2. page.start_css_coverage() / stop_css_coverage(): CSS 覆盖率
3. 覆盖率结果分析

## PDF 生成
1. page.pdf(): 生成 PDF 文档
2. PDF 格式、页边距、页眉页脚配置
3. 选择器转 PDF

## Video 录制
1. record_video_dir: 视频录制目录
2. video.path(): 视频文件路径
3. 视频大小和质量控制

## Console 高级用法
1. ConsoleMessage 类型、参数、位置
2. ConsoleMessage API
3. Worker 中的 console 消息

## Locator 高级选择器
1. get_by_text, get_by_role, get_by_label
2. get_by_placeholder, get_by_alt_text
3. get_by_title, get_by_test_id

## 涉及的 Playwright API
- accessibility.snapshot: 无障碍树快照
- locator.aria_snapshot: ARIA 快照
- page.start_js_coverage/stop_js_coverage: JS 覆盖率
- page.start_css_coverage/stop_css_coverage: CSS 覆盖率
- page.pdf: 生成 PDF
- record_video_dir: 视频录制
- console_message.text/type/args: Console 消息
- locator.get_by_*, page.get_by_*: 定位器方法
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any


# =============================================================================
# 统一使用 /tmp/playwright_demo 目录
# =============================================================================

PDF_DEMO_DIR = Path("/tmp/playwright_demo/pdf")
VIDEO_DEMO_DIR = Path("/tmp/playwright_demo/video")


# =============================================================================
# Accessibility（无障碍）示例
# =============================================================================


def example_01_accessibility_snapshot() -> None:
    """示例 01：Accessibility 快照基础"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html lang="en">
    <head><title>Accessibility Test</title></head>
    <body>
        <header>
            <nav aria-label="Main navigation">
                <ul>
                    <li><a href="/home">Home</a></li>
                    <li><a href="/about">About</a></li>
                </ul>
            </nav>
        </header>
        <main>
            <h1>Accessibility Testing</h1>
            <button id="btn1" aria-pressed="false">Toggle</button>
            <input type="checkbox" id="chk1" checked aria-label="Subscribe">
            <div role="progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
                50%
            </div>
            <article>
                <h2>Article Title</h2>
                <p>Article content goes here.</p>
            </article>
        </main>
        <footer>
            <p>&copy; 2024 Example</p>
        </footer>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # === 获取完整无障碍树 ===
        snapshot = page.accessibility.snapshot()

        def print_ax_tree(node: dict, indent: int = 0) -> None:
            """递归打印无障碍树"""
            role = node.get("role", "")
            name = node.get("name", "")
            prefix = "  " * indent

            info = f"{prefix}{role}"
            if name:
                info += f": {name}"

            # 其他属性
            if node.get("checked"):
                info += f" [checked={node['checked']}]"
            if node.get("expanded") is not None:
                info += f" [expanded={node['expanded']}]"
            if node.get("value"):
                info += f" [value={node['value']}]"

            print(info)

            # 递归处理子节点
            for child in node.get("children", []):
                print_ax_tree(child, indent + 1)

        print("无障碍树:")
        print_ax_tree(snapshot)

        browser.close()


def example_02_accessibility_properties() -> None:
    """示例 02：Accessibility 节点属性详解"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html>
    <body>
        <button id="toggle" aria-pressed="false">Toggle Switch</button>
        <input type="range" id="slider" min="0" max="100" value="50" aria-label="Volume">
        <div role="combobox" aria-expanded="false" aria-haspopup="listbox" aria-controls="list">
            Select option
        </div>
        <ul id="list" role="listbox">
            <li role="option" aria-selected="true">Option 1</li>
            <li role="option">Option 2</li>
        </ul>
        <a href="#" aria-label="Read more" aria-describedby="desc">Continue reading</a>
        <span id="desc">Click to read the full article</span>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # === 获取特定元素的无障碍信息 ===
        snapshot = page.accessibility.snapshot()

        def find_role(node: dict, target_role: str) -> list[dict]:
            """查找特定 role 的节点"""
            results = []
            if node.get("role") == target_role:
                results.append(node)
            for child in node.get("children", []):
                results.extend(find_role(child, target_role))
            return results

        # 查找所有 button 节点
        buttons = find_role(snapshot, "button")
        for btn in buttons:
            print(f"\nButton 元素:")
            print(f"  Role: {btn.get('role')}")
            print(f"  Name: {btn.get('name')}")
            print(f"  Checked (pressed): {btn.get('checked')}")  # 对应 aria-pressed
            print(f"  Disabled: {btn.get('disabled')}")

        # 查找所有 slider (slider) 节点
        sliders = find_role(snapshot, "slider")
        for slider in sliders:
            print(f"\nSlider 元素:")
            print(f"  Role: {slider.get('role')}")
            print(f"  Name: {slider.get('name')}")
            print(f"  Value: {slider.get('value')}")
            print(f"  Min: {slider.get('minValue')}")
            print(f"  Max: {slider.get('maxValue')}")

        # === 使用 interestingOnly 选项 ===
        # interestingOnly=True: 只返回有趣的节点（默认）
        # interestingOnly=False: 返回所有节点
        snapshot_full = page.accessibility.snapshot(interesting_only=False)
        print(f"\n完整快照节点数（包含不可见）: {count_nodes(snapshot_full)}")
        snapshot_interesting = page.accessibility.snapshot(interesting_only=True)
        print(f"有趣快照节点数: {count_nodes(snapshot_interesting)}")

        browser.close()


def count_nodes(node: dict) -> int:
    """递归计算节点数量"""
    count = 1
    for child in node.get("children", []):
        count += count_nodes(child)
    return count


# =============================================================================
# ARIA Snapshot 示例
# =============================================================================


def example_03_aria_snapshot() -> None:
    """示例 03：ARIA Snapshot（可读性更好的快照）"""
    try:
        from playwright.sync_api import sync_playwright, expect
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html>
    <body>
        <nav aria-label="Main">
            <ul role="list">
                <li role="listitem"><a href="/home">Home</a></li>
                <li role="listitem"><a href="/about">About</a></li>
            </ul>
        </nav>
        <main>
            <h1>Page Title</h1>
            <article>
                <h2>Article Heading</h2>
                <p>Article content.</p>
            </article>
        </main>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # === locator.aria_snapshot() ===
        # 生成元素的 ARIA 快照（文本格式）
        nav_snapshot = page.locator("nav").aria_snapshot()
        print("Navigation ARIA Snapshot:")
        print(nav_snapshot)

        # === 完整页面快照 ===
        page_snapshot = page.locator("body").aria_snapshot()
        print("\n页面 ARIA Snapshot:")
        print(page_snapshot)

        # === 使用 expect 匹配 ARIA Snapshot ===
        # 可以验证快照是否匹配预期
        expect(page.locator("nav")).to_match_aria_snapshot("""
            - navigation "Main"
              - list
                - listitem
                  - link "Home"
                - listitem
                  - link "About"
        """)

        # === 序列化选项 ===
        # ARIA Snapshot 支持序列化选项
        article_snapshot = page.locator("article").aria_snapshot()
        print("\nArticle ARIA Snapshot:")
        print(article_snapshot)

        browser.close()


# =============================================================================
# Code Coverage（代码覆盖率）示例
# =============================================================================


def example_04_js_coverage() -> None:
    """示例 04：JavaScript 代码覆盖率"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html>
    <body>
        <h1>JS Coverage Test</h1>
        <button onclick="func1()">Function 1</button>
        <button onclick="func2()">Function 2</button>
        <button onclick="func3()">Function 3 (not called)</button>
        <script>
            function func1() {
                console.log('Function 1 called');
            }
            function func2() {
                console.log('Function 2 called');
            }
            function func3() {
                console.log('Function 3 called');
            }
        </script>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # === JavaScript 覆盖率 ===

        # 1. 开始覆盖率收集
        page.start_js_coverage()

        # 2. 加载页面并执行一些代码
        page.set_content(HTML)
        page.click("button:nth-child(1)")  # 调用 func1
        page.click("button:nth-child(2)")  # 调用 func2
        # func3 没有被调用

        # 3. 停止覆盖率收集
        coverage = page.stop_js_coverage()

        # 4. 分析覆盖率结果
        print("JavaScript 覆盖率:")
        total_bytes = 0
        used_bytes = 0

        for entry in coverage:
            url = entry.get("url", "unknown")
            ranges = entry.get("ranges", [])
            functions = entry.get("functions", [])

            # 计算覆盖率
            entry_used = sum(r.get("end", 0) - r.get("start", 0) for r in ranges)
            entry_total = entry.get("text_length", 0)

            total_bytes += entry_total
            used_bytes += entry_used

            if entry_total > 0:
                coverage_percent = (entry_used / entry_total) * 100
                print(f"\n{url}:")
                print(f"  覆盖率: {coverage_percent:.1f}%")
                print(f"  函数数: {len(functions)}")
                print(f"  覆盖的代码段: {len(ranges)}")

        if total_bytes > 0:
            total_coverage = (used_bytes / total_bytes) * 100
            print(f"\n总覆盖率: {total_coverage:.1f}%")

        browser.close()


def example_05_css_coverage() -> None:
    """示例 05：CSS 代码覆盖率"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            .used-class {
                color: blue;
            }
            .unused-class {
                color: red;
            }
            .another-used {
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <div class="used-class">Used Content</div>
        <div class="another-used">Another Used</div>
        <!-- unused-class 从未被使用 -->
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # === CSS 覆盖率 ===

        # 1. 开始覆盖率收集
        page.start_css_coverage()

        # 2. 加载页面
        page.set_content(HTML)
        page.wait_for_timeout(1000)  # 等待样式应用

        # 3. 停止覆盖率收集
        coverage = page.stop_css_coverage()

        # 4. 分析覆盖率结果
        print("CSS 覆盖率:")
        for entry in coverage:
            url = entry.get("url", "inline")
            ranges = entry.get("ranges", [])
            text_length = entry.get("length", 0)

            used_length = sum(r.get("end", 0) - r.get("start", 0) for r in ranges)
            coverage_percent = (used_length / text_length * 100) if text_length > 0 else 0

            print(f"\n{url}:")
            print(f"  覆盖率: {coverage_percent:.1f}%")
            print(f"  覆盖范围数: {len(ranges)}")

            # 打印已使用的样式
            if ranges:
                print("  已使用的样式范围:")
                for r in ranges:
                    start = r.get("start", 0)
                    end = r.get("end", 0)
                    # 实际应用中可以在这里获取并分析样式内容

        browser.close()


# =============================================================================
# PDF 生成示例
# =============================================================================


def example_06_pdf_generation() -> None:
    """示例 06：PDF 生成基础"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    output_path = PDF_DEMO_DIR / "example.pdf"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    HTML = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; }
            h1 { color: #333; }
            .content { margin: 20px; line-height: 1.6; }
            .footer { position: fixed; bottom: 0; width: 100%; text-align: center; }
        </style>
    </head>
    <body>
        <h1>PDF Generation Test</h1>
        <div class="content">
            <p>This is a test document for PDF generation.</p>
            <p>Playwright can convert HTML to PDF efficiently.</p>
            <ul>
                <li>Feature 1</li>
                <li>Feature 2</li>
                <li>Feature 3</li>
            </ul>
        </div>
        <div class="footer">Page 1</div>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # === 基础 PDF 生成 ===
        page.pdf(
            path=str(output_path),
            # 格式选项：'A4', 'A3', 'Letter', 'Legal', 'Tabloid', 'Ledger'
            format="A4",
            # 打印背景
            print_background=True,
        )

        print(f"PDF 已生成: {output_path}")

        browser.close()


def example_07_pdf_advanced_options() -> None:
    """示例 07：PDF 高级选项"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    output_dir = PDF_DEMO_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    HTML = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @page {
                margin: 20mm;
                @bottom-center {
                    content: "Page " counter(page) " of " counter(pages);
                }
            }
            body { font-family: 'Helvetica', sans-serif; }
            h1 { color: navy; }
            p { text-align: justify; }
            .page-break { page-break-after: always; }
        </style>
    </head>
    <body>
        <h1>Advanced PDF Options</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
        <div class="page-break"></div>
        <h1>Page 2</h1>
        <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco
        laboris nisi ut aliquip ex ea commodo consequat.</p>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # === 高级 PDF 选项 ===

        # 1. 带页眉页脚的 PDF
        page.pdf(
            path=str(output_dir / "with_header.pdf"),
            display_header_footer=True,
            header_template="<div style='font-size:10px;'>{title}</div>",
            footer_template="<div style='font-size:10px;'>Page {page} of {pages}</div>",
            margin={"top": "50px", "bottom": "50px", "left": "50px", "right": "50px"},
        )

        # 2. 横向 PDF
        page.pdf(
            path=str(output_dir / "landscape.pdf"),
            landscape=True,
        )

        # 3. 指定页码范围
        page.pdf(
            path=str(output_dir / "page_range.pdf"),
            page_ranges="1-2",  # 只生成前 2 页
        )

        # 4. 自定义页边距
        page.pdf(
            path=str(output_dir / "custom_margin.pdf"),
            margin={
                "top": "2cm",
                "right": "2cm",
                "bottom": "2cm",
                "left": "2cm",
            },
        )

        # 5. 使用 CSS 媒体类型
        page.pdf(
            path=str(output_dir / "print_media.pdf"),
            media="print",  # 或 "screen"
        )

        # 6. 指定纸张尺寸（单位可以是 px, in, cm, mm）
        page.pdf(
            path=str(output_dir / "custom_size.pdf"),
            width="210mm",
            height="297mm",
        )

        print(f"已生成多个 PDF 文件到: {output_dir}")

        browser.close()


def example_08_pdf_from_selector() -> None:
    """示例 08：从选择器生成 PDF"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    output_path = PDF_DEMO_DIR / "selector.pdf"

    HTML = """
    <!DOCTYPE html>
    <html>
    <body>
        <header>Header - Not Included</header>
        <div id="content">
            <h1>Content to Export</h1>
            <p>This content will be exported to PDF.</p>
        </div>
        <footer>Footer - Not Included</footer>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # === 只导出特定元素到 PDF ===
        page.locator("#content").pdf(path=str(output_path))

        print(f"从选择器生成 PDF: {output_path}")

        browser.close()


# =============================================================================
# Video 录制示例
# =============================================================================


def example_09_video_recording() -> None:
    """示例 09：Video 录制基础"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    video_dir = VIDEO_DEMO_DIR
    video_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        # === 配置视频录制 ===
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            # 视频录制目录
            record_video_dir=str(video_dir),

            # 视频大小
            record_video_size={"width": 1280, "height": 720},
        )

        page = context.new_page()

        # 执行一些操作，会被录制
        page.goto("https://example.com")
        page.wait_for_timeout(2000)
        page.click("h1")

        # 关闭上下文，视频会自动保存
        context.close()
        browser.close()

    # 查找生成的视频文件
    video_files = list(video_dir.glob("*.webm"))
    print(f"生成的视频文件:")
    for video in video_files:
        print(f"  - {video.name} ({video.stat().st_size} 字节)")


def example_10_video_access() -> None:
    """示例 10：访问 Video 对象"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    video_dir = VIDEO_DEMO_DIR

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir=str(video_dir),
        )

        page = context.new_page()
        page.goto("https://example.com")
        page.wait_for_timeout(1000)

        # === 访问当前页面的 Video 对象 ===
        video = page.video
        if video:
            # 获取视频文件路径
            video_path = video.path()
            print(f"视频文件路径: {video_path}")

        # 页面级别的 video 对象也可通过 context 获取
        context.close()
        browser.close()


# =============================================================================
# Console 高级示例
# =============================================================================


def example_11_console_message_api() -> None:
    """示例 11：ConsoleMessage API 详解"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Console Test</h1>
        <script>
            console.log('Regular log', {data: 'value'});
            console.warn('Warning message');
            console.error('Error occurred');
            console.info('Information');
            console.debug('Debug message');
            console.table([{a: 1}, {a: 2}]);
        </script>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 收集所有 console 消息
        console_messages: list[dict] = []

        def on_console(msg: Any) -> None:
            """处理 console 消息"""
            console_messages.append({
                "type": msg.type,
                "text": msg.text,
                "args": msg.args,
                "location": msg.location,
            })

            # 打印消息详情
            print(f"[Console {msg.type}] {msg.text}")

            # === ConsoleMessage API ===
            # msg.type: 消息类型 ("log", "warning", "error", "info", "debug")
            # msg.text: 消息文本
            # msg.args: 参数列表 (JSHandle 对象)
            # msg.location: 消息来源位置 {url, lineNumber, columnNumber}
            # msg.page: 关联的 Page（如果是来自 Worker 则为 None）

            # 访问参数
            if msg.args:
                for i, arg in enumerate(msg.args):
                    try:
                        value = arg.json_value()
                        print(f"  Arg[{i}]: {value}")
                    except Exception:
                        print(f"  Arg[{i}]: (复杂对象)")

        page.on("console", on_console)

        page.set_content(HTML)
        page.wait_for_timeout(1000)

        print(f"\n共收集到 {len(console_messages)} 条 console 消息")

        # === 按类型统计 ===
        type_counts: dict[str, int] = {}
        for msg in console_messages:
            type_counts[msg["type"]] = type_counts.get(msg["type"], 0) + 1

        print("\n消息类型统计:")
        for msg_type, count in type_counts.items():
            print(f"  {msg_type}: {count}")

        browser.close()


def example_12_console_with_worker() -> None:
    """示例 12：Worker 中的 Console 消息"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Worker Console Test</h1>
        <script>
            const worker = new Worker(URL.createObjectURL(new Blob([`
                console.log('Worker log 1');
                console.warn('Worker warning');
                console.error('Worker error');
            `], {type: 'application/javascript'})));

            worker.onmessage = function(e) {
                console.log('Main thread received:', e.data);
            };
        </script>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Page 的 console 消息
        def on_page_console(msg: Any) -> None:
            print(f"[Page Console {msg.type}] {msg.text}")

        page.on("console", on_page_console)

        # === Worker 的 console 消息 ===
        # Worker 中的 console 不会触发 page 的 console 事件
        # 需要监听 worker 的 console 事件

        def on_worker(worker: Any) -> None:
            """Worker 创建事件"""
            print(f"Worker 创建: {worker.url}")

            def on_worker_console(msg: Any) -> None:
                print(f"[Worker Console {msg.type}] {msg.text}")

            worker.on("console", on_worker_console)

        page.on("worker", on_worker)

        page.set_content(HTML)
        page.wait_for_timeout(2000)

        browser.close()


# =============================================================================
# Locator 高级选择器示例
# =============================================================================


def example_13_locator_get_by_methods() -> None:
    """示例 13：locator.get_by_* 系列方法"""
    try:
        from playwright.sync_api import sync_playwright, expect
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Locator Methods Test</h1>

        <!-- Text -->
        <p>Find me by text content</p>
        <a href="/link">Click here</a>

        <!-- Role -->
        <button>Submit Button</button>
        <input type="text" placeholder="Enter your name">
        <input type="email" placeholder="Enter email">

        <!-- Label -->
        <label>
            Username:
            <input type="text" id="username">
        </label>

        <!-- Alt text -->
        <img src="logo.png" alt="Company Logo">
        <img src="icon.png" alt="Menu Icon">

        <!-- Title -->
        <div title="Tooltip text">Hover me</div>

        <!-- Test ID -->
        <button data-testid="submit-btn">Submit Form</button>
        <input data-testid="username-input">

        <!-- ARIA attributes -->
        <nav aria-label="Main Menu">
            <a href="/home">Home</a>
        </nav>

        <!-- Placeholder -->
        <input type="text" placeholder="Search...">
        <textarea placeholder="Enter message"></textarea>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # === page.get_by_* 方法 ===
        # 这些方法直接在 page 上调用，返回 locator

        # 1. get_by_text - 通过文本内容
        by_text = page.get_by_text("Find me by text")
        print(f"get_by_text 找到: {by_text.inner_text()}")

        # 精确匹配
        by_text_exact = page.get_by_text("Find me by text content", exact=True)

        # 2. get_by_role - 通过 ARIA role
        by_role_button = page.get_by_role("button", name="Submit Button")
        print(f"get_by_role(button) 找到: {by_role_button.inner_text()}")

        by_role_link = page.get_by_role("link", name="Click here")
        print(f"get_by_role(link) 找到: {by_role_link.get_attribute('href')}")

        # 3. get_by_label - 通过关联的 label
        by_label = page.get_by_label("Username")
        print(f"get_by_label 找到: {by_label.is_visible()}")

        # 4. get_by_placeholder - 通过 placeholder 属性
        by_placeholder = page.get_by_placeholder("Enter your name")
        print(f"get_by_placeholder 找到: {by_placeholder.is_visible()}")

        # 5. get_by_alt_text - 通过 alt 属性（图片等）
        by_alt = page.get_by_alt_text("Company Logo")
        print(f"get_by_alt_text 找到: {by_alt.get_attribute('src')}")

        # 6. get_by_title - 通过 title 属性
        by_title = page.get_by_title("Tooltip text")
        print(f"get_by_title 找到: {by_title.inner_text()}")

        # 7. get_by_test_id - 通过 data-testid 属性
        by_test_id = page.get_by_test_id("submit-btn")
        print(f"get_by_test_id 找到: {by_test_id.inner_text()}")

        # === 组合选择器 ===
        # 可以链式调用进一步过滤
        submit_input = page.get_by_test_id("username-input")
        print(f"组合选择器结果: {submit_input.is_visible()}")

        # === 使用 filter 过滤 ===
        all_buttons = page.get_by_role("button")
        specific_button = all_buttons.filter(has_text="Submit")
        print(f"过滤后的按钮: {specific_button.inner_text()}")

        browser.close()


def example_14_locator_filter_advanced() -> None:
    """示例 14：Locator 过滤器高级用法"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html>
    <body>
        <div class="item active">Item 1</div>
        <div class="item">Item 2</div>
        <div class="item active">Item 3</div>
        <div class="item">Item 4</div>

        <ul>
            <li class="list-item" data-id="1">First</li>
            <li class="list-item" data-id="2">Second</li>
            <li class="list-item" data-id="3">Third</li>
        </ul>

        <section>
            <h2>Section 1</h2>
            <p class="highlight">Content A</p>
        </section>
        <section>
            <h2>Section 2</h2>
            <p class="highlight">Content B</p>
        </section>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # === filter() 方法 ===

        # 1. has_text - 包含指定文本
        items = page.locator(".item")
        active_items = items.filter(has_text="Item 1")
        print(f"包含 'Item 1' 的元素: {active_items.count()}")

        # 2. has - 包含指定子元素
        items_with_active = items.filter(has=page.locator(".active"))
        print(f"包含 .active 的元素: {items_with_active.count()}")

        # 3. 组合过滤
        filtered = items.filter(
            has_text="Item",  # 包含 "Item"
            has=page.locator(".active"),  # 且包含 .active
        )
        print(f"组合过滤结果: {filtered.count()}")

        # === and_() / or_() ===

        # 4. and_() - 与另一个 locator 取交集
        all_divs = page.locator("div")
        active_divs = all_divs.and_(page.locator(".active"))
        print(f"div AND .active: {active_divs.count()}")

        # 5. or_() - 与另一个 locator 取并集
        list_items = page.locator("li")
        paragraphs = page.locator("p")
        combined = list_items.or_(paragraphs)
        print(f"li OR p: {combined.count()}")

        # === nth() / first / last ===

        # 6. nth() - 获取第 n 个元素
        second_item = items.nth(1)
        print(f"第 2 个 item: {second_item.inner_text()}")

        # 7. first / last
        print(f"第一个: {items.first.inner_text()}")
        print(f"最后一个: {items.last.inner_text()}")

        # === locator.get_by_* ===
        # locator 上也可以使用 get_by_* 方法
        section = page.locator("section").first
        highlighted_in_section = section.get_by_text("Content")
        print(f"Section 中高亮的文本: {highlighted_in_section.inner_text()}")

        browser.close()


def example_15_assertions_advanced() -> None:
    """示例 15：高级断言（使用 get_by_* 和 expect）"""
    try:
        from playwright.sync_api import sync_playwright, expect
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <!DOCTYPE html>
    <html>
    <body>
        <form id="login-form">
            <label for="username">Username</label>
            <input type="text" id="username" value="testuser">

            <label for="password">Password</label>
            <input type="password" id="password" value="secret">

            <button type="submit" disabled>Login</button>
        </form>

        <div class="status" style="display:none">Logged in</div>

        <ul id="list">
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
        </ul>
    </body>
    </html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # === expect() 与 get_by_* 组合 ===

        # 1. 验证元素可见性
        expect(page.get_by_label("Username")).to_be_visible()

        # 2. 验证元素值
        expect(page.get_by_label("Username")).to_have_value("testuser")

        # 3. 验证属性
        expect(page.get_by_role("button", name="Login")).to_have_attribute("disabled")

        # 4. 验证元素数量
        expect(page.locator("#list li")).to_have_count(3)

        # 5. 验证文本内容
        expect(page.locator("#list")).to_contain_text("Item 2")

        # 6. 验证 CSS 类
        expect(page.locator(".status")).to_have_class("status")

        # 7. 验证状态
        expect(page.get_by_role("button", name="Login")).to_be_disabled()

        # 8. 否定断言
        expect(page.locator(".status")).not_to_be_visible()

        # 9. 使用 locator.and_() 的断言
        input_with_label = page.locator("input").and_(page.locator(
            "xpath= ancestor::*[@for='username']"
        ))
        expect(input_with_label).to_be_visible()

        browser.close()


# =============================================================================
# 主程序
# =============================================================================


def main() -> None:
    """主函数：运行所有示例"""
    examples = [
        ("Accessibility 快照", example_01_accessibility_snapshot),
        ("Accessibility 属性", example_02_accessibility_properties),
        ("ARIA Snapshot", example_03_aria_snapshot),
        ("JS 覆盖率", example_04_js_coverage),
        ("CSS 覆盖率", example_05_css_coverage),
        ("PDF 生成基础", example_06_pdf_generation),
        ("PDF 高级选项", example_07_pdf_advanced_options),
        ("PDF 从选择器", example_08_pdf_from_selector),
        ("Video 录制", example_09_video_recording),
        ("Video 访问", example_10_video_access),
        ("Console Message API", example_11_console_message_api),
        ("Worker Console", example_12_console_with_worker),
        ("Locator get_by_*", example_13_locator_get_by_methods),
        ("Locator 过滤器", example_14_locator_filter_advanced),
        ("高级断言", example_15_assertions_advanced),
    ]

    print("== Accessibility、Coverage 和其他高级 API 示例 ==\n")

    for name, func in examples:
        try:
            print(f"\n{'='*60}")
            print(f"示例: {name}")
            print('='*60)
            func()
        except Exception as exc:
            print(f"[skip] {name}: {exc}")

    print("\n== 所有示例执行完毕 ==")


if __name__ == "__main__":
    main()
