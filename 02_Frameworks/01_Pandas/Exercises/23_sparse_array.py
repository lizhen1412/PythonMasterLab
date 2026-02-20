#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 23：创建和使用稀疏数组。
Author: Lambert

题目：
创建一个包含大量零值的 Series，转换为稀疏数组并比较内存使用。

参考答案：
- 本文件函数实现即为参考答案；`main()` 带最小自测。

运行：
    python3 02_Frameworks/01_Pandas/Exercises/23_sparse_array.py
"""

from __future__ import annotations

import pandas as pd
import numpy as np


def create_sparse_series(size: int, sparsity: float = 0.95) -> tuple[pd.Series, pd.Series]:
    """创建普通 Series 和对应的稀疏 Series"""
    # 创建稀疏数据：大部分为0
    data = np.zeros(size)
    n_nonzero = int(size * (1 - sparsity))
    nonzero_indices = np.random.choice(size, n_nonzero, replace=False)
    data[nonzero_indices] = np.random.randn(n_nonzero)

    regular = pd.Series(data)
    sparse = regular.astype("Sparse[float64]")
    return regular, sparse


def main() -> None:
    regular, sparse = create_sparse_series(10000, 0.95)

    print(f"Regular Series memory: {regular.memory_usage(deep=True) / 1024:.2f} KB")
    print(f"Sparse Series memory: {sparse.memory_usage(deep=True) / 1024:.2f} KB")
    print(f"Memory saved: {(1 - sparse.memory_usage(deep=True) / regular.memory_usage(deep=True)) * 100:.1f}%")

    # 验证数据相同
    assert (regular == sparse).all(), "Data should be identical"
    print("[OK] sparse array creation and comparison")


if __name__ == "__main__":
    main()