#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：NaN/Inf 处理。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/09_nan_inf_handling.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    arr = np.array([1.0, np.nan, 2.0, np.inf, -np.inf])
    print("arr ->", arr)

    print("
isnan ->", np.isnan(arr))
    print("isfinite ->", np.isfinite(arr))

    arr2 = np.array([1.0, np.nan, 3.0])
    mean_value = np.nanmean(arr2)
    filled = np.where(np.isnan(arr2), mean_value, arr2)

    print("
原始 arr2 ->", arr2)
    print("nanmean ->", mean_value)
    print("填充后的 arr2 ->", filled)


if __name__ == "__main__":
    main()