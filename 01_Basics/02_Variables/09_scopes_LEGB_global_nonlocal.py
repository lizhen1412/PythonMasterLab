#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：作用域（Scope）与 LEGB：Local/Enclosing/Global/Builtins。
Author: Lambert

你会学到：
1) 变量查找顺序（LEGB）：局部 -> 闭包外层 -> 全局 -> 内置
2) `global`：在函数里“写全局变量”（不推荐滥用，但要懂）
3) `nonlocal`：在嵌套函数里修改外层函数变量（闭包常用）

说明：
- 本示例尽量让代码在运行时/类型检查器下都“干净”，不会制造未捕获异常。
- 对于容易导致静态检查告警的“反例”，我们用字符串代码 `exec()` 来安全演示。

运行：
    python3 01_Basics/02_Variables/09_scopes_LEGB_global_nonlocal.py
"""

from collections.abc import Callable


counter: int = 0


def increment_global() -> int:
    global counter
    counter += 1
    return counter


def make_counter() -> Callable[[], int]:
    count = 0

    def inc() -> int:
        nonlocal count
        count += 1
        return count

    return inc


def demonstrate_legb() -> None:
    builtins_len = len  # Builtins: 内置函数 len
    x = "enclosing"

    def inner() -> None:
        local_x = "local"
        print("local_x =", local_x)  # Local
        print("x =", x)  # Enclosing
        print("len([1,2,3]) =", builtins_len([1, 2, 3]))  # Builtins（通过引用使用）

    inner()


def demonstrate_unboundlocalerror_safely() -> None:
    bad = """
x = 0

def f():
    # 因为有赋值动作，x 会被视为局部变量；但局部变量 x 又在赋值前被读取
    x += 1

f()
"""
    print("\n安全演示：函数内修改外部变量但没写 global/nonlocal 会怎样？")
    try:
        exec(bad, {})
    except UnboundLocalError as exc:
        print("UnboundLocalError:", exc)


def main() -> None:
    print("1) LEGB 示例：")
    demonstrate_legb()

    print("\n2) global 示例：")
    print("counter =", counter)
    print("increment_global() ->", increment_global())
    print("increment_global() ->", increment_global())
    print("counter =", counter)

    print("\n3) nonlocal 示例：")
    c1 = make_counter()
    c2 = make_counter()
    print("c1() ->", c1(), c1(), c1())
    print("c2() ->", c2(), c2())

    demonstrate_unboundlocalerror_safely()


if __name__ == "__main__":
    main()
