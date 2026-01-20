#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：验证 // 与 % 的恒等式（含负数）

题目：
实现 `check_div_mod(a, b)`，要求：
1) b != 0
2) 返回一个 dict，至少包含：
   - q = a // b
   - r = a % b
   - identity_ok: a == q*b + r
   - remainder_range_ok: abs(r) < abs(b)
   - remainder_sign_ok: r == 0 or r 与 b 同号

参考答案：
- 本文件函数实现即为参考答案；`main()` 会对多组正/负样例做自测。

运行：
    python3 01_Basics/09_Operators/Exercises/03_floor_div_mod_rules.py
"""

from __future__ import annotations


def check_div_mod(a: int, b: int) -> dict[str, object]:
    if b == 0:
        raise ValueError("b must not be 0")

    q = a // b
    r = a % b
    return {
        "q": q,
        "r": r,
        "identity_ok": a == q * b + r,
        "remainder_range_ok": abs(r) < abs(b),
        "remainder_sign_ok": (r == 0) or ((r > 0) == (b > 0)),
    }


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    samples = [(7, 3), (-7, 3), (7, -3), (-7, -3)]
    for a, b in samples:
        result = check_div_mod(a, b)
        check(f"identity({a},{b})", result["identity_ok"], True)
        check(f"range({a},{b})", result["remainder_range_ok"], True)
        check(f"sign({a},{b})", result["remainder_sign_ok"], True)


if __name__ == "__main__":
    main()

