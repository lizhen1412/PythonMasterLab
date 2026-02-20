#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：print 一次打印多个内容（最核心）。
Author: Lambert

记住 print 的签名（Python 内置）：
    print(*objects, sep=" ", end="\\n", file=sys.stdout, flush=False)

你会学到：
1) 一次打印多个对象：`print(a, b, c)`
2) `sep`：对象之间用什么分隔
3) `end`：结尾追加什么（默认换行；想“同一行继续输出”就改 end）
4) `flush`：是否立刻刷新（实时进度输出常用）
5) print 会对每个对象调用 `str(obj)`（不是 `repr(obj)`）

运行：
    python3 01_Basics/03_Printing/02_print_multiple_objects.py
"""

from __future__ import annotations


class Demo:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Demo(name={self.name})"

    def __repr__(self) -> str:
        return f"<Demo {self.name!r}>"


def main() -> None:
    name = "Alice"
    age = 20
    score = 98.5
    obj = Demo("X")

    print("1) 默认：print 会在多个对象之间加空格：")
    print("name =", name, "age =", age, "score =", score, "obj =", obj)

    print("\n2) sep：自定义分隔符：")
    print(name, age, score, sep=" | ")

    print("\n3) end：让两次 print 输出在同一行：")
    print("part1", end=" ... ")
    print("part2")

    print("\n4) flush：通常配合进度输出使用（这里演示写法）：")
    print("flushed message", flush=True)

    print("\n5) str vs repr：print 默认用 str()：")
    print("print(obj)      ->", obj)
    print("print(repr(obj))->", repr(obj))
    print("f-string !r     ->", f"{obj!r}")


if __name__ == "__main__":
    main()
