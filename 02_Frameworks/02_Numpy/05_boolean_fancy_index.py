#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：布尔/花式索引与 where。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/05_boolean_fancy_index.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    arr = np.array([1, 3, 5, 2, 4])
    print("arr ->", arr)

    mask = arr % 2 == 0
    print("
偶数 mask ->", mask)
    print("偶数元素 ->", arr[mask])

    print("
花式索引 ->", arr[[0, 2, 4]])

    print("
where 条件替换 ->")
    print(np.where(arr > 3, arr, 0))


if __name__ == "__main__":
    main()