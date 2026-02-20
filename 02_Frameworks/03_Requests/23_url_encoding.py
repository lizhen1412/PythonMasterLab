#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 23：URL 编码与解码。
Author: Lambert

要点：
- requests 自动处理 params 中的特殊字符编码
- 手动 URL 编码使用 requests.utils.quote()
- 解码使用 requests.utils.unquote()
- 处理中文、空格、特殊字符

运行：
    python3 02_Frameworks/03_Requests/23_url_encoding.py
"""

from __future__ import annotations

import requests
from requests.utils import quote, unquote


def demo_auto_encoding() -> None:
    """演示 requests 自动 URL 编码"""
    params = {
        "q": "测试 空格",
        "url": "https://example.com/path?param=value",
        "special": "!@#$%^&*()",
    }

    resp = requests.get(
        "https://httpbin.org/get",
        params=params,
        timeout=5,
    )

    print("=== requests 自动 URL 编码 ===")
    print(f"原始参数 -> {params}")
    print(f"最终 URL -> {resp.json()['url']}")
    print(f"编码后的 args -> {resp.json()['args']}")


def demo_manual_encoding() -> None:
    """演示手动 URL 编码"""
    original = "测试 空格 !@#"

    # 手动编码
    encoded = quote(original)
    print(f"\n=== 手动 URL 编码 ===")
    print(f"原始字符串 -> {original}")
    print(f"编码后 -> {encoded}")

    # 解码
    decoded = unquote(encoded)
    print(f"解码后 -> {decoded}")

    # 验证
    assert original == decoded
    print("编码/解码验证通过")


def demo_safe_characters() -> None:
    """演示保留字符（不编码）"""
    url = "https://example.com/path?key=value&sort=desc"

    # 默认编码，保留 / : ? = &
    encoded_default = quote(url)
    print(f"\n=== 默认编码（保留安全字符） ===")
    print(f"原始 URL -> {url}")
    print(f"编码后 -> {encoded_default}")

    # 不保留任何字符（全部编码）
    encoded_all = quote(url, safe="")
    print(f"\n全部编码 -> {encoded_all}")

    # 自定义保留字符
    encoded_custom = quote(url, safe="/:")
    print(f"只保留 /: -> {encoded_custom}")


def demo_encoding_spaces() -> None:
    """演示空格编码方式"""
    text = "hello world"

    # 方式1：使用 quote（空格编码为 %20）
    encoded_percent = quote(text)
    print(f"\n=== 空格编码方式 ===")
    print(f"quote() 空格 -> {encoded_percent}")

    # 方式2：使用 quote_plus（空格编码为 +）
    from requests.utils import quote_plus
    encoded_plus = quote_plus(text)
    print(f"quote_plus() 空格 -> {encoded_plus}")

    # requests 的 params 默认使用 %20 编码空格
    resp = requests.get(
        "https://httpbin.org/get",
        params={"q": "hello world"},
        timeout=5,
    )
    print(f"requests params 空格 -> {resp.json()['args']['q']}")


def demo_chinese_encoding() -> None:
    """演示中文编码"""
    chinese = "你好世界"

    # UTF-8 编码
    encoded_utf8 = quote(chinese)
    print(f"\n=== 中文编码 ===")
    print(f"原始中文 -> {chinese}")
    print(f"UTF-8 编码 -> {encoded_utf8}")

    # 在 URL 中使用
    resp = requests.get(
        "https://httpbin.org/get",
        params={"q": chinese},
        timeout=5,
    )
    print(f"在 URL 中 -> {resp.json()['url']}")


def demo_special_characters() -> None:
    """演示特殊字符编码"""
    special = {
        "空格": " ",
        "引号": '"',
        "单引号": "'",
        "加号": "+",
        "等号": "=",
        "问号": "?",
        "井号": "#",
        "百分号": "%",
    }

    print(f"\n=== 特殊字符编码 ===")
    for name, char in special.items():
        encoded = quote(char)
        print(f"{name} ({char}) -> {encoded}")


def demo_url_building() -> None:
    """演示 URL 构建的最佳实践"""
    print(f"\n=== URL 构建最佳实践 ===")

    # 错误方式：字符串拼接（不安全）
    query = "测试 空格"
    wrong_url = f"https://httpbin.org/get?q={query}"
    print(f"❌ 字符串拼接 -> {wrong_url}")

    # 正确方式1：使用 params
    resp = requests.get(
        "https://httpbin.org/get",
        params={"q": query},
        timeout=5,
    )
    print(f"✅ 使用 params -> {resp.json()['url']}")

    # 正确方式2：手动编码
    encoded_query = quote(query)
    correct_url = f"https://httpbin.org/get?q={encoded_query}"
    print(f"✅ 手动编码 -> {correct_url}")


def demo_path_encoding() -> None:
    """演示 URL 路径编码"""
    path = "路径/包含/中文"

    # 路径中斜杠通常保留
    encoded_path = quote(path, safe="/")
    print(f"\n=== 路径编码 ===")
    print(f"原始路径 -> {path}")
    print(f"编码后（保留 /） -> {encoded_path}")

    # 完整 URL
    full_url = f"https://example.com/{encoded_path}"
    print(f"完整 URL -> {full_url}")


def main() -> None:
    print("=== URL 编码与解码演示 ===\n")
    demo_auto_encoding()
    demo_manual_encoding()
    demo_safe_characters()
    demo_encoding_spaces()
    demo_chinese_encoding()
    demo_special_characters()
    demo_url_building()
    demo_path_encoding()

    print("\n使用建议:")
    print("  - 优先使用 params 参数，requests 自动处理编码")
    print("  - 手动拼接 URL 时使用 quote() 编码特殊字符")
    print("  - 路径编码保留斜杠: quote(path, safe='/')")
    print("  - 空格在 URL 查询中通常编码为 %20")
    print("  - 中文自动按 UTF-8 编码为 %XX 形式")


if __name__ == "__main__":
    main()