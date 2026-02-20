#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：作用域、`UnboundLocalError`、`global/nonlocal`、闭包。
Author: Lambert

- LEGB：Local -> Enclosing -> Global -> Builtins
- `UnboundLocalError` 触发条件：在局部赋值前读取同名变量
- `global`/`nonlocal` 改变绑定位置
- 闭包：内部函数捕获外层变量；循环中的“延迟绑定”坑
"""

from __future__ import annotations

from typing import Callable

GLOBAL_COUNTER = 0


def unbound_local_demo() -> None:
    """演示为什么会触发 UnboundLocalError，并给出修复。"""
    message = "outer"

    def bad_inner() -> str:
        # Python 看到下一行的赋值，认为 message 是“局部变量”
        # 读取前尚未绑定 -> UnboundLocalError
        message += "!"  # type: ignore[operator]
        return message

    try:
        bad_inner()
    except UnboundLocalError as exc:
        print("bad_inner 触发 UnboundLocalError ->", exc)

    def good_inner() -> str:
        nonlocal message
        message += "!"
        return message

    print("good_inner() ->", good_inner())


def fix_with_nonlocal() -> Callable[[], str]:
    """使用 nonlocal 修改闭包里的外层变量。"""
    counter = 0

    def bump() -> str:
        nonlocal counter
        counter += 1
        return f"count={counter}"

    return bump


def use_global() -> None:
    """修改模块级全局变量。"""
    global GLOBAL_COUNTER
    GLOBAL_COUNTER += 1
    print("GLOBAL_COUNTER ->", GLOBAL_COUNTER)


def make_multipliers_bad() -> list[Callable[[int], int]]:
    """循环中 lambda 捕获同一个变量，所有函数指向同一 binding。"""
    funcs: list[Callable[[int], int]] = []
    for i in range(3):
        funcs.append(lambda x: x * i)
    return funcs


def make_multipliers_good() -> list[Callable[[int], int]]:
    """通过默认参数/内部作用域“固定”当前值，避免延迟绑定。"""
    funcs: list[Callable[[int], int]] = []
    for i in range(3):
        funcs.append(lambda x, factor=i: x * factor)
    return funcs


def show_closure_cells(func: Callable[..., object]) -> None:
    """打印函数捕获的自由变量。"""
    print(f"{func.__name__}.__closure__ ->", func.__closure__)


def main() -> None:
    print("== UnboundLocalError 示例 ==")
    unbound_local_demo()

    print("\n== nonlocal 修复 ==")
    bump = fix_with_nonlocal()
    print(bump(), bump(), bump())
    show_closure_cells(bump)

    print("\n== global 示例 ==")
    use_global()
    use_global()

    print("\n== 闭包延迟绑定坑 ==")
    bad_funcs = make_multipliers_bad()
    print("bad_funcs[0](10) ->", bad_funcs[0](10))
    print("bad_funcs[1](10) ->", bad_funcs[1](10))
    print("bad_funcs[2](10) ->", bad_funcs[2](10))

    good_funcs = make_multipliers_good()
    print("good_funcs[0](10) ->", good_funcs[0](10))
    print("good_funcs[1](10) ->", good_funcs[1](10))
    print("good_funcs[2](10) ->", good_funcs[2](10))


if __name__ == "__main__":
    main()