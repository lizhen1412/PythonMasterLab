#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：a += ... vs a = a + ...（别名与可变性）

题目：
写一个小实验，回答下面问题并用代码验证：
1) 当 `a` 和 `b` 引用同一个 list 时：
   - 执行 `a += [x]` 后，b 会不会变化？a is b 是否仍为 True？
   - 执行 `a = a + [x]` 后，b 会不会变化？a is b 是否仍为 True？
2) tuple 上执行 `a += (...)` 会发生什么？（提示：tuple 不可变）

参考答案：
- 本文件 `demo()` 的实现即参考答案；`main()` 会打印自测结论（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/02_Variables/04_augmented_assignment_vs_concat.py
"""


def demo() -> dict[str, object]:
    a1 = b1 = [1]
    a1 += [2]

    a2 = b2 = [1]
    a2 = a2 + [2]

    a3 = b3 = (1,)
    a3 += (2,)

    return {
        "list_plus_equals_b_changed": b1 == [1, 2],
        "list_plus_equals_a_is_b": a1 is b1,
        "list_rebind_b_changed": b2 == [1, 2],
        "list_rebind_a_is_b": a2 is b2,
        "tuple_plus_equals_b_changed": b3 == (1, 2),
        "tuple_plus_equals_a_is_b": a3 is b3,
    }


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    result = demo()
    check("list += changes b", result["list_plus_equals_b_changed"], True)
    check("list += keeps alias", result["list_plus_equals_a_is_b"], True)
    check("list rebind changes b", result["list_rebind_b_changed"], False)
    check("list rebind breaks alias", result["list_rebind_a_is_b"], False)
    check("tuple += changes b", result["tuple_plus_equals_b_changed"], False)
    check("tuple += breaks alias", result["tuple_plus_equals_a_is_b"], False)


if __name__ == "__main__":
    main()

