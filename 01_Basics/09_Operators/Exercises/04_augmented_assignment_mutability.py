#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：+= 与 + 在可变对象上的差异（别名影响）
Author: Lambert

题目：
实现 `demo()`，要求用代码验证下面事实：
1) list：a = b = [1] 后执行 `a += [2]`：
   - b 会变化
   - a is b 仍为 True
2) list：a = b = [1] 后执行 `a = a + [2]`：
   - b 不变化
   - a is b 变为 False
3) tuple：a = b = (1,) 后执行 `a += (2,)`：
   - b 不变化
   - a is b 变为 False（tuple 不可变，得到新对象）

参考答案：
- 本文件 `demo()` 的实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/09_Operators/Exercises/04_augmented_assignment_mutability.py
"""

from __future__ import annotations


def demo() -> dict[str, object]:
    a1 = b1 = [1]
    a1 += [2]

    a2 = b2 = [1]
    a2 = a2 + [2]

    a3 = b3 = (1,)
    a3 += (2,)

    return {
        "list_plus_equals_b_changed": (b1 == [1, 2]),
        "list_plus_equals_a_is_b": (a1 is b1),
        "list_rebind_b_changed": (b2 == [1, 2]),
        "list_rebind_a_is_b": (a2 is b2),
        "tuple_plus_equals_b_changed": (b3 == (1, 2)),
        "tuple_plus_equals_a_is_b": (a3 is b3),
    }


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    r = demo()
    check("list += changes b", r["list_plus_equals_b_changed"], True)
    check("list += keeps alias", r["list_plus_equals_a_is_b"], True)
    check("list rebind changes b", r["list_rebind_b_changed"], False)
    check("list rebind breaks alias", r["list_rebind_a_is_b"], False)
    check("tuple += changes b", r["tuple_plus_equals_b_changed"], False)
    check("tuple += breaks alias", r["tuple_plus_equals_a_is_b"], False)


if __name__ == "__main__":
    main()
