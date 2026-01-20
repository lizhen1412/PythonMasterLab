# Python 3.11+ 条件判断（Conditionals）学习笔记（第 10 章）

本章是一组“可运行的小脚本”，系统梳理 Python 的条件分支能力：`if/elif/else`（单分支/双分支/多分支/嵌套选择）、`match/case`（结构化模式匹配）、以及写条件时最容易踩的坑（真值测试、短路、优先级、None 判断等）。最后提供“每题一个文件”的练习题集。

---

## 1) 怎么运行

在仓库根目录执行：

- 先看索引：`python3 01_Basics/10_Conditionals/01_overview.py`
- 运行某个示例：`python3 01_Basics/10_Conditionals/06_truthiness_and_condition_building.py`
- 练习题索引：`python3 01_Basics/10_Conditionals/Exercises/01_overview.py`

---

## 2) 本章“知识点全景”清单（不遗漏常用点）

### 2.1 if/elif/else：所有常见写法（结构枚举）

- 单分支：
  - `if condition: ...`
  - `if condition:\n    ...`（多行块）
  - `if condition:\n    pass`（占位）
- 双分支：
  - `if condition: ...\nelse: ...`
- 多分支：
  - `if cond1: ...\nelif cond2: ...\nelif cond3: ...\nelse: ...`
  - `else` 可选：没有 else 时表示“不满足任何条件就什么也不做/走默认路径”
- 嵌套选择（嵌套 if）：
  - `if A:\n    if B:\n        ...\n    else:\n        ...\nelse:\n    ...`
  - 强烈建议配合“卫语句/提前返回/continue”来减少缩进层级（可读性更好）
- 条件表达式（常被当成“双分支的一行写法”）：
  - `x = a if condition else b`（表达式，能产生值）
  - 注意：只适合简单场景；复杂逻辑请用 if/else 语句块
- 赋值表达式（海象运算符）在条件里：
  - `if (m := pattern.match(text)):`（先绑定再判断）
  - `if (n := len(items)) > 0:`（绑定 + 继续比较）

### 2.2 条件表达式里的“判断能力”（如何写出正确条件）

- 真值测试（truthiness）：`if x:` 实际等价于 `if bool(x):`
  - 常见“假值”（Falsy）：`False`、`None`、`0/0.0/0j`、空字符串 `""`、空容器 `[] {} set() ()`、以及自定义对象的 `__bool__` 为 False 或 `__len__` 为 0
- 常见运算符组合（条件里最常见的操作）：
  - 比较：`== != < <= > >=`、链式比较 `0 < x < 10`
  - 成员：`in / not in`（注意：`key in dict` 检查的是 key）
  - 身份：`is / is not`（最常见：`x is None`）
  - 逻辑：`and / or / not`（短路 + 返回值不一定是 bool）
  - 聚合判断：`all(...)` / `any(...)`（把多个子条件合成一个结果）
  - 推导式里的 if：`[x for x in it if cond]` 是过滤；`[x if cond else y for x in it]` 是产生值
- 关键优先级（写条件时最容易误判的地方）：
  - `not` 低于比较：`not 1 == 2` 等价 `not (1 == 2)`
  - `and` 高于 `or`：`A or B and C` 等价 `A or (B and C)`
  - 不确定就加括号：可读性 > 背优先级表

### 2.3 match/case：结构化模式匹配（写法与能力枚举）

- 基本结构：
  - `match subject:\n    case pattern [if guard]:\n        ...\n    case _:\n        ...`
  - 从上到下匹配，第一个匹配成功的 case 执行；不会“贯穿/掉落”（no fallthrough）
- 常见 pattern 类型（重点都要会看懂/会写）：
  - 字面量模式：`case 0:`、`case "yes":`
  - 单例模式：`case None:`、`case True:`、`case False:`
  - 捕获模式：`case x:`（几乎总是匹配成功，并把 subject 绑定到 x；常见坑：它不是“常量匹配”）
  - 通配符：`case _:`（默认分支）
  - OR 模式：`case 200 | 201 | 204:`
  - AS 模式：`case pattern as whole:`
  - 序列模式：`case [x, y]:`、`case [head, *tail]:`
  - 映射模式：`case {"type": "user", "id": user_id}:`、`case {"type": t, **rest}:`
  - 类模式：`case Point(x, y):`、`case Point(x=0, y=y):`
  - 类型判定（类模式的常见用法）：`case int() as n:` / `case str() as s:`
  - Guard（守卫条件）：`case int() as n if n < 0:`
- 重要规则（避免“看起来对其实错”）：
  - `case NAME:` 是捕获，不是常量；要匹配常量请用字面量或“限定名”（如 `case Color.RED:`）
  - 不能把“永远匹配”的 case（如 `case _:`、`case x:`）放在前面，否则后续 case 永远到不了
  - 序列模式通常匹配 list/tuple 等序列，但**不会**把 `str/bytes/bytearray` 当作序列去匹配
  - 映射模式是“按 key 匹配子集”：只要指定的 key 存在且对应 value 匹配即可（并不要求 dict 完全相等）
  - 类模式的“位置参数匹配”依赖 `__match_args__`；关键字匹配依赖属性名（更直观）

### 2.4 常见坑与最佳实践（写条件更稳）

- `if x == None` 不推荐；用 `x is None` / `x is not None`
- 当 0/""/False 是合法值时，不要用 `if x:` 判断“有没有值”；用 `is None` 或更明确的规则
- 不要用 `x and y or z` 模拟三元表达式；请用 `y if x else z`
- 浮点比较尽量用 `math.isclose`，避免 `0.1 + 0.2 == 0.3` 这类坑
- 组合条件尽量拆成“可读的小块”（中间变量/早返回/括号），不要写超长一行表达式
- 长条件换行：用括号分组换行，避免反斜杠

---

## 3) 文件总览

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出全部示例与主题 |
| 02 | [`02_if_single_branch.py`](02_if_single_branch.py) | 条件判断：单分支 if（含 pass/guard 的常见写法） |
| 03 | [`03_if_else_double_branch.py`](03_if_else_double_branch.py) | 条件分支：双分支 if/else + 条件表达式 |
| 04 | [`04_if_elif_else_multi_branch.py`](04_if_elif_else_multi_branch.py) | 多分支：if/elif/else，顺序与覆盖范围 |
| 05 | [`05_nested_selection_and_guard_clauses.py`](05_nested_selection_and_guard_clauses.py) | 嵌套选择 vs 卫语句：减少缩进、提升可读性 |
| 06 | [`06_truthiness_and_condition_building.py`](06_truthiness_and_condition_building.py) | 真值测试 + 组合条件：and/or/not、in、is、优先级 |
| 07 | [`07_match_basics.py`](07_match_basics.py) | match 基础：字面量/单例/OR/guard/默认分支 |
| 08 | [`08_match_structural_patterns.py`](08_match_structural_patterns.py) | match 进阶：序列/映射/类模式、as、*star |
| 09 | [`09_chapter_summary.py`](09_chapter_summary.py) | 本章总结：关键规则 + 常见误区清单 |
| 10 | [`10_leap_year_check.py`](10_leap_year_check.py) | 闰年判断：if/else 分支规则与布尔表达式写法 |
| 11 | [`11_if_condition_patterns.py`](11_if_condition_patterns.py) | if 条件书写模式：范围/否定/多行/推导式条件 |
| 12 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | 本章练习索引（每题一个文件） |

---

## 4) 本章练习（每题一个文件）

练习索引：`python3 01_Basics/10_Conditionals/Exercises/01_overview.py`

- `Exercises/02_truthiness_blank_and_none.py`：None 合并 + 空白字符串规范化（避免 `or` 的坑）
- `Exercises/03_single_branch_append_if_missing.py`：单分支 if + 成员运算符
- `Exercises/04_double_branch_parity_label.py`：双分支 if/else 与条件表达式
- `Exercises/05_multi_branch_grade.py`：if/elif/else 范围判断（链式比较）
- `Exercises/06_nested_vs_guard_access.py`：嵌套选择 vs 卫语句（提前 return）
- `Exercises/07_match_command_tuple.py`：match 解析命令元组（类型模式 + as）
- `Exercises/08_match_sequence_unpack.py`：match 序列模式（pair / head-tail / *star）
- `Exercises/09_match_mapping_event.py`：match 映射模式（dict 解构 + **rest）
- `Exercises/10_match_guard_ranges.py`：match + guard 做范围判断
- `Exercises/11_precedence_and_short_circuit.py`：短路与优先级：安全写条件（先判类型再调用方法）
