#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：类型转换（显式转换 + 常见坑）。

你会学到：
1) `int/float/str`：最常用的显式转换
2) `Decimal`：十进制定点表示（金融/精确计算常见）
3) `bool(x)` 的坑：非空字符串永远是 True（`bool("False") is True`）
4) “解析 bool”通常需要自定义规则（例如 y/n、true/false、1/0）

运行（在仓库根目录执行）：
    python3 01_Basics/06_Variables/06_type_conversions.py
"""

from __future__ import annotations

from decimal import Decimal


TRUE_SET = {"1", "true", "t", "yes", "y", "on"}
FALSE_SET = {"0", "false", "f", "no", "n", "off"}


def parse_bool(text: str) -> bool:
    normalized = text.strip().lower()
    if normalized in TRUE_SET:
        return True
    if normalized in FALSE_SET:
        return False
    raise ValueError(f"cannot parse bool from {text!r}")


def main() -> None:
    print("1) 基本转换：")
    print("int('42') ->", int("42"))
    print("float('3.14') ->", float("3.14"))
    print("str(123) ->", str(123))

    print("\n2) Decimal：")
    a = Decimal("0.1") + Decimal("0.2")
    print("Decimal('0.1') + Decimal('0.2') ->", a)

    print("\n3) bool(x) 的常见坑：")
    for s in ["", "0", "False", "no", "anything"]:
        print(f"bool({s!r}) -> {bool(s)}")
    print("结论：想从字符串得到 True/False，不要用 bool(s)，要自己解析。")

    print("\n4) 自定义 parse_bool：")
    for s in ["y", "N", "true", "0", "off"]:
        print(f"{s!r} -> {parse_bool(s)}")

    print("\n5) 解析失败示例（捕获异常演示）：")
    try:
        _ = parse_bool("maybe")
    except ValueError as exc:
        print("ValueError:", exc)


if __name__ == "__main__":
    main()

