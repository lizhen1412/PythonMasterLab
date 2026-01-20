# Python 3.11+ 类与对象（Classes）学习笔记（第 20 章）

本章是一组“可运行的小脚本”，系统梳理 Python 类与对象的核心能力：`class` 与 `__init__`、实例属性/类属性、方法绑定、`@classmethod`/`@staticmethod`/`@property`、继承与多态、`dataclass`，以及一组高频“魔法方法”（`__str__`、`__repr__`、`__eq__`、`__iter__`、`__enter__` 等）。示例以“看懂 + 能写”为目标，避免过度抽象。

---

## 1) 怎么运行

在仓库根目录执行：

- 先看索引：`python3 01_Basics/20_Classes/01_overview.py`
- 运行某个示例：`python3 01_Basics/20_Classes/06_magic_methods_text_and_compare.py`

---

## 2) 本章“知识点全景”清单（覆盖常用点）

### 2.1 class 基础

- `class` 定义与实例化；`__init__` 初始化实例属性
- `self` 的含义：实例方法的第一个参数
- 实例方法 vs 类方法 vs 静态方法：调用方式与语义差异

### 2.2 属性与方法

- 类属性 vs 实例属性（共享/遮蔽）
- `@classmethod`：操作“类本身”的方法
- `@staticmethod`：放在类命名空间里的普通函数
- `@property`：把方法“伪装成属性”来做校验/封装

### 2.3 继承与多态

- 子类重写方法、`super()` 调用父类逻辑
- `isinstance` / `issubclass` 的常见用法

### 2.4 dataclass

- 自动生成 `__init__` / `__repr__` / `__eq__`
- 默认值与 `field(default_factory=...)`
- `frozen=True` 带来的“不可变”语义

### 2.5 常见魔法方法（高频协议）

- 文本与格式化：`__repr__` / `__str__` / `__format__`
- 比较与哈希：`__eq__` / `__lt__` / `__hash__`
- 容器与迭代：`__len__` / `__getitem__` / `__setitem__` / `__iter__` / `__next__` / `__contains__` / `__bool__`
- 上下文与可调用：`__enter__` / `__exit__` / `__call__`
- 属性访问与限制：`__getattr__` / `__setattr__` / `__delattr__` / `__slots__`

> 说明：魔法方法非常多，本章聚焦“最常用、最有价值”的那一批。

### 2.6 进阶协议与补充案例

- 生命周期与访问：`__new__` / `__del__` / `__getattribute__`
- 容器进阶：`__delitem__` / `__reversed__`
- 数值与转换：`__add__` / `__sub__` / `__mul__` / `__truediv__` / `__floordiv__` / `__mod__` / `__pow__`
- 转换与系统接口：`__int__` / `__float__` / `__complex__` / `__index__` / `__bytes__` / `__fspath__`
- 异步上下文：`__aenter__` / `__aexit__`
- 拷贝与序列化：`__copy__` / `__deepcopy__` / `__getstate__` / `__setstate__` / `__reduce__`
- 描述符与模式匹配：`__get__` / `__set__` / `__delete__` / `__match_args__`

---

## 3) 文件总览

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出全部示例与主题 |
| 02 | [`02_class_basics_init.py`](02_class_basics_init.py) | class 与 `__init__`：实例、属性、方法 |
| 03 | [`03_class_attributes_and_methods.py`](03_class_attributes_and_methods.py) | 类属性/实例属性、`classmethod`/`staticmethod`/`@property` |
| 04 | [`04_inheritance_and_polymorphism.py`](04_inheritance_and_polymorphism.py) | 继承与多态：重写、`super`、`isinstance` |
| 05 | [`05_dataclass_basics.py`](05_dataclass_basics.py) | `dataclass`：自动生成 `__init__`/`__repr__`/`__eq__` |
| 06 | [`06_magic_methods_text_and_compare.py`](06_magic_methods_text_and_compare.py) | `__repr__`/`__str__`/`__format__`/`__eq__`/`__lt__`/`__hash__` |
| 07 | [`07_magic_methods_container_and_iter.py`](07_magic_methods_container_and_iter.py) | `__len__`/`__bool__`/`__getitem__`/`__iter__`/`__next__`/`__contains__` |
| 08 | [`08_magic_methods_context_and_call.py`](08_magic_methods_context_and_call.py) | `__enter__`/`__exit__`/`__call__` |
| 09 | [`09_magic_methods_attribute_and_slots.py`](09_magic_methods_attribute_and_slots.py) | `__getattr__`/`__setattr__`/`__delattr__`/`__slots__` |
| 11 | [`11_magic_methods_numeric_and_conversion.py`](11_magic_methods_numeric_and_conversion.py) | 数值与转换协议：运算符 + 类型转换 |
| 12 | [`12_magic_methods_object_lifecycle_and_attribute.py`](12_magic_methods_object_lifecycle_and_attribute.py) | 生命周期与属性访问：`__new__`/`__del__`/`__getattribute__` |
| 13 | [`13_magic_methods_container_advanced.py`](13_magic_methods_container_advanced.py) | 容器进阶：`__delitem__`/`__reversed__` |
| 14 | [`14_magic_methods_async_context.py`](14_magic_methods_async_context.py) | 异步上下文：`__aenter__`/`__aexit__` |
| 15 | [`15_magic_methods_copy_and_pickle.py`](15_magic_methods_copy_and_pickle.py) | 拷贝与序列化：`__copy__`/`__deepcopy__`/`__getstate__`/`__reduce__` |
| 16 | [`16_magic_methods_descriptor_and_match.py`](16_magic_methods_descriptor_and_match.py) | 描述符与模式匹配：`__get__`/`__set__`/`__delete__`/`__match_args__` |
| 10 | [`10_chapter_summary.py`](10_chapter_summary.py) | 本章总结：关键规则 + 常见误区（建议最后回顾） |
