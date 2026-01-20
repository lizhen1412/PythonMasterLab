# Python 3.11+ 迭代器与生成器（Iterators & Generators）学习笔记（第 21 章）

本章聚焦“可迭代对象 / 迭代器 / 生成器”的完整链条：
- 迭代协议：`iter()` / `next()` / `StopIteration`
- 自定义迭代器类
- 生成器函数与生成器表达式
- `send/throw/close`、`yield from` 委托
- 一次性迭代器的耗尽与复用
- 异步生成器的基本用法

---

## 1) 怎么运行

在仓库根目录执行：

- 先看索引：`python3 01_Basics/21_Iterators_Generators/01_overview.py`
- 运行某个示例：`python3 01_Basics/21_Iterators_Generators/06_generator_function_basics.py`
- 练习题索引：`python3 01_Basics/21_Iterators_Generators/Exercises/01_overview.py`

---

## 2) 本章“知识点全景”清单

### 2.1 可迭代对象 vs 迭代器

- 可迭代对象（iterable）：能被 `iter(x)` 转成迭代器
- 迭代器（iterator）：实现 `__iter__` + `__next__`，`next()` 到头会抛 `StopIteration`
- `for` 循环内部就是 `iter()` + `next()` + 捕获 `StopIteration`

### 2.2 自定义迭代器

- `__iter__` 通常返回 `self`
- `__next__` 在耗尽时必须抛 `StopIteration`
- 常见坑：忘记抛 `StopIteration` 会导致死循环

### 2.3 生成器函数与表达式

- `yield` 会把函数变成生成器函数，返回生成器对象
- 生成器是“惰性”的：需要时才计算
- 生成器表达式：`(x*x for x in items)`，适合流式处理

### 2.4 双向通信与清理

- `send(value)` 可向生成器内部传值（第一次必须 `None`）
- `next(gen)` 等价于 `gen.send(None)`
- `throw(exc)` 可在生成器内部抛异常
- `close()` 会触发 `GeneratorExit`，用 `try/finally` 做清理

### 2.5 `yield from` 委托

- 把迭代责任交给子生成器
- 子生成器 `return` 的值会作为 `yield from` 表达式的结果

### 2.6 一次性迭代器的复用

- 迭代器/生成器只能消费一次
- 需要复用时：缓存为 `list/tuple`，或使用 `itertools.tee`

### 2.7 异步生成器

- `async def` + `yield` 定义异步生成器
- 只能用 `async for` 消费
- 常用于异步 I/O 的流式处理

---

## 3) 文件总览

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出全部示例与主题 |
| 02 | [`02_iterable_and_iterator.py`](02_iterable_and_iterator.py) | 可迭代对象 vs 迭代器：协议与基本用法 |
| 03 | [`03_iter_next_and_stop_iteration.py`](03_iter_next_and_stop_iteration.py) | 手动迭代与 StopIteration；for 的内部机制 |
| 04 | [`04_custom_iterator_class.py`](04_custom_iterator_class.py) | 自定义迭代器类：__iter__/__next__ |
| 05 | [`05_iter_callable_sentinel.py`](05_iter_callable_sentinel.py) | iter(callable, sentinel)：哨兵迭代 |
| 06 | [`06_generator_function_basics.py`](06_generator_function_basics.py) | 生成器函数基础：yield、惰性与状态 |
| 07 | [`07_generator_send_and_two_way.py`](07_generator_send_and_two_way.py) | send 双向通信：next() == send(None) |
| 08 | [`08_generator_throw_and_close.py`](08_generator_throw_and_close.py) | throw/close 与清理：finally 与 GeneratorExit |
| 09 | [`09_yield_from_delegation.py`](09_yield_from_delegation.py) | yield from 委托与返回值 |
| 10 | [`10_generator_expression_vs_list.py`](10_generator_expression_vs_list.py) | 生成器表达式 vs 列表推导式 |
| 11 | [`11_iterator_exhaustion_and_reuse.py`](11_iterator_exhaustion_and_reuse.py) | 一次性迭代器的耗尽与复用 |
| 12 | [`12_async_generator_basics.py`](12_async_generator_basics.py) | 异步生成器：async def + yield + async for |
| 13 | [`13_chapter_summary.py`](13_chapter_summary.py) | 本章总结：关键规则与常见误区 |
| 14 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | 本章练习索引（每题一个文件） |

---

## 4) 本章练习（每题一个文件）

练习索引：`python3 01_Basics/21_Iterators_Generators/Exercises/01_overview.py`

- `Exercises/02_safe_next_with_default.py`：实现安全的 `next_or`（StopIteration -> 默认值）
- `Exercises/03_countdown_iterator.py`：自定义倒计时迭代器
- `Exercises/04_iter_callable_sentinel.py`：用 `iter(callable, sentinel)` 读取到哨兵
- `Exercises/05_generator_even_squares.py`：生成器：偶数平方的惰性序列
- `Exercises/06_yield_from_flatten.py`：用 `yield from` 扁平化嵌套列表
- `Exercises/07_generator_send_step.py`：`send` 改变生成器步长
- `Exercises/08_exhaustion_fix.py`：修复“一次性迭代器被耗尽”的 bug
