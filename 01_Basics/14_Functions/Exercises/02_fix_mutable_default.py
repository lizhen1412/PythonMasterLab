#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：修复可变默认值陷阱。
Author: Lambert

要求：
- 给出一个使用“可变默认值”的反例，并展示跨调用被污染
- 编写安全版本：使用 None 哨兵，在函数体内创建新列表
"""

from __future__ import annotations

from typing import Any, Optional


def append_bad(value: Any, items: list[Any] = []) -> list[Any]:
    """反例：可变默认值在多次调用间共享。"""
    items.append(value)
    return items


def append_good(value: Any, items: Optional[list[Any]] = None) -> list[Any]:
    """修复：用 None 哨兵，并在函数体内创建新列表。"""
    if items is None:
        items = []
    items.append(value)
    return items


def main() -> None:
    print("== 反例：状态被污染 ==")
    first = append_bad("a")
    second = append_bad("b")
    print("first is second ?", first is second)
    print("second ->", second)

    print("\n== 安全写法 ==")
    first_good = append_good("a")
    second_good = append_good("b")
    print("first_good is second_good ?", first_good is second_good)
    print("second_good ->", second_good)


if __name__ == "__main__":
    main()