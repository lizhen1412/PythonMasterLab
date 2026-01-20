# Python 3.11+ 循环（Loops）学习笔记（第 11 章）

本章是一组“可运行的小脚本”，系统梳理循环：`while`、`for`、`break`、`continue`、`for/while ... else ...`、嵌套循环（含九九乘法表），以及“指数爆炸”（2^n 级别增长/组合爆炸）为什么会出现、如何识别与避免。最后提供“每题一个文件”的练习题集。

> 备注：你给的 B 站链接在当前环境无法直接访问；本章示例采用最常见的入门讲解套路（求和、过滤、查找、九九乘法表、指数增长/子集爆炸）。如果你贴出视频里的具体题目/输出格式，我可以再把示例对齐到那一套。

---

## 1) 怎么运行

在仓库根目录执行：

- 先看索引：`python3 01_Basics/11_Loops/01_overview.py`
- 运行某个示例：`python3 01_Basics/11_Loops/05_multiplication_table_9x9.py`
- 练习题索引：`python3 01_Basics/11_Loops/Exercises/01_overview.py`

---

## 2) 本章“知识点全景”清单（尽量不漏）

### 2.1 while：写法枚举（你应该都能看懂/写出）

- 基本结构：初始化 -> 条件 -> 循环体 -> 更新（否则容易无限循环）
  - `i = 0; while i < n: ...; i += 1`
- 无限循环：`while True:` + `break`（常用于“读输入/直到满足条件”）
- do-while 模式（至少执行一次）：`while True: ...; if cond: break`
- sentinel（哨兵）循环：一直处理直到遇到特殊值（如 `"END"`/`None`）
- `:=` 在 while 条件里：`while (line := f.readline()) != "": ...`
- 迭代器驱动：`while (x := next(it, sentinel)) is not sentinel: ...`
- 次数限制循环：最多尝试 N 次（常见于“猜数字/登录重试”）
  - 常用结构：`attempt = 0; while attempt < N: ...; attempt += 1`
- `continue`：跳过本轮剩余逻辑进入下一轮（while 里要小心“跳过更新语句”的坑）
- `while ... else ...`：只有当循环“正常结束（条件变 False）”时才执行 else；如果 `break` 退出则不执行

### 2.2 for：写法枚举（核心是“遍历可迭代对象”）

- 遍历序列/字符串：`for x in items: ...`
- range（区间迭代）：
  - `range(stop)` / `range(start, stop)` / `range(start, stop, step)`（stop 不包含）
  - `range` 是“惰性序列对象”，不会像 `list(range(...))` 那样一次性生成所有元素
  - 反向：`range(n, 0, -1)` 或 `reversed(items)`
- 常用搭配：
  - `enumerate(items, start=1)`：拿到索引 + 元素
  - `zip(a, b, strict=True)`：并行遍历（长度不一致直接报错，避免悄悄丢数据）
  - `for k in d` / `for k, v in d.items()`：遍历 dict（注意：`in d` 检查 key）
- `for ... else ...`：常用于“查找/验证”，未 `break` 时执行 else（典型：素数判断）
- 变量作用域：for 的循环变量在循环结束后仍然可见（会保留最后一次赋的值）
- 常见坑：遍历 list 时不要原地增删元素（会导致跳元素）；更稳的写法是“生成新列表”或遍历副本

### 2.3 break / continue：语义与边界

- `break` 只会跳出“当前这一层循环”（嵌套循环里只跳出内层）
- `continue` 只跳过“当前这一次迭代”
- `pass`：占位（语法需要一个块时用）
- 多层退出常用写法：flag/提前 return/把逻辑拆成函数

### 2.4 嵌套循环与复杂度（为什么会“指数爆炸”）

- 两层 for 往往是 O(n^2)（平方级），三层是 O(n^3)
- “指数爆炸”常见于：每一步都会把“状态数”翻倍/分叉（例如子集：2^n）
- 识别方法：看循环/分支里是否在“复制/扩展一个列表”，并且扩展规模与当前规模成比例
- 建议：
  - 先算“数量级”（n=30 的 2^n 已经非常大）
  - 能算数量就别生成全部结果；能剪枝就剪枝；必要时用生成器/迭代器按需产出

---

## 3) 文件总览

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出全部示例与主题 |
| 02 | [`02_while_loops.py`](02_while_loops.py) | while 基础：计数、sentinel、while-else、continue/break |
| 03 | [`03_for_loops.py`](03_for_loops.py) | for 基础：range/enumerate/zip/dict/for-else/iter-next |
| 04 | [`04_break_and_continue.py`](04_break_and_continue.py) | break/continue 细节：loop-else、嵌套循环退出策略 |
| 05 | [`05_multiplication_table_9x9.py`](05_multiplication_table_9x9.py) | 九九乘法表：嵌套循环 + 输出对齐 |
| 06 | [`06_exponential_explosion.py`](06_exponential_explosion.py) | 指数爆炸：2^n 增长与“子集生成”示例 |
| 07 | [`07_chapter_summary.py`](07_chapter_summary.py) | 本章总结：关键规则 + 常见误区清单 |
| 08 | [`08_guess_number_game_simulated.py`](08_guess_number_game_simulated.py) | while 综合：猜数字（模拟输入），演示 break/continue/while-else |
| 09 | [`09_while_patterns_and_edge_cases.py`](09_while_patterns_and_edge_cases.py) | while 补充模式：do-while、:= 条件、迭代器驱动 |
| 10 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | 本章练习索引（每题一个文件） |

---

## 4) 本章练习（每题一个文件）

练习索引：`python3 01_Basics/11_Loops/Exercises/01_overview.py`

- `Exercises/02_sum_1_to_n.py`：for/while 求和（1..n）
- `Exercises/03_for_else_prime_check.py`：for-else（素数判断）
- `Exercises/04_continue_skip_blanks.py`：continue（过滤空白/规范化）
- `Exercises/05_break_nested_search.py`：break（嵌套循环查找坐标：flag vs return）
- `Exercises/06_enumerate_and_zip.py`：enumerate + zip（并行遍历）
- `Exercises/07_range_step_reverse.py`：range（步长/反向）
- `Exercises/08_multiplication_table_9x9.py`：九九乘法表（嵌套循环）
- `Exercises/09_powerset_count_exponential.py`：指数爆炸（2^n 与 powerset）
- `Exercises/10_fizzbuzz.py`：FizzBuzz（for + 条件分支）
- `Exercises/11_guess_number_simulated.py`：猜数字（while + break + continue + while-else）
