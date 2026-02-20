#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 27：Advanced Indexing - 高级索引工具。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/27_advanced_indexing.py

NumPy 提供了一些高级索引辅助函数，使创建索引数组更方便。
这些函数在构建网格、多维索引和条件选择时非常有用。

本节演示：
1. ix_ - 构建开放网格
2. r_ / c_ - 沿轴连接数组
3. mgrid / ogrid - 网格生成
4. select - 条件选择
5. choose - 选择函数
6. where 条件索引
7. 实际应用案例
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    print("=" * 60)
    print("1. ix_ - 构建开放网格")
    print("=" * 60)

    print("\nix_ 用于将一维数组转换为可广播的开放网格")

    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6, 7])

    print(f"\nx = {x}")
    print(f"y = {y}")

    # 使用 ix_ 创建可广播的索引
    ixgrid = np.ix_(x, y)

    print(f"\nnp.ix_(x, y) 结果:")
    print(f"  ixgrid[0] (x扩展):\n{ixgrid[0]}")
    print(f"  ixgrid[1] (y扩展):\n{ixgrid[1]}")

    # 使用 ix_ 进行索引
    arr = np.arange(20).reshape(4, 5)
    print(f"\n原始数组:")
    print(arr)

    # 选择特定行和列
    selected = arr[np.ix_([0, 2], [1, 3])]
    print(f"\n选择行 [0,2] 和列 [1,3]:")
    print(selected)

    print("\n" + "=" * 60)
    print("2. r_ - 沿行连接数组")
    print("=" * 60)

    print("\nr_ 将数组沿行（第一个轴）连接")

    print("\n连接标量:")
    print(f"np.r_[1, 2, 3] = {np.r_[1, 2, 3]}")

    print("\n连接数组:")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(f"np.r_[a, b] = {np.r_[a, b]}")

    print("\n使用切片对象:")
    print(f"np.r_[1:5, 10:15] = {np.r_[1:5, 10:15]}")

    print("\n使用 step:")
    print(f"np.r_[1:10:2] = {np.r_[1:10:2]}")

    print("\n多维数组:")
    c = np.array([[1], [2]])
    d = np.array([[3], [4]])
    print(f"c = {c.ravel()}")
    print(f"d = {d.ravel()}")
    print(f"np.r_[c, d] = {np.r_[c, d]}")

    print("\n使用 np.r_ 创建范围:")
    print(f"np.r_[0:1:5j] = {np.r_[0:1:5j]}  # 5个等间距点")

    print("\n" + "=" * 60)
    print("3. c_ - 沿列连接数组")
    print("=" * 60)

    print("\nc_ 将数组沿列（第二个轴）连接")

    print("\n连接一维数组（转为列向量）:")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"np.c_[a, b] =")
    print(np.c_[a, b])

    print("\n连接二维数组:")
    c = np.array([[1, 2], [3, 4]])
    d = np.array([[5, 6], [7, 8]])
    print(f"c =")
    print(c)
    print(f"d =")
    print(d)
    print(f"np.c_[c, d] =")
    print(np.c_[c, d])

    print("\n创建列范围:")
    print(f"np.c_[1:5] =")
    print(np.c_[1:5])

    print("\n" + "=" * 60)
    print("4. mgrid - 密集网格")
    print("=" * 60)

    print("\nmgrid 创建密集的多维网格")

    # 一维
    print(f"\nnp.mgrid[0:5, 0:3]:")
    grid = np.mgrid[0:5, 0:3]
    print(f"  shape: {grid.shape}")
    print(f"  第一个维度 (x):")
    print(grid[0])
    print(f"  第二个维度 (y):")
    print(grid[1])

    # 使用复数步长
    print(f"\nnp.mgrid[0:1:5j, 0:1:3j]:")
    grid_fine = np.mgrid[0:1:5j, 0:1:3j]
    print(f"  x 轴 (0到1, 5个点): {grid_fine[0][0, :]}")
    print(f"  y 轴 (0到1, 3个点): {grid_fine[1][:, 0]}")

    print("\n应用: 评估函数 z = x² + y²")
    x, y = np.mgrid[-3:3:10j, -3:3:10j]
    z = x**2 + y**2
    print(f"  在点 (2, 1): x={x[5, 8]:.2f}, y={y[5, 8]:.2f}, z={z[5, 8]:.2f}")

    print("\n" + "=" * 60)
    print("5. ogrid - 开放网格")
    print("=" * 60)

    print("\nogrid 创建开放（稀疏）的多维网格")

    print(f"\nnp.ogrid[0:5, 0:3]:")
    grid_open = np.ogrid[0:5, 0:3]
    print(f"  第一个维度 (shape {grid_open[0].shape}):")
    print(f"    {grid_open[0].ravel()}")
    print(f"  第二个维度 (shape {grid_open[1].shape}):")
    print(f"    {grid_open[1].ravel()}")

    # ogrid 与 mgrid 对比
    print("\nmgrid vs ogrid:")
    print(f"  mgrid: 返回完整网格 ({np.mgrid[0:3, 0:3].shape})")
    print(f"  ogrid: 返回可广播的开放网格")

    x, y = np.ogrid[0:3, 0:3]
    print(f"\nogrid 广播:")
    print(f"  x + y =")
    print(x + y)

    print("\n" + "=" * 60)
    print("6. select - 条件选择")
    print("=" * 60)

    print("\nselect 根据条件从多个数组中选择元素")

    # 定义条件和选择
    x = np.array([0.5, 1.5, 2.5, 3.5, 4.5])

    condlist = [x < 1, x < 3, x >= 3]
    choicelist = [x**2, x**3, x**4]

    result = np.select(condlist, choicelist)
    print(f"\nx = {x}")
    print(f"条件:")
    print(f"  x < 1: x²")
    print(f"  x < 3: x³")
    print(f"  x >= 3: x⁴")
    print(f"结果: {result}")

    # 带默认值
    result_default = np.select(condlist, choicelist, default=0)
    print(f"\n带默认值: {result_default}")

    print("\n" + "=" * 60)
    print("7. choose - 选择函数")
    print("=" * 60)

    print("\nchoose 根据索引数组从选项中选择")

    choices = [[0, 1, 2, 3],
               [10, 11, 12, 13],
               [20, 21, 22, 23]]

    index = [0, 2, 1, 2]

    result = np.choose(index, choices)
    print(f"\nchoices = {choices}")
    print(f"index = {index}")
    print(f"np.choose(index, choices) = {result}")

    print("\n解释:")
    print(f"  index[0]=0 -> choices[0][0]=0")
    print(f"  index[1]=2 -> choices[2][1]=21")
    print(f"  index[2]=1 -> choices[1][2]=12")
    print(f"  index[3]=2 -> choices[2][3]=23")

    print("\n多维 choose:")
    a = np.array([[1, 2, 3], [4, 5, 6]])
    choices = [10, 20]
    index = np.array([[0, 1, 0], [1, 0, 1]])
    result = np.choose(index, choices)
    print(f"\na =")
    print(a)
    print(f"index =")
    print(index)
    print(f"结果 (0->10, 1->20):")
    print(result)

    print("\n" + "=" * 60)
    print("8. 实际应用案例")
    print("=" * 60)

    print("\n案例1: 网格搜索参数组合")
    print("-" * 40)

    # 创建参数网格
    param1 = np.array([0.1, 0.5, 1.0])
    param2 = np.array([10, 20, 30])

    # 使用 mgrid 创建所有组合
    p1, p2 = np.meshgrid(param1, param2, indexing='ij')
    print(f"\n参数组合:")
    for i in range(len(param1)):
        for j in range(len(param2)):
            print(f"  ({p1[i,j]}, {p2[i,j]})")

    print("\n使用 mgrid 评估:")
    x, y = np.mgrid[0:3:4j, 0:2:3j]
    z = np.sin(x) * np.cos(y)
    print(f"\n在网格上评估 sin(x)*cos(y):")
    print(z)

    print("\n案例2: 图像坐标网格")
    print("-" * 40)

    # 创建图像坐标
    height, width = 3, 4
    y_coords, x_coords = np.mgrid[0:height, 0:width]

    print(f"\n图像坐标 ({height}x{width}):")
    print(f"Y 坐标:")
    print(y_coords)
    print(f"X 坐标:")
    print(x_coords)

    # 计算每个像素到中心的距离
    center_y, center_x = height // 2, width // 2
    distance = np.sqrt((y_coords - center_y)**2 + (x_coords - center_x)**2)
    print(f"\n到中心 ({center_x}, {center_y}) 的距离:")
    print(distance)

    print("\n案例3: 分段函数")
    print("-" * 40)

    x = np.linspace(-5, 5, 20)

    # 定义分段函数
    # x < -2: -1
    # -2 <= x < 0: x
    # 0 <= x < 2: x²
    # x >= 2: 4

    condlist = [x < -2, x < 0, x < 2]
    choicelist = [np.ones_like(x) * -1, x, x**2]
    y = np.select(condlist, choicelist, default=4)

    print(f"\n分段函数:")
    print(f"x = {x}")
    print(f"y = {y}")

    print("\n案例4: 构建矩阵索引")
    print("-" * 40)

    # 选择特定位置的元素
    arr = np.arange(20).reshape(4, 5)
    print(f"\n原数组:")
    print(arr)

    # 使用 ix_ 选择
    rows = [0, 2]
    cols = [1, 3, 4]
    selected = arr[np.ix_(rows, cols)]
    print(f"\n选择行 {rows} 和列 {cols}:")
    print(selected)

    print("\n案例5: 多通道颜色处理")
    print("-" * 40)

    # RGB 图像 (3x3 像素, 3 通道)
    image = np.random.randint(0, 256, (3, 3, 3), dtype=np.uint8)
    print(f"\n图像形状: {image.shape}")

    # 分离通道
    r, g, b = image[..., 0], image[..., 1], image[..., 2]

    # 合并通道
    gray = 0.299 * r + 0.587 * g + 0.114 * b
    print(f"\n灰度图:")
    print(gray.astype(int))

    print("\n" + "=" * 60)
    print("9. 函数对比")
    print("=" * 60)

    print("\n网格创建函数对比:")

    print("\n1. meshgrid:")
    print("   np.meshgrid(x, y)")
    print("   - 返回完整网格")
    print("   - 默认使用 'xy' 索引（Cartesian）")

    print("\n2. mgrid:")
    print("   np.mgrid[0:3, 0:4]")
    print("   - 使用切片语法")
    print("   - 返回密集网格")
    print("   - 使用 'ij' 索引（Matrix）")

    print("\n3. ogrid:")
    print("   np.ogrid[0:3, 0:4]")
    print("   - 使用切片语法")
    print("   - 返回开放网格（可广播）")
    print("   - 更节省内存")

    print("\n4. ix_:")
    print("   np.ix_(row_indices, col_indices)")
    print("   - 用于创建可广播的索引数组")
    print("   - 便于选择多维的行和列")

    print("\n" + "=" * 60)
    print("10. 速查表")
    print("=" * 60)

    print("\n索引辅助:")
    print("  np.ix_(*args)           # 构建开放网格")
    print("  np.r_[arrays]           # 沿行连接")
    print("  np.c_[arrays]           # 沿列连接")
    print("  np.mgrid[slices]        # 密集网格")
    print("  np.ogrid[slices]        # 开放网格")

    print("\n条件选择:")
    print("  np.select(condlist, choicelist, default=0)")
    print("  np.choose(a, choices, mode='raise')")
    print("  np.where(condition, x, y)")

    print("\n切片语法:")
    print("  start:stop:step        # 普通切片")
    print("  start:stop:numj        # 复数表示 num 个等间距点")

    print("\n模式参数 (choose):")
    print("  'raise'  # 无效索引引发异常")
    print("  'wrap'   # 循环")
    print("  'clip'   # 裁剪到范围")

    print("\n网格索引约定:")
    print("  'xy' (Cartesian)  # x 变化慢（列）")
    print("  'ij' (Matrix)     # i 变化慢（行）")


if __name__ == "__main__":
    main()