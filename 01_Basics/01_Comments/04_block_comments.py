#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：块注释（多行 #）与使用场景。
Author: Lambert

“块注释”通常指连续多行以 `#` 开头的注释，用于解释一段代码、一个算法步骤、
或某段实现的背景/约束。它不是语法结构，只是多行单行注释的组合。

建议：
1) 注释解释“为什么/有什么约束”，尽量不要解释显而易见的“做什么”。
2) 与代码保持同步，避免过期注释误导读者。
"""


def is_prime(n: int) -> bool:
    # 这里用最朴素的试除法判断质数：
    # - 小于 2 的都不是质数
    # - 只需试除到 sqrt(n)
    # 该实现强调可读性，不追求极致性能
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def main() -> None:
    for x in range(1, 20):
        if is_prime(x):
            print(x, "is prime")


if __name__ == "__main__":
    main()