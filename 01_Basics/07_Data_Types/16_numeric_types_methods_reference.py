#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 16：数值类型方法全覆盖（int / float / complex）。

你会学到：
1) int 的方法与“数值属性”
2) float 的方法与“数值属性”
3) complex 的方法与“数值属性”

运行（在仓库根目录执行）：
    python3 01_Basics/07_Data_Types/16_numeric_types_methods_reference.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def demo(label: str, value: object) -> None:
    print(f"{label:<36} -> {value!r}")


def main() -> None:
    show("1) int 方法与属性")
    n = 42
    demo("bit_length()", n.bit_length())
    demo("as_integer_ratio()", n.as_integer_ratio())
    demo("conjugate()", n.conjugate())
    demo("numerator", n.numerator)
    demo("denominator", n.denominator)
    demo("real", n.real)
    demo("imag", n.imag)
    demo("to_bytes(2, 'big')", n.to_bytes(2, "big"))
    demo("from_bytes(b'\\x00*', 'big')", int.from_bytes(b"\x00*", "big"))
    if hasattr(n, "bit_count"):
        demo("bit_count()", n.bit_count())  # Python 3.8+

    show("2) float 方法与属性")
    x = 3.5
    demo("as_integer_ratio()", x.as_integer_ratio())
    demo("is_integer()", x.is_integer())
    demo("conjugate()", x.conjugate())
    demo("real", x.real)
    demo("imag", x.imag)
    demo("hex()", x.hex())
    demo("fromhex(x.hex())", float.fromhex(x.hex()))

    show("3) complex 方法与属性")
    z = 3 + 4j
    demo("conjugate()", z.conjugate())
    demo("real", z.real)
    demo("imag", z.imag)


if __name__ == "__main__":
    main()
