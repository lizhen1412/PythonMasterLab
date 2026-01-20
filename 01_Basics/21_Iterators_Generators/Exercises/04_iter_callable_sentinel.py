#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：iter(callable, sentinel)。

题目：
实现函数 `read_until_sentinel(values, sentinel)`：
- 使用 iter(callable, sentinel)
- 返回在 sentinel 之前读到的元素列表（不包含 sentinel）

示例：
    values = ["A", "B", "STOP", "C"]
    -> ["A", "B"]

参考答案：
- 本文件实现即为参考答案；main() 带最小自测。

运行：
    python3 01_Basics/21_Iterators_Generators/Exercises/04_iter_callable_sentinel.py
"""

from typing import Callable


def read_until_sentinel(values: list[str], sentinel: str) -> list[str]:
    it = iter(values)

    def read() -> str:
        try:
            return next(it)
        except StopIteration:
            return sentinel

    reader: Callable[[], str] = read
    return list(iter(reader, sentinel))


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    values = ["A", "B", "STOP", "C"]
    check("read_until_sentinel", read_until_sentinel(values, "STOP"), ["A", "B"])
    check("no sentinel", read_until_sentinel(["X"], "STOP"), ["X"])


if __name__ == "__main__":
    main()
