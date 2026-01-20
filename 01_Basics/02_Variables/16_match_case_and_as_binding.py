#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 16（进阶）：match/case、with/except 的 as 绑定。

你会学到：
1) `match/case` 的捕获模式（capture pattern）会“绑定变量”
2) `as` 可以在匹配时“顺便把整体也绑定出来”
3) `with ... as name`、`except ... as exc` 也是一种绑定方式

运行：
    python3 01_Basics/02_Variables/16_match_case_and_as_binding.py
"""

from contextlib import nullcontext


def demo_match() -> None:
    data: object = ["move", 10, 20]

    match data:
        case ["move", x, y] as whole:
            print("matched move:", x, y)
            print("whole =", whole)
        case _:
            print("no match")


def demo_with_as() -> None:
    with nullcontext("resource") as res:
        print("with ... as res ->", res)


def demo_except_as() -> None:
    try:
        _ = 1 / 0
    except ZeroDivisionError as exc:
        print("caught:", exc)

    # Python 3 会在 except 结束后清理 exc 以避免引用环
    print("'exc' in locals() after except ->", "exc" in locals())


def main() -> None:
    demo_match()
    demo_with_as()
    demo_except_as()


if __name__ == "__main__":
    main()
