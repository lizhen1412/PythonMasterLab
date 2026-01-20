#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：`*args/**kwargs` 与解包。

- 收集变长参数：`def func(*args, **kwargs): ...`
- 解包调用：`func(*seq, **mapping)`
- 参数转发：包装/装饰时透传 `*args, **kwargs`
- `**` 合并 mapping 时后者覆盖前者
"""

from __future__ import annotations

from typing import Any, Iterable


def summarize(*args: Any, **kwargs: Any) -> str:
    """打印收到的所有参数，观察收集行为。"""
    return f"args={args}, kwargs={kwargs}"


def call_with_unpacking() -> None:
    """演示解包调用与覆盖规则。"""
    numbers = [1, 2, 3]
    more = (4, 5)
    opts = {"sep": ",", "end": "!"}
    override = {"end": "?"}

    print("summarize(*numbers) ->", summarize(*numbers))
    print("summarize(*numbers, *more) ->", summarize(*numbers, *more))
    print("print(*numbers, **opts) ->", end=" ")
    print(*numbers, **opts)  # 标准库函数也支持解包

    # 后面的 mapping 覆盖前面的 key
    print("summarize(**opts, **override) ->", summarize(**opts, **override))


def forward_args(func, *args: Any, **kwargs: Any) -> Any:
    """包装器：透传所有参数，并记录调用次数。"""
    forward_args.calls += 1  # type: ignore[attr-defined]
    print(f"[DEBUG] call {forward_args.calls} -> forwarding to {func.__name__}")
    return func(*args, **kwargs)


forward_args.calls = 0  # type: ignore[attr-defined]


def multiply(*numbers: float) -> float:
    """把所有数字相乘。"""
    result = 1.0
    for n in numbers:
        result *= n
    return result


def star_in_literals() -> None:
    """`*` 还能在字面量/推导式里解包（与乘法语义区分开）。"""
    a = [1, 2]
    b = [*a, 3, 4]
    print("列表解包 ->", b)

    merged = {**{"x": 1}, **{"y": 2, "x": 99}}
    print("dict 解包覆盖 ->", merged)


def main() -> None:
    print("== 收集与解包 ==")
    call_with_unpacking()

    print("\n== 参数转发 ==")
    print("multiply via forward_args ->", forward_args(multiply, 2, 3, 4))
    print("forward_args.calls ->", forward_args.calls)

    print("\n== 星号在字面量中的解包 ==")
    star_in_literals()


if __name__ == "__main__":
    main()
