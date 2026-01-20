# Python 3.11+ 函数（Functions）学习笔记（第 14 章）

本章是一组“可运行的小脚本”，系统梳理 Python 函数的全部核心能力：定义/调用/返回值、参数种类（位置/关键字/默认/变参/只限位置/只限关键字）、`*args/**kwargs` 收集与转发、作用域与闭包、`lambda` 与高阶函数、常用内置函数（函数式工具）、递归、装饰器/`functools.partial`，以及一个函数化的名片管理小项目。附带针对性的练习题（每题一文件）。

---

## 1) 怎么运行

在仓库根目录执行：

- 先看索引：`python3 01_Basics/14_Functions/01_overview.py`
- 运行某个示例：`python3 01_Basics/14_Functions/05_varargs_kwargs_and_unpacking.py`
- 练习题索引：`python3 01_Basics/14_Functions/Exercises/01_overview.py`

---

## 2) 本章“知识点全景”清单（覆盖常用与易错）

### 2.1 函数基础

- `def` 定义、调用、返回值（无显式 return 默认 `None`）
- 文档字符串与类型注解：`def func(x: int) -> int: ...`
- 参数 vs 实参：形参数量/顺序如何与调用匹配

### 2.2 参数种类与调用规则

- 默认参数求值时机（定义时）；可变默认值陷阱 + `None` 哨兵防御
- 五类参数位：位置仅限 `a, /`；位置或关键字；可变位置 `*args`；关键字仅限 `*, b`；可变关键字 `**kwargs`
- 常见错误信息解析：`got multiple values for argument`、`missing required keyword-only argument`

### 2.3 变参、解包与转发

- 收集：`*args/**kwargs`；解包：`func(*seq, **mapping)`
- 参数转发：包装/装饰时透传 `*args, **kwargs`
- `*` 用于解包 vs 乘法；`**` 合并 dict 时覆盖规则

### 2.4 作用域、闭包与函数是一等公民

- LEGB 复盘；`UnboundLocalError` 触发与修正；`global` 与 `nonlocal`
- 闭包：`__closure__`，循环中延迟绑定的坑与修复
- 函数作为值：存入容器、传入/返回函数、`lambda` 适用场景

### 2.5 常用内置、递归、装饰器

- 内置函数（函数式/迭代工具）：`len/sum/any/all/min/max/sorted/reversed/zip/enumerate/map/filter/round/divmod/pow/abs`（含易错点）
- 内置函数全清单参考：覆盖所有 built-in（含交互/动态执行类函数的安全示例）
- 递归：基线/收敛、调用栈与深度限制、迭代替代
- 装饰器：闭包包装、`functools.wraps`、带参数装饰器、`functools.partial`

---

## 3) 文件总览

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出全部示例与主题 |
| 02 | [`02_function_basics_def_call_return.py`](02_function_basics_def_call_return.py) | 函数定义/调用/返回值，docstring 与类型注解 |
| 03 | [`03_parameters_and_default_values.py`](03_parameters_and_default_values.py) | 参数与默认值：求值时机、可变默认值陷阱与防御 |
| 04 | [`04_parameter_kinds_pos_only_kw_only.py`](04_parameter_kinds_pos_only_kw_only.py) | 参数五种类别：位置仅限、关键字仅限、变参，合法/非法调用 |
| 05 | [`05_varargs_kwargs_and_unpacking.py`](05_varargs_kwargs_and_unpacking.py) | `*args/**kwargs` 收集与解包，参数转发、覆盖规则 |
| 06 | [`06_scope_and_closure.py`](06_scope_and_closure.py) | 作用域、`UnboundLocalError`、`global/nonlocal`、闭包与延迟绑定坑 |
| 07 | [`07_lambda_and_first_class_functions.py`](07_lambda_and_first_class_functions.py) | `lambda` 适用场景，函数作为值（存容器/传参/返回） |
| 08 | [`08_decorators_and_partial.py`](08_decorators_and_partial.py) | 装饰器最小用法、`functools.wraps`、带参数装饰器、`partial` |
| 09 | [`09_common_builtin_functions.py`](09_common_builtin_functions.py) | 常用内置函数分类：聚合/迭代/数值/函数式，易错点提示 |
| 10 | [`13_builtin_functions_reference.py`](13_builtin_functions_reference.py) | 内置函数全覆盖：完整清单 + 关键用法示例 |
| 11 | [`10_recursive_functions.py`](10_recursive_functions.py) | 递归：基线与收敛、调用栈限制、阶乘/斐波那契/树深度 |
| 12 | [`11_chapter_summary.py`](11_chapter_summary.py) | 本章总结：规则清单与常见误区 |
| 13 | [`12_card_management_system.py`](12_card_management_system.py) | 综合示例：函数化的名片管理（增删改查、格式化输出） |
| 14 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | 本章练习索引（每题一个文件） |

---

## 4) 本章练习（每题一个文件）

练习索引：`python3 01_Basics/14_Functions/Exercises/01_overview.py`

- `Exercises/02_fix_mutable_default.py`：修复可变默认值陷阱，使用 None 哨兵与复制
- `Exercises/03_kwonly_api_design.py`：设计带关键字仅限参数的函数并给出调用示例
- `Exercises/04_closure_counter.py`：闭包计数器，演示 `nonlocal` 与状态累积
- `Exercises/05_lambda_sort_and_filter.py`：用 `lambda` 排序/过滤一批记录，比较可读性
- `Exercises/06_implement_simple_map_filter.py`：自己实现简化版 `map/filter` 并与内置对照
- `Exercises/07_factorial_recursive_vs_iterative.py`：阶乘递归 vs 迭代，讨论递归深度限制
- `Exercises/08_timer_decorator.py`：编写计时装饰器，支持透传 `*args/**kwargs`
- `Exercises/09_card_system_feature.py`：为名片系统补充“按姓名模糊搜索”功能

---

## 5) 小贴士（写/看代码时）

- 示例都保持 `main()` + `if __name__ == "__main__": main()`，便于直接运行或被 `import`
- 参数报错信息要读懂：出现 “multiple values for argument” 多半是“位置 + 关键字重复”
- 可变默认值一定谨慎：要么用不可变对象，要么用 None 哨兵 + 防御式创建
- 递归必须先写好“基线”；当可用迭代替代时，优先考虑迭代以避免栈深限制
