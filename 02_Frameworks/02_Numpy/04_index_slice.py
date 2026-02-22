#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：索引与切片。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/04_index_slice.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    arr = np.arange(1, 13).reshape(3, 4)
    print("arr ->")
    print(arr)

    print("\n单个元素 ->", arr[0, 2])
    print("第 2 行 ->", arr[1])
    print("第 2 列 ->", arr[:, 1])
    print("子块 [0:2, 1:3] ->")
    print(arr[:2, 1:3])
    print("步长切片 [:, ::2] ->")
    print(arr[:, ::2])
    print("负索引 ->", arr[-1, -1])

    print("\n切片通常是视图（会影响原数组） ->")
    view = arr[:2, :2]
    view[:] = 0
    print(arr)


if __name__ == "__main__":
    main()
