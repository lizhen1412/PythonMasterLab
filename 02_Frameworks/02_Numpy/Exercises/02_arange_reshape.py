#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：arange + reshape。

题目：
生成 1 到 12 的数组，并 reshape 为 3x4。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/02_Numpy/Exercises/02_arange_reshape.py
"""

from __future__ import annotations

import numpy as np


def make_matrix() -> np.ndarray:
    return np.arange(1, 13).reshape(3, 4)


def check(label: str, got: np.ndarray, expected: np.ndarray) -> None:
    ok = np.array_equal(got, expected)
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")
    if not ok:
        print("got ->")
        print(got)
        print("expected ->")
        print(expected)


def main() -> None:
    result = make_matrix()
    expected = np.array(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
        ]
    )
    check("arange_reshape", result, expected)


if __name__ == "__main__":
    main()
