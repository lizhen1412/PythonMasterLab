#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：数组创建与基础属性。

运行：
    python3 02_Frameworks/02_Numpy/03_array_basics.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([1, 2, 3], dtype=np.int64)
    b = np.arange(0, 6, 2)
    c = np.zeros((2, 3), dtype=float)
    d = np.ones((2, 2), dtype=int)

    print("a ->", a)
    print("b ->", b)
    print("c ->")
    print(c)
    print("d ->")
    print(d)

    print("
属性 ->")
    print("a.shape ->", a.shape)
    print("a.ndim ->", a.ndim)
    print("a.size ->", a.size)
    print("a.dtype ->", a.dtype)


if __name__ == "__main__":
    main()
