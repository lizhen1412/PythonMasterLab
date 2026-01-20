#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 27：集合操作。

运行：
    python3 02_Frameworks/02_Numpy/27_set_operations.py

知识点：
- unique - 去重
- in1d - 成员检查
- intersect1d - 交集
- setdiff1d - 差集
- setxor1d - 对称差
- union1d - 并集
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    print("=" * 70)
    print("1. unique - 去重")
    print("=" * 70)

    arr = np.array([3, 1, 2, 1, 5, 3, 4, 2])
    print(f"原始数组: {arr}")

    print("\n1.1 基础去重")
    print("-" * 70)
    unique_vals = np.unique(arr)
    print(f"unique(arr): {unique_vals}")

    print("\n1.2 返回索引")
    print("-" * 70)
    unique_vals, indices = np.unique(arr, return_index=True)
    print(f"unique(arr, return_index=True):")
    print(f"  唯一值: {unique_vals}")
    print(f"  首次出现索引: {indices}")
    print(f"  验证: {arr[indices]}")

    print("\n1.3 返回计数")
    print("-" * 70)
    unique_vals, counts = np.unique(arr, return_counts=True)
    print(f"unique(arr, return_counts=True):")
    for val, count in zip(unique_vals, counts):
        print(f"  {val}: 出现 {count} 次")

    print("\n1.4 返回反转索引")
    print("-" * 70)
    unique_vals, inverse = np.unique(arr, return_inverse=True)
    print(f"unique(arr, return_inverse=True):")
    print(f"  唯一值: {unique_vals}")
    print(f"  反转索引: {inverse}")
    print(f"  重构数组: {unique_vals[inverse]}")

    print("\n1.5 axis 参数（2D 数组）")
    print("-" * 70)
    arr_2d = np.array([[1, 2, 1], [3, 4, 3], [1, 2, 1]])
    print(f"原始 2D 数组:\n{arr_2d}")

    unique_rows = np.unique(arr_2d, axis=0)
    print(f"\nunique(arr_2d, axis=0) [唯一行]:")
    print(unique_rows)

    unique_cols = np.unique(arr_2d, axis=1)
    print(f"\nunique(arr_2d, axis=1) [唯一列]:")
    print(unique_cols)

    print("\n" + "=" * 70)
    print("2. in1d - 成员检查")
    print("=" * 70)

    arr = np.array([1, 2, 3, 4, 5])
    test = np.array([2, 4, 6, 8])

    print(f"arr: {arr}")
    print(f"test: {test}")

    print("\n2.1 基础成员检查")
    print("-" * 70)
    result = np.in1d(test, arr)
    print(f"in1d(test, arr): {result}")
    print("（test 中的元素是否在 arr 中）")

    print("\n2.2 invert 参数")
    print("-" * 70)
    result = np.in1d(test, arr, invert=True)
    print(f"in1d(test, arr, invert=True): {result}")
    print("（test 中的元素是否不在 arr 中）")

    print("\n2.3 实际应用")
    print("-" * 70)
    products = np.array(["apple", "banana", "cherry", "date"])
    available = np.array(["apple", "date", "fig", "grape"])

    in_stock = np.in1d(products, available)
    print(f"产品: {products}")
    print(f"库存: {available}")
    print(f"是否有货: {in_stock}")
    print(f"有货产品: {products[in_stock]}")

    print("\n" + "=" * 70)
    print("3. intersect1d - 交集")
    print("=" * 70)

    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([3, 4, 5, 6, 7])

    print(f"arr1: {arr1}")
    print(f"arr2: {arr2}")

    print("\n3.1 基础交集")
    print("-" * 70)
    intersection = np.intersect1d(arr1, arr2)
    print(f"intersect1d(arr1, arr2): {intersection}")

    print("\n3.2 return_indices=True")
    print("-" * 70)
    intersection, idx1, idx2 = np.intersect1d(arr1, arr2, return_indices=True)
    print(f"intersect1d(arr1, arr2, return_indices=True):")
    print(f"  交集: {intersection}")
    print(f"  arr1 中的索引: {idx1}")
    print(f"  arr2 中的索引: {idx2}")
    print(f"  验证: arr1[{idx1}] = {arr1[idx1]}")
    print(f"  验证: arr2[{idx2}] = {arr2[idx2]}")

    print("\n" + "=" * 70)
    print("4. setdiff1d - 差集")
    print("=" * 70)

    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([3, 4, 5, 6, 7])

    print(f"arr1: {arr1}")
    print(f"arr2: {arr2}")

    print("\n4.1 arr1 - arr2")
    print("-" * 70)
    diff = np.setdiff1d(arr1, arr2)
    print(f"setdiff1d(arr1, arr2): {diff}")
    print("（在 arr1 但不在 arr2 中）")

    print("\n4.2 arr2 - arr1")
    print("-" * 70)
    diff = np.setdiff1d(arr2, arr1)
    print(f"setdiff1d(arr2, arr1): {diff}")

    print("\n" + "=" * 70)
    print("5. setxor1d - 对称差")
    print("=" * 70)

    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([3, 4, 5, 6, 7])

    print(f"arr1: {arr1}")
    print(f"arr2: {arr2}")

    print("\n5.1 对称差")
    print("-" * 70)
    xor = np.setxor1d(arr1, arr2)
    print(f"setxor1d(arr1, arr2): {xor}")
    print("（在任一数组中但不同时在两个数组中）")

    print("\n5.2 verify")
    print("-" * 70)
    union = np.union1d(arr1, arr2)
    intersection = np.intersect1d(arr1, arr2)
    expected = np.setdiff1d(union, intersection)
    print(f"union - intersection: {expected}")
    print(f"setxor1d 结果: {xor}")
    print(f"相等: {np.array_equal(xor, expected)}")

    print("\n" + "=" * 70)
    print("6. union1d - 并集")
    print("=" * 70)

    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([3, 4, 5, 6, 7])

    print(f"arr1: {arr1}")
    print(f"arr2: {arr2}")

    print("\n6.1 基础并集")
    print("-" * 70)
    union = np.union1d(arr1, arr2)
    print(f"union1d(arr1, arr2): {union}")

    print("\n" + "=" * 70)
    print("7. 字符串数组的集合操作")
    print("=" * 70)

    arr1 = np.array(["apple", "banana", "cherry"])
    arr2 = np.array(["banana", "cherry", "date"])

    print(f"arr1: {arr1}")
    print(f"arr2: {arr2}")

    print(f"\nunique(arr1): {np.unique(arr1)}")
    print(f"intersect1d(arr1, arr2): {np.intersect1d(arr1, arr2)}")
    print(f"setdiff1d(arr1, arr2): {np.setdiff1d(arr1, arr2)}")
    print(f"setxor1d(arr1, arr2): {np.setxor1d(arr1, arr2)}")
    print(f"union1d(arr1, arr2): {np.union1d(arr1, arr2)}")

    print("\n" + "=" * 70)
    print("8. 实际应用示例")
    print("=" * 70)

    # 示例 1: 数据清洗
    print("\n示例 1: 去除重复数据")
    data = np.array([1, 2, 2, 3, 3, 3, 4, 5, 5])
    print(f"原始数据: {data}")
    unique_data = np.unique(data)
    print(f"去重后: {unique_data}")

    # 示例 2: 比较两个数据集
    print("\n示例 2: 找出新增和删除的项目")
    old_list = np.array([1, 2, 3, 4, 5])
    new_list = np.array([3, 4, 5, 6, 7])

    added = np.setdiff1d(new_list, old_list)
    removed = np.setdiff1d(old_list, new_list)
    common = np.intersect1d(old_list, new_list)

    print(f"旧列表: {old_list}")
    print(f"新列表: {new_list}")
    print(f"新增: {added}")
    print(f"删除: {removed}")
    print(f"保留: {common}")

    # 示例 3: 检查数据完整性
    print("\n示例 3: 检查必需字段是否存在")
    required = np.array(["name", "email", "phone"])
    provided = np.array(["name", "email", "address"])

    missing = np.setdiff1d(required, provided)
    print(f"必需字段: {required}")
    print(f"已提供: {provided}")
    print(f"缺失: {missing}")

    # 示例 4: 分类统计
    print("\n示例 4: 统计类别出现次数")
    data = np.array(["A", "B", "A", "C", "B", "A", "D", "A"])
    unique, counts = np.unique(data, return_counts=True)

    print(f"数据: {data}")
    print("\n类别统计:")
    for category, count in zip(unique, counts):
        print(f"  {category}: {count} 次")

    # 示例 5: 集合运算链
    print("\n示例 5: 多集合运算")
    A = np.array([1, 2, 3, 4, 5])
    B = np.array([3, 4, 5, 6, 7])
    C = np.array([5, 6, 7, 8, 9])

    print(f"A: {A}")
    print(f"B: {B}")
    print(f"C: {C}")

    # (A ∪ B) ∩ C
    result = np.intersect1d(np.union1d(A, B), C)
    print(f"\n(A ∪ B) ∩ C: {result}")

    # (A \ B) ∪ (B \ A)
    result = np.union1d(np.setdiff1d(A, B), np.setdiff1d(B, A))
    print(f"(A \\ B) ∪ (B \\ A): {result}")

    # 示例 6: 查找唯一行
    print("\n示例 6: 2D 数组去重")
    arr_2d = np.array([[1, 2], [3, 4], [1, 2], [5, 6], [3, 4]])
    print(f"原始 2D 数组:\n{arr_2d}")

    unique_rows = np.unique(arr_2d, axis=0)
    print(f"\n唯一行:\n{unique_rows}")

    # 示例 7: 数据验证
    print("\n示例 7: 验证数据是否在有效范围内")
    valid_values = np.array([1, 5, 10, 20, 50])
    input_data = np.array([1, 2, 5, 15, 20, 100])

    is_valid = np.in1d(input_data, valid_values)
    print(f"有效值: {valid_values}")
    print(f"输入数据: {input_data}")
    print(f"是否有效: {is_valid}")
    print(f"无效输入: {input_data[~is_valid]}")

    print("\n" + "=" * 70)
    print("9. 性能提示")
    print("=" * 70)

    print("""
性能提示：

1. unique + return_counts 比 collections.Counter 快
2. in1d 比 Python 的 set() 更快
3. 对于大数据，考虑使用 sort + unique
4. 交集/并集/差集操作会自动排序结果
5. 重复操作时，考虑先排序

最佳实践：

1. 使用 unique 而不是手动去重
2. 使用 in1d 而不是循环检查
3. 使用 return_index 追踪原始位置
4. 使用 return_counts 进行频率统计
5. 对于 2D 数组，明确指定 axis
""")


if __name__ == "__main__":
    main()
