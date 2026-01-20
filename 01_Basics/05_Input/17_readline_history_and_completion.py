#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 17：readline 行编辑与历史（可选平台功能）。

你会学到：
1) readline.add_history / get_history_item
2) 简单补全绑定（tab 完成）
3) 如果模块不存在，优雅跳过

运行（在仓库根目录执行）：
    python3 01_Basics/05_Input/17_readline_history_and_completion.py
"""

from __future__ import annotations


def main() -> None:
    try:
        import readline  # type: ignore
    except ImportError:
        print("readline 不可用（Windows 默认不自带该模块）")
        return

    readline.parse_and_bind("tab: complete")
    readline.add_history("help")
    readline.add_history("quit")

    print("history length ->", readline.get_current_history_length())
    print("history #1 ->", readline.get_history_item(1))
    print("history #2 ->", readline.get_history_item(2))

    print("\nTIP: 交互输入时可使用方向键浏览历史。")


if __name__ == "__main__":
    main()
