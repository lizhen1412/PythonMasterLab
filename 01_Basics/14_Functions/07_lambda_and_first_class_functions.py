#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：`lambda` 与“函数是一等公民”。

- lambda 适用场景：短小回调/排序 key/一次性函数
- 不适合：复杂逻辑、多语句、需要注释的场景（请用 def）
- 函数可存入容器、作为参数/返回值
- map/filter 与推导式对比
"""

from __future__ import annotations

from typing import Callable


def demo_sorted_with_lambda() -> None:
    """用 lambda 做排序 key；对比使用 def。"""
    students = [
        {"name": "Alice", "score": 88},
        {"name": "Bob", "score": 75},
        {"name": "Charlie", "score": 95},
    ]

    by_score = sorted(students, key=lambda s: s["score"], reverse=True)
    print("按分数降序 ->", [s["name"] for s in by_score])

    def name_length(student: dict[str, str]) -> int:
        return len(student["name"])

    by_name_len = sorted(students, key=name_length)
    print("按姓名长度升序 ->", [s["name"] for s in by_name_len])


def demo_functions_in_containers() -> None:
    """把函数存入 list/dict，并按需调用。"""
    def double(x: int) -> int:
        return x * 2

    def square(x: int) -> int:
        return x * x

    ops: dict[str, Callable[[int], int]] = {
        "double": double,
        "square": square,
        "increment": lambda x: x + 1,
    }

    for name, func in ops.items():
        print(f"{name}(5) -> {func(5)}")


def demo_map_filter_vs_comprehension() -> None:
    """对比 map/filter 与推导式的可读性。"""
    numbers = [1, 2, 3, 4, 5]
    doubled = list(map(lambda x: x * 2, numbers))
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print("map/filter ->", doubled, evens)

    doubled_comp = [x * 2 for x in numbers]
    evens_comp = [x for x in numbers if x % 2 == 0]
    print("列表推导式 ->", doubled_comp, evens_comp)


def make_multiplier(factor: int) -> Callable[[int], int]:
    """返回一个带记忆参数的函数（闭包 + 返回函数）。"""
    return lambda x: x * factor


def main() -> None:
    print("== lambda 排序 key ==")
    demo_sorted_with_lambda()

    print("\n== 函数存入容器/作为值 ==")
    demo_functions_in_containers()

    print("\n== map/filter vs 推导式 ==")
    demo_map_filter_vs_comprehension()

    print("\n== 返回函数（闭包） ==")
    times3 = make_multiplier(3)
    print("times3(10) ->", times3(10))


if __name__ == "__main__":
    main()
