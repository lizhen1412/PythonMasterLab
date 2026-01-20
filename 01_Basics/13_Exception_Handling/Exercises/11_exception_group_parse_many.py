#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 11（进阶）：ExceptionGroup + except*（Python 3.11+）

题目：
实现函数 `parse_many_ints(values)`：
- 输入：字符串列表 values
- 输出：全部成功时返回 int 列表
- 如果有任何一个元素无法解析为 int：
  - 收集每个失败位置的 ValueError
  - 最后抛 `ExceptionGroup("parse_many_ints failed", errors)`

参考答案：
- 本文件函数实现即为参考答案；main() 演示 except* 的捕获方式。

运行：
    python3 01_Basics/13_Exception_Handling/Exercises/11_exception_group_parse_many.py
"""

from __future__ import annotations


def parse_many_ints(values: list[str]) -> list[int]:
    results: list[int] = []
    errors: list[ValueError] = []
    for i, s in enumerate(values):
        try:
            results.append(int(s))
        except ValueError:
            errors.append(ValueError(f"index={i}, value={s!r}"))
    if errors:
        raise ExceptionGroup("parse_many_ints failed", errors)
    return results


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("all ok", parse_many_ints(["1", "2", "3"]), [1, 2, 3])

    try:
        parse_many_ints(["1", "x", "y"])
    except* ValueError as group:
        check("errors count", len(group.exceptions), 2)


if __name__ == "__main__":
    main()

