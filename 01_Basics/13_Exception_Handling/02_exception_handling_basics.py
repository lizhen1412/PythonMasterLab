#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：异常处理基础（异常是什么？怎么读 traceback？）

你会学到：
1) SyntaxError/IndentationError（解析阶段） vs Exception（运行阶段）
2) traceback（调用栈）怎么读：最后一行是“异常类型 + 消息”
3) BaseException vs Exception：为什么通常只 catch Exception

运行（在仓库根目录执行）：
    python3 01_Basics/13_Exception_Handling/02_exception_handling_basics.py
"""

from __future__ import annotations

import traceback


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def demo_traceback() -> None:
    def level_1() -> float:
        # Call level_2, which will propagate exceptions up the call stack
        return level_2()

    def level_2() -> float:
        # Call level_3, which will raise ZeroDivisionError and propagate up the call stack
        return level_3()

    def level_3() -> float:
        return 1 / 0

    try:
        level_1()
    except ZeroDivisionError as exc:
        print("捕获到异常：", type(exc).__name__, "-", exc)
        print("\ntraceback.print_exc() 输出（包含调用栈）：")
        traceback.print_exc()


def demo_syntax_error_catchable_via_compile() -> None:
    code = "x = )"
    try:
        compile(code, "<string>", "exec")
    except SyntaxError as exc:
        print("compile(...) 捕获到 SyntaxError：", exc)


def main() -> None:
    show("1) 运行时异常（Exception）会产生 traceback")
    demo_traceback()

    show("2) SyntaxError 通常是“写代码就错了”，但可以通过 compile/exec 捕获")
    demo_syntax_error_catchable_via_compile()

    show("3) BaseException vs Exception：通常只 catch Exception")
    print("issubclass(KeyboardInterrupt, Exception) ->", issubclass(KeyboardInterrupt, Exception))
    print("issubclass(SystemExit, Exception) ->", issubclass(SystemExit, Exception))
    print("issubclass(ValueError, Exception) ->", issubclass(ValueError, Exception))
    print("建议：业务代码优先写 `except Exception as exc:`，避免无脑 `except:`。")


if __name__ == "__main__":
    main()

