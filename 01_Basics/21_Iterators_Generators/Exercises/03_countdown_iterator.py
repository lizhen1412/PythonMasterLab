#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：自定义倒计时迭代器。
Author: Lambert

题目：
实现类 `Countdown(start)`：
- 可被 for 循环遍历
- 从 start 递减到 0（包含 0）

参考答案：
- 本文件实现即为参考答案；main() 带最小自测。

运行：
    python3 01_Basics/21_Iterators_Generators/Exercises/03_countdown_iterator.py
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


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    result = list(Countdown(3))
    check("Countdown(3)", result, [3, 2, 1, 0])
    check("Countdown(0)", list(Countdown(0)), [0])
    check("Countdown(-1)", list(Countdown(-1)), [])


if __name__ == "__main__":
    main()