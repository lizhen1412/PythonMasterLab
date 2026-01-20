#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：广播与向量化运算。

运行：
    python3 02_Frameworks/02_Numpy/07_broadcasting_ops.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    mat = np.arange(1, 7).reshape(2, 3)
    row = np.array([10, 20, 30])
    col = np.array([[1], [2]])

    print("mat ->")
    print(mat)
    print("row ->", row)
    print("col ->")
    print(col)

    print("
mat + row（按列广播）->")
    print(mat + row)

    print("
mat * col（按行广播）->")
    print(mat * col)


if __name__ == "__main__":
    main()
