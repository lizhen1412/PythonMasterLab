#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习索引：pandas 2.3.3。

Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/01_Pandas/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_series_even_sum.py", "Series 过滤与求和"),
    ("03_select_rows_loc.py", "loc 选择行"),
    ("04_fillna_mean.py", "缺失值填充"),
    ("05_groupby_sales_sum.py", "分组汇总"),
    ("06_merge_users_orders.py", "合并表"),
    ("07_pivot_table_basic.py", "透视表"),
    ("08_resample_daily.py", "时间序列重采样"),
    ("09_string_cleaning.py", "字符串清洗"),
    ("10_io_csv_stringio.py", "CSV 读写"),
    ("11_drop_duplicates.py", "去重 drop_duplicates"),
    ("12_get_dummies_basic.py", "get_dummies 独热编码"),
    ("13_reindex_fill.py", "reindex + fill_value"),
    ("14_groupby_named_agg.py", "命名聚合"),
    ("15_shift_pct_change.py", "shift 与 pct_change"),
    ("16_json_normalize_basic.py", "json_normalize 展开"),
    # 高级练习 (17-24)
    ("17_grouper_monthly.py", "Grouper 按月分组"),
    ("18_period_conversion.py", "Period 转换"),
    ("19_datetime_filter.py", "DateTime 组件过滤"),
    ("20_clip_outliers.py", "clip 处理异常值"),
    ("21_quantile_binning.py", "quantile 分箱"),
    ("22_crosstab_analysis.py", "crosstab 交叉分析"),
    ("23_sparse_array.py", "稀疏数组"),
    ("24_interval_operations.py", "Interval 操作"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("练习文件清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()
