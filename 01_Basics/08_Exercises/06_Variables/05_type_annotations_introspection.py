#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：类型注解（__annotations__ 与 get_type_hints）
Author: Lambert

题目：
实现 `get_annotations(obj)`，返回两个 dict：
1) raw：直接读取 `obj.__annotations__`（不会解析 ForwardRef）
2) resolved：`typing.get_type_hints(obj)` 的结果（会解析字符串注解）

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/06_Variables/05_type_annotations_introspection.py
"""

from typing import get_type_hints


def add(a: int, b: int) -> int:
    return a + b


def get_annotations(obj) -> tuple[dict[str, object], dict[str, object]]:
    raw = getattr(obj, "__annotations__", {})
    resolved = get_type_hints(obj)
    return raw, resolved


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    raw, resolved = get_annotations(add)
    check("has_a", raw.get("a") is int, True)
    check("has_return", resolved.get("return") is int, True)


if __name__ == "__main__":
    main()