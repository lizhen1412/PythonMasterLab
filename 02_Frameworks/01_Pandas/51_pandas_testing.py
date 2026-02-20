#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 51：Pandas Testing - 测试工具。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/51_pandas_testing.py

Pandas 提供了专门的测试工具模块 `pandas.testing`，用于断言和比较
DataFrame、Series、Index 等对象。这些工具在编写测试或验证数据时非常有用。

本节演示：
1. assert_frame_equal - 断言 DataFrame 相等
2. assert_series_equal - 断言 Series 相等
3. assert_index_equal - 断言 Index 相等
4. assert_extension_array_equal - 断言扩展数组相等
5. 处理不同的比较选项（dtype、order、精度等）
"""

from __future__ import annotations

import pandas as pd
import numpy as np
import pandas.testing as tm


# ============================================================================
# 测试辅助函数
# ============================================================================

def test_frame_equal() -> None:
    """演示 DataFrame 相等性测试。"""
    print("\n1. assert_frame_equal 基本用法:")

    df1 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    df2 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    df3 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 7]})  # 不同

    # 相等的 DataFrame - 不会抛出异常
    try:
        tm.assert_frame_equal(df1, df2)
        print("   df1 和 df2 相等: 通过")
    except AssertionError as e:
        print(f"   df1 和 df2 不相等: {e}")

    # 不相等的 DataFrame - 会抛出异常
    try:
        tm.assert_frame_equal(df1, df3)
        print("   df1 和 df3 相等: 通过")
    except AssertionError as e:
        print(f"   df1 和 df3 不相等: 检测到差异")


def test_series_equal() -> None:
    """演示 Series 相等性测试。"""
    print("\n2. assert_series_equal 基本用法:")

    s1 = pd.Series([1, 2, 3], index=["a", "b", "c"])
    s2 = pd.Series([1, 2, 3], index=["a", "b", "c"])
    s3 = pd.Series([1, 2, 3], index=["a", "c", "b"])  # 顺序不同

    # 相等的 Series
    try:
        tm.assert_series_equal(s1, s2)
        print("   s1 和 s2 相等: 通过")
    except AssertionError as e:
        print(f"   s1 和 s2 不相等: {e}")

    # 顺序不同的 Series
    try:
        tm.assert_series_equal(s1, s3)
        print("   s1 和 s3 相等: 通过")
    except AssertionError as e:
        print("   s1 和 s3 不相等: 检测到索引顺序差异")

    # 使用 check_like=False 忽略顺序
    try:
        tm.assert_series_equal(s1, s3, check_like=False)
        print("   s1 和 s3 相等（忽略顺序）: 通过")
    except AssertionError:
        print("   s1 和 s3 不相等（忽略顺序）: 仍有差异")


def test_index_equal() -> None:
    """演示 Index 相等性测试。"""
    print("\n3. assert_index_equal 基本用法:")

    idx1 = pd.Index([1, 2, 3])
    idx2 = pd.Index([1, 2, 3])
    idx3 = pd.Index([1, 2, 4])

    try:
        tm.assert_index_equal(idx1, idx2)
        print("   idx1 和 idx2 相等: 通过")
    except AssertionError as e:
        print(f"   idx1 和 idx2 不相等: {e}")

    try:
        tm.assert_index_equal(idx1, idx3)
        print("   idx1 和 idx3 相等: 通过")
    except AssertionError:
        print("   idx1 和 idx3 不相等: 检测到差异")


def test_dtype_handling() -> None:
    """演示 dtype 处理选项。"""
    print("\n4. dtype 检查选项:")

    # 创建数据相同但 dtype 不同的 DataFrame
    df_int = pd.DataFrame({"a": [1, 2, 3]}, dtype=np.int64)
    df_float = pd.DataFrame({"a": [1.0, 2.0, 3.0]}, dtype=np.float64)

    print(f"   df_int dtype: {df_int['a'].dtype}")
    print(f"   df_float dtype: {df_float['a'].dtype}")

    # 严格检查 dtype - 会失败
    try:
        tm.assert_frame_equal(df_int, df_float, check_dtype=True)
        print("   相等（检查 dtype）: 通过")
    except AssertionError:
        print("   不相等（检查 dtype）: dtype 不同")

    # 忽略 dtype - 会通过
    try:
        tm.assert_frame_equal(df_int, df_float, check_dtype=False)
        print("   相等（忽略 dtype）: 通过")
    except AssertionError:
        print("   不相等（忽略 dtype）: 仍有差异")


def test_precision_handling() -> None:
    """演示精度处理选项。"""
    print("\n5. 精度检查选项:")

    df1 = pd.DataFrame({"a": [1.0, 2.0, 3.0]})
    df2 = pd.DataFrame({"a": [1.0001, 2.0001, 3.0001]})

    print(f"   df1: {df1['a'].tolist()}")
    print(f"   df2: {df2['a'].tolist()}")

    # 默认精度检查 - 可能失败
    try:
        tm.assert_frame_equal(df1, df2)
        print("   相等（默认精度）: 通过")
    except AssertionError:
        print("   不相等（默认精度）: 检测到微小差异")

    # 使用更宽松的精度
    try:
        tm.assert_frame_equal(df1, df2, atol=0.001)
        print("   相等（atol=0.001）: 通过")
    except AssertionError:
        print("   不相等（atol=0.001）: 差异超出容差")


def test_nan_handling() -> None:
    """演示 NaN 处理选项。"""
    print("\n6. NaN 处理选项:")

    df1 = pd.DataFrame({"a": [1, np.nan, 3]})
    df2 = pd.DataFrame({"a": [1, np.nan, 3]})
    df3 = pd.DataFrame({"a": [1, 2, 3]})

    # NaN 相等性检查
    try:
        tm.assert_frame_equal(df1, df2)
        print("   df1 和 df2 相等（包含 NaN）: 通过")
    except AssertionError:
        print("   df1 和 df2 不相等（包含 NaN）")

    # 比较有 NaN 和无 NaN
    try:
        tm.assert_frame_equal(df1, df3)
        print("   df1 和 df3 相等: 通过")
    except AssertionError:
        print("   df1 和 df3 不相等: NaN vs 实际值")


def test_column_order() -> None:
    """演示列顺序处理选项。"""
    print("\n7. 列顺序检查选项:")

    df1 = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
    df2 = pd.DataFrame({"c": [5, 6], "a": [1, 2], "b": [3, 4]})

    # 检查列顺序
    try:
        tm.assert_frame_equal(df1, df2, check_like=True)
        print("   相等（忽略列顺序）: 通过")
    except AssertionError:
        print("   不相等（忽略列顺序）: 仍有差异")


def test_real_world_validation() -> None:
    """真实场景：数据验证。"""
    print("\n8. 真实场景 - 数据验证:")

    # 原始数据
    original = pd.DataFrame(
        {
            "id": [1, 2, 3, 4],
            "name": ["Alice", "Bob", "Charlie", "David"],
            "score": [85.5, 92.0, 78.5, 88.0],
        }
    )

    # 处理后的数据（假设经过某些转换）
    processed = pd.DataFrame(
        {
            "id": [1, 2, 3, 4],
            "name": ["Alice", "Bob", "Charlie", "David"],
            "score": [85.5, 92.0, 78.5, 88.0],
        }
    )

    print("   验证处理前后数据一致性:")
    try:
        tm.assert_frame_equal(original, processed)
        print("   验证通过: 数据完全一致")
    except AssertionError as e:
        print(f"   验证失败: 数据有差异\n{e}")

    # 场景：验证数据清洗后的预期结果
    dirty = pd.DataFrame({"value": ["  42  ", " 100 ", "  50  "]})
    expected = pd.DataFrame({"value": [42, 100, 50]}, dtype=np.int64)

    # 模拟清洗
    cleaned = pd.DataFrame({"value": dirty["value"].str.strip().astype(int)})

    print("\n   验证数据清洗结果:")
    try:
        tm.assert_frame_equal(cleaned, expected)
        print("   清洗验证通过: 结果符合预期")
    except AssertionError as e:
        print(f"   清洗验证失败: {e}")


def test_comparison_utilities() -> None:
    """演示比较相关的实用工具。"""
    print("\n9. 其他比较实用工具:")

    # 使用 frame_equal 作为条件检查（不抛出异常）
    df1 = pd.DataFrame({"a": [1, 2, 3]})
    df2 = pd.DataFrame({"a": [1, 2, 3]})
    df3 = pd.DataFrame({"a": [1, 2, 4]})

    # 使用 try-except 进行条件检查
    def frames_equal(df_left: pd.DataFrame, df_right: pd.DataFrame) -> bool:
        try:
            tm.assert_frame_equal(df_left, df_right)
            return True
        except AssertionError:
            return False

    print(f"   df1 == df2: {frames_equal(df1, df2)}")
    print(f"   df1 == df3: {frames_equal(df1, df3)}")

    # 比较多个数据框
    print("\n   比较多个数据框:")
    dfs = [df1, df2, df3]
    for i, df_a in enumerate(dfs):
        for j, df_b in enumerate(dfs[i + 1 :], i + 1):
            equal = frames_equal(df_a, df_b)
            print(f"   df{i+1} vs df{j+1}: {'相等' if equal else '不相等'}")


# ============================================================================
# 主函数
# ============================================================================

def main() -> None:
    print("=" * 60)
    print("Pandas Testing 模块演示")
    print("=" * 60)

    test_frame_equal()
    test_series_equal()
    test_index_equal()
    test_dtype_handling()
    test_precision_handling()
    test_nan_handling()
    test_column_order()
    test_real_world_validation()
    test_comparison_utilities()

    print("\n" + "=" * 60)
    print("提示: pandas.testing 主要用于单元测试，在生产代码中使用")
    print("      可以验证数据处理管道的正确性。")
    print("=" * 60)


if __name__ == "__main__":
    main()