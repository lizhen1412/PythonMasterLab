#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 04: decimal context and rounding.
Author: Lambert

Run:
    python3 01_Basics/28_Math_Statistics/04_decimal_context.py
"""

from decimal import Decimal, ROUND_HALF_UP, getcontext


def main() -> None:
    getcontext().prec = 6
    a = Decimal("1") / Decimal("3")
    print("1/3 ->", a)

    price = Decimal("10.125")
    rounded = price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    print("rounded ->", rounded)


if __name__ == "__main__":
    main()