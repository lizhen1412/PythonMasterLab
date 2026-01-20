# Python 3.11+ 变量（Variables）与打印变量学习笔记

本目录是一组“可运行的小脚本”，目标是把 **Python 变量相关的知识点一次讲全**：变量的本质（名字绑定对象）、各种赋值方式、可变性与别名、拷贝、作用域（LEGB）、推导式/海象运算符的作用域细节、类型注解、以及如何专业地打印/格式化变量。

> 建议先把每个脚本跑一遍，再回头精读；“看输出 + 对照代码”是最快的学习方式。

---

## 1) 怎么运行（小白版）

假设你当前在仓库根目录（能看到 `01_Basics/` 那层）：

- 先看索引：`python3 01_Basics/02_Variables/01_overview.py`
- 运行某个示例：`python3 01_Basics/02_Variables/02_variable_basics.py`

Windows 上如果没有 `python3`，可以试：

- `python 01_Basics/02_Variables/02_variable_basics.py`
- 或 `py -3.11 01_Basics/02_Variables/02_variable_basics.py`

> 每个脚本末尾都有固定入口：`if __name__ == "__main__": main()`  
> 含义：文件被“直接运行”时执行 `main()`；被 `import` 时不会自动执行。

---

## 2) 术语小抄（先把概念对齐）

- **对象（object）**：真正保存数据的实体（比如一个 `int`、一个 `list`、一个 `dict`）。
- **变量/名字（name）**：一个标签；Python 里“变量”更准确叫“名字绑定对象”（name binding）。
- **可变/不可变（mutable/immutable）**：`list/dict/set` 通常可变；`int/str/tuple` 通常不可变。
- **别名（alias）**：多个名字指向同一个对象（`a = b` 且两者是同一对象）。
- **作用域（scope）**：名字在哪里可见/可用；Python 的查找顺序是 **LEGB**。
- **类型注解（type annotations）**：主要给 IDE/类型检查器用；运行时不会强制类型。

---

## 3) 文件总览（先知道每个文件干什么）

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出所有示例与主题 |
| 02 | [`02_variable_basics.py`](02_variable_basics.py) | 变量本质：名字绑定对象、`id/type`、动态类型、别名 |
| 03 | [`03_identifiers_and_naming.py`](03_identifiers_and_naming.py) | 变量名规则：`isidentifier`、关键字、命名约定 |
| 04 | [`04_assignment_unpacking.py`](04_assignment_unpacking.py) | 赋值与解包：多重赋值、星号解包、交换变量 |
| 05 | [`05_assignment_targets.py`](05_assignment_targets.py) | 赋值目标：变量名/属性/下标/切片 |
| 06 | [`06_chained_assignment_and_aliasing.py`](06_chained_assignment_and_aliasing.py) | 链式赋值陷阱：`a = b = []` |
| 07 | [`07_augmented_assignment_and_mutability.py`](07_augmented_assignment_and_mutability.py) | `+=` 等增强赋值：原地修改 vs 新对象（别名影响很大） |
| 08 | [`08_copying_shallow_vs_deep.py`](08_copying_shallow_vs_deep.py) | 复制：浅拷贝 vs 深拷贝（嵌套结构很关键） |
| 09 | [`09_scopes_LEGB_global_nonlocal.py`](09_scopes_LEGB_global_nonlocal.py) | 作用域：LEGB、`global`、`nonlocal`（含安全反例演示） |
| 10 | [`10_loop_and_comprehension_scope.py`](10_loop_and_comprehension_scope.py) | `for` 循环变量会保留；推导式循环变量不会泄漏 |
| 11 | [`11_walrus_operator.py`](11_walrus_operator.py) | 海象运算符 `:=`：常见用法 + 作用域细节 |
| 12 | [`12_type_annotations_and_constants.py`](12_type_annotations_and_constants.py) | 变量类型注解、`__annotations__`、`Final/ClassVar` |
| 13 | [`13_print_basics.py`](13_print_basics.py) | `print()` 参数：`sep/end/file/flush` |
| 14 | [`14_string_formatting_fstrings.py`](14_string_formatting_fstrings.py) | 专业打印：f-string、`repr/str`、格式化规格、对齐 |
| 15 | [`15_common_pitfalls.py`](15_common_pitfalls.py) | 常见坑：可变默认参数、闭包晚绑定（含正确写法） |
| 16 | [`16_match_case_and_as_binding.py`](16_match_case_and_as_binding.py) | 进阶绑定：`match/case`、`with/except ... as ...` |
| 17 | [`17_globals_locals_and_del.py`](17_globals_locals_and_del.py) | `globals/locals` 与 `del`：删除名字 vs 对象是否还在 |

---

## 4) 你要掌握的知识点（Checklist）

- 变量的本质：名字绑定对象（不是“盒子”）
- `type()` / `id()` / `is`：类型、身份与“是否同一对象”
- 动态类型：同一名字可以绑定不同类型对象（更推荐用 `object`/`Any` 表达）
- 各种赋值方式：多重赋值、解包、星号解包、交换变量
- 赋值目标：属性、下标、切片也是“赋值目标”
- 链式赋值对可变对象的坑：`a = b = []`
- 可变性与增强赋值：`+=` 可能原地修改，别名会被“连带影响”
- 浅拷贝 vs 深拷贝：嵌套结构下的共享问题
- 作用域与 LEGB：什么时候需要 `global` / `nonlocal`
- `for` vs 推导式作用域：循环变量是否泄漏
- 海象运算符 `:=`：减少重复计算，但要理解它的绑定/作用域规则
- 类型注解：`__annotations__`、`Final`、`ClassVar`，以及“注解主要给工具用”
- 打印变量：`print()` 常用参数、f-string、`{var=}`、格式化输出
- 常见坑：可变默认参数、闭包晚绑定（必须会）
- `globals()`/`locals()`/`del`：名字表与删除绑定

---

## 5) 逐个详解（怎么跑 + 学到什么）

下面每一节都能直接复制命令运行。

### 01 - `01_overview.py`

运行：
- `python3 01_Basics/02_Variables/01_overview.py`

你会学到：
- 如何快速浏览本目录都有哪些示例、是否缺文件

---

### 02 - `02_variable_basics.py`

运行：
- `python3 01_Basics/02_Variables/02_variable_basics.py`

你会学到：
- 变量名是标签、对象才是数据；`id/type` 如何辅助理解
- 不可变对象重新绑定 vs 可变对象原地修改
- “别名”为什么会导致看似奇怪的联动变化

---

### 03 - `03_identifiers_and_naming.py`

运行：
- `python3 01_Basics/02_Variables/03_identifiers_and_naming.py`

你会学到：
- 什么字符串能当变量名（合法标识符）
- 为什么关键字（如 `class`）不能作为变量名
- 变量命名的工程习惯（可读性优先）

---

### 04 - `04_assignment_unpacking.py`

运行：
- `python3 01_Basics/02_Variables/04_assignment_unpacking.py`

你会学到：
- `a, b = 1, 2` 的常见用法
- 星号解包 `first, *middle, last = ...`
- 解包失败会抛 `ValueError`（示例中已捕获，不会让程序崩）

---

### 05 - `05_assignment_targets.py`

运行：
- `python3 01_Basics/02_Variables/05_assignment_targets.py`

你会学到：
- 赋值不仅是“给变量名赋值”，也可以写到对象属性、列表下标、切片、字典 key

---

### 06 - `06_chained_assignment_and_aliasing.py`

运行：
- `python3 01_Basics/02_Variables/06_chained_assignment_and_aliasing.py`

你会学到：
- 为什么 `a = b = []` 会“坑到自己”（共享同一个 list）
- 正确写法：`a, b = [], []`

---

### 07 - `07_augmented_assignment_and_mutability.py`

运行：
- `python3 01_Basics/02_Variables/07_augmented_assignment_and_mutability.py`

你会学到：
- `+=` 对 list 可能是原地修改、对 tuple 会产生新对象
- 当存在别名时，`a += ...` 和 `a = a + ...` 的效果不同

---

### 08 - `08_copying_shallow_vs_deep.py`

运行：
- `python3 01_Basics/02_Variables/08_copying_shallow_vs_deep.py`

你会学到：
- `b = a` 不是复制
- 浅拷贝只复制外层容器；嵌套结构中依旧共享内部对象
- 深拷贝会递归复制，代价更高但更独立

---

### 09 - `09_scopes_LEGB_global_nonlocal.py`

运行：
- `python3 01_Basics/02_Variables/09_scopes_LEGB_global_nonlocal.py`

你会学到：
- LEGB 查找顺序：Local/Enclosing/Global/Builtins
- `global` 如何工作（不建议滥用，但要理解）
- `nonlocal` 解决闭包计数器等常见场景
- “反例”用 `exec()` 安全演示（不会造成文件级静态检查告警）

---

### 10 - `10_loop_and_comprehension_scope.py`

运行：
- `python3 01_Basics/02_Variables/10_loop_and_comprehension_scope.py`

你会学到：
- `for` 循环结束后循环变量仍然存在
- 推导式循环变量在 Python 3 中不会泄漏到外层作用域

---

### 11 - `11_walrus_operator.py`

运行：
- `python3 01_Basics/02_Variables/11_walrus_operator.py`

你会学到：
- `:=` 的实用场景（正则匹配、读取数据）
- 在推导式里：循环变量不泄漏，但 `:=` 绑定的名字会绑定到外层作用域（务必理解）

---

### 12 - `12_type_annotations_and_constants.py`

运行：
- `python3 01_Basics/02_Variables/12_type_annotations_and_constants.py`

你会学到：
- 变量类型注解写法，以及 `__annotations__` 存的是什么
- `Final`/`ClassVar` 表达“常量/类变量意图”（主要给工具用）

---

### 13 - `13_print_basics.py`

运行：
- `python3 01_Basics/02_Variables/13_print_basics.py`

你会学到：
- `print()` 如何打印多个变量
- `sep/end/file/flush` 分别解决什么问题

---

### 14 - `14_string_formatting_fstrings.py`

运行：
- `python3 01_Basics/02_Variables/14_string_formatting_fstrings.py`

你会学到：
- f-string 最常用、最推荐
- 调试利器：`f"{var=}"` 与 `!r`
- 数值格式化与对齐（打印表格/日志经常用）

---

### 15 - `15_common_pitfalls.py`

运行：
- `python3 01_Basics/02_Variables/15_common_pitfalls.py`

你会学到：
- 可变默认参数为什么会“记住上一次的结果”
- 闭包晚绑定导致 `lambda` 全返回同一个值
- 两种坑的正确写法（必须记住）

---

### 16 - `16_match_case_and_as_binding.py`

运行：
- `python3 01_Basics/02_Variables/16_match_case_and_as_binding.py`

你会学到：
- `match/case` 捕获模式会绑定变量
- `as` / `with ... as ...` / `except ... as ...` 都是“绑定名字”的方式

---

### 17 - `17_globals_locals_and_del.py`

运行：
- `python3 01_Basics/02_Variables/17_globals_locals_and_del.py`

你会学到：
- `globals()`/`locals()` 是名字表（dict）
- `del name` 删除的是名字绑定；如果还有别的引用，对象还在

---

## 6) 最终总结（你学完后应该能回答的问题）

- 为什么说 Python 变量是“名字绑定对象”？这对理解别名/拷贝有什么帮助？
- `a = b = []` 为什么危险？如何写得更安全？
- `a += ...` 和 `a = a + ...` 在 list 上有什么本质差别？
- 为什么浅拷贝在嵌套结构里仍然会“连带变化”？什么时候必须用深拷贝？
- LEGB 是什么？`global` / `nonlocal` 什么时候用、为什么不建议滥用？
- `for` 循环变量为什么会保留？推导式变量为什么不会泄漏？
- `:=` 为什么好用？它在推导式里又有什么作用域细节？
- 如何用 `print` + f-string 做到“专业可读”的变量输出？
- 两个必踩坑：可变默认参数、闭包晚绑定——你能解释并写出正确写法吗？
