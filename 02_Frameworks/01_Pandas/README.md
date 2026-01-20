# Pandas 2.3.3 学习笔记（01_Pandas）

本章面向小白，覆盖 pandas 2.3.3 的常见与核心用法：
- Series/DataFrame 基础
- 索引与切片、条件过滤
- 缺失值、类型转换
- 向量化运算、apply/map/replace
- 字符串与时间序列
- 分组聚合、透视与重塑
- 合并、连接、拼接
- 窗口函数与滚动计算
- 类别数据、多级索引
- CSV/JSON/Pickle 等 I/O

版本要求：`pandas==2.3.3`

安装：
- `pip install pandas==2.3.3`

可选依赖（演示中仅提示，不强制）：
- Excel: `openpyxl` / `xlsxwriter`
- Parquet/Feather: `pyarrow`（或 `fastparquet`）
- HDF: `tables`
- HTML: `lxml` / `beautifulsoup4`
- Plot: `matplotlib`

---

## 1) 怎么运行

在仓库根目录执行：

- 先看索引：`python3 02_Frameworks/01_Pandas/01_overview.py`
- 运行某个示例：`python3 02_Frameworks/01_Pandas/03_series_basics.py`
- 练习题索引：`python3 02_Frameworks/01_Pandas/Exercises/01_overview.py`

---

## 2) 知识点全景清单

- 安装与版本检查（必须为 2.3.3）
- Series / DataFrame 创建与基础属性
- Index 与列名管理
- `loc/iloc/at/iat` 选择
- 条件过滤与 `query`
- 缺失值处理 `isna/fillna/dropna`
- 类型转换 `astype/convert_dtypes/to_numeric/to_datetime`
- 向量化运算与对齐
- `map/apply/replace` 的区别
- 字符串处理 `str.*`
- 时间序列 `dt.*`、`date_range` 与 `resample`
- 排序、排名与 top-n
- `groupby` 聚合/转换
- 透视/宽长表转换 `pivot/melt/stack/unstack`
- 合并/连接/拼接 `merge/join/concat`
- 窗口计算 `rolling/expanding/ewm`
- 类别数据与 `category`
- 多级索引 `MultiIndex`
- I/O：CSV/JSON/PKL（Excel/Parquet 为可选依赖）
- 数据清洗与列操作（drop/assign/insert/pop/duplicated/where/mask/clip）
- 缺失值进阶（ffill/bfill/interpolate/dropna 细节）
- 统计概览（describe/value_counts/unique/nunique/quantile/corr/cov/compare）
- 索引对齐与重建（reindex/align/sort_index/Index 集合运算）
- 重塑与编码（get_dummies/explode/wide_to_long/crosstab/concat keys/pivot vs pivot_table）
- groupby 进阶（多键/命名聚合/apply vs transform/size vs count）
- 时间序列进阶（shift/diff/pct_change/tz_localize/to_period/merge_asof/resample 参数）
- I/O 进阶与大文件（read_csv 参数、chunksize、json_normalize、多 sheet Excel）
- 其他格式与 SQL/HTML/剪贴板（可选依赖）
- 互操作与导出（to_numpy/to_dict/to_records、可空类型）
- 展示与样式（set_option/Styler/plot）
- eval/query/pipe 与 SettingWithCopy
- 选择与赋值（[]/loc/assign/where）
- 合并细节（left_on/right_on/suffixes/indicator/validate）
- 时间序列切片与时间窗口（日期切片/rolling("7D")/between_time）
- CSV 实战参数（sep/index_col/na_values/parse_dates/na_rep/date_format）
- 字符串解析（str.split/str.extract）
- 小项目：从读入到报表（清洗/合并/汇总/导出）
- 数值列选择与 numeric_only（select_dtypes/mean）
- 分组累计与排名（cumsum/cumcount/rank）
- 分箱 cut/qcut（成绩分档/分位数）
- 日期格式化（dt.strftime）
- CSV 编码与中文（encoding）

---

## 3) 文件总览

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引 |
| 02 | [`02_install_and_version.py`](02_install_and_version.py) | 安装与版本检查 |
| 03 | [`03_series_basics.py`](03_series_basics.py) | Series 基础 |
| 04 | [`04_dataframe_basics.py`](04_dataframe_basics.py) | DataFrame 基础 |
| 05 | [`05_index_and_columns.py`](05_index_and_columns.py) | Index 与列名管理 |
| 06 | [`06_select_loc_iloc.py`](06_select_loc_iloc.py) | loc/iloc/at/iat |
| 07 | [`07_boolean_filter_query.py`](07_boolean_filter_query.py) | 条件过滤与 query |
| 08 | [`08_missing_values.py`](08_missing_values.py) | 缺失值处理 |
| 09 | [`09_dtypes_and_convert.py`](09_dtypes_and_convert.py) | 类型与转换 |
| 10 | [`10_vectorized_ops_alignment.py`](10_vectorized_ops_alignment.py) | 向量化与对齐 |
| 11 | [`11_apply_map_replace.py`](11_apply_map_replace.py) | apply/map/replace |
| 12 | [`12_string_methods.py`](12_string_methods.py) | 字符串处理 |
| 13 | [`13_datetime_timedelta.py`](13_datetime_timedelta.py) | 时间与时间差 |
| 14 | [`14_sort_rank.py`](14_sort_rank.py) | 排序与排名 |
| 15 | [`15_groupby_agg_transform.py`](15_groupby_agg_transform.py) | 分组聚合 |
| 16 | [`16_pivot_melt_stack.py`](16_pivot_melt_stack.py) | 透视与重塑 |
| 17 | [`17_merge_join_concat.py`](17_merge_join_concat.py) | 合并/连接/拼接 |
| 18 | [`18_window_rolling_ewm.py`](18_window_rolling_ewm.py) | 窗口函数 |
| 19 | [`19_categorical.py`](19_categorical.py) | 类别数据 |
| 20 | [`20_multiindex.py`](20_multiindex.py) | 多级索引 |
| 21 | [`21_io_csv_json.py`](21_io_csv_json.py) | CSV/JSON I/O |
| 22 | [`22_io_pickle_excel_optional.py`](22_io_pickle_excel_optional.py) | Pickle/Excel（可选依赖） |
| 23 | [`23_time_series_resample.py`](23_time_series_resample.py) | 时间序列重采样 |
| 24 | [`24_performance_tips.py`](24_performance_tips.py) | 性能与最佳实践 |
| 25 | [`25_chapter_summary.py`](25_chapter_summary.py) | 本章总结 |
| 26 | [`26_data_cleaning_columns.py`](26_data_cleaning_columns.py) | 数据清洗与列操作 |
| 27 | [`27_missing_values_advanced.py`](27_missing_values_advanced.py) | 缺失值处理进阶 |
| 28 | [`28_stats_summary.py`](28_stats_summary.py) | 统计概览与对比 |
| 29 | [`29_index_align_reindex.py`](29_index_align_reindex.py) | 索引对齐与重建 |
| 30 | [`30_reshape_encoding.py`](30_reshape_encoding.py) | 重塑与编码 |
| 31 | [`31_groupby_advanced.py`](31_groupby_advanced.py) | groupby 进阶 |
| 32 | [`32_time_series_advanced.py`](32_time_series_advanced.py) | 时间序列进阶 |
| 33 | [`33_io_csv_json_excel_advanced.py`](33_io_csv_json_excel_advanced.py) | I/O 进阶 |
| 34 | [`34_io_other_formats_sql_optional.py`](34_io_other_formats_sql_optional.py) | 其他格式与 SQL |
| 35 | [`35_interop_nullable.py`](35_interop_nullable.py) | 互操作与可空类型 |
| 36 | [`36_display_style_plot.py`](36_display_style_plot.py) | 展示与样式 |
| 37 | [`37_eval_query_pipe.py`](37_eval_query_pipe.py) | eval/query/pipe |
| 38 | [`38_settingwithcopy.py`](38_settingwithcopy.py) | SettingWithCopy |
| 39 | [`39_selection_assignment.py`](39_selection_assignment.py) | 选择与赋值 |
| 40 | [`40_merge_variants.py`](40_merge_variants.py) | merge 细节 |
| 41 | [`41_time_series_slicing.py`](41_time_series_slicing.py) | 时间序列切片与时间窗口 |
| 42 | [`42_io_csv_realworld.py`](42_io_csv_realworld.py) | CSV 实战参数 |
| 43 | [`43_string_parse.py`](43_string_parse.py) | 字符串解析与提取 |
| 44 | [`44_mini_project_sales.py`](44_mini_project_sales.py) | 小项目：从 CSV 到报表 |
| 45 | [`45_select_dtypes_numeric_only.py`](45_select_dtypes_numeric_only.py) | 数值列选择与 numeric_only |
| 46 | [`46_groupby_cumrank.py`](46_groupby_cumrank.py) | 分组累计与排名 |
| 47 | [`47_cut_qcut.py`](47_cut_qcut.py) | 分箱 cut/qcut |
| 48 | [`48_datetime_formatting.py`](48_datetime_formatting.py) | 日期格式化 |
| 49 | [`49_io_csv_encoding.py`](49_io_csv_encoding.py) | CSV 编码与中文 |
| 90 | [`90_generate_api_reference.py`](90_generate_api_reference.py) | 生成 API 索引（需 pandas） |
| 91 | [`91_api_reference.md`](91_api_reference.md) | API 索引输出文件 |
| 92 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | 练习索引 |

---

## 4) 本章练习（每题一个文件）

练习索引：`python3 02_Frameworks/01_Pandas/Exercises/01_overview.py`

- `Exercises/02_series_even_sum.py`：Series 过滤与求和
- `Exercises/03_select_rows_loc.py`：loc 选择行
- `Exercises/04_fillna_mean.py`：缺失值填充
- `Exercises/05_groupby_sales_sum.py`：分组汇总
- `Exercises/06_merge_users_orders.py`：合并表
- `Exercises/07_pivot_table_basic.py`：透视表
- `Exercises/08_resample_daily.py`：时间序列重采样
- `Exercises/09_string_cleaning.py`：字符串清洗
- `Exercises/10_io_csv_stringio.py`：CSV 读写
- `Exercises/11_drop_duplicates.py`：drop_duplicates 去重
- `Exercises/12_get_dummies_basic.py`：get_dummies 独热编码
- `Exercises/13_reindex_fill.py`：reindex + fill_value
- `Exercises/14_groupby_named_agg.py`：命名聚合
- `Exercises/15_shift_pct_change.py`：shift 与 pct_change
- `Exercises/16_json_normalize_basic.py`：json_normalize 展开

---

## 5) API 全量索引说明

由于本环境未安装 pandas，`91_api_reference.md` 为空模板。
在已安装 `pandas==2.3.3` 的环境中运行：

- `python3 02_Frameworks/01_Pandas/90_generate_api_reference.py`

会自动生成完整 API 名称索引（DataFrame/Series/Index/GroupBy/Resampler 等）。
