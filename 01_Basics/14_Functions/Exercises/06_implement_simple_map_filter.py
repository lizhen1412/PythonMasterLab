#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 06：实现简化版 map/filter。

要求：
- 实现 simple_map(func, iterable) 与 simple_filter(pred, iterable)
- 返回列表，与内置 map/filter 结果对比
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any, Callable


def simple_map(func: Callable[[Any], Any], iterable: Iterable[Any]) -> list[Any]:
    result: list[Any] = []
    for item in iterable:
        result.append(func(item))
    return result


def simple_filter(pred: Callable[[Any], bool], iterable: Iterable[Any]) -> list[Any]:
    result: list[Any] = []
    for item in iterable:
        if pred(item):
            result.append(item)
    return result


def main() -> None:
    numbers = [1, 2, 3, 4, 5]
    print("simple_map x2 ->", simple_map(lambda x: x * 2, numbers))
    print("simple_filter even ->", simple_filter(lambda x: x % 2 == 0, numbers))

    print("内置 map ->", list(map(lambda x: x * 2, numbers)))
    print("内置 filter ->", list(filter(lambda x: x % 2 == 0, numbers)))


if __name__ == "__main__":
    main()
