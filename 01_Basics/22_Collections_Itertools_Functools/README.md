# Python 3.11+ collections / itertools / functools 学习笔记（第 22 章）

本章聚焦标准库中的三大“效率工具箱”：
- `collections`：更专业的数据结构（deque/Counter/defaultdict/ChainMap/namedtuple）
- `itertools`：迭代组合的积木（链式、切片、组合、分组、流式）
- `functools`：函数工具（partial/wraps/cache/singledispatch/reduce）

---

## 1) 怎么运行

在仓库根目录执行：

- 先看索引：`python3 01_Basics/22_Collections_Itertools_Functools/01_overview.py`
- 运行某个示例：`python3 01_Basics/22_Collections_Itertools_Functools/03_collections_counter.py`
- 练习题索引：`python3 01_Basics/22_Collections_Itertools_Functools/Exercises/01_overview.py`

---

## 2) 本章“知识点全景”清单

### 2.1 collections

- `deque`：两端 O(1) 的追加/弹出，适合队列与滑动窗口
- `Counter`：计数、频率统计、`most_common`、加减合并
- `defaultdict`：自动创建默认值（分组、计数更省心）
- `ChainMap`：多层字典合并视图（配置覆盖）
- `namedtuple`：轻量不可变记录类型

### 2.2 itertools

- 基本积木：`count`/`repeat`/`cycle`/`chain`/`islice`
- 组合：`product`/`permutations`/`combinations`
- 分组：`groupby`（常见坑：必须先按 key 排序）
- 其他常用：`accumulate`/`pairwise`/`zip_longest`

### 2.3 functools

- `partial`：固定部分参数，创建新函数
- `wraps`：装饰器保留原函数元信息
- `cache/lru_cache`：记忆化优化递归与纯函数
- `singledispatch`：按参数类型分发
- `reduce`/`cmp_to_key`：聚合与自定义排序

---

## 3) 文件总览

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出全部示例与主题 |
| 02 | [`02_collections_deque.py`](02_collections_deque.py) | deque：双端队列与滑动窗口 |
| 03 | [`03_collections_counter.py`](03_collections_counter.py) | Counter：计数与频率统计 |
| 04 | [`04_collections_defaultdict.py`](04_collections_defaultdict.py) | defaultdict：分组与默认工厂 |
| 05 | [`05_collections_chainmap.py`](05_collections_chainmap.py) | ChainMap：分层配置 |
| 06 | [`06_collections_namedtuple.py`](06_collections_namedtuple.py) | namedtuple：轻量记录类型 |
| 07 | [`07_itertools_building_blocks.py`](07_itertools_building_blocks.py) | itertools 积木：count/islice/chain/repeat/cycle |
| 08 | [`08_itertools_combinatorics.py`](08_itertools_combinatorics.py) | 组合：product/permutations/combinations |
| 09 | [`09_itertools_groupby.py`](09_itertools_groupby.py) | groupby：按键分组（需排序） |
| 10 | [`10_itertools_accumulate_zip_longest.py`](10_itertools_accumulate_zip_longest.py) | accumulate/pairwise/zip_longest |
| 11 | [`11_functools_partial_and_wraps.py`](11_functools_partial_and_wraps.py) | partial 与 wraps |
| 12 | [`12_functools_cache_lru_cache.py`](12_functools_cache_lru_cache.py) | cache/lru_cache |
| 13 | [`13_functools_singledispatch.py`](13_functools_singledispatch.py) | singledispatch |
| 14 | [`14_functools_reduce_and_cmp_to_key.py`](14_functools_reduce_and_cmp_to_key.py) | reduce 与 cmp_to_key |
| 15 | [`15_chapter_summary.py`](15_chapter_summary.py) | 本章总结：关键规则与常见误区 |
| 16 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | 本章练习索引（每题一个文件） |

---

## 4) 本章练习（每题一个文件）

练习索引：`python3 01_Basics/22_Collections_Itertools_Functools/Exercises/01_overview.py`

- `Exercises/02_deque_sliding_window.py`：deque 实现滑动窗口
- `Exercises/03_counter_top_k.py`：Counter 统计 top-k
- `Exercises/04_defaultdict_grouping.py`：defaultdict 分组
- `Exercises/05_chainmap_layered_config.py`：ChainMap 配置覆盖
- `Exercises/06_namedtuple_points.py`：namedtuple 表示点并计算距离
- `Exercises/07_itertools_chunked.py`：islice 实现分块
- `Exercises/08_itertools_combinations.py`：组合枚举
- `Exercises/09_itertools_groupby_runs.py`：groupby 连续分组
- `Exercises/10_functools_cache_fib.py`：lru_cache 斐波那契
- `Exercises/11_functools_singledispatch_format.py`：singledispatch 格式化
