#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 28：逻辑与比较。

运行：
    python3 02_Frameworks/02_Numpy/28_logic_comparison.py

知识点：
- logical_and / logical_or / logical_not / logical_xor
- bitwise_and / bitwise_or / bitwise_xor / bitwise_not
- all / any - 逻辑聚合
- allclose / isclose - 近似比较
- equal / not_equal
- greater / less / greater_equal / less_equal
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([True, False, True, False])
    b = np.array([True, True, False, False])

    print("=" * 70)
    print("1. 逻辑运算")
    print("=" * 70)

    print(f"a: {a}")
    print(f"b: {b}")

    print("\n1.1 logical_and - 逻辑与")
    print("-" * 70)
    result = np.logical_and(a, b)
    print(f"logical_and(a, b): {result}")
    print("（True AND True = True）")

    print("\n1.2 logical_or - 逻辑或")
    print("-" * 70)
    result = np.logical_or(a, b)
    print(f"logical_or(a, b): {result}")
    print("（True OR False = True）")

    print("\n1.3 logical_not - 逻辑非")
    print("-" * 70)
    result = np.logical_not(a)
    print(f"logical_not(a): {result}")
    print("（NOT True = False）")

    print("\n1.4 logical_xor - 逻辑异或")
    print("-" * 70)
    result = np.logical_xor(a, b)
    print(f"logical_xor(a, b): {result}")
    print("（True XOR True = False, True XOR False = True）")

    print("\n" + "=" * 70)
    print("2. 位运算")
    print("=" * 70)

    x = np.array([1, 2, 3, 4], dtype=np.uint8)
    y = np.array([4, 3, 2, 1], dtype=np.uint8)

    print(f"x: {x}")
    print(f"y: {y}")

    print("\n2.1 bitwise_and - 按位与")
    print("-" * 70)
    result = np.bitwise_and(x, y)
    print(f"bitwise_and(x, y): {result}")
    print("（二进制表示）")
    print(f"  x: {[bin(i) for i in x]}")
    print(f"  y: {[bin(i) for i in y]}")
    print(f"  结果: {[bin(i) for i in result]}")

    print("\n2.2 bitwise_or - 按位或")
    print("-" * 70)
    result = np.bitwise_or(x, y)
    print(f"bitwise_or(x, y): {result}")

    print("\n2.3 bitwise_xor - 按位异或")
    print("-" * 70)
    result = np.bitwise_xor(x, y)
    print(f"bitwise_xor(x, y): {result}")

    print("\n2.4 bitwise_not / invert")
    print("-" * 70)
    result = np.bitwise_not(x)
    print(f"bitwise_not(x): {result}")
    print(f"（~{x[0]} = {result[0]}, 即 {bin(x[0])} -> {bin(result[0])}）")

    print("\n" + "=" * 70)
    print("3. 比较运算")
    print("=" * 70)

    a = np.array([1, 2, 3, 4, 5])
    b = np.array([2, 2, 2, 2, 2])

    print(f"a: {a}")
    print(f"b: {b}")

    print("\n3.1 相等性比较")
    print("-" * 70)
    print(f"equal(a, b): {np.equal(a, b)}")
    print(f"not_equal(a, b): {np.not_equal(a, b)}")

    print("\n3.2 大小比较")
    print("-" * 70)
    print(f"greater(a, b): {np.greater(a, b)}")
    print(f"greater_equal(a, b): {np.greater_equal(a, b)}")
    print(f"less(a, b): {np.less(a, b)}")
    print(f"less_equal(a, b): {np.less_equal(a, b)}")

    print("\n3.3 运算符形式")
    print("-" * 70)
    print(f"a == b: {a == b}")
    print(f"a != b: {a != b}")
    print(f"a > b: {a > b}")
    print(f"a >= b: {a >= b}")
    print(f"a < b: {a < b}")
    print(f"a <= b: {a <= b}")

    print("\n" + "=" * 70)
    print("4. 逻辑聚合")
    print("=" * 70)

    a = np.array([True, True, False, True])
    b = np.array([False, False, False, False])

    print(f"a: {a}")
    print(f"b: {b}")

    print("\n4.1 all - 全部为 True")
    print("-" * 70)
    print(f"all(a): {np.all(a)}")
    print(f"all(b): {np.all(b)}")

    print("\n4.2 any - 存在 True")
    print("-" * 70)
    print(f"any(a): {np.any(a)}")
    print(f"any(b): {np.any(b)}")

    print("\n4.3 按 axis 聚合")
    print("-" * 70)
    arr = np.array([[True, False], [False, False], [True, True]])
    print(f"arr:\n{arr}")

    print(f"\nall(axis=0) [每列]: {np.all(arr, axis=0)}")
    print(f"all(axis=1) [每行]: {np.all(arr, axis=1)}")
    print(f"any(axis=0) [每列]: {np.any(arr, axis=0)}")
    print(f"any(axis=1) [每行]: {np.any(arr, axis=1)}")

    print("\n" + "=" * 70)
    print("5. 近似比较")
    print("=" * 70)

    a = np.array([1.0, 2.0, 3.0])
    b = np.array([1.0000001, 2.0000001, 3.0000001])

    print(f"a: {a}")
    print(f"b: {b}")

    print("\n5.1 equal 精确比较")
    print("-" * 70)
    print(f"a == b: {a == b}")
    print("（浮点数精度问题可能返回 False）")

    print("\n5.2 allclose - 近似相等")
    print("-" * 70)
    result = np.allclose(a, b)
    print(f"allclose(a, b): {result}")
    print("（默认 rtol=1e-5, atol=1e-8）")

    print("\n5.3 isclose - 逐元素近似比较")
    print("-" * 70)
    result = np.isclose(a, b)
    print(f"isclose(a, b): {result}")

    print("\n5.4 自定义容差")
    print("-" * 70)
    result = np.allclose(a, b, rtol=1e-10, atol=1e-10)
    print(f"allclose(a, b, rtol=1e-10, atol=1e-10): {result}")

    print("\n5.5 相对绝对容差")
    print("-" * 70)
    print("allclose 使用公式: |a - b| <= (atol + rtol * |b|)")
    print("rtol: 相对容差")
    print("atol: 绝对容差")

    print("\n" + "=" * 70)
    print("6. 条件选择与计数")
    print("=" * 70)

    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    print(f"data: {data}")

    print("\n6.1 统计满足条件的元素")
    print("-" * 70)
    mask = data > 5
    print(f"mask (data > 5): {mask}")
    print(f"count: {np.sum(mask)}")
    print(f"values: {data[mask]}")

    print("\n6.2 多条件组合")
    print("-" * 70)
    mask = (data > 3) & (data < 8)
    print(f"(data > 3) & (data < 8): {mask}")
    print(f"values: {data[mask]}")

    print("\n6.3 where 函数")
    print("-" * 70)
    result = np.where(data > 5, data, 0)
    print(f"where(data > 5, data, 0): {result}")
    print("（大于 5 保留，否则为 0）")

    print("\n" + "=" * 70)
    print("7. 特殊值比较")
    print("=" * 70)

    data = np.array([1, np.nan, 3, np.inf, -np.inf, 5])

    print(f"data: {data}")

    print("\n7.1 NaN 比较")
    print("-" * 70)
    print(f"data == np.nan: {data == np.nan}")
    print("（NaN != NaN 总是 True）")

    print(f"\nnp.isnan(data): {np.isnan(data)}")

    print("\n7.2 Inf 比较")
    print("-" * 70)
    print(f"data == np.inf: {data == np.inf}")
    print(f"np.isinf(data): {np.isinf(data)}")

    print("\n7.3 有限值检查")
    print("-" * 70)
    print(f"np.isfinite(data): {np.isfinite(data)}")

    print("\n" + "=" * 70)
    print("8. 实际应用示例")
    print("=" * 70)

    # 示例 1: 数据验证
    print("\n示例 1: 验证数据范围")
    data = np.array([15, 25, 35, 45, 55, 65, 75])
    valid_range = (0, 100)

    is_valid = (data >= valid_range[0]) & (data <= valid_range[1])
    print(f"data: {data}")
    print(f"有效范围: {valid_range}")
    print(f"是否全部有效: {np.all(is_valid)}")

    # 示例 2: 阈值检测
    print("\n示例 2: 多阈值分类")
    scores = np.array([45, 67, 89, 92, 78, 56])
    print(f"分数: {scores}")

    grade_A = scores >= 90
    grade_B = (scores >= 80) & (scores < 90)
    grade_C = (scores >= 70) & (scores < 80)
    grade_D = scores < 70

    print(f"\n等级 A (>=90): {scores[grade_A]}")
    print(f"等级 B (80-90): {scores[grade_B]}")
    print(f"等级 C (70-80): {scores[grade_C]}")
    print(f"等级 D (<70): {scores[grade_D]}")

    # 示例 3: 异常值检测
    print("\n示例 3: 基于标准差检测异常值")
    data = np.array([10, 12, 11, 13, 100, 12, 11])
    mean = np.mean(data)
    std = np.std(data)
    threshold = 3

    is_outlier = np.abs(data - mean) > threshold * std
    print(f"data: {data}")
    print(f"均值: {mean:.2f}, 标准差: {std:.2f}")
    print(f"异常值: {data[is_outlier]}")

    # 示例 4: 比较两个数组
    print("\n示例 4: 找出差异位置")
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([1, 2, 5, 4, 6])

    are_equal = arr1 == arr2
    print(f"arr1: {arr1}")
    print(f"arr2: {arr2}")
    print(f"相等: {are_equal}")

    diff_positions = np.where(~are_equal)[0]
    print(f"差异位置: {diff_positions}")
    print(f"差异值: arr1={arr1[diff_positions]}, arr2={arr2[diff_positions]}")

    # 示例 5: 条件求和
    print("\n示例 5: 条件统计")
    data = np.random.randn(100)

    positive_count = np.sum(data > 0)
    negative_count = np.sum(data < 0)
    positive_sum = np.sum(data[data > 0])
    negative_sum = np.sum(data[data < 0])

    print(f"正数个数: {positive_count}")
    print(f"负数个数: {negative_count}")
    print(f"正数和: {positive_sum:.2f}")
    print(f"负数和: {negative_sum:.2f}")

    # 示例 6: 位标志操作
    print("\n示例 6: 位标志")
    flags = np.array([0, 1, 2, 3, 4, 5, 6, 7], dtype=np.uint8)

    # 定义标志位
    FLAG_READ = 0b001  # 1
    FLAG_WRITE = 0b010  # 2
    FLAG_EXEC = 0b100  # 4

    print(f"flags: {flags}")
    print(f"bin(flags): {[bin(f) for f in flags]}")

    has_read = (flags & FLAG_READ) != 0
    has_write = (flags & FLAG_WRITE) != 0
    has_exec = (flags & FLAG_EXEC) != 0

    print(f"\n读权限: {has_read}")
    print(f"写权限: {has_write}")
    print(f"执行权限: {has_exec}")

    # 设置读权限
    flags_with_read = np.bitwise_or(flags, FLAG_READ)
    print(f"\n设置读权限后: {flags_with_read}")

    # 清除写权限
    flags_without_write = np.bitwise_and(flags, ~FLAG_WRITE)
    print(f"清除写权限后: {flags_without_write}")

    print("\n" + "=" * 70)
    print("9. 最佳实践")
    print("=" * 70)

    print("""
最佳实践：

1. 逻辑运算：
   - 使用 logical_* 而不是 and/or/not
   - 使用 & | ~ 而不是 bitwise_*

2. 浮点数比较：
   - 避免使用 == 比较
   - 使用 allclose 或 isclose
   - 考虑合适的容差

3. 条件组合：
   - 使用括号明确优先级
   - (a > 0) & (b < 10) 而不是 a > 0 & b < 10

4. 性能优化：
   - 使用 any/all 检查条件
   - 使用 np.where 而不是循环
   - 使用布尔索引

5. NaN 处理：
   - 使用 isnan 检查 NaN
   - 使用 isfinite 检查有限值
   - 注意 NaN 的特殊行为
""")


if __name__ == "__main__":
    main()
