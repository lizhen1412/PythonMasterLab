#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：变量名合法性与常见命名坑

题目：
实现 `is_good_variable_name(name)`，要求：
1) 必须是合法标识符：`name.isidentifier()`
2) 不能是关键字：`keyword.iskeyword(name)`
3) 尽量避免遮蔽内置名（可选但建议）：例如 `list`, `str`, `id`

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/06_Variables/03_variable_name_validation.py
"""

import builtins
import keyword


def is_good_variable_name(name: str) -> bool:
    if not name.isidentifier():
        return False
    if keyword.iskeyword(name):
        return False
    if hasattr(builtins, name):
        return False
    return True


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("good", is_good_variable_name("user_name"), True)
    check("bad_keyword", is_good_variable_name("class"), False)
    check("bad_identifier", is_good_variable_name("1x"), False)
    check("bad_builtin", is_good_variable_name("list"), False)


if __name__ == "__main__":
    main()

