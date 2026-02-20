#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 16：ufunc 与条件处理（where/clip/sqrt）。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/16_vectorize_ufunc.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    arr = np.array([1, 4, 9, 16])
    print("arr ->", arr)

    print("
sqrt ->", np.sqrt(arr))

    values = np.array([-2, 0, 3, 7])
    print("
clip(-1, 5) ->", np.clip(values, -1, 5))

    print("
where(values > 0, values, 0) ->")
    print(np.where(values > 0, values, 0))

    print("
add.reduce ->", np.add.reduce(values))


if __name__ == "__main__":
    main()