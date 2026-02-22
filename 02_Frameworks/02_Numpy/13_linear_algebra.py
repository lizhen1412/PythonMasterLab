#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 13：线性代数入门（dot/@/solve/norm）。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/13_linear_algebra.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[2, 0], [1, 2]])

    print("a ->")
    print(a)
    print("b ->")
    print(b)

    print("\na @ b ->")
    print(a @ b)

    print("\ndot(a, b) ->")
    print(np.dot(a, b))

    v = np.array([3, 4])
    print("\nvector norm ->", np.linalg.norm(v))

    A = np.array([[2, 1], [1, 3]])
    y = np.array([1, 2])
    x = np.linalg.solve(A, y)
    print("\nsolve Ax=y ->", x)


if __name__ == "__main__":
    main()
