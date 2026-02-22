#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 15：视图与拷贝。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/15_views_copies.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    arr = np.arange(6)
    view = arr[1:4]
    copy = arr[1:4].copy()

    print("arr ->", arr)
    print("view ->", view)
    print("copy ->", copy)

    view[:] = 100
    print("\n修改 view 后 arr ->", arr)

    copy[:] = -1
    print("修改 copy 后 arr ->", arr)

    print("\nshares_memory(view, arr) ->", np.shares_memory(view, arr))
    print("shares_memory(copy, arr) ->", np.shares_memory(copy, arr))


if __name__ == "__main__":
    main()
