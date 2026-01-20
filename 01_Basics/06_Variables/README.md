# Python 3.11+ 变量（Variables）学习笔记（第 06 章）

本章是一组“可运行的小脚本”，把 **Python 变量相关的核心知识点** 系统梳理一遍：变量创建、变量修改（重新绑定 vs 原地修改）、变量命名规则与约定、变量类型与动态类型、类型转换、类型注解、作用域与生命周期、以及最常见的坑。

> 说明：本仓库里 `01_Basics/02_Variables/` 也有一章“更全更进阶”的变量专题（覆盖拷贝/作用域细节/海象运算符等更多内容）。本章更偏“按你列的主题重新整理成一套入门路径”，并补齐 `isinstance`/注解解析等更小白友好的点。

---

## 1) 文件总览（先知道每个文件是干什么的）

建议按编号顺序学；每个文件都能单独运行。

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出全部示例及主题 |
| 02 | [`02_variable_creation.py`](02_variable_creation.py) | 变量创建：赋值、解包、注解、名字绑定对象 |
| 03 | [`03_variable_modification.py`](03_variable_modification.py) | 变量修改：重新绑定 vs 原地修改（可变性/别名） |
| 04 | [`04_variable_naming.py`](04_variable_naming.py) | 变量命名：合法标识符、关键字、命名约定、避免遮蔽 |
| 05 | [`05_variable_types_runtime.py`](05_variable_types_runtime.py) | 变量类型：type/isinstance、动态类型、bool/int 细节 |
| 06 | [`06_type_conversions.py`](06_type_conversions.py) | 类型转换：int/float/str/Decimal/bool（含安全解析） |
| 07 | [`07_type_annotations.py`](07_type_annotations.py) | 类型注解：注解语法、__annotations__、get_type_hints、cast |
| 08 | [`08_scope_and_lifetime.py`](08_scope_and_lifetime.py) | 作用域与生命周期：LEGB、global/nonlocal、del、locals/globals |
| 09 | [`09_assignment_targets.py`](09_assignment_targets.py) | 赋值目标：属性/下标/切片/解包目标、海象运算符 |
| 10 | [`10_common_pitfalls.py`](10_common_pitfalls.py) | 常见坑：is vs ==、链式赋值、可变默认参数、闭包晚绑定 |

---

## 2) 怎么运行（小白版）

下面命令都以“仓库根目录”为当前工作目录（也就是你能看到 `01_Basics/` 的那一层）：

- 先看索引：`python3 01_Basics/06_Variables/01_overview.py`
- 运行某个示例：`python3 01_Basics/06_Variables/02_variable_creation.py`

> 每个脚本末尾都有固定入口：`if __name__ == "__main__": main()`  
> 含义：文件被“直接运行”时执行 `main()`；被 `import` 时不会自动执行。

---

## 3) 你要掌握的知识点（Checklist）

- 变量本质：名字绑定对象（不是“盒子”）
- 变量创建：赋值、解包、注解
- 变量修改：重新绑定 vs 原地修改（可变性/别名/增强赋值）
- 命名规则：`isidentifier`、关键字、大小写敏感
- 命名约定：snake_case / UPPER_CASE / _internal / 避免遮蔽内置名
- 变量类型：`type()`、`isinstance()`、动态类型、bool/int 细节
- 类型转换：int/float/str/Decimal；解析 bool 的常见规则
- 类型注解：主要给工具用；`__annotations__`、`get_type_hints`、`cast`
- 作用域：LEGB、global/nonlocal、locals/globals
- 常见坑：`is` vs `==`、`a=b=[]`、可变默认参数、闭包晚绑定

---

## 4) 逐个详解（怎么跑 + 学到什么）

### 01 - `01_overview.py`

运行：
- `python3 01_Basics/06_Variables/01_overview.py`

它做什么：
- 列出本目录所有示例文件，并标记 `OK/MISSING`

---

### 02 - `02_variable_creation.py`

运行：
- `python3 01_Basics/06_Variables/02_variable_creation.py`

你会学到：
- 变量创建的常见方式：赋值/解包/注解
- `id/type` 视角理解“名字绑定对象”

---

### 03 - `03_variable_modification.py`

运行：
- `python3 01_Basics/06_Variables/03_variable_modification.py`

你会学到：
- 不可变对象的“修改”往往是重新绑定
- 可变对象的修改可能是原地修改（别名会连带变化）
- `+=` 的常见差异：原地 vs 新对象

---

### 04 - `04_variable_naming.py`

运行：
- `python3 01_Basics/06_Variables/04_variable_naming.py`

你会学到：
- 什么名字合法、什么是关键字、大小写敏感
- 工程命名约定：snake_case、常量、内部变量、避免遮蔽内置名

---

### 05 - `05_variable_types_runtime.py`

运行：
- `python3 01_Basics/06_Variables/05_variable_types_runtime.py`

你会学到：
- `type` 与 `isinstance`
- 动态类型：同名变量可绑定不同类型对象
- bool 是 int 子类的细节

---

### 06 - `06_type_conversions.py`

运行：
- `python3 01_Basics/06_Variables/06_type_conversions.py`

你会学到：
- 常见显式转换：int/float/str/Decimal
- `bool("False")` 的坑，以及 parse_bool 的正确思路

---

### 07 - `07_type_annotations.py`

运行：
- `python3 01_Basics/06_Variables/07_type_annotations.py`

你会学到：
- 注解写法、`__annotations__`、`get_type_hints`
- `cast` 不会做运行时转换

---

### 08 - `08_scope_and_lifetime.py`

运行：
- `python3 01_Basics/06_Variables/08_scope_and_lifetime.py`

你会学到：
- LEGB 查找顺序
- `global/nonlocal` 的使用场景
- `del` 删除绑定而不是销毁对象

---

### 09 - `09_assignment_targets.py`

运行：
- `python3 01_Basics/06_Variables/09_assignment_targets.py`

你会学到：
- 赋值不仅能写到名字，也能写到属性/下标/切片
- `:=`（海象运算符）会在表达式里绑定名字

---

### 10 - `10_common_pitfalls.py`

运行：
- `python3 01_Basics/06_Variables/10_common_pitfalls.py`

你会学到：
- 最常见、最值得背下来的变量相关坑与正确写法

