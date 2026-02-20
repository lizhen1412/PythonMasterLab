#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 09：使用 einsum 进行矩阵运算。
Author: Lambert

题目：
使用 np.einsum 计算：
1. 向量点积
2. 矩阵乘法
3. 矩阵迹（对角元素之和）

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/02_Numpy/Exercises/09_einsum.py
"""

from __future__ import annotations

import numpy as np


def dot_product(v1: np.ndarray, v2: np.ndarray) -> float:
    """使用 einsum 计算点积"""
    return float(np.einsum("i,i->", v1, v2))


def matrix_multiply(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """使用 einsum 计算矩阵乘法"""
    return np.einsum("ij,jk->ik", A, B)


def matrix_trace(A: np.ndarray) -> float:
    """使用 einsum 计算矩阵迹"""
    return float(np.einsum("ii->", A))


def check(label: str, got: object, expected: object) -> None:
    ok = (got == expected) if isinstance(got, (int, float)) else np.allclose(got, expected)
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")
    if not ok:
        print(f"  got: {got}")
        print(f"  expected: {expected}")


def main() -> None:
    # 点积测试
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    check("dot_product", dot_product(v1, v2), 32)

    # 矩阵乘法测试
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    expected_mm = np.array([[19, 22], [43, 50]])
    check("matrix_multiply", matrix_multiply(A, B), expected_mm)

    # 矩阵迹测试
    check("matrix_trace", matrix_trace(A), 5)


if __name__ == "__main__":
    main()