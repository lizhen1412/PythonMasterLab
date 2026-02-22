#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 46：locator 高级用法大全。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/04_Playwright/46_advanced_locator_usage.py

本示例展示 locator 的高级用法和所有参数说明。
"""

from __future__ import annotations

from urllib.parse import quote


def example_01_locator_options() -> None:
    """示例 01：locator 选项参数"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <button id="btn" disabled>Click Me</button>
    <div id="container" style="display:none">Hidden Content</div>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # === locator 选项 ===

        # 1. 点击选项
        # click() 有多个选项参数
        page.locator("#btn").click(
            # 点击按钮
            button="left",  # 'left' | 'right' | 'middle'，默认 'left'

            # 点击位置
            # - None: 元素可见部分的中心点（默认）
            # - {x, y}: 相对元素左上角的偏移
            position={"x": 10, "y": 10},

            # 点击次数
            click_count=1,  # 默认 1

            # 延迟（毫秒）
            delay=100,  # 默认 0

            # 强制点击（即使元素不可见或被遮挡）
            force=True,  # 默认 False

            # 修改后的 Ctrl 键状态
            modifiers=["Alt", "Control", "Meta", "Shift"],

            # 超时时间（毫秒）
            timeout=30000,  # 默认 30000

            # 跳过可操作性检查
            # 与 force 效果类似，但更强
            trial=False,  # 默认 False
        )

        # 2. 填写选项
        page.locator("input").fill(
            "text",
            # 填写速度（毫秒/字符），设为 0 则瞬间完成
            timeout=30000,
        )

        # 3. 悬停选项
        page.locator("#elem").hover(
            # 悬停位置
            position={"x": 0, "y": 0},
            # 修改后的键状态
            modifiers=["Shift"],
            # 强制悬停
            force=False,
            # 超时
            timeout=30000,
        )

        browser.close()


def example_02_locator_filters() -> None:
    """示例 02：locator 过滤器"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <div class="item">Item 1</div>
    <div class="item">Item 2</div>
    <div class="item active">Item 3</div>
    <div class="item">Item 4</div>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # === locator 过滤器 ===

        # 1. filter() - 根据文本过滤
        items = page.locator(".item")
        item_with_text = items.filter(has_text="Item 3")
        print("包含 'Item 3' 的元素:", item_with_text.inner_text())

        # 2. filter() - 根据子 locator 过滤
        items_with_active = items.filter(has=page.locator(".active"))
        print("包含 .active 的元素数量:", items_with_active.count())

        # 3. filter() - 组合条件
        filtered = items.filter(
            has_text="Item",  # 包含文本 "Item"
            has=page.locator(".active"),  # 且包含 .active 元素
        )

        # 4. and_() - 与另一个 locator 取交集
        locator1 = page.get_by_role("button")
        locator2 = page.get_by_text("Submit")
        # 查找既是 button 又包含 "Submit" 文本的元素
        combined = locator1.and_(locator2)

        # 5. or_() - 与另一个 locator 取并集
        # 查找匹配 selector1 或 selector2 的元素
        locator_or = page.locator("button").or_(page.locator("a"))

        browser.close()


def example_03_locator_nth_and_first_last() -> None:
    """示例 03：locator 索引和首尾元素"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <ul>
        <li>First</li>
        <li>Second</li>
        <li>Third</li>
        <li>Last</li>
    </ul>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        items = page.locator("li")

        # === nth(), first, last ===

        # nth() - 获取第 n 个元素（从 0 开始）
        second = items.nth(1)
        print("第二个元素:", second.inner_text())

        # first - 第一个元素（等价于 nth(0)）
        first = items.first
        print("第一个元素:", first.inner_text())

        # last - 最后一个元素
        last = items.last
        print("最后一个元素:", last.inner_text())

        # === nth() 的特殊用法 ===

        # 使用 slice 获取多个元素
        # 注意：locator 不直接支持切片，需要用 nth() 逐个获取
        for i in range(items.count()):
            print(f"元素 {i}:", items.nth(i).inner_text())

        browser.close()


def example_04_locator_waiting_strategies() -> None:
    """示例 04：locator 等待策略"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <button id="btn" style="display:none">Button</button>
    <script>
        setTimeout(() => {
            document.querySelector('#btn').style.display = 'block';
        }, 1000);
    </script>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        btn = page.locator("#btn")

        # === 等待策略 ===

        # 1. wait_for() - 等待元素达到指定状态
        btn.wait_for(
            # 等待状态：
            # - 'attached': 元素存在于 DOM
            # - 'detached': 元素从 DOM 移除
            # - 'visible': 元素可见（默认）
            # - 'hidden': 元素隐藏
            state="visible",
            timeout=5000,  # 超时时间
        )

        # 2. 点击时自动等待
        # Playwright 会自动等待元素可操作
        btn.click()  # 会等待按钮可见、启用、可点击

        # 3. 设置元素级别的超时
        btn.click(timeout=10000)  # 单独设置此操作的超时

        # 4. 使用 expect 进行断言（会自动重试）
        from playwright.sync_api import expect
        expect(btn).to_be_visible()

        browser.close()


def example_05_locator_get_attributes() -> None:
    """示例 05：locator 获取属性和状态"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <input id="name" type="text" value="Alice" disabled />
    <input id="email" type="email" value="alice@example.com" />
    <div id="content" data-role="main" class="container">Content</div>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # === 获取属性 ===
        name_input = page.locator("#name")
        content_div = page.locator("#content")

        # get_attribute() - 获取属性值
        data_role = content_div.get_attribute("data-role")
        print("data-role:", data_role)

        # get_attribute() - 属性不存在时返回 None
        placeholder = name_input.get_attribute("placeholder")
        print("placeholder:", placeholder)  # None

        # === 获取多个属性 ===
        # inner_html() - 获取内部 HTML
        print("inner_html:", content_div.inner_html())

        # inner_text() - 获取内部文本
        print("inner_text:", content_div.inner_text())

        # text_content() - 获取文本内容（包括隐藏元素）
        print("text_content:", content_div.text_content())

        # input_value() - 获取输入框的值
        print("input_value:", name_input.input_value())

        # === 检查状态 ===

        # is_checked() - 复选框/单选框是否选中
        print("is_checked:", page.locator("input[type='checkbox']").is_checked())

        # is_disabled() - 是否禁用
        print("is_disabled:", name_input.is_disabled())

        # is_enabled() - 是否启用
        print("is_enabled:", page.locator("#email").is_enabled())

        # is_editable() - 是否可编辑
        print("is_editable:", name_input.is_editable())

        # is_visible() - 是否可见
        print("is_visible:", content_div.is_visible())

        browser.close()


def example_06_locator_count_and_all() -> None:
    """示例 06：locator 数量和批量操作"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <ul>
        <li class="item">Item 1</li>
        <li class="item">Item 2</li>
        <li class="item">Item 3</li>
    </ul>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        items = page.locator(".item")

        # === count() - 获取元素数量 ===
        count = items.count()
        print(f"共有 {count} 个 .item 元素")

        # === all() - 获取所有匹配的元素 ===
        # 返回 ElementHandle 列表
        all_items = items.all()
        print(f"all() 返回了 {len(all_items)} 个元素")

        # === all_text_contents() - 获取所有元素的文本 ===
        texts = items.all_text_contents()
        print("所有文本:", texts)

        # === all_inner_texts() - 获取所有元素的 inner text ===
        inner_texts = items.all_inner_texts()
        print("所有 inner text:", inner_texts)

        browser.close()


def example_07_locator_set_checked() -> None:
    """示例 07：复选框/单选框操作"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <input type="checkbox" id="agree" />
    <input type="checkbox" id="subscribe" checked />
    <input type="radio" name="plan" value="basic" />
    <input type="radio" name="plan" value="pro" />
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # === set_checked() - 设置复选框/单选框状态 ===

        # 勾选复选框
        page.locator("#agree").set_checked(
            True,  # True 表示勾选，False 表示取消勾选
            # 可选参数
            force=False,  # 强制操作
            timeout=30000,  # 超时
            # 注意：position 参数在 set_checked 中不可用
        )

        # 取消勾选
        page.locator("#subscribe").set_checked(False)

        # === check() / uncheck() - 简写方法 ===

        # check() 等价于 set_checked(True)
        page.locator("#agree").check()

        # uncheck() 等价于 set_checked(False)
        page.locator("#subscribe").uncheck()

        # === 单选框操作 ===
        page.locator("input[value='pro']").check()

        browser.close()


def example_08_locator_drag_and_drop() -> None:
    """示例 08：拖拽操作"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <div id="source" draggable="true" style="background:lightblue;padding:20px;">
        拖拽源
    </div>
    <div id="target" style="background:lightgreen;padding:20px;margin-top:20px;">
        放置目标
    </div>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # === drag_and_drop() - 拖拽元素 ===
        page.locator("#source").drag_and_drop(
            "#target",
            # 目标位置（可选）
            target_position={"x": 50, "y": 50},

            # 拖拽源位置（可选）
            source_position={"x": 0, "y": 0},

            # 强制拖拽
            force=False,

            # 超时
            timeout=30000,

            # 拖拽延迟（毫秒）
            # 注意：某些情况下可能需要延迟
            delay=None,
        )

        browser.close()


def example_09_locator_highlight_and_debug() -> None:
    """示例 09：locator 调试和高亮"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <button id="btn">Click Me</button>
    <div id="box">Box</div>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        btn = page.locator("#btn")
        box = page.locator("#box")

        # === highlight() - 高亮元素（用于调试）===
        # 注意：highlight() 只在非 headless 模式下可见
        # duration: 高亮持续时间（毫秒）
        try:
            btn.highlight(duration=2000)
        except Exception as exc:
            print(f"[skip] highlight 需要 headless=False: {exc}")

        # === locator 的字符串表示 ===
        # 打印 locator 的信息
        print("locator 信息:", str(btn))
        print("locator repr:", repr(btn))

        # === 使用 pause() 暂停执行 ===
        # 注意：pause() 只在非 headless 模式下有用
        # 会打开 Playwright Inspector
        try:
            # page.pause()  # 这会暂停执行并打开调试器
            pass
        except Exception as exc:
            print(f"[skip] pause 需要 headless=False: {exc}")

        browser.close()


def example_10_locator_select_option() -> None:
    """示例 10：下拉框操作"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <select id="single">
        <option value="">请选择</option>
        <option value="option1">选项 1</option>
        <option value="option2">选项 2</option>
    </select>
    <select id="multiple" multiple>
        <option value="a">A</option>
        <option value="b">B</option>
        <option value="c">C</option>
    </select>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # === select_option() - 选择下拉框选项 ===

        # 1. 根据值选择
        page.locator("#single").select_option(
            "option1",
            # 可选参数
            timeout=30000,  # 超时
            force=False,  # 强制操作
        )

        # 2. 根据标签选择
        page.locator("#single").select_option(label="选项 2")

        # 3. 根据索引选择
        page.locator("#single").select_option(index=1)

        # 4. 多选下拉框
        page.locator("#multiple").select_option([
            {"value": "a"},  # 根据值
            {"label": "B"},  # 根据标签
            {"index": 2},   # 根据索引
        ])

        # 5. 获取当前选中的值
        selected = page.locator("#single").input_value()
        print("选中的值:", selected)

        browser.close()


def example_11_locator_set_input_files() -> None:
    """示例 11：文件上传操作"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    from pathlib import Path

    HTML = """
    <input type="file" id="file" />
    <input type="file" id="files" multiple />
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        # 创建临时文件
        temp_file = Path("/tmp/playwright_demo/test_file.txt")
        temp_file.parent.mkdir(parents=True, exist_ok=True)
        temp_file.write_text("Test file content")

        # === set_input_files() - 上传文件 ===

        # 1. 上传单个文件
        page.locator("#file").set_input_files(
            str(temp_file),
            # 可选参数
            timeout=30000,
        )

        # 2. 上传多个文件
        page.locator("#files").set_input_files([
            str(temp_file),
            str(temp_file),  # 可以上传同一个文件多次
        ])

        # 3. 使用 Files 对象
        # page.locator("#file").set_input_files(
        #     [
        #         {
        #             "name": "test.txt",
        #             "mimeType": "text/plain",
        #             "buffer": b"file content",
        #         }
        #     ]
        # )

        # 4. 清除文件选择
        page.locator("#file").set_input_files([])

        browser.close()


def example_12_locator_press_and_type() -> None:
    """示例 12：键盘操作"""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"无法导入 playwright: {exc}")
        return

    HTML = """
    <input type="text" id="input" />
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML)

        input_elem = page.locator("#input")

        # === type() - 输入文本 ===
        input_elem.type(
            "Hello World",
            # 输入延迟（毫秒/字符），设为 0 则瞬间完成
            delay=100,  # 默认 0
            timeout=30000,
        )

        # === press() - 按键 ===
        input_elem.press(
            "Enter",
            # 按键延迟（毫秒）
            delay=50,  # 默认 0
            timeout=30000,
        )

        # === fill() - 填写（会先清空）===
        input_elem.fill(
            "New Text",
            timeout=30000,
        )

        browser.close()


def main() -> None:
    """主函数：运行所有示例"""
    examples = [
        ("locator 选项参数", example_01_locator_options),
        ("locator 过滤器", example_02_locator_filters),
        ("索引和首尾元素", example_03_locator_nth_and_first_last),
        ("等待策略", example_04_locator_waiting_strategies),
        ("获取属性和状态", example_05_locator_get_attributes),
        ("数量和批量操作", example_06_locator_count_and_all),
        ("复选框操作", example_07_locator_set_checked),
        ("拖拽操作", example_08_locator_drag_and_drop),
        ("调试和高亮", example_09_locator_highlight_and_debug),
        ("下拉框操作", example_10_locator_select_option),
        ("文件上传", example_11_locator_set_input_files),
        ("键盘操作", example_12_locator_press_and_type),
    ]

    print("== Playwright Locator 高级用法示例 ==\n")

    for name, func in examples:
        try:
            print(f"\n--- {name} ---")
            func()
        except Exception as exc:
            print(f"[skip] {name}: {exc}")

    print("\n== 所有示例执行完毕 ==")


if __name__ == "__main__":
    main()
