#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：pandas 2.3.3 学习索引。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/01_Pandas/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_install_and_version.py", "安装与版本检查"),
    ("03_series_basics.py", "Series 基础"),
    ("04_dataframe_basics.py", "DataFrame 基础"),
    ("05_index_and_columns.py", "Index 与列名管理"),
    ("06_select_loc_iloc.py", "loc/iloc/at/iat 选择"),
    ("07_boolean_filter_query.py", "条件过滤与 query"),
    ("08_missing_values.py", "缺失值处理"),
    ("09_dtypes_and_convert.py", "类型与转换"),
    ("10_vectorized_ops_alignment.py", "向量化与对齐"),
    ("11_apply_map_replace.py", "apply/map/replace"),
    ("12_string_methods.py", "字符串处理"),
    ("13_datetime_timedelta.py", "时间与时间差"),
    ("14_sort_rank.py", "排序与排名"),
    ("15_groupby_agg_transform.py", "分组聚合"),
    ("16_pivot_melt_stack.py", "透视与重塑"),
    ("17_merge_join_concat.py", "合并/连接/拼接"),
    ("18_window_rolling_ewm.py", "窗口函数"),
    ("19_categorical.py", "类别数据"),
    ("20_multiindex.py", "多级索引"),
    ("21_io_csv_json.py", "CSV/JSON I/O"),
    ("22_io_pickle_excel_optional.py", "Pickle/Excel（可选依赖）"),
    ("23_time_series_resample.py", "时间序列重采样"),
    ("24_performance_tips.py", "性能与最佳实践"),
    ("25_chapter_summary.py", "本章总结"),
    ("26_data_cleaning_columns.py", "数据清洗与列操作"),
    ("27_missing_values_advanced.py", "缺失值处理进阶"),
    ("28_stats_summary.py", "统计概览与对比"),
    ("29_index_align_reindex.py", "索引对齐与重建"),
    ("30_reshape_encoding.py", "重塑与编码"),
    ("31_groupby_advanced.py", "groupby 进阶"),
    ("32_time_series_advanced.py", "时间序列进阶"),
    ("33_io_csv_json_excel_advanced.py", "I/O 进阶"),
    ("34_io_other_formats_sql_optional.py", "其他格式与 SQL"),
    ("35_interop_nullable.py", "互操作与可空类型"),
    ("36_display_style_plot.py", "展示与样式"),
    ("37_eval_query_pipe.py", "eval/query/pipe"),
    ("38_settingwithcopy.py", "SettingWithCopy"),
    ("39_selection_assignment.py", "选择与赋值"),
    ("40_merge_variants.py", "merge 细节"),
    ("41_time_series_slicing.py", "时间序列切片与时间窗口"),
    ("42_io_csv_realworld.py", "CSV 实战参数"),
    ("43_string_parse.py", "字符串解析与提取"),
    ("44_mini_project_sales.py", "小项目：从 CSV 到报表"),
    ("45_select_dtypes_numeric_only.py", "数值列选择与 numeric_only"),
    ("46_groupby_cumrank.py", "分组累计与排名"),
    ("47_cut_qcut.py", "分箱 cut/qcut"),
    ("48_datetime_formatting.py", "日期格式化"),
    ("49_io_csv_encoding.py", "CSV 编码与中文"),
    ("50_extension_types.py", "Extension Types - 扩展类型与自定义访问器"),
    ("51_pandas_testing.py", "Pandas Testing - 测试工具"),
    ("52_sparse_arrays.py", "Sparse Arrays - 稀疏数组"),
    ("53_options_api.py", "Options API - 全局选项配置"),
    ("54_plotting_advanced.py", "Advanced Plotting - 高级绘图"),
    ("55_dataframe_methods.py", "DataFrame Methods - nlargest/nsmallest/compare/factorize/sample"),
    ("56_resample_ohlc.py", "Resample OHLC - 金融数据重采样"),
    ("57_io_formats_extended.py", "Extended I/O - Feather/Parquet/Stata/SAS/JSONL"),
    ("58_special_io_formats.py", "Special I/O Formats - HDF5/XML/Clipboard/ExcelWriter"),
    ("59_complete_methods.py", "Complete Methods - corr/cov/rank/pct_change/shift/diff/expanding/explode/get_dummies"),
    ("60_grouper_advanced.py", "Grouper Advanced - 时间序列分组、多级分组"),
    ("61_period_advanced.py", "Period Advanced - Period 创建、运算、转换"),
    ("62_datetime_components.py", "DateTime Components - dt.* 方法和属性完整覆盖"),
    ("63_api_methods_complete.py", "API Methods Complete - clip/quantile/rank/mode/median/between"),
    ("64_crosstab_advanced.py", "Crosstab Advanced - 交叉表进阶、margins、normalize"),
    ("90_generate_api_reference.py", "生成 API 索引（需 pandas）"),
    ("Exercises/01_overview.py", "练习索引"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("示例文件清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()