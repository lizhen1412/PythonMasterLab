#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 50：Extension Types - 扩展类型与自定义访问器。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/50_extension_types.py

Pandas 支持创建自定义扩展类型和访问器，用于扩展 DataFrame/Series 的功能。

本节演示：
1. 注册自定义 DataFrame 访问器
2. 注册自定义 Series 访问器
3. 创建简单的扩展数组类型
4. 使用扩展类型进行类型安全操作
"""

from __future__ import annotations

import pandas as pd
from pandas.api.extensions import register_dataframe_accessor, register_series_accessor
from typing import Iterable


# ============================================================================
# 1. 注册自定义 DataFrame 访问器
# ============================================================================

@register_dataframe_accessor("stats")
class StatisticsAccessor:
    """为 DataFrame 添加统计分析访问器。"""

    def __init__(self, pandas_obj: pd.DataFrame) -> None:
        self._obj = pandas_obj

    def summary(self) -> pd.DataFrame:
        """返回数值列的统计摘要。"""
        numeric_cols = self._obj.select_dtypes(include=["number"]).columns
        if len(numeric_cols) == 0:
            return pd.DataFrame()

        result = pd.DataFrame(
            {
                "mean": self._obj[numeric_cols].mean(),
                "median": self._obj[numeric_cols].median(),
                "std": self._obj[numeric_cols].std(),
                "min": self._obj[numeric_cols].min(),
                "max": self._obj[numeric_cols].max(),
            }
        )
        return result

    def outliers(self, n_std: float = 3.0) -> dict[str, list[str]]:
        """检测各列中的异常值（超过 n_std 倍标准差）。"""
        numeric_cols = self._obj.select_dtypes(include=["number"]).columns
        outliers_dict = {}

        for col in numeric_cols:
            mean = self._obj[col].mean()
            std = self._obj[col].std()
            mask = (self._obj[col] < mean - n_std * std) | (
                self._obj[col] > mean + n_std * std
            )
            outlier_indices = self._obj[mask].index.tolist()
            if outlier_indices:
                outliers_dict[col] = outlier_indices

        return outliers_dict


# ============================================================================
# 2. 注册自定义 Series 访问器
# ============================================================================

@register_series_accessor("text")
class TextAccessor:
    """为 Series (字符串类型) 添加文本处理访问器。"""

    def __init__(self, pandas_obj: pd.Series) -> None:
        self._validate(pandas_obj)
        self._obj = pandas_obj

    @staticmethod
    def _validate(obj: pd.Series) -> None:
        """验证对象是否为字符串类型。"""
        if not pd.api.types.is_string_dtype(obj):
            raise AttributeError("text 访问器仅支持字符串类型的 Series")

    def word_count(self) -> pd.Series:
        """计算每个元素的单词数。"""
        return self._obj.str.split().str.len()

    def avg_word_length(self) -> float:
        """计算平均单词长度。"""
        words = self._obj.str.split().explode()
        return words.str.len().mean()

    def has_pattern(self, pattern: str, case_sensitive: bool = False) -> pd.Series:
        """检查是否包含指定模式。"""
        flags = 0 if case_sensitive else False
        return self._obj.str.contains(pattern, case=case_sensitive, regex=True)


# ============================================================================
# 3. 创建简单的扩展数组类型
# ============================================================================

class ListDtype(pd.api.extensions.ExtensionDtype):
    """存储列表的扩展数据类型。"""

    name = "list"
    type = list
    na_value = None

    @classmethod
    def construct_array_type(cls) -> type[ListArray]:
        return ListArray


class ListArray(pd.api.extensions.ExtensionArray):
    """存储列表的扩展数组。"""

    def __init__(self, values: Iterable[list | None]) -> None:
        self._data = list(values)

    def __getitem__(self, index: int | slice) -> list | ListArray:
        if isinstance(index, int):
            return self._data[index]
        return ListArray(self._data[index])

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"ListArray({self._data})"

    def isna(self) -> pd.Series:
        """检测缺失值。"""
        return pd.Series([v is None for v in self._data])

    def take_nd(self, indices, **kwargs):
        """按索引取值。"""
        return ListArray([self._data[i] for i in indices])

    @property
    def dtype(self) -> ListDtype:
        return ListDtype()

    @classmethod
    def _from_sequence(cls, scalars, dtype=None, copy=False):
        return ListArray(scalars)

    @classmethod
    def _from_factorized(cls, values, original):
        return ListArray(values)

    def _validate_list(self, value):
        if not isinstance(value, (list, type(None))):
            raise ValueError(f"ListArray 只能存储列表或 None，得到 {type(value)}")


# ============================================================================
# 主函数演示
# ============================================================================

def main() -> None:
    print("=" * 60)
    print("1. 自定义 DataFrame 访问器")
    print("=" * 60)

    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
            "age": [25, 30, 35, 100, 28],  # 100 是异常值
            "salary": [50000, 60000, 70000, 50000, 55000],
        }
    )
    print("\n原始数据:")
    print(df)

    print("\n使用 stats.accessor 获取统计摘要:")
    print(df.stats.summary())

    print("\n使用 stats.accessor 检测异常值:")
    outliers = df.stats.outliers(n_std=2.0)
    for col, indices in outliers.items():
        print(f"  {col}: {indices}")

    print("\n" + "=" * 60)
    print("2. 自定义 Series 访问器")
    print("=" * 60)

    text_series = pd.Series(
        ["Hello world", "Pandas is great", "Python data analysis", "Data science"]
    )
    print("\n原始文本数据:")
    print(text_series)

    print("\n使用 text.accessor 计算单词数:")
    print(text_series.text.word_count())

    print("\n使用 text.accessor 计算平均单词长度:")
    avg_len = text_series.text.avg_word_length()
    print(f"平均单词长度: {avg_len:.2f}")

    print("\n使用 text.accessor 检查包含 'data' 模式:")
    print(text_series.text.has_pattern("data", case_sensitive=False))

    print("\n" + "=" * 60)
    print("3. 扩展数组类型")
    print("=" * 60)

    # 创建包含列表的 Series
    list_series = pd.Series(
        [[1, 2, 3], [4, 5], None, [6, 7, 8, 9]],
        dtype=object,
    )
    print("\n包含列表的 Series:")
    print(list_series)

    print("\n检测缺失值:")
    print(pd.isna(list_series))

    print("\n计算每个列表的长度:")
    print(list_series.apply(lambda x: len(x) if x is not None else 0))

    print("\n" + "=" * 60)
    print("4. 链式访问器操作")
    print("=" * 60)

    # 创建一个包含文本和数值的 DataFrame
    df2 = pd.DataFrame(
        {
            "product": ["Apple iPhone", "Samsung Galaxy", "Google Pixel", "OnePlus"],
            "description": [
                "Premium smartphone with great camera",
                "Android flagship with amazing display",
                "Pure Android experience",
                "Fast performance good value",
            ],
            "price": [999, 899, 699, 799],
        }
    )

    print("\n产品数据:")
    print(df2)

    print("\n使用自定义访问器分析:")
    print(f"平均描述单词数: {df2['description'].text.word_count().mean():.2f}")
    print(f"平均价格: {df2['price'].mean():.2f}")
    print(f"价格标准差: {df2['price'].std():.2f}")

    print("\n" + "=" * 60)
    print("5. 访问器在数据清洗中的应用")
    print("=" * 60)

    df3 = pd.DataFrame(
        {
            "text_col": ["  Hello  ", "World  ", "  Pandas  ", None, "  Data  "],
            "value_col": [1, 2, 3, 4, 5],
        }
    )

    print("\n原始数据:")
    print(df3)

    # 结合 str 访问器和自定义 text 访问器
    print("\n清洗后的文本:")
    cleaned = df3["text_col"].str.strip().str.lower()
    print(cleaned)

    print("\n清洗后每个文本的单词数:")
    cleaned_series = pd.Series(cleaned.dropna())
    print(cleaned_series.text.word_count())


if __name__ == "__main__":
    main()