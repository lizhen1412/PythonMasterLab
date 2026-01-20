#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：用 list 实现“栈”（stack）

题目：
用一个 Python list 实现栈的 3 个基本操作：
1) push(stack, item)：入栈（append）
2) pop_stack(stack)：出栈（pop）并返回元素
3) peek(stack)：返回栈顶元素但不弹出

约定：
- pop_stack/peek 在空栈上调用：抛 IndexError

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/12_Composite_Types/Exercises/04_list_stack_ops.py
"""

from __future__ import annotations

from typing import TypeVar

T = TypeVar("T")


def push(stack: list[T], item: T) -> None:
    stack.append(item)


def pop_stack(stack: list[T]) -> T:
    if not stack:
        raise IndexError("pop from empty stack")
    return stack.pop()


def peek(stack: list[T]) -> T:
    if not stack:
        raise IndexError("peek from empty stack")
    return stack[-1]


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def check_raises(label: str, fn, exc_type: type[BaseException]) -> None:
    try:
        fn()
    except exc_type:
        print(f"[OK] {label}: raised {exc_type.__name__}")
    except Exception as exc:  # tiny self-check helper
        print(f"[FAIL] {label}: raised {type(exc).__name__}, expected {exc_type.__name__}")
    else:
        print(f"[FAIL] {label}: no exception, expected {exc_type.__name__}")


def main() -> None:
    s: list[int] = []
    check_raises("peek(empty)", lambda: peek(s), IndexError)
    check_raises("pop(empty)", lambda: pop_stack(s), IndexError)

    push(s, 10)
    push(s, 20)
    check("peek([10,20])", peek(s), 20)
    check("pop -> 20", pop_stack(s), 20)
    check("pop -> 10", pop_stack(s), 10)
    check("stack empty", s, [])


if __name__ == "__main__":
    main()
