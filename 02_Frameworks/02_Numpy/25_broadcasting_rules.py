#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 25：广播规则详解。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/25_broadcasting_rules.py

知识点：
- 广播机制深入
- 维度匹配规则
- 广播性能
- 常见广播陷阱
- 手动广播 vs 自动广播
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    print("=" * 70)
    print("1. 广播基础")
    print("=" * 70)

    a = np.array([1, 2, 3])
    b = 2

    print(f"a: {a}")
    print(f"b: {b}")
    print(f"a + b: {a + b}")
    print("标量自动广播到数组形状")

    print("\n1.1 两个数组广播")
    print("-" * 70)
    a = np.array([[1, 2, 3], [4, 5, 6]])  # (2, 3)
    b = np.array([1, 2, 3])  # (3,)

    print(f"a shape: {a.shape}")
    print(f"b shape: {b.shape}")
    print(f"a + b:\n{a + b}")
    print("b 广播为 (1, 3) -> (2, 3)")

    print("\n" + "=" * 70)
    print("2. 广播规则详解")
    print("=" * 70)

    print("""
广播规则（从右到左比较维度）：
1. 对齐尾部维度
2. 维度相等或其中一个为1时兼容
3. 缺失维度视为1

规则示例：
  (3, 4) + (4,)      -> (3, 4) ✓
  (2, 1, 3) + (2, 3) -> (2, 2, 3) ✓
  (5, 4) + (3, 4)    -> ✗ 不兼容
  (3, 1) + (1, 3)    -> (3, 3) ✓
""")

    print("\n2.1 规则 1: 尾部对齐")
    print("-" * 70)
    a = np.arange(12).reshape(3, 4)  # (3, 4)
    b = np.arange(4)  # (4,)

    print(f"a shape: {a.shape}")
    print(f"b shape: {b.shape}")
    print("b 广播为 (1, 4) -> (3, 4)")
    print(f"a + b:\n{a + b}")

    print("\n2.2 规则 2: 维度为1时扩展")
    print("-" * 70)
    a = np.arange(3).reshape(3, 1)  # (3, 1)
    b = np.arange(3)  # (3,)

    print(f"a shape: {a.shape}")
    print(f"b shape: {b.shape}")
    print("a 扩展列: (3, 1) -> (3, 3)")
    print("b 扩展行: (3,) -> (1, 3) -> (3, 3)")
    print(f"a + b:\n{a + b}")

    print("\n2.3 规则 3: 多维广播")
    print("-" * 70)
    a = np.arange(24).reshape(2, 3, 4)  # (2, 3, 4)
    b = np.arange(12).reshape(3, 4)  # (3, 4)

    print(f"a shape: {a.shape}")
    print(f"b shape: {b.shape}")
    print("b 广播为 (1, 3, 4) -> (2, 3, 4)")
    print(f"结果 shape: {(a + b).shape}")

    print("\n" + "=" * 70)
    print("3. 手动广播 vs 自动广播")
    print("=" * 70)

    a = np.arange(3).reshape(3, 1)  # (3, 1)
    b = np.arange(3)  # (3,)

    print("a shape:", a.shape)
    print("b shape:", b.shape)

    print("\n3.1 自动广播")
    print("-" * 70)
    result_auto = a + b
    print(f"自动广播结果 shape: {result_auto.shape}")

    print("\n3.2 手动广播（显式）")
    print("-" * 70)
    a_explicit = np.broadcast_to(a, (3, 3))
    b_explicit = np.broadcast_to(b, (3, 3))

    print(f"broadcast_to(a, (3, 3)):\n{a_explicit}")
    print(f"broadcast_to(b, (3, 3)):\n{b_explicit}")

    print("\n3.3 广播信息")
    print("-" * 70)
    a = np.array([[1], [2], [3]])  # (3, 1)
    b = np.array([4, 5, 6])  # (3,)

    print(f"a: {a.ravel()}, shape: {a.shape}")
    print(f"b: {b}, shape: {b.shape}")

    result = a + b
    print(f"\n结果 shape: {result.shape}")
    print(f"结果:\n{result}")

    print("\n" + "=" * 70)
    print("4. 广播性能考虑")
    print("=" * 70)

    import time

    # 创建大数组
    a = np.random.randn(1000, 1000)
    b = np.random.randn(1000)

    print(f"a shape: {a.shape}")
    print(f"b shape: {b.shape}")

    # 自动广播
    start = time.perf_counter()
    result = a + b
    time_auto = time.perf_counter() - start
    print(f"\n自动广播耗时: {time_auto:.6f} 秒")

    # 显式广播
    start = time.perf_counter()
    b_expanded = b.reshape(1, -1)
    result = a + b_expanded
    time_manual = time.perf_counter() - start
    print(f"显式广播耗时: {time_manual:.6f} 秒")

    print("\n性能差异主要来自:")
    print("- 自动广播需要计算广播形状")
    print("- 显式广播省去了形状推断")

    print("\n" + "=" * 70)
    print("5. 常见广播陷阱")
    print("=" * 70)

    print("\n5.1 意外的广播结果")
    print("-" * 70)
    a = np.array([1, 2, 3, 4])  # (4,)
    b = np.array([5, 6])  # (2,)

    print(f"a: {a}, shape: {a.shape}")
    print(f"b: {b}, shape: {b.shape}")

    # 这样会报错
    try:
        result = a + b
        print(f"意外成功: {result}")
    except ValueError as e:
        print(f"正确抛出错误: {e}")

    print("\n5.2 丢失维度信息")
    print("-" * 70)
    a = np.arange(12).reshape(3, 4)
    b = np.arange(3)

    print(f"a shape: {a.shape}")
    print(f"b shape: {b.shape}")

    # 可能想要 (3, 4) + (3, 1)，但实际是 (3, 4) + (3,) -> 列广播
    result = a + b
    print(f"\n实际结果 shape: {result.shape}")
    print("如果想要行广播，需要 reshape:")
    result_row = a + b.reshape(3, 1)
    print(f"a + b.reshape(3, 1) shape: {result_row.shape}")

    print("\n5.3 内存使用")
    print("-" * 70)
    a = np.arange(1000).reshape(1000, 1)
    b = np.arange(1000)

    # 广播会创建临时数组
    result = a + b
    print(f"原始 a 内存: {a.nbytes} 字节")
    print(f"原始 b 内存: {b.nbytes} 字节")
    print(f"结果内存: {result.nbytes} 字节")
    print(f"广播过程中可能有临时数组")

    print("\n" + "=" * 70)
    print("6. 广播工具函数")
    print("=" * 70)

    print("\n6.1 broadcast_to - 显式广播")
    print("-" * 70)
    a = np.arange(3)
    result = np.broadcast_to(a, (4, 3))
    print(f"原始: {a}, shape: {a.shape}")
    print(f"广播后 shape: {result.shape}")
    print(f"广播后数组:\n{result}")

    print("\n6.2 broadcast_arrays - 对齐多个数组")
    print("-" * 70)
    a = np.arange(3).reshape(3, 1)
    b = np.arange(3)

    a_broadcast, b_broadcast = np.broadcast_arrays(a, b)
    print(f"原始 a shape: {a.shape}, b shape: {b.shape}")
    print(f"广播后 a shape: {a_broadcast.shape}, b shape: {b_broadcast.shape}")

    print("\n6.3 广播形状")
    print("-" * 70)
    shapes = [(3, 4), (4,), (1, 4), (3, 1)]
    print("广播多个形状:")
    for shape1, shape2 in zip(shapes, shapes[1:]):
        result_shape = np.broadcast_shapes(shape1, shape2)
        print(f"  {shape1} + {shape2} -> {result_shape}")

    print("\n" + "=" * 70)
    print("7. 实际应用示例")
    print("=" * 70)

    # 示例 1: 数据标准化
    print("\n示例 1: 按列标准化")
    data = np.array([[1, 10, 100], [2, 20, 200], [3, 30, 300]], dtype=float)
    print(f"原始数据:\n{data}")

    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    normalized = (data - mean) / std
    print(f"\n标准化后:\n{normalized}")

    # 示例 2: 外积（向量乘法）
    print("\n示例 2: 外积")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    outer = a.reshape(3, 1) * b.reshape(1, 3)
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"外积:\n{outer}")

    # 示例 3: 距离矩阵
    print("\n示例 3: 计算距离矩阵")
    points = np.array([[0, 0], [1, 1], [2, 0]])
    print(f"点:\n{points}")

    # 使用广播计算所有点对之间的距离
    diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
    distances = np.sqrt(np.sum(diff**2, axis=-1))
    print(f"\n距离矩阵:\n{distances}")

    # 示例 4: 图像处理 - 归一化
    print("\n示例 4: 图像归一化")
    image = np.random.randint(0, 256, (10, 10), dtype=np.uint8).astype(float)
    print(f"图像范围: [{image.min()}, {image.max()}]")

    normalized = (image - image.min()) / (image.max() - image.min())
    print(f"归一化后范围: [{normalized.min():.2f}, {normalized.max():.2f}]")

    # 示例 5: 批量操作
    print("\n示例 5: 批量向量-矩阵乘法")
    vectors = np.random.randn(5, 3)  # 5 个向量，每个 3 维
    matrix = np.random.randn(3, 4)  # 3x4 矩阵

    print(f"vectors shape: {vectors.shape}")
    print(f"matrix shape: {matrix.shape}")

    # 广播乘法
    result = vectors @ matrix
    print(f"结果 shape: {result.shape}")
    print("每个向量与矩阵相乘")

    print("\n" + "=" * 70)
    print("8. 广播最佳实践")
    print("=" * 70)

    print("""
最佳实践：

1. 明确意图：
   - 使用 reshape 显式指定广播维度
   - 添加注释说明广播意图

2. 性能考虑：
   - 大数组避免重复广播
   - 考虑使用 in-place 操作
   - 使用广播而非循环

3. 避免陷阱：
   - 检查形状是否兼容
   - 注意维度顺序
   - 测试广播结果是否符合预期

4. 调试技巧：
   - 使用 shape 属性检查维度
   - 使用 broadcast_arrays 查看广播后形状
   - 小数组上测试后再应用到大数据

5. 内存优化：
   - 使用生成器而非中间数组
   - 考虑分块处理大数组
   - 释放不需要的临时数组
""")


if __name__ == "__main__":
    main()