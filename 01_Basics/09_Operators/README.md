# Python 3.11+ 运算符（Operators）学习笔记（第 09 章）

本章是一组“可运行的小脚本”，系统梳理 Python 常用运算符：算术、赋值、比较、逻辑、位运算、成员运算符，以及运算符优先级。最后提供“每题一个文件”的练习题集。

---

## 1) 怎么运行

下面命令都以“仓库根目录”为当前工作目录：

- 先看索引：`python3 01_Basics/09_Operators/01_overview.py`
- 运行某个示例：`python3 01_Basics/09_Operators/05_logical_operators.py`
- 练习题索引：`python3 01_Basics/09_Operators/Exercises/01_overview.py`

---

## 2) 文件总览

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出全部示例与主题 |
| 02 | [`02_arithmetic_operators.py`](02_arithmetic_operators.py) | 算术运算符：`+ - * / // % ** @` 与 `divmod` |
| 03 | [`03_assignment_operators.py`](03_assignment_operators.py) | 赋值运算符：`=`、解包、增强赋值 `+=`、以及 `:=` |
| 04 | [`04_comparison_operators.py`](04_comparison_operators.py) | 比较运算符：`== != < <= > >=`、链式比较、浮点比较 |
| 05 | [`05_logical_operators.py`](05_logical_operators.py) | 逻辑运算符：`and/or/not`、短路、返回值与常见坑 |
| 06 | [`06_bitwise_operators.py`](06_bitwise_operators.py) | 位运算符：`& | ^ ~ << >>` 与位标志（flags） |
| 07 | [`07_membership_operators.py`](07_membership_operators.py) | 成员运算符：`in / not in`（补充：`is / is not`） |
| 08 | [`08_operator_precedence.py`](08_operator_precedence.py) | 运算符优先级：用例子解释“为什么要加括号” |
| 09 | [`09_chapter_summary.py`](09_chapter_summary.py) | 本章总结：关键规则 + 常见误区清单 |
| 10 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | 本章练习索引（每题一个文件） |

---

## 3) 你要掌握的知识点（Checklist）

- `/` 永远返回 float；`//` 是向下取整（负数尤其要小心）
- `%` 与 `//` 满足：`a == (a // b) * b + (a % b)`（b != 0）
- `and/or` 会“短路”，并且返回的是“参与运算的对象”，不一定是 bool
- `x or default` 不是 “None 合并”（0/""/False 会被误当成缺失值）
- `in` 在 `dict` 上检查的是 **key**；`set` 的成员测试通常更快
- `+=` 对可变对象可能是“原地修改”（会影响别名）
- 位运算常用于掩码/标志位；建议用常量命名 `READ = 1 << 0`
- 不确定优先级时加括号；尤其是 `not/and/or` 与比较、以及 `-2**2` 这类表达式
