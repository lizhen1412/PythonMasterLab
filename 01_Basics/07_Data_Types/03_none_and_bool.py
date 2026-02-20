#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：None 与 bool。
Author: Lambert

你会学到：
1) None 是“空值/缺失值”的常见表示；它是单例：用 `is None` 判断
2) bool 在 if/while 中怎么工作（真值测试）
3) `and/or` 的短路行为：返回的不是 True/False，而是“最后一个参与运算的操作数”
4) 常见坑：`if x:` 会把 0/""/[] 也当成 False；当 0 是合法值时要特别处理

运行（在仓库根目录执行）：
    python3 01_Basics/07_Data_Types/03_none_and_bool.py
"""

from __future__ import annotations


def maybe_get_value(flag: bool) -> str | None:
    if flag:
        return "data"
    return None


def main() -> None:
    print("1) None 判断：用 `is None` / `is not None`")
    value = maybe_get_value(False)
    print("value =", value)
    print("value is None ->", value is None)

    print("\n2) 真值测试（常见 falsy 值）：")
    falsy_values = [None, False, 0, 0.0, "", [], {}, set(), range(0)]
    for v in falsy_values:
        print(f"{v!r:<10} -> bool={bool(v)}")

    print("\n3) and/or 短路：返回操作数本身（不是强制转 bool）")
    a = ""
    b = "fallback"
    print("a or b ->", a or b)
    x = "Alice"
    y = "Bob"
    print("x and y ->", x and y)

    print("\n4) 常见坑：0 是合法值时，不要用 `if x:` 判断是否“有值”")
    maybe_number: int | None = 0
    if maybe_number is None:
        print("没有值")
    else:
        print("有值（允许为 0） ->", maybe_number)

    print("\n5) bool 与 int 的关系（细节）：")
    print("isinstance(True, int) ->", isinstance(True, int))
    print("True + 1 ->", True + 1)
    print("sum([True, False, True]) ->", sum([True, False, True]))


if __name__ == "__main__":
    main()
