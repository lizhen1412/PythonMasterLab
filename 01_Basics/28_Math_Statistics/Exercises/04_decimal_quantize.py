#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 04: Decimal rounding.

Task:
Implement round_money(text) -> str to 2 decimal places.

Run:
    python3 01_Basics/28_Math_Statistics/Exercises/04_decimal_quantize.py
"""

from decimal import Decimal, ROUND_HALF_UP


def round_money(text: str) -> str:
    value = Decimal(text)
    rounded = value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"{rounded:.2f}"


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("10.125", round_money("10.125"), "10.13")
    check("2", round_money("2"), "2.00")


if __name__ == "__main__":
    main()
