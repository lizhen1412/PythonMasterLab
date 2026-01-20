#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：set 集合运算

题目：
实现 `set_ops(a, b)`，返回一个 dict，包含：
- union / intersection / difference / symmetric_difference

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/07_Data_Types/04_set_operations.py
"""


def set_ops(a: set[int], b: set[int]) -> dict[str, set[int]]:
    return {
        "union": a | b,
        "intersection": a & b,
        "difference": a - b,
        "symmetric_difference": a ^ b,
    }


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    out = set_ops({1, 2, 3}, {3, 4})
    check("union", out["union"], {1, 2, 3, 4})
    check("intersection", out["intersection"], {3})
    check("difference", out["difference"], {1, 2})
    check("sym_diff", out["symmetric_difference"], {1, 2, 4})


if __name__ == "__main__":
    main()

