# Python 3.11+ 组合数据类型（Composite Types）学习笔记（第 12 章）

本章聚焦“组合数据类型”（也可理解为常用容器/集合）：**序列（sequence）**、**列表 list**、**元组 tuple**、**range**、**字符串 str**、**字典 dict**、**集合 set**，以及它们背后的核心差异：**可变 vs 不可变**、拷贝/别名、遍历方式与常用方法。

---

## 1) 怎么运行

在仓库根目录执行：

- 先看索引：`python3 01_Basics/12_Composite_Types/01_overview.py`
- 运行某个示例：`python3 01_Basics/12_Composite_Types/04_list_daily_operations.py`
- 练习题索引：`python3 01_Basics/12_Composite_Types/Exercises/01_overview.py`

---

## 2) 本章“知识点全景”清单（按类别枚举）

### 2.1 序列（Sequence）通用能力（list/tuple/range/str）

你应该对所有序列都熟练掌握：

- 索引：`seq[i]`、负索引 `seq[-1]`
- 切片：`seq[start:stop:step]`（stop 不包含；step 可为负）
- 长度与成员：`len(seq)`、`x in seq`
- 遍历：`for x in seq`、`enumerate(seq, start=1)`
- 拼接与重复：`seq1 + seq2`、`seq * n`（注意：`[[0]] * 3` 会产生“共享内层对象”的坑）
- 解包：`a, b = seq`、`first, *middle, last = seq`

### 2.2 列表 list：创建、日常操作、遍历、常用方法

- 创建：
  - 字面量：`[]`、`[1, 2, 3]`
  - 构造：`list(iterable)`（如 `list(range(5))`、`list("abc")`）
  - 推导式：`[f(x) for x in items if cond]`
  - 星号解包：`[*iterable]`
- 日常操作（增删改查）：
  - 读/改：索引与切片（含“切片赋值”）
  - 增：`append` / `extend` / `insert`
  - 删：`remove` / `pop` / `del` / `clear`
  - 查：`in` / `index` / `count`
  - 排序：`sort`（原地） vs `sorted`（返回新列表）
  - 拷贝：`copy()` / `list(x)` / `x[:]`（理解“浅拷贝”）
- 遍历：
  - `for x in items`（最常用）
  - `for i, x in enumerate(items)`（推荐代替 `range(len(items))`）
  - **避免**在遍历时原地增删 list（会跳元素）；更稳的写法是“生成新列表”或遍历副本
- 常用方法（要能说清语义）：
  - `append/extend/insert/remove/pop/clear/index/count/sort/reverse/copy`

### 2.3 元组 tuple：创建、常用操作、遍历

- 创建：
  - 空元组：`()`
  - 单元素：`(1,)`（注意逗号）
  - 打包/解包：`a, b = 1, 2`；`x, y = (3, 4)`
  - 构造：`tuple(iterable)`
- 常用操作：
  - 索引/切片/拼接/重复/`in`
  - 方法：`count` / `index`
  - 不可变：不能改“元组自身的元素引用”，但**元素内部**如果是可变对象（如 list），仍可被修改

### 2.4 range：可迭代的“整数序列对象”

- `range(stop)` / `range(start, stop[, step])`（stop 不包含）
- 支持：`len`、成员测试、索引与切片（切片结果仍是 range）
- 边界与易错点：`step` 不能为 0；空 range 的 `len` 为 0；相等比较按序列值判断
- 注意：`list(range(10**9))` 会爆内存；range 适合“只遍历不一次性展开”

### 2.5 字符串 str：序列 + 文本处理

- 作为序列：索引/切片/遍历/`in`
- 不可变：不能原地改字符；“修改”本质上是创建新字符串
- 常用方法（高频）：
  - 清理：`strip/lstrip/rstrip`
  - 拆分：`split` / `splitlines`
  - 拼接：`"sep".join(parts)`（比循环里 `+=` 更稳更快）
  - 替换与查找：`replace/find/index/startswith/endswith`
  - 大小写：`lower/upper/title`

### 2.6 字典 dict：映射（key -> value）

- 创建：`{}` / `dict()` / 推导式 / `dict(zip(keys, values))`
- 访问：`d[k]`（不存在抛 KeyError） vs `d.get(k, default)`
- 更新：赋值、`update`、合并 `|` / `|=`（Py 3.9+）
- 删除：`del d[k]` / `pop` / `popitem` / `clear`
- 遍历：`for k in d`（遍历 key）与 `for k, v in d.items()`
- 常见套路：计数/分组（`get` 或 `setdefault`）

### 2.7 集合 set：去重 + 集合运算

- 创建：`set()`（空集合）、`{1, 2, 3}`
- 操作：`add/update/remove/discard/pop/clear`
- 运算：并 `|`、交 `&`、差 `-`、对称差 `^`；子集 `<=`/超集 `>=`
- `frozenset`：不可变集合（可作为 dict key / set 元素）

### 2.8 可变与不可变（Mutability）

- 可变：`list/dict/set/bytearray`（原地修改会影响别名）
- 不可变：`tuple/str/range/bytes`（“修改”通常产生新对象）
- 关键陷阱：
  - 别名：`b = a` 不是复制
  - 浅拷贝：只复制“外层容器”，内层对象仍共享（嵌套结构最容易踩坑）

---

## 3) 文件总览

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出全部示例与主题 |
| 02 | [`02_sequences_overview.py`](02_sequences_overview.py) | 序列通用操作：索引/切片/解包/拼接/成员测试 |
| 03 | [`03_list_creation.py`](03_list_creation.py) | list 创建方式：字面量/构造/推导式/解包/常见坑 |
| 04 | [`04_list_daily_operations.py`](04_list_daily_operations.py) | list 日常操作：增删改查、排序、拷贝与别名 |
| 05 | [`05_list_traversal.py`](05_list_traversal.py) | list 遍历：for/enumerate/reversed/推导式/安全修改 |
| 06 | [`06_tuple_creation_and_ops.py`](06_tuple_creation_and_ops.py) | tuple 创建与常用操作：解包、不可变、count/index |
| 07 | [`07_range_basics.py`](07_range_basics.py) | range：区间、步长、索引/切片、与 list 的区别 |
| 08 | [`08_string_basics.py`](08_string_basics.py) | str：序列特性 + 高频文本方法（split/join/replace） |
| 09 | [`09_dict_basics.py`](09_dict_basics.py) | dict：创建/访问/更新/遍历/计数分组套路 |
| 10 | [`10_set_basics.py`](10_set_basics.py) | set：去重、成员测试、集合运算、frozenset |
| 11 | [`11_mutability_and_copy.py`](11_mutability_and_copy.py) | 可变 vs 不可变：别名、浅拷贝/深拷贝、嵌套陷阱 |
| 12 | [`13_range_edge_cases.py`](13_range_edge_cases.py) | range 边界与易错点：空区间、负步长、切片、相等比较 |
| 13 | [`12_chapter_summary.py`](12_chapter_summary.py) | 本章总结：关键规则 + 常见误区清单 |
| 14 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | 本章练习索引（每题一个文件） |

---

## 4) 本章练习（每题一个文件）

练习索引：`python3 01_Basics/12_Composite_Types/Exercises/01_overview.py`

- `Exercises/02_sequence_slice_head_tail.py`：序列切片 head/tail + first/middle/last
- `Exercises/03_list_dedup_preserve_order.py`：list 去重但保持顺序
- `Exercises/04_list_stack_ops.py`：list 实现栈（push/pop/peek）
- `Exercises/05_list_filter_and_square.py`：推导式：过滤 + 映射
- `Exercises/06_tuple_unpack_swap.py`：tuple 解包与交换变量
- `Exercises/07_range_generate_slices.py`：range 切片（切片结果仍为 range）
- `Exercises/08_string_split_join_normalize.py`：split/join：规范化空白
- `Exercises/09_dict_word_count_and_group.py`：dict：计数与分组（get/setdefault）
- `Exercises/10_set_unique_and_intersection.py`：set：去重与交集
- `Exercises/11_mutability_copy_fix.py`：修复嵌套列表共享引用坑
