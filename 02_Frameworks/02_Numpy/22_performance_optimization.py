#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 22：Performance Optimization - 性能优化。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/22_performance_optimization.py

NumPy 提供了多种性能优化技术，包括 einsum、nditer、stride tricks 等。
掌握这些技术可以显著提升代码运行效率。

本节演示：
1. np.einsum - 爱因斯坦求和约定
2. np.nditer - 高效迭代器
3. 广播优化
4. 内存布局优化
5. 向量化 vs 循环
6. 性能对比
"""

from __future__ import annotations

import numpy as np
import time


def time_func(func, *args, **kwargs):
    """简单的计时函数"""
    start = time.time()
    result = func(*args, **kwargs)
    elapsed = time.time() - start
    return result, elapsed


def main() -> None:
    print("=" * 60)
    print("1. np.einsum - 爱因斯坦求和约定")
    print("=" * 60)

    print("\neinsum 提供了一种简洁的方式来表达各种数组运算")
    print("基本语法: 'ijk,->' 表示对指定维度进行求和")

    # 向量内积
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print(f"\n向量内积:")
    print(f"  a = {a}")
    print(f"  b = {b}")

    result_dot = np.dot(a, b)
    result_einsum = np.einsum('i,i->', a, b)
    print(f"  np.dot(a, b) = {result_dot}")
    print(f"  np.einsum('i,i->', a, b) = {result_einsum}")

    # 矩阵乘法
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print(f"\n矩阵乘法:")
    print(f"  A = {A.tolist()}")
    print(f"  B = {B.tolist()}")

    result_matmul = A @ B
    result_einsum = np.einsum('ij,jk->ik', A, B)
    print(f"  A @ B = {result_matmul.tolist()}")
    print(f"  einsum('ij,jk->ik', A, B) = {result_einsum.tolist()}")

    # 张量收缩（更复杂的运算）
    T1 = np.random.randn(10, 20, 30)
    T2 = np.random.randn(30, 40)

    print(f"\n张量收缩: T1(10,20,30) @ T2(30,40) -> (10,20,40)")

    result1 = np.einsum('ijk,kl->ijl', T1, T2)
    print(f"  结果形状: {result1.shape}")

    # 沿指定轴求和
    C = np.arange(24).reshape(2, 3, 4)
    print(f"\n沿轴求和:")
    print(f"  数组形状: {C.shape}")

    sum_axis0 = np.einsum('ijk->jk', C)  # 沿第0轴求和
    print(f"  沿轴0求和: {sum_axis0.shape}")

    # 对角线提取
    D = np.arange(9).reshape(3, 3)
    print(f"\n对角线操作:")
    print(f"  D =")
    print(D)

    diag = np.einsum('ii->i', D)
    print(f"  对角线: {diag}")

    # 外积
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    outer = np.einsum('i,j->ij', x, y)
    print(f"\n外积:")
    print(f"  x = {x}")
    print(f"  y = {y}")
    print(f"  外积:")
    print(outer)

    print("\n" + "=" * 60)
    print("2. einsum 性能对比")
    print("=" * 60)

    # 创建较大的数组进行性能测试
    n = 1000
    A = np.random.randn(n, n)
    B = np.random.randn(n, n)
    v = np.random.randn(n)

    print(f"\n数组大小: {n}x{n}")

    # 矩阵乘法
    _, time_matmul = time_func(lambda: A @ B)
    _, time_einsum_matmul = time_func(lambda: np.einsum('ij,jk->ik', A, B))

    print(f"\n矩阵乘法:")
    print(f"  @ 操作符: {time_matmul*1000:.2f} ms")
    print(f"  einsum: {time_einsum_matmul*1000:.2f} ms")
    print(f"  速度比: {time_einsum_matmul/time_matmul:.2f}x")

    # 矩阵-向量乘法
    _, time_dot = time_func(lambda: A @ v)
    _, time_einsum_dot = time_func(lambda: np.einsum('ij,j->i', A, v))

    print(f"\n矩阵-向量乘法:")
    print(f"  @ 操作符: {time_dot*1000:.2f} ms")
    print(f"  einsum: {time_einsum_dot*1000:.2f} ms")
    print(f"  速度比: {time_einsum_dot/time_dot:.2f}x")

    print("\n" + "=" * 60)
    print("3. np.nditer - 高效迭代器")
    print("=" * 60)

    print("\nnditer 提供了高效的数组迭代方式")

    # 基本使用
    a = np.arange(6).reshape(2, 3)
    print(f"\n原数组:")
    print(a)

    print(f"\n使用 nditer 遍历:")
    for x in np.nditer(a):
        print(f"  {x}", end="")
    print()

    # 同时遍历多个数组
    b = np.arange(6, 12).reshape(2, 3)
    print(f"\n两个数组相加（使用 nditer）:")
    print(f"  a =")
    print(a)
    print(f"  b =")
    print(b)

    result = np.empty_like(a)
    for x, y, z in np.nditer([a, b, result], ['readwrite']):
        z[...] = x + y
    print(f"  a + b =")
    print(result)

    # 使用 C 顺序和 F 顺序
    print(f"\n不同的迭代顺序:")
    a = np.arange(6).reshape(2, 3)

    print(f"  C 顺序（行优先）:")
    for x in np.nditer(a, order='C'):
        print(f"    {x}", end="")
    print()

    print(f"  F 顺序（列优先）:")
    for x in np.nditer(a, order='F'):
        print(f"    {x}", end="")
    print()

    # 使用 flags 控制行为
    print(f"\n使用外部循环（提升性能）:")
    a = np.arange(12).reshape(3, 4)
    for x in np.nditer(a, flags=['external_loop']):
        print(f"  {x}")

    print("\n" + "=" * 60)
    print("4. 广播优化")
    print("=" * 60)

    print("\n利用广播避免显式循环")

    # 不好的做法
    a = np.arange(1000000)
    b = np.zeros(1000000)

    print("\n不使用广播（循环）:")
    _, time_loop = time_func(lambda: [b[i] = a[i] * 2 for i in range(len(a))])
    print(f"  时间: {time_loop*1000:.2f} ms")

    print("\n使用广播:")
    _, time_broadcast = time_func(lambda: a * 2)
    print(f"  时间: {time_broadcast*1000:.2f} ms")
    print(f"  加速: {time_loop/time_broadcast:.1f}x")

    # 二维广播
    A = np.random.randn(1000, 100)
    v = np.random.randn(100)

    # 每行加向量
    print("\n二维广播 (1000x100 + 100):")
    _, time_2d_broadcast = time_func(lambda: A + v)
    print(f"  时间: {time_2d_broadcast*1000:.2f} ms")

    print("\n" + "=" * 60)
    print("5. 内存布局优化")
    print("=" * 60)

    print("\nC 连续 vs F 连续")

    # C 连续（行优先）
    c_array = np.array([[1, 2, 3], [4, 5, 6]], order='C')
    print(f"\nC 连续数组:")
    print(c_array)
    print(f"  flags['C_CONTIGUOUS']: {c_array.flags['C_CONTIGUOUS']}")
    print(f"  strides: {c_array.strides}")

    # F 连续（列优先）
    f_array = np.array([[1, 2, 3], [4, 5, 6]], order='F')
    print(f"\nF 连续数组:")
    print(f_array)
    print(f"  flags['F_CONTIGUOUS']: {f_array.flags['F_CONTIGUOUS']}")
    print(f"  strides: {f_array.strides}")

    # 行访问性能
    large_c = np.ones((10000, 1000), order='C')
    large_f = np.ones((10000, 1000), order='F')

    # 按行求和
    _, time_c_row = time_func(lambda: large_c.sum(axis=1))
    _, time_f_row = time_func(lambda: large_f.sum(axis=1))

    print(f"\n按行求和性能:")
    print(f"  C 连续: {time_c_row*1000:.2f} ms")
    print(f"  F 连续: {time_f_row*1000:.2f} ms")
    print(f"  C 更快: {time_f_row/time_c_row:.2f}x")

    # 按列求和
    _, time_c_col = time_func(lambda: large_c.sum(axis=0))
    _, time_f_col = time_func(lambda: large_f.sum(axis=0))

    print(f"\n按列求和性能:")
    print(f"  C 连续: {time_c_col*1000:.2f} ms")
    print(f"  F 连续: {time_f_col*1000:.2f} ms")
    print(f"  F 更快: {time_c_col/time_f_col:.2f}x")

    print("\n建议: 根据主要访问模式选择内存布局")

    print("\n" + "=" * 60)
    print("6. 视图 vs 副本")
    print("=" * 60)

    print("\n使用视图避免不必要的复制")

    large = np.arange(10000000)

    # 创建副本
    _, time_copy = time_func(lambda: large.copy())
    print(f"\n复制数组: {time_copy*1000:.2f} ms")

    # 创建视图（无复制）
    _, time_view = time_func(lambda: large[:])
    print(f"创建视图: {time_view*1000:.4f} ms")
    print(f"快 {time_copy/time_view:.0f}x")

    print("\n" + "=" * 60)
    print("7. 预分配内存")
    print("=" * 60)

    print("\n预分配 vs 动态增长")

    n = 100000

    # 不好的做法：动态增长
    def grow_dynamic():
        arr = []
        for i in range(n):
            arr.append(i * 2)
        return np.array(arr)

    # 好的做法：预分配
    def grow_preallocated():
        arr = np.empty(n)
        for i in range(n):
            arr[i] = i * 2
        return arr

    # 更好的做法：完全向量化
    def grow_vectorized():
        return np.arange(n) * 2

    _, time_dynamic = time_func(grow_dynamic)
    _, time_prealloc = time_func(grow_preallocated)
    _, time_vectorized = time_func(grow_vectorized)

    print(f"\n创建 {n} 元素数组:")
    print(f"  动态增长: {time_dynamic*1000:.2f} ms")
    print(f"  预分配: {time_prealloc*1000:.2f} ms")
    print(f"  向量化: {time_vectorized*1000:.4f} ms")

    print("\n" + "=" * 60)
    print("8. 使用 NumPy 内置函数")
    print("=" * 60)

    print("\nNumPy 内置函数 vs Python 内置函数")

    arr = np.random.randn(1000000)

    # 求和
    _, time_np_sum = time_func(lambda: arr.sum())
    _, time_py_sum = time_func(lambda: sum(arr))
    print(f"\n求和:")
    print(f"  np.sum: {time_np_sum*1000:.2f} ms")
    print(f"  sum(): {time_py_sum*1000:.2f} ms")

    # 平方
    _, time_np_square = time_func(lambda: arr ** 2)
    _, time_py_square = time_func(lambda: [x**2 for x in arr])
    print(f"\n平方:")
    print(f"  arr ** 2: {time_np_square*1000:.2f} ms")
    print(f"  列表推导: {time_py_square*1000:.2f} ms")

    print("\n" + "=" * 60)
    print("9. einsum 常用模式")
    print("=" * 60)

    print("\neinsum 符号速查:")
    patterns = {
        "向量内积": "i,i->",
        "向量外积": "i,j->ij",
        "矩阵乘法": "ij,jk->ik",
        "矩阵-向量": "ij,j->i",
        "转置": "ij->ji",
        "对角线": "ii->i",
        "迹": "ii->",
        "沿轴求和": "ijk->ij",
        "批量矩阵乘法": "ijk,ikl->ijl",
        "点积（多个数组）": "ij,ij->",
    }

    for name, pattern in patterns.items():
        print(f"  {pattern:20s}  # {name}")

    print("\n" + "=" * 60)
    print("10. 性能优化建议")
    print("=" * 60)

    print("\n性能优化建议:")
    print("  1. 优先使用向量化操作，避免循环")
    print("  2. 使用 einsum 表达复杂的多维数组运算")
    print("  3. 根据访问模式选择合适的内存布局（C/F）")
    print("  4. 使用视图而不是副本，避免不必要的复制")
    print("  5. 预分配数组，避免动态增长")
    print("  6. 使用 NumPy 内置函数而非 Python 函数")
    print("  7. 对于超大数组，考虑使用 np.memmap")
    print("  8. 对于特别复杂的操作，考虑使用 Numba 或 Cython")

    print("\n工具函数:")
    print("  np.ascontiguousarray() - 确保 C 连续")
    print("  np.asfortranarray() - 确保 F 连续")
    print("  np.squeeze() - 移除单维度")
    print("  np.ravel() - 展平数组（可能返回视图）")
    print("  np.flatten() - 展平数组（返回副本）")

    print("\n" + "=" * 60)
    print("11. 实际案例")
    print("=" * 60)

    print("\n案例: 计算协方差矩阵")
    print("-" * 40)

    # 生成数据
    n_features = 100
    n_samples = 1000
    X = np.random.randn(n_samples, n_features)

    print(f"数据形状: {X.shape}")

    # 方法1: 使用 np.cov
    _, time_cov = time_func(lambda: np.cov(X, rowvar=False))
    print(f"\n方法1 - np.cov: {time_cov*1000:.2f} ms")

    # 方法2: 手动计算（向量化）
    def manual_cov(X):
        X_centered = X - X.mean(axis=0)
        return (X_centered.T @ X_centered) / (X.shape[0] - 1)

    _, time_manual = time_func(manual_cov)
    print(f"方法2 - 向量化手动计算: {time_manual*1000:.2f} ms")
    print(f"  加速: {time_cov/time_manual:.2f}x")

    # 方法3: 使用 einsum
    def einsum_cov(X):
        X_centered = X - X.mean(axis=0)
        return np.einsum('ij,ik->jk', X_centered, X_centered) / (X.shape[0] - 1)

    _, time_einsum_cov = time_func(einsum_cov)
    print(f"方法3 - einsum: {time_einsum_cov*1000:.2f} ms")
    print(f"  加速: {time_cov/time_einsum_cov:.2f}x")


if __name__ == "__main__":
    main()