#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 24：形状操作全集。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/24_shape_ops_complete.py

知识点：
- flatten vs ravel 区别
- squeeze - 删除长度为1的维度
- swapaxes - 交换轴
- moveaxis - 移动轴
- atleast_1d/2d/3d
- split/vsplit/hsplit/dsplit
- tile/repeat - 重复
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    print("=" * 70)
    print("1. flatten vs ravel")
    print("=" * 70)

    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print("原始数组:")
    print(arr)

    print("\n1.1 ravel - 返回视图（可能）")
    print("-" * 70)
    flattened = arr.ravel()
    print(f"ravel(): {flattened}")
    print(f"是视图: {np.shares_memory(arr, flattened)}")

    # 修改视图
    flattened[0] = 999
    print(f"\n修改 flattened[0] 后:")
    print(f"flattened: {flattened}")
    print(f"arr:\n{arr}")

    print("\n1.2 flatten - 总是返回副本")
    print("-" * 70)
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    flattened = arr.flatten()
    print(f"flatten(): {flattened}")
    print(f"是视图: {np.shares_memory(arr, flattened)}")

    # 修改副本不影响原数组
    flattened[0] = 999
    print(f"\n修改 flattened[0] 后:")
    print(f"flattened: {flattened}")
    print(f"arr:\n{arr}")

    print("\n1.3 order 参数")
    print("-" * 70)
    arr = np.array([[1, 2], [3, 4]])
    print(f"C 顺序 (行优先): {arr.flatten(order='C')}")
    print(f"F 顺序 (列优先): {arr.flatten(order='F')}")

    print("\n" + "=" * 70)
    print("2. squeeze - 删除长度为1的维度")
    print("=" * 70)

    arr = np.arange(6).reshape(1, 2, 1, 3)
    print(f"原始形状: {arr.shape}")
    print(f"数组:\n{arr}")

    squeezed = np.squeeze(arr)
    print(f"\nsqueeze() 后形状: {squeezed.shape}")
    print(f"数组:\n{squeezed}")

    print("\n2.1 指定 axis")
    print("-" * 70)
    arr = np.arange(6).reshape(1, 2, 3)
    print(f"原始形状: {arr.shape}")

    squeezed = np.squeeze(arr, axis=0)
    print(f"squeeze(axis=0) 后形状: {squeezed.shape}")

    print("\n" + "=" * 70)
    print("3. swapaxes - 交换轴")
    print("=" * 70)

    arr = np.arange(24).reshape(2, 3, 4)
    print(f"原始形状: {arr.shape}")

    swapped = np.swapaxes(arr, 0, 2)
    print(f"\nswapaxes(arr, 0, 2) 后形状: {swapped.shape}")
    print("(交换第0维和第2维)")

    print("\n3.1 转置 (2D 特殊情况)")
    print("-" * 70)
    arr_2d = np.arange(6).reshape(2, 3)
    print(f"原始:\n{arr_2d}")
    print(f"\nswapaxes(0, 1) / .T:\n{arr_2d.swapaxes(0, 1)}")

    print("\n" + "=" * 70)
    print("4. moveaxis - 移动轴")
    print("=" * 70)

    arr = np.arange(24).reshape(2, 3, 4)
    print(f"原始形状: {arr.shape}")
    print(f"轴顺序: (0, 1, 2) -> (2, 3, 4)")

    moved = np.moveaxis(arr, 0, -1)
    print(f"\nmoveaxis(arr, 0, -1) 后形状: {moved.shape}")
    print("(将第0维移到最后)")

    print("\n4.1 移动多个轴")
    print("-" * 70)
    arr = np.arange(8).reshape(2, 2, 2)
    print(f"原始形状: {arr.shape}")

    moved = np.moveaxis(arr, [0, 1], [1, 0])
    print(f"moveaxis(arr, [0,1], [1,0]) 后形状: {moved.shape}")
    print("(交换第0维和第1维)")

    print("\n" + "=" * 70)
    print("5. atleast_1d/2d/3d - 确保最小维度")
    print("=" * 70)

    scalar = 5
    arr_1d = np.array([1, 2, 3])
    arr_2d = np.array([[1, 2], [3, 4]])

    print("\n5.1 atleast_1d")
    print("-" * 70)
    print(f"标量 {scalar} -> {np.atleast_1d(scalar)}")
    print(f"1D 数组形状不变: {np.atleast_1d(arr_1d).shape}")

    print("\n5.2 atleast_2d")
    print("-" * 70)
    print(f"标量 {scalar} -> 形状 {np.atleast_2d(scalar).shape}")
    print(f"1D 数组形状 {arr_1d.shape} -> {np.atleast_2d(arr_1d).shape}")
    print(f"2D 数组形状不变: {np.atleast_2d(arr_2d).shape}")

    print("\n5.3 atleast_3d")
    print("-" * 70)
    print(f"1D 数组形状 {arr_1d.shape} -> {np.atleast_3d(arr_1d).shape}")
    print(f"2D 数组形状 {arr_2d.shape} -> {np.atleast_3d(arr_2d).shape}")

    print("\n" + "=" * 70)
    print("6. split - 分割数组")
    print("=" * 70)

    arr = np.arange(12)
    print(f"原始数组: {arr}")

    print("\n6.1 split - 等分")
    print("-" * 70)
    parts = np.split(arr, 3)
    print(f"split(arr, 3):")
    for i, part in enumerate(parts):
        print(f"  部分 {i+1}: {part}")

    print("\n6.2 array_split - 不等分")
    print("-" * 70)
    parts = np.array_split(arr, 5)
    print(f"array_split(arr, 5):")
    for i, part in enumerate(parts):
        print(f"  部分 {i+1}: {part}")

    print("\n6.3 指定分割点")
    print("-" * 70)
    parts = np.split(arr, [3, 7])
    print(f"split(arr, [3, 7]):")
    for i, part in enumerate(parts):
        print(f"  部分 {i+1}: {part}")

    print("\n6.4 vsplit / hsplit")
    print("-" * 70)
    arr_2d = np.arange(12).reshape(4, 3)
    print(f"2D 数组:\n{arr_2d}")

    print(f"\nvsplit(arr_2d, 2) [纵向分割]:")
    for part in np.vsplit(arr_2d, 2):
        print(part)

    print(f"\nhsplit(arr_2d, 3) [横向分割]:")
    for part in np.hsplit(arr_2d, 3):
        print(part)

    print("\n6.5 dsplit - 深度分割 (3D)")
    print("-" * 70)
    arr_3d = np.arange(24).reshape(2, 3, 4)
    print(f"3D 数组形状: {arr_3d.shape}")

    parts = np.dsplit(arr_3d, 2)
    print(f"\ndsplit(arr_3d, 2):")
    for i, part in enumerate(parts):
        print(f"  部分 {i+1} 形状: {part.shape}")

    print("\n" + "=" * 70)
    print("7. repeat - 重复元素")
    print("=" * 70)

    arr = np.array([1, 2, 3])
    print(f"原始数组: {arr}")

    print("\n7.1 repeat - 重复元素")
    print("-" * 70)
    print(f"repeat(arr, 2): {np.repeat(arr, 2)}")
    print(f"repeat(arr, [1, 2, 3]): {np.repeat(arr, [1, 2, 3])}")

    print("\n7.2 按轴重复")
    print("-" * 70)
    arr_2d = np.array([[1, 2], [3, 4]])
    print(f"原始 2D:\n{arr_2d}")

    print(f"\nrepeat(arr_2d, 2, axis=0):\n{np.repeat(arr_2d, 2, axis=0)}")
    print(f"repeat(arr_2d, 2, axis=1):\n{np.repeat(arr_2d, 2, axis=1)}")

    print("\n" + "=" * 70)
    print("8. tile - 平铺数组")
    print("=" * 70)

    arr = np.array([1, 2, 3])
    print(f"原始数组: {arr}")

    print(f"\ntile(arr, 2): {np.tile(arr, 2)}")
    print(f"tile(arr, (2, 3)):\n{np.tile(arr, (2, 3))}")

    print("\n8.1 多维平铺")
    print("-" * 70)
    arr_2d = np.array([[1, 2], [3, 4]])
    print(f"原始 2D:\n{arr_2d}")

    print(f"\ntile(arr_2d, (2, 3)):\n{np.tile(arr_2d, (2, 3))}")
    print("纵向 2 次，横向 3 次")

    print("\n" + "=" * 70)
    print("9. 其他形状操作")
    print("=" * 70)

    print("\n9.1 resize - 就地调整大小")
    print("-" * 70)
    arr = np.arange(12)
    print(f"原始: {arr}")
    arr.resize(6)
    print(f"resize(6) 后: {arr}")
    print("注意: 丢弃了部分数据")

    print("\n9.2 roll - 滚动元素")
    print("-" * 70)
    arr = np.arange(10)
    print(f"原始: {arr}")
    print(f"roll(arr, 2): {np.roll(arr, 2)}")
    print(f"roll(arr, -2): {np.roll(arr, -2)}")

    print("\n9.3 rot90 - 旋转 90 度")
    print("-" * 70)
    arr = np.arange(9).reshape(3, 3)
    print(f"原始:\n{arr}")
    print(f"\nrot90(arr, k=1):\n{np.rot90(arr, k=1)}")
    print(f"\nrot90(arr, k=2):\n{np.rot90(arr, k=2)}")

    print("\n9.4 flip / flipud / fliplr")
    print("-" * 70)
    arr = np.arange(9).reshape(3, 3)
    print(f"原始:\n{arr}")
    print(f"\nflipud(arr) [上下翻转]:\n{np.flipud(arr)}")
    print(f"\nfliplr(arr) [左右翻转]:\n{np.fliplr(arr)}")
    print(f"\nflip(arr, axis=0):\n{np.flip(arr, axis=0)}")

    print("\n" + "=" * 70)
    print("10. 实际应用示例")
    print("=" * 70)

    # 示例 1: 图像处理 - 展平
    print("\n示例 1: 图像数据展平")
    image = np.random.randint(0, 256, (28, 28), dtype=np.uint8)
    print(f"图像形状: {image.shape}")
    flattened = image.ravel()
    print(f"展平后形状: {flattened.shape}")

    # 示例 2: 批处理 - 增加批次维度
    print("\n示例 2: 添加批次维度")
    single_sample = np.random.randn(10)
    batch = np.atleast_2d(single_sample)
    print(f"单样本形状: {single_sample.shape}")
    print(f"批次形状: {batch.shape}")

    # 示例 3: 数据复制 - tile
    print("\n示例 3: 数据增强")
    pattern = np.array([1, 2, 3])
    tiled = np.tile(pattern, 4)
    print(f"原始模式: {pattern}")
    print(f"平铺后: {tiled}")

    # 示例 4: 批量分割
    print("\n示例 4: 批量数据分割")
    data = np.arange(100)
    batches = np.array_split(data, 10)
    print(f"总数据量: {len(data)}")
    print(f"分割成 {len(batches)} 批")
    print(f"各批大小: {[len(b) for b in batches]}")


if __name__ == "__main__":
    main()