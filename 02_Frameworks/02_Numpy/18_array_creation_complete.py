#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 18：数组创建完整版。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/18_array_creation_complete.py

知识点：
- linspace/logspace - 等差/等比序列
- eye/identity - 单位矩阵
- diag/diagflat - 对角矩阵
- fromfunction/fromiter - 从函数/迭代器创建
- empty/empty_like - 未初始化数组
- full/full_like - 填充值
- tri/tril/triu - 三角矩阵
- indices/meshgrid - 网格坐标
- arange - 优化使用
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    print("=" * 70)
    print("1. linspace - 等差序列（指定元素个数）")
    print("=" * 70)

    print("\n1.1 基础用法")
    print("-" * 70)
    arr = np.linspace(0, 10, 5)
    print(f"linspace(0, 10, 5) -> {arr}")

    print("\n1.2 不包含终点")
    print("-" * 70)
    arr = np.linspace(0, 10, 5, endpoint=False)
    print(f"linspace(0, 10, 5, endpoint=False) -> {arr}")

    print("\n1.3 返回步长")
    print("-" * 70)
    arr, step = np.linspace(0, 10, 5, retstep=True)
    print(f"linspace(0, 10, 5, retstep=True) ->")
    print(f"  数组: {arr}")
    print(f"  步长: {step}")

    print("\n1.4 多维数组")
    print("-" * 70)
    arr = np.linspace(0, 10, 20).reshape(4, 5)
    print(f"linspace(0, 10, 20).reshape(4, 5) ->")
    print(arr)

    print("\n" + "=" * 70)
    print("2. logspace - 等比序列（对数空间）")
    print("=" * 70)

    print("\n2.1 基础用法")
    print("-" * 70)
    arr = np.logspace(0, 3, 4)
    print(f"logspace(0, 3, 4) -> {arr}")
    print("(10^0, 10^1, 10^2, 10^3)")

    print("\n2.2 指定底数")
    print("-" * 70)
    arr = np.logspace(0, 3, 4, base=2)
    print(f"logspace(0, 3, 4, base=2) -> {arr}")
    print("(2^0, 2^1, 2^2, 2^3)")

    print("\n2.3 对数间隔")
    print("-" * 70)
    arr = np.logspace(0, 2, 10)
    print(f"logspace(0, 2, 10) ->")
    print(arr)

    print("\n" + "=" * 70)
    print("3. eye / identity - 单位矩阵")
    print("=" * 70)

    print("\n3.1 eye - 单位矩阵（推荐）")
    print("-" * 70)
    arr = np.eye(3)
    print(f"eye(3) ->")
    print(arr)

    print("\n3.2 非方阵单位矩阵")
    print("-" * 70)
    arr = np.eye(3, 4)
    print(f"eye(3, 4) ->")
    print(arr)

    print("\n3.3 指定对角线偏移")
    print("-" * 70)
    arr = np.eye(4, k=1)
    print(f"eye(4, k=1) -> (上移1位)")
    print(arr)

    arr = np.eye(4, k=-1)
    print(f"\neye(4, k=-1) -> (下移1位)")
    print(arr)

    print("\n3.4 identity - 只能创建方阵")
    print("-" * 70)
    arr = np.identity(3)
    print(f"identity(3) ->")
    print(arr)

    print("\n" + "=" * 70)
    print("4. diag / diagflat - 对角矩阵")
    print("=" * 70)

    print("\n4.1 diag - 提取/创建对角矩阵")
    print("-" * 70)
    # 从列表创建
    arr = np.diag([1, 2, 3])
    print(f"diag([1, 2, 3]) ->")
    print(arr)

    # 提取对角线
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    diag_values = np.diag(arr)
    print(f"\n原始矩阵:")
    print(arr)
    print(f"diag(arr) -> {diag_values}")

    print("\n4.2 diagflat - 展平为对角矩阵")
    print("-" * 70)
    arr = np.diagflat([1, 2, 3])
    print(f"diagflat([1, 2, 3]) ->")
    print(arr)

    # 展平二维数组
    arr = np.diagflat([[1, 2], [3, 4]])
    print(f"\ndiagflat([[1, 2], [3, 4]]) ->")
    print(arr)

    print("\n4.3 对角线偏移")
    print("-" * 70)
    arr = np.diag([1, 2, 3], k=1)
    print(f"diag([1, 2, 3], k=1) ->")
    print(arr)

    arr = np.diag([1, 2, 3], k=-1)
    print(f"\ndiag([1, 2, 3], k=-1) ->")
    print(arr)

    print("\n" + "=" * 70)
    print("5. fromfunction - 从函数创建数组")
    print("=" * 70)

    print("\n5.1 一维函数")
    print("-" * 70)
    arr = np.fromfunction(lambda i: i**2, (5,))
    print(f"fromfunction(lambda i: i**2, (5,)) -> {arr}")

    print("\n5.2 二维函数")
    print("-" * 70)
    arr = np.fromfunction(lambda i, j: i + j, (3, 3))
    print(f"fromfunction(lambda i, j: i + j, (3, 3)) ->")
    print(arr)

    print("\n5.3 复杂函数")
    print("-" * 70)
    arr = np.fromfunction(lambda i, j: (i - j)**2, (4, 4), dtype=int)
    print(f"fromfunction(lambda i, j: (i - j)**2, (4, 4)) ->")
    print(arr)

    print("\n" + "=" * 70)
    print("6. fromiter - 从迭代器创建数组")
    print("=" * 70)

    print("\n6.1 从列表迭代")
    print("-" * 70)
    iterable = (x**2 for x in range(5))
    arr = np.fromiter(iterable, dtype=int)
    print(f"fromiter((x**2 for x in range(5)), dtype=int) -> {arr}")

    print("\n6.2 从字符串")
    print("-" * 70)
    arr = np.fromiter("12345", dtype=int)
    print(f"fromiter('12345', dtype=int) -> {arr}")

    print("\n6.3 从文件对象")
    print("-" * 70)
    import io
    data = io.StringIO("1 2 3 4 5")
    arr = np.fromiter(data, dtype=int, count=5)
    print(f"从 StringIO 读取 -> {arr}")

    print("\n" + "=" * 70)
    print("7. empty / empty_like - 未初始化数组")
    print("=" * 70)

    print("\n7.1 empty - 创建未初始化数组")
    print("-" * 70)
    arr = np.empty((3, 3))
    print("empty((3, 3)) -> (值是随机的，未初始化)")
    print(arr)

    print("\n7.2 empty_like - 保持形状和类型")
    print("-" * 70)
    template = np.array([[1, 2, 3], [4, 5, 6]])
    arr = np.empty_like(template)
    print("empty_like(template) ->")
    print(arr)

    print("\n注意：empty/empty_like 的值是随机的，不应该被使用")
    print("它们只是预分配内存，性能优化用")

    print("\n" + "=" * 70)
    print("8. full / full_like - 填充指定值")
    print("=" * 70)

    print("\n8.1 full - 填充标量值")
    print("-" * 70)
    arr = np.full((3, 3), 7)
    print("full((3, 3), 7) ->")
    print(arr)

    print("\n8.2 full_like - 保持形状填充")
    print("-" * 70)
    template = np.array([[1, 2], [3, 4]])
    arr = np.full_like(template, 9)
    print("full_like(template, 9) ->")
    print(arr)

    print("\n8.3 填充不同类型")
    print("-" * 70)
    arr = np.full((2, 2), "hello", dtype="U5")
    print("full((2, 2), 'hello') ->")
    print(arr)

    print("\n" + "=" * 70)
    print("9. tri / tril / triu - 三角矩阵")
    print("=" * 70)

    print("\n9.1 tri - 下三角为1的矩阵")
    print("-" * 70)
    arr = np.tri(4)
    print("tri(4) ->")
    print(arr)

    print("\n9.2 tril - 下三角部分")
    print("-" * 70)
    arr = np.arange(16).reshape(4, 4)
    print("原始矩阵:")
    print(arr)

    lower = np.tril(arr)
    print("\ntril(arr) ->")
    print(lower)

    lower_k = np.tril(arr, k=1)
    print("\ntril(arr, k=1) -> (包含主对角线及其上方1条)")
    print(lower_k)

    print("\n9.3 triu - 上三角部分")
    print("-" * 70)
    upper = np.triu(arr)
    print("triu(arr) ->")
    print(upper)

    upper_k = np.triu(arr, k=1)
    print("\ntriu(arr, k=1) -> (不含主对角线)")
    print(upper_k)

    print("\n" + "=" * 70)
    print("10. indices / meshgrid - 网格坐标")
    print("=" * 70)

    print("\n10.1 indices - 网格索引")
    print("-" * 70)
    grid = np.indices((2, 3))
    print("indices((2, 3)) -> 返回两个数组")
    print("第一个数组 (行坐标):")
    print(grid[0])
    print("\n第二个数组 (列坐标):")
    print(grid[1])

    print("\n10.2 meshgrid - 网格矩阵")
    print("-" * 70)
    x = np.array([1, 2, 3])
    y = np.array([4, 5])
    xx, yy = np.meshgrid(x, y)
    print(f"x = {x}")
    print(f"y = {y}")
    print("\nmeshgrid(x, y):")
    print("xx ->")
    print(xx)
    print("\nyy ->")
    print(yy)

    print("\n10.3 索引='ij'（矩阵索引）")
    print("-" * 70)
    xx, yy = np.meshgrid(x, y, indexing="ij")
    print("meshgrid(x, y, indexing='ij'):")
    print("xx ->")
    print(xx)
    print("\nyy ->")
    print(yy)

    print("\n10.4 sparse=True（稀疏网格）")
    print("-" * 70)
    xx, yy = np.meshgrid(x, y, sparse=True)
    print("meshgrid(x, y, sparse=True):")
    print("xx.shape ->", xx.shape)
    print("yy.shape ->", yy.shape)

    print("\n10.5 mgrid / ogrid（多维网格）")
    print("-" * 70)
    print("mgrid（密集网格）:")
    xx, yy = np.mgrid[0:3, 0:4]
    print("mgrid[0:3, 0:4]:")
    print("xx ->")
    print(xx)
    print("yy ->")
    print(yy)

    print("\nogrid（稀疏网格）:")
    xx, yy = np.ogrid[0:3, 0:4]
    print("ogrid[0:3, 0:4]:")
    print("xx ->")
    print(xx)
    print("yy ->")
    print(yy)

    print("\n" + "=" * 70)
    print("11. copy - 深拷贝")
    print("=" * 70)

    print("\n11.1 copy() 创建独立副本")
    print("-" * 70)
    arr = np.array([1, 2, 3])
    arr_copy = arr.copy()
    arr_copy[0] = 999
    print(f"原始数组: {arr}")
    print(f"修改后的副本: {arr_copy}")
    print("(原始数组不受影响)")

    print("\n11.2 浅拷贝 vs 深拷贝")
    print("-" * 70)
    arr = np.array([[1, 2], [3, 4]])
    shallow = arr.view()  # 浅拷贝（视图）
    deep = arr.copy()  # 深拷贝

    shallow[0, 0] = 999
    print(f"浅拷贝修改后，原数组: {arr[0, 0]}")

    deep[0, 0] = 888
    print(f"深拷贝修改后，原数组: {arr[0, 0]} (不受影响)")

    print("\n" + "=" * 70)
    print("12. 常见创建模式对比")
    print("=" * 70)

    print("""
创建全零数组：
  np.zeros(5)           # 最直接
  np.zeros_like(arr)    # 保持形状
  np.full(5, 0)         # 通用方法

创建全一数组：
  np.ones(5)            # 最直接
  np.ones_like(arr)     # 保持形状
  np.full(5, 1)         # 通用方法

创建范围数组：
  np.arange(0, 10)      # 类似 Python range
  np.linspace(0, 10, 5) # 指定元素个数
  np.logspace(0, 2, 5)  # 对数间隔

创建对角矩阵：
  np.eye(3)             # 单位矩阵
  np.diag([1,2,3])      # 对角矩阵
  np.identity(3)        # 同 eye，只支持方阵
""")

    print("\n" + "=" * 70)
    print("13. 实际应用示例")
    print("=" * 70)

    # 示例 1: 创建测试数据
    print("\n示例 1: 创建回归测试数据")
    x = np.linspace(0, 10, 100)
    y = 2 * x + 3 + np.random.randn(100)
    print(f"x: {x.shape}, y: {y.shape}")

    # 示例 2: 创建坐标网格（用于热力图）
    print("\n示例 2: 创建坐标网格")
    x = np.linspace(-5, 5, 10)
    y = np.linspace(-5, 5, 10)
    xx, yy = np.meshgrid(x, y)
    zz = xx**2 + yy**2  # 圆形函数
    print(f"网格形状: {xx.shape}, 计算结果形状: {zz.shape}")

    # 示例 3: 创建单位矩阵（线性代数）
    print("\n示例 3: 创建单位矩阵")
    I = np.eye(3)
    print(f"单位矩阵 I (3x3):")
    print(I)

    # 示例 4: 从迭代器创建
    print("\n示例 4: 从生成器表达式创建")
    squares = np.fromiter((i**2 for i in range(10)), dtype=int)
    print(f"0-9 的平方: {squares}")

    # 示例 5: 创建三角形矩阵
    print("\n示例 5: 下三角矩阵（协方差矩阵）")
    cov = np.triu(np.ones((3, 3)))
    print(cov)


if __name__ == "__main__":
    main()