#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：try 语句的各种写法（except/else/finally/except*）
Author: Lambert

你会学到：
1) try/except：捕获并处理
2) 多个 except：先具体后泛化
3) except (...)：一次捕获多种类型
4) try/except/else：成功路径放到 else
5) finally：一定执行（清理资源/回收状态）
6) Python 3.11+：except* 处理 ExceptionGroup

运行（在仓库根目录执行）：
    python3 01_Basics/13_Exception_Handling/05_try_statement_patterns.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def parse_int(text: str) -> int:
    return int(text)


def demo_try_except_else_finally(text: str) -> None:
    show("1) try/except/else/finally：推荐结构")
    try:
        n = parse_int(text)
    except ValueError as exc:
        print("ValueError ->", exc)
    else:
        print("parsed int ->", n)
    finally:
        print("finally：这里一定会执行（比如释放资源/写日志/回收状态）")


def demo_multiple_except() -> None:
    show("2) 多分支 except：先具体后泛化")

    def may_fail(kind: str) -> None:
        if kind == "value":
            raise ValueError("bad value")
        if kind == "type":
            raise TypeError("bad type")
        raise RuntimeError("other error")

    for kind in ["value", "type", "other"]:
        try:
            may_fail(kind)
        except ValueError as exc:
            print("caught ValueError:", exc)
        except TypeError as exc:
            print("caught TypeError:", exc)
        except Exception as exc:
            print("caught generic Exception:", type(exc).__name__, exc)


def demo_except_tuple() -> None:
    show("3) except (A, B)：一次捕获多种异常")
    for s in ["123", "x"]:
        try:
            n = int(s)
            print("ok:", n)
        except (TypeError, ValueError) as exc:
            print("caught:", type(exc).__name__, exc)


def demo_try_finally_with_return() -> None:
    show("4) try/finally：即使 return 也会执行 finally")

    def f() -> int:
        try:
            return 1
        finally:
            print("finally in f()")

    print("f() ->", f())


def demo_exception_group_py311() -> None:
    show("5) Python 3.11+：ExceptionGroup 与 except*（进阶）")
    eg = ExceptionGroup("batch", [ValueError("bad value"), TypeError("bad type")])
    try:
        raise eg
    except* ValueError as group:
        print("except* ValueError ->", [type(e).__name__ for e in group.exceptions])
    except* TypeError as group:
        print("except* TypeError ->", [type(e).__name__ for e in group.exceptions])


def main() -> None:
    demo_try_except_else_finally("42")
    demo_try_except_else_finally("not-a-number")
    demo_multiple_except()
    demo_except_tuple()
    demo_try_finally_with_return()
    demo_exception_group_py311()


if __name__ == "__main__":
    main()
