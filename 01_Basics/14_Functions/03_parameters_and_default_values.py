#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：参数与默认值。

- 默认值在“函数定义时”求值并绑定
- 可变默认值陷阱：共享同一对象，导致跨调用污染
- 防御：用 None 作为哨兵，函数体内创建新对象
"""

from __future__ import annotations

from typing import Any, Optional


def append_value(value: Any, container: list[Any] = []) -> list[Any]:
    """
    反例：使用可变默认值。
    所有调用都会共享同一个列表，导致跨调用累积。
    """
    container.append(value)
    return container


def append_value_safe(value: Any, container: Optional[list[Any]] = None) -> list[Any]:
    """
    推荐写法：用 None 当哨兵，在函数体内创建新列表。
    每次调用都会得到独立容器，不会互相污染。
    """
    if container is None:
        container = []
    container.append(value)
    return container


def default_value_evaluation() -> None:
    """展示默认值求值时机：定义时绑定一个对象。"""
    print("append_value.__defaults__ ->", append_value.__defaults__)
    print("append_value_safe.__defaults__ ->", append_value_safe.__defaults__)


def show_mutable_default_pitfall() -> None:
    """两次调用共享同一个默认列表，导致跨调用堆积。"""
    first = append_value("first")
    second = append_value("second")
    print("同一个列表对象?", first is second)
    print("第二次调用结果 ->", second)


def show_safe_pattern() -> None:
    """用 None 哨兵避免共享状态。"""
    first = append_value_safe("first")
    second = append_value_safe("second")
    print("安全写法，列表对象独立?", first is second)
    print("first ->", first)
    print("second ->", second)


def main() -> None:
    print("== 默认值求值时机 ==")
    default_value_evaluation()

    print("\n== 可变默认值陷阱（反例） ==")
    show_mutable_default_pitfall()

    print("\n== 防御式写法（推荐） ==")
    show_safe_pattern()


if __name__ == "__main__":
    main()
