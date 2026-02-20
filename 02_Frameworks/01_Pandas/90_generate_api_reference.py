#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 90：生成 pandas API 名称索引（需 pandas 2.3.3）。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/90_generate_api_reference.py
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import sys


def collect_public_names(obj: object) -> list[str]:
    return sorted({name for name in dir(obj) if not name.startswith("_")})


def collect_module_names(module: object) -> list[str]:
    names = getattr(module, "__all__", None)
    if names:
        return sorted(set(names))
    return collect_public_names(module)


def add_section(sections: list[tuple[str, list[str]]], title: str, names: list[str]) -> None:
    sections.append((title, sorted(set(names))))


def main() -> None:
    try:
        import pandas as pd
    except Exception as exc:
        print("未安装 pandas 或导入失败 ->", exc)
        print("请先安装：pip install pandas==2.3.3")
        sys.exit(1)

    expected = "2.3.3"
    if pd.__version__ != expected:
        print(f"警告：建议版本 {expected}，当前 {pd.__version__}")

    df = pd.DataFrame(
        {
            "group": ["A", "A", "B", "B"],
            "value": [1, 2, 3, 4],
            "text": ["foo", "bar", "baz", "qux"],
            "time": pd.date_range("2024-01-01", periods=4, freq="D"),
        }
    )
    series = df["value"]

    grouped_df = df.groupby("group")
    grouped_series = df.groupby("group")["value"]
    resampler = df.set_index("time")["value"].resample("D")

    rolling = series.rolling(window=2)
    expanding = series.expanding()
    ewm = series.ewm(alpha=0.5)

    str_accessor = df["text"].str
    dt_accessor = df["time"].dt
    td_accessor = pd.Series(pd.to_timedelta([1, 2, 3], unit="D")).dt
    cat_accessor = pd.Series(["a", "b", "a"], dtype="category").cat

    sections: list[tuple[str, list[str]]] = []

    add_section(sections, "pandas 模块公开名称", collect_module_names(pd))
    add_section(sections, "pandas.api", collect_module_names(pd.api))
    add_section(sections, "pandas.api.types", collect_module_names(pd.api.types))
    add_section(sections, "pandas.api.extensions", collect_module_names(pd.api.extensions))
    add_section(sections, "pandas.arrays", collect_module_names(pd.arrays))
    add_section(sections, "pandas.errors", collect_module_names(pd.errors))
    add_section(sections, "pandas.testing", collect_module_names(pd.testing))

    add_section(sections, "DataFrame", collect_public_names(pd.DataFrame()))
    add_section(sections, "Series", collect_public_names(pd.Series([1])))

    add_section(sections, "Index", collect_public_names(pd.Index([1, 2, 3])))
    add_section(
        sections,
        "MultiIndex",
        collect_public_names(
            pd.MultiIndex.from_product([["A", "B"], [1, 2]], names=["g", "id"])
        ),
    )
    add_section(sections, "RangeIndex", collect_public_names(pd.RangeIndex(0, 5)))
    add_section(
        sections, "DatetimeIndex", collect_public_names(pd.date_range("2024-01-01", periods=3))
    )
    add_section(
        sections,
        "TimedeltaIndex",
        collect_public_names(pd.to_timedelta([1, 2, 3], unit="D")),
    )
    add_section(
        sections,
        "PeriodIndex",
        collect_public_names(pd.period_range("2024-01", periods=3, freq="M")),
    )
    add_section(
        sections,
        "CategoricalIndex",
        collect_public_names(pd.CategoricalIndex(["a", "b", "a"])),
    )

    add_section(sections, "Categorical", collect_public_names(pd.Categorical(["a", "b"])))

    add_section(sections, "DataFrameGroupBy", collect_public_names(grouped_df))
    add_section(sections, "SeriesGroupBy", collect_public_names(grouped_series))

    add_section(sections, "Resampler", collect_public_names(resampler))
    add_section(sections, "Rolling", collect_public_names(rolling))
    add_section(sections, "Expanding", collect_public_names(expanding))
    add_section(sections, "EWM", collect_public_names(ewm))

    add_section(sections, "StringMethods (Series.str)", collect_public_names(str_accessor))
    add_section(sections, "DatetimeProperties (Series.dt)", collect_public_names(dt_accessor))
    add_section(sections, "TimedeltaProperties (Series.dt)", collect_public_names(td_accessor))
    add_section(sections, "CategoricalAccessor (Series.cat)", collect_public_names(cat_accessor))

    output = Path(__file__).with_name("91_api_reference.md")
    lines: list[str] = [
        "# Pandas 2.3.3 API 名称索引",
        "",
        f"生成时间: {datetime.now().isoformat(timespec='seconds')}",
        f"pandas 版本: {pd.__version__}",
        "",
        "说明：本文件由脚本自动生成，仅提供名称索引，便于查找。",
        "",
    ]

    for title, names in sections:
        lines.append(f"## {title}")
        lines.append(f"共 {len(names)} 项")
        lines.append("")
        if names:
            lines.extend([f"- `{name}`" for name in names])
        else:
            lines.append("_无公开名称_")
        lines.append("")

    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"已生成 -> {output}")


if __name__ == "__main__":
    main()