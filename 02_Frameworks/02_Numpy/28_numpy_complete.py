#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 28：NumPy Complete - 补充剩余功能。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/28_numpy_complete.py

本节补充 NumPy 中尚未覆盖的重要功能，
确保达到 100% 的方法覆盖。

本节演示：
1. einsum - 爱因斯坦求和（详细）
2. pad - 数组填充
3. np.char - 字符串操作
4. corrcoef/cov - 相关系数/协方差
5. interp - 插值
6. trim_zeros - 移除前导/后导零
7. unique_all - 完整唯一值功能
8. nanpercentile/nanmedian - NaN 统计
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    print("=" * 60)
    print("1. einsum - 爱因斯坦求和（详细）")
    print("=" * 60)

    print("\neinsum 提供了一种简洁的方式来表达各种数组运算")

    # 向量内积
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print(f"\n向量内积:")
    print(f"  a = {a}")
    print(f"  b = {b}")
    print(f"  np.einsum('i,i->', a, b) = {np.einsum('i,i->', a, b)}")
    print(f"  np.dot(a, b) = {np.dot(a, b)}")

    # 矩阵乘法
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print(f"\n矩阵乘法:")
    print(f"  A = {A.tolist()}")
    print(f"  B = {B.tolist()}")
    print(f"  np.einsum('ij,jk->ik', A, B):")
    result = np.einsum('ij,jk->ik', A, B)
    print(f"    {result}")
    print(f"  A @ B = {(A @ B).tolist()}")

    # 对角线
    print(f"\n对角线:")
    print(f"  np.einsum('ii->', A) = {np.einsum('ii->', A)}")
    print(f"  np.trace(A) = {np.trace(A)}")

    # 外积
    print(f"\n外积:")
    print(f"  np.einsum('i,j->ij', a, b):")
    print(f"    {np.einsum('i,j->ij', a, b)}")

    # 转置
    print(f"\n转置:")
    print(f"  np.einsum('ij->ji', A):")
    print(f"    {np.einsum('ij->ji', A)}")

    # Batch 矩阵乘法
    print(f"\n批量矩阵乘法:")
    A_batch = np.random.randn(10, 3, 4)
    B_batch = np.random.randn(10, 4, 5)
    result = np.einsum('bij,bjk->bik', A_batch, B_batch)
    print(f"  A_batch: {A_batch.shape}")
    print(f"  B_batch: {B_batch.shape}")
    print(f"  结果: {result.shape}")

    # 张量收缩
    print(f"\n张量收缩:")
    T = np.random.randn(3, 4, 5)
    print(f"  T: {T.shape}")
    print(f"  沿第0维求和: {np.einsum('ijk->jk', T).shape}")
    print(f"  沿第1维求和: {np.einsum('ijk->ik', T).shape}")
    print(f"  沿第2维求和: {np.einsum('ijk->ij', T).shape}")

    print("\n" + "=" * 60)
    print("2. pad - 数组填充")
    print("=" * 60)

    print("\npad 用于在数组边缘填充值")

    arr = np.array([1, 2, 3, 4, 5])

    print(f"\n原数组: {arr}")

    # constant 填充
    print(f"\npad(arr, 2, mode='constant'):")
    print(f"  {np.pad(arr, 2, mode='constant')}")

    print(f"\npad(arr, 2, mode='constant', constant_values=-1):")
    print(f"  {np.pad(arr, 2, mode='constant', constant_values=-1)}")

    # edge 填充
    print(f"\npad(arr, 2, mode='edge'):")
    print(f"  {np.pad(arr, 2, mode='edge')}")

    # symmetric 填充
    print(f"\npad(arr, 2, mode='symmetric'):")
    print(f"  {np.pad(arr, 2, mode='symmetric')}")

    # reflect 填充
    print(f"\npad(arr, 2, mode='reflect'):")
    print(f"  {np.pad(arr, 2, mode='reflect')}")

    # 不同宽度的填充
    print(f"\npad(arr, ((2, 3), (1, 1)), mode='constant'):")
    print(f"  顶部2，底部3，左侧1，右侧1")
    print(f"  {np.pad(arr, ((2, 3), (1, 1)), mode='constant')}")

    # 多维数组
    arr_2d = np.array([[1, 2], [3, 4]])
    print(f"\n二维数组:")
    print(arr_2d)
    print(f"\npad(arr_2d, 1, mode='constant'):")
    print(np.pad(arr_2d, 1, mode='constant'))

    print("\n" + "=" * 60)
    print("3. np.char - 字符串操作")
    print("=" * 60)

    print("\nnp.char 模块提供对字符串数组的向量化操作")

    # 创建字符串数组
    names = np.array(['alice', 'bob', 'charlie'])

    print(f"\n原始字符串:")
    print(names)

    # 大小写转换
    print(f"\nnp.char.upper(): {np.char.upper(names)}")
    print(f"np.char.lower(): {np.char.lower(names)}")
    print(f"np.char.capitalize(): {np.char.capitalize(names)}")
    print(f"np.char.title(): {np.char.title(names)}")

    # 字符串连接
    print(f"\nnp.char.add(['a', 'b'], ['c', 'd']):")
    print(f"  {np.char.add(['a', 'b'], ['c', 'd'])}")

    # 字符串重复
    print(f"\nnp.char.multiply(['a', 'b'], [3, 2]):")
    print(f"  {np.char.multiply(['a', 'b'], [3, 2])}")

    # 字符串比较
    a = np.array(['abc', 'def'])
    b = np.array(['abc', 'deg'])
    print(f"\nnp.char.equal(a, b): {np.char.equal(a, b)}")
    print(f"np.char.compare(a, b): {np.char.compare(a, b)}")

    # 查找
    print(f"\nnp.char.find(['abc', 'def'], 'b'): {np.char.find(['abc', 'def'], 'b')}")
    print(f"np.char.startswith(['abc', 'def'], 'a'): {np.char.startswith(['abc', 'def'], 'a')}")

    # 去除空白
    print(f"\nnp.char.strip(['  a  ', '  b  ']): {np.char.strip(['  a  ', '  b  '])}")
    print(f"np.char.lstrip(['  a  ', '  b  ']): {np.char.lstrip(['  a  ', '  b  '])}")
    print(f"np.char.rstrip(['  a  ', '  b  ']): {np.char.rstrip(['  a  ', '  b  '])}")

    # 分割和连接
    print(f"\nnp.char.split(['a,b', 'c,d'], ','): {np.char.split(['a,b', 'c,d'], ',')}")
    print(f"np.char.join([':', '-'], [['a', 'b'], ['c', 'd']]):")
    print(f"  {np.char.join([':', '-'], [['a', 'b'], ['c', 'd']])}")

    # 替换
    print(f"\nnp.char.replace(['abc', 'def'], 'a', 'x'): {np.char.replace(['abc', 'def'], 'a', 'x')}")

    print("\n" + "=" * 60)
    print("4. corrcoef/cov - 相关系数/协方差")
    print("=" * 60)

    # 两个变量
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])

    print(f"\nx = {x}")
    print(f"y = {y}")

    # 相关系数
    corr_matrix = np.corrcoef(x, y)
    print(f"\nnp.corrcoef([x, y]):")
    print(corr_matrix)
    print(f"  相关系数: {corr_matrix[0, 1]:.4f}")

    # 协方差
    cov_matrix = np.cov(x, y)
    print(f"\nnp.cov([x, y]):")
    print(cov_matrix)

    # 多变量
    data = np.array([
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9],
        [4, 8, 12]
    ])

    print(f"\n多变量数据:")
    print(data)

    print(f"\nnp.corrcoef(data) - 每行是一个变量:")
    print(np.corrcoef(data))

    print(f"\nnp.cov(data):")
    print(np.cov(data))

    # rowvar 参数
    print(f"\nnp.corrcoef(data, rowvar=False):")
    print("  每列是一个变量:")
    print(np.corrcoef(data, rowvar=False))

    print("\n" + "=" * 60)
    print("5. interp - 插值")
    print("=" * 60)

    # 已知数据点
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([0, 2, 1, 3, 5])

    print(f"\n已知数据点:")
    print(f"  x = {x}")
    print(f"  y = {y}")

    # 在新点插值
    x_new = np.array([0.5, 1.5, 2.5, 3.5])
    y_new = np.interp(x_new, x, y)

    print(f"\n在 x_new = {x_new} 处插值:")
    print(f"  y_new = {y_new}")

    # 外推
    print(f"\n在范围外插值:")
    x_extrap = np.array([-1, 5])
    y_extrap = np.interp(x_extrap, x, y)
    print(f"  x = {x_extrap}")
    print(f"  y = {y_extrap}")

    # 多维插值
    points = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    values = np.array([0, 1, 2, 3])
    xi = np.array([[0.5, 0.5], [0.2, 0.8]])

    print(f"\n二维插值:")
    print(f"  网格点: {points.tolist()}")
    print(f"  值: {values}")
    print(f"  在 {xi} 处插值:")
    print(f"  {np.interp(xi, points, values)}")

    print("\n" + "=" * 60)
    print("6. trim_zeros - 移除零")
    print("=" * 60)

    arr = np.array([0, 0, 1, 2, 0, 0, 3, 0, 0])
    print(f"\n原数组: {arr}")

    # 移除前导和后导零
    trimmed = np.trim_zeros(arr)
    print(f"\nnp.trim_zeros(arr): {trimmed}")

    # 只移除前导零
    trim_leading = np.trim_zeros(arr, trim='f')
    print(f"\nnp.trim_zeros(arr, trim='f'): {trim_leading}")

    # 只移除后导零
    trim_trailing = np.trim_zeros(arr, trim='b')
    print(f"\nnp.trim_zeros(arr, trim='b'): {trim_trailing}")

    print("\n" + "=" * 60)
    print("7. unique_all - 完整唯一值功能")
    print("=" * 60)

    arr = np.array([1, 2, 3, 2, 4, 3, 5])

    print(f"\n原数组: {arr}")

    # unique
    print(f"\nnp.unique(arr): {np.unique(arr)}")

    # return_counts
    values, counts = np.unique(arr, return_counts=True)
    print(f"\nnp.unique(arr, return_counts=True):")
    print(f"  值: {values}")
    print(f"  计数: {counts}")

    # return_index
    values, indices = np.unique(arr, return_index=True)
    print(f"\nnp.unique(arr, return_index=True):")
    print(f"  值: {values}")
    print(f"  首次出现索引: {indices}")

    # return_inverse
    values, inverse = np.unique(arr, return_inverse=True)
    print(f"\nnp.unique(arr, return_inverse=True):")
    print(f"  唯一值: {values}")
    print(f"  反向索引: {inverse}")
    print(f"  重建: {values[inverse]}")

    # axis 参数
    arr_2d = np.array([[1, 2, 3], [2, 1, 3], [3, 2, 1]])
    print(f"\n二维数组:")
    print(arr_2d)

    print(f"\nnp.unique(arr_2d, axis=0):")
    print(f"  {np.unique(arr_2d, axis=0)}")

    print(f"\nnp.unique(arr_2d, axis=1):")
    print(f"  {np.unique(arr_2d, axis=1)}")

    print("\n" + "=" * 60)
    print("8. nanpercentile/nanmedian - NaN 统计")
    print("=" * 60)

    arr = np.array([1, 2, np.nan, 4, 5, np.nan, 6])

    print(f"\n含 NaN 的数组: {arr}")

    # nanmedian
    median = np.nanmedian(arr)
    print(f"\nnp.nanmedian(arr): {median}")

    # nanpercentile
    p25 = np.nanpercentile(arr, 25)
    p50 = np.nanpercentile(arr, 50)
    p75 = np.nanpercentile(arr, 75)

    print(f"\nnp.nanpercentile(arr, [25, 50, 75]):")
    print(f"  25%: {p25}")
    print(f"  50%: {p50}")
    print(f"  75%: {p75}")

    # 多维数组
    arr_2d = np.array([[1, np.nan, 3], [4, 5, np.nan]])
    print(f"\n二维数组:")
    print(arr_2d)

    print(f"\nnp.nanmedian(arr_2d, axis=0): {np.nanmedian(arr_2d, axis=0)}")
    print(f"np.nanmedian(arr_2d, axis=1): {np.nanmedian(arr_2d, axis=1)}")

    # nanmean, nanstd, nanvar
    print(f"\nnp.nanmean(arr): {np.nanmean(arr):.2f}")
    print(f"np.nanstd(arr): {np.nanstd(arr):.2f}")
    print(f"np.nanvar(arr): {np.nanvar(arr):.2f}")

    print("\n" + "=" * 60)
    print("9. 其他有用函数")
    print("=" * 60)

    # np.around
    arr = np.array([1.234, 2.567, 3.891])
    print(f"\nnp.around:")
    print(f"  原值: {arr}")
    print(f"  保留1位小数: {np.around(arr, 1)}")
    print(f"  保留0位小数: {np.around(arr, 0)}")

    # np.isclose
    a = np.array([1.0, 1.0000001, 2.0])
    b = np.array([1.0, 1.0, 2.0])
    print(f"\nnp.isclose(a, b): {np.isclose(a, b)}")
    print(f"np.isclose(a, b, atol=0.001): {np.isclose(a, b, atol=0.001)}")

    # np.allclose
    print(f"\nnp.allclose(a, b): {np.allclose(a, b)}")

    # np.ptp (peak-to-peak)
    arr = np.array([1, 5, 3, 9, 2])
    print(f"\narr: {arr}")
    print(f"np.ptp(arr) = {np.ptp(arr)}  # 最大-最小")

    # np.clip
    arr = np.array([-5, -1, 0, 1, 5])
    print(f"\nnp.clip(arr, -2, 2): {np.clip(arr, -2, 2)}")

    # np.abs
    arr = np.array([-1, -2, 3, -4])
    print(f"\nnp.abs(arr): {np.abs(arr)}")

    # np.sign
    arr = np.array([-5, -1, 0, 1, 5])
    print(f"\nnp.sign(arr): {np.sign(arr)}")
    print(f"  负数->-1, 零->0, 正数->1")

    print("\n" + "=" * 60)
    print("10. 实际应用")
    print("=" * 60)

    print("\n案例1: 使用 einsum 进行复杂计算")
    print("-" * 40)

    # 图像处理示例
    image = np.random.randn(100, 100, 3)
    # 计算 RGB 通道加权和
    weights = np.array([0.299, 0.587, 0.114])
    grayscale = np.einsum('ijk,k->ij', image, weights)
    print(f"  图像: {image.shape}")
    print(f"  灰度图: {grayscale.shape}")

    print("\n案例2: 使用 pad 进行信号处理")
    print("-" * 40)

    signal = np.array([1, 2, 3, 4, 5])
    print(f"  原信号: {signal}")
    padded = np.pad(signal, 2, mode='edge')
    print(f"  填充后: {padded}")

    print("\n案例3: 使用 interp 进行数据平滑")
    print("-" * 40)

    # 采样点
    x_sample = np.linspace(0, 10, 10)
    y_sample = np.sin(x_sample) + np.random.randn(10) * 0.1

    # 高分辨率
    x_dense = np.linspace(0, 10, 50)
    y_interp = np.interp(x_dense, x_sample, y_sample)

    print(f"  采样点: {len(x_sample)}")
    print(f"  插值点: {len(x_dense)}")

    print("\n案例4: 使用 np.char 处理文本数据")
    print("-" * 40)

    names = np.array(['alice@example.com', 'bob@test.com', 'charlie@demo.com'])
    print(f"  原始: {names}")

    # 提取域名
    domains = np.char.split(names, '@')
    print(f"  域名: {np.char.split(names, '@')[:, 1]}")

    print("\n" + "=" * 60)
    print("11. 完整速查")
    print("=" * 60)

    print("\n高级运算:")
    print("  np.einsum('ij,jk->ik', A, B)        # 爱因斯坦求和")
    print("  np.tensordot(A, B, axes=2)        # 张量点积")
    print("  np.kron(A, B)                     # Kronecker 积")

    print("\n填充:")
    print("  np.pad(arr, pad_width, mode='constant')")

    print("\n字符串:")
    print("  np.char.upper(str_arr)")
    print("  np.char.lower(str_arr)")
    print("  np.char.strip(str_arr)")
    print("  np.char.split(str_arr, sep)")
    print("  np.char.join(sep, arr)")

    print("\n统计:")
    print("  np.corrcoef(x)                    # 相关系数")
    print("  np.cov(x)                         # 协方差")
    print("  np.nanmedian(arr)                 # 忽略 NaN 的中位数")
    print("  np.nanpercentile(arr, q)           # 忽略 NaN 的分位数")

    print("\n插值:")
    print("  np.interp(x_new, x, y)             # 线性插值")

    print("\n零处理:")
    print("  np.trim_zeros(arr)                  # 移除前导/后导零")

    print("\n唯一值:")
    print("  np.unique(arr, return_counts=True) # 唯一值和计数")

    print("\n比较:")
    print("  np.isclose(a, b)                    # 浮点数比较")
    print("  np.allclose(a, b)                   # 数组比较")


if __name__ == "__main__":
    main()