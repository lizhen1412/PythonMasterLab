#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：参数五种类别与调用规则。

参数位置顺序（从左到右）：
    1) 位置仅限参数：`a, /`
    2) 位置或关键字参数：`b, c=0`
    3) 变长位置参数：`*args`
    4) 关键字仅限参数：`d, e=1`
    5) 变长关键字参数：`**kwargs`

常见错误信息：
- TypeError: got multiple values for argument 'name'
- TypeError: missing required keyword-only argument: 'name'
"""

from __future__ import annotations

from typing import Any


def describe_params(a: int, /, b: int, c: int = 0, *args: int, d: int, e: int = 1, **kwargs: Any) -> str:
    """
    参数排列示范：
    - a 必须“仅位置”传递
    - b 可以位置或关键字传递
    - c 有默认值，可以省略
    - d 关键字仅限（必须写 d=...）
    - e 关键字仅限且有默认值
    - *args/**kwargs 收集其余
    """
    return (
        f"a={a}, b={b}, c={c}, args={args}, d={d}, e={e}, kwargs={kwargs}"
    )


def safe_call_examples() -> None:
    """合法调用示例。"""
    print(describe_params(1, 2, d=99))  # 最小必需：a=1, b=2, d=99
    print(describe_params(10, b=20, d=30, e=40))  # b 用关键字传递
    print(describe_params(5, 6, 7, 8, 9, d=10, extra="ok"))  # *args 收集多余位置参数


def error_examples() -> None:
    """展示典型错误并打印异常信息，帮助理解规则。"""

    def show_error(label: str, func, *args, **kwargs) -> None:
        try:
            func(*args, **kwargs)
        except TypeError as exc:
            print(f"{label}: TypeError -> {exc}")

    show_error("位置仅限参数被关键字调用", describe_params, a=1, b=2, d=3)
    show_error("位置 + 关键字重复赋值", describe_params, 1, 2, d=3, b=4)
    show_error("缺少关键字仅限参数 d", describe_params, 1, 2)


def main() -> None:
    print("== 合法调用示例 ==")
    safe_call_examples()

    print("\n== 常见错误示例 ==")
    error_examples()


if __name__ == "__main__":
    main()
