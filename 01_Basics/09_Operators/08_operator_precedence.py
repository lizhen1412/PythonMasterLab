#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：运算符优先级（Operator Precedence）

核心建议：不确定就加括号（可读性 > “背优先级表”）。

本例用少量表达式演示常见坑：
1) `-2**2` 等价于 `-(2**2)`（** 高于一元 -）
2) `and` 的优先级高于 `or`
3) 比较运算符（==、<、in、is 等）高于 `not`
4) 链式比较：`1 < x < 3` 会被当成一个整体

运行（在仓库根目录执行）：
    python3 01_Basics/09_Operators/08_operator_precedence.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    show("1) -2**2 vs (-2)**2")
    print("-2**2 =", -2**2)
    print("(-2)**2 =", (-2) ** 2)

    show("2) and vs or")
    # and 优先级高于 or：等价于 (False or (True and False))
    print("False or True and False ->", False or True and False)
    print("(False or True) and False ->", (False or True) and False)

    show("3) not 与比较")
    # 比较优先级高于 not：等价于 not (1 == 2)
    print("not 1 == 2 ->", not 1 == 2)
    print("not (1 == 2) ->", not (1 == 2))

    show("4) 链式比较是一个表达式")
    x = 2
    print("1 < x < 3 ->", 1 < x < 3)
    print("(1 < x) < 3 ->", (1 < x) < 3, "（bool 也是 int 子类，容易误解）")

    show("5) 成员运算符与 not")
    items = [1, 2, 3]
    print("not 2 in items ->", not 2 in items, "（等价于 2 not in items）")
    print("2 not in items ->", 2 not in items)

    show("6) 算术与位运算优先级")
    print("1 << 2 + 1 ->", 1 << 2 + 1, "（等价于 1 << (2 + 1)）")
    print("1 + 2 << 1 ->", 1 + 2 << 1, "（等价于 (1 + 2) << 1）")
    print("1 & 2 == 0 ->", 1 & 2 == 0, "（等价于 (1 & 2) == 0）")

    show("7) 条件表达式（if/else）的优先级")
    cond = False
    a, b, c = "A", "B", "C"
    print("a or b if cond else c ->", a or b if cond else c, "（等价于 (a or b) if cond else c）")
    print("a or (b if cond else c) ->", a or (b if cond else c))

    show("8) 赋值表达式 := 的优先级")
    x = -1
    expr = (x := (0 or 2))
    print("x := (0 or 2) ->", x, expr)
    x = -1
    expr = ((x := 0) or 2)
    print("(x := 0) or 2 ->", x, expr, "（两者结果不同）")

    show("9) lambda 的优先级最低")
    func = (lambda n: n + 1) if cond else (lambda n: n - 1)
    print("cond=False -> func(10) ->", func(10))
    func2 = lambda n: n + 1 if n > 0 else 0
    print("lambda 内条件 ->", func2(-1), func2(2))


if __name__ == "__main__":
    main()
