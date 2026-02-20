#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 13：内置函数全覆盖（Built-in Functions Reference）
Author: Lambert

你会学到：
1) 所有内置函数的分类与最小可运行示例
2) 哪些函数会交互/阻塞（help/breakpoint/input/open）
3) eval/exec/compile 与 __import__ 的安全演示方式

运行（在仓库根目录执行）：
    python3 01_Basics/14_Functions/13_builtin_functions_reference.py
"""

from __future__ import annotations

import asyncio
import io
from contextlib import redirect_stdin
from typing import Any


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def demo(label: str, value: object) -> None:
    print(f"{label:<38} -> {value!r}")


def core_types_and_constructors() -> None:
    show("1) 核心构造与类型")
    demo("object()", object())
    demo("bool(0)", bool(0))
    demo("int('10')", int("10"))
    demo("float('3.5')", float("3.5"))
    demo("complex(2, 3)", complex(2, 3))
    demo("str(123)", str(123))
    demo("bytes('hi', 'utf-8')", bytes("hi", "utf-8"))

    b = bytearray(b"ab")
    b[0] = ord("z")
    demo("bytearray mutate", b)
    mv = memoryview(b"abc")
    demo("memoryview[0]", mv[0])

    demo("list((1, 2))", list((1, 2)))
    demo("tuple([1, 2])", tuple([1, 2]))
    demo("set([1, 1, 2])", set([1, 1, 2]))
    demo("frozenset([1, 2])", frozenset([1, 2]))
    demo("dict([('a', 1)])", dict([("a", 1)]))
    demo("range(1, 5, 2)", list(range(1, 5, 2)))

    s = slice(1, 5, 2)
    demo("slice(1, 5, 2)", s)
    demo("apply slice", [0, 1, 2, 3, 4, 5][s])


def numeric_and_representation() -> None:
    show("2) 数值与表示")
    demo("abs(-3)", abs(-3))
    demo("round(2.675, 2)", round(2.675, 2))
    demo("pow(2, 5)", pow(2, 5))
    demo("pow(2, 5, 7)", pow(2, 5, 7))
    demo("divmod(17, 5)", divmod(17, 5))
    demo("bin(10)", bin(10))
    demo("oct(10)", oct(10))
    demo("hex(10)", hex(10))
    demo("chr(65)", chr(65))
    demo("ord('A')", ord("A"))
    demo("format(3.14159, '.2f')", format(3.14159, ".2f"))


def aggregation_and_predicates() -> None:
    show("3) 聚合与判断")
    nums = [0, 1, 2, 3]
    demo("len(nums)", len(nums))
    demo("sum(nums)", sum(nums))
    demo("sum(nums, 10)", sum(nums, 10))
    demo("min(nums)", min(nums))
    demo("max(nums)", max(nums))
    demo("any(nums)", any(nums))
    demo("all([1, 2, 3])", all([1, 2, 3]))


def iteration_tools() -> None:
    show("4) 迭代工具")
    it = iter([1, 2, 3])
    demo("next(it)", next(it))
    demo("list(it)", list(it))
    demo("enumerate(['a', 'b'])", list(enumerate(["a", "b"], start=1)))
    demo("zip([1,2], ['a','b'])", list(zip([1, 2], ["a", "b"])))
    demo("map(lambda x: x*2, [1,2])", list(map(lambda x: x * 2, [1, 2])))
    demo("filter(lambda x: x%2, [1,2,3])", list(filter(lambda x: x % 2, [1, 2, 3])))
    demo("reversed([1,2,3])", list(reversed([1, 2, 3])))
    demo("sorted([3,1,2])", sorted([3, 1, 2]))


def introspection_and_attributes() -> None:
    show("5) 反射与属性工具")

    class Box:
        def __init__(self, value: int) -> None:
            self.value = value

        def __repr__(self) -> str:
            return f"Box(value={self.value})"

    class CallableBox:
        def __call__(self, x: int) -> int:
            return x * 2

    box = Box(10)
    demo("type(box).__name__", type(box).__name__)
    demo("isinstance(box, Box)", isinstance(box, Box))
    demo("issubclass(Box, object)", issubclass(Box, object))
    demo("callable(Box)", callable(Box))
    demo("callable(CallableBox())", callable(CallableBox()))
    demo("id(box)", id(box))
    demo("hash(123)", hash(123))
    demo("repr(box)", repr(box))
    demo("ascii('hi\\n')", ascii("hi\n"))

    demo("hasattr(box, 'value')", hasattr(box, "value"))
    demo("getattr(box, 'value')", getattr(box, "value"))
    setattr(box, "value", 99)
    demo("after setattr", box.value)
    delattr(box, "value")
    demo("hasattr after delattr", hasattr(box, "value"))

    box.extra = "ok"
    demo("vars(box)", vars(box))
    demo("dir(box)[:5]", dir(box)[:5])


def globals_locals_and_eval() -> None:
    show("6) 作用域与动态执行")
    x = 10

    def scope_demo() -> None:
        y = 20
        demo("locals has y", "y" in locals())
        demo("globals has x", "x" in globals())
        demo("vars().keys()", sorted(vars().keys()))

    scope_demo()

    expr = compile("a + b", "<expr>", "eval")
    demo("eval(compile)", eval(expr, {}, {"a": 2, "b": 3}))

    ns: dict[str, Any] = {}
    exec("m = 7\nn = 8\ns = m + n", ns)
    demo("exec result s", ns["s"])

    math_mod = __import__("math")
    demo("__import__('math').sqrt(9)", math_mod.sqrt(9))


def io_helpers() -> None:
    show("7) 输入输出相关")
    print("print with sep/end:", "A", "B", sep="|", end="!\n")

    fake = io.StringIO("Alice\n")
    with redirect_stdin(fake):
        name = input()
    demo("input()", name)

    with open(__file__, "r", encoding="utf-8") as fh:
        first_line = fh.readline().rstrip("\n")
    demo("open(__file__)", first_line)


def oop_helpers() -> None:
    show("8) OOP 辅助：property/staticmethod/classmethod/super")

    class Base:
        def greet(self) -> str:
            return "base"

    class Child(Base):
        def greet(self) -> str:
            return f"child->{super().greet()}"

    class Tool:
        def __init__(self, n: int) -> None:
            self.n = n

        @property
        def double(self) -> int:
            return self.n * 2

        @staticmethod
        def add(a: int, b: int) -> int:
            return a + b

        @classmethod
        def from_double(cls, value: int) -> "Tool":
            return cls(value // 2)

    demo("Child().greet()", Child().greet())
    demo("Tool(3).double", Tool(3).double)
    demo("Tool.add(2, 3)", Tool.add(2, 3))
    demo("Tool.from_double(8).n", Tool.from_double(8).n)


async def async_demo() -> None:
    async def agen() -> Any:
        for i in range(2):
            yield i

    it = aiter(agen())
    first = await anext(it)
    second = await anext(it)
    end = await anext(it, "end")
    print("aiter/anext ->", first, second, end)


def async_helpers() -> None:
    show("9) 异步内置函数")
    asyncio.run(async_demo())


def interactive_skips() -> None:
    show("10) 交互内置函数（示例中不直接调用）")
    demo("help (skipped)", help)
    demo("breakpoint (skipped)", breakpoint)


def main() -> None:
    core_types_and_constructors()
    numeric_and_representation()
    aggregation_and_predicates()
    iteration_tools()
    introspection_and_attributes()
    globals_locals_and_eval()
    io_helpers()
    oop_helpers()
    async_helpers()
    interactive_skips()


if __name__ == "__main__":
    main()