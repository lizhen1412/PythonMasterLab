# NumPy 2.4.0 学习笔记（02_Numpy）

本章面向小白，覆盖 numpy 2.4.0 的常见与核心用法：
- 数组创建、shape/dtype 基础
- 索引、切片、布尔/花式索引
- reshape/transpose 与视图/拷贝
- 广播与向量化运算
- 聚合统计与 axis
- NaN/Inf 处理
- 排序、去重、searchsorted
- 拼接与拆分
- 随机数（可重复）
- 线性代数
- 保存/读取（内存 I/O）
- ufunc 与 where/clip

版本要求：`numpy==2.4.0`

安装：
- `pip install numpy==2.4.0`

---

## 1) 怎么运行

在仓库根目录执行：

- 先看索引：`python3 02_Frameworks/02_Numpy/01_overview.py`
- 运行某个示例：`python3 02_Frameworks/02_Numpy/03_array_basics.py`
- 练习题索引：`python3 02_Frameworks/02_Numpy/Exercises/01_overview.py`

---

## 2) 知识点全景清单

- 安装与版本检查（建议 2.4.0）
- ndarray 创建：`array/arange/zeros/ones`
- `shape/ndim/size/dtype` 基本属性
- 索引与切片：行列选择、步长、负索引
- 布尔索引与花式索引
- `reshape/ravel/transpose/swapaxes`
- 广播规则与向量化运算
- 聚合：`sum/mean/min/max/argmax` 与 `axis`
- NaN/Inf 处理：`isnan/isfinite/nanmean/where`
- 排序/去重：`sort/argsort/unique/searchsorted`
- 拼接/拆分：`concatenate/stack/split`
- 随机数：`default_rng`、可重复抽样
- 线性代数：`dot/@/linalg.solve/norm`
- I/O：`save/load`、`savetxt/loadtxt`（内存）
- 视图与拷贝：`slice` vs `copy`
- ufunc 与条件：`where/clip/sqrt`

---

## 3) 文件总览

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引 |
| 02 | [`02_install_and_version.py`](02_install_and_version.py) | 安装与版本检查 |
| 03 | [`03_array_basics.py`](03_array_basics.py) | 数组创建与基础属性 |
| 04 | [`04_index_slice.py`](04_index_slice.py) | 索引与切片 |
| 05 | [`05_boolean_fancy_index.py`](05_boolean_fancy_index.py) | 布尔/花式索引与 where |
| 06 | [`06_reshape_transpose.py`](06_reshape_transpose.py) | reshape 与转置 |
| 07 | [`07_broadcasting_ops.py`](07_broadcasting_ops.py) | 广播与向量化运算 |
| 08 | [`08_aggregation_axis.py`](08_aggregation_axis.py) | 聚合与 axis |
| 09 | [`09_nan_inf_handling.py`](09_nan_inf_handling.py) | NaN/Inf 处理 |
| 10 | [`10_sort_unique.py`](10_sort_unique.py) | 排序/去重/searchsorted |
| 11 | [`11_stack_split.py`](11_stack_split.py) | 拼接与拆分 |
| 12 | [`12_random_sampling.py`](12_random_sampling.py) | 随机数（可重复） |
| 13 | [`13_linear_algebra.py`](13_linear_algebra.py) | 线性代数入门 |
| 14 | [`14_io_save_load.py`](14_io_save_load.py) | 保存/读取（内存 I/O） |
| 15 | [`15_views_copies.py`](15_views_copies.py) | 视图与拷贝 |
| 16 | [`16_vectorize_ufunc.py`](16_vectorize_ufunc.py) | ufunc 与条件处理 |
| 17 | [`17_chapter_summary.py`](17_chapter_summary.py) | 本章总结 |
| 90 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | 练习索引 |

---

## 4) 本章练习（每题一个文件）

练习索引：`python3 02_Frameworks/02_Numpy/Exercises/01_overview.py`

- `Exercises/02_arange_reshape.py`：arange + reshape
- `Exercises/03_mask_even.py`：布尔过滤
- `Exercises/04_broadcast_add_row.py`：广播相加
- `Exercises/05_mean_axis0.py`：按列均值
- `Exercises/06_fill_nan_mean.py`：NaN 均值填充
- `Exercises/07_stack_columns.py`：列拼接
- `Exercises/08_dot_product.py`：向量点积
