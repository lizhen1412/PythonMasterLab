#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：类型注解（type annotations）与变量。
Author: Lambert

重点结论：
- 类型注解主要服务于 IDE/类型检查器（pyright/mypy 等），**不会强制运行时类型**。

你会学到：
1) 变量/函数的注解写法：`x: int = 1`、`def f(x: int) -> int: ...`
2) `__annotations__`：注解会存到哪里
3) `typing.get_type_hints()`：把注解解析出来（更像“给工具用”）
4) `typing.cast()`：只影响类型检查，不做运行时转换

运行（在仓库根目录执行）：
    python3 01_Basics/06_Variables/07_type_annotations.py
"""

from __future__ import annotations

from typing import cast, get_type_hints


def add(a: int, b: int) -> int:
    return a + b


def accept_int(x: int) -> None:
    print("accept_int got value =", x, "runtime type =", type(x).__name__)


def plus_one(x: int) -> int:
    return x + 1


def main() -> None:
    x: int = 1
    names: list[str] = ["Alice", "Bob"]
    mapping: dict[str, int] = {"Alice": 20}
    print("x =", x)
    print("names =", names)
    print("mapping =", mapping)

    print("\n1) __annotations__：")
    print("module __annotations__ =", __annotations__)
    print("add.__annotations__ =", add.__annotations__)

    print("\n2) get_type_hints（解析后的类型提示）：")
    print("module hints =", get_type_hints(__import__(__name__)))
    print("add hints =", get_type_hints(add))

    print("\n3) cast：只影响类型检查，不会转换值")
    raw: object = "123"
    as_int = cast(int, raw)
    print("raw =", raw, "type =", type(raw).__name__)
    print("as_int =", as_int, "type =", type(as_int).__name__)
    print("注意：这里的 as_int 仍然是 str，只是 cast 让类型检查器“相信它是 int”。")

    print("\n4) 想真正转换类型，请用 int()/float()/...：")
    real_int = int(cast(str, raw))
    print("real_int =", real_int, "type =", type(real_int).__name__)

    print("\n5) 运行时不强制类型（演示：类型检查器相信你，但运行时不会转换）：")
    accept_int(as_int)
    try:
        print("plus_one(as_int) ->", plus_one(as_int))
    except TypeError as exc:
        print("TypeError:", exc)


if __name__ == "__main__":
    main()