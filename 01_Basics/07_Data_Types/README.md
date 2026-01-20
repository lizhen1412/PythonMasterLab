# Python 3.11+ 数据类型（Data Types）学习笔记（第 07 章）

本章是一组“可运行的小脚本”，把 **Python 最常用的内置数据类型** 系统过一遍，并配上小白能看懂的学习案例：`None`、`bool`、数字（`int/float/complex`）、字符串 `str`、序列（`list/tuple/range`）、映射 `dict`、集合（`set/frozenset`）、二进制（`bytes/bytearray/memoryview`），以及“可变性/拷贝/可哈希性”等必须理解的底层概念。

> 说明：为了把“精度”讲清楚，本章也额外演示了标准库里的 `Decimal` 与 `Fraction`（它们不是 builtins，但非常常见）。

---

## 1) 文件总览（先知道每个文件是干什么的）

建议按编号顺序学；每个文件都能单独运行。

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出全部示例及主题 |
| 02 | [`02_type_system_and_categories.py`](02_type_system_and_categories.py) | 类型系统概览：type/isinstance/真值测试/可变性/可哈希性 |
| 03 | [`03_none_and_bool.py`](03_none_and_bool.py) | None 与 bool：空值、条件判断、短路与常见坑 |
| 04 | [`04_numbers_int_float_complex.py`](04_numbers_int_float_complex.py) | 数字类型：int/float/complex、精度问题、Decimal/Fraction |
| 05 | [`05_strings_str.py`](05_strings_str.py) | 字符串 str：索引切片、常用方法、编码/解码基础 |
| 06 | [`06_list_tuple_range.py`](06_list_tuple_range.py) | 序列类型：list/tuple/range（可变 vs 不可变、解包） |
| 07 | [`07_dict_mapping.py`](07_dict_mapping.py) | dict：创建、访问、遍历、更新、合并、计数/分组案例 |
| 08 | [`08_set_frozenset.py`](08_set_frozenset.py) | set/frozenset：去重、集合运算、可哈希性 |
| 09 | [`09_bytes_bytearray_memoryview.py`](09_bytes_bytearray_memoryview.py) | bytes/bytearray/memoryview：二进制数据与零拷贝视图 |
| 10 | [`10_mutability_copy_and_hashability.py`](10_mutability_copy_and_hashability.py) | 可变性/拷贝/可哈希：为什么 list 不能当 dict key |
| 11 | [`11_common_conversions_and_helpers.py`](11_common_conversions_and_helpers.py) | 常见转换与工具：str/repr/ascii、len/iter/next、sorted/reversed |
| 12 | [`12_str_methods_reference.py`](12_str_methods_reference.py) | str 方法全覆盖：清理/查找/替换/判断/格式化/编码 |
| 13 | [`13_sequence_methods_reference.py`](13_sequence_methods_reference.py) | 序列方法全覆盖：list/tuple/range |
| 14 | [`14_mapping_and_set_methods_reference.py`](14_mapping_and_set_methods_reference.py) | 映射与集合方法全覆盖：dict/set/frozenset |
| 15 | [`15_binary_types_methods_reference.py`](15_binary_types_methods_reference.py) | 二进制方法全覆盖：bytes/bytearray/memoryview |
| 16 | [`16_numeric_types_methods_reference.py`](16_numeric_types_methods_reference.py) | 数值方法全覆盖：int/float/complex |
| 17 | [`17_collection_method_variants.py`](17_collection_method_variants.py) | 集合类方法参数与边界：list/tuple/dict/set |

---

## 2) 怎么运行（小白版）

下面命令都以“仓库根目录”为当前工作目录（也就是你能看到 `01_Basics/` 的那一层）：

- 先看索引：`python3 01_Basics/07_Data_Types/01_overview.py`
- 运行某个示例：`python3 01_Basics/07_Data_Types/04_numbers_int_float_complex.py`

> 每个脚本末尾都有固定入口：`if __name__ == "__main__": main()`  
> 含义：文件被“直接运行”时执行 `main()`；被 `import` 时不会自动执行。

---

## 3) 你要掌握的知识点（Checklist）

### 3.1 “类型”相关的基本能力

- `type(x)` 能告诉你：x 是什么类型（对象的实际类型）
- `isinstance(x, T)` 是推荐的类型判断方式（比 `type(x) == T` 更通用）
- 真值测试：`if x:` 的含义，以及哪些值会被当成 False

### 3.2 内置数据类型必须全认识

- **空值**：`None`
- **布尔**：`bool`
- **数字**：`int` / `float` / `complex`（以及精度问题）
- **字符串**：`str`
- **序列**：`list` / `tuple` / `range`
- **映射**：`dict`
- **集合**：`set` / `frozenset`
- **二进制**：`bytes` / `bytearray` / `memoryview`

### 3.3 进阶但必须懂的“底层概念”

- 可变 vs 不可变：为什么 `b = a` 不是复制
- 浅拷贝 vs 深拷贝：嵌套结构为什么会“连带变化”
- 可哈希性（hashable）：为什么 list/dict/set 不能当 dict key（但 tuple/frozenset/str/int 可以）

---

## 4) 逐个详解（怎么跑 + 学到什么）

### 01 - `01_overview.py`

运行：
- `python3 01_Basics/07_Data_Types/01_overview.py`

它做什么：
- 列出本目录所有示例文件，并标记 `OK/MISSING`

---

### 02 - `02_type_system_and_categories.py`

运行：
- `python3 01_Basics/07_Data_Types/02_type_system_and_categories.py`

你会学到：
- 用 `type/isinstance/bool/hash` 快速“体检”一个对象
- 真值测试、可变性、可哈希性的核心概念

---

### 03 - `03_none_and_bool.py`

运行：
- `python3 01_Basics/07_Data_Types/03_none_and_bool.py`

你会学到：
- `None` 的正确判断方式：`is None`
- `and/or` 的短路与返回值规则
- 0 是合法值时，为什么不能简单 `if x:` 判断“有值”

---

### 04 - `04_numbers_int_float_complex.py`

运行：
- `python3 01_Basics/07_Data_Types/04_numbers_int_float_complex.py`

你会学到：
- int/float/complex 的基本操作
- 浮点误差与 `math.isclose`
- Decimal/Fraction 的使用场景

---

### 05 - `05_strings_str.py`

运行：
- `python3 01_Basics/07_Data_Types/05_strings_str.py`

你会学到：
- 字符串的索引/切片与常用方法
- str 不可变
- 编码/解码：`str.encode` 与 `bytes.decode`

---

### 06 - `06_list_tuple_range.py`

运行：
- `python3 01_Basics/07_Data_Types/06_list_tuple_range.py`

你会学到：
- list 的常用操作：增删改查 + 排序 + 切片
- tuple 的解包与“单元素 tuple”写法
- range 的惰性特性与成员测试

---

### 07 - `07_dict_mapping.py`

运行：
- `python3 01_Basics/07_Data_Types/07_dict_mapping.py`

你会学到：
- dict 的创建/访问/遍历/更新/合并
- 两个经典案例：计数（get）与分组（setdefault）

---

### 08 - `08_set_frozenset.py`

运行：
- `python3 01_Basics/07_Data_Types/08_set_frozenset.py`

你会学到：
- set 的去重、集合运算
- frozenset 的可哈希性（能当 dict key）

---

### 09 - `09_bytes_bytearray_memoryview.py`

运行：
- `python3 01_Basics/07_Data_Types/09_bytes_bytearray_memoryview.py`

你会学到：
- bytes/bytearray 的区别（不可变 vs 可变）
- memoryview 的“零拷贝视图”概念
- 二进制与字符串的相互转换（UTF-8）

---

### 10 - `10_mutability_copy_and_hashability.py`

运行：
- `python3 01_Basics/07_Data_Types/10_mutability_copy_and_hashability.py`

你会学到：
- `b = a` 不是复制
- 浅拷贝/深拷贝的差异（嵌套结构）
- 可哈希性与 dict key 的关系

---

### 11 - `11_common_conversions_and_helpers.py`

运行：
- `python3 01_Basics/07_Data_Types/11_common_conversions_and_helpers.py`

你会学到：
- `str/repr/ascii` 的区别
- list/tuple/set/dict 的常见构造
- `iter/next`、`sorted/reversed` 的使用方式

---

### 12 - `12_str_methods_reference.py`

运行：
- `python3 01_Basics/07_Data_Types/12_str_methods_reference.py`

你会学到：
- str 方法的完整清单与使用示例（清理/切分/查找/替换/对齐/判断/格式化/编码）

---

### 13 - `13_sequence_methods_reference.py`

运行：
- `python3 01_Basics/07_Data_Types/13_sequence_methods_reference.py`

你会学到：
- list/tuple/range 的全部方法与关键属性（start/stop/step）

---

### 14 - `14_mapping_and_set_methods_reference.py`

运行：
- `python3 01_Basics/07_Data_Types/14_mapping_and_set_methods_reference.py`

你会学到：
- dict/set/frozenset 的方法全清单与典型用法

---

### 15 - `15_binary_types_methods_reference.py`

运行：
- `python3 01_Basics/07_Data_Types/15_binary_types_methods_reference.py`

你会学到：
- bytes/bytearray/memoryview 的常用方法与关键属性

---

### 16 - `16_numeric_types_methods_reference.py`

运行：
- `python3 01_Basics/07_Data_Types/16_numeric_types_methods_reference.py`

你会学到：
- int/float/complex 的方法与数值属性（real/imag 等）

---

### 17 - `17_collection_method_variants.py`

运行：
- `python3 01_Basics/07_Data_Types/17_collection_method_variants.py`

你会学到：
- list/tuple/dict/set 方法的参数用法与常见边界（start/stop、默认值、异常行为）
