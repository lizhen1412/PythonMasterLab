#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 06：自定义异常（余额不足）

题目：
实现函数 `withdraw(balance, amount)`：
- amount 必须是非负整数，否则 ValueError
- 如果 amount > balance：抛 InsufficientFundsError
- 否则返回新的余额 balance - amount

参考答案：
- 本文件函数实现即为参考答案；main() 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/13_Exception_Handling/Exercises/06_custom_exception_withdraw.py
"""

from __future__ import annotations


class InsufficientFundsError(Exception):
    pass


def withdraw(balance: int, amount: int) -> int:
    if amount < 0:
        raise ValueError("amount must be >= 0")
    if amount > balance:
        raise InsufficientFundsError(f"balance={balance}, amount={amount}")
    return balance - amount


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def check_raises(label: str, fn, exc_type: type[BaseException]) -> None:
    try:
        fn()
    except exc_type:
        print(f"[OK] {label}: raised {exc_type.__name__}")
    except Exception as exc:
        print(f"[FAIL] {label}: raised {type(exc).__name__}, expected {exc_type.__name__}")
    else:
        print(f"[FAIL] {label}: no exception, expected {exc_type.__name__}")


def main() -> None:
    check("withdraw(100, 30)", withdraw(100, 30), 70)
    check_raises("withdraw(100, -1)", lambda: withdraw(100, -1), ValueError)
    check_raises("withdraw(100, 999)", lambda: withdraw(100, 999), InsufficientFundsError)


if __name__ == "__main__":
    main()

