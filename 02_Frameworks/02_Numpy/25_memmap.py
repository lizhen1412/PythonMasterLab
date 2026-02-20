#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 25：Memory Mapping - 内存映射文件。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/25_memmap.py

NumPy 的 memmap 提供了一种高效处理大型数组的方法。
它允许将文件映射到内存，而不需要一次性加载整个文件。

本节演示：
1. 创建内存映射数组
2. 读写 memmap 文件
3. 只读模式
4. 复制模式
5. 大数据场景应用
6. 性能对比
"""

from __future__ import annotations

import numpy as np
import os


def main() -> None:
    print("=" * 60)
    print("1. 创建内存映射数组")
    print("=" * 60)

    print("\nmemmap 允许处理大于内存的数组")

    # 创建一个大的 memmap 文件
    filename = '/tmp/large_array.dat'
    shape = (1000, 1000)  # 1000x1000 的数组
    dtype = np.float64

    # 创建 memmap
    mmap = np.memmap(filename, dtype=dtype, mode='w+', shape=shape)

    print(f"\n创建 memmap:")
    print(f"  文件: {filename}")
    print(f"  形状: {shape}")
    print(f"  数据类型: {dtype}")
    print(f"  元素总数: {mmap.size}")
    print(f"  内存占用: {mmap.nbytes / 1024 / 1024:.1f} MB")

    # 写入数据
    mmap[:, :] = np.random.randn(*shape)

    # 强制刷新到磁盘
    mmap.flush()

    print(f"\n数据已写入磁盘")

    # 检查文件大小
    file_size = os.path.getsize(filename) / 1024 / 1024
    print(f"文件大小: {file_size:.1f} MB")

    print("\n" + "=" * 60)
    print("2. 读取 memmap 文件")
    print("=" * 60)

    # 重新打开文件读取
    mmap_read = np.memmap(filename, dtype=dtype, mode='r', shape=shape)

    print(f"\n以只读模式打开:")
    print(f"  形状: {mmap_read.shape}")
    print(f"  总和: {mmap_read.sum():.2f}")
    print(f"  平均值: {mmap_read.mean():.2f}")

    # 只访问部分数据（不会全部加载到内存）
    print(f"\n只访问部分数据:")
    print(f"  第一行前5个元素: {mmap_read[0, :5]}")
    print(f"  [100:105, 100:105] 块:")
    print(mmap_read[100:105, 100:105])

    print("\n" + "=" * 60)
    print("3. memmap 模式详解")
    print("=" * 60)

    filename_test = '/tmp/test_modes.dat'
    test_data = np.array([1, 2, 3, 4, 5])

    print("\nmemmap 模式:")

    # mode='r' - 只读
    print(f"\nmode='r' (只读):")
    print(f"  - 文件必须存在")
    print(f"  - 不能修改数据")

    # mode='r+' - 读写
    print(f"\nmode='r+' (读写):")
    print(f"  - 文件必须存在")
    print(f"  - 可以修改数据")

    # mode='w+' - 写入（覆盖或创建）
    print(f"\nmode='w+' (写入):")
    print(f"  - 创建新文件或覆盖现有文件")
    print(f"  - 可以读写")

    # mode='c' - 复制时写入
    print(f"\nmode='c' (复制时写入):")
    print(f"  - 文件必须存在")
    print(f"  - 修改只影响内存副本")
    print(f"  - flush() 或 close() 时才写入磁盘")

    # 演示不同模式
    # w+: 创建并写入
    mmap_w = np.memmap(filename_test, dtype=np.int32, mode='w+', shape=(5,))
    mmap_w[:] = test_data
    mmap_w.flush()
    print(f"\n使用 mode='w+' 创建文件:")
    print(f"  数据: {mmap_w[:]}")

    # r: 只读
    mmap_r = np.memmap(filename_test, dtype=np.int32, mode='r', shape=(5,))
    print(f"\n使用 mode='r' 读取:")
    print(f"  数据: {mmap_r[:]}")

    # c: 复制模式
    mmap_c = np.memmap(filename_test, dtype=np.int32, mode='c', shape=(5,))
    print(f"\n使用 mode='c' (修改前):")
    print(f"  数据: {mmap_c[:]}")

    mmap_c[0] = 999  # 在内存副本中修改
    print(f"  修改后 (内存中): {mmap_c[:]}")

    # 重新读取原文件
    mmap_r2 = np.memmap(filename_test, dtype=np.int32, mode='r', shape=(5,))
    print(f"  磁盘文件 (未 flush): {mmap_r2[:]}")

    # 清理
    del mmap_c
    del mmap_r
    del mmap_w
    os.remove(filename_test)

    print("\n" + "=" * 60)
    print("4. 部分加载与处理")
    print("=" * 60)

    # 创建一个更大的文件
    large_shape = (5000, 5000)  # 25M 元素
    large_file = '/tmp/very_large.dat'

    print(f"\n创建大型 memmap ({large_shape}):")
    large_mmap = np.memmap(large_file, dtype=np.float32,
                           mode='w+', shape=large_shape)
    large_mmap[:, :] = np.random.randn(*large_shape).astype(np.float32)
    large_mmap.flush()

    file_size_mb = os.path.getsize(large_file) / 1024 / 1024
    print(f"  文件大小: {file_size_mb:.1f} MB")

    # 只处理部分数据
    print(f"\n只处理部分数据 (不加载全部):")

    # 重新打开
    large_mmap = np.memmap(large_file, dtype=np.float32,
                           mode='r', shape=large_shape)

    # 计算某一行的统计量
    row_idx = 1000
    row_sum = large_mmap[row_idx, :].sum()
    row_mean = large_mmap[row_idx, :].mean()

    print(f"  第 {row_idx} 行:")
    print(f"    总和: {row_sum:.2f}")
    print(f"    平均: {row_mean:.4f}")

    # 处理一个块
    print(f"\n处理一个块:")
    chunk = large_mmap[1000:1010, 1000:1010]
    chunk_mean = chunk.mean()
    print(f"  块 [1000:1010, 1000:1010] 平均值: {chunk_mean:.4f}")

    # 清理
    del large_mmap
    os.remove(large_file)

    print("\n" + "=" * 60)
    print("5. 实际应用场景")
    print("=" * 60)

    print("\n场景1: 处理无法全部装入内存的大数据集")
    print("-" * 40)

    # 模拟：有一个 10GB 的数据文件，但只有 2GB 内存
    # 使用 memmap 可以按需处理

    print(f"使用 memmap 处理大数据:")
    print(f"  1. 创建/打开 memmap 文件")
    print(f"  2. 分块读取和处理数据")
    print(f"  3. 只在需要时加载到内存")

    print("\n场景2: 多进程共享数据")
    print("-" * 40)

    print(f"使用 memmap 在进程间共享数据:")
    print(f"  1. 主进程创建 memmap 文件并写入数据")
    print(f"  2. 子进程以只读模式打开同一文件")
    print(f"  3. 避免数据复制，节省内存")

    print("\n场景3: 数据缓存")
    print("-" * 40)

    cache_file = '/tmp/cache.dat'

    # 创建缓存
    cache = np.memmap(cache_file, dtype=np.float32, mode='w+',
                      shape=(1000, 100))

    # 写入缓存数据
    cache[:, :] = np.random.randn(1000, 100).astype(np.float32)
    cache.flush()

    print(f"数据已缓存到: {cache_file}")

    # 后续读取缓存
    cache_read = np.memmap(cache_file, dtype=np.float32, mode='r',
                           shape=(1000, 100))

    print(f"缓存大小: {cache_read.shape}")
    print(f"缓存数据样本: {cache_read[0, :5]}")

    # 清理
    del cache
    del cache_read
    os.remove(cache_file)

    print("\n场景4: 增量处理")
    print("-" * 40)

    # 逐块处理大型数据
    process_file = '/tmp/process_data.dat'
    chunk_size = 1000

    process_mmap = np.memmap(process_file, dtype=np.float32,
                             mode='w+', shape=(10000,))

    print(f"增量处理 10000 个元素:")

    # 分块处理
    for i in range(0, 10000, chunk_size):
        end = min(i + chunk_size, 10000)
        # 处理这个块
        process_mmap[i:end] = np.arange(i, end, dtype=np.float32)

    process_mmap.flush()

    # 验证
    result = np.memmap(process_file, dtype=np.float32, mode='r', shape=(10000,))
    print(f"  前10个: {result[:10]}")
    print(f"  后10个: {result[-10:]}")

    # 清理
    del process_mmap
    del result
    os.remove(process_file)

    print("\n" + "=" * 60)
    print("6. memmap 与普通数组对比")
    print("=" * 60)

    size = (5000, 5000)

    # 普通数组（全部加载到内存）
    print(f"\n普通数组 ({size}):")
    print(f"  创建时: 全部数据加载到内存")
    print(f"  访问时: 直接访问内存")
    print(f"  占用: {np.prod(size) * 8 / 1024 / 1024:.1f} MB (float64)")

    # memmap（按需加载）
    print(f"\nmemmap ({size}):")
    print(f"  创建时: 只创建文件映射")
    print(f"  访问时: 按需从磁盘加载")
    print(f"  占用: 极少（只有访问的页）")

    print("\n何时使用 memmap:")
    print("  ✓ 数据太大，无法全部装入内存")
    print("  ✓ 需要频繁访问数据的不同部分")
    print("  ✓ 多进程需要共享数据")
    print("  ✓ 数据持久化存储")

    print("\n何时使用普通数组:")
    print("  ✓ 数据可以全部装入内存")
    print("  ✓ 需要频繁访问全部数据")
    print("  ✓ 追求最快的访问速度")

    print("\n" + "=" * 60)
    print("7. 最佳实践")
    print("=" * 60)

    print("\n使用 memmap 的最佳实践:")

    print("\n1. 选择合适的模式:")
    print("  - 只读数据: mode='r'")
    print("  - 需要修改: mode='r+' 或 'w+'")
    print("  - 延迟写入: mode='c'")

    print("\n2. 及时刷新:")
    print("  mmap.flush()  # 强制写入磁盘")

    print("\n3. 考虑访问模式:")
    print("  - 连续访问更快（空间局部性）")
    print("  - 避免频繁的小块随机访问")

    print("\n4. 文件清理:")
    print("  - 使用完毕后删除文件")
    print("  - 或使用临时文件 (tempfile)")

    print("\n5. 错误处理:")
    print("  - 检查文件是否存在")
    print("  - 捕获 IOError")

    print("\n" + "=" * 60)
    print("8. 函数速查")
    print("=" * 60)

    print("\n创建 memmap:")
    print("  np.memmap(filename, dtype=np.float64, mode='r+', shape=(N, M))")
    print()
    print("  mode 参数:")
    print("    'r'   - 只读，文件必须存在")
    print("    'r+'  - 读写，文件必须存在")
    print("    'w+'  - 写入，创建或覆盖文件")
    print("    'c'   - 复制时写入，文件必须存在")

    print("\n属性:")
    print("  mmap.shape   # 数组形状")
    print("  mmap.dtype   # 数据类型")
    print("  mmap.size    # 元素总数")
    print("  mmap.nbytes  # 字节大小")
    print("  mmap.mode    # 打开模式")
    print("  mmap.filename # 文件名")

    print("\n方法:")
    print("  mmap.flush() # 刷新到磁盘")

    print("\n与普通数组相同的操作:")
    print("  mmap[:] = value     # 赋值")
    print("  mmap.sum()          # 统计")
    print("  mmap[index]         # 索引")


if __name__ == "__main__":
    main()