#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：排序/去重/searchsorted。

运行：
    python3 02_Frameworks/02_Numpy/10_sort_unique.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    arr = np.array([3, 1, 2, 1, 5])
    print("arr ->", arr)

    print("
sort ->", np.sort(arr))
    print("argsort ->", np.argsort(arr))
    print("unique ->", np.unique(arr))

    sorted_arr = np.array([1, 3, 5, 7])
    print("
searchsorted(4) ->", np.searchsorted(sorted_arr, 4))
    print("searchsorted([1,6]) ->", np.searchsorted(sorted_arr, [1, 6]))


if __name__ == "__main__":
    main()
