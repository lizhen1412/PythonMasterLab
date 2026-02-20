#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：iter(callable, sentinel) 的哨兵迭代。
Author: Lambert

你会学到：
1) iter(callable, sentinel) 会反复调用 callable
2) 当返回值等于 sentinel 时停止
3) 常见场景：读取到空行/EOF

运行：
    python3 01_Basics/21_Iterators_Generators/05_iter_callable_sentinel.py
"""


from typing import Callable


def make_reader(values: list[str], sentinel: str) -> Callable[[], str]:
    it = iter(values)

    def read() -> str:
        try:
            return next(it)
        except StopIteration:
            return sentinel

    return read


def main() -> None:
    values = ["A", "B", "STOP", "C"]
    sentinel = "STOP"
    read = make_reader(values, sentinel)

    print("== iter(callable, sentinel) ==")
    for item in iter(read, sentinel):
        print(item)

    print("\n说明：" )
    print("- 返回值等于 sentinel 时停止，STOP 后面的 'C' 不会被读到")


if __name__ == "__main__":
    main()