#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：格式化规格——浮点（float）与 Decimal。
Author: Lambert

你会学到：
1) `f`：定点小数；`.2f` 控制小数位
2) `e`/`E`：科学计数法
3) `g`：自动选择更短表示（常用于“合理显示”）
4) `%`：百分比（值会乘以 100 并加 %）
5) 宽度/对齐/填充：让列对齐更专业
6) `Decimal`：避免部分二进制浮点误差（金融/精确计算常见）

运行：
    python3 01_Basics/04_Formatting/05_format_spec_floats_and_decimal.py
"""

from decimal import Decimal


def main() -> None:
    x = 1234.56789
    ratio = 0.375

    print("1) f / 精度：")
    print(f"x={x} x={x:.2f} x={x:10.2f}")

    print("\n2) e / E：")
    print(f"{x:e}")
    print(f"{x:E}")

    print("\n3) g：")
    for v in [1234.56789, 0.000012345, 123456789.0]:
        print(f"v={v} -> {v:g} / {v:.6g}")

    print("\n4) 百分比：")
    print(f"ratio={ratio} -> {ratio:.1%}")

    print("\n5) 分组与对齐：")
    print(f"{x:>12,.2f}")
    print(f"{-x:>12,.2f}")

    print("\n6) float vs Decimal：")
    a = 0.1 + 0.2
    b = Decimal("0.1") + Decimal("0.2")
    print(f"float 0.1+0.2   -> {a!r}")
    print(f"Decimal 0.1+0.2 -> {b!r}")
    print(f"Decimal formatted -> {b:.2f}")


if __name__ == "__main__":
    main()
