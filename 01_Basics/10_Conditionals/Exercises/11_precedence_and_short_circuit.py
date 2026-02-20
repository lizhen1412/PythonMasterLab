#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 11：优先级与短路（安全写条件）
Author: Lambert

题目：
实现 `is_valid_username(name)`，规则：
- name 必须是 str
- strip 后不能为空
- 长度在 [3, 20]
- 只能包含字母/数字/下划线（_）

要求：
- 必须使用短路：先判断类型，再调用 `.strip()`，否则会对非 str 抛异常
- 尽量用“可读”的括号组织条件（不要赌优先级）

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 01_Basics/10_Conditionals/Exercises/11_precedence_and_short_circuit.py
"""

from __future__ import annotations


def is_valid_username(name: object) -> bool:
    if not isinstance(name, str):
        return False

    s = name.strip()
    if not s:
        return False
    if not (3 <= len(s) <= 20):
        return False

    # 只允许字母/数字/下划线
    return s.replace("_", "").isalnum()


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("not_str", is_valid_username(123), False)
    check("blank", is_valid_username("   "), False)
    check("short", is_valid_username("ab"), False)
    check("ok", is_valid_username("user_01"), True)
    check("bad_char", is_valid_username("a-b"), False)
    check("trim_ok", is_valid_username("  Alice_9  "), True)


if __name__ == "__main__":
    main()
