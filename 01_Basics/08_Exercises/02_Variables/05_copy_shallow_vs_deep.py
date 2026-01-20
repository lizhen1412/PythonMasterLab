#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：浅拷贝 vs 深拷贝（嵌套结构共享问题）

题目：
实现 `copy_sharing_flags()`，要求：
1) 构造一个嵌套结构，例如 `[[1, 2], [3, 4]]`
2) 分别做浅拷贝与深拷贝
3) 修改原对象的“内层 list”
4) 返回两个 bool：
   - shallow 是否与原对象共享“内层 list”
   - deep 是否与原对象共享“内层 list”

参考答案：
- 本文件中函数实现即参考答案；`main()` 里带自测输出（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/02_Variables/05_copy_shallow_vs_deep.py
"""

import copy


def copy_sharing_flags() -> tuple[bool, bool]:
    nested = [[1, 2], [3, 4]]
    shallow = copy.copy(nested)
    deep = copy.deepcopy(nested)

    nested[0].append(99)
    return (shallow[0] is nested[0], deep[0] is nested[0])


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    shallow_shares, deep_shares = copy_sharing_flags()
    check("shallow_shares_inner", shallow_shares, True)
    check("deep_shares_inner", deep_shares, False)


if __name__ == "__main__":
    main()

