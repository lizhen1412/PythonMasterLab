#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：单分支 if（如果不存在就追加）

题目：
实现 `append_if_missing(items, value)`，要求：
- 如果 value 不在 items 里，就 append，并返回 True
- 如果 value 已存在，就不改动 items，并返回 False

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/10_Conditionals/Exercises/03_single_branch_append_if_missing.py
"""

from __future__ import annotations


def append_if_missing(items: list[str], value: str) -> bool:
    if value not in items:
        items.append(value)
        return True
    return False


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    items = ["a"]
    check("append_existing", append_if_missing(items, "a"), False)
    check("items_unchanged", items, ["a"])
    check("append_new", append_if_missing(items, "b"), True)
    check("items_changed", items, ["a", "b"])


if __name__ == "__main__":
    main()

