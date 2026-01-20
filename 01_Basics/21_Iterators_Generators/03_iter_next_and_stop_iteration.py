#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：手动迭代与 StopIteration。

你会学到：
1) next() 在耗尽时抛 StopIteration
2) for 循环内部就是 iter + next + 捕获 StopIteration

运行：
    python3 01_Basics/21_Iterators_Generators/03_iter_next_and_stop_iteration.py
"""


def manual_next(items: list[int]) -> None:
    it = iter(items)
    print("手动 next():")
    while True:
        try:
            value = next(it)
        except StopIteration:
            print("  -> StopIteration (耗尽)")
            break
        print("  ->", value)


def for_loop(items: list[int]) -> None:
    print("for 循环:")
    for value in items:
        print("  ->", value)


def main() -> None:
    data = [10, 20, 30]
    manual_next(data)
    print()
    for_loop(data)


if __name__ == "__main__":
    main()
