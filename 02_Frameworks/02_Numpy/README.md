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
- **新增**: FFT（快速傅里叶变换、频谱分析、信号滤波）
- **新增**: Polynomial（多项式运算、拟合、求根、切比雪夫/勒让德）
- **新增**: Masked Arrays（掩码数组、缺失值处理）
- **新增**: Financial（金融函数、货币时间价值、IRR/NPV）
- **新增**: Performance（einsum、nditer、性能优化）
- **新增**: Signal Processing（convolve/correlate/gradient/trapz/diff）
- **新增**: Histogram & Digitize（直方图/bincount/digitize）
- **新增**: Memmap（内存映射文件）
- **新增**: Structured Arrays（结构化数组）
- **新增**: Advanced Indexing（ix_/mgrid/ogrid/select/choose）
- **新增**: Linear Algebra Advanced（QR/Schur/Cholesky/伪逆/条件数）
- **新增**: FFT Advanced（rfft/rfft2/窗函数/零填充）
- **新增**: Ufunc Advanced（outer/at/reduceat/accumulate/自定义）
- **新增**: DateTime64（datetime64/timedelta64 完整操作）

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
| 18 | [`18_fft_basics.py`](18_fft_basics.py) | FFT - 快速傅里叶变换 |
| 19 | [`19_polynomial.py`](19_polynomial.py) | Polynomial - 多项式运算 |
| 20 | [`20_masked_arrays.py`](20_masked_arrays.py) | Masked Arrays - 掩码数组 |
| 21 | [`21_financial.py`](21_financial.py) | Financial - 金融函数 |
| 22 | [`22_performance_optimization.py`](22_performance_optimization.py) | Performance - 性能优化 |
| 23 | [`23_signal_processing.py`](23_signal_processing.py) | Signal Processing - 信号处理 |
| 24 | [`24_histogram_digitize.py`](24_histogram_digitize.py) | Histogram & Digitize - 直方图与分箱 |
| 25 | [`25_memmap.py`](25_memmap.py) | Memmap - 内存映射文件 |
| 26 | [`26_structured_arrays.py`](26_structured_arrays.py) | Structured Arrays - 结构化数组 |
| 27 | [`27_advanced_indexing.py`](27_advanced_indexing.py) | Advanced Indexing - 高级索引 |
| 28 | [`28_numpy_complete.py`](28_numpy_complete.py) | NumPy Complete - einsum/pad/char/corrcoef/interp/trim_zeros |
| 29 | [`29_linalg_advanced.py`](29_linalg_advanced.py) | Linear Algebra Advanced - QR/Schur/Cholesky/伪逆/条件数 |
| 30 | [`30_fft_advanced.py`](30_fft_advanced.py) | FFT Advanced - rfft/rfft2/窗函数/零填充 |
| 31 | [`31_ufunc_advanced.py`](31_ufunc_advanced.py) | Ufunc Advanced - outer/at/reduceat/accumulate/自定义 |
| 32 | [`32_datetime64.py`](32_datetime64.py) | DateTime64 - datetime64/timedelta64 完整操作 |
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
- `Exercises/09_einsum.py`：einsum 矩阵运算
- `Exercises/10_fft_filter.py`：FFT 频谱分析
- `Exercises/11_outer_product.py`：ufunc.outer 外积
- `Exercises/12_qr_decomposition.py`：QR 分解
- `Exercises/13_datetime_diff.py`：datetime64 运算
- `Exercises/14_accumulate.py`：ufunc.accumulate
- `Exercises/15_structured_array.py`：结构化数组
