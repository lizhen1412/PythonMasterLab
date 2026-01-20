#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：自定义迭代器类。

你会学到：
1) __iter__ 返回 self
2) __next__ 返回下一个值，并在耗尽时抛 StopIteration
3) 迭代器通常是“一次性”的

运行：
    python3 01_Basics/21_Iterators_Generators/04_custom_iterator_class.py
"""


class Countdown:
    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self) -> "Countdown":
        return self

    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


def main() -> None:
    cd = Countdown(3)
    print("第一次遍历:")
    for n in cd:
        print(n, end=" ")
    print("\n再次遍历（已耗尽）:")
    for n in cd:
        print(n, end=" ")
    print()

    print("\n重新创建迭代器:")
    for n in Countdown(2):
        print(n, end=" ")
    print()


if __name__ == "__main__":
    main()
