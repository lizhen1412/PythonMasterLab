#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：递归函数。

- 必须先写“基线” + “收敛步骤”，避免无限递归
- Python 没有尾递归优化，递归深度受 `sys.getrecursionlimit()` 限制
- 用迭代作为对照，理解何时应避免递归
"""

from __future__ import annotations

import sys
from typing import Any


def factorial_recursive(n: int) -> int:
    """阶乘递归版：基线 n <= 1 返回 1。"""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """阶乘迭代版：对照递归，避免栈深限制。"""
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fib_recursive(n: int) -> int:
    """朴素递归版 Fibonacci（指数级，演示慢）。"""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def tree_depth(tree: list[Any]) -> int:
    """
    递归求“嵌套列表”的最大深度。
    基线：空列表深度为 1；遇到非 list 视作叶子节点。
    """
    if not isinstance(tree, list):
        return 0
    if not tree:
        return 1
    return 1 + max(tree_depth(sub) for sub in tree)


def main() -> None:
    print("sys.getrecursionlimit() ->", sys.getrecursionlimit())

    print("\n== 阶乘：递归 vs 迭代 ==")
    print("factorial_recursive(5) ->", factorial_recursive(5))
    print("factorial_iterative(5) ->", factorial_iterative(5))

    print("\n== Fibonacci（小规模演示） ==")
    print("fib_recursive(6) ->", fib_recursive(6))

    print("\n== 嵌套结构深度 ==")
    nested = [1, [2, [3, [4]]], 5]
    print("tree_depth", nested, "->", tree_depth(nested))

    print("\n提示：大规模递归请考虑迭代或显式栈，避免递归深度限制。")


if __name__ == "__main__":
    main()
