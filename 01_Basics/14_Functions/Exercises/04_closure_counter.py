#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：闭包计数器。
Author: Lambert

要求：
- 编写 make_counter，返回一个使用 nonlocal 累加的函数
- 每次调用返回递增的数字
"""

from __future__ import annotations

from typing import Callable


def make_counter(start: int = 0) -> Callable[[], int]:
    count = start

    def bump() -> int:
        nonlocal count
        count += 1
        return count

    return bump


def main() -> None:
    counter = make_counter(10)
    print(counter(), counter(), counter())

    another = make_counter()
    print(another(), another())


if __name__ == "__main__":
    main()